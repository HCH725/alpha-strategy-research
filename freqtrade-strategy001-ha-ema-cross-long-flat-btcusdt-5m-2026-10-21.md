---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade strategy001 Heikin-Ashi EMA-cross trend-state long-flat on BTCUSDT 5m bars
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
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy001.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade strategy001 Heikin-Ashi EMA-cross trend-state long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-strategy002`, and `freqtrade-strategy004` records — this is only its twelfth record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/strategy001.py`.
- GitHub blob SHA at the pinned commit: `aafccb8a2c708411bd30e733fbc535a2c45d8aea`, size 3008 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3008 bytes, 92 lines, SHA-256 `66252e5b53158d50f950e9ade84817c102904dd38cf9c0b4adceee9576afa0e4`, identical to the GitHub blob (`git hash-object` reproduces `aafccb8a…d8aea`) — the entire file was retrieved and inspected.
- Registration: the file defines class `strategy001(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/strategy002.py`, `strategy003.py`, `strategy004.py`, and `strategy005.py`, plus every `user_data/strategies/berlinguyinca/*.py` sibling, are different pins with different constants — this record pins ONLY the strategy001 literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.3`; entry is the three-way AND of `crossed_above(ema20, ema50)`, `ha_close > ema20`, `ha_open < ha_close` (green bar); exit is the three-way AND of `crossed_above(ema50, ema100)`, `ha_close < ema20`, `ha_open > ha_close` (red bar). The docstring attribution (`author@: Gerald Lonlas`, `github@: https://github.com/freqtrade/freqtrade-strategies`, `How to use it? > python3 ./freqtrade/main.py -s Strategy001`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 92 lines.
- Framework calls pinned (all resolved against the contemporaneous first-party Freqtrade commit `d5ad066f8d4af30340da2e12eaef61a88bf48224` dated `2018-06-27`, one calendar day from the strategy pin): `qtpylib.crossed_above(s1, s2)` is `(s1[t] > s2[t]) & (s1[t-1] <= s2[t-1])` — a one-bar edge admitting equality on the prior bar; `qtpylib.heikinashi(bars)` sets `ha_close[t] = (open+high+low+close)[t]/4`, seeds `ha_open` at `open[0]`, then iterates `ha_open[t] = (ha_open[t-1]+ha_close[t-1])/2` — a causal recursion over completed bars and its own past, no future read; `ta.EMA(dataframe, timeperiod=N)` for N in 20/50/100 follows the lane's close-input convention (same reading as the ten admitted siblings from this repository family). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 92 lines this cycle): 0 `short` (case-insensitive — no short leg anywhere); 2 `crossed_above` (exactly the entry and exit edges, no other edge call); 0 `volume` (the order-gating path never reads volume at all — no leakage site exists, unlike the strategy004/005 siblings); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 1 `stoploss` attribute (`-0.3`) and 1 `minimal_roi` ladder as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 110-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage`; 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 4 `heikinashi` (one import-adjacent call plus its three column reads); 12 `EMA` (three indicator assignments plus their entry/exit reads); `Dict`, `List`, `hp`, `reduce` are imported and never called — zero `hp.` calls, zero `reduce(` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.

**Source-native declaration (read before review):** this record reproduces the source rules losslessly — every window reads trailing completed-bar OHLC with non-negative offsets only, so no derivation or repair exists anywhere in this file (the strategy004 sibling's volume-floor repair has no counterpart here: there is no volume read to repair). The only non-source-native behaviours are the five standard predeclared researcher pins shared with the admitted siblings (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with a 110-bar warmup floor, and house sizing/costs) — all disclosed before review, none invented at review.

Pre-write dedup (2026-10-21): working-tree filename/content search for `strategy001` returns only sibling-file fences (strategy002/004 records fence `strategy001.py` as a separate Heikin-Ashi EMA-cross pin whose constants must never be substituted — explicit non-coverage) and FMZ-page boilerplate (`fpemehd Strategy001`) inside the unrelated dual-ema-engulfing record; content search for `ha_close.*ema20` and `crossed_above(.*ema20` returns zero strategy records — no record in the pool conjoins an EMA20/50 cross edge with a Heikin-Ashi green state, or an EMA50/100 cross edge with a Heikin-Ashi red state. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a Heikin-Ashi EMA-cross signal. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none conjoins cross edges with Heikin-Ashi color states under an ROI ladder plus disaster stop. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where a fresh trend impulse prints (EMA20 crossing above EMA50) while the Heikin-Ashi tape confirms trend color (green bar closing above EMA20) — and stand aside to flat when the slow trend itself turns (EMA50 crossing above EMA100) while the Heikin-Ashi tape flips red below EMA20, with a four-rung time-decaying ROI ladder (5% → 4% → 3% → 1%) and a −30% disaster stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 92 lines.

### Research interpretation

Edge-gated Heikin-Ashi trend-state machine, long-only. Unlike bare EMA-cross records (fire on any cross, blind to candle structure), the Heikin-Ashi color legs demand the synthetic tape agree with the cross on the same bar — a golden cross printing inside a red Heikin-Ashi bar buys nothing. Unlike pure Heikin-Ashi flip records (trade every color change), nothing fires without a fresh cross edge — an already-green tape with an old cross holds flat until the next impulse. Unlike level-state records, both legs are one-bar edges: a qualifying bar that fails either color leg is gone forever, never re-fires. The exit is the slow mirror with teeth: it waits for the EMA50/100 golden cross (a slow-trend event, far rarer than the entry edge) confirmed by a red bar under EMA20 — a merely red bar without the slow cross holds the book until ROI or the −30% stop. The coded consequence is a buyer of edge-fresh Heikin-Ashi-confirmed impulses that surrenders only when the slow trend receipt itself expires.

## Signal

Exact rule as pinned (any other lookback, threshold, edge/level choice, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; framework primitives expand to their pinned contemporaneous definitions:

```text
ema20[t]  = TA-Lib EMA(close, 20)
ema50[t]  = TA-Lib EMA(close, 50)
ema100[t] = TA-Lib EMA(close, 100)
ha_close[t] = (open[t]+high[t]+low[t]+close[t])/4
ha_open[0..1] = open[0]; ha_open[t>=1] = (ha_open[t-1]+ha_close[t-1])/2
xab(a,b)[t] = (a[t] > b[t]) AND (a[t-1] <= b[t-1])      // pinned crossed_above
entry = xab(ema20,ema50)[t] AND (ha_close[t] > ema20[t])
        AND (ha_open[t] < ha_close[t])                   // buy = 1, green bar
exit_sig = xab(ema50,ema100)[t] AND (ha_close[t] < ema20[t])
        AND (ha_open[t] > ha_close[t])                   // sell = 1, red bar
risk = time-decaying take-profit minimal_roi {"60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05}; fixed stop at -30% (stoploss -0.3)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on bars printing the three-conjunct entry edge-state, `direction` long-only; `sell=1` on bars printing the three-conjunct exit edge-state. Both legs are EDGE-gated (each fires only on its cross bar — a cross bar whose color legs fail never re-fires; no one-shot latch, no level hold anywhere in code).
- Exact boundaries (pinned semantics): strict `>` on current bars with `<=` admitted on the prior bar per the pinned `crossed_above` expansion — an EMA20 landing exactly on EMA50 on the current bar fires nothing, while touching from below on the prior bar still arms the edge; Heikin-Ashi equality (`ha_open == ha_close`, a doji) satisfies neither color leg — it can neither complete an entry nor an exit. The `20` / `50` / `100` lookbacks, the four ROI rungs, and the stop literal are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `ha_open[t] < ha_close[t]` (strict green) while exit needs `ha_open[t] > ha_close[t]` (strict red) on the same bar — the two color regions are strictly disjoint, so entry and signal-exit never co-print even if both cross edges fire on one bar, and ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the slow-cross-plus-red signal exit, the four-rung ROI ladder, and the −30% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"60"`/`"30"`/`"20"`/`"0"`), preserved verbatim.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying three-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`open`/`high`/`low`/`close` for the Heikin-Ashi transform, `close` for the three EMA seeds) with fixed non-negative offsets (trailing windows plus one `shift(1)` lag inside each edge — no forward reference) — no volume read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The computed `ha_high`/`ha_low` columns are never read by any order line (display leftovers — fenced, not repaired). Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `open`/`high`/`low`/`close` only — for the Heikin-Ashi transform (all four) and the three EMA seeds (`close`). No volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 110 five-minute bars held flat. Covers the 100-bar EMA seed (longest window), the one-bar edge lag, and the Heikin-Ashi recursion seed with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, strategy002 hammer-gated oversold, and strategy004 ADX-gated CCI washout records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one; the Heikin-Ashi transform is deterministic arithmetic over those same completed candles (the admitted forven-heikin-ashi-color-change record already establishes Heikin-Ashi computability as an engine-compatible transform). Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the entry edge opens the full unit on a flat book; the signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (92 lines: the EMA/Heikin-Ashi indicator block, the three-conjunct entry, the three-conjunct exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `strategy001(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 110-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict current-bar `>` fires nothing on equality while the pinned edge admits prior-bar `<=`; a Heikin-Ashi doji (`ha_open == ha_close`) satisfies neither color leg — disclosed, not smoothed.
3. Co-print arithmetic fenced (proven, not asserted): entry and signal-exit need strictly opposite Heikin-Ashi colors on the same bar — mutually exclusive by construction, and the predeclared sell-precedence convention of the lane binds regardless. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins all three EMAs equal (both `crossed_above` edges false — the prior-bar `<=` arm holds but the current-bar `>` arm fails); Heikin-Ashi prints a doji (both color legs false). No division by zero exists anywhere (all guards are comparisons) — disclosed, not repaired.
5. Dead-import plumbing fenced: `Dict`, `List`, `hp`, `reduce` are imported and never called — display/plumbing leftovers with no gate effect. The single `hyperopt` token is that dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values — disclosed, never repaired into a signal.
6. Dead-column plumbing fenced: `ha_high`/`ha_low` are computed by the pinned `heikinashi` and never read by any order line — disclosed, never repaired into a gate.
7. Cousin records fenced as different constructions (none conjoins cross edges with Heikin-Ashi color states under an ROI ladder plus stop): the admitted forven-heikin-ashi-color-change sibling trades a pure red-to-green flip with two-green confirmation on `1h` (no EMA, no cross edge, first-red exit); the admitted heikin-ashi-ema-trend-state sibling latches an EMA77-of-Heikin-Ashi double-smooth trend two-sided always-in-market on `1d` (never an edge, never flat, reversal-only exits); the admitted freqtrade-strategy002 sibling conjoins a TA-Lib hammer with RSI/slow-stoch/BB levels on `5m` (no EMA, no Heikin-Ashi, SAR-plus-Fisher exit); the admitted ema-20-50-cross sibling (if cited) trades a bare EMA cross without any Heikin-Ashi state. Not a threshold re-tuning of any of them: dropping either cross edge, either color leg, or the `ha_close`-vs-`ema20` confirmation would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `strategy002.py` (hammer-gated quadruple-state sample), `strategy003.py` (cross-OR-gated multi-oscillator sample), `strategy004.py` (ADX-gated CCI washout sample), `strategy005.py` (volume-spike SMA40 Fisher-gated sample), and every `berlinguyinca/*.py` sibling are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five standard pins (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 110-bar warmup floor, and house sizing/costs) — all predeclared above. The `5m` frame, the three-conjunct entry with all lookbacks, the three-conjunct exit, the four-rung ROI ladder, the −30% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: three-conjunct entry / all lookbacks / three-conjunct exit / four-rung ROI / −30% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Heikin-Ashi relevance: dropping both color legs (bare EMA20/50 cross entry, same exit/risk) must not improve net expectancy; fail ⇒ the Heikin-Ashi confirmation adds nothing over the bare cross.
- F2 — Edge relevance: replacing the `crossed_above(ema20, ema50)` edge with the level state `ema20 > ema50` (same color legs, same exit/risk) must not improve net expectancy; fail ⇒ edge timing adds nothing over level holding.
- F3 — Exit relevance: replacing the slow-cross-plus-red signal exit with ROI/stop-only management (same entry) must not improve net expectancy; fail ⇒ demanding the slow-trend receipt adds nothing over fixed risk management.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume or exotic feed is read at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib EMA internals and the pinned `qtpylib.heikinashi`/`crossed_above` implementations live in their libraries outside the pinned strategy file — pinned by call with the contemporaneous definitions quoted above, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local arithmetic, under the disclosed 110-bar floor.
- No trailing, no breakeven, no time exit beyond the ROI clock, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy001.py
- https://github.com/berlinguyinca/freqtrade-strategies
