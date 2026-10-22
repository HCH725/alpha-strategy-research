---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade TechnicalExample CMF(21) sign-state long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/TechnicalExampleStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade TechnicalExample CMF(21) sign-state long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, and `freqtrade-macd-cross-cci-edge` records — this is only its eleventh record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/TechnicalExampleStrategy.py`.
- GitHub blob SHA at the pinned commit: `d0cafe787b0c03e4423bfb4dbb287d36f55e3c41`, size 1069 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 1069 bytes, 41 lines, SHA-256 `0a3d94c8ef857284c9bc37d592af329b1a831f9c504fb2d73b63db00d303db50`, identical to the GitHub blob (`git hash-object` reproduces `d0cafe78…f55e3c41`) — the entire file was retrieved and inspected.
- Registration: the file defines class `TechnicalExampleStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/CCIStrategy.py` (dual-CCIdip plus resampled-trend insurance, `1m`, open no PR — different legs, different frame), `berlinguyinca/Low_BB.py` (sub-lower-band dip with an empty exit column, `1m`), `berlinguyinca/MultiRSI.py` (resampled short/long RSI merge), `berlinguyinca/Scalp.py` (EMA-rail plus fast-stoch cross with 60-parallel-trade guidance, `1m`), `berlinguyinca/SmoothOperator.py` (header-disclaimed smoothing playground, `DO NOT USE`), and every other admitted berlinguyinca pin are different pins with different gates — this record pins ONLY the TechnicalExampleStrategy file's literals below, and no reviewer repair may substitute a sibling constant or a sibling indicator.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.05`; indicator `dataframe['cmf'] = cmf(dataframe, 21)` (single indicator call, explicit period 21 — no default-period reading anywhere); entry `(dataframe['cmf'] < 0)` (`enter_long = 1`); exit `(dataframe['cmf'] > 0)` (`exit_long = 1`); exit-column comment `different strategy used for sell points, due to be able to duplicate it to 100%` (prose leftover — the coded `cmf > 0` leg governs, never the comment). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file call pinned (resolved by name, standard vendored library): `cmf` from `technical.indicators` (the `freqtrade/technical` indicator package the collection builds on), invoked with explicit period `21`. Its implementation is the standard Chaikin-money-flow construction (verified against `freqtrade/technical@5852e5407588ad04d539f5d5071c60d9dc69b95a`, `technical/indicators/volume_indicators.py`, where `cmf = chaikin_money_flow`): `mfm = ((close - low) - (high - close)) / (high - low)` per bar, `mfv = mfm * volume`, `cmf = rolling(21).sum(mfv) / rolling(21).sum(volume)` — trailing causal windows only, disclosed, never redefined. No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 41 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume token in the file body — bar volume enters the rule only inside the vendored CMF arithmetic, disclosed); 0 `shift` (no lag call anywhere — the rule reads the decision bar's own CMF print, a persistent state, never an edge); 0 `hyperopt` / 0 `Parameter`; 1 `stoploss` (the `-0.05` attribute) and 1 `minimal_roi` (the single-rung `{"0": 0.01}` ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `open` (no open-column read — the signal path reads `high`/`low`/`close` plus bar `volume` inside CMF only); 0 `crossed` (no edge call — both legs are persistent states); 0 `ta.` / 0 `qtpylib` / 0 `scipy` (no library indicator call in the file body besides the single `cmf` import-and-call). The 3 `dict` tokens are the three `metadata: dict` annotations (plumbing, no gate effect); `Dict`, `List`, and `reduce` are not imported at all — there are no dead imports to fence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the CMF(21) sub-zero entry state, the CMF(21) super-zero exit state, the single-rung 1% ROI target, the −5% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `technicalexample` (case-insensitive) returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a CMF sign-state rule. CMF cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure while 21-bar Chaikin money flow prints below zero (volume accumulating near the lows — distribution), exit while it prints above zero (volume accumulating near the highs). A single-rung 1% ROI target (`0.01` from open) and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Distribution-state fade machine, long-only. The CMF leg signs each bar's volume by where the close sits inside the high–low range and normalizes the 21-bar signed flow by total volume — a bounded [−1, +1] gauge of accumulation versus distribution. The book is long whenever the gauge reads negative and flat whenever it reads positive: unlike edge systems (one-bar crosses) there is no entry-timing trigger beyond the sign itself — a market that stays distributed stays long, and a market that stays accumulated stays flat. The 1% ROI rung harvests micro-reversions quickly while the −5% stop (5× the rung) stands as a disaster backstop that almost never binds first in ordinary tape. The failure mode is plain: a gauge that oscillates around zero whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown), while a deeply negative gauge that keeps bleeding holds the unit all the way to the stop — no time exit exists.

## Signal

Exact rule as pinned (any other CMF period, threshold, state-vs-edge pairing, risk rung, fill, frame, or book is a different, unpinned rule). The CMF period is an explicit file literal (`21`), never a library default:

```text
mfm[t]  = ((close - low) - (high - close)) / (high - low)   // per bar, causal
mfv[t]  = mfm[t] * volume[t]
cmf[t]  = sum(mfv[t-20..t]) / sum(volume[t-20..t])          // rolling 21-bar, causal
entry   = (cmf[t] < 0)    // enter_long = 1, persistent state, strict
exit_sig = (cmf[t] > 0)   // exit_long = 1, persistent state, strict
risk    = ROI {"0": 0.01} (fraction of entry-price distance, by position age in minutes);
          fixed stop at -5% (stoploss -0.05, same basis)
floor   = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on every bar printing a negative CMF, `direction` long-only; `exit_long=1` on every bar printing a positive CMF. Each print is a persistent state, not a one-bar edge — a book already positioned treats further entry-state bars as hold-no-ops under the position pin below, and a flat book treats exit-state bars as no-ops.
- Exact boundaries (pinned semantics): both comparisons are strict (`< 0`, `> 0`) — a bar with `cmf == 0.0` fires neither leg; degenerate zero-range bars (`high == low`) print `0/0 = NaN` and zero-volume 21-bar windows print `NaN`, and every NaN comparison is false, so degenerate bars deterministically fire neither leg (coded library behaviour, disclosed, never repaired). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `cmf[t] < 0` while any signal-exit bar has `cmf[t] > 0` — mutually exclusive on every bar, degenerate, zero, or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill); any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the super-zero signal state, the single-rung 1% ROI target, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rungs and stop are fractions of entry-price distance (close-to-close price return), evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. No trailing, no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-state bars as no-ops; re-entry re-arms on any qualifying negative-CMF bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` (per-bar money-flow multiplier plus two rolling 21-bar sums with fixed non-negative offsets — no forward reference) under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` (money-flow-multiplier construction) plus bar `volume` (read twice inside the rule — once to sign each bar's flow, once to normalize the 21-bar sum; the rule is doubly volume-weighted, disclosed; no standalone volume threshold leg ships). No `open` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 five-minute bars held flat. Covers the 21-bar rolling CMF seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, BinHV27, and MACDStrategy-crossed siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the signal-exit state, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, BinHV27, and MACDStrategy-crossed records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the negative-CMF state opens the full unit on a flat book; the positive-CMF state, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next negative-CMF bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (41 lines: the single `cmf(dataframe, 21)` call, the two strict sign-state legs, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `TechnicalExampleStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-zero rule fenced: both legs are strict — a bar printing exactly `cmf == 0.0` fires neither leg. Strictness preserved throughout — disclosed, not smoothed.
3. Degenerate-bar fence: zero-range bars (`high == low`) and zero-volume 21-bar windows print NaN through the vendored rolling division, and every NaN strict comparison is false — degenerate bars deterministically print neither leg. Coded library behaviour, disclosed, not repaired into a signal.
4. Prose-vs-code fence: the exit column's `different strategy used for sell points, due to be able to duplicate it to 100%` comment is prose — the coded exit leg is `(dataframe['cmf'] > 0)`, so the comment neither narrows nor widens any gate. Coded legs govern; prose never does.
5. Wide-stop fence: the −5% stop is 5× the opening `0.01` ROI rung — by construction the stop is a disaster backstop that almost never binds before the ROI rung or the sign-state exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
6. No-edge fence: the file contains zero `crossed_*` calls and zero `shift` calls — both legs are persistent states evaluated on the decision bar's own CMF print. Converting either leg to a cross-edge (or vice versa) would be a different, unpinned rule with different trade events.
7. Cousin records fenced as different constructions (none trades a 21-bar CMF zero-line sign-state pair, long-flat, with a 1% ROI rung plus a −5% stop): the admitted `forven-chaikin-mf-threshold-cross` pool-mate trades ±0.05 threshold CROSS edges on a 20-bar CMF (one-bar edge events with a hysteresis dead-band, `1h`, no stop, no ROI, Forven source — a market that drifts from −0.01 to +0.01 fires an exit here but nothing there; a market pinned at +0.03 fires an exit-state here but nothing there); the admitted `cmf-velocity-zero-cross-ema200-bracket` pool-mate trades a 7-bar-averaged CMF velocity zero-cross behind an EMA-200 gate with a 2:1 ATR stop/limit bracket (two-sided, `1d`, FMZ source); the admitted `chaikin-oscillator-ad-zero-cross` pool-mate trades a different indicator (3/10-period EMA of the A/D line, momentum-divergence exits, two-sided). Not a threshold re-tuning of any of them: moving the CMF period, adding any threshold band, converting either state to an edge, flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `CCIStrategy.py` (which carries its own inline `chaikin_mf` with period 20 inside a dual-CCI-plus-resample construction), `Low_BB.py`, `MultiRSI.py`, `Scalp.py`, `SmoothOperator.py`, `MACDStrategy.py`, `MACDStrategy_crossed.py`, and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the vendored CMF rolling-sum implementation (pinned by call with explicit period 21, never re-derived), and house sizing/costs with safety tranches deactivated — all predeclared above. The `5m` frame, the CMF(21) sign-state entry leg with all its literals and strictness, the CMF(21) sign-state exit leg, the single-rung ROI target with the −5% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CMF(21) / zero-line sign states with pinned strictness / persistent-state legs / positive-state signal exit / single-rung 1% ROI / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Sign-filter relevance: entering on the first post-warmup bar and holding time-in-market (same ROI/stop exits, no CMF legs) must not improve net expectancy; fail ⇒ the sign filter adds nothing over blind exposure.
- F2 — Zero-threshold relevance: replacing the zero line with a ±0.05 hysteresis band (enter below −0.05, exit above +0.05, same risk) must not improve net expectancy; fail ⇒ the coded zero-line states add nothing over their banded twin.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 1% rung plus −5% backstop adds nothing over the bare state machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose CMF never prints a positive bar is held until the ROI rung or the −5% stop; a market whose CMF oscillates around zero whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown to damp them — disclosed as the principal friction). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- Vendored indicator internals (rolling-sum seeding, NaN propagation through the money-flow division) live in the `technical` library outside the pinned file — pinned by call with explicit period 21, not re-derived; exact reproduction inherits that library's seeding alongside the 40-bar floor.
- The exit-column prose comment is dead — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/TechnicalExampleStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
