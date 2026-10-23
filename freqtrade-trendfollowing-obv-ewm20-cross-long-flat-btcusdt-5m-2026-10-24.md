---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade TrendFollowing OBV-confirmed EWM20-cross long-flat on BTCUSDT 5m bars
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/TrendFollowingStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade TrendFollowing OBV-confirmed EWM20-cross long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-multima`, `freqtrade-hlhb`, `freqtrade-quickie`, `freqtrade-strategy001` through `freqtrade-strategy005`, `freqtrade-cofibit`, and `freqtrade-emaskippump` records at this same pin — this record pins ONLY the TrendFollowingStrategy literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/TrendFollowingStrategy.py`.
- GitHub blob SHA at the pinned commit: `e14f23ddf1a2bdd003f55fa45430492019be39cb`, size 2441 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2441 bytes, 69 lines, SHA-256 `6b8f3e272acfd4923539120364b9ddceccc17a385117d12a249dc1460ea53c4f`, identical to the GitHub blob (`git hash-object` reproduces `e14f23dd…b39cb`) — the entire file was retrieved and inspected.
- Registration: the file defines class `TrendFollowingStrategy(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long` plus the scoped-out `enter_short` / `exit_short` columns, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. The `futures/` directory is a folder location only — the file sets no `trading_mode`, no `can_short`, and no leverage, so it carries no futures-margin semantics of its own.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "5m"`; `minimal_roi = {"0": 0.15, "30": 0.1, "60": 0.05}`; `stoploss = -0.265`; `trailing_stop = True`, `trailing_stop_positive = 0.05`, `trailing_stop_positive_offset = 0.1`, `trailing_only_offset_is_reached = False`; entry `enter_long` is the three-way AND of `close > trend`, `close.shift(1) <= trend.shift(1)`, `obv > obv.shift(1)`; signal exit `exit_long` is the three-way AND of `close < trend`, `close.shift(1) >= trend.shift(1)`, `obv > obv.shift(1)`; indicators are exactly `ta.OBV(dataframe['close'], dataframe['volume'])` and `dataframe['close'].ewm(span=20, adjust=False).mean()`. No performance phrase of any kind ships anywhere in the 69 lines — this record adopts no source-reported performance (see Evidence).
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.OBV(close, volume)` (TA-Lib abstract on-balance volume over the two named columns — the ONLY volume read in the file); pandas `ewm(span=20, adjust=False).mean()` over `close` (the ONLY smoothing in the file); pandas `.shift(1)` backward edge reads (eight tokens, all one-bar lags — no forward reference); `.loc` boolean assignment (pure column writes, no state). `functools.reduce` is imported and never called; `IStrategy` is imported twice (lines 3 and 7) — both display leftovers, fenced, never repaired. No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 69 lines this cycle): `short` tokens exist ONLY inside the two scoped-out short legs and their comments (`enter_short`, `exit_short`, `sell signals here`, `short positions here`) — adaptation 6 scopes them out, see Signal; 0 `Parameter` (no hyperopt search space anywhere — every constant is a plain literal); 0 `resample` / 0 `merge_informative_pair` / 0 `informative` (no informative pair is ever declared — single-frame by construction); 0 `position_adjustment` / 0 `max_open_trades` / 0 `startup_candle_count` / 0 `process_only_new_candles` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `order_types` / 0 `can_short` / 0 `trading_mode` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 0 `crossed_above` / 0 `crossed_below` (both signal legs are hand-rolled shift-comparison edges, never level prints); 0 `fillna` / 0 `ffill` / 0 `interpolate` (no NaN patching anywhere — strict NaN comparisons simply stay false); 1 `volume` (exactly the OBV input — no other volume read); 0 `high` / 0 `low` / 0 `open` (no range/extremum column is ever read); the single commented `# minimal_roi = {"0": 1}` line is dead text, never assigned — fenced, never repaired.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. The coded signal legs are causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no signal-repair site exists). Researcher-declared adaptations are exactly six, all predeclared here: (1) research market `BTCUSDT` on Binance (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 60-bar researcher warmup pin (covers the span-20 EWM stabilization with margin plus the one-bar edge lag; see Required data); (4) framework-default execution semantics pinned as derived behaviour (signal exits enabled, firing at any close; ROI/stop/trailing legs bar-close-evaluated with the fixed precedence below — disclosed, never presented as file literals); (5) the house cost/capital overlay replaces the absent source economics; (6) long-flat expression — the file's `enter_short` / `exit_short` columns are scoped out as inert (the file sets no `can_short`, so under the framework spot default they never fill; flipping that default would be a different, unpinned rule — disclosed, never presented as file behaviour). Every threshold, every lookback, the three-conjunct entry, the asymmetric three-conjunct signal exit, the ROI ladder, the stop, and the trailing triple are untouched.

Pre-write dedup (2026-10-24): working-tree filename/content search for `TrendFollowingStrategy`, `trendfollowing`, and `futures/TrendFollowingStrategy` returns zero strategy records — no `futures/`-sourced record exists anywhere on `main`, and no open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) trades an OBV-confirmed price-average-cross system. The pool's nearest volume-flow neighbour (the admitted `forven-obv-ema-cross-sma-gated` record) is fenced as a different construction in Negative evidence 7 — it crosses the flow line against its own average behind a price-SMA gate, while this record crosses the price line against its own average behind a flow-direction confirmation. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel anywhere in the 69 lines beyond its code: buy the bar where price reclaims its own 20-bar exponential average from below exactly as cumulative signed-volume flow ticks upward, and stand aside to flat on the bar where price loses the average from above while flow still ticks upward — behind a three-rung time-decaying take-profit ladder (15% immediately, 10% after 30 minutes, 5% after 60 minutes), a −26.5% fixed stop, and an always-on trailing stop (arms at +10%, trails 5% under the peak). The `# ROI table` / `# Stoploss:` / `# Trailing stop:` comments are labels only. No backtest numbers of any kind ship in the file — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Participation-confirmed trend-reclaim machine, long-only, edge-triggered both signal legs. Unlike bare price-cross records (fire on any reclaim, blind to participation — a thin-book wiggle through the average buys the full unit), the OBV leg requires cumulative signed volume to have actually ticked up on the same bar, so reclaims printed on distributing tape hold flat. Unlike flow-cross records (the admitted Forven OBV sibling crosses the flow line against its own average — a flow twitch with price still buried under its mean can fire there, never here), the crossed series is price itself: the average must be physically reclaimed. The exit is the record's honest quirk, kept verbatim: it fires only on a cross-down bar where flow still ticks UP — a loss of trend on accumulating tape surrenders at once, while a cross-down on distributing tape (flow ticking down) rides through the signal leg and surrenders only to the risk stack. The coded consequence is a buyer of backed reclamations that is quick to forgive nothing: one-sided confirmation on the way in, perverse confirmation on the way out, and the ROI/stop/trailer behind both.

## Signal

Exact rule as pinned (any other average family, span, confirmation series, strictness, exit symmetry, ROI rung, stop, trailing triple, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
obv[t]   = TA-Lib OBV(close, volume) over completed 5m bars
trend[t] = ewm(span=20, adjust=False).mean() over close
entry    = (close[t] > trend[t]) AND (close[t-1] <= trend[t-1]) AND (obv[t] > obv[t-1])   // enter_long = 1
exit_sig = (close[t] < trend[t]) AND (close[t-1] >= trend[t-1]) AND (obv[t] > obv[t-1])   // exit_long = 1
risk     = time-decaying take-profit minimal_roi {"0":0.15, "30":0.1, "60":0.05} (keys are minutes: 30 = 6 bars, 60 = 12 bars at 5m);
           fixed stop at -26.5% (stoploss -0.265);
           always-on trailing (positive 0.05, offset 0.1, only-offset-reached False: arms once +10% from entry, then trails 5% under the peak)
guard    = pre-warmup bars flat by record rule (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the three-conjunct reclaim edge; `exit_long=1` on any bar printing the three-conjunct loss edge. Both signal legs are EDGES (fire only on the cross bar — the prior-bar conjunct admits equality precisely so a touch-and-go still arms, while the current bar demands strict inequality). New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly.
- Exact boundaries (pinned semantics): strict `>`/`<` on the current bar throughout — a close landing exactly on the average, or OBV printing exactly unchanged, fires nothing on that conjunct; the prior bar admits equality (`<=` on the reclaim side, `>=` on the loss side) exactly as coded. The `20` span, the one-bar lag, the `0.15`/`0.1`/`0.05` rungs, the `30`/`60` minute keys, the `-0.265` stop, and the `0.05`/`0.1`/`False` trailing triple are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `close[t] > trend[t]` while the signal exit needs `close[t] < trend[t]` on the same bar — strictly disjoint price regions, so the two signal legs never co-print even though both demand rising OBV. ROI/stop/trailing legs start at zero distance on the entry bar (no co-fire with entry at the fill — disclosed, not repaired).
- Exit asymmetry (verbatim, disclosed): the exit leg is NOT the mirror of the entry — it conjoins the cross-down with OBV *rising*, the same flow conjunct as the entry. A cross-down bar with falling OBV prints no signal exit (see Negative evidence 3). Softening the exit to a pure opposite cross, or symmetrizing it to falling-OBV, would each be a different, unpinned rule — none is admitted here.
- Direction: long-only under the derived expression (adaptation 6). The file's short columns are scoped out as inert — no `can_short` ships anywhere, so under the framework spot default they never fill. A two-sided reading (enabling shorts) would require flipping a framework default the file never touches — a different rule, not admitted here. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the asymmetric signal exit, the three-rung decaying ROI ladder, the −26.5% stop, and the always-on trailing triple are the complete position-closing set. No breakeven move, no time exit beyond the ladder, no second trailing mode — explicitly none, not invented. Signal-exit/profit-gating and ROI-on-entry-bar semantics ride the predeclared derived behaviour (Execution assumptions), never a file invention.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying reclaim bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` and `volume` (OBV input) with fixed non-negative offsets (the span-20 trailing EWM plus one `shift(1)` lag inside each edge — no forward reference) — no `high`/`low`/`open`, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `# Add your …` comments are scaffolding prose around complete code — they add no conjunct, remove none, and change no event (fenced, not repaired).

## Required data

- Completed `5m` bars of BTCUSDT: `close` and `volume` ONLY — `close` for the EWM20 trend line and both cross edges, `volume` solely as the TA-Lib OBV input for the one-bar flow confirmation. No bar `open`/`high`/`low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` / 0 `resample` / 0 `informative` anywhere).
- Single decision timeframe `5m` (source-native — the file prints `timeframe = "5m"`). One evaluation per completed bar; every window reads the decision bar and its causal past only (span-20 trailing EWM, one-bar edge lag); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 five-minute bars held flat (~5 hours). Covers the span-20 EWM stabilization (three time constants) with margin, the TA-Lib OBV seed (valid from the first bar), and the one-bar edge lag. Coded behaviour underneath: pandas EWM yields values from the first bar and TA-Lib OBV seeds without NaN smear (no `fillna`/`ffill` exists to smear anything); strict comparisons on the seeded prefix are deterministic either way, and the 60-bar record-rule floor additionally holds every early bar flat — disclosed, not repaired. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop/trailing legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted strategy001 HA-EMA-cross, strategy002 hammer-gated, strategy004 ADX-gated CCI, strategy005 volume-surge-Fisher, MACD-CCI dip-state, and ASDTSRockwell records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. The TA-Lib OBV input reads the same completed-bar `volume` field the admitted strategy005 sibling already gates on. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Risk-stack precedent (exact, disclosed): the always-on trailing triple rides the same derived bar-close trailing evaluation the admitted HLHB record carries for its own `trailing_stop = True` source (fixed per-bar precedence below; intrabar sequencing scoped out, never invented).
- Bar-close precedence (predeclared derivation, disclosed): on a positioned book each completed bar evaluates closing legs in fixed order — (1) fixed stop, (2) trailing stop, (3) ROI rung, (4) signal exit; entry is evaluated only on a flat book. At most one net position change per bar by construction plus the mutual-exclusion proof.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder, stop percentage, and trailing triple are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the reclaim edge opens the full unit on a flat book; the asymmetric signal exit, any ROI rung, the stop, or the trailer closes it in full; re-entry after an exit needs only the next qualifying reclaim bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (69 lines: the OBV-plus-EWM20 indicator block, the three-conjunct reclaim entry with its shift-comparison edges, the asymmetric three-conjunct loss exit, the `timeframe`/`minimal_roi`/`stoploss`/trailing literals, and the `TrendFollowingStrategy(IStrategy)` class pin). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: the 60-bar record-rule floor holds every early bar flat — disclosed, not repaired. Underneath, EWM seeds and OBV print deterministic values from the first bars (no NaN-smearing primitive exists to misbehave); strict comparisons there can only stay false or print seeded edges, never reference the future.
2. Exact-touch rule fenced: a close landing exactly on the average, or OBV printing exactly unchanged, fires nothing on that conjunct (strict current-bar inequality on all six conjuncts); a prior-bar touch still arms the edge by the coded `<=`/`>=`. Strictness is preserved throughout — disclosed, not smoothed.
3. Exit-asymmetry bleed fenced: a cross-down bar with FALLING OBV prints no signal exit by verbatim code — the position rides until an ROI rung, the stop, or the trailer ends it. A slow bleed that never prints a rising-OBV cross-down bar rides the full risk stack in full — disclosed, not repaired. Mirror-wise, a reclaim bar with falling OBV never enters, however clean the price cross.
4. Zero-participation fenced: an all-zero-volume tape freezes OBV flat (every `obv[t] > obv[t-1]` conjunct false) — neither signal leg can ever print; the book stays flat forever. No division exists anywhere in the gating path, so no undefined arithmetic can arise — disclosed, not repaired.
5. Dead-import plumbing fenced: `reduce` is imported and never called; `IStrategy` is imported twice; the `# Add your …` comments add no rule; the commented `# minimal_roi = {"0": 1}` line is never assigned — an engine that deletes all four reaches identical events. No reviewer repair may promote any of them into a leg.
6. Short-column scope fenced: `enter_short`/`exit_short` print only in the scoped-out columns under adaptation 6 — with no `can_short` in the file they never fill under the framework spot default. Enabling them (or porting their conjunctions anywhere else) would be a different, unpinned rule — none is admitted here.
7. Cousin records fenced as different constructions (none trades a price-vs-own-EWM cross confirmed by a same-bar OBV tick, long-flat, under an ROI/stop/trailing stack on `5m`): the admitted `forven-obv-ema-cross-sma-gated` sibling crosses the FLOW line against its own EWM20 behind a price-SMA20 gate (crossed series swapped, confirmation swapped, signal-exits-only with zero risk legs, `1h`, different source); the admitted `forven-ema-cross-adx-regime` / `forven-dema-cross` siblings cross price averages with no volume read at all; the admitted `forven-atr-volume-breakout` sibling trades volume-breakout levels with no cumulative line; the admitted `forven-adl-ema-cross` sibling accumulates range-weighted money-flow-volume, never signed-volume OBV; the admitted `freqtrade-strategy001` sibling crosses EMA20/50 under a Heikin-Ashi color state (no flow leg, no trailing); the pool's Supertrend/OTT records trade band-reclaim systems with different triggers and risk. Not a re-tuning of any of them: swapping the crossed series, the average family, the span, the confirmation, the exit symmetry, or any risk literal would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 60-bar warmup floor, derived signal-exit/risk execution semantics with fixed precedence, house sizing/costs, long-flat expression scoping out the inert short columns) — all predeclared above. The `5m` frame, the TA-Lib OBV construction, the EWM20 trend line, the three-conjunct reclaim entry, the asymmetric three-conjunct loss exit, the ROI ladder, the −26.5% stop, and the trailing triple are source-verbatim effective behaviour.
9. The span, the lags, the strictness, the exit asymmetry, the ROI minute-keys, the stop, and the trailing triple are pinned, not removed: re-tuning any span, softening strictness to touches, symmetrizing the exit, converting an edge to a level (or the reverse), adding a stop/target/filter/cooldown/gate, enabling the short side, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: three-conjunct reclaim entry / span-20 EWM / TA-Lib OBV / one-bar edge lags / asymmetric exit / ROI ladder / −26.5% stop / trailing triple / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Confirmation relevance: dropping the OBV tick conjunct (pure price-vs-EWM20 cross entry, same exit/risk) must not improve net expectancy; fail ⇒ the participation confirmation adds nothing over its naked twin.
- F2 — Exit-asymmetry relevance: replacing the rising-OBV exit conjunct with a pure opposite-cross exit (same entry, same risk) must not improve net expectancy; fail ⇒ the verbatim asymmetry adds nothing over the natural mirror.
- F3 — Average-family relevance: replacing the EWM20 trend line with an SMA20 trend line (same edges/confirmation/exit/risk) must not improve net expectancy; fail ⇒ the exponential weighting adds nothing over its simple twin and the record is a smoothing variant.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count (span-20 EWM, one-bar lag, minute-keyed ROI rungs), portable across 24/7 crypto tape. Only the `close` and `volume` candle fields are read (venue print differences move only the EWM/OBV inputs, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions. The `futures/` folder location carries no margin/leverage semantic into this record — no `trading_mode`, `can_short`, or leverage ships in the file.

## Limitations

- TA-Lib OBV internals live in their library outside the pinned file — pinned by call with explicit `(close, volume)` inputs, not re-derived; exact reproduction inherits that module's seeding alongside the file-local wiring, under the disclosed 60-bar floor.
- Pandas EWM internals (`span=20, adjust=False`) live in their library outside the pinned file — pinned by call, not re-derived; reproduction inherits that module's recursive seeding, stabilized under the same floor.
- No hyperopt scaffolding exists anywhere (zero `Parameter` tokens) — there is nothing to freeze and nothing to re-optimize; any re-tuning would be a different, unpinned rule.
- The trailing/stop/ROI legs are evaluated bar-close under the predeclared derivation — the source evaluates risk per its own engine cadence; intrabar stop/trailer sequencing is scoped out, never invented. This record makes no claim about any live-order behaviour.
- No trailing-armed-state subtlety beyond the file literals: `trailing_only_offset_is_reached = False` is preserved verbatim (the trailer tracks from entry, arms its offset at +10%) — never redefined at review.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/TrendFollowingStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
