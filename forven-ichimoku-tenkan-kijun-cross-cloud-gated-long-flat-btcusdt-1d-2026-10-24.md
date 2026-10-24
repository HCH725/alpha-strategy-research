---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Ichimoku 9-26-52 Tenkan-Kijun cross cloud-gated long-flat on BTCUSDT 1d bars
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
  - https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/ichimoku.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Ichimoku 9-26-52 Tenkan-Kijun cross cloud-gated long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the fifty-two admitted Forven records, including the `forven-awesome-oscillator-zero-cross` sibling admitted 2026-10-24 that pins the identical base-class blob below).
- Pinned commit SHA: `0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e` (verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is the cycle date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ichimoku.py`.
- GitHub blob SHA at the pinned commit: `14fb8825e2ccfe041014db200441e89f9c8bd2c6`, size 5871 bytes.
- Byte-identity check: the file on disk at the pinned commit is 5871 bytes, 159 lines, `git hash-object` reproduces `14fb8825…9c8bd2c6` — the entire file was retrieved and inspected.
- Registration: the file defines class `IchimokuStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "ichimoku"` and a one-row roster `STRATEGIES = [("PREBUILT-ICHIMOKU", IchimokuStrategy, {"_asset": "BTC"})]` — venue spelling is the bare `"BTC"` asset label only, no timeframe override. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): module docstring `Entry: Tenkan-sen crosses above Kijun-sen AND price is above the cloud (Senkou Span A & B)`, `Exit: Tenkan-sen crosses below Kijun-sen`; `default_params` returns exactly `{ "tenkan_period": 9, "kijun_period": 26, "senkou_b_period": 52, "leverage": 1.0 }`; vectorized twin (`generate_signals`, docstring: `the SINGLE source of entry/exit logic`) computes `tenkan = (high.rolling(9).max() + low.rolling(9).min()) / 2`, `kijun` over 26 identically, `senkou_a = ((tenkan + kijun) / 2).shift(26)`, `senkou_b = ((high.rolling(52).max() + low.rolling(52).min()) / 2).shift(26)`, NaN spans fall back to `close`, `cloud_top = max(senkou_a_eff, senkou_b_eff)`, `above_cloud = close > cloud_top`, `cross_up = (prev_tenkan <= prev_kijun) & (tenkan > kijun)`, `cross_down` mirrored, `entry = cross_up & above_cloud`, `exit_ = cross_down`, both `fillna(False)`; per-bar guard `len(df) < senkou_b + kijun + 2` (i.e. 80) returns the explicit no-signal `Signal`; every return hardcodes `direction="long"`; per-bar confidence is `min(1.0, (close - cloud_top) / (atr_14 * 3))` when above the cloud else `0.0` (with a `0.5` fallback only when `atr_14` is non-positive). No performance phrase of any kind ships anywhere in the 159 lines.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by the admitted AO sibling) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default, and `BaseStrategy.__init__(strategy_id, params)` merging `{**default_params, **params}`. The file's explicit `direction="long"` on every return needs no default reading.
- ATR provenance (verified this cycle, never assumed): the per-bar path's `from forven.strategies.indicators import atr` resolves through the module's PEP 562 `__getattr__` lazy facade (`_FACADE_NAMES` contains `"atr"`), re-exporting the pure helper `atr` from canonical home `forven.scanner` — actually imported and called this cycle. It feeds confidence decoration only (fenced, never promoted).
- Full-file token census (verified over the 159 lines this cycle): `def generate_signal` once plus `def generate_signals` once (per-bar path delegates its gating lines to the twin: `entries, exits = self.generate_signals(df)`); 0 `short` (no short leg, no short identifier anywhere); 0 `open` / 0 `volume` (sole `df[` reads are `close`/`high`/`low`); 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt` (the single case-insensitive `parameter` hit is the `parameter_space` def line only — a grid menu, never a signal input); 0 `trailing` / 0 `stoploss` / 0 `startup`; 0 `order_types`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `timeframe` / 0 `data_requirements` (the file declares no frame — the `1d` pin below is a disclosed researcher choice); 0 `fillna` beyond the twin's two `fillna(False)`; 0 `ffill` / 0 `interpolate` / 0 `dropna` / 0 `merge` / 0 `can_short` / 0 `nan_to_num`; 2 `direction` (the guard return plus the signal return, both `direction="long"`); the single `leverage` token is the `"leverage": 1.0` defaults entry — an unleveraged hint explicitly adopted (see Execution assumptions); 5 `atr` (import, computation, confidence, indicators echo — confidence-only); 9 `ichimoku` (class/docstring/registration prose, never a second rule).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the 9/26/52 Ichimoku construction, the Tenkan-Kijun edge-cross entry with the above-cloud gate and all strictness, the cross-down exit, the long-only stance, the short-frame neutral guard, and the no-stop posture — but ships no venue spelling beyond `"BTC"`, no frame, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/frame `BTCUSDT` spot `1d` (the roster names `"BTC"` and the file declares no frame; venue spelling and the `1d` decision-frame pin are disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 86400s` with MARKET fills at the decision bar's own close on the cited pinned-engine path (the file returns `price=round(curr_close, 4)` — the decision bar's own close; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit `0.001` BTC position pin with controller-memory state machine plus a 100-bar researcher warmup floor (covers the source's own 80-bar guard with margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no exchange lot/tick quantization in-path) replacing the absent source economics, with the file's `"leverage": 1.0` hint explicitly adopted as unleveraged spot. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `builtin/ichimoku.py`, `IchimokuStrategy`, `PREBUILT-ICHIMOKU`, and `TYPE_NAME = "ichimoku"` returns zero strategy records citing this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an Ichimoku rule. Not a duplicate, paraphrase, or trivial parameter variant: a naked 9/26/52 Tenkan-Kijun edge-cross with a pure cloud-position gate, long-flat, on `1d` bars from this immutable file is fenced against every Ichimoku pool-mate in Negative evidence 6–8.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar whose Tenkan-sen (9-bar high/low midpoint) crosses from at-or-below the Kijun-sen (26-bar midpoint) to strictly above it while the close prints strictly above the Ichimoku cloud top (max of Senkou A/B, NaN spans falling back to close); stand back to flat on the bar whose Tenkan-sen crosses from at-or-above to strictly below the Kijun-sen, with no cloud condition on the exit. The lines are pure trailing-bar high/low midpoints with no volatility normalization and no regime gate. No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Naked Ichimoku trend timer, long-only, edge-triggered, single veto (the cloud gate). Any fresh line-cross up with the close above the cloud enters, however thin the margin above the cloud top, and any fresh line-cross down exits even while price still holds above the cloud — the exit leg is cloud-blind. Unlike the pool's Pine triple-confirm sibling (Tenkan/Kijun level AND-gated with a MACD cross and a Chikou momentum leg — veto-failed crosses fire there never), flat here means only "no fresh cross printed" (or "cross printed under the cloud"), never "MACD/Chikou vetoed". Unlike oscillator-level systems (RSI threshold holds), there is no overbought profit-taking leg — a vertical advance is held with no exit while Tenkan stays above Kijun, and a grinding bleed under the cloud is watched from flat with no short participation. The failure mode is plain: chop that alternates shallow line crosses whipsaws the book with no cooldown, and the 52+26-bar cloud memory lags every V-turn — recoveries are entered strictly after both the cross and the cloud reclaim print.

## Signal

Exact rule as pinned (any other tenkan/kijun/senkou_b length, price input, trigger polarity, gate, frame, fill, book, or risk posture is a different, unpinned rule). `HH(n)/LL(n)` are trailing highest-high/lowest-low:

```text
tenkan_t = (HH(high, 9)[t] + LL(low, 9)[t]) / 2
kijun_t  = (HH(high, 26)[t] + LL(low, 26)[t]) / 2
senkouA_t = ((tenkan + kijun) / 2)[t-26]        // pandas .shift(+26): settled past value
senkouB_t = ((HH(high, 52) + LL(low, 52)) / 2)[t-26]
cloud_t  = max(senkouA_t, senkouB_t)            // NaN span falls back to close_t pre-seeding
ready    = positional length >= 80              // source guard: senkou_b + kijun + 2
entry_t  = (tenkan_{t-1} <= kijun_{t-1}) AND (tenkan_t > kijun_t) AND (close_t > cloud_t) AND ready
exit_t   = (tenkan_{t-1} >= kijun_{t-1}) AND (tenkan_t < kijun_t) AND ready
```

- Trade events: `entry_signal` on a fresh Tenkan-over-Kijun edge with the close above the cloud; `direction` long-only; `exit_signal` on a fresh Tenkan-under-Kijun edge with no cloud condition. Both legs are one-bar edge crosses (refires require a fresh cross back through the line). A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): strict current-bar comparisons (`>`, `<`) with setup legs (`<=`, `>=`) exactly as coded — a line touch (`tenkan == kijun`) fires neither leg; a close print exactly on the cloud top (`close == cloud_top`) fails the gate and holds the prior state. `price=round(curr_close, 4)`, `confidence`, and the `indicators={tenkan, kijun, senkou_a, senkou_b, above_cloud, atr_14}` echo are diagnostic/formatting — read by zero order-gating comparisons (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): entry requires `tenkan_t > kijun_t`; exit requires `tenkan_t < kijun_t` — jointly unsatisfiable on every bar, degenerate or otherwise. Empirically confirmed this cycle: the real rule evaluated over a 300-bar synthetic tape prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and every return hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the fresh cross-down is the sole position-ending path. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the eventual cross-down exit (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further entry-edge bars as hold-no-ops — no pyramiding, no averaging; a flat book treats exit-leg bars as no-ops; re-entry re-arms on any qualifying fresh cross-up after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low` (inside the line/cloud construction) and `close` (cloud gate plus the diagnostic price echo — the exit predicate reads the lines only) with fixed non-positive offsets (`iloc[-1]`/`iloc[-2]`, `.shift(1)`, `.shift(26)` — positive pandas shifts are lags, never forward references); the decision bar's own `open` and `volume` are never read (census zero). The `.shift(26)` Senkou displacement is causal by construction: the value read at row `t` was computed from rows `≤ t−26` (the forward plot displacement is display; order logic reads the settled lagged value — the same causal reading the admitted Pine triple-confirm record verifies with its `[25]` back-shift). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set is class metadata read by zero signal lines.

## Required data

- Completed `1d` bars of BTCUSDT spot: `high`/`low` (Tenkan/Kijun/Senkou construction), `close` (above-cloud gate plus diagnostic price echo — the exit predicate reads the lines only). No `open` read, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (researcher pin, disclosed — the file declares no frame; the rule is pure bar-count logic so any fixed interval preserves the predicates; `1d` rides the `forven-naked-donchian-20` `1d` precedent — no novel-interval confirmation burden attaches).
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below); the decision/fill effective time for row `t` is `timestamp_t + 86400s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete and `close_t` is the current market print: signals read no future, fills take no future. Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 86400s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (researcher pin, disclosed): 100 completed `1d` bars held flat. Covers the source's own 80-bar guard (seeding the 52-bar Senkou window plus its 26-bar lag plus the one-bar edge, with margin 20). Coded behaviour underneath: rolling windows print NaN until seeded and IEEE comparisons against NaN are all False, so no leg can fire early even at the guard boundary; the twin's NaN→close fallback additionally collapses every pre-seeded cloud gate to `close > close = False`, so warmup bars cannot smuggle an entry through the gate; the guard collapses short frames to neutral. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT spot, unleveraged (researcher choice — the roster names `"BTC"` only; the file's `"leverage": 1.0` defaults hint is explicitly adopted as unleveraged spot; no source-market equivalence is claimed).
- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`; verified ancestor of that repository's current HEAD this cycle): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue, `_get_rest_candles_params`; `"1d"` is a member of the pinned `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting. MARKET executors fill at the creation row's timestamp and close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the decision bar's own close at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): the controller keeps its own fill ledger (created BUY executor ids with base qty) with states flat/long(Q). On row `t` it evaluates the source predicates over completed bars `≤ t`; flat+entry creates one MARKET BUY for `Q = 0.001` BTC and records long(Q); long+exit creates one MARKET SELL for `Q` and records flat; long+entry is a hold-no-op; flat+exit is a no-op. Exit sizing comes from the controller's own ledger, never from engine timing. Engine `positions_held`/`executors_info` timing (including the one-row hold-conversion lag inside `update_state` and the 3600s terminated-executor view window, `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60 * 60` in `backtesting_engine_base.py`, which is exactly what the `1d` (86400s) spacing requires) never gates a decision — the design is window-independent by construction. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim fee line); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and the configured quantity is `Q = 0.001` BTC. The simulator explicitly converts `config.amount` to binary float before multiplying by the close, and `ExecutorSimulation` converts the resulting float quote amounts to `Decimal`; binary floating-point rounding and tiny residual base balances after netting are therefore possible. Exact decimal representability and exact net-zero engine holds are not claimed. As specified above, controller-memory flat/long state, not the engine hold `is_closed` flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path (`BacktestPositionHold.add_executor` accumulates both; `get_position_summary` reports them separately). Explicitly fenced: the engine `net_pnl_quote` summary field is gross-only (it does not deduct hold fees) and `update_state total_pnl` mixes open-hold unrealized with executor realized — neither label is used here as fee-inclusive equity or closed-trade cash; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state. The file's `1.0` leverage hint is adopted exactly as this unleveraged posture and no perps/isolated-margin accounting is admitted.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (159 lines: the Tenkan/Kijun/Senkou block, the one-bar edge entry/exit with the cloud gate, the `TYPE_NAME`/roster registration, and the `{"tenkan_period": 9, "kijun_period": 26, "senkou_b_period": 52, "leverage": 1.0}` defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, local pandas/numpy venv): the REAL `OrderExecutorSimulator.simulate`, the REAL `BacktestPositionHold` class (AST-extracted from the pinned file, unmodified), and the REAL `ichimoku.py` rule running on the REAL `forven/strategies/base.py` (byte-identical blob) — hummingbot enum/config names carried by minimal stand-ins with identical member names/values (`TradeType`, `CloseType`, `ExecutionStrategy`, `OrderExecutorConfig`, `ExecutorSimulation`, `ExecutorInfo`), no behavioural stubbing. 46 asserts, all passing:

- A1–A4 source identity (4 asserts): forven HEAD equals the pinned commit; `ichimoku.py` blob `14fb8825`, 5871 bytes, 159 lines; `base.py` blob equals the sibling-pinned `27508a2a`.
- R1 defaults pin (1 assert): strategy resolves `tenkan 9 / kijun 26 / senkou_b 52 / leverage 1.0` under pinned defaults.
- R2–R13 rule causality (21 asserts): short-frame guard neutral on 79-bar frames with boundary evaluation at 80 bars; long-only on every sampled bar; zero entry/exit co-print bars over a 300-bar synthetic tape; prefix evaluation equals full-frame point-in-time edges on 25 prefixes per leg (no future read by construction); both legs fire on synthetic tape (pinned seed 1); flat tape holds neutral; monotonic ramp refires at most one entry edge; per-bar `generate_signal` (exercising the real lazy-`atr` facade path) agrees with the vectorized twin on 6 prefixes per leg; no negative shift anywhere and every `.shift()` offset non-negative; census zeros for short/volume/funding/trailing/stoploss/pyramid/cooldown/timeframe; exactly 2 `direction` and 1 `leverage` tokens.
- V1 MARKET-fill primitive (5 asserts): BUY `0.001` base fills at the creation row's timestamp and close, `POSITION_HOLD`, `filled_quote = amount × close` (1e-9), `cum_fees = trade_cost × quote` (1e-12), engine `net_pnl_quote` stays `0` (gross-only label, as fenced).
- V2 hold-netting primitive (5 asserts): BUY `0.001 @ 100000` then SELL `0.001 @ 110000` at cost `0.001`/side → closed (`net_base = 0`), gross `10.0` exact, `cum_fees ≈ 0.21` (1e-9 — binary-float dust disclosed), `net = gross − fees ≈ 9.79` — the stated economics identity on engine primitives.
- V3 code-evidence asserts (7 asserts): `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60 * 60` literal present; `collect_executors_ledger` present; MARKET-first-candle comment present; hold realized/fee accumulation split present; `INTERVALS` contains `1d`; REST parse uses `row[0]` open-time; `timestamp + 86400s` mapping asserted on a synthetic `1d` grid. Not a performance backtest, not a deployment — a primitive capability check, exactly the once-per-new-requirement validation the contract calls for.

### Negative evidence

1. Leading-window behaviour fenced: rolling seeds print NaN until windowed and every IEEE NaN comparison in the gating path is False; the twin's NaN→close span fallback collapses every pre-seeded cloud gate to `close > close = False`; the file's explicit `len(df) < 80` guard collapses short frames to neutral. The 100-bar researcher floor additionally holds all pre-seed bars flat — disclosed, not repaired.
2. Exact-touch rule fenced: entry demands strict `tenkan > kijun` with setup `prev_tenkan <= prev_kijun` plus strict `close > cloud_top`; exit demands strict `tenkan < kijun` with setup `prev >= prev`. A line touch or a close print exactly on the cloud top fires neither leg — touches hold the prior state, disclosed, not smoothed.
3. `close`-level scope fenced: `close` enters the entry predicate only through the `close > cloud_top` gate — the exit predicate reads the Tenkan/Kijun lines only, so a cross-down exits even with price still above the cloud. `curr_close` otherwise enters only the diagnostic `price=round(curr_close, 4)` echo and the confidence denominator. Promoting any other close level (e.g. a close-above-MA gate) into a leg would be a different, unpinned rule with different trade events.
4. Diagnostic quarantine fenced: `confidence` (cloud-distance scaled by ATR14, entry context only), `price=round(curr_close, 4)`, and the `indicators={tenkan, kijun, senkou_a, senkou_b, above_cloud, atr_14}` dict are envelope decoration read by zero order-gating comparisons; `atr(df, 14)` (lazy `forven.scanner` facade, verified resolvable this cycle) never gates; `compatible_regimes` (`TREND_UP`/`TREND_DOWN`) is class metadata read by zero signal lines; the `PREBUILT-ICHIMOKU` roster row is an asset label, not a rule.
5. Variant menus fenced: `parameter_space()` (`tenkan_period` 7–12 step 1, `kijun_period` 20–30 step 2, `senkou_b_period` 44–60 step 4) is a tuning grid read by zero signal lines — this record freezes canonical `9/26/52` as written; adopting any grid point would change trade events and is never claimed here.
6. Pool Pine Ichimoku siblings fenced: `ichimoku-macd-triple-confirm-reversal-ethusdt-1h-2026-10-08` (Coinrule Pine source, two-sided, `1h`) AND-gates the line cross with a MACD cross and a Chikou momentum leg and exits by opposite-signal reversal — a veto-failed cross fires there never, while any cloud-passing cross fires here; directionality, frame, and immutable source all differ. `ichimoku-rsi-gated-reversal-btcusdt-1d-2026-10-08` (Coinrule RSI Pine source) adds an RSI confirmation leg with different trade events on every RSI-vetoed bar. Neither record is the other's provenance.
7. Pool batch Ichimoku item fenced: reconstruction-batch `#20 Ichimoku-RSI` (unmerged PR #58 family) is a different source lineage with an RSI leg — not this file, not this mechanism.
8. Pool MA-cross cousins fenced: `forven-dema/tema/hma-cross` and `forven-ema-cross-adx-regime` records trade price-line crossings of moving averages, never high/low-midpoint lines gated by a displaced cloud — none evaluates a Tenkan/Kijun edge with a Senkou cloud-position gate; the pool's `forven-obv-ema-cross` cousin crosses a volume-derived line through its own average (different primitive and data). None is this construction.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+86400s` mapping; fills are never claimed intrabar; the 3600s terminated view is never relied on for position state.
10. Derivation boundary fenced: the only non-source-native behaviours are the BTCUSDT-spot-`1d` market/frame pin, the effective-time MARKET-close fills, the single-unit/controller-memory/warmup pin, the pinned cost model with leverage `1.0` adopted as unleveraged, and the `+86400s`/gap data rule — all predeclared above. The 9/26/52 construction, the Tenkan-Kijun edge-cross entry with its cloud gate and all strictness, the cloud-blind cross-down exit, the guard, the long-only stance, and the no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Ichimoku 9/26/52 construction / Tenkan-Kijun edge-cross entry with cloud gate and pinned strictness / cloud-blind cross-down exit / long-only / no-stop posture / single-unit `0.001` BTC / `1d` BTCUSDT spot / effective-time close fills are frozen.

- F1 — Cloud-gate relevance: dropping the above-cloud gate entirely (naked Tenkan/Kijun cross entry, same exit, same posture) must not improve net expectancy; fail ⇒ the cloud gate carries no weight beyond decoration.
- F2 — Slow-cloud relevance: replacing the 52-bar Senkou-B window with a 40-bar window (same 9/26 lines, same edges, same posture) must not improve net expectancy; fail ⇒ the slow 52-bar cloud memory adds nothing over a faster cloud and the record is a label variant of one.
- F3 — Exit-leg relevance: dropping the cross-down exit entirely (entries only, never exiting — buy-and-hold from the first gated cross) must not improve net expectancy; fail ⇒ the exit leg carries no weight beyond decoration.

## Crypto portability

BTCUSDT spot `1d` is the research pin (roster names `"BTC"` only). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Late entries by construction: the 52-bar Senkou window plus its 26-bar lag trails price after any V-turn, so recoveries are entered strictly after both the line cross and the cloud reclaim print — disclosed lag profile.
- Chop whipsaw: alternating shallow Tenkan/Kijun crosses print repeated enter-then-exit round trips with no cooldown and no structural filter beyond the cloud gate — disclosed chop profile.
- Crash-through blindness: a bar that gaps the lines from bull to deeply bear exits one bar later — there is no stop order to front-run it, disclosed.
- Cloud-blind exit asymmetry: the exit fires on the line cross alone even when price still holds above the cloud, while the entry demands the cloud reclaim — a rally that crosses up under the cloud is watched from flat until both conditions align, disclosed.
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

- https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/ichimoku.py
- https://github.com/judder659/Forven
