---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven MACD 5/13/3 ADX-regime-gated cross long-flat on ETHUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/macd.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven MACD 5/13/3 ADX-regime-gated cross long-flat on ETHUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-donchian-regime-breakout`, `forven-keltner-adx-gated-breakout`, `forven-parabolic-sar-cross`, `forven-rsi-boundary-rejection`, and thirty-five further Forven-sibling records on `main`).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/macd.py`.
- GitHub blob SHA at the pinned commit: `90410fdd7a8873079c410222425d62dd68b1c51d`, size 3872 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3872 bytes, 115 lines, SHA-256 `ab52871811f34d8b5c53c689c78e4a069fdfb37edc8a9ebd387e8832fe1cc4e8` (dual-fetch byte-identical this cycle), and `git hash-object` reproduces the GitHub blob (`90410fdd7…b1c51d`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = MACDStrategy` (line 111), `TYPE_NAME = "macd"` (line 7), and the single-leg `STRATEGIES = [("S030-MACD-ETH", MACDStrategy, {"_asset": "ETH"})]` roster pin (lines 113–115). No pool record cites this source file (see pre-write dedup below).
- The file's own words (quoted for gate evidence, never extended): module docstring `MACD Cross strategy — S030.` (line 1); `describe()` returns `Uses MACD (5/13/3) to track momentum. Buys when MACD crosses above the signal line in an uptrend. Sells on the reverse crossover.` at defaults (lines 35–41 — the `Sells` token is display prose; no short leg exists, see census); `default_params` returns exactly `{ "fast": 5, "slow": 13, "signal": 3, "ema_regime": 200, "adx_min": 20, "leverage": 3.0 }` (lines 25–29); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 32–34, metadata never read by the signal path — the single `compatible_regimes` token in the 115 lines is its own definition); `parameter_space()` returns `{ "fast": (3, 8, 1), "slow": (10, 21, 2), "signal": (2, 5, 1) }` (lines 103–108, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 115 lines — this record adopts no source-reported performance (see Evidence).
- Dual decision paths, verified mutually consistent: `generate_signal()` (lines 66–101) is the scalar bar path; `generate_signals()` (lines 43–64) is the vectorized twin whose docstring declares itself the `SINGLE source of entry/exit logic` (line 44). Predicate for predicate they agree — cross-up/cross-down legs (lines 59–60 vs the twin's own booleans consumed at lines 87–88), regime leg (line 61 vs same), ADX leg (line 61 vs same), entry conjunction (line 61), unconditional cross-down exit (line 62) — with `.fillna(False)` a no-op over NaN-free series (see Signal). The scalar path delegates its booleans to the twin (`entries, exits = self.generate_signals(df)`, line 86) and only echoes numerics. No third decision logic exists.
- External helpers pinned at the same commit (same-pin lineage as the admitted `forven-ema-cross-adx-regime` sibling, which verified these byte ranges at this exact commit): `generate_signal` imports `adx, atr` from `forven.strategies.indicators` (line 67; twin re-imports `adx` at line 47), resolving to the pinned scanner chain — `adx(df, period)` is an `ewm(span=period, adjust=False)`-smoothed TR/DM/DX chain with `1e-9` floors and no `min_periods` (seeded from bar 0, defined on every bar); `atr(df, period)` is a `rolling(period).mean()` true-range average. Both read `high`/`low`/`close` plus one-bar shifts only — trailing, causal, deterministic. The `atr_14` value is echoed into `indicators` only and never enters any predicate (see Signal).
- Base-class semantics pinned at the same commit (same-pin lineage as the admitted siblings): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes, verified via the contents API this cycle) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; `_normalize_signal_direction` maps the `"long"` literal back to `"long"` on entry and non-entry bars alike — the file's single `direction="long"` literal (line 92) therefore survives untouched on every bar.
- Full-file token census (verified by search over the 115 lines this cycle): `direction=` occurs exactly once (`"long"` — no short leg exists); 0 `short` anywhere; 1 `sell` / 1 `crossover`, both inside the `describe()` prose sentence on line 40 (`Sells on the reverse crossover.` — display text, zero order-gating lines); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default, replaced by the house overlay — see Execution assumptions); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (order-gating reads are `close` directly plus `high`/`low` inside the pinned ADX/ATR helpers); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `rsi` / 0 `stoch` / 0 `vwap` / 0 `supertrend` / 0 `ichimoku` / 0 `rolling(` (no foreign indicator, no lookback helper of its own); 0 `len(df)` (the file ships no length guard — the 200-bar warmup in Required data is a predeclared researcher pin, never a source claim). The 9 `return` hits are Python return statements and the 1 `win` hit is the `twin` docstring token — zero performance language.
- Param fence: the predicate reads only keys present in `default_params` (`fast`, `slow`, `signal`, `ema_regime`, `adx_period` via `.get` default 14, `adx_min`) — treating any other key as live would be a different, unpinned rule, and no optimizer range is exercised by this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the S030 ETH roster leg, the 5/13/3/200/14/20 construction, the ADX-plus-regime entry conjunction, the unconditional cross-down exit, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no length guard, no position-sizing rule, and no entry/exit evaluation ordering beyond its own conjunction. Researcher-declared adaptations are exactly four: (1) research market/timeframe `ETHUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset ETH` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, pivot-s1-bounce, volatility-contraction-breakout, connors-rsi, kdj, heikin-ashi, bb-edge-fade, rsi-s00139, obv-ema-cross, mfi-threshold-cross, williams-r-adx-gated, rsi-boundary-rejection, ema-cross-adx-regime, tema-cross, and sibling records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 200-bar researcher warmup pin (the file carries no position reference and no length guard — an already-positioned book treats same-side entry bars as hold-no-ops, a flat book treats cross-down exit bars as no-ops, re-entry re-arms on the next qualifying gated cross with no cooldown, and the first 200 completed bars are flat warmup covering the EMA200 plus ADX ewm seeding; SQZMOM-LB / volatility-contraction-breakout precedent for the bookkeeping, warmup derived as `max(5, 13, 3, 200, 14)` exactly as the admitted ema-cross-adx-regime record derives its 200-bar warmup — both pins disclosed, never presented as source-native behaviour); (4) the source's bare `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/macd` / `MACDStrategy` / `S030-MACD` returns zero strategy records citing this source file (the two `S030` filename hits are `S0304`-DOI substrings inside unrelated Grinblatt paper records, verified forven-free). The pool's MACD cousins are fenced as different constructions in Negative evidence 8 (naked FMZ 12/26/9 two-sided reversal, Ichimoku-triple-confirm composite, VSTOP-trailing Alorse leg, MACD+BB deadzone system — none trades a 5/13/3 MACD/signal cross conjunction-gated by ADX14 ≥ 20 and a close-above-EMA200 regime leg with an unconditional cross-down exit, long-only, from this file). No closed `research/*` PR ever carried this source file (merged Scout PRs through #314 are WorldQuant/PVI/Mayer/PGO plus forty-three Forven files through TEMA cross #314, none of them MACD). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), #251 (Swift 2-year MA multiplier zone-state long-flat), and #304 (Forven CCI oversold-recross long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: second-order oscillator rotation (MACD-minus-signal of double-smoothed price) plus two conjunctive entry gates is a different normalized signal with strictly different entry events from any naked cross, not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: momentum tracking that buys when the 5/13/3 MACD crosses above its signal line in an uptrend (regime plus strength agreement), and sells — i.e. exits the long — on the reverse crossover. No behavioural, structural, or risk-premium channel is claimed anywhere in the 115 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Gated second-order rotation machine, long-only, both gates conjunctive. Unlike the pool's naked-cross MACD record (FMZ 12/26/9: every rotation enters, including rotations printed inside directionless chop, and every death cross reverses to short), this system fires on a faster 5/13/3 construction and spends two vetoes before every entry: the ADX leg vetoes crosses fired in flat markets where directional movement is weak, and the regime leg vetoes crosses printed below the prevailing 200-bar drift — and it never shorts, so vetoed or reversed bars leave the book flat instead of reversed. Unlike the admitted `forven-ema-cross-adx-regime` sibling (first-order price-average cross with the same 200/ADX20 gate idiom), the trigger here compares two derived momentum series (both functions of 5/13 EMAs of close, then smoothed again by 3) — entries fire on second-order rotation, strictly later and smoother than first-order price crosses, at the cost of deeper lag into V-turns; gate-sharing is not signal-sharing. Unlike oscillator-reclaim cousins (RSI pullback, KDJ, Connors, Stochastic level-recross), neither gate carries a reclaim or recross memory: ADX and regime are pure level states evaluated on the decision bar alone, so the only event memory in the system is the two-bar MACD cross itself. Unlike stop-carrying records, the sole risk control is the ungated cross-down exit — a position opened under strong, aligned conditions is still cut the first bar the momentum lines re-cross, with no stop, no target, and no regime-based early exit.

## Signal

Exact rule as pinned (any other average variant, period, threshold, gate, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 66–101) is the single source of truth and the twin `generate_signals` (lines 43–64) agrees leg for leg:

```text
ema_fast[t]   = close.ewm(span=5, adjust=False).mean()
ema_slow[t]   = close.ewm(span=13, adjust=False).mean()
macd[t]       = ema_fast[t] - ema_slow[t]
macd_sig[t]   = macd.ewm(span=3, adjust=False).mean()
ema_regime[t] = close.ewm(span=200, adjust=False).mean()
adx[t]        = scanner.adx(df, 14): TR=max(h-l,|h-prev_close|,|l-prev_close|);
                dm+/dm- strict-comparison-clipped; di±=100*dm±.ewm(span14)/max(atr_e,1e-9);
                dx=100*|di+-di-|/max(di++di-,1e-9); adx=dx.ewm(span14)
cross_up      = prev_macd <= prev_macd_sig AND curr_macd > curr_macd_sig
cross_down    = prev_macd >= prev_macd_sig AND curr_macd < curr_macd_sig
regime_ok     = close[t] > ema_regime[t]
adx_ok        = adx[t] >= 20
long_entry    = cross_up AND regime_ok AND adx_ok
long_exit     = cross_down                            // unconditional, ungated
guard         = none in source — first 200 completed bars flat by researcher pin
```

- Trade events: `entry_signal=True` with `direction="long"` on gated cross-up bars (line 92); otherwise `entry_signal=False` with `exit_signal=bool(cross_down)` (lines 90–91). Entry and exit legs are provably mutually exclusive (Negative evidence 6), so no bar ever fires both legs and no ordering assumption exists to verify.
- Exact boundaries (pinned semantics): cross legs admit previous-bar equality (`<=` / `>=`) but demand strict current-bar separation (`>` / `<`) — momentum lines printing exactly equal fire neither leg. `regime_ok` is strict (`>` — `close == ema200` admits no entry and, the exit being cross-only, holds any open side by code). `adx_ok` admits equality (`>=` — ADX printing exactly 20.0 gates nothing out). A bar with both momentum lines exactly equal fires neither entry nor exit regardless of gates.
- Direction: long-only with an explicit pre-first-signal flat state plus the 200-bar warmup flat. The file's single `direction="long"` literal survives the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no `strategy.short`-equivalent path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the ungated cross-down is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min(1.0, adx/40)` on gated entries, `0.0` elsewhere, line 93) and the full `indicators` echo (`macd`, `macd_signal`, `ema_regime`, `adx`, `atr_14`) are diagnostic — none conditions any order line, and `atr_14` (a `rolling(14).mean()` true-range average, NaN on the first 13 bars) never enters any predicate.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats cross-down exit bars as no-ops; re-entry re-arms on any qualifying gated cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by pin. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (EMA seed, MACD arithmetic, regime comparison, cross legs) and `high`/`low` (inside the pinned ADX/ATR helpers) — no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). All windows (ewm seeds, one-bar shifts, cross lookback) are trailing and deterministic given the pinned pandas semantics; ewm series carry no `min_periods`, so every value from bar 0 is seed-defined rather than NaN-gated — the 200-bar researcher warmup exists precisely to fence that seeding (Negative evidence 1). The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` ranges are optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of ETHUSDT: `close` (the two EMAs, the MACD/signal pair, the regime comparison, both cross legs) and `high`/`low` (true-range and directional-movement legs inside the pinned ADX/ATR helpers). No bar `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all seeds, shifts, and the two-bar cross read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships no length guard, so this record predeclares a 200-bar researcher warmup pin — `max(fast = 5, slow = 13, signal = 3, ema_regime = 200, adx_period = 14) = 200`, exactly the derivation the admitted ema-cross-adx-regime sibling applies to its own set. The pin covers the EMA200 seed, the span-14 ADX ewm seeding chain, and the two-bar cross lookback; the first 200 completed bars are flat by pin. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: ETHUSDT Binance perpetual under the house overlay (researcher choice of the `S030-MACD-ETH` roster leg — the source roster pins `_asset ETH` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-side entry bars hold without adds; cross-down bars on a flat book are no-ops; any open long ends on the first cross-down bar regardless of gates. Re-entry after an exit needs only the next qualifying gated cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (115 lines: module docstring with the S030 tag, `TYPE_NAME`, `default_params` with the 5/13/3/200/14/20 set, the MACD/signal/regime/ADX arithmetic, the ADX-plus-regime conjunction, the unconditional cross-down exit, the `direction="long"` literal and the `round(curr_close, 4)` price echo, the twin vectorized path, the `S030-MACD-ETH` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Missing-guard fenced with a pin, not a repair: the file contains zero `len(df)` checks, and every series it touches is seed-defined from bar 0 (ewm without `min_periods`; ADX ewm chain with `1e-9` floors and no NaN gate) — so without a pin the rule would already fire entries on the earliest bars of any frame, with values dominated by seeding. The 200-bar researcher warmup (`max(5, 13, 3, 200, 14)`) fences exactly that: pre-warmup bars are flat by pin, post-warmup events are seed-stable. An engine evaluating from bar 0 without the pin reaches different early events — disclosed, never load-bearing past warmup.
2. ADX variant fenced: the pinned `scanner.adx` smooths with `ewm(span=14)` (α = 2/15), not Wilder's RMA (α = 1/14) — close but not identical under the hood, and the `adx_min = 20` threshold applies to this span-smoothed variant as written. Disclosed, not converted to textbook Wilder.
3. Diagnostic-only values fenced: `confidence` (`min(1.0, adx/40)`), the full `indicators` echo, and `atr_14` (rolling-14 true-range mean, NaN on the first 13 bars) condition no predicate — deleting all three reaches identical events on every bar.
4. Regime metadata fenced: `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` is defined once and never called by either decision path (both take only `df`/`params`); treating the label as an entry gate would be a different, unpinned rule.
5. Dual-path consistency fenced: scalar and vectorized twins agree leg for leg (cross-up, cross-down, regime, ADX, entry conjunction, unconditional exit); `.fillna(False)` is a verified no-op over the NaN-free ewm/ADX series. No twin-selection ambiguity exists here — disclosed, not repaired.
6. Co-fire impossibility proven: `cross_up` needs current MACD strictly above current signal while `cross_down` needs it strictly below — both jointly true is impossible; both-lines-equal fires neither. No tiebreak is needed and none is missing.
7. Exact-touch rules fenced: previous-bar equality admits a cross leg (`<=` / `>=`), current-bar equality kills both legs; `close == ema200` admits no entry and triggers no exit (hold by code); ADX printing exactly 20.0 satisfies `adx_ok`. Strictness is preserved throughout — disclosed, not smoothed.
8. Cousin records fenced as different constructions (none trades a 5/13/3 MACD/signal cross conjunction-gated by ADX14 ≥ 20 and a close-above-EMA200 regime leg with an unconditional cross-down exit, long-only, on `1h` ETH bars from this file): the admitted `macd-signal-cross-reversal` record pins the FMZ 356844 Pine demo — a naked 12/26/9 rotation with zero confirmation legs, two-sided always-in-market reversal on `1d` BTC bars (every weak-ADX and below-regime cross this record vetoes trades there, and every exit here reverses to short there); the admitted `ichimoku-macd-triple-confirm-reversal` AND-gates the line/signal cross behind three Ichimoku confirmation legs on ETHUSDT 1h; the admitted `alorse-macd-dmi14-vstop20` leg exits through a VSTOP trail rather than the reverse crossover; the admitted `waddah-attar-explosion-macd-bb` system fires on MACD/BB deadzone explosion, not on a signal-line cross; the admitted `forven-ema-cross-adx-regime` sibling shares only the ADX-plus-EMA200 gate idiom over a first-order price-average cross (different signal series, different seed dynamics, different market); the admitted `forven-dema-cross` / `forven-tema-cross` / `forven-hma-cross` siblings cross smoothed price averages, never a second-order oscillator pair; the pool's `slow-stochastic-14-3-regime-recross` and `kdj-golden-cross` records trade range-position level events and J×D line crosses, never MACD rotation. Not a re-tuning of any of them: swapping the oscillator family, any period, the ADX threshold, the regime length, the strictness, the exit, or the direction handling would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the ETHUSDT-`1h` market choice, the same-bar-close fills, the position-state plus 200-bar warmup pins, and house sizing/costs — all predeclared above; the 5/13/3/200/14/20 set, the span-smoothed ADX chain, the strict cross/regime boundaries, the unconditional cross-down exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 5/13/3 periods, the ADX 14/20 pair, the strict cross/regime boundaries, the unconditional exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning any period or threshold, converting the ADX/regime conjunction to a disjunction, gating the exit, adding a stop/target/filter/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 5/13/3/200/14/ADX20 / strict boundaries / unconditional cross-down exit / single-unit long-only / `1h` ETHUSDT / same-bar-close fills / 200-bar warmup are frozen.

- F1 — ADX relevance: dropping the ADX leg (plain rotation plus regime gate, exit unchanged) must not improve net expectancy; fail ⇒ the strength veto adds nothing over the rotation-plus-regime machine.
- F2 — Regime relevance: dropping the EMA200 leg (plain rotation plus ADX gate, exit unchanged) must not improve net expectancy; fail ⇒ the regime veto adds nothing over the rotation-plus-strength machine.
- F3 — Exit relevance: replacing the cross-down exit with a close-below-EMA200 regime exit (same gated entries, same guard/pins) must not improve net expectancy; fail ⇒ the momentum-recross exit adds nothing over a regime-loss exit.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue ETHUSDT perpetual `1h` completed bars with standard high/low/close prints (the rule reads `close` for averages/rotation/regime/cross plus `high`/`low` inside the ADX/ATR helpers — no `open`, no `volume` dependency at all). No session calendar (crypto trades continuously; the two-bar cross needs no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every shift-1 reference is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `3.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no length guard: the 200-bar warmup is a disclosed researcher pin. Pre-warmup seeding behaviour (Negative evidence 1) is fenced flat, never evaluated.
- The source ships no costs and no position semantics: all economics come from the house overlay, and single-unit/hold-no-op bookkeeping is a predeclared researcher pin (SQZMOM-LB / volatility-contraction-breakout precedent), never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- ADX span-smoothing variant (Negative evidence 2); diagnostic-only confidence/ATR echo (Negative evidence 3); unread regime metadata (Negative evidence 4).
- The `parameter_space` optimizer ranges are in-file metadata — disclosed; the rule reads only `default_params` keys and exercises no search range.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only. (The pool's naked-cross MACD cousin is a two-sided daily reversal system with its own evidence — cited as that record's evidence, not this rule's; this gated long-flat rule's expectancy is unmeasured.)

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/macd.py
- https://github.com/judder659/Forven
