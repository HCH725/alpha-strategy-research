---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Awesome Oscillator zero-cross long-flat on BTCUSDT 1d bars
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-24
sources:
  - https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/awesome_oscillator.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Awesome Oscillator zero-cross long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the fifty-one admitted Forven records, including the `forven-naked-donchian-20` sibling admitted 2026-10-24 that pins the identical base-class blob below).
- Pinned commit SHA: `0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e` (committed `2026-10-24T00:08:46Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/awesome_oscillator.py`.
- GitHub blob SHA at the pinned commit: `9edfcf95151ee42bfbde9773a8a95518e9130b9c`, size 2989 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2989 bytes, 110 lines, SHA-256 `a38c1139643c913029816dc76df4a8199711c9842ba07d20c291faaeb2b8fddf`, identical to the GitHub blob (`git hash-object` reproduces `9edfcf95…130b9c`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AwesomeOscillatorStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "awesome_oscillator"` and a one-row roster `STRATEGIES = [("PREBUILT-AO", AwesomeOscillatorStrategy, {"_asset": "BTC"})]` — venue spelling is the bare `"BTC"` asset label only, no timeframe override. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): module docstring `AO = SMA(median_price, 5) - SMA(median_price, 34)`, `Entry: AO crosses above 0`, `Exit: AO crosses below 0`; `default_params` returns exactly `{ "fast_period": 5, "slow_period": 34, "leverage": 1.0 }`; construction is `median_price = (df["high"] + df["low"]) / 2.0`, `sma_fast = median_price.rolling(window=p["fast_period"]).mean()`, `sma_slow = median_price.rolling(window=slow).mean()`, `ao = sma_fast - sma_slow`; trigger reads `curr_ao = float(ao.iloc[-1])`, `prev_ao = float(ao.iloc[-2])`, `curr_close = float(close.iloc[-1])`; entry is `prev_ao <= 0 and curr_ao > 0`; exit is `prev_ao >= 0 and curr_ao < 0`; short-frame guard `len(df) < slow + 2` returns the explicit no-signal `Signal`; every return hardcodes `direction="long"`; confidence is `min(1.0, abs(curr_ao) / (curr_close * 0.005 + 1e-10))` on entry bars else `0.0`. No performance phrase of any kind ships anywhere in the 110 lines.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by the admitted naked-Donchian sibling) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default, and `BaseStrategy.__init__(strategy_id, params)` merging `{**default_params, **params}`. The file's explicit `direction="long"` on every return needs no default reading.
- Full-file token census (verified over the 110 lines this cycle): `def generate_signal` exactly once (a single per-bar path — no vectorized twin); 0 `short` (no short leg, no short identifier anywhere); 0 `open` / 0 `volume` (sole `df[` reads are `close`/`high`/`low`); 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt` (the single case-insensitive `parameter` hit is the `parameter_space` def line only — a grid menu, never a signal input); 0 `trailing` / 0 `stoploss` / 0 `startup`; 0 `order_types`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `timeframe` / 0 `data_requirements` (the file declares no frame — the `1d` pin below is a disclosed researcher choice); 0 `shift` (offsets are `iloc[-1]`/`iloc[-2]` — fixed one-bar causal offsets, no forward reference); 0 `fillna` / 0 `ffill` / 0 `interpolate` / 0 `dropna` / 0 `merge` / 0 `can_short` / 0 `nan_to_num`; 2 `direction` (the two `direction="long"` returns); the single `leverage` token is the `"leverage": 1.0` defaults entry — an unleveraged hint explicitly adopted (see Execution assumptions).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the 5/34 median-price AO construction, the zero-cross entry and exit with all strictness, the long-only stance, the short-frame neutral guard, and the no-stop posture — but ships no venue spelling beyond `"BTC"`, no frame, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/frame `BTCUSDT` spot `1d` (the roster names `"BTC"` and the file declares no frame; venue spelling and the `1d` decision-frame pin are disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 86400s` with MARKET fills at the decision bar's own close on the cited pinned-engine path (the file returns `price=round(curr_close, 4)` — the decision bar's own close; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit `0.001` BTC position pin with controller-memory state machine plus a 60-bar researcher warmup floor (covers the source's own 36-bar guard with margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no exchange lot/tick quantization in-path) replacing the absent source economics, with the file's `"leverage": 1.0` hint explicitly adopted as unleveraged spot. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `awesome_oscillator.py`, `AwesomeOscillatorStrategy`, `PREBUILT-AO`, and `TYPE_NAME = "awesome_oscillator"` returns zero strategy records citing this source file. The pool's two AO-worded neighbours are fenced in Negative evidence 6–7 (Pine two-sided 4h system; freqtrade MACD-gated 5m system — different immutable sources, mechanisms, directionality, and frames). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a naked AO zero-cross. Not a duplicate, paraphrase, or trivial parameter variant: a naked 5/34 median-price zero-cross edge, long-flat, on `1d` bars from this immutable file is fenced against every oscillator pool-mate in Negative evidence 6–8.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar whose Awesome Oscillator (SMA5 minus SMA34 over median price) crosses from at-or-below zero to above zero; stand back to flat on the bar whose oscillator crosses from at-or-above zero to below zero. The oscillator is pure trailing-bar arithmetic with no volatility normalization and no regime gate. No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Naked Bill-Williams-style momentum timer, long-only, edge-triggered, no veto. Any fresh zero-cross up enters, however small the histogram print, and any fresh zero-cross down exits, however shallow the fade. Unlike the pool's MACD-gated freqtrade sibling (AO cross AND-gated with a MACD condition — veto-failed crosses fire there never), flat here means only "no fresh cross printed", never "vetoed". Unlike oscillator-level systems (RSI threshold holds), there is no overbought profit-taking leg — a vertical advance is held with no exit while the histogram stays positive, and a grinding bleed is exited only at the slow 34-bar-seeded cross down. The failure mode is plain: chop that alternates small positive and negative histogram prints whipsaws the book with no cooldown; a crash that gaps the histogram from positive to deeply negative exits one bar later with no stop to front-run it.

## Signal

Exact rule as pinned (any other fast/slow length, price input, trigger polarity, frame, fill, book, or risk posture is a different, unpinned rule). `mp_t` is the pinned median price:

```text
mp_t   = (high_t + low_t) / 2
AO_t   = SMA(mp, 5)[t] - SMA(mp, 34)[t]     // rolling means, default min_periods
ready  = positional length >= 36            // source guard: len(df) >= slow + 2
entry_t = (AO_{t-1} <= 0) AND (AO_t > 0) AND ready
exit_t  = (AO_{t-1} >= 0) AND (AO_t < 0) AND ready
```

- Trade events: `entry_signal` on a fresh zero-cross-up bar, `direction` long-only; `exit_signal` on a fresh zero-cross-down bar. Both legs are one-bar edge crosses (refires require a fresh cross back through zero). A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): strict current-bar comparisons (`>`, `<`) with setup legs (`<=`, `>=`) exactly as coded — a histogram print of exactly `0.0` fires neither leg (`curr > 0` fails and `curr < 0` fails); touches hold the prior state. `price=round(curr_close, 4)`, `confidence`, and the `indicators={ao, prev_ao}` echo are diagnostic/formatting — read by zero order-gating comparisons (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): entry requires `AO_t > 0`; exit requires `AO_t < 0` — jointly unsatisfiable on every bar, degenerate or otherwise. Empirically confirmed this cycle: the real rule evaluated over 140 synthetic bars prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and every return hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the fresh zero-cross down is the sole position-ending path. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the eventual cross-down exit (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further entry-edge bars as hold-no-ops — no pyramiding, no averaging; a flat book treats exit-leg bars as no-ops; re-entry re-arms on any qualifying fresh cross-up after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low` (inside the median) and `close` (for the diagnostic price echo only — never inside the entry/exit predicate) with fixed non-positive offsets (`iloc[-1]`/`iloc[-2]` only — no forward reference); the decision bar's own `open` and `volume` are never read (census zero). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set is class metadata read by zero signal lines.

## Required data

- Completed `1d` bars of BTCUSDT spot: `high`/`low` (inside the pinned median-price construction only), `close` (diagnostic price echo only — the entry/exit predicate reads the oscillator, never the close level). No `open` read, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (researcher pin, disclosed — the file declares no frame; the rule is pure bar-count logic so any fixed interval preserves the predicates; `1d` rides the `forven-naked-donchian-20` `1d` precedent — no novel-interval confirmation burden attaches).
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below); the decision/fill effective time for row `t` is `timestamp_t + 86400s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete and `close_t` is the current market print: signals read no future, fills take no future. Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 86400s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (researcher pin, disclosed): 60 completed `1d` bars held flat. Covers the source's own 36-bar guard (seeding the 34-bar slow SMA plus the one-bar `iloc[-2]` edge) with margin. Coded behaviour underneath: rolling windows print NaN until seeded and IEEE comparisons against NaN are all False (`nan <= 0`, `nan > 0`, `nan >= 0`, `nan < 0` — every leg fails), so no leg can fire early even at the guard boundary; the guard additionally collapses short frames to neutral. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT spot, unleveraged (researcher choice — the roster names `"BTC"` only; the file's `"leverage": 1.0` defaults hint is explicitly adopted as unleveraged spot; no source-market equivalence is claimed).
- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`; verified ancestor of that repository's current HEAD this cycle): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue, `_get_rest_candles_params`; `"1d"` is a member of the pinned `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting. MARKET executors fill at the creation row's timestamp and close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the decision bar's own close at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): the controller keeps its own fill ledger (created BUY executor ids with base qty) with states flat/long(Q). On row `t` it evaluates the source predicates over completed bars `≤ t`; flat+entry creates one MARKET BUY for `Q = 0.001` BTC and records long(Q); long+exit creates one MARKET SELL for `Q` and records flat; long+entry is a hold-no-op; flat+exit is a no-op. Exit sizing comes from the controller's own ledger, never from engine timing. Engine `positions_held`/`executors_info` timing (including the one-row hold-conversion lag inside `update_state` and the 3600s terminated-executor view window, `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 3600`) never gates a decision — the design is window-independent by construction, which is exactly what the `1d` (86400s) spacing requires. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim fee line); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and the configured quantity is `Q = 0.001` BTC. The simulator explicitly converts `config.amount` to binary float before multiplying by the close, and `ExecutorSimulation` converts the resulting float quote amounts to `Decimal`; binary floating-point rounding and tiny residual base balances after netting are therefore possible. Exact decimal representability and exact net-zero engine holds are not claimed. As specified above, controller-memory flat/long state, not the engine hold `is_closed` flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path (`BacktestPositionHold.add_executor` accumulates both; `get_position_summary` reports them separately). Explicitly fenced: the engine `net_pnl_quote` summary field is gross-only (it does not deduct hold fees) and `update_state total_pnl` mixes open-hold unrealized with executor realized — neither label is used here as fee-inclusive equity or closed-trade cash; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state. The file's `1.0` leverage hint is adopted exactly as this unleveraged posture and no perps/isolated-margin accounting is admitted.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (110 lines: the median-price/SMA-difference block, the one-bar edge entry/exit, the `TYPE_NAME`/roster registration, and the `{"fast_period": 5, "slow_period": 34, "leverage": 1.0}` defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, local pandas/numpy venv): the REAL `OrderExecutorSimulator.simulate`, the REAL `BacktestPositionHold` class (AST-extracted from the pinned file, unmodified), and the REAL `awesome_oscillator.py` rule running on the REAL `forven/strategies/base.py` (byte-identical blob) — hummingbot enum/config names carried by minimal stand-ins with identical member names/values (`TradeType`, `CloseType`, `ExecutionStrategy`, `OrderExecutorConfig`, `ExecutorSimulation`, `ExecutorInfo`), no behavioural stubbing. 25 asserts, all passing:

- R1 defaults pin (1 assert): strategy resolves `fast 5 / slow 34 / leverage 1.0` under pinned defaults.
- R2–R8 rule causality (7 asserts): short-frame guard neutral on bars 0–34; long-only on every bar; zero entry/exit co-print bars over 140 synthetic bars; prefix evaluation equals full-frame point-in-time edge on every eligible bar (no future read by construction); both legs fire on synthetic tape; flat tape (AO exactly 0.0) holds neutral; monotonic ramp refires at most one entry edge.
- V1 MARKET-fill primitive (5 asserts): BUY `0.001` base fills at the creation row's close, `POSITION_HOLD`, `filled_quote = amount × close` exact, `cum_fees = trade_cost × quote` exact, engine `net_pnl_quote` stays `0` (gross-only label, as fenced).
- V2 hold-netting primitive (5 asserts): BUY `0.001 @ 100000` then SELL `0.001 @ 110000` at cost `0.001`/side → closed (`net_base = 0`), gross `10.0`, `cum_fees 0.21`, `net = gross − fees = 9.79` — the stated economics identity on engine primitives.
- V3 code-evidence asserts (7 asserts): `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 3600` literal present; `collect_executors_ledger` completeness docstring present; MARKET-first-candle comment present; hold realized/fee accumulation split present; `INTERVALS` contains `1d`; REST parse uses `row[0]` open-time; `timestamp + 86400s` mapping asserted on a synthetic `1d` grid. Not a performance backtest, not a deployment — a primitive capability check, exactly the once-per-new-requirement validation the contract calls for.

### Negative evidence

1. Leading-window behaviour fenced: rolling seeds print NaN until windowed and every IEEE NaN comparison in the gating path is False; the file's explicit `len(df) < 36` guard collapses short frames to neutral. The 60-bar researcher floor additionally holds all pre-seed bars flat — disclosed, not repaired.
2. Exact-touch rule fenced: entry demands strict `curr_ao > 0` with setup `prev_ao <= 0`; exit demands strict `curr_ao < 0` with setup `prev_ao >= 0`. A print of exactly `0.0` fires neither leg — touches hold the prior state, disclosed, not smoothed.
3. `close`-level quarantine fenced: `curr_close` enters only the diagnostic `price=round(curr_close, 4)` echo and the confidence denominator — the entry/exit predicate reads the oscillator only. Promoting a close level (e.g. a close-above-MA gate) into a leg would be a different, unpinned rule with different trade events.
4. Diagnostic quarantine fenced: `confidence` (entry-only scaled magnitude else 0.0), `price=round(curr_close, 4)`, and the `indicators={ao, prev_ao}` dict are envelope decoration read by zero order-gating comparisons; `compatible_regimes` (`TREND_UP`/`TREND_DOWN`) is class metadata read by zero signal lines; the `PREBUILT-AO` roster row is an asset label, not a rule.
5. Variant menus fenced: `parameter_space()` (`fast_period` 3–7 step 1, `slow_period` 28–40 step 2) is a tuning grid read by zero signal lines — this record freezes canonical `5/34` as written; adopting any grid point would change trade events and is never claimed here.
6. Pool Pine AO sibling fenced: `awesome-oscillator-zero-cross-reversal-two-sided-btcusdt-4h-2026-10-12` (EternaHybridExchange Pine source, two-sided, `4h`) differs on immutable source, directionality (its short leg reverses where this record stands flat — different trade events on every down-cross), and frame. Neither record is the other's provenance.
7. Pool freqtrade AO sibling fenced: `freqtrade-awesome-macd-ao-cross-macd-gated-long-flat-btcusdt-1h-2026-10-20` (AwesomeMacd.py: AO cross AND-gated with a MACD condition, `1h`) differs on source file, gate (veto vs none — a veto-failed cross fires there never, while any veto-failed cross fires here), and frame. Not a threshold re-tuning of it: changing this record's construction to add a MACD gate would be a different, unpinned rule.
8. Pool MA-cross cousins fenced: `forven-dema/tema/hma-cross` records trade price-line crossings of moving averages, never a median-price-difference oscillator crossing the zero line — none evaluates `SMA(mp,5) − SMA(mp,34)` sign edges; the pool's `forven-obv-ema-cross` cousin crosses an OBV line through its own average (volume-derived, different primitive and data). None is this construction.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+86400s` mapping; fills are never claimed intrabar; the 3600s terminated view is never relied on for position state.
10. Derivation boundary fenced: the only non-source-native behaviours are the BTCUSDT-spot-`1d` market/frame pin, the effective-time MARKET-close fills, the single-unit/controller-memory/warmup pin, the pinned cost model with leverage `1.0` adopted as unleveraged, and the `+86400s`/gap data rule — all predeclared above. The 5/34 median-price construction, the zero-cross entry/exit with all strictness, the guard, the long-only stance, and the no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: AO 5/34 median-price construction / zero-cross entry-exit pair with pinned strictness / long-only / no-stop posture / single-unit `0.001` BTC / `1d` BTCUSDT spot / effective-time close fills are frozen.

- F1 — Slow-length relevance: replacing the 34-bar slow SMA with a 21-bar slow SMA (same fast 5, same edges, same posture) must not improve net expectancy; fail ⇒ the slow 34-bar memory adds nothing over a faster oscillator and the record is a label variant of one.
- F2 — Exit-leg relevance: dropping the cross-down exit entirely (entries only, never exiting — buy-and-hold from the first cross) must not improve net expectancy; fail ⇒ the exit leg carries no weight beyond decoration.
- F3 — Edge-vs-level relevance: entering on every bar with positive AO (level-hold instead of the prior-bar cross edge, same exit) must not improve net expectancy; fail ⇒ the cross-edge timing adds nothing over a persistent momentum state.

## Crypto portability

BTCUSDT spot `1d` is the research pin (roster names `"BTC"` only). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Late entries by construction: the 34-bar slow SMA lags price after any V-turn, so recoveries are entered strictly after the histogram prints a fresh cross-up — disclosed lag profile.
- Chop whipsaw: alternating small positive/negative histogram prints alternating cross-up/cross-down edges print repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- Crash-through blindness: a bar that gaps the histogram from positive to deeply negative exits one bar later — there is no stop order to front-run it, disclosed.
- No risk leg: no stop loss, take profit, ROI rung, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions have no capital guardrail besides the cross-down exit.
- Downtrend blindness: declines are watched from flat with no short participation — the zero-`short` posture is a stance choice with a return cost in sustained downtrends, disclosed.
- Single-market scope: derived pin is BTCUSDT spot `1d` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived pins and the stated economics identity — not the source engine's own semantics, and not the engine summary labels fenced above.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/awesome_oscillator.py
- https://github.com/judder659/Forven
