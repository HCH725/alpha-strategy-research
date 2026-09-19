---
schema: strategy-research-record-v1
title: "StableEval Arena: Agentic Stablecoin Peg-Risk Benchmark Negative Evidence (arXiv 2609.18949)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - stablecoin
  - peg-risk
  - agentic-ai
  - benchmark
  - negative-evidence
  - llm
status: research-only
confidence: medium
source_as_of: 2026-08-07
sources:
  - "Sean Wan, Dongping Liu, and Luyao Zhang, 'StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction', arXiv:2609.18949v1 [cs.LG], August 7, 2026. https://arxiv.org/abs/2609.18949"
  - "Benchmark dataset (source-reported release): https://huggingface.co/datasets/SeanWan05/stableeval-arena"
  - "Benchmark code (source-reported release): https://github.com/StableTradeAtlas/StableEval-Arena (full commit SHA not captured this cycle)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# StableEval Arena: Agentic Stablecoin Peg-Risk Benchmark Negative Evidence (arXiv 2609.18949)

## Provenance

- **Source**: arXiv:2609.18949v1 [cs.LG]
- **Authors**: Sean Wan (Duke Kunshan University), Dongping Liu (Tenorshare), Luyao Zhang (Duke Kunshan University)
- **Submitted**: 2026-08-07
- **Venue note (HTML)**: KDD Workshop on Evaluation and Trustworthiness of Agentic AI; August 2026; Jeju, Korea
- **DOI**: https://doi.org/10.48550/arXiv.2609.18949
- **URL**: https://arxiv.org/abs/2609.18949
- **HTML reviewed 2026-09-20**: https://arxiv.org/html/2609.18949v1 (abstract + §1 Introduction with release URLs and qualitative results; full experiment tables not fully rendered/audited this cycle)
- **Source-reported public artifacts**:
  - Hugging Face dataset: https://huggingface.co/datasets/SeanWan05/stableeval-arena
  - GitHub code: https://github.com/StableTradeAtlas/StableEval-Arena — **full commit SHA not preserved this cycle** (`data gap` per GitHub provenance rule)
- **Review scope this cycle**: abstract + introduction HTML; six-agent configuration table and per-metric numeric leaderboards not restated beyond qualitative direction in intro.
- **Deduplication audit (2026-09-20)**: Repository-wide search found **zero** prior records citing `arXiv:2609.18949`, StableEval Arena, or these HF/GitHub artifact URLs. Adjacent records are different:
  - `autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19.md` — strategy/system capture on stablecoin flow/carry; not a peg-risk **benchmark** of agentic systems.
  - `sok-farsight-llm-trading-agents-robustness-security-negative-evidence-arxiv-2609.19705-2026-09-19.md` — security/robustness SoK of LLM **trading agents**; different evaluation target (attack/robustness vs peg-stress diagnosis).
  - `look-ahead-bias-pretrained-financial-forecasting-pit-vintage-arxiv-2609.20554-2026-09-19.md` — foundation-model **forecast vintage** methodology; not stablecoin peg labels.
  - Prediction-market / Polymarket / Kalshi records — market mechanisms, not agent peg-risk evaluation.

## Economic mechanism

### Source-reported

Source-reported problem: stablecoins underpin trading, lending, payments, collateral, liquidity, and settlement; utility depends on remaining near one U.S. dollar. Peg failure risks pricing errors, liquidity stress, payment failure, and settlement uncertainty. Stablecoin risk assessment differs from full-path crypto forecasting: the task is to judge whether a stablecoin remains stable, enters a warning state, or experiences peg stress over a **fixed future window**.

Source-reported benchmark design (abstract + intro):

- **Task:** diagnose peg stress and forecast deviations from the $1 peg over a **hidden seven-day horizon**.
- **Data:** leakage-safe historical replay with exchange price–volume data and market-context features.
- **Case structure:** frozen **30-day** lookback window; structured next-**7-day** assessment requesting stable/watch/stress label, depeg probability, maximum peg-deviation estimate, direction, confidence, and rationale.
- **Blocks:** **120-case** stress-enriched validation; **507-case** natural-distribution full-arena.
- **Systems:** **six** LLM-backed agent configurations plus baselines.
- **Metrics:** prediction quality, stress recall, missed-depeg risk, calibration, valid-output rate, latency, token usage, estimated inference cost; trustworthiness as joint quality/reliability/cost property.

Source-reported qualitative results (intro; diagnostic framing):

- Gap between **protocol-following reliability** and **financial-risk reliability**.
- Agents **reliably produce valid structured outputs** at modest measured cost.
- Agents **still miss most rare severe-stress and sustained-depeg cases**.
- Agents **do not consistently outperform simple baselines**.
- Stress-enriched validation: calibrated agents improve **aggregate Macro-F1** vs simple baselines.
- Natural-distribution 507-case block: **simple baselines remain strong**; raw accuracy shaped by **stable-dominant class balance**.
- Across both settings: **rare-stress and sustained-depeg detection remain weak**.
- Paper is **diagnostic rather than agent-promotional**.

### Research interpretation

This is **family-level negative / evaluation evidence** for using LLM/agentic systems as **stablecoin peg-risk assessors** — not a trading entry/exit strategy and not proof that any specific in-repo AI stablecoin system fails.

Hypothesized research relevance:

1. **Class imbalance ≠ skill:** High aggregate accuracy under natural peg-stable dominance can mask failure on rare depeg/stress — intake must require stress recall / missed-depeg metrics, not headline accuracy.
2. **Protocol validity ≠ risk validity:** Structured-output compliance and low token cost must not be read as financial competence.
3. **Boundary for AI-stablecoin captures:** Any Scout record that treats an LLM agent as a peg-stress detector or depeg forecaster remains `research-only` and should pre-declare stress-recall and missed-depeg evaluation; this paper **strengthens** that boundary.
4. **Not a trading rule:** No entry/exit, sizing, or venue execution is specified for alpha capture.

Component roles (normalized):

```text
Not a trading signal.
Evidence class: agentic benchmark / negative evidence for rare peg-stress detection.
Required practice (research-proposed): evaluate peg-risk agents on stress-enriched + natural blocks; report missed-depeg and calibration, not accuracy alone; preserve leakage-safe replay.
```

## Signal

Not applicable as a trading signal. No long/short entry, holding period, or position sizing in this source for alpha reconstruction.

Research evaluation sketch only (research-proposed):

- **Formation timestamp:** case origin \(t\); features from frozen 30-day window ending at \(t\); labels over \((t, t+7\text{d}]\) hidden at inference.
- **Lookback:** source-reported **30 days** market/context window; forecast horizon **7 days**.
- **Entry / Exit / Holding:** N/A.
- **Parameters:** block sizes 120 / 507; six agent configs (names/tables not fully restated this cycle beyond HTML table stub).

## Required data

- **Instrument / universe (source-reported):** stablecoin(s) in the benchmark pool; exact coin list not fully restated from intro this cycle (`data gap` beyond abstract-level “stablecoin” task).
- **Venue / fields:** exchange price–volume; market-context features; leakage-safe historical replay.
- **Market type:** stablecoin spot/peg monitoring (crypto-native); not perpetual futures alpha.
- **Point-in-time:** source emphasizes leakage-safe replay and hidden horizon — central to the design.
- **Costs:** agent evaluation includes latency/token/inference cost as metrics; **not** a trading fee model.

## Execution assumptions

No trading execution proposed. Agent “execution” in the paper is benchmark protocol compliance (structured outputs), not order placement.

## Evidence

### Source-reported

All quantitative **counts** in this record trace to arXiv:2609.18949v1 abstract/introduction (2026-08-07 / HTML reviewed 2026-09-20): hidden 7-day horizon; 30-day frozen lookback; 120 stress-enriched cases; 507 natural-distribution cases; six LLM-backed agent configurations; qualitative finding that valid structured outputs coexist with weak rare severe-stress / sustained-depeg detection; agents not consistently better than simple baselines; Macro-F1 gains limited to calibrated agents on stress-enriched block; natural block dominated by stable class balance.

Per-metric numeric tables are **not** restated here beyond intro-level direction. Dataset/code URLs are source-reported releases.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported **negative direction** for agentic peg-risk reliability on rare stress/depeg events (core incremental value of this capture).
- Class-balance sensitivity (natural vs stress-enriched blocks) is itself negative evidence against leaderboard-only evaluation.
- No independent re-run of StableEval Arena in our stack this cycle; GitHub **commit SHA** not captured (`data gap`).
- Absence of our replication is not evidence that all AI peg monitors fail.

## Falsification plan

Research-proposed evaluation standards for future agentic stablecoin-risk records (not a source trading rule):

1. **Stress-recall gate (research-defined falsification threshold):** Any claimed agentic peg-risk system must be evaluated on a pre-declared stress-enriched set; if severe-stress/sustained-depeg **recall remains ≤ simple baseline** after cost-aware protocol alignment, reject “improved risk detection” claims.
2. **Natural vs stress blocks:** Report both; if accuracy is high only under stable-dominant natural mix while stress recall is weak, mark as non-load-bearing for depeg risk.
3. **Protocol vs financial validity:** Measure valid-output rate **and** missed-depeg rate; high validity with high missed-depeg fails the joint trustworthiness claim.
4. **Leakage audit:** Recompute cases with strict PIT features; fail any result that peeks into the hidden 7-day window.
5. **Cost-quality frontier:** Pre-declare token/latency budget; reject systems that buy accuracy only via unconstrained tool/cost expansion without stress-recall gains.
6. **Action on failure:** Keep related AI-stablecoin strategy records `research-only`; do not promote agent peg monitors on protocol metrics alone.

## Crypto portability

**Portability: `direct` for the evaluation domain (crypto stablecoin peg risk); `not applicable` as a trading strategy port.**

- Task is crypto-native (stablecoin peg).
- Not authorization to trade; not a basis/funding/LP strategy.
- Risks if misused as “AI edge”: rare-event blindness, class imbalance, venue-specific price feeds, model/version drift, non-reproducible agent stacks.

## Limitations

- **Review depth:** abstract + intro HTML this cycle; full numeric tables / agent roster not fully audited.
- **GitHub provenance incomplete:** no full commit SHA this cycle.
- **not independently reproduced**
- **Not a strategy record:** no reconstructable entry/exit; incremental value is **agentic peg-risk negative evidence** (FARSIGHT-adjacent family boundary, different target).
- Do not overclaim: paper finds agents **can** improve Macro-F1 when calibrated on stress-enriched data; the durable negative is **rare severe-stress / sustained-depeg weakness** and lack of consistent dominance over simple baselines.
- Exact stablecoin pool composition and per-agent configs require PDF/code read before any system-specific claim.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: public dataset/code releases reported; **not** treated as our validation or as a trading system.

## Adoption boundary

Research-only. Presence here does **not** mean any agent or strategy is profitable, validated, or approved.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known for this arXiv capture at write time. Do not fabricate Wiki links.

In-repo related: `autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19.md`; `sok-farsight-llm-trading-agents-robustness-security-negative-evidence-arxiv-2609.19705-2026-09-19.md`; look-ahead foundation-model PIT record.

## Sources

1. Sean Wan, Dongping Liu, Luyao Zhang. "StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction." arXiv:2609.18949v1 [cs.LG], August 7, 2026. https://arxiv.org/abs/2609.18949
2. HTML full text (abstract + introduction): https://arxiv.org/html/2609.18949v1 (reviewed 2026-09-20)
3. Dataset: https://huggingface.co/datasets/SeanWan05/stableeval-arena
4. Code: https://github.com/StableTradeAtlas/StableEval-Arena (commit SHA not captured 2026-09-20)
