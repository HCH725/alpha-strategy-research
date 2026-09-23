---
schema: strategy-research-record-v1
title: Bitcoin / USDT Dominance Liquidity-Adjusted Price Regime
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/UjV6kYHL/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin / USDT Dominance Liquidity-Adjusted Price Regime

## Provenance

Public TradingView open-source indicator **Bitcoin/USDT Dominance Ratio | Astral Vision**, author/page identity `AstralVision`, published 2026-05-08. Stable source: https://www.tradingview.com/script/UjV6kYHL/ . Source reviewed as of 2026-09-23.

The source defines a ratio of Bitcoin price to USDT market-cap dominance and interprets the joint movement as a crypto risk-on/risk-off liquidity context. This record normalizes that public hypothesis without copying Pine source code.

## Economic mechanism

### Source-reported

The author describes USDT dominance as the share of total crypto market capitalization held in Tether. High USDT dominance is interpreted as capital parked in stablecoins / lower risk appetite, while low USDT dominance is interpreted as capital deployed into risk assets. The source states that dividing Bitcoin price by USDT dominance amplifies the joint state: the ratio rises when BTC appreciates while USDT dominance contracts and falls when BTC depreciates while USDT dominance expands. The author describes the resulting series as a liquidity-adjusted Bitcoin price and argues that a BTC rally accompanied by contracting USDT dominance is structurally stronger than the same rally with stable or rising USDT dominance.

### Research interpretation

The falsifiable hypothesis is not that the ratio is intrinsically valuable, but that **stablecoin-capital rotation contributes incremental information beyond Bitcoin price momentum and USDT dominance considered separately**. If declining USDT dominance represents deployment of sidelined stablecoin capital into risky crypto assets, then joint BTC appreciation plus falling USDT dominance may identify a stronger risk-on regime; the opposite joint state may identify risk-off pressure.

Because the ratio mechanically contains BTC price in its numerator, apparent predictiveness can be a repackaging of price momentum. Incremental-information and component-ablation tests are therefore mandatory.

## Signal

Source-reported core construction:

`ratio_t = BTC_price_t / USDT_dominance_percent_t`

The source describes threshold crossings, candle coloring, and background regime highlighting, but the reviewed public description does not expose the exact threshold values or a complete trading lifecycle.

- Signal formation timestamp: source does not specify a canonical execution timestamp; underspecified.
- Lookback window: no lookback is required for the raw ratio itself; any threshold-estimation lookback is underspecified in the reviewed description.
- Long entry: no complete executable long-entry rule is specified by the source.
- Short entry: no complete executable short-entry rule is specified by the source.
- Exit: underspecified.
- Holding period: underspecified.
- Re-entry: underspecified.
- Position sizing: underspecified.
- Multi-timeframe dependency: not specified in the reviewed description.

Research-proposed operationalization, only for falsification after reconstructing point-in-time inputs: classify joint component states directly (BTC return sign/quantile × change in USDT dominance sign/quantile), and separately test trailing percentile or z-score changes in the ratio. These are research-proposed tests, not source-reported trading rules.

## Required data

- Bitcoin spot/reference price with stable timestamp convention.
- USDT market capitalization and total crypto market capitalization, or a point-in-time USDT-dominance series equivalent to the TradingView source.
- Daily data is a conservative research starting frequency; the source page does not establish a canonical execution timeframe in the reviewed description.
- Point-in-time availability timestamps for market-cap/dominance data are required. Do not backfill revised or later-known constituent values into earlier signal timestamps.
- The total-market-cap universe and stablecoin data methodology must be held consistent through a test or explicitly versioned; historical constituent coverage can create structural breaks.

## Execution assumptions

The source does not specify signal-to-order timing, order type, fills, fees, spread, slippage, impact/capacity, leverage, funding, borrow, latency, or partial-fill handling.

For any later research-proposed backtest, form a signal only after all component data for the observation is known point-in-time and execute no earlier than the next eligible bar. Spot and perpetual implementations must be tested separately; a perpetual implementation additionally requires funding, mark/index conventions, leverage/margin and liquidation assumptions.

## Evidence

### Source-reported

The TradingView author presents the ratio as a risk-on/risk-off and liquidity-context visualization and states that BTC appreciation with contracting USDT dominance represents a stronger risk-on condition than BTC appreciation with stable/rising USDT dominance. The reviewed source does not provide a traceable independent backtest, Sharpe ratio, CAGR, drawdown, hit rate, or other performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative backtest was identified in the reviewed TradingView page. However, the construction has an important structural objection: BTC price is directly embedded in the numerator, so a rising ratio can arise from BTC appreciation even if USDT dominance adds no predictive information. USDT dominance also changes mechanically with the denominator (total crypto market capitalization), so falling dominance during a broad rally need not represent new stablecoin capital deployment. These are direct confounding risks, not evidence that the hypothesis works.

## Falsification plan

1. Reconstruct BTC price and USDT dominance with point-in-time availability and fixed timestamp conventions; reject the test if historical dominance cannot be made leakage-safe.
2. Primary controls: BTC price momentum alone, USDT-dominance change alone, total-crypto-market momentum, and a simple two-component interaction (`BTC momentum × -change in USDT dominance`).
3. Test the raw ratio only against those simpler components. The ratio layer fails if it adds no out-of-sample predictive information after conditioning on BTC momentum and USDT-dominance change.
4. Ablate the mechanism into four states: BTC up / dominance down; BTC up / dominance up; BTC down / dominance down; BTC down / dominance up. Require the claimed risk-on/risk-off ordering to persist out of sample rather than only in the full-sample ratio chart.
5. Use walk-forward evaluation and leave-one-major-crypto-regime/cycle-out tests. Do not fit thresholds on the full history.
6. Stress any research-proposed trailing percentile/z-score lookbacks across a broad neighborhood. Reject threshold-specific findings that disappear under nearby parameters.
7. Control for the mechanical denominator effect by testing changes in absolute USDT market cap and total crypto market cap separately. If the signal is explained by broad-market capitalization moves rather than stablecoin liquidity, reject the stablecoin-deployment interpretation.
8. Apply data-availability lags and timestamp-placebo tests to market-cap/dominance inputs.
9. If translated to a tradable strategy, test realistic spread, fees, slippage and, for perpetuals, funding. Require net-of-cost OOS improvement over the simplest BTC-momentum baseline.
10. Failure action: reject the composite ratio as an alpha layer if it does not provide robust incremental OOS information; retain at most the simpler component that survives independently.

## Crypto portability

direct

The source itself is Bitcoin/crypto-specific and uses USDT dominance. Portability beyond BTC is unproven. Venue fragmentation, stablecoin composition changes, total-market-cap methodology, 24/7 candle boundaries, and spot-versus-perpetual execution can materially alter results.

## Limitations

- Not independently reproduced.
- Exact source threshold logic is underspecified in the reviewed public description.
- Complete entry, exit, holding, re-entry and sizing rules are underspecified.
- The ratio embeds BTC price directly and is therefore highly exposed to price-momentum redundancy.
- USDT dominance is a relative share, not a direct measure of stablecoin inflow/outflow; denominator effects can mimic liquidity rotation.
- Historical market-cap and dominance series may contain methodology and constituent changes.
- No source-reported performance statistics were identified.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full-backtest validation has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitability, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No Hermes Wiki Brain lookup was performed because this Scout run is GitHub-only. Repository-level conceptual relatives include stablecoin-dominance regime research and Bitcoin price-momentum baselines; no fabricated Wiki links are asserted.

## Sources

- TradingView — AstralVision, **Bitcoin/USDT Dominance Ratio | Astral Vision**, published 2026-05-08: https://www.tradingview.com/script/UjV6kYHL/ (public open-source indicator; reviewed 2026-09-23).
