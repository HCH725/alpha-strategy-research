---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Adaptive SMI ergodic threshold-recross gated two-sided on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-10-06
sources:
  - https://www.tradingview.com/script/YwjZvSpI-Adaptive-SMI-Ergodic-Strategy/
  - https://www.tradingview.com/support/solutions/43000594669-smi-ergodic-indicator/
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive SMI ergodic threshold-recross gated two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView script page, fetched 2026-10-13):

- Canonical page: https://www.tradingview.com/script/YwjZvSpI-Adaptive-SMI-Ergodic-Strategy/ (page title `Adaptive SMI Ergodic Strategy by NantzOS`, badge `OPEN-SOURCE SCRIPT`, publisher `NantzOS`, script header `// © DraftVenture`, description date Oct 5 2023, `Updated Oct 6, 2023` — adopted as `source_as_of` 2023-10-06; release note `Cleaned up script, updated entry logic for more trades, added classic default colors, and added gradient fill for oversold and overbought zones`). The page-visible counters (`1` / `8` / `3` / `5 883`) are favorites/copies/views affordances, not performance numbers — this record claims no source-reported performance of any kind.
- The full 43-line `//@version=5` Pine block was read verbatim from the page's `Source code` tab this cycle. Order-gating lines, quoted exactly: `erg = ta.tsi(close, shortlen, longlen)` / `sig = ta.ema(erg, siglen)` / `longEntry = ta.crossover(erg, overS) and erg > sig` / `shortEntry = ta.crossunder(erg, overB) and erg < sig` / `if longEntry` → `strategy.entry("Long", strategy.long)` / `if shortEntry` → `strategy.entry("Short", strategy.short)`. Input defaults read verbatim from the same block: `longlen = input.int(12, ...)`, `shortlen = input.int(5, ...)`, `siglen = input.int(5, ...)`, `overS = input.float(-0.4, ...)`, `overB = input.float(0.4, ...)` (page-embedded input metadata confirms `Long Length` defval 12, `Short Length` defval 5, visible bands at `0.4` / `-0.4` / `0`). Text census over the recovered block: 2 `strategy.entry` (the Long/Short pair above) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `request.*` / 0 `time(` / 0 `volume` / `open`/`high`/`low` read nowhere (the rule reads `close` only). The `strategy(...)` declaration carries no `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, commission, slippage, or sizing argument — all pinned as unspecified-by-source, never treated as live configuration. All `plot` / `hline` / `fill` legs (including the zero line, overbought/oversold bands, and gradient fills) render only and gate no order.
- Code-over-prose pin (material discrepancy, disclosed): the page prose describes entries as `SMI crosses over the EMA signal line with both below oversold` (long) / `crosses under with both above overbought` (short), but the executable code implements threshold recrosses — `ta.crossover(erg, overS) and erg > sig` (cross back above the −0.4 level while above the signal line) and `ta.crossunder(erg, overB) and erg < sig` (cross back below the +0.4 level while below the signal line). The derived spec follows the executable code exclusively; the prose-described signal-cross rule is a different, unimplemented rule and is excluded from every order leg here.
- Corroborating first-party semantics (no rule taken from them): TradingView's official SMI Ergodic support article confirms the ergodic construction is TSI plus a signal-line EMA (`ERGODIC = TSI`, `Signal Line = EMA(TSI)`) with guide-gated cross signals; the official Pine v5 reference confirms `ta.tsi(source, short_length, long_length)` returns a value in range `[-1, 1]` and `ta.ema` uses `alpha = 2 / (length + 1)`. These fix the ±0.4 thresholds as genuine 40%-of-range bands, not near-zero noise gates.
- Licence and rights: the page is a public open-source TradingView publication (`In true TradingView spirit, the creator ... has made it open-source, so that traders can review and verify its functionality`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/timeframe port — the source ships no symbol or timeframe (a chart-applied script); the derived record trades BTCUSDT Binance perpetual on completed `1d` closes; (2) same-bar-close fills (the source sets no execution-timing argument, so source fills are next-tick by language default); (3) position-state pin — the source ships no pyramiding/sizing/close argument, so live same-side-add and reversal-quantity behavior is unspecified-by-source; the derived record pins single-unit per side, repeat-signal-while-positioned as no-op, full reversal on the opposite entry, predeclared (matching Pine `pyramiding=0` default order semantics); (4) an adopted 40-bar warmup with pre-warmup bars flat by record rule (covers `change(1)` + EMA 12 + EMA 5 + signal EMA 5 plus seeding margin — see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The double-smoothing arithmetic (5/12/5), the ±0.4 bands, the dual-gate recross triggers, the Long/Short order pair, and the reversal-only no-stop posture are source-native and unmodified.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `nantz`, `adaptive-smi`, `ergodic`, `YwjZvSpI`, `476269`, `430740` return zero hits anywhere — no admitted rule uses this source, author publication, indicator, or mechanism (the sole `Smi` hit pool-wide is the `Smidt` author citation inside the turn-of-month record). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal) — single-file heads verified, different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsi-signal-cross-reversal-btcusdt-1d-2026-10-10.md` crosses a 25/13/13 double-smoothed TSI against its own signal EMA with no bands (raw cross, no threshold gate); `demarker-threshold-recross-cooldown-two-sided-btcusdt-1h-2026-10-12.md` recrosses DeMarker levels with a time cooldown and no signal-side confirmation; `slow-stochastic-14-3-regime-recross-two-sided-btcusdt-1d-2026-10-12.md` recrosses stochastic levels under a regime filter, not an oscillator-vs-own-EMA confirmation. Five-axis distinction: source identity differs (TV YwjZvSpI Oct-2023 versus FMZ 428611 or other TV authors), signal construction differs (`ta.tsi(close,5,12)` in `[-1,1]` plus own EMA(5) versus 25/13/13, DeMarker, or stochastic constructions), trigger differs (dual-gate threshold-recross-plus-signal-side versus raw cross, cooldown, or regime recross), bands differ (explicit ±0.4 gates versus none or different levels), and scale differs (`[-1,1]` ergodic versus `[-100,100]` TSI).

## Economic mechanism

### Source-reported

Ergodic momentum with a confirmation gate: the double-smoothed change ratio (`erg`) measures trend-normalized momentum persistence in `[-1,1]`; its own EMA (`sig`) is the signal line. A long is taken only when momentum recrosses back above the −0.4 oversold band while already above its signal line (washout-recovery with confirmation); a short only on recross back below the +0.4 overbought band while below its signal line (exhaustion-roll with confirmation). The ±0.4 bands suppress mid-zone chop crosses entirely — most bars can fire nothing.

### Research interpretation

Edge-triggered two-sided reversal system with no price level, stop, target, or confirmation leg beyond the two gates — always-in-market after the first signal, flipping only on the opposite gated recross. Unlike raw-cross holders (TSI record) that flip on every signal-line touch, this system fires only on band-edge events, so mid-zone oscillations hold the position through adverse excursion with no guardrail, while band-edge whipsaws in a range can flip repeatedly at the edges. Unlike cooldown-gated recross systems (DeMarker record) there is no time latch — confirmation is purely cross-sectional (`erg` versus `sig` on the signal bar). The bet, ported to BTCUSDT's own daily closes, is on daily ergodic-momentum band-edge persistence, never on a level, breakout, squeeze, calendar, volume, or mean-reversion anchor.

## Signal

Exact rule as pinned (12/5/5 lengths and ±0.4 bands frozen at source defaults; any other value is a different, unpinned rule):

- Declaration (source-native): `//@version=5` Pine semantics (`ta.tsi`, `ta.ema`, `ta.crossover`, `ta.crossunder`, `strategy.entry` v5 defaults). The `strategy(...)` header carries no live argument — `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, commission, slippage, and sizing are unspecified-by-source (house overlay applies to the derived evaluation; see Execution assumptions). `calc_on_every_tick` unset defaults false: exactly one evaluation per completed bar.
- Indicator arithmetic (source-native): `erg = ta.tsi(close, 5, 12)` (Pine arg order: short 5, long 12; output in `[-1,1]` per the v5 reference) and `sig = ta.ema(erg, 5)` with `alpha = 2 / 6` — all on BTCUSDT `1d` closes (market/timeframe port is the predeclared derivation; nesting order, lengths, operators, and bands verbatim).
- Entry long: `longEntry = ta.crossover(erg, -0.4) and erg > sig` → `strategy.entry("Long", long)` — fires only on the recross bar on confirmed closes, same-bar-close execution under the derived declaration. While already long, a repeat `longEntry` is a no-op by record rule (predeclared single-unit pin).
- Entry short / reversal: `shortEntry = ta.crossunder(erg, +0.4) and erg < sig` → `strategy.entry("Short", short)` — fires only on the recross bar; while long it closes the full long and opens the full short in the same execution step (full reversal, no residual leg); while already short, a repeat `shortEntry` is a no-op by record rule. Before the first signal the system is flat (no position by construction).
- `longEntry`/`shortEntry` are mutually exclusive on every bar by construction (`erg` cannot recross above −0.4 and below +0.4 on one bar, and `erg > sig` / `erg < sig` cannot both hold) — no same-bar ordering ambiguity exists anywhere in this record. The measure-zero edge `erg == sig` on a recross bar fails the strict side predicate and the position simply holds — stated, not patched. An `na` erg (warmup, or a degenerate all-flat seeding run) fires neither predicate — pinned as hold, never patched with a guard constant.
- Risk legs (pinned absence, not invented): 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit.
- Direction: two-sided long/short with symmetric reversal. Futures venue required for the short leg (realistic on the pinned perpetual venue).
- Display isolation: every `plot` / `hline` / `fill` leg (zero line, ±0.4 bands, gradients, background) renders only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read by `ta.tsi(close, ...)` in the derived record). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The rule makes no live `request.*` call, so it is single-symbol single-frame by construction.
- Single decision timeframe `1d` (researcher port; the source ships chart-applied with no timeframe). One evaluation per completed bar.
- Warmup: `change` needs 1 bar, the nested EMAs need 12 then 5 bars of seeding, and the signal EMA needs 5 bars of `erg` output. The adopted warmup is the first 40 completed `1d` bars flat by record rule (predeclared researcher choice — covers 1 + 12 + 5 + 5 plus seeding margin); no signal before bar 41 may trade. No repainting (`tsi`/`ema` read only completed closes), no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (naming normalization only; the signal-series port to own-`1d` closes is the predeclared derivation, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-tick (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive gated legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no live sizing, capital, commission, fee, slippage, margin, or funding assumption anywhere. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side under the fixed order IDs `Long`/`Short` (predeclared pin over absent source text, matching Pine `pyramiding=0` default order semantics); repeat same-side gated recrosses while positioned are no-ops; the opposite gated recross reverses in full in one step; re-entry after a reversal needs only the next opposite gate (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

No performance table, figure, backtest metric, Sharpe, win rate, drawdown, or profit number ships anywhere on the canonical page or in the recovered Pine block (page counters are engagement affordances, not results) — this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The page prose describes a different entry rule (signal-line cross with both series beyond the threshold) than the executable code implements (threshold recross with signal-side confirmation). The prose rule is excluded from this record; adopting it would specify a different, unverified strategy.
- The `// © DraftVenture` header inside a `NantzOS`-published page leaves authorship split as-shown; no author claim beyond the canonical URL and the verbatim header is made here.
- The TV support article's generic SMI rule (`crossedBelow(SMI, SIGNAL)` above the top guide) is corroborating semantics only — this record's triggers come from the script's executable lines, never from the generic article.

## Falsification plan

- Recompute `erg`/`sig` from BTCUSDT `1d` closes with 5/12/5 lengths and verify gated recross bars against an independent implementation (e.g., pandas ewm with `alpha = 2/(n+1)`, `adjust = False` semantics checked against Pine `ta.ema`).
- Falsified if: independent recomputation disagrees on signal bars; any order fires on a bar where neither gate holds; a flat pre-warmup bar carries a position; or any fill requires an intrabar path, a stop/target leg, or non-close data.
- Downstream performance screening (house overlay, fees plus historical funding) is out of scope for admission; only event-level rule fidelity matters here.

## Crypto portability

Direct: single-symbol close-only rule with no equity-session, breadth, fundamental, or calendar dependency. The short leg ports to the perpetual short permission without rule change; spot-only evaluation would disable the short leg explicitly (a different, long/flat-only evaluation, not covered by this record's two-sided claim).

## Limitations

- Reversal-only exits: no stop, target, trailing, or time exit exists by source construction; adverse band-edge whipsaws and mid-zone chop are held without guardrail.
- Gate sparsity: entries require band-edge recrosses, so long calm periods hold a stale-side position with no re-confirmation leg.
- Derivation scope: market/timeframe port, same-bar-close fills, 40-bar warmup, and house economics are researcher-declared (above); the record is a disclosed derivative, not a lossless source reproduction.
- No funding treatment in the source; realized-funding performance cannot be claimed without a verified implementation (house cost assumptions govern downstream evaluation).
- `confidence: medium` reflects interpretation confidence (verbatim code, first-party scale corroboration), not expected profitability.

## Implementation status

`not-implemented` — no Hummingbot controller, no Qlib job, no backtest, no Paper/Testnet/Live artifact exists for this record.

## Adoption boundary

`not-approved`, `research-only`. This record is an admission candidate only: eligible for downstream model-consistent research after independent six-gate review. No trading authorization of any kind is implied or granted.

## Related Wiki records

None — no Wiki Brain write was performed for this Scout cycle.

## Sources

- https://www.tradingview.com/script/YwjZvSpI-Adaptive-SMI-Ergodic-Strategy/ — canonical primary source (open-source Pine strategy, NantzOS, script header `// © DraftVenture`, Oct 2023); executable rule, input defaults, and order pair read verbatim this cycle.
- https://www.tradingview.com/support/solutions/43000594669-smi-ergodic-indicator/ — official first-party SMI Ergodic semantics corroboration (ergodic = TSI + signal-line EMA, guide-gated cross signals).
- https://www.tradingview.com/pine-script-reference/v5/ — official Pine v5 reference (`ta.tsi` range `[-1, 1]`, `ta.ema` alpha definition, v5 order-default semantics).
