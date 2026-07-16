# ELEVATE 2026 — Team Evaluation Rubric · Version 02 (DRAFT)

> Status: **draft for discussion** — supersedes `../version-01/` (kept intact as
> reference). Owners: Asitha, Isanka, Sachith.
>
> **What changed from v01 (team decision, 16 Jul):** one venue, one floor, one
> round. The event moves to **349 Colombo Main Rd, Colombo 00300**, whose larger
> floors host all 29 teams (87 builders) in a single sitting — no split floors, no
> two-level ladder. **Ten judges roam in five pairs and select the Judges' Pick 8**,
> who close the night with a knowledge-sharing session instead of competitive
> pitches. The value element of the old L2 pitch round is folded into the floor
> round as a sixth scoring step. The Judges' Pick is the recognition — no separate
> winners, no pillar awards.

## The one principle above everything (unchanged)

**An agentic solution is measured by its effectiveness on the project — never by the
complexity of the agent.**

A single well-placed agent that removes a real bottleneck beats a five-agent
orchestration that moves nothing. If two teams moved their pillar equally, the
*simpler* solution wins. (Evidence: `../version-01/research-grounding.md` — DORA
2025, MIT/NANDA 2025, Gartner 2025, McKinsey 2025, Anthropic "Building Effective
Agents".)

## The bearing document — 99x North Star V1.1, word for word

`99x North Star - V1.1.pdf` is corporate-final and this rubric uses its language
verbatim:

> **"Incorporate AI into the software development lifecycle in a way that elevates
> project performance."**
> *Our shared commitment — to our own teams and to every client we guide through
> this transformation.*

The four pillars, exactly as named there:

| Pillar | North Star line |
|---|---|
| **Higher Pace** | Ship faster, every bolt |
| **Better Quality** | An outcome of AI-elevated practices |
| **Extended Value** | New upside that AI-DLC unlocks |
| **A Team That Thrives** | An enjoyable journey for everyone |

> **The measure of every move:** for us and for our clients, if it doesn't advance
> this objective, we don't pursue it.

v01's working names (Pace · Quality · Value · Happiness) are retired; every card,
plate and graphic says the V1.1 names. The knowledge-sharing close is the North
Star's **Analyze → Align → Accelerate** loop in miniature: eight analyzed, aligned
patterns handed to every team to accelerate with on their own project.

## Event shape (evening of Fri 7 Aug 2026 · 5–9 PM · one floor)

- **One working floor** at 349 Colombo Main Rd — all 29 teams settle, build, and
  are judged there. No room changes all evening.
- **Ten judges, five pairs**, roving from 5 PM. Early laps are formative (mentor
  style, no scores); the **scoring lap runs 7:00–8:00** — each pair scores ~6
  stations at ~10 min each.
- Judges ID teams by the **printed name plate** on each table.
- Timeline: 5:00 kickoff → 5:15 build + mentor laps → 7:00 scoring lap →
  ~7:45 dinner opens, judges deliberate → 8:00 full company joins →
  **8:15 Judges' Pick 8 announced** (every team handed its 2–3 written notes) →
  8:20 knowledge sharing → ~8:55 close. Detail: `event-layout.md`.

## The single round

| | The floor round |
|---|---|
| Who judges | 5 pairs, each owning a fixed route of ~6 stations |
| What it proves | **The team found a real pain, the agent moved it — and it's worth something beyond the demo** |
| Selects | Each pair shortlists 2 → 10 candidates → panel of ten deliberates → **Judges' Pick 8** |
| Scorecard | `floor-scorecard.md` — **six steps in order** × 0–5, /30 |
| Then | The eight share what they built with the whole company — not scored, not ranked |

**Judging order still matters:** the pain first (1), the mapping (2), only then the
agent (3), the gate (4), the proof (5), and — new in v02 — **the offering (6)**,
the Extended Value question the old pitch round used to ask. Pain + Mapping +
Proof + Offering = 20 of 30 points: effectiveness and value are structurally the
majority, no weighting multiplier needed.

**Fair at scale (unchanged logic):** each pair ranks *within its own route* and
never across — absolute scores drift when judges see only a slice of the field
(HackMIT/Gavel). The full panel's dinner deliberation over the 10 shortlisted
candidates is where routes reconcile, with score sheets and the five-check gate as
the common frame.

## Qualifying bar (pass/fail — announced on day one, unchanged)

- [ ] **Genuinely agentic** — the model directs its own process/tool use toward the
      stage's goal; a prompt chain with LLM steps does not qualify.
- [ ] **Ran on the real project** — at least one rough, warts-visible run of the
      core loop. Mock data or slideware does not qualify.
- [ ] **Pillar declared** — 1–2 of the four pillars declared up front; evidence is
      scored on the declared pillar(s) only.

## Files in this version

| File | What it is |
|---|---|
| `floor-scorecard.md` | The single scorecard — six steps in order, /30 |
| `event-layout.md` | One-floor layout at 349 Colombo Main Rd + evening timeline |
| `../version-01/anchors-graphic.md` | Per-pillar pains/paths/proofs — content carries over; **pillar names to be updated to V1.1 wording** |
| `../version-01/research-grounding.md` | Unchanged — every axis still traces to the same sources |

**Graphics (`graphics/`, rendered 16 Jul):** `floor-scorecard` (six steps, /30),
`judge-guide` (five pairs → Judges' Pick flow), `judge-anchors` + `team-nameplate` +
`team-area` (V1.1 pillar names; plate has route·table + metric line). The L2 pitch
card and the building-plan board are retired — no floor map needed on one floor.
Same print spec: white bg, 3840×2160, HTML source + headless Chrome.
**Still pending:** event-day invite card reissue (old venue).

## Open questions for v02

- Pair routes: fixed table blocks or drawn on the night?
- Knowledge-sharing slot length: 8 × ~4–5 min fits 8:20–8:55 — enough, or trim to 6 picks?
- Does the expert panel announce its "goes forward to customer" list on the night
  or after? (The pick ≠ automatically forwarded.)
- Name-plate reprint: drop the floor field, add the metric + baseline line (Team
  Guide doctrine) in the same pass?
