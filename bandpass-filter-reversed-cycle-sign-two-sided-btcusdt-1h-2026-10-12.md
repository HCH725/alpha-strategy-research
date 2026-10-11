---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Bandpass-filter cycle-sign reversal two-sided on BTCUSDT 1h bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2016-11-24
sources:
  - https://www.fmz.com/strategy/439878
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E4%B8%80%E7%A7%8D%E5%9F%BA%E4%BA%8E%E5%B8%A6%E9%80%9A%E6%BB%A4%E6%B3%A2%E5%8F%8D%E8%BD%AC%E7%AD%96%E7%95%A5Bandpass-Filter-Reversed-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bandpass-filter cycle-sign reversal two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (canonical FMZ strategy page fetched live over HTTPS plus the byte-pinned GitHub mirror file, verified 2026-10-12):

- Canonical page: https://www.fmz.com/strategy/439878 (title `一种基于带通滤波反转策略Bandpass-Filter-Reversed-Strategy`, FMZ publisher `ChaoZhang`, page fetched live at 751,469 bytes: `Bandpass Filter`×16, page id `439878`×20, `HPotter`×2, backtest-stanza `period: 1h`×2, `Futures_Binance`×2, `Mar 2010`×1, `strategy.entry`×2 — page identity confirmed, zero performance numbers anywhere on the page).
- Byte-pinned mirror: `一种基于带通滤波反转策略Bandpass-Filter-Reversed-Strategy.md` in `fmzquant/strategies` at repo HEAD `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified via `git ls-remote` during this cycle — the same pin as the prior ten-plus PASS admissions). Local `git hash-object` of the fetched mirror file reproduces blob SHA `c36f6026deb5cc988f51f26aeacbcf27ecfb0538` with 9,266 bytes, exactly matching the GitHub contents API (`sha`, `size`) at the pinned ref — byte-level provenance, no paraphrase.
- Code header (source-verbatim): `Copyright by HPotter v1.0 24/11/2016` — adopted as `source_as_of` 2016-11-24. The FMZ `Author: ChaoZhang` line is the FMZ publisher/uploader credit; the executable Pine block is HPotter-authored (both credits disclosed, never conflated). Theory header cites the related article as copyrighted material from `Stocks & Commodities Mar 2010` (Ehlers bandpass-filter lineage, source-reported; this record claims no article content beyond that citation line).
- Executable spec (source-verbatim, stanza first): `start: 2024-01-16 00:00:00 / end: 2024-01-23 00:00:00 / period: 1h / basePeriod: 15m / exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` followed by the full `//@version=2` block: `strategy(title="Bandpass Filter Reversed Strategy")`, inputs `Length = input(20, minval=1)`, `Delta = input(0.5)`, `TriggerLevel = input(0)`, fixed `xPrice = hl2`, `hline(TriggerLevel, ...)`, the `beta`/`gamma`/`alpha` coefficient lines, the `BP` recursion line, the `pos` latch, both `strategy.entry` legs, the `barcolor(...)` assignment, and `plot(BP, color=red, title="Bandpass Filter Strategy")`. Every line that can open, close, or size a position was read verbatim from the pinned mirror.
- Text census over the pinned code block: 1 `strategy(` (title only — no `process_orders_on_close`, no `pyramiding`, no commission/slippage/capital argument) / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, no price/qty argument) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `stop=`/`limit=` / 0 `crossover`/`crossunder` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `var` / 3 `nz(` (`BP[1]`, `BP[2]` recursion seeds, `pos[1]` latch seed) / 0 `volume` / 0 `open` / 0 `close` (the rule reads `high`/`low` only, via `hl2`; neither `open`, `close`, nor `volume` appears in any order-gating line) / exactly 3 `input(` (`Length 20`, `Delta 0.5`, `TriggerLevel 0` — all strategy inputs, no date-window, no mode switch, no webhook string).
- Args-table discrepancy, fenced: the FMZ mirror's `Strategy Arguments` table lists `v_input_3|false|TriggerLevel`, but the Pine block declares `TriggerLevel = input(0)`. The code is authoritative — this record freezes `TriggerLevel = 0` per code and treats the table's `false` as a publisher-side rendering quirk (same class of quirk as prior screened files, disclosed, never silently adopted).
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the prose's stop-loss paragraphs sit under `优化方向` (future optimization directions, explicitly not built) — the no-stop/no-target posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number — the advantage/risk prose is purely qualitative) — this record claims no source-reported performance and no reproduced performance. The stanza names the market and frame outright (`Futures_Binance BTC_USDT`, `1h`) — the `BTCUSDT 1h` pin below is source-faithful, not a researcher derivation.

Licence and rights: the pinned code block carries `// Copyright by HPotter v1.0 24/11/2016` with a paper-trading-only warning. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source ships no execution-timing argument — Pine default fills evaluate per completed bar and fill on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 100-bar warmup with pre-warmup bars flat by record rule (five times the `Length = 20` center cycle — covers the `BP[1]`/`BP[2]` recursion seed plus one full passband cycle plus margin; see Required data); (3) house sizing/capital/costs replacing the absent source economics (the source ships no commission/slippage/capital/funding/margin assumption at all — see Execution assumptions). The `1h` frame, the Binance-futures BTCUSDT venue, the `hl2` price, the `20/0.5/0` inputs, the `beta`/`gamma`/`alpha` arithmetic, the `BP` recursion, the reversed sign-state map, the `Long`/`Short` order IDs, the reversal-only exits, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-12): working-tree case-insensitive search for `bandpass`, `TriggerLevel`, `Center Of Gravity`, `xLG1r`, `MESA`, `cyber-cycle`, `Butterworth`, and `detrended synthetic` returns only two Ehlers-adjacent records — `laguerre-rsi` (Ehlers Laguerre gamma-filter `L0`–`L3` recursion feeding a `cu`/`cd` RSI with a crossover order pair and a date-window gate) and `fisher-zero-cross` (Ehlers Fisher-Transform nonlinear normalization with a zero-cross) — both different formulas, different triggers, different orders, different sources (five-axis distinction in Signal and Negative evidence). The `linreg` hits (`chop-zone` display-only block gating no order; `sqzmom` linreg-of-detrended-price momentum as one leg of a three-part combo) are not collisions — this rule uses no `linreg` anywhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs contain no bandpass record. No pool record computes an Ehlers cosine-derived resonator, and no pool record trades a bandpass-cycle sign state.

## Economic mechanism

### Source-reported

Passband-cycle reversal (code header plus bilingual theory prose, no performance section ships): a first-order IIR bandpass resonator centered on a 20-bar cycle (`Length = 20`) with bandwidth parameter `Delta = 0.5` strips high- and low-frequency noise and keeps only the medium-frequency cycle component `BP`. When the filter output prints above the zero trigger the cycle is deemed stretched upward and the system holds short; when it prints at or below zero the system holds long — the mapping is deliberately reversed (hence the strategy name): the rule fades the contemporaneous cycle polarity rather than riding it. There is deliberately no stop, no target, and no flat state after seeding — the header admits paper-trading-only status with no risk leg anywhere, by design gap rather than by hidden leg.

### Research interpretation

Zero-trigger cycle-sign state machine, two-sided with reversal exits and an explicit pre-seed flat state. Unlike cross systems that trade the moment one line passes another, this rule never trades a cross at all: its only comparison is filter-output-versus-constant (`0`), and the `pos` latch makes every non-qualifying print a hold. Unlike always-in-market flip systems, the rule rests flat while `BP` is `na` (the first two bars, where `xPrice[2]` is unseeded, fail both strict comparisons and hold the `0` seed, which fires neither leg). Note the two pinned asymmetries, stated plainly: first, the mapping is reversed — `BP > 0` holds short and `BP <= 0` holds long, so the system leans against the measured cycle phase; second, the latch's hold branch is unreachable for real prints (`BP > 0` and `BP <= 0` cover the whole real line, equality taking the long branch), so latch memory only ever bridges `na` bars — for all numbered bars the rule is a pure sign map, disclosed, not a memory system. The price of the construction is cycle-chop: a filter output flickering across zero prints full long/short reversals at the worst prints of each flicker, and a trending market whose 20-bar cycle component stays signed keeps the system faded against the trend with no stop beyond the opposite-sign reversal. The bet is on medium-frequency cycle reversion at a frozen 20-bar center, not on any trend level, volume print, mean-reversion extreme, or calendar effect.

## Signal

Exact rule as pinned (`Length 20`, `Delta 0.5`, `TriggerLevel 0`, `hl2` price, reversed mapping frozen — any other value is a different, unpinned rule):

- Declaration (source-faithful): `strategy(title="Bandpass Filter Reversed Strategy")` semantics preserved with the stanza-native `BTCUSDT 1h` market/frame pin and same-bar-close execution adopted (no such timing argument ships in the source) and house sizing/costs replacing the absent source economics (see Execution assumptions). Pine-default no-pyramiding semantics hold (no `pyramiding` argument ships): at most one open position, same-direction refires are no-ops, opposite entries reverse in full.
- Coefficients (pinned arithmetic — evaluated from the frozen inputs, not tuned): `beta = cos(3.14 * (360 / 20) / 180) ≈ 0.951106`; `gamma = 1 / cos(3.14 * (720 * 0.5 / 20) / 180) ≈ 1.051408`; `alpha = gamma - sqrt(gamma * gamma - 1) ≈ 0.726664`. Constants, recomputed here to six decimals from the pinned formula for audit convenience — the formula, not these decimals, is the pinned truth.
- Filter (pinned): `xPrice = hl2`; `BP = 0.5 * (1 - alpha) * (xPrice - xPrice[2]) + beta * (1 + alpha) * nz(BP[1]) - alpha * nz(BP[2])` — a causal first-order IIR resonator: at decision bar `t` it reads only `hl2` through `t` and its own prior outputs. No zero-guard ships in the source and none is needed (no division anywhere in the order path).
- State map (pinned, reversed): `pos = iff(BP > TriggerLevel, -1, iff(BP <= TriggerLevel, 1, nz(pos[1], 0)))` with `TriggerLevel = 0` — strictly positive prints hold short, zero-or-negative prints hold long, `na` holds the prior state. There is no `reverse` switch anywhere in this source (unlike other HPotter backtests) — direction inversion would be a different, unpinned rule.
- Entry long: `strategy.entry("Long", strategy.long)` under `if (pos == 1)` — fires on any completed bar whose filter prints at or below zero, with same-bar-close execution under the derived declaration. Refires while already long are no-ops under default no-pyramiding semantics.
- Entry short: `strategy.entry("Short", strategy.short)` under `if (pos == -1)` — fires on any completed bar whose filter prints above zero, with same-bar-close execution under the derived declaration. From flat it opens short; from long it reverses to short in full (the sole exit path — coded, not invented).
- Direction: two-sided with an explicit pre-seed flat state (the latch seeds from `0` via `nz(pos[1], 0)` and `0` fires neither leg; before `BP` first prints a number, no order can fire). After seeding the system is always in market (long or short) — there is no coded flat state beyond the seed, disclosed, not enabled.
- Display isolation: the `hline(TriggerLevel, ...)` setup line, the `barcolor(...)` assignment, and `plot(BP, ...)` render only and cannot change any order; order logic reads exactly the two `if` lines. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.

## Required data

- Completed `1h` bars of BTCUSDT: `high` and `low` (only indicator inputs, via `hl2`). No `open`, no `close`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (stanza-faithful; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction — the stanza's `basePeriod: 15m` is the FMZ replay sub-step, never read by any order-gating line, disclosed, not a second signal frame).
- Warmup: the `BP` recursion references `xPrice[2]`, `BP[1]`, and `BP[2]`, and the resonator is centered on a 20-bar cycle — binding constraint is a seeded recursion plus one full passband cycle. The adopted warmup is the first 100 completed `1h` bars flat by record rule (predeclared researcher choice — five times `Length`, covers seed plus a full center cycle plus margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's `hl2` enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (stanza-faithful — venue choice and symbol spelling come from the pinned stanza, never presented as a researcher invention; see Provenance).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry legs are evaluated in source order (long block before short block): `pos` takes exactly one of `1`/`-1`/`0` per bar, so at most one leg can fire on any bar — no same-bar double-fill ordering exists under either evaluation order.
- Sizing/capital/costs: the source ships no economics at all (no capital, no commission/slippage argument, no funding, no margin assumption — quoted verbatim in census; the absence is disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: Pine-default no-pyramiding semantics hold — at most one open position under the fixed order IDs `Long`/`Short`; same-direction refires while already positioned are no-ops by the pinned default, the opposite entry reverses in full (the sole position-closing path), an entry while flat opens, and re-placement is allowed immediately on the next qualifying bar after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (fixed `hl2` price, `Length 20` / `Delta 0.5` / `TriggerLevel 0` inputs, cosine-derived `beta`/`gamma`/`alpha`, the `BP` IIR recursion, the reversed sign-state map with fixed `Long`/`Short` order IDs, display-only hline/barcolor/plot), the active `strategy(...)` declaration, the `Bandpass Filter Reversed Strategy` title, the `1h` / `Futures_Binance BTC_USDT` stanza, and the HPotter 24/11/2016 header with the Stocks & Commodities Mar 2010 lineage note. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=` — the sole position-closing path is the coded opposite-state `strategy.entry` reversal. The absence is coded (the order block ends with the short leg and only display code follows it in evaluation order) and the header carries no risk leg anywhere; the prose's stop-loss paragraphs sit under future `优化方向`, explicitly unbuilt.
2. Coded rule is a pure reversed sign map, not a memory latch, stated plainly: `BP > 0` and `BP <= 0` cover the whole real line (equality takes the long branch), so the `nz(pos[1], 0)` hold fires only on `na` prints. Substituting a symmetric ±band with genuine hold memory, or un-reversing the mapping, would each be a different, unpinned rule.
3. No future leakage in the resonator, stated plainly: at decision bar `t`, `BP` reads `hl2` through `t` (including the two-bar difference `xPrice - xPrice[2]`) and its own seeded prior outputs — every input is a completed historical bar. No `security()`, no `request.*`, no negative index, no `open`/`close`/`volume` read, no `barstate.islast`-gated repainting path.
4. Same-bar entry ordering fenced: `pos` is exactly one of `1`/`-1`/`0` per bar (the map's two real-line branches are mutually exclusive, plus the `na`-hold), so at most one of the two entry legs can fire on any bar. Deterministic under either fill convention.
5. Two-sided posture provably complete: both `strategy.long` and `strategy.short` appear exactly once each, each under its own guarded `if`; no third direction exists. There is no `reverse` input anywhere — direction inversion is not a pinned option.
6. Zero-mean trigger with a live short side, admitted plainly: unlike absolute-threshold oscillators that can peg one-sided at crypto scale, the `0` trigger sits at the resonator's natural center (the difference-driven IIR output oscillates around zero by construction), so both states are reachable without retuning — while an index flickering across zero prints full long/short reversals at the worst prints of each flicker, and a sustained cycle-signed stretch holds the fade against the trend. There is no confirmation filter, no stop, and no flat state after seeding — the coded posture, disclosed as the record's principal risk.
7. The `hl2`-only input, the `20/0.5/0` inputs, the cosine-derived coefficients, the `BP` recursion, the strict reversed inequalities, the fixed `Long`/`Short` order IDs, the reversal-only exits, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any input, converting the sign map into a cross, adding a stop/target/filter/cooldown, swapping `hl2` for another price, or deploying on another market or frame would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the market/frame pin is stanza-faithful, and the coefficients, recursion, state map, order IDs, reversal handling, and risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `hl2`-only Ehlers resonator / `20/0.5/0` inputs / reversed zero-trigger sign map / reversal exits / two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Direction relevance: un-reversing the side mapping (`BP > 0` long, `BP <= 0` short, same recursion and entries) must not improve net expectancy; fail ⇒ the coded reversal adds nothing over its trend-following mirror.
- F2 — Resonator relevance: replacing the `BP` recursion with a same-length simple moving average of `hl2` (same zero-trigger sign map and entries) must not improve net expectancy; fail ⇒ the coded bandpass construction adds nothing over plain smoothing.
- F3 — Cycle-length relevance: replacing the `Length = 20` center cycle with `Length = 40` (same `Delta`, trigger, and map) must not improve net expectancy; fail ⇒ the coded 20-bar passband adds nothing over its octave twin.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (stanza-faithful; the source stanza already names this venue, symbol, and frame). The `hl2` arithmetic ports across perpetual venues without structural change; the rule reads no volume, so venue volume-definition differences cannot touch it. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal-to-flat/short mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1h` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: beyond Pine defaults the source ships no capital, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop, no post-seed flat: adverse excursion after placement has no guardrail beyond the opposite-sign reversal; a position whose filter never prints on the opposite side of zero is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Chop sensitivity: zero-line flicker prints full reversals in trendless markets, and sustained cycle-signed stretches hold the fade against the trend (the reversed mapping leans into mean reversion by design). The sign-map-plus-reversal construction is the coded design, disclosed, not smoothed.
- Recursion seed: the `BP[1]`/`BP[2]` seed transient plus one full 20-bar center cycle dominate early bars; the first 100 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Args-table quirk: the FMZ mirror's arguments table renders `TriggerLevel` default as `false` against the code's `input(0)` — code governs (frozen `0`); anyone re-reading the mirror table without the code block could mis-set the trigger, disclosed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://www.fmz.com/strategy/439878 (primary source — FMZ strategy page, publisher ChaoZhang, HPotter-authored Pine block, stanza `2024-01-16→2024-01-23`, `1h`, `Futures_Binance BTC_USDT`; fetched live 2026-10-12)
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E4%B8%80%E7%A7%8D%E5%9F%BA%E4%BA%8E%E5%B8%A6%E9%80%9A%E6%BB%A4%E6%B3%A2%E5%8F%8D%E8%BD%AC%E7%AD%96%E7%95%A5Bandpass-Filter-Reversed-Strategy.md (byte-pinned mirror — blob `c36f6026deb5cc988f51f26aeacbcf27ecfb0538`, 9,266 bytes, verified against the GitHub contents API at the pinned ref during this cycle)
- https://www.tradingview.com/pine-script-reference/v5/ (Pine semantics reference for census terms — defaults only, never a source of strategy facts)
