---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: StockSharp Simplest DeMarker 0.2/0.8 threshold re-cross with cooldown two-sided on BTCUSDT 1h bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-12
sources:
  - https://github.com/StockSharp/AlgoTrading/blob/a021cf9e92ac1037cb4f9145e8e2594512331519/API/3401-3500/3450_Simplest_DeMarker/PY/simplest_de_marker_strategy.py
  - https://github.com/StockSharp/AlgoTrading/blob/a021cf9e92ac1037cb4f9145e8e2594512331519/API/3401-3500/3450_Simplest_DeMarker/README.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# StockSharp Simplest DeMarker 0.2/0.8 threshold re-cross with cooldown two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (raw file fetch 2026-10-12, adopted as `source_as_of`):

- Strategy file (60-line Python class, immutable pin): `StockSharp/AlgoTrading` commit `a021cf9e92ac1037cb4f9145e8e2594512331519` (repository `main` HEAD as read), exact path `API/3401-3500/3450_Simplest_DeMarker/PY/simplest_de_marker_strategy.py` — class `simplest_de_marker_strategy(Strategy)`, `OnStarted2` subscribes candles and binds `DeMarker()` with `Length = DemarkerPeriod`, `_process_candle` returns early unless `candle.State == CandleStates.Finished`.
- Pinned defaults read verbatim from the file: `CandleType = 60 minutes`, `DemarkerPeriod = 14`, `Oversold = 0.2`, `Overbought = 0.8`, `SignalCooldownCandles = 4`; state fields `_prev_value = 0.0`, `_candles_since_trade = 4` (initialized to the cooldown value, i.e. eligible from the first formed signal), `_has_prev = False` (same initialization in both `OnReseted` and `OnStarted2`).
- Order legs read verbatim: `if self._has_prev:` → buy leg `self._prev_value < self.Oversold and dm_val >= self.Oversold and self.Position <= 0 and self._candles_since_trade >= self.SignalCooldownCandles` → `self.BuyMarket()` + counter reset; `elif self._prev_value > self.Overbought and dm_val <= self.Overbought and self.Position >= 0 and self._candles_since_trade >= self.SignalCooldownCandles` → `self.SellMarket()` + counter reset. The file contains 0 `StartProtection`, 0 stop/target/trailing/time calls, 0 `TradeOnBarOpen` parameter, 0 `request.*`/`security(` equivalent, 0 multi-symbol or multi-timeframe subscription — one candle subscription only.
- Indicator construction verified against the sibling immutable source `StockSharp/StockSharp` `Algo.Indicators/DeMarker.cs` at `master` commit `61cc0f169742b33218fef8a80a3c227def11cb0e`: `DeMax = currentHigh > _prevHigh ? currentHigh - _prevHigh : 0`, `DeMin = currentLow < _prevLow ? _prevLow - currentLow : 0`, both legs through `SimpleMovingAverage` of `Length`, `DeMarker = deMaxSma / (deMaxSma + deMinSma)` with `0.5` when the denominator is zero; state advances only on finalized input (`IsFinal` gating; first bar only seeds `_prevHigh/_prevLow`), `CalcIsFormed` requires both SMAs formed. The strategy therefore reads bar `high`/`low` only through this indicator — zero `close`, zero `volume`, zero `open` reads anywhere in the order-gating path.
- Sibling README (`API/3401-3500/3450_Simplest_DeMarker/README.md`, same commit) tracked, never adopted as rules where it diverges: it describes the CS/MQL lineage (`Trade On Bar Open` flag, `StartProtection` stop/take distances, configurable Volume) — none of which exists in the pinned PY file. Where README prose and PY code conflict, the code governs (fenced in Negative evidence).
- No performance table, figure, or number ships anywhere in the strategy file or the README — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the source repository is a public open-source publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market BTCUSDT Binance perpetual `1h` (the source default candle type is 60 minutes — identical frame — but names no venue or symbol; the README asks only for a sufficiently liquid instrument); (2) finished-bar decision with next-bar-open fills, adopting the source's own execution posture (the PY file acts only on `Finished` candles and sends market orders — see Execution assumptions); (3) position-state pin — single default lot, volume-for-volume netting so the opposite signal flattens rather than reverses, same-side adds rejected, re-entry only on a fresh re-cross after cooldown (the source passes no volume argument, i.e. default-lot netting — see Signal); (4) an adopted 25-bar warmup with pre-warmup bars flat by record rule (covers SMA-14 seeding plus the one-bar `has_prev` latch plus margin — see Required data); (5) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The 14 length, the 0.2/0.8 thresholds, the strict-inequality re-cross pair with `elif` priority, the 4-candle cooldown, the DeMax/DeMin SMA-ratio formula with 0.5-on-zero-denominator, and the no-stop/no-target posture of the PY file are source-verbatim.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `demarker`, `de-marker`, `DeMax`, `DeMin`, `SignalCooldown` return zero strategy records using this source, author, indicator, or mechanism — the only `Demark`/`demark` text in the pool is `td-sequential-setup9-perfected-long-btcusdt-1h-2026-10-12.md` (Tom DeMark Sequential 9-count perfected-exhaustion countdown on consecutive closes — a different indicator, different inputs, different state machine; fenced in Negative evidence) and one incidental prose mention inside the Mass Index record. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool oscillators differ on all four axes: RSI-family records smooth close-to-close changes (DeMarker never reads `close`); `williams-r-level-cross` reads a position inside the highest-high/lowest-low range (DeMarker reads high-to-high and low-to-low differentials, never a range position); `stoch-rsi-kd-zone-cross` and `cci-*`/`mfi-*` use different constructions and data (MFI folds in volume — DeMarker reads zero volume); no pool record crosses a DeMax/DeMin SMA-ratio against 0.2/0.8 with a post-trade candle cooldown. Four-axis distinction: signal construction differs (SMA(DeMax,14)/(SMA(DeMax,14)+SMA(DeMin,14)) with 0.5-on-zero), trigger differs (strict-inequality re-cross pair with `elif` priority plus 4-finished-candle cooldown and position-side gates), data differs (high/low differentials only — zero close/volume reads), and source identity differs (StockSharp AlgoTrading `3450_Simplest_DeMarker` PY at pinned SHA versus all other sources).

## Economic mechanism

### Source-reported

High/low-differential exhaustion fade: the DeMarker oscillator isolates buying pressure (rising highs) from selling pressure (falling lows) into a bounded ratio; a reading pinned under 0.2 marks selling-pressure exhaustion and a reading over 0.8 marks buying-pressure exhaustion. The strategy fades the exhaustion only on the re-cross back inside the neutral band (prev outside, current back at/inside the line) — never on touch, never on level-hold — with a 4-candle cooldown enforcing at most one fill per local event cluster. Per the README lineage, the logic reproduces the original MetaTrader expert advisor.

### Research interpretation

Edge-triggered two-sided exhaustion-fade system on high/low differentials, with no price level, band, stop, target, or confirmation leg beyond the single DeMarker-versus-threshold re-cross — long on the 0.2 upward re-cross, short on the 0.8 downward re-cross, flattening (never reversing) on the opposite re-cross, silent otherwise. Unlike close-based oscillators (RSI, CCI, Stochastic, KDJ, Laguerre) where every input derives from closes or close-derived ranges, here both smoothing legs derive from high-to-high and low-to-low differentials alone: a trending-close bar with equal highs and lows moves nothing, and a high-wick/low-wick bar with a flat close moves everything — the bet, as derived, is on BTCUSDT hourly intrabar auction exhaustion, never on a close level, breakout, squeeze, calendar, or mean-reversion anchor. Unlike cumulative or range-position systems (OBV, PVT, %R, Donchian), the SMA-ratio normalization makes the state scale-free across volatility regimes. The cost is symmetric: chop that alternately re-crosses both thresholds flattens and re-enters with only the 4-candle cooldown as guard, and adverse excursion after entry has no guardrail beyond the opposite re-cross, which may arrive many bars later.

## Signal

Exact rule as pinned (`DemarkerPeriod = 14` / `Oversold = 0.2` / `Overbought = 0.8` / `SignalCooldownCandles = 4` / 60-minute candles frozen — any other values are a different, unpinned rule):

- Declaration (derived): StockSharp PY semantics observed — one candle subscription, indicator bound at start, `_process_candle` gated on `CandleStates.Finished`; all five parameters gate calculation, zero display-only inputs.
- Oscillator (pinned, source-verbatim): `DeMax = max(High - High[1], 0)`; `DeMin = max(Low[1] - Low, 0)`; `DeM = SMA(DeMax, 14) / (SMA(DeMax, 14) + SMA(DeMin, 14))`, `0.5` when the denominator is zero. Bar `high`/`low` are the sole series read; `open`, `close`, `volume` are read nowhere.
- State (pinned, source-verbatim): `_has_prev` latch (first formed value only seeds `_prev_value`, never trades); per finished candle the trade counter increments first (`_candles_since_trade += 1` while below the cooldown), then the pair is evaluated with `elif` priority — buy leg first. Buy leg: `_prev_value < 0.2 and DeM >= 0.2 and Position <= 0 and counter >= 4` → `BuyMarket()` + counter reset to 0. Sell leg (only if buy leg false): `_prev_value > 0.8 and DeM <= 0.8 and Position >= 0 and counter >= 4` → `SellMarket()` + counter reset to 0. All other bars are explicit no-ops.
- The two legs are mutually exclusive on every bar by construction (strict `prev < 0.2` versus strict `prev > 0.8` can never co-hold, and `elif` orders them) — no bar can ever fire both legs, so no same-bar ordering ambiguity exists anywhere in this record.
- Position and re-entry (pinned defaults): default-lot market orders under netting semantics — from flat a signal opens one unit; from the opposite one-unit position the offsetting order flattens to zero (volume-for-volume offset, never a reversal to the opposite side); same-side signals while positioned are rejected by the `Position <= 0` / `Position >= 0` gates. Re-entry after any fill needs a fresh strict-inequality re-cross at least 4 finished candles later (counter reaches 4 on the fourth post-trade candle: T+1→1, T+2→2, T+3→3, T+4→4 eligible). No pyramiding, no adds, no DCA, no missing rule.
- Risk legs (pinned absence, not invented): the PY file ships 0 stop/target/trailing/time calls — the derived posture is explicitly no stop, no target, no trailing, no time exit; exits are opposite re-crosses to flat only.
- Direction: two-sided long/short with symmetric flattening. Futures venue required for the short leg (researcher market choice — pinned).
- Degenerate-input behavior (pinned, edge-case-explicit): all-flat bars drive the denominator to zero and yield exactly `0.5`, which sits inside the neutral band and can only arm (never fire) a leg — a 0.5 bar can serve as neither side's `prev` trigger since both triggers require strict outside (`< 0.2`, `> 0.8`); the first seeding bar returns no value and only initializes previous high/low. `ponytail:` no approximation is made beyond the coded 0.5 fallback.

## Required data

- Completed `1h` bars of BTCUSDT: bar `high` and `low` ONLY through the DeMarker binding — the sole series read by any order-gating line. No `open`, `close`, `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (one candle subscription, zero cross-feed calls).
- Single decision timeframe `1h`, matching the source default 60-minute candle type tick-for-tick. One evaluation per finished bar; all reads reference finalized bars only (`Finished` state plus `IsFinal` indicator gating).
- Warmup: each SMA(14) leg needs 14 differential values, the differentials start on the second finished bar, both SMAs are first formed on the 15th finished bar, and the `_has_prev` latch needs one more formed value — the first decidable bar is the 16th finished candle at the earliest. The adopted warmup is the first 25 completed `1h` bars flat by record rule (16-bar first-definable signal + 9 bars stabilization margin — predeclared researcher choice); no signal before bar 26 may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source default is 60-minute bars on an unnamed sufficiently liquid instrument; naming normalization to BTCUSDT `1h` is the only market step, and no source-market equivalence is claimed).
- Order timing (source posture, adopted as-is, disclosed): the PY file processes only `Finished` candles and sends market orders on completion — the signal is decided on the completed bar and filled at the next bar's open. This record adopts exactly that convention (completed-bar decision, next-bar-open fill), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`); no same-bar-close conversion is performed and none is claimed. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive order legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, margin, or funding concept of any kind (the PY file passes no volume argument — default-lot netting, pinned). The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/flatten-on-opposite/no-add pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit long, short, or flat at any time; the opposite re-cross flattens in one step and never reverses; re-entry needs a fresh re-cross after the 4-candle cooldown. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.
- High/low semantics: the rule reads the traded venue's own per-bar candle extremes only; no assumption about spot-versus-perpetual wick comparability is pinned beyond that read — disclosed, not approximated.

## Evidence

### Source-reported

The source ships the full construction (60-line PY class: 5 pinned parameters at 60m/14/0.2/0.8/4, the Finished-only gate, the `_has_prev` latch, the `if/elif` re-cross pair with position-side gates and cooldown gate, the `BuyMarket`/`SellMarket` pair with counter resets, and the `DeMarker()` binding whose SMA-ratio formula with 0.5-on-zero-denominator is verified in the sibling `DeMarker.cs`). The source ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer in the pinned file: 0 `StartProtection` / stop / target / trailing / time calls ship anywhere in the PY — the sole position-changing paths are the two market-order legs, and the opposite leg flattens rather than reverses under default-lot netting. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. README-versus-code divergence admitted plainly: the sibling README describes `Trade On Bar Open` fills and `StartProtection` stop/take distances from the CS/MQL lineage — neither exists in the pinned PY file (no such parameter, no such call). This record follows the PY file only; adopting the README's SL/TP or next-open flag would be a different, unpinned rule.
3. README prose imprecision fenced: "New signals are ignored while a position exists" reads as if opposite signals were ignored, but the code evaluates the opposite leg whenever `Position <= 0` (buy) or `Position >= 0` (sell) — from a one-unit short, the buy leg fires `BuyMarket()` and nets to flat; from a one-unit long, the sell leg nets to flat. The code governs: opposite re-cross exits to flat, same-side re-entry while positioned is ignored. Pinned, never "corrected" into a reversal.
4. Cooldown admitted plainly: at most one fill per 4 finished candles by construction — a textbook re-cross inside the cooldown window is deliberately untraded, and re-entry after a flatten requires a fresh strict-inequality re-cross, so a market that sits on the line after flattening stays flat. This is the coded trade, disclosed, not a tunable parameter here.
5. No-stop flat-to-flat whipsaw admitted plainly: alternating 0.2/0.8 re-crosses flatten and re-enter across the cooldown with no guardrail beyond the opposite re-cross; adverse excursion between re-crosses has no guardrail of any kind. Disclosed as a principal risk alongside high/low-only blindness (a close-trend bar with equal highs/lows cannot move the state).
6. DeMarker-is-not-Sequential fenced: this oscillator (Tom DeMark, high/low differentials, SMA ratio, 0.2/0.8) shares only a namesake with the pool's TD Sequential record (consecutive-close 9-count with perfection qualifier) — different inputs, different formula, different state machine, different source. Neither record is evidence for the other.
7. Warmup flatness fenced: the first 25 bars are flat by record rule, so any textbook re-cross inside warmup is deliberately untraded — pinned, not recovered.
8. Source basis fenced: the source names no venue or symbol (60-minute default frame adopted tick-for-tick as `1h`). The BTCUSDT choice, next-bar-open fills, single-lot/flatten-on-opposite pin, 25-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-venue deployment passes.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market choice, the next-bar-open fill adoption, the position-state pin, the adopted 25-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the 14 length, the 0.2/0.8 thresholds, the strict-inequality re-cross pair with `elif` priority, the 4-candle cooldown, the DeMax/DeMin SMA-ratio formula with 0.5-on-zero-denominator, the `Finished`-only causality, and the no-stop/no-target posture are source-verbatim. This record is therefore never evidence that the original repository itself passes.
10. The `14` / `0.2` / `0.8` / `4` literals, the re-cross (not touch, not hold) trigger pair, the flatten-on-opposite (not reversal) stance, the two-sided posture, and the no-stop/no-target/no-trailing stance are pinned, not removed: retuning any literal, converting re-crosses into touches, adding a stop/target/filter/gate, reversing instead of flattening, dropping a side, or sizing partially instead of single-lot would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `14` / `0.2` / `0.8` / `4` / strict re-cross pair / flatten-on-opposite / two-sided / `1h` BTCUSDT / next-bar-open fills are frozen.

- F1 — Threshold relevance: replacing the 0.2/0.8 re-cross pair with the 0.3/0.7 pair through the identical 14-length chain and cooldown must not improve net expectancy; fail ⇒ the pinned thresholds carry no advantage over neighboring exhaustion lines.
- F2 — Cooldown relevance: replacing the 4-candle cooldown with 0 (trade every fresh re-cross) must not improve net expectancy; fail ⇒ the cooldown adds nothing over unthrottled re-cross trading.
- F3 — Parameter relevance: replacing the pinned length 14 with an adjacent value must not improve net expectancy; fail ⇒ the pinned default carries no advantage over neighboring lookbacks and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame source-identical `1h`; arithmetic over the venue's own candle highs/lows with no venue-specific read and zero close/volume reads). The construction ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no time gating anywhere), so session-gap behavior needs no approximation. Wick-magnitude comparability across venues is not claimed — the rule reads the traded venue's own candle extremes only. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Researcher market: the source names no venue or symbol — BTCUSDT is a researcher choice; signal timing on other markets would differ by construction. (The `1h` frame is source-identical, not a choice.)
- Adopted fill timing: next-bar-open execution follows the source's own Finished-candle-plus-market-order posture, but the source never states a fill convention in prose — backtest economics of other timings differ by construction; the adoption is disclosed, not hidden.
- Position-state pin: default-lot netting has no explicit source prose beyond the parameterless `BuyMarket()`/`SellMarket()` calls and the `Position <= 0` / `Position >= 0` gates; the single-lot/flatten-on-opposite/no-add pin is a researcher reading of that code, disclosed, not independently prose-verified.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite re-cross, which may arrive many bars later or after deep excursion; alternating re-crosses flatten and re-enter repeatedly across the cooldown. This is the coded posture, disclosed as a principal risk alongside high/low-only blindness.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 25 bars are flat by record rule, so any textbook re-cross inside warmup is deliberately untraded — pinned, not recovered.
- Zero-denominator guard: an all-flat lookback yields exactly 0.5 and can only arm, never fire — fenced, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Simplest DeMarker Strategy [StockSharp AlgoTrading] pinned strategy file (commit `a021cf9e92ac1037cb4f9145e8e2594512331519`, read 2026-10-12): https://github.com/StockSharp/AlgoTrading/blob/a021cf9e92ac1037cb4f9145e8e2594512331519/API/3401-3500/3450_Simplest_DeMarker/PY/simplest_de_marker_strategy.py
- Simplest DeMarker Strategy README [StockSharp AlgoTrading] same commit (lineage prose, not rules): https://github.com/StockSharp/AlgoTrading/blob/a021cf9e92ac1037cb4f9145e8e2594512331519/API/3401-3500/3450_Simplest_DeMarker/README.md
- DeMarker indicator construction [StockSharp StockSharp] `Algo.Indicators/DeMarker.cs` at `master` commit `61cc0f169742b33218fef8a80a3c227def11cb0e`
