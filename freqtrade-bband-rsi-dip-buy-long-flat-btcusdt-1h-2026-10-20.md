---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade BbandRsi band-dip RSI-conjunction long-flat on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BbandRsi.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade BbandRsi band-dip RSI-conjunction long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-combined-binh-cluc` and `td-sequential-setup9-perfected` records — this is only its third record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/BbandRsi.py`.
- GitHub blob SHA at the pinned commit: `addc87268affc2f3b1b00549f1ca8b119e41e655`, size 1854 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 1854 bytes, 64 lines, SHA-256 `65718e8d0c14094b67be82b66238ea60a4af4bbf6fd9a6e1879dad5c48125547`, identical to the GitHub blob (`git hash-object` reproduces `addc8726…1e655`) — the entire file was retrieved and inspected.
- Registration: the file defines class `BbandRsi(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with body/tail microstructure guards, pump cap, profit-gated midline exit, `5m`) and `berlinguyinca/ClucMay72018.py` (single discount leg under EMA50 with `0.985` band fraction and pump cap, `5m`) are different pins with different constants — this record pins ONLY the BbandRsi file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `author@: Gert Wohlgemuth`; `converted from: https://github.com/sthewissen/Mynt/blob/master/src/Mynt.Core/Strategies/BbandRsi.cs` (lineage note only — no line-level fact here comes from the Mynt file, which was never fetched); `INTERFACE_VERSION: int = 3`; `minimal_roi = { "0": 0.1 }`; `stoploss = -0.25`; `timeframe = '1h'`; indicators `ta.RSI(dataframe, timeperiod=14)` and `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)`; entry `(rsi < 30) & (close < bb_lowerband)`; exit `(rsi > 70)`. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (both resolved by name, both standard): `ta.RSI(dataframe, timeperiod=14)` (TA-Lib abstract RSI on closes, Wilder smoothing); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` returning the `lower`/`mid`/`upper` dict entries (typical price `(high+low+close)/3`, the Freqtrade vendor call pinned by call — its internal rolling arithmetic lives outside this file and is disclosed as such, never re-derived here). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 64 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `short` (no short leg anywhere); 1 `stoploss` (`-0.25`) and 1 `minimal_roi` (`{"0": 0.1}`) as the only risk legs; 0 `trailing` / 0 `startup_candle` / 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no volume read anywhere — the rule is pure price); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); `bb_middleband`/`bb_upperband` are computed but never read by any order line (display-only, fenced below).

Pre-write dedup (2026-10-20): working-tree filename/content search for `BbandRsi` / `bband` / `Wohlgemuth` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI) trades a Bollinger-RSI conjunction. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none trades an RSI(14) level AND typical-price BB(20, 2) lower-band dip conjunction, long-only, with a symmetric RSI overbought exit plus a single ROI/stop risk pair. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where short-horizon momentum is washed out (RSI under 30) AND the close sits under the typical-price Bollinger lower band (a band-penetration dip, not a mid-band drift); exit when momentum overheats (RSI over 70). A 10% ROI target and a −25% stoploss backstop every position. The file's only prose beyond authorship is the ROI comment (`adjust based on market conditions ... keep it low for quick turn arounds`) — a sizing hint, never a second trigger. No behavioural, structural, or risk-premium channel is claimed anywhere in the 64 lines. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Patient dip-buying machine with a two-key lock, long-only. Unlike pure-level RSI records (buy every sub-30 print), the band conjunction refuses washes that never broke structure — RSI can sit oversold inside a tight range for bars without printing an entry until price actually pierces the lower band. Unlike penetration records that demand microstructure proof (body displacement, tail, volume caps), this file asks only the penetration fact plus the RSI fact — two thresholds, no shape analysis. The shared exit is momentum-exhaustion discipline, not a reversal signal: the RSI-70 print banks overheating while losing positions ride to the wide −25% stop or the 10% ROI, so chop that oscillates between 30 and 70 without touching either extreme holds the book flat or holds the position. The coded consequence is a buyer of confirmed band-break weakness that harvests only measured overheating.

## Signal

Exact rule as pinned (any other RSI length, band window, multiplier, price basis, threshold, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
rsi14[t]      = TA-Lib RSI(close, 14)                       // Wilder smoothing
typ[t]        = (high[t] + low[t] + close[t]) / 3
bb_lower20[t] = qtpylib BB(20, 2) lower over typ             // mid/upper computed, never gated
entry         = (rsi14[t] < 30) AND (close[t] < bb_lower20[t])   // enter_long = 1
exit_sig      = (rsi14[t] > 70)                               // exit_long = 1
risk          = take-profit at +10% from entry (minimal_roi {"0": 0.1}); fixed stop at -25% (stoploss -0.25)
guard         = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar where both conjuncts print, `direction` long-only; `exit_long=1` on bars printing RSI above 70. The exit is a STATE-neutral level (while positioned above 70 it stays true every bar — close-and-hold-flat); the entry is a level that can reprint across consecutive bars while flat (no one-shot latch in code).
- Exact boundaries (pinned semantics): both entry conjuncts strict (`<` — RSI exactly 30 or a close exactly on the band fires nothing); the exit strict (`>` — RSI exactly 70 holds). Strictness preserved throughout — disclosed, not smoothed.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `rsi14[t] < 30` while any signal-exit bar has `rsi14[t] > 70` — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `enter_short`/`exit_short`/`short` tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the RSI-70 signal, the +10% ROI leg, and the −25% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying conjunction bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`close` for RSI and the band comparison, `high`/`low` inside typical price) with fixed non-negative offsets — no `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` for the RSI(14)/typical-price/BB(20) path and the band comparison. No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; both windows (14-bar RSI, 20-bar bands) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 25 one-hour bars held flat. Covers the 20-bar band seed, the 14-bar RSI seed, and all reads. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced CombinedBinHAndCluc and TDSequential siblings and the admitted Forven siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the RSI-70 signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (disclosed, not assumed): `1h` is the current campaign decision timeframe with extensive PASS precedent on `main` — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI/stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the conjunction opens the full unit on a flat book; the signal exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying conjunction bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (64 lines: the `ta.RSI(close, 14)` call, the typical-price BB(20, 2) block, the two-conjunct long entry, the RSI-70 exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `BbandRsi(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 25-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fire nothing on equality; RSI exactly 30, a close exactly on the band, or RSI exactly 70 all hold. Strictness preserved throughout — disclosed, not smoothed.
3. No-loss-cutting-signal fenced: an RSI-70 print is the only signal exit and it fires only on overheating — a position decaying sideways between 30 and 70 is held until ROI or the wide −25% stop. There is no trend-loss leg; the stop is the sole red-book guardrail — disclosed, not repaired.
4. Dead-band plumbing fenced: `bb_middleband`/`bb_upperband` are computed and never read by any order line — display-only, never triggers, never repaired into gates.
5. Zero-variance fenced: flat tape pins band width at 0 with bands on the mean; entry still needs RSI strictly under 30, which flat tape cannot print (RSI pins at 50/100 on zero-loss runs depending on implementation seeding — either way the conjunction is unreachable without a real decline). No division by zero exists anywhere (all gates are comparisons) — disclosed, not repaired.
6. No-volume fenced: the file reads zero volume — availability of the venue's candle volume is irrelevant to this rule; low-participation drift-throughs enter exactly like high-volume breaks. The absence is a coded fact, never a participation requirement — disclosed, not reinterpreted.
7. Cousin records fenced as different constructions (none trades an RSI-level AND typical-price-lower-band dip conjunction with a symmetric overbought exit and a single ROI/stop pair): the admitted chartart-bollinger-rsi sibling needs a same-bar joint RSI(6)-50 edge AND a 200-bar rail reclaim two-sided always-in (edges, not levels; 200-bar rails, not 20); the admitted forven-bollinger-s00120 sibling breaks the UPPER rail while RSI reads oversold (continuation breakout, opposite direction of trade); the admitted forven-bb-edge-fade-reclaim and forven-bb-squeeze-breakout siblings trade edge-fade and squeeze-release mechanics with different gates; the admitted alorse-kodify-bb350 sibling crosses a 350-period upper band with a midline exit but no RSI conjunction and no ROI/SL pair; the admitted rsi-classic sibling trades pure RSI 30/60 levels with no band anywhere and no risk legs; the admitted oversold-rsi-tight-sl sibling pairs RSI-30 with fixed −1%/+7% price levels and no band; the admitted forven-rsi-s00139 sibling needs an SMA-gated washout-cross edge with a dual overbought-or-trend-loss exit and no stop. Not a threshold re-tuning of any of them: moving the RSI length, softening the 30/70 pair, widening the band window, changing the price basis, or dropping the conjunction would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `CombinedBinHAndCluc.py` (dual penetration legs with microstructure fractions, pump cap, profit-gated midline exit, `5m`, ROI `0.05`) and `ClucMay72018.py` (single EMA50/`0.985`-discount leg with pump cap, `5m`, ROI `0.01`) are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 25-bar warmup floor, the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs — all predeclared above. The `1h` frame, the two-conjunct entry with both literals, the typical-price BB(20, 2) basis, the RSI-70 exit, the +10%/−25% risk pair, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: conjunction construction / RSI(14) / BB(20, 2, typical) / 30-70 pair / RSI-70 exit / +10% ROI / −25% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Band-conjunction relevance: dropping the lower-band conjunct (pure RSI<30 entry, same exit/risk) must not improve net expectancy; fail ⇒ the band-dip filter adds nothing over the bare RSI washout.
- F2 — Exit relevance: replacing the RSI-70 signal exit with midline reclaim (same entry/risk) must not improve net expectancy; fail ⇒ the overbought exit adds nothing over a band-state exit.
- F3 — Risk-pair relevance: removing the ROI/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the +10%/−25% backstop adds nothing over the bare signal machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume feed is required at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides extensive campaign precedent — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- The signal exit fires only on measured overheating; an engine that adds a trend-loss or time exit would trade a different, unpinned rule.
- qtpylib BB(20, 2)/typical-price internals live in the Freqtrade vendor module outside the pinned file — pinned by call, not re-derived; exact reproduction inherits that module's rolling semantics alongside TA-Lib's RSI seeding.
- TA-Lib RSI(14) seeding inherits the library's Wilder warmup; the 25-bar floor keeps early-bar instability out of trusted events.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BbandRsi.py
- https://github.com/freqtrade/freqtrade-strategies
