---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: DSS-Bressert double-smoothed stochastic trigger-latch reversal two-sided on BTCUSDT 2h bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-04-05
sources:
  - https://www.fmz.com/strategy/441102
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8F%8C%E5%B9%B3%E6%BB%91%E9%9A%8F%E6%9C%BA%E6%8C%87%E6%95%B0%E5%B8%83%E9%9B%B7%E7%91%9F%E7%AD%96%E7%95%A5Dual-Smoothed-Stochastic-Bressert-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DSS-Bressert double-smoothed stochastic trigger-latch reversal two-sided on BTCUSDT 2h bars

## Provenance

Primary source read end to end (canonical FMZ strategy page fetched live over HTTPS plus the byte-pinned GitHub mirror file, verified 2026-10-12):

- Canonical page: https://www.fmz.com/strategy/441102 (title `双平滑随机指数布雷瑟策略Dual-Smoothed-Stochastic-Bressert-Strategy`, FMZ publisher `ChaoZhang`, page fetched live at 770,731 bytes: page id `441102`×4, `DSS Bressert`×2, `HPotter`×2, backtest-stanza `period: 2h`×1, `Futures_Binance`×2, `strategy.entry`×2 — page identity confirmed, zero performance numbers anywhere on the page: `Sharpe`/`Net Profit`/`Win Rate`/`Max Drawdown`/`Profit Factor` all 0).
- Byte-pinned mirror: `双平滑随机指数布雷瑟策略Dual-Smoothed-Stochastic-Bressert-Strategy.md` in `fmzquant/strategies` at repo HEAD `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified via `git ls-remote` during this cycle — the same pin as the prior dozen-plus PASS admissions). The pinned blob (`b29e72948d39f91823ef3f962ef3d4a0a847070e`, 7,196 bytes per the GitHub contents API at the pinned ref) was extracted from a local fetch and diffed byte-identical against the mirror text read this cycle (`diff -q` clean, 190 lines) — byte-level provenance, no paraphrase.
- Code header (source-verbatim): `Copyright by HPotter v1.0 05/04/2017` — adopted as `source_as_of` 2017-04-05 (same DD/MM/YYYY reading as prior HPotter admissions). The header names the construction as William Blau's Double Smoothed Stochastics with a paper-trading-only warning. The FMZ `Author: ChaoZhang` line is the FMZ publisher/uploader credit; the executable Pine block is HPotter-authored (both credits disclosed, never conflated).
- Executable spec (source-verbatim, stanza first): `start: 2024-01-05 00:00:00 / end: 2024-02-04 00:00:00 / period: 2h / basePeriod: 15m / exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` followed by the full `//@version=2` block: `strategy(title="DSS Bressert (Double Smoothed Stochastic)", shorttitle="DSS Bressert")`, inputs `PDS = input(10, minval=1)`, `EMAlen = input(9, minval=1)`, `TriggerLen = input(5, minval=1)`, `Overbought = input(80, minval=1)`, `Oversold = input(20, minval=1)`, `reverse = input(false, title="Trade reverse")`, the `xPreCalc`/`xDSS`/`xTrigger` lines, the `pos` latch, the `possig` map, both `strategy.entry` legs, the `barcolor(...)` assignment, and the `plot(xDSS, ...)` / `plot(xTrigger, ...)` pair. Every line that can open, close, or size a position was read verbatim from the pinned mirror.
- Text census over the pinned code block: 1 `strategy(` (title/shorttitle only — no `pyramiding`, no `process_orders_on_close`, no commission/slippage/capital argument) / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, no price/qty argument) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `stop=`/`limit=` / 0 `crossover`/`crossunder` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `var` / 1 `nz(` (`pos[1]` latch seed) / 0 `position_size` / 0 `position_avg` / 0 `openprofit` / 0 `equity` / 0 `volume` / 0 `open` (the rule reads `close`/`high`/`low` exactly once each, in the single `stoch(close, high, low, PDS)` call; neither `open` nor `volume` appears anywhere) / 3 `stoch(` / 3 `ema(` / 2 `hline` / 1 `barcolor` / exactly 6 `input(` (`PDS 10`, `EMAlen 9`, `TriggerLen 5`, `Overbought 80`, `Oversold 20`, `reverse false` — all strategy inputs; the mirror's `Strategy Arguments` table lists the same six with the same defaults, no date-window, no mode switch beyond `reverse`).
- Code-over-prose pin, fenced: the mirror prose (both Chinese and English) states longs when the trigger sits below DSS under the oversold line and shorts when above DSS over the overbought line — the executable latch codes the exact opposite (`xTrigger < xDSS` with `xTrigger < Oversold` maps to `-1`/Short; `xTrigger > xDSS` with `xTrigger > Overbought` maps to `+1`/Long). The code governs — this record freezes the coded mapping and treats the prose as an inverted description (same class of code-over-prose pin as the admitted TSI record, disclosed, never silently adopted).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the prose's stop-loss paragraphs sit under `优化方向/Optimization` (future optimization directions, explicitly not built) — the no-stop/no-target posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number — the advantage/risk prose is purely qualitative) — this record claims no source-reported performance and no reproduced performance. The stanza names the market and frame outright (`Futures_Binance BTC_USDT`, `2h`) — the `BTCUSDT 2h` pin below is source-faithful, not a researcher derivation.

Licence and rights: the pinned code block carries `// Copyright by HPotter v1.0 05/04/2017` with a paper-trading-only warning. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the `PDS = 10` double stochastic lookbacks plus the `EMAlen = 9` / `TriggerLen = 5` EMA seedings plus margin; see Required data); (3) house sizing/capital/costs replacing the absent source economics (the source ships no commission/slippage/capital/funding/margin assumption at all — see Execution assumptions). The `2h` frame, the Binance-futures BTCUSDT venue, the `close/high/low` price reads, the `10/9/5/80/20/false` inputs, the double-smoothed-stochastic arithmetic, the zone-conjunction latch map with `reverse = false` frozen, the `Long`/`Short` order IDs, the reversal-only exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive search for `dss`, `bressert`, `double.smooth`, `441102`, and `b29e7294` returns zero strategy records using this source, author script, or construction — no `main` record reads a double-smoothed stochastic anywhere in any order leg. The admitted `tsi-signal-cross` record is the closest Blau relative and is distinguished on four axes: it double-smooths bar-to-bar price change normalized by smoothed absolute change (bounded momentum), while this rule double-smooths a bounded stochastic twice (price-position within range, then stochastic-of-stochastic); it triggers on oscillator-vs-own-signal-EMA crosses, while this rule never trades a cross and fires only on trigger-vs-DSS zone conjunctions (`>80` / `<20`); it is always-in-market edge-triggered, while this rule is a zone latch that holds flat-to-seeded state through mid-zone chop; source identity differs (FMZ 428611 versus FMZ 441102). The `stochastic-ott-dual-trend` record crosses a single %K/%D pair under a trend-filter overlay with no smoothing stack and no zone latch — different formula, different trigger, different orders. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. No pool record evaluates a Blau double-smoothed stochastic, and no pool record latches entries on DSS/trigger zone conjunctions.

## Economic mechanism

### Source-reported

Double-smoothed range-position reversal (code header plus bilingual theory prose, no performance section ships): the first stochastic situates the close inside its `PDS`-bar high/low range and the first EMA smooths it (`xPreCalc`); the second stochastic re-situates that smoothed series inside its own `PDS`-bar range and the second EMA smooths it again (`xDSS`) — William Blau's double smoothing, which suppresses single-leg whipsaws at the cost of lag. A trigger EMA (`xTrigger`, length 5) rides the DSS line. When the trigger prints above DSS while above the overbought rail (`80`), upside exhaustion is deemed confirmed and the system holds long; when the trigger prints below DSS while below the oversold rail (`20`), it holds short — the coded mapping (prose inverted, code governs per the fenced pin above). There is deliberately no stop, no target, and no flat state after seeding — the header admits paper-trading-only status with no risk leg anywhere, by design gap rather than by hidden leg.

### Research interpretation

Zone-conjunction latch state machine, two-sided with reversal exits and an explicit pre-seed flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a cross at all: its only comparisons are trigger-versus-DSS plus trigger-versus-constant (`80`/`20`), and the `pos` latch makes every mid-zone print a hold — the system sits through the entire 20–80 middle band without acting. Unlike always-in-market flip systems, the rule rests flat while `pos` is `0` (the `nz(pos[1], 0)` seed fires neither leg until the first conjunction prints). Note the two pinned asymmetries, stated plainly: first, entries demand zone confirmation — a trigger/DSS cross in the middle band does nothing, so the system can ride a full mid-zone round trip flat; second, the `reverse` switch is frozen `false`, so `possig == pos` identically and direction inversion would be a different, unpinned rule. The price of the construction is double-smoothing lag: by the time both stochastic legs and both EMA legs agree inside a zone, the exhaustion move is mature, and a market that trends hard through a zone without a trigger/DSS inversion keeps the system faded against the push with no stop beyond the opposite-zone reversal. The bet is on post-exhaustion reversal at frozen `10/9/5/80/20` geometry, not on any trend level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (`PDS 10`, `EMAlen 9`, `TriggerLen 5`, `Overbought 80`, `Oversold 20`, `reverse false` frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy(title="DSS Bressert (Double Smoothed Stochastic)", shorttitle="DSS Bressert")` semantics preserved with the stanza-native `BTCUSDT 2h` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing/costs replacing the absent source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires are no-ops, opposite entries reverse in full.
- Indicator (pinned arithmetic — evaluated from the frozen inputs, not tuned): `xPreCalc = ema(stoch(close, high, low, 10), 9)`; `xDSS = ema(stoch(xPreCalc, xPreCalc, xPreCalc, 10), 9)`; `xTrigger = ema(xDSS, 5)` — all Pine v2 built-ins on completed bars: `stoch` is the 0–100 range-position function, `ema` the causal recursive average. No zero-guard ships in the source and none is needed (no division anywhere in the order path).
- State map (pinned, code-governed): `pos = iff(xTrigger < xDSS and xTrigger < 20, -1, iff(xTrigger > xDSS and xTrigger > 80, 1, nz(pos[1], 0)))` with `reverse = false` so `possig == pos` identically — trigger-below-DSS under the oversold rail holds short, trigger-above-DSS over the overbought rail holds long, every mid-zone or non-confirming print holds the prior state. There is no other mode switch anywhere in this source — direction inversion would be a different, unpinned rule.
- Entry long: `strategy.entry("Long", strategy.long)` under `if (possig == 1)` — fires on any completed bar whose trigger prints above DSS over `80`, with same-bar-close execution under the derived declaration. Refires while already long are no-ops under default no-pyramiding semantics.
- Entry short: `strategy.entry("Short", strategy.short)` under `if (possig == -1)` — fires on any completed bar whose trigger prints below DSS under `20`, with same-bar-close execution under the derived declaration. From flat it opens short; from long it reverses to short in full (the sole exit path — coded, not invented).
- Direction: two-sided with an explicit pre-seed flat state (the latch seeds from `0` via `nz(pos[1], 0)` and `0` fires neither leg; before the first zone conjunction, no order can fire). After seeding the system is always in market (long or short) — there is no coded flat state beyond the seed, disclosed, not enabled.
- Display isolation: the two `hline(...)` setup lines, the `barcolor(...)` assignment, and both `plot(...)` calls render only and cannot change any order; order logic reads exactly the two `if` lines. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.

## Required data

- Completed `2h` bars of BTCUSDT: `close`, `high`, and `low` (only indicator inputs, via the single `stoch(close, high, low, PDS)` call). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `2h` (stanza-faithful; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction — the stanza's `basePeriod: 15m` is the FMZ replay sub-step, never read by any order-gating line, disclosed, not a second signal frame).
- Warmup: the construction stacks two `PDS = 10` stochastic lookbacks with two `EMAlen = 9` EMA seedings plus a `TriggerLen = 5` EMA — binding constraint is the stacked lookback plus recursive-EMA seeding. The adopted warmup is the first 100 completed `2h` bars flat by record rule (predeclared researcher choice — roughly five times the longest structural lookback, covers both stochastic windows plus EMA seeding plus margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's `close`/`high`/`low` enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (stanza-faithful — venue choice and symbol spelling come from the pinned stanza, never presented as a researcher invention; see Provenance).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long block before short block): `possig` takes exactly one of `1`/`-1`/`0` per bar, so at most one leg can fire on any bar — no same-bar double-fill ordering exists under either evaluation order.
- Engine path for `2h` (gate 5, stated plainly): `2h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `2h` candles (`close`/`high`/`low`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h`/`4h`/`1d` records (the `1h/4h/1d` whitelist stands removed as an independent ban, and no ban is reinstated here by another name); the source stanza itself executed this venue, symbol, and frame on `Futures_Binance`. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships no economics at all (no capital, no commission/slippage argument, no funding, no margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default no-pyramiding semantics hold — at most one open position under the fixed order IDs `Long`/`Short`; same-direction refires while already positioned are no-ops by the pinned default, the opposite entry reverses in full (the sole position-closing path), an entry while flat opens, and re-placement is allowed immediately on the next qualifying bar after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (fixed `close/high/low` price reads, `PDS 10` / `EMAlen 9` / `TriggerLen 5` / `Overbought 80` / `Oversold 20` / `reverse false` inputs, double `stoch` + double `ema` stack with trigger EMA, the zone-conjunction latch with fixed `Long`/`Short` order IDs, display-only hline/barcolor/plots), the active `strategy(...)` declaration, the `DSS Bressert (Double Smoothed Stochastic)` title, the `2h` / `Futures_Binance BTC_USDT` stanza, and the HPotter 05/04/2017 header with the William Blau lineage note. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the coded opposite-zone `strategy.entry` reversal. The absence is coded (the order block ends with the short leg and only display code follows it in evaluation order) and the header carries no risk leg anywhere; the prose's stop-loss paragraphs sit under future `优化方向/Optimization`, explicitly unbuilt.
2. Coded rule is a zone latch, not a cross system, stated plainly: no `crossover`/`crossunder` appears anywhere; a trigger/DSS cross inside the 20–80 middle band changes nothing, and equality on either rail takes the hold branch. Substituting a naked cross trigger, or un-freezing `reverse`, would each be a different, unpinned rule.
3. Code-over-prose mapping fenced: the prose assigns long to trigger-below-DSS-under-oversold and short to trigger-above-DSS-over-overbought; the executable latch codes the opposite. This record follows the code. Anyone re-reading the mirror prose without the code block could trade it backwards, disclosed here.
4. No future leakage in the stack, stated plainly: at decision bar `t`, both `stoch` calls read completed-bar ranges through `t` and every `ema` reads its own seeded prior outputs — every input is a completed historical bar. No `security()`, no `request.*`, no negative index, no `open`/`volume` read, no `barstate.islast`-gated repainting path.
5. Same-bar entry ordering fenced: `possig` is exactly one of `1`/`-1`/`0` per bar (the map's two zone branches are mutually exclusive, plus the seeded hold), so at most one of the two entry legs can fire on any bar. Deterministic under either fill convention.
6. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own guarded `if`; no third direction exists. With `reverse` frozen `false`, `possig == pos` identically — direction inversion is not a pinned option.
7. Zone-confirmed entries with a live short side, admitted plainly: unlike absolute-threshold oscillators that can peg one-sided at crypto scale, the 0–100 stochastic rails re-normalize every `PDS` window by construction, so both zones stay reachable without retuning — while a market that grinds through a zone without a trigger/DSS inversion holds the fade with no stop, and double smoothing delays both entries and reversals symmetrically. There is no confirmation filter, no stop, and no flat state after seeding — the coded posture, disclosed as the record's principal risk.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the market/frame pin is stanza-faithful, and the price reads, inputs, smoothing stack, latch map, order IDs, reversal handling, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `close/high/low` Blau stack / `10/9/5/80/20/false` inputs / zone-conjunction latch / reversal exits / two-sided / `2h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Zone relevance: replacing the `80`/`20` zone conjunctions with a naked trigger/DSS cross (same stack and entries) must not improve net expectancy; fail ⇒ the coded zone confirmation adds nothing over its cross twin.
- F2 — Double-smoothing relevance: replacing the `xDSS` stack with the single-smoothed `xPreCalc` against the same trigger construction (same zones and entries) must not improve net expectancy; fail ⇒ the second smoothing leg adds nothing over single smoothing.
- F3 — Rail-width relevance: widening the rails to `90`/`10` (same stack, latch, and entries) must not improve net expectancy; fail ⇒ the coded `80`/`20` geometry adds nothing over its wider twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `2h` under the house overlay (stanza-faithful; the source stanza already names this venue, symbol, and frame). The `stoch`/`ema` arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `2h` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no post-seed flat: adverse excursion after placement has no guardrail beyond the opposite-zone reversal; a position whose trigger never prints the opposite zone conjunction is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Lag and mid-zone blindness: the double stochastic-plus-EMA stack delays zone entries symmetrically, and the latch ignores the entire 20–80 middle band — a full round trip inside the band is ridden flat, while a hard trend through a zone without inversion is faded. The latch-plus-reversal construction is the coded design, disclosed, not smoothed.
- Recursion seed: the stacked `stoch` windows plus `ema` seedings dominate early bars; the first 100 `2h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Prose-inversion quirk: the FMZ mirror's theory prose assigns the long/short sides opposite to the executable latch — code governs (frozen as coded); anyone re-reading the mirror prose without the code block could invert the sides, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/strategy/441102 (primary source — FMZ strategy page, publisher ChaoZhang, HPotter-authored Pine block, stanza `2024-01-05→2024-02-04`, `2h`, `Futures_Binance BTC_USDT`; fetched live 2026-10-12)
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%8F%8C%E5%B9%B3%E6%BB%91%E9%9A%8F%E6%9C%BA%E6%8C%87%E6%95%B0%E5%B8%83%E9%9B%B7%E7%91%9F%E7%AD%96%E7%95%A5Dual-Smoothed-Stochastic-Bressert-Strategy.md (byte-pinned mirror — blob `b29e72948d39f91823ef3f962ef3d4a0a847070e`, 7,196 bytes, verified against the GitHub contents API at the pinned ref during this cycle)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
