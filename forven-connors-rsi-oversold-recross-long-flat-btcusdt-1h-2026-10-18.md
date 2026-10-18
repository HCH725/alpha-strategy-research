---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Connors RSI composite oversold-recross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/connors_rsi.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Connors RSI composite oversold-recross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, and `forven-volatility-contraction-breakout` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/connors_rsi.py`.
- GitHub blob SHA at the pinned commit: `3b629f931005117c176676fcf3b93206808011d2`, size 4930 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4930 bytes, 161 lines, SHA-256 `3385f4dd782cec8fa7df6ed8050d19b093cdf5423dd64d873cded5c114d0660d`, identical to the GitHub blob (`git hash-object` reproduces `3b629f93…08011d2`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = ConnorsRSIStrategy` (line 157), `TYPE_NAME = "connors_rsi"` (line 14), and the `STRATEGIES = [("PREBUILT-CONNORS-RSI", ConnorsRSIStrategy, {"_asset": "BTC"})]` roster pin (lines 159–161). This record pins the `PREBUILT-CONNORS-RSI` roster leg.
- The file's own words (quoted for gate evidence, never extended): module docstring `Connors RSI strategy.` with `CRSI = (RSI(close, n) + RSI(streak, n) + PercentRank(ROC, n)) / 3`, `Entry: CRSI crosses above oversold`, `Exit: CRSI crosses below overbought`, `Compatible Regimes: RANGE_BOUND` (lines 1–7); class docstring `Connors RSI mean-reversion strategy. CRSI averages three components: standard RSI, streak RSI, and percent rank of rate of change to identify short-term reversals.` (lines 55–59); `default_params` returns exactly `{ "rsi_period": 3, "streak_period": 2, "rank_period": 100, "oversold": 10, "overbought": 90, "leverage": 1.0 }` (lines 74–82); `describe()` returns `Connors RSI(3/2/100). Enters when CRSI crosses above 10; exits when CRSI crosses below 90.` (lines 88–94); `compatible_regimes` returns `{"RANGE_BOUND"}` (lines 85–86, metadata never read by the signal path); `parameter_space()` returns `{ "rsi_period": (2, 5, 1), "streak_period": (2, 4, 1), "rank_period": (50, 150, 25), "oversold": (5, 20, 5), "overbought": (80, 95, 5) }` (lines 147–154, a documented search surface only — this record pins the defaults and runs no search).
- Single decision path (verified by `def` census): `generate_signal()` (lines 96–145) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the file, no scalar delegate, no second decision logic exists to diverge. All three component helpers (`_rsi` lines 17–25, `_streak` lines 28–39, `_percent_rank` lines 42–51) are file-local and called exactly once each from the single path. The `confidence` value (lines 129–131, 138) and the four `indicators` fields (`crsi`, `rsi_close`, `rsi_streak`, `pct_rank`, lines 139–144) are diagnostic echoes — none ever enters any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion that refuses non-Boolean flags and resolves direction labels (`_normalize_signal_flag`, `_normalize_signal_direction`, lines 140–180) — flags arriving as strict booleans (as here, via `bool(...)` at lines 134–135) pass through unchanged, and the `direction="long"` literals resolve to their book.
- Full-file token census (verified by search over the 161 lines this cycle): 0 `direction="short"` (the single `direction="long"` literals at lines 106 and 137 are the guard default and the signal); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` (no order arguments, no risk legs of any kind — the four `loss` hits are the RSI gain/loss identifiers at lines 18/21/23/24 only); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (the only column read is `df["close"]` at line 98 — see Signal); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the CRSI(3/2/100) composite, the 10/90 cross thresholds, the long-only book, the overbought-cross exit, and the 105-bar guard — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own two comparisons. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, pivot-s1-bounce, and volatility-contraction records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin (the file carries no position reference; an already-positioned book treats same-side entry bars as hold-no-ops and a flat book treats exit bars as no-ops — pin disclosed, never presented as source-native semantics); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (the file ships no sizing, capital, fee, margin, or funding concept; modeled funding is never reported as realized — the source declares no funding treatment at all).

Pre-write dedup (2026-10-18): working-tree filename/content search for `connors_rsi` / `PREBUILT-CONNORS` returns zero strategy records citing this source file; no closed `research/*` PR ever carried it (merged Scout PRs #270–291 are WorldQuant/PVI/Mayer/PGO/Caporale-Plastun/wick/Ehlers/Caporale and twenty-one other Forven files). The pool's Connors-adjacent records are fenced as different constructions in Negative evidence 8 (connors-rsi2-ma70-fade: single RSI(2) state vs a 70-bar average, two-sided, FMZ source — no streak leg, no percent-rank leg, no cross events; double-seven-connors-pullback: MA200 regime plus 7-close minimum/maximum pullback levels, FMZ source — no oscillator of any kind). The pool's other RSI-dip records (catching-the-bottom, oversold-rsi-tight-sl, rsi-classic-level-reversal, cumulative-rsi-dual-threshold, forven-ema-rsi-pullback-reclaim) are all single-RSI level or EMA-gated constructions — none computes the three-component CRSI with a streak-RSI leg and a ROC percent-rank leg. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a three-component composite-oscillator cross machine is a different signal construction from any single-RSI level fade or price-extreme pullback — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: short-term reversals are identified by averaging three components — standard RSI, streak RSI, and percent rank of rate of change — entering when the composite crosses above oversold and exiting when it crosses below overbought, in a ranging regime. No behavioural, structural, or risk-premium channel is claimed anywhere in the 161 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Composite-oscillator snap-back, long-only, cross-gated. Unlike single-RSI dip records (rsi-classic: one RSI(14) against fixed levels; catching-the-bottom: RSI dip plus price shape), this system never reads a lone RSI print — its only tradable voice is the mean of three legs, so a deep RSI(close) washout with no streak persistence and no ROC-rank confirmation cannot fire, and symmetrically a streaky tape with a calm RSI(close) cannot fire. Unlike state-hold records (connors-rsi2-ma70: long while `CLOSE < ma70 AND RSI2 < 10`), entries here are pure cross events evaluated per completed bar — a bar that merely sits under 10 with no upward cross enters nothing. Unlike price-extreme pullbacks (double-seven: fresh 7-close low/high prints), no rolling price extreme appears anywhere — the rank leg ranks momentum (ROC), never price. The coded consequence is a patient machine: the 100-bar percent-rank leg moves slowly, so entries cluster only after genuinely washed-out tapes where all three legs agree the snap has started.

## Signal

Exact rule as pinned (any other period, threshold, boundary, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 96–145) is the single source of truth:

```text
rsi_c    = 100 - 100/(1 + rs screen), rs = ewm_gain/ewm_loss of close diffs,
           ewm(alpha=1/3, min_periods=3, adjust=False); exact-zero avg_loss → 1e-10
streak   = loop over close diffs: diff>0 → max(prev,0)+1; diff<0 → min(prev,0)-1; diff==0 → 0
rsi_s    = same ewm-RSI construction with period 2 applied to the streak series
roc1     = 100 * (close - close.shift(1)) / close.shift(1)
prank    = PercentRank(roc1, 100): 100 * (# of prior 99 roc prints strictly below current) / 99
crsi     = (rsi_c + rsi_s + prank) / 3.0
entry    = prev_crsi <= 10 AND curr_crsi > 10      // cross up through oversold
exit_    = prev_crsi >= 90 AND curr_crsi < 90      // cross down through overbought
guard    = fewer than 105 completed bars → flat by source rule
```

- Trade events: `entry_signal=True` with `direction="long"` on cross-up bars (lines 133–137); otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. Entry and exit can never co-fire (entry needs `prev <= 10`, exit needs `prev >= 90`) — no ordering pin is needed and none is pretended.
- Exact boundaries (pinned semantics): entry needs the current print strictly above 10 (`curr > 10` — a print landing exactly on 10.0 enters nothing); exit needs the current print strictly below 90 (`curr < 90`); the previous-bar legs are inclusive (`<= 10`, `>= 90` — cross semantics, so a tape pinned flat under 10 never entries until it actually ticks up through the line).
- Direction: long-only with an explicit pre-first-signal flat state plus the 105-bar guard flat. Zero `direction="short"` literals ship anywhere; a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the overbought-cross leg is the sole position-ending path (`exit_`, lines 127/135). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min(1.0, (10 - prev + 10)/20)` on entries, `0.0` elsewhere, lines 129–131) and the four `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops; re-entry re-arms on any qualifying cross-up bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and guard bars are flat by source rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (diffs, ewm seeds, the shift-1 ROC, rolling windows); no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only — for the RSI(3) ewm legs, the streak loop, the 1-bar ROC, and the 100-bar percent-rank window. No `open`-series read, no `high`/`low` read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all windows (diffs, `shift(1)`, rolling-100, ewm seeds) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard — `max(rsi_period=3, streak_period=2, rank_period=100) + 5 = 105`, and shorter frames return an explicit all-flat Signal (lines 99–109, via `Signal(price=…, direction="long")` defaults `entry_signal=False, exit_signal=False`). The 105-bar floor covers the percent-rank window, the ewm `min_periods` seeds, and the two-bar cross lookback. The record adopts this guard verbatim as its flat rule — no researcher warmup pin is needed and none is pretended. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-CONNORS-RSI` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-one admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; same-side entry bars hold without adds; any exit-cross bar closes the open side in full; re-entry after an exit needs only the next qualifying cross-up bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (161 lines: module docstring with the CRSI formula and cross rules, `TYPE_NAME`, `default_params` with the 3/2/100 periods and 10/90 thresholds, the streak/percent-rank helpers, the cross-up entry, the cross-down exit, the 105-bar guard, the `direction="long"` literals and the `round(curr_close, 4)` price echo, the `PREBUILT-CONNORS-RSI` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard/NaN behaviour fenced: inside the guard every early `NaN` (ewm `min_periods`, rolling-100 `min_periods`, leading `diff`/`shift` nulls) compares `False` against both thresholds, so pre-guard bars are doubly flat — by guard rule and by NaN semantics. Disclosed, not repaired.
2. Zero-loss flooring fenced: a tape with no down-diffs over the ewm seed pins `avg_loss → 1e-10` and the RSI leg at exactly 100.0 (line 24) — deterministic, no divide-by-zero branch, and it pushes the composite up (away from entries), never into a spurious oversold cross. A perfectly flat close tape resets `streak` to 0 every bar (line 38) — deterministic, disclosed.
3. ROC division fenced: `roc` divides by `close.shift(1)` with no zero guard (line 114) — a zero print in the prior close would yield `inf`/`NaN`; BTC spot/perpetual closes are strictly positive, so the branch is unreachable on the pinned market. Disclosed, not repaired.
4. Exact-touch rules fenced: a CRSI print landing exactly on 10.0 enters nothing (`curr > 10` strict); a print landing exactly on 90.0 exits nothing (`curr < 90` strict); a tape resting flat under 10 with no upward tick never entries (`prev <= 10` alone is insufficient). Strictness is preserved throughout — disclosed, not smoothed.
5. Co-fire impossibility fenced: entry needs `prev_crsi <= 10`, exit needs `prev_crsi >= 90` — no bar satisfies both, so the single return statement (lines 133–137) never faces a both-legs-true bar. No tiebreak exists to specify.
6. Confidence diagnostic fenced: the entry-only `min(1.0, (10 - prev + 10)/20)` never enters any predicate — an engine that skips computing confidence reaches identical events. The four indicator echoes duplicate the predicate values and likewise change no event when skipped.
7. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Cousin records fenced as different constructions (none trades a three-component CRSI cross): the admitted connors-rsi2-ma70 sibling trades single-RSI(2)-vs-MA70 state persistence two-sided off an FMZ Pine source (no streak leg, no percent-rank leg, no cross events, different source); the admitted double-seven-connors-pullback sibling trades MA200-regime plus fresh 7-close minimum/maximum price prints off an FMZ source (no oscillator of any kind); the admitted forven-ema-rsi-pullback sibling reclaims an EMA with a single RSI confirmation on SOL (no composite, no rank window); the pool's remaining RSI-dip records are single-RSI level fades with no streak and no ROC-rank construction. Not a threshold re-tuning of any of them.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, and house sizing/costs — all predeclared above; the 3/2/100 periods, the 10/90 cross thresholds, the strict boundaries, the long-only stance, the overbought-cross exit, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 3/2/100 periods, the 10/90 thresholds, the cross (not state) construction, the long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning any period, converting crosses to state holds, adding a stop/target/filter/cooldown/gate, adding a short leg, dropping the streak or rank legs, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CRSI(3/2/100) / 10-90 crosses / strict boundaries / overbought-cross exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Composite relevance: replacing the three-leg CRSI with the RSI(close,3) leg alone (same 10/90 cross rules and exit) must not improve net expectancy; fail ⇒ the streak and percent-rank legs add nothing over lone-RSI dip-crossing.
- F2 — Exit relevance: replacing the overbought-cross exit with a fixed 10-bar time exit must not improve net expectancy; fail ⇒ the 90-cross profit-taking rule adds nothing over a fixed lifespan.
- F3 — Cross relevance: replacing the cross-up entry (`prev <= 10 AND curr > 10`) with the state entry (`curr < 10` on every bar under the line) must not improve net expectancy; fail ⇒ waiting for the upward tick adds nothing over buying every washed-out bar.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with the `close` field only. No session calendar (crypto trades continuously; the 100-bar rank window and ewm seeds need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every window bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics: single-unit bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- ROC zero-division unguarded in code (Negative evidence 3); exact-touch holds (Negative evidence 4).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/connors_rsi.py
- https://github.com/judder659/Forven
