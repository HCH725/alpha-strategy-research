---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven OBV EMA-cross SMA-gated long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/obv_trend.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven OBV EMA-cross SMA-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, `forven-bb-edge-fade-reclaim`, and `forven-rsi-s00139-washout-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T13:50:18-03:00`; verified as the repository HEAD via `git ls-remote` and a full shallow clone during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/obv_trend.py`.
- GitHub blob SHA at the pinned commit: `7eedebf0acbae61f6d8686e07be83103011b4d56`, size 3125 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit and from the clone at the pinned HEAD is 3125 bytes, 107 lines, SHA-256 `eb20c4bcbcf45ab9b543ab644ce119bff3ac6e68c2ea67ca08183a39122d058e`, identical to the GitHub blob (`git hash-object` reproduces `7eedebf0…b4d56`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = OBVTrendStrategy` and the `STRATEGIES = [("PREBUILT-OBV", OBVTrendStrategy, {"_asset": "BTC"})]` roster pin. This record pins the `PREBUILT-OBV` roster leg. Repo-wide search for `OBVTrendStrategy` / `PREBUILT-OBV` / `obv_trend` returns this file only for signal logic — identity is unique (the only other `obv_trend` hits are the framework's `params.py` category/allowlist lines, which name the family and tolerate legacy alias keys but contain no decision logic).
- The file's own words (quoted for gate evidence, never extended): module docstring `OBV Trend strategy - On-Balance Volume with EMA crossover.`; class docstring `Entry: OBV crosses above its EMA AND close > SMA(close, sma_period).` with `Exit: OBV crosses below its EMA.`; `default_params` returns exactly `{ "ema_period": 20, "sma_period": 20, "leverage": 1.0 }`; `describe()` returns `Enters when OBV crosses above its 20-bar EMA and close > 20-bar SMA. Exits when OBV crosses below EMA.` No performance phrase of any kind ships anywhere in the 107 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path (verified by `def` census): the file defines one signal method, `generate_signal()` — no `generate_signals` vectorized twin exists anywhere in the file, no scalar delegate, no second decision logic exists to diverge. The `confidence` value (`0.7` on entry bars, else `0.0`) and the `indicators` dict (`obv`, `obv_ema`, `sma_close`, `above_sma`) are diagnostic echoes — none ever enters any predicate.
- No out-of-file indicator imports: OBV is computed inline with `numpy.sign` over `close.diff()` times `volume` (cumsum), the OBV average with pandas `ewm(span=20, adjust=False)`, and the price gate with a trailing `rolling(20).mean()` — all in-file pandas/numpy over passed frames (no DB, no network, no global state). The only local import is the `BaseStrategy, Signal` base. No facade, no scanner passenger, no hidden arithmetic variant exists to pin.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-bb-edge-fade-reclaim` and `forven-rsi-s00139-washout-cross` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` normalization of both flags and the direction literal. The base further pins `supported_trade_modes == {"long_only"}` and `mirror_short_safe == False` — the long-only lane below is the class's own declared posture, not a researcher reinterpretation.
- Full-file token census (verified by search over the 107 lines this cycle): 4 `direction="long"` literals and zero `short` / zero `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind — unlike the S00139 sibling there is not even dead stop code to fence); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line; 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal). The only `high`/`low` substrings in the file are the English words inside the `crosses below` docstring/describe sentences — no `high`/`low` OHLC column is ever read. The order-gating path reads exactly two columns: `close` and `volume`.
- Param-alias fence (verified in `params.py` at the pinned commit): the framework allowlist names `obv_trend` with accepted keys `{"obv_ema_period", "signal_period", "ema_period", "sma_period"}` and passes unknown params through without enforcement. The predicate below reads only `p["ema_period"]` / `p["sma_period"]` (both present in defaults); the alias keys never enter any predicate — treating them as live parameters would be a different, unpinned rule.

Pre-write dedup (2026-10-19): working-tree filename/content search for `obv_trend` / `OBVTrendStrategy` / `PREBUILT-OBV` returns zero strategy records citing this source file. No closed `research/*` PR ever carried this file (merged Scout PRs #270–296 are WorldQuant/PVI/Mayer/PGO/Caporale-Plastun/wick/Ehlers/Caporale and twenty-six Forven files through S00139 #296). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. The pool's nearest volume-flow neighbours are fenced as different constructions in Negative evidence 8 — none trades textbook Granville OBV against its own EMA(20) with an SMA(20) price gate, long-only, signal-exits-only. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `On-Balance Volume trend strategy` that buys when cumulative signed-volume flow turns up through its own average while price holds above its mean, and exits when flow turns back down through the average. No behavioural, structural, or risk-premium channel is claimed anywhere in the 107 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Accumulation-confirmation machine with a price leash, long-only, edge-triggered both legs. Unlike price-cross records (ema-20-50, dema-cross: averages of price crossing averages of price — blind to participation), this system never fires on a price wiggle alone: the OBV leg requires signed volume to have actually accumulated through its own 20-bar average, so breakouts on collapsing participation print nothing. Unlike the pool's ATR-scaled OBV record (volume-squared-over-ATR cum crossed 6-over-24, two-sided with a 3% stop), this system cumulates raw signed volume one-for-one (Granville form — a steady drip of small up-volume days drags the line just as a single spike does) and smooths once (EMA20, not a fast-over-slow pair), so slow institutional-style accumulation that never spikes any scaled oscillator still crosses. The SMA(20) gate is the sole capital guardrail in a file with zero risk legs: flow may turn, but if the close is still buried under its mean, no entry prints. The coded consequence is a patient participation buyer: entries print only on bars where flow proves itself reversed AND price has already recovered trend position, and every position ends on a single flow-failure edge.

## Signal

Exact rule as pinned (any other OBV construction, average length, gate length, strictness, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path is the single source of truth:

```text
obv[t]     = cumsum(sign(close[i] - close[i-1]) * volume[i])   // Granville, i = 1..t; NaN diff skipped
obv_ema[t] = ewm(span=20, adjust=False).mean() over obv
sma20[t]   = mean(close[t-19 .. t])
entry      = (obv[t-1] <= obv_ema[t-1]) AND (obv[t] > obv_ema[t]) AND (close[t] > sma20[t])
exit_      = (obv[t-1] >= obv_ema[t-1]) AND (obv[t] < obv_ema[t])
guard      = len(df) < 22 -> flat/flat by coded rule (see Required data)
```

- Trade events: `entry_signal=True` with `direction="long"` on flow-cross-plus-price bars; otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. Both legs are EDGES (fire only on the cross bar) — there is no level-hold leg anywhere: a book parked under the average without a fresh cross holds, it does not re-exit.
- Exact boundaries (pinned semantics): both crosses admit equality on the prior bar (`<=` / `>=`) but demand strict inequality on the current bar (`>` / `<`) — a print landing exactly on its average fires nothing. Entry needs price STRICTLY above the SMA (`>` — a close landing exactly on the average fires nothing). At zero variance (all-equal closes, all-zero volumes) OBV pins flat at its seed and the averages coincide — strictness makes entry impossible and exit false by construction (fenced, not repaired).
- Both-legs coexistence (coded, no researcher ordering needed): entry and exit are mutually exclusive by strictness — the current bar cannot print OBV both strictly above AND strictly below its average. No priority rule can ever fire; no same-bar dual-fire sequencing is left to any engine.
- Direction: long-only with an explicit pre-first-signal flat state plus the coded guard flat. Zero `short`/`sell` tokens ship anywhere; the base class pins `supported_trade_modes == {"long_only"}` and `mirror_short_safe == False` — a two-sided reading would contradict the file and its base. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the OBV cross-down is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent from the file in every form (0 `stop` / 0 `limit` / 0 `profit` / 0 `trail` tokens — not even dead code) and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`0.7` on entry bars, else `0.0`) and the `indicators` dict are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats further entry-only bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit-only legs as no-ops; re-entry re-arms on any qualifying flow-cross bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and guard bars are flat by coded/record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` and `volume` with fixed non-negative offsets — no `high`/`low`/`open`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above). The OBV cumsum skips the single leading-`NaN` diff by pandas `skipna` convention and the averages use trailing windows — deterministic given the pinned pandas/numpy semantics. The `compatible_regimes` set (`{"TREND_UP"}`) is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close` and `volume` ONLY — textbook OBV over signed close-changes times volume for the flow path, plus the 20-bar price SMA for the gate. No bar `open`/`high`/`low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; both windows (the 20-bar EMA/SMA seeds, the one-bar cross edge lookback) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard (`len(df) < max(ema_period, sma_period) + 2`, i.e. 22 bars at defaults). This record adopts a 22-bar record-rule warmup with pre-warmup bars flat (no derivation — the coded guard already holds them flat with `entry=False, exit=False`): at 22+ bars the SMA seed (20), the OBV-EMA seed (20 over a cumsum valid from bar 1), and the one-prior-bar edge read are all defined. Before that, `NaN` comparisons are `False` by construction, so no leg can fire early — coded behaviour, disclosed. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-OBV` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-six admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and both legs are mutually exclusive edges (see Signal) — no ambiguous same-bar fill order is left to the engine.
- Volume faithfulness (declared): the flow leg reads the venue's own completed-bar `volume` prints — the same field the admitted `forven-atr-volume-breakout` sibling already gates on. No rebased, normalized, or cross-venue volume enters any predicate; a venue printing different volume prints different events by construction, disclosed.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; flow-cross bars while positioned hold without adds; the cross-down leg closes the open side in full; re-entry after an exit needs only the next qualifying flow-cross bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (107 lines: module docstring with the OBV-crossover rule, `default_params` with the 20/20 set, the SMA gate, the strict flow-cross entry, the mirror cross-down exit, the `direction="long"` literals and the `round(curr_close, 4)` price echo, the `PREBUILT-OBV` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard behaviour fenced: before the 22nd bar the coded guard returns flat/flat; leading-`NaN` legs compare false by construction, so every pre-warmup bar is flat twice over — disclosed, not repaired. A shorter warmup would admit `NaN`-flat bars only (never spurious events), but the 22-bar floor is still pinned so the first trusted bar has fully defined windows.
2. Exact-touch rule fenced: prints landing exactly on their averages fire nothing on either leg (strict current-bar inequality both sides); a close landing exactly on the SMA is NEITHER above (no entry) NOR an exit condition (the exit leg reads flow only) — it holds by strictness. Strictness is preserved throughout — disclosed, not smoothed.
3. Below-average loiter fenced: while positioned with OBV parked below its EMA WITHOUT a fresh cross (entered earlier, flow drifted down gradually), the exit leg stays false — only a fresh cross-down bar ends the position. There is no level-hold exit by construction; a slow bleed that never prints a qualifying cross bar rides in full — disclosed, not repaired. Mirror-wise, while flat with OBV parked above its EMA, no entry can fire without a fresh cross-up bar.
4. Zero-participation fenced: an all-zero-volume tape pins OBV flat at seed with coinciding averages — strictness admits no event on either leg. A tape of all-equal closes zeroes every diff with the same consequence. No division exists anywhere in the signal path, so no undefined arithmetic can arise — disclosed, not repaired.
5. Confidence/indicators diagnostic fenced: `confidence` and the full `indicators` dict never enter any predicate — an engine that skips computing all of them reaches identical events.
6. Param-alias surface fenced: the framework allowlist tolerates `obv_ema_period` / `signal_period` keys, but the predicate reads only `ema_period` / `sma_period` — passing the aliases changes no event. An implementation that re-wires the average length through an alias would be a different, unpinned rule — none is admitted here.
7. Spot-expression fenced: the long-only, no-stop, edge-exit book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both. The short side is explicitly disabled, never merely untested.
8. Cousin records fenced as different constructions (none trades textbook Granville OBV against its own EMA(20) with an SMA(20) price gate, long-only, signal-exits-only): the pool's `obv-ema-crossover-trend` record cumulates volume-squared-over-ATR(3) (a different series entirely — spike-weighted, not one-for-one) crossed 6-over-24, two-sided with a 3% stop on `1d` bars from FMZ 442252 (different formula, different lengths, different direction handling, different risk, different frame, different source); the admitted `forven-adl-ema-cross` sibling accumulates money-flow-volume ((close-low)-(high-close))/(high-low) — a range-position-weighted flow, not signed-volume flow; the admitted `forven-atr-volume-breakout` sibling trades volume-breakout levels with no cumulative line at all; the admitted `forven-chaikin-mf-threshold-cross` sibling trades a bounded money-flow ratio against a threshold, never a line-cross; the pool's Klinger/PVO/PVT/CMF-velocity records are oscillator/ratio constructions with different triggers and risk; every price-cross record (ema-20-50, dema-cross) reads price only and never volume. Not a re-tuning of any of them: swapping the OBV formula, the EMA/SMA lengths, the gate, the exit, or the direction handling would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, and house sizing/costs — all predeclared above; the 22-bar guard floor is source-verbatim code, not an adoption. The Granville OBV construction, the EMA(20) cross, the SMA(20) gate, the mirror cross-down exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour.
10. The OBV formula, the 20/20 pair, the strict cross edges, the SMA gate, the mirror exit, the long-only stance, and the no-stop stance are pinned, not removed: re-tuning any length, softening strictness to touches, converting an edge to a level (or the reverse), adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Granville OBV / EMA20 cross / SMA20 gate / mirror cross-down exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: dropping the SMA gate (pure OBV cross-up entry, same exit) must not improve net expectancy; fail ⇒ the coded price gate adds nothing over its ungated twin.
- F2 — Exit relevance: replacing the flow cross-down exit with a close-under-SMA exit (same entry) must not improve net expectancy; fail ⇒ the flow-failure leg adds nothing over the trend-loss leg.
- F3 — Series relevance: trading the identical gate-plus-cross structure on the ADL money-flow-volume series (same lengths/entry/exit/pins, Granville OBV replaced) must not reproduce-or-beat net expectancy; fail ⇒ the signed-volume construction adds nothing over its range-weighted twin and the record is a label variant of the admitted `forven-adl-ema-cross` sibling.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with `close` and `volume` fields only. No session calendar (crypto trades continuously; the 20-bar seeds and the one-bar edge lookback need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics: single-unit bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- The file ships no risk leg in any form (verified zero tokens): the exits-only posture is source-verbatim effective behaviour, but any downstream evaluation must carry the full unprotected long-flat book, not an assumed stop.
- Flow bleeds that never print a fresh cross-down bar ride in full (Negative evidence 3); washouts in flow that recover without price recovering the SMA never trade.
- Volume-print differences across venues shift the OBV series and hence events; this record claims only the venue's own prints.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/obv_trend.py
- https://github.com/judder659/Forven
