---
schema: strategy-research-record-v1
title: TradingView Cross-Venue Spot/Futures Volume-Profile Dispersion
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/P2XgvcKM-Aggregated-Volume-Profile-Spot-Futures/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Cross-Venue Spot/Futures Volume-Profile Dispersion

## Provenance

- **Source:** TradingView open-source script, `Aggregated Volume Profile Spot & Futures` by HALDRO.
- **Stable public URL:** https://www.tradingview.com/script/P2XgvcKM-Aggregated-Volume-Profile-Spot-Futures/
- **Initial publication shown by source:** 2023-01-11.
- **Latest update shown by source:** 2025-03-10.
- **Source as-of:** 2026-09-20.
- The source describes a crypto-only fixed-range volume-profile tool that can combine spot, futures, and other selected TradingView symbols across multiple exchanges. The 2025 update states that 20 built-in exchanges are available and adds VAH/VAL.

## Economic mechanism

### Source-reported

The source presents cross-exchange aggregation as a way to view crypto volume profiles using more than one venue. It permits aggregate calculations by sum, average, median, or variance, and permits bullish, bearish, or total-volume profile views. It does not report a trading strategy or establish that any profile-derived rule is profitable.

### Research interpretation

**Hypothesis:** venue fragmentation contains information that a single-exchange volume profile discards. A price level accepted across many spot/futures venues should represent broader market participation than a level dominated by one venue, while unusually high cross-venue volume dispersion may identify venue-specific positioning or dislocation.

Two competing, falsifiable mechanisms should be tested rather than assuming one direction:

1. **Consensus/acceptance continuation:** when spot and futures venues concentrate volume at similar price levels and price leaves the jointly accepted value area with broad participation, subsequent continuation may be stronger than after a single-venue breakout.
2. **Dispersion/rebalancing:** when venue-specific profiles disagree materially — for example, profile centers or value areas separate while price remains common across venues — the disagreement may reflect localized flow that subsequently converges or mean-reverts as arbitrage capital reallocates.

The conversion from a visualization to predictive signals is **research-proposed**. The source itself does not claim these exact alpha rules.

## Signal

The source supplies profile construction capabilities, not a complete entry/exit strategy. The following research operationalization is therefore explicitly **research-proposed**.

### Source-supported primitives

- Select one or multiple crypto exchange/symbol sources, including spot/futures where available.
- Construct a fixed-range volume profile.
- Aggregate volume by `SUM`, `AVG`, `MEDIAN`, or `VARIANCE`.
- Select bullish, bearish, or combined volume.
- Observe profile structure including POC and, after the 2025 update, VAH/VAL.

### Research-proposed features

At each causal profile refresh, compute per-venue profile features using the same fixed historical range:

- POC price by venue;
- VAH and VAL by venue;
- distance of current price from each venue POC/value area;
- cross-venue POC dispersion normalized by contemporaneous price or ATR;
- overlap ratio among venue value areas;
- spot-versus-futures profile-center spread;
- concentration of aggregate volume attributable to the largest venue;
- aggregate-profile breakout/re-entry state.

Candidate hypotheses:

- **Consensus continuation:** test whether low POC dispersion + high value-area overlap + confirmed exit from the aggregate value area predicts continuation in the exit direction.
- **Dispersion convergence:** test whether extreme normalized POC/value-area dispersion predicts contraction of the dispersion and/or price reversion toward the cross-venue consensus profile center.

Formation timing must use only profiles available at the completed signal timestamp. Exact fixed-range length, dispersion threshold, overlap threshold, confirmation rule, entry, exit, holding horizon, re-entry, and sizing are **underspecified by the source** and must be pre-registered as research parameters rather than attributed to HALDRO.

## Required data

- **Universe:** crypto assets with sufficiently liquid listings across multiple TradingView-supported venues.
- **Market types:** spot and futures/perpetuals as applicable to the selected symbols.
- **Fields:** synchronized OHLCV per venue; market-type and quote-currency metadata.
- **Profile inputs:** causal historical price ranges and volume at each venue.
- **Timestamp requirements:** normalized timestamps/candle boundaries across venues; no forward-filled future venue observations.
- **Point-in-time requirements:** only symbols and venue data actually available at each historical timestamp; avoid survivorship from current exchange listings.
- **Normalization:** quote-currency and contract-unit differences must be normalized before comparing or aggregating volume.
- True trade-at-price data would be preferable for independent reproduction; bar-based volume allocation may only approximate the underlying volume-at-price distribution depending on implementation/data availability.

## Execution assumptions

The source does not specify executable trading rules, order type, signal-to-order timing, fill model, fees, spread, slippage, impact, funding, leverage, margin, borrow, latency, partial fills, or failure handling.

For testing, any strategy derived from a completed bar/profile should execute no earlier than the next realistically tradable observation unless an intrabar simulation with point-in-time data is explicitly implemented. Spot/futures comparisons must include venue-specific fees, spread/slippage, futures funding where applicable, contract specifications, and transfer/latency constraints if the proposed trade requires cross-venue execution. These are **research-proposed** requirements, not source-reported assumptions.

## Evidence

### Source-reported

The source reports functionality rather than performance: aggregation across multiple crypto exchanges, selectable spot/futures sources, sum/average/median/variance aggregation, bullish/bearish/combined volume modes, and fixed-range POC/VAH/VAL profile construction. No traceable Sharpe, CAGR, drawdown, win rate, or profitability result is reported on the reviewed source page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source's April 2023 release notes state that volume extraction/processing was substantially changed for accuracy, and the March 2025 release notes state that volume errors caused by an update to the built-in volume-type function were fixed. Historical reproducibility is therefore version-sensitive.
- Cross-venue volume is not automatically comparable: spot and derivative contracts can use different units, quote currencies, multipliers, and reporting conventions.
- A fixed-range profile is path- and anchor-dependent; arbitrary range selection can create researcher degrees of freedom.
- Profile agreement may simply proxy common price history and market beta rather than incremental cross-venue information.
- No source-reported trading performance was found on the reviewed page; absence of a reported backtest is not evidence of alpha.

## Falsification plan

1. **Incremental-information ablation:** compare price-only baseline → single-venue profile → aggregate profile → cross-venue dispersion/overlap features. Reject the incremental thesis if the dispersion layer does not improve strictly out-of-sample performance or predictive information after costs.
2. **Spot/futures ablation:** compare spot-only, futures-only, and combined profiles. A combined signal must outperform or add orthogonal information relative to the stronger component rather than merely averaging it.
3. **Venue leave-one-out:** recompute signals while excluding each major venue in turn. A result dominated by one exchange weakens the cross-venue mechanism.
4. **Venue-label placebo:** permute venue identities or pair unrelated venue profiles while preserving marginal distributions. Genuine cross-venue alignment should outperform these placebos.
5. **Anchor sensitivity:** pre-register several causal fixed-range lengths and reject results that depend on a narrow hand-selected range.
6. **Unit-normalization sensitivity:** repeat with coin-volume, properly normalized notional volume, and robust cross-venue scaling. Material sign changes imply measurement dependence.
7. **Regime/OOS tests:** evaluate trend, range, high/low volatility, bull/bear, and venue-stress regimes with purged chronological out-of-sample splits.
8. **Cost test:** apply realistic venue-specific fees, spreads, slippage, and funding. Reject any executable interpretation whose net edge is not robust to conservative costs.
9. **Leakage audit:** verify every profile bin, POC, VAH/VAL, venue membership, and normalization input is point-in-time and formed only from information available by the signal timestamp.

Failure of the cross-venue layer should result in rejection or simplification to the surviving baseline; complexity alone is not evidence of alpha.

## Crypto portability

**direct** — the source explicitly states that the indicator is for crypto and is designed to aggregate crypto exchange sources, including spot/futures selections.

Portability across crypto venues is still nontrivial because of 24/7 candle-boundary alignment, exchange outages, venue fragmentation, quote-currency differences, derivative contract specifications, funding, mark/index versus traded price, symbol-history changes, and unequal liquidity.

## Limitations

- The source is an indicator/tool, not a complete trading strategy.
- Entry, exit, holding horizon, sizing, thresholds, and re-entry are **underspecified**.
- The predictive use of profile consensus/dispersion is **research-proposed**.
- Volume-profile construction may be approximate when reconstructed from bar data rather than true trade-at-price records.
- Cross-venue symbol and unit normalization is a material data-quality risk.
- Fixed-range anchoring introduces degrees of freedom that require pre-registration and robustness testing.
- **Not independently reproduced.**

## Implementation status

No implementation or Qlib full-backtest validation has been completed in our research stack. This record is normalized external research material only.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable, represents validated alpha, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain record is linked from this GitHub-only Scout run. No Wiki link is fabricated.

## Sources

- HALDRO, `Aggregated Volume Profile Spot & Futures`, TradingView open-source script. Initial publication shown: 2023-01-11; latest update shown: 2025-03-10; accessed/as-of 2026-09-20. https://www.tradingview.com/script/P2XgvcKM-Aggregated-Volume-Profile-Spot-Futures/
