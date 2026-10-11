---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: RSI pivot divergence oscillator reversal two-sided on BTCUSDT 4h bars
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
  - https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/rsi_divergence.pine
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI pivot divergence oscillator reversal two-sided on BTCUSDT 4h bars

## Provenance

Primary source read end to end (raw file fetched live over HTTPS twice this cycle — floating `master` and pinned commit — byte-identical, 3,456 bytes, SHA-256 `7c4c6bd154ac8f61b53d3b564bad17a98c57563e76b94b005a4d688576ce7f11`):

- Repository: https://github.com/EternaHybridExchange/tradingview-strategies (`master` default branch; repo created 2026-03-12; open-source collection of executable Pine Script strategies with alert-JSON handoff for automated execution).
- Immutable pin: commit `01e4346df876f6fd124332e40a2cd62286174894` (2026-03-12T18:38:03Z, `Initial commit: 20 Pine Script strategies with Eterna MCP in`), path `strategies/momentum/rsi_divergence.pine` (84 lines, `//@version=5`). Adopted `source_as_of` 2026-03-12 is that commit's date, disclosed here, never an authorship date.
- Strategy declaration (source-verbatim): `strategy("RSI Divergence Strategy - Eterna MCP", shorttitle="RSI Div", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)`. No `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission` argument ships — Pine language defaults govern the unfrozen timing, fenced below.
- Text census over the pinned 84-line file: 1 `strategy("` declaration / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, gated by `strategy.position_size == 0`, alert JSON attached, no price/qty/when order argument) / 2 `strategy.close` (`"Long"` closed when the bearish divergence prints while long; `"Short"` closed when the bullish divergence prints while short) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 live `crossover(`/`crossunder(` (no cross of two series anywhere — the trigger is strict-inequality pivot comparisons, disclosed) / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 6 `input.` (4 live trading inputs frozen below plus `leverageSize`/`positionSize` alert-payload parameters, fenced below) / 4 `position_size` reads (2 entry gates, 2 exit guards) / 0 `position_avg` / 0 `openprofit` / 0 `strategy.equity` / 1 `ta.rsi(` / 2 `ta.pivothigh(` / 2 `ta.pivotlow(` / 2 `alert(` (JSON execution-handoff strings only — no order-leg effect, disclosed) / display tokens only: 1 `plot(` (RSI line) plus 3 `hline` (70/50/30 guides) plus 2 `plotshape` (divergence triangles) — render only, cannot change any order.
- Four live trading inputs frozen (any other value is a different, unpinned rule): `rsiLength = 14`, `rsiOverbought = 70`, `rsiOversold = 30`, `pivotLookback = 5`. The remaining two inputs (`leverageSize = 5.0`, `positionSize = 0.01`) parameterize only the alert-JSON handoff strings, never an order leg — house sizing/capital/costs replace the absent source economics (see Execution assumptions).
- No risk layer ships anywhere in the executable code: zero stop/target/trailing/time-exit order legs — the no-stop/no-target posture below is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention. The README's Risk Management line `Set stop-loss at recent swing high/low` is prose-only generic advice with no length, distance, or order leg anywhere in the 84-line file — this record follows the code, never the prose, and pins explicitly-no-stop/no-target (see Negative evidence).
- Sibling README (same repository, `strategies/momentum/README_rsi_divergence.md`, fetched live this cycle): Recommended Timeframes `Primary: 1H, 4H` / `Secondary: 15m, 1D` / `Not recommended: < 5m (too noisy)`; Optimal Settings `BTC/ETH: RSI Length 14, Pivot 5, Timeframe 4H`. The `4H` frame token for BTC is adopted as the record's decision timeframe (source-table-faithful, disclosed here, not code-derived — the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction).
- Performance language fenced and discarded: the README's Performance Notes (`Win rate: ~55-65% in ranging markets`, `Risk/Reward: 1:1.5 to 1:2`) ship with no table, figure, section, sample, trade count, or cost provenance anywhere in the repository — per the exact-numbers rule this record omits them entirely and claims no source-reported performance.

Licence and rights: the pinned file carries no licence gate; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures (the source is market-agnostic via `syminfo.ticker` — the code names no symbol); (2) decision timeframe `4h` per the sibling README's Primary list and its BTC/ETH-optimal-4H row (the code takes no timeframe input and makes no `request.*`/`security(` call, so it is single-frame by construction); (3) same-bar-close fills on completed-bar decisions (the source ships no `process_orders_on_close`/`calc_on_every_tick` argument, so its backtest fills next-bar by language default; this record freezes completed-bar evaluation with same-bar-close execution and scopes any live intrabar behavior out, see Limitations); (4) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the RSI-14 seed plus the 5-bar pivot-confirmation lag plus stored-pivot history plus margin; see Required data); (5) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `14/70/30/5` inputs, the RSI arithmetic, the four pivot reads, the last-confirmed-pivot register block, the zone-gated divergence pair, the fixed `Long`/`Short` order IDs, the opposite-signal exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `rsi_divergence`, `rsi-divergence`, `RSI Div`, and `EternaHybrid` return zero strategy records using this source script, file, or mechanism — the sole `EternaHybrid` hit is yesterday's Chaikin record (a different script, indicator, and trigger in the same repository, see five-axis distinction). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `pivot-point-breakout-kaufman-btcusdt-1d` uses `ta.pivothigh(3,3)`/`ta.pivotlow(3,3)` swing detection but trades confirmed price-level breakouts long-only (no oscillator, no divergence comparison, no short side); `camarilla-r1-s1-rail-cross` computes fractional-range rails with no swing detection anywhere; `rsi-classic-level-reversal` and `rsi-ma-crossover-reversal` trade RSI level/cross triggers with no pivot structure; `rsi-sma-gated-cross-reversal` is an RSI/SMA cross; yesterday's `chaikin-oscillator` divergence pair compares 5-bar price/oscillator extremes with float-equality semantics on a cumulative volume-weighted line with no pivot function, no zone gate, and a cross-plus-momentum entry leg this rule has no form of. Five-axis distinction: mechanism differs (confirmed-pivot price-vs-RSI divergence with zone gating, not a level cross, rail cross, price breakout, or zero-cross), signal construction differs (no pool record computes `ta.pivothigh/ta.pivotlow` on BOTH the RSI series and the price series with last-confirmed register storage), trigger differs (strict-inequality divergence legs — zero `crossover`/`crossunder` calls anywhere), data differs (`high`/`low`/`close` only; no `open`, no `volume` read in any live line), and source identity differs (Eterna `rsi_divergence.pine` at the pinned commit).

## Economic mechanism

### Source-reported

RSI-momentum reversal (code plus sibling README `price and momentum indicators move in opposite directions, often signaling potential trend reversals`, no performance section admitted): each completed bar prints RSI-14 on its close; confirmed pivot highs/lows of the RSI series (5 bars each side) are stored alongside the price pivots confirming on the same bar. A bullish leg fires when price undercuts its last stored price low while RSI holds above its last stored RSI low with RSI still under 30 — selling exhaustion the close alone cannot see. A bearish leg mirrors it above 70. The opposite divergence closes the position. There is deliberately no stop, no target, and no flat state beyond pre-signal bars — the order block ends with the two `strategy.close` guards and no risk leg ships anywhere, by design gap rather than by hidden leg.

### Research interpretation

Confirmed-pivot RSI divergence, two-sided with reversal exits — the first pivot-divergence record in the pool. Unlike RSI level/cross rules (`rsi-classic-level-reversal`, `rsi-ma-crossover-reversal`), the trigger never reads an RSI threshold crossing — it compares the bar's extreme against a stored confirmed pivot extreme on both the price and oscillator axes at once, so chop that merely tags 30/70 fires nothing; unlike the Kaufman pivot breakout (price levels only, long-only), both axes are pivot-structured and both directions trade; unlike the Chaikin divergence legs (float-equality 5-bar extremes on a cumulative volume line), the extremes here are confirmation-lagged pivot prints with explicit zone gates, so late-stage divergences after RSI has already left the zone fire nothing — the setup is exhaustion-inside-the-zone only, disclosed. The bet is on momentum non-confirmation at frozen `14/70/30/5` geometry, not on any price level, volatility extreme, calendar effect, or trend-rail position.

## Signal

Exact rule as pinned (`rsiLength 14 / rsiOverbought 70 / rsiOversold 30 / pivotLookback 5` frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy("RSI Divergence Strategy - Eterna MCP", shorttitle="RSI Div", overlay=false, default_qty_type=strategy.percent_of_equity, default_qty_value=100, initial_capital=1000)` semantics preserved with the derived `BTCUSDT 4h` market/frame pin and same-bar-close execution adopted (see derived declaration) and house sizing/costs replacing the source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires while positioned are blocked by the `position_size == 0` entry gates, opposite entries arrive only via the close-then-enter path below.
- Indicator (pinned arithmetic — evaluated from the frozen inputs, not tuned): `rsi = ta.rsi(close, 14)` — causal recursion on completed-bar closes.
- Pivot reads (all four confirmed with 5 bars each side — a pivot extreme at bar `t-5` first becomes readable on completed bar `t`, never repainting after confirmation): `pivotHigh = ta.pivothigh(rsi, 5, 5)` / `pivotLow = ta.pivotlow(rsi, 5, 5)` / `pricePivotHigh = ta.pivothigh(high, 5, 5)` / `pricePivotLow = ta.pivotlow(low, 5, 5)`.
- Register block (source-verbatim semantics, disclosed consequence): `var` registers `lastRsiHigh/lastPriceHigh/lastRsiLow/lastPriceLow` seeded `na`; `if not na(pivotHigh)` stores `pivotHigh` into `lastRsiHigh` and the as-of-that-bar `pricePivotHigh` into `lastPriceHigh` (which is `na` on bars where no price pivot confirms alongside — deterministic language behavior, not a gap); `if not na(pivotLow)` mirrors for the lows. Until both registers of a side are non-`na`, that side's guard is false and fires nothing.
- Bullish leg: `bullishDiv = not na(lastRsiLow) and not na(lastPriceLow) and low < lastPriceLow and rsi > lastRsiLow and rsi < 30` (completed bar undercuts the last confirmed price low while RSI holds above its last confirmed RSI low, RSI still in the sub-30 zone).
- Bearish leg: `bearishDiv = not na(lastRsiHigh) and not na(lastPriceHigh) and high > lastPriceHigh and rsi < lastRsiHigh and rsi > 70` (mirrored above 70).
- Entry long: `strategy.entry("Long", strategy.long)` under `if bullishDiv and strategy.position_size == 0` — fires on completed bars with same-bar-close execution under the derived declaration.
- Entry short: `strategy.entry("Short", strategy.short)` under `if bearishDiv and strategy.position_size == 0` — mirrored.
- Exits (coded, the sole position-closing path): `strategy.close("Long")` under `if bearishDiv and strategy.position_size > 0`; `strategy.close("Short")` under `if bullishDiv and strategy.position_size < 0`. No stop, no target, no trailing exit leg, no time exit — pinned as written, explicitly none, not invented. The README's `Set stop-loss at recent swing high/low` line is prose advice with no coded leg and is excluded here — a stop-carrying variant would be a different, unpinned rule.
- Direction: two-sided with no coded flat state past seeding (after the first signal the system is always in market — disclosed, not enabled). The two legs are mutually exclusive by construction (`rsi < 30` and `rsi > 70` cannot co-print), so at most one entry leg fires per bar; a co-printing exit-plus-opposite-entry resolves as the pinned same-bar close-then-enter reversal (see Execution assumptions).
- No-`na` surprises, stated plainly: Pine comparisons against `na` are false, so seeding bars and bars with half-confirmed registers fire no leg and any inherited position persists by language semantics, disclosed, not invented.
- Display isolation: the `plot`/`hline`/`plotshape` calls render only and cannot change any order; the two `alert(` JSON strings are execution-handoff payloads with no order-leg effect. No order logic reads any display output.

## Required data

- Completed `4h` bars of BTCUSDT: `high`, `low`, `close` (via the RSI read, the four pivot reads, and the `low < lastPriceLow` / `high > lastPriceHigh` comparisons). No `open`-series read and no `volume` read ships in any live line (the alert payload's `positionSize` is a string parameter, never a volume read); no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere.
- Single decision timeframe `4h` (README Primary list plus BTC/ETH-optimal-4H row; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the construction stacks an RSI-14 seed beneath 5-each-side pivot confirmation plus stored-register history (structural lag ≈ 20 bars before both registers of a side can first be non-`na`). The adopted warmup is the first 100 completed `4h` bars flat by record rule (predeclared researcher choice — roughly five times the structural lag with register-history margin; ≈17 days of `4h` history). No negative shift, no future reference, no full-sample normalization; one evaluation per completed bar under the derived freeze. Each bar's prints enter the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills, including the confirmation-lagged pivot values (a pivot extreme enters only via its confirmation bar's close, never at the extremum bar).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the source names no market — `syminfo.ticker`-agnostic — so the venue/symbol pin is a researcher market choice, disclosed, never presented as source-native; the `4h` frame comes from the source sibling README's Primary list and BTC/ETH-optimal row).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no `process_orders_on_close`/`calc_on_every_tick` argument (quoted verbatim in census) — its backtest fills next-bar by language default; this record does not claim that source behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long `if` before short `if`): the two legs cannot co-print (sub-30 RSI and above-70 RSI are mutually exclusive), so at most one entry leg can fire on any bar; an exit guard and its opposite entry can co-print (e.g. `bearishDiv` while long closes Long, and the short entry gate `position_size == 0` reads the pre-close position intrabar — under Pine semantics the close executes first and the flat-gated entry fills the same bar, i.e. a full reversal; this record pins that reversal as the close-then-enter same-bar path, disclosed).
- Engine path for `4h` (gate 5, stated plainly): `4h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `4h` candles (`high`/`low`/`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume leg, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h`/`2h`/`15m`/`30m`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name). Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only Pine-default economics (`percent_of_equity 100 / initial_capital 1000`, no commission/slippage/funding/margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) plus alert-payload-only `leverageSize`/`positionSize` parameters with no order-leg effect — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default single-position semantics hold — at most one open position under the order IDs `Long`/`Short`; entries are flat-gated, exits are opposite-signal closes with a same-bar close-then-enter reversal path (above), and re-placement is allowed immediately on the next qualifying bar after any close (no cooldown specified — explicitly none, not invented). `na`/half-confirmed-register bars hold the inherited position by language semantics, disclosed. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (frozen `14/70/30/5` inputs, RSI-14 on close, four 5-each-side pivot reads across the RSI and price series, last-confirmed-pivot register block, zone-gated strict-inequality divergence pair, fixed `Long`/`Short` order IDs with flat-gated entries and opposite-signal closes), the active `strategy("RSI Divergence Strategy - Eterna MCP", ...)` declaration, and the sibling README's timeframe table (`Primary: 1H, 4H`, BTC/ETH optimal `4H` — frame adopted as disclosed). It ships zero traceable performance numbers: no return, no win rate with sample, no profit factor, no trade count, no Strategy Tester table or figure (the README's `~55-65%` and `1:1.5 to 1:2` phrases are omitted for want of provenance) — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the sole position-closing path is the coded opposite-signal `strategy.close` pair. The absence is coded (the order block ends with the two close guards and only plotting follows). The README's stop-loss advice line is prose with no coded leg and is fenced out of the rule, not silently adopted.
2. No cross-of-two-series anywhere, stated plainly: 0 `crossover(`/`crossunder(` — substituting any MA/signal-line cross trigger would be a different, unpinned rule.
3. Divergence legs fenced: strict inequalities (`low < lastPriceLow`, `rsi > lastRsiLow`) with zone gates (`rsi < 30` long / `rsi > 70` short) — chop that merely tags the zone without undercutting a confirmed pivot fires nothing; divergences after RSI has left the zone fire nothing by construction, disclosed.
4. Register-timing consequence, admitted plainly: a price pivot confirming on a different bar than its RSI pivot stores `na` into that side's price register (source-verbatim `:=` semantics), and that side stays silent until a later bar re-stores both registers non-`na` — deterministic, disclosed, not patched.
5. No future leakage in the stack, stated plainly: at decision bar `t`, the RSI value, the current-bar extreme comparisons, and the confirmation-lagged pivot registers read completed-bar prints through `t` and seeded priors only. No `security()`, no `request.*`, no negative index, no `open` read, no `volume` read, no `barstate.islast`-gated path; confirmed pivots never repaint after confirmation.
6. Same-bar ordering fenced: the two legs are mutually exclusive (sub-30 vs above-70 RSI), so at most one entry leg fires per bar; the co-printing exit-plus-opposite-entry path is pinned as a same-bar close-then-enter reversal, disclosed under Execution assumptions. Deterministic under the declared fill convention.
7. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own flat-gated `if`; both `strategy.close` guards cover the opposite-signal exits; no third direction exists. No flat state is coded after the first signal — always-in-market past seeding, disclosed.
8. Exhaustion-inside-the-zone reachability, admitted plainly: because both legs require RSI inside the far zone at the signal bar, a market that trends without printing a zone-confined divergence is simply not traded, and a position whose pair never prints the opposite divergence is held indefinitely with no stop. This is the coded posture, disclosed as the record's principal risk.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the README-table `4h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the inputs, RSI arithmetic, pivot reads, register block, divergence legs, order IDs, gating, exits, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, prose stop-loss variant, or the alert-JSON execution handoff of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `14/70/30/5` RSI-pivot geometry / zone-gated divergence entries / opposite-signal exits / two-sided / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Zone-gate relevance: dropping the zone gates (pure pivot divergence without the sub-30/above-70 requirement, same exits) must not improve net expectancy; fail ⇒ the coded zone confinement adds nothing over its ungated twin.
- F2 — Pivot-structure relevance: replacing the confirmation-lagged pivot extremes with same-window float-equality extremes (`low == lowest(low, 11)` style, same exits) must not improve net expectancy; fail ⇒ the pivot-confirmation structure adds nothing over its window-extreme twin.
- F3 — Divergence-leg relevance: disabling both divergence legs in favor of plain RSI zone-cross entries (cross-up-30 long / cross-down-70 short, same exits) must not improve net expectancy; fail ⇒ the coded divergence pair adds nothing over its zone-cross twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `4h` under the house overlay (market pin is a researcher choice on a market-agnostic source; the `4h` frame is README-table-faithful). The `high`/`low`/`close` pivot arithmetic ports across perpetual venues without structural change; venue print differences move pivot locations but the rule reads only confirmed relative extremes, never an absolute level — disclosed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no volume-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no `process_orders_on_close`/`calc_on_every_tick` argument (backtest fills next-bar by language default); this record evaluates completed bars only and executes same-bar-close on `4h` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live intrabar behavior is out of scope.
- Derived market pin: the code names no symbol (`syminfo.ticker`-agnostic) — BTCUSDT is a researcher market choice for the house universe, never a source claim.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind. The README's `~55-65%` and `1:1.5 to 1:2` phrases are omitted for want of traceable provenance.
- Excluded prose stop: the README's `Set stop-loss at recent swing high/low` advice has no length, distance, or order leg in the executable file and is excluded from the rule — a stop-carrying variant would be a different, unpinned claim.
- No price stop, no time stop, no flat state: adverse excursion after placement has no guardrail beyond the opposite-signal close; a position whose pair never prints the opposite divergence is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Seed and half-confirmed bars: registers seed `na` and a side stays silent until both its registers are non-`na`; bars with asynchronously confirming pivots store `na` price registers by source-verbatim semantics. The first 100 `4h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Alert-handoff quarantine: the two `alert(` JSON strings (`Eterna MCP` execution handoff with `leverageSize`/`positionSize` parameters) are payload text with no order-leg effect — treating them as order semantics would be a different, unpinned rule, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/EternaHybridExchange/tradingview-strategies/blob/01e4346df876f6fd124332e40a2cd62286174894/strategies/momentum/rsi_divergence.pine (primary source — executable `//@version=5` strategy, 84 lines, fetched live 2026-10-12 at pinned commit byte-identical to `master`, 3,456 bytes, SHA-256 `7c4c6bd1…88576ce7f11`; sibling README timeframe table `Primary: 1H, 4H` with BTC/ETH optimal `4H` — frame adopted as disclosed, performance phrases omitted)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
