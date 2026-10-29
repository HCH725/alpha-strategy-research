---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AdxSmas ADX-gated SMA3/6 cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AdxSmas.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AdxSmas ADX-gated SMA3/6 cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-combined-binh-cluc` and `freqtrade-bband-rsi-dip-buy` records — this is only its third record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/AdxSmas.py`.
- GitHub blob SHA at the pinned commit: `5bc99c1c1e32b8c1dc12c265176b511f44cbc242`, size 1784 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 1784 bytes, 61 lines, SHA-256 `01356e36b3164b66aa4338a70f67f4bb887d4c79ae81b1bc2d1be5c5ba76fca5`, identical to the GitHub blob (`git hash-object` reproduces `5bc99c1c…cbc242`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AdxSmas(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/BbandRsi.py` (RSI-30 AND typical-price lower-band dip conjunction with RSI-70 exit, `1h`) and `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with body/tail microstructure guards, pump cap, profit-gated midline exit, `5m`) are different pins with different gates — this record pins ONLY the AdxSmas file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `author@: Gert Wohlgemuth`; `converted from: https://github.com/sthewissen/Mynt/blob/master/src/Mynt.Core/Strategies/AdxSmas.cs` (lineage note only — no line-level fact here comes from the Mynt file, which was never fetched); `INTERFACE_VERSION: int = 3`; `minimal_roi = { "0": 0.1 }`; `stoploss = -0.25`; `timeframe = '1h'`; indicators `ta.ADX(dataframe, timeperiod=14)`, `ta.SMA(dataframe, timeperiod=3)` (column `short`), `ta.SMA(dataframe, timeperiod=6)` (column `long`); entry `(adx > 25) & crossed_above(short, long)`; exit `(adx < 25) & crossed_above(long, short)`. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.ADX(dataframe, timeperiod=14)` (TA-Lib abstract ADX on high/low/close, Wilder smoothing); `ta.SMA(dataframe, timeperiod=3/6)` (TA-Lib abstract SMA on closes); `qtpylib.crossed_above(a, b)` (the Freqtrade vendor edge `a[t-1] <= b[t-1] AND a[t] > b[t]` over completed bars — pinned by call, its two-bar shift arithmetic lives outside this file and is disclosed as such, never re-derived here). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 61 lines this cycle): 1 `enter_long` and 1 `exit_long` as the only order legs; 0 `enter_short` / 0 `exit_short` / 0 `can_short` (no short leg anywhere — the 3 `short` tokens name the fast-SMA column `dataframe['short']`, never a position; likewise `long` names the slow-SMA column, fenced below); 1 `stoploss` (`-0.25`) and 1 `minimal_roi` (`{"0": 0.1}`) as the only risk legs; 0 `trailing` / 0 `startup_candle` / 0 `order_types` / 0 `order_time_in_force` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `process_only_new_candles` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no volume read anywhere — the rule is pure price/range); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic).

Pre-write dedup (2026-10-20): working-tree filename/content search for `AdxSmas` / `adx-sma` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI) trades an ADX-gated SMA cross. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none trades a fast-SMA(3)/slow-SMA(6) cross conjunction-gated by ADX(14) > 25 with a mirrored ADX < 25 AND reverse-cross exit, long-only, with a single ROI/stop risk pair. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where trend strength is confirmed (ADX over 25) AND the 3-bar average freshly crosses above the 6-bar average (a fast/slow momentum edge, not a level); exit only on the bar where strength has decayed (ADX under 25) AND the averages cross back the other way. A 10% ROI target and a −25% stoploss backstop every position. The file's only prose beyond authorship is the ROI comment (`adjust based on market conditions ... keep it low for quick turn arounds`) — a sizing hint, never a second trigger. No behavioural, structural, or risk-premium channel is claimed anywhere in the 61 lines. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Impatient trend-surfer with a two-key lock on both sides, long-only. Unlike plain-cross records (every fast/slow edge enters, including edges printed inside directionless chop), the ADX leg vetoes crosses fired in weak markets — entry needs strength AND the edge on the same bar. Unlike regime-filter records (a slow drift veto that stays permissive for months), the ADX veto is a fast strength state that can flip bar to bar. The mirrored exit is the coded consequence that bites: because the exit needs weakness AND the reverse edge jointly, a position opened under strong, aligned conditions can ride deep into decay — the reverse cross alone exits nothing while ADX holds above 25, and weak ADX alone exits nothing without the cross. Chop that oscillates without printing the joint exit holds the position until the wide −25% stop or the 10% ROI. The coded consequence is a buyer of confirmed fast-momentum edges under proven strength that surrenders only to confirmed joint surrender.

## Signal

Exact rule as pinned (any other average variant, period, ADX length, threshold, gate, exit leg, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
adx[t]        = TA-Lib ADX(high, low, close, 14)           // Wilder smoothing
sma3[t]       = SMA(close, 3)   // column `short`
sma6[t]       = SMA(close, 6)   // column `long`
edge_up       = crossed_above(sma3, sma6)  // sma3[t-1] <= sma6[t-1] AND sma3[t] > sma6[t]
edge_down     = crossed_above(sma6, sma3)  // mirror
entry         = (adx[t] > 25) AND edge_up                  // enter_long = 1
exit_sig      = (adx[t] < 25) AND edge_down                // exit_long = 1
risk          = take-profit at +10% from entry (minimal_roi {"0": 0.1}); fixed stop at -25% (stoploss -0.25)
guard         = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar where the strength gate and the up-edge co-print, `direction` long-only; `exit_long=1` on bars where the weakness gate and the down-edge co-print. The exit is a STATE-neutral conjunction (while positioned it stays true only on joint bars — close-and-hold-flat otherwise); the entry is a level-edge conjunction that can reprint across consecutive bars while flat (no one-shot latch in code).
- Exact boundaries (pinned semantics): both ADX gates strict (`>` / `<` — ADX exactly 25 fires neither leg, a joint dead zone that holds by code); both cross legs admit previous-bar equality (`<=`) but demand strict current-bar separation (`>`) per the vendor edge. Strictness preserved throughout — disclosed, not smoothed.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `adx[t] > 25` while any signal-exit bar has `adx[t] < 25` — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `enter_short`/`exit_short`/`can_short` tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The column names `short`/`long` name the 3/6-bar SMA columns only (fenced in Provenance census). The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the joint ADX-plus-reverse-cross signal, the +10% ROI leg, and the −25% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying joint bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`close` for both SMAs and the cross edges, `high`/`low`/`close` inside ADX) with fixed non-negative offsets — no `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `1h` bars of BTCUSDT: `close` (both SMAs, both cross edges) and `high`/`low` (directional-movement legs inside ADX) for the full path. No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; the ADX(14) window, both SMA windows, and the two-bar cross lookback read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 30 one-hour bars held flat. Covers the 6-bar SMA seed, the TA-Lib ADX(14) Wilder seeding chain (lookback `2*14-1 = 27`), and the cross edge's `t-1` read. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced CombinedBinHAndCluc and BbandRsi siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the joint signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (disclosed, not assumed): `1h` is the current campaign decision timeframe with extensive PASS precedent on `main` — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI/stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the joint entry opens the full unit on a flat book; the joint signal exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying joint bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (61 lines: the `ta.ADX(close, 14)` / `ta.SMA(close, 3)` / `ta.SMA(close, 6)` calls, the strength-gated up-cross long entry, the weakness-gated down-cross exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `AdxSmas(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 30-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict ADX gates fire nothing at exactly 25 on either side — a joint dead zone that holds by code; the vendor cross admits previous-bar equality but demands strict current-bar separation. Strictness preserved throughout — disclosed, not smoothed.
3. Joint-exit rarity fenced: the reverse cross alone exits nothing while ADX holds above 25, and weak ADX alone exits nothing without the down-edge — a decaying position with no joint bar rides until ROI or the wide −25% stop. There is no trend-loss or time leg; the stop is the sole red-book guardrail — disclosed, not repaired.
4. Column-name fence: `short`/`long` name the 3/6-bar SMA columns only (Provenance census) — no short position, short order, or short leg exists anywhere. A two-sided reading would contradict the file — disclosed, not reinterpreted.
5. Zero-variance fenced: flat tape pins ADX toward 0/NaN-seed and both SMAs on the mean; entry still needs a strict up-edge under ADX strictly over 25, unreachable without a real move. No division by zero exists anywhere (all gates are comparisons) — disclosed, not repaired.
6. No-volume fenced: the file reads zero volume — availability of the venue's candle volume is irrelevant to this rule; low-participation edges enter exactly like high-volume breaks. The absence is a coded fact, never a participation requirement — disclosed, not reinterpreted.
7. Cousin records fenced as different constructions (none trades a fast-SMA(3)/slow-SMA(6) cross conjunction-gated by ADX(14) > 25 with a mirrored ADX < 25 AND reverse-cross exit, long-only, with a single ROI/stop pair): the admitted forven-ema-cross-adx-regime sibling trades an EMA20/50 cross gated by ADX14 ≥ 20 PLUS a close-above-EMA200 regime leg with an unconditional cross-down exit and no risk legs (different average family, periods, gate set, exit, economics); the admitted golden-cross-sma-regime-gated sibling trades SMA 9/100/50 golden-cross mechanics with no ADX anywhere; the admitted eterna-sma-50-200 sibling trades a 50/200 SMA cross two-sided on `4h` with no ADX and no risk legs; the admitted adx-di-cross sibling trades DI-line crosses with an EMA50 regime filter two-sided on `1d` with a decay-constant exit — gate-sharing is not signal-sharing; the admitted forven-macd-cross-adx-regime sibling crosses a MACD signal line, not price averages. Not a threshold re-tuning of any of them: moving either SMA period, the ADX length, either threshold, the strictness, the exit conjunction, or the direction handling would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `BbandRsi.py` (RSI-30 AND typical-price lower-band dip with RSI-70 exit, `1h`, ROI `0.1`) and `CombinedBinHAndCluc.py` (dual penetration legs with microstructure fractions, pump cap, profit-gated midline exit, `5m`, ROI `0.05`) are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 30-bar warmup floor, the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs — all predeclared above. The `1h` frame, the SMA(3)/SMA(6) pair, the ADX(14) 25-pair gates, the mirrored joint exit, the +10%/−25% risk pair, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA(3)/SMA(6) pair / ADX(14) / 25-pair gates / mirrored joint exit / +10% ROI / −25% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Strength-gate relevance: dropping the ADX conjunct on entry (pure SMA3/6 cross entry, same exit/risk) must not improve net expectancy; fail ⇒ the ADX > 25 filter adds nothing over the bare cross.
- F2 — Joint-exit relevance: replacing the mirrored joint exit with an unconditional down-cross exit (same entry/risk) must not improve net expectancy; fail ⇒ the ADX < 25 exit conjunct adds nothing over the bare cross exit.
- F3 — Risk-pair relevance: removing the ROI/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the +10%/−25% backstop adds nothing over the bare joint machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume feed is required at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides extensive campaign precedent — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- The joint exit fires only on confirmed joint surrender; an engine that exits on the bare reverse cross or on weak ADX alone would trade a different, unpinned rule.
- qtpylib `crossed_above` internals live in the Freqtrade vendor module outside the pinned file — pinned by call, not re-derived; exact reproduction inherits that module's two-bar edge semantics alongside TA-Lib's Wilder ADX seeding.
- TA-Lib ADX(14)/SMA seeding inherits the library's warmup; the 30-bar floor keeps early-bar instability out of trusted events.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AdxSmas.py
- https://github.com/freqtrade/freqtrade-strategies
