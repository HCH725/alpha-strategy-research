---
schema: strategy-research-record-v1
title: "Agora: Sealed Joint Search for Emergent Alpha Scoring via Agent-to-Agent Self-Evolution"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - agentic-alpha-discovery
  - multi-agent-systems
  - self-evolving-scoring
  - sealed-joint-search
  - formulaic-alpha
  - china-a-shares
  - csi1000
  - reinforcement-learning
status: research-only
confidence: medium
source_as_of: 2026-06-28
sources:
  - "Yuqi Li, Siyuan Liu, and Bingjun Liu, AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution, arXiv:2606.29194v1 cs.AI, submitted June 28, 2026. Stable URLs: https://arxiv.org/abs/2606.29194, https://arxiv.org/html/2606.29194v1, https://arxiv.org/pdf/2606.29194, DOI: 10.48550/arXiv.2606.29194"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Agora: Sealed Joint Search for Emergent Alpha Scoring via Agent-to-Agent Self-Evolution

## Provenance

- **Primary Source:** Yuqi Li, Siyuan Liu, and Bingjun Liu, "AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution", arXiv preprint arXiv:2606.29194v1 cs.AI, submitted June 28, 2026 (source-reported).
  - Abstract URL: https://arxiv.org/abs/2606.29194
  - Full-Text HTML URL: https://arxiv.org/html/2606.29194v1
  - Full-Text PDF URL: https://arxiv.org/pdf/2606.29194
  - Canonical DOI: https://doi.org/10.48550/arXiv.2606.29194
  - License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) (source-reported).
- **Verification Integrity:** The complete full-text manuscript of arXiv:2606.29194v1 was directly retrieved and audited. The five structural conditions (P1-P5), the SJS framework, the Agora system architecture (five agent classes, nine clients, three channels, eight skill libraries), the experimental setup (CSI 1000, RiceQuant OHLCV, 2014-2026 temporal split, 91-day holdout), and all empirical results in Tables 1-5 and Sections 3-5 trace directly to the primary source. Authors confirmed as Yuqi Li, Siyuan Liu, and Bingjun Liu. Same author group as the later VST paper (arXiv:2609.07065, September 2026), but Agora (June 2026) is chronologically earlier and focuses on joint search over scoring functions rather than verifiable transport protocols.
- **Repository Deduplication Audit:** Comprehensive search across all .md records in alpha-strategy-research found zero existing records matching arXiv:2606.29194, the title, "Sealed Joint Search", or "Agora" in an alpha-mining context. The VST record (vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12.md) covers a different protocol layer from the same research group. No source overlap.

## Economic mechanism

### Source-reported

1. **The Scoring Function Blind Spot:** Automated alpha mining systems (GP, RL, LLM-driven search) hold the scoring function fixed and vary only the search algorithm. A search that converges against a fixed scorer overfits whatever the scorer cannot penalize. The authors argue this is a primary cause of the out-of-sample generalization gap - when the bottleneck is the choice of objective rather than the choice of expression, better search algorithms cannot help (source-reported).

2. **Sealed Joint Search (SJS):** A framework treating the scoring function as a search artifact alongside the alpha factors. The framework imposes five structural conditions on information flow to prevent joint search from collapsing into self-confirmation while keeping the external evaluator sealed (source-reported):
   - P1 (Decomposed proposal): Proposers and adjudicators are separate roles with no shared state.
   - P2 (Bounded inter-temporal edges): Cross-round influence is limited to a small number of typed records controlled by the substrate, not agents.
   - P3 (Provenance-determined read scope): Each record carries a provenance tag; reading roles have scoped access enforced at the substrate level.
   - P4 (Skill stores as evolution locus): Persistent state in role-owned stores evolves only through substrate-computed transitions.
   - P5 (Closure-induced state transitions): Skill store advances only through substrate-local promotion rules referencing internal outcome variables.

3. **Emergent Metrics:** Two scoring metrics emerged during the 100-round Agora run that the system was not designed to produce. Neither was produced by any single agent; each emerged from aggregate promotion evidence across rounds. An ablation shows these two metrics account for only 1.57 of the +2.25 Sharpe-unit gap vs. frozen libraries, indicating the remaining gap comes from the F4+F5 mechanism itself (source-reported).

### Research interpretation

The hypothesis is that fixing the scoring function (typically IC or Sharpe on training data) creates a structural overfitting bottleneck that no search algorithm improvement can resolve. By allowing the scoring function itself to co-evolve with alpha factors - under strict information-topology constraints that prevent self-confirmation - the system can discover objective functions that generalize better to unseen data.

The mechanism is analogous to co-evolutionary dynamics in biology: the scoring function and the alpha candidates co-evolve under selective pressure, with the sealed external evaluator acting as the "environment." The SJS topology prevents the trivial collapse where a system satisfies itself by relaxing its own criteria.

The two emergent metrics suggest that the system discovers scoring functions that capture aspects of return predictability missed by standard IC-based selection - potentially related to regime conditioning, non-linearity, or factor interaction effects. However, this is speculative; the paper does not identify what those metrics actually measure.

## Signal

### Formation timestamp
Agora runs 100 outer rounds on the training segment (2014-10 to 2019-12). Each round executes a fixed sequence: research-report advisory, alpha-miner proposes candidates, alpha-evaluator panel scores on training segment, evaluation-miner proposes metric action, candidates re-scored on test segment under new metric set, composite portfolio run through layered backtest, factor-metrics-evaluator writes reports, orchestrator commits. The 2026 holdout (2026-01 to 2026-05) is loaded only after all 100 rounds complete (source-reported).

### Lookback
Training segment: 2014-10-17 to 2019-12-31, 1277 trading days. Test segment: 2020-01 to 2025-12, 1461 trading days. Holdout segment: 2026-01 to 2026-05, 91 trading days. RiceQuant post-adjusted OHLCV daily data with combo_mask (tradable membership), limit_up_filter (price-limit binary mask), and next-day open price (source-reported).

### Entry
Top-30 alphas selected by training-segment information coefficient, equal-weight z-score combined into a composite signal. Portfolio constructed via 10-decile sort with 5-day rebalance on next-day open (source-reported).

### Exit
5-day rebalance cadence. No explicit stop-loss or take-profit at the portfolio level. Per-alpha selection is by train-segment IC ranking (source-reported).

### Holding period
5-day rebalance window (source-reported).

### Parameters
- 100 outer rounds (source-reported)
- claude-sonnet-4-6 backbone for all 9 LLM clients (source-reported)
- Alpha-side libraries seeded from AlphaGen operator vocabulary and MaskablePPO infrastructure (source-reported)
- Metric library seeded with 4 builtins (rank IC, information ratio, score stability, turnover penalty) (source-reported)
- 64 total builtin skills across 8 libraries (source-reported)
- Promotion threshold: absolute correlation >= 0.6 between metric score and training Sharpe; demotion below 0.4 (source-reported)
- RTX 5090 GPU for optional PPO relay (source-reported)
- ~60 GPU-hours + ~4,500 LLM calls total (source-reported)

### Position sizing
Equal-weight z-score combination of top-30 alphas. No leverage (source-reported).

## Required data

- **Instrument:** CSI 1000 dynamic-universe equities (source-reported).
- **Venue:** RiceQuant post-adjusted OHLCV (source-reported).
- **Market type:** China A-share equities, daily bars (source-reported).
- **Timeframe:** Daily (source-reported).
- **Fields:** Open, High, Low, Close, Volume (OHLCV), combo_mask (tradable membership), limit_up_filter (price-limit binary mask), next-day open price (source-reported).
- **Point-in-time:** Not explicitly stated; RiceQuant post-adjusted data used without explicit point-in-time audit. Data gap.
- **Missing-data:** Not discussed. Data gap.
- **Funding/fee/spread:** Round-trip cost is 9 bps one-way (double-sided 0.04% commission + 0.05% stamp tax) (source-reported). Funding not applicable for equities.

## Execution assumptions

- **Signal-to-order timing:** Next-day open execution (source-reported).
- **Order type:** Market order assumed (source-reported).
- **Fill model:** Assumed perfect fill at next-day open (source-reported).
- **Fees:** 0.04% commission + 0.05% stamp tax per side, total 9 bps round-trip (source-reported).
- **Slippage:** Not modeled. Data gap.
- **Impact:** Not modeled. Data gap.
- **Leverage:** Not used (source-reported).
- **Latency:** Not applicable for daily rebalance (source-reported).

## Evidence

### Source-reported

| Metric | Agora | Best baseline (B2 AlphaGen-PPO seed=42) |
|--------|-------|----------------------------------------|
| Holdout Portfolio Sharpe | +1.872 | +1.334 |
| Portfolio IC | +0.0894 | +0.0500 |
| Portfolio Annualized Return | +0.484 | +0.354 |
| Decile Monotonicity | +0.285 | +0.673 |
| Per-alpha Median Sharpe | +1.06 | +0.377 |

From Tables 1-5 and Section 5 of arXiv:2606.29194v1 (source-reported).

Cross-seed analysis (B2): B2 Sharpe swings from +1.334 (seed=42) to -3.08 (seed=0), mean -0.039, std 2.29 across 3 seeds. Agora's full-system seed variance is uncharacterized (single-seed only) (source-reported).

Statistical significance: Agora vs. B1 (GP): reject at alpha=0.01 (t=2.94); Agora vs. B7 (random search): reject at alpha=0.01 (t=3.24). Agora vs. B2 (AlphaGen-PPO): fail to reject (t=0.19, p=0.42) - 91-day window too short to distinguish 1.5 Sharpe-unit gap (source-reported).

Ablation: Frozen libraries (B6) holdout Sharpe = 0.379. The F4+F5 (persistence + promotion) mechanism contributes at most +2.25 Sharpe units. Two emergent metrics account for only +1.57 of that gap; the remaining +0.68 is attributable to library evolution more broadly (source-reported).

Signal is short-side concentrated: bottom-decile (G1) annualized return is +0.843 on holdout; top-decile (G10) is +0.040. The strategy is intended for long-short or short-extension deployment (source-reported).

Source-reported results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Single-seed Agora run; full-system variance uncharacterized (source-reported).
- 91-day holdout window insufficient for statistical significance against strongest baselines (B2, B3, B5, B6 all fail to reject at conventional levels) (source-reported).
- Short-side concentrated signal; long-only deployment trails the equal-weight benchmark by -0.336 annualized (source-reported).
- Cross-seed robustness of B2 is severe: Sharpe ranges from +1.334 to -3.08 across three seeds, indicating the baseline comparison itself is unstable (source-reported).
- The paper does not disclose what the two emergent metrics actually measure, limiting interpretability (source-reported).
- None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Multi-seed replication:** Run Agora at 3 or more independent random seeds and report mean and std of holdout Sharpe. If the mean falls below B2's cross-seed mean (-0.039), the single-seed headline is a lucky draw (research-defined falsification threshold).
2. **Extended holdout:** Evaluate on a longer holdout window (12 months or more) to increase statistical power. If Agora-vs-B2 significance does not reach p < 0.05 on a 12-month window, the edge is undetectable at practical sample sizes (research-defined falsification threshold).
3. **Ablation: disable metric evolution only:** Freeze metric library while allowing operator/library evolution. If holdout Sharpe retains more than 80% of the gap vs. B6, the emergent metrics are not the primary contribution (research-defined falsification threshold).
4. **Non-CSI universe:** Port to a different equity universe (e.g., S&P 500, Russell 3000) or crypto. If the SJS topology does not produce emergent metrics in a different domain, the contribution may be universe-specific (research-defined falsification threshold).
5. **Cost sensitivity:** Stress test at higher transaction costs (2-3x the current 9 bps). If the short-side concentrated signal requires very low costs to remain profitable, practical viability is limited (research-defined falsification threshold).

## Crypto portability

unproven

The SJS framework is domain-agnostic (it specifies information topology, not market mechanics). However, the Agora instantiation is evaluated exclusively on CSI 1000 equities with specific execution assumptions (daily rebalance, next-day open, 9 bps costs, China A-share market structure). Crypto portability faces several challenges:
- 24/7 session structure and intraday funding rate dynamics differ fundamentally from equity daily close (research interpretation).
- Liquidity fragmentation across venues and the absence of a unified settlement layer in crypto may break the assumption of perfect fill at a reference price (research interpretation).
- The short-side concentrated signal may not translate to crypto markets where shorting requires perpetual funding payments or borrow costs (research interpretation).
- The paper does not test on any non-equity universe. Crypto portability is entirely speculative.

## Limitations

- **Single-seed headline:** The full Agora run was performed at a single random seed due to compute budget (~60 GPU-hours + ~4,500 LLM calls). The 95% CI on Agora's holdout Sharpe is [-2.124, +6.102], spanning zero and indicating the point estimate is not statistically reliable (source-reported).
- **91-day holdout:** The evaluation window is too short to distinguish Agora from its strongest baselines at conventional significance levels (source-reported).
- **Short-side concentration:** The alpha signal is primarily driven by the short leg, limiting deployment to long-short or short-extension portfolios (source-reported).
- **Interpretable gap:** The two emergent metrics are not identified or characterized - the paper reports that they exist and correlate with training Sharpe but does not explain what they measure (source-reported).
- **Chinese equity market specific:** Evaluated on CSI 1000 with RiceQuant data; generalizability to other markets is undemonstrated (source-reported).
- **LLM cost:** ~4,500 LLM calls (claude-sonnet-4-6) at ~60 GPU-hours represents substantial compute for a 91-day holdout evaluation (source-reported).
- **No independent reproduction** of any reported result.

## Implementation status

not-implemented

The paper releases an open-source implementation (referenced in the paper as Agora's codebase), but no implementation has been performed in our research stack. The paper's backtest is a layered 10-decile sort with 5-day rebalance, not a production trading system.

## Adoption boundary

research-only

This record documents a research framework (Sealed Joint Search) and its empirical instantiation (Agora) evaluated on a sealed holdout. Presence in this repository does not imply:
- Profitable or validated alpha
- Approved for implementation
- Approved for paper trading, testnet, or live trading
- Generalizable across markets or time periods

The headline Sharpe (+1.872) is from a single seed on a 91-day holdout and should not be treated as a validated result.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] (schema specification)
- No directly related strategy research records share the same source identity. The VST record (vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12.md) covers a different protocol layer from the same author group but addresses auditable transport rather than joint search over scoring functions.

## Sources

1. Yuqi Li, Siyuan Liu, and Bingjun Liu. "AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution." arXiv preprint arXiv:2606.29194v1 cs.AI, submitted June 28, 2026. https://arxiv.org/abs/2606.29194. License: CC BY-SA 4.0.
