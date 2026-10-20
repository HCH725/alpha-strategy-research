---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade MACDStrategy MACD-CCI dip-state long-flat on BTCUSDT 5m bars
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
  - https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/MACDStrategy.py
  - https://github.com/berlinguyinca/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade MACDStrategy MACD-CCI dip-state long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/berlinguyinca/freqtrade-strategies (open-source Freqtrade strategy collection; the original upstream of the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, and `freqtrade-asdts-rockwell` records — this is only its ninth record, and the first pinned to this upstream rather than the `freqtrade/` fork).
- Pinned commit SHA: `ae998aec37cd4c83b8f0e512d9ea44edc7726351` (committed `2018-06-27T17:27:40Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/MACDStrategy.py`.
- GitHub blob SHA at the pinned commit: `93f4dd97e4df4c31e37488231cb89bd392d6db73`, size 2313 bytes.
- Byte-identity check: the file downloaded via the GitHub contents API at the pinned commit is 2313 bytes, 84 lines, SHA-256 `8f8d065fbd7fecdc843a28fa75103d21620cbe89e7f095f1ffa356a39e5223c8`, identical to the GitHub blob (`git hash-object` reproduces `93f4dd97…392d6db73`) — the entire file was retrieved and inspected.
- Registration: the file defines class `MACDStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/ADXMomentum.py` (ADX/DI/MOM four-conjunct state, `1h`), `berlinguyinca/ASDTSRockwellTrading.py` (dual-polarity MACD state, `5m`), `berlinguyinca/AdxSmas.py` (SMA3/6 cross gated by ADX polarity, `1h`, open PR #331), `berlinguyinca/AwesomeMacd.py` (AO-cross gated by MACD polarity, `1h`), `berlinguyinca/BbandRsi.py` (RSI dip with BB penetration, `1h`), `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards, `5m`), `berlinguyinca/EMASkipPump.py` (EMA-stack dip with volume veto, `5m`), and `berlinguyinca/CMCWinner.py` (CCI+MFI+CMO triple-oversold state, `15m`) are different pins with different gates — this record pins ONLY the MACDStrategy file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): docstring idea `MACD above MACD signal and CCI < -50` (uptrend), `MACD below 0 line and below MACD signal and CCI > 100` (downtrend); `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.3`; `ticker_interval = '5m'` (old-API frame spelling — the file prints `ticker_interval`, never `timeframe`); indicators `macd = ta.MACD(dataframe)` and `dataframe['cci'] = ta.CCI(dataframe)` (both called with NO argument — TA-Lib defaults apply, disclosed below, never overridden anywhere in the file); entry `(dataframe['macd'] > dataframe['macdsignal']) & (dataframe['cci'] <= -50.0)` (`buy = 1`); exit `(dataframe['macd'] < dataframe['macdsignal']) & (dataframe['cci'] >= 100)` (`sell = 1`). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.MACD` (TA-Lib MACD on close, default fastperiod 12 / slowperiod 26 / signalperiod 9 — no override in the file; the histogram leg is computed into `macdhist` and never read by any order line, fenced below); `ta.CCI` (TA-Lib Commodity Channel Index on high/low/close, default period 14 — no override in the file). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits — the single `hyperopt` token is the dead `from hyperopt import hp` import with zero `hp.` calls anywhere), no informative-pair call in the file.
- Full-file token census (verified over the 84 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — both legs are persistent states, never one-bar edges); 0 `volume` (no volume read of any kind — CCI reads high/low/close only); 0 `shift` (no lag call — per-bar state evaluation under the file's own framework contract); 3 `stoploss` (two comment lines plus the `-0.3` attribute) and 2 `minimal_roi` (one comment line plus the four-rung ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`. `Dict`, `List`, `hp`, `reduce`, and `qtpylib` are imported and never called — dead imports, fenced as plumbing with no gate effect.

Pre-write dedup (2026-10-20): working-tree filename/content search for `macdstrategy` (case-insensitive) returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross) trades a MACD-plus-CCI conjunction state. MACD/CCI cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: buy the bar printing MACD above its signal line together with CCI at or under −50 (momentum-bias plus oversold-dip conjunction), sell the bar printing MACD below its signal line together with CCI at or over +100 (momentum-loss plus overbought conjunction). A four-rung ROI ladder (`0.05` from open, `0.04` after 20 min, `0.03` after 30 min, `0.01` after 60 min) and a fixed −30% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Dip-in-trend conjunction state, long-only. The MACD leg supplies the trend bias (momentum still accelerating versus its own smoothing) while the CCI leg demands the bar also sit in an oversold dip (entry) — so a strong-rally bar with elevated CCI prints nothing, and a deeply oversold bar in a rolled-over MACD regime prints nothing either. The exit mirrors the construction with an asymmetric overbought threshold (+100 versus −50): the book is held through mild MACD wobble unless the oscillator confirms exhaustion, and held through elevated CCI unless momentum actually rolls. Unlike cross-edge records (trade the single crossing bar), no cross is ever traded: both legs are persistent states re-evaluated per bar, and a book already positioned treats further entry bars as hold-no-ops. The exit is deliberately narrower than a pure signal-line-loss rule — both the MACD loss AND the overbought print are required — so a scheme that exits on either leg alone would be a different, unpinned rule.

## Signal

Exact rule as pinned (any other MACD/CCI periods, thresholds, strictness, comparison pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; MACD periods are TA-Lib library defaults (12/26/9) and the CCI period is the TA-Lib default (14), disclosed, never overridden in the file:

```text
macd[t], signal[t] = TA-Lib MACD(close, 12, 26, 9)  // defaults — no file override; hist leg discarded
cci[t]             = TA-Lib CCI(high, low, close, 14) // default — no file override
entry    = (macd[t] > signal[t]) AND (cci[t] <= -50.0)  // buy = 1, persistent state
exit_sig = (macd[t] < signal[t]) AND (cci[t] >= 100)    // sell = 1, persistent state
risk     = ROI ladder {"0": 0.05, "20": 0.04, "30": 0.03, "60": 0.01} (fraction, by position age in minutes);
           fixed stop at -30% (stoploss -0.3)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `buy=1` on any bar printing the MACD-over-signal plus oversold-CCI state, `direction` long-only; `sell=1` on bars printing the MACD-under-signal plus overbought-CCI state. Each print is a state print re-evaluated per bar, not a one-bar edge — a book already positioned treats further entry bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the MACD comparisons are strict (`>`, `<`) while the CCI comparisons are inclusive (`<=`, `>=`) — a bar with `macd == signal` fires neither leg; a bar with `cci == -50.0` fires the entry CCI leg; a bar with `cci == 100` fires the exit CCI leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `macd[t] > signal[t]` while any signal-exit bar has `macd[t] < signal[t]` — and additionally any entry bar has `cci[t] <= -50` while any signal-exit bar has `cci[t] >= 100`. Both pairings are mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the conjunct signal exit, the four-rung ROI ladder, and the −30% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying conjunct-dip bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (MACD triple smoothing plus CCI mean-deviation, fixed non-negative offsets — no forward reference) with no `shift` call because Freqtrade's `populate_*_trend` evaluates per completed bar under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` only (MACD on `close`; CCI on `high`/`low`/`close`). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; every window reads the decision bar's causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 five-minute bars held flat. Covers the TA-Lib MACD seed (26-bar slow EMA plus 9-bar signal smoothing ≈ 35 bars) and the 14-bar CCI seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict/inclusive NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, and ASDTSRockwell siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the conjunct signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, and ASDTSRockwell records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the conjunct-dip state opens the full unit on a flat book; the conjunct signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying conjunct-dip bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (84 lines: the default-period MACD and CCI calls, the conjunct-dip long state, the conjunct signal exit, the `ticker_interval`/`minimal_roi`/`stoploss` literals, and the `MACDStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the MACD legs are strict (`>`/`<`) while the CCI legs are inclusive (`<=`/`>=`) — a bar sitting exactly on the signal line fires nothing on either side; a bar sitting exactly on −50.0 (100) satisfies the entry (exit) CCI leg. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `Dict`, `List`, `hp`, `reduce`, and `qtpylib` are imported and never called anywhere in the 84 lines — display/plumbing leftovers with no gate effect, never repaired into a signal. The single `hyperopt` token is that dead import alone: zero `hp.` calls, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.
4. Dead-histogram fence: `macdhist` is computed into the frame and read by no order line — the histogram plays no gating role, never repaired into a third leg.
5. Prose-vs-code fence: the docstring's `downtrend definition` (MACD below zero AND below signal AND CCI > 100) is prose — the coded exit requires only MACD below signal AND CCI ≥ 100 with no zero-line leg, so a positive-but-rolling-over MACD with hot CCI still exits. Symmetrically the coded entry has no zero-line leg either. Coded legs govern; prose never narrows or widens them.
6. Wide-stop fence: the −30% stop is ~6× the opening `0.05` ROI rung — by construction the stop is a disaster backstop that almost never binds before an ROI rung or the conjunct signal exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
7. Cousin records fenced as different constructions (none trades a MACD-polarity-plus-CCI-threshold conjunction state long-flat with an ROI ladder): the admitted `freqtrade-asdts-rockwell` pool-mate trades a dual-polarity MACD state (zero-line AND signal-line) with a signal-line-only exit — this record replaces the zero-line leg with the inclusive CCI dip/exhaustion legs on both sides; the admitted `freqtrade-awesome-macd` pool-mate trades an AO cross gated by MACD polarity (edge vs state); the admitted `freqtrade-cmcwinner` pool-mate trades a CCI+MFI+CMO triple-oversold state with a one-bar `shift(1)` lag (triple vs pair, lagged vs same-bar); the admitted `cci-threshold-extreme-reversal` and `cci-ema-rsi-cross-trailing-stop` pool-mates are pure/single-CCI systems with no MACD leg and different exits (reversal closes / trailing ratchet vs ROI ladder); the admitted `forven-macd-cross-adx-regime` pool-mate trades a MACD cross edge gated by an ADX regime (edge-plus-regime vs conjunct state). Not a threshold re-tuning of any of them: moving any MACD/CCI period, dropping either conjunction leg, converting either state to a cross edge, flipping any strictness, or changing any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Fork-divergence fence: the `freqtrade/` fork's newer revision of this same filename adds live `IntParameter` hyperopt spaces (`buy_cci`/`sell_cci`), fitted `buy_params`/`sell_params` (`-48`/`687`), a `volume > 0` guard, and `populate_entry/exit_trend` renames (3052 bytes, blob `94595a28…f2a1a58` at fork commit `f3340ce`) — that fitted artifact is NOT pinned here. This record pins ONLY the hardcoded `-50.0`/`100` upstream artifact above; no reviewer repair may substitute the fork's fitted constants, spaces, or guards.
9. Sibling-file fence: `ADXMomentum.py`, `AdxSmas.py`, `ASDTSRockwellTrading.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, `EMASkipPump.py`, and `CMCWinner.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
10. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the TA-Lib default-period readings (MACD 12/26/9, CCI 14 — library defaults, never file literals), and house sizing/costs — all predeclared above. The `5m` frame, the conjunct-dip entry with all its literals and strictness, the conjunct signal exit, the four-rung ROI ladder with the −30% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: MACD(12,26,9) / CCI(14) / conjunct legs / `-50.0`+`100` thresholds with pinned strictness / persistent-state legs / conjunct signal exit / four-rung ROI ladder / −30% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — CCI-dip relevance: dropping the CCI legs (pure MACD-polarity state, same exit MACD leg only, same risk) must not improve net expectancy; fail ⇒ the oversold-dip witness adds nothing over trend polarity.
- F2 — MACD-bias relevance: dropping the MACD legs (pure CCI-dip state: long while `cci <= -50`, exit while `cci >= 100`, same risk) must not improve net expectancy; fail ⇒ the momentum-bias witness adds nothing over the oscillator alone.
- F3 — Risk-ladder relevance: removing the ROI ladder/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the four-rung ladder plus −30% backstop adds nothing over the bare state machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose MACD stays above its signal line without printing the conjunct exit is held until an ROI rung or the −30% stop; a market that oscillates with hot CCI but intact MACD polarity prints repeated hold-no-ops with no flat state to rest in, while a market that rolls MACD without hot CCI likewise holds (conjunct-exit profile, disclosed). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (EMA seeding, default-period handling, CCI mean-deviation arithmetic) live in the library outside the pinned file — pinned by call with default periods 12/26/9 and 14, not re-derived; exact reproduction inherits that library's seeding alongside the 40-bar floor.
- The `Dict`/`List`/`hp`/`reduce`/`qtpylib` imports and the `macdhist` column are dead — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/berlinguyinca/freqtrade-strategies/blob/ae998aec37cd4c83b8f0e512d9ea44edc7726351/user_data/strategies/berlinguyinca/MACDStrategy.py
- https://github.com/berlinguyinca/freqtrade-strategies
