---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView growbharat2005 EMA9/20 crossover EMA200-gated close/EMA20-cross exit derived long-flat BTCUSDT 1h"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/fURZdvM1-Long-Only-EMA-Strategy-9-20-with-200-EMA-Filter/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView growbharat2005 EMA9/20 crossover + EMA200 regime, long-flat BTCUSDT 1h (explicit derivative)

## Provenance and immutable research identity

- **Primary TradingView publication:** https://www.tradingview.com/script/fURZdvM1-Long-Only-EMA-Strategy-9-20-with-200-EMA-Filter/ ; script ID `fURZdvM1`; author **growbharat2005**; published **2025-12-03**; public descriptive text checked **2026-10-25**.
- **Research identity (frozen):** `TV-fURZdvM1 | derived-EMA9-20-cross-EMA200-regime-close20-exit | BTCUSDT-Binance-spot-1h | v1 | 2026-10-25`. This pins *this researcher's rule*, not a cryptographic snapshot of the original mutable TradingView Pine.
- **Source facts directly recoverable from the public description:** three EMAs of 9, 20, 200; long-only; enter when EMA9 crosses **above** EMA20 while **close > EMA200**; exit when **close crosses below EMA20**; intended standard candles; source explicitly describes no shorts. The author says the strategy is configurable and can be applied across symbols and frames, and suggests potential future protective additions. No original full Pine listing, exact `strategy()` order-fill flags, source position size, commission or default risk-order code was independently recovered in this cycle. “Open-source script” labeling is **not** a claim that the complete source bytes were retrieved.
- **Explicit independent derived strategy — NOT lossless Pine reconstruction.** The researcher fixes BTCUSDT spot 1h, a particular EMA seed and cross comparison, completed-bar MARKET-close research fills, a 220-completed-bar warmup, one fixed BTC unit, flat/long position state, disabled protective orders, fees, and a close-time audit clock. Those choices are **researcher-designed** where the source does not fully specify them. The described entry and exit mechanism itself is retained, but Pine fill/size/risk defaults are **not** asserted.
- The source script is an immutable **identifier** only; source prose may later change. Do not silently infer missing original Pine semantics. This version is frozen independently of later author edits.

## Economic mechanism

**Source-reported:** a short-term EMA9/EMA20 bullish crossover triggers only above the long-term EMA200 regime; a close/EMA20 downward crossover cuts the position. The author describes trend-following participation and exit on lost medium-term structure, not a statistically validated edge.

**Research hypothesis (not source performance):** the slow EMA200 regime gate vetoes bullish fast/medium crosses during a long-term downtrend; the independent close-under-EMA20 exit can terminate the long *before* the EMA9 crosses back below EMA20. This is not the same machine as an ungated two-EMA crossover or an ADX-gated EMA20/50 cross.

## Signal — exact derived executable specification

Only Binance **BTCUSDT spot** completed, contiguous **1h** OHLCV bars are used. All three averages use **close**, no adjusted/Heikin-Ashi source. Index `t` denotes a completed bar. Seed each EMA at the first available close `EMA_L[0]=close[0]`, and for every `t>=1` calculate `EMA_L[t] = (2/(L+1))*close[t] + (1-2/(L+1))*EMA_L[t-1]` for `L=9,20,200`. No fitted coefficients, parameter search, external data or future samples. Full contiguous input history and seed are part of reproducibility.

```text
fast_up[t] = EMA9[t-1] <= EMA20[t-1] AND EMA9[t] > EMA20[t]
regime[t]  = close[t] > EMA200[t]                  // strict; equality does not pass
exit20[t]  = close[t-1] >= EMA20[t-1] AND close[t] < EMA20[t]

eligible[t] = t >= 220 AND history contiguous and all required closes finite

if not eligible[t]: NO NEW SIGNAL; no fabricated price or fill
else if state == LONG and exit20[t]:
    SELL exactly Q BTC at modeled completed-bar close[t]; state -> FLAT
else if state == FLAT and fast_up[t] and regime[t]:
    BUY exactly Q BTC at modeled completed-bar close[t]; state -> LONG
else:
    HOLD unchanged
Q = 0.001 BTC (researcher sizing; fixed base units, not percent of equity)
```

- Direction: **LONG / FLAT only**. No short, reverse, or hedged exposure.
- Entry: strict EMA9-over-EMA20 crossover, with previous-bar equality permitted, plus strict `close>EMA200` on the **same completed bar**. A crossover rejected by the regime gate does **not** trigger a delayed entry on a later bar merely because the regime subsequently turns positive; a fresh fast/medium crossover is required.
- Exit: strict `close` cross **below** EMA20, previous equality permitted. Exit ignores EMA200 and EMA9; a regime failure or EMA9 cross-down **alone** does not exit. A downward close cross while FLAT is a no-op. There is no stop loss, take profit, trailing, time-based close, scale-out, liquidation rule, or discretionary override. These are expressly **disabled in this derivative**, not presumed original Pine defaults.
- Priority: check the exit while LONG, otherwise check entry while FLAT. A LONG cannot add; a FLAT cannot sell. No same-bar close-and-reenter, even if theoretical predicates overlap. No averaging, safety orders, pyramiding, DCA, martingale, cooldown, shared-capital sizing, position-dependent indicator inputs or multiple simultaneous positions.
- State initialization: FLAT at the start. First **220 completed bars** (indices 0 through 219) are flat warmup, first eligible decision at index 220; EMAs are still recursively updated throughout warmup. After any exit, only a new eligible `fast_up` can re-enter, no next-bar auto-entry. At predetermined research-window end, report any remaining open position marked to the final available close; **do not invent a forced exit trade**. Any run that cannot supply the full necessary contiguous history is incomplete and not claimable.
- Only these declared defaults form version v1. Variants of EMA length, source, market, timeframe, order timing, size, protective risk or DCA are **different research configurations** and cannot silently replace this record.

## Required data, warmup and point-in-time causality

- One Binance spot pair `BTC-USDT`, interval `1h`, candle open timestamp, `open/high/low/close/volume` from the pinned candle adapter; the signal itself reads only **close** and the one-hour time grid. No cross-asset, higher-timeframe, order-book, funding, open-interest, news or external indicator input.
- Binance/Hummingbot raw candle `timestamp` is **bar-open time**, not the time the close became known. Signal and modeled fill are audit-stamped at **`raw_open_timestamp + 3600 seconds`**, after the bar has completed. The engine's raw simulated fill label remains bar-open; preserve both fields rather than asserting that the raw label proves causal availability.
- The same-bar-close MARKET fill is a **backtest convention**, not an assertion that an exchange can see the final close and guarantee a fill at that exact close in live trading. No next-open, intrabar stop, limit-maker queue or partial-fill model is required by this specifically defined derivative.
- Missing or non-finite bar prices, duplicate timestamps, a gap in the hourly grid, or insufficient warmup are **fail-closed data defects**: do not synthesize candles, shift a signal, silently carry a new fill across a gap, or claim a complete replay. Do not infer an unobserved close. The backtest must flag the affected run as incomplete rather than manufacture economics.
- All calculations use completed current and past bars; no future extrema, negative shifts, repainting, fitted full-sample parameters, incomplete HTF candle, or lookahead. Warmup 220 is a **researcher choice**, not an author default or proof of exact EMA convergence.

## Execution assumptions — pinned Hummingbot code-level compatibility

**Pinned admission baseline:** package `20260920`, `hummingbot/VERSION = dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. These source paths were read from the GitHub connector at this exact commit for this cycle (not inferred from product documentation):

1. **Market/candles:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1h` in `INTERVALS`; `binance_spot_candles/binance_spot_candles.py` builds Binance spot kline requests with `symbol` and `interval`, and parses REST `row[0]` or WS `k.t` as candle **open** timestamp. The controller must consume only completed bars, normalize availability to `open+3600`, and must not treat a still-forming WS update as final.
2. **Action/fill path:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` loops `update_state(row)` then `controller.determine_executor_actions()`, handling `CreateExecutorAction`. The `OrderExecutorConfig` / `OrderExecutorSimulator.simulate` path in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` supports `ExecutionStrategy.MARKET`, fills on the first supplied row's **close**, and writes `filled_amount_quote = amount * entry_price`, `cum_fees_quote = trade_cost * amount_quote`, with `CloseType.POSITION_HOLD`. The simulator's fill timestamp is the supplied row's **open label**; compare at normalized effective close time, not as an exchange timestamp.
3. **Position accounting:** `BacktestPositionHold` is defined in `backtesting_engine_base.py`. Its BUY/SELL netting tracks `net_amount_base`, average entry price, realized gross quote PnL and accumulated `cum_fees_quote` separately. A future controller must own a deterministic FLAT/LONG state plus filled-event ledger and not infer its state solely from the engine's terminated executor list or a delayed `positions_held` view. No new controller is implemented by this research PR.
4. **Sizing and economics:** fixed `Q=0.001 BTC` per BUY/SELL, spot `BTC-USDT`, no leverage/margin/liquidation; **futures funding is inapplicable** rather than a fabricated zero-realized-funding stream. Declare `trade_cost=0.001` (0.1% of quote notional) **per simulated side**. Modeled slippage `0.0` means only that this simulator prices MARKET fills at the input close; **not** that real-market slippage is zero. Research fee-adjusted PnL is gross realized quote PnL minus the sum of both legs' `cum_fees_quote`; `net_pnl_quote` from an individual MARKET executor is not the complete cash/equity ledger. The simulator's float arithmetic does not establish exchange precision, minimum-notional compliance, or a live fill guarantee.
5. **Capability boundary:** one symbol, one 1h candle stream, a three-EMA state machine and one close-priced BUY/SELL leg per signal. No next-open, intrabar, maker, multi-timeframe, shared capital, short or futures path is required. The code-level primitives are compatible with this **declared derivative**; the exact controller and event-level parity remain unimplemented and untested. A separate representative parity test is required before large-scale Qlib screening if this path is not already verified; no candidate-specific parity is asserted by this record.

## Six-gate HB_READY evidence for independent Hermes Auditor

1. **Determinism:** fixed EMA9/20/200 recursion, close input, equality/strictness, fixed warmup, crossover and position-state logic; no learned or discretionary signal.
2. **Direction:** Binance spot long/flat only, explicit short prohibition.
3. **Entries/exits/risk:** complete gated EMA cross entry, independent close/EMA20 cross exit; protective stops, targets, trailing, timeouts and discretionary exits expressly disabled.
4. **Position/re-entry:** Q=0.001 BTC, exactly one position, no adds/DCA, no cooldown, fresh crossover required, FLAT/LONG transitions and exit-first priority.
5. **Pinned engine/data:** Hummingbot package/version/commit, BinanceSpotCandles 1h, controller/action/OrderExecutor MARKET-close path, raw vs effective timestamps, BacktestPositionHold ledger, per-side modeled fees, spot funding N/A and float/precision/slippage limitations pinned to actual code. Static path evidence only; no claim of a running implementation.
6. **Causality:** 220 completed-bar warmup, trailing EMA recursion, strict hourly grid, no future inputs, close-effective time normalization, fail-closed gaps.

**PASS in this file is a proposed Scout admission status, not an independent audit verdict.** Only the independent Hermes Auditor may validate all six gates and approve an exact-head merge; if material compatibility or source-fact gaps remain, the automated research PR must be closed as NOT_LOSSLESS. It grants no Qlib parity, profitability, Survivor, HB Certified or Paper/Testnet/Live permission.

## Evidence, dedup, limitations and falsification

- **Source-reported:** the TradingView author text supplies the three lengths, crossover-plus-regime entry, close/EMA20 exit and long-only intent. No original Pine byte snapshot or source backtest metrics were retrieved; no source `process_orders_on_close`, fee, position size, pyramiding or risk defaults are asserted.
- **Independently reproduced:** none. No strategy backtest, simulator execution, actual fills, Qlib parity or trade was performed in this Scout cycle. Static GitHub source inspection is **not** a substitute for an engine test.
- **Dedup on `main` SHA `4deefd8ed820a3559b1ae0e2ec69da1c63475f82` (312 root-level records; README counter 312):** GitHub code search for exact `fURZdvM1` and author `growbharat2005` returned no main hit; GitHub PR search for `fURZdvM1` returned no PR. Open research PRs were reviewed for source/mechanism. The existing `ema-20-50-cross-btcusdt-1h-2026-10-06.md` is an **ungated EMA20/50 entry and EMA20/50 cross-down exit**; `forven-ema-cross-adx-regime-long-flat-btcusdt-1h-2026-10-19.md` uses EMA20/50 with ADX14≥20 and EMA200 gate, exiting on **EMA20/50 cross-down**; `golden-cross-sma-regime-gated-long` is a **SMA** 9/50/100 cross mechanism. This candidate instead has EMA9/20 gated by EMA200, exiting on **close crossing EMA20**, a materially different exit and entry event map rather than a parameter-only re-label.
- **Source limitations:** the TradingView page exposes the author's public description but not a complete recoverable Pine source listing in this cycle; therefore this is **not** lossless source-native. TradingView script ID plus observation date are provenance, not immutable source-code bytes. The entire proposed strategy is separately frozen in this record.
- **Execution limitations:** modeled same-bar-close execution and fees are research conventions, not exchange-realized prices/costs. No protective stop means adverse trends can persist until the close/EMA20 exit. Missing data invalidates the run. The 0.001 BTC unit may violate exchange-specific filters at some prices; no real order is authorized. The static engine code path is not a claim of a strategy-specific HB implementation.
- **Falsification plan (downstream only):** compare EMA seed/warmup behavior, inspect all cross-equality boundaries, validate that failed EMA200 gates do not late-enter, validate that close/EMA20 exit can precede EMA9/20 cross-down, audit raw/open versus normalized/close timestamps, reconcile both-side fees and position ledger, and test full-history/OOS without tuning from final OOS. Do not promote hypothetical source-reported performance.

## Implementation and adoption boundary

`implementation_status: not-implemented`; `status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. No executable controller, Qlib strategy, Hummingbot deployment, n8n workflow, backtest or live-trading permission is created by this record. House BO6/SO6/SO6, 7-symbol 42-cell research and isolated 3×/5× are **optional later campaign experiments** and are **not** this spot single-unit strategy or admission prerequisites. If applied, declare a separately derived execution configuration with its own event/economic evidence.
