# Output templates

Two files: the personas document (main file) and the evidence ledger (extra material under the same stem). Default paths: `research/personas.md` and `research/personas/evidence-ledger.md`. Write them in the language of the user's project; keep the tags in English so the script works. Tags, header block, Sources format and index row follow `references/kit-protocol.md`.

Tag use in this skill:
- `[user: <file>]` for what the user said or wrote in their files (brief, interview notes, desk-research notes). The brief's stated facts are `[user: research/brief.md]`; the brief's own unverified beliefs ("we think most users are on Android") are `[assumption]`.
- `[source: Sn]` / `[snippet: Sn]` for pages and excerpts you collected yourself, or carried over from a sibling file (re-cite its source under your own `Sn`; keep its weight).
- Qualifiers used here: `weak` (second-hand or unverifiable: review excerpt without context, forum comment, undated blog), `vendor` (the product's own claim, price or marketing). No qualifier on a `[user]` or `[source]` tag means first-hand from the target user or their data (interview, ticket, analytics, survey they answered).
- `[assumption]` + `(G#)`: inference or belief with no checked data. Nothing at all, not even a reasoned inference: write plain `unknown (G#)`.
- `[synthetic]`: anything that came from a simulated interview. A hypothesis, never evidence.
- `[unverified]`: from model memory only. Avoid in persona items; prefer a gap.

## 1. Personas document

```markdown
# Proto-personas: <product>

> Skill: proto-personas · Date: <YYYY-MM-DD> · Product: <name, one line>
> Inputs: <files and sources this file was built from, e.g. "research/brief.md, research/competitive-analysis.md, research/interview-notes.md, 6 web sources">
> Tags: [user] · [source: Sn] · [snippet: Sn] · [unverified] · [assumption] · [estimate] · [synthetic] (legend at the bottom)

Hypotheses about users built from secondary data (list the inputs), not interviews. Their job is to drive design decisions.
Evidence ledger: research/personas/evidence-ledger.md (L# facts, G# gaps).
`-> I#` at the end of an item = the insight of this persona that the item feeds.
Phrases on persona cards are constructed from source wording and are not user quotes, unless marked "verbatim" with the ledger id.

## Persona set and rationale

| # | Persona (by role) | Slug | Segment | Scenarios covered | Priority |
|---|---|---|---|---|---|
| P1 | Shift manager | shift-manager | ... | 1, 3 | Primary |
| P2 | Line cook | line-cook | ... | 2 | Secondary |
| S | Stress: first-time user on a phone mid-shift | stress-phone-user | cross-cutting | 2 | Card only |

The slug is the persona's file-safe name; other tools use it (for example `research/interview-<slug>.md`).

**Why this many.** <one paragraph: what the sources show about segments; buyer vs user; what was not made a persona and why>

**Mismatches shown to the user.** <roles in the brief vs segments in the evidence; contradictions between sources; or "none">

## Primary persona

**P1. <Role>** (slug `shift-manager`). Full card below under "P1".

**Why P1.** <evidence-based: share of key scenarios, strength of evidence (L#), frequency of use, pain severity, goal fit; why the others are secondary; what would change the choice>

---

## P1. <Role> (PRIMARY)

Slug: `shift-manager`

#### 1. Role and context
- **1a.** <who they are, what they do> [user: research/interview-notes.md] (L3) -> I1
- **1b.** <where the product sits in their day; other tools> [user: research/brief.md] -> I2

#### 2. Job to be done
- **2a.** Hires the product to <task> [user: research/brief.md] -> I1
- **2b.** Situation: <when it arises> [user: research/interview-notes.md] (L1) -> I1
- **2c.** Success looks like: <outcome> [assumption] (G5) -> I2
- **2d.** Job story: *When <situation>, I want <motivation>, so that <outcome>.* [user: research/interview-notes.md] (L1) -> I1

#### 3. Behaviour
- **3a.** Frequency, device, place, rush: <...> [assumption] (G1) -> I2
- **3b.** Typical scenario: <step 1> -> <step 2> -> <step 3> [user: research/interview-notes.md] (L2) -> I1
- **3c.** Solves it today with: <named direct competitors and substitutes, details in the table below> [source: S2, vendor] (L2) -> I1

| Tool | What it covers (as stated) | What it does not cover for this person | Price as stated | Feeds, source |
|---|---|---|---|---|
| <competitor> | <...> | <...> | <...> | I1 · [source: S2, vendor] (L2) |

#### 4. Frustrations and constraints
- **4a.** <pain with a named current solution> [source: S3, weak] (L5) -> I1
- **4b.** Constraints: time / budget / skills: <...> [assumption] (G2) -> I3
- **4c.** Fear when switching: <...> [user: research/interview-notes.md] (L4) -> I2

#### 5. Choice triggers
- **5a.** Finds the product through <channel> [assumption] (G3) -> I2
- **5b.** Tries it when <trigger> [assumption] (G6) -> I1
- **5c.** Stays if <condition> unknown (G4) -> I3
- **5d.** Dealbreaker: <...> [source: S3, weak] (L6) -> I1

#### 6. Insights
- **I1.** Because <fact: 3b, 4a> -> we need <concrete design decision>.
- **I2.** Because <...> -> we need <...>.
- **I3.** Because <...> -> we need <...>.

**Biggest assumption to test:** <one sentence, with G#>

#### 7. Persona card
- Digital literacy <1-5> [assumption] (G7); experience with analogues: <which, how long> [user: research/interview-notes.md]
- Device and context by default: <...> [assumption] (G1)
- Goals in their words: <1-3> [user: research/interview-notes.md]
- Fears and stop factors: <...> [user: research/interview-notes.md]
- How they talk: "<verbatim quote>" (L1, verbatim) [user: research/interview-notes.md]; "<constructed phrase>" (constructed from L4, not a quote) [assumption] (G8)

(If the persona has modes, add 7a, 7b, one card per mode.)

---

## P2. <Role> (SECONDARY)

Slug: `line-cook`

<same structure; may be shorter, but sections 3 to 5 and the card keep their tags>

## S. Stress persona (card only)

Slug: `stress-phone-user`

#### 7. Persona card
- ...

---

## Summary

| | P1 | P2 | S |
|---|---|---|---|
| Job to be done | ... | ... | ... |
| Priority | primary | secondary | card only |
| Key design takeaway | ... | ... | ... |
| Biggest assumption to test | ... | ... | ... |

## Validation plan (what to check with real people)

| # | Assumption (G#/L#) | Insight that breaks if false | Method and sample | Ask (plain words, about past behaviour) | Falsified if |
|---|---|---|---|---|---|
| 1 | <...> | P1-I1 | 5 interviews with shift managers | "Tell me about the last time a shift needed covering." | <e.g. 3 of 5 never use a group chat> |

Order by risk: the assumption whose failure invalidates the primary persona goes first.

## Assumption statistics

<paste the script output: per area, items, pure assumptions %, any-assumption % including [unverified], unknown count>
Reading: <which areas are thin, what that means for next steps>

## Self-check (0-2)

| Criterion | Score | Note |
|---|---|---|

## Changes

- <YYYY-MM-DD>: created. (On a rerun, add a dated line saying what changed; do not make a copy of the file.)

## Sources

S1 · <title> · <URL> · accessed <YYYY-MM-DD> · <official / review / forum / vendor / news / research>

(Same `Sn` as in the ledger. List only sources actually cited. Files the user gave you are cited as `[user: <file>]`, not here. Omit this section if no `[source]` or `[snippet]` tag is used.)

## Legend

| Tag | Meaning |
|---|---|
| `[user]` | said by the user in chat or written in their own files; name the file when there is one: `[user: docs/brief.md]` |
| `[source: Sn]` | from a page or document that was actually opened; `Sn` is its row in the Sources list |
| `[snippet: Sn]` | seen only in a search-result excerpt, page not opened |
| `[unverified]` | known from model memory, not checked against a source |
| `[assumption]` | reasoning or inference, not checked; points to a gap `G<n>` |
| `[estimate]` | a size, effort or quantity guess, with what it assumes |
| `[synthetic]` | said by a simulated persona; a hypothesis, never evidence |

Qualifiers: `weak` (second-hand or unverifiable), `vendor` (the product's own claim). `unknown (G#)`: no data and no inference; see the gap note.
```

## 2. Evidence ledger

```markdown
# Evidence ledger: <product>

> Skill: proto-personas · Date: <YYYY-MM-DD> · Product: <name, one line>
> Inputs: <list of files and URLs read, with dates>
> Tags: [user] · [source: Sn] · [snippet: Sn] · [unverified] · [assumption] · [estimate] · [synthetic] (legend at the bottom)

## Evidence

| ID | Claim | Source (file section, or Sn and location) | Source wording (verbatim) | Tag |
|---|---|---|---|---|
| L1 | Staff swap shifts through a WhatsApp group | research/interview-notes.md, Interview 1 | "we just post it in the group and hope" | [user: research/interview-notes.md] |
| L2 | Competitor X claims fewer no-shows | S2, pricing page | "reduces no-shows by 30%" | [source: S2, vendor] |
| L3 | Most staff are on Android | research/brief.md, "What we believe" | "Most staff are on Android phones." | [assumption] (G1) |

Weight is in the tag: no qualifier = first-hand from the target user or their data; `weak` = second-hand or unverifiable; `vendor` = the product's own claim; `[assumption]` = a belief or guess (for example one the brief states as unverified).
Carried over from a sibling file (for example research/competitive-analysis.md): keep its tag, re-cite its source under your own `Sn`, and name the sibling file in the Source column.

## Gap notes (looked, found nothing)

| ID | Looked for | Where | Why it matters |
|---|---|---|---|
| G1 | Share of users on Android vs iOS | brief, reviews, analytics | decides the first platform |

## Sources

S1 · <title> · <URL> · accessed <YYYY-MM-DD> · <type>

## Legend

<same table as in the personas document>

## Changes

- <YYYY-MM-DD>: created.
```

## 3. Index row

After writing, add or replace the row in `research/INDEX.md` (create the file if missing; newest first):

```markdown
| research/personas.md | proto-personas | <YYYY-MM-DD> | Primary: <role and why in a few words>; <N>% of items are assumptions |
```
