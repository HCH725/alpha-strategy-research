---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FRAMA-gated SMA13/26 cross long with FRAMA-rail exit on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-01-15
sources:
  - https://www.fmz.com/strategy/438806
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8EFRAMA%E6%8C%87%E6%A0%87%E7%9A%84MA%E5%9D%87%E7%BA%BF%E4%BA%A4%E5%8F%89%E7%AD%96%E7%95%A5FraMA-and-MA-Crossover-Trading-Strategy-Based-on-FRAMA-Indicator.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FRAMA-gated SMA13/26 cross long with FRAMA-rail exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-10):

- Canonical page: https://www.fmz.com/strategy/438806 (page title `基于FRAMA指标的MA均线交叉策略 | FMZ`, publisher account `ChaoZhang`, `2024-01-15` stamp appearing twice on the page, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (752204 bytes): the page embeds the full `//@version=2` Pine block exactly once inside its data payload (page-wide counts read `strategy.entry` 1 / `strategy.close` 1 / `strategy.exit` 0 / `strategy.order` 0, with zero `stop=` / `limit=` anywhere) plus the `/*backtest*/` header (`start: 2023-01-14 00:00:00`, `end: 2024-01-14 00:00:00`, `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT`, 2 hits each) and the four argument defaults (`price` = `hl2`, `len` = `16`, `FC` = `1`, `SC` = `198`) in the page's strategy-parameters form. Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2024-01-15 from the page stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray, ActionZone and Fibonacci admissions), exact file path `基于FRAMA指标的MA均线交叉策略FraMA-and-MA-Crossover-Trading-Strategy-Based-on-FRAMA-Indicator.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 6091 bytes, blob SHA `f5b33d745955aef27205762608375ffaac38f987` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Detail` = https://www.fmz.com/strategy/438806 and `> Last Modified` = 2024-01-15 14:38:48 (equal to the page stamp). The page-embedded code block (escape-decoded) and the mirror ```pinescript block are byte-identical (1311 bytes each) — the decoded page block was diffed line for line against the mirror block with zero differences.
- Full `//@version=2` block read in full (code lines from `/*backtest` through the final `strategy.close`, strategy declaration `strategy("Fractal Adaptive Moving Average",shorttitle="FRAMA",overlay=true)`). The page-embedded `/*backtest*/` header (`period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`, 1h execution granularity) are therefore source-native, never researcher-chosen. With market entry and full-close legs only (no stop/limit/intrabar legs anywhere), the 1h base granularity is immaterial to fills (24 native 1h bars per 1d bar on a 24/7 venue); this record keeps the source-native 1d/1h frame with no frame derivation.
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry(id= "MA cross", long = true, when = entry())` — v2 long-only market entry, no price argument, no quantity) / 1 `strategy.close` (`strategy.close(id= "MA cross", when = exit())` — full close, no quantity qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`qty` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open` word (the rule reads `high`/`low`/`close`/`hl2` only) / exactly 4 `input(` (`price = input(hl2)`, `len = input(defval=16,minval=1)`, `FC = input(defval=1,minval=1)`, `SC = input(defval=198,minval=1)` — all pinned at defaults) / 3 `plot` calls (`ma_fast`, `ma_slow`, FRAMA `out` — display only, feeding no order condition). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission_*` and `slippage` are unset throughout (Pine language defaults apply — v2 `calc_on_every_tick` defaults false: exactly one evaluation per completed bar; default `pyramiding` 0: no same-direction adds).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs. The FRAMA-rail close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the pinned code block carries no licence header of its own (the FMZ page is the publication vehicle). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 40-bar warmup with pre-warmup bars flat by record rule (covers the 26-bar slow average, the 24-bar FRAMA window-plus-lag, and cross-reference margin — see Required data); (3) house sizing/capital replacing the source economics stub (no quantity, capital, commission, fee, slippage, or margin assumption ships anywhere — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`1d`, 1h base), the pinned `13 / 26 / hl2 / 16 / 1 / 198` literals, the FRAMA arithmetic, both signal functions, order IDs, direction handling, the full close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `frama`, `fractal adaptive`, and `438806` return zero hits anywhere — no admitted rule uses this source, author strategy, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs (#1–#113 reviewed by title) contain no FRAMA record; the single title sharing the word "Fractal" (#109, Williams Fractal EMA-band reversal) is a different mechanism class (Bill Williams 5-bar price-fractal pattern rails — never a fractal-dimension adaptive average). Closest pool records are different mechanism classes: `ema-20-50-cross-btcusdt-1h` trades a naked dual-EMA cross with no gate and no adaptive leg; `golden-cross-sma-regime-gated-long-btcusdt-1h` gates a cross on a slow-SMA regime (never a fractal-dimension rail); `mcginley-ema-touch-regime-reversal` and `vidya-cmo-adaptive-slope-trend` use different adaptive averages (McGinley, VIDYA/CMO — never log-range-dimension alpha). Five-axis distinction: mechanism differs (SMA13/26 cross additionally gated on price holding above a fractal-dimension adaptive rail, with exit on the opposite cross OR losing the adaptive rail — versus naked crosses, SMA-regime gates, or other adaptive formulas), signal construction differs (log-range fractal dimension `dimen` with adaptive `alpha` recomputed every bar from 8/16-bar high/low windows — no pool record computes `(log(N1+N2)-log(N3))/log(2)`), trigger differs (gated cross entry plus dual-leg exit on one long-only unit), and source identity differs (fmzquant pin `7853bb2` port of ChaoZhang 438806, 2024-01-15).

## Economic mechanism

### Source-reported

Fractal-adaptive gated trend capture (mirror Overview/Logic plus code, no performance section ships): the 13-day and 26-day simple averages define trend direction by cross, while the FRAMA rail — an exponential average whose smoothing `alpha` is recomputed every bar from the fractal dimension of recent ranges — defines the tradable side. A fast-over-slow cross buys only while price holds above the adaptive rail (trend with efficiency behind it); the trade ends either on the opposite cross or on the first close that loses the adaptive rail. The design bets that crosses backed by high-efficiency (trending) price structure resolve further than naked crosses, while a close back under the adaptive rail admits the structure broke.

### Research interpretation

Efficiency-gated cross-following with an explicit flat state, long-only. Unlike naked dual-MA systems that buy every fast-over-slow cross, this system skips crosses printed while price rides at or under the adaptive rail — strictly fewer entries at the cost of missing V-shaped recoveries where the cross fires before price reclaims the rail. Unlike regime-gated systems that freeze a slow-SMA side for weeks, the FRAMA rail breathes every bar with the 8/16-bar range structure, so the gate can flip from permissive to blocking within a single choppy window — at the cost of whipsawed permission in exactly the chop FRAMA is meant to filter. Unlike always-in-market holders, the system rests flat before the first cross and after every exit leg, and it never shorts: opposite crosses while flat are no-ops. The bet is on cross timing *inside* efficient structure, not on any oscillator level, volatility band, volume print, or calendar effect.

## Signal

Exact rule as pinned (`13 / 26 / hl2 / 16 / 1 / 198` frozen — the MA lengths and all four inputs at defaults; any other value is a different, unpinned rule):

- Declaration (derived): `strategy("Fractal Adaptive Moving Average",shorttitle="FRAMA",overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the source economics stub (see Execution assumptions). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). No commission, margin, fee, or slippage assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Dual averages (pinned): `ma_fast = sma(close, 13)`; `ma_slow = sma(close, 26)`. Both recompute every bar from completed closes.
- FRAMA rail (pinned, `price = hl2`, `len = 16`, `len1 = len/2 = 8` exactly, `FC = 1`, `SC = 198`): `w = log(2/(SC+1))` (natural log); `H1 = highest(high, 8)`, `L1 = lowest(low, 8)`, `N1 = (H1-L1)/8`; `H2 = highest(high, 16)[8]`, `L2 = lowest(low, 16)[8]`, `N2 = (H2-L2)/8`; `H3 = highest(high, 16)`, `L3 = lowest(low, 16)`, `N3 = (H3-L3)/16`; `dimen1 = (log(N1+N2)-log(N3))/log(2)`; `dimen = (N1>0 and N2>0 and N3>0) ? dimen1 : prior dimen` (seed 0 via `nz` — see Negative evidence); `alpha1 = exp(w*(dimen-1))`; `oldalpha = clamp(alpha1, 0.01, 1)`; `oldN = (2-oldalpha)/oldalpha`; `N = ((SC-FC)*(oldN-1))/(SC-1)+FC` (identically `oldN` at the pinned `FC=1, SC=198` — see Negative evidence); `alpha_ = 2/(N+1)`; `alpha = clamp(alpha_, 2/(SC+1), 1)`; `out = (1-alpha)*prior out + alpha*hl2` (seeded at first-bar `hl2` since `alpha` clamps to 1 — see Negative evidence). The rail recomputes every bar from rolling windows (never frozen).
- Entry long: `strategy.entry(id= "MA cross", long = true, when = entry())` with `entry() => crossover(ma_fast, ma_slow) and (out < close)` — fires on the single bar where the fast average crosses strictly up through the slow average while the close holds strictly above the FRAMA rail, with same-bar-close execution under the derived declaration.
- Exit: `strategy.close(id= "MA cross", when = exit())` with `exit() => crossover(ma_slow, ma_fast) or crossunder(out, close)` — full close of the long on any bar with the opposite strict cross or a strict close cross under the FRAMA rail (no quantity qualifier), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state (`long = true` v2 syntax; no short leg exists anywhere). Before the averages and rail exist both signals are `na`/false by construction (no trade). On a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: the 3 `plot` calls (`ma_fast`, `ma_slow`, FRAMA `out`) render only and cannot change any order; order logic reads exactly the two signal functions.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (FRAMA windows), `low` (FRAMA windows), `close` (both averages, both cross legs, rail gate), `hl2` (FRAMA price input — `(high+low)/2` of the same completed bar). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1h` equals native 1h execution granularity — 24 1h bars per 1d bar on a 24/7 venue — and with market-entry/full-close legs only, no intrabar path exists for the base to affect). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: the slow average needs 26 completed `1d` bars, the FRAMA construction needs 24 (`highest(high,16)[8]`), and each cross reads one prior bar; `highest`/`lowest`/`sma` are `na` until their windows fill and crosses against `na` never fire. The adopted warmup is the first 40 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 26-bar average, the 24-bar FRAMA depth, and cross-reference margin). `highest`/`lowest`/`sma` are exact window functions with no seed transient beyond the `na` prefix, so no decay margin is required. No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. The current bar's `high`/`low`/`close` enter the windows only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit legs are evaluated in source order (entry block before exit block): on the rare bar where a fast-over-slow cross coincides with a rail-loss crossunder (see Negative evidence), the derived execution fills the entry at the close and closes it at the same close, ending flat; no ordering resolution beyond source order is required.
- Sizing/capital/costs: the source ships no quantity, capital, commission, fee, slippage, or margin assumption anywhere (quoted verbatim — the v2 declaration carries no economics at all) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `MA cross`; entry refires while already long are no-ops by the language default, the exit leg closes in full, an exit while flat is a no-op, and re-entry is allowed immediately on the next gated cross after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (SMA13/26, hl2/16/1/198 FRAMA with log-range dimension and adaptive alpha, `crossover`-gated entry, dual-leg `crossover`/`crossunder` exit, fixed `MA cross` order ID), the active `strategy(...)` declaration, the `Fractal Adaptive Moving Average` title, and the page-embedded 1d/1h January-2023→January-2024 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`qty` — the sole position-closing path is the coded dual-leg `strategy.close("MA cross")`. The absence is coded (the order block ends with the close leg and only display plots follow it in evaluation order).
2. Dual-leg same-bar coincidence, admitted plainly: `entry()` and `exit()` can both be true on one bar (a fast-over-slow cross landing on the same close that crosses strictly under the reshaped FRAMA rail). Source order (entry block before exit block) fills the long at the close and closes it at the same close, ending flat with two fills and no overnight exposure. This is the coded ordering, disclosed as the record's principal microstructure edge case.
3. Opposite crosses are mutually exclusive by the strict definitions (both cannot fire together), so the exit leg's cross half and the entry leg never coincide — only the rail-loss half can coincide with an entry, as fenced above.
4. Flat-range determinism fenced: when any of `N1/N2/N3` is zero (degenerate flat window), `dimen` holds its prior value by the coded `iff` (seeded 0 via `nz` on the first bars) instead of evaluating `log(0)` — deterministic, disclosed, not guarded. When `range1`-style collapse makes all three rails equal a single print, the strict cross definitions still decide deterministically.
5. First-bar seed, disclosed: with `dimen` seeded 0, `alpha1 = exp(w*(0-1)) = (SC+1)/2 > 1` clamps through `oldalpha = 1` to `alpha = 1`, so `out` seeds exactly at first-bar `hl2` — a pinned inductive start, not a hidden lookback.
6. At the pinned `FC = 1, SC = 198`, `N = ((198-1)*(oldN-1))/(198-1)+1` is identically `oldN` — the two-stage smoothing collapses to one stage by arithmetic, disclosed, not simplified away (the record pins the full formula; retuning `FC`/`SC` would be a different, unpinned rule).
7. `len1 = len/2` evaluates to exactly `8` (no fractional part at the pinned `len = 16`), so the float-vs-integer window/offset reading is immaterial — recorded as integer 8 with identical values, never as a parameter change.
8. The `13 / 26` lengths, the `hl2 / 16 / 1 / 198` input set, the rolling (never frozen) rail semantics, the strict cross (not touch) triggers, the rail gate, the fixed order ID, the long-only posture, the full close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, converting a cross into a touch, dropping the rail gate, adding a stop/target/filter/cooldown, or enabling a short side would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 40-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every literal, the FRAMA arithmetic, both signal functions, the close leg, and the risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `13/26` / hl2-16-1-198 FRAMA / rolling rail / gated-cross entry / dual-leg exit / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: replacing the FRAMA-gated entry with the naked SMA13/26 cross entry (same exit leg) must not improve net expectancy; fail ⇒ the adaptive-rail gate adds nothing over the naked cross.
- F2 — Exit relevance: removing the FRAMA-rail-loss exit half (holding through rail losses until the opposite cross — since no other exit exists) must not improve net expectancy; fail ⇒ the adaptive-rail exit is dominated by simply staying positioned.
- F3 — Adaptivity relevance: replacing the FRAMA rail with a fixed-alpha EMA of the same 16-bar span (same gate and exit roles) must not improve net expectancy; fail ⇒ the fractal-dimension adaptivity adds nothing over a fixed smoother.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The high/low/close/hl2 arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the opposite cross or the breathing FRAMA rail, which recomputes every bar and can drop with the window; a position whose rail never breaks is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Breathing gate: unlike frozen-regime systems, the FRAMA rail re-freezes every bar from the rolling range structure, so a slow range compression can drag the rail with the market and delay both permission and exit, while fast window turnover can whip the gate on marginal crosses. The breathing is the coded construction, disclosed, not smoothed.
- Dimension lag: `H2/L2` read the 16-bar window as of 8 bars ago, so the efficiency estimate trails fast regime shifts by construction — a fresh breakout initially inherits the old range's dimension. Disclosed, not re-lagged.
- No source cost declaration: no quantity, capital, commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, 2024-01-15): https://www.fmz.com/strategy/438806
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `f5b33d745955aef27205762608375ffaac38f987`, 6091 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8EFRAMA%E6%8C%87%E6%A0%87%E7%9A%84MA%E5%9D%87%E7%BA%BF%E4%BA%A4%E5%8F%89%E7%AD%96%E7%95%A5FraMA-and-MA-Crossover-Trading-Strategy-Based-on-FRAMA-Indicator.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
