---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade backtest-validation SMA14/28 trend-state long-flat on BTCUSDT 1h bars
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/Freqtrade_backtest_validation_freqtrade1.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade backtest-validation SMA14/28 trend-state long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/Freqtrade_backtest_validation_freqtrade1.py`.
- GitHub blob SHA at the pinned commit: `74a1b2a1a37810aac45b2964d5a14335d0cf4650`, size 1646 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 1646 bytes, 50 lines, SHA-256 `758d3730e57c7337f988ac68420d8140a0bff72d99fa9182017cd1f8b160c869`, identical to the GitHub blob (`git hash-object` reproduces `74a1b2a1…cf4650`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Freqtrade_backtest_validation_freqtrade1(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/AdxSmas.py` (ADX-gated SMA3/6 cross edges, `1h`, open PR #331 — different periods, edge vs state, gated), `berlinguyinca/AverageStrategy.py` (EMA8/21 cross edges, `4h`, closed #391 — different averages, edge vs state), `berlinguyinca/Simple.py` (MACD-polarity plus rising-BB plus RSI70 state, `5m`, admitted — different construction), every `futures/*` pin, and every other admitted berlinguyinca pin are different pins with different gates — this record pins ONLY the validation-file literals below, and no reviewer repair may substitute a sibling constant or a sibling indicator.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '1h'`; `minimal_roi = { "40": 2.0, "30": 2.01, "20": 2.02, "0": 2.04 }`; `stoploss = -0.90`; indicators `dataframe['fastMA'] = ta.SMA(dataframe, timeperiod=14)` and `dataframe['slowMA'] = ta.SMA(dataframe, timeperiod=28)` (two explicit-period calls, no other indicator call anywhere); entry `(dataframe['fastMA'] > dataframe['slowMA'])` (`enter_long = 1`); exit `(dataframe['fastMA'] < dataframe['slowMA'])` (`exit_long = 1`); header comments (`This script is 1 of a pair the other being freqtrade_backtest_validation_tradingview1`, `These should be executed on their respective platforms for the same coin/period/resolution`, `The purpose is to test Freqtrade backtest provides like results to a known industry platform`) are lineage prose only — no recoverable rule lives in them, and no sample, window, trade count, or cost basis ships anywhere in the 50 lines. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (both resolved by name, both TA-Lib standard defaults): `ta.SMA(dataframe, timeperiod=14)` and `ta.SMA(dataframe, timeperiod=28)` (TA-Lib abstract SMA defaults `price='close'` pinned by call — both legs read the decision-bar close only through the library default; the file names no `open`/`high`/`low`/`close`/`volume` column anywhere in the gating path). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 50 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume column is ever named or read); 0 `shift` (no lag call anywhere — both legs read the decision bar's own SMA prints, persistent states, never edges); 0 `crossed` / 0 `cross` (no edge call — both legs are persistent states); 0 `hyperopt` / 0 `Parameter`; 1 `stoploss` (the `-0.90` attribute) and 1 `minimal_roi` (the four-rung `{"40": 2.0, "30": 2.01, "20": 2.02, "0": 2.04}` ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `open` / 0 `close` / 0 `high` column names (the `low` trigram fires only inside the `slowMA` identifier — no low-column read exists); 2 `ta.` (the two SMA calls); 1 `qtpylib` (the dead `import freqtrade.vendor.qtpylib.indicators as qtpylib` alone — zero `qtpylib.` calls, disclosed dead import, never a gate). The 3 `dict` tokens are the three `metadata: dict` annotations (plumbing, no gate effect). 0 `ema` / 0 `rsi` / 0 `macd` / 0 `adx` / 0 `cci` / 0 `mfi` / 0 `stoch` / 0 `fisher` / 0 `sar` as file-level indicator gates (smoothing lives only inside the two TA-Lib SMA library calls).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the SMA(14)-above-SMA(28) entry state, the SMA(14)-below-SMA(28) exit state, the four-rung 200%+ ROI ladder, the −90% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `backtest_validation`, `Freqtrade_backtest_validation_freqtrade1`, `fastMA`, and `slowMA` returns zero strategy records — no record in the pool cites this source file and no record trades an SMA14/28 state pair (the two `fastMA`/`slowMA` trigram hits are `tdi-pac` MACD 8/16/1 display plumbing on `2h` and `vcts` VWMA 13/26 TTI construction on `1d`, both fenced in Negative evidence 7). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an SMA14/28 trend-state rule. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure while the 14-bar simple average prints above the 28-bar simple average (short-horizon trend above long-horizon trend), exit while it prints below. A four-rung 200%+ ROI ladder (`2.04` at open decaying to `2.0` after 40 minutes) and a fixed −90% stoploss backstop every position — both effectively never bind in ordinary tape (see Negative evidence 5). The header states only cross-platform validation intent (Freqtrade backtest vs a known industry platform) — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Slow trend-state rider, long-only. Both averages are equal-weighted trailing means of the same close tape — the fast leg reacts in ~14 hours, the slow leg in ~28 hours, so the spread signs the medium-horizon drift without any oscillator, gate, or threshold band: a market that stays in an up-drift stays long, and a market that stays in a down-drift stays flat. There is no entry-timing trigger beyond the sign itself and no profit-harvest leg that can bind (the 200%+ ROI rungs are dead by construction while the −90% stop is a disaster backstop that almost never binds first in ordinary tape) — the signal-exit state does all the work. The failure mode is plain: a spread that oscillates around zero whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown), while a persistently positive spread that keeps bleeding holds the unit all the way down with no time exit.

## Signal

Exact rule as pinned (any other SMA periods, state-vs-edge pairing, risk rung, fill, frame, or book is a different, unpinned rule). Both SMA periods are explicit file literals (`14`, `28`), never library defaults:

```text
fastMA[t] = mean(close[t-13..t])              // SMA 14, causal
slowMA[t] = mean(close[t-27..t])              // SMA 28, causal
entry     = (fastMA[t] > slowMA[t])           // enter_long = 1, persistent state, strict
exit_sig  = (fastMA[t] < slowMA[t])           // exit_long = 1, persistent state, strict
risk      = ROI {"40": 2.0, "30": 2.01, "20": 2.02, "0": 2.04} (fraction of entry-price distance, by position age in minutes);
            fixed stop at -90% (stoploss -0.90, same basis)
floor     = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on every bar printing fast-above-slow, `direction` long-only; `exit_long=1` on every bar printing fast-below-slow. Each print is a persistent state, not a one-bar edge — a book already positioned treats further entry-state bars as hold-no-ops under the position pin below, and a flat book treats exit-state bars as no-ops.
- Exact boundaries (pinned semantics): both comparisons are strict (`>`, `<`) — a bar with `fastMA == slowMA` fires neither leg; leading-window bars print `NaN` through the trailing means and every NaN comparison is false, so under-seeded bars deterministically fire neither leg (coded library behaviour, disclosed, never repaired). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `fastMA[t] > slowMA[t]` while any signal-exit bar has `fastMA[t] < slowMA[t]` — mutually exclusive on every bar, equal, seeded, or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill); any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the below-state signal exit, the four-rung 200%+ ROI ladder, and the −90% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rungs and stop are fractions of entry-price distance (close-to-close price return), evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. No trailing, no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-state bars as no-ops; re-entry re-arms on any qualifying fast-above-slow bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar closes through two trailing means with fixed non-negative offsets — no forward reference — under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (both SMA legs read the same close tape through the TA-Lib default price; no `open`/`high`/`low` column is named anywhere, no bar `volume` is read by any order-gating line). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 hourly bars held flat. Covers the 28-bar slow-SMA seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: trailing means print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed, and TechnicalExample-CMF siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the signal-exit state, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the ADXMomentum, AwesomeMacd, and BbandRsi records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the fast-above-slow state opens the full unit on a flat book; the fast-below-slow state, the ROI ladder, or the stop closes it in full; re-entry after an exit needs only the next fast-above-slow bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (50 lines: the two `ta.SMA(dataframe, timeperiod=…)` calls, the two strict trend-state legs, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `Freqtrade_backtest_validation_freqtrade1(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance. The header's cross-platform validation intent is prose lineage only.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: trailing means print NaN until seeded and every strict NaN comparison is false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-equal rule fenced: both legs are strict — a bar printing exactly `fastMA == slowMA` fires neither leg. Strictness preserved throughout — disclosed, not smoothed.
3. No-division fence: both averages are equal-weighted means with no divisor that can vanish on real tape (unlike money-flow ratios) — no degenerate `0/0 = NaN` path exists beyond the leading-window NaN already fenced; no repair converts a flat tape into a signal.
4. Prose-vs-code fence: the three header comment lines (pair-platform intent, same coin/period/resolution guidance, backtest-parity purpose) are prose — the coded legs are the two strict SMA-state comparisons, so the comments neither narrow nor widen any gate. Coded legs govern; prose never does. The dead `qtpylib` import (zero `qtpylib.` calls) is plumbing, never a hidden indicator.
5. Dead-risk fence: the four ROI rungs (`2.04`/`2.02`/`2.01`/`2.0` = 204%/202%/201%/200%) require a ≥200% close-to-close excursion to bind while the −90% stop requires a −90% excursion — by construction both are disaster/dead legs that almost never bind before the trend-state exit in ordinary tape. Coded facts, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
6. No-edge fence: the file contains zero `crossed_*` calls and zero `shift` calls — both legs are persistent states evaluated on the decision bar's own SMA prints. Converting either leg to a cross-edge (or vice versa) would be a different, unpinned rule with different trade events.
7. Cousin records fenced as different constructions (none trades a 14/28 SMA trend-state pair, long-flat, with a 200%+ ROI ladder plus a −90% stop): the open `research/hermes-adx-smas` PR trades SMA3/6 one-bar CROSS edges behind an ADX25 gate with a 10% ROI rung plus a −25% stop (`1h`, berlinguyinca source — a market pinned fast-above-slow fires an entry here but nothing there unless a cross just printed with ADX > 25); the `futures/*` FAdxSma family (closed, never merged) trades SMA12/48 ADX-gated edges two-sided; the closed AverageStrategy (EMA8/21 cross edges, `4h`) trades exponential averages as edges, not simple averages as states; the admitted `freqtrade-simple-macd-bb-rsi` pool-mate trades a four-way MACD-polarity plus rising-BB plus RSI70 conjunction exited by RSI80 (`5m`); the `tdi-pac` pool-mate's `fastMA 8 / slowMA 16` trigram is a MACD 8/16/1 display parameter inside a TDI/PAC alert-reversal system (`2h`, TradingView source); the `vcts` pool-mate's `fastMA`/`slowMA` trigram is a VWMA 13/26 TTI construction (`1d`). Not a threshold re-tuning of any of them: moving either SMA period, converting either state to an edge, adding any gate, or changing the ROI ladder, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `AverageStrategy.py`, `AdxSmas.py`, `Simple.py`, `MACDStrategy.py`, `MACDStrategy_crossed.py`, `Quickie.py`, `BinHV27.py`, `CCIStrategy.py`, `Low_BB.py`, `Scalp.py`, `TechnicalExampleStrategy.py`, and every other file in the collection (including all seven `futures/*` pins) are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the TA-Lib SMA close-default price (pinned by call with explicit periods 14/28, never re-derived), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1h` frame, the SMA(14)-above-SMA(28) entry leg with all its literals and strictness, the SMA(14)-below-SMA(28) exit leg, the four-rung ROI ladder with the −90% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA(14)/SMA(28) / strict trend states / persistent-state legs / below-state signal exit / four-rung 200%+ ROI / −90% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Trend-filter relevance: entering on the first post-warmup bar and holding time-in-market (same ROI/stop exits, no SMA legs) must not improve net expectancy; fail ⇒ the trend filter adds nothing over blind exposure.
- F2 — Period-pair relevance: replacing the 14/28 pair with a 14/14 identity (fast equals slow — never fires) or a swapped 28/14 pair (mirror image) must not improve net expectancy; fail ⇒ the coded period pair adds nothing over its degenerate twin.
- F3 — Risk-leg relevance: removing the ROI ladder/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 200%+ ladder plus −90% backstop adds nothing over the bare state machine (expected — both legs are dead by construction).

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Closes are native Binance kline fields on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent (ADXMomentum, AwesomeMacd, BbandRsi `1h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose fast average never prints below the slow average is held until the ROI ladder or the −90% stop; a market whose spread oscillates around zero whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown to damp them — disclosed as the principal friction). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- The 200%+ ROI ladder and −90% stop are dead by construction in ordinary tape — the signal-exit state does all the work; exact reproduction inherits that dead-leg property alongside the 40-bar floor.
- Vendored indicator internals (trailing-mean seeding, NaN propagation) live in the TA-Lib library outside the pinned file — pinned by call with explicit periods 14/28, not re-derived; exact reproduction inherits that library's seeding alongside the 40-bar floor.
- The header prose and the dead `qtpylib` import are inert — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/Freqtrade_backtest_validation_freqtrade1.py
- https://github.com/freqtrade/freqtrade-strategies
