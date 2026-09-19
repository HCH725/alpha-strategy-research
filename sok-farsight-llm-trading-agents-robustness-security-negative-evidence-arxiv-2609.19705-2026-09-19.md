---
schema: strategy-research-record-v1
title: "SoK FARSIGHT Negative Evidence: Academic Financial LLM Trading Schemes Fail Robustness and Security Gates"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - negative-evidence
  - falsification
  - llm-trading-agents
  - sok
  - robustness
  - security
  - flash-crash
  - adversarial
  - research-boundary
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - "Mengxiao Wang and Nitesh Saxena, 'SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes', arXiv:2609.19705v1 [cs.CR, cs.AI, cs.MA], September 17, 2026. https://arxiv.org/abs/2609.19705"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SoK FARSIGHT Negative Evidence: Academic Financial LLM Trading Schemes Fail Robustness and Security Gates

## Provenance

- **Source**: arXiv:2609.19705v1 [cs.CR; cs.AI; cs.MA]
- **Authors**: Mengxiao Wang, Nitesh Saxena
- **Version**: v1, submitted September 17, 2026
- **DOI**: https://doi.org/10.48550/arXiv.2609.19705
- **URL**: https://arxiv.org/abs/2609.19705
- **Format**: 24 pages, 6 figures, 11 tables, 118 references; SoK paper
- **Framework name (source)**: FARSIGHT — Financial Agent Robustness and Security Investigation and Global Holistic Testing
- **Evaluated set (source)**: **15** representative academic financial LLM trading-agent schemes
- **Review scope this cycle**: abstract and arXiv metadata only (PDF-only submission; HTML not available at review time). Scheme names, per-scheme scores, and metric definitions beyond the abstract are **not restated here** and must be read from the PDF before any scheme-specific claim.

### Repository Deduplication Audit

Repository-wide search on 2026-09-19 found **zero** prior records citing `arXiv:2609.19705`, Wang/Saxena, FARSIGHT, or this SoK. Adjacent records capture **individual** LLM/agent trading hypotheses as research-proposed material (for example LLM news/sentiment, multi-agent alpha discovery, strategy-discovery leakage audits, self-improving agents). This record is **cross-cutting negative evidence** about the academic LLM-trading-agent family, not a new trading rule and not a paraphrase of any single-scheme capture.

## Economic mechanism

### Source-reported

The paper frames autonomous LLM trading agents as a **high-stakes agentic security** case: a compromised or miscalibrated agent has direct execution authority over real capital in an adversarial, reflexive market. Existing agentic-AI security work is described as largely domain-agnostic and blind to this attack surface.

FARSIGHT evaluates schemes on two axes (source):

1. **Robustness under market turbulence**, including flash-crash-like scenarios.
2. **Security** against three attack classes: (i) attacks on information sources, (ii) attacks on agents, (iii) agent-as-attacker behaviors.

Headline quantitative findings (source abstract):

- **80%** of the 15 evaluated academic schemes **fail at least one core robustness metric**.
- **100%** exhibit **security vulnerabilities**.
- The authors argue the two failure modes are **inseparable**: a small misjudgment can cascade into a market-wide crash on its own, while an adversary can deliberately trigger the same collapse at minimal cost.

### Research interpretation

This record does **not** claim that every LLM trading idea in this repository is worthless. It records that, under an external SoK evaluation of academic schemes, **most lacked robustness gates and all showed security holes**. The economic implication for research staging is about **adoption and implementation risk**, not about discovering a new alpha:

> Academic LLM trading-agent presentations that report backtest or paper metrics without explicit turbulence robustness tests and adversarial threat models are, on this evidence, insufficient grounds for moving beyond `research-only` / `not-implemented`.

Crypto portability of the **security claim** is plausible (agents trading crypto perps also hold execution authority; markets are adversarial and reflexive) but **not source-proven** for a crypto-only universe in the abstract reviewed.

## Signal

**Not a trading signal.** This SoK is an evaluation/falsification artifact for the LLM-trading-agent family.

### Formation timestamp / lookback / entry / exit / holding period / parameters

Not applicable as an executable strategy. Source-reported evaluation objects are scheme-level robustness metrics and three security attack classes; exact metric formulas, turbulence scenario definitions, and per-scheme parameter grids are **underspecified in the abstract** and require the PDF body.

`research-proposed` governance mapping (not source-reported as a trading rule):

- Any future implementation proposal that depends on an LLM/agent execution loop must pre-register: (1) turbulence/flash-crash robustness tests, (2) information-source integrity checks, (3) agent-compromise and agent-as-attacker tests, and (4) a fail-closed kill path when any gate fails.
- `research-defined falsification threshold` for **adoption readiness** of an LLM-agent design: if the design cannot demonstrate non-failure on pre-registered robustness gates comparable in spirit to FARSIGHT’s turbulence tests, **reject** advancement beyond research capture. This threshold is MiMo research-defined, not an author trading cutoff.

## Required data

Not applicable as a strategy. For **replication of the SoK** (not performed here):

- **Instrument/universe**: 15 named academic financial LLM trading schemes (names in the source PDF).
- **Data**: scheme implementations/papers plus whatever market data each scheme uses; turbulence and adversarial scenarios constructed by FARSIGHT.
- **Fields**: robustness metric outputs; security vulnerability outcomes under the three attack classes.
- **Point-in-time**: not specified in the abstract; evaluation is scheme-level, not a live PIT trading dataset.

## Execution assumptions

Not applicable. The source evaluates **academic scheme designs**, not a live execution stack. No claim is made that any named production bot fails these tests unless the source PDF says so for that bot.

## Evidence

### Source-reported

- SoK paper arXiv:2609.19705v1 (2026-09-17), 24 pages, evaluates **15** academic financial LLM trading-agent schemes.
- Framework: **FARSIGHT**, two axes — robustness under market turbulence (including flash-crash-like scenarios) and security under three attack types (information sources, agents, agent-as-attacker).
- **80%** fail at least one core robustness metric.
- **100%** exhibit security vulnerabilities.
- Authors: robustness and security failures are inseparable; adversary can trigger crash-like collapse at minimal cost once agents share fragile decision patterns.
- Comments field: “SoK paper. Evaluates 15 academic financial LLM trading agent schemes on robustness and security.”

### Independently reproduced

`not independently reproduced`

### Negative evidence

This record **is** negative evidence for the academic LLM-trading-agent family:

1. **Family-level robustness gap**: majority fail at least one core robustness metric under turbulence/flash-crash-like stress (source).
2. **Family-level security gap**: all evaluated schemes show security vulnerabilities (source).
3. **Cascade coupling**: small model error and adversarial exploitation can produce the same crash-like outcome (source interpretation of joint failure).
4. **Abstract-level limits**: no HTML body; exact metrics, scheme list, and crypto-only stratification not re-audited this cycle — treat percentages as source-reported, not independently verified.
5. Relation to this repo: many captures here are **single-scheme research hypotheses**. This SoK does not refute each capture’s mechanism description; it **strengthens the implementation/adoption boundary** that those records already claim (`not-implemented` / `not-approved`).

## Falsification

Research-proposed falsification / gate tests for anyone proposing LLM-agent deployment beyond research staging:

1. **Turbulence gate.** Pre-register flash-crash-like and high-volatility scenarios on the target market (crypto perps allowed). **Research-defined falsification threshold:** reject the agent design if any core robustness metric fails on the pre-registered scenario set.
2. **Information-source integrity.** Corrupt or delay news/API/social inputs. Fail if the agent’s positions move in a direction that systematically benefits the corrupted input without a detectable anomaly flag.
3. **Agent compromise.** Simulate tool/API key theft or prompt injection with execution rights. Fail if the agent can drain or flip risk beyond a pre-registered cap.
4. **Agent-as-attacker.** Test whether the agent, when instructed adversarially, can be induced to wash/spoof/cascade-trade in ways that would be market-abusive. Fail if yes without hard policy blocks.
5. **Scheme-level replication.** If a paper’s scheme is claimed crypto-portable, re-run FARSIGHT-style gates on crypto data. Fail the portability claim if robustness/security failures replicate.
6. **Compare to non-LLM baselines.** Fail the “LLM adds value” claim if a simple rules baseline matches net performance **and** has strictly better robustness/security under the same gates.
7. **PDF body audit.** Before citing scheme-specific numbers, read arXiv:2609.19705 PDF; fail closed on any record that would require body-level metrics not present in the abstract.

## Crypto portability

- **Negative-evidence portability: adapted / unproven.** The SoK’s domain is “financial trading agents” generally. Crypto agents share execution authority, 24/7 adversarial venues, and reflexive feedback; the **risk narrative** ports directly.
- **Not proven** that the 15 schemes are crypto-specific or that the 80%/100% rates hold on a crypto-only sample — do not overclaim.
- Spot vs perpetual vs options: any future crypto agent gate must specify instrument, leverage, funding, and venue.
- Crypto portability of this negative evidence is **not** authorization to trade or to dismiss all crypto LLM research captures.

## Limitations

- Abstract-only review; PDF body (scheme identities, metric definitions, tables) not ingested this cycle.
- Percentages are source-reported for a **15-scheme academic sample**, not a census of production bots.
- No independent reproduction of FARSIGHT runs.
- Not a strategy record: no entry/exit edge is claimed.
- Existing repo LLM-agent records remain valid as **research captures**; this record constrains **adoption language**, not the existence of those captures.
- Incremental-write threshold: **met** via new family-level negative evidence (robustness/security failure rates) that materially strengthens the research-only boundary for LLM trading agents.

## Implementation status

`not-implemented`

No FARSIGHT harness, no agent-security testbed, and no LLM trading runtime change exist in this research stack. This record does not modify NautilusTrader or authorize any Paper/Testnet/Live path.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of LLM-agent research records in this repository remains **research-only**. This SoK is additional reason not to treat academic LLM-trading demos as implementation-ready.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical schema
- `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` — methodology audit for LLM strategy search (related governance, different artifact)
- `llm-agent-population-scale-behavioral-null-volatility-blind-sizing-2026-09-10.md` — behavioral null / sizing issues for agent populations
- Other `llm-*` / `*-agentic-*` / `webcryptoagent-*` records — individual research hypotheses; this SoK is family-level negative evidence, not a duplicate rule
- `crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01.md` — adjacent adversarial/null evidence family for retail systematic claims

## Sources

1. Mengxiao Wang and Nitesh Saxena. "SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes." arXiv:2609.19705v1 [cs.CR], September 17, 2026. https://arxiv.org/abs/2609.19705
2. arXiv metadata/abstract reviewed 2026-09-19; PDF body not re-read this cycle.
