---
schema: strategy-research-record-v1
title: Crypto Correlation Decoupling Alpha Regime
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
  - https://www.tradingview.com/script/V8xTszSe-Crypto-Correlation-Oscillator/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Correlation Decoupling Alpha Regime

## Provenance

- Public TradingView open-source indicator: **Crypto Correlation Oscillator** by `Frey_Crypto`.
- Stable source URL: https://www.tradingview.com/script/V8xTszSe-Crypto-Correlation-Oscillator/
- Published: 2025-11-08.
- Source reviewed as of: 2026-09-23.
- The source describes a companion/context indicator rather than a self-contained backtested strategy.

## Economic mechanism

### Source-reported

The author interprets falling or low rolling correlation between a crypto asset and Bitcoin as increasing independence from Bitcoin and therefore a potential alpha opportunity or market-regime change. The source also uses Coin/BTC-versus-BTC correlation as a relative-strength context, and optionally correlates the coin with USDT dominance and BTC dominance to contextualize flight-to-safety and altcoin/BTC regimes.

### Research interpretation

The falsifiable hypothesis is narrower than the source's use of the word “alpha”: **a transition from high BTC co-movement to low BTC co-movement may identify a distinct conditional regime in which an altcoin's own relative-strength or reversal signal has different forward-return behavior than during a high-correlation regime.**

Low contemporaneous correlation alone is not directional alpha. It can reflect idiosyncratic information, venue/liquidity fragmentation, noise, stale pricing, or a temporary volatility mismatch. Therefore the correlation state should be tested as a conditioning variable against simple BTC beta/correlation controls rather than assumed to be a trade signal.

A major specification risk is that the TradingView description says the calculation uses close prices. Correlation of non-stationary price levels can be spurious. Return-correlation must therefore be an explicit falsification control; it is not a source-reported replacement rule.

## Signal

Source-specified indicator construction:

- Update: every bar on the selected timeframe.
- Primary series: rolling Pearson correlation between the chart coin and BTC.
- Default correlation lookback: 100 bars.
- Default smoothing: 5-bar EMA applied to raw correlations.
- Source interpretation zones for the primary Coin-vs-BTC line:
  - above 0.7: high correlation / BTC-following regime;
  - below 0.3: low-correlation / potential alpha regime;
  - below 0: inverse-correlation regime;
  - crossing 0.5 is described as a major correlation-regime shift.
- Additional source-described series:
  - Coin/BTC vs BTC correlation;
  - Coin vs Coin/BTC correlation;
  - optional Coin vs USDT.D correlation;
  - optional Coin vs BTC.D correlation.
- The source notes multi-timeframe capability through `request.security()`.

The source does **not** specify a complete long/short entry, exit, holding period, re-entry rule, position sizing rule, stop, or portfolio-construction rule. Those elements are underspecified.

Research-proposed operationalization for falsification only:

1. Treat the primary correlation state as a regime variable, not a standalone directional signal.
2. Compare forward relative returns (`coin return - BTC return`) after transitions into low-correlation, high-correlation, and inverse-correlation states.
3. Separately condition simple coin/BTC relative momentum and reversal signals on those states.
4. Repeat the entire test using correlations of log returns rather than price levels.
5. Stress lookbacks around the source default rather than optimizing one best value.

These operationalizations are research-proposed and are not claimed by the source.

## Required data

- Liquid crypto assets with continuously tradable Coin/USDT (or comparable USD-stablecoin) history.
- BTC benchmark price on a consistent venue or defensible consolidated benchmark.
- Coin/BTC cross rate, either directly observed or reconstructed point-in-time from synchronized prices.
- Optional BTC.D and USDT.D series only for tests of the source's optional contextual lines.
- Timestamp-aligned close prices at the selected bar frequency.
- Point-in-time symbol availability and delisting history to avoid survivorship bias.
- Consistent candle boundaries and timezone across all series.

## Execution assumptions

The source does not specify execution mechanics. For any later test, signal formation must use only fully closed bars and orders should be modeled no earlier than the next executable bar unless a stricter point-in-time model is justified.

Fees, spread, slippage, impact, capacity, order type, partial fills, leverage, funding, borrow/short availability, and venue failures are not specified by the source and remain data/execution gaps.

## Evidence

### Source-reported

The source provides interpretation thresholds and usage guidance but does not report a traceable backtest, Sharpe ratio, CAGR, drawdown, win rate, or other independently auditable performance statistic. It describes low Coin-vs-BTC correlation as a potential alpha opportunity and correlation shifts as regime changes; these are source claims, not verified profitability evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No source-reported backtest establishes that low correlation predicts positive absolute or relative returns.
- Correlation is symmetric and non-directional; a low value alone does not specify which asset should outperform.
- Correlation of non-stationary price levels can generate misleading relationships.
- Coin/USDT, BTC/USDT, and Coin/BTC are mechanically linked by triangular pricing, so some of the displayed relationships are not independent economic signals.
- Low correlation may be caused by illiquidity, stale prices, listing events, or idiosyncratic volatility rather than exploitable information.
- No independent reproduction was performed during this Scout run.

## Falsification plan

1. **Price-level spurious-correlation test:** reproduce the source-compatible close-price correlation and compare it with rolling log-return correlation using the same lookback and smoothing. If the apparent regime effect disappears under returns, reject the price-level alpha interpretation.
2. **Directionality test:** measure forward absolute and BTC-relative returns after low-correlation transitions. If conditional return distributions are indistinguishable from unconditional controls after multiple-testing correction, reject the predictive-regime hypothesis.
3. **Incremental-information test:** compare against rolling BTC beta, raw return correlation, coin/BTC momentum, coin momentum, BTC momentum, realized volatility, and liquidity. Reject the transformation if it adds no stable out-of-sample information.
4. **Ablation:** test the primary Coin-vs-BTC correlation alone before adding Coin/BTC, BTC.D, or USDT.D context. Added lines must improve out-of-sample results rather than merely increase in-sample fit.
5. **Parameter neighborhood:** stress correlation lookbacks around 50, 70, 100, 150, and 200 bars and smoothing around the source default of 5. A result that survives only one precise setting is treated as overfit.
6. **Regime robustness:** evaluate bull, bear, high-volatility, low-volatility, high-BTC-dominance, and altcoin-led periods separately.
7. **Cross-sectional robustness:** require the effect across multiple liquid assets and leave-one-asset-out tests; reject a result driven by one token or listing episode.
8. **Point-in-time controls:** enforce synchronized closes, actual historical listing availability, and no future symbol membership.
9. **Cost sensitivity:** any directional strategy derived from the regime must survive realistic fees, spread, slippage, and funding/borrow where applicable.
10. **Failure action:** if low-correlation states do not provide stable out-of-sample incremental information beyond simple return correlation/beta and relative momentum, reject the correlation-decoupling layer rather than adding complexity.

## Crypto portability

`direct`

The source itself is designed for cryptocurrency pairs and explicitly uses BTC, Coin/BTC, USDT.D, and BTC.D relationships. Portability across crypto venues remains unproven because exchange-specific closes, stablecoin basis, listing history, liquidity fragmentation, and 24/7 candle boundaries can materially alter rolling correlations.

## Limitations

- `underspecified`: no complete trading lifecycle is supplied.
- `not independently reproduced`: no independent empirical verification in this Scout run.
- `data gap`: exact venue/symbol choices and historical availability must be fixed point-in-time before testing.
- `unproven`: low correlation is labeled an alpha opportunity by the source, but no source backtest demonstrates predictive returns.
- Potential spurious regression/correlation from price levels is a first-order methodological risk.
- Optional dominance series may have provider-specific construction and revision issues.

## Implementation status

Research-only normalization. No Qlib implementation or full backtest has been completed for this record.

## Adoption boundary

This record is external research material only. It has not passed Research Intake Review, entered the production candidate pool, completed Qlib validation, become a frozen survivor or leaderboard entry, or been approved for Paper, Testnet, or Live trading.

## Related Wiki records

- [[cryptocurrency-correlation-network-consensus-clustering-mpt-2026-09-17]]
- [[crypto-cross-sectional-betting-against-beta-2026-08-31]]
- [[crypto-cross-sectional-price-delay-information-diffusion-2026-08-31]]
- [[tradingview-crypto-tri-align-ema-slope-relative-strength-2026-09-19]]

## Sources

- TradingView, Frey_Crypto, **Crypto Correlation Oscillator**, published 2025-11-08, reviewed 2026-09-23: https://www.tradingview.com/script/V8xTszSe-Crypto-Correlation-Oscillator/
