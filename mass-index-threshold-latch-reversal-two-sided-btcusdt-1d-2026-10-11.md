---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Mass Index 26.5-threshold latch reversal two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-27
sources:
  - https://www.fmz.com/strategy/442924
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Mass Index 26.5-threshold latch reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page fetched live over HTTPS and read in full during this cycle, verified 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/442924 (page title `Short-term Trading Strategy Based on Momentum Indicator`, publisher account `ChaoZhang`, `Created: 2024-02-27 14:07:09` stamp on the page — adopted as `source_as_of` 2024-02-27). Prose states the full rule twice (Chinese plus English `[trans]`): smooth the high-minus-low range with two EMAs, take the summed ratio as the Mass Index, go short when the index crosses above a threshold, go long when it crosses below. The page-embedded `/*backtest*/` header reads `start: 2023-02-20 00:00:00`, `end: 2024-02-26 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. The strategy-arguments table pins `Fast 3`/`Slow 10` display defaults alongside `Trigger 26.5` and `Trade reverse false` (the two moving-average rows belong to the page-template prose illustration; the executable block below takes only `Length1 9`, `Length2 25`, `Trigger 26.5`, `reverse false` — quoted verbatim in census).
- Full `//@version=2` block verified live inside the canonical page itself (the page embeds the complete executable source: `Copyright by HPotter v1.0 12/09/2017`, `strategy(title="Money Flow Indicator (Chaikin Oscillator)", shorttitle="MFI")`, inputs `Length1 = input(9, minval=1)`, `Length2 = input(25, minval=1)`, `Trigger = input(26.5, step = 0.01)`, `reverse = input(false, title="Trade reverse")`, `hline(27, ...)` setup line plus `hline(Trigger, ...)` trigger line, `xPrice = high - low`, `xEMA = ema(xPrice, Length1)`, `xSmoothXAvg = ema(xEMA, Length1)`, `nRes = sum(iff(xSmoothXAvg != 0, xEMA / xSmoothXAvg, 0), Length2)`, the `pos` latch, the `possig` reverse switch, both `strategy.entry` legs, the `barcolor(...)` assignment, and the final `plot(nRes, color=red, title="MASS Index")`). No login wall stands between the reader and any order-gating line: every line that can open, close, or size a position was read verbatim from the canonical page.
- Text census over the pinned code block: 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, no price argument) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` (the rule reads `high`/`low` only — `xPrice = high - low`; neither `open`, `close`, nor `volume` appears in any order-gating line) / exactly 4 `input(` (`Length1 9`, `Length2 25`, `Trigger 26.5`, `reverse false` — all strategy inputs, no webhook strings) / `process_orders_on_close` unset (Pine default: signals evaluate per completed bar, fills on the next bar) / `pyramiding` unset (Pine default: no same-direction adds) / no `commission`/`slippage` arguments (Pine defaults — recorded as absent, never as zero-cost evidence; see Execution assumptions).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the prose risk section only muses that a stop loss could be added (`Needs stop loss`, `Incorporate stop loss strategy`) — the no-stop/no-target posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the pinned code block carries `// Copyright by HPotter v1.0 12/09/2017` with an educate-only warning. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) market/frame pin `BTCUSDT 1d` — this one is near-lossless (the source executable `/*backtest*/` header already backtests `period: 1d` on `Futures_Binance BTC_USDT`; only the venue spelling and house-universe framing are normalized, disclosed here, never presented as a different claim); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 40-bar warmup with pre-warmup bars flat by record rule (covers the 9-bar EMA seed plus the 25-bar ratio sum plus margin — see Required data) and house sizing/capital/costs replacing the absent source economics (the source ships no commission/slippage/capital/funding/margin assumption at all — see Execution assumptions). The range-ratio-sum formula, the `9/25` lengths, the `26.5` trigger, the `reverse=false` setting, the threshold-latch state machine, the `Long`/`Short` order IDs, the two-sided reversal handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree case-insensitive search for `mass-index`, `massindex`, and `demarker` returns zero hits anywhere — no admitted rule uses this source, author strategy, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs contain no Mass Index record. Closest pool records are different mechanism classes: `cmf-velocity-zero-cross-ema200-bracket` is a normalized Chaikin-Money-Flow ratio with a velocity gate inside an EMA-200 bracket (never a 25-bar sum of EMA ratios of the raw high-low range, never a single-level latch); `klinger-volume-oscillator-trigger-flip` is a volume-force oscillator trigger flip (reads `volume`; this rule reads no volume at all); `obv-ema-crossover-trend` crosses an OBV line against its EMA (cumulative signed volume; this rule never touches volume or a cross of two indicator lines — its only comparison is index-versus-constant); `ultimate-oscillator-oversold-breakout` is a three-frame weighted momentum breakout (never a range-volatility latch). Five-axis distinction: mechanism differs (Donald-Dorsey range-expansion latch with binary ±1 state and reversal exits — versus money-flow ratios, volume oscillators, or momentum breakouts), signal construction differs (no pool record computes `sum(ema(high-low,9)/ema(ema(high-low,9),9),25)`), trigger differs (index-above-`26.5` short state versus index-below-`26.5` long state, held until the opposite placement — not a cross, not a band touch, not a flip on opposite signal), data differs (high/low only; no close, open, volume, or multi-frame read), and source identity differs (ChaoZhang 442924, 2024-02-27, HPotter v1.0 block).

## Economic mechanism

### Source-reported

Range-exhaustion reversal (page Overview/Principles plus code, no performance section ships): as a trend matures, the daily high-low range widens and the Mass Index — a 25-bar sum of the fast-to-slow EMA ratio of that range — rises; when volatility stretches past the `26.5` trigger the move is deemed climactic and the system holds short, and when the range contracts back below `26.5` the exhaustion is deemed spent and the system holds long. The design bets that volatility expansion predicts reversal rather than continuation, and it expresses that bet as a latched two-sided state, not as a one-shot cross: once placed above or below the trigger, the posture persists until the index prints on the opposite side. There is deliberately no stop, no target, and no flat state after the first placement — the prose admits risk controls are absent and lists them only as future optimization, by design gap rather than by hidden leg.

### Research interpretation

Single-threshold volatility latch, two-sided with reversal exits and an explicit pre-first-signal flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a cross at all: its only comparison is index-versus-constant (`26.5`), and the `pos` latch (`nz(pos[1], 0)` memory) makes every non-crossing bar a hold, not a decision. Unlike always-in-market flip systems, the rule rests flat before the first threshold placement (the latch seeds from `0`, and `0` fires neither entry leg). The price of the latch is whipsaw at the line: an index that flickers across `26.5` prints full long/short reversals at the worst prints of each flicker, and a strong trend whose range stays expanded keeps the system short into the teeth of continuation — the coded rule shorts climactic expansion rather than fading it with confirmation. The bet is on range-exhaustion reversal, not on any trend persistence, volume print, mean-reversion level, or calendar effect.

## Signal

Exact rule as pinned (`9/25` lengths, `26.5` trigger, `reverse=false` frozen — any other value is a different, unpinned rule):

- Declaration (derived): `strategy(title="Money Flow Indicator (Chaikin Oscillator)", shorttitle="MFI")` semantics preserved with the derived `BTCUSDT 1d` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing/costs replacing the absent source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires are no-ops, opposite entries reverse in full.
- Index (pinned): `xPrice = high - low`; `xEMA = ema(xPrice, 9)`; `xSmoothXAvg = ema(xEMA, 9)`; `nRes = sum(iff(xSmoothXAvg != 0, xEMA / xSmoothXAvg, 0), 25)` — the zero-guard ships in the source (a zero denominator contributes `0` to the sum, never `na`, never an error). Every input is a completed bar's `high`/`low`; no `open`, `close`, or `volume` is read.
- State latch (pinned): `pos = iff(nRes > Trigger, -1, iff(nRes < Trigger, 1, nz(pos[1], 0)))` with `Trigger = 26.5` — strictly above places short state, strictly below places long state, exact equality holds the prior state. With `reverse = false`, `possig = pos`.
- Entry long: `strategy.entry("Long", strategy.long)` under `if (possig == 1)` — fires on any completed bar whose latched state is long, with same-bar-close execution under the derived declaration. Refires while already long are no-ops under default no-pyramiding semantics.
- Entry short: `strategy.entry("Short", strategy.short)` under `if (possig == -1)` — fires on any completed bar whose latched state is short, with same-bar-close execution under the derived declaration. From flat it opens short; from long it reverses to short in full (the sole exit path — coded, not invented).
- Direction: two-sided with an explicit pre-first-signal flat state (the latch seeds `pos` from `0` via `nz(pos[1], 0)` and `0` fires neither leg; before the ratio sum first places on either side of `26.5`, no order can fire). After the first placement the system is always in market (long or short) — there is no coded flat state beyond the seed, disclosed, not enabled.
- Display isolation: the `hline(27, ...)` setup line, the `hline(Trigger, ...)` trigger line, the `barcolor(...)` assignment, and `plot(nRes, ...)` render only and cannot change any order; order logic reads exactly the two `if` lines. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (range input), `low` (range input). No `open`, no `close`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the source executable header's `period: 1d`; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: the EMA-9 seed needs 9 completed `1d` bars and the ratio sum reads 25 terms — binding constraint is bar index ≥ 33 before every referenced value is fully seeded. The adopted warmup is the first 40 completed `1d` bars flat by record rule (predeclared researcher choice — covers seed, sum window, and margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's high/low enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the source executable header already backtests `Futures_Binance BTC_USDT` at `period: 1d` — venue transfer and symbol spelling are disclosed here, never presented as a different claim).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long block before short block): `possig` takes exactly one of `1`/`-1`/`0` per bar, so at most one leg can fire on any bar — no same-bar double-fill ordering exists under either evaluation order.
- Sizing/capital/costs: the source ships no economics at all (no capital, no commission/slippage argument, no funding, no margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default no-pyramiding semantics hold — at most one open position under the fixed order IDs `Long`/`Short`; same-direction refires while already positioned are no-ops by the pinned default, the opposite entry reverses in full (the sole position-closing path), an entry while flat opens, and re-placement is allowed immediately on the next qualifying bar after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction (high-minus-low range, dual EMA-9 smoothing, 25-bar ratio sum with zero-guard, `26.5` single-trigger latch, `reverse=false`, fixed `Long`/`Short` order IDs, display-only hlines/barcolor/plot), the active `strategy(...)` declaration, the `Money Flow Indicator (Chaikin Oscillator)` / `MASS Index` titles, the four pinned inputs, and the `/*backtest*/` header (2023-02-20→2024-02-26, `1d`, `Futures_Binance BTC_USDT`). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the coded opposite-state `strategy.entry` reversal. The absence is coded (the order block ends with the short leg and only display code follows it in evaluation order) and the prose lists risk controls only as future optimization (`Needs stop loss`, `Incorporate stop loss strategy`).
2. Coded rule is a single-level latch, not the textbook Dorsey reversal bulge, stated plainly: Dorsey's classic signal arms above `27` and fires on retreat below `26.5`; this source's `hline(27, ...)` setup line renders but gates nothing — the only comparison any order leg reads is `nRes` versus the single `Trigger = 26.5` with latch memory. This record pins the coded latch, never the textbook bulge; substituting the bulge would be a different, unpinned rule.
3. No future leakage in the smoothing, stated plainly: at decision bar `t`, `xEMA` reads completed-bar ranges through `t`, `xSmoothXAvg` reads `xEMA` values through `t`, and the sum reads 25 completed ratio terms — every input is a completed historical bar. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path.
4. Same-bar entry ordering fenced: `possig` is exactly one of `1`/`-1`/`0` per bar (the latch's three branches are mutually exclusive by strict inequalities plus else-hold), so at most one of the two entry legs can fire on any bar. Deterministic under either fill convention.
5. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own guarded `if`; no third direction exists. The `reverse` switch is pinned `false` — enabling it would invert both sides and would be a different, unpinned rule.
6. Range-flicker whipsaw, admitted plainly: an index oscillating across `26.5` prints full long/short reversals at the worst prints of each flicker, and a sustained expansion holds short through continuation. There is no confirmation filter, no stop, and no flat state after the first placement — the coded posture, disclosed as the record's principal risk.
7. The `high-low` range source, the dual EMA-9 smoothing, the 25-bar ratio sum with zero-guard, the `26.5` trigger, the `reverse=false` setting, the strict latch inequalities, the fixed `Long`/`Short` order IDs, the reversal-only exits, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length or the trigger, converting the latch into a cross, adding a stop/target/filter/cooldown, enabling `reverse`, or gating on the display-only `27` setup line would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 40-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the ratio-sum formula, lengths, trigger, latch, order IDs, reversal handling, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: high-low range / dual EMA-9 / 25-bar ratio sum / `26.5` latch / `reverse=false` / reversal exits / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Direction relevance: inverting the side mapping (above-`26.5` long, below-`26.5` short, same latch mechanics) must not improve net expectancy; fail ⇒ the coded exhaustion direction adds nothing over its mirror.
- F2 — Latch relevance: replacing the single-`26.5` latch with the textbook Dorsey bulge (arm above `27`, fire only on retreat below `26.5`, same entries) must not improve net expectancy; fail ⇒ the coded single-level latch is dominated by the textbook two-line construction it resembles.
- F3 — Memory relevance: replacing the 25-bar ratio sum with the un-summed spot ratio (`xEMA/xSmoothXAvg` of the latest bar only, same trigger and latch) must not improve net expectancy; fail ⇒ the 25-bar summation memory adds nothing over the instantaneous ratio.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin from an already-Binance-`1d`-backtested source). The high/low arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar on a `1d` Binance backtest with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market spelling: the source header backtests `Futures_Binance BTC_USDT`; this record pins `BTCUSDT` under the house overlay. Venue-transfer differences are real — the adaptation is disclosed, and this record makes no claim about any other venue's performance.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no post-placement flat: adverse excursion after placement has no guardrail beyond the opposite-threshold reversal; a position whose index never prints on the opposite side of `26.5` is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Chop sensitivity: threshold flicker prints full reversals in ranging markets, and sustained expansion holds shorts through continuation. The latch-plus-reversal construction is the coded design, disclosed, not smoothed.
- Short source window: the source header backtests a single ~12-month window (2023-02-20→2024-02-26); this record inherits the rule, never any window-specific performance claim.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang, 2024-02-27, full executable Pine verified live in-page): https://www.fmz.com/strategy/442924
- Pine strategy semantics (order calls, default execution, history-referencing semantics): https://www.tradingview.com/pine-script-reference/v5/
