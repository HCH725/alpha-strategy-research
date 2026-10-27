---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade HourBased UTC-hour-window long-flat on BTCUSDT 1h bars
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-07-10
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/HourBasedStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade HourBased UTC-hour-window long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official, open-source Freqtrade strategy collection; the upstream lane that supplied the admitted `freqtrade-swinghightosky`, `freqtrade-strategy001` through `freqtrade-strategy004`, and `freqtrade-multima` records — this is a different file pin with different constants).
- Pinned commit SHA: `7f91ff52bb664423ae673092a6a18d76c50c2c29` (committed `2022-07-10T09:44:41Z`, message `Add INterface_version to all strategies`; the most recent commit touching this file path per the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/HourBasedStrategy.py`.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 4270 bytes, 104 lines, SHA-256 `61755d49c46b3037c102f60de30841910472b6da06e9b578882b3dfc125b9ccc`, git blob SHA-1 `8f0abc74262da360b2cfb8ac853cc83e8376a612` — and byte-identical to the `main`-HEAD download this cycle (no later commit touched the file). The entire file was retrieved and inspected.
- Registration: the file defines class `HourBasedStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, every sibling file under `user_data/strategies/` and `user_data/strategies/berlinguyinca/` is a different pin with different constants — this record pins ONLY the HourBasedStrategy literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '1h'`; `buy_params = { "buy_hour_max": 24, "buy_hour_min": 4 }`; `sell_params = { "sell_hour_max": 21, "sell_hour_min": 22 }`; `minimal_roi = { "0": 0.528, "169": 0.113, "528": 0.089, "1837": 0 }`; `stoploss = -0.10`; entry is `dataframe['hour'].between(self.buy_hour_min.value, self.buy_hour_max.value)` where `dataframe['hour'] = dataframe['date'].dt.hour`; exit is `dataframe['hour'].between(self.sell_hour_min.value, self.sell_hour_max.value)`. The header comment states the intent (`find the best hours to buy and sell in a day (in hourly timeframe)`, `you should just use 1h timeframe`) and ships four commented hyperopt anecdote blocks (SHIB/SAND/KDA single-pair and one six-pair run with trade counts, profit percents and durations) — comments only, fenced below, never operative legs.
- Out-of-file calls pinned: none. The gating path uses zero indicator libraries, zero resampling, zero informative merges, zero cross/edge helpers — the only dataframe operation is `.dt.hour` plus two pandas `.between` calls. No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 104 lines this cycle): 0 `short` (case-insensitive — no short leg anywhere); 0 `trailing`; 0 `startup`; 0 `resample` / 0 `informative`; 0 `request` / 0 `security`; 0 `shift` (no lag call of any kind — the rule reads only the decision bar's own hour); 0 `cross`; 0 `volume`; 0 `leverage` / 0 `futures` / 0 `funding` / 0 `mark_price`; 0 `can_short` / 0 `max_open_trades` / 0 `order_types` / 0 `order_time_in_force`; 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `use_exit` / 0 `exit_profit_only`; 4 `IntParameter` constructors (buy min/max, sell min/max — values resolved from the operative dicts below, never from constructor defaults alone); 2 `.between` (the only two gate lines); 1 `stoploss` attribute (`-0.10`) and 1 `minimal_roi` ladder as the only risk legs. The header's `hyperopt` tokens are the command-line comment lines alone: zero `hp.` calls, zero fitted values anywhere in the operative code.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market — its anecdotes use SHIB/SAND/KDA); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 20-bar researcher warmup floor; (4) the house cost/capital overlay replaces the absent source economics; (5) the UTC-hour reading of the `date` column and the empty-sell-window consequence below are disclosed framework readings. Every hour bound, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-27): working-tree filename/content search for `HourBased`, `hourbased`, `hour.*between`, and `dt.hour` returns zero strategy records — no record in the pool gates entries on candle hour-of-day. The pool's nearest time-structured records are fenced as different constructions in Negative evidence 7 (intraday momentum timing, IST-window breakout, weekday-filtered indicator systems, turn-of-month holds — none is an hour-window state with ROI-ladder exits). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) trades an hour-of-day system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bars whose hour-of-day falls inside the fitted buy window, exit on the sell window, otherwise let a four-rung time-decaying ROI ladder (52.8% → 11.3% → 8.9% → breakeven) and a −10% stop close the trade. No behavioural, structural, or risk-premium channel is claimed anywhere in the 104 lines; the header frames it only as finding the best hours to buy and sell.

### Research interpretation

Pure intraday-seasonality long-flat holder with no price, volume, or indicator condition of any kind: inside UTC hours 04–23 the book wants to be long; outside them it never opens. With the frozen sell window empty (proved below), the strategy is an open-and-wait system — every in-window entry is closed only by profit-decay targets or the disaster stop, never by a clock or an opposite signal. Unlike window-breakout systems (which need a range print) or weekday systems (which still need an indicator trigger), this rule fires on time alone, so its trade count is bounded by clock arithmetic, not by market prints.

## Signal

Exact rule as pinned (any other hour bound, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
hour[t] = hour-of-day of the completed 1h bar t (UTC reading, disclosed)
entry = hour[t] BETWEEN 4 AND 24, both ends inclusive   // enter_long = 1 (state)
exit_sig = hour[t] BETWEEN 22 AND 21                   // exit_long = 1 (never fires: empty set)
risk = time-decaying take-profit minimal_roi {"0": 0.528, "169": 0.113, "528": 0.089, "1837": 0};
       fixed stop at -10% (stoploss -0.10)
guard = leading-window bars: flat by record rule (see Required data)
```

- Trade events: `enter_long=1` on every bar printing the in-window hour state, `direction` long-only; the hour exit leg provably never prints (see boundaries). Both ROI/stop legs are bar-close-evaluated under the derived fill convention below. Entry prints are STATE prints (while flat and in-window they stay true every qualifying bar — first qualifying bar opens, no one-shot latch in code).
- Hour arithmetic (pinned semantics): pandas `.between` is inclusive on both ends, so entry covers hour values 4, 5, …, 23 (20 of 24 hourly bars — hour value 24 never occurs on a 0–23 clock). Bars at UTC 00:00–03:59 never print entry. The sell `.between(22, 21)` has left > right and therefore matches nothing on any bar — file-literal consequence, disclosed, never repaired into a clock exit.
- Parameter-resolution note (disclosed framework reading): the four `IntParameter(0, 24, default=…)` constructors ship defaults (1, 0, 1, 0) that are superseded at runtime by the checked-in `buy_params` / `sell_params` dicts — the operative frozen values are exactly the dict literals (4/24 buy, 22/21 sell). Under constructor defaults alone the entry window would also be empty; the dict values are the file's own operative pin and are preserved verbatim here.
- UTC note (disclosed framework reading): `hour` is read off the strategy dataframe's `date` column — exchange-UTC candle timestamps under the freqtrade UTC-date convention. A non-UTC feed mapping would be a different, unpinned rule. The official strategy-customization documentation fetched this cycle independently confirms the `minimal_roi` dict keys are minutes-since-trade-open (52.8% from open, 11.3% after 169 min, 8.9% after 528 min, any non-loss after 1837 min ≈ 30.6 h).
- Same-bar co-print pin (proved, not asserted): the only hour exit set is empty, so no entry/exit co-print can ever reach the engine and no fill-ordering invention is ever needed. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere, and no `can_short` attribute enables shorting — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the four-rung ROI ladder and the −10% stop are the complete position-closing set. No trailing, no time exit beyond the ROI clock, no breakeven move, no opposite-signal exit that can fire — explicitly absent or empty, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further in-window entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats risk legs as no-ops; re-entry re-arms on any qualifying in-window bar after any exit (no cooldown specified — explicitly none, not invented). Pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only the completed bar's own timestamp hour with fixed non-negative references (no trailing window at all, no forward reference) — no indicator, no volume read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `1h` bars of BTCUSDT: the `date` (opening timestamp, UTC reading) for the hour gate; `high`/`low`/`close` only to evaluate the derived bar-close ROI/stop legs and fills. No volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'` and its header directs hourly use). One evaluation per completed bar; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 20 one-hour bars held flat (~20 hours). The hour gate needs no indicator seed — the floor exists only to guarantee a contiguous, validity-checked candle run before any decision. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; its comment anecdotes use SHIB/SAND/KDA and are fenced as non-operative; no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry and ROI/stop legs are all bar-close-evaluated; the Signal co-print proof leaves no ambiguous same-bar fill order to the engine. The source-native freqtrade stop/ROI would be intrabar-checked; the close-only evaluation is a declared derivation (protective-stop economics are NOT reproduced — a gap through the stop realizes the close, disclosed as a material limitation).
- Interval precedent (exact, disclosed): exact-`1h` PASS records saturate `main` (including admitted Freqtrade-sourced long-flat records) — this record rides the same specified single-frame completed-bar `1h` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the in-window hour state opens the full unit on a flat book; any ROI rung or the stop closes it in full; re-entry after an exit needs only the next qualifying in-window bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (104 lines: the hour-column wiring, the two `.between` gate lines, the `timeframe`/`buy_params`/`sell_params`/`minimal_roi`/`stoploss` literals, and the `HourBasedStrategy(IStrategy)` class pin). Its comment blocks additionally carry hyperopt anecdotes for non-operative parameter sets on SHIB/USDT, SAND/USDT, KDA/USDT and one six-pair run (trade counts 51–158, profit percents up to four digits, durations) — quoted scope only; this record claims no source-reported performance for the frozen operative pin.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Empty-sell-window fenced (proved, not asserted): `sell_hour_min=22 > sell_hour_max=21` makes the exit `.between(22, 21)` match no hour value on any bar — the hour exit leg is dead by file-literal arithmetic. Position closes only via the ROI ladder or the −10% stop. No reviewer repair may invent a clock exit.
2. Constructor-default trap fenced: the `IntParameter` defaults (1, 0, 1, 0) would leave the entry window empty if read alone; the operative values are the checked-in dicts (4/24 buy). Both readings are file-literal; the dict-supersedes-default resolution is the disclosed framework reading — never tuned here.
3. Boundary hours fenced: inclusive `.between` admits hour 4 and hour 23; UTC 00:00–03:59 bars never print entry; hour value 24 never occurs so the `buy_hour_max=24` bound bites only as an inclusive ceiling. An hour landing exactly on 4 or 23 fires; no other clock value does.
4. Zero-indicator fenced: no TA library, no window, no seed, no NaN-leading-edge behaviour exists anywhere in the gating path — the only invalid-input case is a missing/malformed bar, which aborts the research sample, never yields a signal.
5. Comment-anecdote fence: the four `buy_params`/`sell_params`/`minimal_roi`/`stoploss` comment blocks (lines 21–50) are hyperopt outputs for other markets and other parameter sets — explicitly non-operative; this record never conditions on them and no reviewer repair may promote any of them into a leg.
6. Derivation-effect fenced: this record computes no behaviour differently from the file's letter — the five adaptations are market choice, fill convention, position/warmup pins, house economics, and the UTC/empty-window readings only. Every hour bound, the ROI ladder, and the stop are verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none gates entries on candle hour-of-day with ROI-ladder-only exits): the admitted `bitcoin-intraday-first-halfhour` sibling times momentum between the first/last 30-minute window on `30m` (momentum-timing construction, no hour-state entry, different source); the FMZ time-range-breakout sibling trades an IST-window high/low breakout with a 2R bracket (breakout construction, different repository family); the admitted `turnaround-tuesday` sibling filters weekdays AND requires SMA30/RSI3/ATR gates (indicator-gated weekday construction); the admitted `turn-of-month` sibling holds a fixed 4-day calendar window (holding construction, no hourly state, no ROI ladder). Not a threshold re-tuning of any of them: changing any hour bound, any ROI rung, or the stop would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file under `user_data/strategies/` and `user_data/strategies/berlinguyinca/` (Strategy001–005 samples, Quickie, MultiMA, Diamond, PowerTower, SmoothScalp, and the rest) is a separate pin — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 20-bar warmup floor, house sizing/costs, UTC/empty-window readings) — all predeclared above. The `1h` frame, the hour-window entry with every literal, the empty hour exit, the four-rung ROI ladder, the −10% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: hour-window entry / all bounds / four-rung ROI / −10% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window relevance: entering on every completed bar regardless of hour (same exit/risk) must not improve net expectancy; fail ⇒ the 04–23 UTC window adds nothing over always-long availability.
- F2 — Profit-decay relevance: replacing the four-rung ladder with a single take-profit at the rung mean (same entry/stop) must not improve net expectancy; fail ⇒ the time-decayed profit schedule adds nothing over a flat target.
- F3 — Stop relevance: removing the −10% stop (same entry/ROI ladder) must not improve net expectancy; fail ⇒ the disaster stop adds nothing over ladder-only exits.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. Every window is a trailing clock-hour state, portable across 24/7 crypto tape with no equity-hours concept. No volume feed is read at all — only the bar timestamp plus standard `high`/`low`/`close` fields; no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `buy_params`/`sell_params`-supersede-defaults resolution and the UTC-hour reading are disclosed framework readings, not file literals; a non-UTC feed mapping or a defaults-only parameter resolution would each be a different, unpinned rule.
- The close-only ROI/stop evaluation is a derivation: source-native freqtrade checks stops intrabar, so gap-through-stop losses are understated versus live semantics — disclosed, never repaired.
- No trailing, no breakeven, no time exit beyond the ROI clock, no short leg, no cooldown, no functioning hour exit — all explicitly absent or empty, never to be added by repair.
- The header hyperopt anecdotes (SHIB/SAND/KDA/six-pair, large percents) describe non-operative parameter sets on other markets and are not performance evidence for this pin.
- Source publication commit date is not a version-pinned strategy revision beyond the file pin itself. A later contradictory primary-source fact must be independently reviewed, not silently rewritten.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/HourBasedStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
