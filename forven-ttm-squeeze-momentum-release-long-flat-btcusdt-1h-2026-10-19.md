---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven TTM-squeeze momentum-release long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ttm_squeeze.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven TTM-squeeze momentum-release long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-bb-squeeze-breakout-long-flat`, `forven-chandelier-exit-long-stop-cross`, `forven-engulfing-body-cover-volume`, `forven-stddev-cross-swing`, `forven-hma-cross`, and thirty other admitted Forven records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ttm_squeeze.py`.
- GitHub blob SHA at the pinned commit: `07aa1c5d3f13328e757c8567fa78e52a812efe9c`, size 5417 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 5417 bytes, 169 lines, SHA-256 `e2b876a54343f85c6cc97e6d556d8c2f7042d58146bcb62ba4c19c2c52b1dc28`, and `git hash-object` reproduces the GitHub blob (`07aa1c5d…2efe9c`) — the entire file was retrieved twice and inspected (both fetches byte-identical, matching the local cache).
- Registration: the file self-registers via `STRATEGY_CLASS = TTMSqueezeStrategy`, `TYPE_NAME = "ttm_squeeze"`, and the `STRATEGIES = [("PREBUILT-TTM-SQUEEZE", TTMSqueezeStrategy, {"_asset": "BTC"})]` roster pin. Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `builtin/ttm_squeeze` / `PREBUILT-TTM-SQUEEZE` / `TTMSqueezeStrategy` / `TYPE_NAME = "ttm_squeeze"` returns zero strategy records citing this source file (the sole pool mention is fence prose inside the admitted `forven-bb-squeeze-breakout` record, which names this file only as an unadmitted neighbour).
- The file's own words (quoted for gate evidence, never extended): module docstring `TTM Squeeze strategy.` with `Entry: Bollinger Bands contract inside Keltner Channels (squeeze on), then squeeze releases and momentum turns positive.` and `Exit: Momentum turns negative after being positive.`; `describe()` returns `Squeeze detected when BB(20, 2.0std) fits inside KC(20, 1.5x ATR). Enters on squeeze release with positive momentum(12). Exits when momentum turns negative.`; `default_params` returns exactly `{ "bb_period": 20, "bb_std": 2.0, "kc_period": 20, "kc_mult": 1.5, "mom_period": 12, "leverage": 1.0 }`; `compatible_regimes` returns `{"BREAKOUT", "TREND_UP"}` (metadata never read by the signal path); `parameter_space()` returns `{ "bb_period": (15, 25, 5), "bb_std": (1.5, 2.5, 0.5), "kc_period": (15, 25, 5), "kc_mult": (1.0, 2.0, 0.5), "mom_period": (8, 16, 4) }` (a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 169 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 169 lines, so no twin-selection ambiguity exists. The method pins its constants (`bb_period` 20, `bb_std` 2.0, `kc_period` 20, `kc_mult` 1.5, `mom_period` 12), builds the Bollinger triple in-file (rolling mean plus population standard deviation `ddof=0`), builds the Keltner pair in-file (EMA midline plus in-file rolling-mean ATR), builds the linreg-style momentum oscillator in-file, reads the last two squeeze prints and the last two momentum prints, evaluates the release-plus-positive-momentum entry and the momentum-flip exit on the decision bar, and returns a single `Signal`.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-bb-squeeze-breakout`, `forven-chandelier-exit-long-stop-cross`, and `forven-engulfing-body-cover-volume` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default with direction normalization.
- Full-file token census (verified by search over the 169 lines this cycle): `def generate_signal` exactly once, `def generate_signals` zero times; `direction` on three code lines only (the warmup-guard literal `"long"`, the dynamic `direction = "long" if curr_mom > 0 else "short"` oscillator-sign label, and its constructor pass-through — entry bars always carry `"long"`, see Signal); 0 `sell` / 0 `stop=` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` as order arguments; 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request.` / 0 `security(` / 0 `barstate` / 0 `timeframe` in any line; 0 `rsi` / 0 `macd` / 0 `stoch` / 0 `supertrend` / 0 `ichimoku` / 0 `vwap` / 0 `adx` (no second indicator, no regime filter beyond the squeeze gate itself); 0 `df["open"]` / 0 `df["volume"]` reads (the rule consumes `close`/`high`/`low` only — `close` directly, `high`/`low` inside the in-file TR and momentum midline); 0 `isna` / 0 `isnull` guards (NaN behaviour disclosed in Negative evidence 3, never invented); 0 `pyramid` / 0 `position_` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); `len(df)` exactly once (the `min_len = max(20, 20, 12) + 2 = 22` short-frame guard); `ewm` exactly once (the KC EMA midline); `rolling` five times (BB pair, ATR, momentum midline); `shift` once (the `prev_close` for True-Range).
- ATR/KC construction pinned in-file (no facade ambiguity): True-Range `max(high - low, |high - prev_close|, |low - prev_close|)` with a plain rolling mean (`tr.rolling(window=kc_period).mean()`) — SMA smoothing, never Wilder RMA, never EWM; the KC midline is `close.ewm(span=20, adjust=False).mean()` (seeded from bar 0, fenced by the warmup pin); the KC pair is therefore `EMA20(close) ± 1.5 × SMA-ATR(20)`, fully pinned. The Bollinger pair is `SMA20(close) ± 2.0 × population-stdev(close, 20, ddof=0)` — population denominator, never sample `ddof=1`; substituting the sample estimator would be a different, unpinned rule.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 20-bar SMA midline, the 2.0-sigma population-stdev Bollinger triple, the 20-bar EMA-midline plus SMA-ATR Keltner pair at 1.5×, the prior-bar BB-inside-KC squeeze gate, the squeeze-release-plus-positive-momentum entry, the momentum-flip exit, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit long-flat position pin with hold-no-op semantics plus a 30-bar researcher warmup floor (an already-positioned book treats further release bars as hold-no-ops, a flat book treats momentum-flip bars as no-ops, re-entry re-arms on any qualifying release-plus-momentum bar after any exit with no cooldown, pre-warmup bars flat by record rule, and the dynamic `direction` label is read only as the momentum-sign diagnostic — entry bars always carry `"long"`, exit bars carry the `"short"` sign but close to flat, never open a short — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/ttm_squeeze` / `PREBUILT-TTM-SQUEEZE` / `TTMSqueezeStrategy` / `TYPE_NAME = "ttm_squeeze"` returns zero strategy records citing this source file. No open `research/*` PR carries this source file (open PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources; #304 is the Forven `cci.py` sibling, a different file and a different oscillator-recross machine). Not a duplicate, paraphrase, or trivial parameter variant: a squeeze-release-plus-momentum-oscillator machine (contraction release AND oscillator-sign trigger, momentum-flip exit) is a different signal construction from a band-breakout machine, a raw band breakout, or a dual-percentile contraction system — different gate × different trigger × different exit × different immutable source file.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `TTM Squeeze strategy` where `Bollinger Bands contract inside Keltner Channels (squeeze on), then squeeze releases and momentum turns positive`, entering on that release and exiting when `Momentum turns negative after being positive.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 169 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Volatility-contraction-release momentum timing, long-only, state-holding. The system waits for compression first (the whole Bollinger envelope nesting strictly inside the Keltner envelope on the prior bar), then buys only the exact bar the envelope expands back out while the linreg-style momentum oscillator prints positive — unlike the admitted BB-squeeze sibling, a band break without oscillator confirmation prints nothing here, and unlike raw-breakout systems, an expansion without a preceding squeeze prints nothing either. The exit is the momentum down-flip, so the trade holds the expansion leg until the oscillator itself rolls over, with no band-midline leg and no stop. The failure mode is plain: a release that prints positive momentum but immediately fades whipsaws with no stop and no cooldown, a grinding advance whose oscillator never flips is held with no profit-taking leg, and downside resolutions never enter (long-only with no short leg).

## Signal

Exact rule as pinned (any other band period, sigma multiple, KC period, KC multiple, midline estimator, ATR smoother, stdev denominator, momentum period, gate polarity, trigger polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` is the single source of truth — no second decision logic exists:

```text
inputs (defaults, frozen): bb_period = 20, bb_std = 2.0, kc_period = 20, kc_mult = 1.5, mom_period = 12
bb_ma_t    = SMA(close, 20) on bars ending at bar t              // rolling mean
bb_sd_t    = population stdev(close, 20, ddof=0) on bars ending at t
bb_upper_t = bb_ma_t + 2.0 * bb_sd_t
bb_lower_t = bb_ma_t - 2.0 * bb_sd_t
kc_ma_t    = EMA(close, span 20, adjust=False) on bars ending at t
TR_t       = max(high_t - low_t, |high_t - close_{t-1}|, |low_t - close_{t-1}|)
atr20_t    = mean(TR over the last 20 bars ending at bar t, plain rolling mean)
kc_upper_t = kc_ma_t + 1.5 * atr20_t
kc_lower_t = kc_ma_t - 1.5 * atr20_t
sqz_t      = (bb_lower_t > kc_lower_t) AND (bb_upper_t < kc_upper_t)
mid12_t    = (highest(high, 12)_t + lowest(low, 12)_t) / 2
mom_t      = close_t - (mid12_t + bb_ma_t) / 2
released   = sqz_{t-1} AND (NOT sqz_t)
entry      = released AND (mom_t > 0)
exit_      = (mom_{t-1} > 0) AND (mom_t <= 0)
```

- Warmup (predeclared researcher pin — the source ships only a 22-bar `min_len` guard): 30 completed `1h` bars flat by record rule. Structural minimum is the 22nd completed bar (20-bar BB/KC seeds plus the TR one-bar shift plus the prior-bar squeeze reference). Pre-warmup bars are flat by record rule; the raw source would print NaN-gated no-signals through bar 20 — that unreachable region is fenced here by the record rule, never presented as source behaviour. The KC EMA midline is seeded from bar 0 (`ewm` without `min_periods`) — the 30-bar floor fences that seeding the same way the admitted EMA-cross record fences its own EWM chain. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.
- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`. A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. The entry is an edge event (fires once on the release bar — refires require a fresh squeeze-plus-release); the exit is an edge event (fires once on the momentum down-flip bar). The `direction` field is the momentum-sign diagnostic: every entry bar carries `"long"` by construction (`mom_t > 0`); exit bars carry the `"short"` sign but this record closes to flat and never opens a short — no short `entry_signal` exists on any bar.
- Mutual-exclusion proof (no tie-break pin required): entry requires `mom_t > 0` while exit requires `mom_t <= 0` — the strict oscillator-sign inequalities are pairwise opposite, unsatisfiable on every bar. A zero print (`mom_t == 0`) fails the entry leg and satisfies only the exit leg when the prior print was positive. The squeeze conjunct cannot reunite the legs. The reviewer is never asked to invent an ordering.
- Exits and risk (explicit): the momentum down-flip is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (momentum-magnitude ratio over the trailing 20-bar momentum stdev, zero-guarded) and the `indicators={...}` dict are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit long-flat; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying release-plus-momentum bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` with fixed non-negative offsets (last two squeeze prints, last two momentum prints, plus trailing 20/20/12-bar windows ending at the decision bar), exact comparisons, and one zero-guarded ratio (`mom_std > 0` before the confidence division — the order legs divide nothing). No `request.*`, `security()`, `timeframe*`, `barstate.*`, `open`/`volume` read, RSI/MACD/Stochastic/ADX/Supertrend/Ichimoku smoothing, session/calendar call, or stop/limit order argument exists anywhere in the order-gating path (verified by the census above returning zero matches). The `compatible_regimes == {"BREAKOUT", "TREND_UP"}` set is metadata never read by the signal path, so no regime model gates any order. Substituting sample-stdev, Wilder-RMA smoothing, an SMA KC midline, a band-breakout trigger, or any second gate would be a different, unpinned rule.

## Required data

- `close`/`high`/`low` on `BTCUSDT` `1h` completed bars only (sole reads: `close` directly for the bands, KC midline, and momentum; `high`/`low` inside the in-file True-Range arithmetic and the 12-bar momentum midline). No `open`, no `volume`, no external feed, no funding/OI/mark-price leg, no calendar, no multi-asset input.
- Warmup: 30 completed `1h` bars flat by record rule (structural minimum the 22nd completed bar — 20-bar BB/KC seeds plus the TR shift plus the prior-bar squeeze reference — plus margin for the KC EMA seeding).
- Point-in-time: every window is trailing over completed bars ending at the decision bar (the band/ATR/momentum windows are unshifted but the decision bar is completed before evaluation — no future bar, no unfinished-bar read, no repainting); the decision bar's own `close` is both the last input and (via the derived same-bar-close pin, `price=round(curr_close, 4)`) the fill price basis.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1h`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit long-flat position with hold-no-op semantics plus the 30-bar researcher warmup floor, house sizing/capital/costs replacing the bare `leverage: 1.0` default.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1h` with declared house fees/funding/slippage overlay; squeeze-gated momentum-release arithmetic over completed `close`/`high`/`low` on a single frame with same-bar-close fills is within the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record. The single `ewm(span=20)` KC midline reuses the already-verified EWM primitive from the admitted EMA-cross sibling — no new smoother is introduced.
- Sizing/capital (stated plainly): the admitted version trades exactly one fixed unit — a flat book enters one unit on an entry bar, a long book exits the whole unit on an exit bar, same-direction refires are hold-no-ops, no pyramiding, no averaging, no safety orders, no cooldown. The downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus modeled funding/slippage with explicit limitations; modeled funding is never reported as realized funding) apply to the derived evaluation here and change no trade event under the predeclared single-unit rule — DCA is a downstream execution experiment, never an admission leg of this version. No capital-dependent forced-close state beyond the standard isolated-margin accounting is admitted.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `bb_period 20` / `bb_std 2.0` / `kc_period 20` / `kc_mult 1.5` / `mom_period 12` inputs with an SMA midline, population-stdev bands, EMA-midline plus SMA-ATR Keltner pair, prior-bar squeeze nesting, release-plus-positive-momentum entry and momentum-flip exit, oscillator-sign direction label, no risk legs) and the `PREBUILT-TTM-SQUEEZE` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: full-file search returns exactly one `def generate_signal` and zero `def generate_signals` — there is no second decision path to select between.
2. No estimator ambiguity: the ATR is built in-file as a plain rolling mean over in-file True-Range — no facade import, no registry key, no Wilder/EWM variant is reachable from this file's import path. The KC midline is the file's own single `ewm(span=20, adjust=False)` line — no SMA-midline alternative exists in this file. The Bollinger stdev is the file's own single `std(ddof=0)` line — population denominator, never sample. No variant selection exists to pin or fence beyond the recorded construction.
3. NaN determinism, stated plainly: the file ships no `isna` guard (verified zero matches), so a `NaN` band/ATR/momentum print can only meet the strict gate/trigger inequalities as `False` on both legs — NaN bars emit no signal by construction, never a spurious order. On complete data the 30-bar record floor already covers all 20-bar seeds plus the prior-bar reference, so no NaN reaches any order line in the admitted configuration; missing bars stay flat and are never fabricated. Below the 22-bar guard the raw source returns the flat early-guard — fenced unreachable by the record warmup rule, disclosed here, never a load-bearing claim.
4. Equality boundaries fire nothing on the entry leg: the release requires a strict prior-inside plus current-outside pair and the momentum leg requires strict `> 0`; a close that merely touches a band or prints exactly `mom == 0` holds the prior state on the entry leg by construction. The exit leg fires on `mom <= 0` only from a strictly positive prior print — a flat-zero hover without a positive prior prints nothing.
5. Same-bar double-fire is impossible (mutual-exclusion proof in Signal) — no ordering assumption, invented or otherwise, is required. The entry is an edge release and the exit is an edge flip on opposite oscillator signs, so an entry bar can never simultaneously satisfy the exit leg.
6. Pool Bollinger cousins fenced, stated plainly: `bollinger-band-breakout-long-midline-exit` breaks the raw upper band with no contraction gate and exits at the midline (any breakout bar fires there; here only post-squeeze releases with positive momentum fire — a breakout without a preceding squeeze trades there and fires nothing here, so the trade-event sets differ by construction); `sideways-dmi-bollinger-breakout`, `chartart-bollinger-rsi-double-joint-cross`, and `forven-bollinger-s00120-rsi-breakout` each add DMI/RSI joint-cross gates this record never evaluates. None requires the prior-bar BB-inside-KC nesting AND-gated with a momentum-oscillator sign this record gates on.
7. Pool squeeze cousins fenced, stated plainly: the admitted `forven-bb-squeeze-breakout` sibling (same repo, file `builtin/bb_squeeze.py`, blob `d7805ee7…72dd9c`) enters on close-vs-upper-band breakout AND-gated with the same prior-bar nesting but exits at the band midline with no oscillator — different trigger (price-breakout vs release-plus-momentum), different exit (midline vs momentum flip), different KC midline (SMA vs EMA), different stdev denominator (sample vs population), different immutable source file. `sqzmom-lb-squeeze-release-ema100` (LazyBear, TradingView) enters on squeeze-colour transitions AND-gated with a linreg-momentum oscillator rising/falling against trailing 100-bar extremes plus EMA100 plus close-tick gates, two-sided with momentum-tick exits — different trigger detail, different exit, different direction handling (long-flat vs two-sided), different immutable source. `forven-volatility-contraction-breakout` (sibling file `builtin/volatility_contraction_breakout.py`) requires a dual squeeze (ATR below its 200-bar 20th percentile AND BB-width below half its 200-bar median) AND-gated with an EMA200 trend filter and an RSI50 gate, two-sided with EMA200-fallthrough exits and a 200-bar source guard — different gate (dual percentile/median vs single prior-bar nesting), different trigger (trend-plus-momentum level vs release-plus-oscillator-sign), different exit, different direction, different immutable source file. The FMZ Keltner-momentum record (481364) breaks a Keltner envelope AND-gated with a 14-bar momentum-sign filter, two-sided — no Bollinger triple, no squeeze nesting, no linreg-style oscillator. This record is therefore never evidence for any of those rules, and none of them is this rule's provenance.
8. Variant menus fenced, stated plainly: the `parameter_space()` surface (`bb_period` 15–25, `bb_std` 1.5–2.5, `kc_period` 15–25, `kc_mult` 1.0–2.0, `mom_period` 8–16) is a documented search grid the code never runs — this record freezes the `20/2.0/20/1.5/12` defaults as written; adopting any grid point, switching to sample stdev, switching the KC midline to SMA, switching to Wilder/EWM ATR smoothing, or adding a trend/volume gate would each be a different, unpinned rule.
9. Diagnostic quarantine, stated plainly: the `direction` sign on non-entry bars, `confidence` (momentum-magnitude ratio), and the `compatible_regimes == {"BREAKOUT", "TREND_UP"}` set are computed into the signal label, the confidence field, or class metadata and read by zero order-gating comparisons beyond the pinned entry/exit legs — treating any of them as an extra gate, filter, exit leg, or sizing input would be a different, unpinned rule.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20/2.0/20/1.5/12` squeeze-release-plus-momentum / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: replacing the prior-bar BB-inside-KC squeeze gate with an unconditional positive-momentum trigger (same momentum-flip exit) must not improve net expectancy on the frozen 42-cell campaign; fail ⇒ the contraction gate adds nothing over the bare oscillator.
- F2 — Trigger relevance: replacing the release-plus-momentum entry with the sibling's close-vs-upper-band breakout entry (same squeeze gate, midline exit) must not improve net expectancy; fail ⇒ the oscillator trigger adds nothing over the price-breakout trigger.
- F3 — Exit relevance: replacing the momentum-flip exit with the sibling's band-midline-recross exit (same release-plus-momentum entries) must not improve net expectancy; fail ⇒ the oscillator exit adds nothing over the midline exit.

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1h` OHLCV on Binance — the rule consumes completed-bar `close`/`high`/`low` only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. The long-only no-stop posture expresses fully on spot; perps add no required leg. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding.

## Limitations

- Late entries by construction: the entry demands a full contraction print plus an expansion bar plus positive momentum, so expansions that never compress first are skipped entirely and post-squeeze releases enter strictly after the first expansion bar closes — disclosed lag-and-skip profile.
- False-release whipsaw: releases whose momentum immediately rolls over print enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- Down-move blindness: squeeze resolutions to the downside never enter (long-only, no short leg; the `"short"` direction token on exit bars is the oscillator sign, never a short order) — disclosed opportunity gap, never a hidden short.
- No risk leg: no stop loss, take profit, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions after a release entry have no capital guardrail besides the eventual momentum flip.
- No profit-taking disposition: a grinding advance whose oscillator stays positive is held with no target — the momentum flip is the sole exit and there is no time stop; opportunity cost accrues, disclosed.
- Researcher warmup pin: the 30-bar floor is a record rule covering the 22-bar source guard plus the KC EMA seeding — the raw source is NaN-gated below its seed windows; the admitted configuration never evaluates there.
- Single-market scope: derived pin is `BTCUSDT` `1h` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ttm_squeeze.py (primary source — executable Python strategy, 169 lines, fetched live 2026-10-19 at pinned HEAD commit, 5,417 bytes, SHA-256 `e2b876a54343f85c6cc97e6d556d8c2f7042d58146bcb62ba4c19c2c52b1dc28`, blob `07aa1c5d…2efe9c`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository context; pinned HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` verified this cycle)
- `forven/strategies/base.py` at the same commit (supporting semantics — `Signal` defaults and direction normalization, 12,238 bytes, blob `27508a2a…fabf881`, identical to the blob pinned by admitted sibling records)
