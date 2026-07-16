# ELEVATE 2026 — Event Calendar & Sessions · source of truth

Editable source for the **Event Calendar** and **Sessions** tabs on the site, and
for the four invitation cards in `marketing/invites/`. Venue for runway sessions:
**99x · 65 Walukarama Road, Colombo**. **Event day (7 Aug) moved to
99x · 349 Colombo Main Rd, Colombo 00300** (16 Jul decision — one floor hosts the
whole event; event-day invite card needs a reissue).

## The runway (from the ELEVATE 2026 Action Plan)

| Date | Milestone | Notes |
|---|---|---|
| Fri 10 Jul | Introductory email | Sent — the "Stay tuned" flyer |
| Mon 20 Jul | **Briefing for team leads** | Format, expectations, the NorthStar pillars, how judging works |
| Fri 24 Jul | **Ramp-up Session 1** | LX-meeting style steering discussions · keynote · setting up an agent on Xianix · SWOT · ~1.5h |
| Fri 31 Jul | **Ramp-up Session 2 — the Panel Discussion** | Xianix-focused · walkthrough of worked examples · panel Q&A |
| Mon 3 – Thu 6 Aug | **Judges' preparation** | Rubric walkthrough & calibration; judging context pack handed to every judge |
| **Fri 7 Aug** | **ELEVATE 2026 — Event Day** | 5–9 PM · two working floors · pitches & awards at the cafe podium |

(Team registration milestone removed from the public calendar per organizing
decision, 15 Jul.)

## The sessions

### Ramp-up Session 1 — Fri 24 Jul (~1.5h, time & venue TBC)

From idea to a running start — in three parts:

1. **1/3 — The NorthStar & agentic maturity.** Plug the four pillars, then locate
   each project on **Gartner's agentic-AI maturity roadmap** (five levels, from
   task-specific assistants through single agents with human gates to orchestrated
   multi-agent systems and largely autonomous operations). The point teams take
   home: **maturity is matched autonomy, not an autonomy race** — Gartner also
   predicts 40%+ of agentic projects canceled by 2027 for unclear value, which is
   exactly what our rubric scores against.
2. **2/3 — Xianix, live.** A worked example on **[xianix.ai](https://xianix.ai/)**
   — 99x's own agent platform (AI-DLC: FDE-style pods of AI agents + human
   engineers; "AI agents do the work. Humans own the outcome." — same thesis as
   our tagline). Built on Claude Code plugins, open, no vendor lock-in.
3. **3/3 — SWOT + the platform landscape.** Each team SWOTs its agentic play, with
   a map of what's popular beyond Xianix as of Jul 2026 —
   *managed platforms:* Microsoft Copilot Studio, AWS Bedrock AgentCore, Google
   Vertex AI Agent Builder, OpenAI's agent platform, Salesforce Agentforce;
   *frameworks/SDKs:* LangGraph (stateful workflows, human-in-the-loop), Claude
   Agent SDK / Claude Code (what Xianix builds on), CrewAI (role-based crews),
   Microsoft Agent Framework, AutoGen/AG2, LlamaIndex Workflows, Pydantic AI.
   These are wave 5 of the seminar's **5 waves of AI tooling** — platforms for
   custom agent workforces.

### Ramp-up Session 2 — the Panel Discussion — Fri 31 Jul (time & venue TBC)

One week before the event. The panel represents three seats:

- **Engineering** — people who have shipped agentic solutions on real projects
- **Delivery** — delivery leaders who run the projects teams will elevate
- **Senior leadership** — the strategic view

Format: discuss the projects and challenges we have already seen, so teams get
inspired and clarify the details they still have open. Bring the hardest questions.

## Invitations (`marketing/invites/`)

Four invite cards, dark brand style (flyer look), logo + tagline, one per event:

| Card | Event | Date line |
|---|---|---|
| `invite-leads-briefing` | Briefing for team leads | Mon 20 Jul · time & venue TBC |
| `invite-rampup-1` | Ramp-up Session 1 | Fri 24 Jul · ~1.5h · time & venue TBC |
| `invite-rampup-2` | Ramp-up Session 2 — Panel Discussion | Fri 31 Jul · time & venue TBC |
| `invite-event-day` | ELEVATE 2026 — Event Day | Fri 7 Aug · 5–9 PM · 99x, 349 Colombo Main Rd, Colombo 00300 — **reissue pending** (rendered card still shows old venue) |

Each card: HTML source next to rendered PNG (portrait 2400×3000, headless Chrome).

**v2 design (15 Jul):** the robot character extracted from the launch flyer
(`marketing/logos/elevate-robot.png`, transparent cutout) anchors bottom-right of
every card; a glowing **four-point NorthStar** sits above the invite line; a
five-arc **"5 waves of AI tooling"** motif (from the AI-DLC breakfast seminar)
rises from the bottom-left corner. The original v1 cards are parked in
`marketing/invites/v1/` for easy revert.
