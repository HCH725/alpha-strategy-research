---
schema: strategy-research-record-v1
title: "M²-Alpha: Micro-Macro Alternating Attention for A-Share Cross-Sectional Stock Ranking"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - deep-learning
  - transformer
  - cross-sectional-equity
  - a-share
  - attention-mechanism
  - stock-selection
  - dense-supervision
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "https://github.com/Johnny-xuan/M2-Alpha (commit e587b95a33de0c628f683914c4eb2fc5ed1d205e, released 2026-07-07)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# M²-Alpha: Micro-Macro Alternating Attention for A-Share Cross-Sectional Stock Ranking

## Provenance

- **Repository:** https://github.com/Johnny-xuan/M2-Alpha
- **Full commit SHA:** `e587b95a33de0c628f683914c4eb2fc5ed1d205e` (main branch as of 2026-09-13)
- **License:** Apache-2.0
- **Released checkpoints:** `ml/m2alpha.pt` (M-0-M), `ml/m2alpha-m1m.pt` (M-1-M), `ml/m2alpha-m2m.pt` (M-2-M)
- **Technical report (EN):** `docs/report/M2Alpha_Technical_Report_EN.pdf`
- **Results documentation:** `docs/RESULTS.md`
- **Method documentation:** `docs/METHOD.md`
- **Source as-of date:** Repository commit `e587b95`, released 2026-07-07; benchmark window 2025-07 to 2026-06.
- **Authors:** "M2-Alpha contributors" (per CITATION.cff; primary GitHub account: Johnny-xuan)

## Economic mechanism

### Source-reported

The repository proposes that a useful stock ranking score needs two simultaneous views: (1) how an individual stock has behaved over its own recent path (micro view), and (2) where that stock sits relative to other stocks on the same day (macro view). The model alternates between these two views via stacked "M² Blocks," each containing a time-axis self-attention pass (micro) and a cross-stock self-attention pass (macro). The claim is that this alternation captures both short-horizon patterns (momentum, reversal, volatility regime) and cross-sectional structure (relative cheapness/expansion/pressure) more effectively than models that collapse the time dimension or treat the panel as a single sequence.

### Research interpretation

The hypothesized mechanism is that cross-sectional stock ranking benefits from joint modeling of temporal trajectory and relative peer position. The micro attention encodes per-stock time-series signals (momentum, mean-reversion, volatility regime shifts). The macro attention learns soft peer groups and relative valuation/pressure signals without an explicit industry graph. The interaction between these two views across stacked blocks acts as a learned iterative refinement process, analogous to a trader repeatedly comparing an individual stock's path against the cross-section.

Key architectural components:
- **Micro attention:** causal time-axis self-attention within each stock (Gaussian recency bias, sigma=4.0)
- **Macro attention:** cross-stock self-attention at each time step (no explicit industry graph; learned soft peer groups)
- **FFN:** position-wise feed-forward network after each M² Block
- **Dense supervision:** MSE loss over the full (stocks × time) grid during training; only last timestep used at inference

## Signal

### Formation timestamp

- Signal formed daily after market close using that day's full cross-sectional panel.
- Next-day execution at open price/open NAV.
- Timezone: CST (China Standard Time, UTC+8).

### Lookback

- Window length τ = 8 trading days.
- Input tensor shape: (stocks, 8, 35) — 35 daily factors over 8-day lookback per stock.
- Features are computed within each stock's history, then robust-z-scored against the cross-section of the same trade date.

### Entry

- At inference, the model's last-timestep score is used to rank all stocks in the tradable universe.
- Long the top N stocks by rank (N varies by strategy configuration: 5, 7, 10, 15, or 30).
- Equal weight across held positions.

### Exit

- Sell rule: drop stocks whose rank falls below a configurable sell_rank threshold.
- Sell rank varies by strategy: 20, 35, 50, 100, or 200 (research-defined parameter).
- Industry concentration cap: configurable max fraction per industry (1, 2, 3, 4, 5, or no cap).

### Holding period

- Daily rebalance cadence.
- Effective holding period depends on turnover and sell rule.

### Parameters

| Parameter | Value | Source |
|---|---|---|
| Lookback τ | 8 trading days | Source-reported |
| Features F | 35 daily factors | Source-reported |
| Hidden size | 128 | Source-reported |
| Optimizer | AdamW | Source-reported |
| Learning rate | 1e-5 | Source-reported |
| Weight decay | 1e-4 | Source-reported |
| Gradient clipping | norm 5.0 | Source-reported |
| Max epochs | 40 | Source-reported |
| Early stopping metric | Validation IC | Source-reported |
| Default seed | 42 | Source-reported |
| Fee rate | 0.0013 (0.13%) | Source-reported |
| Execution price | Open / Open NAV | Source-reported |

**Portfolio rule (selected post-hoc on historical grid, not untouched OOS):**

| Model | n_hold | sell_rank | industry cap | Cumulative return | Sharpe | MDD | Turnover |
|---|---|---|---|---|---|---|---|
| M-2-M (5-block) | 5 | 50 | max 3 per industry | +443.01% | 3.99 | -13.86% | 0.5502 |
| M-1-M (3-block) | 5 | 200 | max 1 per industry | +242.07% | 3.24 | -15.43% | 0.2916 |
| M-0-M (baseline) | 7 | 35 | max 3 per industry | +170.92% | 2.93 | -13.16% | n/a |

Source-reported. Evaluation window: 2025-07-10 to 2026-06-10 (≈11.5 months). This is post-hoc strategy selection from a 145-combination sweep; it is NOT untouched out-of-sample evidence.

### Underspecified

- The exact composition of the 35 features is listed in groups (momentum returns, MA deviation, volatility, candlestick shape, volume activity, turnover/PE/PB/PS, money-flow structure) but granular feature names are in the source code, not fully enumerated in the docs.
- The open-data reconstruction route may miss or approximate: historical true volume ratio, free-float turnover, valuation fields for some symbols/dates, order-size money-flow fields, and consistent industry/market-cap snapshots.

## Required data

- **Instrument:** A-share stocks (China mainland, Shanghai/Shenzhen exchanges).
- **Universe:** Dynamic top-1000 by free-float market cap. Full tradable list for ranking; pool_rank=100 retained as a historical parameter but the current benchmark ranks the full list.
- **Venue:** A-share spot market (no derivatives).
- **Timeframe:** Daily bars.
- **Fields:** 35 daily features: multi-scale returns (1d, 5d, 60d, etc.), moving-average deviation (MA5, MA60), rolling volatility, candlestick shape (body, range, upper/lower shadow), volume ratios, daily basic fields (turnover, PE, PB, PS, volume ratio), net money-flow ratio, large-vs-small buy imbalance.
- **Data sources:** BaoStock (historical base), AKShare and efinance (snapshot enrichment). Full-factor research panel is NOT publicly bundled; the open-data route is best-effort.
- **Point-in-time:** Features are computed within each stock's history and cross-sectionally normalized on the same trade date. No look-ahead in feature construction.
- **Missing data:** Handled by exclusion of invalid stocks per day. Incomplete factor families from open data may materially change model rankings (source caveat).

## Execution assumptions

- **Signal-to-order timing:** Daily signal formed after close; execution at next-day open.
- **Order type:** Market order at open price.
- **Fill model:** Assumed full fill at open price / open NAV.
- **Fees:** fee_rate = 0.0013 (0.13% per trade). Source-reported.
- **Slippage:** Not explicitly modeled beyond fee assumption. Underspecified.
- **Spread:** Not modeled. Underspecified.
- **Impact / capacity:** Not modeled. The universe is top-1000 A-shares by free-float market cap, which has meaningful liquidity, but capacity constraints at scale are not discussed.
- **Leverage / margin:** Not applicable (long-only equity).
- **Shorting:** Not used (long-only ranking).
- **Partial fills / failures:** Not modeled.

## Evidence

### Source-reported

Source reports backtest results on a compatible full-factor top-1000 A-share panel, 2025-07 to 2026-06:
- M-2-M (5-block): +443.01% cumulative return, Sharpe 3.99, MDD -13.86%, turnover 0.5502
- M-1-M (3-block): +242.07% cumulative return, Sharpe 3.24, MDD -15.43%, turnover 0.2916
- M-0-M (baseline): +170.92% cumulative return, Sharpe 2.93, MDD -13.16%

These are historical simulations with post-hoc strategy selection from a 145-combination sweep. The source explicitly states: "This is historical strategy-selection result, not an untouched out-of-sample strategy comparison."

Ablation results (source-reported):
- 4-block checkpoint: +147.38% cumulative, Sharpe 1.93, MDD -30.14%
- Dense supervision beat last-step-only supervision in ablation
- Both micro and macro attention contributed to performance in ablation
- Validation IC was not a reliable checkpoint-selection rule

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The 4-block ablation performed substantially worse than 3-block and 5-block, suggesting non-monotonic depth scaling.
- The evaluation window is ≈11.5 months, which is short for assessing regime robustness.
- The source acknowledges that open-data reconstruction may miss or neutralize key factor families, materially affecting results.
- Post-hoc strategy selection from a 145-combination grid inflates apparent performance relative to a pre-declared strategy.

## Falsification plan

1. **Out-of-sample test:** Run the released checkpoints on a forward period beyond 2026-06-10 using the same fixed-protocol benchmark. Failure: Sharpe drops below 1.0 or cumulative return turns negative on a 6+ month forward window.
2. **Data completeness sensitivity:** Reconstruct the full factor panel from open sources and compare results. Failure: if model ranking or performance materially changes (e.g., Sharpe degrades by >1.0), the results are data-dependent.
3. **Depth ablation consistency:** If deeper blocks (e.g., 6+) do not continue to improve or match 5-block performance, the architecture scaling claim is weakened.
4. **Parameter perturbation:** Hold n_hold and sell_rank fixed at the declared values and sweep alternative seeds/checkpoints. Failure: high variance across seeds (>1.5 Sharpe std across seeds 42, 123, 2024).
5. **Regime decomposition:** Break the 11.5-month window into bull/bear/sideways subperiods. Failure: if Sharpe is negative or near-zero in any subperiod exceeding 2 months, regime dependence is confirmed.
6. **Industry concentration stress:** Test with no industry cap vs. max-1 industry. Failure: if the gap exceeds 1.5 Sharpe, the industry constraint is a material alpha source, not the model.

## Crypto portability

**unproven**

This model is designed for A-share daily stock selection with 35 equity-specific factors (PE, PB, PS, money-flow, candlestick shape, industry classification). Direct portability to crypto is not demonstrated and faces several structural barriers:
- Crypto markets lack the factor taxonomy (PE, PB, industry) that drives the feature set.
- 24/7 trading, funding rates, perpetual/futures structure, and venue fragmentation differ fundamentally from A-share spot.
- The cross-sectional ranking paradigm assumes a stable universe of hundreds of liquid stocks; crypto universe composition is more volatile.
- The micro-macro attention concept (time-axis + cross-section attention) could theoretically be adapted to a cross-sectional crypto ranking task (e.g., top-N altcoin selection), but this would require re-engineering the entire feature set and is untested.

## Limitations

- **Short evaluation window:** ≈11.5 months (2025-07 to 2026-06) is insufficient to assess regime robustness or long-term decay.
- **Post-hoc strategy selection:** The reported Sharpe 3.99 comes from selecting the best of 145 strategy combinations on the same historical window. This is not untouched OOS evidence.
- **Data dependency:** Full-factor research panel is not publicly bundled. The open-data route is best-effort and may miss key factor families (true volume ratio, free-float turnover, money-flow fields), materially affecting results.
- **Not independently reproduced:** No independent reproduction exists.
- **No transaction cost beyond fees:** Slippage, spread, and market impact are not modeled.
- **Architecture depth non-monotonic:** The 4-block ablation performed substantially worse than 3-block, suggesting depth scaling is not straightforward.
- **A-share specific:** The factor set, universe construction, and market structure are A-share specific. Portability to other markets is speculative.
- **Source quality:** The repository is by a single contributor (Johnny-xuan) with 2 GitHub stars. The technical report is self-published (not peer-reviewed). Results should be treated as preliminary.

## Implementation status

No implementation in our research stack (PyBroker/Nautilus). Not implemented, not backtested, not paper-traded.

## Adoption boundary

This record is research material only. Presence in this repository does NOT mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining]] (related LLM-based alpha mining for A-shares, different mechanism)
- [[quant/nystrom-attention-cross-sectional-stock-transformer-low-rank]] (related cross-sectional stock transformer, different attention mechanism)

## Sources

1. M2-Alpha contributors. "M²-Alpha: A Research-to-Reproduction A-Share Deep-Learning Alpha Repository." GitHub repository. https://github.com/Johnny-xuan/M2-Alpha. Commit `e587b95a33de0c628f683914c4eb2fc5ed1d205e`. Released 2026-07-07. License: Apache-2.0.
2. M2-Alpha contributors. "M²-Alpha Technical Report (EN)." PDF at `docs/report/M2Alpha_Technical_Report_EN.pdf` in the repository.
3. M2-Alpha contributors. "Results." `docs/RESULTS.md` in the repository. Commit `e587b95a33de0c628f683914c4eb2fc5ed1d205e`.
4. M2-Alpha contributors. "Method." `docs/METHOD.md` in the repository. Commit `e587b95a33de0c628f683914c4eb2fc5ed1d205e`.
