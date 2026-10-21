---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade BinHV45 BB-penetration delta-guard long-flat on BTCUSDT 1m bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BinHV45.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade BinHV45 BB-penetration delta-guard long-flat on BTCUSDT 1m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/BinHV45.py`.
- GitHub blob SHA at the pinned commit: `c03bd418a95daddddc6f76cc320ffee9151627a5`, size 2641 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2641 bytes, 71 lines, SHA-256 `ae76994b6fc8dd1937d84fc6d5ef0b9d7b702f01f61f5ccf5a2870278a3422a2`, identical to the GitHub blob (`git hash-object` reproduces `c03bd418…1627a5`) — the entire file was retrieved and inspected.
- Registration: the file defines class `BinHV45(IStrategy)` (the only class in the file) plus one module-level helper `bollinger_bands()` (defined lines 12-17, never called anywhere in the file — dead helper, fenced below). `INTERFACE_VERSION: int = 3` (framework marker, no gate effect).
- The file's own words (quoted for gate evidence, never extended): `minimal_roi = { "0": 0.0125 }` (single rung); `stoploss = -0.05`; `timeframe = '1m'`; indicators `bollinger = qtpylib.bollinger_bands(dataframe['close'], window=40, stds=2)` with `mid`/`lower` kept, `bbdelta = (mid - lower).abs()`, `pricedelta = (open - close).abs()` (dead column, fenced below), `closedelta = (close - close.shift()).abs()`, `tail = (close - low).abs()`; entry `lower.shift().gt(0) & bbdelta.gt(close * buy_bbdelta.value / 1000) & closedelta.gt(close * buy_closedelta.value / 1000) & tail.lt(bbdelta * buy_tail.value / 1000) & close.lt(lower.shift()) & close.le(close.shift())` (`enter_long = 1`); exit `dataframe.loc[:, 'exit_long'] = 0` under the docstring `no sell signal`. No `trailing`, no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only`, no `process_only_new_candles`, no `position_adjustment`, no `order_types`, no `leverage`, no `max_open_trades`, no protections ship anywhere.
- Parameter resolution (pinned in-file, disclosed): `buy_params = { "buy_bbdelta": 7, "buy_closedelta": 17, "buy_tail": 25 }` is the file's loaded parameter set, so the entry leg resolves to `close * 0.007`, `close * 0.017`, `bbdelta * 0.025`. The three `IntParameter(low, high, default, space='buy', optimize=True)` constructor triples are hyperopt search-space declarations pinned in the same file but never read by any gating line; no optimization runs in the admitted version and no fitted value enters it beyond these three literals.
- Full-file token census (verified over the 71 lines this cycle): 0 `short` (case-insensitive — no short leg; framework default long-only applies, disclosed default, never a file literal); 0 `volume`; 4 `shift` (lines 49, 56, 60, 61 — the complete lag inventory: one `close.shift()` in `closedelta`, one `lower.shift()` in the positivity guard, one `lower.shift()` and one `close.shift()` in the entry); 1 `hyperopt` (line 34 comment only); `Parameter` on 4 lines (import plus three constructors) plus 1 comment line; 0 `trailing`; 0 `resample` / 0 `informative`; 0 `request` / 0 `security`; 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades`; 0 `leverage` / 0 `funding` / 0 `mark_price`; 0 `order_types`; 0 `protections`; 0 `can_short` / 0 `use_exit` / 0 `startup`; 0 `DCA` / 0 `grid`. `numpy` is imported and never called (dead import, no gate effect).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1m` frame, the six-conjunct BB(40,2)-penetration entry with the `{7, 17, 25}` parameter set, the absent exit signal (`exit_long` identically 0), the single-rung `0.0125` ROI, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly five: (1) research market BTCUSDT on Binance spot (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) one-bar publication lag — the decision at event timestamp `T_i` reads the entry conjunction computed on bars strictly before `i` (completed-bar semantics; derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 41-bar researcher warmup floor (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) source `stoploss = -0.05` researcher-disabled (`stop_loss = None`) with the rationale quoted in Execution assumptions (disclosed, never presented as source-native risk); (5) sizing and costs ride the explicit derived cost model below (continuous accounting, `trade_cost = 0.001` per side; no hypothetical zero funding claimed — there is no funding leg on the declared spot path at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `BinHV45` returns zero records pinning this file — the only pool hits are sibling-fences inside the admitted `freqtrade-combined-binh-cluc` record (which names `BinHV45.py` as a different pin with different constants) and the admitted `freqtrade-binhv27` record (a different file, different mechanism — see Negative evidence). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian ratio) trades a BB-penetration delta-guard conjunction. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where close penetrates below the shifted 40-bar lower Bollinger band while the band sits above zero, the band width exceeds 0.7% of close, the bar-to-bar close move exceeds 1.7% of close, and the lower wick is under 2.5% of the band width, with close also not above the prior close. No exit signal exists (`no sell signal`); the single `0.0125` ROI rung and the `-0.05` stop backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Breakdown-penetration dip machine, long-only, TP-only exits. The `close < lower.shift()` leg supplies the penetration event while the three delta guards veto penetrations printed without band width (`bbdelta`), without bar conviction (`closedelta`), or with an excessive lower wick (`tail`) — so a drift through a flat band prints nothing, a tiny-bodied touch prints nothing, and a long-wicked rejection prints nothing either. Unlike state records (trade every qualifying bar), the positioned book treats further entry bars as hold-no-ops until the TP rung fires; unlike signal-exit records, nothing here ever exits on an oscillator reclaim — a position that never reaches +1.25% net is held to the end of data by explicit rule, never by omission.

## Signal

Exact rule as pinned (any other BB window, std multiple, threshold, strictness, lag, risk rung, fill, frame, or book is a different, unpinned rule). Parameter set `{7, 17, 25}` is the file's `buy_params`, disclosed above:

```text
mid[t], lower[t] = 40-bar rolling mean / mean-minus-2x-sample-std of close  // qtpylib BB(40,2); pandas semantics, ddof=1; see Required data
bbdelta[t]    = |mid[t] - lower[t]|
closedelta[t] = |close[t] - close[t-1]|
tail[t]       = |close[t] - low[t]|
enter[k]      = (lower[k-1] > 0) AND (bbdelta[k] > 0.007 * close[k])
                AND (closedelta[k] > 0.017 * close[k]) AND (tail[k] < 0.025 * bbdelta[k])
                AND (close[k] < lower[k-1]) AND (close[k] <= close[k-1])   // enter_long = 1
signal[i]     = enter[i-1] for i >= 41, else 0                            // one-bar publication lag; pre-floor flat
exit_sig[i]   = 0 for all i                                               // source-verbatim: no sell signal
risk          = take_profit 0.0125 on close-based net-of-cost return (fraction); stop_loss None;
                trailing None; time_limit None (held to data end — see Execution assumptions)
floor         = first 41 one-minute bars flat (see Required data)
```

- Trade events: `signal = 1` opens the full single unit on a flat book (long-only; `signal` never negative); a positioned book treats further `signal = 1` bars as hold-no-ops under the position pin below. `exit_sig` is identically 0 — there is no signal exit in the source or in this version. The TP rung and the data-end rule are the complete position-closing set.
- Exact boundaries (pinned semantics): five strict comparisons (`lower.shift() > 0`, `bbdelta > 0.007 * close`, `closedelta > 0.017 * close`, `tail < 0.025 * bbdelta`, `close < lower.shift()`) plus one inclusive comparison (`close <= close.shift()`). A bar exactly on any strict threshold fires nothing on that leg; a bar with `close` exactly equal to the prior close satisfies the sixth leg. All preserved throughout.
- Tie-break proof (no tie-break pin required): the exit leg is identically 0, so entry and signal-exit never co-print on any bar, degenerate or otherwise. The TP leg cannot co-fire with entry on the entry bar either: the simulator books entry-row net return as `-2 * trade_cost = -0.002`, which never satisfies the strict `> 0.0125` TP scan (see Execution assumptions). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the file sets no `can_short` (framework default long-only applies — disclosed default, never a file literal). The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Position rule (predeclared researcher pin, executed by pinned base-class logic — see Execution assumptions): single-unit, at most one open position per market (`max_executors_per_side = 1`); a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats risk legs as no-ops; re-entry re-arms on any qualifying published-signal bar after any close (`cooldown_time = 1`, the minimum legal value — disclosed pin, never a file semantic). Pre-floor bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`low` (`open` appears solely in the dead `pricedelta` column, never in any gate) through fixed non-negative offsets (40-bar rolling window plus one-bar `shift`) with no forward reference; the decision at event timestamp `T_i` reads `signal[i] = enter[i-1]`, i.e. bars at or before `i - 1` only — the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt search, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1m` bars of BTCUSDT: `close` and `low` only (BB/mid/delta guards on `close`; `tail` on `close`/`low`). No bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (source-native — the file prints `timeframe = '1m'`). `1m` is a supported Binance-spot interval on the pinned path (`INTERVALS` in `binance_spot_candles/constants.py` lists `1m`; REST `GET /api/v3/klines`). One evaluation per completed bar; every window reads the decision event's causal past only (plus the one-bar publication lag); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 41 one-minute bars held flat. Covers the 40-bar BB seed plus the one-bar `shift` (first fully-defined row is index 40, i.e. the 41st bar). The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: the BB rolling windows seed over the leading bars and every strict/inclusive NaN comparison is false — no leg can fire early; the 41-bar floor additionally holds every pre-seed bar flat. The qtpylib `min_periods` library variant is fenced by the same floor: once the 40-bar window is full, all variants agree, and no pre-floor bar can trade either way. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT on Binance spot (`connector_name = "binance"`, trading pair `BTC-USDT`, `leverage = 1` — the config base's own prompt reads "Set it to 1 for spot trading"). Researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed. Spot structurally has no funding leg, and the pinned simulation path contains no funding term at all (zero `funding` hits in `backtesting_engine_base.py`, `position_executor_simulator.py`, and `directional_trading_controller_base.py` at the pinned commit — verified this cycle), so no funding model is missing and none is defaulted to zero.
- Pinned engine: `hummingbot/hummingbot@fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467` (2026-09-20; `hummingbot/VERSION` reads `dev-2.17.0`, verified byte-for-byte this cycle), i.e. the README baseline package `20260920` / `dev-2.17.0`. Applicable path: `DirectionalTradingControllerBase` + `PositionExecutorConfig` (market entry) + `PositionExecutorSimulator`, fed by `BinanceSpotCandles` `1m`.
- Time contract (candle-open label → completed-bar availability → decision/fill, each mapping enforced at the cited line):
  1. Candle-open label: `_parse_rest_candles` (`binance_spot_candles.py:80-85`) maps Binance kline `row[0]` (open time) to row `timestamp`; `prepare_market_data` (`backtesting_engine_base.py:470`) sets the event `timestamp = timestamp_bt`, i.e. every event is labelled by its bar's open time.
  2. Completed-bar availability: `signal[i] = enter[i-1]` uses bars at or before `i - 1` only; bar `i - 1` completes exactly at `T_i`, so the signal is available at the decision event. The features merge (`backtesting_engine_base.py:466-468`, `merge_asof` backward on `timestamp_bt`) hands row `i` the latest feature at or before `T_i`, i.e. exactly `signal[i]`.
  3. Decision timestamp: `simulate_execution` (`backtesting_engine_base.py:282-284`) runs `update_state(row)` (price becomes the row's `close_bt`, provider time becomes the row's open-label timestamp — lines 364-368) and then `determine_executor_actions()` at that same event.
  4. Signal-to-action: the base controller creates one `PositionExecutorConfig` market entry when scalar `signal != 0` and `can_create_executor` holds (`directional_trading_controller_base.py:167-183`); with `max_executors_per_side = 1` a positioned book blocks further creates (line 193) and `cooldown_time = 1` re-arms entry on the next bar (line 194, strict `>`); `stop_actions_proposal` is identically empty (lines 197-202), matching the source's absent exit signal with no adaptation.
  5. Fill: `open_order_type = MARKET` is hardcoded in the base `triple_barrier_config` property (lines 124-135), so the simulator's market-entry branch applies: `start_timestamp` is the slice minimum, i.e. the decision event `T_i`, and `entry_price` is that row's `close` (`position_executor_simulator.py:11-16, 40`). Decision at open label, fill at that bar's close — both timestamped `T_i`, causally ordered (close is known after open), with no maker-touch, queue, or intrabar-path-dependent fill anywhere.
- Risk legs on the pinned simulator, all close-evaluated on the same rows (trigger and settlement share each row's close — no intrabar ordering assumption is needed):
  - Take-profit (source-native, single scalar): `take_profit = 0.0125`; `net_pnl_pct = side * (cumprod(1 + pct_change(close)) - 1) - 2 * trade_cost` (lines 43-46); first row with `net_pnl_pct > 0.0125` closes the unit `TAKE_PROFIT` (line 58, strict `>`). Return basis is therefore close-to-close directional price return net of round-trip cost — on spot at 1× this equals the position return; no leverage-basis ambiguity exists in this version. The entry row books `-2 * trade_cost` and can never satisfy the scan.
  - Stop-loss (researcher-disabled, disclosed): `stop_loss = None`, so the low/high barrier scan (lines 60-64) is skipped entirely — the `if config.triple_barrier_config.stop_loss:` guard is False. Rationale: the source's `stoploss = -0.05` cannot be carried over because the pinned scan covers the entry bar's `low` with no start-timestamp filter (a pre-fill intrabar extreme could trigger it) while settlement would still book that row's close-based return (lines 46, 79) — an inconsistent barrier/settlement pair for a same-close-fill model that this record refuses to paper over. No SL leg exists in the admitted version.
  - Trailing (absent in source, absent here): `trailing_stop = None`; lines 22-24 and 52-56 skipped.
  - Time limit (researcher pin, disclosed): `time_limit = None`; `tl_timestamp` becomes the last data timestamp (line 26), so a position that never reaches TP is held flat-open to the end of data and closes `TIME_LIMIT` there (lines 66-76). The complete close-type set of this version is therefore `{TAKE_PROFIT, TIME_LIMIT}` — `STOP_LOSS`, `TRAILING_STOP`, `EARLY_STOP` (needs a stop action the base path never emits), `POSITION_HOLD`, and `FAILED` cannot occur.
- Sizing/capital/costs (derived cost model, completely specified — nothing deferred downstream): `total_amount_quote = 1000` (matches the results denominator default); `amount = total_amount_quote / price / max_executors_per_side` per base line 177 — continuous Decimal division with no rounding step in the path; `filled_amount_quote = amount * entry_price` (sim line 47); `trade_cost = 0.001` per side (researcher-pinned 10 bps taker-class assumption, not a venue-schedule claim); `cum_fees_quote = 2 * trade_cost * filled_amount_quote` (sim line 49). Precision is explicitly declared as continuous/unquantized research accounting: no tick-size rounding, no lot-size quantization, no minimum-notional enforcement — the position simulator never reads trading rules (zero `trading_rule` hits, verified), so no hidden precision layer exists in the modeled path.
- Concurrency: at most one position per market at any time; the published-signal edge opens the full unit on a flat book; the TP rung or the data-end rule closes it in full; re-entry after a close needs only the next qualifying published-signal bar. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (71 lines: the BB(40,2) call, the four derived columns, the six-conjunct entry, the identically-zero exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `BinHV45(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling windows seed over the leading bars and every NaN comparison is false (no early entry possible); the 41-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: five legs are strict (`>`, `>`, `>`, `<`, `<`) while the sixth is inclusive (`<=`) — a bar sitting exactly on any strict threshold fires nothing on that leg; a bar with `close` exactly equal to the prior close satisfies the sixth leg. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-code plumbing fenced: the module-level `bollinger_bands()` helper (lines 12-17) is defined and never called; `pricedelta` (line 48) is computed and read by no gating line; `Dict`, `List`, `reduce` are imported and never called; `numpy` is imported and never called; `macdhist`-style leftovers do not exist here. All display/plumbing leftovers with no gate effect, never repaired into a signal. Zero fitted values enter the admitted version beyond the pinned `{7, 17, 25}` literals.
4. Hyperopt-metadata fence: the three `IntParameter` constructor triples (search ranges and out-of-range defaults `30`) are optimizer configuration, never read by `populate_entry_trend` — the entry leg reads only `self.buy_X.value`, resolved by the file's `buy_params` to `{7, 17, 25}`. No search runs in the admitted version; thresholds are literals.
5. `min_periods` fence: the qtpylib BB variant computes expanding-window bands on the leading bars, but the 41-bar flat floor makes the variant immaterial — no pre-floor bar can trade, and all variants agree once the 40-bar window is full. Post-floor behaviour is exactly the stated rolling-mean/sample-std construction.
6. Cousin records fenced as different constructions (none trades a six-conjunct BB(40,2)-penetration with per-mille delta guards, TP-only exits, long-flat, on `1m`): the admitted `freqtrade-combined-binh-cluc` pool-mate trades a DIFFERENT file's dual-leg OR entry on `5m` — its BinH leg hardcodes `0.008 / 0.0175 / 0.25` (the tail guard is 10× looser: `0.25` vs this record's `0.025`, a materially different selectivity), adds a Cluc EMA50/BB-discount second leg, exits on a BB-mid profit gate, and risks `0.05` ROI — every trade event differs; the admitted `freqtrade-binhv27` pool-mate trades the SIBLING file's RSI/ADX/DI/SMA regime-state system on `5m` with a five-arm reclaim exit (different primitives, different frame, different exit machine); the admitted CofiBit/Scalp-family siblings trade EMA-rail plus stochastic-cross systems with rail-reclaim exits (never BB-penetration guards); the pool's MACD/AO/SMA siblings trade oscillator-cross systems (never level-penetration conjunctions). Not a threshold re-tuning of any of them: moving the BB window, the std multiple, any guard constant, any strictness, the publication lag, the TP rung, or the frame would each be a different, unpinned rule — none is admitted here.
7. Sibling-file fence: `CombinedBinHAndCluc.py`, `BinHV27.py`, `ClucMay72018.py`, `CofiBitStrategy.py`, `Scalp.py`, `SmoothScalp.py`, `MACDStrategy.py`, and every other file in the pinned directory are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market choice, the one-bar publication lag with same-bar-close fills, the single-unit/no-add/`cooldown_time = 1` position pin, the 41-bar warmup floor (the file ships none), the `stop_loss = None` / `time_limit = None` risk pins (the file ships `stoploss = -0.05` and no time concept), the framework-default readings (long-only, per-completed-bar evaluation), the `buy_params` resolution of the entry thresholds, the standard-library BB arithmetic, and the derived sizing/cost/precision model — all predeclared above. The `1m` frame, the six-conjunct entry with all its literals and strictness, the absent exit signal, the single-rung `0.0125` TP, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: BB(40,2) / `{7, 17, 25}` guards with pinned strictness / six-conjunct entry / one-bar publication lag / no signal exit / `0.0125` TP / no SL / no trailing / no time exit / single-unit long-only / `1m` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — Band-width-guard relevance: dropping the `bbdelta` leg (penetration plus remaining guards, same risk) must not improve net expectancy; fail ⇒ the width veto adds nothing over raw penetration timing.
- F2 — Wick-guard relevance: dropping the `tail` leg (same entry otherwise, same risk) must not improve net expectancy; fail ⇒ the lower-wick veto adds nothing over the remaining conjunction.
- F3 — Risk-rung relevance: removing the TP rung (enter-and-hold to data end, no other exit) must not improve net expectancy; fail ⇒ the `0.0125` rung adds nothing over buy-and-hold selection.

## Crypto portability

BTCUSDT Binance spot `1m` is the research pin (source names no market). Long-only with full-unit open/close expresses natively on spot with no naked shorting and no funding leg. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Costs are the declared `0.001`-per-side model with continuous accounting; funding is structurally absent on the spot path, not assumed away.

## Limitations

- The `1m` frame rides existing admission precedent on `main` (several admitted `1m` Freqtrade-sourced records) and is a listed Binance-spot interval — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market that never prints +1.25% net is held to the end of data; there is no decay, chop, trend-loss, stop, trailing, or further time exit — disclosed, not repaired. The `-0.05` source stop is intentionally not carried (see Execution assumptions for the exact simulator rationale).
- TA-library internals (pandas rolling seeding, sample-std arithmetic) live outside the pinned file — pinned by call (`window = 40`, `stds = 2`) plus the disclosed ddof-1/floor fencing, not re-derived; exact reproduction inherits those libraries' arithmetic alongside the 41-bar floor.
- The `bollinger_bands()` helper, the `pricedelta` column, and the `numpy`/`Dict`/`List`/`reduce` imports are dead — nothing further to fence.
- No trailing, no short leg, no cooldown beyond the disclosed 1-second minimum — all explicitly absent or pinned, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BinHV45.py
- https://github.com/freqtrade/freqtrade-strategies
