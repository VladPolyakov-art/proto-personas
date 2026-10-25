# proto-personas

A Claude Code skill that builds proto-personas from the research you already have (a brief, competitor notes, reviews, interview notes, analytics, or sibling research files) without inventing anything. Every claim is traced to a source or openly marked as an assumption, and the result ends with a primary persona and a plan of what to check with real users.

## How it works

- **Evidence ledger first.** Every input becomes `L#` rows (claim, source, the source's own wording, shared tag with its weight). Missing data becomes `G#` gap notes: "looked, found nothing".
- **Personas are hypotheses, not characters.** Labelled by role, no stock names, photos or hobbies. Each has a job to be done and job story, behaviour (including the direct competitors named in your research), frustrations, choice triggers, and 3 to 5 insights in the form "Because [fact] -> we need [decision]".
- **Source tags on everything.** The shared kit tags: `[user: research/interview-notes.md]`, `[source: S3, weak]`, `[source: S2, vendor]`, `[assumption] (G#)`, `[synthetic]`. Quotes are verbatim; phrases the model constructs are labelled as such. An item that feeds no insight is deleted.
- **Primary persona with a justification**, under a clear "Primary persona" heading, each persona with a slug, a stress persona card, and buyer versus user kept separate in B2B.
- **Assumption share by script** (`scripts/assumption_share.py`): per area, pure and any assumptions, plus untagged and untraced items. A high share is reported as the finding: it means real customer discovery comes next.
- **Validation plan:** per top assumption, a method, a plain-words question about past behaviour, and what would falsify it.

With no brief and no research, the skill asks 3 to 5 questions first and does not write personas from nothing.

## Output

- `research/personas.md`: the personas, summary table, validation plan, assumption statistics, self-check, Sources and tag legend.
- `research/personas/evidence-ledger.md`: facts and gap notes.
- A row in `research/INDEX.md`, and a short summary in chat, in your language. Paths can be overridden.

Optional next step: persona cards are the input for simulated interviews and synthetic user runs. Findings from those are hypotheses until real people confirm them.

## Contents

| Path | What |
|---|---|
| `SKILL.md` | instructions for the agent |
| `references/kit-protocol.md` | shared rules of the research kit (file names, tags, header block, index) |
| `references/output-template.md` | templates for the ledger and the personas document |
| `references/checklist.md` | done criteria (scored 0 to 2) and common failure patterns |
| `references/ux-researcher.md` | role prompt for a `general-purpose` sub-agent |
| `scripts/assumption_share.py` | stdlib-only Python, counts assumption share and finds untagged items |
| `evals/` | scenarios for checking the skill's behaviour |

## Works with

This skill is one of six research skills that share file names and evidence tags.

| Skill | Writes | Repo |
|---|---|---|
| competitive-research | `research/competitive-analysis.md` | https://github.com/VladPolyakov-art/competitive-research |
| deep-research | `research/deep-research.md` | https://github.com/VladPolyakov-art/deep-research |
| ux-audit | `research/ux-audit/<product>/audit_report.md` (+ `research/ux-audit/summary.md`) | https://github.com/VladPolyakov-art/ux-audit |
| proto-personas | `research/personas.md` | https://github.com/VladPolyakov-art/proto-personas |
| simulated-interview | `research/interview-<persona-slug>.md` | https://github.com/VladPolyakov-art/simulated-interview |
| feature-research | `research/feature-<slug>.md` | https://github.com/VladPolyakov-art/feature-research |

Each skill works alone; when a sibling's output is in `research/`, it is reused instead of redone.

## Installation

```bash
git clone https://github.com/VladPolyakov-art/proto-personas ~/.claude/skills/proto-personas
```

Requirements: Claude Code. Python 3 is optional (for the assumption count; otherwise the skill counts by hand and says so).

## Optional tools

- Firecrawl, WebSearch or WebFetch: to collect public reviews and competitor pages when you have no material of your own. Without them the skill works only from what you provide and says so.
- Public pages only. The skill does not sign in, sign up or fill in forms, and never asks for passwords or tokens.

## License

[MIT](LICENSE)
