---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven MFI threshold-cross long-flat on BTCUSDT 1h bars
created: 2026-10-19
updated: 2026-10-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/mfi.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven MFI threshold-cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, `forven-bb-edge-fade-reclaim`, `forven-rsi-s00139-washout-cross`, and `forven-obv-ema-cross-sma-gated` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T13:50:18-03:00`; verified as the repository HEAD via `git ls-remote` and a full shallow clone during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/mfi.py`.
- GitHub blob SHA at the pinned commit: `08352d3d61e6f45981c843e39e06b5cf3cc3b05f`, size 3163 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit and from the clone at the pinned HEAD is 3163 bytes, 117 lines, SHA-256 `fe6ea70a3879b48fd22433ba27dd8980e0ebc4da2d9b592a4f22cb3b1d87a24d`, identical to the GitHub blob (`git hash-object` reproduces `08352d3d…b05f`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = MFIStrategy` and the `STRATEGIES = [("PREBUILT-MFI", MFIStrategy, {"_asset": "BTC"})]` roster pin. This record pins the `PREBUILT-MFI` roster leg. Repo-wide search for `MFIStrategy` / `PREBUILT-MFI` / `builtin/mfi` returns this file only for signal logic — identity is unique (the only other `mfi` hits are the framework's `params.py` category/allowlist lines, which name the family and its accepted keys but contain no decision logic).
- The file's own words (quoted for gate evidence, never extended): module docstring `MFI (Money Flow Index) strategy.` with `Entry: MFI crosses above oversold level` and `Exit: MFI crosses below overbought level`; class docstring `MFI = 100 - (100 / (1 + positive_flow / negative_flow))` with `Entry when MFI crosses above oversold; exit when MFI crosses below overbought.`; `default_params` returns exactly `{ "mfi_period": 14, "oversold": 20, "overbought": 80, "leverage": 1.0 }`; `describe()` returns `Enters when MFI(14) crosses above 20. Exits when MFI crosses below 80.` No performance phrase of any kind ships anywhere in the 117 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path (verified by `def` census): the file defines one signal method, `generate_signal()` — no `generate_signals` vectorized twin exists anywhere in the file, no scalar delegate, no second decision logic exists to diverge. The `confidence` value (`min(1.0, (curr_mfi - 20) / 20.0)` on entry bars, else `0.0`) and the `indicators` dict (`mfi`, `prev_mfi`) are diagnostic echoes — none ever enters any predicate.
- No out-of-file indicator imports: MFI is computed inline with pandas over passed frames (typical price `(high + low + close) / 3`, raw money flow `tp * volume`, signed rolling sums, the bounded ratio) — all in-file pandas over passed frames (no DB, no network, no global state, no `forven.strategies.indicators` facade, no `scanner` import). The only local import is the `BaseStrategy, Signal` base. No facade, no scanner passenger, no hidden arithmetic variant exists to pin.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-obv-ema-cross-sma-gated`, `forven-bb-edge-fade-reclaim` and `forven-rsi-s00139-washout-cross` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` normalization of both flags and the direction literal. The base further pins `supported_trade_modes == {"long_only"}` and `mirror_short_safe == False` — the long-only lane below is the class's own declared posture, not a researcher reinterpretation.
- Full-file token census (verified by search over the 117 lines this cycle): 2 `direction="long"` literals and zero `short` / zero `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line; 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `open` column reads anywhere. The order-gating path reads exactly four columns: `high`, `low`, `close`, `volume`.
- Param fence (verified in `params.py` at the pinned commit): the framework allowlist names `mfi` with accepted keys `{"mfi_period", "oversold", "overbought"}`. The predicate below reads only those three keys (all present in defaults); no alias keys exist to re-wire lengths through — treating any other key as live would be a different, unpinned rule.

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/mfi` / `MFIStrategy` / `PREBUILT-MFI` returns zero strategy records citing this source file. No closed `research/*` PR ever carried this file (merged Scout PRs #261–297 are WorldQuant/PVI/Mayer/PGO plus twenty-seven Forven files through OBV #297). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. The pool's nearest money-flow neighbours are fenced as different constructions in Negative evidence 8 — none trades pure 14-bar money-flow-index threshold-crosses (20 up / 80 down), long-only, signal-exits-only, on `1h` bars from this file. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Money Flow Index volume-weighted RSI strategy` that buys when volume-weighted buying pressure crosses back up out of oversold and exits when it crosses back down out of overbought. No behavioural, structural, or risk-premium channel is claimed anywhere in the 117 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Exhaustion-reclaim machine with a volume truth serum, long-only, edge-triggered both legs. Unlike price-only RSI records (S00139 washout, connors, ema-rsi-pullback: averages of close-changes blind to participation), this system never fires on a price wiggle alone: the MFI leg requires dollar-flow (typical-price-signed volume accumulated over 14 bars) to have actually reclaimed the 20 line, so selloffs on collapsing participation that still print low RSI prints nothing here. Unlike the pool's ATR-scaled OBV record (volume-squared-over-ATR cum) or the ADL/Chaikin flow records (range-position-weighted flows), this system weights every bar's full dollar volume by the sign of its typical-price change (up-bar full weight to positive flow, down-bar full weight to negative flow, flat-bar to neither) and bounds the ratio to 0–100 — a steady drip of small up-dollar days drags the line just as a single spike does, while a high-volume doji contributes nothing to either side. The coded consequence is a patient participation buyer: entries print only on bars where dollar-flow proves itself reclaimed from oversold, and every position ends on a single overbought-failure edge with no stop to second-guess it.

## Signal

Exact rule as pinned (any other MFI construction, period, threshold, strictness, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path is the single source of truth:

```text
tp[t]       = (high[t] + low[t] + close[t]) / 3
raw_mf[t]   = tp[t] * volume[t]
pos_flow[t] = sum(raw_mf[i] for i in t-13..t where tp[i] > tp[i-1])
neg_flow[t] = sum(raw_mf[i] for i in t-13..t where tp[i] < tp[i-1])
mfi[t]      = 100 - (100 / (1 + pos_flow[t] / max(neg_flow[t], 1e-10)))
entry       = (mfi[t-1] <= 20) AND (mfi[t] > 20)
exit_       = (mfi[t-1] >= 80) AND (mfi[t] < 80)
guard       = len(df) < 17 -> flat/flat by coded rule (see Required data)
```

- Trade events: `entry_signal=True` with `direction="long"` on reclaim bars; otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. Both legs are EDGES (fire only on the cross bar) — there is no level-hold leg anywhere: a book parked above 20 without a fresh cross holds, it does not re-enter; a book parked below 80 without a fresh cross holds, it does not re-exit.
- Exact boundaries (pinned semantics): both crosses admit equality on the prior bar (`<=` / `>=`) but demand strict inequality on the current bar (`>` / `<`) — a print landing exactly on its threshold fires nothing. Flat-TP bars (`tp[i] == tp[i-1]`) contribute to neither flow sum by construction (both `where` predicates strict). At zero variance (all-equal typical prices, all-zero volumes) both flows pin at zero, `neg_flow` is floored to `1e-10`, MFI pins at `0.0` — strictness makes entry (`0 > 20` false) and exit (`0 >= 80` false) both false by construction (fenced, not repaired).
- Both-legs coexistence (coded, no researcher ordering needed): entry and exit are mutually exclusive by thresholds — the prior bar cannot print MFI both at-or-below 20 AND at-or-above 80 (20 < 80 always), so no bar can satisfy both prior-bar gates at once. No priority rule can ever fire; no same-bar dual-fire sequencing is left to any engine.
- Direction: long-only with an explicit pre-first-signal flat state plus the coded guard flat. Zero `short`/`sell` tokens ship anywhere; the base class pins `supported_trade_modes == {"long_only"}` and `mirror_short_safe == False` — a two-sided reading would contradict the file and its base. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the MFI cross-down through 80 is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent from the file in every form (0 `stop` / 0 `limit` / 0 `profit` / 0 `trail` tokens) and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min(1.0, (curr_mfi - 20) / 20.0)` on entry bars, else `0.0`) and the `indicators` dict are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats further entry-only bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit-only legs as no-ops; re-entry re-arms on any qualifying reclaim bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and guard bars are flat by coded/record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`, `low`, `close`, `volume` with fixed non-negative offsets — no `open`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above). The typical-price diff skips the single leading-`NaN` by pandas convention and all windows are trailing sums — deterministic given the pinned pandas semantics. The `compatible_regimes` set (`{"RANGE_BOUND", "TREND_UP"}`) is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` ranges are optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `high`, `low`, `close`, `volume` — typical price plus dollar-flow accumulation for the MFI path. No bar `open`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; both windows (the 14-bar flow sums, the one-bar cross edge lookback) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard (`len(df) < period + 3`, i.e. 17 bars at defaults). This record adopts a 17-bar record-rule warmup with pre-warmup bars flat (no derivation — the coded guard already holds them flat with `entry=False, exit=False`): at 17+ bars the 14-bar flow sums (which need one prior typical price, so 15 prints) plus the one-prior-bar edge read are all defined. Before that, `NaN` comparisons are `False` by construction, so no leg can fire early — coded behaviour, disclosed. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-MFI` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-seven admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and both legs are mutually exclusive edges (see Signal) — no ambiguous same-bar fill order is left to the engine.
- Volume faithfulness (declared): the flow leg reads the venue's own completed-bar `volume` prints — the same field the admitted `forven-atr-volume-breakout` sibling already gates on. No rebased, normalized, or cross-venue volume enters any predicate; a venue printing different volume prints different events by construction, disclosed.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; reclaim bars while positioned hold without adds; the cross-down leg closes the open side in full; re-entry after an exit needs only the next qualifying reclaim bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (117 lines: module docstring with the MFI-cross rule, `default_params` with the 14/20/80 set, the typical-price dollar-flow sums, the strict reclaim entry, the mirror overbought exit, the `direction="long"` literals and the `round(curr_close, 4)` price echo, the `PREBUILT-MFI` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard behaviour fenced: before the 17th bar the coded guard returns flat/flat; leading-`NaN` legs compare false by construction, so every pre-warmup bar is flat twice over — disclosed, not repaired. A shorter warmup would admit `NaN`-flat bars only (never spurious events), but the 17-bar floor is still pinned so the first trusted bar has fully defined windows.
2. Exact-touch rule fenced: prints landing exactly on their thresholds fire nothing on either leg (strict current-bar inequality both sides). A flat typical-price bar contributes to neither flow sum by strict `>` / `<` predicates — it holds by construction. Strictness is preserved throughout — disclosed, not smoothed.
3. Above-threshold loiter fenced: while positioned with MFI parked below 80 WITHOUT a fresh cross (entered earlier, flow drifted sideways), the exit leg stays false — only a fresh cross-down bar ends the position. There is no level-hold exit by construction; a slow bleed that never prints a qualifying cross bar rides in full — disclosed, not repaired. Mirror-wise, while flat with MFI parked above 20, no entry can fire without a fresh cross-up bar.
4. Zero-flow fenced: an all-zero-volume tape pins both flows at zero with `neg_flow` floored to `1e-10`, MFI pins at `0.0` — strictness admits no event on either leg. A tape of all-equal typical prices zeroes every diff with the same consequence. The single `replace(0, 1e-10)` floor is the only arithmetic guard in the path and it is source-verbatim — disclosed, not added.
5. Confidence/indicators diagnostic fenced: `confidence` and the full `indicators` dict never enter any predicate — an engine that skips computing all of them reaches identical events.
6. Spot-expression fenced: the long-only, no-stop, edge-exit book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both. The short side is explicitly disabled, never merely untested.
7. Cousin records fenced as different constructions (none trades pure 14-bar money-flow-index threshold-crosses 20-up/80-down, long-only, signal-exits-only, on `1h` bars from this file): the pool's `mfi-threshold-divergence-reversal` record crosses the same 14/20/80 lines but adds a 5-bar price-vs-MFI divergence pair plus an MFI-50 midline gate, trades two-sided with opposite-signal exits on `4h` bars from a Pine `ta.mfi` source (different gates, different direction handling, different exits, different frame, different source); the pool's `percent-b-mfi-dual-thrust-cross` record gates every MFI cross behind a Bollinger `%B` 0.80/0.20 thrust filter, trades two-sided with full reversals on `1d` bars (different filter, different direction, different exits, different frame, different source); the pool's `alphatrend-mfi-atr-trailing-reversal` record uses MFI only as a 50-gate inside an AlphaTrend ATR ratchet with a 2-bar self-cross trigger and a trailing construction, two-sided on `4h` bars (different indicator stack, different trigger, different risk, different frame, different source); the admitted `forven-rsi-s00139-washout-cross`, `forven-connors-rsi-oversold-recross` and `forven-ema-rsi-pullback-reclaim` siblings trade price-only RSI variants that never read `high`/`low`/`volume` — a different series entirely (dollar-flow vs close-changes); the admitted `forven-adl-ema-cross`, `forven-chaikin-mf-threshold-cross` and `forven-obv-ema-cross-sma-gated` siblings accumulate signed-volume or range-weighted flows against averages or thresholds, never a bounded 0–100 money-flow ratio against fixed 20/80 lines. Not a re-tuning of any of them: swapping the MFI formula, the period, either threshold, the exit, or the direction handling would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, and house sizing/costs — all predeclared above; the 17-bar guard floor is source-verbatim code, not an adoption. The money-flow construction, the 14/20/80 set, the strict reclaim entry, the mirror overbought exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour.
9. The MFI formula, the 14/20/80 triple, the strict cross edges, the mirror exit, the long-only stance, and the no-stop stance are pinned, not removed: re-tuning any length or threshold, softening strictness to touches, converting an edge to a level (or the reverse), adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: money-flow 14 / oversold 20 reclaim / overbought 80 exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: dropping the volume weighting (pure 14-bar RSI reclaim 20 with the same exit, same frame/pins) must not improve net expectancy; fail ⇒ the dollar-flow construction adds nothing over its price-only twin.
- F2 — Exit relevance: replacing the overbought cross-down exit with a close-under-14-bar-SMA exit (same entry) must not improve net expectancy; fail ⇒ the overbought-failure leg adds nothing over the trend-loss leg.
- F3 — Series relevance: trading the identical reclaim-plus-exit structure on the ADL money-flow-volume series (same lengths/entry/exit/pins, MFI replaced) must not reproduce-or-beat net expectancy; fail ⇒ the typical-price-signed dollar-flow construction adds nothing over its range-weighted twin and the record is a label variant of the admitted `forven-adl-ema-cross` sibling.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with `high`, `low`, `close`, `volume` fields only. No session calendar (crypto trades continuously; the 14-bar flow sums and the one-bar edge lookback need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics: single-unit bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- The file ships no risk leg in any form (verified zero tokens): the exits-only posture is source-verbatim effective behaviour, but any downstream evaluation must carry the full unprotected long-flat book, not an assumed stop.
- Reclaims that never print a fresh cross-down bar ride in full (Negative evidence 3); oversold dips that recover in price without dollar-flow reclaiming 20 never trade.
- Volume-print differences across venues shift the money-flow series and hence events; this record claims only the venue's own prints.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/mfi.py
- https://github.com/judder659/Forven
