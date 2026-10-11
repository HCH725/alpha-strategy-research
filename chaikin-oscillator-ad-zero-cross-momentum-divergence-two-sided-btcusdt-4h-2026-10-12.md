---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Chaikin Oscillator AD zero-cross momentum-divergence two-sided on BTCUSDT 4h bars
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
  - https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/chaikin_oscillator.pine
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Chaikin Oscillator AD zero-cross momentum-divergence two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (raw file fetched live over HTTPS twice this cycle — floating `master` and pinned commit — byte-identical, 4,115 bytes, SHA-256 `b50925e35a73fe9ac3c9e8457bdd67b8170b06f6b56b74012755d97bf896e`):

- Repository: https://github.com/EternaHybridExchange/tradingview-strategies (`master` default branch; repo created 2026-03-12; open-source collection of executable Pine Script strategies with alert-JSON handoff for automated execution).
- Immutable pin: commit `01e4346df876f6fd124332e40a2cd62286174894` (2026-03-12T18:38:03Z, `Initial commit: 20 Pine Script strategies with Eterna MCP in`), path `strategies/momentum/chaikin_oscillator.pine` (99 lines, `//@version=5`). Adopted `source_as_of` 2026-03-12 is that commit's date, disclosed here, never an authorship date.
- Strategy declaration (source-verbatim): `strategy("Chaikin Oscillator - Eterna MCP", shorttitle="Chaikin", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)`. No `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission` argument ships — Pine language defaults govern the unfrozen timing, fenced below.
- Text census over the pinned 99-line file: 1 `strategy("` declaration / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, gated by `strategy.position_size == 0`, alert JSON attached, no price/qty/when order argument) / 2 `strategy.close` (`"Long"` closed when the sell signal prints while long; `"Short"` closed when the buy signal prints while short) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 1 live `ta.crossover(` (zero-line cross up) plus 1 live `ta.crossunder(` (zero-line cross down) — the third `crossover` token sits inside the `// Zero-line crossovers` comment, display prose only / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 6 `input.` (4 live trading inputs frozen below plus `leverageSize`/`positionSize` alert-payload parameters, fenced below) / 4 `position_size` reads (2 entry gates, 2 exit guards) / 0 `position_avg` / 0 `openprofit` / 0 `strategy.equity` / 1 `ta.cum(` / 2 `ta.ema(` / 2 `ta.lowest(` / 2 `ta.highest(` / 2 `alert(` (JSON execution-handoff strings only — no order-leg effect, disclosed) / 7 `plot` tokens (5 plot calls plus `plotshape` markers and display `bgcolor` — render only, cannot change any order).
- Six live trading inputs frozen (any other value is a different, unpinned rule): `fastLength = 3`, `slowLength = 10`, `signalThreshold = 0`, `divergenceLookback = 5`. The remaining two inputs (`leverageSize = 5.0`, `positionSize = 0.01`) parameterize only the alert-JSON handoff strings, never an order leg — house sizing/capital/costs replace the absent source economics (see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Repo index-table row (same repository `README.md`, fetched live 15,427 bytes this cycle): `| [Chaikin Oscillator](strategies/momentum/chaikin_oscillator.pine) | Volume | 54% | 4H | Accumulation/distribution momentum |`. The `54%` figure ships with no table, figure, section, sample, or cost provenance anywhere in the repository — per the exact-numbers rule this record omits it entirely and claims no source-reported performance. The `4H` frame token is adopted as the record's decision timeframe (source-table-faithful, disclosed here, not code-derived).
- Page performance language is otherwise absent — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the pinned file carries no licence gate; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures (the source is market-agnostic via `syminfo.ticker` — the code names no symbol); (2) decision timeframe `4h` per the repo index-table row (the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction); (3) same-bar-close fills on completed-bar decisions (the source ships no `process_orders_on_close`/`calc_on_every_tick` argument, so its backtest fills next-bar by language default; this record freezes completed-bar evaluation with same-bar-close execution and scopes any live intrabar behavior out, see Limitations); (4) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the EMA-10 seed plus the 5-bar divergence window plus margin; see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `3/10/0/5` inputs, the money-flow-multiplier and AD-line arithmetic, the fast-minus-slow oscillator, the cross-plus-momentum/divergence entry pair, the fixed `Long`/`Short` order IDs, the opposite-signal exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `chaikin_oscillator`, `chaikin-oscillator`, and `EternaHybrid` return zero strategy records using this source, author script, file, or repository. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Name-fragment caution, fenced explicitly: the pool record `mass-index-threshold-latch-reversal` embeds a source block whose FMZ page title contains the words `Chaikin Oscillator`, but its coded construction is Donald Dorsey's Mass Index (`sum(ema(high-low,9)/ema(ema(high-low,9),9),25)` latched at `26.5` — no AD line, no EMA pair, no zero cross, no volume read); the five-axis distinction in Signal and Negative evidence shows zero overlap with the AD-cumulative MACD construction pinned here. Closest pool records are different mechanism classes: `cmf-velocity-zero-cross-ema200-bracket` trades a bounded windowed CMF ratio with a velocity gate inside an EMA-200 bracket (never a cumulative AD line, never a fast-minus-slow EMA pair); `obv-ema-crossover-trend` crosses cumulative signed volume against its own EMA (no range-position weighting, no zero-line semantics); `klinger-volume-oscillator-trigger-flip` is a volume-force trigger flip with its own signal line; `macd-signal-cross-reversal` applies the MACD structure to price, not to the money-flow-weighted AD line. Five-axis distinction: mechanism differs (MACD structure on the cumulative range-position-weighted AD line, not on price or raw volume), signal construction differs (no pool record computes `ta.ema(ta.cum(mfm*volume),3) - ta.ema(ta.cum(mfm*volume),10)`), trigger differs (zero-line cross confirmed by two-bar oscillator momentum, OR a 5-bar price/oscillator divergence — not a bracket, band, or signal-line cross), data differs (high/low/close/volume jointly through the multiplier — no pool record reads the money-flow multiplier), and source identity differs (EternaHybridExchange commit `01e4346`, 2026-03-12).

## Economic mechanism

### Source-reported

Money-flow-momentum reversal (code plus index-table description `Accumulation/distribution momentum`, no performance section ships): each bar's close position inside its range weights that bar's volume into a cumulative Accumulation/Distribution line; a fast EMA (3) minus a slow EMA (10) of that line yields the Chaikin Oscillator, which prints positive while money-flow momentum accelerates upward and negative while it decays. A zero-line cross confirmed by two consecutive oscillator steps in the cross direction — or a 5-bar divergence between price extremes and oscillator extremes — opens a position in the signal direction; the opposite signal closes it. There is deliberately no stop, no target, and no flat state beyond pre-signal bars — the order block ends with the two `strategy.close` guards and no risk leg ships anywhere, by design gap rather than by hidden leg.

### Research interpretation

Volume-weighted MACD on the AD line, two-sided with reversal exits — the first true-Chaikin-Oscillator record in the pool. Unlike price MACD (`macd-signal-cross-reversal`), the input series is not price but the cumulative money-flow line, so the trigger fires on institutional conviction shifts (close-near-high on high volume) that a price EMA pair cannot see; unlike bounded windowed money-flow ratios (`cmf-velocity`), the oscillator is unbounded and cumulative, so its zero line stays a reachable state at any crypto volume scale without retuning; unlike OBV (`obv-ema-crossover`), every volume print is first scaled by where the bar closed inside its range, so low-conviction mid-range volume contributes near zero. Note the two pinned asymmetries, stated plainly: first, entries need either cross-plus-momentum or divergence — a bare zero cross without two confirming oscillator steps fires nothing, so slow grinds through zero are ignored by construction; second, the divergence legs require the oscillator to sit on the System's own side of zero (`chaikin < 0` for longs, `> 0` for shorts), so late-stage divergences after the oscillator has already crossed fire nothing — the setup is early-turn only, disclosed. The bet is on money-flow momentum turns at frozen `3/10/0/5` geometry, not on any price level, volatility extreme, calendar effect, or trend-rail position.

## Signal

Exact rule as pinned (`fastLength 3 / slowLength 10 / signalThreshold 0 / divergenceLookback 5` frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy("Chaikin Oscillator - Eterna MCP", shorttitle="Chaikin", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)` semantics preserved with the derived `BTCUSDT 4h` market/frame pin and same-bar-close execution adopted (see derived declaration) and house sizing/costs replacing the source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires while positioned are blocked by the `position_size == 0` entry gates, opposite entries arrive only via the close-then-enter path below.
- Indicator (pinned arithmetic — evaluated from the frozen inputs, not tuned): `mfm = ((close - low) - (high - close)) / (high - low)` (money-flow multiplier, +1 at the high, −1 at the low); `mfv = mfm * volume`; `ad = ta.cum(mfv)` (cumulative AD line); `chaikin = ta.ema(ad, 3) - ta.ema(ad, 10)` — all causal recursion on completed bars.
- Zero-cross legs: `bullishCross = ta.crossover(chaikin, 0)`; `bearishCross = ta.crossunder(chaikin, 0)`.
- Momentum confirmation: `bullishMomentum = chaikin > chaikin[1] and chaikin[1] > chaikin[2]`; `bearishMomentum` mirrored. A bare cross without two confirming steps fires nothing — coded, not invented.
- Divergence legs (5-bar window, exact Pine float-equality semantics, disclosed): `bullishDiv = low == ta.lowest(low, 5) and chaikin > ta.lowest(chaikin, 5) and chaikin < 0` (price prints a 5-bar low while the oscillator holds above its own 5-bar low, still negative); `bearishDiv` mirrored with `high == ta.highest(high, 5)` and `chaikin > 0`.
- Entry long: `strategy.entry("Long", strategy.long)` under `if buySignal and strategy.position_size == 0` where `buySignal = (bullishCross and bullishMomentum) or bullishDiv` — fires on completed bars with same-bar-close execution under the derived declaration.
- Entry short: `strategy.entry("Short", strategy.short)` under `if sellSignal and strategy.position_size == 0` where `sellSignal = (bearishCross and bearishMomentum) or bearishDiv` — mirrored.
- Exits (coded, the sole position-closing path): `strategy.close("Long")` under `if sellSignal and strategy.position_size > 0`; `strategy.close("Short")` under `if buySignal and strategy.position_size < 0`. No stop, no target, no trailing exit leg, no time exit — pinned as written, explicitly none, not invented.
- Direction: two-sided with no coded flat state past seeding (after the first signal the system is always in market — disclosed, not enabled). Equality/`na` bars (Pine comparisons against `na` are false — e.g. a zero-range `high == low` bar poisons `mfm` to `na`) fire no leg and the inherited position simply persists by language semantics, disclosed, not invented.
- Display isolation: the `plot`/`plotshape`/`hline`/`bgcolor` calls render only and cannot change any order; the two `alert(` JSON strings are execution-handoff payloads with no order-leg effect. No order logic reads any display output.

## Required data

- Completed `4h` bars of BTCUSDT: `high`, `low`, `close`, and `volume` (via the `mfm`/`mfv` reads and their `[1]/[2]` oscillator lags plus the 5-bar `lowest`/`highest` divergence windows). No `open`-series read ships in any live line; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `4h` (index-table-faithful; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks a cumulative `ta.cum` seed beneath an EMA-10 smoother and 5-bar extreme windows (structural lag ≈ 15 bars). The adopted warmup is the first 100 completed `4h` bars flat by record rule (predeclared researcher choice — roughly six times the structural lag with smoother-decay margin; ≈17 days of `4h` history). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar under the derived freeze. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills. Binance spot/futures candle volume is the point-in-time print for the completed bar — no restatement, no revision.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the source names no market — `syminfo.ticker`-agnostic — so the venue/symbol pin is a researcher market choice, disclosed, never presented as source-native; the `4h` frame comes from the source index table).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close`/`calc_on_every_tick` argument (quoted verbatim in census) — its backtest fills next-bar by language default; this record does not claim that source behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long `if` before short `if`): `buySignal` and `sellSignal` cannot both print on one bar by construction (a cross-up and a cross-down of the same zero line are mutually exclusive, and the two divergence legs require opposite oscillator signs), so at most one entry leg can fire on any bar; an exit guard and its opposite entry can co-print (e.g. `sellSignal` while long closes Long, and the short entry gate `position_size == 0` reads the pre-close position intrabar — under Pine semantics the close executes first and the flat-gated entry fills the same bar, i.e. a full reversal; this record pins that reversal as the close-then-enter same-bar path, disclosed).
- Engine path for `4h` (gate 5, stated plainly): `4h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `4h` candles (`high`/`low`/`close`/`volume`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h`/`2h`/`15m`/`30m`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name). Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only Pine-default economics (`percent_of_equity 100 / initial_capital 1000`, no commission/slippage/funding/margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) plus alert-payload-only `leverageSize`/`positionSize` parameters with no order-leg effect — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default single-position semantics hold — at most one open position under the order IDs `Long`/`Short`; entries are flat-gated, exits are opposite-signal closes with a same-bar close-then-enter reversal path (above), and re-placement is allowed immediately on the next qualifying bar after any close (no cooldown specified — explicitly none, not invented). `na` bars hold the inherited position by language semantics, disclosed. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `3/10/0/5` inputs, money-flow multiplier, volume-weighted cumulative AD line, fast-minus-slow oscillator, cross-plus-two-step-momentum entry pair, 5-bar price/oscillator divergence pair, fixed `Long`/`Short` order IDs with flat-gated entries and opposite-signal closes), the active `strategy("Chaikin Oscillator - Eterna MCP", ...)` declaration, the repo index-table row (`Volume | 54% | 4H | Accumulation/distribution momentum` — percentage omitted for want of provenance, frame adopted as disclosed). It ships zero traceable performance numbers: no return, no win rate with sample, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the sole position-closing path is the coded opposite-signal `strategy.close` pair. The absence is coded (the order block ends with the two close guards and only plotting follows) and the prose carries no risk leg anywhere.
2. Bare crosses fire nothing, stated plainly: entries require `(crossover and two-step momentum) or divergence` — substituting edge-only zero-cross entries would be a different, unpinned rule. The lone extra `crossover` token is inside the `// Zero-line crossovers` comment — display prose, never an order leg.
3. Divergence legs fenced: exact 5-bar windows with Pine float-equality extremes (`low == ta.lowest(low, 5)`) and same-side-of-zero requirements (`chaikin < 0` long / `> 0` short) — late-stage divergences after the oscillator has crossed fire nothing by construction, disclosed.
4. No future leakage in the stack, stated plainly: at decision bar `t`, the `mfm`/`mfv`/`ad`/`chaikin` legs plus the `[1]/[2]` momentum lags and the 5-bar `lowest`/`highest` windows read completed-bar prints through `t` and seeded priors only. No `security()`, no `request.*`, no negative index, no `open` read, no `barstate.islast`-gated path; zero-range bars degrade to `na`-hold, never to a forward read.
5. Same-bar ordering fenced: at most one entry leg can fire per bar (mutually exclusive cross directions and opposite-sign divergence requirements); the co-printing exit-plus-opposite-entry path is pinned as a same-bar close-then-enter reversal, disclosed under Execution assumptions. Deterministic under the declared fill convention.
6. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own flat-gated `if`; both `strategy.close` guards cover the opposite-signal exits; no third direction exists. No flat state is coded after the first signal — always-in-market past seeding, disclosed.
7. Unbounded-oscillator reachability, admitted plainly: because the AD line is cumulative and volume-scaled, the oscillator has no universal overbought/oversold levels — the record uses only the zero line and relative extremes, so both directions stay reachable at any crypto volume scale without retuning; while a market that grinds without printing a confirmed cross or divergence is simply not traded, and a position whose pair never prints the opposite signal is held indefinitely with no stop. This is the coded posture, disclosed as the record's principal risk.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the index-table `4h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the inputs, multiplier/AD/oscillator arithmetic, cross/momentum/divergence legs, order IDs, gating, exits, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the alert-JSON execution handoff of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `3/10` AD oscillator / `0` threshold / `5`-bar divergence / cross-plus-momentum or divergence entries / opposite-signal exits / two-sided / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Momentum-gate relevance: dropping the two-step momentum confirmation (bare zero-cross entries, same exits) must not improve net expectancy; fail ⇒ the coded confirmation adds nothing over its bare-cross twin.
- F2 — Divergence-leg relevance: disabling both divergence legs (cross-plus-momentum entries only, same exits) must not improve net expectancy; fail ⇒ the coded divergence pair adds nothing over its cross-only twin.
- F3 — Volume-weighting relevance: replacing the range-position-weighted AD line with a plain cumulative signed-volume (OBV-style) line through the same `3/10` oscillator and entries must not improve net expectancy; fail ⇒ the money-flow weighting adds nothing over its OBV twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `4h` under the house overlay (market pin is a researcher choice on a market-agnostic source; the `4h` frame is index-table-faithful). The `high`/`low`/`close`/`volume` multiplier arithmetic ports across perpetual venues without structural change; venue volume-definition differences move the oscillator's scale but the rule reads only the zero line and relative extremes, never an absolute level — disclosed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no `process_orders_on_close`/`calc_on_every_tick` argument (backtest fills next-bar by language default); this record evaluates completed bars only and executes same-bar-close on `4h` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live intrabar behavior is out of scope.
- Derived market pin: the code names no symbol (`syminfo.ticker`-agnostic) — BTCUSDT is a researcher market choice for the house universe, never a source claim.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind. The `54%` index-table figure is omitted for want of traceable provenance.
- No price stop, no time stop, no flat state: adverse excursion after placement has no guardrail beyond the opposite-signal close; a position whose pair never prints the opposite signal is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Zero-range and seed bars: a `high == low` bar poisons `mfm` to `na` (comparisons against `na` are false — the bar holds position); the cumulative AD seed plus EMA-10 smoothing dominate early bars; the first 100 `4h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Alert-handoff quarantine: the two `alert(` JSON strings (`Eterna MCP` execution handoff with `leverageSize`/`positionSize` parameters) are payload text with no order-leg effect — treating them as order semantics would be a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/chaikin_oscillator.pine (primary source — executable `//@version=5` strategy, 99 lines, fetched live 2026-10-12 at pinned commit byte-identical to `master`, 4,115 bytes, SHA-256 `b50925e3…97bf896e`; repo index row `Volume | 54% | 4H` — percentage omitted, frame adopted as disclosed)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
