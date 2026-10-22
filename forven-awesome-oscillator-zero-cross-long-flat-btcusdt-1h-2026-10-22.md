---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Awesome Oscillator 5/34 zero-cross long-flat on BTCUSDT 1h spot bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/awesome_oscillator.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Awesome Oscillator 5/34 zero-cross long-flat on BTCUSDT 1h spot bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted Forven records on `main`, including the `forven-tema-cross`, `forven-dema-cross`, and `forven-hma-cross` siblings — this record pins a different builtin file).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; record `source_as_of` is that commit date, never a fetch date). This pin is **not** the repository HEAD: `git ls-remote` this cycle reports HEAD as `b7ea8825ff88500bcc13a479ff2fbef054391f92`. The record pins the immutable commit only and claims nothing about the branch tip.
- Exact file path: `forven/strategies/builtin/awesome_oscillator.py`.
- GitHub blob SHA at the pinned commit: `9edfcf95151ee42bfbde9773a8a95518e9130b9c`, size 2989 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2989 bytes, 110 lines, SHA-256 `a38c1139643c913029816dc76df4a8199711c9842ba07d20c291faaeb2b8fddf`, identical to the GitHub blob (`git hash-object` reproduces `9edfcf95…9130b9c`; the Contents API independently reports the same blob SHA and size 2989) — the entire file was retrieved and inspected.
- Registration: the file carries `TYPE_NAME = "awesome_oscillator"` (line 13), `STRATEGY_CLASS = AwesomeOscillatorStrategy` (line 106), and the roster pin `STRATEGIES = [("PREBUILT-AO", AwesomeOscillatorStrategy, {"_asset": "BTC"})]` (lines 108–110). Repo-wide, no other builtin file carries this `TYPE_NAME`.
- The file's own words (quoted for gate evidence, never extended): module docstring `AO = SMA(median_price, 5) - SMA(median_price, 34)` / `Entry: AO crosses above 0` / `Exit: AO crosses below 0` (lines 1–7); `default_params` returns exactly `{ "fast_period": 5, "slow_period": 34, "leverage": 1.0 }` (lines 38–43); guard `if len(df) < slow + 2:` returning both-signals-false (lines 61–69); construction `median_price = (df["high"] + df["low"]) / 2.0`, `sma_fast = median_price.rolling(window=p["fast_period"]).mean()`, `sma_slow = median_price.rolling(window=slow).mean()`, `ao = sma_fast - sma_slow` (lines 71–74); predicates `entry = prev_ao <= 0 and curr_ao > 0` / `exit_ = prev_ao >= 0 and curr_ao < 0` (lines 80–81); return `Signal(entry_signal=bool(entry), exit_signal=bool(exit_), price=round(curr_close, 4), direction="long", ...)` (lines 87–97). No performance phrase of any kind ships anywhere in the 110 lines — this record adopts no source-reported performance (see Evidence).
- Envelope semantics (sibling-pinned at the same commit, re-verified identical this cycle): `forven/strategies/base.py` (12238 bytes, 361 lines, blob `27508a2a6b8c546e21adefdb97fc0144fabf881` — `git hash-object` reproduces it) defines the `Signal` dataclass (lines 66–80): `entry_signal`/`exit_signal` coerced to plain booleans, `direction` resolved by `_normalize_signal_direction` (lines 160–180) which maps `"long"` to `"long"` on entry and non-entry bars alike. The file's two `direction="long"` literals therefore reach every reader unchanged; no side relabeling exists.
- Full-file token census (case-insensitive search over the 110 lines this cycle): 0 `short` / 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` / 0 `funding` / 0 `mark_price` (no economics beyond the `leverage: 1.0` default, replaced by the fixed research cost model — see Execution assumptions); 0 `volume` / 0 `open`-series reads (order-gating reads are `high`/`low`/`close` only); 0 `request` / 0 `security` / 0 `resample` / 0 `informative` / 0 `timeframe` (no external feed, no multi-frame logic); 0 `hyperopt` / 0 `pyramid` / 0 `cooldown` / 0 `position` / 0 `shift` / 0 `crossed` (no cross helper — the predicates are explicit prior/current comparisons); 0 `rsi` / 0 `macd` / 0 `stoch` / 0 `vwap` / 0 `supertrend` / 0 `ichimoku` (no second indicator conditions any order); `direction=` occurs exactly twice (both `"long"` — guard line 66 and live line 91); `leverage` occurs exactly once (the `1.0` default); the single `Parameter` token is the plain method name `parameter_space` (lines 99–103, optimizer metadata returning `{"fast_period": (3, 7, 1), "slow_period": (28, 40, 2)}` — never imported, never read by `generate_signal`; this record pins the defaults and runs no search).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the AO(5/34) median-price construction, the zero-cross-up entry, the zero-cross-down exit, the long-only stance, the no-stop/no-target posture, and its own `slow + 2` short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` **spot** `1h` (the file names no market and no timeframe; the roster pins `_asset BTC`; spot is chosen so the pinned simulator's funding-free semantics are structurally exact — disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills plus the exact controller/executor mapping below (derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics with the source's own 36-bar guard adopted verbatim as the warmup floor (no cooldown — explicitly none, not invented); (4) a fixed in-record research cost model replacing the bare `leverage: 1.0` default — `trade_cost = 0.001` per side, zero added slippage, continuous-fractional accounting, runtime min-notional preflight (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `awesome_oscillator` / `PREBUILT-AO` / `AwesomeOscillatorStrategy` returns zero strategy records citing this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an AO rule. AO cousins in the pool are fenced as different constructions in Negative evidence 6. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: momentum trend-following on the Awesome Oscillator (`SMA(median,5) − SMA(median,34)`); buys when AO crosses above the zero line, exits when AO crosses below it. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Lagged zero-line momentum switch, long-only, state-holding. The AO leg subtracts a slow 34-bar median average from a fast 5-bar one, so the zero cross fires only after a sustained median-price displacement — earlier than a 34-bar level break but later than a fast-edge trigger. The entry buys the exact bar the displacement turns positive; the exit surrenders the unit on the exact bar it turns negative. There is no gate, no filter, and no holding leg beyond the sign itself: a market whose AO oscillates around zero prints repeated full round-trips with no flat state to rest in (whipsaw profile, disclosed), while a leg whose reverse cross never prints is held indefinitely. Unlike stop-based systems there is no fixed-distance risk leg — the reverse cross is the sole risk control by construction.

## Signal

Exact rule as pinned (any other period, average family, threshold, edge/state pairing, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 56–97) is the single decision method and no vectorized twin exists:

```text
med[t]    = (high[t] + low[t]) / 2                       // median price, causal
F[t]      = SMA(med, 5)[t]                               // rolling 5-bar mean, causal
S[t]      = SMA(med, 34)[t]                    // rolling 34-bar mean, causal
ao[t]     = F[t] - S[t]
guard     = len(df) < 36 → both signals false (source floor: slow + 2)
entry     = (ao[t-1] <= 0) and (ao[t] > 0)               // strict cross-up edge
exit_sig  = (ao[t-1] >= 0) and (ao[t] < 0)               // strict cross-down edge
```

- Trade events: `entry_signal=True` with `direction="long"` on cross-up bars; `exit_signal=True` on cross-down bars. Each print is a one-bar edge on the decision bar's own AO print.
- Exact boundaries (pinned semantics): the current-bar inequalities are strict (`> 0` / `< 0`) — a bar printing exactly `ao == 0.0` fires neither leg; the prior-bar branches admit equality (`<=` / `>=`), so a flat-tied prior bar still admits a genuine current-bar break. Seeding prints (`NaN` while either rolling window is unseeded) compare false on every strict leg, so unseeded bars deterministically fire neither leg (pandas rolling semantics, disclosed, never repaired).
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `ao[t] > 0` while any signal-exit bar has `ao[t] < 0` — mutually exclusive on every bar, degenerate, zero, or NaN, so entry and signal-exit never co-print. The record carries no TP/SL/trailing/time legs that could co-fire. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere and both `direction=` literals read `"long"` (envelope-verified above). A two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue with no naked shorting.
- Exits and risk (explicit): the reverse cross is the sole position-ending path. Stop loss, take profit, trailing stop, and time limit are absent in source and recorded as explicitly disabled in the derived triple-barrier mapping (all unset — never defaults to be assumed). `confidence` (lines 83–85) and the `indicators={ao, prev_ao}` echo (lines 93–96) are diagnostic per-bar constants — neither conditions any predicate (verified: zero order-gating reads of either).
- Position rule (predeclared researcher pin): single-unit, at most one open position; a positioned book treats further cross-up bars as hold-no-ops (no pyramiding, no averaging — no position-aware token ships anywhere); a flat book treats cross-down bars as no-ops; re-entry re-arms on any qualifying cross-up after any exit (no cooldown specified — explicitly none, not invented). Pre-guard bars are flat by the source's own rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` with fixed non-negative offsets (two trailing rolling means plus a one-bar cross lookback); no `open`-series read, no `volume` read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt machinery, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set and `parameter_space` ranges are metadata never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT spot: `high`/`low` (median-price construction) plus `close` (the `price` echo and the fill basis). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). `1h` is an already-admitted interval on `main` (83 records) and a standard Binance kline interval served by the pinned spot-candles feed (see Execution assumptions). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (source-verbatim, disclosed): 36 bars (`len(df) < slow + 2`, lines 61–69). Covers the 34-bar slow-mean seed with margin; bars inside the guard return both-signals-false. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

Pinned engine (all files read byte-verified at this pin during this cycle): `hummingbot/hummingbot` commit `fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467` (committer date `2026-09-20`, subject `Update version number in setup.py` — the 20260920-package pin named by the README admission baseline; `VERSION dev-2.17.0`):

- E1 — spot data path: `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (109 lines, 3924 bytes, blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`, hash reproduced this cycle), lines 80–85: each REST kline row maps `row[0]` (the candle's open time) to the row `timestamp` in seconds with that bar's open/high/low/close/volume attached. A row therefore labels a completed bar whose full OHLCV is known — the decision row's close is available at that row.
- E2 — causal availability: `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (727 lines, 39071 bytes, blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`, hash reproduced this cycle), lines 455–470: strategy features are merged onto the candle frame with `pd.merge_asof(..., left_on="timestamp_bt", right_on="timestamp", direction="backward")` — only feature rows with timestamps at or before the candle timestamp are visible — then `timestamp = timestamp_bt` (line 470). No forward feature can leak into a decision.
- E3 — decision-then-fill order: same file, lines 282–291: for each row `i`, `update_state(row)` publishes that row's `close_bt` as the controller price and stamps controller time to the row timestamp (lines 364–368) *before* `controller.determine_executor_actions()` runs; a `CreateExecutorAction` is simulated on `processed_features.loc[i:max_ts]` (line 287) — the slice starts exactly at the decision row.
- E4 — market fill at decision-row close: `hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py` (88 lines, 5023 bytes, blob `5539f0d2957c56973467cb940fb87c8c1396c943`, hash reproduced this cycle), lines 11–16 (non-limit order takes the slice-first row as `start_timestamp`) and line 40 (`entry_price = df.loc[start_timestamp, 'close']`). Combined with E3, a market position created on decision row `i` fills at row `i`'s close — the derived same-bar-close fill is pinned simulator behavior, not an assumption. Returns and TP scan closes (lines 44, 58); SL scans bar lows/highs (lines 62–64) — this record sets no SL/TP/trailing/time legs, so none of those scans exist in this derived version.
- E5 — signal-exit close: same engine base, lines 568–599 (`handle_stop_action` with `keep_position=False` terminates with `close_type=EARLY_STOP` at the action row's timestamp and books that timestamp's `net_pnl_quote`) together with `hummingbot/strategy_v2/backtesting/executor_simulator_base.py` (100 lines, 4453 bytes, blob `f77fc6104aef554b8ce7484481015311da1222a5`, hash reproduced this cycle), lines 29–56 (`get_executor_info_at_timestamp` reads the last simulation row at or before the timestamp — the exit row's close-based PnL). A reverse-cross exit therefore closes at the exit-signal bar's close-based economics.
- E6 — fixed costs, no funding: the position simulator carries the complete cost model in lines 44–49 (`cumulative_returns = (... * side_multiplier) - 2 * trade_cost`; `cum_fees_quote = 2 * trade_cost * filled_amount_quote`) with continuous-float amounts (lines 47–48). A case-insensitive search of both simulator files returns zero `funding` tokens — the pinned path models no funding leg at all, and the derived version trades spot, where no funding payments structurally exist. Nothing is silently zeroed: funding is absent by venue and by engine alike, disclosed on both sides.
- Derived controller mapping (researcher-specified, disclosed — the controller callback itself is strategy code, while fills/exits/costs ride E1–E6): connector Binance spot, trading pair BTCUSDT, `1h` candles; on each completed row, evaluate the Signal rule; flat book + entry edge → one `CreateExecutorAction` with a market `PositionExecutorConfig` (`side=BUY`, `entry_price=row close`, `timestamp=row timestamp`, triple-barrier TP/SL/trailing/time-limit all unset, single-unit amount); open book + exit edge → one `StopExecutorAction(keep_position=False)` at the exit row's timestamp. The Signal mutual-exclusion proof leaves no row that both creates and stops. An open position at the final data row closes as simulator-native `TIME_LIMIT` at the last close (simulator lines 26, 66, 76, 79) — terminal accounting, disclosed, never a strategy exit.
- Sizing/capital/costs (fixed in-record, never deferred): `trade_cost = 0.001` per side (researcher pin matching Binance spot standard 0.10% taker economics; the simulator deducts the 2× round trip per E6); zero added slippage (the simulator fills exactly at close — a simulator-native simplification, fenced, not live economics); continuous-fractional accounting (simulator-native floats per E6 — venue quantization is out of model scope, disclosed); min-notional runtime preflight per baseline §4 with a declared floor (the single-unit tranche must exceed 10 USDT-equiv at the runtime capital — sub-floor capital is out of model scope and the preflight rejects it, so no order is ever silently dropped). The source's bare `leverage: 1.0` default is superseded by spot leverage-1 execution under this pin. No safety-order/add tranche activates under the single-unit/no-add pin, so position events are fully determined by the signal legs and sizing changes no event — disclosed as derived behavior, never source-native.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (110 lines: module docstring with the AO formula and cross rules, `TYPE_NAME`, `default_params` with the 5/34 set, the 36-bar guard, the median/SMA construction, the strict cross-up entry, the strict cross-down exit, the fixed long-only stance, the `round(curr_close, 4)` price echo, and the `PREBUILT-AO` roster pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard adopted verbatim, not repaired: the file's own `len(df) < slow + 2 = 36` check returns both-signals-false on shorter frames — pre-guard bars are flat by the source's own rule, and the 34-bar slow mean seeds inside the guard. Seeding `NaN` comparisons are false on every strict leg, so no evaluated bar can fire early — disclosed, not repaired.
2. Exact-zero rule fenced: both legs are strict on the current bar — a bar printing exactly `ao == 0.0` fires neither leg. Prior-bar equality (`<=` / `>=`) still admits a genuine current-bar break. Strictness preserved throughout — disclosed, not smoothed.
3. Confidence/indicators fenced: `confidence` (lines 83–85) and the `indicators` echo (lines 93–96) are written but never read by any predicate — deleting both reaches identical entry/exit events on every bar.
4. Optimizer metadata fenced: `parameter_space()` (lines 99–103) and `compatible_regimes` (lines 45–47) are never called by the decision path (which takes only `df`/`params`); treating either as a gate or running the search would be a different, unpinned rule. This record pins the defaults.
5. Envelope fenced: the `Signal` import (line 11) is plumbing — the base-class dataclass (re-verified blob-identical this cycle) coerces the already-boolean flags and preserves both `"long"` literals; it adds no gate, no timing, and no side.
6. Cousin records fenced as different constructions (none trades a bare AO(5/34) zero-cross pair, long-flat, on `1h` spot from this file): the admitted `awesome-oscillator-zero-cross-reversal-two-sided` pool-mate trades an AO zero-cross from an EternaHybridExchange TradingView Pine source, two-sided always-in, on `4h` (different source family, different direction handling, different frame); the admitted `freqtrade-awesome-macd-ao-cross-macd-gated` pool-mate trades an AO-cross leg behind a MACD gate from a Freqtrade file (gated vs bare, different legs, different source). Not a re-tuning of either: adding any gate, flipping direction handling, changing either period, or moving the threshold would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot-`1h` market choice, the E1–E6 controller/executor/cost mapping, the single-unit/no-add/no-cooldown position pin, and the fixed `trade_cost = 0.001` research cost model — all predeclared above. The AO(5/34) construction, the strict cross boundaries, the reverse-cross exit, the long-only stance, the no-stop/no-target/no-trailing/no-time-exit stance, and the 36-bar guard floor are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: AO(5/34) median-price construction / strict zero-cross pair / reverse-cross exit / single-unit long-only / `1h` BTCUSDT spot / same-bar-close fills / 36-bar guard floor / `trade_cost = 0.001` are frozen.

- F1 — Oscillator relevance: replacing both AO legs with same-period SMA(5/34) close-price legs (same guard shape at 36 bars, same pins) must not improve net expectancy; fail ⇒ the median-price construction adds nothing over plain close averages.
- F2 — Exit relevance: replacing the reverse-cross exit with a fixed 8-bar time exit (same cross entries, same guard/pins) must not improve net expectancy; fail ⇒ the reverse-cross exit adds nothing over a clock exit.
- F3 — Family relevance: replacing the AO(5/34) pair with the admitted dual-TEMA 12/26 cross pair (same bookkeeping, its own 80-bar floor, same pins) must not improve net expectancy; fail ⇒ the oscillator pair adds nothing over the triple-smoothed average pair.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses identically on a USDT-M perpetual long leg with no shorting; the spot pin additionally removes the funding leg structurally. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar high/low/close are native Binance kline fields on both spot and perpetual venues.

## Limitations

- The reverse cross is the sole risk control: a position whose reverse cross never prints is held to the end of data (simulator-native `TIME_LIMIT` terminal close, disclosed in Execution assumptions); a market whose AO oscillates around zero whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown to damp them — disclosed as the principal friction). There is no stop, target, trailing, decay, chop, or time exit — disclosed, not repaired.
- Simulator-native simplifications (fenced, not live economics): fills exactly at close, zero added slippage, continuous-fractional amounts, no venue quantization, no funding leg. Live-spot deployment would need venue precision/min-notional binding beyond the runtime preflight declared here.
- The `1h` frame rides existing admission precedent (83 records on `main`) and the pinned spot-candles feed serves standard Binance intervals — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- Vendored envelope internals (`Signal` normalization) live in `forven/strategies/base.py` outside the pinned strategy file — re-verified blob-identical at the same commit, never re-derived.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/awesome_oscillator.py
- https://github.com/judder659/Forven
- Pinned-engine evidence (read byte-verified this cycle, `hummingbot/hummingbot@fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467`): `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`), `hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py` (blob `5539f0d2957c56973467cb940fb87c8c1396c943`), `hummingbot/strategy_v2/backtesting/executor_simulator_base.py` (blob `f77fc6104aef554b8ce7484481015311da1222a5`)
