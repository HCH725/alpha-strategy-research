---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade CMCWinner triple-oscillator state long-flat on BTCUSDT 15m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/CMCWinner.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade CMCWinner triple-oscillator state long-flat on BTCUSDT 15m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, and `freqtrade-adx-momentum` records — this is only its seventh record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/CMCWinner.py`.
- GitHub blob SHA at the pinned commit: `80ce364274f56c9fe70f743dbe0f75fe57b03498`, size 3163 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3163 bytes, 95 lines, SHA-256 `0529996f7e895c3c15ee143f1f0c5ff75d78fd6522856ba0daa55b94437bfc3f`, identical to the GitHub blob (`git hash-object` reproduces `80ce3642…75fe57b03498`) — the entire file was retrieved and inspected.
- Registration: the file defines class `CMCWinner(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/ADXMomentum.py` (ADX/DI/MOM four-conjunct state, `1h`), `berlinguyinca/AdxSmas.py` (SMA3/6 cross gated by ADX polarity, `1h`, open PR #331), `berlinguyinca/AwesomeMacd.py` (AO-cross gated by MACD polarity, `1h`), `berlinguyinca/BbandRsi.py` (RSI dip with BB penetration, `1h`), `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards, `5m`), and `berlinguyinca/EMASkipPump.py` (EMA-stack dip with volume veto, `5m`) are different pins with different gates — this record pins ONLY the CMCWinner file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): class docstring `This is a test strategy to inspire you.`; `minimal_roi = { "40": 0.0, "30": 0.02, "20": 0.03, "0": 0.05 }`; `stoploss = -0.05`; `timeframe = '15m'`; indicators `ta.CCI(dataframe)`, `ta.MFI(dataframe)`, `ta.CMO(dataframe)` (all three called with NO period argument — TA-Lib defaults apply, disclosed below, never overridden anywhere in the file); entry `cci.shift(1) < -100 & mfi.shift(1) < 20 & cmo.shift(1) < -50` (`enter_long = 1`); exit `cci.shift(1) > 100 & mfi.shift(1) > 80 & cmo.shift(1) > 50` (`exit_long = 1`); CCI comment `values Oversold:<-100, Overbought:>100`. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.CCI` (TA-Lib Commodity Channel Index on high/low/close, default period 14 — no override in the file); `ta.MFI` (TA-Lib Money Flow Index on high/low/close/volume, default period 14 — the file's only volume consumer, disclosed in Required data); `ta.CMO` (TA-Lib Chande Momentum Oscillator on close, default period 14). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`CategoricalParameter`/`DecimalParameter` zero hits — the two `hyperopt` tokens are docstring prose only: the must-keep method list and the performance note), no informative-pair call in the file.
- Full-file token census (verified over the 95 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 1 `stoploss` (`-0.05`) and 1 `minimal_roi` (the four-rung ladder above) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 30-bar floor is a predeclared researcher pin, never a file semantic); 2 `hyperopt` (prose only, fenced above); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no explicit volume line — volume enters only inside the TA-Lib MFI call); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic). `qtpylib` and `numpy` are imported and never called — dead imports, fenced as plumbing with no gate effect.

Pre-write dedup (2026-10-20): working-tree filename/content search for `CMCWinner` / `cmcwinner` / `cmc-winner` returns zero strategy records — no record in the pool cites this source file. Indicator search for `CMO(` returns exactly one pool record, the admitted `chande-momentum-80-cross-reversal` (a single-indicator CMO threshold-cross, fenced in Negative evidence 7 — different construction, different scope). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross) trades a CCI+MFI+CMO three-way state conjunction. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: a self-described test strategy that opens long when the prior bar prints a triple-oversold state (CCI under −100 with MFI under 20 and CMO under −50) and exits long on the mirrored triple-overbought state (CCI over +100 with MFI over 80 and CMO over +50). A four-rung ROI ladder (`0.05` from open, `0.03` after 20 min, `0.02` after 30 min, breakeven `0.0` after 40 min) and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Triple-witness capitulation fade, long-only. Each leg watches a different tape dimension — CCI prices the bar's deviation from its own mean, MFI weights that move by volume conviction, CMO signs the close-to-close momentum sum — so entry demands price, participation, and momentum all agree the prior bar was washed out, and exit demands all three agree the book is overheated. Unlike single-oscillator records (fire on one witness, blind to the other two), any lone-witness extreme with the other two calm prints nothing. Unlike cross-edge records (trade the crossing bar), no cross is ever traded: both legs are `shift(1)` state prints evaluated per bar, never a one-bar edge. The prior-bar lag is the honesty feature — the decision bar's own values are never read, so no same-bar formation ambiguity exists by construction.

## Signal

Exact rule as pinned (any other CCI/MFI/CMO period, threshold, lag, risk rung, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; periods are TA-Lib library defaults (14/14/14), disclosed, never overridden in the file:

```text
cci[t] = TA-Lib CCI(high, low, close, 14)   // default period — no file override
mfi[t] = TA-Lib MFI(high, low, close, volume, 14)  // default period; sole volume consumer
cmo[t] = TA-Lib CMO(close, 14)              // default period — no file override
entry  = (cci[t-1] < -100) AND (mfi[t-1] < 20) AND (cmo[t-1] < -50)   // enter_long = 1
exit_sig = (cci[t-1] > 100) AND (mfi[t-1] > 80) AND (cmo[t-1] > 50)   // exit_long = 1
risk   = ROI ladder {"0": 0.05, "20": 0.03, "30": 0.02, "40": 0.0} (fraction, by position age in minutes);
         fixed stop at -5% (stoploss -0.05)
lag    = shift(1) on all six legs — the decision bar t reads only completed bar t-1 values
floor  = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar whose PRIOR bar prints the triple-oversold state, `direction` long-only; `exit_long=1` on bars whose prior bar prints the triple-overbought state. Each print is a state print re-evaluated per bar, not a one-bar edge — a book already positioned treats further entry bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): all six legs strict (`<`, `>`) — a prior bar with `cci == ±100`, `mfi == 20/80`, or `cmo == ∓50` fires neither leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `cci[t-1] < -100` AND `mfi[t-1] < 20` AND `cmo[t-1] < -50` while any signal-exit bar has `cci[t-1] > 100` AND `mfi[t-1] > 80` AND `cmo[t-1] > 50` — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirrored triple-overbought signal, the four-rung ROI ladder, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move beyond the ladder's own 40-minute `0.0` rung — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying triple-oversold bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`high`/`low`/`close` for CCI, plus bar `volume` inside MFI, `close` for CMO) with fixed non-negative offsets (trailing windows plus one `shift(1)` lag — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `15m` bars of BTCUSDT: `high`/`low`/`close` for the CCI path, plus bar `volume` for the MFI(14) path, and `close` for the CMO(14) path. No `open`-series read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `15m` (source-native — the file prints `timeframe = '15m'`). One evaluation per completed bar; every window reads the decision bar's causal past only, and every leg additionally lags one bar via `shift(1)`; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 30 fifteen-minute bars held flat. Covers the three 14-bar TA-Lib seeds plus the one-bar signal lag with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, and ADXMomentum siblings use. The `shift(1)` lag makes this conservative: the signal is knowable at the decision bar's open, yet the fill is pinned to its close. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirrored signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `15m` is an already-admitted interval on `main` via the PMax record, and the sub-`15m` `5m` frame rides the admitted EMASkipPump and CombinedBinHAndCluc records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the triple-oversold state opens the full unit on a flat book; the mirrored triple-overbought exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying triple-oversold bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (95 lines: the CCI/MFI/CMO default-period calls, the `shift(1)` triple-oversold long entry, the mirrored `shift(1)` triple-overbought exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `CMCWinner(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 30-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: every leg is strict (`<`/`>`) — a prior bar sitting exactly on any of the six thresholds fires nothing on either side. Strictness preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `qtpylib` and `numpy` are imported and never called anywhere in the 95 lines — display/plumbing leftovers with no gate effect, never repaired into a signal.
4. `hyperopt`-prose fence: the two `hyperopt` tokens are docstring prose (the must-keep method list and the frugality note) — no `IntParameter`/`CategoricalParameter`/`DecimalParameter`, no search space, no fitted surface exists anywhere. Nothing to freeze, nothing fitted.
5. Prolonged-extreme hold fenced: a market that stays oversold without printing the mirrored overbought state holds the position until an ROI rung or the −5% stop — there is no decay, chop, or time exit beyond the ladder's own 40-minute breakeven rung. Disclosed, not repaired.
6. Symmetric stop-distance fence: the −5% stop equals the opening `0.05` ROI rung by construction — the first minutes of a position are a symmetric ±5% bracket that tightens as the ladder descends. Coded fact, disclosed, not reinterpreted as a tight or loose risk regime.
7. Cousin records fenced as different constructions (none conjoins prior-bar CCI+MFI+CMO triple states with a four-rung ROI ladder): the admitted `chande-momentum-80-cross-reversal` pool-mate trades a single-indicator CMO threshold-cross edge, two-sided (edge vs state, one witness vs three, opposite direction scope); the admitted `cci-threshold-extreme-reversal` pool-mate trades CCI-only threshold-cross edges from a Pine script, two-sided, `4h` (one witness, edge vs state, different source family); the admitted `alphatrend-mfi-atr-trailing-reversal` pool-mate gates an AlphaTrend engine by MFI with ATR trailing (different engine, trailing risk, no CCI/CMO); the open-PR Forven CCI sibling (`#304`) is a single-indicator CCI oversold-recross edge, `1h` (per its title/pin — edge vs triple-state, one witness vs three). Not a threshold re-tuning of any of them: moving any period default, any of the six thresholds, the `shift(1)` lag, any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `ADXMomentum.py`, `AdxSmas.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, and `EMASkipPump.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 30-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the TA-Lib default-period readings (14/14/14 — library defaults, never file literals), and house sizing/costs — all predeclared above. The `15m` frame, the `shift(1)` triple-oversold entry with all its literals, the mirrored triple-overbought exit, the four-rung ROI ladder with the −5% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CCI(14)/MFI(14)/CMO(14) / six thresholds / `shift(1)` triple-state legs / mirrored exit / four-rung ROI ladder / −5% stop / single-unit long-only / `15m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Third-witness relevance: dropping the CMO legs (pure prior-bar CCI+MFI states, same exit mirror/risk) must not improve net expectancy; fail ⇒ the CMO witness adds nothing over price-deviation plus volume conviction.
- F2 — Volume-witness relevance: dropping the MFI legs (pure prior-bar CCI+CMO states, same exit mirror/risk) must not improve net expectancy; fail ⇒ the volume-weighted witness adds nothing over price-deviation plus momentum.
- F3 — Risk-ladder relevance: removing the ROI ladder/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the four-rung ladder plus −5% backstop adds nothing over the bare state machine.

## Crypto portability

BTCUSDT Binance perpetual `15m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count plus one fixed lag bar, portable across 24/7 crypto tape. Bar volume is a standard Binance kline field consumed only inside MFI. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `15m` frame rides existing admission precedent (PMax `15m`; EMASkipPump/CombinedBinHAndCluc `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market that never prints the mirrored triple-overbought state is held until an ROI rung or the −5% stop; a market that alternates triple states prints repeated full round-trips with no flat state to rest in (whipsaw profile, disclosed). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (Wilder-style seeding, default-period handling) live in the library outside the pinned file — pinned by call with default periods 14/14/14, not re-derived; exact reproduction inherits that library's seeding alongside the 30-bar floor.
- The `qtpylib`/`numpy` imports are dead — nothing further to fence.
- No trailing, no breakeven beyond the ladder's own 40-minute rung, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/CMCWinner.py
- https://github.com/freqtrade/freqtrade-strategies
