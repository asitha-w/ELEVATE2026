# Research Grounding for Rubric v01

Fresh research pass, 14 Jul 2026. Three sweeps: (A) measuring AI's effect on
delivery, (B) agent autonomy & human-oversight frameworks, (C) agentic maturity
models & judging practice. Every rubric axis traces to at least one source here.

## A. Measuring effectiveness (grounds "effectiveness over complexity" + the surface metrics)

| Source | Key finding we use |
|---|---|
| **DORA State of AI-assisted Software Development 2025** — https://dora.dev/dora-report-2025/ | ~90% of devs use AI; AI adoption lifts throughput but still hurts stability. "AI is an amplifier" — magnifies strong foundations and dysfunction alike. → score downstream outcomes, not tool sophistication. |
| **DORA AI Capabilities Model** — https://dora.dev/ai/capabilities-model/report/ | 7 capabilities that amplify AI benefit, incl. working in small batches, user-centric focus, AI-accessible internal data. → grounding for Partnership/Quality anchors. |
| **SPACE framework** (Forsgren, Storey et al., 2021) — https://queue.acm.org/detail.cfm?id=3454124 | Productivity is multidimensional; surveys are first-class measurements. → legitimizes the Dev Happiness before/after survey. |
| **DX Core 4** (2024) — https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/ | Speed / Effectiveness / Quality / Impact with primary metrics; maps ~1:1 onto Pace, Dev Happiness, Quality, Value. |
| **DX AI Measurement Framework** (2025) — https://getdx.com/blog/introducing-the-ai-measurement-framework/ | Measure AI via utilization → impact → cost; impact read through delivery outcomes, never AI usage stats. |
| **METR RCT** (2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | Experienced devs *believed* +20% with AI, measured −19%. → self-report is unreliable; demand demonstrated before/after ("the METR trap" in L2 axis 1). |
| **GitHub/Accenture Copilot study** — https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/ | Standard measurement pattern: timed task comparison + PR cycle time + confidence survey. |
| **Microsoft CLI coding-agents study** (2026) — https://arxiv.org/abs/2607.01418 | Agentic CLI adopters: ~24% more merged PRs sustained over 4 months; authors caveat merged PRs ≠ value. |
| **Stack Overflow Dev Survey 2025** — https://survey.stackoverflow.co/2025/ai | Trust in AI output fell to 29%; 66% cite "almost right" outputs; 45% say debugging AI code takes longer. → Quality anchor: rework rate on agent output. |
| **MIT/NANDA "GenAI Divide" 2025** — coverage: https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ | ~95% of GenAI pilots show no measurable P&L impact; the 5% embed in real workflows and integrate deeply. → Value anchors. |
| **McKinsey State of AI 2025** — https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | Value correlates with fundamental workflow redesign (high performers 3.6× more likely), not tool bolt-ons. → L2 axis 4. |

## B. Autonomy & the decision gate (grounds L1 axes 2–3, L2 axis 3)

| Source | Key finding we use |
|---|---|
| **Feng, McDonald & Zhang 2025, Levels of Autonomy for AI Agents** — https://arxiv.org/abs/2506.12469 | 5 levels by the human's role: operator → collaborator → consultant → approver → observer. → the L1 autonomy ladder. |
| **Morris et al. (DeepMind), Levels of AGI** — https://arxiv.org/abs/2311.02462 | Autonomy should be *chosen* per context; lower autonomy can be the responsible choice. → "appropriate autonomy, not maximum" (score 5 anchor). |
| **Hugging Face smolagents agency spectrum** — https://huggingface.co/docs/smolagents/en/conceptual_guides/intro_agents | Separates workflows-with-LLM-steps from real agents. → bottom of the ladder + the qualifying "genuinely agentic" check. |
| **Anthropic, Building Effective Agents** (2024) — https://www.anthropic.com/engineering/building-effective-agents | Workflow vs. agent definition; simplest-thing-that-works; agents = higher cost + compounding error. → qualifying check + simplicity principle. |
| **Anthropic, Safe & Trustworthy Agents framework** (2025) — https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents | Read-only by default, approval before mutating actions, tiered earned trust, transparency as precondition of oversight. → gate anchors. |
| **Anthropic, Building Effective Human-Agent Teams** (2026) — https://claude.com/blog/building-effective-human-agent-teams | "Oversight = being positioned to intervene when it matters," trust granted in proportion to demonstrated reliability. |
| **LangChain HITL docs** — https://docs.langchain.com/oss/python/langchain/human-in-the-loop | A real gate is a typed approve/edit/reject pause the agent incorporates — not a console prompt. → gate 4–5 anchor. |
| **Anthropic, Measuring AI Agent Autonomy in Practice** (2026) — https://www.anthropic.com/news/measuring-agent-autonomy | Measurable oversight: human interruption rate, clarification-request rate, uninterrupted-run duration. → L2 "state your oversight numbers". |
| **tau-bench / tau²-bench** — https://arxiv.org/abs/2406.12045 | pass^k consistency collapse (60% pass@1 → 25% pass@8). → Evidence anchor: repeated runs beat one lucky take. |

## C. Maturity & judging practice (grounds L2 + mechanics)

| Source | Key finding we use |
|---|---|
| **AWS AI-DLC** — https://agentic-ai.readthedocs.io/en/latest/Standards/aidlc/ | Bolts not sprints; humans validate every AI-proposed plan; defines *no* evaluation threshold — our rubric fills that gap. (Also the event's conceptual base.) |
| **AWS Well-Architected Agentic AI Lens** — https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf01-bp01.html | Success criteria defined up front; eval signals incl. task completion, tool-use accuracy, cost per completion. |
| **Gartner, 40%+ of agentic projects canceled by 2027** (2025) — https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | Top failure causes: unclear business value, escalating cost, weak risk controls; "agent washing." → L2 customer-readiness axis + qualifying check. |
| **Microsoft Agentic AI Adoption Maturity Model** — https://learn.microsoft.com/en-us/agents/adoption-maturity-model/ | What moves a demo up-level is repeatability + governance, not features. → L2 axis 4. |
| **Deloitte Tech Trends 2026** — https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html | Only ~11% of agentic initiatives reach production. → the pilot→production chasm L2 tests for. |
| **LangChain State of Agent Engineering** — https://www.langchain.com/state-of-agent-engineering | 89% have observability, only ~52% run evals — teams watch failures but can't catch regressions. |
| **Microsoft AI Agents Hackathon 2025 rules** — https://microsoft.github.io/AI_Agents_Hackathon/rules/ | 5 equal axes at 20% incl. human-in-the-loop under usability; ties broken by fresh judges on same criteria. |
| **HackMIT / Gavel judging research** — https://anishathalye.com/designing-a-better-judging-system/ | Absolute scores fail when each judge sees a slice: score drift, order effects. Fix: comparative ranking within what one judge saw, or per-judge normalization. → rank-within-flow rule; absolute scoring reserved for the pitch round where all judges see all 8. |

## The four load-bearing conclusions

1. **Score measured project deltas, never agent architecture** (DORA, DX, McKinsey, MIT).
2. **Demand demonstrated before/after — self-report is systematically wrong** (METR).
3. **Autonomy axis = the human's role; gate axis = handoff-packet quality; top score = autonomy matched to risk** (Feng et al., Morris et al., Anthropic, LangChain).
4. **Rank within a flow, never across; absolute scores only when every judge sees every team** (Gavel/HackMIT).
