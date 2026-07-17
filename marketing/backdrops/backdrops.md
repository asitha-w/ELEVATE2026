# Backdrops — stage & venue graphics · source of truth

Four backdrop designs for the event, distilled from the organizer's reference set
(`graphics_reference/`): 2001-style one-point perspective, human+machine partnership
with halftone texture, movie-poster typography, and minimal line-art conceptualism.

| File | Design | Essence |
|---|---|---|
| `backdrop-corridor` | **The Corridor** — octagonal tunnel in one-point perspective, NorthStar at the vanishing point, the robot walking out of it | 2001: A Space Odyssey |
| `backdrop-decide` | **The Decision** — giant split typography (hollow "AGENTS DELIVER." / gradient "YOU DECIDE."), a glowing gate line, robot on the far side, halftone field | poster typography + partnership |
| `backdrop-northstar` | **The NorthStar** — thin-line four-point star with orbit rings, a node constellation, the five rising wave arcs, four pillar names | minimal line art |
| `backdrop-waves` | **The Waves** — the 5-wave elevation ladder in the event theme (matte ink + apricot): grey steps rise into orange at wave 4, "you build here", "the project calls the agent" | the Team Guide ladder, print-size |

## Size — what to tell the printer

Files are **7680 × 4320 px, 16:9**. Backdrops are viewed from 2–5 m, and
large-format printing only needs **30–75 dpi at final size**, so one file covers
every realistic option:

| Printed size | Effective dpi | Verdict |
|---|---|---|
| 3.0 × 1.7 m | ~65 dpi | crisp |
| 4.0 × 2.25 m | ~49 dpi | standard stage backdrop |
| 6.0 × 3.4 m | ~32 dpi | fine at stage distance |

- Tell the vendor: *scale proportionally to the frame, 16:9 source, add their
  standard bleed*. Key content sits in the **center 80%** (safe for modest crops).
- LED walls / screens: use the PNG directly (native 16:9).
- If the frame is a non-16:9 shape (e.g. 8×8 ft square step-and-repeat), send the
  frame dimensions and we re-compose — don't let the printer squash it.

Render: headless Chrome `--window-size=7680,4320`; layout 1920×1080 scaled 4×.
Robot & logo assets referenced from `../logos/`.
