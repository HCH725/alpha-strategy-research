---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AverageStrategy EMA8/EMA21 cross-edge long-flat on BTCUSDT 4h bars
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AverageStrategy EMA8/EMA21 cross-edge long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/AverageStrategy.py`.
- GitHub blob SHA at the pinned commit: `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, size 2630 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2630 bytes, 79 lines, SHA-256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`, identical to the GitHub blob (`git hash-object` reproduces `dbb0ba65…0d308d493`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AverageStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/MACDStrategy.py` (MACD-vs-signal state with CCI-threshold legs, `5m`, already admitted), `berlinguyinca/MACDStrategy_crossed.py` (MACD cross edges with CCI gates, `5m`, already admitted), `berlinguyinca/Simple.py` (four-way MACD/BB-rise/RSI70 conjunction, `5m`, already admitted), `berlinguyinca/TechnicalExampleStrategy.py` (CMF sign states, `5m`, already admitted), and every other admitted berlinguyinca pin are different pins with different gates — this record pins ONLY the AverageStrategy literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '4h'`; `minimal_roi = { "0": 0.5 }`; `stoploss = -0.2`; `buy_range_short = IntParameter(5, 20, default=8)`; `buy_range_long = IntParameter(20, 120, default=21)`; entry is `qtpylib.crossed_above(ema{short}, ema{long})` AND `volume > 0` (`enter_long = 1`); exit is `qtpylib.crossed_above(ema{long}, ema{short})` AND `volume > 0` (`exit_long = 1`). The docstring (`author@: Gert Wohlgemuth`, `idea: buys and sells on crossovers - doesn't really perfom that well and its just a proof of concept`) is lineage only — the "doesn't perform well" disclaimer is adopted as a no-profitability-claim fence (see Negative evidence 8), and no sample, window, trade count, or cost basis ships anywhere in the 79 lines.
- Out-of-file calls pinned (all resolved by name): `ta.EMA(dataframe, timeperiod=val)` (TA-Lib abstract EMA over the default `close` price — standard causal exponential recursion, disclosed default, never redefined); `qtpylib.crossed_above(a, b)` (vendored helper; the record pins its exact formula below rather than any helper version — see Signal). `populate_indicators` computes one EMA column per integer in the two declared IntParameter ranges (dead columns except `ema8`/`ema21`, fenced below). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no informative-pair call, no `buy_params`/`sell_params` fitted dict anywhere in the file.
- Full-file token census (verified over the 79 lines this cycle): 4 `short` (all four are the parameter *name* `buy_range_short` — zero short-direction legs, zero short identifiers beyond the name); 0 `trailing`; 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `can_short` (the derived long-flat book below is a researcher pin, never a framework-default claim); 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 3 `Parameter` (the two `IntParameter` declarations plus the `CategoricalParameter, DecimalParameter, IntParameter` import — no fitted `buy_params`/`sell_params` dict, so the coded defaults 8/21 are the only code-level values); 0 `shift` in the file body (the one-bar lag lives inside the pinned cross formula, disclosed); 3 `cross` (the two `crossed_above` calls plus the docstring `crossovers` — no other edge call).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `4h` frame, the EMA8/EMA21 pair, the cross-edge legs with the volume guard, the single-rung 50% ROI target, the −20% stop, and the absence of any short/trailing/sizing rule — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` spot (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) cross confirmed on completed bar `t`, controller evaluation on simulator row `t+1`, MARKET fill at row `t+1` close — next-bar-close fills (derivation disclosed, never presented as the source engine's own timing); risk legs evaluated on subsequent row closes only; (3) single-unit/no-add/no-cooldown position pin plus a 40-bar researcher warmup floor (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) fixed 200 USDT-per-position spot sizing with `trade_cost = 0.0001` per filled side (explicit research cost assumption, never a live-fee claim); (5) both IntParameters frozen at their coded defaults (8, 21) — no fitted dict ships anywhere, so the freeze is lossless with respect to the file, and any other pair is a different, unpinned rule. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `averagestrategy` (case-insensitive) and `buy_range_short` returns zero strategy records — no record in the pool cites this source file or this parameter pair. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a dual-EMA cross system. EMA-cross cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure while the fast 8-bar EMA prints above the slow 21-bar EMA on `4h` bars (entered on the upward cross edge with non-zero volume), exit on the downward cross edge, with a single-rung 50% ROI target and a fixed −20% stoploss behind every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Fast dual-EMA trend-capture machine, long-only. Unlike slow regime systems (50/200-style, holding for weeks), the 8/21 pair on `4h` bars responds within ~1–3 days: effective lookbacks ≈ 32h vs ≈ 84h. The cross edge is the whole timing model — there is no oscillator gate, no volatility filter, no pattern confirmation beyond the volume guard. The 50% ROI rung almost never binds first on `4h` crypto (it is a moon-bag harvester, coded fact, not a tight target), so live exits are dominated by the downward cross edge and the −20% disaster stop. The failure mode is plain: a sideways tape whipsaws the book across alternating cross edges with no cooldown, while a Strat-entry that immediately bleeds rides the full unit to the −20% stop — no time exit exists.

## Signal

Exact rule as pinned (any other EMA pair, edge-vs-state pairing, threshold, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own, with the two IntParameters frozen at their coded defaults:

```text
ema8[t]  = TA-Lib EMA(close, 8)    // causal recursion over completed closes
ema21[t] = TA-Lib EMA(close, 21)   // causal recursion over completed closes
up[t]    = (ema8[t] > ema21[t]) & (ema8[t-1] <= ema21[t-1]) & (volume[t] > 0)
down[t]  = (ema21[t] > ema8[t]) & (ema21[t-1] <= ema8[t-1]) & (volume[t] > 0)
entry    = up[t]      // enter_long = 1, one-bar cross edge
exit_sig = down[t]    // exit_long = 1, one-bar cross edge
risk     = ROI {"0": 0.5} (fraction of entry-price distance, by position age in minutes);
           fixed stop at -20% (stoploss -0.2, same basis)
floor    = 40 leading 4h bars held flat (researcher pin; NaN comparisons false underneath)
```

- The cross formula is pinned by behaviour, not by helper version: `crossed_above(a, b)` ≡ `(a[t] > b[t]) & (a[t-1] <= b[t-1])` (vendored-helper lineage verified this cycle against `freqtrade/technical` `technical/vendor/qtpylib/indicators.py`, where `crossed_above` delegates to `crossed(..., "above")` with exactly this expression). Even if the helper ever changed, this record's rule is the formula above.
- Trade events: `enter_long=1` on cross-up edge bars, direction long-only; `exit_long=1` on cross-down edge bars. Each print is a one-bar edge, not a persistent state — a book already positioned treats further cross-up bars as hold-no-ops under the position pin below, and a flat book treats cross-down bars as no-ops.
- Exact boundaries (pinned semantics): strict `>` on the decision bar, non-strict `<=` on the lag bar — an equal-then-up bar (`ema8[t-1] == ema21[t-1]`, `ema8[t] > ema21[t]`) fires; an up-then-equal bar does not. The volume guard is strict (`> 0`) on both legs. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `ema8[t] > ema21[t]` while any signal-exit bar has `ema21[t] > ema8[t]` — mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill); any row co-printing a signal exit with an ROI/stop leg closes the full unit flat either way. The reviewer is never asked to invent an ordering.
- Direction: long-only by researcher pin. Zero short-direction instructions ship anywhere (the four `short` tokens are the parameter name `buy_range_short`), and the derived book never sells what it does not hold — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the cross-down edge, the single-rung 50% ROI target, and the −20% stop are the complete position-closing set, all evaluated on row closes under the derived timing (intrabar touches that do not survive to a row close are ignored — disclosed derivation, never presented as source semantics). ROI rungs and stop are fractions of entry-price distance (close-to-close price return), evaluated at bar closes — this basis is leverage-invariant, and the derived book is spot in any case, so margin accounting cannot alter any exit event. No trailing, no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further cross-up bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats cross-down bars as no-ops; re-entry re-arms on the next qualifying cross-up bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (two causal EMA recursions) plus `volume` (strict positivity guard) under completed-bar evaluation; the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt-fitted dict, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `4h` bars of BTCUSDT spot: `close` (both EMA recursions) plus bar `volume` (strict `> 0` guard on both legs). No `open`/`high`/`low` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the next bar's close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 four-hour bars held flat. Covers the 21-bar EMA seed, the one-bar cross lag, and margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: EMA windows print NaN until seeded and every NaN comparison (including inside the cross formula) is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT **spot** under the derived rule (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Spot is chosen deliberately: with no leverage, no margin, no mark price, and no funding leg anywhere in the path, the three cost blockers that close perpetual-declared Scout PRs (unproven historical funding, leveraged margin accounting, liquidation) cannot arise by construction — disclosed, never a claim about futures economics.
- Engine path (verified this cycle against the pinned commit, not by mutual reference): Hummingbot `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (committed 2026-09-20, `hummingbot/VERSION` fetched as `dev-2.17.0`), consistent with mandated pinned package `20260920` / VERSION `dev-2.17.0`. Static source evidence inspected read-only; no engine run, no image digest claimed, no test executed.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (727 lines, read): `BacktestingEngineBase.run_backtesting(controller_config, start, end, backtesting_resolution, trade_cost)` with `backtesting_resolution` a free string and `trade_cost` an explicit per-fill argument; `initialize_backtesting_data_provider` builds `CandlesConfig(connector, trading_pair, interval=backtesting_resolution)`; `simulate_execution` iterates timestamped rows, calls `controller.determine_executor_actions()` per row, and routes each `CreateExecutorAction` into `simulate_executor(config, processed_features.loc[i:max_ts], trade_cost)` — i.e. the action determined on row `i` is simulated on data starting at row `i`; `prepare_market_data` merges candles with controller features via point-in-time `merge_asof(..., direction="backward")` and `dropna()`s incomplete rows (no imagined fills for missing candles); `BacktestPositionHold` (defined in the same file) nets buys/sells with `_process_order` realizing PnL on matched volume — a SELL of exactly the held base closes the book to net zero, never a naked short.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (71 lines, read in full): `ExecutionStrategy.MARKET` fills at the first (current) row timestamp with `entry_price` equal to that row's `close`, books `cum_fees_quote = trade_cost * amount_quote`, and returns `CloseType.POSITION_HOLD`. Composed with the derived timing (signal bar `t` completed → evaluation row `t+1` → fill at row `t+1` close), every fill in this record is a next-bar-close MARKET fill at a printed historical close — no maker-touch, queue, or intrabar-path-dependent fill anywhere.
- Data path (verified names at the pinned commit): `BacktestingDataProvider.get_candles_df(connector_name, trading_pair, interval)` keyed `{connector}_{pair}_{interval}` (feed class `binance_spot_candles` present in the pinned tree); `CandlesBase.interval_to_seconds` maps `"4h"` to 14400 (verified in `hummingbot/data_feed/candles_feed/candles_base.py`) — the `4h` frame needs no novel-interval confirmation; `initialize_trading_rules(connector_name)` plus `quantize_order_amount` / `quantize_order_price` provide connector quantity/price quantization. The existing native MARKET `OrderExecutorConfig` + `CreateExecutorAction` construction is illustrated by `controllers/generic/pmm_mister.py` (MARKET config block and `CreateExecutorAction` returns, read); the AverageStrategy-specific signal controller itself has **not** been written and is not asserted to exist — admission is not materialization (see Implementation status).
- Pre-existing tests at the pinned commit (listed via the versioned tree API, inspected as names, **not** newly run): `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py`, `test_backtesting_engine_directional.py`, `test_backtesting_final_tick_ledger.py`.
- Sizing/capital/costs: account 1000 USDT, one **fixed** 200 USDT MARKET BUY per position quantized to the base increment; the exact filled base quantity is sold at exit; flat between positions; no compounding. Fixed `trade_cost = 0.0001` per filled side (0.01% — explicit research cost assumption, **not** a claim of any live fee tier); spread/slippage unmodeled and disclosed; funding/mark/liquidation absent by spot construction, never zero-filled as futures economics. The source ships no sizing, capital, fee, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs while sizing and costs ride this explicit overlay, under the single-unit/no-add position pin from Signal. No safety-order/add tranche exists in this derived version, so sizing changes no event.
- Concurrency: at most one position per market at any time; the cross-up edge opens the full unit on a flat book; the cross-down edge, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next cross-up edge (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (79 lines: the EMA-range loop, the two `crossed_above` edge legs with the volume guard, the `timeframe`/`minimal_roi`/`stoploss` literals, the two `IntParameter` declarations, and the `AverageStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: EMA seed NaNs compare false inside the cross formula (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Equal-bar boundary fenced: the lag comparison is non-strict (`<=`) — an equal-then-up bar fires the edge; an up-then-equal bar does not. Strictness asymmetry preserved throughout — disclosed, not smoothed.
3. Dead-column fence: `populate_indicators` computes one EMA column per integer in both declared ranges, but only `ema8` and `ema21` are ever read — every other column (including the overlapping `ema20`) is dead computation with no gate effect. No reviewer repair may substitute a dead column into the rule.
4. No-hyperopt fence: the file ships zero `buy_params`/`sell_params` fitted dicts — the 8/21 freeze reads the only code-level values, never a chosen hyperopt epoch. Any other pair is a different, unpinned rule.
5. Volume-guard fence: both legs require strictly positive bar volume — a zero-volume bar deterministically fires neither leg even on a clean cross print. The guard is preserved, never dropped as noise.
6. Wide-risk fence: the 50% ROI rung is 2.5× the −20% stop distance — by construction the rung is a moon-bag harvester that almost never binds before the cross edge or the stop on `4h` tape. Coded fact, disclosed, not reinterpreted as a tight profit regime and not tightened by repair.
7. Cousin records fenced as different constructions (none trades a standard-close EMA8/EMA21 cross-edge pair, long-flat, on `4h`, with 50% ROI plus −20% stop): the admitted `forven-simple-ema-cross` pool-mate trades Pine-seeded EMA20/50 on `1h` with a 12-month demo window gate, no volume read, and explicitly disabled stop/TP (a market that drifts 25% past entry without a cross-down holds here-to-stop but holds signal-only there; a zero-volume cross bar fires there but nothing here); the admitted `eterna-sma-50-200-crossover` pool-mate trades SMA50/200 golden-cross regime, two-sided, on `4h` (different MA variant, different horizon, different direction scope); the admitted `dual-ema-engulfing-volume` pool-mate requires an engulfing candle pattern plus volume confirmation on `1h` (pattern-gated construction, not a pure cross); the admitted `freqtrade-strategy001-ha-ema-cross` pool-mate crosses EMAs on Heikin-Ashi-transformed prices on `5m` (different price input, different frame); the admitted `forven-dema/hma/tema-cross` pool-mates trade DEMA/HMA/TEMA variants, never plain EMA. Not a parameter re-tuning of any of them: moving either EMA length, converting either edge to a state, adding any gate, flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Author-disclaimer fence: the file's own docstring says the idea "doesn't really perform that well and its just a proof of concept" — this record adopts the disclaimer as a hard no-profitability claim. Admission here is engine expressibility only, never expected return.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT spot market choice, the next-bar-close MARKET fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the frozen 8/21 defaults, the pinned cross formula (helper lineage cited, behaviour frozen), the fixed 200 USDT sizing with `trade_cost = 0.0001`, and connector quantization — all predeclared above. The `4h` frame, the EMA8/EMA21 cross-up entry edge with the volume guard, the mirrored cross-down exit edge, the single-rung 50% ROI with the −20% stop, and the absence of any short/trailing/sizing rule are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA8/EMA21 with pinned strictness / cross-edge legs / volume guard / signal exit / single-rung 50% ROI / −20% stop / single-unit long-only / `4h` BTCUSDT spot / next-bar-close MARKET fills are frozen.

- F1 — Cross-edge relevance: replacing both cross edges with a same-direction persistent state (hold long whenever `ema8 > ema21`, flat otherwise; same ROI/stop exits) must not improve net expectancy; fail ⇒ the edge timing adds nothing over the bare state.
- F2 — Period relevance: the 20/50 EMA twin (same edges, same guards, same risk, same frame/market/fills) must not dominate the pinned 8/21 pair net of costs; fail ⇒ the 8/21 choice adds nothing over its slower twin.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 50% rung plus −20% backstop adds nothing over the bare edge machine.
- F4 — Volume-guard relevance: dropping the `volume > 0` guard from both legs must not improve net expectancy; fail ⇒ the guard filters nothing real.

## Crypto portability

Direct (same venue class): the rule reads only completed `4h` spot candles and trades a long-flat book that expresses unchanged on Binance BTC spot — no short, no borrow, no leverage, no funding, no expiry, no settlement calendar. Porting to another spot venue changes only symbol spelling and quantization; perpetual, margin, or 24/7-session adaptations are out of scope for this record and would each be a separate declared derivative. Performance unproven — no return is claimed anywhere in this record.

## Limitations

No protective stop tighter than −20%; an entry that bleeds slowly without a cross-down holds the full unit a long time. Sideways tape whipsaws the book across alternating edges with no cooldown. The 50% ROI rung almost never binds — exits are effectively edge-or-stop only. Spot fee model (`trade_cost = 0.0001` per side, no spread/slippage) is a bounded research assumption, not live futures economics; funding/mark/liquidation are absent by spot construction, never modelled as zero futures costs. Sub-connector-minimum quantity handling is unmodelled beyond provider quantization — fixed 200 USDT sizing keeps positions far above dust, but no minimum-notional gate is asserted in the MARKET path read. TA-Lib EMA seeding follows the library's causal recursion; the 40-bar floor absorbs seed effects by researcher pin. The vendored cross helper is cited as lineage only — the record's rule is the printed formula, immune to helper drift. No implemented strategy controller and no backtest replay exist for this record.

## Implementation status

`not-implemented`. GitHub research record only — no strategy-specific Hummingbot controller has been written (the engine path above reuses existing, version-pinned native primitives only), and no Qlib screen, Paper, Testnet, or Live run exists for this record. Any future implementation must demonstrate the pinned-engine path and representative event-level parity before mass screening; that materialization step is `IMPLEMENTATION_NEEDED`, not a second admission gate, and is never written back into this record as a qualification field.

## Adoption boundary

`research-only`, `not-approved`; independent six-gate PASS required for this derived model, not a survivor, Testnet or Mainnet authorization.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- Primary strategy source: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
- Strategy repository: https://github.com/freqtrade/freqtrade-strategies
- Cross-helper lineage (behaviour pinned by formula in Signal): https://github.com/freqtrade/technical/blob/master/technical/vendor/qtpylib/indicators.py
- Engine pin: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine version: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Engine backtester: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting
- Engine tests: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Admission contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
