---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AverageStrategy EMA(8/21) cross volume-gated long-flat on BTCUSDT 4h bars
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

# Freqtrade AverageStrategy EMA(8/21) cross volume-gated long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/AverageStrategy.py`.
- GitHub blob SHA at the pinned commit: `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, size 2630 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2630 bytes, 79 lines, SHA-256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`, identical to the GitHub blob (`git hash-object` reproduces `dbb0ba65…0d308d493`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AverageStrategy(IStrategy)` (the only class in the file; author line credits Gert Wohlgemuth, self-described as a crossover proof of concept — `buys and sells on crossovers`, quoted, never extended). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/ReinforcedAverageStrategy.py` (hyperopt-reinforced variant of this idea — a different pin with different constants, never substituted here), `berlinguyinca/CCIStrategy.py`, `berlinguyinca/Low_BB.py`, `berlinguyinca/MultiRSI.py`, `berlinguyinca/Scalp.py`, `berlinguyinca/TechnicalExampleStrategy.py`, and every other admitted berlinguyinca pin are different pins with different gates — this record pins ONLY the AverageStrategy file's literals below, and no reviewer repair may substitute a sibling constant or a sibling indicator.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '4h'`; `minimal_roi = { "0": 0.5 }`; `stoploss = -0.2`; parameters `buy_range_short = IntParameter(5, 20, default=8)` and `buy_range_long = IntParameter(20, 120, default=21)` (defaults are file literals — the file ships no hyperopt result comment and no fitted table, so the defaults ARE the pinned rule, never a choice among variants); indicator loop `dataframe[f'ema{val}'] = ta.EMA(dataframe, timeperiod=val)` over the union of both parameter ranges; entry `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_short.value}'], dataframe[f'ema{self.buy_range_long.value}']) & (dataframe['volume'] > 0)` (`enter_long = 1`); exit `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_long.value}'], dataframe[f'ema{self.buy_range_short.value}']) & (dataframe['volume'] > 0)` (`exit_long = 1`). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no `position_adjustment`, no `cooldown`, no `max_open_trades`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (resolved by name, standard vendored libraries): `ta.EMA` (TA-Lib exponential moving average, `timeperiod` explicit per column) and `qtpylib.crossed_above` (the standard one-bar edge: `(A[t-1] <= B[t-1]) & (A[t] > B[t])`, verified vendored semantics, disclosed, never redefined). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no informative-pair call in the file.
- Full-file token census (verified over the 79 lines this cycle): 4 `short` — all four are the `buy_range_short` IntParameter NAME (declaration, range-listing, and two `.value` reads), zero short-leg/order tokens anywhere; 0 `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `can_short` (framework default `False` applies — disclosed default, never a file literal); 0 `position_adjustment` / 0 `pyramid` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security` / 0 `hyperopt`; 0 `shift` (no lag call — the edge is inside `crossed_above`, disclosed); 0 `open` (no open-column read — the rule reads `close`-derived EMAs plus bar `volume` only); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 2 `crossed_above` (the entry and exit edges); 2 `volume` (the two `> 0` guards); 5 `Parameter` (three in the single import line — `CategoricalParameter`, `DecimalParameter`, `IntParameter` — plus two live `IntParameter` declarations; no Categorical/Decimal/Boolean parameter is ever instantiated); 1 `reduce` (dead `functools` import, never called — plumbing, no gate effect); 1 `set(` (the `set(...)` dedup in the indicator loop — column-computation order only, every `ema{val}` column is computed independently so output values are order-invariant; disclosed, no gate effect).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `4h` frame, the EMA(8)-over-EMA(21) cross entry with `volume > 0`, the mirrored EMA(21)-over-EMA(8) cross exit with `volume > 0`, the single-rung 50% ROI target, the −20% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `averagestrategy` (case-insensitive) returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an EMA(8/21) cross rule. EMA-cross cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints (plus its own one-line idea note: `buys and sells on crossovers`): ride long exposure while the fast 8-bar EMA sits above the slow 21-bar EMA, entering on the upward cross (with positive bar volume) and leaving on the mirrored downward cross (with positive bar volume). A single-rung 50% ROI target (`0.5` from open) and a fixed −20% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Classic fast-slow trend-following machine, long-only, edge-triggered on both legs. The 8/21 EMA pair is a short-horizon trend filter: the book is long only while recent price outweighs its three-week-equivalent baseline (21 × 4h ≈ 3.5 days). The `volume > 0` guard is a degenerate-bar fence, not a volume thesis — it suppresses signals on empty bars (exchange halts, data gaps) while passing every real bar. The 50% ROI rung is so wide it almost never binds before the mirrored cross exit in ordinary tape (a de-facto signal-only exit regime with a disaster backstop plus the −20% stop, 2.5× tighter than the rung). The failure mode is plain: a range-bound market that chops across the EMA pair generates alternating cross edges — exit-then-re-enter round trips with no cooldown — while a parabolic rally holds the unit all the way to the 50% rung with no trailing harvest. There is no time exit.

## Signal

Exact rule as pinned (any other MA type, period pair, guard, risk rung, fill, frame, or book is a different, unpinned rule). Both periods are explicit file-literal defaults (`8`, `21`), never library defaults and never a choice among fitted variants:

```text
ema8[t]   = EMA(close, 8)                        // TA-Lib, causal
ema21[t]  = EMA(close, 21)                       // TA-Lib, causal
entry     = crossed_above(ema8, ema21)[t] & (volume[t] > 0)   // enter_long = 1, one-bar edge
exit_sig  = crossed_above(ema21, ema8)[t] & (volume[t] > 0)   // exit_long = 1, one-bar edge
risk      = ROI {"0": 0.5} (fraction of entry-price distance, by position age in minutes);
            fixed stop at -20% (stoploss -0.2, same basis)
floor     = leading-window bars: EMA seeding NaNs make crossed_above false (see Required data)
```

- Trade events: `enter_long=1` on the single bar where EMA(8) crosses above EMA(21) with positive bar volume, `direction` long-only; `exit_long=1` on the single bar where EMA(21) crosses above EMA(8) with positive bar volume. Both legs are one-bar edges, not persistent states — a book already positioned treats further entry-edge bars as hold-no-ops under the position pin below, and a flat book treats exit-edge bars as no-ops.
- Exact boundaries (pinned semantics): `crossed_above(A,B)` is `(A[t-1] <= B[t-1]) & (A[t] > B[t])` — strict on the decision bar, weak on the prior bar. Touch-equality on the decision bar (`ema8 == ema21`) fires neither leg; EMA-seeding NaNs propagate false through both comparisons, so pre-seed bars deterministically fire neither leg (coded library behaviour, disclosed, never repaired). The volume guard is strict (`> 0`) — a zero-volume bar fires neither leg even on a geometric cross.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `ema8[t] > ema21[t]` while any signal-exit bar has `ema21[t] > ema8[t]` — mutually exclusive on every bar, degenerate, zero-volume, or otherwise, so entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill); any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere (the four `short` tokens are the `buy_range_short` parameter name — fenced in Provenance), and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirrored cross edge, the single-rung 50% ROI target, and the −20% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rung and stop are fractions of entry-price distance (close-to-close price return), evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. No trailing, no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-edge bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-edge bars as no-ops; re-entry re-arms on any qualifying cross edge after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (through two fixed-period causal EMAs) and completed-bar `volume` under the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal); the decision bar's own forming values are never read. The indicator loop's `set(...)` ordering affects only dead-column computation order, never read values (disclosed). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter value read beyond the two pinned defaults, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `4h` bars of BTCUSDT: `close` (both EMA constructions) plus bar `volume` (the strict `> 0` guard on each leg — a degenerate-bar fence, disclosed; no volume thesis, no volume threshold leg beyond positivity). No `open`/`high`/`low` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 four-hour bars held flat. Covers the 21-bar slow-EMA seed with margin (the only read lookback). The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: EMA seeding prints NaN until seeded and every `crossed_above` NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced HLHB, MultiMA-TEMA, and all eight admitted 5m siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the signal-exit edge, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `4h` is an already-admitted interval on `main` via the HLHB and MultiMA-TEMA records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the upward cross edge opens the full unit on a flat book; the mirrored cross edge, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying cross edge (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (79 lines: the EMA loop, the two pinned `IntParameter` defaults, the two guarded cross edges, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `AverageStrategy(IStrategy)` class pin) plus its one-line idea note (`buys and sells on crossovers`). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: EMA-seeding NaNs make `crossed_above` false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-equality rule fenced: the edge is strict on the decision bar — a bar printing exactly `ema8 == ema21` fires neither leg. Strictness preserved throughout — disclosed, not smoothed.
3. Zero-volume fence: the strict `volume > 0` guard on both legs means a geometric cross on a zero-volume bar fires neither leg. The guard is a degenerate-bar fence, never reinterpreted as a volume thesis and never widened into a threshold.
4. Dead-code fences: the `reduce` import is never called; the `set(...)` in the indicator loop affects only dead-column computation order (all read columns are order-invariant); the imported-but-never-instantiated `CategoricalParameter`/`DecimalParameter` are plumbing. None of them narrows or widens any gate.
5. Wide-rung fence: the 50% ROI rung is 2.5× the −20% stop distance — by construction the rung is a disaster backstop that almost never binds before the mirrored cross exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight profit-taking regime and not tightened by repair.
6. Default-pin fence: the file ships no hyperopt result comment and no fitted table — the `IntParameter` defaults (8, 21) are the only numeric rule the file offers, so pinning them is verbatim reproduction, never a choice among plausible variants. Substituting any hyperopt-found or sibling-file period pair would be a different, unpinned rule.
7. Cousin records fenced as different constructions (none trades an EMA(8)/EMA(21) symmetric guarded cross pair, long-flat, on `4h`, with a 50% ROI rung plus a −20% stop): the admitted `eterna-sma-50-200-crossover` pool-mate trades SMA(50/200) two-sided on `4h` (different MA type, different periods, different direction); the admitted Forven DEMA/HMA/TEMA-cross pool-mates trade double-smoothed MA variants on `1h` (different indicator math, different frame, Forven source); the admitted `alma-cross-volume-gate` pool-mate trades ALMA on `1d` (different indicator); the admitted `obv-ema-crossover` pool-mate trades OBV against its own EMA (different construction — volume-derived line, not price-EMA pair); the admitted `freqtrade-strategy001-ha-ema-cross` pool-mate trades an EMA cross on Heikin-Ashi-transformed data on `5m` (different data, different frame); the admitted `freqtrade-multima-tema-stack` pool-mate trades a TEMA stack on `4h` (different indicator); open PR #331 (AdxSmas SMA3/6-cross, `1h`) differs in type, periods, frame, and gate. Not a threshold re-tuning of any of them: moving either period, changing the MA type, dropping the volume guard, converting either edge to a state, flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `ReinforcedAverageStrategy.py` (hyperopt-reinforced variant), `CCIStrategy.py`, `Low_BB.py`, `MultiRSI.py`, `Scalp.py`, `TechnicalExampleStrategy.py`, `MACDStrategy.py`, `MACDStrategy_crossed.py`, and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the vendored EMA/`crossed_above` implementations (pinned by call with explicit periods, never re-derived), and house sizing/costs with safety tranches deactivated — all predeclared above. The `4h` frame, the EMA(8)/EMA(21) guarded cross entry with all its literals and strictness, the mirrored guarded cross exit, the single-rung ROI target with the −20% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA(8/21) / guarded cross edges with pinned strictness / mirrored signal exit / single-rung 50% ROI / −20% stop / single-unit long-only / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Cross-filter relevance: entering on the first post-warmup bar and holding time-in-market (same ROI/stop exits, no cross legs) must not improve net expectancy; fail ⇒ the cross filter adds nothing over blind exposure.
- F2 — Guard relevance: dropping the `volume > 0` guard on both legs (pure geometric crosses, same risk) must not improve net expectancy; fail ⇒ the coded guard adds nothing over its unguarded twin.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 50% rung plus −20% backstop adds nothing over the bare cross machine.

## Crypto portability

BTCUSDT Binance perpetual `4h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `4h` frame rides existing admission precedent (HLHB, MultiMA-TEMA `4h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a permanently trending market is held until the 50% rung or the mirrored cross; a range-bound market that chops across the EMA pair whipsaws the book across alternating edges (exit-then-re-enter round trips with no cooldown to damp them — disclosed as the principal friction). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- Vendored indicator internals (TA-Lib EMA seeding, `crossed_above` NaN propagation) live outside the pinned file — pinned by call with explicit periods, not re-derived; exact reproduction inherits that seeding alongside the 40-bar floor.
- The author's proof-of-concept note is a humility flag, not a rule — nothing further to fence.
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
