---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse MTF RSI source-signal RSI14 under30 with EMA900 long-only, duplicate keyword normalized"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/MTF%20RSI.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse MTF RSI source-signal RSI14 under30 with EMA900 long-only, duplicate keyword normalized

## Provenance, explicit source defects and derivative boundary

Original whole file read at `Alorse/pinescript-strategies@8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, `strategies/MTF RSI.pine`: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/MTF%20RSI.pine. Title is **MTF RSI**, but the source executable order logic makes ZERO `request.security` or `security` multi-timeframe calls; it computes RSI and MA on its chart's own close. Do not invent a second timeframe because of the filename.

Original declaration literally `strategy("MTF RSI", overlay=true, overlay=true, pyramiding=0, ..., default_qty_value=20, commission_value=0.01)`. Repeated identical `overlay=true` keyword appears TWICE, which is a **Pine v5 compilation defect** (duplicate named argument). Source is not claimed to compile unmodified. The research *syntax-only* derivation removes the second redundant keyword and preserves all source indicators, thresholds, order conditions and single-long state. This is an explicitly declared separate syntactic repair, NOT an invented trading strategy improvement. No source code is modified in Alorse repository. Source initial_capital 1000 USD and 20%-current-equity position sizing are recorded; our selected fixed 200 USDT initial-capital entry allocation is an additional disclosed economic derivative.

## Economic mechanism

An RSI14 oversold long is permitted only when price remains above a very long EMA900 secular-regime anchor. Position held until RSI14>70 or price falls below EMA900. Different from a plain RSI30/70 reversal or a fast-EMA filter; signal does **not** require RSI to *cross* 30 (it is a LEVEL predicate), and does not require 900-minute or other HTF candles.

## Signal — original rules, unchanged by the declaration repair

- `lenRSI=14`; `rsi_overbought=70`, `rsi_oversold=30`. `RSI=ta.rsi(close,14)`.
- `ma_type='EMA'` (SMA optional, inactive), `ma_length=900`; `ma=ta.ema(close,900)`.
- `longEntry[t] = close[t]>ma[t] AND RSI[t]<30`. Both strict.
- `longExit[t] = RSI[t]>70 OR close[t]<ma[t]`. Both strict; equality never triggers.
- Live calls `strategy.entry('Long',strategy.long,when=longEntry)` and `strategy.close('Long',when=longExit)`. No short side, price stop, TP limit, trailing, time exit, cooldown, safety order or portfolio state. Source `pyramiding=0` suppresses repeated entry while held; later qualifying longEntry after flat opens again.
- Entry and exit can cofire on one bar only if RSI<30 and RSI>70 (impossible) or close>ma and close<ma (impossible); so no entry/exit action-priority ambiguity.
- Source inputs `overlay=true` duplicated are display-only duplicate identical values, removed once; no other source line deleted/rewritten.
- Conservative research `930` complete 1h candles flat warmup for EMA900 and RSI14 numeric stabilization, explicitly researcher-adopted rather than a source input. Only past and current completed close, no MTF, no intrabar price and no lookahead/repaint.

## Pinned execution, data, costs and position

Research execution derivative: `BTC-USDT` spot `binance` on `1h` completed candles, not original source-specific timeframe selection. Generate decision from completed t OHLC and execute BUY (when flat) or SELL of the full actually filled BTC amount (when held) as MARKET at NEXT simulated candle `t+1` CLOSE, using source-t boolean cached/shifted strictly one bar. This differs from Pine strategy's native t+1 OPEN fill; no t+1 signal may control its own t+1 fill. If last signal lacks a following bar, no fill. 1000 USDT initial capital, fixed 200 USDT source-adjusted research notional/position (20% initial, differs from source 20% equity), amount quantized down to Binance spot tick/step, skip if invalid min-notional instead of phantom fill. Simulated `trade_cost=0.0001` one-way (0.01% matching nominal source commission numerically), **not** actual fee tier or implicit slippage. No futures funding/margin/liquidation because **spot**; house 3x/5x and BO/SO DCA different research scope.

Pinned Hummingbot native source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, 2026-09-20 UTC, `hummingbot/VERSION=dev-2.17.0` confirms VERSION of canonical package 20260920. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` `run_backtesting(backtesting_resolution='1h',trade_cost=0.0001)` merges historical OHLCV features, loops row by row and calls controller `determine_executor_actions()`, then routes `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET at first-row CLOSE, fee `trade_cost*filled_amount_quote`, `POSITION_HOLD`; `BacktestPositionHold._process_order` nets equal BTC BUY/SELL with realized PnL and fees. `BacktestingDataProvider` loads `binance_BTC-USDT_1h` OHLC and real connector trading rules/quantization. `controllers/generic/pmm_mister.py` demonstrates native MARKET `OrderExecutorConfig` use. EMA900 calculation/controller **not yet coded into Hummingbot**, implementation_status not-implemented; this is source-backed admission of supported primitive, not deployed strategy.

Version-pinned pre-existing engine tests inspected (NOT executed): `test_backtest_position_hold.py` `test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`; `test_backtesting_final_tick_ledger.py` spot Binance OrderExecutor POSITION_HOLD and closing-tick accounting; `test_backtesting_engine_directional.py` Binance candle/action flow. No invented fill or profit result. Potential historical candle fetch count must include 930+ bars; a particular backtest dataset not demonstrated here, so the reviewer must verify the bounded capacity in canonical engine rather than assume magic 500-bar defaults prohibit it.

## Evidence

Original source v5 read in full including duplicate keyword; only redundant identical display argument removed. No source profit/reproduction asserted. Main contains RSI strategy families but a literal 900-close EMA regime and level-based RSI30 entry/RSI70-or-EMA900 exit is not the same fixed signal as existing fast-EMA gated reversal.

## Falsification plan

Prove removing duplicate identical `overlay=true` cannot change price series or strategy order conditions. Reconstruct ta.rsi(close,14), ta.ema(close,900) with trailing complete candles, assert strict level conditions and no short; no trades before 930-bar warmup. One-bar next-close fill delay and 0.0001 per-side fee, consistent quantity netting and no naked short. Distinguish source 20% rolling equity and original next-open from derived fixed initial stake and next-close fills. Verify actual data-provider initialization fetch can hold the 930-bar history; if not, Gate5 remains HOLD.

## Crypto portability

No literal second timeframe dependency: despite its name MTF RSI, one 1h close history is sufficient. Other symbols/4h/1d and futures economics require separate declared experiments.

## Limitations

Unmodified source has a duplicate Pine strategy keyword and cannot be claimed compiled as-is. EMA900 can gate very long histories; this is a declared syntactic and execution derivative, not bit-identical source trading implementation. Research fixed-rate trade cost excludes spread/slippage; no historical strategy backtest claimed.

## Implementation status

`not-implemented`; no live GitHub engine/Qlib/n8n/deployment edits.

## Adoption boundary

`research-only`, `not-approved`. Independent reviewer must validate source facts and declared correction, exact canonical engine Gate5 and sufficient OHLC history; no unverified PASS merge.

## Sources

- Original https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/MTF%20RSI.pine
- Pinned Hummingbot VERSION https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Pinned tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Existing admission contract https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
