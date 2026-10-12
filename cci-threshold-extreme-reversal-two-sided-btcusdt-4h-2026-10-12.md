---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: CCI threshold-cross extreme-reversal two-sided on BTCUSDT 4h bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-03-12
sources:
  - https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/cci_strategy.pine
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CCI threshold-cross extreme-reversal two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (raw file fetched live over HTTPS twice this cycle — floating `master` and pinned commit — byte-identical, 3,579 bytes, 81 lines, SHA-256 `1a452670426b06d22f16f023abf8f4c77a59ca7704f775590111c357ff6862e2`):

- Repository: https://github.com/EternaHybridExchange/tradingview-strategies (`master` default branch; repo created 2026-03-12; open-source collection of executable Pine Script strategies with alert-JSON handoff for automated execution).
- Immutable pin: commit `01e4346df876f6fd124332e40a2cd62286174894` (2026-03-12T18:38:03Z, `Initial commit: 20 Pine Script strategies with Eterna MCP in`), path `strategies/momentum/cci_strategy.pine` (81 lines, `//@version=5`). Adopted `source_as_of` 2026-03-12 is that commit's date, disclosed here, never an authorship date.
- Strategy declaration (source-verbatim): `strategy("CCI Strategy - Eterna MCP", shorttitle="CCI", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)`. No `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission` argument ships — Pine language defaults govern the unfrozen timing, fenced below.
- Text census over the pinned 81-line file (comments stripped before counting): 1 `strategy("` declaration / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, each gated by `strategy.position_size == 0`, alert JSON attached, no price/qty/when order argument) / 2 `strategy.close` (`"Long"` closed when the sell signal prints while long; `"Short"` closed when the buy signal prints while short) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 2 `crossover(` (`ta.crossover(cci, oversoldLevel)` trading leg plus `ta.crossover(cci, 0)` display-only leg, fenced below) plus 2 `crossunder(` (`ta.crossunder(cci, overboughtLevel)` trading leg plus `ta.crossunder(cci, 0)` display-only leg) — no further `crossover`/`crossunder`/`ta.cross(` tokens anywhere / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 7 `input.` (5 live trading inputs frozen below plus `leverageSize`/`positionSize` alert-payload parameters, fenced below) / 4 `position_size` reads (2 entry gates, 2 exit guards) / 1 `ta.cci(` / 0 `ta.ema/dema/tema/hma/rma/wma/vwma/rsi/mfi(` / 0 bare-v4 `ema(/rsi(/rma(/wma(/vwma(` / 0 `ta.highest(`/`ta.lowest(` / 0 `volume` / 0 `open`/`high`/`low`/`hlc3` series reads in any live line / 2 `alert(` (JSON execution-handoff strings only — no order-leg effect, disclosed) / 2 `syminfo` (inside alert strings only — the code names no market) / `plot(` plus 4 `plotshape` plus `hline`/`bgcolor` (render only, cannot change any order).
- Five live trading inputs frozen (any other value is a different, unpinned rule): `cciLength = 20`, `overboughtLevel = 100`, `oversoldLevel = -100`, `extremeOB = 200`, `extremeOS = -200`. The remaining two inputs (`leverageSize = 5.0`, `positionSize = 0.01`) parameterize only the alert-JSON handoff strings, never an order leg — house sizing/capital/costs replace the absent source economics (see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Strategy README (`strategies/momentum/README_cci.md`, same repo, same pin): `Recommended Timeframes — Primary: 1H, 4H`; parameters table restates the frozen `20 / +100 / -100 / +200 / -200` defaults; prose claims `BUY: CCI crosses above -100 (oversold) or reverses from extreme oversold (< -200)`, `SELL: CCI crosses below +100 (overbought) or reverses from extreme overbought (> +200)`, `Trend confirmation: Zero-line crossovers indicate trend direction`, and `Win rate: ~60-70% from extreme levels`. Three disclosures follow. First, the `~60-70%` figure ships with no table, figure, section, sample, or cost provenance anywhere in the repository — per the exact-numbers rule this record omits it entirely and claims no source-reported performance. Second, the `Trend confirmation` phrase overclaims against the code: the script computes `bullishTrend = ta.crossover(cci, 0)` and `bearishTrend = ta.crossunder(cci, 0)` but each is read exactly once, inside its own `plotshape` marker — no order leg, signal leg, or gate anywhere reads either series. Code governs: this record's signals carry no zero-line confirmation, and the dead pair is fenced as negative evidence, not silently adopted. Third, the README's `Optimal Settings` section (`Crypto (volatile): Length 14, Thresholds ±150`) is a variant menu the code does not take — this record freezes the coded defaults and adopts no variant, disclosed.
- Page performance language is otherwise absent — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the repository carries an MIT licence badge; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures (the source is market-agnostic via `syminfo.ticker` inside alert strings only — the code names no symbol); (2) decision timeframe `4h` taken from the strategy README's Primary pair `1H, 4H` (the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction; the `4h` choice matches the sibling oscillator records and is disclosed here, not code-derived); (3) same-bar-close fills on completed-bar decisions (the source ships no `process_orders_on_close`/`calc_on_every_tick` argument, so its backtest fills next-bar by language default; this record freezes completed-bar evaluation with same-bar-close execution and scopes any live intrabar behavior out, see Limitations); (4) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the 20-bar CCI seed plus margin; see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `20/100/-100/200/-200` inputs, the Pine `ta.cci` arithmetic, the threshold-cross-plus-extreme-reversal entry pair, the fixed `Long`/`Short` order IDs, the opposite-signal exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `cci_strategy`, `cci-threshold`, and `EternaHybrid` return the five sibling Eterna records only (Chaikin, AO, VWAP, RSI-divergence, MFI — same repository, never this file, indicator, or rule) plus zero records using this source file. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `cci-ema-rsi-cross-trailing-stop` (FMZ 362029 triple-gate trend system — CCI above ±50 gates a fast/slow RSI cross under a slow-EMA price filter with a ratcheting close-evaluated trailing stop, `1h`; this record is a pure single-oscillator threshold-cross plus extreme-reversal system with opposite-signal exits and no stop leg, `4h`); `rsi-classic-level-reversal` and `rsi-ma-crossover-reversal` (price-only RSI constructions, no CCI read anywhere); `williams-r-level-cross-mean-reversion` (highest/lowest-range oscillator, long-only, fixed-RR exits); `stochastic-ott-dual-trend` (dual-trend confirmation stack). Five-axis distinction: source identity differs (Eterna immutable commit plus `cci_strategy.pine` path, never FMZ 362029), mechanism differs (single-oscillator threshold-cross/extreme-reversal, not a triple-gate plus trailing ratchet), signal construction differs (no pool record computes Pine `ta.cci(close, 20)` with `±100` threshold crosses plus `±200` extreme reversals), exits differ (opposite-signal closes only, no trailing-stop leg), horizon differs (`4h` versus the pool CCI record's `1h`). No closed NOT_LOSSLESS PR touches CCI.

## Economic mechanism

### Source-reported

Mean-reversion on the Commodity Channel Index (strategy README: CCI `measures the deviation of price from its statistical mean`, `identify cyclical trends and overbought/oversold conditions`; no performance section ships): CCI prints high when price stretches far above its 20-bar mean and low when it stretches far below. A cross back up through −100 (or a reversal back up out of the sub-−200 extreme while still under −100) opens a long; a cross back down through +100 (or a reversal back down out of the above-+200 extreme while still over +100) opens a short; the opposite signal closes the position. There is deliberately no stop, no target, and no flat state beyond pre-signal bars — the order block ends with the two `strategy.close` guards and no risk leg ships anywhere, by design gap rather than by hidden leg.

### Research interpretation

Threshold-cross mean reversion on a mean-deviation oscillator, two-sided with reversal exits — the first pure-CCI threshold record in the pool. Unlike the pool's FMZ CCI system (`cci-ema-rsi-cross-trailing-stop`), entries here need no RSI-cross confirmation, no EMA price filter, and no CCI ±50 broadening gate — a bare cross of the ±100 thresholds (or a one-bar extreme reversal) suffices, so the system fires earlier and more often at the cost of holding every leg with no trailing guardrail; unlike price RSI threshold systems, the input is CCI's mean-deviation statistic on `close` with fixed ±100/±200 geometry, so overbought/oversold are absolute statistical levels rather than Wilder smoothing levels; unlike the MFI sibling (`mfi-threshold-divergence-reversal`), there is no volume read anywhere, no divergence leg, and no midline gate — the whole rule is four comparisons on one series. Note the two pinned asymmetries, stated plainly: first, entries need a fresh cross or a fresh extreme reversal — a CCI that merely sits under −100 or over +100 without crossing or reversing fires nothing, so congestion at extremes is ignored by construction; second, the extreme legs require the oscillator to still sit on the extreme side of the standard threshold (`cci < -100` long / `cci > +100` short), so a reversal that has already normalized past ±100 fires only via a fresh threshold cross, never via the extreme leg — the setup is early-turn only, disclosed. The bet is on mean-deviation exhaustion turns at frozen `20/±100/±200` geometry, not on any price level, volume print, trend-rail position, or calendar effect.

## Signal

Exact rule as pinned (`cciLength 20 / overboughtLevel 100 / oversoldLevel -100 / extremeOB 200 / extremeOS -200` frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy("CCI Strategy - Eterna MCP", shorttitle="CCI", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)` semantics preserved with the derived `BTCUSDT 4h` market/frame pin and same-bar-close execution adopted (see derived declaration) and house sizing/costs replacing the source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires while positioned are blocked by the `position_size == 0` entry gates, opposite entries arrive only via the close-then-enter path below.
- Indicator (pinned arithmetic — evaluated from the frozen inputs, not tuned): `cci = ta.cci(close, 20)` — Pine built-in Commodity Channel Index on `close`, causal recursion on completed bars. No `open`/`high`/`low`/`hlc3`/`volume` series is read by any live line (census-verified zero).
- Threshold-cross legs: `bullishStandard = ta.crossover(cci, oversoldLevel)` (cross back up through −100); `bearishStandard = ta.crossunder(cci, overboughtLevel)` (cross back down through +100).
- Extreme-reversal legs (one-bar turn out of the extreme, still beyond the standard threshold): `extremeBullish = cci[1] < extremeOS and cci > extremeOS and cci < oversoldLevel` (prior bar under −200, current bar back above −200 yet still under −100); `extremeBearish = cci[1] > extremeOB and cci < extremeOB and cci > overboughtLevel` (mirrored).
- Entry long: `strategy.entry("Long", strategy.long)` under `if buySignal and strategy.position_size == 0` where `buySignal = bullishStandard or extremeBullish` — fires on completed bars with same-bar-close execution under the derived declaration.
- Entry short: `strategy.entry("Short", strategy.short)` under `if sellSignal and strategy.position_size == 0` where `sellSignal = bearishStandard or extremeBearish` — mirrored.
- Exits (coded, the sole position-closing path): `strategy.close("Long")` under `if sellSignal and strategy.position_size > 0`; `strategy.close("Short")` under `if buySignal and strategy.position_size < 0`. No stop, no target, no trailing exit leg, no time exit — pinned as written, explicitly none, not invented.
- Direction: two-sided with no coded flat state past seeding (after the first signal the system is always in market — disclosed, not enabled). `na` seed bars (Pine comparisons against `na` are false) fire no leg and the inherited position simply persists by language semantics, disclosed, not invented.
- Display isolation: the `plot`/`plotshape`/`hline`/`bgcolor` calls render only and cannot change any order; the two `alert(` JSON strings are execution-handoff payloads with no order-leg effect. The `bullishTrend`/`bearishTrend` zero-cross pair computes but feeds only its own `plotshape` markers — no order logic reads either series.

## Required data

- Completed `4h` bars of BTCUSDT: `close` only. No `open`/`high`/`low`/`hlc3` read ships in any live line; no volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `4h` (README-Primary-faithful; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction carries a single 20-bar CCI seed (structural lag ≈ 20 bars — the lightest seed in the admitted Eterna oscillator family). The adopted warmup is the first 100 completed `4h` bars flat by record rule (predeclared researcher choice — five times the structural lag with margin; ≈17 days of `4h` history). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar under the derived freeze. Each bar's print enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the source names no market — `syminfo.ticker` appears inside alert-payload strings only — so the venue/symbol pin is a researcher market choice, disclosed, never presented as source-native; the `4h` frame comes from the strategy README's Primary pair).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close`/`calc_on_every_tick` argument (quoted verbatim in census) — its backtest fills next-bar by language default; this record does not claim that source behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long `if` before short `if`): `buySignal` and `sellSignal` cannot both print on one bar by construction (every buy leg requires the prior bar at or under −100 with the current bar rising; every sell leg requires the prior bar at or over +100 with the current bar falling — the prior-bar requirements are mutually exclusive on every bar, and the current-bar requirements cannot jointly satisfy a cross up through −100 and a cross down through +100), so at most one entry leg can fire on any bar; an exit guard and its opposite entry can co-print (e.g. `sellSignal` while long closes Long, and the short entry gate `position_size == 0` reads the pre-close position intrabar — under Pine semantics the close executes first and the flat-gated entry fills the same bar, i.e. a full reversal; this record pins that reversal as the close-then-enter same-bar path, disclosed).
- Engine path for `4h` (gate 5, stated plainly): `4h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `4h` candles (`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h`/`2h`/`15m`/`30m`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name). Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only Pine-default economics (`percent_of_equity 100 / initial_capital 1000`, no commission/slippage/funding/margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) plus alert-payload-only `leverageSize`/`positionSize` parameters with no order-leg effect — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default single-position semantics hold — at most one open position under the order IDs `Long`/`Short`; entries are flat-gated, exits are opposite-signal closes with a same-bar close-then-enter reversal path (above), and re-placement is allowed immediately on the next qualifying bar after any close (no cooldown specified — explicitly none, not invented). `na` bars hold the inherited position by language semantics, disclosed. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `20/±100/±200` inputs, Pine `ta.cci(close, 20)` mean-deviation oscillator, threshold-cross entry pair, one-bar extreme-reversal entry pair with beyond-threshold requirements, fixed `Long`/`Short` order IDs with flat-gated entries and opposite-signal closes), the active `strategy("CCI Strategy - Eterna MCP", ...)` declaration, and the strategy README (`Primary: 1H, 4H` frame guidance adopted as disclosed; `20 / ±100 / ±200` parameter table restated). It ships zero traceable performance numbers: the `~60-70%` README phrase carries no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the sole position-closing path is the coded opposite-signal `strategy.close` pair. The absence is coded (the order block ends with the two close guards and only plotting follows) and the prose carries no risk leg anywhere.
2. Zero-line-confirmation prose disproven against the code, stated plainly: the README promises `Trend confirmation: Zero-line crossovers indicate trend direction`, but the census shows `bullishTrend`/`bearishTrend` each defined once and read zero times outside their own `plotshape` markers — substituting a zero-line-gated entry would be a different, unpinned rule. This record freezes the ungated signals as written.
3. Bare extremes fire nothing, stated plainly: entries require a fresh cross (`crossover`/`crossunder` against ±100) or a fresh one-bar extreme reversal — a CCI that merely sits under −100 or over +100 without crossing or reversing fires nothing. Relaxing to level-holding entries would be a different, unpinned rule.
4. Extreme legs fenced: the reversal must still sit beyond the standard threshold on the signal bar (`cci < -100` long / `cci > +100` short) — a turn that has already normalized past ±100 fires only via a fresh threshold cross, never via the extreme leg, disclosed.
5. `Optimal Settings` variant menu fenced: the README's `Length 14, Thresholds ±150` crypto suggestion is not taken — the frozen rule is the coded `20/±100/±200` defaults, and any 14/±150 evaluation would be a different, unpinned rule, disclosed.
6. No future leakage in the stack, stated plainly: at decision bar `t`, the `ta.cci` accumulation reads completed-bar `close` prints through `t` and seeded priors only, and the extreme legs read one prior bar (`cci[1]`). No `security()`, no `request.*`, no negative index, no `open`/`high`/`low`/`volume` read, no `barstate.islast`-gated path; seed bars degrade to `na`-hold, never to a forward read.
7. Same-bar ordering fenced: at most one entry leg can fire per bar (the prior-bar `≤ −100` versus `≥ +100` requirements are mutually exclusive on every bar); the co-printing exit-plus-opposite-entry path is pinned as a same-bar close-then-enter reversal, disclosed under Execution assumptions. Deterministic under the declared fill convention.
8. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own flat-gated `if`; both `strategy.close` guards cover the opposite-signal exits; no third direction exists. No flat state is coded after the first signal — always-in-market past seeding, disclosed.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the README-Primary `4h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the inputs, CCI arithmetic, cross/extreme-reversal legs, order IDs, gating, exits, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the alert-JSON execution handoff of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `20` CCI / `±100` thresholds / `±200` extremes / cross-or-extreme-reversal entries / opposite-signal exits / two-sided / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Extreme-leg relevance: disabling both extreme-reversal legs (threshold-cross entries only, same exits) must not improve net expectancy; fail ⇒ the coded extreme pair adds nothing over its cross-only twin.
- F2 — Threshold-choice relevance: widening both standard thresholds to ±150 at frozen `20/±200` (same exits) must not improve net expectancy; fail ⇒ the coded ±100 choice adds nothing over its wider twin.
- F3 — Mean-deviation relevance: replacing Pine `ta.cci(close, 20)` with a price-only Wilder RSI(20) through the same `±100`-style cross geometry and exits must not improve net expectancy; fail ⇒ the mean-deviation construction adds nothing over its price-only twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `4h` under the house overlay (market pin is a researcher choice on a market-agnostic source; the `4h` frame is README-Primary-faithful). The CCI arithmetic ports across perpetual venues without structural change — it reads `close` only, so venue volume-definition differences cannot move the oscillator at all, disclosed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. The strategy README names liquid crypto pairs as a fit venue — adopted as venue rationale, not as performance evidence. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no `process_orders_on_close`/`calc_on_every_tick` argument (backtest fills next-bar by language default); this record evaluates completed bars only and executes same-bar-close on `4h` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live intrabar behavior is out of scope.
- Derived market pin: the code names no symbol (`syminfo.ticker` appears inside alert-payload strings only) — BTCUSDT is a researcher market choice for the house universe, never a source claim.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind. The `~60-70%` README phrase is omitted for want of traceable provenance.
- No price stop, no time stop, no flat state: adverse excursion after placement has no guardrail beyond the opposite-signal close; a position whose pair never prints the opposite signal is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Congestion at extremes is untraded: a CCI parked under −100 or over +100 without a fresh cross or extreme reversal fires nothing — long flat stretches between events are the coded posture, disclosed.
- Seed bars: the 20-bar CCI seed dominates early bars; the first 100 `4h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Alert-handoff quarantine: the two `alert(` JSON strings (`Eterna MCP` execution handoff with `leverageSize`/`positionSize` parameters) are payload text with no order-leg effect — treating them as order semantics would be a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/cci_strategy.pine (primary source — executable `//@version=5` strategy, 81 lines, fetched live 2026-10-12 at pinned commit byte-identical to `master`, 3,579 bytes, SHA-256 `1a452670…e2`; strategy README `Primary: 1H, 4H` — `4h` adopted as disclosed, `~60-70%` phrase omitted)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
