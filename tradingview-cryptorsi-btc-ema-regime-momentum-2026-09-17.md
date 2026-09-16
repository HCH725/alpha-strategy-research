---
schema: strategy-research-record-v1
title: "TradingView CryptoRSI BTC-Regime Momentum"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/cvosgS3M/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView CryptoRSI BTC-Regime Momentum

## Provenance

Public TradingView open-source strategy **CryptoRSI** by **Konscio**, published 2026-03-05 and reviewed as of 2026-09-17. Stable source URL: https://www.tradingview.com/script/cvosgS3M/

The source describes a long-only cryptocurrency strategy combining RSI momentum extremes on the traded symbol with a BTC daily trend-regime filter and a mechanical exit. The normalized record below uses only logic explicitly described on the public TradingView page; it does not reproduce or redistribute the Pine source.

## Economic mechanism

### Source-reported

The author describes the strategy as seeking participation in strong upside phases after momentum becomes extreme. It combines an RSI entry rule, a market-regime filter based on BTC relative to its EMA, and a mechanical exit. The author explicitly notes that the framework does not guarantee results and that crypto markets can produce long streaks of false signals.

### Research interpretation

The falsifiable hypothesis is a **conditional momentum-continuation effect**: an unusually strong RSI state in an individual crypto asset may contain more continuation information when the broader crypto market, proxied by BTC, is already in a positive daily trend regime.

Component roles:

- **Regime:** `BITSTAMP:BTCUSD` daily close above EMA(50).
- **Primary signal:** RSI on the traded symbol exceeds the preset buy threshold.
- **Signal smoothing:** Original preset smooths RSI with an SMA; exact smoothing parameters are not stated on the public description.
- **Exit / risk logic:** Original exits below WMA(50); Agressif exits when RSI falls below its sell threshold.

The BTC regime filter and RSI trigger should be ablated separately in later research; their combination should not be assumed to provide incremental alpha without testing.

## Signal

Source-specified normalized logic:

1. Long-only strategy.
2. Compute RSI on the traded symbol.
3. If the default market filter is enabled, allow entries only while `BITSTAMP:BTCUSD` on the **Daily** timeframe is above its **EMA(50)**.
4. **Original preset:** RSI is SMA-smoothed; enter long when the resulting RSI exceeds the preset Buy Threshold. Exit when price crosses below WMA(50).
5. **Agressif preset:** uses faster RSI and higher thresholds according to the author; enter long when RSI exceeds its Buy Threshold and exit when RSI drops below its Sell Threshold.
6. No short-entry rule is described.

**Underspecified:** the public description does not expose the exact RSI length, Original SMA smoothing length, Original/Agressif buy thresholds, Agressif RSI length, Agressif sell threshold, chart timeframe for the traded symbol, exact cross/close confirmation semantics, re-entry behavior, or position sizing. These must not be guessed.

**Research-proposed operationalization:** first reproduce the two presets only after their exact public Pine parameters can be independently inspected and pinned. For leakage-safe testing, the BTC daily regime value available to an intraday traded-symbol bar should use only the most recently completed BTC daily bar unless the source code explicitly establishes another point-in-time-safe convention.

## Required data

- Traded crypto instrument OHLCV sufficient to compute RSI and WMA.
- `BITSTAMP:BTCUSD` daily OHLC data sufficient to compute EMA(50).
- Exact traded-symbol timeframe: **underspecified** in the public description.
- Timestamp alignment between the traded symbol and BTC daily regime series.
- Point-in-time availability of the BTC daily regime value must be preserved; no future daily close may leak into earlier intraday decisions.
- Venue and market type for the traded symbol are not constrained by the public description and therefore remain **underspecified**.

## Execution assumptions

The author explicitly states that the displayed backtests assume **frictionless execution with no fees and no slippage**.

The public description does not specify market versus limit orders, same-bar versus next-bar fills, spread, impact, funding, borrow, leverage, latency, partial fills, or failure handling. Those assumptions are therefore **underspecified** and must be modeled explicitly before any validation.

For perpetual-futures adaptation, funding and venue-specific fees would be material and cannot be omitted merely because the source backtest omits them.

## Evidence

### Source-reported

The public TradingView description explains the rule framework and qualitative distinction between the Original and Agressif presets. It does not provide a source-traceable Sharpe ratio, CAGR, drawdown, win rate, or other quantitative performance statistic in the reviewed description, so none is recorded here.

The author states that Original is smoother/more selective and that Agressif is faster with more signals and more noise. These are author characterizations, not independently verified findings.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself warns that crypto markets can produce long streaks of false signals and states that its backtests omit fees and slippage. No independent negative study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Recover and pin the exact preset parameters from the public source before implementation; fail closed if they cannot be reconstructed.
2. Test across a broad, point-in-time crypto universe rather than only hand-selected survivors.
3. Compare the combined rule against: RSI trigger alone; BTC EMA(50) regime alone; simple buy-and-hold; and a generic time-series momentum baseline.
4. Ablate the BTC regime filter to test whether it adds information beyond the traded asset's own momentum.
5. Test Original and Agressif separately rather than pooling their outcomes.
6. Use walk-forward/OOS evaluation and multiple market regimes, including major crypto drawdowns and sideways periods.
7. Apply realistic fees, spread/slippage and, for perpetuals, funding.
8. Reject or materially weaken the hypothesis if the combined rule fails to improve risk-adjusted OOS behavior versus its simpler controls after realistic costs, or if results are concentrated in a small number of assets/regimes.

## Crypto portability

**direct** — the source explicitly presents CryptoRSI as a cryptocurrency strategy and uses BTC itself as the market-regime series.

Portability still depends on instrument type and venue. Spot and perpetual implementations can differ because of funding, fees, liquidity and mark/index conventions. Crypto's 24/7 structure also makes the definition and point-in-time availability of the BTC daily candle important.

## Limitations

- Exact preset RSI lengths and thresholds: **underspecified**.
- Original RSI smoothing parameter: **underspecified**.
- Traded-symbol timeframe: **underspecified**.
- Entry/exit bar confirmation and fill timing: **underspecified**.
- Position sizing and re-entry: **underspecified**.
- Source backtest omits fees and slippage.
- Cross-symbol daily-regime alignment requires leakage-safe implementation.
- Not independently reproduced.

## Implementation status

No implementation in our research stack has been completed. No PyBroker/Qlib or other formal historical validation is implied by this record.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — Konscio, **CryptoRSI**, published 2026-03-05, reviewed 2026-09-17: https://www.tradingview.com/script/cvosgS3M/
