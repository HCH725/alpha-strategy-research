---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Alors MACD+RSI 5-bar washout-memory cross long-flat on BTCUSDT 1h (lag-1 OrderExecutor mapping)
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-25
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/MACD+RSI.pine
  - https://github.com/Alorse/pinescript-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alors MACD+RSI 5-bar washout-memory cross long-flat on BTCUSDT 1h (lag-1 OrderExecutor mapping)

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/Alorse/pinescript-strategies (open-source Pine strategy collection; the lane that supplied the admitted `alorse-bb-aroon`, `alorse-bb-winner-lite`, `alorse-dmi-winner`, `alorse-exceeded-candle`, `alorse-flawless-victory`, `alorse-kodify-bb350`, `alorse-macd-dmi14-vstop20`, `alorse-mtf-rsi14-ema900`, `alorse-qqe-first-trail`, `alorse-stochrsi-supertrend-ema200`, `alorse-supertrend-rsi50`, and `alorse-williams-vix-fix` records — this is only its thirteenth record, and the first pinned to this exact file).
- Pinned commit SHA: `8fb3837ddcd137f1450c3e82d654ff3df24d54d5` (committed `2026-08-25T11:48:57Z`; record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `strategies/momentum/MACD+RSI.pine`.
- GitHub blob SHA at the pinned commit: `3367b11cbe535f8321fc792746764a98a5db1edb`, size 2380 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2380 bytes, 53 lines, SHA-256 `80d128599079ef753682cf6cf251630f656f172d4fea7195f74e31a95273931b`, identical to the GitHub blob (`git hash-object` reproduces `3367b11c…5db1edb`) — the entire file was retrieved and inspected.
- Authorship note (fenced, no gate effect): the header comment credits `fredoorse` while the file lives in the Alorse collection; identity here is file path plus blob, both unique.
- The file's own words (quoted for gate evidence, never extended): `//@version=4`; header `strategy(title="MACD + RSI Strategy [Alorse]", overlay=true, shorttitle="MACD+RSI STRTG", pyramiding=0, currency=currency.USD, default_qty_type=strategy.percent_of_equity, default_qty_value=100)`; MACD defaults `fast_length=12`, `slow_length=26`, `signal_length=9` with `sma_source="EMA"` and `sma_signal="EMA"` defaults; RSI `len=14` on `src=close`; washout memory `rsiBack=5`, `rsiDown=30`, `rsiUp=70`; loops `for i = 1 to rsiBack` testing `rsi[i] <= rsiDown` into `wasRsiDown` and `rsi[i] >= rsiUp` into `wasRsiUp`; `bull_cross = crossover(macd, signal) and wasRsiDown`; `bear_cross = crossunder(macd, signal) and wasRsiUp`; `strategy.entry("Long", strategy.long, when=bull_cross)`; `strategy.close("Long", when=bear_cross)`; `SL = 99 * 0.01` with `StopPrice = strategy.position_avg_price * (1 - SL)` and `if (strategy.position_size > 0) strategy.exit(id="Exit", stop=StopPrice)`; `TP = 10` input declared and never referenced by any order call (dead input, fenced below); `// strategy.entry("Sell", strategy.short, when=bear_cross)` commented out (the only `strategy.short` token lives in that comment).
- Out-of-file calls pinned (all resolved by name, all standard Pine v4 builtins): `ema`/`sma` (selected by the `EMA` defaults — no override anywhere in the file); `rsi(src, len)` (Pine v4 Wilder-RMA RSI, period 14 — no override); `crossover`/`crossunder` (standard edge: `a[1] <= b[1] and a > b` and its mirror — causal two-bar comparison, disclosed, never redefined). No `request.security`, no `request.*`, no multi-timeframe read, no `volume` read, no Heikin-Ashi, no repaint-prone `security` lookahead.
- Full-file token census (verified over the 53 lines this cycle): 0 `security` / 0 `request` (single timeframe, no external feed); 0 `volume` (RSI reads `close` only; MACD reads `close` only); 2 `strategy.entry` (one live long, one commented short); 1 `strategy.close` (the live long exit); 1 `strategy.exit` (the 99% stop only); 1 `pyramiding` (the `=0` header literal); 0 `trailing` / 0 `time` exit / 0 `limit` order (the `TP` input never reaches any order call); 1 `strategy.short` (comment-only, fenced); 0 `hyperopt` / 0 `Parameter` (no fitted values anywhere).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live TradingView deployment. The source pins the MACD(12,26,9)-cross-plus-5-bar-RSI-memory entry conjunction, the mirrored memory-gated exit, the `pyramiding=0` stance, the long-only book (short leg commented out), and the 99%-stop disaster backstop — but ships no venue spelling, no fill-timing flag, no warmup guard, and no base-asset sizing rule. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` spot `1h` (the file names no market or timeframe; venue spelling, symbol normalization, and frame choice are the only market steps, and no source-market equivalence is claimed); (2) lag-1 causal information set with row-close MARKET fills via the OrderExecutor path (decision at tick `i` reads only bars `<= i-1`; fills land on row `i` close — derivation disclosed with exact line-level engine mapping below, never presented as the Pine broker emulator's own next-open timing); (3) fixed `0.001` BTC base-quantity position pin with hold-no-op semantics plus a 60-bar researcher warmup floor (the file carries no base sizing and no length guard — disclosed, never presented as source-native behaviour); (4) the 99% stop evaluated on lagged row closes only, never intrabar (evaluation-path pin, disclosed); (5) the source's absent sizing/costs ride explicit model pins (`trade_cost=0.001`/side, continuous unquantized accounting, spot with no funding leg) while the house `6%+6%+6%` DCA campaign overlay is explicitly excluded from this admission version (see Execution assumptions). This record is therefore never evidence that the original Pine strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `macd+rsi`, `fredoorse`, `wasRsi`, and `rsiBack` returns zero strategy records — no record in the 302-record pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian ratio) trades a MACD-cross-plus-RSI-memory conjunction edge. MACD cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the single bar where MACD crosses up through its signal line together with an RSI washout printed somewhere in the prior five bars (`rsi <= 30` on any of `rsi[1..5]`); close the long the single bar where MACD crosses down through its signal line together with an overheated RSI in the prior five bars (`rsi >= 70` on any of `rsi[1..5]`). A fixed 99% stop backstops every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Rotation-edge machine with a five-bar oscillator memory, long-only. The MACD-cross leg supplies timing (momentum rotation confirmed on the decision bar) while the RSI-memory leg vetoes rotations printed without a recent washout — so a cross fired after five calm bars prints nothing, and a fresh washout without a rotation prints nothing either. Unlike single-bar conjunction records (which demand the oscillator state on the crossing bar itself), each leg here consults a trailing five-bar window that excludes the decision bar (`rsi[1..5]`), so the memory is already one step lagged in the source. The exit mirrors the construction with an asymmetric overbought threshold (70 versus 30): the book is held through every non-crossing bar by design, and even a death-cross bar is held unless the memory confirms recent heat. The exit is deliberately narrower than a pure cross-down rule — both the rotation AND the memory are required — so a scheme that exits on either leg alone would be a different, unpinned rule.

## Signal

Exact rule as pinned (any other MACD/RSI periods, thresholds, memory length, strictness, edge-vs-state pairing, stop handling, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; MACD periods are the file's own input defaults (12/26/9, EMA path) and the RSI period is the file's own input default (14, Pine v4 Wilder RMA), disclosed, never overridden in the file:

```text
fast[t]   = EMA(close, 12)[t]
slow[t]   = EMA(close, 26)[t]
macd[t]   = fast[t] - slow[t]
signal[t] = EMA(macd, 9)[t]
rsi[t]    = Wilder-RMA RSI(close, 14)[t]
wasDown[t] = ANY(rsi[t-k] <= 30 for k = 1..5)   // excludes decision bar, source-native
wasUp[t]   = ANY(rsi[t-k] >= 70 for k = 1..5)   // excludes decision bar, source-native
bull[t] = (macd[t-1] <= signal[t-1] is FALSE framing — precisely: macd[t-1] > signal[t-1] AND macd[t-2] <= signal[t-2]) AND wasDown[t-1]
bear[t] = (macd[t-1] < signal[t-1] AND macd[t-2] >= signal[t-2]) AND wasUp[t-1]
entry_sig[i] = bull evaluated with decision bar = i-1   // lag-1: tick i reads bars <= i-1 only
exit_sig[i]  = bear evaluated with decision bar = i-1   // lag-1: tick i reads bars <= i-1 only
stop_sig[i]  = positioned AND (close[i-1] <= 0.01 * avg_entry_price)  // 99% row-close backstop, lagged
floor = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `entry_sig=1` on a tick whose lagged decision bar prints the cross-up edge plus washout memory, `direction` long-only; `exit_sig=1` (or `stop_sig=1`) on a tick whose lagged decision bar prints the cross-down edge plus heat memory. Each print is a one-bar edge on the lagged bar, not a persistent state — a book already positioned treats non-exit ticks (including further entry edges) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the cross edges are strict on the lagged decision bar (`macd > signal` for entry, `macd < signal` for exit) with inclusive previous-bar equality (`prev <= prev` / `prev >= prev` inside the standard edge); the RSI memory comparisons are inclusive (`<= 30`, `>= 70`) over exactly five lagged offsets `1..5` relative to the lagged decision bar (i.e. `i-2..i-6` relative to tick `i`) — a bar with `macd == signal` fires neither leg; a memory bar with `rsi == 30.0` (`70.0`) satisfies the entry (exit) memory leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry tick has `macd[d] > signal[d]` on its lagged decision bar `d=i-1` while any signal-exit tick has `macd[d] < signal[d]` on the same `d` — mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print. `stop_sig` cannot co-fire with entry on the entry tick either (zero distance at the fill; the stop needs a positioned book). The reviewer is never asked to invent an ordering.
- Direction: long-only. The sole short-entry line is commented out in the source (`// strategy.entry("Sell", ...)` — the only `strategy.short` token is comment text); `pyramiding=0` ships in the header. A two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the conjunct signal close, plus the 99% row-close disaster backstop, are the complete position-closing set. No take-profit (the `TP` input never reaches any order call — dead input, fenced), no trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit fixed `0.001` BTC base quantity, at most one open position per market; a positioned book treats further entry edges as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying tick after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup ticks are flat by record rule.
- Controller decision invariant (pinned-engine binding): at tick `i` the researcher controller reads ONLY `{entry_sig[i], exit_sig[i], stop_sig[i], position_state}` — precomputed lagged columns timestamped at the row open label. It never branches on row `i`'s `open/high/low/close/volume`, never reads the provider mid-price for a decision, and never divides a quote amount by a price. The same-row close sitting in the provider at tick `i` therefore cannot enter any decision or sizing path.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (MACD triple smoothing plus Wilder RSI, fixed non-negative offsets, plus the standard one-bar edge lookback and the five-bar memory — no forward reference) with the decision bar itself lagged one further row; the tick's own forming values are never read. No funding/OI/mark-price read, no `request.*`, no session/calendar call, no resample, no interpolate, no hyperopt parameter anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (MACD on `close`; RSI on `close`). No `open` read, no `high`/`low` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher choice — the file names no timeframe; the memory windows are trailing bar counts, portable to any frame, and `1h` is the pinned frame of this derived version only). One evaluation per row; every window reads the tick's causal past only (lagged decision bar `i-1` plus its own fixed lookbacks); fills land on the tick row's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 one-hour bars held flat. Covers the EMA-26 seed plus 9-bar signal smoothing (~35 bars), the 14-bar RSI seed, the 5-bar memory, and the one-bar publication lag, with margin. The file ships no warmup guard — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict/inclusive NaN comparison is false — no leg can fire early; the engine's own `dropna` on the merged frame (`backtesting_engine_base.py:478`) additionally removes unseeded leading rows. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT on the `binance` spot connector, `1h` BinanceSpotCandles feed, `leverage 1`, no margin, no funding leg (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Pinned engine (exact): Hummingbot package `20260920`, VERSION `dev-2.17.0`, commit `fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467`. Applicable path: `BinanceSpotCandles` feed → `BacktestingDataProvider` → researcher signal-gated controller → `OrderExecutorSimulator` with `ExecutionStrategy.MARKET` → `BacktestPositionHold` netting ledger. This record deliberately does NOT use `DirectionalTradingControllerBase.create_actions_proposal` (whose `total_amount_quote / price` sizing at `directional_trading_controller_base.py:174-177` reads the same-row close) and does NOT use `PositionExecutorConfig`/its triple-barrier simulator (whose same-row barrier checks would couple the fill row's range into the decision tick). Both avoided paths are named so the reviewer need not guess which controller this record means.
- Timestamp and availability mapping (verified line by line at the pinned commit): Binance Spot REST Klines define `row[0]` as Open time and `row[4]`/`row[6]` as Close/Close time (first-party market-data docs); `_parse_rest_candles` stores `ensure_timestamp_in_seconds(row[0])` as the row timestamp (`binance_spot_candles.py:80-84`), so every engine row timestamp is the bar OPEN label while `high/low/close` are fixed only at bar close. `prepare_market_data` backward-merges researcher features onto candle rows (`backtesting_engine_base.py:466-468`) and stamps `timestamp = timestamp_bt` (`:470`). `update_state` loads `close_bt` into the provider price and stamps provider time with the row timestamp (`:364-368`) BEFORE `simulate_execution` calls `determine_executor_actions` (`:282-284`). Researcher features are timestamped at the row open label but computed exclusively from bars `<= i-1` (lag-1 info set in Signal); the controller's decision function reads only those lagged columns plus position state (invariant above). Hence the decision at tick `i` provably precedes — in real time — both the information it uses (fixed at `i-1` close) and the fill price it receives (row `i` close, fixed after the tick label). Pre-placed-order-same-row-fill semantics are disclosed as the derived convention, never as the Pine emulator's next-open timing.
- Fill path (verified): `OrderExecutorSimulator` MARKET fills at the first row of its slice (`order_executor_simulator.py:22-24`), takes `entry_price = close` at that row (`:56`), books `filled_amount_quote = amount * entry_price` (`:59`) with `cum_fees_quote = trade_cost * amount_quote` (`:62`), trims to the fill row (`:65`), and closes as `POSITION_HOLD` (`:67-71`). Its `net_pnl_quote`/`net_pnl_pct` columns stay `0.0` (`:12-13`, never updated after) — OrderExecutor legs contribute zero executor PnL by construction; ALL economics flow through the position-hold ledger. The next tick's `_update_positions_from_stopped_executors` routes the hold into `BacktestPositionHold.add_executor` (`backtesting_engine_base.py:540-566`), which nets buys/sells incrementally (`_process_order`, `:65-103`) so a SELL OrderExecutor for the full held base returns the book exactly flat.
- Amount path (verified, leak-free): the researcher controller sets `OrderExecutorConfig.amount = 0.001` BTC constant. No quote-division by any price occurs anywhere in this record's path (the `total_amount_quote / price` line in the avoided directional base is never executed). `total_amount_quote` (fixed `1000` USDT) enters ONLY `summarize_results` as the `net_pnl_pct` denominator (`:680`) — a reporting scaler with zero event effect, disclosed, never a sizing input.
- Cost and accounting model (verified, stated to pre-empt misreading): `trade_cost = 0.001`/side is the explicit model input to `run_backtesting`/`simulate_execution` (`:221-225`, `:269`), flowing into `cum_fees_quote` per fill (`order_executor_simulator.py:62`) and accumulating in `BacktestPositionHold.cum_fees_quote` (`:119`). `realized_pnl_quote` is the GROSS matched spread with no fee term (`:73-80`). `summarize_results` reports `net_pnl_quote = executor_pnl + position_realized_pnl` (`:624`) while returning `total_fees_quote` as a SEPARATE field (`:613`, `:703`), and it EXCLUDES `POSITION_HOLD` legs from `executor_pnl` (`:609-612`). This record therefore NEVER reads `summarize_results.net_pnl_quote` as a net-of-fees figure; net research economics equal gross realized spread minus accumulated `cum_fees_quote`, computed downstream. No hypothetical zero funding is reported as realized funding — the spot version has no funding leg at all.
- Precision (explicit pin): continuous unquantized accounting — the fill path performs float/Decimal arithmetic with no rounding (`order_executor_simulator.py:59-62`; `BacktestPositionHold` holds raw Decimals, `:51-57`), and this record never calls `quantize_order_amount`/`quantize_order_price` (`backtesting_data_provider.py:142-162`, available but explicitly unused). Live LOT_SIZE/PRICE_FILTER rounding is a named upgrade path (see Limitations), never silently assumed.
- Excluded overlay (explicit, to keep Gate 4 single-valued): the downstream campaign house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) is NOT part of this admission version — no Safety Orders, no averaging, no leverage, no shared-portfolio state. Any DCA/leverage experiment would be a separately identified derivative with its own record, never an event-neutral overlay on this one.
- Backtesting resolution: market-data resolution `1h` with the single `1h` candles config (`initialize_backtesting_data_provider`, `:259-267`) — one frame, no multi-timeframe alignment burden.
- Concurrency: at most one position per market at any time; the lagged cross-plus-memory edge opens the fixed unit on a flat book; the lagged conjunct signal close or the lagged 99% row-close backstop closes it in full; re-entry after an exit needs only the next qualifying tick (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (53 lines: the 12/26/9 EMA-path MACD, the 14-period Wilder RSI, the two `1..5` memory loops, the two conjunct edges, the long-only entry plus signal close, the 99% stop, and the `MACD + RSI Strategy` header pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 60-bar record-rule floor additionally holds every pre-seed tick flat — disclosed, not repaired. The file ships no warmup guard, so the floor is purely a researcher pin, never misattributed. The engine `dropna` (`:478`) is a second, independent leading-window fence.
2. Exact-touch rule fenced: the cross edges are strict on the lagged decision bar while admitting previous-bar equality; the memory legs are inclusive (`<= 30`, `>= 70`) — a bar sitting exactly on the signal line fires nothing on either side; a memory bar sitting exactly on 30.0 (70.0) satisfies the entry (exit) memory leg. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-TP-input fence: `TP = 10` is declared and read by no order call anywhere in the 53 lines — a dead input with no gate effect, never repaired into a take-profit leg. Zero `limit` order tokens ship anywhere.
4. Commented-short fence: the only short-entry line is commented out (`// strategy.entry("Sell", strategy.short, when=bear_cross)`); the live book is long-only by construction. The `strategy.short` token is comment text, never an order leg.
5. Memory-exclusion fence: the source loops `rsi[1..5]`, excluding the decision bar's own RSI — the memory is already lagged in the source. The derived version's extra one-row publication shift (decision bar `i-1` at tick `i`) is a disclosed causal adaptation, never presented as source-native timing; Pine's own emulator fills at next-bar open while this version fills at the tick row's close.
6. Wide-stop fence: the 99% stop sits at 1% of the average entry price — by construction a disaster backstop that never binds before the conjunct signal close in ordinary tape. Coded fact, disclosed, evaluated on lagged row closes only (never intrabar), not reinterpreted as a tight risk regime and not tightened by repair.
7. Cousin records fenced as different constructions (none trades a MACD-signal-cross edge conjunct with a five-bar RSI memory window, long-flat, with this risk pair): the admitted `freqtrade-macd-cross-cci-edge` pool-mate trades a MACD-cross conjunct with a SINGLE-bar CCI state plus a four-rung ROI ladder and −30% stop (no memory window, different oscillator, different risk); the admitted `freqtrade-macd-cci-dip-state` pool-mate trades persistent MACD-polarity-plus-CCI state (every qualifying bar, never a one-bar edge); the admitted `macd-signal-cross-reversal` pool-mate trades a naked FMZ 12/26/9 two-sided cross with no oscillator leg at all; the admitted `freqtrade-asdts-rockwell` pool-mate trades dual-polarity MACD state with a signal-line-only exit; the admitted `alorse-macd-dmi14-vstop20` pool-mate gates MACD+DMI with a volatility stop (different gate, different risk). Not a threshold re-tuning of any of them: moving any MACD/RSI period, dropping either conjunction leg, collapsing the five-bar memory to a single-bar state, flipping any strictness, or changing the stop, frame, or book would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: the other 47 files in the Alorse collection (including `RSI + EMA.pine`, `Double RSI.pine` with its `request.security` MTF leg, and `MACD + DMI.pine`) are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot-1h market/frame choice, the lag-1 information set with row-close MARKET fills, the fixed-0.001-BTC/no-add/no-cooldown position pin, the 60-bar warmup floor, the row-close-only 99% stop evaluation, the `trade_cost=0.001`/continuous-accounting/no-funding cost pins, and the Pine-default readings (EMA paths, Wilder RSI, standard edge semantics) — all predeclared above. The `12/26/9` MACD, the `14` RSI, the `5`-bar `30/70` memory windows with all strictness, the conjunct entry edge, the conjunct close, the 99% stop level, `pyramiding=0`, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: MACD(12,26,9) / RSI(14) / conjunct edges / `30`+`70` memory thresholds with pinned strictness and `1..5` offsets / one-bar-edge legs / conjunct signal close / 99% row-close backstop / fixed-0.001-BTC single-unit long-only / `1h` BTCUSDT spot / lag-1 row-close fills are frozen.

- F1 — Memory relevance: dropping the RSI-memory legs (naked MACD-signal-cross edge, same conjunct-exit MACD leg only, same risk) must not improve net expectancy; fail ⇒ the five-bar washout memory adds nothing over rotation timing.
- F2 — Rotation-timing relevance: dropping the cross edges (pure RSI-memory state: long while any of `rsi[1..5] <= 30`, exit while any of `rsi[1..5] >= 70`, same risk) must not improve net expectancy; fail ⇒ the rotation edge adds nothing over the oscillator memory alone.
- F3 — Exit-conjunction relevance: widening the exit to any cross-down bar regardless of memory (unconditional `crossunder` close, same entry, same risk) must not improve net expectancy; fail ⇒ the heat-memory exit filter adds nothing over the bare rotation exit.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names no market or frame). Long-only with full-unit open/close expresses unchanged on a USDT-M perpetual venue with leverage 1 and no short leg, but that venue mapping is not part of this admission version. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and absent by construction in this spot version (no modeled funding, no realized funding, no zero-funding claim).

## Limitations

- The `1h` frame is an already-admitted interval on `main` via many pool records — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose MACD never prints the conjunct exit edge is held until the 99% backstop; a market that oscillates with hot RSI memory but no death-cross prints repeated hold-no-ops with no flat state to rest in, while a market that rolls MACD without hot memory likewise holds (conjunct-exit profile, disclosed). There is no decay, chop, trend-loss, trailing, take-profit, or further time exit — disclosed, not repaired.
- Pine's EMA seeding, Wilder-RMA RSI seeding, and the standard `crossover`/`crossunder` edge live in the Pine runtime outside the pinned file — pinned by call with defaults 12/26/9 and 14, not re-derived; exact reproduction inherits those seedings alongside the 60-bar floor. The derived lag-1 shift adds a further one-row delay versus the Pine emulator's own timing, disclosed above.
- Live-trading upgrade path (not part of this admission): exchange LOT_SIZE/PRICE_FILTER quantization, minimum-notional checks, live fee-tier confirmation, and latency/reject handling would be required before any execution use; this record's continuous accounting is a research-model pin only.
- The `TP` input and the commented short line are dead/comment text — nothing further to fence.
- No trailing, no take-profit, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/MACD+RSI.pine
- https://github.com/Alorse/pinescript-strategies
