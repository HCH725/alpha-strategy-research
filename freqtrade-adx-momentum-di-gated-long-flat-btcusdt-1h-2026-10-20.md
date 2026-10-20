---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade ADXMomentum ADX-DI-momentum-gated long-flat on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/ADXMomentum.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade ADXMomentum ADX-DI-momentum-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, and `freqtrade-emaskippump` records — this is only its sixth record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/ADXMomentum.py`.
- GitHub blob SHA at the pinned commit: `2ac48debd8449d6b36220f0d6b4e3df300e79fe0`, size 2137 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2137 bytes, 69 lines, SHA-256 `7ed9c2306f337a1cc49cb2e11ddf6b66397853b9c4155faa13e5cf1ea61a651a`, identical to the GitHub blob (`git hash-object` reproduces `2ac48deb…e79fe0`) — the entire file was retrieved and inspected.
- Registration: the file defines class `ADXMomentum(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/AdxSmas.py` (SMA3/6 cross gated by ADX polarity, `1h`, open PR #331), `berlinguyinca/AwesomeMacd.py` (AO-cross gated by MACD polarity, `1h`), `berlinguyinca/BbandRsi.py` (RSI(14) level AND typical-price BB(20, 2) dip conjunction, `1h`), `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards, `5m`), and `berlinguyinca/EMASkipPump.py` (EMA-stack dip with MIN/MAX extremes, typical-price rails, and volume veto, `5m`) are different pins with different gates — this record pins ONLY the ADXMomentum file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `INTERFACE_VERSION: int = 3`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.25`; `timeframe = '1h'`; `startup_candle_count: int = 20`; class docstring `author@: Gert Wohlgemuth` / `converted from: https://github.com/sthewissen/Mynt/blob/master/src/Mynt.Core/Strategies/AdxMomentum.cs`; indicators `ta.ADX(dataframe, timeperiod=14)`, `ta.PLUS_DI(dataframe, timeperiod=25)`, `ta.MINUS_DI(dataframe, timeperiod=25)`, `ta.SAR(dataframe)`, `ta.MOM(dataframe, timeperiod=14)`; entry `adx > 25 & mom > 0 & plus_di > 25 & plus_di > minus_di` (`enter_long = 1`); exit `adx > 25 & mom < 0 & minus_di > 25 & plus_di < minus_di` (`exit_long = 1`). No `trailing`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.ADX` / `ta.PLUS_DI` / `ta.MINUS_DI` (Wilder TA-Lib trend-strength/directional system on high/low/close, fixed periods 14/25/25); `ta.MOM` (TA-Lib momentum `close[t] − close[t−14]`, fixed period 14); `ta.SAR` (TA-Lib parabolic SAR with library defaults, computed and never read by any order line — fenced below). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 69 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 1 `stoploss` (`-0.25`) and 1 `minimal_roi` (`{"0": 0.01}`) as the only risk legs; 0 shipped `trailing`; 1 `startup_candle_count` (`20`, file literal — the record's stricter 60-bar floor is a predeclared researcher pin, never a file semantic); 1 `sar` (indicator plumbing only, never an order gate); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no volume read anywhere); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic).

Pre-write dedup (2026-10-20): working-tree filename/content search for `ADXMomentum` / `AdxMomentum` / `adx-momentum` / `plus_di` returns zero strategy records — no record in the pool reads TA-Lib `PLUS_DI`/`MINUS_DI` at all, and the only `MOM(` hit pool-wide is the unrelated monthly time-series-momentum record. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross) trades an ADX-plus-directional-dominance-plus-momentum conjunction. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none conjoins single-bar ADX(14) strength, ±DI(25) dominance with level gates, and TA-Lib MOM(14) polarity into a long entry with a mirrored momentum-flipped exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: hold long only while trend strength (ADX(14) above 25) coincides with upward directional dominance (PLUS_DI(25) above 25 and above MINUS_DI) and positive 14-bar momentum; exit the mirror (ADX still above 25, now downward dominance with MINUS_DI above 25 and negative momentum). A 1% ROI target and a −25% stoploss backstop every position; the file recommends keeping ROI low for quick turnarounds. Converted from the Mynt `AdxMomentum` C# strategy. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Trend-with-receipts machine, long-only. Unlike bare ADX-threshold records (fire on strength alone, direction-agnostic), both legs demand a signed directional verdict: the winning DI line must both clear its own 25 level AND lead its rival, so directionless high-ADX chop with tangled DI lines prints nothing. Unlike DI-cross records (trade the cross edge), no cross is ever traded: both entry and exit are state prints re-evaluated per bar, never a one-bar edge. The MOM(14) polarity clause is the second witness — a bar where price sits inside an upward DI stack but 14-bar momentum has already rolled negative cannot arm entry, and symmetrically a long is surrendered the first bar momentum flips negative inside a downward DI stack. The shared ADX>25 clause on both legs means exits fire only inside still-strong trends; a trend that merely decays (ADX sliding under 25 with no directional flip) is held until ROI or the −25% stop.

## Signal

Exact rule as pinned (any other ADX/DI/MOM period, level gate, risk pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
adx[t]      = TA-Lib ADX(high, low, close, 14)
plus_di[t]  = TA-Lib PLUS_DI(high, low, close, 25)
minus_di[t] = TA-Lib MINUS_DI(high, low, close, 25)
mom[t]      = TA-Lib MOM(close, 14)            // close[t] − close[t−14]
sar[t]      = TA-Lib SAR(high, low)            // computed, never read — fenced
entry       = (adx[t] > 25) AND (mom[t] > 0) AND (plus_di[t] > 25)
              AND (plus_di[t] > minus_di[t])   // enter_long = 1
exit_sig    = (adx[t] > 25) AND (mom[t] < 0) AND (minus_di[t] > 25)
              AND (plus_di[t] < minus_di[t])   // exit_long = 1
risk        = take-profit at +1% from entry (minimal_roi {"0": 0.01}); fixed stop at -25% (stoploss -0.25)
floor       = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the four-conjunct uptrend state, `direction` long-only; `exit_long=1` on bars printing the four-conjunct downtrend state. Each print is a state print re-evaluated per bar, not a one-bar edge — a book already positioned treats further entry bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): all four legs strict (`>`, `<`) — a bar with `adx == 25`, `mom == 0`, a DI exactly on 25, or `plus_di == minus_di` fires neither leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `mom[t] > 0` AND `plus_di[t] > minus_di[t]` while any signal-exit bar has `mom[t] < 0` AND `plus_di[t] < minus_di[t]` — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirrored downtrend-state signal, the +1% ROI leg, and the −25% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying uptrend-state bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`high`/`low` for ADX/DI/SAR, `close` for MOM) with fixed non-negative offsets (trailing windows only, no shift at all) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` for the ADX(14)/±DI(25)/SAR path and `close` for the MOM(14) path. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 one-hour bars held flat. Covers the ±DI(25) Wilder seeding (the longest window — TA-Lib directionals need roughly twice their period to stabilize), the ADX(14) stack, the MOM(14) back-read, and the SAR seed. The file's own `startup_candle_count = 20` is quoted verbatim above and deliberately superseded by this stricter floor — disclosed, not misattributed. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, and EMASkipPump siblings and the open-PRs AdxSmas sibling (`1h`, the direct interval sibling from this same file family) use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirrored signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar signal fill order, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the BbandRsi and AwesomeMacd records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI/stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the uptrend state opens the full unit on a flat book; the mirrored downtrend-state exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying uptrend-state bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (69 lines: the ADX(14)/±DI(25)/SAR/MOM(14) calls, the four-conjunct long entry, the mirrored four-conjunct exit, the `timeframe`/`minimal_roi`/`stoploss`/`startup_candle_count` literals, and the `ADXMomentum(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file's own `startup_candle_count = 20` is superseded, never silently adopted.
2. Exact-touch rule fenced: every leg is strict (`>`/`<`) — `adx == 25`, `mom == 0`, DI-on-25, and DI-equality bars fire nothing on either side. Strictness preserved throughout — disclosed, not smoothed.
3. Dead-column plumbing fenced: `sar` is computed and never read by any order line — plumbing/display-only, never a trailing-stop proxy, never repaired into a gate.
4. Decay-hold fenced: a trend that weakens (ADX sliding under 25) without printing the mirrored downtrend state holds the position until ROI or the −25% stop — there is no ADX-decay exit leg in the file. Disclosed, not repaired.
5. Stop-distance fence: the −25% stop is far below the +1% ROI by construction (quick-turnaround design per the file comment) — deep adverse excursions are held, not cut early. Coded fact, disclosed, not reinterpreted as a tight risk regime.
6. No-volume fence: the file reads no `volume` anywhere — thin-tape bars gate exactly like busy ones. Disclosed, not reinterpreted as a liquidity requirement.
7. Cousin records fenced as different constructions (none conjoins single-bar ADX strength, ±DI dominance with level gates, and MOM polarity): the open-PR AdxSmas pool-neighbour trades an SMA3/6 cross edge behind an ADX-polarity gate (cross vs state, no DI lines, no MOM); the admitted AwesomeMacd pool-mate trades AO-cross edges gated by MACD polarity (no ADX, no DI, no MOM); the admitted `adx-di-cross-strength-gated-two-sided` pool-mate fires on a ±DI cross behind a strength gate, two-sided (edge vs state, no MOM, opposite direction scope); the admitted `forven-adx-trend-pulse-reclaim` sibling enters on an EMA21 reclaim edge inside an ADX-regime window (reclaim edge vs state print, no DI lines, no MOM); the admitted `alorse-dmi-winner` sibling demands three consecutive DI-dominance bars plus ADX>23, EMA55, and candle colour (triple-bar pattern vs single-bar state, different DI/ADX lengths, no MOM). Not a threshold re-tuning of any of them: moving any period, any of the three 25 levels, the MOM polarity, the ROI/stop pair, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `AdxSmas.py`, `AwesomeMacd.py`, `BbandRsi.py`, `CombinedBinHAndCluc.py`, and `EMASkipPump.py` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 60-bar warmup floor (stricter than the file's 20), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs — all predeclared above. The `1h` frame, the four-conjunct entry with all its literals, the mirrored four-conjunct exit, the +1%/−25% risk pair, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ADX(14)/±DI(25)/MOM(14) / triple-25 gates / mirrored state exit / +1% ROI / −25% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Directional-dominance relevance: dropping the DI clauses (pure ADX>25 AND MOM-polarity states, same exit mirror/risk) must not improve net expectancy; fail ⇒ the ±DI dominance gates add nothing over strength-plus-momentum.
- F2 — Momentum-witness relevance: dropping the MOM polarity clauses (pure ADX>25 AND DI-dominance states, same exit mirror/risk) must not improve net expectancy; fail ⇒ the MOM witness adds nothing over ADX-plus-directionals.
- F3 — Risk-pair relevance: removing the ROI/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the +1%/−25% backstop adds nothing over the bare state machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume or exotic feed is read. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent (BbandRsi, AwesomeMacd) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a decaying trend (ADX under 25, no mirrored print) is held until ROI or the −25% stop; a position in directionless high-ADX chop (tangled DI lines, whipping MOM) likewise sits until risk legs resolve it. There is no decay, chop, trend-loss, or time exit — disclosed, not repaired.
- TA-Lib Wilder smoothing/seed internals live in the library outside the pinned file — pinned by call (fixed periods 14/25/25/14), not re-derived; exact reproduction inherits that library's seeding alongside the 60-bar floor.
- The SAR column is computed and gated nowhere — nothing further to fence.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/ADXMomentum.py
- https://github.com/freqtrade/freqtrade-strategies
