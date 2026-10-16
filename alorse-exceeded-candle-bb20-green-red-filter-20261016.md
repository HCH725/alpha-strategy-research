---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse Exceeded Candle with BB20 and two-earlier-red-bars veto"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/Exceeded%20candle.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse Exceeded Candle with BB20 and two-earlier-red-bars veto

## Provenance

Primary complete Pine v4 source: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/Exceeded%20candle.pine. Immutable source revision `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, path `strategies/mean-reversion/Exceeded candle.pine`. The source is a long-flat strategy with `pyramiding=0`, initial_capital=1000, default sizing 10% of equity, commission 0.01% per side, and no process_orders_on_close override.

This record is an EXPLICITLY DERIVED EXECUTION version of the full Alorse signal, NOT a source-native Pine market-fill reproduction. Researcher chooses BTC-USDT Binance **spot** on 1h closed candles, no margin/funding; fill on the NEXT completed candle's CLOSE using the Hummingbot OrderExecutorSimulator MARKET path instead of Pine's default next-bar-open. Signals/formulas are unchanged; fill timing, static stake and spot venue are researcher choices, not source claims. No author timeframe is a strategy requirement.

## Economic mechanism

Bullish reversal below Bollinger middle line: current green candle exceeds prior red candle's open, but the two still earlier candles cannot both be red. A held long exits only after close exceeds the upper band. This differs from a generic Bollinger breakout or simple 1-3-1 reversal.

## Signal

Exact Pine inputs: `src=close`, `length=20`, `mult=2.0`, `basis=sma(close,20)`, `dev=2*stdev(close,20)`, `upper=basis+dev`, `lower=basis-dev`.

- `greenLastCandle[t] = close[t-1]<open[t-1] AND close[t]>open[t] AND close[t]>open[t-1]`.
- `last3red[t] = close[t-2]<open[t-2] AND close[t-3]<open[t-3]`: despite its misleading name, it tests **only t−2 and t−3**. Prior t−1 red is separately guaranteed by greenLastCandle.
- `buyEntry[t] = greenLastCandle[t] AND close[t]<basis[t] AND NOT last3red[t]`.
- `buyExit[t] = close[t]>upper[t]`.
- `strategy.entry("Long",true,when=buyEntry)`; `strategy.close("Long",when=buyExit)`. Original Short lines are commented out, therefore **no shorts**. No stop loss, target order, trailing, time exit, cooldown, safety orders or multiple positions. While long, another entry is a no-op; after flat, the next qualifying pattern re-enters.
- Entry and exit are mutually exclusive by strict comparisons since `close<basis` contradicts `close>upper=basis+nonnegative_dev`. Thus no entry-versus-exit same-bar priority ambiguity exists.
- `redLastCandle` is a display-only annotation.

## Required data

Single pair completed OHLC; no volume-dependent signal, multi-timeframe request, synthetic candles, lookahead or fitted model. Warmup 20 full bars (SMA/stdev20 and t−3 candle history); until then stay flat. Bar t signal is available after bar t closes. Only historical and current t prices are used; no t+1 information enters the signal.

## Execution assumptions

Version assessed: spot BTC-USDT, connector `binance`, candle feed `binance/BTC-USDT/1h`; isolated leverage/futures funding not applicable to SPOT. 1000 USDT starting capital and constant 100 USDT notional initial BUY per entry (10% of initial capital, no compounding); quantize order BTC quantity downward to the connector trading-rule base increment, reject orders below min notional rather than simulate partial phantom fills. Exit SELL is exactly remaining BTC amount, never naked short. Source's percent-of-current-equity sizing vs this fixed initial capital stake is a disclosed economic derivation.

Decision/fill clock: compute source signal on fully completed t; on simulation row t+1 use ONLY the source signal from t (one-candle shifted features). The simulator's MARKET order enters or exits at row t+1 CLOSE, not t+1 OPEN. Last signal without a following completed candle remains pending/not filled. No same-row close-signal/close-fill shortcut or lookahead. One long and one flat transition maximum; no other action when already long or flat.

Real code-path evidence read at `HCH725/hummingbot` fork commit `2dbc844fadb9d863b3ab0af1b8ab100472102e42`:

- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase.run_backtesting`, `prepare_market_data` provide timestamped completed OHLCV, loop `simulate_execution` calls controller `determine_executor_actions()` per row, routes `OrderExecutorConfig` to `OrderExecutorSimulator`; `BacktestPositionHold` nets BUY versus SELL, reports realized PnL and cum fees.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: MARKET fills at first simulation row timestamp **at its close price**; quote fees `trade_cost * filled_amount_quote`, returns `POSITION_HOLD` executor.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`: connector/pair/interval feed keys, `initialize_trading_rules`, base-quantity/price quantization.
- Actual MARKET `CreateExecutorAction` plus `OrderExecutorConfig` construction already exists in `controllers/generic/pmm_mister.py` and the existing backtesting engine. Minimal strategy-specific `ControllerBase` signal logic is **not yet implemented** (implementation_status reflects this), but no adapter/compiler/new system is introduced.
- `run_backtesting(...backtesting_resolution="1h", trade_cost=0.0001)`: fixed simulated **0.01% per filled side** matching the source's numerical commission input. This is a frozen *research approximation*, NOT an assertion about actual Binance fee tier, maker queue, spread, slippage or realized fills; no missing futures funding is silently zeroed since the adopted spot venue has no perpetual funding contract.
- Required Hummingbot pinned admission baseline is package `20260920`, VERSION `dev-2.17.0`. Fork commit evidence is code-level; reviewer MUST independently confirm these exact primitives exist in the mandated pinned package. Do NOT treat more recent master alone as successful Gate 5 validation.

## Evidence

Primary original Pine code read in full; no source-reported performance, no independently executed trades, no HB parity, and no live economics are claimed. Exact signal defaults and stopped/disabled behavior are source-backed. Spot market, fixed initial stake and shifted same-close fills are explicit derivatives.

## Falsification plan

Bar-by-bar source-rule recomputation over OHLC, assert no entries before warmup or while already long, exit only when `close>upper`. On execution, verify pending event from t is applied strictly to t+1 close, fee 0.0001 per side, exact quantity netting, and source next-open-to-derived next-close price difference. Any unverified pinned-engine detail is a HOLD, not automatic PASS.

## Crypto portability

No rule depends on BTC, 1d or the author's benchmark horizon; this one derivative pins spot BTC-USDT 1h only to make the six-gate executable scope reviewable. Other coin/frame studies and house 3x/5x isolated futures with DCA are separate, explicitly parameterized execution studies, NOT part of this candidate's source or admitted economics.

## Limitations

No source stop; gap and crash risk. Position may remain open indefinitely before an upper-band exit. Spot quote-fee model excludes real spread/slippage, and fork master is not proof of pinned package parity.

## Implementation status

`not-implemented`. No Qlib, Hummingbot backtest, n8n, deployment or live trading touched.

## Adoption boundary

`research-only`, `not-approved`. Proposed PASS is conditional on actual independent six-gate audit, especially pinned-engine Gate 5; do not merge on unverified assumption.

## Sources

- Original: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/Exceeded%20candle.pine
- Engine code: https://github.com/HCH725/hummingbot/tree/2dbc844fadb9d863b3ab0af1b8ab100472102e42
- Policy: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
