#!/usr/bin/env python3
"""Count the share of assumptions in a proto-personas markdown file.

Usage: python3 assumption_share.py research/personas.md   (or "-" for stdin)

Items are bullet lines and table body rows inside persona sections whose heading
starts with a number: "#### 1." to "#### 5." and "#### 7." (persona cards), or whose
heading contains "persona card". Everything else is ignored.

Tags are the shared kit tags: [user], [source: S3], [snippet: S2], [unverified],
[assumption], [estimate], [synthetic]. A qualifier may follow a colon or comma,
for example [source: S3, weak] or [user: research/brief.md]. Only the first word counts.
  pure assumption : every tag on the item is [assumption] (or [synthetic]:
                    simulated-persona claims are hypotheses, so they count too)
  any assumption  : item has [assumption], [unverified] or [synthetic]
  unknown         : item says "unknown (G<n>)" with no tag: a named hole, not a guess
  untagged        : no tag and not "unknown (G<n>)" (a defect: exit code 1)
  untraced        : sections 1-5 item without "-> I<number>" (a table row may name "I<number>"
                    in its Feeds column instead) (a defect: exit code 1)
Stdlib only.
"""
import re
import sys

KNOWN = {"user", "source", "snippet", "unverified", "assumption", "estimate", "synthetic"}
ASSUMPTION_LIKE = {"assumption", "synthetic"}      # count as pure assumption
ANY_ASSUMPTION = {"assumption", "unverified", "synthetic"}
TAG = re.compile(r"\[([^\]\n]+)\](?!\()")
HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
NUM = re.compile(r"^(\d)[a-z]?\.")
TRACE = re.compile(r"(->|→)\s*I\d+")
ROW_TRACE = re.compile(r"\bI\d+\b")   # table rows may say "I1 · [tag]" in a Feeds column
UNKNOWN = re.compile(r"\bunknown\s*\(G\d+\)")
AREAS = {"1": "context+jtbd", "2": "context+jtbd", "3": "behaviour+pains",
         "4": "behaviour+pains", "5": "triggers", "7": "persona cards"}
ORDER = ["context+jtbd", "behaviour+pains", "triggers", "persona cards"]


def tags_of(line):
    """Return (known tag names, unrecognised bracket texts) for one line."""
    known, other = [], []
    for t in TAG.findall(line):
        m = re.match(r"\s*([A-Za-z]+)", t)
        if m and m.group(1).lower() in KNOWN:
            known.append(m.group(1).lower())
        elif re.search(r"[A-Za-z]{3,}", t):
            other.append(t.strip())
    return known, other


def area_of(title):
    m = NUM.match(title.strip())
    if m and m.group(1) in AREAS:
        return AREAS[m.group(1)]
    if "persona card" in title.lower():
        return "persona cards"
    return None


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) == 2 else 2
    text = sys.stdin.read() if argv[1] == "-" else open(argv[1], encoding="utf-8").read()
    lines = text.splitlines()
    area = None
    stats = {a: {"items": 0, "pure": 0, "any": 0, "unknown": 0} for a in ORDER}
    untagged, untraced = [], []
    for i, line in enumerate(lines):
        h = HEAD.match(line)
        if h:
            area = area_of(h.group(2))
            continue
        if area is None:
            continue
        s = line.strip()
        is_bullet = bool(re.match(r"^[-*]\s+\S", s))
        is_row = s.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", s)
        if is_row and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|?\s*$", lines[i + 1]):
            is_row = False  # table header
        if not (is_bullet or is_row):
            continue
        tags, other = tags_of(s)
        st = stats[area]
        st["items"] += 1
        is_unknown = bool(UNKNOWN.search(s)) and not tags
        if is_unknown:
            st["unknown"] += 1
        elif not tags:
            note = "  (unrecognised tag: [%s])" % other[0] if other else ""
            untagged.append((i + 1, s[:90] + note))
            continue
        if tags:
            if all(t in ASSUMPTION_LIKE for t in tags):
                st["pure"] += 1
            if any(t in ANY_ASSUMPTION for t in tags):
                st["any"] += 1
        traced = TRACE.search(s) or (is_row and ROW_TRACE.search(s))
        if area != "persona cards" and not traced:
            untraced.append((i + 1, s[:90]))

    def pct(n, d):
        return "n/a" if d == 0 else "%d%%" % round(100.0 * n / d)

    print("%-18s %6s %16s %24s %8s" % ("area", "items", "pure assumption",
                                       "any (+unverified)", "unknown"))
    tot = {"items": 0, "pure": 0, "any": 0, "unknown": 0}
    for a in ORDER:
        st = stats[a]
        for k in tot:
            tot[k] += st[k]
        print("%-18s %6d %16s %24s %8d" % (a, st["items"], pct(st["pure"], st["items"]),
                                           pct(st["any"], st["items"]), st["unknown"]))
    print("%-18s %6d %16s %24s %8d" % ("total", tot["items"], pct(tot["pure"], tot["items"]),
                                       pct(tot["any"], tot["items"]), tot["unknown"]))
    if untagged:
        print("\nUNTAGGED items (add a shared tag, or 'unknown (G#)' when there is nothing):")
        for n, s in untagged:
            print("  line %d: %s" % (n, s))
    if untraced:
        print("\nUNTRACED items in sections 1-5 (add '-> I#' or delete the item):")
        for n, s in untraced:
            print("  line %d: %s" % (n, s))
    return 1 if (untagged or untraced) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
