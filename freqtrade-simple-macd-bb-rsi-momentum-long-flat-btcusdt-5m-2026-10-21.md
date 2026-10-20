---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Simple MACD-BB-RSI momentum long-flat on BTCUSDT 5m bars
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
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/Simple.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Simple MACD-BB-RSI momentum long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-strategy001`, `freqtrade-strategy002`, `freqtrade-strategy003`, `freqtrade-strategy004`, `freqtrade-hlhb`, and `freqtrade-quickie` records — this is only its fifteenth record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/Simple.py`.
- GitHub blob SHA at the pinned commit: `b86dd0c0c46f06b0f9d262531a93df90f1928d15`, size 2648 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2648 bytes, 76 lines, SHA-256 `58953b8bfdff0d15e3a3c88ecec2d63cba094eaac3f4f707d9b4d8bff5579c8a`, identical to the GitHub blob (`git hash-object` reproduces `b86dd0c0…1928d15`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Simple(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/strategy001.py` through `strategy005.py` plus every other `user_data/strategies/berlinguyinca/*.py` sibling are different pins with different constants — this record pins ONLY the Simple literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.25`; entry is the four-way AND of `macd > 0`, `macd > macdsignal`, `bb_upperband > bb_upperband.shift(1)`, `rsi > 70`; exit is `rsi > 80`. The docstring attribution (`author@: Gert Wohlgemuth`, `idea: this strategy is based on the book, 'The Simple Strategy'`, plus an Amazon book URL) is lineage only — no recoverable rule lives in the book link, and no performance, sample, window, trade count, or cost basis ships anywhere in the 76 lines.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.MACD(dataframe)` (TA-Lib defaults fastperiod 12 / slowperiod 26 / signalperiod 9 pinned by call — `macd`/`macdsignal` live both legs, `macdhist` computed but never read: dead column, fenced below); `ta.RSI(dataframe, timeperiod=7)` (explicit 7 — live both legs); `qtpylib.bollinger_bands(dataframe['close'], window=12, stds=2)` returning `upper` into `bb_upperband` (live entry leg) with `lower`/`mid` computed but never read (dead columns, fenced below). No volume column is read by any indicator in the gating path (MACD/RSI/Bollinger read `close` only). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 76 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `cross` (no edge call — entry is a persistent four-state conjunction, exit a persistent level state); 0 `volume` (no volume column is ever named or read); 0 `resample` / 0 `informative` / 0 `request` / 0 `security` / 0 `typical_price` (the band reads `close` directly, unlike the typical-price BbandRsi sibling); 1 `shift` (the rising-upper-band leg — the only lag call; fixed one-bar offset, no forward reference); 1 `stoploss` attribute (`-0.25`) and 1 `minimal_roi` (`{"0": 0.01}`) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 60-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 2 `buy` / 3 `sell` (old-interface `populate_buy_trend` / `populate_sell_trend` plumbing plus the `buy`/`sell` column writes — mapped to enter-long/exit-long framework reading below, never a second leg). `hp` is the dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact. 0 `ema` / 0 `sma` direct calls (smoothing lives only inside the TA-Lib MACD/RSI library calls, never as file-level EMA/SMA gates); 0 `stoch` / 0 `adx` / 0 `cci` / 0 `mfi` / 0 `sar` / 0 `fisher`.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 60-bar researcher warmup pin (covers the MACD 26+9 seed, the 12-bar Bollinger seed, the RSI7 seed, and the two-bar upper-band edge with margin); (4) the house cost/capital overlay replaces the absent source economics. Every threshold, every lookback, the rising-band leg, the ROI rung, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `berlinguyinca/Simple`, `class Simple(`, `timeperiod=7`, and `window=12` returns zero strategy records — no record in the pool uses RSI7 or a 12-bar Bollinger. No record conjoins positive-polarity MACD-above-signal with a rising 12-bar upper band and an RSI70 floor, exited by RSI80. The pool's nearest MACD cousins are fenced as different constructions in Negative evidence 7 (AO-cross edge pair on `1h`; MACD-polarity state with MACD-signal-loss exit on `5m`; oversold typical-price BB20 dip with RSI14 on `1h`). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a MACD/BB-rise/RSI momentum system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where trend momentum is confirmed from three independent angles at once (MACD above zero and above its signal line, the 12-bar upper band itself pointing up bar-over-bar) while short-horizon strength is already hot (RSI7 above 70) — and stand aside to flat when heat turns extreme (RSI7 above 80), with a flat 1% take-profit and a −25% stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 76 lines.

### Research interpretation

Overbought-momentum breakout buyer with an exhaustion exit, long-only. Unlike dip systems (buy cheap prints), the entry demands confirmed heat, not a discount: MACD must be both positive and leading its signal, the volatility envelope must be expanding upward, AND RSI7 must already exceed 70 — a cold tape, a MACD still beneath zero, a flat-or-falling upper band, or merely warm RSI prints nothing. Unlike pure MACD-polarity holders, two extra permission keys are required: the rising upper band (trend must be visibly stretching the envelope, not just sitting above zero) and the RSI70 floor (momentum must be hot on the fast 7-bar clock). The exit is deliberately one notch hotter than the entry (RSI80): heat between 70 and 80 holds the position; only extreme heat, the 1% ROI, or the disaster stop closes it. The coded consequence is a buyer of confirmed hot breakouts that harvests only further overheating, quick scalp profits, or the wide stop.

## Signal

Exact rule as pinned (any other MACD period, RSI length, band window, threshold, shift lookback, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
macd[t], signal[t] = TA-Lib MACD(close, 12, 26, 9)   // defaults pinned by call; hist discarded
rsi7[t]    = TA-Lib RSI(close, 7)                     // Wilder smoothing
bb_up[t]   = Bollinger upper of close, window 12, stds 2
entry = (macd[t] > 0) AND (macd[t] > signal[t])
        AND (bb_up[t] > bb_up[t-1]) AND (rsi7[t] > 70)  // buy = 1
exit_sig = (rsi7[t] > 80)                               // sell = 1
risk = flat take-profit at +1% (minimal_roi {"0": 0.01}); fixed stop at -25% (stoploss -0.25)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar printing the four-conjunct state, `direction` long-only; `sell=1` on bars printing the RSI80 state. Both legs are STATE prints (while positioned they stay true every qualifying bar — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). Old-interface `buy`/`sell` columns read as enter-long/exit-long (disclosed framework reading, never a second leg).
- Exact boundaries (pinned semantics): strict throughout (`>`, never `>=` — a MACD exactly at 0, MACD exactly on its signal, a flat upper band (`bb_up[t] == bb_up[t-1]`), RSI exactly on 70 or 80 fires nothing on that conjunct). The `0` / `70` / `80` / `7` / `12` literals are never tuned here.
- Same-bar co-print pin (possible, resolved by position pin — disclosed, not repaired): entry needs `rsi7 > 70` while exit needs `rsi7 > 80`, so any bar with RSI above 80 that also satisfies the three MACD/band legs prints BOTH legs. No engine ordering is invented: under the single-unit position pin, a flat book treats the bar as entry (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a positioned book treats the bar as exit-close (further entry bars are hold-no-ops). ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the RSI80 signal exit, the flat 1% ROI leg, and the −25% stop are the complete position-closing set (old-interface `use_sell_signal = True` / `sell_profit_only = False` framework-default reading — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying four-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (MACD/RSI/Bollinger all close-sourced) with fixed non-negative offsets (trailing windows plus the two-bar band edge — no forward reference) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `close` for the MACD/RSI7/Bollinger-12 path and all comparisons. No `high`/`low` band-price basis (the band reads `close` directly, not typical price), no volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 five-minute bars held flat (~5 hours). Covers the MACD 26-bar slow seed plus 9-bar signal smoothing (~35 bars effective), the 12-bar Bollinger seed, the RSI7 seed, and the two-bar band edge with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print rule leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, strategy002 hammer-gated oversold, strategy004 ADX-gated CCI washout, and Quickie TEMA-slope records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the four-conjunct entry opens the full unit on a flat book; the RSI80 signal exit, the 1% ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (76 lines: the MACD/RSI/Bollinger indicator block, the four-conjunct entry with its rising-band leg, the RSI80 exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `Simple(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>` fires nothing on equality; a flat upper band (`bb_up[t] == bb_up[t-1]`) satisfies neither entry nor anything else. A MACD exactly at 0 or on its signal, or RSI exactly on 70/80, holds — disclosed, not smoothed.
3. Co-print arithmetic fenced (possible, resolved — disclosed, not repaired): bars with RSI above 80 satisfying all three MACD/band legs print both legs; the position pin resolves them (flat → enter, positioned → exit-close, never a same-bar round-trip). ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins MACD toward 0/NaN (failing `> 0` and the signal comparison), the Bollinger bandwidth to zero (flat upper band fails the rising leg), and RSI toward 50/100 on zero-loss runs (the `> 70`/`> 80` pair is unreachable without a real advance on at least one seeding). No division by zero exists anywhere in the gating path (all legs are comparisons; band-width arithmetic lives inside the library call, never in a gate denominator) — disclosed, not repaired.
5. Dead-column plumbing fenced: `macdhist` is computed every bar and read nowhere; `bb_lowerband`/`bb_middleband` are computed and read nowhere — display/plumbing leftovers with no gate effect; this record never conditions on them and no reviewer repair may promote any of them into a leg. The single `hyperopt` token is the dead `hp` import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values — disclosed, never repaired into a signal.
6. Derivation-effect fenced: this record computes no behaviour differently from the file's letter — the four adaptations are market choice, fill convention, position/warmup pins, and house economics only. Every threshold, lookback, the rising-band leg, the ROI rung, and the stop are verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none conjoins positive MACD-above-signal with a rising 12-bar upper band and an RSI7>70 floor): the admitted freqtrade-awesome-macd sibling trades a bare AO sign-flip edge pair inside MACD polarity on `1h` (edge-cross construction, no RSI, no Bollinger, no level persistence); the admitted freqtrade-asdts-rockwell sibling trades a bare MACD-polarity state exited by signal-line loss on `5m` (no band leg, no RSI leg, different exit); the admitted freqtrade-bband-rsi-dip-buy sibling buys oversold RSI14<30 typical-price BB20 lower-band breaks exited by RSI70 on `1h` (opposite side of the RSI spectrum, different RSI length, different band basis/window, different exit); the admitted strategy003 sibling trades an RSI-Fisher-MFI washout with EMA gating on `5m` (oscillator-washout construction, no MACD polarity, no band-slope leg). Not a threshold re-tuning of any of them: dropping the band-rise leg, either MACD conjunct, or the RSI70 floor would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `strategy001.py` through `strategy005.py` and every other `berlinguyinca/*.py` sibling are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the four declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 60-bar warmup floor, house sizing/costs) — all predeclared above. The `5m` frame, the four-conjunct entry with every literal and the band-rise leg, the RSI80 exit, the 1% ROI rung, the −25% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: four-conjunct entry / all lookbacks, thresholds, band-rise leg / RSI80 exit / 1% ROI / −25% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band-rise relevance: replacing the rising-upper-band leg with the bare MACD-polarity-plus-RSI state (same MACD/RSI entry, same exit/risk) must not improve net expectancy; fail ⇒ the envelope-expansion timing adds nothing over the polarity state.
- F2 — Heat-floor relevance: dropping the RSI70 conjunct (same MACD/band entry, same exit/risk) must not improve net expectancy; fail ⇒ the hot-momentum filter adds nothing over the ungated breakout state.
- F3 — Exhaustion-exit relevance: replacing the RSI80 signal exit with ROI/stop-only exits (same entry, same risk) must not improve net expectancy; fail ⇒ the overheating exit adds nothing over fixed risk alone.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume feed is read at all — only standard `close` candle fields; no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib MACD/RSI internals and the `qtpylib.bollinger_bands` rolling arithmetic live in their libraries outside the pinned file — pinned by call with defaults, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local column wiring, under the disclosed 60-bar floor.
- The MACD histogram and the Bollinger lower/middle bands are computed and ignored — a reader must not mistake any of them for a gate; none gates anything.
- No trailing, no breakeven, no time exit beyond the flat ROI rung, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The Amazon book link is lineage only — no rule in this record is sourced from the book; every literal comes from the pinned `.py` file.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/Simple.py
- https://github.com/berlinguyinca/freqtrade-strategies
