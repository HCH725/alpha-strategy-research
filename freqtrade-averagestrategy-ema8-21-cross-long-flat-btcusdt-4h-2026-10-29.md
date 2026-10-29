---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AverageStrategy EMA8/21 cross-edge with volume guard and close-evaluated risk pair, independent BTC-USDT spot 4h long-flat derivative
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - freqtrade
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies/tree/f3340ce11f5bdf62f598522e64d1f5638eaa13f5
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AverageStrategy EMA8/21 cross-edge long-flat — independent BTC-USDT spot 4h derivative

## Provenance

**Primary source (immutable, read end to end this cycle):** repository `freqtrade/freqtrade-strategies`, pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed 2026-09-08), exact file path `user_data/strategies/berlinguyinca/AverageStrategy.py`. File size **2630 bytes**, **79 lines**; GitHub contents API at the pin returns blob SHA `dbb0ba65518e1932cfd7cbccb04a01b0d308d493` and size 2630, both matching an independent local `git hash-object`/byte count of the fetched bytes (SHA256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`). Class `AverageStrategy(IStrategy)`, `INTERFACE_VERSION = 3`, docstring attribution `author@: Gert Wohlgemuth` with idea `buys and sells on crossovers - doesn't really perfom that well and its just a proof of concept` (sic — author's own words, adopted as no performance claim).

**Source-verbatim trading configuration (quoted, not paraphrased):** `timeframe = '4h'`; `minimal_roi = {"0": 0.5}`; `stoploss = -0.2`; `buy_range_short = IntParameter(5, 20, default=8)`; `buy_range_long = IntParameter(20, 120, default=21)`. Absent anywhere in the file (whole-file token census over all 79 lines): `can_short`, `position_stacking`, `position_adjustment`, `protections`, `use_custom_stoploss`, `custom_stoploss`, `trailing`, `startup_candle_count`, `order_types`, `order_time_in_force`, `use_exit_signal`, `exit_profit_only`, `leverage`, `funding`, `mark_price`, `DCA`, `cooldown`, `max_open_trades`, `informative_pairs`, `resample`, `merge`, any `enter_short`/`exit_short` leg (exactly one `'enter_long'] = 1` leg, exactly one `'exit_long'] = 1` leg), any short/sell-short order call.

**Source-verbatim signal code (quoted):** indicators use TA-Lib abstract plus qtpylib only (`import talib.abstract as ta`, `import freqtrade.vendor.qtpylib.indicators as qtpylib`): `dataframe[f'ema{val}'] = ta.EMA(dataframe, timeperiod=val)` for every val in the set union of the short range (5–20) and the long range (20–120). Entry leg: `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_short.value}'], dataframe[f'ema{self.buy_range_long.value}']) & (dataframe['volume'] > 0)` → `'enter_long'] = 1`. Exit leg: `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_long.value}'], dataframe[f'ema{self.buy_range_short.value}']) & (dataframe['volume'] > 0)` → `'exit_long'] = 1`. Both legs are cross edges on the same completed bar plus a volume-positivity guard; no second timeframe, no oscillator, no volume indicator beyond `> 0`.

**Independent derivative — NOT source-native or lossless:** researcher-declared adaptations are exactly: (1) market **Binance BTC-USDT spot 4h** (the source names no market; no timeframe adaptation — the source is already 4h); (2) hyperopt menus not taken — **EMA8/EMA21 pinned** at the file's own defaults; (3) **completed-bar close-effective MARKET** fills instead of any framework order default (the file ships no order-type mapping; no source-market equivalence is claimed); (4) the `minimal_roi 0.5` take-profit and `-0.2` stoploss are **retained as bar-close-evaluated legs on a fee-exclusive gross basis with researcher-pinned priority stoploss → ROI → signal** (freqtrade evaluates risk intrabar on high/low with fee-inclusive profit ratio; that intrabar path is not modelable on the pinned close-fill lane, so the timing/basis change is owned here and can change source trades); (5) fixed **0.001 BTC** sizing on 10,000 USDT unborrowed cash with hypothetical **0.1% per-side** simulator cost instead of any framework sizing default; (6) warmup of **50 consecutive valid completed 4h bars**, flat before that by record rule (the file ships no `startup_candle_count`; the count covers the maximum read lookback 21 plus one shift bar plus margin — disclosed researcher choice). All six choices can change source trades and are evaluated only as this independently specified executable research strategy.

**Immutable identity:** `FT:AverageStrategy:berlinguyinca@f3340ce | independent-derived-v1:2026-10-29 | EMA8/EMA21-cross-edge:talib-abstract | volume>0 | ROI0.5/SL-0.2-close-gross:priority-SL-ROI-signal | BinanceSpot:BTC-USDT:4h:LONG-FLAT:0.001BTC:cash10000 | completed-close-MARKET:trade_cost=0.001 | warmup50`. Any change in windows, operators, thresholds, priority, market, clock, size, cost, state, or fill model is a different research version.

**Dedup on main `8442b11376a5f28e86c8e153d681c44cc31bbf04`:** current main has **442** root-level strategy Markdown records and README pool count **442**. Working-tree filename/content searches for `AverageStrategy`, `averagestrategy`, `buy_range_short`, and `Wohlgemuth` return **zero** records trading this file's rule (the `Wohlgemuth` hits are sibling berlinguyinca files — ADXMomentum, AwesomeMacd, BbandRsi, Quickie, Simple — each a different pinned indicator set, none a bare dual-EMA cross). All **11** currently open `research/*` PRs were inspected (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas ADX-gated SMA3/6, #350 ClucMay BB-discount, #353 Heracles Keltner-Donchian, #593 Vinicius Supertrend volume/body/RSI) — none cites this source or any EMA8/21 cross-edge rule. Closed-PR search for `AverageStrategy` returns nothing. Nearest main cousins are materially different constructions: (a) `forven-ema-cross-adx-regime-long-flat-btcusdt-1h-2026-10-19.md` trades an **EMA20/50 cross gated by an ADX regime** on 1h — this candidate has no regime gate, different lengths, different horizon; (b) `tradingview-joat-atr-velocity-ribbon-impulse-long-flat-btcusdt-1h-2026-10-28.md` trades an **ATR-velocity onset with an EMA8/21/34 ribbon plus volume impulse** on 1h — this candidate trades the bare cross edge itself with no velocity/ribbon/impulse logic; (c) `freqtrade-crossema-28-48-stochrsi-threshold-long-flat-btcusdt-1h-2026-10-26.md` trades **EMA28/48 level alignment (never a cross) gated by raw StochRSI thresholds** on 1h — different operator, different lengths, different gate, different horizon and source; (d) `freqtrade-strategy001-ha-ema-cross-long-flat-btcusdt-5m-2026-10-21.md` trades a **Heikin-Ashi EMA cross** on 5m — different price input and horizon. No duplicate source or materially identical normalized rule was identified: no pool record conjoins bare EMA8/EMA21 cross edges in both directions with a pure volume-positivity guard and a 50%/-20% close-evaluated risk pair on 4h.

## Economic mechanism

### Source-reported

The author's construction bets that a fast-over-slow EMA cross edge marks a trend turn worth holding until the mirror cross edge prints, with a volume-positivity guard refusing signals on zero-volume bars and a 50% ROI target / −20% stoploss backstopping every position. The docstring itself warns the idea `doesn't really perfom that well and its just a proof of concept`. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance beyond the quoted construction facts.

### Research interpretation

Bare trend-turn holder with receipts-only exits, long-only: the position opens on the first up-cross print and persists through every bar until the mirror down-cross, the take-profit, or the stop — no oscillator, regime, or price-pattern filter ever intervenes, so chop between crosses costs only opportunity while a genuine reversal exits on its first jointly-confirming bar. Unlike level-alignment EMA systems the legs are edges — a persistent fast-above-slow state after entry is a hold (no-op), never a re-fire. Unlike gated cross systems there is no second opinion: the cross plus a positive-volume print is sufficient. The volume `> 0` guard is a data-validity condition, not a volume signal. The retained 50% ROI leg is distant enough to rarely bind on 4h crypto while the −20% stop is the only loss backstop; missing any tighter protection is a material loss risk, not an implicit engine default.

## Signal

**Market/data clock:** exactly one actual Binance spot `BTC-USDT` **4h** OHLCV stream. Each exchange opening timestamp `T[t]` labels a four-hour bar whose data become available only at **T[t]+14400 seconds**. Require consecutive opening timestamps separated by 14400 seconds; O/H/L/C finite and positive, H>=max(O,C), L<=min(O,C), V finite and nonnegative. No incomplete bar, forward-fill, future bar, or synthetic price is accepted. The rule reads **Close** (EMA chain, risk ratios) and **Volume** (positivity guard only); Open/High/Low are validity-checked but never read by any order-gating line.

**Frozen arithmetic (TA-Lib abstract semantics, pinned here):** `ema8[t]` / `ema21[t]` are exponential moving averages over closes with `k=2/(N+1)` (N=8/21), first valid index N−1 seeded as the simple mean of closes[0..N−1], then `EMA[t]=C[t]*k+EMA[t-1]*(1-k)` recursively in chronological float64. `crossed_above(A,B)[t] = (A[t]>B[t]) AND (A[t-1]<=B[t-1])` — strict on the current bar, non-strict on the prior bar (ties on the prior bar still arm the edge; equality on the current bar never fires). Any NaN operand makes its conjunction False (never trades on undefined prints).

**Legs (pinned defaults short=8, long=21; the IntParameter menus 5–20 / 20–120 are not taken):** `ENTRY[t] = crossed_above(ema8,ema21)[t] AND V[t]>0`; `SIGNAL_EXIT[t] = crossed_above(ema21,ema8)[t] AND V[t]>0`. Entry and signal-exit can never co-fire: they require contradictory strict orderings (`ema8>ema21` vs `ema21>ema8`) on the same bar, disjoint by arithmetic, so no tie-break is required. Gross distance ratios on entry-bar close are zero by construction, so neither risk leg can co-fire with entry either.

**Risk legs (bar-close-evaluated, fee-exclusive gross basis):** with entry fill price `Pe` and bar close `C[t]`, `g[t]=(C[t]-Pe)/Pe`. `STOP[t] = g[t]<=-0.20`; `TP[t] = g[t]>=+0.50`. Both use strict-or-equal bounds as written (exact −20.0% / +50.0% prints fire). Same-bar priority, predeclared researcher rule mirroring freqtrade's risk-first convention: **stoploss, then take-profit, then signal exit** — the first trigger in that order closes the position in full; the others are not evaluated further that bar. This close-only evaluation is the disclosed adaptation: freqtrade checks risk intrabar on high/low with fee-inclusive profit ratio, which the pinned close-fill lane cannot model.

**Warmup:** require **50 consecutive fully completed valid 4h bars** (bar indices 0..49, covering the maximum read lookback 21 plus one shift bar plus margin — all read EMA columns are valid throughout), flat before that by record rule. Begin with 10,000 USDT, zero BTC, FLAT, no pending order, and no pre-warmup inferred position. First eligible decision t is index 50.

**Order and re-entry state:** `FLAT -> LONG -> FLAT`, with changes **only after validated full fill**. While FLAT with no pending action, `ENTRY[t]` emits one BUY filled in full at `C[t]`; an ENTRY while LONG is ignored (hold-no-op), never queued. While LONG, the exit set `{STOP, TP, SIGNAL_EXIT}` is evaluated at each subsequent completed close in the pinned priority; the first trigger emits one full SELL filled at that bar's close. A failed, rejected, partial, missing-price or mismatched fill **aborts** the bounded simulation; never silently mark it filled, resize, or fill at a synthetic price. A final-bar signal with no real bar to fill against is unfilled and not counted. Re-entry requires a **new** ENTRY edge on a later eligible bar after SELL fill; no latch of an ignored crossing, no same-fill-bar re-entry, no cooldown (explicitly none — the file ships no cooldown concept).

**Explicitly disabled:** SHORT, borrowing, margin, leverage, futures, funding, DCA, safety orders, pyramiding, scale-in/out, multi-pair concurrency, compounding, extra cooldown, intrabar stop/TP, trailing, breakeven, stop-limit/maker, time exit, opposite-side reversal, and forced end-of-sample liquidation. There is **no protective price stop tighter than −20% gross on close**: a large adverse gap can occur before any exit binds, and the close-only stop can print well beyond −20% on a gap bar. If still LONG at sample end, report unrealized mark-to-last-real-close only.

## Required data

- Completed `4h` bars of BTCUSDT: `close` for the EMA8/EMA21 chain and the gross risk ratios, `volume` for the positivity guard. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Warmup accounting: the first 50 consecutive valid completed bars are indicator-warmup only (EMAs may accumulate, but no trade orders). A missing/invalid bar resets the consecutive-valid count rather than letting a dataframe `dropna` silently alter the time series.

## Execution assumptions

- Research market: BTCUSDT Binance **spot** under this record (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with **same-bar-close MARKET fills** — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced EMASkipPump (`5m`), CombinedBinHAndCluc (`5m`), BbandRsi, AwesomeMacd and TDSequential siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the signal exit, and both risk legs are all bar-close-evaluated; the Signal mutual-exclusion proof plus the predeclared risk priority leave no ambiguous same-bar fill order to the engine. Decision and fill share timestamp E[t]=T[t]+14400, when C[t] is already known — no future bar is read.
- Interval precedent (disclosed, not assumed): `4h` is an already-admitted interval on `main` via the HLHB EMA-RSI-ADX record (`freqtrade-hlhb-ema-rsi-adx-quad-gated-long-flat-btcusdt-4h-2026-10-21.md`) — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: fixed **0.001 BTC** per BUY on 10,000 USDT unborrowed starting cash with hypothetical **0.1% per-side** simulator cost (`trade_cost=0.001`); at BUY price Pb debit `Q*Pb*(1+0.001)`, at SELL price Ps credit `Q*Ps*(1-0.001)`; check cash sufficiency before BUY and abort rather than resize. The downstream 6%+6%+6% research campaign overlay is **not** part of this admission identity — applying it would create a separately declared derivative, never an event-neutral reinterpretation of this record. The source ships no sizing, capital, fee, margin, or funding concept; none is attributed to it.
- Concurrency: at most one position in this market at any time; the cross edge opens the full fixed unit on a flat book; the stoploss, take-profit, or signal exit closes it in full; re-entry after an exit needs only the next qualifying cross edge (no cooldown — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (79 lines: the EMA range computation, the IntParameter defaults 8/21, the guarded cross-edge long entry, the mirrored cross-edge exit, and the `timeframe`/`minimal_roi`/`stoploss` literals). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance. The author's own docstring frames the idea as a proof of concept that does not perform well.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No pool record trades this file's exact rule (see Dedup): sibling `Wohlgemuth` files are different indicator sets; the EMA-cross cousins all add gates (ADX regime, ATR velocity, ribbon, StochRSI, Heikin-Ashi) or use different lengths/operators/horizons.
- The 50% ROI leg will rarely bind and the strategy carries no tighter protection — admitted as a limitation, not as evidence of viability. HB_READY is not a profitability finding.
- Do not screen this strategy at Qlib scale until representative Qlib/Hummingbot event-level parity for any newly required execution path is validated. HB_READY is not profitability, Survivor, Qlib parity or Paper/Testnet/Live authorization.

## Falsification plan

Later authorized testing (not performed) must check, at minimum: EMA seed/first-valid-index handling; tie prints on current vs prior bar for both cross directions; zero-volume bar veto on entry and exit; warmup boundary (index 49 vs 50); exact −20.0% / +50.0% risk-boundary prints; gap bar beyond the stop; same-bar STOP+TP+signal priority; signal-exit vs TP co-fire ordering; entry-edge re-fire while LONG (must hold, never add); re-entry on the next edge after exit; final-bar unfilled signal; missing/duplicate candle handling and warmup-count reset; missing-price `Decimal("1")` fallback refusal; fee-ledger reconciliation `0.001*Q*(Pb+Ps)` and cash-insufficiency abort; timestamp labeling (decision/fill both E[t]); no end-of-sample liquidation. Any failure is record falsification, never a silent repair.

## Crypto portability

Long-only spot expression ports to any Binance spot market with validated 4h OHLCV; sizing and cash must be re-pinned per market (this record's 0.001 BTC / 10,000 USDT pin is BTC-specific). No leverage, margin, or funding leg exists, so no perpetual accounting is invoked — porting to perpetual/futures would require a separately declared derivative with explicit funding, precision, and margin treatment. Other venues, timeframes, and fee tiers are untested and unclaimed.

## Limitations

- Simulator costs are a hypothetical 0.1%/side research input, not Binance realized fees; live fee tier, spread, latency, slippage, partial fills, minimum notional/lot/tick precision, and real-market execution are **not verified** — the simulator's absent separate slippage is a modeled limitation, not evidence of zero realized slippage.
- Close-only risk evaluation differs from freqtrade's intrabar high/low evaluation and can delay or soften both the stop and the take-profit; gap bars can print well beyond −20% before the close-evaluated stop binds.
- Profit-ratio basis is fee-exclusive gross on closes; freqtrade's fee-inclusive ratio is not replicated — disclosed, never presented as equivalent.
- TA-Lib abstract EMA seeding is pinned here as SMA-seed; a different TA-Lib build's unstable-period handling would need re-verification before reuse.
- Single market, single timeframe, fixed size; no compounding; no short side; no protection tighter than the −20% close-evaluated stop.
- This is a Scout-submitted PASS claim pending independent Hermes Auditor review, not an implementation or a preapproved deployment.

## Implementation status

`not-implemented`. No executable recipe, entrypoint, configuration artifact, or backtest output ships with this record. When this strategy is formally selected for execution, the engineering route is `IMPLEMENTATION_NEEDED`: add the minimal strategy-specific implementation, then return to the same research pipeline without redoing HB_READY. This route is physical materialization pending, not strategy REJECT and not a new gate.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record authorizes no Paper, Testnet, or Live trading, no Qlib mass screening, and no Hummingbot deployment. Only independently reviewed `hb_ready_status: PASS` admits to model-consistent research; profitability, Survivor status, and any trading authorization are separate downstream decisions.

## Related Wiki records

None.

## Sources

- Immutable file blob: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py (2630 bytes, blob SHA `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, read end to end 2026-10-29)
- Raw bytes at pin: https://raw.githubusercontent.com/freqtrade/freqtrade-strategies/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py (SHA256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`)
- Repository tree at pin: https://github.com/freqtrade/freqtrade-strategies/tree/f3340ce11f5bdf62f598522e64d1f5638eaa13f5
- Pinned execution baseline: `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`hummingbot/VERSION` reads `dev-2.17.0`; package label `20260920` per Alpha admission policy): `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (lists `4h`, REST `/api/v3/klines`), `binance_spot_candles.py::_parse_rest_candles` (row[0] → bar-open timestamp, row[1..5] → O/H/L/C/V), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` (row loop → `controller.determine_executor_actions()` → `CreateExecutorAction(OrderExecutorConfig)` → `simulate_executor`; `BacktestPositionHold` nets matched fills with separate cumulative quote fees; `terminated_executors_window` default noted), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (`ExecutionStrategy.MARKET` fill at the supplied row's close with `filled_amount_quote`/`cum_fees_quote` and `CloseType.POSITION_HOLD`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py::get_price_by_type` (missing-price `Decimal("1")` fallback at line 140 — forbidden by this record; only actual finite positive closes may fill or mark). All paths directly inspected at the pin via raw fetch on 2026-10-29; prior Alpha PR #414 supplies wheel/source mapping evidence, and this cycle did not re-hash a wheel.
