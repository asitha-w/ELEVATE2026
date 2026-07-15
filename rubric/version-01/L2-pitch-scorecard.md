# Level 2 — Pitch Scorecard (panel, whole company watching) · v01 DRAFT

**Purpose:** prove the solution is an **offering** — something 99x can put in front
of the real customer with a straight face.
**Who:** the full panel; every judge sees all 8 finalists, so absolute scoring is
safe here (unlike the floor round, which ranks within a floor).
**Output:** ~3 winners; the panel also lists every entry recommended to the 99x
expert panel → customer as a real offering (the list can exceed 3).
**Format:** fresh scores — floor scores do NOT carry into L2 (they feed the pillar
awards only). 5 min pitch + 2 Q&A.

The floor round already proved the agent is real. The pitch round asks a harder
question: **is this a product, or a demo?** Deloitte's funnel says only ~11% of
agentic initiatives ever reach production; Gartner predicts 40%+ get canceled,
with *unclear business value* as the top killer. These four steps test exactly the
things that kill agentic projects after the applause dies down.

## The four steps (0–5 each, equal weight → max 20)

The universal scale applies: **0–1 a claim** · **2–3 a demonstration** ·
**4–5 a measurement**.

### Step 1 — The Number
*One honest before/after on the declared pillar.*

**What it measures:** whether the elevation is real or felt. Builders cannot feel
their own speedup — in the METR randomized trial, experienced developers *believed*
AI made them 20% faster while it measurably made them 19% slower. So testimony
("it feels much faster now") scores as a claim. What scores high is a number with
a baseline: what the task/metric was before, what it is with the agent, and how
the team measured both.

**The Q&A test:** the number survives "how did you measure that?" — the team can
name the task, the baseline, the sample, and what the measurement misses.

| Score | Anchor |
|---|---|
| 0–1 | Vibes; self-reported speedup with no measurement |
| 2–3 | A real number with a rough baseline; honest about what it misses |
| 4–5 | Clean before/after on the real project; the method survives Q&A |

### Step 2 — The Offering *(was "The Customer" — renamed, see v1-improvements #2)*
*Would this customer adopt it and pay for it — as a product, not a demo?*

**What it measures:** every team has a customer by construction — that scores
nothing. This step measures the distance between "we have a customer" and "our
customer would run this on Monday": (a) a **named user** inside the customer — not
"Skanska" but the person whose Monday changes; (b) the **workflow it lands in** —
embedded in how the customer already works, not asking them to change behavior
first (MIT 2025: the ~5% of GenAI pilots that create value are the embedded ones);
(c) **unit economics** — what one run costs (tokens, infra, human review time) vs.
what one run is worth; (d) the **honest gap list** — what's missing before 99x can
sell this, and how big that gap is.

**The Q&A test:** "if the customer says yes tomorrow, what must you build first,
and what does a month of running it cost?"

| Score | Anchor |
|---|---|
| 0–1 | A demo with no named user, no workflow, no cost story |
| 2–3 | Named user & workflow; rough cost-to-run; honest gap list |
| 4–5 | Named user + workflow + unit economics + credible path past pilot — 99x could scope the offering from this pitch |

### Step 3 — The Stress Test
*Break it on purpose — does the gate hold?*

**What it measures:** trustworthy autonomy. No agent never fails; a trustworthy
system is one where failure is *caught*. Two layers:

- **Demonstrated (scored on the anchors):** the team deliberately feeds their agent
  a case it gets wrong, live or recorded, and shows the human gate catching it —
  ideally the human rejects/edits and the agent incorporates the correction.
- **Probed (judges' Q&A):** judges push at the edges the team hasn't handled —
  ambiguous inputs, 10× volume, a week of rubber-stamped approvals. Scored on how
  the team *reasons about its boundary*: **"it can't break" is a red flag; "it
  breaks at X, the blast radius is Y, the gate contains it because Z" is a top
  answer** — even if X is unhandled.

| Score | Anchor |
|---|---|
| 0–1 | No failure shown, or the gate is a confirm-click; "it can't break" |
| 2–3 | Failure demonstrated; human catches it, recovery is manual |
| 4–5 | Human rejects/edits, agent incorporates it; team knows its boundary and can state oversight numbers (e.g. intervention rate, cost of a missed catch) |

### Step 4 — Beyond the Demo
*Does this change how the project works — and could other 99x teams repeat it?*

**What it measures:** whether the agent changed the *system of work* or sits beside
it. McKinsey's data: value correlates with workflow redesign, not tool bolt-ons —
high performers are 3.6× more likely to have redesigned the workflow. The tell:
the team can name **what they stopped doing**. And because winners become 99x
offerings, the pattern must be repeatable — the pitch should let another 99x team
see how they'd adopt it on a different project.

**The Q&A test:** "what did you stop doing?" and "what would team X on project Y
need to change to run this?"

| Score | Anchor |
|---|---|
| 0–1 | A bolt-on tool beside the real workflow; nothing stopped |
| 2–3 | The workflow actually changed; the team can say what they stopped doing |
| 4–5 | Workflow redesigned around the agent + the pattern is transferable — another 99x team could adopt it from this pitch |

## Q&A prompts for the panel (2 questions per team)

- Why does this need to be an agent — what would the simple version miss?
- What does one run cost, and what is one run worth?
- How did you measure that number — and what does it miss?
- What happens when the input is *ambiguous*, not wrong?
- What breaks first at 10× usage, and who notices?
- What ships if the human rubber-stamps approvals for a week?
- Which failure would you *not* catch?
- What did the floor crew challenge, and what changed since?
- If the customer says yes tomorrow, what must you build first?

## Deliberation

1. Sum scores → provisional ranking of 8.
2. Panel deliberates as one — ties broken on **The Stress Test** (the event's
   thesis), then panel vote.
3. Select ~3 winners; separately list every entry recommended to the 99x expert
   panel as a customer offering (can exceed 3).
4. Award the four pillar prizes from banked floor scores (Best Pace / Quality /
   Value / Dev Happiness).
