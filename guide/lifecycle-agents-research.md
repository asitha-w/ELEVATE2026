# Lifecycle agents — the research behind the Extended Guide

**Question:** which AI agents have software teams *actually* incorporated into the development
lifecycle as of mid-2026 — at which stage, owning what job, gated how, and with what evidence of
real production adoption?

**Method:** five parallel research angles (construction · review/quality · requirements/design ·
deployment/dependencies/migration · operations) ran web search + source fetching and extracted
falsifiable claims. Every claim then faced **two independent adversarial verifiers** instructed to
refute it — by fetching the cited sources and checking that (a) the source actually says it,
(b) the evidence grade is honest, (c) the tool belongs at the claimed stage, and (d) "ownership"
isn't dressed-up assistance. **37 raw claims → 21 survived, 15 killed.** Evidence grades:
**measured** (numbers from a survey/study/engineering blog) > **documented** (credible qualitative
account of production use) > **vendor-claim** (only the vendor says so).

The Extended Guide tab distills this file. Where the tab says "vendor-reported," this file is why.

---

## The headline findings

1. **Ownership is real but narrow.** Agents genuinely own jobs today at: first-pass code review,
   E2E-suite maintenance, issue-to-PR construction, backlog grooming, dependency updates,
   first-response incident investigation, first-line support resolution, and feedback mining.
2. **Deployment is the human stage — measured, not assumed.** Stack Overflow 2025: **76% of
   developers don't plan to use AI for deployment/monitoring** — the most-resisted category.
   DORA 2025: AI adoption correlates with **faster throughput AND more instability/rework**
   ("AI is an amplifier"). Teams keep the release call human even where AI writes most of the code.
3. **The gate is universal.** Every surviving claim has a human decision gate: the PR, the merge
   block, the spec approval, the escalation, the roadmap call. No surviving claim describes
   unattended production ownership without one.
4. **Adoption is thinner than the vendor narrative.** Stack Overflow 2025: only **30.9%** of
   developers use agents regularly; **37.9% have no plans to**. DORA 2025: **61%** of respondents
   (June–July 2025) had never interacted with agentic workflows, and **<10% of week-1 agent users
   were still using them 10 weeks later**. Being early is normal; two focused weeks is a real
   catch-up window.
5. **"Assistance rebranded as ownership" is the most common overclaim.** The verifiers killed
   more claims for this than for anything else (see the kill list).

---

## Stage by stage — verified claims

### Requirement

- **Ticket triage & workflow actions — Atlassian Rovo agents in Jira** *(vendor-claim, at scale)*.
  Agents are assigned tickets, act on comment mentions, and execute workflow steps; every action
  logged. Vendor-reported scale: 5M MAU, used by 90%+ of Atlassian enterprise cloud customers,
  ~2.4M automated workflow actions across customers in six months, 14M+ assisted actions in May
  2026 alone. Verifiers cross-checked figures against SEC 8-K shareholder letters and community
  docs — numbers corroborated but all vendor-originated.
  **Gate:** human assigns/mentions; admins govern scope; audit log.
  [deviniti.com — Atlassian AI statistics](https://deviniti.com/blog/enterprise-software/38-atlassian-ai-statistics-for-2026-rovo-atlassian-intelligence-adoption/) ·
  [SiliconAngle — Rovo agentic execution, Team '26](https://siliconangle.com/2026/05/06/atlassian-opens-teamwork-graph-pushes-rovo-agentic-execution-team-26/)

- **Spec drafting — AWS Kiro** *(vendor-claim, CONTESTED)*. Kiro drafts structured specs
  (requirements.md / design.md / tasks.md) that humans approve before build. **Verifier caveat:**
  in AWS's own flagship case study the humans wrote the specs and Kiro generated ~95% of the code —
  i.e. the evidence shows spec-*driven* code generation, not agent-drafted specs. Treat spec
  drafting as emerging, not established.
  [AWS — three-week drug discovery agent using Kiro](https://aws.amazon.com/blogs/industries/from-spec-to-production-a-three-week-drug-discovery-agent-using-kiro/) ·
  [kiro.dev/docs/specs](https://kiro.dev/docs/specs/)

- **Reality check** *(documented, CONTESTED on specificity)*: DORA 2025 — 61% had never touched
  agentic workflows; <10% ten-week retention among triers. Requirement/solutioning agents are the
  thinnest slice of that. [dora.dev/dora-report-2025](https://dora.dev/dora-report-2025/)

### Solutioning

- **Backlog grooming & duplicate hunting** *(MEASURED — the strongest non-vendor number in this
  file; contested only on "prototype vs product")*. Empirical study, five senior PM/test managers
  (10–20+ yrs) at two Nordic IT consultancies, GPT-4o + vector-embedding duplicate detection on a
  30-issue backlog: **12–21 duplicates found vs 7–12 manually, 100% precision, 45% less time per
  duplicate (2:54 → 1:35), satisfaction 2–4/10 → 7–9/10**. Nothing changes in Jira without
  per-suggestion human confirmation. Verifier confirmed every figure against the paper; note it is
  a research prototype, not a shipping product.
  [arXiv 2507.10753 — GenAI-Enabled Backlog Grooming](https://arxiv.org/html/2507.10753v1)

- **Estimation — nobody owns it** *(vendor-claim, included to flag the gap)*. Marketplace
  estimation apps have negligible traction (one had 3 installs); practitioners instead report
  estimation getting *harder* once AI acceleration breaks velocity assumptions.
  [Scrum.org forum thread](https://www.scrum.org/forum/scrum-forum/94752/how-approach-story-point-estimation-advent-ai-dev-acceleration-tools)

### Construction

- **In-session agentic coding — Claude Code** *(vendor-claim: Anthropic's own telemetry, but
  corroborated verbatim by both verifiers)*. ~400,000 real sessions (Oct 2025–Apr 2026): humans
  keep **~70% of planning decisions**, the agent carries **~80% of execution**; 56% of session
  activity is writing/fixing/testing code; intermediate-or-higher-expertise operators verify-succeed
  at 28–33% vs 15% for novices — *steering skill is the effective gate*.
  [anthropic.com/research/claude-code-expertise](https://www.anthropic.com/research/claude-code-expertise)

- **Async issue-to-PR agents** *(documented)*. GitHub Copilot coding agent, Cursor background
  agents, OpenAI Codex, Claude Code remote tasks: assigned a ticket, work unattended in a sandbox,
  hand back a PR. GitHub docs confirm the mechanism (ephemeral Actions sandbox, ~59-min session
  cap). **No agent auto-merges its own work by default — the PR is the gate.** Verifier softened
  one overclaim: sources do not support "mainstream working pattern."
  [GitHub docs — about the coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent) ·
  [Security Boulevard — 6 background AI agents](https://securityboulevard.com/2026/06/6-background-ai-agents-for-async-development/)

- **Assist-level already moves merge metrics — Accenture RCT** *(MEASURED)*. ~450 developers vs
  200-developer control: **+8.69% PRs/dev, +15% PR merge rate, +84% successful builds**; rollout
  since expanded past 12,000 developers. (Survey-based 90%/91% adoption figures are self-report;
  the RCT deltas are the measured part.)
  [github.blog — Copilot × Accenture research](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/)

- **Reality check** *(documented)*. Stack Overflow 2025 (agents = "autonomous, minimal human
  intervention"): 30.9% regular agent use, 37.9% no plans, 87% concerned about accuracy, 81% about
  security/privacy; only 17.1% of agent users see team-wide benefit vs ~69% personal gains.
  [survey.stackoverflow.co/2025/ai](https://survey.stackoverflow.co/2025/ai/)

- **Benchmark hype flag** *(vendor-claim, CONTESTED)*: GPT-5-Codex "85.5% SWE-bench Verified"
  circulates in secondary press; independent figures cluster ~74.5–74.9%. Benchmarks ≠ deployed
  practice; excluded from the tab.

### Quality

- **First-pass code review at scale — Cloudflare (in-house, GitLab-integrated)** *(vendor-claim,
  but an engineering-blog account with unusually complete numbers, verified verbatim)*. First 30
  days in production: **131,246 review runs · 48,095 MRs · 5,169 repos · 0.6% human-override
  ("break glass") rate · median review 3m39s · ~$0.98/review**. Tiered gate: advisory comments
  flow; multiple risk warnings or any critical finding **blocks merge** until a logged human
  override. [blog.cloudflare.com/ai-code-review](https://blog.cloudflare.com/ai-code-review/)

- **Review agents as the common agentic entry point** *(documented, CONTESTED)*. Copilot code
  review, CodeRabbit, Cursor Bugbot are the widely-cited production reviewers. **Verifier
  correction:** DORA 2025's survey-measured top AI use is *writing new code* (71%) — "review
  dominates agentic use" traces to the report author's interview, not survey data. Both verifiers
  agree human review stays mandatory ("more critical, not obsolete"); 30% of developers report
  little/no trust in AI code. [dora.dev/dora-report-2025](https://dora.dev/dora-report-2025/)

- **AI-written code gets its own gates** *(vendor-claim/practice pattern)*. Convergent 2026
  guidance: treat AI-assisted PRs as a distinct path — non-bypassable CI checks (SAST,
  secret/dependency scanning), named-owner sign-off for exceptions; AI review verdict = necessary,
  never sufficient.
  [Codacy — AI code review is not enough](https://blog.codacy.com/ai-code-review-is-not-enough-how-engineering-leaders-should-gate-ai-generated-code)

- **E2E regression suite, owned — QA Wolf** *(documented)*. Managed AI+human service creates AND
  maintains the Playwright suite — flake triage included; customer team reviews coverage and gates
  releases on pass/fail. USD 5–20k+/month — ownership of quality infrastructure as a service.
  [QA Wolf 2026 review](https://qaskills.sh/blog/qa-wolf-ai-testing-guide-2026)

### Deployment

- **The release call stays human — measured resistance** *(documented)*. Stack Overflow 2025:
  **76% don't plan to use AI for deployment/monitoring** — highest resistance of any task
  category; trust in AI output fell to 29% (−11pts YoY).
  [survey.stackoverflow.co/2025/ai](https://survey.stackoverflow.co/2025/ai/)

- **Throughput up, stability down — DORA 2025** *(documented)*. 90% use AI; adoption correlates
  with faster delivery AND more change failures/rework — "amplifier, not owner." Testing/review/QA
  is the bottleneck AI-accelerated code exposes.
  [dora.dev/dora-report-2025](https://dora.dev/dora-report-2025/) ·
  [Google Cloud announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)

- **Dependency updates & auto-merge** *(documented — reinstated after citation repair)*. The
  original claim died because it cited a Mend marketing page; the verifier explicitly confirmed
  the mechanism via GitHub's own docs: Renovate/Dependabot detect, PR, and **auto-merge behind
  branch protection** (`gh pr merge --auto`, required checks). The policy — which checks must
  pass, which update types may self-merge — is the human gate.
  [GitHub docs — auto-merge & branch protection](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) ·
  [Renovate docs — automerge](https://docs.renovatebot.com/key-concepts/automerge/)

### Operations — incident response

- **First-response investigation — incident.io AI SRE** *(vendor-claim, CONTESTED on a fabricated
  citation, mechanism confirmed)*. On incident fire: parallel diagnostic searches, hypothesis
  formation, written findings report in Slack within ~1–2 minutes. Agent never closes incidents or
  pushes fixes — the responding engineer owns the diagnosis call. **Verifier note:** the "48-min
  MTTR breakdown / 80% cut" figures could not be located in the cited sources; use the mechanism,
  not the numbers. [incident.io — what is an AI SRE agent](https://incident.io/blog/ai-sre-agent-definition)

### Operations — support

- **First-line resolution — Intercom Fin** *(vendor-claim)*. Fin answers, resolves, and closes
  conversations end-to-end, billing per resolution; escalates the rest. Vendor-reported: case-study
  resolution 42–50%, platform rolling ~67% (Dec 2025), 40M+ resolved conversations, Sharesies 70%
  at 12 weeks. [Intercom — Fin outcomes](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)

- **First-line resolution — Decagon** *(vendor-claim)*. Substack 90%+ auto-resolution, Notion −34%
  resolution time, Rippling deflection 38%→50%+, NG.CASH 13%→70%. Verifiers confirmed the case
  studies say this — and also confirmed independent analysis of a **30–40-point gap between vendor
  marketing figures and cross-program medians**. Configure eligibility per ticket category; humans
  take escalations. [Decagon case studies](https://decagon.ai/case-studies/notion)

### Operations — feedback

- **Feedback mining — Enterpret** *(vendor-claim, CONTESTED as all-vendor-sourced)*. Ingests and
  categorizes feedback across 50+ channels; Notion's monthly insights report went **2 weeks →
  3 days** and justified staffing a login-fix team; Canva surfaces insights in days. Product
  leadership makes every roadmap call. [Enterpret × Notion](https://www.enterpret.com/customers/notion)

### Operations — monitoring

- **Still early, policy-first** *(documented)*. DORA 2025: unattended ops-agent triage remains
  early-stage; some orgs saw customer-facing incidents double alongside AI adoption — leadership
  is setting explicit AI stance/policy before delegating ops jobs.
  [dora.dev/dora-report-2025](https://dora.dev/dora-report-2025/)

---

## The kill list — 15 claims that did not survive, and why it matters

**Bucket 1 — assistance dressed up as ownership** (the finding: the human gate is not optional):

- *Amazon Q Code Transformation "owns migrations end-to-end"* — AWS's own blog: a "remaining
  portion" needs manual work; one insurance case auto-completed only 36%.
- *Google internal LLM migration tooling "owns migrations"* — the paper's real numbers (39
  migrations/12 months, 74% of edits LLM-generated, ~50% estimated time saved) explicitly frame it
  as "aiding developers"; humans direct which files change.
- *Devin "owned" Nubank's ETL migration* — Nubank's post says Devin automated repetitive
  refactoring within a human-managed program (12× efficiency claim is real but is assistance).
- *CI-failure auto-fix agents "own the loop until green"* — they push fixes to a separate branch /
  new PR for human merge; explicitly not self-merging.
- *PagerDuty agents "run major-incident coordination end-to-end"* — cited coverage says the agents
  assist teams, in so many words.

**Bucket 2 — citation integrity** (practice may be real; the specific evidence was miscited —
reinstate only with correct sources, as done for Renovate above):

- CodeRabbit adoption stats, Graphite Diamond "500k PRs", Datadog Bits figures (Nulab/70% MTTR),
  Cleric×BlaBlaCar capacity figure, Meticulous+Applitools pairing claim, release-notes-agent
  stats, mabl/Gartner forecast, ADR-drafting practice account (source real, stats grafted from
  elsewhere).

**Honesty rule for the tab:** mechanisms from these tools may be described only with correctly
attributed sources; the killed numbers stay out.

---

## What this means for the Extended Guide

1. Ten embed points across the strip carry verified content; deployment carries an honest
   "the release call stays human" panel instead of a pretend card — it echoes the event's own
   line: *agents deliver, you decide*.
2. Every card states the gate, because every surviving claim has one.
3. Evidence language on the tab mirrors the grades here: "measured" / "documented" /
   "vendor-reported" — the same honesty the proof ladder demands of teams.
4. The adoption reality-checks (61% never tried agents; <10% ten-week retention) belong on the
   tab as encouragement: the median team hasn't done this yet; two weeks of focused work is a
   genuine catch-up window, not a losing race.

*Compiled 20 Jul 2026. Fan-out research: 5 angles / 37 raw claims; adversarial verification:
2 refuters per claim, kill on double-refute; 21 survived. Companion to
`rubric/version-01/research-grounding.md`.*
