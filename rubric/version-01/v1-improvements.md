# v1 Improvements — tuning notes for the next revision

Running list of changes agreed while tuning v01 with the team. Items here are
**pending** — applied to the mds/graphics in batches, then re-rendered.

## 1. Team pod: drop the dedicated demo screen (Asitha, 14 Jul)

Teams don't need a separate demo screen at the pod — **showing the run on one
laptop screen is enough**. The bar stays the same: any judge, any lap, "run it
now" should be a 30-second ask. Update `team-area` graphic (remove the DEMO
SCREEN element, reposition the callout to a laptop) and the pod checklist
("demo screen live" → "demo laptop ready").

## 2. L2 "The Customer" — clarify what it actually measures (discussion, 14 Jul)

Every team *has* a customer by construction (they're project teams) — so the axis
must not read as "do you have a customer?". What it measures is **offering
readiness**: would *this specific customer* adopt and pay for this as a product,
not a hackathon demo. Candidate rename: **"The Offering"**. Scored substance
stays: named user + workflow it lands in, cost-to-run vs value-per-run (unit
economics), honest gap list, credible path past pilot.

## 3. L2 "The Stress Test" — judge guidance on edge-case probing (discussion, 14 Jul)

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
