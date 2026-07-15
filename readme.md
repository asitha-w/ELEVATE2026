# ELEVATE 2026

99x agentic-AI hackathon — judging rubric & event pack.
**Event: Fri 7 Aug 2026 · 5–9 PM · 99x, 65 Walukarama Road, Colombo.**

- 🌐 **Site:** https://asitha-w.github.io/ELEVATE2026/ — four tabs:
  **The Pack** (rubric & event graphics) · **Event Calendar** (runway to event day) ·
  **Sessions** (ramp-up 1 & 2 with invitations) · **Marketing** (flyer, invites, logos)
- 📄 **Single-file pack:** [`ELEVATE2026-pack.html`](ELEVATE2026-pack.html) (all graphics embedded — download & open anywhere)
- 📁 **Current rubric:** [`rubric/version-01/`](rubric/version-01/) — see its [README](rubric/version-01/README.md)
- 📅 **Calendar & sessions source:** [`event/calendar-and-sessions.md`](event/calendar-and-sessions.md)
- 📣 **Marketing kit:** [`marketing/`](marketing/) — logos, launch flyer, invitation cards (print originals)

**The NorthStar — four pillars** (Partnership retired 15 Jul): Pace · Quality · Value · Happiness.
Official tagline: *"Agents deliver. You decide."*

## Versioning

The rubric is versioned by directory: `rubric/version-01/`, `rubric/version-02/`, …
Each version is self-contained (markdown sources + `graphics/` with HTML + rendered
PNG). **v01 is the current draft** — being tuned with the organizing team; tag
`v01` marks its first published state; running changes in
[`v1-improvements.md`](rubric/version-01/v1-improvements.md).

Every graphic has a markdown source of truth — edit the md, then the HTML, then
re-render (headless Chrome, `--window-size=3840,2160`; invites `2400,3000`):

| Graphic | Markdown source |
|---|---|
| `rubric/version-01/graphics/judge-guide.png`, `judge-anchors.png` | `rubric/version-01/anchors-graphic.md` |
| `rubric/version-01/graphics/scorecard-l1.png` | `rubric/version-01/L1-floor-scorecard.md` |
| `rubric/version-01/graphics/scorecard-l2.png` | `rubric/version-01/L2-pitch-scorecard.md` |
| `rubric/version-01/graphics/building-plan.png`, `team-area.png`, `team-nameplate.png` | `rubric/version-01/event-layout.md` |
| `marketing/invites/invite-*.png` (4 cards) | `event/calendar-and-sessions.md` |

Research citations for every scoring axis: [`research-grounding.md`](rubric/version-01/research-grounding.md).
