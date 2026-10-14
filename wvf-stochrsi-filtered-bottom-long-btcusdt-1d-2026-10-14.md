---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WVF fear-spike-resolution filtered bottom long with StochRSI overbought exit on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-28
sources:
  - https://www.fmz.com/strategy/428088
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Williams-VIX修复策略Williams-VIX-Fix-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# WVF fear-spike-resolution filtered bottom long with StochRSI overbought exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-14):

- Canonical page: https://www.fmz.com/strategy/428088 (fetched live over HTTPS during this cycle with HTTP 200, 829261 bytes of landing HTML). Landing-page token census: `Vix FIX` × 2; `StochRSI` × 2; `strategy.entry` × 1; author token `ChaoZhang` × 2; `428088` × 4. The ZH/EN prose states the组合 plainly: Williams VIX Fix formula plus Stochastic RSI and RSI legs; Stoch RSI falling from the overbought zone produces the sell signal; a WVF value below the lower Bollinger band is the buying basis (prose claim — fenced against the code below, which buys the fear-spike *resolution*, never a sub-lower-band print).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` during this cycle — the same head pin as the merged Inside-Bar-Failure, Bollinger-breakout, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and further admissions), exact file path `Williams-VIX修复策略Williams-VIX-Fix-Strategy.md` (13297 bytes, 275 lines, non-ASCII filename quoted verbatim, no encoding ambiguity). The mirror prints `> Name` = `Williams-VIX修复策略Williams-VIX-Fix-Strategy`, `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/428088, `> Last Modified` = `2023-09-28 15:29:48` (date part adopted as `source_as_of`), the `[trans]` ZH/EN prose matching the canonical page, a 28-row Strategy Arguments table (`v_input_1` through `v_input_28`, frozen below), and the complete executable `//@version=4` Pine block.
- Full block read in full (the entire file was retrieved; order-affecting lines are the two `strategy.entry`/`strategy.close` legs, the `filtered`/`filtered_Aggr` WVF-resolution definitions, the `upRange`/`upRange_Aggr` price-action conjunctions, the `close[3]`/`close[40]`/`close[14]` strength-regime tests, and the `crossover(k,d)` exit; everything else is declaration, dead-indicator, or display plumbing). The `/*backtest*/` stanza prints verbatim `start: 2022-09-21 00:00:00`, `end: 2023-09-27 23:59:00` (quoted here as printed in the mirror — the mirror shows `end: 2023-09-27 00:00:00`, never normalized into a claim), `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — the executable stanza itself backtests `Futures_Binance BTC_USDT` on the `1d` decision frame, so this record's `BTCUSDT 1d` market/frame pin is source-native, not a derivation (see derived declaration for the only three adaptations).
- Strategy declaration (source-verbatim): `strategy("Vix FIX / StochRSI Strategy", pyramiding=9, initial_capital=10000, default_qty_type=strategy.percent_of_equity, overlay=false)`. No `default_qty_value`, no `commission`, no `process_orders_on_close`, no `calc_on_every_tick`, no `shorttitle` ships anywhere in the declaration — Pine language defaults govern the unfrozen economics and timing, fenced below.
- Text census over the pinned code block (comments stripped before counting): 1 `strategy(` declaration / 1 `strategy.entry` (`"Long"` with `strategy.long`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 1 `strategy.close` (`"Long"`, no `when=` qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 active `stop=`/`limit=`/`profit=`/`loss=` / 1 `crossover(` (the exit leg only) / 0 `crossunder(` / 2 `highest(` (`highest(close, pd)`, `highest(wvf, lb)`) / 0 `lowest(` / 1 `stdev(` / 3 `sma(` (K smoothing, D smoothing, WVF midline) / 1 `stoch(` / 1 `rsi(` / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 1 bare `open` read (`close > open[1]` inside `upRange_Aggr`, census-verified the only `open` token) / 0 `position_size` reads / 0 `plotshape` / 3 `plot(` (`isOverBought`, `filteredAlert`, `aggressiveAlert` render-only lines) / 28 `input(` (frozen below). No short leg ships anywhere — long-only by coded construction, never by researcher choice.
- Licence and rights: the mirror block ships no licence header line; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) completed-bar decisions with same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census — this record pins completed-bar evaluation with same-bar-close fills and claims no next-bar timing, disclosed here); (2) an adopted 80-bar warmup with pre-warmup bars flat by record rule (covers the 50-bar WVF percentile seed stacked on the 22-bar highest seed plus the 40-bar regime reference with margin — see Required data); (3) house sizing/capital/costs replacing the absent source economics (the declaration carries `initial_capital=10000` and percent-of-equity quantity type but no quantity value, no commission, no funding leg — see Execution assumptions). The `BTCUSDT 1d` market/frame pin is source-native per the verbatim stanza above. The WVF arithmetic, all 13 live inputs, both entry conjunctions, the StochRSI exit, the `Long` order ID, the pinned `pyramiding=9` add semantics, and the no-stop/no-target posture are source-native and unmodified. No tie-break had to be invented: the two entry conjunctions co-fire deterministically into ordered adds, and the single exit leg cannot conflict with itself (see Negative evidence).

Pre-write dedup (2026-10-14): working-tree case-insensitive filename search for `wvf`, `vix-fix`, `vixfix`, and `428088` returns zero strategy records; content search for `wvf` / `rangeHigh` / `filteredAlert` / `upRange_Aggr` / `Vix FIX / StochRSI` pool-wide returns zero records using this source, author script, indicator, or rule. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `stoch-rsi-kd-zone-cross-two-sided-btcusdt-1h-2026-10-12.md` trades zone-gated StochRSI K/D crosses two-sided on `1h` (StochRSI is the trigger, computed RSI-then-stochastic, flat-gated, no pyramiding); this record never trades a StochRSI cross for entry — StochRSI appears solely as the long-exit trigger, computed price-stochastic-then-double-SMA, while entries come from the WVF fear-spike-resolution conjunctions with `pyramiding=9` adds, long-only, `1d`. No other pool record evaluates a Williams VIX Fix series anywhere. Five-axis distinction: source identity differs (FMZ 428088 versus Eterna/FMZ-others), mechanism differs (synthetic-volatility fear-spike-resolution bottom-fishing versus oscillator-cross reversal), signal construction differs (WVF(22,20,2.0,50,0.85) plus bar-geometry and close-position conjunctions versus RSI-chain K/D), exits differ (overbought K/D cross close of a pyramided long book versus opposite-cross closes), position state differs (pyramiding-9 long-only adds versus flat-gated two-sided). Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Fear-spike-resolution bottom-fishing with an exhaustion exit (code plus bilingual prose, no performance section ships): the Williams VIX Fix measures how far the current low has fallen below the highest close of the last 22 bars — a synthetic-volatility panic gauge in the Larry Williams lineage that needs no options data. When that gauge prints an extreme (above its own 20-bar Bollinger upper band or above 85% of its own 50-bar peak) and then resolves back below both rails on the next bar, the panic is deemed released; the system buys the release only when the tape agrees (an up-range bar that closes above the close 3 bars back while still closing below a 40-bar or 14-bar lookback close — weakness with a pulse, not strength-chasing). The prose ships a buying story (sub-lower-band calm) the code never trades — code governs (see Negative evidence). The long book is held with no stop and no target until the slow stochastic's %K crosses down through %D above 80 — upside exhaustion, not a price level, ends the trade. The header admits conservative-degenerate risk posture (large possible drawdown, needs position sizing) by design gap rather than by hidden leg.

### Research interpretation

Single-sided panic-release machine, event-driven, long-only, pyramided, exhaustion-exited. Unlike every oscillator-cross record in the pool (StochRSI-cross, KDJ, DSS, TSI, Schaff) this system never trades an oscillator cross for entry: the WVF series is a *permission-and-timing* device (extreme-then-resolve), and the entry trigger is bar geometry plus close-position, so legs fire on bars where every oscillator-cross system in the pool is silent. Unlike every breakout-follow record (Donchian, Darvas, Turtle-55d, NR7, BB-breakout) entries require the close to still sit *below* a 40-bar or 14-bar lookback close — the system buys only inside unresolved weakness, so clean new-high breakouts fire nothing by construction. Unlike stop-carrying records there is no protective leg: up to 9 same-direction adds can stack into a falling tape while the StochRSI exit stays mute, and adverse excursion has no guardrail beyond the exit cross. The edge, if any, lives in the documented contrarian intuition that released panic spikes on daily crypto bars snap back within the stochastic-exhaustion horizon — a bet on fear-mean-reversion with a chaperone (the regime test blocks buys into fresh strength), not on any trend, level, volume print, funding regime, or second timeframe.

## Signal

Exact rule as pinned (all 13 live inputs frozen — any other value is a different, unpinned rule):

- Declarations (source-faithful): long/flat machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long(1..9 units)}; no short leg ships anywhere — the short side is explicitly absent, not silently dropped.
- Live inputs (frozen): `Stochlength 14 / StochOverBought 80 / StochOverSold 20 / smoothK 3 / smoothD 3 / RSIlength 14 / RSIOverBought 70 / RSIOverSold 30 / pd 22 / bbl 20 / mult 2.0 / lb 50 / ph 0.85`. The remaining 15 inputs are display/alert/text-plot toggles (`false`/`true` as printed) plus `ltLB 40 / mtLB 14 / str 3` (live, fenced below) — the toggle block renders or alerts only and cannot change any order.
- WVF gauge (pinned arithmetic): `wvf(t) = (highest(close, 22)(t) − low(t)) / highest(close, 22)(t) × 100` — Larry Williams construction, highest-close anchor (not highest-high), normalized to percent. `sDev = 2.0 × stdev(wvf, 20)`; `midLine = sma(wvf, 20)`; `upperBand = midLine + sDev`; `lowerBand = midLine − sDev` (computed but read by zero order legs — fenced as dead); `rangeHigh = highest(wvf, 50) × 0.85`. Elevated test: `wvf >= upperBand or wvf >= rangeHigh` (either rail suffices).
- Resolution legs (pinned verbatim): `filtered(t)` = elevated(`t−1`) and `wvf(t) < upperBand(t)` and `wvf(t) < rangeHigh(t)` (was-true-now-false); `filtered_Aggr(t)` = elevated(`t−1`) and NOT(`wvf(t) < upperBand(t)` and `wvf(t) < rangeHigh(t)`) (was-true-still-true). Mutually exclusive on every bar by construction — no bar satisfies both.
- Price-action conjunctions (pinned verbatim): `upRange` = `low(t) > low(t−1)` and `close(t) > high(t−1)` (bar fully above prior high with rising low); `upRange_Aggr` = `close(t) > close(t−1)` and `close(t) > open(t−1)` (softer: up close clearing the prior body top). Strength: `close(t) > close(t−3)` (`str = 3`). Regime: `close(t) < close(t−40)` or `close(t) < close(t−14)` (`ltLB = 40`, `mtLB = 14` — weakness chaperone).
- Entry legs (pinned verbatim): `alert3(t)` = `upRange` and strength and regime and `filtered(t)` → `strategy.entry("Long", strategy.long)`; `alert4(t)` = `upRange_Aggr` and strength and regime and `filtered_Aggr(t)` → the same `strategy.entry("Long", strategy.long)` second call. Both legs are live, so a bar satisfying both adds two units in script order (alert3 first); adds beyond the 9th open unit are rejected no-ops under the pinned `pyramiding=9` default (see Execution assumptions). After any exit the next bar satisfying either conjunction enters immediately (no cooldown specified — explicitly none, not invented).
- Exit leg (pinned verbatim — the sole position-closing path): `k = sma(stoch(close, high, low, 14), 3)`; `d = sma(k, 3)`; `isOverBought(t)` = `crossover(k, d)(t)` and `k(t) > 80` → `strategy.close("Long")` closes the entire book (all stacked units) in one event. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Script order (pinned as coded): entries precede the close in the block, so a bar carrying both a fresh entry conjunction and the exit cross opens-then-closes within the same event — net flat by the close with costed fills (see Negative evidence). Deterministic by script order, never ambiguous.
- Display isolation: the three `plot(` calls and all text-plot/alert toggles render or signal only and cannot change any order; `col` (lime/gray) is bar-color plumbing with no order-leg read.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (WVF anchor, stochastic source, all strength/regime tests), `high` (upRange rail, stochastic range), `low` (WVF numerator, upRange rail, stochastic range), `open` (single read: `close > open[1]` inside `upRange_Aggr`). No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is both the stanza's verbatim `period` and a campaign timeframe — never presented as anything beyond that (see Limitations for the verbatim `basePeriod: 1h` label).
- Warmup: the deepest causal chain is `highest(wvf, 50)` stacked on `wvf`'s own `highest(close, 22)` seed (∼72 bars) plus the `close[40]` regime reference, so the first fully-seeded bar is ≈72 completed `1d` bars in; the exit chain (`stoch` 14 + double SMA) seeds far earlier. This record adopts an 80-bar warmup with pre-warmup bars flat by record rule, covering the seed with margin. No repainting, no negative shift, no future reference, no full-sample normalization; `highest`/`lowest`/`sma`/`stdev`/`stoch`/`rsi`/`crossover` are all causal recursions on completed bars.

## Execution assumptions

- Research market: BTCUSDT perps under the house overlay (the stanza's verbatim venue is `Futures_Binance BTC_USDT`; the rule reads completed-bar OHLC only, so venue transfer is mechanical — never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decisions with same-bar-close fills, 1:1 compatible with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no timing argument ships — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. Zero `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule; the only same-bar sequencing is the coded entry-before-close order (see Signal), which resolves deterministically.
- Sizing/capital: the source declaration carries `initial_capital=10000` and percent-of-equity quantity type but no quantity value, no commission, and no funding leg, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior. Historical funding is flagged per the house baseline: no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: `pyramiding=9` is set in the declaration (not defaulted): up to 9 same-direction `"Long"` adds may stack while positioned; the 10th and further same-bar/bars adds are rejected no-ops; the single `strategy.close("Long")` always liquidates the whole book; re-entry is allowed immediately on the next qualifying conjunction after any exit (no cooldown — explicitly none). Single engine position-id; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The long-only stance ports to perps or spot without structural change; there are no short legs whose venue permission could lapse.

## Evidence

### Source-reported

The canonical page ships the WVF-plus-StochRSI/RSI combination claim, the overbought-fall sell story, the sub-lower-band buy story, prose risk guidance (Bollinger mistuning, StochRSI false signals, conservative-miss risk, large-drawdown warning), and optimization wishes (parameter tuning, stops/targets, ML). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance. The mirror's `/*backtest*/` stanza prints a date window and venue but no result metrics of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the StochRSI overbought cross-close is the sole position-ending path by construction, and the code promises no stop or target.
2. Entry conjunctions are NOT mutually exclusive — and that is fenced, not fixed: `alert3` needs `filtered` (resolved) while `alert4` needs `filtered_Aggr` (still elevated), which exclude each other, but `upRange` and `upRange_Aggr` can co-print with strength+regime on one bar only when both WVF legs agree — impossible, since the WVF legs exclude each other. Hence at most one entry leg fires per bar (one add), proven by the WVF-leg exclusion. Resolved by code structure, never guessed.
3. Dead-indicator fencing (code governs, prose does not): `vrsi = rsi(close, 14)` is computed and read zero times by any order leg — the RSI block gates nothing; `StochOverSold = 20` is read zero times; `lowerBand` is computed and read zero times (the prose's sub-lower-band buy basis fires nothing — the coded buys are spike-resolutions, pinned); the `rangeLow`/lowest-percentile leg present in other WVF scripts ships nowhere here. None is silently adopted.
4. Prose-vs-code fence: the overview's "hidden bullish divergences" and "RSI determines long/short positions" describe machinery absent from the Pine block (no pivot/divergence detection, no short leg). This record follows the executable block; the prose claims are quoted as claims, never as rules.
5. Same-bar open-plus-close determinism: a bar carrying both a fresh entry conjunction and the exit cross executes entry-then-close in script order — net flat by the close with costed fills under the house overlay. Resolved by code order, never guessed.
6. Flat-state determinism: `strategy.close("Long")` with no open position is a no-op; pre-seed bars (`na` in any `highest`/`sma`/`stdev`/`stoch` seed or any `[40]` reference) satisfy no order condition by themselves, since Pine comparisons against `na` are false.
7. The window (stanza dates), the `1d` frame, the 13 live inputs, `pyramiding=9`, both conjunctions, the single exit, and the no-stop posture are pinned, not removed: retuning any lookback/threshold, adding a stop/target/cooldown/session filter, enabling a short leg, or widening `upRange` to touches would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the 80-bar warmup, and house sizing/costs — all predeclared above; every edge, input, default, ordering, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: WVF(22,20,2.0,50,0.85) / resolution conjunctions / price-action chaperones / `pyramiding=9` / StochRSI(14,3,3,80) exit / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — WVF relevance: entering on the price-action conjunctions alone (upRange/upRange_Aggr + strength + regime, WVF legs forced true) must not improve net expectancy; fail ⇒ the fear-spike-resolution filter adds nothing over bare weakness-with-a-pulse buying.
- F2 — Exit relevance: closing each long book exactly 10 bars after entry (time exit) instead of the coded StochRSI overbought cross must not improve net expectancy; fail ⇒ the exhaustion exit adds nothing over a blind clock.
- F3 — Chaperone relevance: dropping the regime test (`close < close[40] or close < close[14]`) while keeping everything else must not improve net expectancy; fail ⇒ the weakness chaperone adds nothing over buying every resolved spike.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The OHLC-only long-only logic ports to perps or spot without structural change; there are no short legs, no funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond the single `close > open[1]` body test, so session-gap behavior is simply absent rather than approximated. The WVF gauge is explicitly marketed by its lineage as venue-agnostic (no options data), and the stanza's own venue is Binance futures — transfer is mechanical. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open; this record executes same-bar-close. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Stanza label: the mirror prints `basePeriod: 1h` alongside `period: 1d` (quoted verbatim, never normalized); this record decides and fills on completed `1d` bars only.
- No price stop: adverse excursion after entry has no guardrail beyond the StochRSI cross; a vertical-against move with mute %K is held to the exit cross, and up to 9 adds can stack into the fall — the coded cost of the design, disclosed, not smoothed.
- Exit can sleep: `crossover(k, d)` needs a *fresh* cross above 80 — a grind that pins %K high without re-crossing, or chop that never reaches 80, holds the book indefinitely; flat stretches and long-held pyramided books are both in-sample behaviors, not bugs.
- Infrequent setups by construction: a 50-bar-percentile fear extreme that resolves the very next bar, jointly with rising-low bar geometry and below-lookback closes, is a rare daily event; evaluation windows contain long flat stretches.
- Performance evidence is absent: the canonical page and mirror report no numbers at all; nothing here is calibrated, fitted, or tuned to any backtest. The stanza window (2022-09-21 to 2023-09-27) is a quoted label, not a claimed result.

## Implementation status

Not implemented. No Hummingbot/Qlib/n8n execution, no Paper/Testnet/Live run, no parameter tuning, no independent reproduction — per the Scout contract the record stops at admission review.

## Adoption boundary

Research-only, not approved for any adoption scope. A PASS here means admissibility to model-consistent research under the pinned Hummingbot benchmark — not profitability, not Qlib parity, not Paper/Testnet/Live permission. Any downstream use requires its own separate authorization outside this repository's admission lane.

## Related Wiki records

None — per the Scout contract no Wiki Brain write is performed in this lane.

## Sources

- FMZ canonical strategy page (primary rule prose + backtest stanza): https://www.fmz.com/strategy/428088
- Immutable code mirror (primary executable rule, commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `Williams-VIX修复策略Williams-VIX-Fix-Strategy.md`): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Williams-VIX修复策略Williams-VIX-Fix-Strategy.md
- Larry Williams VIX Fix lineage (synthetic-volatility construction, 22/20/2.0/50/0.85 defaults): https://www.tradingview.com/script/bBCjDnFN-CQ-A-Larry-Williams-Vix-Fix-V4-Tops-Bottoms-Histogram
