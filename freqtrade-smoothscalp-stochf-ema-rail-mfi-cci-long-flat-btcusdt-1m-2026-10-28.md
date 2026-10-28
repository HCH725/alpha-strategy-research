---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade SmoothScalp STOCHF-EMA-rail MFI-CCI long-flat on BTCUSDT 1m bars
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade SmoothScalp STOCHF-EMA-rail MFI-CCI long-flat on BTCUSDT 1m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf-sign-state` records — this is only its twelfth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/SmoothScalp.py`.
- GitHub blob SHA at the pinned commit: `9d0718b04aad27e8bc989b2362a22934485e9520`, size 3861 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 3861 bytes, 102 lines, SHA-256 `e32a8f758d8d57876210d479576e7e415ff924400b8d037bb0f30799cd801a5b`, identical to the GitHub blob (`git hash-object` reproduces `9d0718b0…485e9520`) — the entire file was retrieved and inspected.
- Registration: the file defines class `SmoothScalp(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/Scalp.py` (same STOCHF-rail-ADX skeleton but no MFI/CCI legs, stop `-0.04`, `1m`), `berlinguyinca/ReinforcedSmoothScalp.py` (hyperopt `IntParameter`/`BooleanParameter` grid plus `resample_to_interval` trend merge — different legs, different gates), `berlinguyinca/CofiBitStrategy.py` (the admitted stochf-rail ADX-gated record's pin, `5m`, ROI ladder, no MFI/CCI), and every other admitted berlinguyinca pin are different pins with different gates — this record pins ONLY the SmoothScalp file's literals below, and no reviewer repair may substitute a sibling constant or a sibling indicator.
- The file's own words (quoted for gate evidence, never extended): `INTERFACE_VERSION: int = 3`; `timeframe = '1m'`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.5`; indicators `ta.EMA(high,5)` / `ta.EMA(low,5)` (rails), `ta.EMA(close,5)` (dead — never read, fenced below), `ta.STOCHF(dataframe, 5, 3, 0, 3, 0)` (`fastk`/`fastd`), `ta.ADX(dataframe)` (library-default period 14), `ta.MFI(dataframe)` (library-default period 14), `ta.RSI(dataframe, timeperiod=14)` (dead), `ta.CCI(dataframe, timeperiod=20)` then overwritten by `ta.CCI(dataframe)` (library-default period 14 — the second assignment governs, both lines quoted, never merged into a third value), `qtpylib.bollinger_bands(close, 20, 2)` (graphing-only, dead), `ta.MACD(dataframe)` (library defaults, dead); entry `(open < ema_low) & (adx > 30) & (mfi < 30) & (fastk < 30) & (fastd < 30) & crossed_above(fastk, fastd)` (`enter_long = 1`); exit `((open >= ema_high) | crossed_above(fastk, 70) | crossed_above(fastd, 70)) & (cci > 150)` (`exit_long = 1`). No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.EMA` / `ta.STOCHF` / `ta.ADX` / `ta.MFI` / `ta.CCI` (TA-Lib abstract, fixed explicit-or-library-default periods above; MFI reads completed-bar `high`/`low`/`close`/`volume` inside its own arithmetic, disclosed); `qtpylib.crossed_above(a, b)` (the Freqtrade vendor edge `a[t-1] <= b[t-1] AND a[t] > b[t]` over completed bars — pinned by call, never re-derived; the two scalar-70 arms use the same primitive with a broadcast threshold, exactly as the admitted CofiBit sibling rides it). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call, no custom/confirm/adjust/stake callback in the file.
- Full-file token census (verified over the 102 lines this cycle): 1 `enter_long` and 1 `exit_long` as the only order legs; 0 `enter_short` / 0 `exit_short` / 0 `can_short` (no short leg anywhere — the single `short` token is the line-37 comment `the shorter the better`, prose, never a position); 1 `stoploss` attribute (`-0.5`) and 1 `minimal_roi` attribute (the single-rung `{"0": 0.01}` ladder) as the only risk legs; 0 shipped `trailing`; 0 `startup_candle_count` (the record's 40-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no volume token in the file body — bar volume enters the rule only inside the vendored MFI arithmetic, disclosed); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 3 `crossed_above` (one stoch-cross entry edge, two scalar-70 exit edges — the complete edge set); 0 `shift` (no lag call beyond the edges' own two-bar arithmetic). `Dict`, `List`, `reduce`, `numpy`, `DatetimeIndex`, and `merge` are imported but never read by any order-gating line (dead imports, fenced — no gate effect).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1m` frame, the six-conjunct STOCHF-rail-ADX-MFI entry edge, the CCI-gated three-arm signal exit, the single-rung 1% ROI target, the −50% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 40-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-28): working-tree filename/content search for `SmoothScalp.py` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a STOCHF-rail-MFI-CCI rule. The pool's nearest cousins are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the micro-dip when the 1-minute open prints under the 5-bar low-EMA while trend strength (ADX>30), oversold money flow (MFI<30), an oversold fast stochastic pair (fastk/fastd<30), and a fresh fastk-over-fastd cross all agree; exit when the open reclaims the 5-bar high-EMA rail or either stochastic line crosses above 70, provided the CCI(14) prints hot (>150). A single-rung 1% ROI target (`0.01` from open) and a fixed −50% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Oversold-micro-dip harvester with a hot-exhaust gate, long-only, on 1-minute bars. The entry is a six-way handshake: price position (open under the low rail), trend permission (ADX>30, so the dip sits inside a moving tape rather than dead chop), two oversold gauges from different families (MFI brings volume-weighted flow, CCI is fenced out of the entry entirely), and a timing edge (the fastk/fastd cross fires only on the crossing bar). The exit refuses to sell into weakness: even a rail reclaim or a stochastic 70-cross closes nothing unless momentum is genuinely overheated (CCI>150). The 1% ROI rung harvests micro-reversions quickly while the −50% stop is a catastrophic backstop that by construction almost never binds before the ROI rung or the signal exit in ordinary tape. The failure mode is plain: a chop that keeps printing fresh crosses with CCI pinned hot whipsaws the book bar-to-bar (no cooldown), while a dip that keeps dipping with CCI cold holds the unit with no time exit — the stop is the only floor.

## Signal

Exact rule as pinned (any other stochastic period, EMA length, ADX/MFI/CCI period or threshold, edge construction, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
ema_high[t] = EMA5(high); ema_low[t] = EMA5(low)
fastk[t], fastd[t] = STOCHF(5, 3, 0, 3, 0)
adx[t]  = ADX(14);  mfi[t] = MFI(14);  cci[t] = CCI(14)   // effective: second assignment governs
entry = (open[t] < ema_low[t]) AND (adx[t] > 30) AND (mfi[t] < 30)
        AND (fastk[t] < 30) AND (fastd[t] < 30)
        AND crossed_above(fastk, fastd)[t]                  // enter_long = 1, edge
exit_sig = ((open[t] >= ema_high[t]) OR crossed_above(fastk, 70)[t]
        OR crossed_above(fastd, 70)[t]) AND (cci[t] > 150)  // exit_long = 1
risk = ROI {"0": 0.01} (fraction of entry-price distance, by position age in minutes);
       fixed stop at -50% (stoploss -0.5, same basis)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the six-conjunct entry (the cross arm is a one-bar edge; the five level arms persist while true), `direction` long-only; `exit_long=1` on bars printing the CCI-gated three-arm exit. A book already positioned treats further entry bars as hold-no-ops under the position pin below, and a flat book treats exit bars as no-ops.
- Exact boundaries (pinned semantics): strict throughout except the rail exit (`<`, `>` strict; exit rail `>=` fires on exact touch — an open exactly on `ema_low`, ADX/MFI/fastk/fastd exactly on 30, CCI exactly on 150 fires nothing on that conjunct). The `5` / `14` / `30` / `70` / `150` literals are never tuned here. The three `crossed_above` edges ride the same verified vendor primitive the admitted CofiBit sibling evidences (scalar-broadcast inclusive edge on the two 70 arms, never a hand-rolled comparison).
- Same-bar co-print pin (resolved by position pin — disclosed, not repaired): entry needs `fastk < 30` and `fastd < 30` while the stochastic exit arms need a cross above 70 on the same bar — arithmetically exclusive on the oscillator legs. Entry needs `open < ema_low` while the rail exit arm needs `open >= ema_high` — exclusive unless the two period-5 high/low EMAs momentarily invert. No engine ordering is invented: under the single-unit position pin, a flat book treats any residual co-print bar as entry (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a positioned book treats it as exit-close. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero short-leg tokens ship anywhere — the lone `short` token is prose inside the timeframe comment (`the shorter the better`), never a leg — and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the CCI-gated three-arm signal exit, the single-rung 1% ROI target, and the −50% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rung and stop are fractions of entry-price distance (close-to-close price return), evaluated at bar closes — this basis is leverage-invariant, so downstream leverage/margin accounting cannot alter any exit event. No trailing, no time exit, no breakeven move — explicitly none, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying six-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). The file's 60-parallel-trade guidance is portfolio prose for a multi-market bot — this derived record pins one market and one unit, so the guidance never activates here (disclosed, never presented as source-native behaviour). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC plus bar volume inside MFI(14) (`open` for the rail comparisons, `high`/`low`/`close` for EMA/ADX/STOCHF/CCI, `volume` inside MFI only) with fixed non-negative offsets (trailing windows plus the two-bar `crossed_above` edges — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `open` legs read the completed bar's own open — point-in-time available at the decision, never intrabar. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract (`process_only_new_candles` default true — disclosed default, never a file literal).

## Required data

- Completed `1m` bars of BTCUSDT: `open` (both rail comparisons), `high`/`low`/`close` (EMA rails, ADX, STOCHF, CCI), plus bar `volume` read once inside the rule — inside the vendored MFI(14) arithmetic only; no standalone volume threshold leg ships. No `open`-beyond-rails read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (source-native — the file prints `timeframe = '1m'`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 one-minute bars held flat. Covers every live lookback (MFI/ADX/CCI 14, STOCHF seed, EMA 5, two-bar edges) with margin; the dead BB(20)/RSI(14)/MACD columns need no cover. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: TA-Lib seed windows print NaN until filled and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed, and TechnicalExample siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the CCI-gated signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal co-print pin leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed. The `1m` fill mechanics ride the admitted 1m low-BB sibling's evidenced path (MARKET fills at the first provided row's close, `POSITION_HOLD` holds, `Decimal("1")` missing-price guard, `trade_cost` pinned downstream as hypothetical — never actual Binance fees).
- Interval precedent (disclosed, not assumed): `1m` is an already-admitted interval on `main` via the low-BB sub-band record — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs (fractions of entry-price distance, leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the six-conjunct edge opens the full unit on a flat book; the CCI-gated exit, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying edge bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (102 lines: the EMA-rail/STOCHF/ADX/MFI/CCI calls, the six-conjunct entry edge, the CCI-gated three-arm exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `SmoothScalp(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result. (Deliberately no replay statistics are claimed in this record — no event count, hash, or terminal state is asserted that a reviewer would need to re-derive.)

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib seed NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. CCI-overwrite fence: the `timeperiod=20` CCI assignment is dead on arrival — the very next indicator block reassigns the same `cci` column with library-default period 14, so the effective exit gate is `CCI(14) > 150`, never 20. Both lines are quoted in Provenance; no third value is invented and the 20-bar variant is never claimed.
3. Dead-column fence: `ema_close`, `rsi`, `macd`/`macdsignal`/`macdhist`, and the `bb_lowerband`/`bb_upperband`/`bb_middleband` trio (marked `required for graphing` in the file's own comment) are computed and never read by any order-gating line — removing any of them changes no trade event. Dead imports (`Dict`, `List`, `reduce`, `numpy`, `DatetimeIndex`, `merge`) likewise gate nothing.
4. Exact-boundary fence: five entry conjuncts are strict, the rail exit arm fires on exact touch (`>=`), and `CCI == 150.0` exactly fires nothing. Strictness preserved throughout — disclosed, not smoothed.
5. Wide-stop fence: the −50% stop is 50× the opening `0.01` ROI rung — by construction the stop is a catastrophic backstop that almost never binds before the ROI rung or the CCI-gated exit in ordinary tape. Coded fact, disclosed, not reinterpreted as a tight risk regime and not tightened by repair.
6. No-60-trade fence: the docstring's 60-parallel-trade guidance is multi-market portfolio prose — this derived record pins a single market and a single unit, so the guidance is fenced out of every gate rather than silently adopted or silently violated.
7. Cousin records fenced as different constructions (none trades a six-conjunct STOCHF-rail-ADX-MFI entry edge with a CCI(14)-gated three-arm exit, long-flat, with a 1% ROI rung plus a −50% stop, on `1m`): the admitted `freqtrade-cofibit-stochf-ema-rail-adx-gated` pool-mate trades the same rail-plus-stoch skeleton but WITHOUT the MFI<30 and CCI>150 legs, with a four-rung ROI ladder and a −25% stop, on `5m` (a market printing MFI 45 with CCI 200 fires an exit here but nothing there; a market printing MFI 20 fires entries under different gates); the unadmitted sibling `berlinguyinca/Scalp.py` carries the same skeleton with no MFI/CCI legs and a −4% stop (different legs, different risk — never substituted); the admitted `freqtrade-macd-cci-dip-state` pool-mate gates on MACD polarity plus a CCI dip with different arms and frame; the admitted `freqtrade-strategy005-volume-surge-fisher-washout` pool-mate is a Fisher/MFI washout system with volume-surge legs. Not a threshold re-tuning of any of them: adding/removing the MFI or CCI legs, moving any period or threshold, converting any edge to a state (or vice versa), flipping any strictness, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `Scalp.py`, `ReinforcedSmoothScalp.py` (hyperopt grid plus resampled trend merge), `MACDStrategy_crossed.py`, `ADXMomentum.py`, and every other file in the collection are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the vendored TA-Lib/qtpylib implementations (pinned by call with explicit-or-default periods, never re-derived), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1m` frame, the six-conjunct entry edge with all its literals and strictness, the CCI-gated three-arm exit, the single-rung ROI target with the −50% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: STOCHF(5,3,0,3,0) / EMA5 rails / ADX(14)>30 / MFI(14)<30 / sub-30 stoch levels with cross edge / CCI(14)>150 exit gate with three arms / single-rung 1% ROI / −50% stop / single-unit long-only / `1m` BTCUSDT / same-bar-close fills are frozen.

- F1 — MFI/CCI relevance: removing the MFI<30 entry conjunct and the CCI>150 exit gate (bare rail-plus-stoch system, same risk) must not improve net expectancy; fail ⇒ the volume-flow and overheat legs add nothing over the skeleton.
- F2 — Edge relevance: replacing the fastk/fastd cross edge with the persistent sub-30 state (enter on every oversold bar, same exits) must not improve net expectancy; fail ⇒ the one-bar timing edge adds nothing over the bare state.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 1% rung plus −50% backstop adds nothing over the bare signal machine.

## Crypto portability

BTCUSDT Binance perpetual `1m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field on both spot and perpetual venues (read only inside MFI). Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1m` frame rides existing admission precedent (low-BB sub-band-dip `1m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions). Finer-frame microstructure noise and fee drag are downstream performance questions, not admission gates.
- A dip that keeps dipping with CCI cold is held with no time exit (the −50% stop is the only floor); a chop that keeps printing fresh crosses with CCI pinned hot whipsaws the book bar-to-bar with no cooldown to damp it — disclosed as the principal frictions. There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- Vendored indicator internals (TA-Lib seeding, NaN propagation, the `crossed_above` two-bar edge) live outside the pinned file — pinned by call with explicit-or-default periods, not re-derived; exact reproduction inherits those libraries' seeding alongside the 40-bar floor.
- The dead graphing/BB/MACD/RSI columns and dead imports are fenced — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
- https://github.com/freqtrade/freqtrade-strategies
