---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade strategy004 ADX-gated CCI washout dual-stoch recross long-flat on BTCUSDT 5m bars
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
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy004.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade strategy004 ADX-gated CCI washout dual-stoch recross long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, and `freqtrade-strategy002` records — this is only its eleventh record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/strategy004.py`.
- GitHub blob SHA at the pinned commit: `00ba79d2152170634660a1902413d3fd96880029`, size 4083 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4083 bytes, 120 lines, SHA-256 `2274250b7cb6215911fdb5c6f6fb707c8532d1ac45872a84cb2ad184c0bb65c9`, identical to the GitHub blob (`git hash-object` reproduces `00ba79d2…680029`) — the entire file was retrieved and inspected.
- Registration: the file defines class `strategy004(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/strategy001.py`, `strategy002.py`, `strategy003.py`, and `strategy005.py`, plus every `user_data/strategies/berlinguyinca/*.py` sibling, are different pins with different constants — this record pins ONLY the strategy004 literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.3`; entry is the nine-way AND of `(adx > 50) | (slowadx > 26)`, `cci < -100`, `fastk-previous < 20`, `fastd-previous < 20`, `slowfastk-previous < 30`, `slowfastd-previous < 30`, `fastk-previous < fastd-previous`, `fastk > fastd`, `mean-volume > 0.75`, `close > 0.00000100`; exit is the four-way AND of `slowadx < 25`, `(fastk > 70) | (fastd > 70)`, `fastk-previous < fastd-previous`, `close > ema5`. The docstring attribution (`author@: Gerald Lonlas`, `github@: https://github.com/freqtrade/freqtrade-strategies`, `How to use it? > python3 ./freqtrade/main.py -s Strategy004`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 120 lines.
- Out-of-file calls pinned (all resolved by name, all standard TA-Lib defaults): `ta.ADX(dataframe)` (default `timeperiod=14` pinned by call); `ta.ADX(dataframe, 35)` (explicit 35); `ta.CCI(dataframe)` (default `timeperiod=20` pinned by call); `ta.STOCHF(dataframe, 5)` (fast stoch — TA-Lib defaults fastk_period 5 / fastd_period 3); `ta.STOCHF(dataframe, 50)` (slow stoch — fastk_period 50 / fastd_period 3); `ta.EMA(dataframe, timeperiod=5)` (explicit 5). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 120 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — the fast-stoch turn is a hand-rolled `shift(1)` alignment flip, a persistent state pair, never a one-bar edge call); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 1 `stoploss` attribute (`-0.3`) and 1 `minimal_roi` ladder as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 60-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 2 `volume` (the leaking mean-floor line plus its entry read — the sole derivation site, repaired below); 4 `shift` (all `shift(1)` prior-bar reads — causal lags, never negative); `Dict`, `List`, `hp`, `reduce` are imported and never called — zero `hp.` calls, zero `reduce(` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file's `dataframe['mean-volume'] = dataframe['volume'].mean()` is a full-sample scalar (it reads future bars — gate-6 leakage as written, and no causally computable reading preserves its exact events). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 60-bar researcher warmup pin (covers the 50-bar slow-stoch seed, the 35-bar slow-ADX seed, the 20-bar CCI seed, and the one-bar `shift(1)` lag); (4) the house cost/capital overlay replaces the absent source economics; (5) the causal volume-floor repair — `mean-volume[t]` is `volume.rolling(30).mean().shift(1)` evaluated at the entry threshold `0.75`, verbatim. The 30-bar window follows the admitted EMASkipPump sibling's causal volume-guard window from this same repository family (disclosed precedent, never a source fact); the `0.75` literal, every other threshold, every lookback, the ROI ladder, and the stop are untouched. The dust filter `close > 0.00000100` is kept verbatim (causal as written, degenerate-always-true on BTCUSDT — fenced, never repaired).

Pre-write dedup (2026-10-20): working-tree filename/content search for `strategy004`, `slowadx`, `slowfastk`, `fastk-previous`, and `STOCHF` returns zero strategy records — no record in the pool reads dual fast/slow STOCHF stacks, a 35-period slow ADX, or this nine-conjunct entry. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades an ADX-gated CCI-plus-dual-stoch signal. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none conjoins an ADX(14)/slow-ADX(35) regime gate, a CCI<−100 washout, a doubly-oversold fast-STOCHF(5) recross, and a slow-STOCHF(50) oversold context with a regime-collapse exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where trend strength is certified (ADX(14) above 50 or slow ADX(35) above 26) while the tape prints a washout (CCI under −100) and the fast stochastic turns up out of a doubly-oversold prior bar (both fast %K/%D under 20) inside a slow-stochastic oversold context (both slow legs under 30), on a bar clearing a volume floor and a dust-price floor — and stand aside to flat when the regime collapses (slow ADX under 25) while the fast stochastic reads overbought (either leg above 70) from a bearish-aligned prior bar with price above its 5-bar EMA, with a four-rung time-decaying ROI ladder (5% → 4% → 3% → 1%) and a −30% disaster stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 120 lines.

### Research interpretation

Regime-certified washout-fade machine, long-only. Unlike bare CCI-dip records (fire on any −100 print, blind to trend context), the ADX gate demands certified trend strength first — chop prints nothing even at deep CCI. Unlike single-stochastic recross records (trade one oscillator's turn), the turn must fire inside a slow-STOCHF(50) oversold context — a fast wiggle in a calm slow backdrop prints nothing. Unlike cross-edge records, no edge primitive is ever called: the "recross" is a hand-rolled prior-vs-current alignment flip (`fastk-previous < fastd-previous` AND `fastk > fastd`), a persistent two-bar state re-evaluated per bar. The exit is the mirror discipline with teeth: it fires only after the regime itself collapses (slow ADX under 25) — a merely overbought stochastic inside a still-strong regime holds the book until ROI or the −30% stop. The coded consequence is a buyer of certified-trend washouts that surrenders only when the trend receipt expires.

## Signal

Exact rule as pinned (any other lookback, threshold, window, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own, except the `meanvol` repair which is the declared derivation:

```text
adx[t]       = TA-Lib ADX(high, low, close, 14)
slowadx[t]   = TA-Lib ADX(high, low, close, 35)
cci[t]       = TA-Lib CCI(high, low, close, 20)
fastk[t], fastd[t]         = TA-Lib STOCHF(close windows; fastk 5, fastd 3)
slowfastk[t], slowfastd[t] = TA-Lib STOCHF(close windows; fastk 50, fastd 3)
ema5[t]      = TA-Lib EMA(close, 5)
meanvol[t]   = volume.rolling(30).mean().shift(1)   // DERIVED causal repair (see Provenance)
entry = ((adx[t] > 50) OR (slowadx[t] > 26)) AND (cci[t] < -100)
        AND (fastk[t-1] < 20) AND (fastd[t-1] < 20)
        AND (slowfastk[t-1] < 30) AND (slowfastd[t-1] < 30)
        AND (fastk[t-1] < fastd[t-1]) AND (fastk[t] > fastd[t])
        AND (meanvol[t] > 0.75) AND (close[t] > 0.00000100)        // buy = 1
exit_sig = (slowadx[t] < 25) AND ((fastk[t] > 70) OR (fastd[t] > 70))
        AND (fastk[t-1] < fastd[t-1]) AND (close[t] > ema5[t])     // sell = 1
risk = time-decaying take-profit minimal_roi {"60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05}; fixed stop at -30% (stoploss -0.3)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar printing the nine-conjunct state, `direction` long-only; `sell=1` on bars printing the four-conjunct regime-collapse state. Both legs are STATE prints (while positioned they stay true every qualifying bar — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code).
- Exact boundaries (pinned semantics): strict throughout (`>`, `<` — an ADX landing exactly on 50, a slow ADX exactly on 26/25, a CCI exactly on −100, a stochastic leg exactly on its level, or a close exactly on the EMA5/dust line fires nothing). The `50` / `26` / `25` / `−100` / `20` / `30` / `70` / `0.75` / `0.00000100` literals are never tuned here.
- Same-bar co-print pin (predeclared, framework-default reading): the entry's `(adx > 50) | (slowadx > 26)` arm and the exit's `slowadx < 25` arm overlap only through the `adx > 50 & slowadx < 25` corner, and a full co-print additionally needs a one-bar `<20 → >70` fast-stoch jump inside a `cci < −100` bar with `close > ema5` — pathological by construction. Should it ever print, the bar resolves to the exit leg (Freqtrade sell-side precedence: a bar co-printing both legs opens nothing new — disclosed framework-default reading, never a file literal). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the regime-collapse signal exit, the four-rung ROI ladder, and the −30% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"60"`/`"30"`/`"20"`/`"0"`), preserved verbatim.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying nine-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`high`/`low`/`close` for ADX/CCI/EMA, `close` for both STOCHF stacks, `volume` for the repaired trailing floor) with fixed non-negative offsets (trailing windows plus one `shift(1)` lag — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` for the ADX/CCI/EMA path, `close` for both STOCHF stacks, `volume` for the repaired 30-bar trailing floor. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only — the volume floor is additionally `shift(1)`-lagged, so it never sees the decision bar's own volume average; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 five-minute bars held flat. Covers the 50-bar slow-stoch seed (longest window), the 35-bar slow-ADX seed, the 20-bar CCI seed, and the one-bar `shift(1)` lag with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print pin leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, and strategy002 hammer-gated oversold records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the nine-conjunct entry opens the full unit on a flat book; the regime-collapse signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (120 lines: the ADX/CCI/dual-STOCHF/EMA indicator block, the nine-conjunct entry, the four-conjunct exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `strategy004(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>`/`<` fire nothing on equality; the dust leg admits only closes strictly above `0.00000100`. An ADX exactly on 50, a slow ADX exactly on 26 or 25, a CCI exactly on −100, a stochastic leg exactly on its level, or a close exactly on EMA5 holds — disclosed, not smoothed.
3. Co-print arithmetic fenced (not by assertion): a full entry/exit co-print needs `adx > 50 & slowadx < 25` with a one-bar sub-20-to-over-70 fast-stoch jump inside a `cci < −100` bar with `close > ema5` — outside reachable tape by construction, and the predeclared sell-precedence pin binds regardless. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins ADX near 0 (failing both regime arms — no entry, and `slowadx < 25` alone never suffices for exit without the overbought-plus-EMA legs); CCI prints 0 (failing `< −100`); stochastics pin at midscale (failing both the sub-20/sub-30 entry context and the over-70 exit leg). No division by zero exists anywhere (all guards are comparisons) — disclosed, not repaired.
5. Dead-import plumbing fenced: `Dict`, `List`, `hp`, `reduce` are imported and never called — display/plumbing leftovers with no gate effect. The single `hyperopt` token is that dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values — disclosed, never repaired into a signal.
6. Derivation-effect fenced: the only behaviour this record computes differently from the file's letter is the volume floor (trailing 30-bar lagged mean vs the file's incomputable full-sample scalar). The `0.75` literal is preserved; no other threshold, lookback, rung, or leg is altered; the repaired floor is fully specified above, so no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none trades an ADX-regime-gated CCI washout with a dual-STOCHF recross entry and a regime-collapse exit): the admitted freqtrade-macd-cci-dip-state sibling conjoins MACD polarity with CCI ±states on `5m` (no ADX, no stochastic, symmetric exit); the admitted freqtrade-cmcwinner sibling trades a CCI+MFI+CMO prior-bar triple state on `15m` (no ADX, no stochastic, mirrored exit); the admitted freqtrade-adx-momentum sibling conjoins ADX(14) with ±DI(25) dominance and MOM(14) polarity on `1h` (no CCI, no stochastic, momentum-flip exit); the admitted forven-stochastic-k20 sibling trades a raw-FastK 20-recross with a dual exit on `1h` (no ADX, no CCI, no slow-stoch context); the admitted cci-threshold sibling trades a pure single-oscillator CCI threshold-cross two-sided on `4h` (no ADX, no stochastic, reversal exits); the open-PRs AdxSmas sibling trades an ADX-gated SMA3/6 cross on `1h` (edge, never a washout state). Not a threshold re-tuning of any of them: dropping the ADX gate, the CCI leg, either stoch stack, or the regime-collapse exit would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `strategy001.py` (Heikin-Ashi synthetic-series sample), `strategy002.py` (hammer-gated quadruple-state sample), `strategy003.py` (cross-OR-gated multi-oscillator sample), `strategy005.py` (volume-spike SMA40 Fisher-gated sample), and every `berlinguyinca/*.py` sibling are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 60-bar warmup floor, house sizing/costs, and the causal volume-floor repair) — all predeclared above. The `5m` frame, the nine-conjunct entry with all other literals, the four-conjunct exit, the four-rung ROI ladder, the −30% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: nine-conjunct entry / all lookbacks, thresholds, pattern literals / four-conjunct exit / four-rung ROI / −30% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills / 30-bar lagged volume floor are frozen.

- F1 — Slow-context relevance: dropping both slow-STOCHF(50) sub-30 conjuncts (same ADX/CCI/fast-stoch entry, same exit/risk) must not improve net expectancy; fail ⇒ the slow oversold context adds nothing over the fast turn.
- F2 — Regime-gate relevance: dropping the `(adx > 50) | (slowadx > 26)` arm (same washout/stoch entry, same exit/risk) must not improve net expectancy; fail ⇒ the ADX certification adds nothing over the bare washout-plus-turn.
- F3 — Exit-collapse relevance: replacing the regime-collapse exit with an overbought-plus-EMA exit alone (same entry/risk) must not improve net expectancy; fail ⇒ demanding regime expiry adds nothing over a bare stochastic exit.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Volume is a standard candle field on the venue; no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib ADX/CCI/STOCHF/EMA internals live in their library outside the pinned file — pinned by call with defaults, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local arithmetic, under the disclosed 60-bar floor.
- No trailing, no breakeven, no time exit beyond the ROI clock, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The file's full-sample volume mean is not executed anywhere in this record (gate-6 leakage as written) — the only executable volume semantic is the declared trailing repair; a reviewer must never silently swap the global mean back in.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy004.py
- https://github.com/berlinguyinca/freqtrade-strategies
