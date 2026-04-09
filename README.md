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

| Term | Meaning |
|------|---------|
| Addy | address |
| AF | as f**k (intensifier) |
| Amirite | am I right |
| Amped | excited |
| And I oop | expression of surprise or shock |
| ASL | as hell (intensifier) |
| Ate (and left no crumbs) | did something perfectly |
| Aura | coolness, perceived power, mystery |
| Bae | romantic partner |
| Bandwagon | follows trends just to fit in |
| Basic | unoriginal, only into popular things |
| BBG | baby girl / better be going |
| BDE | big confidence without arrogance |
| Bed rot | extended time doing nothing in bed |
| Beige flag | mundane, uninteresting |
| Bet | okay / agreed / affirmative |
| Big back | overindulging |
| Big yikes | very awkward or embarrassing |
| Bih | informal/playful "b***h" |
| Body count | number of sexual partners |
| Boo | romantic partner |
| Boo'd up | in a relationship |
| Boomer / Okay Boomer | dismissive retort toward older-gen opinions |
| Boujee | rich, luxurious, fancy |
| Brat | genuine, self-possessed, non-conforming |
| Bussin' | really good |
| Buttah | smooth, easy, excellent |
| Cake | large, well-shaped bottom |
| Cap | lying or faking |
| No cap | not lying, seriously |
| Cash | awesome or cool |
| Catch feels | develop romantic attachment |
| Catfish | fake online persona |
| Caught in 4k | caught red-handed / obviously |
| Chad | stereotypically confident dominant male |
| Chat | group of people / friends / audience |
| Cheugy | outdated, unfashionable |
| Clapback | sharp witty response to criticism |
| Cooked | done for, exhausted, broken |
| Core | suffix for aesthetic/lifestyle (cottagecore, etc.) |
| Crash out | get mad despite better judgment |
| Cray cray | crazy |
| Cringe | embarrassing, uncomfortable |
| Crossfaded | drunk and high simultaneously |
| Curve | reject romantic advances |
| Dank | excellent, high quality |
| Dap | greeting gesture (fist bump / handshake hybrid) |
| Dayroom | basic and uninteresting |
| Dead / Dying / Ded | response to something funny |
| Delulu | delusional |
| Dip | leave suddenly |
| DL | down low, discreet |
| Dope | exceptional, awesome |
| Dox | publish someone's private info maliciously |
| Drag | mock or humiliate |
| Drip | stylish appearance |
| DTF | down to hook up |
| Dub | win (short for W) |
| Egirl / Eboy | edgy TikTok aesthetic |
| Extra | overly dramatic, attention-seeking |
| Facts | emphasizes agreement / truth |
| Faded | high / under the influence |
| Fan service | content made as a nod to hardcore fans |
| FBOI | manipulative promiscuous man |
| FFA | free for all (gaming) |
| Finna | going to / fixing to |
| Finsta | fake/private Instagram account |
| Fire | amazing, exciting |
| Fit | outfit |
| Flavored air | vaping |
| Flex | brag / show off |
| FML | f**k my life |
| FR | for real |
| FRFR | for real for real (extra emphasis) |
| FTW | for the win |
| Fugly | very ugly |
| Furry | fan of anthropomorphic animals |
| FW | f**k with (really like) |
| FWB | friends with benefits |
| FYP | TikTok For You Page |
| G | term of endearment for a friend |
| Gassing | exaggerating someone's abilities |
| GG | good game |
| Ghost | cut off communication with no explanation |
| Gigachad | ultimate masculine man |
| Girl dinner | random snacks passed off as a meal |
| Girl math | humorous non-conventional calculation |
| Giving me life | something exciting |
| Glow-up | major transformation / improvement |
| GOAT | greatest of all time |
| Granola | outdoorsy, environmentally aware person |
| Guap | large sum of money |
| Gucci | fancy, excellent |
| Gyat | expression of admiration |
| Hammered | extremely intoxicated |
| Heated | angry or frustrated |
| Heem | better version, total package |
| Hella skrilla | lots of money |
| Here for this | excited, showing support |
| High key | obvious, overt |
| Highlighter kid | child in neon clothes |
| Hits different | uniquely impactful / special |
| Hollywood | negative behavior change after success |
| Hop off | stop bothering someone |
| Hot take | controversial opinion |
| Hunty | term of endearment (LGBTQ+) |
| Hype | excited / something is great |
| Ick | feeling of disgust |
| ICYMI | in case you missed it |
| IRL | in real life |
| ISO | in search of |
| IYKYK | if you know, you know |
| Jittleyang | something that grabs attention |
| Juul | vape / e-cigarette |
| KDA | kills/deaths/assists (gaming) |
| Keep it 100 | be honest and genuine |
| KMS | kill myself (joking frustration) |
| Krunk | extremely intoxicated |
| KYS | kill yourself (offensive harassment) |
| L | loss / loser |
| Left on read | read but not replied to |
| Let them cook | trust someone's process |
| Let's get this bread | let's work hard / hustle |
| Lewk | carefully curated outfit/look |
| LFG | let's f**king go |
| Lit | exciting, excellent |
| LMAO | laughing my a** off |
| LMS | like my status |
| LOL | laugh out loud |
| Looksmaxxing | improving appearance through various methods |
| Low key | somewhat / understated |
| Low taper fade | hairstyle / lighthearted meme phrase |
| Mad | really, extremely |
| Meatriding | excessively praising someone |
| Menty b | mental breakdown |
| Mewing | jaw exercise for sharp jawline |
| Mid | average, not great |
| Mogging | one-upping on appearance |
| Munch | performs oral sex |
| Netflix and chill | euphemism for hooking up |
| NGL | not gonna lie |
| NSFW | not safe for work |
| OMG | oh my god |
| OML | oh my lord |
| OMW | on my way |
| ONG | on god (strong agreement) |
| On fleek | perfectly done |
| On point | perfect, exactly right |
| Only in Ohio | label for strange or cursed things |
| Ops | opponents |
| OTP | one true pairing (favorite couple) |
| Periodt | emphasizes finality |
| Plug | supplier of hard-to-find goods |
| PMOYS | put me on your Snapchat |
| Poggers | expression of excitement (gaming) |
| Preppy | colorful, girly, name-brand aesthetic |
| Pressed | annoyed, stressed |
| Pulling | attracting romantic interest |
| Put on blast | publicly embarrass someone |
| Pwn | dominate / have power over |
| Rad | awesome, very good |
| Ran through | perceived as overly sexually active |
| Ratchet | out of control, tacky |
| Read | publicly point out someone's flaws |
| Real | serious |
| Receipts | evidence, proof |
| Rent free | living in someone's head / obsessing |
| Rizz | ability to charm / attract people |
| Rizzler | someone skilled at flirting |
| ROTFLMAO | rolling on the floor laughing |
| RN | right now |
| RPG | role-playing game |
| Salty | upset, resentful, bitter |
| Savage | fierce, bold |
| Say less | understood, no need to explain |
| Sending me | response to something hilarious |
| Shade | subtle contempt / throw shade |
| Ship | support a romantic pairing |
| Shook | shocked, surprised |
| Shorty | attractive girl |
| Sick | cool, awesome |
| Sigma | cool, successful, introverted lone wolf |
| Simp | desperate for affection |
| Skibidi Toilet | dystopian YouTube animated series |
| Slap | amazing, excellent |
| Slay | doing something extremely well |
| Slim thick / thicc | hourglass body type |
| Small dick energy | insecure but overconfident |
| Smash | hook up / casual sex |
| SMH | shaking my head |
| Smol | small, cute, endearing |
| Smut | sexually explicit written content |
| Snack | attractive person |
| Snatched | perfect, attractive |
| Sneaky link | secret hookup |
| SO | shout out / significant other |
| Sparks | moment a joint is lit |
| Stan | obsessed fan |
| Stoked | very excited |
| Sus | suspicious |
| Swerve | avoid someone |
| Swole | muscular |
| Swoop | give or get a ride |
| Take a seat | dismissive, calm down |
| Tea | gossip / spill the tea |
| TF | the f**k (surprise/disbelief) |
| TFW | that feeling when |
| Thirsty | desperate for attention |
| Thirst trap | provocative post for attention |
| Thot | promiscuous person (derogatory) |
| Totes | totally |
| Touch grass | go outside / spend time in real world |
| Trap phone | prepaid phone for sketchy activity |
| Twin | close friend with shared interests |
| Twizzy | variation of twin |
| Uhh | confusion, awkward response |
| Unc | older person / millennial |
| Understood the assignment | went above and beyond |
| Upper decky | nicotine pouch on upper gums |
| V | very |
| Vanilla | ordinary, boring |
| Vibe | feeling, ambience |
| VSCO girl | trendy girl with edited photos |
| W | win, winner |
| Wallflower | introvert |
| Weird flex but ok | odd thing to brag about |
| Whip | car |
| Whole meal | someone who looks really good |
| Wig snatched | extreme excitement/astonishment |
| Woke | socially aware |
| WYA | where you at |
| WYD | what you doing |
| Xan | Xanax |
| YAAS | enthusiastic yes |
| Yeet | throw forcefully |
| Zaddy | handsome fashionable older man |

## License

MIT
