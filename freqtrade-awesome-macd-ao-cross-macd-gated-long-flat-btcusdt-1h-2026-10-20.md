---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade AwesomeMacd AO-cross MACD-gated long-flat on BTCUSDT 1h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AwesomeMacd.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AwesomeMacd AO-cross MACD-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same repository that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, and `td-sequential-setup9-perfected` records — this is only its fourth record).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/AwesomeMacd.py`.
- GitHub blob SHA at the pinned commit: `4ccc85dca00d1fb8dd140faa54720c98adf317b0`, size 1935 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 1935 bytes, 67 lines, SHA-256 `8872b23514791b1e81a67e9d486e4efdd20fc08732ee5c0bf87312a82ff8a4c7`, identical to the GitHub blob (`git hash-object` reproduces `4ccc85dc…f317b0`) — the entire file was retrieved and inspected.
- Registration: the file defines class `AwesomeMacd(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `berlinguyinca/BbandRsi.py` (RSI(14) level AND typical-price BB(20, 2) dip conjunction, `1h`) and `berlinguyinca/CombinedBinHAndCluc.py` (dual-leg BB-penetration with microstructure guards, `5m`) are different pins with different gates — this record pins ONLY the AwesomeMacd file's literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `author@: Gert Wohlgemuth`; `converted from: https://github.com/sthewissen/Mynt/blob/master/src/Mynt.Core/Strategies/AwesomeMacd.cs` (lineage note only — no line-level fact here comes from the Mynt file, which was never fetched); `INTERFACE_VERSION: int = 3`; `minimal_roi = { "0": 0.1 }`; `stoploss = -0.25`; `timeframe = '1h'`; indicators `ta.ADX(dataframe, timeperiod=14)`, `qtpylib.awesome_oscillator(dataframe)`, and `ta.MACD(dataframe)` (defaults); entry `(macd > 0) & (ao > 0) & (ao.shift() < 0)`; exit `(macd < 0) & (ao < 0) & (ao.shift() > 0)`. No `trailing`, no `startup_candle_count`, no `use_exit_signal` / `exit_profit_only` override, no `can_short`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.MACD(dataframe)` (TA-Lib abstract MACD on closes, default fastperiod 12 / slowperiod 26 / signalperiod 9, exposing `macd`/`macdsignal`/`macdhist`); `qtpylib.awesome_oscillator(dataframe)` (Bill Williams Awesome Oscillator — the Freqtrade vendor call pinned by call; its internal median-price SMA(5)-SMA(34) arithmetic lives outside this file and is disclosed as such, never re-derived here); `ta.ADX(dataframe, timeperiod=14)` (TA-Lib abstract ADX on HLC, Wilder smoothing — computed into `dataframe['adx']` and never read by any order line, fenced below). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 67 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `short` (case-insensitive — no short leg anywhere); 1 `stoploss` (`-0.25`) and 1 `minimal_roi` (`{"0": 0.1}`) as the only risk legs; 0 `trailing` / 0 `startup_candle` / 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `volume` (no volume read anywhere — the rule is pure price); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); `macdsignal`/`macdhist`/`adx` are computed but never read by any order line (display/plumbing-only, fenced below).

Pre-write dedup (2026-10-20): working-tree filename/content search for `AwesomeMacd` / `awesome-macd` / `Wohlgemuth` returns zero strategy records. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades an AO-cross/MACD-polarity conjunction. The pool's nearest cousins are fenced as different constructions in Negative evidence 7 — none trades a Bill Williams AO zero-cross-up edge gated by positive MACD polarity, long-only, with a mirrored MACD-negative AO-cross-down exit plus a single ROI/stop risk pair. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where the Awesome Oscillator crosses up through zero (prior bar negative, current bar positive) while MACD polarity confirms the bullish half (MACD above zero) — a momentum-spread reclaim that refuses zero-crosses printed against a negative MACD; exit the mirror (AO crosses down through zero while MACD sits below zero). A 10% ROI target and a −25% stoploss backstop every position. The file's only prose beyond authorship is the ROI comment (`adjust based on market conditions ... keep it low for quick turn arounds`) — a sizing hint, never a second trigger. No behavioural, structural, or risk-premium channel is claimed anywhere in the 67 lines. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Patient momentum-confirmation machine with a two-key lock, long-only. Unlike bare AO records (fire every zero-cross both ways), the MACD-polarity gate refuses reclaim crosses printed while the slower MACD still reads bearish — the AO edge must agree with the MACD half. Unlike pure MACD-cross records (trade the MACD/signal edge itself), the traded edge here is the AO's zero crossing; MACD is a bouncer, never the trigger — `macdsignal` is computed and never gated. The mirrored exit is polarity-symmetric discipline, not a reversal signal: the AO-cross-down print banks only while MACD confirms the bearish half, so chop that wiggles AO around zero without MACD leaving its half holds the book flat or holds the position. The coded consequence is a buyer of polarity-confirmed momentum reclaims that harvests only polarity-confirmed fades.

## Signal

Exact rule as pinned (any other MACD periods, AO construction, polarity side, shift lookback, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
macd[t]       = TA-Lib MACD(close, 12, 26, 9)               // default periods
ao[t]         = qtpylib.awesome_oscillator                   // vendor AO
entry         = (macd[t] > 0) AND (ao[t] > 0) AND (ao[t-1] < 0)   // enter_long = 1
exit_sig      = (macd[t] < 0) AND (ao[t] < 0) AND (ao[t-1] > 0)   // exit_long = 1
risk          = take-profit at +10% from entry (minimal_roi {"0": 0.1}); fixed stop at -25% (stoploss -0.25)
guard         = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the AO-cross-up edge inside positive MACD polarity, `direction` long-only; `exit_long=1` on bars printing the mirrored cross-down edge inside negative MACD polarity. Each edge prints on exactly one bar (strict sign flip across one shift) — the exit is a one-bar event, not a holding level; the entry edge likewise re-arms only on a fresh flip.
- Exact boundaries (pinned semantics): all four comparisons strict (`>`/`<` — MACD exactly 0, AO exactly 0, or prior AO exactly 0 fires nothing on that conjunct). Strictness preserved throughout — disclosed, not smoothed.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `macd[t] > 0` while any signal-exit bar has `macd[t] < 0` — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `enter_short`/`exit_short`/`short` tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the mirrored AO/MACD signal, the +10% ROI leg, and the −25% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying edge bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`close` for MACD, vendor HLC-median inside AO) with fixed non-negative offsets (`t`, `t-1`) — no `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` for the MACD(12, 26, 9)/AO path and the polarity comparisons. No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = '1h'`). One evaluation per completed bar; the MACD seed, the AO vendor seed, and the one-bar shift all read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 one-hour bars held flat. Covers the AO vendor seed (SMA-34 leg), the MACD EMA-26 plus 9-bar signal seed, the ADX(14) Wilder seed, and the one-bar shift read. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced CombinedBinHAndCluc, BbandRsi, and TDSequential siblings and the admitted Forven siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the mirrored signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (disclosed, not assumed): `1h` is the current campaign decision timeframe with extensive PASS precedent on `main` — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI/stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the edge opens the full unit on a flat book; the mirrored signal exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying edge bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (67 lines: the `ta.MACD(close)` call, the `qtpylib.awesome_oscillator` block, the ADX(14) computation, the polarity-gated AO-edge long entry, the mirrored exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `AwesomeMacd(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>`/`<` fire nothing on equality; MACD exactly 0, AO exactly 0, or prior AO exactly 0 each veto their conjunct. Strictness preserved throughout — disclosed, not smoothed.
3. No-loss-cutting-signal fenced: the mirrored edge is the only signal exit and it fires only on a polarity-confirmed fade — a position decaying sideways (AO pinned positive without a fresh flip, or MACD pinned positive) is held until ROI or the wide −25% stop. There is no trend-loss leg; the stop is the sole red-book guardrail — disclosed, not repaired.
4. Dead-column plumbing fenced: `macdsignal`/`macdhist`/`adx` are computed and never read by any order line — plumbing/display-only, never triggers, never repaired into gates. In particular the ADX(14) column is a decoy: no ADX threshold, cross, or regime appears in either order leg — disclosed, not reinterpreted as a strength filter.
5. Zero-variance fenced: flat tape pins AO at 0 with no strict sign flip, so the edge is unreachable without a real oscillation (AO exactly 0 vetoes both the current-bar and prior-bar conjuncts). No division by zero exists anywhere (all gates are comparisons) — disclosed, not repaired.
6. No-volume fenced: the file reads zero volume — availability of the venue's candle volume is irrelevant to this rule; low-participation wiggles enter exactly like high-volume reclaims. The absence is a coded fact, never a participation requirement — disclosed, not reinterpreted.
7. Cousin records fenced as different constructions (none trades an AO zero-cross edge gated by MACD polarity, long-only, with a mirrored polarity exit and a single ROI/stop pair): the admitted awesome-oscillator sibling fires every bare AO zero-cross both ways with opposite-cross exits, no polarity gate, no risk legs, `4h` (always-in reversal, opposite book); the admitted ac-accelerator sibling trades the AO-minus-SMA5 residual's bar-to-bar rise/fall, never a zero-cross; the admitted forven-macd-cross-adx-regime sibling crosses the MACD/signal lines themselves under an ADX regime (the crossed quantity differs — signal line, not zero — and the gate is ADX, not MACD polarity); the admitted macd-signal-cross-reversal sibling trades the bare MACD/signal cross two-sided with no AO anywhere; the admitted waddah-attar-explosion-macd-bb-deadzone sibling conjoins MACD with Bollinger deadzone geometry (no AO edge); the admitted BbandRsi pool-mate conjoins RSI(14) levels with BB dips (no MACD, no AO). Not a threshold re-tuning of any of them: moving the MACD periods, changing the AO construction, dropping the polarity gate, flipping a side, or touching the ROI/stop pair would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `BbandRsi.py` (RSI/BB conjunction, `1h`, ROI `0.1`) and `CombinedBinHAndCluc.py` (dual penetration legs with microstructure fractions, `5m`, ROI `0.05`) are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the single-unit/no-add/no-cooldown position pin, the 40-bar warmup floor, the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs — all predeclared above. The `1h` frame, the AO-cross-up/MACD-positive entry with all four literals, the vendor AO basis, the mirrored exit, the +10%/−25% risk pair, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: AO-edge/MACD-polarity conjunction / default MACD(12, 26, 9) / vendor AO / strict edges / mirrored exit / +10% ROI / −25% stop / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Polarity-gate relevance: dropping the MACD conjuncts (bare AO-cross-up entry, bare AO-cross-down exit, same risk) must not improve net expectancy; fail ⇒ the MACD-polarity gate adds nothing over the bare AO edge.
- F2 — Exit relevance: replacing the mirrored exit with MACD-polarity loss (exit when `macd < 0` regardless of AO edge, same entry/risk) must not improve net expectancy; fail ⇒ the AO-edge exit adds nothing over a polarity-state exit.
- F3 — Risk-pair relevance: removing the ROI/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the +10%/−25% backstop adds nothing over the bare signal machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. No volume feed is required at all. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides extensive campaign precedent — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- The signal exit fires only on a polarity-confirmed fade edge; an engine that adds a trend-loss or time exit would trade a different, unpinned rule.
- qtpylib `awesome_oscillator` internals live in the Freqtrade vendor module outside the pinned file — pinned by call, not re-derived; exact reproduction inherits that module's rolling semantics alongside TA-Lib's MACD/ADX seeding.
- TA-Lib MACD/ADX seeding inherits the library's EMA/Wilder warmup; the 40-bar floor keeps early-bar instability out of trusted events.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The ADX(14) column is computed and gated nowhere — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AwesomeMacd.py
- https://github.com/freqtrade/freqtrade-strategies
