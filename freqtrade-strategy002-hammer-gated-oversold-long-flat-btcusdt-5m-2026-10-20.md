---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade strategy002 hammer-gated oversold quadruple-state long-flat on BTCUSDT 5m bars
created: 2026-10-20
updated: 2026-10-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2018-06-27
sources:
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy002.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade strategy002 hammer-gated oversold quadruple-state long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, and `freqtrade-macd-cci-dip-state` records — this is only its tenth record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/strategy002.py`.
- GitHub blob SHA at the pinned commit: `9f203e98eb66b1f066b2155c87b9129448471e9e`, size 3213 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3213 bytes, 101 lines, SHA-256 `da156b83d24cdcb93411e7a034cd71820d4cbb4b9764d60a092d59578185ccd4`, identical to the GitHub blob (`git hash-object` reproduces `9f203e98…48471e9e`) — the entire file was retrieved and inspected.
- Registration: the file defines class `strategy002(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/strategy001.py` (Heikin-Ashi EMA-cross sample), `strategy003.py` (cross-OR-gated multi-oscillator sample), `strategy004.py`, and `strategy005.py`, plus every `user_data/strategies/berlinguyinca/*.py` sibling, are different pins with different constants — this record pins ONLY the strategy002 literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.3`; entry is the four-way AND of `rsi < 30`, `slowk < 20`, `bb_lowerband > close`, `CDLHAMMER == 100`; exit is the two-way AND of `sar > close`, `fisher_rsi > 0.3`. The docstring attribution (`author@: Gerald Lonlas`, `github@: https://github.com/freqtrade/freqtrade-strategies`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 101 lines.
- Out-of-file calls pinned (all resolved by name, all standard TA-Lib/vendor defaults): `ta.STOCH(dataframe)` (TA-Lib defaults pinned by call — fastk 5, slowk 3, slowd 3; only the `slowk` leg is read); `ta.RSI(dataframe)` (TA-Lib default `timeperiod=14` pinned by call); `ta.SAR(dataframe)` (TA-Lib defaults pinned by call — acceleration 0.02, maximum 0.2); `ta.CDLHAMMER(dataframe)` (TA-Lib integer pattern code, `0` or `100` — the file's own comment prints `values [0, 100]`); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` returning the `lower` entry only (typical price `(high+low+close)/3`; the vendor call is pinned by call — its internal rolling arithmetic lives outside this file and is disclosed as such, never re-derived here). The inverse-Fisher warp `fisher_rsi = (exp(2*r)-1)/(exp(2*r)+1)` with `r = 0.1*(rsi-50)` is fully visible file-local arithmetic. No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 101 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — both legs are persistent states, never one-bar edges); 0 `volume` (no volume read of any kind — Stoch/RSI/BB/SAR/Hammer/Fisher all read OHLC only); 0 `shift` (no lag call — per-bar state evaluation under the file's own framework contract); 1 `stoploss` attribute (`-0.3`) and 1 `minimal_roi` ladder as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`. `Dict`, `List`, `hp`, `reduce`, and `numpy` are imported; only `numpy.exp` is called (inside the visible Fisher warp) — the single `hyperopt` token is the dead `hp` import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.

Pre-write dedup (2026-10-20): working-tree filename/content search for `strategy002`, `CDLHAMMER`, `fisher_rsi`, and the `rsi < 30 & slowk < 20 & lower-band & hammer` conjunction returns zero strategy records. Case-insensitive `slowk` pool hits (`SlowK` inside the slow-stochastic-14-3 regime-recross and forven-stochastic-k20-recross records) trade recross-edge events two-sided/`1d` or dual-exit `1h` — never this level-state conjunction; the lone `Strategy001` pool hit is FMZ-page boilerplate inside an unrelated engulfing record, never this file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a hammer-gated oversold signal. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none trades an exact TA-Lib hammer print ANDed with RSI, stochastic-%K, and lower-band penetration with a SAR-plus-Fisher-level signal exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy an oversold dip confirmed four ways — RSI under 30, stochastic %K under 20, close pierced through the lower Bollinger band, and an exact TA-Lib hammer print on the bar — and stand aside to flat when the Parabolic SAR flips above the close while the inverse-Fisher-warped RSI reads above 0.3, with a four-rung time-decaying ROI ladder (5% → 4% → 3% → 1%) and a −30% disaster stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 101 lines.

### Research interpretation

Pattern-gated dip-catching machine, long-only. Unlike pure level systems (an RSI-BB double fires on any soft drift through the band), the hammer conjunct demands the market print a textbook rejection-shaped bar on the entry bar itself — the pattern is the trigger, the three oscillator/band legs are the oversold context. Unlike breakout records (upper-rail breaks bought for continuation), this leg buys penetration weakness only when the bar shape already shows rejection. The exit is the mirror discipline: SAR above close means the trailing stop-dot has flipped overhead, and Fisher above 0.3 means warped momentum has normalized — both must agree, so a SAR flip during still-depressed momentum holds, and a momentum pop under a still-supportive SAR holds. The coded consequence is a buyer of hammer-marked band breaks that harvests normalization only when trend-dot and warped momentum agree it arrived.

## Signal

Exact rule as pinned (any other lookback, threshold, pattern code, ROI rung, stop, fill, frame, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
slowk[t]      = TA-Lib STOCH slowk (defaults: fastk 5, slowk-ma 3, slowd-ma 3)
rsi[t]        = TA-Lib RSI(close, 14)
fisher_rsi[t] = (exp(2*r[t])-1)/(exp(2*r[t])+1), r[t] = 0.1*(rsi[t]-50)
bb_lower[t]   = qtpylib BB(20, 2) over typical price (lower only)
sar[t]        = TA-Lib SAR(high, low; accel 0.02, max 0.2)
hammer[t]     = TA-Lib CDLHAMMER in {0, 100}
entry = (rsi[t] < 30) AND (slowk[t] < 20) AND (bb_lower[t] > close[t]) AND (hammer[t] == 100)   // buy = 1
exit_sig = (sar[t] > close[t]) AND (fisher_rsi[t] > 0.3)                                        // sell = 1
risk = time-decaying take-profit minimal_roi {"60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05}; fixed stop at -30% (stoploss -0.3)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar where all four conjuncts print, `direction` long-only; `sell=1` on bars where SAR sits above close with Fisher above 0.3. Both legs are STATE levels (while positioned they stay true every qualifying bar — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code).
- Exact boundaries (pinned semantics): entry is strict throughout (`<`, `>`, `==` — an RSI landing exactly on 30, a %K exactly on 20, a close exactly on the band, or a non-hammer bar fires nothing); the exit is strict throughout (`>` — SAR exactly on close or Fisher exactly on 0.3 holds). The `30` / `20` / `0.3` / `100` literals are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `rsi[t] < 30`, which caps the Fisher warp at `(e^-4-1)/(e^-4+1) ≈ -0.964`; exit needs `fisher_rsi[t] > 0.3`, which needs `rsi[t]` above ≈ 53. The two RSI regions (`< 30` vs `> ~53`) are strictly disjoint on every bar — entry and signal-exit never co-print, and ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the SAR-plus-Fisher signal exit, the four-rung ROI ladder, and the −30% stop are the complete position-closing set. No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"60"`/`"30"`/`"20"`/`"0"`), preserved verbatim.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying four-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`close` for RSI/Fisher/BB/SAR, `high`/`low` inside typical price and SAR, `open` inside the hammer pattern call) with fixed non-negative offsets — no volume read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `open`/`high`/`low`/`close` for the Stoch/RSI/Fisher/BB/SAR/hammer path. No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; all windows (20-bar bands, 14-bar RSI, ~11-bar Stoch chain, SAR recursion, single-bar pattern) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 five-minute bars held flat. Covers the 20-bar band seed, the 14-bar RSI seed plus its Fisher warp, the ~11-bar Stoch slowk chain, and SAR recursion settling with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early); the hammer call prints 0 without a pattern. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state and MACDStrategy MACD-CCI dip-state records, both `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the four-conjunct entry opens the full unit on a flat book; the SAR-plus-Fisher signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (101 lines: the STOCH/RSI/Fisher/BB/SAR/hammer indicator block, the four-conjunct entry, the two-conjunct exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `strategy002(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fire nothing on equality; the hammer leg admits only the exact integer `100`. An RSI exactly on 30, a %K exactly on 20, a close exactly on the band, SAR exactly on close, or Fisher exactly on 0.3 holds — disclosed, not smoothed.
3. Entry/exit disjointness fenced arithmetically (not by assertion): any entry bar has `fisher_rsi ≤ −0.96` by the RSI cap, so the `> 0.3` exit conjunct is false on that bar by construction — no priority choice exists anywhere. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins band width at 0 with `lower == mid == close`, failing the strict `lower > close` conjunct — no entry; exit needs strict SAR-above-close. No division by zero exists anywhere (all guards are comparisons; the Fisher warp's denominator `exp(2r)+1` is strictly positive) — disclosed, not repaired.
5. Dead-import plumbing fenced: `Dict`, `List`, `hp`, `reduce` are imported and never called — display/plumbing leftovers with no gate effect. The single `hyperopt` token is that dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values — disclosed, never repaired into a signal.
6. SAR seeding fenced: TA-Lib SAR recursion settles within a handful of bars; the 40-bar floor keeps any early-bar SAR instability out of trusted events — disclosed, not repaired.
7. Cousin records fenced as different constructions (none trades an exact hammer print ANDed with RSI, stochastic-%K, and lower-band penetration with a SAR-plus-Fisher-level exit): the admitted freqtrade-bband-rsi sibling fires an RSI-and-band double with no pattern, no stochastic, and no signal exit; the admitted wick-reversal-hammer sibling trades wick-dominance fractions plus a 15-bar momentum context on `1d` (geometric construction, never the TA-Lib integer pattern code); the admitted combo-123-fisher sibling gates on Fisher *slope* agreement two-sided on `4h` (never a Fisher *level* exit leg); the admitted forven-parabolic-sar-cross sibling trades a SAR *cross edge* (never a SAR *level* exit); the admitted slow-stochastic and forven-stochastic-k20 siblings trade stochastic *recross edges* (never a `slowk < 20` level state). Not a threshold re-tuning of any of them: dropping the hammer conjunct, softening any level, or swapping an edge for a state would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `strategy001.py` (Heikin-Ashi synthetic-series EMA-cross sample), `strategy003.py` (cross-OR-gated multi-oscillator sample), `strategy004.py`, `strategy005.py`, and every `berlinguyinca/*.py` sibling are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor, and house sizing/costs — all predeclared above. The `5m` frame, the four-conjunct entry with all thresholds, the two-conjunct exit, the four-rung ROI ladder, the −30% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: four-conjunct entry / all lookbacks, thresholds, pattern code / two-conjunct exit / four-rung ROI / −30% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Hammer relevance: dropping the `CDLHAMMER == 100` conjunct (same levels/exit/risk) must not improve net expectancy; fail ⇒ the pattern print adds nothing over its oscillator/band context.
- F2 — Stochastic relevance: dropping the `slowk < 20` conjunct (same entry/exit/risk) must not improve net expectancy; fail ⇒ the %K leg adds nothing over its RSI/band/hammer context.
- F3 — Exit-agreement relevance: honoring either exit conjunct alone (same entry/risk) must not improve net expectancy; fail ⇒ the SAR-plus-Fisher agreement adds nothing over a single-leg exit.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume read exists, so no venue volume-definition dependence. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib STOCH/RSI/SAR/CDLHAMMER and qtpylib BB(20, 2)/typical-price internals live in their libraries outside the pinned file — pinned by call with defaults, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local Fisher arithmetic, under the disclosed 40-bar floor.
- No trailing, no breakeven, no time exit beyond the ROI clock, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy002.py
- https://github.com/berlinguyinca/freqtrade-strategies
