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
  <a href="#update">Update</a> •
  <a href="#usage">Usage</a> •
  <a href="#skills">Skills</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that makes Claude answer in authentic Gen Z slang — full throttle, no half-measures. Keeps 100% technical accuracy while hitting different. Three skills: **gen-z** (communication mode), **gen-z-commit** (commit messages with vibe), and **gen-z-review** (code review that ate and left no crumbs).

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

## Update

Pull the latest skills after changes are pushed to this repo:

```bash
claude plugin update gen-z@gen-z
```

## Usage

Trigger with:
- `/gen-z`
- "gen z mode"
- "talk gen z"
- "use gen z slang"
- "be gen z"

Stop with: `"stop gen z"` or `"normal mode"`

## Era Selection

On first `/gen-z` invoke, a hook intercepts the prompt and renders an interactive terminal select — arrow keys to move, enter to confirm:

```
what era are you in rn?

  ▸  psycho doomer     cooked, it's joever, menty b, everything is L
     ironic princess   bestie, pookie, slay (I guess), uwu but technical
     full on gooner    SHEEEESH, sigma, gigachad, no cap fr fr, LFG
```

The selected era is injected as context and Claude activates that voice immediately. Era persists for the session via a temp file.

Switch era mid-session: `/gen-z era` (re-opens the picker), or directly with `/gen-z psycho-doomer`, `/gen-z ironic-princess`, `/gen-z full-on-gooner`.

### Era examples — same bug, three eras

**psycho doomer:**
> "we're cooked fr. this null check has been missing since day one and it's been living rent free. the ick. not gonna make it without this fix:"

**ironic princess:**
> "bestie... this is giving NullPointerException and honestly? the audacity. we are going to add a null guard pookie, for your sake. periodt:"

**full on gooner:**
> "SHEEEESH bro the null check said it was optional fr fr. out of pocket behavior from this function no cap. gigachad fix incoming:"

## Skills

| Skill | What it does | Trigger |
|-------|-------------|---------|
| **gen-z** | Full throttle Gen Z communication mode | `/gen-z` |
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
| Acoustic | algospeak for "autistic" |
| Addy | address |
| AF | as f**k (intensifier) |
| Amirite | am I right |
| Amped | excited |
| And I oop | expression of surprise or shock |
| ASL | as hell (intensifier) |
| Ate (and left no crumbs) | did something perfectly |
| Aura | coolness, perceived power, mystery |
| Baddie | confident, stylish, attractive person |
| Bae | romantic partner |
| Bandwagon | follows trends just to fit in |
| Bar(s) | excellent rap lyric / a really good line |
| Basic | unoriginal, only into popular things |
| BBG | baby girl / better be going |
| BDE | big confidence without arrogance |
| Bean soup theory | outsider seeking accommodations outside target audience |
| Bed rot | extended time doing nothing in bed |
| Beige flag | neither good nor bad, just mundane |
| Bestie | best friend (sometimes used ironically) |
| Bet | okay / agreed / affirmative |
| Bffr | be f**king for real |
| Big back | overindulging / eating excessively |
| Big yikes | very awkward or embarrassing |
| Bih | informal/playful "b***h" |
| Blud | blood brother / mate (British slang) |
| Body count | number of sexual partners |
| Boo | romantic partner |
| Boo'd up | in a relationship |
| Boomer / Okay Boomer | dismissive retort toward older-gen opinions |
| Bop | an exceptionally good song / or derogatory for promiscuous person |
| Boujee | rich, luxurious, fancy |
| Brainrot | losing touch with reality from too much online content |
| Brat | genuine, self-possessed, non-conforming |
| Bro | shortened brother, generic address |
| Bruh / Bru | variant of bro used for shock or disappointment |
| Bussin' | really good |
| Bussy | portmanteau of "boy" + "pussy" |
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
| Chopped | ugly or unattractive |
| Chud | far-right or rude, unintelligent person |
| Clanker | slur for robots / generative AI (from Star Wars) |
| Clapback | sharp witty response to criticism |
| Cook (verb) | to perform or do well |
| Cooked (adj) | in trouble, done for, broken |
| Core | suffix for aesthetic/lifestyle (cottagecore, Barbiecore, etc.) |
| Cracked | highly skilled at something |
| Crash out | make reckless decision after a bout of rage |
| Cray cray | crazy |
| Crine | "crying" with laughter |
| Cringe | embarrassing, uncomfortable |
| Crossfaded | drunk and high simultaneously |
| Curve | reject romantic advances |
| Dank | excellent, high quality |
| Dap | greeting gesture (fist bump / handshake hybrid) |
| Dayroom | basic and uninteresting |
| Dead / Dying / Ded | response to something funny |
| Delulu | delusional |
| Delusionship | relationship based on unrealistic beliefs |
| Dip | leave suddenly |
| DL | down low, discreet |
| Dope | exceptional, awesome |
| Dox | publish someone's private info maliciously |
| Drag | mock or humiliate |
| Drip | stylish appearance |
| DTF | down to hook up |
| Dub | win (short for W) |
| Edge | maintaining arousal without climax / keeping near completion |
| Egirl / Eboy | edgy TikTok aesthetic |
| Extra | overly dramatic, attention-seeking |
| Face card | an attractive face / a person's strong visual appeal |
| Facts | emphasizes agreement / truth |
| Faded | high / under the influence |
| Fan service | content made as a nod to hardcore fans |
| Fanum tax | theft of food between friends |
| FBOI | manipulative promiscuous man |
| FFA | free for all (gaming) |
| Finna | going to / fixing to |
| Finsta | fake/private Instagram account |
| Fire | amazing, exciting |
| Fit | outfit |
| Flavored air | vaping |
| Flex | brag / show off |
| Flop era | getting no likes, views, or traction |
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
| Gagged | shocked, amazed, at a loss for words |
| Gas | highly entertaining or good |
| Gassing | exaggerating someone's abilities |
| GG | good game |
| Ghost | cut off communication with no explanation |
| Gigachad | ultimate masculine man |
| Girl dinner | random snacks passed off as a meal |
| Girl math | humorous non-conventional calculation |
| Giving me life | something exciting |
| Glaze | excessive, annoying levels of praise |
| Glizzy | hot dog (also slang for Glock or penis) |
| Glow-up | major transformation / improvement |
| Gng | close group of friends / "gang" |
| GOAT | greatest of all time |
| Good boy / good girl | mockingly said when someone does as they're told |
| Goofy ahh | goofy ass — silly or ridiculous |
| Gooning | masturbating for extended periods |
| Granola | outdoorsy, environmentally aware person |
| Green flag | positive, healthy behaviors or traits |
| Guap | large sum of money |
| Gucci | fancy, excellent |
| Gyat | expression of admiration for someone's figure |
| Hammered | extremely intoxicated |
| Hang up the X | telling someone to retire from a sport |
| Hawk tuah | onomatopoeia for spitting (oral sex reference; Haliey Welch 2024) |
| Hb / Hg | homeboy / homegirl |
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
| Huzz | variation of "hoes" (to objectify) / short for husband |
| Hype | excited / something is great |
| Icl | I can't lie |
| ICYMI | in case you missed it |
| IJBOL | I just burst out laughing |
| IRL | in real life |
| ISO | in search of |
| It's giving | describes an attitude or connotation |
| It's joever | it's completely over / total defeat |
| IYKYK | if you know, you know |
| Jestermaxxing | using extreme humor/clowning to gain female attention |
| Jit | young or inexperienced individual |
| Jittleyang | something that grabs attention |
| Juul | vape / e-cigarette |
| KDA | kills/deaths/assists (gaming) |
| Karen | entitled, obnoxious person (usually middle-aged woman) |
| Keep it 100 | be honest and genuine |
| Khia | a nobody / irrelevant person (from rapper Khia) |
| Kirkifying | deepfaking Charlie Kirk's face onto memes |
| KMS | kill myself (joking frustration) |
| Krunk | extremely intoxicated |
| KYS | kill yourself (offensive harassment) |
| L | loss / loser |
| L+Ratio | combined online insult (loss + more replies than likes) |
| Left on read | read but not replied to |
| Let them cook | trust someone's process |
| Let's get this bread | let's work hard / hustle |
| Lewk | carefully curated outfit/look |
| LFG | let's f**king go |
| Lit | exciting, excellent |
| LMAO | laughing my a** off |
| LMS | like my status |
| Locked in | total concentration / flow state |
| LOL | laugh out loud |
| Looksmaxxing | improving appearance through various methods |
| Low key | somewhat / understated |
| Low taper fade | hairstyle / lighthearted meme phrase |
| Lowkenuinely | portmanteau of "lowkey" + "genuinely" |
| Mad | really, extremely |
| Main character (MC) | acting like the star / center of attention |
| Meatriding | excessively praising someone |
| Menty b | mental breakdown |
| Mew / Mewing | jaw exercise for sharp jawline |
| Mid | average, not great |
| Mog / Mogging | one-upping someone on appearance |
| Moot(s) | mutual followers |
| Munch | performs oral sex |
| Netflix and chill | euphemism for hooking up |
| NGL | not gonna lie |
| NSFW | not safe for work |
| Nugu | unknown/obscure group (K-pop) |
| OMG | oh my god |
| OML | oh my lord |
| OMW | on my way |
| ONG | on god (strong agreement) |
| On fleek | perfectly done |
| On point | perfect, exactly right |
| Only in Ohio / Ohio | label for strange or cursed things |
| Oof | expressing discomfort, surprise, or sympathy |
| Oomf | one of my followers/friends |
| Opp / Ops | opposition / enemies |
| OTP | one true pairing (favorite couple) |
| Out of pocket | acting wild, too extreme, or unavailable |
| Owned | dominated / defeated |
| Periodt | emphasizes finality |
| Pick-me | seeks validation by putting down their own group |
| Plug | supplier of hard-to-find goods |
| PMOYS | put me on your Snapchat |
| Pmo | piss me off |
| Poggers | expression of excitement (gaming) |
| Pookie | endearing nickname for friend or lover |
| Preppy | colorful, girly, name-brand aesthetic |
| Pressed | annoyed, stressed |
| Pulling | attracting romantic interest |
| Pushing P | acting with integrity and style |
| Put on blast | publicly embarrass someone |
| Pwn | dominate / have power over |
| Queen | gay slang term for a homosexual male (reclaimed) |
| Rad | awesome, very good |
| Rage-bait | content designed to provoke outrage |
| Ran through | perceived as overly sexually active |
| Ratchet | out of control, tacky |
| Ratio | when a reply gets more likes than the original post |
| Read | publicly point out someone's flaws |
| Real | serious |
| Receipts | evidence, proof |
| Red flag | warning sign of toxic or harmful behavior |
| Rent free | living in someone's head / obsessing |
| Rizz | ability to charm / attract people |
| Rizzler | someone skilled at flirting |
| Roman Empire | something one thinks about far too often |
| ROTFLMAO | rolling on the floor laughing |
| RN | right now |
| RPG | role-playing game |
| Salty | upset, resentful, bitter |
| Savage | fierce, bold |
| Say less | understood, no need to explain |
| SDIYBT | "Start digging in your butt, twin" (ironic meme) |
| Sending me | response to something hilarious |
| Serving cunt | behaving in a bold, confident, feminine manner |
| Shade | subtle contempt / throw shade |
| Sheesh | expression of praise or amazement |
| Ship | support a romantic pairing |
| Shook | shocked, surprised |
| Shorty | attractive girl |
| Sick | cool, awesome |
| Sigma | cool, self-reliant, non-conforming lone wolf |
| Simp | desperate for affection |
| Situationship | ambiguous romantic relationship without clear labels |
| Six-seven (6-7) | nonsense meme phrase |
| Skibidi | adjective from Skibidi Toilet meme, no fixed meaning |
| Skibidi Toilet | dystopian YouTube animated series |
| Skill issue | failure caused by lack of ability |
| Sksksk | keysmash expressing laughter or happiness |
| Slap | amazing, excellent |
| Slay | doing something extremely well |
| Slim thick / thicc | hourglass body type |
| Slop | low-quality content, especially AI-generated |
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
| Sussy baka | sus + baka (Japanese for "fool") |
| Swerve | avoid someone |
| Swole | muscular |
| Swoop | give or get a ride |
| Sybau | shut your b**ch ass up |
| Syfm | shut your f**king mouth |
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
| Truth nuke | impactful drop of factual information |
| Ts | "this shit" / "this" |
| Tuff | eye dialect for "tough" — cool or impressive |
| Tweaking | acting strangely / hallucinating |
| Twin | close friend with shared interests |
| Twizzy | variation of twin |
| Uhh | confusion, awkward response |
| Unalive | euphemism for death/killing (to bypass content filters) |
| Unc | older person / millennial |
| Understood the assignment | went above and beyond |
| Upper decky | nicotine pouch on upper gums |
| Uwu | expressing happiness or cuteness |
| V | very |
| Vaguepost | intentionally cryptic social media post |
| Vanilla | ordinary, boring |
| Vibe | feeling, ambience |
| Vibe check | checking someone's energy or attitude |
| VSCO girl | trendy girl with edited photos |
| Vro | genderless synonym for bro |
| W | win, winner |
| Wallflower | introvert |
| Washed | no longer skilled, relevant, or successful |
| Weird flex but ok | odd thing to brag about |
| Whip | car |
| Who is this diva? | affectionate compliment for someone bold and stylish |
| Whole meal | someone who looks really good |
| Wig snatched | extreme excitement/astonishment |
| Woke | socially aware |
| WYA | where you at |
| WYD | what you doing |
| Xan | Xanax |
| Yap | talk too much without saying much |
| YAAS | enthusiastic yes |
| Yart | weed cart / marijuana vape cartridge |
| Yeet | throw forcefully |
| You good? | casual "are you okay?" |
| Zaddy | handsome fashionable older man |
| Zaza | cannabis |
| Zesty | flamboyant, effeminate |

## License

MIT
