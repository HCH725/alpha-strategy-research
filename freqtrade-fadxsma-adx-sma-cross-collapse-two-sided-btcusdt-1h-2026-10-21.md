---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade FAdxSmaStrategy ADX-threshold SMA-cross collapse-exit two-sided on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FAdxSmaStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade FAdxSmaStrategy ADX-threshold SMA-cross collapse-exit two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, and `freqtrade-macd-cross-cci-edge` records — this is only its eleventh record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/FAdxSmaStrategy.py`.
- GitHub blob SHA at the pinned commit: `3bb13caf079e8360a959c3ad4dd2b2507f3045c0`, size 4091 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 4091 bytes, 130 lines, SHA-256 `43ae02ecca4553b8a609d4533cb4d5b6517292d35b41fc4c77f54f8e959ced89`, identical to the GitHub blob (`git hash-object` reproduces `3bb13caf…2507f3045c0`) — the entire file was retrieved and inspected.
- Registration: the file defines class `FAdxSmaStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/AdxSmas.py` (SMA3/6 cross gated by ADX polarity state, long-flat, `1h`, open PR #331), `berlinguyinca/ADXMomentum.py` (ADX/DI/MOM four-conjunct state, long-flat, `1h`), `user_data/strategies/hlhb.py` (EMA-RSI-ADX quad-gated, long-flat, `4h`), and `futures/TrendFollowingStrategy.py` (EMA20 cross with OBV confirmation plus trailing stop, two-sided, `5m`) are different pins with different gates — this record pins ONLY the FAdxSmaStrategy file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "1h"`; `minimal_roi = {"60": 0.075, "30": 0.1, "0": 0.05}`; `stoploss = -0.05`; `can_short = True`; `trailing_stop = False`; `process_only_new_candles = True`; `startup_candle_count: int = 14`; entry long `adx_{adx_period} > pos_entry_adx` AND `crossed_above(sma_short_{sma_short_period}, sma_long_{sma_long_period})` (`enter_long = 1`); entry short `adx_{adx_period} > pos_entry_adx` AND `crossed_below(sma_short_{sma_short_period}, sma_long_{sma_long_period})` (`enter_short = 1`); exits (BOTH sides) `adx_{adx_period} < pos_entry_adx` (`exit_long = 1`, `exit_short = 1`). No `buy_params`/`sell_params` dict, no `order_types`, no `order_time_in_force`, no `leverage`, no `funding`/`mark_price`, no `use_exit_signal` / `exit_profit_only` override, no `pyramiding`/`position_adjustment`/`cooldown`/`max_open_trades` ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Hyperopt-parameter pin (all resolved by default `.value`, never optimized): `pos_entry_adx = DecimalParameter(15, 40, decimals=1, default=30.0, space="buy")`; `adx_period = IntParameter(4, 24, default=14, space='buy')`; `sma_short_period = IntParameter(4, 24, default=12, space='buy')`; `sma_long_period = IntParameter(12, 175, default=48, space='buy')`. There is NO `buy_params`/`sell_params` dict anywhere in the file, so the defaults ARE the single value source — no dict-vs-Parameter clash exists (unlike the deliberately passed-over HourBased/Supertrend/BinHV45/MACDStrategy files). Effective pinned rule: ADX(14) vs 30.0, SMA(12) vs SMA(48).
- Out-of-file calls pinned (all resolved by name, all standard): `ta.ADX` (TA-Lib Average Directional Index on high/low/close, period 14 — pinned default); `ta.SMA` (TA-Lib Simple Moving Average on close, periods 12 and 48 — pinned defaults); `qtpylib.crossed_above` / `qtpylib.crossed_below` (standard Freqtrade one-bar edge: `(s1 > s2) & (s1.shift(1) <= s2.shift(1))` and its mirror — causal two-bar comparison, disclosed, never redefined). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no informative-pair call in the file.
- Full-file token census (verified over the 130 lines this cycle): 0 `volume` (no volume read of any kind — ADX reads high/low/close, SMAs read close); 0 `shift` (no lag call in the file body — the single one-bar lookback lives inside the standard `crossed_*` edge, disclosed above); 1 `hyperopt` (comment `# Hyperoptable parameters` only — prose, no fitted value); 0 `buy_params` / 0 `sell_params`; 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `use_exit_signal` / 0 `exit_profit_only`; 2 `cross` (the two `crossed_*` edge calls); 1 `can_short` (`can_short = True` — the explicit two-sided charter); 1 `startup_candle_count` (`14` — quoted source value, fenced in Negative evidence 1 as shorter than the SMA48 seed); 5 `trailing` (one `trailing_stop = False` plus its heading comment plus three commented-out offset lines — trailing explicitly disabled, never armed). `numpy as np`, `pandas as pd`, `BooleanParameter`, and `CategoricalParameter` are imported and never referenced again — dead imports, fenced as plumbing with no gate effect. `pos_exit_adx` (DecimalParameter default 30.0, space sell) is defined and read by NO order line — the exits use `pos_entry_adx` instead — fenced as a dead parameter in Negative evidence 3, never repaired into a second threshold.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the ADX(14)-vs-30.0 threshold gate, the SMA12/48 cross edges, the single ADX-collapse exit shared by both sides, the three-rung ROI ladder, the −5% stop, the disabled trailing, and the two-sided charter — but ships no venue spelling, no fill-timing flag, no sufficient warmup guard (its `14` does not cover SMA48), and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills (the file's own framework contract evaluates per completed bar via `process_only_new_candles = True` — derivation disclosed, never presented as the source engine's own timing); (3) single-unit per-market position pin with opposite-entry hold-no-op semantics plus a 50-bar researcher warmup pin (the file carries no position reference and its `14` guard is fenced as insufficient — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). The admitted version's trade events are single full-unit opens/closes: the house percentages partition capital behind that same one unit and add NO second entry event, NO averaging-down trigger, and NO staged add to this version (none ships anywhere). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `fadxsma` (case-insensitive) and for `pos_entry_adx` / `sma_long_48` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles KCD-ratio) trades an ADX-threshold-plus-SMA-cross two-sided machine with a shared ADX-collapse exit. ADX/SMA cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: when trend strength is high (ADX(14) above 30.0), buy the single bar where SMA(12) crosses up through SMA(48) and short the single bar where SMA(12) crosses down through SMA(48); when trend strength collapses (ADX(14) below 30.0), exit whichever side is held. A three-rung ROI ladder (`0.05` from open, `0.10` after 30 min, `0.075` after 60 min) and a fixed −5% stoploss backstop every position; trailing explicitly off. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Trend-strength-gated rotation machine, two-sided. The ADX leg supplies the regime (only trade rotations printed while the tape trends hard), while the SMA-cross leg supplies the timing (the exact rotation bar) and the side (up-cross = long, down-cross = short). The exit is deliberately regime-based rather than rotation-mirrored: EITHER side is abandoned the moment strength collapses below 30.0, even without an opposite cross — so a position opened on a valid cross is held through every high-ADX bar by design, including bars printing the opposite cross (held as no-ops under the position pin, never reversed). Unlike persistent-state records (trade every bar the condition holds), each entry leg can fire at most on its crossing bar — a book already positioned treats further bars as hold-no-ops until the shared collapse exit, an ROI rung, or the stop. The exit threshold equals the entry threshold with opposite strictness (`>` vs `<`), so the ADX == 30.0 knife-edge holds either book flat and firing nothing — disclosed, not smoothed.

## Signal

Exact rule as pinned (any other ADX/SMA periods, thresholds, strictness, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; ADX/SMA periods and the 30.0 gate are the file's pinned Parameter defaults (no dict override exists):

```text
adx[t]              = TA-Lib ADX(high, low, close, 14) // pinned default — no file override
sma12[t]            = TA-Lib SMA(close, 12)            // pinned default — no file override
sma48[t]            = TA-Lib SMA(close, 48)            // pinned default — no file override
enter_long  = (adx[t] > 30.0) AND crossed_above(sma12, sma48)[t]  // one-bar edge
enter_short = (adx[t] > 30.0) AND crossed_below(sma12, sma48)[t]  // one-bar edge
exit_any    = (adx[t] < 30.0)  // persistent collapse state, closes long AND short in full
risk        = ROI ladder {"0": 0.05, "30": 0.10, "60": 0.075} (fraction, by position age in minutes);
              fixed stop at -5% (stoploss -0.05); trailing explicitly OFF
floor       = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on a bar printing the up-cross edge under high ADX; `enter_short=1` on a bar printing the down-cross edge under high ADX; `exit_long=1` / `exit_short=1` on any bar printing the ADX-collapse state. Entries are one-bar edges, the exit is a persistent state — a positioned book exits on the FIRST collapse bar; a flat book treats collapse bars as no-ops.
- Exact boundaries (pinned semantics): the cross edges are strict on the decision bar (`sma12 > sma48` for long, `sma12 < sma48` for short) with inclusive previous-bar equality inside the standard edge; the ADX gate is strict on both sides (`> 30.0` entries, `< 30.0` exits) — a bar with `adx == 30.0` fires nothing on any leg; a bar with `sma12 == sma48` fires neither entry leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any long-entry bar has `sma12[t] > sma48[t]` while any short-entry bar has `sma12[t] < sma48[t]` — entries are mutually exclusive on every bar, degenerate or otherwise. Additionally every entry bar has `adx[t] > 30.0` while every exit bar has `adx[t] < 30.0` — entries and exits never co-print on any bar. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: two-sided, explicit. `can_short = True` ships in the file (never a default reading), and both `enter_short` and `exit_short` legs ship with mirrored construction — a long-only reading would contradict the file. The short leg requires a short-capable venue (see Crypto portability); the long leg expresses unchanged on spot.
- Exits and risk (explicit): the shared ADX-collapse exit, the three-rung ROI ladder, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). Trailing is explicitly OFF (`trailing_stop = False` plus disabled offsets — quoted absence, never armed). No time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further same-side entry edges AND opposite-side entry edges as hold-no-ops (no pyramiding, no averaging, no reversal — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying cross-edge bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (ADX smoothing plus SMA windows, fixed non-negative offsets, plus the standard one-bar edge lookback — no forward reference) with no `shift` call in the file body because the single lookback lives inside the standard `crossed_*` edge under the file's own framework contract (`process_only_new_candles = True` — file literal, not a default reading); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt value, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only (ADX on `high`/`low`/`close`; SMAs on `close`). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = "1h"`). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the one-bar edge lookback); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 50 one-hour bars held flat. Covers the 48-bar SMA(48) seed and the TA-Lib ADX(14) seed (~28 bars) with margin. The file ships `startup_candle_count = 14` — quoted source value, fenced in Negative evidence 1 as NOT adopted (it does not cover SMA48). Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, BinHV27, and MACDStrategy-crossed siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entries, the shared collapse exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing the collapse exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the ADXMomentum, AwesomeMacd, and BbandRsi records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add/no-reversal position pin from Signal, never presented as source-native behaviour. The house percentages partition the one admitted unit; they contribute no entry event of their own.
- Concurrency: at most one position per market at any time; the cross edge opens the full unit on a flat book (long on up-cross, short on down-cross); the shared collapse exit, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying cross-edge bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (130 lines: the four pinned Parameter defaults, the ADX/SMA indicator loop, the two `crossed_*` conjunct entries, the shared collapse exit for both sides, the `timeframe`/`minimal_roi`/`stoploss`/`can_short`/`trailing_stop` literals, and the `FAdxSmaStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The file's own `startup_candle_count = 14` does NOT cover the 48-bar SMA(48) seed, so the 50-bar record-rule floor governs instead — disclosed, not repaired. The `14` is quoted, never misattributed as sufficient.
2. Exact-touch rule fenced: the cross edges are strict on the decision bar while admitting previous-bar equality; the ADX gate is strict on BOTH sides (`>` entries, `<` exits) — a bar sitting exactly on 30.0 fires nothing on any leg (neither entry nor exit). Strictness preserved throughout — disclosed, not smoothed.
3. Dead-parameter fence: `pos_exit_adx` (DecimalParameter default 30.0, space sell) is defined once and read by zero order lines — both exits use `pos_entry_adx`. It plays no gating role, never repaired into a second threshold. Zero `buy_params`/`sell_params` dicts exist, so the four live defaults are the single value source.
4. Dead-import plumbing fenced: `numpy as np`, `pandas as pd`, `BooleanParameter`, and `CategoricalParameter` are imported and never referenced again in the 130 lines — display/plumbing leftovers with no gate effect, never repaired into a signal. The hyperopt-space loop (`for val in self.*.range`) computes unread columns for non-default periods — only `adx_14`, `sma_short_12`, and `sma_long_48` are read by any order line; the rest are dead columns, never repaired into extra legs.
5. Prose-vs-code fence: the file's header comment `This class is a sample` is prose — the coded legs are a complete deterministic rule (gated edges, shared exit, ROI, stop, explicit no-trailing, explicit `can_short`), so the record pins the code, never the modesty of the comment. The commented-out `# minimal_roi = {"0": 1}` is dead — the live three-rung ladder governs.
6. Wide-ladder fence: the ROI ladder is non-monotonic in time (`0.05` at open, `0.10` at 30 min, `0.075` at 60 min) — Freqtrade semantics apply the rung of the largest key at or under the elapsed minutes, verbatim. Coded fact, disclosed, not re-sorted or reinterpreted, not tightened by repair.
7. Cousin records fenced as different constructions (none trades an ADX-threshold-gated SMA12/48 cross edge, two-sided, with a shared ADX-collapse exit): the open PR #331 `AdxSmas` pool-candidate trades an SMA3/6 cross gated by ADX polarity state, long-flat, with a cross-down exit (different periods, different gate form, one-sided, ungated-permissive exit); the admitted `freqtrade-adx-momentum` pool-mate trades an ADX/DI/MOM four-conjunct persistent state with no SMA cross and no collapse exit; the admitted `adx-di-cross-strength-gated` pool-mate trades a DI-cross with no SMA leg; the admitted `freqtrade-hlhb` pool-mate trades an EMA-RSI-ADX quad gate with no cross edge and no shared exit; the `futures/TrendFollowingStrategy` sibling trades an EMA20 cross with OBV confirmation plus trailing stop (different indicators, trailing armed). Not a threshold re-tuning of any of them: moving any ADX/SMA period, dropping the ADX gate, converting either edge to a persistent state, mirroring the exit per-side, flipping any strictness, or changing any ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `AdxSmas.py`, `ADXMomentum.py`, `hlhb.py`, `TrendFollowingStrategy.py`, `FSupertrendStrategy.py`, `FOttStrategy.py`, `VolatilitySystem.py`, and all `berlinguyinca/*` files are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-reversal/no-cooldown position pin, the 50-bar warmup floor (the file ships only an insufficient `14`), the framework-default readings (`use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), the pinned Parameter-default readings (ADX 14, SMA 12/48, gate 30.0 — file defaults, never optimized values), the standard `crossed_*` one-bar edge semantics, and house sizing/costs — all predeclared above. The `1h` frame, the ADX-gated cross entries with all their literals and strictness, the shared collapse exit, the three-rung ROI ladder with the −5% stop, the explicitly disabled trailing, and the two-sided charter are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ADX(14) / SMA(12,48) / gated cross edges / `30.0` threshold with pinned strictness / one-bar-edge entries / shared collapse exit / three-rung ROI ladder / −5% stop / trailing OFF / single-unit two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — ADX-gate relevance: dropping the ADX legs (naked SMA12/48-cross edge both sides, collapse exit replaced by opposite-cross exit, same risk) must not improve net expectancy; fail ⇒ the trend-strength gate adds nothing over rotation timing.
- F2 — Rotation-timing relevance: dropping the cross edges (pure ADX-threshold state: long while `adx > 30`, flat while `adx < 30`, same risk) must not improve net expectancy; fail ⇒ the rotation edge adds nothing over the regime alone.
- F3 — Risk-ladder relevance: removing the ROI ladder/stop pair (collapse-only exits) must not improve net expectancy; fail ⇒ the three-rung ladder plus −5% backstop adds nothing over the bare gated machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Two-sided with full-unit open/close; the long leg expresses unchanged on a spot venue with no naked shorting, while the short leg requires a short-capable (perpetual) venue — disclosed, not assumed portable to spot. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent (ADXMomentum, AwesomeMacd, BbandRsi `1h`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose ADX never prints the collapse state is held until an ROI rung or the −5% stop; a market that oscillates ADX across 30.0 without a fresh cross prints repeated hold-no-ops with no flat state to rest in on the positioned side, while a flat book treats collapse bars as no-ops. There is no decay, chop, trend-loss, or further time exit — disclosed, not repaired.
- A positioned book that prints an opposite-side cross edge under high ADX holds without reversing by record rule — the reversal some venues might execute is explicitly NOT this version's behaviour.
- TA-Lib indicator internals (Wilder smoothing seeding, SMA seeding) and the standard `crossed_*` one-bar edge live in libraries outside the pinned file — pinned by call with periods 14/12/48 and gate 30.0, not re-derived; exact reproduction inherits those libraries' seeding alongside the 50-bar floor.
- The `Dict`/`List`/`reduce` plumbing and the dead `pos_exit_adx` / unread hyperopt-range columns are fenced — nothing further.
- No trailing, no breakeven, no cooldown — trailing explicitly disabled, the rest explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FAdxSmaStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
