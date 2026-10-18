---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven KDJ dual-gate J-zero plus KD-cross long-flat on BTCUSDT 1h bars
created: 2026-10-18
updated: 2026-10-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/kdj.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven KDJ dual-gate J-zero plus KD-cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, and `forven-connors-rsi-oversold-recross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/kdj.py`.
- GitHub blob SHA at the pinned commit: `e95505e9fcbd9dacd0ea622f6880fc6e452ee3d4`, size 3777 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3777 bytes, 133 lines, SHA-256 `93865bc704f1ea913729d6000584a2e80005092a035f647c5e1549782e5596bd`, identical to the GitHub blob (`git hash-object` reproduces `e95505e9…452ee3d4`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = KDJStrategy` (line 129), `TYPE_NAME = "kdj"` (line 15), and the `STRATEGIES = [("PREBUILT-KDJ", KDJStrategy, {"_asset": "BTC"})]` roster pin (lines 131–133). This record pins the `PREBUILT-KDJ` roster leg.
- The file's own words (quoted for gate evidence, never extended): module docstring `K = SMA(RSV, k_smooth) where RSV = (close - lowest_low) / (highest_high - lowest_low) * 100`, `D = SMA(K, d_smooth)`, `J = 3*K - 2*D`, `Entry: J crosses above 0 from below AND K crosses above D`, `Exit: J crosses below 100 from above OR K crosses below D`, `Compatible Regimes: RANGE_BOUND, TREND_UP` (lines 1–9); class docstring `Extension of stochastic oscillator with a J line (3K - 2D) that provides early reversal signals.` (lines 19–23); `default_params` returns exactly `{ "k_period": 9, "k_smooth": 3, "d_smooth": 3, "leverage": 1.0 }` (lines 38–44); `describe()` returns `KDJ(9/3/3). Enters when J crosses above 0 and K crosses above D. Exits when J drops below 100 or K crosses below D.` (lines 50–56); `compatible_regimes` returns `{"RANGE_BOUND", "TREND_UP"}` (lines 46–48, metadata never read by the signal path); `parameter_space()` returns `{ "k_period": (5, 14, 1), "k_smooth": (2, 5, 1), "d_smooth": (2, 5, 1) }` (lines 121–126, a documented search surface only — this record pins the defaults and runs no search).
- Single decision path (verified by `def` census): `generate_signal()` (lines 58–119) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the file, no scalar delegate, no second decision logic exists to diverge. All smoothing is inline (`rolling().min/max/mean` at lines 79–86, called exactly once each from the single path). The `confidence` value (lines 104–106) and the three `indicators` fields (`k`, `d`, `j`, lines 114–118) are diagnostic echoes — none ever enters any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion that refuses non-Boolean flags and resolves direction labels (`_normalize_signal_flag`, `_normalize_signal_direction`, lines 140–180) — flags arriving as strict booleans (as here, via `bool(...)` at lines 109–110) pass through unchanged, and the `direction="long"` literal resolves to its book.
- Full-file token census (verified by search over the 133 lines this cycle): 0 `direction="short"` (the single `direction="long"` literals at lines 74 and 112 are the guard default and the signal); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` (no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (the only columns read are `df["close"]` at line 60, `df["high"]` at line 61, `df["low"]` at line 62 — see Signal); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the KDJ(9/3/3) SMA construction, the dual-gate entry (J-zero-cross AND KD-cross), the disjunctive exit (J-hundred-cross OR KD-cross), the long-only book, and the 17-bar guard — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own four comparisons. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, pivot-s1-bounce, volatility-contraction, and connors-rsi records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin (the file carries no position reference; an already-positioned book treats same-side entry bars as hold-no-ops and a flat book treats exit bars as no-ops — pin disclosed, never presented as source-native semantics); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (the file ships no sizing, capital, fee, margin, or funding concept; modeled funding is never reported as realized — the source declares no funding treatment at all).

Pre-write dedup (2026-10-18): working-tree filename/content search for `PREBUILT-KDJ` / `builtin/kdj` returns zero strategy records citing this source file; no closed `research/*` PR ever carried it (merged Scout PRs #270–292 are WorldQuant/PVI/Mayer/PGO/Caporale-Plastun/wick/Ehlers/Caporale and twenty-two other Forven files). The pool's KDJ record is fenced as a different construction in Negative evidence 8 (kdj-golden-cross: FMZ source, bcwsma Wilder-style smoothing, single J-cross-D entry, J>100 level exit — no J-zero gate, no K-cross leg, no SMA construction, different source). The pool's stochastic records (slow-stochastic-14-3, dss-bressert-double-smoothed, stochastic-ott, stoch-rsi-kd-zone) are all %K/%D stochastic constructions with no J line of any kind. The pool's RSI-dip records never compute RSV, K, D, or J. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a dual-gate SMA-KDJ cross machine (J-zero AND KD-cross entry, J-hundred OR KD-cross exit) is a different signal construction from any single-cross stochastic or single-RSI fade — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an extension of the stochastic oscillator with a J line (`3K - 2D`) that provides early reversal signals, entering when J crosses above 0 and K crosses above D, exiting when J drops below 100 or K crosses below D, in ranging or up-trend regimes. No behavioural, structural, or risk-premium channel is claimed anywhere in the 133 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Dual-gate snap-plus-confirmation, long-only, cross-gated. Unlike single-gate stochastics (slow-stochastic: %K crosses %D alone; dss-bressert: smoothed trigger latch alone), this system never trades on one cross — its only tradable voice is the conjunction of a deeply-washed J print snapping back through zero AND a K-over-D confirmation on the same bar, so a J snap with no K confirmation fires nothing, and symmetrically a K cross with J still pinned under zero fires nothing. Unlike the FMZ KDJ cousin (J crossing above D alone, bcwsma-smoothed), the J-zero leg here is an absolute-level gate (0/100 rails), not a relative K/D ordering — a bar where J crosses D mid-range (say 40→50) with no rail cross trades nothing here. Unlike state-hold records (kdj-golden-cross holds while J>D), entries here are pure cross events evaluated per completed bar — a bar that merely sits with J above 0 and K above D with no fresh cross enters nothing. Unlike price-extreme pullbacks (double-seven: fresh 7-close extremes), no rolling price extreme is traded directly — the 9-bar high/low window only normalizes RSV, never fires an order by itself. The coded consequence is a patient machine: the double requirement means entries cluster only on bars where momentum snap (J) and trend confirmation (K/D) agree on the same close.

## Signal

Exact rule as pinned (any other period, smoothing, threshold, boundary, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 58–119) is the single source of truth:

```text
lowest_low   = rolling_min(low, 9)
highest_high = rolling_max(high, 9)
hh_ll        = (highest_high - lowest_low) with exact-0 replaced by 1e-10
rsv          = 100 * (close - lowest_low) / hh_ll
k_line       = SMA(rsv, 3)          // rolling mean, trailing 3 RSV prints
d_line       = SMA(k_line, 3)       // rolling mean, trailing 3 K prints
j_line       = 3 * k_line - 2 * d_line
j_cross_up   = prev_j <= 0   AND curr_j > 0     // J snaps back through zero
k_cross_up   = prev_k <= prev_d AND curr_k > curr_d  // K crosses above D
j_cross_down = prev_j >= 100 AND curr_j < 100   // J falls back under 100
k_cross_down = prev_k >= prev_d AND curr_k < curr_d  // K crosses below D
entry        = j_cross_up AND k_cross_up
exit_        = j_cross_down OR k_cross_down
guard        = fewer than 17 completed bars → flat by source rule
```

- Trade events: `entry_signal=True` with `direction="long"` on dual-gate bars (lines 108–113); otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. Entry and exit can never co-fire (entry needs `prev_j <= 0`, exit's J leg needs `prev_j >= 100`; entry needs K-cross-up, exit's K leg needs K-cross-down — the strict current-bar legs `curr_k > curr_d` vs `curr_k < curr_d` are mutually exclusive even on the `prev_k == prev_d` equality edge) — no ordering pin is needed and none is pretended.
- Exact boundaries (pinned semantics): J-up needs the current print strictly above 0 (`curr_j > 0` — a print landing exactly on 0.0 enters nothing); J-down needs strictly below 100 (`curr_j < 100`); K-up needs strictly above (`curr_k > curr_d`); K-down needs strictly below (`curr_k < curr_d`); the previous-bar legs are inclusive (`<= 0`, `<= prev_d`, `>= 100`, `>= prev_d` — cross semantics, so a tape pinned flat above zero with K above D never entries until a fresh double cross actually prints).
- Direction: long-only with an explicit pre-first-signal flat state plus the 17-bar guard flat. Zero `direction="short"` literals ship anywhere; a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the disjunctive rail-or-confirmation leg is the sole position-ending path (`exit_`, lines 98–102). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min(1.0, (curr_k - curr_d)/20)` on entries, `0.0` elsewhere, lines 104–106) and the three `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops; re-entry re-arms on any qualifying dual-gate bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and guard bars are flat by source rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (rolling 9-bar extremes, two chained 3-bar means, two-bar cross lookbacks); no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule. The `hh_ll` zero-guard (`replace(0, 1e-10)`, line 81) pins the flat-range branch — substituting any other epsilon would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only — for the 9-bar rolling extremes, the RSV normalization, and the chained 3+3 SMA legs. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all windows (rolling-9 extremes, rolling-3 means, two-bar cross lookbacks) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard — `k_period(9) + k_smooth(3) + d_smooth(3) + 2 = 17`, and shorter frames return an explicit all-flat Signal (lines 67–77, via `Signal(price=…, direction="long")` defaults `entry_signal=False, exit_signal=False`). The 17-bar floor covers the 9-bar extreme window, both 3-bar SMA seeds, and the two-bar cross lookback. The record adopts this guard verbatim as its flat rule — no researcher warmup pin is needed and none is pretended. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-KDJ` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-two admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; same-side entry bars hold without adds; any exit-cross bar closes the open side in full; re-entry after an exit needs only the next qualifying dual-gate bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (133 lines: module docstring with the RSV/K/D/J formulas and dual-gate/disjunctive rules, `TYPE_NAME`, `default_params` with the 9/3/3 periods, the rolling-extreme plus chained-SMA chain, the J-zero AND KD-cross entry, the J-hundred OR KD-cross exit, the 17-bar guard, the `direction="long"` literals and the `round(curr_close, 4)` price echo, the `PREBUILT-KDJ` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard/NaN behaviour fenced: inside the guard every early `NaN` (rolling-9 `min/max` seeds, rolling-3 `mean` seeds) compares `False` against all four cross predicates, so pre-guard bars are doubly flat — by guard rule and by NaN semantics. Disclosed, not repaired.
2. Flat-range guard fenced: a tape with identical high/low prints over the 9-bar window pins `highest_high - lowest_low → 1e-10` (line 81) and RSV at `100 * (close - lowest_low) / 1e-10` — deterministic, no divide-by-zero branch; on a perfectly flat tape (`close == lowest_low`) RSV pins at exactly 0.0 and the J/K/D legs rest deterministically, never into a spurious dual-gate cross. Disclosed, not repaired.
3. Exact-touch rules fenced: a J print landing exactly on 0.0 enters nothing (`curr_j > 0` strict); a J print landing exactly on 100.0 exits nothing (`curr_j < 100` strict); K needs strict `>`/`<` against D on the current bar; a tape resting with J above 0 and K above D with no fresh cross never entries (`prev <=` legs alone are insufficient). Strictness is preserved throughout — disclosed, not smoothed.
4. Co-fire impossibility fenced: entry needs `prev_j <= 0` AND K-cross-up, exit needs (`prev_j >= 100` AND J-down) OR K-cross-down — no bar satisfies an up leg and a down leg simultaneously (the J-leg previous bars `<= 0` vs `>= 100` are disjoint; the K-leg current bars `curr_k > curr_d` vs `curr_k < curr_d` are strictly exclusive even when `prev_k == prev_d`), so the single return statement (lines 108–113) never faces a both-legs-true bar. No tiebreak exists to specify.
5. Confidence diagnostic fenced: the entry-only `min(1.0, (curr_k - curr_d)/20)` never enters any predicate — an engine that skips computing confidence reaches identical events. The three indicator echoes duplicate the predicate values and likewise change no event when skipped.
6. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
7. Smoothing basis fenced: both smoothings are plain trailing SMA (`rolling().mean()`), pinned as written — substituting Wilder/bcwsma/EMA weighting would be a different, unpinned rule (see cousin fencing next).
8. Cousin records fenced as different constructions (none trades a dual-gate SMA-KDJ cross): the admitted kdj-golden-cross sibling trades a single J-cross-D edge with bcwsma Wilder-style smoothing and a J>100 level exit off an FMZ source (no J-zero rail gate, no K-cross leg, different smoothing math, different source); the admitted slow-stochastic-14-3 sibling trades %K/%D recrosses with no J line at all; the dss-bressert sibling trades a double-smoothed trigger latch with no J line; the stochastic-ott sibling trades OTT-dual-trend with no RSV/K/D/J chain; the pool's RSI-dip records (catching-the-bottom, rsi-classic, cumulative-rsi, forven-ema-rsi-pullback) are single-RSI level or EMA-gated constructions with no RSV normalization and no K/D/J legs. Not a threshold re-tuning of any of them.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, and house sizing/costs — all predeclared above; the 9/3/3 periods, the SMA (not Wilder) smoothing, the 0/100 rails, the strict boundaries, the dual-gate entry, the disjunctive exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 9/3/3 periods, the SMA smoothing, the 0/100 rails, the AND-gated entry, the OR-gated exit, the long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning any period, converting crosses to state holds, dropping either entry gate, dropping either exit leg, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: KDJ(9/3/3 SMA) / 0-100 rails / strict boundaries / dual-gate entry / disjunctive exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Dual-gate relevance: replacing the dual-gate entry (J-zero-cross AND KD-cross) with the J-zero-cross leg alone (same exit) must not improve net expectancy; fail ⇒ the K-cross confirmation adds nothing over lone-J snapping.
- F2 — Exit-disjunction relevance: replacing the disjunctive exit (J-hundred-cross OR KD-cross) with the KD-cross leg alone must not improve net expectancy; fail ⇒ the J-hundred rail exit adds nothing over lone-KD reversal exits.
- F3 — Cross relevance: replacing the dual cross-up entry (`prev <=` AND `curr >`) with the state entry (`curr_j > 0` AND `curr_k > curr_d` on every qualifying bar) must not improve net expectancy; fail ⇒ waiting for the fresh double cross adds nothing over buying every doubly-raised bar.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with the `high`/`low`/`close` fields only. No session calendar (crypto trades continuously; the 9-bar extreme window and 3-bar SMA seeds need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every window bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics: single-unit bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Flat-range `1e-10` guard and exact-touch holds as fenced (Negative evidence 2–3); `compatible_regimes` is display metadata only.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/kdj.py
- https://github.com/judder659/Forven
