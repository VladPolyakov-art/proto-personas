---
name: proto-personas
description: Builds evidence-based proto-personas from whatever research exists (a brief, competitor notes, app-store or forum reviews, interview notes, analytics, or sibling research files such as competitive-analysis and deep-research) and nothing invented. Each persona has jobs, pains, context, behaviours and choice triggers; quotes come only from sources; every assumption is tagged. It ends with a clearly headed primary persona and its justification, and a plan of what to validate with real users. Use it when the user asks for personas, proto-personas, user profiles, "who are our users", "make personas from this research", "jobs to be done for our segments", or wants to pick a primary user before design or PRD work. Also use it to audit or rewrite personas that look made up (stock names, hobbies, no sources). It also serves Russian-speaking users.
---

# Proto-personas from evidence

The goal is personas that drive design decisions, not decoration. A proto-persona is a **hypothesis about a user segment** built from secondary data. It is not a real person and not an interview result. The value is in the traceability: every statement points to a source or is openly marked as an assumption, so the team knows what to trust and what to test.

Shared rules for the kit this skill belongs to (tags, header block, file names, index) are in `references/kit-protocol.md`. Read it before writing.

## Rules (the reason this skill exists)

1. **Facts only from the user or from a source.** No invented numbers, quotes, reviews, demographics, photos, hobbies, or "Maria, 34". Label a persona by role ("Shift manager"), not by a fake name.
2. **Every claim in sections 1 to 5 and on persona cards carries a shared tag** (`[user: <file>]`, `[source: Sn]`, `[snippet: Sn]`, `[unverified]`, `[assumption]`, `[estimate]`, `[synthetic]`). With no checked data the tag is `[assumption]` and it points to a gap note (`G#`), meaning "searched, nothing found". With nothing at all, not even a reasoned inference, write plain `unknown (G#)`. Without the gap link, an assumption is just a guess nobody can follow up.
3. **Quotes are verbatim and attributed.** A phrase put into a persona's mouth that is not a verbatim source quote is labelled "constructed from source wording, not a user quote".
4. **Every item feeds an insight** (`-> I#`). An item that changes no design decision is deleted. This is what separates a persona from a character sketch.
5. **Exactly one primary persona**, under a heading called "Primary persona", with a written justification.
6. **Vendor claims are not user evidence.** Pricing, feature lists and "reduces X by 30%" from a product's own site get the qualifier `vendor`: `[source: S2, vendor]`. They describe the product, not the people.
7. **Simulated is not evidence.** Anything from a simulated interview stays `[synthetic]`: it can shape the validation plan, never a fact.
8. Public sources only. Do not sign up, log in, or fill in forms on any service. Do not ask for passwords or tokens.

## Process

### Step 0. Reconnaissance and intake (read-only)

1. List `research/` (or the folder the user names), plus `docs/`, `README`, notes, exports, and any files the user pointed to. Read them fully, not by filename.
2. Reuse sibling outputs when present (rules in `references/kit-protocol.md` §4); never require them:
   - `research/competitive-analysis.md`: the named direct competitors for "solves it today", their pricing (tag `vendor`), user-voice excerpts and review pains for frustrations. Keep its tags and weak/vendor qualifiers; re-cite its sources under your own `Sn`.
   - `research/deep-research.md`: segments, behaviours, market context and any voice-of-users material. Keep its confidence qualifiers.
   - `research/ux-audit/summary.md` and `research/ux-audit/<product>/audit_report.md`: usability pains in the current solutions, for section 4. An audit describes an interface, not what a user feels; do not use it as proof of a feeling.
   - `research/interview-*.md` (from simulated-interview): all `[synthetic]`. Use to sharpen the validation plan, never as evidence. Real interview notes the user wrote are `[user: <file>]`.
   - If a sibling file is older than about 3 months or the product changed, say so and ask whether to refresh it, unless the user already said.
   - Name every file you used in the `Inputs` line. Do not edit a sibling's file; if you find an error in it, mention it in the summary.
3. Establish the minimum: what the product does, who it is meant for, the main scenarios. **If there is no brief, no research and no sibling output, stop and ask 3 to 5 questions** instead of writing:
   - Who is it for (roles or segments), and who pays versus who uses it?
   - What do those people do today instead (tools, spreadsheets, workarounds, named competitors)?
   - What real material exists: interviews, support tickets, reviews, analytics, survey answers?
   - What are the 2 to 4 main scenarios?
   - Anything known to be true versus only believed?
4. Offer the options: (a) the user pastes or points to material; (b) you collect public material yourself (competitor reviews, forum threads) if web tools are available; (c) a **hypothesis-only draft** where every item is `[assumption]`, with no quotes and no numbers, clearly headed as a list of questions to validate. Do not silently pick (c).
5. Web research is optional. Use Firecrawl, WebSearch or WebFetch if present. If none is available, say so in one line and continue with what the user provided.

### Step 1. Evidence ledger (before any persona)

Walk through every input and write the ledger (template in `references/output-template.md`), by default to `research/personas/evidence-ledger.md`:
- `L<n>` rows: claim, source (file and section, or `Sn` and location), the **source's own wording**, and the shared tag with its weight.
- `G<n>` rows: gaps, "looked for X in Y, no data". Typical gaps: how often they use it, devices, budget and who decides, why people leave a competitor, accessibility needs.
- A "Sources" list in the protocol format for every web page or document you opened.

Weight, expressed in the tag:
- no qualifier: first-hand from the target user or their data (interview, support ticket, analytics, survey they answered), for example `[user: research/interview-notes.md]`.
- `weak`: second-hand or unverifiable (review excerpt without context, forum comment, undated blog, raw model-generated research, an author's summary of unknown origin): `[source: S3, weak]`.
- `vendor`: the product's own claim, price or marketing: `[source: S2, vendor]`.
- `[assumption]`: a guess stated in the brief ("we think most users are on Android") or your own inference.

Why first: writing personas straight from a pile of material mixes facts with plausible filler. Doing the ledger first drops the share of unsupported statements sharply, especially in the "choice triggers" section.

### Step 2. Segments and the persona set

- Default 3 personas; 2 to 4 if the sources show fewer or more distinct segments (say why). Each covers a separate segment and a separate scenario. One is primary.
- If the roles named in the brief do not match the segments the evidence shows, **show the mismatch to the user**, do not bend the data to fit.
- B2B: the buyer and the user are different people. Make them different personas, or give an explicit "who decides on purchase" section.
- If a role has one read-only task, do not build a persona; write a short role preset (task, blockers, 3 to 4 requirements).
- If one persona has distinct modes (for example a manager who approves and a coordinator who schedules), give each mode its own persona card.
- If the user already has marketing personas, add a "Relation to existing personas" section: where each went and why. Marketing personas split people by sales channel; product personas split by who works in the interface directly.
- Add one **stress persona** (low digital literacy, phone on the move, or accessibility, whichever fits the product). Persona card only, no full profile.
- Give every persona a **slug** (`shift-manager`), shown in the set table and under its heading. Other tools find the persona by it.
- Show the set (table: persona, segment, scenarios, priority) and the mismatches to the user **before** writing the full profiles if there is any real doubt. Otherwise continue and present it with the result.

### Step 3. Write each persona

Use `references/output-template.md`. Keep its structure exactly: other skills read the persona cards by these headings. Sections:
1. **Role and context**: who, how the product fits their day, other tools around it. No photo, no hobbies.
2. **Job to be done**: the task they "hire" the product for, the situation, the successful outcome, and a job story: "When [situation], I want [motivation], so that [outcome]".
3. **Behaviour**: frequency, device, place, rush; a typical scenario in concrete steps; how they solve it today, **including the direct competitors named in the research**, not only substitutes like "a spreadsheet".
4. **Frustrations and constraints**: what annoys them in current solutions (cite the competitor or audit source), time, budget, skills, and what they fear when switching.
5. **Choice triggers**: how they would find the product, what makes them try it, what makes them stay, what is a dealbreaker. This section is where most assumptions hide: count it separately.
6. **Insights** (the point of the exercise): 3 to 5 design decisions in the form "Because [fact from the persona] -> we need [decision]".
7. **Persona card** (at most 10 lines, compact): digital literacy 1 to 5, experience with analogues, default device and context, goals in the user's words, fears and stop factors, how they talk (2 to 3 phrases, quote rules above). **Each attribute carries a tag**, otherwise invented details enter downstream testing as data.

### Step 4. Insights and pruning

Write insights per persona, then trace: every item in sections 1 to 5 ends with `-> I#`. Delete any item that feeds no insight. Re-read each insight: is the design decision concrete (a screen, a default, a copy rule, a removed step), or generic ("make it easy")? Rewrite generic ones.

### Step 5. Primary persona, summary table, validation plan

- **Pick the primary** and justify with evidence under the heading `## Primary persona` (placed right after the persona-set table): share of the key scenarios, strength of evidence, frequency of use, severity of the pain, fit with the product goal. Cite `L#`. State why the others are secondary. If the choice is close, say so and name what would change it. The primary's full section is also marked "(PRIMARY)".
- **Summary table** across personas: JTBD, priority, key design takeaway, the single biggest assumption to test.
- **Validation plan** (what to check with real people, per persona): the assumption, which insight breaks if it is false, a method (5 interviews with X, a 3-question survey, a fake-door test, a look at analytics), the question to ask in plain words, and the result that would falsify it. Order by risk. Interview questions about past behaviour, not about hypothetical future use.

### Step 6. Measure and self-check

- Run `python3 scripts/assumption_share.py research/personas.md` (path relative to this skill's folder, for example `~/.claude/skills/proto-personas/scripts/assumption_share.py`). It counts items per area (sections 1 to 2, 3 to 4, 5, persona cards), reports the share of pure assumptions (`[assumption]` or `[synthetic]` only) and of any assumption including `[unverified]`, counts `unknown (G#)` items, and lists untagged or untraced items. Put its numbers in an "Assumption statistics" section. Without Python, count by hand and say it is a hand count. A manual count tends to undercount; the script is stricter.
- High share (rule of thumb: over a third of sections 3 to 5 is assumption) is not a failure, it is the finding: say plainly that real customer discovery is the next step, and list which sections are thin.
- Self-check against `references/checklist.md` (score each 0 to 2) and fix anything below 2.

### Step 7. Deliver

Write the files: `research/personas.md` and `research/personas/evidence-ledger.md` (if the user names another folder, use it for both and say so). Both start with the header block, end with Sources (where `[source]` or `[snippet]` is used), the tag legend, and a "Changes" line; a rerun updates them in place with a new dated Changes line, no `-v2` copies. Then update `research/INDEX.md`: one row, newest first, replace your own row on a rerun (format in `references/output-template.md`). The takeaway names the primary persona and the assumption share.

Then reply in chat, in the user's language, in a short summary: the set, the primary and why, the assumption share and the thinnest area, the top 3 things to validate, open questions for the user. Do not paste the whole document. End with at most one next-step line: if the personas rest mostly on assumptions, suggest `simulated-interview` (it can show what to ask real users; its output stays `[synthetic]`), or `deep-research` if the segments themselves are unclear. If that skill is not installed (check `~/.claude/skills/<name>/` and `.claude/skills/<name>/`), give its repo link from the kit table in `references/kit-protocol.md`. Suggest only; never run it without the user's go-ahead. Synthetic users never replace real ones, and a case study must not present them as a user test.

## Sub-agent (optional)

When there are many sources, delegate the ledger or one persona to a `general-purpose` sub-agent with the role prompt in `references/ux-researcher.md`. Give it the file paths, the output path, the rules above and the path of `references/kit-protocol.md`, since it knows nothing else. Review its result against the checklist before accepting it. The agent does not talk to the user; open questions come back in its report.

## Edge cases

- **Sources contradict each other:** keep both ledger rows, say which is stronger, and do not average them into a made-up middle.
- **Only vendor and weak sources:** write the personas, tag accordingly, and state that the base is thin.
- **Single clear segment:** one full persona plus a stress card is fine; say why there are not three.
- **User asks to "make it more vivid" with names, faces, hobbies:** decline the invented detail, offer vivid wording drawn from real quotes.
- **Existing personas to audit:** build the ledger from the same inputs, tag every statement of the old personas, and report which are unsupported.
- **Sensitive data in sources** (names of interviewees, emails): keep it out of the output; refer to "Interview 2".
- **Sibling file contradicts the user's own notes:** keep both ledger rows with their tags and show the conflict to the user.

## Works with other skills

- Reads, if present: `research/competitive-analysis.md`, `research/deep-research.md`, `research/ux-audit/*`, `research/interview-*.md` (as `[synthetic]` only). None is required.
- Read by siblings: `simulated-interview` takes a persona card from `research/personas.md` (found by its slug and the "Primary persona" heading); `feature-research` uses the personas to say who needs a feature and how well the evidence backs it.
- Full rules: `references/kit-protocol.md`.
