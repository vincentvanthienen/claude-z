#!/usr/bin/env python3
"""
gen-z era selector hook.

Runs on UserPromptSubmit when /gen-z is invoked.
- No era set yet → shows interactive arrow-key terminal select
- Era already set → re-injects era as context so Claude knows
- /gen-z era → force re-selection
- /gen-z psycho-doomer|ironic-princess|full-on-gooner → set directly
"""
import json
import os
import sys
import termios
import tty

ERAS = [
    {
        "id": "psycho-doomer",
        "label": "psycho doomer",
        "desc": "cooked, it's joever, menty b, everything is L",
    },
    {
        "id": "ironic-princess",
        "label": "ironic princess",
        "desc": "bestie, pookie, slay (I guess), uwu but technical",
    },
    {
        "id": "full-on-gooner",
        "label": "full on gooner",
        "desc": "SHEEEESH, sigma, gigachad, no cap fr fr, LFG",
    },
]

ERA_MAP = {e["id"]: e for e in ERAS}
ERA_ALIASES = {}
for e in ERAS:
    ERA_ALIASES[e["id"]] = e["id"]
    ERA_ALIASES[e["label"]] = e["id"]
    ERA_ALIASES[e["id"].replace("-", " ")] = e["id"]


def era_file(session_id):
    return f"/tmp/gen-z-era-{session_id}"


def load_era(session_id):
    try:
        with open(era_file(session_id)) as f:
            era_id = f.read().strip()
            return era_id if era_id in ERA_MAP else None
    except FileNotFoundError:
        return None


def save_era(session_id, era_id):
    with open(era_file(session_id), "w") as f:
        f.write(era_id)


def interactive_select():
    """Show arrow-key select via /dev/tty. Returns selected era id."""
    fd = os.open("/dev/tty", os.O_RDWR | os.O_NOCTTY)

    def w(s):
        os.write(fd, s.encode("utf-8") if isinstance(s, str) else s)

    selected = 0
    n = len(ERAS)

    def render(first=False):
        if not first:
            w(f"\r\033[{n}A\033[J")
        for i, era in enumerate(ERAS):
            if i == selected:
                w(f'  \033[1;96m▸  {era["label"]:<18}\033[0m  \033[90m{era["desc"]}\033[0m\n')
            else:
                w(f'     \033[2m{era["label"]:<18}\033[0m  \033[90m{era["desc"]}\033[0m\n')

    w("\033[?25l")  # hide cursor
    w("\nwhat era are you in rn?\n\n")
    render(first=True)

    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = os.read(fd, 3)
            if ch in (b"\x1b[A", b"\x1bOA"):  # up arrow
                selected = (selected - 1) % n
                render()
            elif ch in (b"\x1b[B", b"\x1bOB"):  # down arrow
                selected = (selected + 1) % n
                render()
            elif ch in (b"\r", b"\n"):  # enter
                break
            elif ch[:1] == b"\x03":  # ctrl+c
                w("\033[?25h\n")
                os.close(fd)
                sys.exit(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

    w("\033[?25h\n")  # show cursor
    os.close(fd)
    return ERAS[selected]["id"]


def system_msg(text):
    print(json.dumps({"systemMessage": text}))


def era_context(era_id):
    era = ERA_MAP[era_id]
    return (
        f'[gen-z] era is "{era_id}". '
        f'Use the {era["label"]} communication style for all responses this session. '
        f'Confirm activation in that era\'s voice, then answer any follow-up.'
    )


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    prompt = data.get("user_prompt", "").strip()
    session_id = data.get("session_id", "default")

    # Only act on /gen-z prompts
    if not prompt.lower().startswith("/gen-z"):
        sys.exit(0)

    rest = prompt[len("/gen-z"):].strip().lower()

    # /gen-z <era-id or label> — set directly without prompt
    if rest in ERA_ALIASES:
        era_id = ERA_ALIASES[rest]
        save_era(session_id, era_id)
        system_msg(era_context(era_id))
        sys.exit(0)

    # /gen-z era — force re-selection
    if rest == "era":
        era_id = interactive_select()
        save_era(session_id, era_id)
        system_msg(era_context(era_id))
        sys.exit(0)

    # /gen-z, /gen-z lite, /gen-z full, /gen-z ultra
    current = load_era(session_id)
    if current is None:
        # No era set — show interactive picker first
        era_id = interactive_select()
        save_era(session_id, era_id)
        system_msg(era_context(era_id))
    else:
        # Era already set — re-inject as context so Claude remembers
        system_msg(era_context(current))

    sys.exit(0)


if __name__ == "__main__":
    main()
