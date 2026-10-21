---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AverageStrategy EMA8/21 mirror-cross long-flat on BTCUSDT 4h bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AverageStrategy EMA8/21 mirror-cross long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macdstrategy-crossed`, `freqtrade-multima`, `freqtrade-hlhb`, `freqtrade-cofibit`, `freqtrade-quickie`, `freqtrade-simple-macd`, `freqtrade-strategy001/002/003/004/005`, `freqtrade-swinghightosky`, `freqtrade-universalmacd`, and `td-sequential-setup9-perfected` records — this is only its next record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/AverageStrategy.py`.
- GitHub blob SHA at the pinned commit: `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, size 2630 bytes, 79 lines.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is byte-identical (`cmp` clean) to the pinned-tree object, SHA-256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`, identical to the GitHub blob (`git hash-object` reproduces `dbb0ba65…0d308d493`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AverageStrategy(IStrategy)` (the only class in the file, author `Gert Wohlgemuth`). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration, `5m`, admitted), `berlinguyinca/BinHV27.py` (RSI/ADX/DI regime-state, `5m`, admitted), `berlinguyinca/EMASkipPump.py` (EMA-stack dip with volume veto, `5m`, admitted), `berlinguyinca/Quickie.py` (TEMA-slope BB-mid ADX-gated, `5m`, admitted), `berlinguyinca/Simple.py` (MACD/BB/RSI momentum, `5m`, admitted), `berlinguyinca/MACDStrategy.py` / `MACDStrategy_crossed.py` (MACD-polarity state / MACD-cross edge, `5m`, admitted), `berlinguyinca/CCIStrategy.py` (resample-interpolated multi-frame, `1m`), `berlinguyinca/BinHV45.py` (BB(40) penetration, `1m`), `berlinguyinca/MultiRSI.py` (resampled multi-frame RSI, `5m`), `berlinguyinca/Scalp.py` / `SmoothScalp.py` (`1m` stoch-EMA scalp states), `berlinguyinca/TDSequentialStrategy.py` (TD setup-9 perfection, `1h`, admitted), `berlinguyinca/AdxSmas.py` (SMA3/6 cross ADX-gated, `1h`, open PR #331), and `berlinguyinca/ClucMay72018.py` (BB-discount EMA-gated, `5m`, open PR #350) are different pins with different gates — this record pins ONLY the AverageStrategy file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): docstring idea `buys and sells on crossovers - doesn't really perform that well and its just a proof of concept`; `minimal_roi = { "0": 0.5 }`; `stoploss = -0.2`; `timeframe = '4h'`; parameters `buy_range_short = IntParameter(5, 20, default=8)` and `buy_range_long = IntParameter(20, 120, default=21)` (no `space`, no `optimize` flag, and — critically — no `buy_params`/`sell_params` dict anywhere in the file, so the pinned defaults 8/21 govern with no variant to choose); indicators loop `dataframe[f'ema{val}'] = ta.EMA(dataframe, timeperiod=val)` over the union of both parameter ranges; entry `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_short.value}'], dataframe[f'ema{self.buy_range_long.value}']) & (dataframe['volume'] > 0)` (`enter_long = 1`); exit `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_long.value}'], dataframe[f'ema{self.buy_range_short.value}']) & (dataframe['volume'] > 0)` (`exit_long = 1`, the exact mirror). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.EMA` (TA-Lib EMA on close, pinned periods 8 and 21 as read by the gating legs — no override in the file); `qtpylib.crossed_above` (standard Freqtrade one-bar edge: `(s1 > s2) & (s1.shift(1) <= s2.shift(1))` — causal two-bar comparison, disclosed, never redefined). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no informative-pair call, no `merge_informative_pair` in the file.
- Full-file token census (verified over the 79 lines this cycle): 4 `short` (case-insensitive — all four are the `buy_range_short` window identifier: declaration line 35, range-union line 41, entry read line 55, exit read line 74 — zero short-side order semantics anywhere); 2 `volume` (the two `> 0` presence guards, entry line 58 and exit line 76 — no volume arithmetic, no volume threshold); 3 `Parameter` (all on the single import line 4: `CategoricalParameter, DecimalParameter, IntParameter` — only `IntParameter` is ever instantiated, twice; the other two are dead imports fenced below); 0 `buy_params` / 0 `sell_params` (no hyperopt dict — defaults govern unambiguously); 0 `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `shift` (no lag call in the file body — the single one-bar lookback lives inside the standard `crossed_above` edge, disclosed above); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`. The `CategoricalParameter`/`DecimalParameter` imports, the `Dict`/`List`/`reduce` imports, and every computed `ema{val}` column except `ema8`/`ema21` are dead plumbing/columns with no gate effect, fenced below.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `4h` frame, the EMA8/EMA21 mirror-cross edges with the `volume > 0` presence guards, the single-rung 50% ROI, the −20% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `averagestrategy` (case-insensitive) returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles band-ratio state) trades a bare dual-EMA mirror-cross. EMA-cross cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: buy the single bar where EMA8 crosses up through EMA21 together with positive bar volume (trend-rotation edge with a presence guard), sell the single bar where EMA21 crosses up through EMA8 (the exact mirror, i.e. EMA8 crossing down) together with positive bar volume. A single-rung 50% ROI (`"0": 0.5`) and a fixed −20% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence). The author's own docstring warns the idea `doesn't really perform that well and its just a proof of concept` — quoted honesty, never a gate fact.

### Research interpretation

Bare-bones trend-rotation machine, long-only. The EMA8/EMA21 pair supplies both the timing and the regime: a cross-up edge opens the book, and the book is then held through every non-crossing bar by design until the mirror edge, the 50% rung, or the −20% stop closes it. Unlike persistent-state records (trade every bar the condition holds), each leg can fire at most on its crossing bar — a book already positioned treats further bars as hold-no-ops until a qualifying exit. The `volume > 0` legs are presence guards, not thresholds: on BTCUSDT `4h` they are satisfied on every traded bar and never veto, but they are preserved verbatim because a zero-volume bar must print nothing on either side. The exit is the exact logical mirror of the entry — there is no independent exit indicator, no profit target in working range, and no time exit — so the holding period is whatever the tape dictates between opposite crosses, bounded only by the two risk legs.

## Signal

Exact rule as pinned (any other EMA periods, guard, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; EMA periods are the file's pinned IntParameter defaults (8/21), effective because the file ships no `buy_params`/`sell_params` dict:

```text
ema8[t]  = TA-Lib EMA(close, 8)   // pinned default — no file override path exists
ema21[t] = TA-Lib EMA(close, 21)  // pinned default — no file override path exists
entry    = crossed_above(ema8, ema21)[t] AND (volume[t] > 0)  // enter_long = 1, one-bar edge
exit_sig = crossed_above(ema21, ema8)[t] AND (volume[t] > 0)  // exit_long = 1, one-bar mirror edge
risk     = ROI ladder {"0": 0.5} (fraction, by position age in minutes);
           fixed stop at -20% (stoploss -0.2)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on a bar printing the cross-up edge with positive volume, `direction` long-only; `exit_long=1` on a bar printing the mirror edge with positive volume. Each print is a one-bar edge, not a persistent state — a book already positioned treats non-exit bars (including further entry edges) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): both cross edges are strict on the decision bar (`fast > slow`) with inclusive previous-bar equality (`prev fast <= prev slow` inside the standard edge); the volume guards are strict (`> 0`) — a bar with `ema8 == ema21` fires neither leg; a zero-volume bar fires neither leg even on a cross print. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `ema8[t] > ema21[t]` while any signal-exit bar has `ema21[t] > ema8[t]` — mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print regardless of the volume legs. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-order tokens ship anywhere (the four `short` hits are the fast-window identifier), and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirror signal exit, the single 50% ROI rung, and the −20% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry edges as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying mirror-cross bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (EMA smoothing, fixed non-negative offsets, plus the standard one-bar edge lookback — no forward reference) and the decision bar's own `volume` presence flag, with no `shift` call in the file body because the single lookback lives inside the standard `crossed_above` edge under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter read at decision time (both parameters resolve to file-pinned constants before the first bar), or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `4h` bars of BTCUSDT: `close` (EMA8/EMA21) and `volume` (presence guard only — no volume arithmetic, no volume threshold). No `open` read, no `high`/`low` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the one-bar edge lookback); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 four-hour bars held flat. Covers the TA-Lib EMA21 seed (SMA-of-21 start plus smoothing) with margin; the gating EMAs are 8/21 only — the wider computed-but-unread EMA columns (5–120) never gate and need no seeding. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, BinHV27, MultiMa, HLHB, CofiBit, Quickie, SimpleMACD, Strategy001–005, SwingHighToSky, UniversalMACD, and TDSequential siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirror signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `4h` is an already-admitted interval on `main` via the MultiMa, HLHB, and Heracles-lane records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its 50% ROI rung and −20% stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the cross-up edge opens the full unit on a flat book; the mirror signal exit, the 50% rung, or the −20% stop closes it in full; re-entry after an exit needs only the next qualifying cross-up bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (79 lines: the two pinned IntParameter defaults, the EMA range-union loop, the two mirror `crossed_above` conjunct edges with their volume guards, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `AverageStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance. The author's proof-of-concept disclaimer is quoted in Economic mechanism, not converted into a performance claim.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: both cross edges are strict on the decision bar while admitting previous-bar equality; the volume guards are strict (`> 0`) — a bar sitting exactly on the slow line fires nothing on either side; a zero-volume bar fires nothing even with a cross print. Strictness preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `CategoricalParameter`, `DecimalParameter`, `Dict`, `List`, and `reduce` are imported and never called anywhere in the 79 lines — display/plumbing leftovers with no gate effect, never repaired into a signal. Zero `buy_params`/`sell_params` tokens, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.
4. Dead-column fence: the indicator loop computes EMA columns for every window in the union of both parameter ranges (5–120), but the gating legs read ONLY `ema8` and `ema21` — every other column is unread by any order line, never repaired into a third leg or a regime filter. Pinning the defaults (8/21) is not choosing among variants: with no `buy_params` dict the file leaves the framework no other value source, and the unread columns gate nothing under any value.
5. No-default-ambiguity fence: unlike hyperopt-tuned siblings whose `buy_params` dicts disagree with their Parameter defaults (HourBasedStrategy, Supertrend, BinHV45 — all deliberately left unpinned this cycle), this file ships NO dict at all, so `buy_range_short.value = 8` and `buy_range_long.value = 21` is the single file-determined reading. The reviewer is never asked to choose between a dict value and a default.
6. Wide-risk fence: the 50% ROI rung is ~2.5× the −20% stop distance — by construction the ROI leg is an effectively-disabled moonshot backstop that almost never binds before the mirror signal exit or the stop in ordinary tape. Coded fact, disclosed, not reinterpreted as a working profit target and not tightened by repair.
7. Cousin records fenced as different constructions (none trades a bare EMA8/EMA21 mirror-cross with a volume presence guard, long-flat, on `4h` with this risk pair): the admitted `ema-20-50-cross` pool-mate trades a 20/50 cross on `1h` from a different source with different risk; the admitted `forven-ema-cross-adx-regime` pool-mate gates its EMA cross on an ADX regime leg with an unconditional cross-down exit profile; the admitted `freqtrade-strategy001-ha-ema-cross` pool-mate trades Heikin-Ashi EMAs on `5m` with different periods and exits; the admitted `freqtrade-multima` pool-mate trades a TEMA stack, not a two-line cross; Guppy/hull/DEMA/TEMA cross pool-mates use different averages, stacks, or frames. Not a threshold re-tuning of any of them: moving either EMA period, dropping the volume guard, converting either edge to a persistent state, flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `CombinedBinHAndCluc.py`, `BinHV27.py`, `BinHV45.py`, `EMASkipPump.py`, `Quickie.py`, `Simple.py`, `MACDStrategy.py`, `MACDStrategy_crossed.py`, `CCIStrategy.py`, `MultiRSI.py`, `Scalp.py`, `SmoothScalp.py`, `TDSequentialStrategy.py`, `AdxSmas.py`, and `ClucMay72018.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the pinned IntParameter-default readings (EMA 8/21 — the file's only value source, never a reviewer choice), the standard `crossed_above` one-bar edge semantics, and house sizing/costs — all predeclared above. The `4h` frame, the mirror-cross entry/exit edges with all their literals and strictness, the volume presence guards, the single 50% ROI rung with the −20% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA(8)/EMA(21) / mirror-cross edges / `volume > 0` guards with pinned strictness / one-bar-edge legs / mirror signal exit / single 50% ROI rung / −20% stop / single-unit long-only / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Rotation-timing relevance: replacing the cross edges with a persistent state (long while `ema8 > ema21`, exit while `ema8 < ema21`, same guards and risk) must not improve net expectancy; fail ⇒ the one-bar rotation edge adds nothing over the regime state.
- F2 — Guard relevance: dropping the `volume > 0` legs (naked mirror-cross, same risk) must not change trade events on BTCUSDT `4h`; fail ⇒ the presence guard binds somewhere in the sample and its veto matters.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 50%/−20% backstops add nothing over the bare mirror machine.

## Crypto portability

BTCUSDT Binance perpetual `4h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. The `volume > 0` guard is satisfied on every traded BTCUSDT bar; funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `4h` frame rides existing admission precedent (MultiMa, HLHB `4h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market that trends without ever printing the mirror cross is held until the 50% rung or the −20% stop; a market that chops across the lines prints alternating full-unit flips with no chop filter, while a market that drifts sideways with the fast line pinned above the slow line holds indefinitely with no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib EMA internals (SMA seeding, smoothing arithmetic) and the standard `crossed_above` one-bar edge live in libraries outside the pinned file — pinned by call with periods 8/21, not re-derived; exact reproduction inherits those libraries' seeding alongside the 40-bar floor.
- The `CategoricalParameter`/`DecimalParameter`/`Dict`/`List`/`reduce` imports and every computed-but-unread `ema{val}` column are dead — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The author's proof-of-concept disclaimer is a caution about expected edge, not a gate fact — admission here is pinned-engine expressibility, never a profitability claim.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
