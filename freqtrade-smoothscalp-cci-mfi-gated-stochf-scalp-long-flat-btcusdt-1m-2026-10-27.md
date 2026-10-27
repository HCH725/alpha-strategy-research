---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade SmoothScalp CCI/MFI-gated fast-stochastic EMA-rail scalp long-flat on BTCUSDT 1m bars
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade SmoothScalp CCI/MFI-gated fast-stochastic EMA-rail scalp long-flat on BTCUSDT 1m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade community strategy collection; the lane that supplied the admitted `freqtrade-cofibit`, `freqtrade-quickie`, `freqtrade-strategy003`, `freqtrade-strategy004`, `freqtrade-strategy005`, and `freqtrade-hlhb` records — this is a new file pin from the same `berlinguyinca/` directory, not a re-pin of any of them).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/SmoothScalp.py`.
- GitHub blob SHA at the pinned commit: `9d0718b04aad27e8bc989b2362a22934485e9520`, size 3861 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3861 bytes, 102 lines, SHA-256 `e32a8f758d8d57876210d479576e7e415ff924400b8d037bb0f30799cd801a5b`, identical to the GitHub blob (`git hash-object` reproduces `9d0718b0…e9520`) — the entire file was retrieved and inspected.
- Registration: the file defines class `SmoothScalp(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, every sibling file (`CofiBitStrategy.py`, `Quickie.py`, `strategy002.py` … `strategy005.py`, and all other `berlinguyinca/*.py` files) is a different pin with different constants — this record pins ONLY the SmoothScalp literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '1m'`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.5` (with the author's own comment `should not be below 3% loss`); the docstring idea (`generating a lot of potentatils buys and make tiny profits on each trade`) and its parallel-trade recommendation (`we recommend to have at least 60 parallel trades at any time to cover non avoidable losses` — explicitly NOT adopted; see Derived-record declaration); entry is the seven-way AND of `open < ema_low`, `adx > 30`, `mfi < 30`, `fastk < 30`, `fastd < 30`, `crossed_above(fastk, fastd)`, `cci < -150` (`enter_long = 1`); exit is `((open >= ema_high) OR crossed_above(fastk, 70) OR crossed_above(fastd, 70)) AND cci > 150` (`exit_long = 1`). The file ships no sample, window, trade count, or cost basis — no performance is claimed anywhere in the 102 lines.
- Framework calls pinned (all resolved against contemporaneous first-party commits read directly this cycle): `qtpylib.crossed_above(s1, s2)` forwards through `freqtrade@3d31927c8232830729e37ce9c36f230ab8d9c7c2` (`freqtrade/vendor/qtpylib/indicators.py`, a re-export shim) to `technical@9c6d8fd366ef0ed3e046b32e534bcec9f9479449` (`technical/vendor/qtpylib/indicators.py`), where `crossed(s1, s2, "above")` broadcasts a scalar second argument (`70`) to a constant Series and returns `(s1[t] > s2[t]) & (s1[t-1] <= s2[t-1])` — a one-bar edge admitting equality on the prior bar, scalar-safe. `ta.EMA(dataframe, timeperiod=5, price=...)` for `high`/`close`/`low` follows the lane's price-input convention (same reading as the admitted CofiBit/Quickie siblings). `ta.ADX` / `ta.MFI` / `ta.RSI` use TA-Lib defaults (period 14); `ta.CCI` is assigned twice and the effective column is the second call's default period 14 (disclosed below, never re-derived); `ta.STOCHF(dataframe, 5, 3, 0, 3, 0)` and `ta.MACD(dataframe)` are quoted verbatim as written. No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 102 lines this cycle): 0 `short` (case-insensitive — no short leg anywhere); 3 `crossed_above` (exactly the entry fastk/fastd edge plus the two scalar-70 exit edges, no other edge call); 0 `volume` (no order-gating line reads volume — no leakage site exists); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 1 `stoploss` attribute (`-0.5`) and 1 single-rung `minimal_roi` as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 60-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage`; 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` / 0 `protections` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `use_exit_signal` / 0 `exit_profit_only` (framework defaults disclosed below, never file literals); 0 `hyperopt` / 0 `hp.` / 0 `*Parameter` / 0 `reduce(` (the `Dict`/`List`/`reduce`/`numpy` imports are never called — dead plumbing); 1 `enter_long` and 1 `exit_long` (new-interface columns, read directly as enter-long/exit-long).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 60-bar researcher warmup pin (covers the ADX14 seed, the CCI14/MFI14/RSI14/STOCHF seeds, the EMA5 seeds, and the two-bar `crossed_above` edges with margin) — the docstring's 60-parallel-trade recommendation is explicitly NOT adopted; (4) the house cost/capital overlay replaces the absent source economics; (5) the `1m` frame is the file's own literal, executed on the explicitly `1m`-mapped pinned-engine candle path (see Execution assumptions). Every threshold, every lookback, all three `crossed_above` edges, both EMA rails, the flat 1% ROI, and the −50% stop are untouched.

Pre-write dedup (2026-10-27): working-tree filename search for `smoothscalp` returns zero records; content search for `open.*ema_low` returns only the admitted CofiBit sibling (fenced leg-by-leg in Negative evidence 7 — different entry conjunction, different exit gating, different risk, different frame); content search for `cci.*150` returns only unrelated constructions (CCI-threshold-extreme reversal, Eterna SMA-crossover, morning/evening-star ratio — none conjoins a fast-stochastic edge with EMA rails, ADX, MFI, and CCI washout gates); the `mfi.*30` hits are different constructions or fencing text (strategy003 washout, strategy005 washout, CMCWinner oscillators, FMZ quad-confluence — none conjoins MFI<30 with a STOCHF edge, EMA rails, and a CCI-gated exit). No open `research/*` PR (Heracles, ClucMay72018, AdxSmas, Forven-CCI, Swift-2YMA, SSL, Chandelier, SuperTrend, Gauss-StochRSI, Larry-Williams — verified this cycle) trades a CCI/MFI-gated stochastic scalp. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the minute bar where price opens under its 5-bar low-rail while trend is certified (ADX above 30), money flow is weak (MFI under 30), both fast-stochastic limbs sit under 30 with fastk freshly crossing above fastd, and the CCI prints a −150 washout — and stand aside to flat when heat returns (CCI above 150) together with either a high-rail reclaim or either stochastic limb crossing above 70, behind a flat 1% take-profit and a −50% disaster stop. No behavioural, structural, or risk-premium channel is claimed anywhere in the 102 lines.

### Research interpretation

Washout-gated micro-scalp inside certified trend, long-only, with price-rail discipline on both sides. Unlike the admitted CofiBit sibling (which buys any trend-certified stochastic turn at the low rail), two extra permission keys are required at once: money flow must confirm weakness (MFI under 30) AND the CCI must print a full −150 washout — a stochastic turn without commodity-channel capitulation buys nothing. Unlike pure oscillator-turn records, price itself holds a veto through the EMA rails on both sides. The exit is deliberately stricter than the entry's mirror: no heat exit fires without the CCI above-150 gate — a rail reclaim or stochastic-70 cross printing while the CCI stays cool holds the book until the 1% ROI or the disaster stop. The coded consequence is a buyer of trend-certified, money-flow-confirmed stochastic turns at washout extremes that surrenders only on CCI-certified heat, a rail reclaim with heat, ladder profits, or the wide stop.

## Signal

Exact rule as pinned (any other stochastic period, EMA length, ADX/MFI/CCI length, threshold, edge construction, ROI, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; framework primitives expand to their pinned contemporaneous definitions:

```text
ema_high[t]  = EMA5(high); ema_low[t] = EMA5(low); ema_close[t] = EMA5(close, dead)
fastk[t], fastd[t] = TA-Lib STOCHF(high/low/close windows; call quoted verbatim:
                     ta.STOCHF(dataframe, 5, 3, 0, 3, 0))
adx[t] = TA-Lib ADX(high/low/close, 14); mfi[t] = TA-Lib MFI(high/low/close/volume, 14)
rsi[t] = TA-Lib RSI(close, 14, dead)
cci[t] = TA-Lib CCI(high/low/close, 14)   // second assignment wins; the period-20
                                          // first assignment is superseded, never read
xab(a,b)[t] = (a[t] > b[t]) AND (a[t-1] <= b[t-1])      // pinned crossed_above,
                                          // scalar b broadcast to constant Series
entry = (open[t] < ema_low[t]) AND (adx[t] > 30) AND (mfi[t] < 30)
        AND (fastk[t] < 30) AND (fastd[t] < 30) AND xab(fastk,fastd)[t]
        AND (cci[t] < -150)                               // enter_long = 1
exit_sig = ((open[t] >= ema_high[t]) OR xab(fastk,70)[t] OR xab(fastd,70)[t])
        AND (cci[t] > 150)                                // exit_long = 1
risk = flat take-profit minimal_roi {"0": 0.01}; fixed stop at -50% (stoploss -0.5)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on bars printing the seven-conjunct entry (edge-plus-levels), `direction` long-only; `exit_long=1` on bars printing the CCI-gated three-arm exit. The three `crossed_above` legs are edge prints (true only on the crossing bar); the level legs persist while true — close-and-hold-flat. New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly (no old-interface translation).
- Exact boundaries (pinned semantics): strict `<`/`>` on the entry legs with `<=` admitted on the prior bar per the pinned `crossed_above` expansion — an open exactly on `ema_low`, fastk/fastd exactly on 30, ADX/MFI exactly on 30, or CCI exactly on −150 fires nothing on that conjunct; the exit rail fires on exact touch (`>=`) exactly as coded, while the CCI `> 150` gate stays strict. The `5` / `14` / `30` / `70` / `150` literals, the flat `0.01` ROI, and the stop literal are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `cci[t] < -150` while every exit arm needs `cci[t] > 150` on the same bar — the two CCI regions are strictly disjoint, so entry and signal-exit NEVER co-print on any bar, and no engine ordering is ever invented. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the CCI-gated three-arm signal exit, the flat 1% ROI, and the −50% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI reads Freqtrade-native: rung `{"0": 0.01}` demands 1% from the entry minute — quoted verbatim, never smoothed. The −50% stop is the author's disaster literal with the author's own `should not be below 3% loss` comment preserved as lineage, never promoted into a tighter stop.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — the docstring's 60-parallel-trade recommendation is explicitly not adopted); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying seven-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`open` for the rail comparisons, `high`/`low`/`close` for EMA/ADX/CCI, `high`/`low`/`close`/`volume` for MFI14) with fixed non-negative offsets (trailing windows plus one `shift(1)` lag inside each edge — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `open` legs read the completed bar's own open — point-in-time available at the decision, never intrabar. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `1m` bars of BTCUSDT: `open` for the rail comparisons; `high`/`low`/`close` for the EMA5 rails, ADX14, and CCI14 paths; `high`/`low`/`close`/`volume` for the MFI14 path; `close` windows for the STOCHF path. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (source-native — the file prints `timeframe = '1m'`, with the author's own `the shorter the better` comment). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 one-minute bars held flat (~1 hour). Covers the ADX14 seed (~28 bars effective), the CCI14/MFI14/RSI14/STOCHF seeds, the EMA5 seeds, and the two-bar `crossed_above` edges with margin — the same 60-bar floor the admitted CofiBit sibling uses for the same longest seed. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval path (exact, disclosed): the pinned engine source (`HCH725/hummingbot@8b0e067`, `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, read directly at the pin this cycle) explicitly maps `1m` in its `INTERVALS` bidict — the required `1m` Binance candle path is specified by the engine itself, not assumed by analogy to the admitted `5m` siblings (ASDTSRockwellTrading, MACD-CCI dip-state, strategy002/003/004, Quickie, Simple MACD-BB-RSI, all `5m` Freqtrade-sourced long-flat). Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its flat 1% ROI and −50% stop are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the seven-conjunct entry opens the full unit on a flat book; any CCI-gated exit arm, the ROI, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (102 lines: the EMA/STOCHF/ADX/CCI/RSI/MFI/BB/MACD indicator block, the seven-conjunct entry with its edge-plus-rail-plus-ADX-plus-washout legs, the CCI-gated three-arm exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `SmoothScalp(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit; no `fillna` exists to smear seeds forward). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality on the entry legs and the CCI exit gate; the exit rail fires on exact touch (`>=`) exactly as coded. An open exactly on either rail, fastk/fastd exactly on 30, ADX/MFI exactly on 30, or CCI exactly on ±150 holds that leg — disclosed, not smoothed.
3. Co-print arithmetic fenced (proven, not asserted): entry needs `cci < -150` while every exit arm needs `cci > 150` on the same bar — strictly disjoint by construction, so no entry/exit co-print can occur on any bar and no position-pin tie-break is ever invoked. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins stochastics midscale (failing the sub-30 conjuncts), ADX toward 0/NaN (failing `> 30`), MFI midscale (failing `< 30`), CCI at 0/NaN (failing both washout gates), and EMA rails onto the flat line (the `open < ema_low` leg fails on exact equality). No division by zero exists anywhere in the gating path (all legs are comparisons or library-internal rolling arithmetic) — disclosed, not repaired.
5. Dead-column plumbing fenced: `ema_close`, `rsi`, `bb_lowerband`, `bb_upperband`, `bb_middleband`, `macd`, `macdsignal`, `macdhist` are computed every bar and read nowhere — display/plumbing leftovers with no gate effect; this record never conditions on them and no reviewer repair may promote any of them into a leg. The first `cci` (period-20) assignment is superseded by the second (period-14) before any order line runs — effective CCI is 14, disclosed, never re-derived. Zero `hyperopt` tokens ship anywhere — no tuning surface exists to repair into a signal.
6. STOCHF call fenced: the trailing `3, 0` literals repeat the STOCH-style slots verbatim from the file (the file's own 2020-04-04 commit message reads `stochf parameters are all integers`) — quoted as written, never reinterpreted; effective behaviour is the file's own call, not a re-derived parameter set. Same verbatim-call treatment the admitted CofiBit sibling uses for its identical STOCHF stack.
7. Cousin records fenced as different constructions (none conjoins a CCI/MFI-gated fast-STOCHF oversold edge with EMA high/low price rails and an ADX gate on `1m`): the admitted CofiBit sibling buys a five-conjunct stoch-edge-plus-rail-plus-ADX entry on `5m` with an UNGATED three-arm exit, a four-rung ROI ladder, and a −25% stop (no MFI leg, no CCI leg anywhere, exit fires without any washout gate); the admitted strategy004 sibling trades an ADX-gated CCI washout with a hand-rolled dual-STOCHF recross, a volume floor, and a regime-collapse exit on `5m` (no `crossed_above` primitive, no price rails, no MFI, no scalar-70 exit edges); the admitted strategy003 sibling trades an RSI/Fisher/MFI triple washout with an EMA-regime OR-arm on `5m` (oscillator level-states, never an oversold edge; SAR/Fisher exit, never a rail reclaim or CCI gate); the admitted Quickie sibling conjoins a TEMA-slope state with a BB-mid reclaim and an ADX gate on `5m` (trend-slope construction, never a stochastic edge or washout gate). Not a threshold re-tuning of any of them: dropping the MFI gate, either CCI washout gate, the edge primitive, or either rail would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `berlinguyinca/*.py` sibling is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 60-bar warmup floor, house sizing/costs, `1m` execution on the explicitly mapped engine path) — all predeclared above. The `1m` frame, the seven-conjunct entry with every literal and edge, the CCI-gated three-arm exit, the flat 1% ROI, the −50% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: seven-conjunct entry / all lookbacks, thresholds, edges, rails / CCI-gated three-arm exit / flat 1% ROI / −50% stop / single-unit long-only / `1m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Washout-gate relevance: dropping the `cci < -150` entry conjunct and the `cci > 150` exit gate (same stoch-edge-plus-rail-plus-ADX-plus-MFI entry, same risk) must not improve net expectancy; fail ⇒ the CCI washout certification adds nothing over the ungated turn-plus-rail state.
- F2 — Money-flow relevance: dropping the `mfi < 30` conjunct (same entry otherwise, same exit/risk) must not improve net expectancy; fail ⇒ the money-flow confirmation adds nothing over the pure washout-turn state.
- F3 — Gated-exit relevance: replacing the CCI-gated signal exit with ROI/stop-only exits (same entry, same risk) must not improve net expectancy; fail ⇒ the CCI-certified heat exit adds nothing over fixed risk alone.

## Crypto portability

BTCUSDT Binance perpetual `1m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only standard OHLCV candle fields are read (`open` for rails, `high`/`low`/`close` for EMA/ADX/CCI, `high`/`low`/`close`/`volume` for MFI, `close` windows for STOCHF); no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib STOCHF/EMA/ADX/CCI/MFI/RSI internals and the `qtpylib.crossed_above` edge arithmetic live in their libraries outside the pinned file — pinned by call with defaults/explicits, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local column wiring, under the disclosed 60-bar floor.
- `ema_close`, `rsi`, the three Bollinger columns, and the three MACD columns are computed and ignored — a reader must not mistake any of them for a gate; they gate nothing. The superseded period-20 CCI assignment must not be mistaken for the effective period-14 CCI.
- The STOCHF call's trailing `3, 0` literals repeat the STOCH-style slots verbatim from the file — quoted as written, never reinterpreted; effective behaviour is the file's own call, not a re-derived parameter set.
- The −50% stop is a disaster literal, not a trading stop — severe adverse moves within −50% are held until the CCI-gated exit or the 1% ROI; no protective stop, trailing, breakeven, time exit, short leg, or cooldown exists — all explicitly absent, never to be added by repair.
- The docstring's parallel-trade recommendation is lineage only — this record's single-unit pin explicitly supersedes it; no multi-position behaviour is admitted here.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
- https://github.com/freqtrade/freqtrade-strategies
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Admission contract: https://github.com/HCH725/alpha-strategy-research/blob/aa2c50d42794858bdf2c332bd79aa1a24920528c/.github/HB_READY_REVIEW.md
