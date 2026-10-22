---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade FSample RSI-cross TEMA-mirror flip two-sided on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade FSample RSI-cross TEMA-mirror flip two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to the `futures/` directory).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/FSampleStrategy.py`.
- GitHub blob SHA at the pinned commit: `cb55a9253473697fb7ccb71c8a8fe3454929cd92`, size 5413 bytes.
- Byte-identity check: the file at the pinned commit is 5413 bytes, 162 lines, SHA-256 `3fcbe2ed16dd097fd6e4548172acbde871bdfe64c5a7341f337f19caf3daa225`, identical to the GitHub blob (`git hash-object` reproduces `cb55a925…4929cd92`) — the entire file was retrieved and inspected.
- Registration: the file defines class `FSampleStrategy(IStrategy)` (the only class in the file; `grep -c 'class .*IStrategy'` returns 1). No sibling file in the repository defines this class — identity is class plus file path, both unique.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "1h"` (line 27); `minimal_roi = {"0": 1}` (line 31); `stoploss = -0.05` (line 33); `can_short = True` (line 34); `trailing_stop = False` (line 37); `process_only_new_candles = True` (line 43); `startup_candle_count: int = 30` (line 46); header comment `This class is a sample. Feel free to customize it.` (line 23 — framework-sample provenance, never a production claim). Entry long (lines 99–112): `qtpylib.crossed_above(dataframe["rsi"], 30)` with `tema <= bb_middleband`, `tema` rising (`tema > tema.shift(1)`), `volume > 0`. Entry short (lines 114–127): `crossed_above(rsi, 70)` with `tema > bb_middleband`, `tema` falling, `volume > 0`. Exit long (lines 131–145) repeats the short-entry conjunction verbatim; exit short (lines 147–160) repeats the long-entry conjunction verbatim — exits are exact mirrors, never separate inventions.
- Source test-context (quoted, never adopted as admission evidence): the sibling `user_data/strategies/futures/Readme.md` states `all strategies are tested against this config. Tests only done on binance futures`, with `trading_mode: futures`, `margin_mode: isolated`, `stake_currency: USDT`, and `BTC/USDT:USDT` on its pair whitelist. The `BTCUSDT` perpetual-isolated venue choice below is consistent with this context, but the record's economics are the record's own pins, never the readme's live-order-book pricing block.
- Full-file token census (verified over the 162 lines this cycle): 1 `enter_short` / 1 `exit_short` / 1 `can_short` (the complete short stance — shipped `True`, never a default reading); 4 `crossed_above` (exactly the four RSI one-bar edges) / 0 `crossed_below`; 4 `shift` (exactly the four `tema.shift(1)` slope reads, all lag-1, never negative); 8 `volume` (exactly the four `volume > 0` guards plus their four `Make sure Volume is not 0` comments — bar volume additionally enters inside TA-Lib MFI arithmetic, a dead column, disclosed); 0 `open` (no open-column read anywhere in the gating path); 0 `.value` with 4 `Parameter` import lines (`BooleanParameter`/`CategoricalParameter`/`DecimalParameter`/`IntParameter` imported and never instantiated — dead imports, fenced, no fitted constant anywhere); 0 `hyperopt`; 5 `trailing` (one `Trailing stoploss` comment, the shipped `trailing_stop = False`, three commented trailing lines — trailing explicitly off, never defaulted); 3 `minimal_roi` (two comment lines plus the single active rung); 2 `stoploss` (the `-0.05` attribute plus the `Trailing stoploss` comment); 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` (no economics beyond ROI/stop); 0 `position_adjust` / 0 `max_open_trades` / 0 `cooldown` / 0 `pyramid` / 0 `position_size` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `use_exit_signal` / 0 `exit_profit_only` (framework defaults disclosed below, never file literals); 0 `resample` / 0 `informative` / 0 `merge` / 0 `request.` / 0 `security` (single-frame, no external feed); 0 `np.` / 0 `pd.` (`numpy`/`pandas` imported and never called — dead imports, fenced as plumbing). `Dict`, `List`, `reduce`, `DatetimeIndex` are not imported at all.
- Indicator census: only three gated columns — `rsi` (`ta.RSI`, no period override → TA-Lib default 14, disclosed default, never a file literal), `tema` (`ta.TEMA`, explicit `timeperiod=9`), `bb_middleband` (20-bar midline of typical price, `window=20, stds=2`, both explicit). Dead computed-never-read columns: `adx`, `fastd`/`fastk`, `macd`/`macdsignal`/`macdhist`, `mfi`, `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width`, `sar`, `htsine`/`htleadsine` — fenced, no gate effect.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the four RSI-cross conjunctions, the mirrored exit pairing, the single-rung ROI, the −5% stop, the shipped trailing-off, the shipped 30-bar startup floor, the shipped per-completed-bar evaluation, and the two-sided stance — but ships no venue spelling, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` on Binance USDT-M perpetual, Isolated (the file names no market; consistent with the futures-readme test context, never claimed as source-market equivalence); (2) completed-bar decisions with same-bar-close market fills (derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op and flip semantics plus adoption of the file's own 30-bar floor (the 30 is source-native; the single-unit/flip pin is researcher-declared); (4) framework-default readings (`use_exit_signal=True`, `exit_profit_only=False` — exits fire even at a loss; disclosed defaults, never file literals); (5) record-pinned research costs (fixed taker fee, no slippage add-on, contract precision; funding explicitly excluded per baseline §4 — see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree filename/content search for `fsample` (case-insensitive) returns zero strategy records — no record in the pool cites this source file or class. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an RSI-cross/TEMA-mirror rule. TEMA and RSI-cross cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: a framework sample that enters long on a one-bar RSI-cross above 30 while 9-bar TEMA sits at/below its 20-bar Bollinger midline and rises, enters short on the mirrored RSI-cross above 70 while TEMA sits above its midline and falls, and closes each side on the other side's entry print. A single-rung 100% ROI target (`1` from open — effectively non-binding, preserved verbatim) and a fixed −5% stoploss backstop every position; trailing explicitly off. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Two-sided oversold/overbought snap-back flip machine. Each side demands three simultaneous facts: a fresh one-bar momentum edge (RSI crossing its trigger — not merely residing beyond it, so a market pinned above 70 keeps no standing short-entry bid), a value location (TEMA on the weak side of its own Bollinger midline), and a slope confirmation (TEMA moving toward the midline, i.e. mean-reverting, not accelerating away). Because each side's exit is the other side's entry, a positioned book reverses instead of merely flattening whenever the opposite print arrives — the strategy is always either long, short, or flat, never both. The −5% stop (20× tighter than the file's own disabled-scale ROI rung) is the only risk leg that can bind in ordinary tape. The failure mode is plain: a tape that alternates RSI-cross prints direction every few bars flips the book long-short-long with no cooldown to damp the round trips (disclosed as the principal friction), while a one-sided trend that never prints the opposite conjunction holds the unit until the stop.

## Signal

Exact rule as pinned (any other RSI period/threshold, TEMA period, midline window, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). The TEMA period (9) and Bollinger window/stds (20/2) are explicit file literals; the RSI period is the TA-Lib default 14 (no override in the file — disclosed, never filled in from elsewhere):

```text
rsi[t]  = TA-Lib RSI(close, 14)
tema[t] = TA-Lib TEMA(close, 9)
mid[t]  = 20-bar SMA of typical price ((high+low+close)/3)
long_in  = crossed_above(rsi, 30) AND (tema[t] <= mid[t]) AND (tema[t] > tema[t-1]) AND (volume[t] > 0)
short_in = crossed_above(rsi, 70) AND (tema[t] >  mid[t]) AND (tema[t] < tema[t-1]) AND (volume[t] > 0)
exit_long  = short_in          // verbatim mirror, lines 131-145
exit_short = long_in           // verbatim mirror, lines 147-160
risk = ROI {"0": 1} (fraction of entry-price distance, +100% — effectively non-binding, preserved verbatim);
       fixed stop at -5% (stoploss -0.05, same basis); trailing explicitly False (shipped)
floor = first 30 bars flat (shipped startup_candle_count, source-native)
```

- Trade events: `enter_long=1` / `enter_short=1` are one-bar edges (each `crossed_above` is true only on the crossing bar: `rsi[t] > K AND rsi[t-1] <= K`). A positioned book treats same-side re-prints as hold-no-ops under the position pin below; a flat book treats exit prints as no-ops; an opposite-side print on a positioned book flips it (close-then-open at the same decision-bar close — end-state deterministic, see Execution assumptions).
- Exact boundaries (pinned semantics): RSI comparisons are cross-edges with strict `>` on the decision bar and `<=` on the prior bar — a bar with `rsi == 30.0` exactly can only satisfy the prior-bar side, never fire; TEMA-vs-midline is `<=` long / `>` strict short (a TEMA exactly on the midline admits long-entry, never short-entry); both slope guards are strict (a flat TEMA bar fires neither side); the volume guard is strict `> 0` (zero-volume bars deterministically fire nothing). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): long entries demand `tema[t] <= mid[t]` while short entries demand `tema[t] > mid[t]` — mutually exclusive on every bar, so the two entries never co-print even when a single bar's RSI jumps from ≤30 to >70 and prints both cross edges (fenced in Negative evidence). By the mirror identity the two exits are equally exclusive. The reviewer is never asked to invent an ordering: every same-bar fill lands on the same decision-bar close, so close-then-open and open-then-close converge to the identical end-of-bar book (one unit of the surviving side, or flat).
- Direction: two-sided, explicit. `can_short = True` ships on line 34 — a long-only reading would contradict the file. The two-sided book requires a margin venue (see Crypto portability — not expressible on spot as-is).
- Exits and risk (explicit): the mirrored signal exits, the single-rung 100% ROI target, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rung and stop are fractions of entry-price distance (close-to-close price return), evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. The 100% rung is effectively non-binding in ordinary tape (disclosed consequence of the coded magnitude, never a repair — the magnitude is preserved verbatim). Trailing is explicitly off (shipped `False`); no time exit, no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — funding changes only a downstream performance report, never whether an exit fires (disclosed; this record claims no performance).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; same-side re-prints are hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); flat-book exit prints are no-ops; opposite-side prints flip (close-then-open at the same close); re-entry re-arms on any qualifying edge after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar values (trailing windows plus one-bar edges with fixed non-negative offsets — no forward reference) under the file's own shipped framework contract (`process_only_new_candles = True` — file literal, never a default reading); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar/hour call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` (typical-price midline, RSI, TEMA construction) plus bar `volume` (the four `> 0` entry guards; volume additionally enters inside the dead TA-Lib MFI column only). No `open` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = "1h"`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (source-native): the file's own `startup_candle_count = 30` holds the first 30 one-hour bars flat. Covers the 20-bar midline seed (the longest gated lookback) with margin; RSI(14) and TEMA(9) seed inside it. Coded behaviour underneath: rolling windows print NaN until seeded and every strict/edge NaN comparison is false — no leg can fire early. The dead Hilbert/MACD/SAR columns seed later but never gate any order line (fenced). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT on Binance USDT-M perpetual, Isolated (researcher choice consistent with the source futures-readme test context — `trading_mode: futures`, `margin_mode: isolated`, USDT stake, BTC whitelisted — quoted above; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, and ADXMomentum `1h` siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entries, mirrored exits, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order (every co-print converges to the identical end-of-bar book at the same close price); the source framework's own same-candle evaluation order (risk legs, then exits, then entries) is disclosed as context, never needed to resolve any ambiguity here.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the BbandRsi, AwesomeMacd, and ADXMomentum records plus the Forven `1h` family — no novel-interval confirmation is required for this frame. The two-sided single-position flip rides the same completed-bar path as the admitted two-sided Eterna records (one surviving position, immediate reversal, no shared portfolio state).
- Sizing/capital/costs (record-pinned, reproducible): the source ships no sizing, capital, fee, margin, or funding concept. Sizing rides the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) under the single-unit/no-add position pin — no safety-order tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event. Costs are this record's own fixed research numbers (never presented as source-native, never as canonical HB economics): taker fee 0.05% per side (Binance USDT-M published standard rate, no discount claimed), fills printed at the decision-bar close with no slippage add-on (lane-native simplification, disclosed), quantity/price precision at the public BTCUSDT contract spec (tick 0.1, step 0.001 — disclosed assumption; quantization moves reported cents, never event existence). Funding is explicitly EXCLUDED from this record's economics: per `docs/hb-backtest-baseline-v1.0.md` §4 the pinned V2 simulator has not proven historical-funding support, so no historical funding is claimed and none is silently recorded as zero — funding is flagged unsupported/unmodeled, and since no order-gating line reads funding or net profit, every trade event in this record is funding-invariant (only a downstream performance report, which this record does not claim, could move).
- Margin/liquidation fence (arithmetic, not assumed): the −5% price-distance stop equals −15% of margin equity at 3x and −25% at 5x Isolated; liquidation needs roughly −30% (3x) / −18% (5x) adverse price — the stop binds first at either house setting with wide margin, so no liquidation leg can pre-empt any exit event. The 100% ROI rung needs +100% price (+300%/+500% equity) and is effectively non-binding (disclosed, preserved verbatim).
- Concurrency: at most one position per market at any time; an edge opens the full unit on a flat book (or flips a positioned book); the mirrored exit, the ROI rung, or the stop closes it in full. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. (The futures-readme test config's `max_open_trades: -1` and live order-book pricing block are source-test context only — never adopted; the derived single-unit pin governs.)

## Evidence

### Source-reported

The file ships the full construction (162 lines: the four RSI-cross conjunctions with all literals, the verbatim mirrored exits, the `timeframe`/single-rung-ROI/`stoploss`/`can_short`/trailing-off/per-bar-evaluation/30-bar-floor literals, and the `FSampleStrategy(IStrategy)` class pin) plus its own `This class is a sample` provenance note. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false and cross-edges need two valid bars (no early entry, no early exit). The 30-bar floor is the file's own shipped literal — adopted, never repaired. The commented-out alternative ROI (`{"60": 0.1, "30": 0.2, "0": 0.2}`, line 30) is dead prose — the active rung is `{"0": 1}`; no reviewer repair may substitute the comment.
2. Exact-boundary fence: RSI edges need strict `>` on the decision bar (`rsi == 30/70` exactly never fires); TEMA-on-midline admits long-entry only; flat-TEMA bars fire neither side; zero-volume bars fire nothing. Strictness preserved throughout — disclosed, not smoothed.
3. RSI-jump fence: a bar leaping from `rsi <= 30` to `rsi > 70` prints both cross edges, but entries stay exclusive via the mirrored `tema <= mid` / `tema > mid` level split on the same bar's single TEMA/midline values — a full entry co-print is arithmetically impossible and no fill-ordering invention is ever needed.
4. Dead-column fence: `adx`, `fastd`/`fastk`, `macd` triple, `mfi`, `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width`, `sar`, `htsine`/`htleadsine` are computed and never read by any order line — their library seeding (including the long Hilbert seed) cannot move any event. Dead imports (`BooleanParameter`/`CategoricalParameter`/`DecimalParameter`/`IntParameter`, `numpy`, `pandas`) are plumbing with no gate effect; no fitted constant ships anywhere.
5. Wide-rung fence: the 100% ROI rung is effectively disabled by its own coded magnitude (needs +100% price) — disclosed consequence, preserved verbatim, never tightened by repair. The −5% stop is the only risk leg that binds in ordinary tape.
6. Flip-order fence: exit-long IS enter-short and exit-short IS enter-long (line-identical conjunctions) — a flip bar closes one unit and opens one unit at the same decision-bar close, converging to the identical end-of-bar book under either micro-order; the source framework's risk-then-exit-then-entry same-candle order is consistent with, but never required for, this convergence. Stop co-prints resolve identically (flat-then-fill at the same close).
7. Cousin records fenced as different constructions (none trades one-bar RSI 30/70 crosses with a TEMA-vs-20-bar-midline plus slope mirror, two-sided, `1h`, ROI-disabled, −5% stop): the admitted `freqtrade-quickie-tema-slope-bbmid` pool-mate trades long-only persistent STATE legs (ADX>30, TEMA<mid, rising slope, close<SMA200, `5m`) with a four-rung decaying ROI ladder plus a −25% stop (a market drifting with RSI pinned at 60 fires entries there but nothing here; a fresh RSI-30 cross with ADX<30 fires here but nothing there); the admitted `freqtrade-bband-rsi-dip-buy` pool-mate trades a BB-rider dip state (`1h`, long-flat, different risk); the admitted `forven-chaikin-mf-threshold-cross` pool-mate trades ±0.05 CMF threshold CROSS edges on a 20-bar CMF (`1h`, long-flat, no stop, Forven source); the admitted two-sided Eterna SMA records trade dual-moving-average cross states behind different gates on different frames. Not a threshold re-tuning of any of them: moving any period, threshold, strictness, edge/state pairing, side, rung, stop, or frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in the collection — all of `berlinguyinca/` (including the admitted TechnicalExample, BinHV27, MACDStrategy pair, Quickie, Simple, and the rejected BinHV45/CCIStrategy/Scalp neighbours) and every other `futures/` file (`VolatilitySystem` with averaging/leverage calls, `FSupertrendStrategy`, `FOttStrategy`, `FReinforcedStrategy`, `FAdxSmaStrategy`, `TrendFollowingStrategy`) — are separate pins; their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT perpetual-isolated market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown flip pin, the framework-default readings (`use_exit_signal=True`, `exit_profit_only=False`), and the record-pinned fee-only costs with funding excluded — all predeclared above. The `1h` frame, the four RSI-cross conjunctions with all literals and strictness, the verbatim mirrored exits, the single-rung ROI with the −5% stop, the shipped trailing-off, the shipped 30-bar floor, the shipped per-bar evaluation, and the two-sided stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14) 30/70 cross edges / TEMA(9) vs 20-bar-midline with pinned strictness and slope guards / verbatim mirrored exits / single-rung 100% ROI / −5% stop / trailing-off / single-unit two-sided flip / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Edge relevance: replacing each one-bar cross with its persistent residing state (RSI>30 / RSI>70 held every qualifying bar, same guards and risk) must not improve net expectancy; fail ⇒ the cross edges add nothing over standing exposure.
- F2 — Slope/location relevance: dropping the TEMA-vs-midline and slope guards (bare RSI-cross flips, same risk) must not improve net expectancy; fail ⇒ the value/slope conjunction adds nothing over naked RSI edges.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (mirror-signal-only exits) must not improve net expectancy; fail ⇒ the −5% backstop adds nothing over the bare flip machine.

## Crypto portability

BTCUSDT Binance USDT-M perpetual `1h` is the research pin (source names no market; consistent with the futures-readme Binance-futures test context). The two-sided flip book requires a margin venue and is NOT portable to spot as-is (no naked shorting) — disclosed, not repaired; a long-only cut would be a different, unpinned rule. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field. Funding is declared nowhere in the source and is explicitly excluded from this record's economics (see Execution assumptions).

## Limitations

- Funding is excluded from this record's economics per baseline §4 (pinned path unproven) — flagged, never zero-claimed; trade events are funding-invariant but any future reported performance must re-add a proven funding treatment before it can be called HB economics.
- The book can flip long-short-long on consecutive alternating RSI-cross bars (no cooldown to damp round trips — disclosed as the principal friction). There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- The 100% ROI rung is effectively disabled by construction — disclosed, not repaired into a tighter target.
- Dead-column internals (TA-Lib seeding, NaN propagation) live outside the pinned file — never read by any order line, so exact reproduction inherits no unpinned behaviour through them.
- The futures-readme test config (`max_open_trades: -1`, order-book pricing, unfilled-timeout block) is live-test context only — nothing further to fence beyond non-adoption.
- No trailing, no breakeven, no time exit, no cooldown — all explicitly absent (trailing explicitly off by shipped literal), never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
