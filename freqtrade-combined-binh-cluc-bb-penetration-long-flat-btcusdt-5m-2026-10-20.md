---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade CombinedBinHAndCluc BB-penetration dual-leg long-flat on BTCUSDT 5m bars
created: 2026-10-20
updated: 2026-10-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/CombinedBinHAndCluc.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade CombinedBinHAndCluc BB-penetration dual-leg long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `td-sequential-setup9-perfected` record — this is only its second record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/CombinedBinHAndCluc.py`.
- GitHub blob SHA at the pinned commit: `872468c2446d375d3cb3409b0d0b9842d2a2072d`, size 3265 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3265 bytes, 76 lines, SHA-256 `546256271db535f1e326130c6b2d9849dd9a5efb602eb92ed45dad282967f45d`, identical to the GitHub blob (`git hash-object` reproduces `872468c2…2072d`) — the entire file was retrieved and inspected.
- Registration: the file defines class `CombinedBinHAndCluc(IStrategy)` (the only class in the file) plus one module-level helper `bollinger_bands()`. Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/BinHV45.py` (hyperopt-parameterised single leg, `timeframe = '1m'`) and `berlinguyinca/ClucMay72018.py` (single leg, `timeframe = '5m'`) are different pins with different constants — this record pins ONLY the Combined file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = { "0": 0.05 }`; `stoploss = -0.05`; `use_exit_signal = True`; `exit_profit_only = True`; `ignore_roi_if_entry_signal = False`; entry is the OR of a BinHV45 leg (`lower.shift().gt(0)`, `bbdelta.gt(close * 0.008)`, `closedelta.gt(close * 0.0175)`, `tail.lt(bbdelta * 0.25)`, `close.lt(lower.shift())`, `close.le(close.shift())`) and a Cluc leg (`close < ema_slow`, `close < 0.985 * bb_lowerband`, `volume < volume_mean_slow.shift(1) * 20`); exit is `close > bb_middleband`. The `max_open_trades = 2` remark in the class comment is cross-market backtest commentary, never a per-pair add rule (see Signal). The `volume > 0`-style emptiness guard is NOT in this file — the volume line is a 20×-mean pump cap, disclosed as coded.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.EMA(dataframe, timeperiod=50)` (TA-Lib abstract EMA on closes); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` returning the `lower`/`mid` dict entries (typical price `(high+low+close)/3`, the Freqtrade vendor call pinned by call — its internal rolling arithmetic lives outside this file and is disclosed as such, never re-derived here); the file-local `bollinger_bands(close, 40, 2)` helper (fully visible: pandas `rolling(40).mean()` / `rolling(40).std()` with pandas-default `ddof=1`, wrapped in `np.nan_to_num`, disclosed below). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 76 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `short` (no short leg anywhere); 1 `stoploss` (`-0.05`) and 1 `minimal_roi` (`{"0": 0.05}`) as the only risk legs; 0 `trailing` / 0 `startup_candle` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); `volume` appears only in the pump-cap line and its MA construction; 0 `pyramid` / 0 `position` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic).

Pre-write dedup (2026-10-20): working-tree filename/content search for `CombinedBinHAndCluc` / `BinHV45` / `ClucMay72018` / `bbdelta` / `closedelta` / `0.985` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI) trades a Bollinger-penetration signal. The pool's nearest Bollinger cousins are fenced as different constructions in Negative evidence 7 — none trades this dual-leg BB(40)-penetration-with-body-guards OR EMA50/BB(20)-discount-plus-pump-cap entry with a BB-mid profit-gated exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: a combination of two Bollinger-band-dip buyers — the BinHV45 leg buys a close that pierces the lower BB(40, 2σ) band with a large prior-bar body move but a small lower tail (a shoved-through-the-band bar, not a long-tail hammer), and the Cluc leg buys a close parked under both EMA(50) and 1.5% under the lower BB(20, 2σ) band provided volume is not spiking (under 20× its 30-bar mean — an anti-pump cap). Both legs exit on reclaim of the BB(20) midline, but only when the trade is profitable; a 5% ROI target and a −5% stoploss backstop every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 76 lines. The class comment's `max_open_trades = 2` backtest remark ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Dip-catching machine with two independent triggers sharing one profit-aware exit, long-only. Unlike breakout records (upper-rail breaks bought for continuation), both legs buy penetration weakness: leg A demands microstructure proof the push through the band was decisive (body displacement over 1.75% of price, tail under a quarter of band width — a close pinned under the band, not a wick that already rejected it); leg B buys the slower discount (under EMA50 AND 1.5% under the band) but refuses to catch pumps (volume cap). The shared exit is patient capital discipline, not a reversal signal: the midline reclaim banks only when green (`exit_profit_only`), while red positions sit until the 5% ROI prints or the −5% stop admits failure — so a V-recovery that never reaches midline still pays via ROI, and a dead-cat that reclaims midline red is held, not sold. The coded consequence is a buyer of confirmed band breaks that harvests mean-reversion only when it actually pays.

## Signal

Exact rule as pinned (any other band window, multiplier, fraction, volume multiple, ROI/stop pair, profit gate, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
mid40[t], lower40[t] = nan_to_num(rolling_mean40(close)), nan_to_num(rolling_mean40(close) - 2 * rolling_std40(close, ddof=1))
bbdelta[t]    = |mid40[t] - lower40[t]|
closedelta[t] = |close[t] - close[t-1]|
tail[t]       = |close[t] - low[t]|
bb_lower20[t], bb_mid20[t] = qtpylib BB(20, 2) over typical price (lower / mid)
ema50[t]      = TA-Lib EMA(close, 50)
volMA30[t]    = mean(volume[t-29 .. t])
legA = (lower40[t-1] > 0) AND (bbdelta[t] > 0.008 * close[t]) AND (closedelta[t] > 0.0175 * close[t])
       AND (tail[t] < 0.25 * bbdelta[t]) AND (close[t] < lower40[t-1]) AND (close[t] <= close[t-1])
legB = (close[t] < ema50[t]) AND (close[t] < 0.985 * bb_lower20[t]) AND (volume[t] < 20 * volMA30[t-1])
entry     = legA OR legB                                            // enter_long = 1
exit_sig  = (close[t] > bb_mid20[t]) honored ONLY when position PnL > 0 at the close
risk      = take-profit at +5% from entry (minimal_roi {"0": 0.05}); fixed stop at -5% (stoploss -0.05)
guard     = leading-window bars: NaN comparisons false; nan_to_num zeros fail the coded guards (see Required data)
```

- Trade events: `enter_long=1` on any bar where legA or legB prints, `direction` long-only; `exit_long=1` on bars where the close reclaims the BB(20) midline. The midline exit is a STATE level (while positioned above midline it stays true every bar — close-and-hold-flat); both entry legs are edges/levels that can reprint across consecutive bars (no one-shot latch in code).
- Exact boundaries (pinned semantics): legA compares with strict `.gt`/`.lt` (exact equality fires nothing) except `close <= previous close` (`.le` — an unchanged close satisfies the sixth conjunct); legB is strict throughout (`<`); the exit is strict (`>` — a close landing exactly on the midline holds). The `0.985` discount and the `20×` volume multiple are literals, never tuned here.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close[t]` strictly under a lower band at or below its midline (`lower40 ≤ mid40` since σ ≥ 0; `0.985 × bb_lower20 < bb_lower20 ≤ bb_mid20` for the positive bands of positive prices), hence `close[t] > bb_mid20[t]` is false on that bar — entry and signal-exit never co-print outside degenerate non-positive-band windows, which the warmup below excludes. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `enter_short`/`exit_short`/`short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the profit-gated midline signal, the +5% ROI leg, and the −5% stop are the complete position-closing set (`use_exit_signal = True`, `exit_profit_only = True`, `ignore_roi_if_entry_signal = False` — all file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented. The profit gate is evaluated on position PnL at the decision close (fees handled by the house cost model downstream, never claimed as source economics).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — the file's `max_open_trades = 2` comment is cross-market commentary, never a per-pair add rule); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying leg-A-or-B bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`close`/`low` for bands/tail/deltas, `high` inside typical price, `volume` only for the pump cap) with fixed non-negative offsets — no `volume`-beyond-cap, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, or stop/limit order argument anywhere in the gating path. The `compatible_regimes`-style metadata does not exist in this file at all. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` for the BB(40)/BB(20)/EMA(50)/delta/tail path plus `volume` for the 30-bar mean pump cap ONLY. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; all windows (40-bar bands, 50-bar EMA, 20-bar BB, 30-bar volume mean, one-bar shifts) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 55 five-minute bars held flat. Covers the 40-bar band seed, the nominal 50-bar EMA window, the 30-bar volume seed, and all one-bar shift reads. Coded behaviour underneath: pandas rolling windows print NaN until seeded (every strict NaN comparison false — no leg can fire early), while the file-local helper's `np.nan_to_num` turns its leading mid/lower into zeros that fail the `lower.shift() > 0` and `bbdelta > 0.8%` guards by construction; the qtpylib midline prints NaN early so the exit leg stays false. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced TDSequential sibling and the admitted volume-gated Forven siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry legs, the midline signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine. The profit gate reads booked position PnL at the decision close — a position-state condition, not an intrabar path.
- Interval precedent (disclosed, not assumed): sub-1h PASS records already on `main` (`15m`, `30m`, `12m`, `10m`, `36m`, `6m`) demonstrate the pinned engine's sub-1h Binance candle path; no exact-`5m` PASS record exists yet, so the `5m` step is flagged for reviewer confirmation rather than claimed as pre-verified. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI/stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; either entry leg opens the full unit on a flat book; the gated signal exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying leg bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (76 lines: the visible `bollinger_bands(close, 40, 2)` helper with its `0.008`/`0.0175`/`0.25` fractions, the qtpylib BB(20, 2)/EMA(50)/volume-MA(30) indicator block, the OR-ed dual entry legs with the `0.985` discount and `20×` pump cap, the `close > bb_middleband` exit, the `timeframe`/`minimal_roi`/`stoploss`/`use_exit_signal`/`exit_profit_only`/`ignore_roi_if_entry_signal` literals, and the `CombinedBinHAndCluc(IStrategy)` class pin). It ships a `max_open_trades = 2` backtest remark with no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: pandas rolling NaNs compare false (no early entry, no early qtpylib exit); the local helper's `nan_to_num` zeros fail `lower.shift() > 0` and the `bbdelta` fraction guard. The 55-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `.gt`/`.lt`/`<`/`>` fire nothing on equality; only legA's sixth conjunct admits equality (`close <= prior close`). A close exactly on the midline holds; a close exactly 1.5% under the lower band does not enter. Strictness preserved throughout — disclosed, not smoothed.
3. Profit-gate cost fenced: a midline reclaim printed red is ignored by code — the position rides until ROI or stop. There is no level-hold exit and no loss-cutting signal leg; the −5% stop is the sole red-book guardrail — disclosed, not repaired.
4. Volume-cap edge fenced: entries print only when `volume < 20 × mean` — pump bars are skipped even with perfect band penetration, and a low-volume drift-through still enters. The cap is anti-spike only, never a participation requirement — disclosed, not reinterpreted.
5. `lower.shift() > 0` guard fenced: trivially true for live BTC prices (bands of positive closes stay positive past seeding) — a coded no-op under real data, preserved verbatim, never presented as a live filter.
6. Zero-variance fenced: flat tape pins σ at 0, bands collapse onto the mean, `bbdelta = 0` fails the fraction guard — no entry; exit needs strict reclaim. No division by zero exists anywhere (all guards are multiplicative comparisons) — disclosed, not repaired.
7. Cousin records fenced as different constructions (none trades a dual-leg lower-band penetration with body/tail microstructure guards plus a pump-capped discount leg and a profit-gated midline exit): the admitted chartart-bollinger-rsi sibling needs a joint RSI(6)-50 turn AND a 200-bar rail reclaim two-sided always-in; the admitted forven-bollinger-s00120 sibling breaks the UPPER rail while RSI reads oversold (continuation breakout, opposite direction of trade); the admitted forven-bb-edge-fade-reclaim and forven-bb-squeeze-breakout siblings trade edge-fade and squeeze-release mechanics with different gates; the admitted alorse-kodify-bb350 sibling crosses a 350-period upper band with a midline exit but no penetration legs, no volume cap, no profit gate. Not a threshold re-tuning of any of them: moving a band window, softening the `0.985` discount, dropping the tail/volume guards, or ungating the exit would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `BinHV45.py` (hyperopt `buy_bbdelta`/`buy_closedelta`/`buy_tail` parameters, `1m` frame, no exit signal) and `ClucMay72018.py` (single leg, `ema100`-named-but-50 EMA, ROI `0.01`) are separate pins — their constants must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 55-bar warmup floor, and house sizing/costs — all predeclared above. The `5m` frame, the dual-leg entry with all six-plus-three conjuncts, the profit-gated midline exit, the +5%/−5% risk pair, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: dual-leg construction / all band windows, multipliers, fractions, discount, volume multiple / profit-gated midline exit / +5% ROI / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Leg relevance: dropping the BinHV45 leg (Cluc leg only, same exit/risk) must not improve net expectancy; fail ⇒ the penetration-microstructure leg adds nothing over its discount twin.
- F2 — Profit-gate relevance: honoring midline exits regardless of profit (same entry/risk) must not improve net expectancy; fail ⇒ the profit gate adds nothing over an ungated signal exit.
- F3 — Volume-cap relevance: removing the 20× pump cap (same legs/exit/risk) must not improve net expectancy; fail ⇒ the anti-pump guard adds nothing over uncapped entries.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — the "first-N-bars" session semantics some breakout systems need do not exist here; every window is a trailing bar count, portable across 24/7 crypto tape. Volume-gating uses the venue's own candle volume, available on the same feed as the bars. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` interval has sub-1h family precedent but no exact-`5m` PASS record — reviewer confirms the one-step-down path (see Execution assumptions), never assumed quiet.
- The profit-gated signal exit is position-state-conditional by file literal; an engine that honors signal exits unconditionally would trade a different, unpinned rule.
- qtpylib BB(20, 2)/typical-price internals live in the Freqtrade vendor module outside the pinned file — pinned by call, not re-derived; exact reproduction inherits that module's rolling semantics alongside the file-local helper's disclosed pandas `ddof=1` arithmetic.
- TA-Lib EMA(50) seeding inherits the library's recursive warmup; the 55-bar floor keeps early-bar EMA instability out of trusted events.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/CombinedBinHAndCluc.py
- https://github.com/freqtrade/freqtrade-strategies
