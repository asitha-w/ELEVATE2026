# Anchors Graphic — Surfaces & Elevation Paths · v01 DRAFT

Spec for the judge/team context-setting images. This md is the editable source of
truth — refine here, then re-render the graphics.

Two boards share this role:

- **`graphics/judge-anchors.png`** — the anchors: five surfaces + elevation paths + the 0–5 scale.
- **`graphics/judge-guide.png`** — the judge's step-by-step guide through the evening.

## Design system (all v01 graphics)

Print-first: **white background, dark ink, colored borders** (dark fills only as
small accents). Palette: ink `#241f2d`, muted `#6d6779`, line `#d9d4e4`, accent
purple `#7a4fc0`; surface colors (print-dark variants): Pace `#4f7d2c`, Quality
`#1f8a7d`, Value `#a8811c`, Partnership `#c04f7c`, Happiness `#2f6fb8`.
16:9, 3840×2160. Layout at 1920×1044 scaled 2× via CSS transform (avoids
device-scale font drift); render headless Chrome `--window-size=3840,2160`.

## Board 1 — Anchors: "Five surfaces. One elevation path each."

Subtitle: *Teams declare 1–2 surfaces at registration. Judging starts at the pain:
is it real, is it mapped to the right surface, and did that surface move?*

Five color-coded columns, each with three blocks:

| Surface | The pain looks like | The elevation path | Proof that counts |
|---|---|---|---|
| **Higher Pace** — ship faster, every bolt | Long lead times, waiting on hand-offs, "that takes a sprint" | Agent owns the slow step end-to-end; humans decide at the gate | **Time a real task before vs. with the agent** — lead time / throughput delta |
| **Higher Quality** — gated, tested, reliable | Rework, escaped defects, flaky releases, "almost right" output | Agent tests, reviews or gates every change before it lands | **Rework / change-failure rate down**; defects caught at the gate, shown |
| **Greater Value** — outcomes clients feel | Effort burns on toil while the customer's KPI stands still | Agent absorbs the toil; effort shifts to what the customer pays for | **A named customer KPI, before/after**; % effort moved from toil to new capability |
| **Stronger Partnership** — handholding through change | Slow feedback loops, opaque progress, surprises at the demo | Agent keeps the customer in the loop with evidence, continuously | **A customer-visible artifact the customer validated**; feedback loop measurably faster |
| **Developer Happiness** — engaged, fulfilled teams | Toil, cognitive overload, dread work nobody wants to own | Agent takes the toil; humans keep the judgment and the interesting work | **Before/after team survey + time reclaimed**; "would you keep it on Monday?" |

Footer band — **the universal 0–5 scale** (same reading on every step, both scorecards):

| 0–1 | 2–3 | 4–5 |
|---|---|---|
| **A claim** — told, not shown | **A demonstration** — shown working on the real project, roughly | **A measurement** — proven, repeatable, honest about its limits |

## Board 2 — Judge's guide: "Five steps from the floor to the podium."

Principles strip: Effectiveness over complexity · Evidence over claims (METR
+20%/−19%) · Appropriate autonomy · A real gate, not theater.

The five steps (evening timing):

1. **5:00 PM · together — Brief & calibrate.** Read the anchors board; agree what
   0/3/5 look like; split into 2 crews, one per floor.
2. **5–7:30 PM · your floor — Mentor laps.** Visit, unblock, challenge — no scores.
   Watch who iterates.
3. **~7:30 PM · scoring lap — Score the floor card.** ~10 min per table, five checks
   in order: pain · mapping · agent · gate · proof. First: is the pain real, mapped
   to the right surface? Only then the details. No table-talk between teams.
4. **~8:00 PM · floor closes — Rank & advance.** Rank within your floor, never
   across; top 4 per floor; 2–3 written notes per finalist. Scores banked for
   surface awards.
5. **~8:15 PM · cafe stage — Pitch & pick.** All judges, all 8, fresh scores; ties
   break on Trustworthy Autonomy (The Stress Test); ~3 winners + list every
   customer-ready entry.

Footer: five surface chips + qualifying bar (genuinely agentic · ran on the real
project · surface declared).
