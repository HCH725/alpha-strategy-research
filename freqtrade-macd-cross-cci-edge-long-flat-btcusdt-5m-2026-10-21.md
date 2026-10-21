---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade MACDStrategy_crossed MACD-cross CCI-gated edge long-flat on BTCUSDT 5m bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/MACDStrategy_crossed.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade MACDStrategy_crossed MACD-cross CCI-gated edge long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, and `freqtrade-binhv27` records — this is only its tenth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/MACDStrategy_crossed.py`.
- GitHub blob SHA at the pinned commit: `5d5f12d9063d3aba767ee5e64d8d3e0419a4af0e`, size 2335 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2335 bytes, 78 lines, SHA-256 `af5aed1cbb9a9d3ed519ea8649363a2cfaa95cbffe443f073d9f96b2aa91b0f6`, identical to the GitHub blob (`git hash-object` reproduces `5d5f12d9…19a4af0e`) — the entire file was retrieved and inspected.
- Registration: the file defines class `MACDStrategy_crossed(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/MACDStrategy.py` (persistent MACD-polarity-plus-CCI state, no cross edge — separately admitted), `berlinguyinca/ADXMomentum.py` (ADX/DI/MOM four-conjunct state, `1h`), `berlinguyinca/ASDTSRockwellTrading.py` (dual-polarity MACD state, `5m`), `berlinguyinca/AdxSmas.py` (SMA3/6 cross gated by ADX polarity, `1h`, open PR #331), `berlinguyinca/AwesomeMacd.py` (AO-cross gated by MACD polarity, `1h`), `berlinguyinca/BbandRsi.py` (RSI dip with BB penetration, `1h`), `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards, `5m`), `berlinguyinca/EMASkipPump.py` (EMA-stack dip with volume veto, `5m`), `berlinguyinca/CMCWinner.py` (CCI+MFI+CMO triple-oversold state, `15m`), and `berlinguyinca/ClucMay72018.py` (BB-discount EMA-gated state, `5m`, open PR #350) are different pins with different gates — this record pins ONLY the MACDStrategy_crossed file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): docstring idea `MACD crosses MACD signal above and CCI < -50` (buy), `MACD crosses MACD signal below and CCI > 100` (sell); `minimal_roi = { "60": 0.01, "30": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.3`; `timeframe = '5m'`; indicators `macd = ta.MACD(dataframe)` and `dataframe['cci'] = ta.CCI(dataframe)` (both called with NO argument — TA-Lib defaults apply, disclosed below, never overridden anywhere in the file); entry `qtpylib.crossed_above(dataframe['macd'], dataframe['macdsignal']) & (dataframe['cci'] <= -50.0)` (`enter_long = 1`); exit `qtpylib.crossed_below(dataframe['macd'], dataframe['macdsignal']) & (dataframe['cci'] >= 100.0)` (`exit_long = 1`). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.MACD` (TA-Lib MACD on close, default fastperiod 12 / slowperiod 26 / signalperiod 9 — no override in the file; the histogram leg is computed into `macdhist` and never read by any order line, fenced below); `ta.CCI` (TA-Lib Commodity Channel Index on high/low/close, default period 14 — no override in the file); `qtpylib.crossed_above` / `qtpylib.crossed_below` (standard Freqtrade one-bar edge: `(s1 > s2) & (s1.shift(1) <= s2.shift(1))` and its mirror — causal two-bar comparison, disclosed, never redefined). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 78 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume read of any kind — CCI reads high/low/close only); 0 `shift` (no lag call in the file body — the single one-bar lookback lives inside the standard `crossed_*` edge, disclosed above); 0 `hyperopt` / 0 `Parameter`; 3 `stoploss` (two comment lines plus the `-0.3` attribute) and 2 `minimal_roi` (one comment line plus the four-rung ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`. `Dict`, `List`, and `reduce` are imported and never called — dead imports, fenced as plumbing with no gate effect. The 5 `cross` tokens are the class name, the two docstring `crosses` words, and the two `crossed_*` edge calls — nothing further.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the MACD-cross-plus-CCI entry edge, the mirrored conjunct exit edge, the four-rung ROI ladder, the −30% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `macdstrategy_crossed` (case-insensitive) returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount) trades a MACD-cross-plus-CCI conjunction edge. MACD cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: buy the single bar where MACD crosses up through its signal line together with CCI at or under −50 (rotation edge plus oversold-dip conjunction), sell the single bar where MACD crosses down through its signal line together with CCI at or over +100 (rotation edge plus overbought conjunction). A four-rung ROI ladder (`0.05` from open, `0.04` after 20 min, `0.03` after 30 min, `0.01` after 60 min) and a fixed −30% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Rotation-edge dip machine, long-only. The MACD-cross leg supplies the timing (momentum rotation confirmed on this exact bar) while the CCI leg vetoes rotations printed without an oversold washout (entry) — so a cross fired from an already-elevated oscillator prints nothing, and a deeply oversold bar without a rotation prints nothing either. The exit mirrors the construction with an asymmetric overbought threshold (+100 versus −50): the book is held through every non-crossing bar by design, and even a death-cross bar is held unless the oscillator confirms exhaustion. Unlike persistent-state records (trade every bar the condition holds), each leg can fire at most on its crossing bar — a book already positioned treats further bars as hold-no-ops until a qualifying exit edge, an ROI rung, or the stop. The exit is deliberately narrower than a pure cross-down rule — both the rotation AND the overbought print are required — so a scheme that exits on either leg alone would be a different, unpinned rule.

## Signal

Exact rule as pinned (any other MACD/CCI periods, thresholds, strictness, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; MACD periods are TA-Lib library defaults (12/26/9) and the CCI period is the TA-Lib default (14), disclosed, never overridden in the file:

```text
macd[t], signal[t] = TA-Lib MACD(close, 12, 26, 9)  // defaults — no file override; hist leg discarded
cci[t]             = TA-Lib CCI(high, low, close, 14) // default — no file override
entry    = crossed_above(macd, signal)[t] AND (cci[t] <= -50.0)  // enter_long = 1, one-bar edge
exit_sig = crossed_below(macd, signal)[t] AND (cci[t] >= 100.0)  // exit_long = 1, one-bar edge
risk     = ROI ladder {"0": 0.05, "20": 0.04, "30": 0.03, "60": 0.01} (fraction, by position age in minutes);
           fixed stop at -30% (stoploss -0.3)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on a bar printing the cross-up edge plus the oversold-CCI state, `direction` long-only; `exit_long=1` on a bar printing the cross-down edge plus the overbought-CCI state. Each print is a one-bar edge, not a persistent state — a book already positioned treats non-exit bars (including further entry edges) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the cross edges are strict on the decision bar (`macd > signal` for entry, `macd < signal` for exit) with inclusive previous-bar equality (`prev macd <= prev signal` / `prev macd >= prev signal` inside the standard edge); the CCI comparisons are inclusive (`<= -50.0`, `>= 100.0`) — a bar with `macd == signal` fires neither leg; a bar with `cci == -50.0` fires the entry CCI leg; a bar with `cci == 100.0` fires the exit CCI leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `macd[t] > signal[t]` while any signal-exit bar has `macd[t] < signal[t]` — and additionally any entry bar has `cci[t] <= -50` while any signal-exit bar has `cci[t] >= 100`. Both pairings are mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the conjunct signal exit, the four-rung ROI ladder, and the −30% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry edges as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying conjunct-cross bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (MACD triple smoothing plus CCI mean-deviation, fixed non-negative offsets, plus the standard one-bar edge lookback — no forward reference) with no `shift` call in the file body because the single lookback lives inside the standard `crossed_*` edge under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` only (MACD on `close`; CCI on `high`/`low`/`close`). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the one-bar edge lookback); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 five-minute bars held flat. Covers the TA-Lib MACD seed (26-bar slow EMA plus 9-bar signal smoothing ≈ 35 bars) and the 14-bar CCI seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict/inclusive NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the conjunct signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, and BinHV27 records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the conjunct-cross edge opens the full unit on a flat book; the conjunct signal exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying conjunct-cross bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (78 lines: the default-period MACD and CCI calls, the two `crossed_*` conjunct edges, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `MACDStrategy_crossed(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the cross edges are strict on the decision bar while admitting previous-bar equality; the CCI legs are inclusive (`<=`/`>=`) — a bar sitting exactly on the signal line fires nothing on either side; a bar sitting exactly on −50.0 (100.0) satisfies the entry (exit) CCI leg. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `Dict`, `List`, and `reduce` are imported and never called anywhere in the 78 lines — display/plumbing leftovers with no gate effect, never repaired into a signal. Zero hyperopt tokens, zero `*Parameter` spaces, zero fitted values anywhere in this artifact.
4. Dead-histogram fence: `macdhist` is computed into the frame and read by no order line — the histogram plays no gating role, never repaired into a third leg.
5. Prose-vs-code fence: the docstring's `CCI < -50` / `CCI > 100` (strict) is prose — the coded legs require `cci <= -50.0` / `cci >= 100.0` (inclusive), so an exactly-−50.0 (100.0) bar fires the entry (exit) CCI leg. Coded legs govern; prose never narrows or widens them.
6. Wide-stop fence: the −30% stop is ~6× the opening `0.05` ROI rung — by construction the stop is a disaster backstop that almost never binds before an ROI rung or the conjunct signal exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
7. Cousin records fenced as different constructions (none trades a MACD-signal-cross edge conjunct with an asymmetric CCI threshold pair, long-flat, with this ROI ladder): the admitted `freqtrade-macd-cci-dip-state` pool-mate trades the SIBLING file's persistent MACD-polarity-plus-CCI state (every qualifying bar, never a one-bar edge — this record's edge-vs-state swap changes every trade event); the admitted `macd-signal-cross-reversal` pool-mate trades a naked FMZ 12/26/9 two-sided cross with no CCI leg, no ROI, no stop, always-in-market (no conjunction, no flat state); the admitted `forven-macd-cross-adx-regime` pool-mate trades a 5/13/3 MACD cross gated by ADX14 ≥ 20 plus an EMA200 regime leg with an unconditional cross-down exit (different periods, different gates, ungated exit); the admitted `freqtrade-asdts-rockwell` pool-mate trades a dual-polarity MACD state (zero-line AND signal-line, state not edge) with a signal-line-only exit and no oscillator leg; the admitted `freqtrade-awesome-macd` pool-mate trades an AO cross gated by MACD polarity (edge on a different oscillator, gate not conjunction). Not a threshold re-tuning of any of them: moving any MACD/CCI period, dropping either conjunction leg, converting either edge to a persistent state, flipping any strictness, or changing any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `MACDStrategy.py`, `ADXMomentum.py`, `AdxSmas.py`, `ASDTSRockwellTrading.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, `EMASkipPump.py`, `CMCWinner.py`, and `ClucMay72018.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the TA-Lib default-period readings (MACD 12/26/9, CCI 14 — library defaults, never file literals), the standard `crossed_*` one-bar edge semantics, and house sizing/costs — all predeclared above. The `5m` frame, the conjunct-cross entry edge with all its literals and strictness, the conjunct exit edge, the four-rung ROI ladder with the −30% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: MACD(12,26,9) / CCI(14) / conjunct edges / `-50.0`+`100.0` thresholds with pinned strictness / one-bar-edge legs / conjunct signal exit / four-rung ROI ladder / −30% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — CCI-gate relevance: dropping the CCI legs (naked MACD-signal-cross edge, same conjunct-exit MACD leg only, same risk) must not improve net expectancy; fail ⇒ the oversold-washout veto adds nothing over rotation timing.
- F2 — Rotation-timing relevance: dropping the cross edges (pure CCI-threshold state: long while `cci <= -50`, exit while `cci >= 100`, same risk) must not improve net expectancy; fail ⇒ the rotation edge adds nothing over the oscillator alone.
- F3 — Risk-ladder relevance: removing the ROI ladder/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the four-rung ladder plus −30% backstop adds nothing over the bare edge machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, BinHV27 `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose MACD never prints the conjunct exit edge is held until an ROI rung or the −30% stop; a market that oscillates with hot CCI but no death-cross prints repeated hold-no-ops with no flat state to rest in, while a market that rolls MACD without hot CCI likewise holds (conjunct-exit profile, disclosed). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (EMA seeding, default-period handling, CCI mean-deviation arithmetic) and the standard `crossed_*` one-bar edge live in libraries outside the pinned file — pinned by call with default periods 12/26/9 and 14, not re-derived; exact reproduction inherits those libraries' seeding alongside the 40-bar floor.
- The `Dict`/`List`/`reduce` imports and the `macdhist` column are dead — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/MACDStrategy_crossed.py
- https://github.com/freqtrade/freqtrade-strategies
