---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: T3 Tillson channel-breakout latched two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-14
sources:
  - https://www.fmz.com/strategy/426786
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/T3%E5%9D%87%E7%BA%BF%E9%80%9A%E9%81%93%E7%AA%81%E7%A0%B4%E7%AD%96%E7%95%A5T3-Moving-Average-Channel-Breakout-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# T3 Tillson channel-breakout latched two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/426786 (page title carrying `T3 Moving Average Channel Breakout Strategy`, author token `Trader_7ye` and strategy token `T3MA_KC` present page-wide). Fetched live over HTTPS during this cycle with HTTP 200 (744070 bytes). The page's ZH/EN prose states the rule twice: one T3 average as midline, upper band = average plus range, lower band = average minus range, long when price breaks above the upper band, short when price breaks below the lower band, background-colour trend aiding judgement. The page-embedded `/*backtest*/` header reads `start: 2022-09-07 00:00:00`, `end: 2023-04-15 00:00:00`, `period: 4d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Profit Factor` 0, `Max Drawdown` 0, `Win Rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2023-09-14 from the mirror's `> Last Modified` stamp 2023-09-14 15:51:25).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800; repository head verified via the GitHub commits API — the same head pin as the merged Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray, ActionZone, Fibonacci, FRAMA and Balance-of-Power admissions), exact file path `T3均线通道突破策略T3-Moving-Average-Channel-Breakout-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 4690 bytes, blob SHA `7b3dd84dc7c71d3e7c04454b49621747ce4848dc` (verified against the GitHub contents API at the pinned commit — size and SHA both match; byte-identical to a fresh `master` fetch). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/426786, and its `[trans]` prose matches the canonical page text quoted above. The executable Pine block carries its own header `// © Trader_7ye` under MPL-2.0.
- Full `//@version=4` block read in full (70 Pine lines, `strategy(title="T3MA_KC_7ye  Strategy", shorttitle="T3MA_KC_7ye  Strategy", max_bars_back=500, overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=5000, currency=currency.USD)`). The executable order block is the `t3()` six-EMA definition, the `Length`/`xPrice` inputs, the midline plus range-channel arithmetic, the slope-and-position conjunctions, the `direction` latch, the two flip detectors, and the two guarded entries: `if (alertlong)` → `strategy.entry("Long", strategy.long)`; `if (alertshort)` → `strategy.entry("Short", strategy.short)`. Everything else is display-only (`plot`/`fill`/`bgcolor` — feeding no order condition).
- Text census over the pinned code block: 1 `strategy(` / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`, both inside single-`if` guards, no `when=`/`qty=`/`limit=`/`stop=` qualifiers) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `barstate` / 0 `timenow` / 0 `ta.` (v4 built-in `ema()` only) / 0 `crossover` / 0 `crossunder` / 0 `nz(` / 0 `var` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `calc_on_every_tick` / exactly 2 `input(` (`Length = input(..., defval=24, minval=1)`, `xPrice = input(..., defval=close)`). The `initial_capital=5000` / `default_qty_value=100` / `strategy.percent_of_equity` economics line is recorded as an absent portable-economics stub, never as cost evidence.
- No risk layer ships anywhere in the source: zero close/exit/risk legs. Reversal through the opposite entry is therefore the only coded position-closing path, pinned as written (declared explicitly, never hidden), not a researcher invention.

Licence and rights: the executable block ships an MPL-2.0 header (`© Trader_7ye`) via the public FMZ publication; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; the mirror's executable `/*backtest*/` stanza backtests `Futures_Binance BTC_USDT` at `basePeriod: 1d` — this pin follows that stanza, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 150-bar warmup with pre-warmup bars flat by record rule (covers the six-fold nested EMA(24) cascade on both the price and range chains with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The Tillson coefficients, `Length = 24`, `xPrice = close`, the strict slope-and-position conjunctions, the `direction` latch with flip-only entries, the full-reversal exit path, and the no-stop/no-target/no-cooldown stance are source-native and unmodified. No tie-break had to be invented: the source calls no `cross`/`crossover` function anywhere — every comparison is a strict inequality or a latch equality test with a single deterministic outcome per bar (see Negative evidence).

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `t3ma`, `tillson`, `trader_7ye`, `426786`, and word-boundary `T3` return zero strategy records using this source, author script, indicator, or construction — no `main` record evaluates a Tillson T3 average anywhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. All 122 closed PRs reviewed by title contain no T3/Tillson record. Closest pool records are different mechanism classes: `tema-dema-hma-cross-trend-two-sided-btcusdt-1d` crosses three unrelated averages (TEMA/DEMA/HMA — none is the six-EMA Tillson linear combination, and it has no channel, no slope gate, no latch); `keltner-momentum-breakout-gated-btcusdt-1d` breaks an EMA ± ATR-multiple band (its width is a volatility multiple, never a T3-smoothed bar range, and its trigger has no slope conjunction or latched state); `donchian-20-10-breakout-btcusdt-1h` breaks highest-high/lowest-low rails (no average at all); `sideways-dmi-bollinger-breakout-long-btcusdt-4h` breaks standard-deviation bands. No pool record computes a Tillson T3, smooths the bar range through the same T3, or latches direction across bars with flip-only entries.

## Economic mechanism

### Source-reported

Low-lag trend capture on a self-smoothed channel (mirror prose plus code): the Tillson T3 (a fixed-coefficient linear combination of six nested EMAs with `b = 0.7`) tracks price with less lag than any single constituent average, while the band width is the same T3 applied to the bar's own travelled range — so the channel breathes with recent bar size rather than with a volatility multiple. A long is prescribed only when two facts agree on the same bar: the midline is rising AND the bar's average price (`ohlc4`) prints above the upper band — momentum direction plus positional confirmation. The mirror short leg is the exact image. The `direction` latch then holds the posture through any bar that fails the opposite conjunction, so exits need no target: the design bets that a T3-slope-confirmed band break resolves further in the break direction, and that the opposite flip — not a level — is the timely exit. There is no stop, no target, no flat-holding logic beyond the pre-first-flip flat.

### Research interpretation

Slope-and-position breakout system, two-sided, latched, always-in-market after the first flip. Unlike naked-cross records, the trigger has two bouncers that must agree: slope alone (rising T3 inside the channel) moves nothing, and position alone (overbought print on a falling midline) moves nothing — only their conjunction flips the latch, so chop that lifts price without turning the average, and drift that turns the average without reaching the band, both sit out. Unlike threshold-cross oscillators, there is no mid-zone and no re-entry event: after the first flip the book is always positioned, and same-state bars are structural no-ops (the flip detectors fire only on latch change, so pyramiding semantics are unreachable by construction, not by parameter). The price of the latch is commitment: a leg whose opposite conjunction never prints is held indefinitely, and alternating flips print full reversals with no resting flat. The bet is on low-lag slope-plus-breakout turns, not on any second average, volatility multiple, volume print, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`Length = 24`, `xPrice = close`, `b = 0.7` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; flat exists only before the first flip — after the first `alertlong`/`alertshort` the latch is 1 or −1 forever and the book is always positioned.
- Tillson T3, pinned verbatim (`b = 0.7`; `c1 = −b³ = −0.343`; `c2 = 3b² + 3b³ = 2.499`; `c3 = −6b² − 3b − 3b³ = −6.069`; `c4 = 1 + 3b + b⁴ + 3b² = 4.8101`): `xe1 = ema(src, 24)` … `xe6 = ema(xe5, 24)` (v4 built-in `ema` recursion, once per completed bar); `t3(src) = c1·xe6 + c2·xe5 + c3·xe4 + c4·xe3`. Midline `T3ma = t3(close, 24)`; `range = high − low`; `rangema = t3(range, 24)`; `upper = T3ma + rangema`; `lower = T3ma − rangema`.
- Slope and position, strict inequalities (every outcome deterministic — no `cross` call exists to need a tie-break): `upCol ⟺ T3ma(t) > T3ma(t−1)`; `downCol ⟺ T3ma(t) < T3ma(t−1)`; `buySignal ⟺ upCol ∧ ohlc4(t) > upper(t)`; `sellSignal ⟺ downCol ∧ ohlc4(t) < lower(t)`. An exactly-flat midline bar satisfies neither slope leg (latch holds); an `ohlc4` print exactly on a band fails the strict test (no flip). `buySignal`/`sellSignal` are mutually exclusive on every bar (their slope legs are opposite strict inequalities on the same pair).
- Latch and entries (pinned verbatim, flip-only): `direction(0) = 0`; `direction(t) = buySignal ? 1 : sellSignal ? −1 : direction(t−1)`; `alertlong ⟺ direction(t) ≠ direction(t−1) ∧ direction(t) = 1` → `strategy.entry("Long", strategy.long)`; `alertshort` mirrored → `strategy.entry("Short", strategy.short)`. From flat the first flip opens the leg; from the opposite leg the entry reverses in full as a single atomic reversal event (Pine opposite-side entry semantics); refires while already positioned are structurally impossible (the detector requires a latch change). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (zero close/exit/risk legs ship anywhere), explicitly none, not invented.
- Direction: two-sided with pre-first-flip flat only. A long-only or short-only reading would contradict the prescribed `"Short"` leg; each is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (midline source), `high`/`low` (range chain), `ohlc4` (position test). No `open` (except inside `ohlc4`), no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the executable header's `basePeriod: 1d`; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the six-fold nested EMA(24) cascade, run on both the price chain and the range chain (≈ six time-constants ≈ 144 bars to settle). The adopted warmup is the first 150 completed `1d` bars flat by record rule (predeclared researcher choice — covers both cascades plus margin; no traded bar reads a seeded value). `max_bars_back = 500` ships in the declaration and only widens Pine history reservation — the rule's deepest explicit reference is `[1]`, so the warmup, not the reservation, binds. No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's OHLC enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin following the executable header's `Futures_Binance BTC_USDT` at `basePeriod: 1d` — venue transfer and symbol spelling are disclosed here, never presented as source-native). Full two-sided expression assumes a futures venue; a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the two flip detectors are mutually exclusive per bar, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics (100% of equity at `initial_capital=5000` with no commission, slippage, or funding argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine by latch construction — at most one open leg; the flip detectors fire only on latch change so same-state bars and same-side refires are structurally impossible (no `pyramiding` ships anywhere and none is needed — the value is unreachable); the opposite flip reverses in full as one atomic event; re-entry is allowed on the next fresh flip after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (six-EMA Tillson definition with `b = 0.7`, `Length = 24`, `xPrice = close`, the T3-smoothed range channel, the strict slope-and-position conjunctions, the `direction` latch with flip-only `"Long"`/`"Short"` entries, `max_bars_back = 500`), the active `strategy(...)` declaration titled `T3MA_KC_7ye  Strategy`, and the `/*backtest*/` stanza (2022-09-07→2023-04-15, `Futures_Binance BTC_USDT`, `basePeriod: 1d`) — quoted in Provenance. It ships no portable performance: no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the body contains zero `strategy.close` / `strategy.exit` / `strategy.order` legs and zero `stop=`/`limit=` qualifiers; the only position-closing path is the opposite-side `strategy.entry` reversal on the next flip. The no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. Flip exclusivity fenced: `buySignal` requires `T3ma(t) > T3ma(t−1)` while `sellSignal` requires `T3ma(t) < T3ma(t−1)` — opposite strict inequalities on the same pair — so no bar fires both detectors, no priority rule is needed or invented (the latch ternary's first-match order is never contested), and no bar produces both an open and a reversal.
3. Same-side refire structurally impossible, stated plainly: `alertlong`/`alertshort` each require `direction(t) ≠ direction(t−1)`, so after a flip the latch must change again before another entry on that side can print — consecutive same-side entries cannot occur on any bar sequence. Pyramiding semantics are unreachable by construction; the absent `pyramiding` argument changes nothing.
4. Flat-midline and on-band determinism fenced: `T3ma(t) == T3ma(t−1)` satisfies neither slope leg (latch holds by the ternary fall-through); `ohlc4` exactly equal to one band fails the strict `>`/`<` test (no flip). Both outcomes fall directly out of the quoted strict inequalities — no researcher tie-break, no alternative reading.
5. Latch-seed fence, stated plainly: `direction` is declared `0` and `direction[1]` is `na` on the first bar, so `direction ≠ direction[1]` evaluates to `na` (false in the `if` guard) — no flip can print before real bars exist; combined with the record-rule 150-bar warmup flat, no seeded value ever trades.
6. No division, no `na` propagation path: the T3 is a pure linear combination (no quotient anywhere — unlike channel-normalized oscillators there is no zero-divisor bar); `high − low ≥ 0` always, and a zero-range bar simply narrows the channel to the midline while every test stays strict and deterministic. No guard invented because none is needed.
7. No future leakage in the stack, stated plainly: at decision bar `t` the slowest inputs are completed closes/highs/lows through bar `t` (both six-EMA cascades resolve long before the 150-bar warmup ends) — every input is complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `time` read at all, no `barstate`-gated path. All `plot`/`fill`/`bgcolor` calls render only and drive no order.
8. HLC data fence, admitted plainly: unlike close-only records, the order-gating chain reads venue `high`/`low` (range width) and `ohlc4` (position test) — venue bar-construction differences can touch `rangema`, both bands, and the position test. A venue that cannot supply completed HLC daily bars cannot trade the pinned rule; extension to heikin-ashi or otherwise resampled feeds would be a different, unpinned rule.
9. Always-in-market posture provably complete: after the first flip the latch is ±1 forever with symmetric flip-only entries on both legs — the book is long or short on every post-warmup bar. No third direction exists; the flat state exists only pre-first-flip.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 150-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the Tillson coefficients, `24`/`close` inputs, the range-channel arithmetic, the strict conjunctions, the latch with flip-only entries, the full-reversal exit path, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (blob SHA recorded, re-fetched at the pinned SHA with identical bytes); the FMZ canonical page verified live the title, the `Trader_7ye`/`T3MA_KC` tokens, the ZH/EN rule prose, and the `Futures_Binance BTC_USDT` backtest stanza — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Tillson `b = 0.7` / `Length = 24` / `close` source / T3 range channel / strict slope-and-position conjunctions / latch with flip-only entries / full reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Channel relevance: dropping the band-position conjunctions (naked T3-slope latch flips, same entries) must not improve net expectancy; fail ⇒ the T3-smoothed range channel adds nothing over the bare slope.
- F2 — Slope-gate relevance: dropping the slope legs (band-position-only flips: `ohlc4` outside the band sets the latch) must not improve net expectancy; fail ⇒ the midline-slope agreement adds nothing over positional breaks alone.
- F3 — Short-leg relevance: disabling the short leg (long-only with the same slope-and-position entries, closing to flat on the short flip) must not improve net expectancy; fail ⇒ two-sided expression adds nothing over the long leg alone.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` stanza at `basePeriod: 1d`). The OHLC arithmetic ports across perpetual venues without structural change, but venue bar-construction differences touch `high`/`low`/`ohlc4` and hence the channel and the position test — disclosed above, not hand-waved. The range channel auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d` following the executable stanza's `Futures_Binance BTC_USDT` at `basePeriod: 1d` (against its `period: 4d` chart setting). Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Always-in-market commitment: after the first flip the book is never flat; adverse excursion after entry has no guardrail beyond the opposite flip, and a leg whose opposite conjunction never prints is held indefinitely. This is the prescribed posture, disclosed as the principal risk.
- Whipsaw sensitivity: alternating flips print repeated full reversals with no flat state to rest in, and a slope turn without band reach (or a band touch without slope) strands the book in the old leg through the whole move. The conjunction-plus-latch asymmetry is the prescribed design, disclosed, not smoothed.
- No source economics: beyond `strategy.percent_of_equity`/`initial_capital=5000` plumbing the source ships no commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Long seed: the six-fold EMA(24) cascade needs roughly 144 completed closes plus margin; the first 150 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (rule prose plus `Futures_Binance BTC_USDT` backtest stanza verified live via HTTP-200 page record): https://www.fmz.com/strategy/426786
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `7b3dd84dc7c71d3e7c04454b49621747ce4848dc`, 4690 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/T3%E5%9D%87%E7%BA%BF%E9%80%9A%E9%81%93%E7%AA%81%E7%A0%B4%E7%AD%96%E7%95%A5T3-Moving-Average-Channel-Breakout-Strategy.md
- Pine strategy semantics (order calls, default execution, built-in `ema` semantics): https://www.tradingview.com/pine-script-reference/v5/
