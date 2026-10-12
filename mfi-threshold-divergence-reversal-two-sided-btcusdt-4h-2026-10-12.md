---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: MFI threshold-cross divergence-gated reversal two-sided on BTCUSDT 4h bars
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
  - https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/mfi_strategy.pine
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MFI threshold-cross divergence-gated reversal two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (raw file fetched live over HTTPS twice this cycle — floating `master` and pinned commit — byte-identical, 3,765 bytes, 90 lines, SHA-256 `32162d9414eadd15479e09cee60ab1b03d04aa315354fee29396d710a2a4fd67`):

- Repository: https://github.com/EternaHybridExchange/tradingview-strategies (`master` default branch; repo created 2026-03-12; open-source collection of executable Pine Script strategies with alert-JSON handoff for automated execution).
- Immutable pin: commit `01e4346df876f6fd124332e40a2cd62286174894` (2026-03-12T18:38:03Z, `Initial commit: 20 Pine Script strategies with Eterna MCP in`), path `strategies/momentum/mfi_strategy.pine` (90 lines, `//@version=5`). Adopted `source_as_of` 2026-03-12 is that commit's date, disclosed here, never an authorship date.
- Strategy declaration (source-verbatim): `strategy("MFI Strategy - Eterna MCP", shorttitle="MFI", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)`. No `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission` argument ships — Pine language defaults govern the unfrozen timing, fenced below.
- Text census over the pinned 90-line file: 1 `strategy("` declaration / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, each gated by `strategy.position_size == 0`, alert JSON attached, no price/qty/when order argument) / 2 `strategy.close` (`"Long"` closed when the sell signal prints while long; `"Short"` closed when the buy signal prints while short) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 1 `ta.crossover(` (MFI cross up through the oversold level) plus 1 `ta.crossunder(` (MFI cross down through the overbought level) — no further `crossover`/`crossunder` tokens anywhere, not even in comments / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 6 `input.` (4 live trading inputs frozen below plus `leverageSize`/`positionSize` alert-payload parameters, fenced below) / 4 `position_size` reads (2 entry gates, 2 exit guards) / 1 `ta.mfi(` / 1 `ta.sma(` (20-bar average volume — display/dead leg, fenced below) / 2 `ta.lowest(` / 2 `ta.highest(` / 2 `alert(` (JSON execution-handoff strings only — no order-leg effect, disclosed) / 2 `plot(` plus 4 `plotshape` plus `hline`/`bgcolor` (render only, cannot change any order).
- Four live trading inputs frozen (any other value is a different, unpinned rule): `mfiLength = 14`, `overboughtLevel = 80`, `oversoldLevel = 20`, `divergenceLookback = 5`. The remaining two inputs (`leverageSize = 5.0`, `positionSize = 0.01`) parameterize only the alert-JSON handoff strings, never an order leg — house sizing/capital/costs replace the absent source economics (see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Strategy README (`strategies/momentum/README_mfi.md`, same repo, same pin): `Recommended Timeframes — Primary: 1H, 4H`; parameters table restates the frozen `14 / 80 / 20 / 5` defaults; prose claims `BUY: MFI crosses above 20 (oversold) or shows bullish divergence with high volume` and `Win rate: ~65-75% with volume confirmation`. Two disclosures follow. First, the `~65-75%` figure ships with no table, figure, section, sample, or cost provenance anywhere in the repository — per the exact-numbers rule this record omits it entirely and claims no source-reported performance. Second, the README's `with high volume` phrase overclaims against the code: the script computes `avgVolume = ta.sma(volume, 20)` and `highVolume = volume > avgVolume * 1.5` but no order leg, signal leg, or gate anywhere reads `highVolume` — it is plotted only (`plot(highVolume ? 90 : na, ...)`). Code governs: this record's signals carry no volume gate, and the dead leg is fenced as negative evidence, not silently adopted.
- Page performance language is otherwise absent — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the repository carries an MIT licence badge; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures (the source is market-agnostic via `syminfo.ticker` inside alert strings only — the code names no symbol); (2) decision timeframe `4h` taken from the strategy README's Primary pair `1H, 4H` (the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction; the `4h` choice matches the sibling oscillator records and is disclosed here, not code-derived); (3) same-bar-close fills on completed-bar decisions (the source ships no `process_orders_on_close`/`calc_on_every_tick` argument, so its backtest fills next-bar by language default; this record freezes completed-bar evaluation with same-bar-close execution and scopes any live intrabar behavior out, see Limitations); (4) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the MFI-14 seed plus the 20-bar average-volume line plus the 5-bar divergence windows plus margin; see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `14/80/20/5` inputs, the Pine `ta.mfi` money-flow arithmetic, the threshold-cross-plus-divergence entry pair with midline gates, the fixed `Long`/`Short` order IDs, the opposite-signal exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `mfi_strategy`, `mfi-threshold`, and `EternaHybrid` return zero strategy records using this source file or author script — the Chaikin/AO/VWAP/RSI-divergence sibling records share only the repository, never the file, indicator, or rule. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `alphatrend-mfi-atr-trailing-reversal` reads `ta.mfi(hlc3, 15)` only as a `>= 50` coefficient gate steering an ATR ratchet whose signal is a delayed self-cross `ta.crossover(AlphaTrend, AlphaTrend[2])` — MFI never crosses a threshold, never prints entries, never diverges there; `cmf-velocity-zero-cross-ema200-bracket` trades a bounded windowed CMF ratio with a velocity gate inside an EMA-200 bracket (never a Wilder-style money-flow oscillator, never 80/20 thresholds); `obv-ema-crossover-trend` crosses cumulative signed volume against its own EMA (no range/typical-price weighting, no threshold semantics, no divergence legs); `klinger-volume-oscillator-trigger-flip` is a volume-force trigger flip with its own signal line; `rsi-divergence-pivot-oscillator-reversal` is price-only Wilder RSI with pivot-anchored divergence (no volume read anywhere, no threshold-cross entries, no midline gate); `macd-signal-cross-reversal` applies a MACD structure to price. Five-axis distinction: mechanism differs (volume-weighted money-flow oscillator threshold-cross reversal, not a ratchet, ratio, cumulative line, or price oscillator), signal construction differs (no pool record computes Pine `ta.mfi(close, 14)` with `80/20` threshold crosses), trigger differs (cross-plus-5-bar-extreme divergence pair under opposite midline gates — not a self-cross, rail, or signal-line cross), source identity differs (Eterna `mfi_strategy.pine` at pin `01e4346d`), and research frame is BTCUSDT `4h`.

## Economic mechanism

### Source-reported

Volume-weighted RSI reversal (strategy README: `volume-weighted RSI`, `money flowing in and out`; no performance section ships): each bar's typical-price move weights that bar's volume into positive/negative money flow over 14 bars; the 0–100 MFI prints high while money flows in and low while it flows out. A cross back up through 20 (or a 5-bar bullish price/MFI divergence while MFI stays under 20) opens a long; a cross back down through 80 (or a 5-bar bearish divergence while MFI stays over 80) opens a short; the opposite signal closes the position. Both entry pairs additionally require the oscillator to sit on the System's own side of the 50 midline. There is deliberately no stop, no target, and no flat state beyond pre-signal bars — the order block ends with the two `strategy.close` guards and no risk leg ships anywhere, by design gap rather than by hidden leg.

### Research interpretation

Threshold-cross mean reversion on money flow, two-sided with reversal exits — the first pure-MFI record in the pool. Unlike price RSI (`rsi-divergence-pivot-oscillator`), the input series multiplies every typical-price print by that bar's volume before accumulating, so the trigger fires on conviction-backed flow turns (heavy-volume washouts and blow-offs) that a price-only oscillator cannot distinguish from thin chop; unlike bounded windowed money-flow ratios (`cmf-velocity`), the oscillator is Wilder-smoothed over 14 bars with fixed 80/20 extremes, so entries wait for a genuine cross rather than a velocity flicker; unlike OBV (`obv-ema-crossover`), oversold/overbought levels are absolute (20/80), not relative to a drifting cumulative line, so both directions stay reachable at any crypto volume scale without retuning. Note the two pinned asymmetries, stated plainly: first, entries need a fresh cross or a fresh divergence — a MFI that merely sits under 20 or over 80 without crossing or diverging fires nothing, so congestion at extremes is ignored by construction; second, the divergence legs require the oscillator to sit beyond the extreme that the cross legs use (`mfi < 20` for longs, `> 80` for shorts) plus the midline gate, so late-stage divergences after the oscillator has already normalized fire nothing — the setup is early-turn only, disclosed. The bet is on money-flow exhaustion turns at frozen `14/80/20/5` geometry, not on any price level, volatility extreme, calendar effect, or trend-rail position.

## Signal

Exact rule as pinned (`mfiLength 14 / overboughtLevel 80 / oversoldLevel 20 / divergenceLookback 5` frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy("MFI Strategy - Eterna MCP", shorttitle="MFI", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)` semantics preserved with the derived `BTCUSDT 4h` market/frame pin and same-bar-close execution adopted (see derived declaration) and house sizing/costs replacing the source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires while positioned are blocked by the `position_size == 0` entry gates, opposite entries arrive only via the close-then-enter path below.
- Indicator (pinned arithmetic — evaluated from the frozen inputs, not tuned): `mfi = ta.mfi(close, 14)` — Pine built-in Money Flow Index on `close` with volume, 0–100, causal recursion on completed bars.
- Threshold-cross legs: `bullishOB = ta.crossover(mfi, 20)`; `bearishOS = ta.crossunder(mfi, 80)`.
- Divergence legs (5-bar window, exact Pine float-equality semantics, disclosed): `bullishDiv = low == ta.lowest(low, 5) and mfi > ta.lowest(mfi, 5) and mfi < 20` (price prints a 5-bar low while MFI holds above its own 5-bar low, still oversold); `bearishDiv = high == ta.highest(high, 5) and mfi < ta.highest(mfi, 5) and mfi > 80` (mirrored).
- Midline gates: longs additionally require `mfi < 50`; shorts additionally require `mfi > 50`.
- Entry long: `strategy.entry("Long", strategy.long)` under `if buySignal and strategy.position_size == 0` where `buySignal = (bullishOB or bullishDiv) and mfi < 50` — fires on completed bars with same-bar-close execution under the derived declaration.
- Entry short: `strategy.entry("Short", strategy.short)` under `if sellSignal and strategy.position_size == 0` where `sellSignal = (bearishOS or bearishDiv) and mfi > 50` — mirrored.
- Exits (coded, the sole position-closing path): `strategy.close("Long")` under `if sellSignal and strategy.position_size > 0`; `strategy.close("Short")` under `if buySignal and strategy.position_size < 0`. No stop, no target, no trailing exit leg, no time exit — pinned as written, explicitly none, not invented.
- Direction: two-sided with no coded flat state past seeding (after the first signal the system is always in market — disclosed, not enabled). `na` seed bars (Pine comparisons against `na` are false) fire no leg and the inherited position simply persists by language semantics, disclosed, not invented.
- Display isolation: the `plot`/`plotshape`/`hline`/`bgcolor` calls render only and cannot change any order; the two `alert(` JSON strings are execution-handoff payloads with no order-leg effect. The `avgVolume`/`highVolume` lines compute but feed only a plot — no order logic reads any display or volume-average output.

## Required data

- Completed `4h` bars of BTCUSDT: `close` and `volume` (via the Pine `ta.mfi` money-flow accumulation), plus `high`/`low` for the 5-bar `highest`/`lowest` divergence windows. No `open`-series read ships in any live line; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `4h` (README-Primary-faithful; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks a 14-bar money-flow seed beneath 5-bar extreme windows and a 20-bar average-volume line (structural lag ≈ 20 bars). The adopted warmup is the first 100 completed `4h` bars flat by record rule (predeclared researcher choice — roughly five times the structural lag with smoother-decay margin; ≈17 days of `4h` history). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar under the derived freeze. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills. Binance spot/futures candle volume is the point-in-time print for the completed bar — no restatement, no revision.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the source names no market — `syminfo.ticker` appears inside alert-payload strings only — so the venue/symbol pin is a researcher market choice, disclosed, never presented as source-native; the `4h` frame comes from the strategy README's Primary pair).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close`/`calc_on_every_tick` argument (quoted verbatim in census) — its backtest fills next-bar by language default; this record does not claim that source behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long `if` before short `if`): `buySignal` and `sellSignal` cannot both print on one bar by construction (longs require `mfi < 50`, shorts require `mfi > 50` — mutually exclusive on every bar, including the divergence legs which carry the same gates), so at most one entry leg can fire on any bar; an exit guard and its opposite entry can co-print (e.g. `sellSignal` while long closes Long, and the short entry gate `position_size == 0` reads the pre-close position intrabar — under Pine semantics the close executes first and the flat-gated entry fills the same bar, i.e. a full reversal; this record pins that reversal as the close-then-enter same-bar path, disclosed).
- Engine path for `4h` (gate 5, stated plainly): `4h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `4h` candles (`close`/`high`/`low`/`volume`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h`/`2h`/`15m`/`30m`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name). Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only Pine-default economics (`percent_of_equity 100 / initial_capital 1000`, no commission/slippage/funding/margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) plus alert-payload-only `leverageSize`/`positionSize` parameters with no order-leg effect — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default single-position semantics hold — at most one open position under the order IDs `Long`/`Short`; entries are flat-gated, exits are opposite-signal closes with a same-bar close-then-enter reversal path (above), and re-placement is allowed immediately on the next qualifying bar after any close (no cooldown specified — explicitly none, not invented). `na` bars hold the inherited position by language semantics, disclosed. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `14/80/20/5` inputs, Pine `ta.mfi(close, 14)` money-flow oscillator, threshold-cross entry pair, 5-bar price/MFI divergence pair with extreme-side requirements, opposite-midline gates, fixed `Long`/`Short` order IDs with flat-gated entries and opposite-signal closes), the active `strategy("MFI Strategy - Eterna MCP", ...)` declaration, and the strategy README (`Primary: 1H, 4H` frame guidance adopted as disclosed; `14 / 80 / 20 / 5` parameter table restated). It ships zero traceable performance numbers: the `~65-75%` README phrase carries no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the sole position-closing path is the coded opposite-signal `strategy.close` pair. The absence is coded (the order block ends with the two close guards and only plotting follows) and the prose carries no risk leg anywhere.
2. Volume-confirmation prose disproven against the code, stated plainly: the README promises entries `with high volume` and `Volume confirmation strengthens signal reliability`, but the census shows `highVolume` computed once and read zero times outside its own plot — substituting a volume-gated entry would be a different, unpinned rule. This record freezes the ungated signals as written.
3. Bare extremes fire nothing, stated plainly: entries require `(cross or divergence) and midline-gate` — a MFI that merely sits under 20 or over 80 without a fresh cross or divergence fires nothing. Relaxing to level-holding entries would be a different, unpinned rule.
4. Divergence legs fenced: exact 5-bar windows with Pine float-equality extremes (`low == ta.lowest(low, 5)`) plus beyond-extreme requirements (`mfi < 20` long / `> 80` short) plus the midline gate — late-stage divergences after the oscillator has normalized fire nothing by construction, disclosed.
5. No future leakage in the stack, stated plainly: at decision bar `t`, the `ta.mfi` accumulation plus the 5-bar `lowest`/`highest` windows read completed-bar prints through `t` and seeded priors only. No `security()`, no `request.*`, no negative index, no `open` read, no `barstate.islast`-gated path; seed bars degrade to `na`-hold, never to a forward read.
6. Same-bar ordering fenced: at most one entry leg can fire per bar (the `mfi < 50` / `mfi > 50` gates are mutually exclusive on every bar); the co-printing exit-plus-opposite-entry path is pinned as a same-bar close-then-enter reversal, disclosed under Execution assumptions. Deterministic under the declared fill convention.
7. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own flat-gated `if`; both `strategy.close` guards cover the opposite-signal exits; no third direction exists. No flat state is coded after the first signal — always-in-market past seeding, disclosed.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the README-Primary `4h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the inputs, MFI arithmetic, cross/divergence/midline legs, order IDs, gating, exits, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the alert-JSON execution handoff of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `14` MFI / `80/20` thresholds / `5`-bar divergence / 50-midline gates / cross-or-divergence entries / opposite-signal exits / two-sided / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Divergence-leg relevance: disabling both divergence legs (threshold-cross entries only, same exits and gates) must not improve net expectancy; fail ⇒ the coded divergence pair adds nothing over its cross-only twin.
- F2 — Midline-gate relevance: dropping both 50-midline gates (bare cross-or-divergence entries, same exits) must not improve net expectancy; fail ⇒ the coded gates add nothing over their ungated twin.
- F3 — Volume-weighting relevance: replacing Pine `ta.mfi(close, 14)` with a price-only Wilder RSI(14) through the same `80/20` crosses, divergence legs, and gates must not improve net expectancy; fail ⇒ the money-flow weighting adds nothing over its price-only twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `4h` under the house overlay (market pin is a researcher choice on a market-agnostic source; the `4h` frame is README-Primary-faithful). The money-flow arithmetic ports across perpetual venues without structural change; venue volume-definition differences move the oscillator's scale but the rule reads only fixed 80/20/50 levels, never an absolute flow value — disclosed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. The strategy README itself warns volume data must be reliable and names liquid crypto pairs as the fit venue — adopted as venue rationale, not as performance evidence. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no `process_orders_on_close`/`calc_on_every_tick` argument (backtest fills next-bar by language default); this record evaluates completed bars only and executes same-bar-close on `4h` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live intrabar behavior is out of scope.
- Derived market pin: the code names no symbol (`syminfo.ticker` appears inside alert-payload strings only) — BTCUSDT is a researcher market choice for the house universe, never a source claim.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind. The `~65-75%` README phrase is omitted for want of traceable provenance.
- No price stop, no time stop, no flat state: adverse excursion after placement has no guardrail beyond the opposite-signal close; a position whose pair never prints the opposite signal is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Congestion at extremes is untraded: a MFI parked under 20 or over 80 without a fresh cross or divergence fires nothing, and a mirror-leg divergence after normalization fires nothing — long flat stretches between events are the coded posture, disclosed.
- Seed and extreme-equality bars: the 14-bar money-flow seed dominates early bars; the first 100 `4h` bars are flat by record rule, so early-history signals never enter any evaluation. Divergence legs use exact float equality on 5-bar extremes — a near-extreme that is not the extreme fires nothing, disclosed.
- Alert-handoff quarantine: the two `alert(` JSON strings (`Eterna MCP` execution handoff with `leverageSize`/`positionSize` parameters) are payload text with no order-leg effect — treating them as order semantics would be a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/mfi_strategy.pine (primary source — executable `//@version=5` strategy, 90 lines, fetched live 2026-10-12 at pinned commit byte-identical to `master`, 3,765 bytes, SHA-256 `32162d94…2a4fd67`; strategy README `Primary: 1H, 4H` — `4h` adopted as disclosed, `~65-75%` phrase omitted)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
