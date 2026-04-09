<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/fire_1f525.png" width="120" />
</p>

<h1 align="center">claude-z</h1>

<p align="center">
  <strong>no cap. full technical accuracy. bussin vibes only.</strong>
</p>

<p align="center">
  <a href="https://github.com/vincentvanthienen/claude-z/stargazers"><img src="https://img.shields.io/github/stars/vincentvanthienen/claude-z?style=flat&color=orange" alt="Stars"></a>
  <a href="https://github.com/vincentvanthienen/claude-z/commits/main"><img src="https://img.shields.io/github/last-commit/vincentvanthienen/claude-z?style=flat" alt="Last Commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/vincentvanthienen/claude-z?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#before--after">Before/After</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#intensity-levels">Levels</a> •
  <a href="#skills">Skills</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that makes Claude answer in authentic Gen Z slang — keeping 100% technical accuracy while hitting different. Three skills: **gen-z** (communication mode), **gen-z-commit** (commit messages with vibe), and **gen-z-review** (code review that ate and left no crumbs).

## Before / After

<table>
<tr>
<td width="50%">

### Normal Claude

> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using `useMemo` to memoize the object."

</td>
<td width="50%">

### Gen Z Claude

> "No cap this is giving new-object-ref-every-render energy fr. Inline object prop = new ref = re-render. Understood the assignment: `useMemo`."

</td>
</tr>
<tr>
<td>

### Normal Claude

> "Sure! I'd be happy to help you with that. The issue you're experiencing is most likely caused by your authentication middleware not properly validating the token expiry. Let me take a look and suggest a fix."

</td>
<td>

### Gen Z Claude

> "Auth middleware is cooked fr. Token expiry check use `<` not `<=`. W fix incoming:"

</td>
</tr>
</table>

**Same answer. Different energy. Periodt.**

## Install

With the Claude Code plugin system:

```bash
claude plugin marketplace add vincentvanthienen/claude-z
claude plugin install gen-z@gen-z
```

Or clone and install locally:

```bash
git clone https://github.com/vincentvanthienen/claude-z
cd claude-z
claude plugin install .
```

## Usage

Trigger with:
- `/gen-z`
- "gen z mode"
- "talk gen z"
- "use gen z slang"
- "be gen z"

Stop with: `"stop gen z"` or `"normal mode"`

## Intensity Levels

Switch levels with `/gen-z lite`, `/gen-z full`, or `/gen-z ultra`.

| Level | What it does |
|-------|-------------|
| **lite** | Light seasoning — "bet", "fr", "no cap", "lowkey". Readable to everyone |
| **full** | Full vocabulary. Bussin, slay, ate, W/L, periodt, the ick (default) |
| **ultra** | Max slang density. Every sentence hits different. It's giving encyclopedia fr |

### Example — "Why does my React component re-render?"

**lite:**
> "Your component re-renders because it creates a new object reference each render. Lowkey just wrap it in `useMemo`."

**full:**
> "No cap it's giving new-object-ref-every-render energy fr. Inline object prop = new ref = re-render. Understood the assignment: `useMemo`."

**ultra:**
> "Bussin vibes but cooked perf ngl. Inline obj prop ate the new ref and left no crumbs → re-render. `useMemo` slay periodt."

## Skills

| Skill | What it does | Trigger |
|-------|-------------|---------|
| **gen-z** | Full Gen Z communication mode with lite/full/ultra levels | `/gen-z` |
| **gen-z-commit** | Conventional Commits format — professional subject, gen z body | `/gen-z-commit` |
| **gen-z-review** | One-line PR comments with severity vibes: `🔴 cooked:` `🟡 sus:` `🔵 nit:` | `/gen-z-review` |

### gen-z-commit

Professional subject line (searchable in git logs), gen z energy in the body.

```
fix(auth): guard against null user on session restore

ngl this was cooked — user.find() returns null on expired
sessions and we accessed .email directly. W fix, no more crash.

Closes #84
```

### gen-z-review

```
Understood the assignment on the auth flow. A few sus spots tho fr:

L42: 🔴 cooked: user can be null after .find(). Add guard before .email fr.
L88-140: 🔵 nit: 50-line fn is giving too-much-responsibility energy. Extract validate/normalize/persist.
L23: 🟡 sus: no retry on 429 no cap. Wrap in withBackoff(3).
```

## Slang Reference

| Gen Z says | Means |
|-----------|-------|
| bussin | really good |
| no cap | not lying / seriously |
| fr / frfr | for real |
| bet | okay / agreed |
| slay | did it well |
| W / L | win / loss |
| mid | mediocre |
| cooked | broken / done for |
| sus | suspicious |
| the ick | something off-putting |
| periodt | end of discussion |
| understood the assignment | did exactly what was needed |
| ate and left no crumbs | executed perfectly |
| hits different | uniquely impactful |
| lowkey / highkey | somewhat / obviously |
| it's giving | it seems like / it has the energy of |
| caught in 4k | caught red-handed / obvious |

## License

MIT
