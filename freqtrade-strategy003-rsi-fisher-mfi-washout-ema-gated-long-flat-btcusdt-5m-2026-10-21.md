---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade strategy003 RSI-Fisher-MFI washout EMA-regime-gated long-flat on BTCUSDT 5m bars
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
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy003.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade strategy003 RSI-Fisher-MFI washout EMA-regime-gated long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-strategy002`, and `freqtrade-strategy004` records — this is only its twelfth record).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/strategy003.py`.
- GitHub blob SHA at the pinned commit: `5fcd8e3033c7b6d5ae0749f836438e92d0e42204`, size 3960 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3960 bytes, 118 lines, SHA-256 `8976784e2fbe4428bc8fe6681ab87e93574184f7a41d4155ec7fba87527b7a5e`, identical to the GitHub blob (`git hash-object` reproduces `5fcd8e30…0e42204`) — the entire file was retrieved and inspected.
- Registration: the file defines class `strategy003(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `user_data/strategies/strategy001.py`, `strategy002.py`, `strategy004.py`, and `strategy005.py`, plus every `user_data/strategies/berlinguyinca/*.py` sibling, are different pins with different constants — this record pins ONLY the strategy003 literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `ticker_interval = '5m'`; `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.3`; entry is the eight-way AND of `rsi < 28`, `rsi > 0`, `close < sma`, `fisher_rsi < -0.94`, `mfi < 16.0`, `(ema50 > ema100) | crossed_above(ema5, ema10)`, `fastd > fastk`, `fastd > 0`; exit is the two-way AND of `sar > close`, `fisher_rsi > 0.3`. The docstring attribution (`author@: Gerald Lonlas`, `github@: https://github.com/freqtrade/freqtrade-strategies`, `How to use it? > python3 ./freqtrade/main.py -s Strategy003`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 118 lines.
- Out-of-file calls pinned (all resolved by name, all standard TA-Lib defaults): `ta.MFI(dataframe)` (default `timeperiod=14` pinned by call — the file's only volume read); `ta.STOCHF(dataframe)` (TA-Lib defaults fastk_period 5 / fastd_period 3 pinned by call); `ta.RSI(dataframe)` (default `timeperiod=14` pinned by call); `ta.EMA(dataframe, timeperiod=5/10/50/100)` (all explicit); `ta.SMA(dataframe, timeperiod=40)` (explicit 40); `ta.SAR(dataframe)` (TA-Lib defaults acceleration 0.02 / maximum 0.2 pinned by call); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` returning the `lower` rail into `bb_lowerband` only — computed but never read by either leg (dead column, fenced below). The inverse-Fisher warp `fisher_rsi = (exp(2*r)-1)/(exp(2*r)+1)` with `r = 0.1*(rsi-50)` is fully visible file-local arithmetic. The single `crossed_above(ema5, ema10)` edge rides the same verified `qtpylib.crossed_above` primitive the admitted HLHB sibling evidenced (`freqtrade@3d31927` forwarding to `technical@9c6d8fd`, scalar-broadcast inclusive edge). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 118 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 1 `cross` (the single `crossed_above(ema5, ema10)` OR-arm — the only edge call; every other leg is a persistent level state); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `volume` (no volume column is ever named — the MFI call reads the OHLCV frame's volume field internally, the file's sole volume dependency); 0 `shift` (no lag call — per-bar state evaluation under the file's own framework contract); 1 `stoploss` attribute (`-0.3`) and 1 `minimal_roi` ladder as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 110-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 5 `buy` / 3 `sell` (old-interface `populate_buy_trend` / `populate_sell_trend` plumbing plus the `buy`/`sell` column writes — mapped to enter-long/exit-long framework reading below, never a second leg). `Dict`, `List`, `hp`, `reduce` are imported; `reduce(` is never called — the two `hyperopt` tokens are the dead `hp` import plus its comment-line echo: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive — no repair site exists). Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 110-bar researcher warmup pin (covers the 100-bar EMA seed, the 40-bar SMA seed, the 20-bar Bollinger seed, the 14-bar RSI/MFI seeds, the STOCHF seed, the SAR seed, and the two-bar `crossed_above` edge with margin); (4) the house cost/capital overlay replaces the absent source economics. Every threshold, every lookback, the OR-arm, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `strategy003`, `fisher_rsi < -0.94`, and the `mfi < 16` conjunction returns zero strategy records — no record in the pool conjoins an RSI-plus-inverse-Fisher washout with an MFI floor, an SMA40 under-close filter, and an EMA-regime-OR-cross gate. The lone pool `fisher_rsi` hit is the admitted strategy002 sibling, fenced as a different construction in Negative evidence 7 (it shares only the two exit legs). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades an RSI/Fisher/MFI washout with an EMA-regime-OR-cross entry. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where the tape prints a triple-confirmed washout (RSI under 28, inverse-Fisher-warped RSI under −0.94, money-flow under 16) while price sits beneath its 40-bar average and the fast stochastic aligns bullishly (fast %D above fast %K, above zero) inside a permissive trend-regime gate (slow EMAs stacked bullishly OR a fresh 5/10 EMA golden edge) — and stand aside to flat when the Parabolic SAR flips above the close while warped momentum normalizes above 0.3, with a four-rung time-decaying ROI ladder (5% → 4% → 3% → 1%) and a −30% disaster stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 118 lines.

### Research interpretation

Triple-witness washout-fade machine with a regime escape hatch, long-only. Unlike single-oscillator dip records (one RSI print suffices), three differently-constructed witnesses must agree — price momentum (RSI), warped momentum (Fisher, which stretches the RSI tails so −0.94 demands a genuinely extreme tail, not a soft drift), and money flow (MFI, the only leg that sees volume). Unlike pure level systems, the OR-gate adds trend permission with two keys: either the slow trend is already stacked (EMA50 above EMA100 — buy dips inside an established uptrend) or a fresh short-EMA edge just fired (catch the turn itself) — chop with flat slow EMAs and no fresh edge prints nothing. The exit is normalization discipline, not reversal: SAR overhead plus warped momentum back above 0.3, so a SAR flip during still-crushed momentum holds, and a momentum pop under a still-supportive SAR holds. The coded consequence is a buyer of volume-confirmed extreme washouts inside permitted regimes that surrenders only when stop-dot and warped momentum agree the washout is over.

## Signal

Exact rule as pinned (any other lookback, threshold, window, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
rsi[t]       = TA-Lib RSI(close, 14)
mfi[t]       = TA-Lib MFI(high, low, close, volume, 14)   // sole volume read
fastk[t], fastd[t] = TA-Lib STOCHF(close windows; fastk 5, fastd 3)
fisher_rsi[t] = (exp(2*r[t])-1)/(exp(2*r[t])+1), r[t] = 0.1*(rsi[t]-50)
sma[t]       = TA-Lib SMA(close, 40)
ema5/10/50/100[t] = TA-Lib EMA(close, 5 / 10 / 50 / 100)
sar[t]       = TA-Lib SAR(high, low; 0.02 / 0.2)
bb_lower     = BB20-2 typical-price lower rail — COMPUTED, NEVER READ (dead column)
entry = (rsi[t] < 28) AND (rsi[t] > 0) AND (close[t] < sma[t])
        AND (fisher_rsi[t] < -0.94) AND (mfi[t] < 16.0)
        AND ((ema50[t] > ema100[t]) OR crossed_above(ema5, ema10)[t])
        AND (fastd[t] > fastk[t]) AND (fastd[t] > 0)                          // buy = 1
exit_sig = (sar[t] > close[t]) AND (fisher_rsi[t] > 0.3)                      // sell = 1
risk = time-decaying take-profit minimal_roi {"60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05}; fixed stop at -30% (stoploss -0.3)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar printing the eight-conjunct state, `direction` long-only; `sell=1` on bars printing the two-conjunct normalization state. Both legs are STATE prints (while positioned they stay true every qualifying bar — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). Old-interface `buy`/`sell` columns read as enter-long/exit-long (disclosed framework reading, never a second leg).
- Exact boundaries (pinned semantics): strict throughout (`>`, `<` — an RSI landing exactly on 28 or 0, a close exactly on the SMA40, a Fisher print exactly on −0.94 or 0.3, an MFI exactly on 16.0, stacked EMAs exactly equal, a stochastic leg exactly on its peer or on zero, or a SAR dot exactly on the close fires nothing). The `28` / `0` / `−0.94` / `16.0` / `0.3` literals are never tuned here.
- Same-bar co-print pin (proved, not asserted): entry demands `fisher_rsi[t] < −0.94` while exit demands `fisher_rsi[t] > 0.3` on the same bar's single Fisher value — mutually exclusive by construction, so a full entry/exit co-print is arithmetically impossible and no fill-ordering invention is ever needed. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the SAR-plus-Fisher normalization signal exit, the four-rung ROI ladder, and the −30% stop are the complete position-closing set (old-interface `use_sell_signal = True` / `sell_profit_only = False` framework-default reading — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"60"`/`"30"`/`"20"`/`"0"`), preserved verbatim.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying eight-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`high`/`low`/`close` for MFI/RSI/SAR/EMA/SMA, `close` for STOCHF, `volume` inside the MFI call only) with fixed non-negative offsets (trailing windows plus the two-bar edge seed — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`buy`/`sell` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` for the MFI/RSI/SAR/EMA/SMA path, `close` for the STOCHF stack, `volume` inside the MFI call only (the file names no volume column — the OHLCV frame's volume field feeds MFI internally). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 110 five-minute bars held flat. Covers the 100-bar EMA seed (longest window), the 40-bar SMA seed, the 20-bar Bollinger seed, the 14-bar RSI/MFI seeds, the STOCHF/SAR seeds, and the two-bar `crossed_above` edge with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, strategy002 hammer-gated oversold, and strategy004 ADX-gated CCI washout records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the eight-conjunct entry opens the full unit on a flat book; the normalization signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (118 lines: the MFI/STOCHF/RSI/Fisher/Bollinger/EMA/SAR/SMA indicator block, the eight-conjunct entry with its EMA-regime OR-arm, the two-conjunct exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `strategy003(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 110-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>`/`<` fire nothing on equality; the `rsi > 0` and `fastd > 0` legs additionally exclude only the degenerate all-flat-tape prints. An RSI exactly on 28, a close exactly on the SMA40, a Fisher print exactly on −0.94 or 0.3, an MFI exactly on 16.0, or exactly-equal EMA stacks hold — disclosed, not smoothed.
3. Co-print arithmetic fenced (proved, not asserted): entry's `fisher_rsi < −0.94` and exit's `fisher_rsi > 0.3` read one bar's single Fisher value — mutually exclusive, so no co-print can ever reach the engine. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins RSI at 0 (the `rsi > 0` leg fails — no entry); MFI pins midscale (failing `< 16.0`); stochastics pin at midscale (failing the `fastd > fastk` entry alignment only when exactly equal — otherwise flat-tape stochastics drift, but the triple-washout conjuncts still gate); SAR dots sit on the flat line (exit additionally needs `fisher_rsi > 0.3`, unreachable from a pinned-0 RSI warp). No division by zero exists anywhere (all guards are comparisons; the Fisher warp's denominator `exp(2r)+1` is strictly positive) — disclosed, not repaired.
5. Dead-column plumbing fenced: `bb_lowerband` is computed every bar and read nowhere — display/plumbing leftover with no gate effect; this record never conditions on it and no reviewer repair may promote it into a leg. `Dict`, `List`, `hp`, `reduce` are imported and never called — the two `hyperopt` tokens are the dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values — disclosed, never repaired into a signal.
6. Derivation-effect fenced: this record computes no behaviour differently from the file's letter — the four adaptations are market choice, fill convention, position/warmup pins, and house economics only. Every threshold, lookback, the OR-arm, the ROI ladder, and the stop are verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none conjoins an RSI/Fisher/MFI triple washout with an SMA40 under-close filter and an EMA-regime-OR-cross gate): the admitted strategy002 sibling shares the exact two exit legs (`sar > close & fisher_rsi > 0.3`) but buys a hammer-pattern-plus-band-penetration entry (pattern trigger, never a triple-oscillator washout); the admitted freqtrade-bband-rsi-dip-buy sibling buys BB-penetration RSI dips on `1h` (no Fisher, no MFI, no EMA-regime gate); the admitted strategy004 sibling trades an ADX-gated CCI washout with a dual-STOCHF recross on `5m` (no RSI, no Fisher, no MFI, no EMA gate, regime-collapse exit); the admitted freqtrade-hlhb sibling conjoins an RSI-50 edge with an EMA5/10 edge plus ADX>25 on `4h` (edge-cross construction, never a sub-28 washout state, quad-gated exit with trailing stop); the admitted strategy001 sibling trades a Heikin-Ashi EMA-cross trend state on `5m` (synthetic-series trend, never an oscillator washout); the open-PR AdxSmas sibling trades an ADX-gated SMA3/6 cross on `1h` (edge, never a washout state). Not a threshold re-tuning of any of them: dropping the Fisher leg, the MFI leg, the SMA filter, or either OR-arm key would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `strategy001.py` (Heikin-Ashi sample), `strategy002.py` (hammer-gated sample), `strategy004.py` (ADX-gated CCI sample), `strategy005.py` (hyperopt-parameterized volume-spike sample), and every `berlinguyinca/*.py` sibling are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the four declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 110-bar warmup floor, house sizing/costs) — all predeclared above. The `5m` frame, the eight-conjunct entry with every literal and the OR-arm, the two-conjunct exit, the four-rung ROI ladder, the −30% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: eight-conjunct entry / all lookbacks, thresholds, pattern literals / two-conjunct exit / four-rung ROI / −30% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Fisher-tail relevance: dropping the `fisher_rsi < −0.94` conjunct (same RSI/MFI/SMA/regime/stoch entry, same exit/risk) must not improve net expectancy; fail ⇒ the warped-tail witness adds nothing over the raw RSI-plus-MFI washout.
- F2 — Regime-gate relevance: dropping the `(ema50 > ema100) | crossed_above(ema5, ema10)` arm (same washout/stoch entry, same exit/risk) must not improve net expectancy; fail ⇒ the trend-permission gate adds nothing over the bare washout-plus-alignment.
- F3 — MFI-volume relevance: dropping the `mfi < 16.0` conjunct (same RSI/Fisher/SMA/regime/stoch entry, same exit/risk) must not improve net expectancy; fail ⇒ the money-flow witness adds nothing over the price-momentum washout pair.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Volume feeds only the MFI call — a standard candle field on the venue; no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib MFI/STOCHF/RSI/EMA/SMA/SAR internals live in their library outside the pinned file — pinned by call with defaults, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local Fisher arithmetic, under the disclosed 110-bar floor.
- The Bollinger lower rail is computed and ignored — a reader must not mistake `bb_lowerband` for a gate; it gates nothing.
- No trailing, no breakeven, no time exit beyond the ROI clock, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/strategy003.py
- https://github.com/berlinguyinca/freqtrade-strategies
