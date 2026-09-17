---
schema: strategy-research-record-v1
title: "TradingView Crypto Volatility Bitcoin Correlation: Dual Volatility Expansion (VIXFix + BitMEX BVOL7D) with 50 EMA Trend Filter"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - bitcoin
  - bvol7d
  - vixfix
  - volatility-expansion
  - ema-trend-filter
status: research-only
confidence: low
source_as_of: 2024-10-05
sources:
  - "https://www.tradingview.com/script/B0skL3uT-Crypto-Volatility-Bitcoin-Correlation-Strategy/"
  - "https://pine-facade.tradingview.com/pine-facade/get/PUB;02c9f7642e0746f58a509df292371655/1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Volatility Bitcoin Correlation: Dual Volatility Expansion (VIXFix + BitMEX BVOL7D) with 50 EMA Trend Filter

## Provenance

- **Primary Source URL:** `https://www.tradingview.com/script/B0skL3uT-Crypto-Volatility-Bitcoin-Correlation-Strategy/`
- **Pine Facade API / Script Identifier:** `PUB;02c9f7642e0746f58a509df292371655` (Version 1.0)
- **Publication Title:** *Crypto Volatility Bitcoin Correlation Strategy* (referenced in source header comments as *Bitcoin Volatility Master Strategy*)
- **Author:** `exlux` (TradingView public author, Pro Premium)
- **Publication Date:** 2024-10-05T22:39:31Z (captured and verified: 2026-09-17)
- **License:** Mozilla Public License 2.0 (MPL-2.0)
- **Implementation Artifact:** Public open-source TradingView Pine Script v5 strategy (`strategy(..., overlay=true)`)
- **Primary Tested Asset:** `COINBASE:BTCUSD` (tested on daily timeframe `1D`)

## Economic mechanism

### Source-reported

1. **Market Volatility Timing:** The strategy is designed to capitalize on large impulse movements in Bitcoin by identifying periods of expanding volatility that align with an established directional trend.
2. **Dual Volatility Confirmation:**
   - *Synthetic Price Volatility (`VIXFix`):* Measures distance between the highest close over a 22-bar lookback and the current low relative to the 22-bar high: $\text{VIXFix} = ((\text{Highest}(\text{Close}, 22) - \text{Low}) / \text{Highest}(\text{Close}, 22)) \times 100$. Rising VIXFix ($\text{VIXFix} > \text{VIXFix}[1]$) indicates increasing price dispersion and range expansion.
   - *Derivatives Implied/Realized Volatility (`BVOL7D`):* Ingests `BITMEX:BVOL7D` (BitMEX 7-Day Bitcoin Volatility Index). An upward slope ($\text{bvol7d} > \text{bvol7d}[1]$) indicates that external derivatives-market volatility is expanding.
3. **Directional Trend Confirmation:** A 50-period Exponential Moving Average (`EMA(50)`) filters market regime. When price trades above the EMA ($\text{Close} > \text{EMA}(50)$), an uptrend is confirmed.
4. **Long Entry & Exit Alignment:** Positions are entered only when both volatility measures are accelerating in an uptrend, and closed immediately when price falls below the 50-period EMA.

### Research interpretation

- **Hypothesized Mechanism:** Volatility breakout continuation conditioned on intermediate trend regime. Rather than trading purely price breakouts or oscillator oversold reversals, the thesis posits that simultaneous acceleration in synthetic price-range dispersion (VIXFix) and external exchange-wide derivatives volatility (BitMEX BVOL7D) during an established uptrend signals an expansion regime that provides positive drift.
- **Component Roles in Composite Structure:**
  - *Regime Filter 1 (Internal Volatility):* 22-period synthetic VIX Fix acceleration ($\text{VIXFix}_t > \text{VIXFix}_{t-1}$).
  - *Regime Filter 2 (External Volatility):* 7-day BitMEX volatility index acceleration ($\text{BVOL7D}_t > \text{BVOL7D}_{t-1}$).
  - *Directional Filter:* 50-period EMA trend boundary ($\text{Close}_t > \text{EMA}_{50, t}$).
  - *Exit Trigger:* 50-period EMA breakdown ($\text{Close}_t < \text{EMA}_{50, t}$).
- **Structural Tension:** The Williams VIX Fix was originally developed by Larry Williams as a synthetic inverted VIX for bottom-picking equities (spiking on panic selloffs). In this crypto strategy, the author repurposes VIXFix as a general volatility expansion indicator; however, because VIXFix increases when `Low` drops relative to the 22-bar high, the entry condition $\text{VIXFix}_t > \text{VIXFix}_{t-1}$ while $\text{Close}_t > \text{EMA}_{50, t}$ effectively selects candles that print wider downward wicks or intraday range expansions while closing above the 50 EMA. Whether this conveys genuine predictive alpha over a simple ATR or Donchian expansion requires strict ablation.

## Signal

### Source-reported logic (Pine Script v5 specification)

1. **Parameters & Inputs (Source-Reported):**
   - `symbol = input.symbol("COINBASE:BTCUSD", title="Bitcoin Symbol")`
   - `symbol_volatility_index = input.symbol("BITMEX:BVOL7D", title="Bitcoin Volatility Index (7D)")`
   - `VIXFixLength = input.int(22, title="VIX Fix Length")`
   - `emaLength = input.int(50, title="EMA Length")`

2. **Data Ingestion via Security Calls:**
   ```pinescript
   close_ = request.security(symbol, timeframe.period, close)
   low_ = request.security(symbol, timeframe.period, low)
   bvol7d = request.security(symbol_volatility_index, timeframe.period, close)
   ```

3. **Feature Formulations:**
   $$\text{VIXFix}_t = \frac{\max_{i=0,\dots,21}(\text{close}_{t-i}) - \text{low}_t}{\max_{i=0,\dots,21}(\text{close}_{t-i})} \times 100$$
   $$\text{EMA}_{50, t} = \text{EMA}(\text{close}_t, 50)$$

4. **Entry Trigger (Source-Reported):**
   $$\text{longCondition}_t = (\text{VIXFix}_t > \text{VIXFix}_{t-1}) \land (\text{bvol7d}_t > \text{bvol7d}_{t-1}) \land (\text{close}_t > \text{EMA}_{50, t})$$
   Executed as: `strategy.entry('Long Position', strategy.long, when=longCondition)`

5. **Exit Trigger (Source-Reported):**
   $$\text{exitCondition}_t = \text{close}_t < \text{EMA}_{50, t}$$
   Executed as: `strategy.close("Long Position", when=exitCondition)`

6. **Short Logic:** None. Strategy is exclusively long-only.

### Operational overlay and execution timing (`research-proposed`)

Because the source Pine Script code relies on default TradingView simulation behavior without specifying live routing, order types, or slippage, any formal quantitative evaluation requires `research-proposed` operational rules:
- **Signal Formation Timestamp (`research-proposed`):** Calculated on daily bar close at UTC 00:00:00 upon receipt of final daily tick and finalized BVOL7D index close.
- **Order Timing and Fill Model (`research-proposed`):** Market order executed at next-bar open (UTC 00:00:01) to eliminate same-bar intrabar lookahead bias.
- **Position Sizing Model (`research-proposed`):** Fixed 1.0x unleveraged allocation of current portfolio equity (100% equity on long signal, 0% on exit).
- **Protective Stop-Loss (`research-proposed`):** 2.5x ATR(14) catastrophic trailing stop below entry price, addressing the source-acknowledged gap where price could suffer major drawdowns before breaching the 50-day EMA.

## Required data

- **Primary Instrument:** Bitcoin spot or perpetual contract (`COINBASE:BTCUSD` or `BINANCE:BTCUSDT`).
- **External Volatility Index:** Daily closing series of `BITMEX:BVOL7D` (BitMEX 7-day rolling annualized volatility index) or modern exchange equivalent (`DERIBIT:DVOL` / `DERIBIT:BTC_DVOL`).
- **Data Fields:** Daily OHLCV for primary instrument; daily Close for volatility benchmark.
- **Point-in-Time & Synchronization:** Primary asset and external volatility index must be synchronously timestamped to UTC 00:00:00 without post-hoc retrospective revisions.
- **Missing Data Policy (`research-proposed`):** If `BVOL7D` feed is missing, halted, or stale for $>1$ trading day, suppress new entries (`fail-closed`).

## Execution assumptions

### Source-reported

- TradingView default backtesting engine assumptions.
- No commission model, slippage, order routing delay, or execution margin is specified in the script (`strategy()` declaration specifies only `overlay=true`).

### Research-proposed assumptions

- **Execution Venue (`research-proposed`):** Binance BTCUSDT perpetual or Coinbase BTC-USD spot.
- **Fee Model (`research-proposed`):** 5 bps taker fee per side (10 bps round-trip) for spot; 2 bps taker / 0 bps maker for perpetual contracts.
- **Slippage Model (`research-proposed`):** 2.5 bps modeled slippage on market orders.
- **Funding Cost (`research-proposed`):** Continuous 8-hour funding cashflows applied to open positions if evaluated on perpetual futures contracts.
- **Latency (`research-proposed`):** 500 ms fill delay after UTC 00:00:00 bar closure.

## Evidence

### Source-reported

- The author states that the strategy was tested on the Bitcoin daily timeframe (`1D`) to capture longer-term trends and volatility spikes.
- **Quantitative Performance Data Gap:** The source publication contains **no explicit performance table, backtest metric summary, win rate, Sharpe ratio, maximum drawdown, or CAGR figure**. This is recorded explicitly as a **source-reported provenance gap**; no quantitative profitability claim is made by the source.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **VIXFix Inversion in Strong Trends:** The VIXFix metric reaches minimum values during sustained low-volatility grinding uptrends. Requiring $\text{VIXFix}_t > \text{VIXFix}_{t-1}$ means the strategy systematically rejects clean, low-drawdown momentum runs, entering only after a wide-range bar or pullback.
- **Single-Bar Differencing Noise:** Using a simple 1-bar slope test ($\text{VIXFix}_t > \text{VIXFix}_{t-1}$ and $\text{bvol7d}_t > \text{bvol7d}_{t-1}$) is prone to whipsaws caused by single-day noise spikes in volatile consolidation regimes.
- **Deprecation / Thin Volume of BitMEX BVOL7D:** BitMEX BVOL7D has experienced declining relevance and intermittent data feed availability compared to options-implied volatility indices like Deribit DVOL, creating potential data fragility.
- None identified in the reviewed source documentation itself; absence is not evidence of no negative result.

## Falsification plan

Research-defined operational tests to evaluate or reject the core mechanism:

1. **External Volatility (BVOL7D) Incremental Value Test:**
   - Run an ablation backtest comparing the full strategy against an ablated variant omitting `BVOL7D` ($\text{Close}_t > \text{EMA}_{50, t} \land \text{VIXFix}_t > \text{VIXFix}_{t-1}$).
   - **Research-defined falsification threshold:** If adding `BVOL7D` fails to improve the net-of-friction Sharpe ratio by at least $0.15$ or reduces net profit over 2018–2026 BTC data, the BitMEX BVOL7D filter is falsified as non-load-bearing.

2. **Synthetic Volatility (VIXFix) Ablation Test:**
   - Compare the strategy against a classic benchmark: simple 50 EMA trend following ($\text{Close}_t > \text{EMA}_{50, t}$).
   - **Research-defined falsification threshold:** If the VIXFix rising condition reduces total risk-adjusted return (Calmar ratio or Sharpe) compared to the simple EMA baseline across $\ge 100$ trades, the VIXFix requirement is falsified as noise-inducing.

3. **Modern Volatility Proxy Robustness Test:**
   - Replace `BITMEX:BVOL7D` with `DERIBIT:DVOL` (Deribit 30-day implied volatility index) and 7-day realized Parkinson volatility.
   - **Research-defined falsification threshold:** If substituting modern volatility benchmarks causes strategy performance or trade direction to degrade into negative expectancy, the signal is sensitive to venue-specific historical artifacting.

4. **Transaction Cost & Slippage Stress Test:**
   - Evaluate strategy returns under parametric fee/slippage scaling: 0, 10, 20, 30, and 50 bps round-trip.
   - **Research-defined falsification threshold:** If net profit expectancy per trade falls below zero at $\le 15$ bps round-trip cost, the strategy is falsified as economically unviable.

## Crypto portability

- **Portability status:** `direct`
- **Portability Rationale:** The strategy was designed, coded, and demonstrated natively for cryptocurrency markets (`COINBASE:BTCUSD` and `BITMEX:BVOL7D`).
- **Crypto-Specific Operational Dynamics:**
  - *Perpetual Funding Rate Drag:* In perpetual markets, periods of expanding volatility combined with bullish price action above the 50 EMA typically coincide with positive funding spikes, creating substantial holding cost drag for long positions.
  - *Cross-Venue Latency & Discrepancy:* BitMEX index calculation methodologies differ from Binance or Deribit index prices; discrepancies between spot venues and derivatives volatility indices can cause signal desynchronization.
  - *24/7 Continuous Session:* Unlike traditional equities where VIXFix operates across daily market opens/closes, crypto 24/7 trading requires rigorous adherence to standardized candle alignment (UTC 00:00:00).

## Limitations

- **Absence of Source Performance Metrics:** No third-party empirical backtest statistics are reported by the author.
- **Underspecified Risk Controls:** The source lacks any protective stop-loss, profit target, or dynamic position sizing, leaving capital exposed during large trend-breakdown candles.
- **External Indicator Dependency:** Strong coupling to `BITMEX:BVOL7D` creates vulnerability to exchange feed discontinuations or historical API gaps.
- **Parameter Rigidity:** Fixed window parameters (22-period VIXFix, 50-period EMA, 7-day BVOL) without reported parameter stability or walk-forward verification.
- **Long-Only Vulnerability:** The strategy cannot exploit downward volatility expansions during bear market phases.

## Implementation status

- **Current Status:** `not-implemented`
- **Stack Scope:** Research capture only. No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader exists.
- **Not Authorized:** Not approved for Paper, Testnet, or Live execution.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Capturing this research record does not imply strategy adoption, statistical profitability, or implementation approval.

## Related Wiki records

- `tradingview-btc-volatility-band-pullback-2026-09-17.md`
- `tradingview-btc-volatility-adjusted-momentum-zscore-2026-09-17.md`
- `tradingview-dual-phase-vol-regime-fast-slow-oscillator-2026-09-17.md`
- `tradingview-fluxvector-liquidity-dlp-vol-curvature-impact-efficiency-2026-09-17.md`
- `tradingview-hyper-sar-reactor-adaptive-psar-logistic-af-2026-09-17.md`
- `tradingview-quantum-flux-entropy-efficiency-vol-squash-gain-2026-09-17.md`
- `crypto-l2-liquidity-state-transitions-order-flow-2026-09-01.md`

## Sources

- **Primary Source Listing:** https://www.tradingview.com/script/B0skL3uT-Crypto-Volatility-Bitcoin-Correlation-Strategy/
- **Script ID Part:** `PUB;02c9f7642e0746f58a509df292371655` (Version 1.0)
- **Direct Pine Facade API Source:** https://pine-facade.tradingview.com/pine-facade/get/PUB;02c9f7642e0746f58a509df292371655/1
- **Author:** `exlux` (TradingView verified public script author; published 2024-10-05T22:39:31Z; captured and verified 2026-09-17)
- **Underlying Conceptual Lineage:**
  - Williams, Larry (1998): *Long-Term Secrets to Short-Term Trading*, John Wiley & Sons (synthetic VIX Fix formulation).
  - BitMEX Research (2018): *BVOL7D Index Specification* (7-day annualized rolling volatility index based on Bitcoin 1-minute prices).
