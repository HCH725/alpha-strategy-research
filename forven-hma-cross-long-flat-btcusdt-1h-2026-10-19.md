---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven HMA 9/21 cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/hma_cross.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven HMA 9/21 cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, `forven-bb-edge-fade-reclaim`, `forven-rsi-s00139-washout-cross`, `forven-obv-ema-cross-sma-gated`, `forven-mfi-threshold-cross`, `forven-williams-r-adx-gated`, `forven-rsi-boundary-rejection`, `forven-ema-cross-adx-regime`, and `forven-vwap-pullback-distance` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/hma_cross.py`.
- GitHub blob SHA at the pinned commit: `3915333435c5cf888958a402dd2c2acd7eeea811`, size 3606 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3606 bytes, 124 lines, SHA-256 `8c5b7a29cdb12b408d7a2c680ebbe045fa55234a5dc84e0c140401f3977ce61d`, and `git hash-object` reproduces the GitHub blob (`391533…ea811`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = HMACrossStrategy` (line 120), `TYPE_NAME = "hma_cross"` (line 10), and the `STRATEGIES = [("PREBUILT-HMA-CROSS", HMACrossStrategy, {"_asset": "BTC"})]` roster pin (lines 122–124). Repo-wide, no other builtin file carries this `TYPE_NAME`; working-tree search for `hma_cross` / `PREBUILT-HMA-CROSS` / `HMACrossStrategy` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `HMA Cross strategy.` (line 1); class docstring `Entry: Fast HMA crosses above Slow HMA.` / `Exit: Fast HMA crosses below Slow HMA.` (lines 30–34); `describe()` returns `Buys when {hma_fast}-bar HMA crosses above {hma_slow}-bar HMA. Exits on the reverse crossover.` (lines 60–65); `default_params` returns exactly `{ "hma_fast": 9, "hma_slow": 21, "leverage": 1.0 }` (lines 49–54); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 56–58, metadata never read by the signal path); `parameter_space()` returns `{ "hma_fast": (5, 15, 2), "hma_slow": (15, 30, 3) }` (lines 113–117, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 124 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` (lines 67–111) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 124 lines, so no twin-selection ambiguity exists. The Hull arithmetic is in-file (`_wma` lines 13–16, `_hma` lines 19–26 — no out-of-file average conditions any order); the method reads `close` (line 71), applies its own short-frame guard (lines 73–77), builds both Hull legs (lines 79–80), evaluates the cross pair (lines 90–94), and returns a single `Signal` (lines 100–111).
- ATR import pinned and fenced: `from forven.strategies.indicators import atr` (line 68) resolves through that module's PEP 562 lazy facade (`_FACADE_NAMES` includes `"atr"`, re-exported from `forven.scanner`); the call `atr(df, 14)` (line 81) feeds only the `confidence` diagnostic (lines 96–98, 105) and the `indicators` echo (line 109) — no entry/exit comparison reads its output, so its removal changes no trade event (see Negative evidence 2). The admitted `forven-dema-cross` sibling establishes this exact import-and-diagnostic pattern for the same repository family.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; `_normalize_signal_direction` maps the `"long"` literal back to `"long"` on entry and non-entry bars alike — the file's single live `direction="long"` literal (line 104; the guard's line-77 literal is the same token) therefore survives untouched on every bar.
- Full-file token census (verified by search over the 124 lines this cycle): `direction=` occurs exactly twice (both `"long"` — guard line 77 and live line 104; no short leg exists); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads plus 0 `volume` reads anywhere (order-gating reads are `close` only — the `atr` call's inputs feed the diagnostic alone); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `short` (case-insensitive — no short path exists); `len(df)` occurs exactly once (the line-75 guard — the file's own warmup floor, adopted verbatim, never invented).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the HMA9/HMA21 construction, the cross-up entry, the cross-down exit, the long-only stance, the no-stop posture, and its own `min_bars = slow + int(sqrt(slow)) + 2` short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-one admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics with the source's own 27-bar guard adopted verbatim as the warmup floor (an already-positioned book treats same-direction cross-up bars as hold-no-ops, a flat book treats cross-down bars as no-ops, re-entry re-arms on any qualifying cross-up after any exit with no cooldown, pre-guard bars flat by the source's own rule — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/hma_cross` / `PREBUILT-HMA-CROSS` / `HMACrossStrategy` / `TYPE_NAME = "hma_cross"` returns zero strategy records — no record cites this source file. Roster-name search for `PREBUILT-HMA-CROSS` returns this record only. The pool's Hull/average-cross cousins are fenced as different constructions in Negative evidence 6 (dual-DEMA cross, Hull-vs-EMA cross, gated triple-average cross, bare EMA cross, EHMA band — none trades a dual-Hull 9/21 cross pair, long-flat, from this file). No open or closed `research/*` PR ever carried this source file (closed-PR title/branch search for `hma` returns zero; the 100 most recent closed PRs contain no Hull-average Scout candidate). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a dual-Hull cross pair (WMA-cascaded Hull legs, `WMA(2·WMA(n/2)−WMA(n), √n)`, no gate, no filter), long-flat, from immutable file `builtin/hma_cross.py`, is a different signal construction from a double-smoothed DEMA cross, a Hull-vs-EMA cross, or a regime-gated triple-average cross — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `HMA Cross strategy` that `Buys when 9-bar HMA crosses above 21-bar HMA. Exits on the reverse crossover.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 124 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Lag-reduced Hull trend following, long-only, state-holding. Each Hull leg cancels single-average lag (weighted WMA cascade with square-root smoothing length), so the fast/slow cross turns earlier than a same-length single-average cross at the cost of less smoothing — the entry buys the exact bar the fast Hull retakes the slow Hull, and the exit surrenders the unit on the exact bar it falls back below. There is no gate, no filter, and no holding leg: a market that alternates crosses prints repeated full round-trips with no flat state to rest in (whipsaw profile, disclosed), while a leg whose reverse cross never prints is held indefinitely. Unlike stop-based systems there is no fixed-distance risk leg — the reverse cross is the sole risk control by construction. Unlike the pool's dual-DEMA sibling (double-smoothed exponential legs, 12/26, 54-bar guard), this system reacts through linear-weighted Hull legs at 9/21 with a 27-bar guard — strictly different turn timing on identical closes, not a re-parameterization of the same curve.

## Signal

Exact rule as pinned (any other period, average family, gate, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `_wma`/`_hma` (lines 13–26) are in-file and `generate_signal` (lines 67–111) is the single source of truth — no second decision logic exists:

```text
WMA(s, n)[t]    = Σ(k=1..n) k·s[t-n+k] / Σ(k=1..n) k            // linear weights, causal
HMA(s, n)[t]    = WMA( 2·WMA(s, floor(n/2)) − WMA(s, n), max(1, int(√n)) )[t]
F[t]            = HMA(close, 9)[t]    // half=4, sqrt=int(√9)=3
S[t]            = HMA(close, 21)[t]   // half=10, sqrt=int(√21)=4
guard           = len(df) < 27 → both signals false, price 0.0 (source's own floor)
long_entry      = F[t-1] <= S[t-1] and F[t] > S[t]              // strict cross-up edge
long_exit       = F[t-1] >= S[t-1] and F[t] < S[t]              // strict cross-down edge
```

- Trade events: `entry_signal=True` with `direction="long"` on cross-up bars (lines 90, 93, 101); otherwise `entry_signal=False` with `exit_signal=bool(cross_down)` (lines 91, 94, 102). Entry and exit legs are provably mutually exclusive (Negative evidence 3), so no bar ever fires both legs and no ordering assumption exists to verify.
- Exact boundaries (pinned semantics): entry needs a strict current-bar inequality (`F[t] > S[t]` — a bar closing with `F == S` to the tick fires neither leg and holds by code); the prior-bar branch admits equality (`<=` / `>=`), so a flat-tied prior bar still admits a genuine current-bar break. Equality on the current bar is a hold, never an entry or an exit. `confidence` (lines 96–98, 105) and the `indicators={hma_fast, hma_slow, atr_14}` echo (lines 106–110) are diagnostic constants per bar — neither conditions any predicate.
- ATR diagnostic fence (lines 68, 81, 88, 96–98): `atr_14` scales only `confidence = min(1.0, spread / (atr*2))` (0.5 fallback when `atr <= 0`) and the echo — deleting the import, the call, and both readers reaches identical entry/exit events on every bar.
- Direction: long-only with an explicit pre-guard flat state (lines 75–77 return both-false). The file's `direction="long"` literals survive the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no short path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the reverse cross is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` and the indicators echo are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further cross-up bars as hold-no-ops (no pyramiding, no averaging); a flat book treats cross-down bars as no-ops; re-entry re-arms on any qualifying cross-up after any exit (no cooldown specified — explicitly none, not invented). Pre-guard bars are flat by the source's own rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` for every order-gating comparison, with fixed non-negative offsets (trailing WMA folds plus a one-bar cross lookback — no shifts, no negative indices); no `open`-series read, no `volume` read, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). All windows are trailing and deterministic given the pinned pandas/numpy semantics. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` range is optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (both Hull legs, the cross read, and the `price` echo). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. (The `atr(df, 14)` call exists only to print the `atr_14` diagnostic and scale `confidence` — it conditions no order and its removal changes no trade event.)
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; every window reads the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own guard — `min_bars = hma_slow + int(sqrt(hma_slow)) + 2 = 21 + 4 + 2 = 27` completed bars, shorter frames returning both-signals-false with `price=0.0` — adopted verbatim as the warmup floor, flat by record rule (predeclared: the guard *is* the seeding discipline for the nested WMA stack; no researcher length is invented). No repainting, no negative shift, no future bars/extrema, no full-sample normalization. Rolling-apply seeding resolves inside the guard: no evaluated bar reads an unseeded window.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-HMA-CROSS` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the thirty-one admitted Forven records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-direction cross-up bars hold without adds; cross-down bars on a flat book are no-ops; any open long ends on the first cross-down bar. Re-entry after an exit needs only the next qualifying cross-up (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (124 lines: module docstring with the cross rule, `TYPE_NAME`, in-file `_wma`/`_hma` helpers, `default_params` with the 9/21 set, the cross-up entry, the cross-down exit, the fixed long-only stance with the literal `"long"` direction tokens, its own 27-bar short-frame guard, the `round(curr_close, 4)` price echo, the `PREBUILT-HMA-CROSS` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard adopted verbatim, not repaired: the file's own `min_bars = slow + int(sqrt(slow)) + 2 = 27` check returns both-signals-false with `price=0.0` on shorter frames — pre-guard bars are flat by the source's own rule, and the nested WMA stack (deepest live window: the 21-bar full WMA inside a 4-bar outer WMA) seeds inside the guard. An engine evaluating from bar 0 without the guard would print NaN-comparison bars (all false) and then start firing cross events from barely-seeded Hull legs — disclosed, never load-bearing past the guard.
2. ATR/confidence/indicators fenced: `atr(df, 14)` (line 81) feeds only `confidence` (lines 96–98, 105) and the `indicators` echo (lines 106–110) — zero order-gating comparisons read any of them. Deleting the import, the call, the spread/confidence block, and the echo reaches identical events on every bar.
3. Co-fire impossibility proven: entry needs `F[t] > S[t]` while exit needs `F[t] < S[t]` — both jointly true is impossible on any bar, including NaN prints (every strict NaN comparison is false, so a NaN leg fires neither side). No tiebreak is needed and none is missing.
4. Exact-touch rules fenced: `F[t] == S[t]` to the tick fires neither leg regardless of history (hold by code); prior-bar equality (`<=` / `>=`) still admits a genuine current-bar break. Strictness is preserved throughout — disclosed, not smoothed.
5. Regime metadata fenced: `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` is defined once and never called by the decision path (which takes only `df`/`params`); treating the label as an entry gate would be a different, unpinned rule.
6. Cousin records fenced as different constructions (none trades a dual-Hull 9/21 cross pair, long-flat, on `1h` BTC bars from this file): the admitted `forven-dema-cross` sibling trades a dual-DEMA 12/26 cross pair (double-smoothed exponential legs `2·EMA(n)−EMA(EMA(n))`, 54-bar guard — different average family, different periods, different guard); the admitted `hull-ema-crossover-reversal` record trades a contemporaneous Hull(5)-vs-EMA(5) cross with immediate two-sided reversal on `1d` from FMZ 430563 (different legs, different direction handling, different frame, different source); the admitted `tema-dema-hma-cross-trend-two-sided` record trades a TEMA(8)-vs-DEMA(43) cross behind an HMA(52) slope gate, two-sided always-in, from a TradingView mirror (different legs, gated vs bare, different source); the admitted `ema-20-50-cross` record trades a bare single-EMA cross (different average family); the admitted `ehma-range-band-breakout` record trades an exponential-Hull envelope band with zero crossover calls (band vs cross). The pool's `dpo-ema-crossover`, `obv-ema-crossover`, `pvt-ema-crossover`, `rvi-swma-cross`, and `cci-ema-rsi-cross` records each cross different constructions (detrended oscillator, volume/price-trend lines, trailing-stop stack, RSI-gated) — none evaluates two Hull averages against each other. Not a re-tuning of any of them: swapping the average family, the periods, the direction handling, or the gate would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the single-unit/hold-no-op position pin, and house sizing/costs — all predeclared above; the in-file Hull arithmetic, the 9/21 pair, the strict cross boundaries, the reverse-cross exit, the long-only stance, the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance, and the 27-bar guard floor are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
8. The 9/21 pair, the Hull construction, the strict cross boundaries, the reverse-cross exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning the periods, converting the cross edge to a level, gating with a regime/volume/ADX filter, adding a stop/target/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: HMA9/HMA21 dual-Hull strict cross pair / reverse-cross exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills / 27-bar guard floor are frozen.

- F1 — Hull relevance: replacing both Hull legs with same-period SMAs (SMA9/SMA21 cross, same guard/pins) must not improve net expectancy; fail ⇒ the Hull construction adds nothing over plain averages.
- F2 — Exit relevance: replacing the reverse-cross exit with a fixed 8-bar time exit (same cross entries, same guard/pins) must not improve net expectancy; fail ⇒ the reverse-cross exit adds nothing over a clock exit.
- F3 — Family relevance: replacing the HMA9/21 pair with the admitted DEMA12/26 cross pair (same bookkeeping, same guard shape at its own 54-bar floor, same pins) must not improve net expectancy; fail ⇒ the Hull pair adds nothing over the double-smoothed exponential pair.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue BTCUSDT perpetual `1h` completed bars with standard close prints (the rule reads `close` for every order-gating comparison — no `open`, no `high`/`low`, no `volume`, no funding/OI reads in any order leg). No session calendar (crypto trades continuously; the trailing WMA folds need no session-gap semantics), no corporate actions, no dividends, no cross-venue state. 24/7 continuity means the rolling windows are always the immediately prior prints — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no position semantics: single-unit/hold-no-op bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour. The 27-bar guard floor is source-verbatim, not a researcher pin.
- The source ships no costs: all economics come from the house overlay; the Forven engine's own fills may differ — this record is not evidence of source-engine economics.
- ATR dependence is diagnostic-only (Negative evidence 2); unread regime metadata (Negative evidence 5).
- The `parameter_space` optimizer range names the period search surface — disclosed; the rule reads only the `hma_fast=9` / `hma_slow=21` defaults and exercises no search.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/hma_cross.py
- https://github.com/judder659/Forven
