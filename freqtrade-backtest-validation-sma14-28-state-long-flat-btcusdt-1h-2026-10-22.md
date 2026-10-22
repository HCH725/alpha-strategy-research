---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade backtest-validation SMA(14/28) cross-state long-flat on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/Freqtrade_backtest_validation_freqtrade1.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade backtest-validation SMA(14/28) cross-state long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` plus a fresh shallow clone resolving HEAD to the same SHA during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/Freqtrade_backtest_validation_freqtrade1.py`.
- GitHub blob SHA at the pinned commit: `74a1b2a1a37810aac45b2964d5a14335d0cf4650`, 1646 bytes, 50 lines.
- Byte-identity check: the file in the fresh clone at the pinned commit is 50 lines, 1646 bytes, SHA-256 `758d3730e57c7337f988ac68420d8140a0bff72d99fa9182017cd1f8b160c869`, identical to the GitHub blob (`git hash-object` reproduces `74a1b2a1…f4650`; working tree clean versus HEAD) — the entire file was retrieved and inspected.
- Registration: the file defines class `Freqtrade_backtest_validation_freqtrade1(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/Simple.py` (already admitted from a sibling fork as `freqtrade-simple-macd-bb-rsi-momentum` — different legs, different gates, fenced in Negative evidence 7), `berlinguyinca/AverageStrategy.py` (open no PASS — closed NOT_LOSSLESS twice, different legs, different frame), `berlinguyinca/TechnicalExampleStrategy.py` (admitted as `freqtrade-technical-cmf-sign-state` — CMF sign-state, different indicator), and every other admitted berlinguyinca pin are different pins with different gates — this record pins ONLY the validation file's literals below, and no reviewer repair may substitute a sibling constant or a sibling indicator.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '1h'`; `minimal_roi = { "40": 2.0, "30": 2.01, "20": 2.02, "0": 2.04 }` (four-rung descending ladder, 200–204%); `stoploss = -0.90`; indicators `dataframe['fastMA'] = ta.SMA(dataframe, timeperiod=14)` and `dataframe['slowMA'] = ta.SMA(dataframe, timeperiod=28)` (single-input SMAs over the talib.abstract default close series — both periods explicit file literals, never library defaults); entry `(dataframe['fastMA'] > dataframe['slowMA'])` (`enter_long = 1`); exit `(dataframe['fastMA'] < dataframe['slowMA'])` (`exit_long = 1`); header comment `This script is 1 of a pair the other being freqtrade_backtest_validation_tradingview1` / `The purpose is to test Freqtrade backtest provides like results to a known industry platform` (purpose prose — the coded legs govern, never the comment; the TradingView twin is an unpinned external reference, never a data dependency). `INTERFACE_VERSION: int = 3` (plumbing). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no `order_types` / `order_time_in_force` ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- No out-of-file indicator call exists: both legs are plain `talib.abstract` SMAs computed inline in the file body with explicit periods — there is no vendored-library construction to pin beyond talib's deterministic SMA itself. No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 50 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume token in the file body — the rule is close-only); 0 `open` (no open-column read anywhere); 0 `shift` (no lag call anywhere — the rule reads the decision bar's own SMA prints, a persistent state, never an edge); 0 `hyperopt` / 0 `Parameter`; 1 `stoploss` (the `-0.90` attribute) and 1 `minimal_roi` (the four-rung ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `crossed` (no edge call — both legs are persistent states); 0 `scipy`; 2 `ta.` (exactly the two `ta.SMA` calls); 1 `qtpylib` (the single dead import line `import freqtrade.vendor.qtpylib.indicators as qtpylib` — never referenced in the body, fenced, no gate effect). The 2 `Dict`/`List`-family tokens do not exist here — imports are only `IStrategy`, `DataFrame`, `ta`, and the dead `qtpylib` line; there are no other dead imports to fence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the SMA(14)-over-SMA(28) entry state, the mirrored sub-state exit, the four-rung 200–204% ROI ladder, the −90% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `freqtrade_backtest_validation` (case-insensitive) and for `fastMA`/`slowMA` rule tokens returns zero strategy records citing this source file — no record in the pool pins this file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an SMA(14/28) cross-state rule. SMA cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure while the 14-bar simple average of closes prints above the 28-bar simple average (near-term trend above longer-term trend), exit while it prints below. A four-rung 200–204% ROI ladder (`2.04` at open decaying to `2.0` after 40 minutes) and a fixed −90% stoploss backstop every position — both effectively non-binding in ordinary tape, preserved verbatim (see Signal). The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Slow-trend-state machine, long-only, close-only. The rule signs each bar by the relative position of two trailing simple averages — a bounded, fully causal trend gauge with no volume, volatility, or momentum input. The book is long whenever the fast average leads and flat whenever it lags: unlike edge systems (one-bar crosses) there is no entry-timing trigger beyond the state itself — a market that stays in an uptrend stays long, and a market that stays in a downtrend stays flat. Because the 200–204% ROI ladder and the −90% stop almost never bind first in ordinary tape, effective exits are the mirrored signal state: the strategy is, in practice, a pure two-state trend holder with a disaster backstop. The failure mode is plain: averages that hover in near-equality whipsaw the book across consecutive bars (exit-then-re-enter round trips with no cooldown), while a fast average that stays above a bleeding slow average holds the unit through the whole drawdown — no time exit exists.

## Signal

Exact rule as pinned (any other SMA period, threshold, state-vs-edge pairing, risk rung, fill, frame, or book is a different, unpinned rule). Both SMA periods are explicit file literals (`14`, `28`), never library defaults:

```text
fastMA[t] = SMA(close[t-13..t], 14)     // trailing 14-bar simple average, causal
slowMA[t] = SMA(close[t-27..t], 28)     // trailing 28-bar simple average, causal
entry    = (fastMA[t] > slowMA[t])      // enter_long = 1, persistent state, strict
exit_sig = (fastMA[t] < slowMA[t])      // exit_long = 1, persistent state, strict
risk     = ROI {"0": 2.04, "20": 2.02, "30": 2.01, "40": 2.0}
           (fractions of entry-price distance, by position age in minutes);
           fixed stop at -90% (stoploss -0.90, same basis)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on every bar printing fastMA above slowMA, `direction` long-only; `exit_long=1` on every bar printing fastMA below slowMA. Each print is a persistent state, not a one-bar edge — a book already positioned treats further entry-state bars as hold-no-ops under the position pin below, and a flat book treats exit-state bars as no-ops.
- Exact boundaries (pinned semantics): both comparisons are strict (`>`, `<`) — a bar with `fastMA == slowMA` fires neither leg; pre-seed bars print `NaN` and every NaN comparison is false, so unseeded bars deterministically fire neither leg (coded library behaviour, disclosed, never repaired). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `fastMA[t] > slowMA[t]` while any signal-exit bar has `fastMA[t] < slowMA[t]` — mutually exclusive on every bar, seeded, unseeded, or exactly equal, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill); any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirrored sub-state signal exit, the four-rung 200–204% ROI ladder, and the −90% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rungs and stop are fractions of entry-price distance (close-to-close price return) by position age in minutes, evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. In ordinary tape the ladder and the −90% stop are effectively non-binding (disclosed consequence of the coded magnitudes, never a repair — the magnitudes are preserved verbatim). No trailing, no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-state bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-state bars as no-ops; re-entry re-arms on any qualifying fastMA-above-slowMA bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` values (two trailing simple averages with fixed non-negative offsets — no forward reference) under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. No volume/open/high/low read, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (both SMA inputs; no `open`/`high`/`low`/`volume` read anywhere in the gating path). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 one-hour bars held flat. Covers the 28-bar slow-SMA seed with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, and ADXMomentum 1h siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirrored signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the BbandRsi, AwesomeMacd, and ADXMomentum records plus the Forven 1h family — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the fastMA-above-slowMA state opens the full unit on a flat book; the mirrored sub-state, the ROI ladder, or the stop closes it in full; re-entry after an exit needs only the next qualifying bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (50 lines: the two explicit-period `ta.SMA` calls, the two strict mirrored state legs, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `Freqtrade_backtest_validation_freqtrade1(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-equality rule fenced: both legs are strict — a bar printing exactly `fastMA == slowMA` fires neither leg. Strictness preserved throughout — disclosed, not smoothed.
3. Purpose-prose fence: the header's backtest-validation purpose and its reference to the `freqtrade_backtest_validation_tradingview1` twin are prose — the coded legs are the complete rule, so the comment neither narrows nor widens any gate, and the unpinned twin contributes no input. Coded legs govern; prose never does.
4. Non-binding-risk fence: the 200–204% ROI ladder and the −90% stop are coded magnitudes preserved verbatim — by construction they are disaster-only rungs that almost never bind before the mirrored signal exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
5. No-edge fence: the file contains zero `crossed_*` calls and zero `shift` calls — both legs are persistent states evaluated on the decision bar's own SMA prints. Converting either leg to a cross-edge (or vice versa) would be a different, unpinned rule with different trade events.
6. Dead-import fence: the single `qtpylib` token is the import line only — the body never references it. It contributes no input, no transform, and no gate; disclosed, never silently dropped from the census.
7. Cousin records fenced as different constructions (none trades a plain SMA(14)-over-SMA(28) mirrored state pair, long-flat, `1h`, close-only, with a 200–204% ladder plus a −90% stop): the admitted `ema-20-50-cross-btcusdt-1h` pool-mate trades EMA(20/50) from a different (Forven Pine) source with different periods and a different averaging kernel; the admitted `forven-ema-cross-adx-regime` pool-mate trades an EMA cross behind an ADX regime gate (gated edges, Forven source); the open-PR `AdxSmas` (#331) pool-candidate trades an SMA(3/6) cross with an ADX gate (different periods, gated, different file); the admitted `eterna-sma-50-200-crossover` pool-mate trades SMA(50/200) two-sided on `4h` (different periods, two-sided, different frame and source); the admitted `actionzone-dual-ema-zone-transition` pool-mate trades a dual-EMA zone transition two-sided on `1d`; the admitted `dpo-ema-crossover-trend` pool-mate trades a DPO-vs-EMA construction on `1d`. Not a threshold re-tuning of any of them: moving either SMA period, converting either state to an edge, adding any gate, flipping any strictness, or changing the ROI ladder, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `Simple.py` (admitted from a sibling fork as `freqtrade-simple-macd-bb-rsi-momentum` — MACD/BB/RSI conjunction, different legs), `AverageStrategy.py` (EMA 8/21 cross, `4h`), `TechnicalExampleStrategy.py` (admitted as `freqtrade-technical-cmf-sign-state` — CMF(21) sign states), and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the talib SMA default-close input (explicit periods, never re-derived), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1h` frame, the SMA(14)-over-SMA(28) entry state with all its literals and strictness, the mirrored exit state, the four-rung ROI ladder with the −90% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA(14)/SMA(28) / strict mirrored states / persistent-state legs / mirrored signal exit / four-rung 200–204% ROI ladder / −90% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — State relevance: entering on the first post-warmup bar and holding time-in-market (same ROI/stop exits, no SMA legs) must not improve net expectancy; fail ⇒ the cross-state filter adds nothing over blind exposure.
- F2 — Period relevance: replacing the 14/28 pair with a 20/50 SMA pair (same state construction, same risk) must not improve net expectancy; fail ⇒ the coded periods add nothing over their cousin pair.
- F3 — Risk-leg relevance: removing the ROI ladder/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the ladder plus backstop adds nothing over the bare state machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. The rule reads only `close`, a native Binance kline field on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent (BbandRsi, AwesomeMacd, ADXMomentum `1h`, plus the Forven 1h family) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose fastMA never prints below slowMA is held until the ROI ladder or the −90% stop; a market whose averages hover in near-equality whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown to damp them — disclosed as the principal friction). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- The ROI ladder and stop are effectively non-binding coded magnitudes — exact reproduction inherits them verbatim; any downstream experiment that tightens them is a different, separately declared derivative.
- The exit-column purpose prose and the unpinned TradingView twin reference are dead — nothing further to fence.
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
