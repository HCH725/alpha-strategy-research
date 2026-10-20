---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Quickie TEMA-slope BB-mid ADX-gated momentum long-flat on BTCUSDT 5m bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2018-06-27
sources:
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/Quickie.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Quickie TEMA-slope BB-mid ADX-gated momentum long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-strategy001`, `freqtrade-strategy002`, `freqtrade-strategy003`, `freqtrade-strategy004`, and `freqtrade-hlhb` records — this is only its fourteenth record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/Quickie.py`.
- GitHub blob SHA at the pinned commit: `13db60b15bf24cf8849eb01c997f9f8f34e59705`, size 2600 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2600 bytes, 78 lines, SHA-256 `4428df93cce5a9a1b13ca37fe813d1c8b96d4ea8d904be0f33cf9d36b447cb40`, identical to the GitHub blob (`git hash-object` reproduces `13db60b1…34e59705`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Quickie(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/strategy001.py` through `strategy005.py` plus every other `user_data/strategies/berlinguyinca/*.py` sibling are different pins with different constants — this record pins ONLY the Quickie literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "100": 0.01, "30": 0.03, "15": 0.06, "10": 0.15 }`; `stoploss = -0.25`; entry is the four-way AND of `adx > 30`, `tema < bb_middleband`, `tema > tema.shift(1)`, `sma_200 > close`; exit is the three-way AND of `adx > 70`, `tema > bb_middleband`, `tema < tema.shift(1)`. The docstring attribution (`author@: Gert Wohlgemuth`, `idea: momentum based strategie. The main idea is that it closes trades very quickly, while avoiding excessive losses. Hence a rather moderate stop loss in this case`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 78 lines.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.TEMA(dataframe, timeperiod=9)` (explicit 9 — live entry/exit leg); `ta.SMA(dataframe, timeperiod=200)` into `sma_200` (explicit 200 — live entry leg) and a second identical `ta.SMA(dataframe, timeperiod=200)` into `sma_50` (file-literal mislabel, computed but never read — dead column, fenced below); `ta.ADX(dataframe)` (TA-Lib default `timeperiod=14` pinned by call — live both legs); `ta.MACD(dataframe)` (TA-Lib defaults fastperiod 12 / slowperiod 26 / signalperiod 9 pinned by call — `macd`/`macdsignal`/`macdhist` computed but never read by either leg: dead columns, fenced below); `qtpylib.bollinger_bands(dataframe['close'], window=20, stds=2)` returning `mid` into `bb_middleband` (live both legs) with `lower`/`upper` computed but never read (dead columns, fenced below). No volume column is read by any indicator in the gating path (TEMA/SMA/Bollinger read `close` only; ADX reads `high`/`low`/`close` only). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 78 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `cross` (no edge call — every leg is a persistent level/slope state); 0 `volume` (no volume column is ever named or read); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 2 `shift` (the entry rising-slope leg and the exit falling-slope leg — the only lag calls; fixed one-bar offset, no forward reference); 1 `stoploss` attribute (`-0.25`) and 1 `minimal_roi` ladder as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 210-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 2 `buy` / 2 `sell` (old-interface `populate_buy_trend` / `populate_sell_trend` plumbing plus the `buy`/`sell` column writes — mapped to enter-long/exit-long framework reading below, never a second leg). `Dict`, `List`, `hp`, `reduce` are imported; `reduce(` is never called and `hp.` is never called — the single `hyperopt` token is the dead `hp` import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 210-bar researcher warmup pin (covers the 200-bar SMA seed, the 20-bar Bollinger seed, the 14-bar ADX seed, the TEMA9 seed, and the two-bar slope edge with margin); (4) the house cost/capital overlay replaces the absent source economics. Every threshold, every lookback, both slope legs, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `Quickie`, `berlinguyinca/Quickie`, and the `tema < bb_middleband` / `adx > 30` conjunction returns zero strategy records — no record in the pool conjoins a sub-mid rising TEMA9 slope with an ADX30 floor and an SMA200 under-close filter, exited by an over-mid falling TEMA9 slope under an ADX70 ceiling. The pool's lone TEMA-signal record (`forven-tema-cross`, dual-TEMA 12/26 edge-cross on `1h`) is fenced as a different construction in Negative evidence 7 (pure cross pair, no Bollinger rail, no slope leg, no ADX gate, different source family). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a TEMA-slope/Bollinger-mid/ADX/SMA200 system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where lag-reduced momentum turns up from beneath its own mean (TEMA9 below the 20-bar Bollinger midline but rising) while trend strength is confirmed (ADX above 30) yet price still sits beneath its 200-bar average — and stand aside to flat when momentum turns down from above its mean (TEMA9 above the midline but falling) under strong trend (ADX above 70), with a four-rung time-decaying ROI ladder (15% → 6% → 3% → 1%) and a −25% stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 78 lines.

### Research interpretation

Dip-turn momentum catcher with a strength filter, long-only. Unlike pure level systems (oversold print suffices), the entry demands a turning state, not just a cheap state: TEMA9 must be both positioned below its Bollinger midline AND rising bar-over-bar — a falling knife that has not yet turned prints nothing, and a recovery already stretched above its mean prints nothing. Unlike ungated turn systems, two permission keys are required: ADX above 30 (turns inside dead chop are refused) and close beneath SMA200 (turns already extended above the long average are refused — this is a below-average recovery buyer, not a breakout chaser). The exit mirrors the entry with a deliberately harder strength key (ADX above 70): a midline reclaim that rolls over in merely moderate trend holds; only a top-side rollover inside a raging trend surrenders the unit — otherwise the ROI ladder and the stop do the closing. The coded consequence is a buyer of early below-average momentum turns inside confirmed trend that exits only onlate top-side momentum failure, time-decayed profit targets, or the disaster stop.

## Signal

Exact rule as pinned (any other lookback, threshold, window, average family, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
tema[t]   = TA-Lib TEMA(close, 9)
sma200[t] = TA-Lib SMA(close, 200)
adx[t]    = TA-Lib ADX(high, low, close, 14)
bb_mid[t] = Bollinger midline of close, window 20, stds 2
entry = (adx[t] > 30) AND (tema[t] < bb_mid[t])
        AND (tema[t] > tema[t-1]) AND (sma200[t] > close[t])     // buy = 1
exit_sig = (adx[t] > 70) AND (tema[t] > bb_mid[t])
        AND (tema[t] < tema[t-1])                                // sell = 1
risk = time-decaying take-profit minimal_roi {"100": 0.01, "30": 0.03, "15": 0.06, "10": 0.15}; fixed stop at -25% (stoploss -0.25)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar printing the four-conjunct state, `direction` long-only; `sell=1` on bars printing the three-conjunct state. Both legs are STATE prints (while positioned they stay true every qualifying bar — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). Old-interface `buy`/`sell` columns read as enter-long/exit-long (disclosed framework reading, never a second leg).
- Exact boundaries (pinned semantics): strict throughout (`>`, `<` — an ADX landing exactly on 30 or 70, a TEMA exactly on the midline, a flat TEMA bar (`tema[t] == tema[t-1]`), or a close exactly on the SMA200 fires nothing). The `30` / `70` / `9` / `200` / `20` literals are never tuned here.
- Same-bar co-print pin (proved, not asserted): entry demands `tema[t] < bb_mid[t]` with a rising slope while exit demands `tema[t] > bb_mid[t]` with a falling slope on the same bar's single TEMA/midline values — level and slope both mutually exclusive by construction, so a full entry/exit co-print is arithmetically impossible and no fill-ordering invention is ever needed. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the top-side rollover signal exit, the four-rung ROI ladder, and the −25% stop are the complete position-closing set (old-interface `use_sell_signal = True` / `sell_profit_only = False` framework-default reading — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"100"`/`"30"`/`"15"`/`"10"`), preserved verbatim: 15% within the first 10 minutes decaying to 1% after 100 minutes.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying four-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`high`/`low`/`close`, zero volume reads) with fixed non-negative offsets (trailing windows plus the two-bar slope edge — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` for the ADX path, `close` for the TEMA/SMA200/Bollinger path. No volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 210 five-minute bars held flat (~17.5 hours). Covers the 200-bar SMA seed (longest window), the 20-bar Bollinger seed, the 14-bar ADX seed, the TEMA9 seed, and the two-bar slope edge with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, strategy002 hammer-gated oversold, and strategy004 ADX-gated CCI washout records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the four-conjunct entry opens the full unit on a flat book; the rollover signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (78 lines: the MACD/TEMA/SMA/ADX/Bollinger indicator block, the four-conjunct entry with its slope leg, the three-conjunct exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `Quickie(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 210-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>`/`<` fire nothing on equality; a flat TEMA bar (`tema[t] == tema[t-1]`) satisfies neither the entry rising leg nor the exit falling leg. An ADX exactly on 30 or 70, a TEMA exactly on the midline, or a close exactly on the SMA200 holds — disclosed, not smoothed.
3. Co-print arithmetic fenced (proved, not asserted): entry's `tema < bb_mid` plus rising slope and exit's `tema > bb_mid` plus falling slope read one bar's single TEMA/midline values — mutually exclusive on both level and slope, so no co-print can ever reach the engine. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins ADX toward 0/NaN (failing both `> 30` and `> 70`); the Bollinger standard deviation collapses to zero so the midline equals the flat close and the flat TEMA equals it too (both strict level legs fail). No division by zero exists anywhere in the gating path (all legs are comparisons; band-width arithmetic lives inside the library call, never in a gate denominator) — disclosed, not repaired.
5. Dead-column plumbing fenced: `macd`/`macdsignal`/`macdhist` are computed every bar and read nowhere; `sma_50` is a file-literal `SMA(close, 200)` mislabel computed and read nowhere (its 200 period is quoted exactly as shipped, never "corrected" to 50); `bb_lowerband`/`bb_upperband` are computed and read nowhere — display/plumbing leftovers with no gate effect; this record never conditions on them and no reviewer repair may promote any of them into a leg. `Dict`, `List`, `hp`, `reduce` are imported and never called — the single `hyperopt` token is the dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values — disclosed, never repaired into a signal.
6. Derivation-effect fenced: this record computes no behaviour differently from the file's letter — the four adaptations are market choice, fill convention, position/warmup pins, and house economics only. Every threshold, lookback, both slope legs, the ROI ladder, and the stop are verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none conjoins a sub-mid rising TEMA9 slope with an ADX30 floor and an SMA200 under-close filter): the admitted forven-tema-cross sibling trades a bare dual-TEMA 12/26 edge-cross pair on `1h` (cross construction, no Bollinger rail, no slope leg, no ADX gate, different repository family); the admitted freqtrade-adx-momentum sibling gates directional-index crosses with ADX on `1h` (DI-cross construction, no TEMA, no Bollinger, no slope); the admitted strategy004 sibling trades an ADX-gated CCI washout with a dual-STOCHF recross on `5m` (oscillator-washout construction, no TEMA, no Bollinger midline, no slope leg); the admitted freqtrade-hlhb sibling conjoins an RSI-50 edge with an EMA5/10 edge plus ADX>25 on `4h` (edge-cross construction, never a sub-mid slope state). Not a threshold re-tuning of any of them: dropping the slope leg, either ADX key, the midline rail, or the SMA200 filter would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `strategy001.py` through `strategy005.py` (Heikin-Ashi, hammer-gated, Fisher-MFI washout, ADX-gated CCI, and volume-spike samples) and every other `berlinguyinca/*.py` sibling are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the four declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 210-bar warmup floor, house sizing/costs) — all predeclared above. The `5m` frame, the four-conjunct entry with every literal and the slope leg, the three-conjunct exit, the four-rung ROI ladder, the −25% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: four-conjunct entry / all lookbacks, thresholds, slope legs / three-conjunct exit / four-rung ROI / −25% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Slope relevance: replacing the rising-slope leg with the bare level state (`tema < bb_mid` alone, same ADX/SMA200 entry, same exit/risk) must not improve net expectancy; fail ⇒ the turn timing adds nothing over the cheap-position state.
- F2 — Strength-gate relevance: dropping both ADX keys (same TEMA-slope/SMA200 entry, same midline-rollover exit without the ADX70 key, same risk) must not improve net expectancy; fail ⇒ the trend-strength filter adds nothing over the bare slope system.
- F3 — Under-close relevance: dropping the `sma200 > close` conjunct (same TEMA-slope/ADX entry, same exit/risk) must not improve net expectancy; fail ⇒ the below-average positioning adds nothing over the ungated turn system.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume feed is read at all — only standard `high`/`low`/`close` candle fields; no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib TEMA/SMA/ADX internals live in their library outside the pinned file — pinned by call with defaults, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local column wiring, under the disclosed 210-bar floor.
- The MACD triple, the mislabelled `sma_50`, and the Bollinger outer rails are computed and ignored — a reader must not mistake any of them for a gate; none gates anything.
- No trailing, no breakeven, no time exit beyond the ROI clock, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/Quickie.py
- https://github.com/berlinguyinca/freqtrade-strategies
