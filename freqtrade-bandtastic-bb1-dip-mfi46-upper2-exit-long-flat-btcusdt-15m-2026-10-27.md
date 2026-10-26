---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Bandtastic 1σ-dip trigger with MFI-gated 2σ exit — independently derived BTCUSDT spot 15m long-flat
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Bandtastic 1σ-dip trigger with MFI-gated 2σ exit — independently derived BTCUSDT spot 15m long-flat

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-bband-rsi-dip-buy`, `freqtrade-hlhb-ema-rsi-adx-quad-gated`, and `freqtrade-trendfollowing-ewm20-obv-cross` records — this is a further record from that collection, pinned to its own file only).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Bandtastic.py`.
- GitHub blob SHA at the pinned commit: `f7710c76ae1e4ac7aff90857a647e4c2143baf9f`, size 7310 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 7310 bytes, 163 lines, SHA-256 `15dcb60d49a3681241cd39645f0fe8e6dc247687bf878c2026f37bb1c5790b57`, identical to the GitHub blob (`git hash-object` reproduces `f7710c76…3baf9f` and the Contents API at the pinned ref returns the same blob SHA and size) — the entire file was retrieved and inspected.
- Registration: the file defines class `Bandtastic(IStrategy)` (the only class in the file; header credits `Robert Roman`, MIT, `__version__ = "1.0"`). Freqtrade strategies carry no roster tuple — identity here is class plus file path, both unique.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '15m'`; `startup_candle_count = 999`; `minimal_roi = { "0": 0.162, "69": 0.097, "229": 0.061, "566": 0 }`; `stoploss = -0.345`; `trailing_stop = True`, `trailing_stop_positive = 0.01`, `trailing_stop_positive_offset = 0.058`, `trailing_only_offset_is_reached = False`; indicators `dataframe['rsi'] = ta.RSI(dataframe)` and `dataframe['mfi'] = ta.MFI(dataframe)` (TA-Lib abstract defaults, 14-bar each — library defaults, never file literals) plus four typical-price Bollinger blocks `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=1/2/3/4)` storing `bb_lowerband1..4` / `bb_middleband1..4` / `bb_upperband1..4`; the EMA loop over the union of the four declared hyperopt ranges; entry defaults `buy_rsi_enabled=False`, `buy_mfi_enabled=False`, `buy_ema_enabled=False`, `buy_trigger="bb_lower1"`; exit defaults `sell_rsi_enabled=False`, `sell_mfi_enabled=True`, `sell_ema_enabled=False`, `sell_trigger="sell-bb_upper2"` with `sell_mfi` default `46`; both legs end with `conditions.append(dataframe['volume'] > 0)`. No `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `process_only_new_candles`, no `order_types`, no informative/resample call ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.RSI` / `ta.MFI` (TA-Lib abstract, Wilder smoothing, default 14-bar); `ta.EMA(dataframe, timeperiod=period)` for each computed period; `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=k)` returning the `lower`/`mid`/`upper` dict entries (typical price `(high+low+close)/3`; the Freqtrade vendor call pinned by call — its internal rolling arithmetic lives outside this file and is disclosed as such, never re-derived here). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 163 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `can_short` (no short leg anywhere); 1 `minimal_roi` and 1 `stoploss` (`-0.345`) as the file's risk legs; 4 `trailing` (exactly the four trailing literals); 1 `startup_candle_count` (`999`); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop/trailing); 0 `informative` / 0 `resample` / 0 `merge_informative_pair` (single-frame by construction); 0 `position_adjustment` / 0 `protections` / 0 `cooldown` / 0 `custom_stoploss` / 0 `use_exit_signal` / 0 `exit_profit_only` (the position pin below is a predeclared researcher rule, never a file semantic); `volume` gates exactly two order lines (entry line 125, exit line 156); `RSI` constructed once and read on the two disabled-guard lines only; `heikinashi` 0; `RealParameter`, `DecimalParameter`, `numpy as np`, `pandas as pd` imported and never called in any gating line (dead imports — fenced, not repaired).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. Researcher-declared adaptations are exactly six, all predeclared here: (1) market pin `BTCUSDT` on Binance spot (the source is pair-agnostic — no symbol, no venue, no `trading_mode` anywhere in the file); (2) same-bar-close market fills on completed-bar decisions (the source engine fills on later candles; this record freezes completed-bar evaluation with same-bar-close execution and scopes live/limit-order-book behaviour out — the same derivation the admitted hlhb and TD-Sequential records carry); (3) an adopted 999-bar warmup with pre-warmup bars flat by record rule (exactly the source `startup_candle_count = 999`; covers the 366-bar EMA-365 seed, the 20-bar band seed, and the 14-bar RSI/MFI seeds — see Required data); (4) house sizing/capital/costs replacing the absent source economics; (5) bar-close evaluation of the fixed stop, the trailing stop, and the ROI ladder with the explicit precedence below (the source evaluates risk intrabar; intrabar sequencing is scoped out, never invented); (6) the hyperopt search spaces frozen at file defaults (any other enable flag, trigger choice, threshold, or MA length is a different, unpinned rule — never substituted, never tuned here). The `15m` frame, the typical-price BB(20, 1/2/3/4) block, the RSI(14)/MFI(14) constructions, the default 1σ-dip entry, the default MFI-46-gated 2σ-reclaim exit, the dual `volume > 0` guards, the four-rung ROI ladder, the −34.5% stop, the always-armed trailing quadruple, the long-only posture, and the exit-even-at-loss setting are source-native and unmodified.

Pre-write dedup (2026-10-27): working-tree filename/content search for `Bandtastic`, `bandtastic`, `Robert Roman`, `bb_lower1`, and `buy_trigger` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian) trades a multi-width-Bollinger trigger with an MFI-gated exit. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none trades a guard-free 1σ lower-band dip entry with an MFI-conjunction upper-band exit plus an ROI-ladder/trailing risk stack on `15m`. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where price dips under the 1σ typical-price lower band on a live tape (a shallow-penetration dip, not a 2σ washout, with every oscillator/EMA guard defaulted off); stand aside to flat only when money flow confirms the reclaim (MFI above 46) AND price reclaims above the 2σ upper band. A four-rung time-decaying ROI ladder (16.2% → 9.7% → 6.1% → 0%), a −34.5% fixed stop, and an always-armed trailing stop backstop every position. The file's only prose beyond authorship is the Sharpe-optimisation comment header (a fitting note, never a second trigger) and the per-block comments. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Impatient dip-buyer with a strict bouncer on the way out, long-only. Unlike 2σ-washout records (wait for deep dislocation plus an RSI sub-30 print), the 1σ trigger fires on the first shallow band-break with no momentum proof demanded — the entry is deliberately easy, so the book turns over faster and chop that merely kisses the 1σ rail enters. Unlike RSI-reclaim exits (bank any momentum print), the exit is deliberately hard: price must reach all the way across to the opposite 2σ rail AND money flow must read firm above 46 — a V-bounce that reclaims the midline but stalls under the upper rail, or a volume-flow-starved drift up, holds the position until the ROI ladder, the trailer, or the wide stop. The coded consequence is a buyer of shallow weakness that surrenders only on flow-confirmed strength or the risk stack. The always-armed trailer does the economic work the lofty first ROI rung (16.2%) cannot: most profit-taking in any realistic tape runs through the 1%-trail/5.8%-offset leg, not the ladder.

## Signal

Exact rule as pinned (any other band width, σ menu choice, threshold, guard combination, ROI/stop/trailing literal, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
rsi14[t]        = TA-Lib RSI(close, 14)                    // default length, Wilder smoothing
mfi14[t]        = TA-Lib MFI(high, low, close, volume, 14) // default length
typ[t]          = (high[t] + low[t] + close[t]) / 3
bbL1[t]         = qtpylib BB(20, 1σ) lower over typ        // mid/upper1, all of bands 2-4 computed
bbU2[t]         = qtpylib BB(20, 2σ) upper over typ
entry           = (close[t] < bbL1[t]) AND (volume[t] > 0) // enter_long = 1, all buy guards off
exit_sig        = (mfi14[t] > 46) AND (close[t] > bbU2[t]) AND (volume[t] > 0)  // exit_long = 1
risk            = time-decaying take-profit minimal_roi {"0": 0.162, "69": 0.097, "229": 0.061, "566": 0};
                  fixed stop at -34.5% (stoploss -0.345);
                  always-armed trailing (positive 0.01, offset 0.058, only-offset-reached False)
guard           = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the dip conjunction, `direction` long-only; `exit_long=1` on bars printing the MFI-plus-reclaim conjunction. Both are STATE-neutral levels (while positioned above the reclaim with firm flow, the exit stays true every bar — close-and-hold-flat; while flat under the 1σ rail, the entry reprints — no one-shot latch in code).
- Exact boundaries (pinned semantics): every gating comparison strict (`<` / `>` — a close exactly on either rail, MFI exactly 46, or volume exactly 0 fires nothing). The `14` / `20` / `1σ` / `2σ` / `46` literals, the four ROI rungs, the stop literal, and the trailing quadruple are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close[t] < bbL1[t]` while any signal-exit bar has `close[t] > bbU2[t]`; since `bbL1[t] = mid − 1σ ≤ mid + 2σ = bbU2[t]` on every bar (degenerate σ = 0 included), both can never co-print. ROI/stop/trailing cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `enter_short`/`exit_short`/`can_short` tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the MFI-gated reclaim signal, the four-rung ROI ladder, the −34.5% stop, and the always-armed trailing stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No breakeven move, no time exit — explicitly none, not invented.
- Bar-close precedence (predeclared derivation, disclosed): on a positioned book each completed bar evaluates closing legs in fixed order — (1) fixed stop, (2) trailing stop, (3) ROI rung, (4) signal exit; entry is evaluated only on a flat book. At most one net position change per bar by construction plus the mutual-exclusion proof.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying dip bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV with fixed non-negative offsets — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, or stop/limit order argument anywhere in the gating path. The hyperopt spaces exist but are frozen at file defaults (see Provenance); no optimiser is run by this record. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `15m` bars of BTCUSDT: `high`/`low`/`close` for the RSI(14)/typical-price/BB(20, 1–4σ) path and both rail comparisons; `high`/`low`/`close`/`volume` for the MFI(14) path; `volume` for the dual alive-tape guards. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `15m` (source-native — the file prints `timeframe = '15m'`). One evaluation per completed bar; all windows (14-bar RSI/MFI, 20-bar bands, up-to-365-bar EMAs) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule above.
- Warmup (source-count, disclosed): 999 fifteen-minute bars held flat (≈ 10.4 days). Exactly covers the source `startup_candle_count = 999` plus every indicator seed beneath it (EMA-365 needs 366, bands 20, RSI/MFI 14). Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot `15m` (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Long-only with full-unit open/close expresses natively on spot with no naked shorting and no funding leg anywhere in the rule.
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, CombinedBinHAndCluc, hlhb, TD-Sequential, and TrendFollowing siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the MFI-gated signal exit, and the stop/trailing/ROI legs are all bar-close-evaluated under the precedence above; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (disclosed, not assumed): `15m` carries PASS precedent on `main` (cmcwinner, cofibit, swinghightosky, trustrategy-ichimoku siblings) — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/precision downstream and never report hypothetical zero funding as realized funding (spot pin carries no funding leg at all).
- Sizing/capital/costs: the source ships no sizing, capital, fee, or funding concept — its ROI/stop/trailing percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay with pinned house cost assumptions, under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the dip conjunction opens the full unit on a flat book; the signal exit, any ROI rung, the stop, or the trailer closes it in full; re-entry after an exit needs only the next qualifying dip bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (163 lines: the `ta.RSI`/`ta.MFI` calls, the four typical-price BB(20, 1/2/3/4) blocks, the EMA-range loop, the default 1σ-dip entry with its volume guard, the default MFI-46-gated 2σ-reclaim exit with its volume guard, the `timeframe`/`startup_candle_count`/`minimal_roi`/`stoploss`/trailing literals, and the `Bandtastic(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance. (The Sharpe-optimisation comment header reports a fitted hyperopt print, not a verifiable sample — adopted as nothing.)

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 999-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fire nothing on equality; a close exactly on either rail, MFI exactly 46, or volume exactly 0 all hold. Strictness preserved throughout — disclosed, not smoothed.
3. Easy-entry/hard-exit asymmetry fenced: the default entry demands no oscillator proof (all buy guards ship default-off), so shallow chop that kisses the 1σ rail enters freely; the default exit demands both flow firmness and a full cross-tape reclaim, so midline recoveries are held until the risk stack. There is no trend-loss leg; the stop/trailer are the sole red-book guardrails — disclosed, not repaired.
4. Dead-plumbing fenced: bands 3/4, the mid/upper-1 rails, `bb_lowerband2`, the RSI column, both EMA-length parameter sets, and all 365 EMA columns are computed but unread by any order line under frozen defaults — compute-only, never triggers, never repaired into gates. The `RealParameter`/`DecimalParameter`/`numpy`/`pandas` imports are dead — display leftovers, never repaired.
5. Zero-variance fenced: flat tape pins band width at 0 with all rails on the mean; entry still needs a close strictly under the rail (impossible on a perfectly flat bar) and every exit needs a close strictly above the 2σ rail with MFI strictly above 46 — flat tape prints neither. No division by zero exists anywhere (all gates are comparisons) — disclosed, not repaired.
6. No-volume fenced the other way: both legs require `volume > 0`, so a zero-volume bar can neither enter nor signal-exit; ROI/stop/trailing legs still evaluate bar-close under the derived precedence. The guard is a coded fact, never a participation requirement — disclosed, not reinterpreted.
7. Cousin records fenced as different constructions (none trades a guard-free 1σ typical-price dip entry with an MFI-conjunction 2σ-reclaim exit plus an ROI-ladder/always-armed-trailing stack on `15m`): the admitted freqtrade-bband-rsi sibling needs an RSI(14)-sub-30 AND 2σ-dip conjunction with a symmetric RSI-70 exit and a single ROI/stop pair on `1h` (momentum-gated deep dip, different trigger, different exit, different risk, different frame); the admitted connorgeary150/gpsrosario/chartart/forven-bb siblings trade different RSI/BB conjunctions, edges, or breakout directions; the admitted kodify-bb350 sibling crosses a 350-period upper band with no oscillator gate and no risk stack; the admitted combined-binh-cluc sibling trades dual-leg microstructure penetration with a pump cap and profit-gated midline exit on `5m`; the admitted hlhb sibling needs a same-bar RSI-50-cross × EMA-cross × ADX-25 quadruple with a mirrored double-cross exit; the admitted crossema sibling trades EMA28/48-cross with StochRSI thresholds. Not a threshold re-tuning of any of them: moving the σ menu, softening the 46 line, enabling a guard, or dropping the conjunction would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in `user_data/strategies/` (including the `berlinguyinca/` and `futures/` pins and the hyperopt-artifact Diamond/PowerTower/mabStra neighbours) is a separate pin — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT spot market choice, the same-bar-close fills, the 999-bar warmup floor, the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the frozen-default treatment of the hyperopt spaces, the bar-close risk precedence, and house sizing/costs — all predeclared above. The `15m` frame, the 1σ-dip entry with both literals, the typical-price BB(20) basis, the MFI-46/2σ-reclaim exit with all three literals, the four-rung ladder, the −34.5% stop, the trailing quadruple, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: four-width-BB construction / frozen defaults / 1σ-dip entry / MFI-46-gated 2σ-reclaim exit / dual volume guards / ROI ladder / −34.5% stop / always-armed trailing / single-unit long-only / `15m` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — Entry-width relevance: promoting the entry trigger to the 2σ rail (same exit/risk) must not improve net expectancy; fail ⇒ the shallow 1σ dip adds nothing over the standard deep-dip trigger.
- F2 — Exit-gate relevance: dropping the MFI-46 conjunct (pure 2σ-reclaim exit, same entry/risk) must not improve net expectancy; fail ⇒ the money-flow gate adds nothing over the bare rail reclaim.
- F3 — Risk-stack relevance: removing the ROI ladder and trailer (signal/stop-only exits) must not improve net expectancy; fail ⇒ the ladder-plus-trailer adds nothing over the bare signal machine.

## Crypto portability

BTCUSDT Binance spot `15m` is the research pin (source names no market). Long-only with full-unit open/close expresses natively on spot with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Both volume guards read the venue's native candle volume. No funding leg exists in the rule, so no funding portability question arises.

## Limitations

- The `15m` frame rides existing campaign precedent — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- The signal exit fires only on flow-confirmed full-tape reclaims; an engine that adds a midline, trend-loss, or time exit would trade a different, unpinned rule.
- qtpylib BB/typical-price internals live in the Freqtrade vendor module outside the pinned file — pinned by call, not re-derived; exact reproduction inherits that module's rolling semantics alongside TA-Lib's RSI/MFI/EMA seeding.
- TA-Lib RSI(14)/MFI(14)/EMA seeding inherits the library's warmup; the 999-bar floor keeps early-bar instability out of trusted events.
- The hyperopt spaces are frozen at file defaults — any enabled guard, alternative trigger, or retuned threshold is a different, unpinned rule, never a repair.
- No breakeven move, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence` describes confidence in the research interpretation, not expected profitability.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
- https://github.com/freqtrade/freqtrade-strategies
