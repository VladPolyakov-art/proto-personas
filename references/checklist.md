# Done criteria and self-check

Score each line 0 (missing), 1 (partial), 2 (fully met). Fix every line below 2 before delivering.

| # | Criterion |
|---|---|
| 1 | No photos, stock names, hobbies or abstract goals; personas are labelled by role |
| 2 | An evidence ledger exists (research/personas/evidence-ledger.md) with `L#` rows (verbatim source wording, shared tag with weight) and `G#` gap notes |
| 3 | Every item in sections 1 to 5 and on persona cards has a shared tag (`[user: file]`, `[source: Sn]`, `[assumption]`, ...); no item is untagged |
| 4 | Every `[assumption]` points to a `G#` gap note; items with no data and no inference say `unknown (G#)` |
| 5 | Every item in sections 1 to 5 ends with `-> I#`; items that feed no insight were deleted |
| 6 | Quotes are verbatim and traced to an `L#`; constructed phrases are labelled as such |
| 7 | Frustrations are tied to named competitors, audit findings or reviews, not invented |
| 8 | "Solves it today" names the direct competitors from the research, not only substitutes |
| 9 | Each persona has 3 to 5 insights in the form "Because [fact] -> we need [decision]", and each decision is concrete |
| 10 | Exactly one primary, justified with evidence and with what would change the choice |
| 11 | Buyer and user are separate personas (or an explicit decision-maker section) when they differ |
| 12 | Mismatches between brief and evidence, and contradictions between sources, are shown, not smoothed over |
| 13 | A stress persona card exists (or a stated reason why not) |
| 14 | The validation plan has, per top assumption: method, plain-words question, falsifier; ordered by risk |
| 15 | Assumption statistics come from the script (or are labelled a hand count); thin areas are named |
| 16 | No invented numbers, reviews or sources anywhere; vendor claims carry the `vendor` qualifier |
| 17 | The file has the header block (Skill, Date, Product, Inputs, Tags), a Sources list, the tag legend and a Changes line; `Inputs` names every sibling file used |
| 18 | A `## Primary persona` heading exists, every persona has a slug, and `research/INDEX.md` has a row for this file |
| 19 | Claims carried over from a sibling file keep their tag and weight; anything from a simulated interview is still `[synthetic]` |

## Common failure patterns

- Plausible filler: a "typical day" with a time of day, a commute, a coffee. If no source says it, delete it.
- Choice triggers written from imagination; this is the section where gaps usually are. Use `[assumption]` + `G#`, or `unknown (G#)`.
- Pains that are really the product's features restated. A pain must exist without our product.
- Two roles hidden in one persona ("manager or coordinator"). Split or justify.
- Quotes polished by the model. Copy the source text exactly, or do not use quotation marks.
