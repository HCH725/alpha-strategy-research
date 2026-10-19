---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven BB-squeeze-gated band breakout long-flat on BTCUSDT 1h bars
created: 2026-10-19
updated: 2026-10-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/bb_squeeze.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven BB-squeeze-gated band breakout long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-chandelier-exit-long-stop-cross`, `forven-engulfing-body-cover-volume`, `forven-stddev-cross-swing`, `forven-hma-cross`, `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, and twenty-eight other admitted Forven records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/bb_squeeze.py`.
- GitHub blob SHA at the pinned commit: `d7805ee7e37f4f6bf9d7c4838ac0d725bc72dd9c`, size 2161 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 2161 bytes, 54 lines, SHA-256 `319400ee16571e62620b850101fda51a729c04658971ab2cc6a052adc18f2cff`, and `git hash-object` reproduces the GitHub blob (`d7805ee7…72dd9c`) — the entire file was retrieved twice and inspected (both fetches byte-identical).
- Registration: the file self-registers via `STRATEGY_CLASS = BBSqueezeStrategy`, `TYPE_NAME = "bb_squeeze"`, and the `STRATEGIES = [("TOMB-BBSQUEEZE", BBSqueezeStrategy, {"_asset": "BTC"})]` roster pin. Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `builtin/bb_squeeze` / `TOMB-BBSQUEEZE` / `BBSqueezeStrategy` / `TYPE_NAME = "bb_squeeze"` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `Bollinger Band Squeeze Breakout strategy.`; `describe()` returns `Detects a volatility squeeze (BB inside KC) and trades the breakout.`; `default_params` returns exactly `{ "bb_period": 20, "bb_std": 2.0, "kc_period": 20, "kc_mult": 1.5, "leverage": 3.0 }`; `compatible_regimes` returns `{"RANGE_BOUND", "VOLATILE"}` (metadata never read by the signal path); `parameter_space()` returns `{ "bb_period": (15, 25, 5), "kc_mult": (1.0, 2.0, 0.5) }` (a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 54 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 54 lines, so no twin-selection ambiguity exists. The method pins its constants (`bb_period` 20, `bb_std` 2.0, `kc_period` 20, `kc_mult` 1.5), builds the Bollinger triple in-file (rolling mean plus sample standard deviation), resolves the ATR through the repository facade (see estimator pin below), builds the Keltner pair off the same midline in-file, reads the last two closes against the last two upper-band prints, evaluates the prior-bar squeeze gate and the upper-band breakout on the decision bar, and returns a single `Signal`.
- ATR estimator pinned at the same commit (actually read): `generate_signal` imports `atr` from `forven.strategies.indicators`, which re-exports it lazily (PEP 562 `__getattr__` over the `_FACADE_NAMES` allowlist, verified in `indicators.py` at the pinned commit) from its canonical home `forven.scanner.atr` (lines 1946–1957 of `scanner.py`, 464565 bytes, blob `9a1d77b90bf214c03aa230a5f46775aab94748bd`): True-Range `max(high - low, |high - close.shift()|, |low - close.shift()|)` with a plain rolling mean (`tr.rolling(period).mean()`) — SMA smoothing, never Wilder RMA, never EWM. The KC pair is therefore `SMA20(mid) ± 1.5 × SMA-ATR(20)`, fully pinned.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-chandelier-exit-long-stop-cross`, `forven-engulfing-body-cover-volume`, and `forven-bb-edge-fade-reclaim` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default — the live `direction = "long"` literal survives untouched on every evaluated bar.
- Full-file token census (verified by search over the 54 lines this cycle): `direction` occurs exactly once (the constructor literal `"long"` — no short leg exists anywhere); 0 `sell` / 0 `stop=` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` as order arguments; 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `rsi` / 0 `ema` / 0 `adx` / 0 `vwap` / 0 `stoch` / 0 `macd` / 0 `supertrend` / 0 `ichimoku` (no second indicator, no regime filter, no momentum oscillator); 0 `open` / 0 `volume` reads (the rule consumes `close`/`high`/`low` only — `close` directly, `high`/`low` inside the facade ATR); 0 `isna` / 0 `isnull` / 0 `nan` guards (NaN behaviour disclosed in Negative evidence 3, never invented); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); `len(df)` occurs zero times — the file ships no short-frame guard of its own, so the warmup floor below is a predeclared researcher pin (disclosed, never presented as source verbatim).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar SMA midline, the 2.0-sigma sample-stdev Bollinger triple, the 20-bar SMA-ATR Keltner pair at 1.5×, the prior-bar BB-inside-KC squeeze gate, the close-vs-upper-band breakout entry, the midline-recross exit, the long-only stance, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 30-bar researcher warmup floor (an already-positioned book treats further breakout bars as hold-no-ops, a flat book treats midline-untouched bars as no-ops, re-entry re-arms on any qualifying squeeze-plus-breakout bar after any exit with no cooldown, pre-warmup bars flat by record rule — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 3.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/bb_squeeze` / `TOMB-BBSQUEEZE` / `BBSqueezeStrategy` / `bb_squeeze` returns zero strategy records — no record cites this source file. The word `squeeze` occurs in the pool only inside unrelated mechanisms and explicit fence prose (see Negative evidence 6–8), never as this gate-plus-breakout construction. No open `research/*` PR carries this source file (open PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources; #304 is the Forven `cci.py` sibling, a different file and a different oscillator-recross machine). Not a duplicate, paraphrase, or trivial parameter variant: a squeeze-gated band-breakout machine (contraction gate AND price-breakout trigger, midline exit) is a different signal construction from a raw band breakout, a momentum-oscillator squeeze system, or a dual-squeeze trend-plus-momentum system — different gate × different trigger × different exit × different direction handling × different immutable source file.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Bollinger Band Squeeze Breakout strategy` that `Detects a volatility squeeze (BB inside KC) and trades the breakout.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 54 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Volatility-contraction-gated band breakout, long-only, state-holding. The system waits for compression first (the whole Bollinger envelope nesting strictly inside the Keltner envelope on the prior bar — the market has gone quieter than its own 1.5-ATR noise shell), then buys only the exact bar the close crosses back above the upper band — unlike raw-breakout systems, a band break that fires without a preceding squeeze prints nothing, and unlike momentum-squeeze systems, no oscillator rotation can trigger anything: only contraction-then-price-breakout flips state. The exit is the midline recross, so the trade holds the expansion leg until price sinks back through its own 20-bar average. The failure mode is plain: a squeeze that resolves downward never enters (long-only with no short leg), a false poke above the band that collapses back under the midline whipsaws the book with no stop and no cooldown, and a grinding advance is held with no profit-taking leg until the midline itself is lost.

## Signal

Exact rule as pinned (any other band period, sigma multiple, ATR period, ATR multiple, estimator, gate polarity, trigger polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` is the single source of truth — no second decision logic exists:

```text
inputs (defaults, frozen): bb_period = 20, bb_std = 2.0, kc_period = 20, kc_mult = 1.5
bb_mid_t   = SMA(close, 20) on bars ending at bar t            // rolling mean
bb_sd_t    = sample stdev(close, 20, ddof=1) on bars ending at t // rolling std
bb_upper_t = bb_mid_t + 2.0 * bb_sd_t
bb_lower_t = bb_mid_t - 2.0 * bb_sd_t
TR_t       = max(high_t - low_t, |high_t - close_{t-1}|, |low_t - close_{t-1}|)
atr20_t    = mean(TR over the last 20 bars ending at bar t, plain rolling mean) // scanner.atr
kc_upper_t = bb_mid_t + 1.5 * atr20_t
kc_lower_t = bb_mid_t - 1.5 * atr20_t
sqz_on     = (bb_upper_{t-1} < kc_upper_{t-1}) AND (bb_lower_{t-1} > kc_lower_{t-1})
breakup    = (close_{t-1} <= bb_upper_{t-1}) AND (close_t > bb_upper_t)
entry      = sqz_on AND breakup
exit_      = (close_t < bb_mid_t)
```

- Warmup (predeclared researcher pin — the source ships no guard): 30 completed `1h` bars flat by record rule. Structural minimum is the 21st completed bar (20-bar SMA/stdev/ATR seeds plus the prior-bar squeeze reference — plus margin). Pre-warmup bars are flat by record rule; the raw source would `IndexError` on `iloc[-2]` below 2 bars and print NaN-gated no-signals through bar 20 — that unreachable region is fenced here by the record rule, never presented as source behaviour. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.
- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is an edge cross (fires once on the crossing bar — refires require a fresh squeeze-plus-cross); the exit is a level hold (fires on any bar closing under the midline, including bars that never entered).
- Mutual-exclusion proof (no tie-break pin required): entry requires `close_t > bb_upper_t` where `bb_upper_t = bb_mid_t + 2.0 * bb_sd_t >= bb_mid_t` (sample stdev is non-negative; equality only in the degenerate all-equal window), while exit requires `close_t < bb_mid_t` — the strict close-vs-band inequalities are pairwise opposite, unsatisfiable on every bar including the degenerate window. A touch (`close_t == bb_upper_t` or `== bb_mid_t`) fails the strict leg and fires nothing on that leg. The reviewer is never asked to invent an ordering.
- Exits and risk (explicit): the midline recross is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (hardcoded `1.0`) and the `indicators={"squeeze_on": ...}` dict are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying squeeze-plus-breakout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` with fixed non-negative offsets (last two closes against the last two upper-band prints, the prior-bar squeeze pair, plus trailing 20-bar windows ending at the decision bar), exact comparisons, and zero divisions (no ratio anywhere — the order legs divide nothing). No `request.*`, `security()`, `timeframe*`, `barstate.*`, `open`/`volume` read, EMA/RMA/WMA/RSI/MFI/ADX/Stochastic/MACD/Supertrend smoothing, session/calendar call, or stop/limit order argument exists anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes == {"RANGE_BOUND", "VOLATILE"}` set is metadata never read by the signal path, so no regime model gates any order. Substituting Wilder-RMA smoothing, a momentum oscillator, an EMA trend filter, or any second gate would be a different, unpinned rule.

## Required data

- `close`/`high`/`low` on `BTCUSDT` `1h` completed bars only (sole reads: `close` directly for the bands and both cross comparisons; `high`/`low` inside the facade `scanner.atr` True-Range arithmetic). No `open`, no `volume`, no external feed, no funding/OI/mark-price leg, no calendar, no multi-asset input.
- Warmup: 30 completed `1h` bars flat by record rule (structural minimum the 21st completed bar — 20-bar SMA/stdev/ATR seeds plus the prior-bar squeeze reference — plus margin).
- Point-in-time: every window is trailing over completed bars ending at the decision bar (the band/ATR windows are unshifted but the decision bar is completed before evaluation — no future bar, no unfinished-bar read, no repainting); the decision bar's own `close` is both the last input and (via the derived same-bar-close pin, `price=round(curr_close, 4)`) the fill price basis.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1h`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit position with hold-no-op semantics plus the 30-bar researcher warmup floor, house sizing/capital/costs replacing the bare `leverage: 3.0` default.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1h` with declared house fees/funding/slippage overlay; squeeze-gated band-breakout arithmetic over completed `close`/`high`/`low` on a single frame with same-bar-close fills is within the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record.
- Sizing/capital (stated plainly): the admitted version trades exactly one fixed unit — a flat book enters one unit on an entry bar, a long book exits the whole unit on an exit bar, same-direction refires are hold-no-ops, no pyramiding, no averaging, no safety orders, no cooldown. The downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus modeled funding/slippage with explicit limitations; modeled funding is never reported as realized funding) apply to the derived evaluation here and change no trade event under the predeclared single-unit rule — DCA is a downstream execution experiment, never an admission leg of this version. No capital-dependent forced-close state beyond the standard isolated-margin accounting is admitted.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `bb_period 20` / `bb_std 2.0` / `kc_period 20` / `kc_mult 1.5` inputs with an SMA midline, sample-stdev bands, facade-resolved SMA-ATR Keltner pair, prior-bar squeeze gate, upper-band breakout entry and midline-recross exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `TOMB-BBSQUEEZE` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: full-file search returns exactly one `def generate_signal` and zero `def generate_signals` — there is no second decision path to select between.
2. No estimator ambiguity: the single `atr` facade import resolves through the pinned `indicators.py` allowlist hook to exactly one implementation, `scanner.atr` (True-Range plus plain rolling mean — read at the pinned commit, lines 1946–1957). The EWM and Wilder ATR helpers (`_atr_ewm`, `_atr_wilder`) live in `indicators.py` but are reachable only through other registry keys — nothing in this file's import path touches them, so no variant selection exists to pin or fence beyond the recorded resolution.
3. NaN determinism, stated plainly: the file ships no `isna` guard (verified zero matches), so a `NaN` band/ATR print can only meet the strict gate/trigger inequalities as `False` on both legs — NaN bars emit no signal by construction, never a spurious order. On complete data the 30-bar record floor already covers all 20-bar seeds plus the prior-bar reference, so no NaN reaches any order line in the admitted configuration; missing bars stay flat and are never fabricated. Below 2 bars the raw source would raise on `iloc[-2]` — fenced unreachable by the record warmup rule, disclosed here, never a load-bearing claim.
4. Equality boundaries fire nothing: the breakout uses strict `>` on the current-bar comparison and the exit uses strict `<` on the midline; a close that merely touches the upper band or the midline holds the prior state by construction. The `<=` prior-bar conjunct admits touch equality only as a setup, never as a standalone trigger; the squeeze pair is strict on both sides.
5. Same-bar double-fire is impossible (mutual-exclusion proof in Signal) — no ordering assumption, invented or otherwise, is required. The exit is a level hold, so a long book that entered on an earlier bar exits on the first bar closing under the midline; an entry bar can never simultaneously satisfy the exit leg.
6. Pool Bollinger cousins fenced, stated plainly: `bollinger-band-breakout-long-midline-exit` breaks the raw upper band with no contraction gate (any breakout bar fires there; here only post-squeeze breakouts fire — a breakout without a preceding squeeze trades there and fires nothing here, so the trade-event sets differ by construction); `sideways-dmi-bollinger-breakout`, `chartart-bollinger-rsi-double-joint-cross`, and `forven-bollinger-s00120-rsi-breakout` each add DMI/RSI joint-cross gates this record never evaluates. None requires the prior-bar BB-inside-KC nesting this record gates on.
7. Pool squeeze cousins fenced, stated plainly: `sqzmom-lb-squeeze-release-ema100` (LazyBear, TradingView) enters on squeeze-colour transitions AND-gated with a linreg-momentum oscillator rising/falling against trailing 100-bar extremes plus EMA100 plus close-tick gates, two-sided with momentum-tick exits — different trigger (price-breakout vs oscillator), different exit (midline vs momentum downtick/uptick), different direction handling (long-flat vs two-sided), different band parameters (2.0σ/SMA-ATR vs 1.5σ/SMA-TR), different immutable source. `forven-volatility-contraction-breakout` (sibling file `builtin/volatility_contraction_breakout.py`) requires a dual squeeze (ATR below its 200-bar 20th percentile AND BB-width below half its 200-bar median) AND-gated with an EMA200 trend filter and an RSI50 gate, two-sided with EMA200-fallthrough exits and a 200-bar source guard — different gate (dual percentile/median vs single prior-bar nesting), different trigger (trend-plus-momentum level vs band breakout cross), different exit, different direction, different immutable source file. The FMZ Keltner-momentum record (481364) breaks a Keltner envelope AND-gated with a 14-bar momentum-sign filter, two-sided — no Bollinger triple, no squeeze nesting, no midline exit. This record is therefore never evidence for any of those rules, and none of them is this rule's provenance.
8. Unadmitted same-repo neighbour fenced, stated plainly: `builtin/ttm_squeeze.py` (TTM Squeeze — BB-inside-KC squeeze release AND-gated with a rising positive linreg-momentum oscillator, momentum-flip exit) is not in `main` and rides in no open `research/*` PR, so it collides with nothing; it is named here only to show the family line was walked — its trigger (oscillator release) and exit (momentum flip) differ from this record's trigger (close-vs-band breakout) and exit (midline recross), so consolidating the two into one record would erase a load-bearing event difference.
9. Variant menus fenced, stated plainly: the `parameter_space()` surface (`bb_period` 15–25, `kc_mult` 1.0–2.0) is a documented search grid the code never runs — this record freezes the `20/2.0/20/1.5` defaults as written; adopting any grid point, switching to Wilder/EWM ATR smoothing, switching the midline to EMA, or adding a momentum/trend gate would each be a different, unpinned rule.
10. Diagnostic quarantine, stated plainly: `squeeze_on`, `confidence == 1.0`, and the `compatible_regimes == {"RANGE_BOUND", "VOLATILE"}` set are computed into the indicators dict, the confidence field, or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, exit leg, or sizing input would be a different, unpinned rule.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20/2.0/20/1.5` squeeze-gated band breakout / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: replacing the prior-bar BB-inside-KC squeeze gate with an unconditional raw upper-band breakout (same midline exit) must not improve net expectancy on the frozen 42-cell campaign; fail ⇒ the contraction gate adds nothing over the bare breakout.
- F2 — Exit relevance: replacing the midline-recross exit with the next qualifying squeeze-plus-breakout reversal (hold through midline touches until an opposite-side setup) must not improve net expectancy; fail ⇒ the midline exit adds nothing over a gate-to-gate holding rule.
- F3 — Estimator relevance: replacing the facade SMA rolling-mean ATR with Wilder-RMA ATR (same midline, same multiple, same gate and triggers) must not improve net expectancy; fail ⇒ the pinned estimator carries no advantage over the classic smoother.

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1h` OHLCV on Binance — the rule consumes completed-bar `close`/`high`/`low` only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. The long-only no-stop posture expresses fully on spot; perps add no required leg. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding.

## Limitations

- Late entries by construction: the entry demands a full contraction print plus a band breakout, so expansions that never compress first are skipped entirely and post-squeeze breakouts enter strictly after the first expansion bar closes — disclosed lag-and-skip profile.
- False-breakout whipsaw: pokes above the upper band that collapse back under the midline print enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- Down-move blindness: squeeze resolutions to the downside never enter (long-only, no short leg) — disclosed opportunity gap, never a hidden short.
- No risk leg: no stop loss, take profit, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions after a breakout entry have no capital guardrail besides the eventual midline recross.
- No profit-taking disposition: a grinding advance is held with no target — the midline cross is the sole exit and there is no time stop; opportunity cost accrues, disclosed.
- Researcher warmup pin: the 30-bar floor is a record rule, not a source guard — the raw source is undefined (NaN-gated, and sub-2-bar raising) below its seed windows; the admitted configuration never evaluates there.
- Single-market scope: derived pin is `BTCUSDT` `1h` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/bb_squeeze.py (primary source — executable Python strategy, 54 lines, fetched live 2026-10-19 at pinned HEAD commit, 2,161 bytes, SHA-256 `319400ee16571e62620b850101fda51a729c04658971ab2cc6a052adc18f2cff`, blob `d7805ee7…72dd9c`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository context; pinned HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` verified this cycle)
- `forven/strategies/base.py` at the same commit (supporting semantics — `Signal` defaults and direction normalization, 12,238 bytes, blob `27508a2a…fabf881`, identical to the blob pinned by admitted sibling records)
- `forven/scanner.py` `atr` at the same commit (facade-resolved ATR estimator — True-Range plus plain rolling mean, lines 1946–1957, file blob `9a1d77b9…4748bd`)
