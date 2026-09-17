---
schema: strategy-research-record-v1
title: "TradingView Bitcoin Leverage Sentiment: Z-Score Normalized Bitfinex Margin Long/Short Ratio Strategy"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - tradingview
  - sentiment
  - margin-positioning
  - long-short-ratio
  - z-score
  - bitfinex
status: research-only
confidence: low
source_as_of: 2024-02-28
sources:
  - "TradingView public strategy: 'Bitcoin Leverage Sentiment - Strategy [presentTrading]', https://www.tradingview.com/script/nqHXDfp1-Bitcoin-Leverage-Sentiment-Strategy-presentTrading/ (published 2024-02-28; accessed 2026-09-17; open-source Pine Script v5)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bitcoin Leverage Sentiment: Z-Score Normalized Bitfinex Margin Long/Short Ratio Strategy

## Provenance

- **Source URL**: https://www.tradingview.com/script/nqHXDfp1-Bitcoin-Leverage-Sentiment-Strategy-presentTrading/
- **Title**: Bitcoin Leverage Sentiment - Strategy [presentTrading]
- **Author**: PresentTrading (TradingView verified author)
- **Type**: Public open-source TradingView strategy script (Pine Script v5)
- **License**: Mozilla Public License 2.0 (https://mozilla.org/MPL/2.0/)
- **Immutable script identifier**: `PUB;360b40ff16744393b1d441386b9d4113` (version 1)
- **Publication date**: 2024-02-28T17:15:32Z
- **Review / as-of date**: 2026-09-17
- **Reference chart / demo context**: `BINANCE:BTCUSDT` on 240m (4-hour) timeframe

## Economic mechanism

### Source-reported

The author posits that trading based on market sentiment derived from leveraged positions provides a predictive advantage over traditional price-action indicators. Specifically:

1. **Leveraged position ratio**: The strategy tracks the ratio of leveraged long positions to the sum of leveraged long and short positions (`ratioBTC = priceLongs / (priceLongs + priceShorts)`), where `priceLongs` is fetched from `BTCUSDLONGS` and `priceShorts` from `BTCUSDSHORTS`.
2. **Sentiment standardization**: Because raw position levels drift across market regimes, the ratio is standardized via a rolling Z-score: `Z = (ratioBTC - meanRatioBTC) / stdDevRatioBTC` over a customizable period.
3. **Sentiment momentum & exhaustion**: The author assumes that extreme positive deviations (Z > 1.0) reflect dominant bullish sentiment warranting a long entry, while extreme negative deviations (Z < -1.618) reflect pervasive bearish sentiment warranting a short entry. Long exits occur when sentiment turns severely negative (Z < -1.618), and short exits occur when sentiment recovers to bullish levels (Z > 1.0).

### Research interpretation

The hypothesized economic mechanism is a **leveraged positioning momentum vs. crowded-trade liquidation thesis**:

1. **Positioning momentum (author's thesis)**: In trending phases, aggressive leveraged participants accumulate positions ahead of spot momentum. Rising margin longs indicate speculative confidence and capital commitment that drives upward spot drift.
2. **Crowded trade / cascade vulnerability (microstructure critique)**: In cryptocurrency derivatives, extreme skew in leveraged positioning (Z > 1.0) frequently marks a crowded trade susceptible to cascading long liquidations rather than persistent upside drift. Conversely, deeply negative positioning (Z < -1.618) can trigger short squeezes. The author's directional momentum rule (entering long on high long ratios) stands in direct tension with contrarian liquidation-cascade dynamics.
3. **Asymmetric threshold heuristic**: The choice of +1.0 for long entry and -1.618 for short entry incorporates the golden ratio (φ = 1.618) as a heuristic threshold rather than an economically derived boundary. The asymmetry reflects a built-in bullish bias tailored to Bitcoin's secular upward drift.
4. **Venue segmentation & information decay**: `BTCUSDLONGS` and `BTCUSDSHORTS` originate from Bitfinex margin books. While Bitfinex was an institutional bellwether in 2017–2019, modern crypto leverage has shifted overwhelmingly to perpetual swaps on Binance, Bybit, and OKX, meaning Bitfinex margin data captures a diminishing slice of aggregate market leverage.

## Signal

### Formation timestamp

- **Bar interval**: 4-hour bars (`240m` chart resolution; `timeframeInput` defaults to chart timeframe).
- **Evaluation timing**: Signals are evaluated at the close of each 4H bar after fetching closing values of `BTCUSDLONGS` and `BTCUSDSHORTS` via `request.security()`.
- **Execution timestamp**: Tradable at subsequent bar open (`research-proposed execution timing`).

### Lookback

- **Z-Score period**: `zScoreCalculationPeriod = 252` bars (source-reported default; at 4H resolution, 252 bars equal 1,008 hours / 42 days).
- **SMA and Stdev**: `meanRatioBTC = ta.sma(ratioBTC, 252)`, `stdDevRatioBTC = ta.stdev(ratioBTC, 252)`.
- **Sampling**: Continuous rolling window, inclusive of the latest bar close.

### Long entry

- **Trigger**: `conditionLongEntry = ta.crossover(zScoreBTCRatio, thresholdLongEntry)`
- **Threshold**: `thresholdLongEntry = 1.0` (source-reported default).
- **Direction gate**: `tradeDirection == "Long"` or `tradeDirection == "Both"` (source-reported default is `"Both"`).
- **Order execution**: `strategy.entry("Long", strategy.long)`

### Long exit

- **Trigger**: `conditionLongExit = ta.crossunder(zScoreBTCRatio, thresholdLongExit)`
- **Threshold**: `thresholdLongExit = -1.618` (source-reported default).
- **Order execution**: `strategy.close("Long")`

### Short entry

- **Trigger**: `conditionShortEntry = ta.crossunder(zScoreBTCRatio, thresholdShortEntry)`
- **Threshold**: `thresholdShortEntry = -1.618` (source-reported default).
- **Direction gate**: `tradeDirection == "Short"` or `tradeDirection == "Both"`.
- **Order execution**: `strategy.entry("Short", strategy.short)`

### Short exit

- **Trigger**: `conditionShortExit = ta.crossover(zScoreBTCRatio, thresholdShortExit)`
- **Threshold**: `thresholdShortExit = 1.0` (source-reported default).
- **Order execution**: `strategy.close("Short")`

### Holding period

- Variable holding period driven by cross-threshold duration. Because lookback is 252 bars (42 days) and thresholds are placed at +1.0 and -1.618 standard deviations, positions typically remain open for days to several weeks (`research-proposed characterization`).

### Position sizing & money management

- **Capital base**: $10,000 initial capital (`initial_capital = 10000`, `currency = currency.USD`).
- **Sizing rule**: Fixed cash order size of $10,000 (`default_qty_type = strategy.cash`, `default_qty_value = 10000`).
- **Pyramiding**: 0 (single position per side; no stacking).

## Required data

- **Traded instrument**: Bitcoin against USD/USDT spot or perpetual (`BINANCE:BTCUSDT` in demo).
- **External data feeds**:
  - `BTCUSDLONGS`: Bitfinex Bitcoin margin long open position volume (source-reported).
  - `BTCUSDSHORTS`: Bitfinex Bitcoin margin short open position volume (source-reported).
- **Venue**: Bitfinex for margin metrics; primary spot/perpetual venue for traded asset.
- **Timeframe**: 4H (`240m`) aggregation.
- **Point-in-time & lookahead considerations**:
  - In Pine Script, `request.security(symbol, "", close)` evaluates bar close synchronously with current chart bars when `timeframeInput` matches chart resolution, avoiding future leakage. However, if a higher timeframe is supplied without `barmerge.lookahead_off`, lookahead bias can occur (`research-proposed audit note`).
  - Bitfinex margin data updates periodically; live execution requires validating whether exchange-published margin metrics update with delay relative to spot ticks (`research-proposed data gap`).
- **Missing data handling**: No imputation logic is provided in the source script; missing feed values propagate nulls into the Z-score calculation.

## Execution assumptions

### Source-reported

- **Initial capital**: $10,000 USD
- **Order size**: $10,000 USD (100% of initial equity on non-compounded cash basis)
- **Commission**: 0.1% per trade (`commission_value = 0.1`, `commission_type = strategy.commission.percent`)
- **Slippage**: 1 tick (`slippage = 1`)
- **Fill model**: Standard Pine Script next-bar open fill simulation upon crossover condition.

### Research-proposed operational rules

- **Signal-to-order timing**: Market order submitted at next bar open (t+1) following the 4H bar close (`research-proposed`).
- **Short borrow & interest rate**: The source omits borrow fees for spot short positions; a live spot implementation would incur continuous borrow interest (`research-proposed limitation`).
- **Perpetual funding rate**: Porting to perpetual futures incurs 8-hour funding payments, which are not modeled in the source script (`research-proposed operational rule`).
- **Liquidity & capacity filter**: Minimum 24h spot volume > $100M USD on the traded pair to absorb $10,000 market orders without adverse price impact (`research-proposed universe filter`).

## Evidence

### Source-reported

- **Published charts**: The author provides three visual trade chart snapshots:
  - BTC 4h L/S Performance: `https://www.tradingview.com/x/Tlhc5kIk/`
  - Local chart detail: `https://www.tradingview.com/x/iBWodHyp/`
  - Z-score visualization: `https://www.tradingview.com/x/2YNO4pSG/`
- **Quantitative claim provenance gap**: The author states that the default settings provide a "balanced approach to leverage sentiment trading" but does not report numeric backtest summary statistics (e.g., net profit percentage, annual Sharpe ratio, profit factor, maximum drawdown, or trade count) in the published text. Quantitative figures are omitted here rather than invented.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Market share decay of Bitfinex**: Academic and industry literature confirms Bitfinex's share of aggregate Bitcoin leverage dropped drastically from >50% in 2017 to <5% by 2024, replaced by perpetual contracts on Binance, OKX, and Bybit. A signal derived exclusively from Bitfinex margin books carries structural obsolescence risk.
- **Liquidation cascade vulnerability**: High leveraged long ratios (Z > 1.0) frequently correspond to late-cycle speculative euphoria, leaving positions exposed to catastrophic downside wick liquidations before any crossunder exit can trigger.
- None identified in the source listing; absence is not evidence of no negative result.

## Falsification plan

Research-defined falsification tests (not source-reported):

1. **Cross-venue positioning vs. single-venue Bitfinex test**:
   - *Test data*: Compare signals derived from Bitfinex `BTCUSDLONGS`/`BTCUSDSHORTS` against Binance Top Trader Long/Short Ratio (Accounts) and aggregated Perpetual Futures Open Interest skew over 2021–2026.
   - **Research-defined falsification threshold**: If the Bitfinex-derived signal produces annualized Sharpe ≤ 0.0 while Binance perpetual long/short ratios generate statistically significant positive risk-adjusted returns (or vice versa), the single-venue Bitfinex metric is falsified as unrepresentative idiosyncratic noise.
2. **Contrarian squeeze vs. momentum ablation test**:
   - *Test logic*: Invert the strategy's entry rules (Short on Z > 1.0, Long on Z < -1.618) to evaluate whether crowded leverage creates mean-reverting squeeze alpha rather than momentum alpha.
   - **Research-defined falsification threshold**: If the contrarian (fade-the-crowd) implementation achieves higher net Sharpe and lower maximum drawdown than the source momentum rule across ≥ 100 round-trip trades on BTC 4H, the author's positioning-momentum thesis is falsified in favor of a liquidation-exhaustion thesis.
3. **Friction and funding stress test**:
   - *Test logic*: Evaluate strategy performance under realistic perpetual swap execution: 0.05% taker fee, 0.05% slippage, and cumulative historical 8-hour funding rates.
   - **Research-defined falsification threshold**: If net cumulative return drops by > 50% or the strategy becomes net unprofitable after incorporating funding rates and taker fees, the signal lacks operational viability.
4. **Rolling window & threshold sensitivity perturbation**:
   - *Test logic*: Perturb `zScoreCalculationPeriod` across {126, 180, 252, 300, 365} and thresholds across {±0.75, ±1.0, ±1.5, ±1.618, ±2.0}.
   - **Research-defined falsification threshold**: If Sharpe flips negative across more than 40% of parameter permutations, the default (252, +1.0, -1.618) combination is classified as sample-specific data mining.

## Crypto portability

- **Portability classification**: **Adapted** (the strategy is authored natively on Bitcoin, but depends on Bitfinex spot margin borrowing data; adapting it to the primary modern crypto liquidity venue—centralized perpetual futures—requires substituting exchange-wide perpetual long/short account ratios or funding rates).
- **Perpetual futures considerations**:
  - In perpetual futures markets, long skew is continuously taxed via positive funding rates paid from longs to shorts. A long-holding strategy during extended high-sentiment regimes suffers compounding funding drag.
  - 24/7 continuous session structure applies natively, with 4-hour bar timestamps aligned to UTC candle boundaries (00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC).
- Crypto portability is not authorization to trade.

## Limitations

- **Underspecified empirical track**: The author did not publish numeric performance tables, trade frequency, win rates, or drawdown metrics in the text.
- **Data dependency on legacy exchange**: Strong reliance on `BTCUSDLONGS` and `BTCUSDSHORTS` on Bitfinex limits scalability and introduces survivorship/relevance risk.
- **Asymmetric heuristic thresholds**: Entry/exit thresholds (+1.0 and -1.618) lack theoretical grounding beyond Fibonacci numerology and may be overfit to historical bull cycles.
- **Confidence**: **Low**.

## Implementation status

- `not-implemented` in `nautilus-quant-system` or PyBroker.
- No historical backtest or production pipeline has been created.
- Not authorized for Paper, Testnet, or Live execution.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Capturing this record into the alpha-strategy-research repository serves purely as a normalized research asset for potential future hypothesis synthesis. It does not imply strategy viability, profitability, or permission to deploy capital.

## Related Wiki records

- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
- `volume-profile-breakout-poc-reclaim-continuation-2026-09-17.md`
- `tradingview-hyper-sar-reactor-adaptive-psar-logistic-af-2026-09-17.md`
- `tradingview-fluxvector-liquidity-dlp-vol-curvature-impact-efficiency-2026-09-17.md`
- `usdt-premium-dual-regime-crisis-safe-haven-flight-crypto-2026-09-17.md`

## Sources

1. PresentTrading, *Bitcoin Leverage Sentiment - Strategy [presentTrading]*, TradingView public open-source Pine Script v5 strategy, published 2024-02-28, reviewed 2026-09-17. URL: https://www.tradingview.com/script/nqHXDfp1-Bitcoin-Leverage-Sentiment-Strategy-presentTrading/
2. TradingView Pine Facade API, immutable script record `PUB;360b40ff16744393b1d441386b9d4113`, Version 1, inspected 2026-09-17. URL: https://pine-facade.tradingview.com/pine-facade/get/PUB;360b40ff16744393b1d441386b9d4113/1
