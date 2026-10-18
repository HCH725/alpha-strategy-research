---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven volatility-contraction squeeze-state breakout two-sided on BTCUSDT 1h bars
created: 2026-10-18
updated: 2026-10-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/volatility_contraction_breakout.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven volatility-contraction squeeze-state breakout two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, and `forven-pivot-s1-bounce-r1-exit` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/volatility_contraction_breakout.py`.
- GitHub blob SHA at the pinned commit: `c25d5122411e16efd8e2c0a27712fb097294f743`, size 8414 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 8414 bytes, 199 lines, SHA-256 `adc1bc6c50d2080168abbdc64d88d3de182679a9f06f101d33ddeac3855c98ad`, identical to the GitHub blob (`git hash-object` reproduces `c25d5122…f743`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = VolatilityContractionBreakoutStrategy`, `TYPE_NAME = "volatility_contraction_breakout"` (lines 7, 195), and the `STRATEGIES = [("S-VCB-BTC", … {"_asset": "BTC"}), ("S-VCB-ETH", … {"_asset": "ETH"})]` roster pin (lines 197–200). This record pins the `S-VCB-BTC` roster leg.
- The file's own words (quoted for gate evidence, never extended): module docstring `Volatility Contraction Breakout strategy — trades squeeze expansions.` (line 1); class docstring long/short entry quads `ATR(14) < 20th percentile … BB width < 0.5 * BB width median … close >/< EMA(period) … RSI(14) >/< 50` and `Exit: price crosses EMA from the entry direction, or ATR resumes above median.` (lines 27–44); `describe()` returns `Trades the expansion phase after a volatility squeeze. Long when ATR and Bollinger Band width contract below threshold while price holds above EMA200 and RSI confirms momentum. Short mirrors the logic for downtrend environments.` (lines 76–82); `default_params` returns exactly `{ "atr_period": 14, "bb_period": 20, "bb_std": 2.0, "ema_period": 200, "rsi_period": 14, "atr_percentile": 20, "bb_width_multiplier": 0.5, "lookback": 200, "leverage": 3.0 }` (lines 59–70); `compatible_regimes` returns `{"RANGE_BOUND", "TREND_UP", "TREND_DOWN"}` (lines 73–74, metadata never read by the signal path); `parameter_space()` returns `{ "atr_percentile": (10, 40, 5), "bb_width_multiplier": (0.3, 0.8, 0.1), "ema_period": (100, 300, 50), "rsi_period": (7, 21, 7) }` (lines 186–193, a documented search surface only — this record pins the defaults and runs no search).
- Single decision path (verified line by line): `generate_signal()` (lines 84–184) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the file (0 matches), no scalar delegate, no second decision logic exists to diverge. The `confidence` values (`1.0` on entries, `0.0` elsewhere, lines 144/161/176) and the six `indicators` fields (`atr_14`, `bb_width`, `bb_width_median`, `ema_200`, `rsi`, `squeezed`) are diagnostic echoes — none ever enters any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion that refuses non-Boolean flags and resolves direction labels (`_normalize_signal_flag`, `_normalize_signal_direction`, lines 140–178) — flags arriving as strict booleans (as here, via `bool(...)` at line 173 and literal `True`/`False` at lines 139–140/156–157/172) pass through unchanged, and the `direction="long"` / `direction="short"` literals resolve to their books.
- Full-file token census (verified by search over the 199 lines this cycle): `direction="long"` (lines 91, 142, 175 — guard default, long entry, fallthrough default) and `direction="short"` (line 159 — the ONLY short literal); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (direct reads are exactly `df["close"]` / `df["high"]` / `df["low"]` at lines 94–96 — see Signal); 0 `macd` / 0 `stoch` / 0 `supertrend` / 0 `donchian` / 0 `keltner` / 0 `linreg` (no Keltner, no Donchian, no linreg-momentum construction of any kind — the squeeze is pure ATR-percentile plus BB-width-median); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the 200-bar squeeze window, the ATR-percentile/BB-width squeeze pair, the EMA200/RSI50 directional gates, the EMA-cross exits, and the 200-bar guard — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own if-chain. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(price_now, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, and pivot-s1-bounce records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with atomic-reversal semantics (the file carries no position reference; an already-positioned book treats same-side entry bars as hold-no-ops, a flat book treats fallthrough exit bars as no-ops, and an opposite-side entry bar atomically closes and reverses in one event — the SQZMOM-LB sibling establishes single-position reversal as the pinned-Hummingbot-compatible posture for two-sided state machines; pin disclosed, never presented as source-native semantics); (4) house sizing/capital/costs replacing the bare `leverage: 3.0` default (see Execution assumptions — the source declares no fee, funding, or margin treatment at all).

Pre-write dedup (2026-10-18): working-tree filename/content search for `volatility_contraction_breakout` / `VolatilityContraction` / `S-VCB` returns zero strategy records citing this source file. The pool's squeeze cousins are fenced as different constructions in Negative evidence 8 (NR7 raw 7-bar range-minimum plus channel breakout plus time/ATR-stop long-only; SQZMOM-LB BB-inside-Keltner plus linreg-momentum release with momentum-dowtick exits; chartart joint RSI(6)-cross-50 plus BB-rail-reclaim cross events with opposite-cross exits; no pool record gates state entries on an ATR-percentile/BB-width-median squeeze pair with EMA200/RSI50 alignment and EMA-cross exits). No closed `research/*` PR ever carried this source file. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a dual-threshold squeeze-state plus trend/momentum-gated two-sided machine with EMA-cross exits is a different signal construction from any range-minimum breakout, Keltner squeeze-release, or rail-reclaim cross system — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: volatility contracts before it expands — trade the expansion phase after a squeeze where both ATR and Bollinger Band width contract below threshold, with price holding its EMA side and RSI confirming momentum (long above EMA200 with RSI > 50, short mirrored). No behavioural, structural, or risk-premium channel is claimed anywhere in the 199 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Squeeze-state holding, two-sided, state-gated. Unlike range-minimum breakouts (NR7: buy the channel break the day after the narrowest range of seven) this system never measures a raw range rank and never trades a breakout event — it holds a side only while the contracted state plus trend/momentum alignment persists. Unlike oscillator squeeze-release systems (SQZMOM-LB: BB-inside-Keltner transition plus linreg-momentum flip) there is no band-inside-band geometry and no momentum oscillator leg — contraction is a dual-threshold state (ATR below its 20th percentile AND BB width below half its median, both over 200 bars) and the only directional voice is the EMA200 side plus the RSI-50 side. Unlike rail-reclaim cross systems (chartart: RSI crossing 50 on the same bar price reclaims a BB rail) there is no cross event anywhere — entries are pure state conjunctions evaluated per completed bar. The coded consequence (Negative evidence 1) is a hold-only-while-gated machine: a position survives a bar only if that bar re-fires its own entry state; the first bar the squeeze lapses, the EMA side flips without re-gating, or RSI recrosses 50, the fallthrough exit leg closes it.

## Signal

Exact rule as pinned (any other period, threshold, boundary, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 84–184) is the single source of truth:

```text
atr_now     = mean(TR[14]) on decision bar, TR = max(H-L, |H-C[t-1]|, |L-C[t-1]|), rolling mean min_periods=1
atr_pct20   = 20th percentile of atr_series over last 200 bars (pandas quantile, linear interpolation)
bb_mid      = SMA(close, 20); bb_sd = sample stdev(close, 20, ddof=1)
bb_width    = 2 * 2.0 * bb_sd                       // upper - lower
bb_med      = median(bb_width over last 200 bars)
squeezed    = atr_now < atr_pct20 AND bb_width < 0.5 * bb_med
ema200      = Wilder-incompatible plain EMA: close.ewm(span=200, adjust=False)
rsi14       = Wilder RSI via ewm(alpha=1/14, adjust=False), zero-loss floored at 1e-10
long_entry  = squeezed AND close > ema200 AND rsi14 > 50
short_entry = squeezed AND close < ema200 AND rsi14 < 50
long_exit   = close < ema200                        // fallthrough only
short_exit  = close > ema200                        // fallthrough only
guard       = fewer than 200 completed bars → flat by source rule
```

- Trade events: `entry_signal=True` with `direction="long"`/`"short"` on entry bars (lines 137–169); otherwise `entry_signal=False` with `exit_signal=bool(long_exit or short_exit)` (lines 171–184). Evaluation order is the code's own if-chain: long entry, then short entry, then the fallthrough — and the two entries are mutually exclusive by construction (`close > ema` vs `close < ema` cannot co-fire; the long-first order is therefore unreachable as a tiebreak — disclosed, not load-bearing).
- Same-bar ordering: no ordering pin is needed. An entry bar carries `exit_signal=False` by code, and a fallthrough bar carries `entry_signal=False` by code — no bar ever fires both legs, so no co-fire resolution exists to specify. A bar with `close == ema200` exactly fires neither entry (both strict) and, on the fallthrough, neither exit leg (`<` and `>` both fail) — it holds any open side by code, disclosed as the exact-touch rule.
- Exact boundaries (pinned semantics): the squeeze pair is strict (`atr_now < percentile`, `bb_width < 0.5 * median` — equality on either leg voids the squeeze); the trend pair is strict (`close > ema200` / `close < ema200`); the momentum pair is strict (`rsi > 50` / `rsi < 50` — an RSI printing exactly 50.0 enters nothing). Guard bars are flat by source rule.
- Direction: two-sided with an explicit pre-first-signal flat state plus the 200-bar guard flat. Both legs are coded live (the single `direction="short"` literal at line 159); a single-sided reading would contradict the shipped short entry. The short side requires a margin venue (see Crypto portability).
- Exits and risk (explicit): the EMA-cross fallthrough is the sole position-ending path (`long_exit`/`short_exit`, lines 133–135). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. The class-docstring phrase `or ATR resumes above median` (line 44) ships nowhere in the order-gating code — code governs, prose fenced (Negative evidence 2). `confidence` (`1.0` on entries, `0.0` elsewhere) and the six `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats fallthrough exit bars as no-ops; an opposite-side entry bar reverses atomically (close plus open as one event — SQZMOM-LB precedent); re-entry re-arms on any qualifying state bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and guard bars are flat by source rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (TR legs, BB arithmetic, EMA/RSI seeds, percentile/median windows); no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The module-level `_atr` helper (lines 10–14) is dead code — never called anywhere in the file (exactly one `_atr(` occurrence: its own `def` line); the live ATR is computed inline at lines 100–101 — disclosed, not part of the rule. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` for the TR/ATR legs; `close` for the SMA(20)/stdev(20) BB arithmetic, the EMA(200), and the Wilder RSI(14); `high`/`low`/`close` jointly seed the 200-bar percentile/median windows. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all windows (`iloc[-lb:]` slices, rolling means, ewm seeds) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(price_now, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard — `max(lookback=200, bb_period=20, ema_period=200, rsi_period=14) = 200`, and shorter frames return an explicit all-flat Signal (lines 87–93, via `Signal(price=…, direction="long")` defaults `entry_signal=False, exit_signal=False`). The 200-bar floor covers the percentile/median windows and the EMA200 seed. The record adopts this guard verbatim as its flat rule — no researcher warmup pin is needed and none is pretended. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `S-VCB-BTC` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(price_now, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit/reversal orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/atomic-reversal position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; same-side entry bars hold without adds; opposite-side entry bars reverse atomically; any non-entry bar closes any open side (hold-only-while-gated machine — Negative evidence 1). Re-entry after an exit needs only the next qualifying state bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (199 lines: module docstring with the squeeze-expansion sentence, `TYPE_NAME`, `default_params` with the 200-bar lookback / `leverage 3.0`, the ATR-percentile/BB-width-median squeeze pair, the EMA200/RSI50 directional gates, the EMA-cross exits, the 200-bar guard, the `direction="long"` / `direction="short"` literals and the `round(price_now, 4)` price echo, the `S-VCB-BTC` / `S-VCB-ETH` roster pins). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Hold-only-while-gated fenced: from a long book, any bar that does not re-fire `long_entry` reaches the fallthrough, where `exit_signal = long_exit or short_exit` is true whenever `close != ema200` (one of the two strict legs always fires off-equality) — so a long survives only across consecutive long-state bars, and symmetrically for shorts. Positions are therefore state-rentals, never EMA-cross-to-EMA-cross swings in the docstring's looser sense. Disclosed, not repaired.
2. Doc/code mismatch fenced: the class docstring promises `or ATR resumes above median` as an exit (line 44) and the module docstring promises expansion trading — neither ATR-resumption nor any expansion leg ships in the order-gating code (lines 128–135 read EMA side only). Code governs; prose is never executed.
3. Dead helper fenced: the module-level `_atr()` (lines 10–14, which would in any case compute `close.diff().abs()` rather than true range) is called zero times — the live ATR is the inline TR-max computation at lines 100–101. An engine that deletes `_atr` reaches identical events.
4. Exact-touch rules fenced: squeeze equality voids (`<` strict on both legs); `close == ema200` fires no entry and no exit (hold by code); `rsi == 50.0` enters nothing. Strictness is preserved throughout — disclosed, not smoothed.
5. Degenerate-window behaviour fenced: an exactly flat 200-bar window pins `atr_pct20 == 0` and `bb_med == 0`, voiding the squeeze (`atr_now < 0` unsatisfiable for non-negative ATR; `bb_width < 0` unsatisfiable) — entries correctly die in zero-volatility tapes rather than firing spuriously. RSI zero-loss flooring (`1e-10`, line 24) prevents division-by-zero without changing any threshold event. Disclosed, not repaired.
6. Confidence diagnostic fenced: constant `1.0` on entries / `0.0` elsewhere never enters any predicate — an engine that skips computing confidence reaches identical events. The six indicator echoes duplicate the predicate values and likewise change no event when skipped.
7. Source basis fenced: the source names no market beyond `_asset BTC/ETH` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit/atomic-reversal pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Cousin records fenced as different constructions (none gates state entries on an ATR-percentile/BB-width-median squeeze pair with EMA200/RSI50 alignment and EMA-cross exits): the admitted NR7 sibling conditions entries on the current daily range being the narrowest of the last seven sessions with a next-day channel-breakout entry and a 10-day time exit plus ATR-multiple protective level, long-only (raw-rank school, no indicator, no state holding); the admitted SQZMOM-LB sibling keys squeeze off BB-inside-Keltner geometry with a linreg-momentum release trigger and momentum-dowtick exits (oscillator-release school, no percentile/median windows, no RSI leg); the admitted chartart BB-RSI sibling enters only on joint cross events (RSI(6) crossing 50 on the same bar price reclaims a BB rail) with opposite-cross exits (cross-event school, close-only reads, no high/low, no squeeze state); Donchian buys every rolling-extreme break with no contraction precondition; Keltner/SuperTrend/Chandelier trail volatility bands without any squeeze gate. Not a threshold re-tuning of any of them.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, and house sizing/costs — all predeclared above; the 200-bar window, the ATR-percentile/BB-width squeeze pair, the EMA200/RSI50 gates, the strict boundaries, the EMA-cross exits, the two-sided book, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 14/20/2.0/200/14 periods, the 20th-percentile/0.5-multiplier pair, the 200-bar window, the strict boundaries, the single-unit two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning any period, re-anchoring the squeeze on Keltner or raw ranges, converting state entries to cross events, adding a stop/target/filter/cooldown/gate, dropping the short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 200-bar dual-threshold squeeze / EMA200-RSI50 gates / strict boundaries / EMA-cross exits / single-unit two-sided atomic-reversal / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Squeeze relevance: replacing the dual-threshold squeeze gate with always-squeezed (`is_squeezed = True`, keeping the EMA200/RSI50 gates and exits) must not improve net expectancy; fail ⇒ the contraction state adds nothing over plain trend-momentum gating.
- F2 — Dual-threshold relevance: replacing the squeeze pair with the ATR-percentile leg alone (dropping the BB-width-vs-median leg) must not improve net expectancy; fail ⇒ the BB-width confirmation adds nothing over the ATR contraction alone.
- F3 — Exit relevance: replacing the EMA-cross fallthrough exit with a fixed 10-bar time exit must not improve net expectancy; fail ⇒ the EMA-side holding rule adds nothing over a fixed lifespan.

## Crypto portability

Direct for the long leg, margin-gated for the short leg: single-venue BTCUSDT perpetual `1h` completed bars with standard OHLC fields. No session calendar (crypto trades continuously; the 200-bar percentile/median windows need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every window bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `3.0` default. The short leg requires a margin venue (perpetual qualifies under the house overlay); a spot-only deployment expresses the long leg alone and would not be the same rule.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics: single-unit/atomic-reversal bookkeeping is a predeclared researcher pin (SQZMOM-LB precedent), never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Hold-only-while-gated concentration (Negative evidence 1); doc/code exit mismatch (Negative evidence 2); exact-touch holds (Negative evidence 4).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/volatility_contraction_breakout.py
- https://github.com/judder659/Forven
