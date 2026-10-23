---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade TrendFollowing OBV-slope-filtered EWM20 cross long-flat on BTCUSDT 5m bars
created: 2026-10-23
updated: 2026-10-23
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

# Freqtrade TrendFollowing OBV-slope-filtered EWM20 cross long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/TrendFollowingStrategy.py` (the `futures/` directory placement is organizational only — the file calls no futures-only API: zero `leverage`, `funding`, or `mark_price` tokens anywhere; see census).
- GitHub blob SHA at the pinned commit: `e14f23ddf1a2bdd003f55fa45430492019be39cb`, size 2441 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2441 bytes, 69 lines, SHA-256 `6b8f3e272acfd4923539120364b9ddceccc17a385117d12a249dc1460ea53c4f`, identical to the GitHub blob (`git hash-object` reproduces `e14f23dd…19be39cb`) — the entire file was retrieved and inspected.
- Registration: the file defines class `TrendFollowingStrategy(IStrategy)` (the only class in the file). Identity here is class plus file path, both unique. Repo-wide, the sibling files `futures/VolatilitySystem.py` (3h-resampled ATR/abs-change breakout with `position_adjustment` DCA and a `leverage()` override), `futures/FOttStrategy.py` (header-declared hyperopt-fitted OTT/ADX60 construction), `futures/FSampleStrategy.py`, `futures/FSupertrendStrategy.py`, `futures/FAdxSmaStrategy.py`, and every other file in the collection are different pins with different gates — this record pins ONLY the TrendFollowingStrategy file's literals below, and no reviewer repair may substitute a sibling constant, leg, frame, or risk pair.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "5m"`; `minimal_roi = {"0": 0.15, "30": 0.1, "60": 0.05}` (three-rung ladder, fractions of entry-price distance); `stoploss = -0.265`; `trailing_stop = True` with `trailing_stop_positive = 0.05`, `trailing_stop_positive_offset = 0.1`, `trailing_only_offset_is_reached = False`; indicators `dataframe['obv'] = ta.OBV(dataframe['close'], dataframe['volume'])` (single vendored call, zero parameters) and `dataframe['trend'] = dataframe['close'].ewm(span=20, adjust=False).mean()` (explicit span 20, explicit `adjust=False`); long entry `(close > trend) & (close.shift(1) <= trend.shift(1)) & (obv > obv.shift(1))` (`enter_long = 1`); long exit `(close < trend) & (close.shift(1) >= trend.shift(1)) & (obv > obv.shift(1))` (`exit_long = 1`); shipped short legs `(close < trend) & (close.shift(1) >= trend.shift(1)) & (obv < obv.shift(1))` (`enter_short = 1`) and `(close > trend) & (close.shift(1) <= trend.shift(1)) & (obv < obv.shift(1))` (`exit_short = 1`) — both fenced as inert under the file's own framework contract below, never deleted from provenance. No `can_short`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (resolved by name, standard libraries): `ta.OBV` from `talib.abstract` (vendored TA-Lib binding, invoked with close-plus-volume and zero parameters — pinned by call, never re-derived; only its one-bar-lagged slope sign enters the gating path); pandas `ewm(span=20, adjust=False).mean()` (explicit span and recursion mode — recursive causal weighting seeded from the first available bar, never re-derived). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter`/`RealParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 69 lines this cycle): 0 `Parameter` / 0 `hyperopt`; 0 `resample` / 0 `informative`; 0 `can_short` (the long-only pin below follows the framework default `False` — disclosed default, never a file literal); 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage`; 0 `position_adjustment` / 0 `pyramid` / 0 `cooldown` / 0 `max_open_trades` / 0 `custom_stake_amount` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `request` / 0 `security` / 0 `scipy`; 0 `crossed` (no edge call — both signal legs are hand-built strict-comparison-plus-`shift(1)` edges); 0 `open`-column reads / 0 `high`-column reads / 0 price-`low` reads (the 6 case-insensitive `low` substring hits are all inside the identifier `TrendFollowingStrategy` / prose `following` — no low-price leg ships); 1 `volume` (the single OBV constructor read — bar volume enters the rule only there, disclosed; no standalone volume-threshold leg ships); 12 `shift`, all `shift(1)` causal one-bar lags, never a forward reference; 3 `short` tokens, all inside the two inert short legs fenced below. Dead plumbing fenced with zero gate effect: one unused `reduce` import, one unused `qtpylib` import (zero `qtpylib.` uses), and a duplicated `IStrategy` import line (module plus `interface` path). The commented-out `# minimal_roi = {"0": 1}` line and the `# Add your trend following … here` scaffold comments are dead prose — the coded three-rung table and coded legs govern, never the comments.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the EWM20 trend construction with all its literals, the OBV-slope-filtered cross entry edge, the OBV-slope-filtered cross signal exit, the three-rung ROI ladder, the −26.5% stop, and the four trailing literals — but ships no venue spelling, no fill-timing flag, no warmup guard, no position-sizing rule, and no `can_short` override. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing; the ROI/stop/trailing legs are likewise bar-close-evaluated in this derived version, disclosed); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) long-only stance with the two shipped short legs fenced as inert (the file sets no `can_short = True`, so under its own framework contract the framework default `can_short = False` applies and no short position can open — disclosed default, never a file literal; this record pins that effective behaviour rather than inventing a two-sided book); (5) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for the exact source identity (`TrendFollowingStrategy`, `futures/TrendFollowingStrategy`) returns zero strategy records — no record in the pool cites this source file or class. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an OBV-slope-filtered EWM-cross rule. OBV and cross cousins in the pool are fenced as different constructions in Negative evidence 8. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: ride up-trends while closes hold above their 20-bar exponential average, entering on the first bar that crosses back above it with rising on-balance volume, and stepping aside on the first bar that crosses back below it (still with rising volume). A three-rung ROI ladder (15% / 10% / 5% by position age in minutes), a fixed −26.5% stoploss, and a trailing stop (5% positive trail, 10% offset, active without waiting for the offset) backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Trend-reclaim edge machine, long-only. The EWM20 leg draws a fast recursive trendline through closes; the OBV-slope leg demands that the reclaim bar print expanding cumulative volume conviction (rising OBV), filtering out low-participation wiggles above the line. Entry and signal exit are opposite crosses, so the book can only ever hold one side of the line at a time — there is no state-holding beyond the edges: a market that stays above the line without re-crossing simply holds. The ROI ladder harvests extended trends in stages (15% early, decaying to 5%), while the −26.5% stop (far wider than any rung) stands as a disaster backstop that almost never binds first in ordinary tape, and the trailing leg locks in a 5% give-back once profits stretch past the 10% offset region. The failure mode is plain: a market oscillating across the EWM20 whipsaws the book edge-to-edge (cross-up entry, cross-down exit, no cooldown to damp the round trips), and the exit leg's own rising-OBV requirement means a breakdown on collapsing volume does NOT fire the signal exit — that tape leaves only the ROI/stop/trailing legs to close the book.

## Signal

Exact rule as pinned (any other EWM span, recursion mode, OBV construction, slope direction, comparison strictness, risk rung, fill, frame, or book is a different, unpinned rule):

```text
obv[t]   = ta.OBV(close, volume)[t]              // vendored, causal, pinned by call
trend[t] = close.ewm(span=20, adjust=False).mean()[t]  // explicit span + recursion, causal
upX[t]   = (close[t] > trend[t]) & (close[t-1] <= trend[t-1])    // reclaim edge
dnX[t]   = (close[t] < trend[t]) & (close[t-1] >= trend[t-1])    // breakdown edge
obvUp[t] = (obv[t] > obv[t-1])                   // strict rising-volume filter
entry    = upX[t] & obvUp[t]       // enter_long = 1, one-bar edge, strict
exit_sig = dnX[t] & obvUp[t]       // exit_long = 1, one-bar edge, strict
risk     = ROI {"0": 0.15, "30": 0.1, "60": 0.05} (fraction of entry-price distance, by position age in minutes);
           fixed stop at -26.5% (stoploss -0.265, same basis);
           trailing stop positive 0.05 / offset 0.1 / only-offset-reached False (same basis)
floor    = leading-window bars: shift(1) NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on a reclaim edge with rising OBV, `direction` long-only; `exit_long=1` on a breakdown edge with rising OBV. Each print is a one-bar edge, not a persistent state — non-edge bars are hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the decision-bar comparisons are strict (`>` / `<`); the prior-bar confirmations admit equality (`<=` / `>=`); the OBV filter is strict (`>`). A bar with `close == trend` fires neither signal leg; a bar with `obv == obv.shift(1)` fires neither signal leg (both legs require strict OBV rise). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close[t] > trend[t]` while any signal-exit bar has `close[t] < trend[t]` — mutually exclusive on every bar, so entry and signal-exit never co-print. ROI/stop/trailing cannot co-fire with entry on the entry bar either (zero distance at the fill); any bar co-printing a signal exit with an ROI/stop/trailing leg closes the full unit flat either way. The short-leg pair (`enter_short`/`exit_short`) is inert under the long-only pin and never co-prints with any active leg. The reviewer is never asked to invent an ordering.
- Direction: long-only (derived pin, disclosed). The file ships `enter_short`/`exit_short` legs but sets no `can_short = True`, so under the file's own framework contract the default `can_short = False` applies and no short position can open — this record pins that effective long-only behaviour. A two-sided reading would contradict the file's default-config behaviour.
- Exits and risk (explicit): the breakdown-edge signal exit, the three-rung ROI ladder, the −26.5% stop, and the trailing leg (positive 0.05, offset 0.1, `trailing_only_offset_is_reached = False`) are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rungs, stop, and trailing are fractions of entry-price distance (close-to-close price return), evaluated at bar closes in this derived version — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. No time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-edge bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-edge bars as no-ops; re-entry re-arms on any qualifying reclaim edge after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` and `volume` (one vendored OBV construction, one recursive EWM20, fixed one-bar causal lags — no forward reference) under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `close` (EWM20 construction plus both cross edges) and bar `volume` (read once inside the rule — inside the vendored OBV constructor; the rule is volume-slope-gated, disclosed; no standalone volume-threshold leg ships). No `open`, `high`, or `low` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = "5m"`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 five-minute bars held flat. Covers twice the EWM span-20 recursion seed with margin; OBV is cumulative from the first available bar and only its one-bar slope sign is gated, so no longer seed is needed. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: `shift(1)` prints NaN on the first bar and every strict NaN comparison is false — no leg can fire on the first bar. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, ADXMomentum, EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed, and CMF-sign-state siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the signal-exit edge, and the ROI/stop/trailing legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop/trailing leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed, and CMF-sign-state records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder, stop percentage, and trailing literals are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the reclaim edge opens the full unit on a flat book; the breakdown-edge signal exit, any ROI rung, the stop, or the trailing leg closes it in full; re-entry after an exit needs only the next qualifying reclaim edge (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (69 lines: the OBV and EWM20 indicator lines with all literals, the four coded signal legs with strictness, the `timeframe`/three-rung-`minimal_roi`/`stoploss`/four-trailing literals, and the `TrendFollowingStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: `shift(1)` prints NaN on the first bar and every strict NaN comparison is false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-equality fence: the decision-bar comparisons are strict — a bar printing exactly `close == trend` fires neither signal leg, and a bar printing exactly `obv == obv.shift(1)` fires neither signal leg. Strictness and the admitted prior-bar equalities (`<=` / `>=`) preserved throughout — disclosed, not smoothed.
3. Dead-comment fence: the commented-out `# minimal_roi = {"0": 1}` line and the `# Add your trend following … here` scaffold comments are prose — the coded three-rung ladder `{"0": 0.15, "30": 0.1, "60": 0.05}` and coded legs govern; prose never does.
4. Wide-stop fence: the −26.5% stop is wider than every ROI rung (15% / 10% / 5%) — by construction the stop is a disaster backstop that almost never binds before the ladder or the signal exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
5. Trailing-leg fence: all four trailing literals (`True` / `0.05` / `0.1` / `False`) are preserved verbatim with bar-close evaluation in this derived version (see Execution assumptions) — disclosed, not converted into a tighter stop, not dropped, and not re-timed intrabar by repair.
6. No-edge-call fence: the file contains zero `crossed_*` calls and builds both signal legs from strict comparisons plus causal `shift(1)` — converting either leg to a library edge call (or vice versa) would be a different, unpinned rule with different trade events.
7. Short-leg inert fence: the shipped `enter_short`/`exit_short` legs never activate in this derived version — the file sets no `can_short = True`, so the framework default `False` governs. The legs remain quoted in Provenance; they are fenced, never silently deleted and never traded.
8. Cousin records fenced as different constructions (none trades a close-vs-EWM20 cross pair slope-gated by strict OBV rise, long-flat, with a 15%/10%/5% ROI ladder plus a −26.5% stop plus a 5%-trail on `5m`): the admitted `obv-ema-crossover-trend` pool-mate trades an OBV-vs-EMA positional cross state (two-sided, `1d`, different indicator pairing, no slope filter, no ladder); the admitted `forven-obv-ema-cross-sma-gated` pool-mate trades an OBV/EMA cross behind an SMA regime gate (Forven source, `1h`, different gate, different risk); the admitted `freqtrade-technical-cmf-sign-state` pool-mate trades 21-bar CMF zero-line persistent states (state machine, not cross edges, different indicator, different risk); the admitted `wilder-volatility-system-sic` pool-mate trades Wilder's system stop-and-reverse (different source, different mechanism). Not a threshold re-tuning of any of them: moving the EWM span, changing the recursion mode, flipping any strictness or slope direction, converting either edge to a state, or changing any ROI rung, the stop, the trailing literals, or the frame would each be a different, unpinned rule — none is admitted here.
9. Sibling-file fence: `VolatilitySystem.py`, `FOttStrategy.py`, `FSampleStrategy.py`, `FSupertrendStrategy.py`, `FAdxSmaStrategy.py`, `TrendRiderStrategy.py`, and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
10. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills with bar-close-evaluated risk legs, the long-only pin with inert short legs, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none of these), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the vendored OBV call and pandas EWM recursion (pinned by call with explicit span/mode, never re-derived), the dead-import/dead-comment fencing, and house sizing/costs with safety tranches deactivated — all predeclared above. The `5m` frame, the EWM20 construction with all its literals, the OBV-slope-filtered reclaim entry edge, the OBV-slope-filtered breakdown signal exit, the three-rung ROI ladder with the −26.5% stop and the four trailing literals are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: OBV constructor / EWM(20, adjust=False) / strict OBV-rise filter / reclaim-vs-breakdown edges with pinned strictness and prior-bar equalities / breakdown signal exit / 15%-10%-5% ROI ladder / −26.5% stop / 5%-trail literals / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Volume-filter relevance: dropping the strict OBV-rise requirement from both signal legs (bare EWM20 reclaim/breakdown edges, same risk) must not improve net expectancy; fail ⇒ the OBV slope filter adds nothing over the naked cross.
- F2 — Exit-asymmetry relevance: replacing the breakdown-plus-rising-OBV signal exit with a symmetric breakdown edge regardless of OBV slope (same entry, same risk) must not improve net expectancy; fail ⇒ the coded exit asymmetry adds nothing over its symmetric twin.
- F3 — Risk-leg relevance: removing the ROI ladder/stop/trailing set (signal-only exits) must not improve net expectancy; fail ⇒ the 15%-10%-5% ladder plus −26.5% backstop plus 5%-trail adds nothing over the bare edge machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count (EWM span, one-bar lags, minute-aged ROI rungs) on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed, CMF-sign-state `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A market oscillating across the EWM20 whipsaws the book edge-to-edge (reclaim entry, breakdown exit, no cooldown to damp the round trips — disclosed as the principal friction). A breakdown on flat-or-falling OBV fires no signal exit — that tape leaves only the ROI/stop/trailing legs to close the book (disclosed exit asymmetry, not repaired).
- OBV is cumulative from the first available bar, so its slope sign inherits the visible history window alongside the 40-bar floor — pinned by call, not re-derived; exact reproduction inherits the same seeding.
- The trailing leg's bar-close evaluation is a derived-research convention (see Execution assumptions) — disclosed, never presented as the source engine's intrabar timing.
- No short leg, no time exit, no breakeven, no cooldown — all explicitly absent or inert, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/TrendFollowingStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
