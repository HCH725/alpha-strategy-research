---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AverageStrategy EMA8/21 cross volume-guarded long-flat on BTCUSDT 4h bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AverageStrategy EMA8/21 cross volume-guarded long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-binhv27` records — this is only its eleventh record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/AverageStrategy.py`.
- GitHub blob SHA at the pinned commit: `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, size 2630 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2630 bytes, 79 lines, SHA-256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`, identical to the GitHub blob (`git hash-object` reproduces `dbb0ba65…08d493`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AverageStrategy(IStrategy)` (the only class in the file; author note `Gert Wohlgemuth`; idea line `buys and sells on crossovers`). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/MACDStrategy.py` (persistent MACD-polarity-plus-CCI state — separately admitted), `berlinguyinca/MACDStrategy_crossed.py` (MACD-cross-plus-CCI one-bar edge — separately admitted), `berlinguyinca/ADXMomentum.py` (ADX/DI/MOM four-conjunct state — separately admitted), `berlinguyinca/ASDTSRockwellTrading.py` (dual-polarity MACD state — separately admitted), `berlinguyinca/AdxSmas.py` (SMA3/6 cross gated by ADX polarity, open PR #331), `berlinguyinca/AwesomeMacd.py` (AO-cross gated by MACD polarity — separately admitted), `berlinguyinca/BbandRsi.py` (RSI dip with BB penetration — separately admitted), `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards — separately admitted), `berlinguyinca/EMASkipPump.py` (EMA-stack dip with volume veto — separately admitted), `berlinguyinca/CMCWinner.py` (CCI+MFI+CMO triple-oversold state — separately admitted), `berlinguyinca/ClucMay72018.py` (BB-discount EMA-gated state, open PR #350), and `berlinguyinca/BinHV27.py` (RSI-ADX-DI regime state — separately admitted) are different pins with different gates — this record pins ONLY the AverageStrategy file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): idea `buys and sells on crossovers`; `minimal_roi = { "0": 0.5 }`; `stoploss = -0.2`; `timeframe = '4h'`; `buy_range_short = IntParameter(5, 20, default=8)`; `buy_range_long = IntParameter(20, 120, default=21)`; indicators `dataframe[f'ema{val}'] = ta.EMA(dataframe, timeperiod=val)` over the union of both parameter ranges (talib.abstract default price is close — disclosed default, never a file literal); entry `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_short.value}'], dataframe[f'ema{self.buy_range_long.value}']) & (dataframe['volume'] > 0)` (`enter_long = 1`); exit `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_long.value}'], dataframe[f'ema{self.buy_range_short.value}']) & (dataframe['volume'] > 0)` (`exit_long = 1`). No `buy_params`/`sell_params` dict ships anywhere — the two Parameter defaults (8, 21) are the effective values, disclosed, never overridden. No `trailing`, no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `process_only_new_candles`, no `custom_stoploss`, no `protection`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.EMA` (TA-Lib exponential moving average on close with the effective periods 8 and 21); `qtpylib.crossed_above` (standard Freqtrade one-bar edge: `(s1 > s2) & (s1.shift(1) <= s2.shift(1))` and its mirror — causal two-bar comparison, disclosed, never redefined). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no informative-pair call in the file.
- Full-file token census (verified over the 79 lines this cycle): 0 short legs (the 4 case-insensitive `short` tokens are all the `buy_range_short` parameter identifier — declaration, range union, and the two f-string reads — no short order leg, no short identifier anywhere else); 2 `volume` (exactly the two `volume > 0` guards, one per leg); 0 `shift` (no lag call in the file body — the single one-bar lookback lives inside the standard `crossed_above` edge, disclosed above); 0 `hyperopt` / 0 shipped `buy_params` / 0 shipped `sell_params`; 3 `stoploss` (two comment lines plus the `-0.2` attribute) and 2 `minimal_roi` (one comment line plus the single-rung ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 30-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond the ROI rung and the stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security` / 0 `custom_stoploss` / 0 `protection`. `reduce` is imported and never called — a dead import, fenced as plumbing with no gate effect. The 3 `cross` tokens are the docstring `crossovers` word and the two `crossed_above` edge calls — nothing further.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `4h` frame, the EMA8/EMA21 mirror-cross edges with the `volume > 0` guards, the single-rung 50% ROI, the −20% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 30-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `averagestrategy` (case-insensitive) and `buy_range_short` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian ratio) trades a naked EMA8/21 mirror-cross edge pair. Plain-EMA-cross cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and idea line print: buy the single bar where EMA8 crosses up through EMA21 with positive bar volume, sell the single bar where EMA21 crosses back up through EMA8 (the mirror cross-down) with positive bar volume. A single 50% ROI rung and a fixed −20% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Naked two-average trend machine, long-only, edge-triggered. The entry edge fires only on the rotation bar itself (fast average reclaiming the slow average), not on every bar the fast average spends on top — so a book already positioned treats all continuation bars as hold-no-ops until the mirror cross, the 50% rung, or the stop. The 50% opening rung is ~2.5× the −20% stop distance: by construction the ROI leg is a moonshot catcher that almost never binds before the mirror-cross signal exit or the stop in ordinary tape, making the effective exit profile signal-first with a disaster backstop. The `volume > 0` guards are near-tautological on a 4h perpetual bar (they suppress both legs only on a literally tradeless bar) — coded fact, disclosed, never repaired into a volume filter with a real threshold. Unlike persistent-state records (trade every bar the condition holds), each leg can fire at most on its crossing bar.

## Signal

Exact rule as pinned (any other EMA periods, guard, strictness, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; EMA periods are the shipped Parameter defaults (8, 21), disclosed, never overridden anywhere:

```text
ema8[t]  = TA-Lib EMA(close, 8)   // effective default — no override ships in the file
ema21[t] = TA-Lib EMA(close, 21)  // effective default — no override ships in the file
entry    = crossed_above(ema8, ema21)[t] AND (volume[t] > 0)  // enter_long = 1, one-bar edge
exit_sig = crossed_above(ema21, ema8)[t] AND (volume[t] > 0)  // exit_long = 1, one-bar edge (mirror cross-down)
risk     = ROI ladder {"0": 0.5} (fraction, by position age); fixed stop at -20% (stoploss -0.2)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on a bar printing the cross-up edge plus positive volume, `direction` long-only; `exit_long=1` on a bar printing the mirror cross-down edge plus positive volume. Each print is a one-bar edge, not a persistent state — a book already positioned treats non-exit bars (including further cross-up prints, impossible without an intervening cross-down in exact arithmetic, and in any case) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the cross edges are strict on the decision bar (`ema8 > ema21` for entry, `ema21 > ema8` for exit) with inclusive previous-bar equality (`prev ema8 <= prev ema21` / `prev ema21 >= prev ema8` inside the standard edge); the volume guards are strict (`> 0`) — a bar with `ema8 == ema21` fires neither leg; a bar with exactly zero volume fires neither leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `ema8[t] > ema21[t]` while any signal-exit bar has `ema21[t] > ema8[t]` — mutually exclusive on every bar, degenerate or otherwise, and the shared `volume > 0` guard cannot reunite them, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirror-cross signal exit, the single 50% ROI rung, and the −20% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry edges as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying mirror-cross bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (EMA fixed offsets) and `volume` (strict positivity) plus the standard one-bar edge lookback — no forward reference — with no `shift` call in the file body because the single lookback lives inside the standard `crossed_above` edge under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt space, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `4h` bars of BTCUSDT: `close` (both EMAs) and `volume` (positivity guards only) — no `open`/`high`/`low` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the one-bar edge lookback); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 30 four-hour bars held flat. Covers the TA-Lib EMA21 seed (20-bar lookback) plus the one-bar edge lookback with margin — the first legally possible signal bar is index 21, and the record floor additionally holds bars 0–29 flat. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed-edge, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirror-cross signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `4h` is an already-admitted interval on `main` via the MultiMa TEMA-stack and HLHB records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the cross-up edge opens the full unit on a flat book; the mirror-cross signal exit, the 50% rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying cross-up bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (79 lines: the two Parameter declarations with effective defaults 8/21, the EMA materialization loop, the two `crossed_above` mirror edges with `volume > 0` guards, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `AverageStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 30-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed. The first legally possible signal bar (index 21) is fixed by the EMA21 lookback plus the edge lookback — the reviewer is never asked to choose a seeding.
2. Exact-touch rule fenced: the cross edges are strict on the decision bar while admitting previous-bar equality; the volume guards are strict (`> 0`) — a bar sitting exactly on the EMA line fires nothing on either side; a literally tradeless bar fires nothing on either side. Strictness preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `reduce` is imported and never called anywhere in the 79 lines — a display/plumbing leftover with no gate effect, never repaired into a signal. Zero hyperopt tokens, zero shipped `buy_params`/`sell_params` spaces, zero fitted values anywhere in this artifact (the effective 8/21 are round Parameter defaults, never hyperopt-paste results).
4. Dead-column fence: the indicator loop materializes a superset of EMA columns (the union of the short range 5–20 and the long range 20–120) but the order path reads ONLY `ema8` and `ema21` — every other column is dead, never repaired into an extra leg or an alternative period.
5. Wide-rung fence: the 50% ROI rung is 2.5× the −20% stop distance — by construction the rung is a moonshot catcher that almost never binds before the mirror-cross signal exit or the stop in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
6. Near-tautology guard fence: `volume > 0` on a 4h perpetual bar suppresses both legs only on a literally tradeless bar — coded fact, disclosed, never upgraded into a real volume filter with an invented threshold.
7. Cousin records fenced as different constructions (none trades a naked EMA8/21 one-bar mirror-cross edge pair with strict volume-positivity guards, long-flat, with this risk pair): the admitted `ema-20-50-cross` pool-mate trades a Forven Pine persistent cross-STATE (long every bar the fast average spends on top, never a one-bar edge — this record's edge-vs-state swap changes every trade event) on different periods (20/50), a different frame (1h), and a different source family; the admitted `freqtrade-strategy001` pool-mate trades a Heikin-Ashi-plus-EMA cross; the admitted `freqtrade-multima-tema-stack` pool-mate trades a triple-TEMA stack trend state; the admitted `dual-ema-engulfing-volume` pool-mate requires an engulfing candle plus a real volume comparison; the admitted `dpo-ema-crossover` pool-mate adds a detrended-price-oscillator leg; the admitted `alma-cross-volume-gate` pool-mate crosses an ALMA (different average construction); open PR #331 `AdxSmas` crosses SMA3/6 under an ADX-polarity gate on 1h; the admitted `freqtrade-universalmacd` pool-mate trades an EMA-ratio dip band (state, not edge); the admitted `freqtrade-asdts-rockwell` and `freqtrade-awesome-macd` pool-mates trade MACD-family constructions. Not a threshold re-tuning of any of them: moving either EMA period, dropping the volume guards, converting either edge to a persistent state, flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `MACDStrategy.py`, `MACDStrategy_crossed.py`, `ADXMomentum.py`, `AdxSmas.py`, `ASDTSRockwellTrading.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, `EMASkipPump.py`, `CMCWinner.py`, `ClucMay72018.py`, and `BinHV27.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 30-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the talib.abstract close-price default, the standard `crossed_above` one-bar edge semantics, and house sizing/costs — all predeclared above. The `4h` frame, the EMA8/EMA21 mirror-cross entry/exit edges with all their literals, guards and strictness, the single 50% ROI rung with the −20% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA(8)/EMA(21) / mirror-cross one-bar edges / strict `volume > 0` guards with pinned strictness / mirror signal exit / single 50% ROI rung / −20% stop / single-unit long-only / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Volume-guard relevance: dropping the `volume > 0` guards (naked EMA8/21 mirror-cross edges, same risk) must not improve net expectancy; fail ⇒ the positivity guards add nothing over the bare cross machine.
- F2 — Edge-vs-state relevance: converting both legs to persistent states (long while `ema8 > ema21` with volume, exit while `ema21 > ema8` with volume, same risk) must not improve net expectancy; fail ⇒ the one-bar-edge rotation timing adds nothing over the persistent trend state.
- F3 — Risk-pair relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 50% rung plus −20% backstop adds nothing over the bare edge machine.

## Crypto portability

BTCUSDT Binance perpetual `4h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. The only volume use is a strict-positivity guard, satisfiable on any venue that prints at least one trade per 4h bar. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `4h` frame rides existing admission precedent (MultiMa TEMA-stack, HLHB `4h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose averages never print the mirror cross is held until the 50% rung or the −20% stop; a market that whipsaws prints alternating full-unit edges with no cooldown — both profiles disclosed, not repaired. There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib EMA internals (seeding arithmetic) and the standard `crossed_above` one-bar edge live in libraries outside the pinned file — pinned by call with effective periods 8 and 21, not re-derived; exact reproduction inherits those libraries' seeding alongside the 30-bar floor.
- The `reduce` import and the unread EMA columns are dead — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
