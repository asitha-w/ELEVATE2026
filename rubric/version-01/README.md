# ELEVATE 2026 — Team Evaluation Rubric · Version 01 (DRAFT)

> Status: **draft for discussion** — not yet agreed. Owners: Asitha, Isanka, Sachith.

## The one principle above everything

**An agentic solution is measured by its effectiveness on the project — never by the
complexity of the agent.**

A single well-placed agent that removes a real bottleneck beats a five-agent
orchestration that moves nothing. If two teams moved their surface equally, the
*simpler* solution wins. This is what the industry evidence says separates the ~5%
of AI initiatives that produce measurable value from the rest (see
`research-grounding.md`: DORA 2025, MIT/NANDA 2025, Gartner 2025, McKinsey 2025,
Anthropic "Building Effective Agents").

## Supporting principles

1. **Evidence over claims.** Developers systematically misjudge their own AI speedup
   (METR 2025: believed +20%, measured −19%). We score *demonstrated* before/after,
   not testimony. Running the agent is not the ruler — it is the **evidence
   standard**: a claim with no demonstrated run is scored as a claim.
2. **Appropriate autonomy, not maximum autonomy.** The right autonomy level is a
   design choice matched to the risk of the lifecycle stage (Morris et al./DeepMind,
   Anthropic). Removing the human entirely is not a higher score.
3. **A real gate, not compliance theater.** A genuine decision gate shows the human
   *why* (context, evidence, diff), offers reject/edit paths the agent actually
   incorporates, and sits at the consequential action (Anthropic, LangChain HITL).
4. **Judge fairly at scale.** Each floor crew ranks *within its own floor* and never
   across — absolute scores drift when judges see only a slice of the field
   (HackMIT/Gavel research). The pitch panel sees all 8 finalists, so absolute
   scoring is safe there.

## Event shape (evening of Fri 7 Aug 2026 · 5–9 PM · one building)

- **Two working floors** — floors 1 and 5. Teams settle, group, and build there.
  Each floor gets its own roving **expert crew** (Crew A / Crew B) from the start.
- **Cafe (ground floor) = the podium** — kickoff, the 8-team pitch round, awards.
- **Dinner** on floor 6 + cafe from ~7:45 PM. Sodas on both working floors + cafe.
- Judges ID teams by the **printed name plate** on each table (team · project &
  customer · stage owned · declared surfaces · floor & table).
- Proposed timeline: 5:00 kickoff (cafe) → 5:15 build + mentor laps → ~7:30 scoring
  lap → ~8:00 finalists announced + dinner → ~8:15 pitches → ~8:50 awards.

## The two levels

| | Level 1 — Floor | Level 2 — Pitch |
|---|---|---|
| Who judges | 2 expert crews, one per floor, roving from 5 PM | Panel, all judges, whole company watching |
| What it proves | **The team found a real pain and the agent moved it** | **The solution is an offering a customer would pay for** |
| Selects | Top 4 per floor → 8 finalists | ~3 winners → 99x expert panel → customer |
| Scorecard | `L1-floor-scorecard.md` — **five steps in order** × 0–5, /25 | `L2-pitch-scorecard.md` — 4 steps × 0–5, /20 |
| Also feeds | The 5 surface awards (banked floor scores) | Winner list + customer-offering list |

**L1 judging order matters:** Step 1 asks if the team identified an *effective pain
point*; Step 2 whether it's correctly *mapped to the declared surface* with a real
measure; only then the details — the agent (3), the gate (4), the proof (5).
Pain + mapping + proof = 15 of 25 points: effectiveness is structurally the
majority, no weighting multiplier needed.

## Qualifying bar (checked at L1, pass/fail — announced on day one)

- [ ] **Genuinely agentic** — the model directs its own process/tool use toward the
      stage's goal; a prompt chain with LLM steps does not qualify (Anthropic
      workflow-vs-agent test; Gartner "agent washing").
- [ ] **Ran on the real project** — at least one rough, warts-visible run of the
      core loop. Mock data or slideware does not qualify.
- [ ] **Surface declared** — 1–2 of the five surfaces declared up front; evidence is
      scored on the declared surface(s) only.

## The five surfaces (unchanged)

Pace · Quality · Value · Partnership · Dev Happiness — per-surface pains, elevation
paths, and proofs in `anchors-graphic.md` and the `judge-anchors` graphic.

## Files in this version

| File | What it is |
|---|---|
| `L1-floor-scorecard.md` / `graphics/scorecard-l1.png` | Floor round scorecard — five steps in order |
| `L2-pitch-scorecard.md` / `graphics/scorecard-l2.png` | Pitch round scorecard |
| `anchors-graphic.md` / `graphics/judge-anchors.png` | The five surfaces + elevation paths + 0–5 scale |
| `graphics/judge-guide.png` | Judge's guide — five steps from floor to podium |
| `event-layout.md` / `graphics/building-plan.png` | Building map + evening timeline |
| `graphics/team-area.png` | The team pod — how a work area is set up |
| `graphics/team-nameplate.png` | Printable per-team name plate (judges' team ID) |
| `research-grounding.md` | Every rubric axis traced to citable sources |

All graphics: print-first (white background, dark ink, colored borders), 3840×2160.
Source HTML next to each PNG; render via headless Chrome at `--window-size=3840,2160`.

## Open questions for v02

- Do the ~3 winners rank (1st/2nd/3rd) or stand equal?
- Surface awards: computed from which L1 step — The Proof, or total?
- Can a finalist also win a surface award?
- Exact team count per floor (27 teams → 13/14 split?) and table numbering.
- Scoring lap timing: is 13–14 tables × ~10 min per crew feasible in one lap, or
  does the scoring lap need to start earlier / crews sub-split?
