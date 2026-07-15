# v1 Improvements — tuning notes for the next revision

Running list of changes agreed while tuning v01 with the team. Items are applied to the
mds/graphics in batches, then re-rendered — status marked per item.

## 1. Team pod: drop the dedicated demo screen (Asitha, 14 Jul) — ✅ APPLIED 14 Jul

Teams don't need a separate demo screen at the pod — **showing the run on one
laptop screen is enough**. The bar stays the same: any judge, any lap, "run it
now" should be a 30-second ask. Update `team-area` graphic (remove the DEMO
SCREEN element, reposition the callout to a laptop) and the pod checklist
("demo screen live" → "demo laptop ready").

## 2. L2 "The Customer" — clarify what it actually measures (discussion, 14 Jul) — ✅ APPLIED 14 Jul (renamed "The Offering")

Every team *has* a customer by construction (they're project teams) — so the axis
must not read as "do you have a customer?". What it measures is **offering
readiness**: would *this specific customer* adopt and pay for this as a product,
not a hackathon demo. Candidate rename: **"The Offering"**. Scored substance
stays: named user + workflow it lands in, cost-to-run vs value-per-run (unit
economics), honest gap list, credible path past pilot.

## 3. L2 "The Stress Test" — judge guidance on edge-case probing (discussion, 14 Jul) — ✅ APPLIED 14 Jul

Two layers, both belong to the axis:

- **Demonstrated (the team's job, scored):** the team deliberately breaks their own
  agent on stage — feeds it a case it gets wrong — and shows the human gate
  catching it, and ideally the agent incorporating the correction.
- **Probed (the judges' job, in Q&A):** judges ask edge-of-thinking questions the
  team may not have considered — inputs, scale, and failure modes that would break
  their current design. The score reflects how the team *reasons about* edges they
  haven't handled: do they know where the boundary is, or do they claim it can't
  break?

Add 3–4 canonical edge probes to the L2 card's Q&A prompts (see below).

## 4. NorthStar update: Partnership removed — four pillars (corporate, 15 Jul) — ✅ APPLIED 15 Jul

Corporate NorthStar defines **four pillars: Pace, Quality, Value, Happiness** —
Partnership is dropped as a pillar. Applied everywhere (mds, all graphics, site,
pack): anchors board becomes four columns, nameplate/scorecards carry four chips,
"5 surface awards" → "4 pillar awards", and the working term changes from
*surface* to **pillar** under the NorthStar name. Partnership's substance (customer
trust, human gate) already lives in L1 "The Gate" and L2 "The Offering" — the
rubric loses nothing.

## 5. Official marketing kit adopted (15 Jul) — ✅ APPLIED 15 Jul

Marketing shared the logo set (Colour / Full black / B&P / W&P) and the launch
flyer. The flyer confirms **"Agents deliver. You decide."** as the official tagline
(nameplate note updated). Logos used on the site header and invite cards; marketing
material collected under `marketing/`.

## 6. Site restructured into four tabs (15 Jul) — ✅ APPLIED 15 Jul

`docs/index.html` becomes: **The Pack** (rubric & event graphics) · **Event
Calendar** (runway from the action plan; registration milestone removed; judges'
prep 3–6 Aug worded as rubric walkthrough + context-pack handover) · **Sessions**
(ramp-up 1 · 24 Jul, ramp-up 2 = the panel discussion · 31 Jul, each with its
invitation) · **Marketing** (flyer, logo set, all four invite cards, downloadable).
Building graphic redrawn as a 2D building elevation with the address
**99x · 65 Walukarama Road, Colombo**.

## 7. Session agendas detailed + invite design v2 (Asitha, 15 Jul) — ✅ APPLIED 15 Jul

**Ramp-up 1** structured in thirds: 1/3 NorthStar plug + **Gartner agentic-AI
maturity roadmap** (maturity = matched autonomy, not an autonomy race) · 2/3 live
**Xianix** example (xianix.ai, 99x-owned) · 3/3 SWOT + the popular agent-platform
landscape (Copilot Studio, Bedrock AgentCore, Vertex AI Agent Builder, OpenAI,
Agentforce; LangGraph, Claude Agent SDK, CrewAI, AutoGen, LlamaIndex, Pydantic AI).
**Ramp-up 2 panel** seats defined: engineering (shipped agentic solutions),
delivery, senior leadership — discussing projects/challenges already seen.
**Invites v2:** flyer robot extracted as a transparent cutout + four-point
NorthStar + five-arc "5 waves of AI tooling" motif on every card; v1 set parked in
`marketing/invites/v1/` for revert.
