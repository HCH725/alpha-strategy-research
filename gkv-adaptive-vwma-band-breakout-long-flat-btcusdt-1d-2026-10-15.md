---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Garman-Klass adaptive VWMA band breakout long-flat on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-12-20
sources:
  - https://www.fmz.com/strategy/475603
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Garman-Klass adaptive VWMA band breakout long-flat on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-15):

- Canonical strategy page: https://www.fmz.com/strategy/475603 (`Adaptive VWAP Bands with Garman-Klass Volatility Dynamic Tracking Strategy`, porter-side author stamp `ChaoZhang` in the mirror header, `Created : 2024-12-20 14:51:00`). Fetched live over HTTPS during this cycle (HTTP 200, 714422 bytes of landing HTML). Stripped-text census: `Garman` 19 / `475603` 21 / `vwma` 1 / `vwapStdDev` 3 / `strategy.entry` 1 / `strategy.close` 1 / `Sharpe` 0 / `Win Rate` 0 / `Max Drawdown` 0 / `Annualized` 0 / `Profit Factor` 0 / `夏普` 0 / `胜率` 0 / `回撤` 0 / `净利润` 0. The 14 `backtest` hits are the ported `/*backtest ... */` stanza text and page UI labels (strategy-parameters / copy-and-backtest chrome), never a result table. The page ships no performance numbers of any kind. The executable Pine ships behind the page's code gate, so every code-line fact below comes from the immutable mirror, and every page fact (title, Created stamp, zero performance tokens) was verified live on the landing HTML.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies at full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` during this cycle), exact file path `自适应VWAP波段基于Garman-Klass波动率动态跟踪策略-Adaptive-VWAP-Bands-with-Garman-Klass-Volatility-Dynamic-Tracking-Strategy.md` (6686 bytes, blob SHA `975f810f1dabb87d9964b2e8deac9baa88b59a46` — the GitHub contents API at the pinned HEAD returns the identical `sha`/`size`, and `git hash-object` on the re-download reproduces it). The mirror prints `> Name` = the full Chinese-English title, `> Author` = `ChaoZhang` (mirror porter), the bilingual strategy prose (thesis, principle, advantages, risks, optimisation directions, summary), the FMZ backtest stanza (`start: 2019-12-23 08:00:00`, `end: 2024-12-18 08:00:00`, `period: 1d`, `basePeriod: 1d`, `Futures_Binance BTC_USDT`), and the complete `//@version=5` Pine block quoted below. `> Last Modified` = `2024-12-20 14:51:00` (adopted as `source_as_of`).
- Text census over the pinned Pine block: 1 `strategy(` (title/`overlay=true` only — 0 `initial_capital`, 0 `commission`, 0 `default_qty_*`, 0 `pyramiding`, 0 `process_orders_on_close`, 0 `calc_on_every_tick`, recorded as absent, never as evidence) / 2 `input.int` (`Volatility Length` 25, `VWAP Length` 14) + 1 `input.float` (`Volatility Multiplier` 1.0) / 1 `strategy.entry` (`"Long"`/`strategy.long`) / 1 `strategy.close` (`"Long"`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `strategy.short` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 1 `ta.vwma(` / 1 `ta.stdev(` / 1 `ta.sma(` / 1 `math.sqrt(` / series reads: `high`/`low`/`close`/`open` in the Garman-Klass loop, `close` in VWMA/stdev, `volume` inside `ta.vwma` — 0 `security(`/`request.*`/`timeframe(`/`time`/`barstate`/`timenow`. The `var float sum_gkv` accumulator is reset to `0.0` on every bar before the loop (no cross-bar state — disclosed); the three `plot` calls and `barcolor` are display-only.

Licence and rights: the pinned file is a public port of a publicly listed FMZ strategy release. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market pin `BTCUSDT` Binance futures `1d` (the stanza already backtests `Futures_Binance BTC_USDT` at `period: 1d` with `basePeriod: 1d` — venue, frame, and granularity are kept, so only the symbol spelling and the futures-long/flat permission reading are disclosed here, never presented as source-native; no frame transfer exists in this record); (2) same-bar-close market fills (the source evaluates per completed bar and fills at the next bar under Pine defaults — no `process_orders_on_close` ships anywhere; this record pins completed-bar decision with same-bar-close execution, predeclared); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the 49-bar multiplier seed plus VWMA/stdev seeding plus Pine partial-window caution, see Required data); (4) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `25` / `14` / `1.0` constants, the Garman-Klass loop, the VWMA(14) center, the `stdev(close,14)` width, the `gcv/sma(gcv,25)` adaptive multiplier, the level-based long entry, the lower-band `strategy.close` exit, and the long-only no-stop-no-target posture are source-verbatim. **No Safety Order, no DCA event, no pyramiding, no short leg, and no second leg is admitted in this record's version** — the admitted machine holds at most one long leg; the house BO/SO/SO DCA matrix is a downstream experiment, never part of this admission.

Pre-write dedup (2026-10-15): working-tree case-insensitive searches for `garman`, `klass`, `475603`, `adaptive-vwap`, and `adaptive vwap` return zero strategy records using this source, author page, estimator, or rule. `vwma` hits in six pool files are incidental mentions inside unrelated census/comparison prose (CCI-threshold, EHMA-band, Flying-Dragon, StochRSI-KD, Ultimate-Oscillator, VCTS records — none centers any signal on VWMA). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — per-PR file lists checked live, zero `garman`/`klass`/`vwma`/`475603`/`vwap-band` tokens in any of them. Closest pool records are different mechanism classes: `vwap-bounce-band-reversal-two-sided-btcusdt-1h-2026-10-12.md` anchors on session `ta.vwap` with fixed ±0.5% bands, an EMA50 trend gate, touch-reversal entries, a midline exit, and two-sided posture (different center, fixed width, gated reversal, different exit, different direction); `bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md` breaks an SMA(20) ± 1.5σ price envelope with a midline exit (no volume anywhere, fixed multiplier, different exit); `ehma-range-band-breakout-btcusdt-1d-2026-10-05.md` breaks EHMA(180) ± fixed 2% (different smoother, fixed width, no OHLC estimator). No pool record uses a Garman-Klass OHLC volatility estimator, and none scales a volume-weighted band by volatility-relative-to-its-own-mean.

## Economic mechanism

### Source-reported

Volatility-adaptive trend tracking: the author's prose states the thesis directly — VWAP is the price pivot, close-price standard-deviation bands are drawn around it, and the Garman-Klass estimator (which reads open, high, low, and close, hence "more accurate than traditional volatility") dynamically scales the band width. Price breaking above the upper band opens long; breaking below the lower band closes to cash. Higher volatility raises the breakout bar, lower volatility lowers it, which "effectively avoids false breakouts". The author lists ranging-market over-trading, parameter sensitivity, and slow reaction to violent reversals as the known risks, and its stop-loss / trend-filter / multi-timeframe suggestions are generic advice prose, never coded rules — none is adopted here.

### Research interpretation

Level-state breakout machine with an adaptive threshold, long/flat only. Unlike fixed-width breakout systems (EHMA ± 2%, Bollinger ± kσ) where the trigger distance is a constant multiple of dispersion, here the multiple itself breathes with the market: the Garman-Klass reading relative to its own 25-bar mean widens the bands exactly when OHLC-estimated volatility runs hot and tightens them when it runs cold — so the entry bar is quoted in units of *current* volatility regime, not in fixed sigma. Unlike session-anchored VWAP systems (fixed-percentage rails, reversal entries, trend gates), the center here is a rolling 14-bar volume-weighted mean with no session reset and the trigger is a plain level break with no gate — every completed-bar close above the upper rail while flat opens, every close below the lower rail while long closes, and the between-band zone holds. The price of the wide lower-band exit is riding full adverse excursions; the price of the adaptive width is that volatility spikes push the entry bar further away precisely when momentum looks strongest. The bet is on volatility-normalized persistence of VWMA-rail breaks, never on a squeeze, level, calendar, divergence, or volume-spike print.

## Signal

Exact rule as pinned (`Volatility Length = 25`, `VWAP Length = 14`, `Volatility Multiplier = 1.0` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open long leg; state ∈ {flat, long}; flat exists before the first signal, between signals, and throughout the warmup. No Safety Order, no DCA event, no pyramiding — explicitly none admitted here, not invented.
- Volatility block, pinned verbatim: `sum_gkv(t) = Σ_{i=0..24} [ 0.5 × ln(high[i]/low[i])² − (2×ln2 − 1) × ln(close[i]/open[i])² ]` (recomputed from scratch each bar — the accumulator is zeroed before the loop, so no hidden cross-bar state); `gcv(t) = sqrt(sum_gkv(t) / 25)`; `multiplier(t) = ( gcv(t) / sma(gcv, 25)(t) ) × 1.0`.
- Band block, pinned verbatim: `vwap(t) = ta.vwma(close, 14)(t)` (volume-weighted MA of closes); `vwapStdDev(t) = ta.stdev(close, 14)(t)` (Pine v5 biased/population stdev of closes); `upperBand(t) = vwap(t) + vwapStdDev(t) × multiplier(t)`; `lowerBand(t) = vwap(t) − vwapStdDev(t) × multiplier(t)`.
- Entry long, pinned verbatim (level semantics, not an edge — every qualifying bar re-asserts): `close(t) > upperBand(t)` → open long (from flat; while already long the re-issued entry is a no-op under the Pine default no-pyramiding construction — explicitly no adds, not invented).
- Exit, pinned verbatim (the sole close path — 0 `strategy.exit` legs anywhere): `close(t) < lowerBand(t)` → `strategy.close("Long")` (flat when already flat — no-op, not a short).
- Middle zone: `lowerBand(t) ≤ close(t) ≤ upperBand(t)` (either equality included) → no action, state holds. Exact-touch determinism: equality on either rail fires nothing.
- Exits/risk: the lower-band close only. No stop, no target, no trailing, no time exit, no midline exit, no neutral-return rule — explicitly none by record rule, not invented. A long leg whose lower-band print never arrives is held indefinitely.
- Direction: long-only with an explicit flat state (0 `strategy.short` tokens anywhere; a two-sided reading would contradict the shipped code).
- Priority: the `if / else if` chain plus `upperBand(t) ≥ lowerBand(t)` construction means no bar can satisfy both legs (strictly exclusive unless both bands are `na`, in which case both comparisons are false and the bar holds — disclosed, never traded).

## Required data

- Completed `1d` bars of BTCUSDT: `open`/`high`/`low`/`close` (Garman-Klass loop) plus `volume` (inside `ta.vwma`). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (the Pine logic contains no timeframe constant and zero `security(`/`request.*` calls — single-frame by construction; the stanza `period: 1d` / `basePeriod: 1d` is kept, not transferred).
- Warmup: the binding cost is the multiplier seed — `gcv` needs 25 bars and `sma(gcv,25)` needs 25 `gcv` values, so the first fully-formed multiplier sits at the 49th bar; VWMA/stdev need 14 bars. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — full 49-bar seed plus wide margin; no signal before bar 61 may trade). No repainting (`calc_on_every_tick` unset so Pine evaluates per completed bar; every comparison reads the current completed bar only), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Every input is complete at bar `t`'s close — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (stanza venue affinity `Futures_Binance BTC_USDT` kept at stanza-native `1d`; symbol spelling and long/flat permission disclosed in Provenance, never presented as source claims).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `qstick-zero-cross-trend-two-sided-btcusdt-1h`, `imi-50-midline-cross-flip-two-sided-btcusdt-1d`, `macd-signal-cross-reversal-btcusdt-1d`, `ppo-signal-cross-reversal-two-sided-btcusdt-1d`, and `bollinger-band-breakout-long-midline-exit-btcusdt-1d` PASS records (single-frame completed-bar decision, same-bar-close market fill, single-position machine, no protective stop/limit legs anywhere in the derived machine, hence no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open, or close). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record.
- Sizing/capital/costs: the source ships no portable economics (no quantity, capital, or commission argument — recorded as absent economics, never as zero-cost evidence) — derived evaluation carries the fixed, reproducible house research cost model (Base 6% + Safety 6% + Safety 6% notional framing, Isolated, 3x/5x; pinned house cost assumptions for fees plus modeled funding — no hypothetical zero funding claimed, never presented as source-native behavior). Funding is modeled, never reported as realized or canonical funding; no historical-funding settlement path is required or claimed for this version. No Safety-Order/DCA event participates in the admitted trigger machine regardless of downstream campaign settings.
- Concurrency: single-position machine — at most one open long leg; same-state bars while positioned are no-ops; re-entry is allowed on the next `close > upperBand` bar after any close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (Garman-Klass summation loop with lengths, `ta.vwma(close,14)`, `ta.stdev(close,14)`, the `gcv/sma(gcv,25)` multiplier, both rails), the level-based long entry and lower-band `strategy.close` exit with their order ids, the `overlay=true` plots, the bilingual thesis/principle/risk prose, the author/date header, and the stanza. The FMZ page and both code sources ship zero performance numbers (page-wide census above: zero Sharpe/win-rate/drawdown/annualized/profit-factor tokens in either language; the mirror's only image is an undecorated upload asset, performance content unread — no numbers transcribed, never a source fact here), so this record carries zero source-reported performance numbers and claims no performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance to carry, admitted plainly: unlike paper-sourced records with backtest tables, the rule sources ship construction, triggers, and prose context only — there is no expectancy number anywhere to fence, and this record claims none.
2. Long-only posture provably complete: 0 `strategy.short` tokens and the sole close path is `strategy.close("Long")` — no third direction exists, and a two-sided reading would contradict the shipped code (unlike touch-reversal VWAP systems that re-enter against the rail).
3. No hidden exits or risk layer: the traded machine names no stop, no target, no trailing, no time exit, no midline exit anywhere — the no-stop/no-target posture is the record rule, explicitly none, never hidden. The prose "risk control suggestions" (set stop-loss, add trend filters, multi-timeframe analysis) are uncoded generic advice and are adopted by nothing. Every adverse excursion is held to the lower-band close.
4. Level-trigger exclusivity proved: entry needs `close > upperBand` while exit needs `close < lowerBand` on the same bar — with `upperBand ≥ lowerBand` by construction no bar satisfies both, so no priority rule beyond the shipped `if/else if` is needed or invented; `na` bands satisfy neither and hold.
5. `na`/seed determinism fenced: before seeding, Pine partial-window `ta.*` values and any `na` multiplier propagate `na` comparisons that are false, so no edge can fire — and the adopted 60-bar flat absorbs all seeding structurally regardless of the partial-window behavior. A zero `sma(gcv,25)` divisor, a negative GK sum under `math.sqrt`, or a zero-volume VWMA window all resolve to `na` bands and a deterministic hold (disclosed, not smoothed). No seeded or `na` value ever trades.
6. Dead code fenced: the three `plot` calls, `barColor`, and `barcolor()` are display-only; the `var float sum_gkv = na` initializer is overwritten by the per-bar `:= 0.0` reset before any read. None gates anything.
7. Estimator/center/width-family overlap fence, admitted plainly: the pool's price-envelope records trade fixed-multiple rails off SMA/EHMA centers with midline or touch exits; the pool's VWAP record anchors on session `ta.vwap` with fixed-percentage rails, a trend gate, and reversal entries; the pool's volatility records trade ATR, standard-deviation, or RVI constructions, never an OHLC Garman-Klass estimator. Shared `VWAP`/`band` vocabulary is not shared signal: this record's `VWMA(14) ± stdev(close,14) × gcv/sma(gcv,25)` with a lower-band close exit exists nowhere else in the pool.
8. Economics absence fenced: 0 quantity/capital/commission arguments — the record carries house sizing/costs only as a predeclared derivation, never as a source claim.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTC_USDT`→`BTCUSDT` symbol spelling with the futures long/flat permission reading, the per-completed-bar level evaluation with same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs with no admitted Safety-Order/DCA event — all predeclared above; the 25/14/1.0 constants, the GK loop, the VWMA center, the stdev width, the adaptive multiplier, the entry/exit pair, the single-position guards, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, length, multiplier, center, width, trigger set, or timing of the source passes.
10. Division of evidence disclosed: the formula, lengths, order ids, dead code, stanza, and prose above were byte-verified in the pinned mirror file (6686 bytes, blob SHA recorded, contents-API `sha`/`size` matched, `git hash-object` identical); the title, Created stamp, and zero-performance census were byte-verified in the fetched FMZ landing page (714422 bytes, HTTP 200). The division is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `25` / `14` / `1.0` / Garman-Klass loop / VWMA center / `stdev(close,14)` width / `gcv/sma(gcv,25)` multiplier / level-break long entry / lower-band close exit / no-stop-no-target posture / long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Adaptive-multiplier relevance: replacing the GK multiplier with the constant `1.0` (plain VWMA ± σ band, same entry/exit handling) must not improve net expectancy; fail ⇒ the volatility adaptation adds nothing over its fixed-width component.
- F2 — Volume-center relevance: replacing the VWMA(14) center with SMA(14) (same GK multiplier, same bands, same handling) must not improve net expectancy; fail ⇒ volume weighting adds nothing over an ordinary mean.
- F3 — Wide-exit relevance: exiting at a center reclaim (`close < vwap`) instead of the lower band (same entry) must not improve net expectancy; fail ⇒ the wide lower-band exit is dominated by a midline exit on this market.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (stanza-venue affinity kept at stanza-native `1d`, no frame transfer — disclosed). The rule reads completed daily OHLCV only, so no open-print, session, or cross-venue difference can touch any order-gating line beyond each calendar-day bar's own prints — but spot-vs-perp prints can still differ structurally (funding-driven drift, venue aggregation, and especially volume prints feeding VWMA), so the futures-venue pin is load-bearing and disclosed. Lengths and multiplier are fixed bar-count constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is long-only with a cash-flat state, so a spot-only deployment expresses the full machine wherever shorting is unavailable — full futures expression is assumed only for the pinned venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each bar's own OHLC (no session gating anywhere; the GK loop treats each daily bar's internal range identically); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No source economics: the source ships no quantity, capital, commission, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the lower-band close, which may arrive many bars later or after deep excursion; a leg whose lower-band print never arrives is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Ranging-market churn: the author's own risk list warns of frequent trading in oscillation — alternating upper-break entries and lower-break exits grind through repeated round trips with no flat state to rest in, by the prescribed design.
- Adaptive-width lag: volatility spikes widen the bands precisely when momentum looks strongest, so entries arrive strictly after the volatility-normalized turn by construction; violent reversals may print the exit late, as the author warns.
- Volume-print dependence: the VWMA center inherits venue volume-print differences (spot vs perp, wash, outages) — a corrupted volume window moves the center and both rails deterministically; no volume-quality guard ships anywhere.
- Seed convention cost: Pine partial-window values before bar 49 are structurally excluded by the adopted 60-bar warmup (which is wider than any code-enforced seed) — early-bar behavior differences between seeding conventions never trade here.
- Next-bar timing reading: the same-bar-close fill is a predeclared derivation from Pine's default next-bar fills; any engine that modeled entries at the next open would trade different (slightly later) events.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page, Adaptive VWAP Bands with Garman-Klass Volatility Dynamic Tracking Strategy (Created 2024-12-20, zero performance claims — verified live in the fetched landing page during this cycle): https://www.fmz.com/strategy/475603
