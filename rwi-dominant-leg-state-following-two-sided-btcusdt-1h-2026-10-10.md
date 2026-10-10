---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: RWI dominant-leg state-following two-sided on BTCUSDT 1h bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-01
sources:
  - https://www.fmz.com/strategy/440724
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/RWI波动率反转策略RWI-Volatility-Contrarian-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RWI dominant-leg state-following two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (canonical FMZ page, fetched 2026-10-10):

- Canonical page: https://www.fmz.com/strategy/440724 (page title `RWI波动率反转策略|RWI Volatility Contrarian Strategy`, public `Common strategy`, `Created: 2024-02-01 14:56:58` — adopted as `source_as_of` 2024-02-01). Fetched over HTTPS during this cycle (744301 bytes): the page embeds the full Pine block byte-verbatim — `strategy("RWI Strategy", overlay=false)`, `length = input(title="Length", type=input.integer, defval=14, minval=1)`, `threshold = input(title="Threshold", type=input.float, defval=1.0, step=0.1)`, the `rwi(length, threshold) =>` function (`rwi_high = (high - nz(low[length])) / (atr(length) * sqrt(length))`, `rwi_low = (nz(high[length]) - low) / (atr(length) * sqrt(length))`, `is_rw = rwi_high < threshold and rwi_low < threshold`), the state pair `long = not is_rw and rwi_high > rwi_low` / `short = not is_rw and rwi_low > rwi_high`, the live order pair `strategy.entry("Long", strategy.long, when=long)` / `strategy.entry("Short", strategy.short, when=short)`, and the page-embedded `/*backtest*/` header (`start: 2024-01-01 00:00:00`, `end: 2024-01-31 23:59:59`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Net Profit` 0, `Win Rate` 0, `Max Drawdown` 0, `Profit Factor` 0, `Annual(ized)` 0 — the page ships no quantitative performance numbers of any kind (adopted as no claimed performance anywhere in this record; the prose's qualitative `胜率较高` / `high winning rate` language is marketing text with no table, figure, or number and is never treated as evidence).
- Text census over the embedded code block: 2 `strategy.entry` (the Long/Short pair quoted above, no `qty` argument on either) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `request.security` (single-frame by construction) / 0 `volume` reads / 0 `time(` gates (no date-window convenience inputs anywhere — unlike sibling FMZ publications, this strategy has no backtest-window filter to remove) / 2 `input(` declarations (`Length` 14, `Threshold` 1.0 — both pinned at defaults; any other value is a different, unpinned rule) / `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, commission and slippage appear nowhere (Pine v4 language defaults govern: see Signal). The `input.*` / `color.*` namespaces and `strategy.long` / `strategy.short` constants pin Pine v4 semantics (`//@version=4` ships in the block). The `plot(rwi_high)` / `plot(rwi_low)` legs and the `color=is_rw?color.gray:...` ternaries render only and gate no order.
- GitHub mirror corroboration (verbatim-identical Pine block): `fmzquant/strategies` file `RWI波动率反转策略RWI-Volatility-Contrarian-Strategy.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (2025-04-30), whose `Detail` field points back to `https://www.fmz.com/strategy/440724` and whose `Last Modified` reads 2024-02-01. Code copyright header `// Copyright (c) 2020-present, JMOZ (1337.ltd)` ships in the block; no licence grant beyond the visible publication is claimed.
- No `©` republication beyond single-line declarations quoted for gate evidence; this record cites and normalizes the rule and reproduces no source block beyond the short declarations above.

Licence and rights: the canonical page is a public FMZ strategy publication and the mirror is a public GitHub implementation file. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) same-bar-close fills (the source sets no execution-timing argument anywhere, so source fills are next-tick by language default); (2) position-state pin — single-unit per side, repeat-state-while-positioned as no-op, full reversal on the opposite state, ranging-hold (the source `strategy(...)` header carries no `pyramiding` argument, so Pine v4 default `pyramiding=0` — no same-direction adds — already governs the live code; the pin restates it as record rule, predeclared); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers `high[14]`/`low[14]` lookback plus RMA-based `atr(14)` seeding margin — see Required data); (4) house sizing/capital/costs replacing the source economics (live code passes no `qty`: Pine v4 default is one fixed unit; no commission, fee, slippage, margin, or funding assumption ships anywhere — see Execution assumptions); (5) venue naming normalization only (`BTC_USDT` → `BTCUSDT`). There is deliberately NO timeframe adaptation (source header `period: 1h`; derived frame `1h`), NO formula or length/threshold change, and NO date-window removal (the code ships no `time(` gate). The RWI arithmetic (14/1.0), the ranging-state gate, the dominant-leg state predicates, and the Long/Short order pair are source-verbatim.

**Code-over-prose pin (material, predeclared):** the page prose claims the high-leg-dominant regime means reversal-short (`RWI高点大于RWI低点超过阈值…可以考虑做空`) and the low-leg-dominant regime means reversal-long — the executable code does the exact opposite (`long = not is_rw and rwi_high > rwi_low`, i.e. it follows the dominant leg). The derived spec follows the executable code and excludes the prose direction from all order logic. A genuinely contrarian (fade-the-dominant-leg) variant would be a different, unpinned rule — none is admitted here. The `Contrarian` in the publication title is therefore never evidence of fade behavior.

Pre-write dedup (2026-10-10): working-tree case-insensitive word-boundary searches for `\brwi\b` and `laguerre` return zero hits anywhere — no admitted rule uses this source, author publication, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` breaks raw N-bar highest/lowest extremes with no volatility normalization and no ranging-state gate; `nr7-price-breakout-long-btcusdt-1d-2026-10-10.md` is a narrowest-range contraction breakout, long-only, with no ATR-normalized dual-leg state machine; oscillator-cross records (`kst`, `fisher`, `qqe`, `tsi`, `qstick`) cross a smoothed oscillator against a signal line or zero level rather than comparing two ATR-normalized displacement legs under a sub-threshold ranging hold. Four-axis distinction: signal construction differs (dual-leg `(high − low[14]) / (atr(14)·√14)` displacement pair versus extremes, ranges, or single-oscillator crosses — no pool record evaluates an RWI pair), trigger differs (dominant-leg state with ranging hold versus edge-cross or extreme-break), exits differ in event set (reversal-only via the opposite dominant-leg state with a flat-capable ranging hold versus stop/target or cross exits), and source identity differs (FMZ 440724 February-2024 versus other FMZ IDs or TV authors).

## Economic mechanism

### Source-reported

Random-Walk-Index displacement: each leg measures how far price has travelled from the opposite extreme N bars ago, normalized by N-period ATR scaled by √N — the distance a pure random walk would be expected to cover. When both legs sit below 1.0 the market is not displacing beyond random-walk expectation (ranging — no action). When either leg reaches 1.0+, price is displacing directionally; the executable code holds the side of the dominant leg until the other leg takes over.

### Research interpretation

State-following (not edge-triggered) two-sided system with no price stop, target, trailing, or time exit — always positioned after the first non-ranging bar, flipping only when the dominant leg changes hands, holding through ranging regimes. Unlike edge-cross systems (TSI, KST, Fisher) that trade only crossing bars, this system re-asserts the dominant-leg state every bar: a fresh ranging→trending transition enters immediately, while chop that keeps both legs sub-threshold costs nothing (flat-capable hold — the record's distinctive guardrail). Unlike raw extreme-break systems (Donchian) there is an explicit volatility-normalized ranging gate — a dead market cannot force entries. Unlike the prose title's `contrarian` suggestion, the coded bet is dominant-leg persistence at the 1h frame on BTCUSDT's own displacement, never a fade, a level, a breakout distance, a squeeze, a calendar, or a mean-reversion anchor.

## Signal

Exact rule as pinned (14/1.0 frozen — any other length or threshold is a different, unpinned rule):

- Declaration (derived): Pine v4 semantics (`//@version=4` ships in the block; `atr()` is the RMA-smoothed true-range builtin, `sqrt` the v4 global, `nz(x)` yields 0.0 on leading `na`). The `strategy(...)` header carries no `pyramiding`, `process_orders_on_close`, or `calc_on_every_tick` argument — v4 defaults govern (`pyramiding=0`: no same-direction adds; `calc_on_every_tick` false: exactly one evaluation per completed bar). No `qty` ships on either entry — v4 default one fixed unit, replaced by the house overlay in derived evaluation (see Execution assumptions, predeclared).
- Indicator arithmetic (pinned, source-verbatim, single-TF): `rwi_high = (high - nz(low[14])) / (atr(14) * sqrt(14))`; `rwi_low = (nz(high[14]) - low) / (atr(14) * sqrt(14))`; `is_rw = rwi_high < 1.0 and rwi_low < 1.0` — all on BTCUSDT `1h` bars (source header `period: 1h`; no `request.*` call anywhere).
- Entry long: `long = not is_rw and rwi_high > rwi_low` → `strategy.entry("Long", strategy.long)` — true on every bar the high leg dominates outside the ranging state; same-bar-close execution under the derived declaration. While already long, a persisting `long` state is a no-op by record rule (predeclared pin over the v4 no-pyramiding default).
- Entry short / reversal: `short = not is_rw and rwi_low > rwi_high` → `strategy.entry("Short", strategy.short)` — true on every bar the low leg dominates outside the ranging state; while long it closes the full long and opens the full short in the same execution step (full reversal, no residual leg); while already short, a persisting `short` state is a no-op by record rule. While `is_rw` (both legs sub-threshold) the system holds whatever it has — including staying flat before the first signal (no position by construction).
- `long`/`short` are mutually exclusive on every bar by construction (strict opposing inequalities on the same two values), so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record. The measure-zero edge `rwi_high == rwi_low` fires neither leg (both strict predicates fail) and the position simply holds — stated, not patched. A `0 / 0`-style divide (fourteen zero-range bars driving `atr(14)` to exactly zero) yields `na`, which fires neither state — pinned as hold under Pine `na`-comparison semantics, never patched with a guard constant. Leading-bar `nz(low[14])`/`nz(high[14])` zeros fall inside the adopted warmup flat (see Required data).
- Risk legs (pinned absence, not invented): 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit; the prose's stop-loss suggestions (`配置止损策略` listed under future optimizations) are wishes, never rules, and none is adopted here.
- Direction: two-sided long/short with symmetric state reversal. Futures venue required for the short leg (source venue is already `Futures_Binance BTC_USDT` — pinned).
- Display isolation: both `plot(...)` legs (including the `is_rw?...:...` color ternaries) render only and cannot change any order.

## Required data

- Completed `1h` bars of BTCUSDT: `high` and `low` only (sole series read by the RWI pair; `close` is read nowhere in any order-gating line — the `lot`-style equity sizing fragments seen in sibling publications ship nowhere here). No `open`, no `close`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` calls).
- Single decision timeframe `1h` (source chart header `period: 1h`; `basePeriod: 15m` equals native 15m execution granularity — 4 quarter-hour bars per 1h bar on a 24/7 venue — and with state-entry reversal legs only plus zero intrabar-conditional legs, no intrabar path exists for the base to affect; pinned as irrelevant, not modeled).
- Warmup: `high[14]`/`low[14]` need 14 bars and the RMA-based `atr(14)` needs seeding history. The adopted warmup is the first 60 completed `1h` bars flat by record rule (predeclared researcher choice — covers 14-bar lookback plus RMA seeding margin); no state before bar 61 may trade. No repainting (`high`/`low`/`atr` read only completed bars), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (source venue is already `Futures_Binance BTC_USDT` on the source `1h` chart frame — naming normalization to `BTCUSDT` is the only market change; formula, lengths, threshold, and frame are verbatim, never presented as anything but the coded rule).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-tick (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive state legs and no stop/target legs, there is no same-bar ordering ambiguity of any kind. `1h` is a supported pinned-engine interval (current campaign already screens `1h`).
- Sizing/capital/costs: the source ships no live sizing argument (both entries omit `qty`; v4 default one fixed unit) and no commission, fee, slippage, margin, or funding assumption anywhere. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full/ranging-hold position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side under the fixed order IDs `Long`/`Short` (v4 `pyramiding=0` default restated as record rule, predeclared); persisting same-side states while positioned are no-ops; the opposite dominant-leg state reverses in full in one step; ranging states hold with no action; re-entry after a reversal needs only the next opposite dominant-leg state (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (v4 header, `RWI Strategy` working title, `overlay=false`, 14/1.0 inputs, `rwi()` nesting with `nz(low[14])` / `nz(high[14])` / `atr(14)` / `sqrt(14)`, `is_rw` sub-threshold gate, `long`/`short` dominant-leg state predicates, Long/Short order pair, JMOZ copyright line, the 1h/15m Jan-2024 backtest header on `Futures_Binance BTC_USDT`, bilingual RWI prose). It ships zero quantitative performance numbers: no return, no win rate figure, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order` — the sole position-changing path is the opposite dominant-leg state reversing the full unit. The absence of any live stop is coded absence, disclosed, not a tunable parameter here.
2. Always-positioned exposure outside ranging regimes, admitted plainly: after the first non-ranging bar the system holds a side until the other leg dominates — a market that trends against the entry keeps the full unit on with no guardrail beyond the dominant-leg flip, which may arrive many bars later or after deep excursion. Chop that alternates dominant legs across the threshold flips the full unit repeatedly. This is the coded trade, disclosed, not a tunable parameter here.
3. Prose/code divergence fenced: the page prose's contrarian direction (`high-dominance → consider short`) is contradicted by the executable entries (high-dominance → long). The derived spec follows the code; a genuine fade-the-dominant-leg variant would be a different, unpinned rule — none is admitted here. The publication title's `Contrarian` describes prose intent, never coded behavior.
4. Ranging-state flat admitted: while `is_rw` the system takes and holds no new action — entries only exist outside the sub-threshold gate. A market that ranges for an extended stretch leaves the system holding stale exposure (or flat, pre-first-signal) with no time exit — disclosed, not patched with a holding-period cap.
5. Non-classic RWI construction fenced: textbook RWI compares the current extreme against the highest-high/lowest-low range over the lookback; this source compares single-bar `high`/`low` against the single opposite extreme 14 bars back under an ATR normalization. The derived record reproduces the coded construction verbatim and makes no claim of equivalence to textbook RWIdyn — a highest/lowest-range variant would be a different, unpinned rule.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the restated single-unit/no-add/reverse-full/ranging-hold position pin, the adopted 60-bar warmup with record-rule pre-warmup flat, venue naming normalization, and house sizing/costs — all predeclared above; the 14/1.0 literals, the ATR-√N normalization, the `nz` seeding, the sub-threshold gate, the strict dominant-leg predicates, the Long/Short order pair, the `==`/`na` hold edges, and the no-stop/no-target/no-cooldown stance are source-verbatim. This record is therefore never evidence that any contrarian-fade, textbook-RWI, or next-tick-fill reading of the source itself passes.
7. The `14` / `1.0` literals, the strict dominant-leg definitions (not touch, not level-hold, not fade), the full-unit reversal, the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any literal, converting state-following into edge-crossing, adding a stop/target/filter/cooldown/gate, dropping the short leg, flipping to the prose's contrarian direction, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `14` / `1.0` / ATR-√N dual-leg construction / strict dominant-leg states / full-unit reversal / two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Threshold relevance: replacing the pinned `1.0` ranging gate with any adjacent classic gate must not improve net expectancy; fail ⇒ the pinned threshold carries no advantage over neighboring gates and the record's literal choice is arbitrary.
- F2 — Direction relevance: replacing the coded dominant-leg-following direction with the prose's contrarian direction (fade the dominant leg under the identical gate) must not improve net expectancy; fail ⇒ the executable direction adds nothing over its prose opposite and the code-over-prose pin is unmoored.
- F3 — Normalization relevance: replacing the ATR-√N normalization with a raw displacement comparison at the same length must not improve net expectancy; fail ⇒ the volatility normalization adds nothing over unnormalized displacement.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame source-native `1h`; no signal-series adaptation of any kind — predeclared section above lists all five derivations, none touching frame or formula). The high/low/ATR arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-tick on a 1h-decision/15m-base backtest; this record executes same-bar-close on `1h` BTCUSDT perpetual. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden.
- Position-state pin: restates the v4 `pyramiding=0` no-add default plus single-unit/no-op/reverse-full/ranging-hold as record rule; live same-side-add quantity behavior beyond the default is unspecified-by-code and the pin is a researcher choice where it goes beyond the default, disclosed, not source-verbatim.
- Prose/code divergence: the contrarian direction exists only in prose and is excluded here — a reader trusting the prose alone would reconstruct the opposite, unpinned rule.
- No price stop, no time stop, never flat outside ranging states: adverse excursion after entry has no guardrail beyond the opposite dominant-leg state, which may arrive many bars later or after deep excursion; alternating chop across the gate flips the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no live capital, commission, fee, slippage, margin, or funding assumption ships anywhere in the active code — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue naming only: the source venue is already `Futures_Binance BTC_USDT`; the derived venue is Binance `BTCUSDT` perpetual. Microstructure, tick size, fee, and funding differences are carried by the house overlay — no equivalence is claimed.
- One-month source backtest window (Jan-2024 header) is a page setting, not a strategy rule: it bounds no derived claim and this record draws no performance inference from it.

## Implementation status

Not implemented. No Hummingbot controller/executor has been written for this record; no Qlib screening, parity run, Paper, Testnet, or live deployment is authorized or claimed. Admission PASS (upon independent review) means model-consistent research admissibility under the pinned engine assumptions above — nothing more.

## Adoption boundary

- `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is not authorization to trade, allocate capital, or deploy to any live, paper, or test venue.
- Downstream eligibility (Qlib screening after event-level parity, Hummingbot re-validation, survivor promotion) is governed solely by the repository's downstream contract and is never implied by this record alone.
- Any parameter, frame, market, direction, fill-timing, or risk change versus the pinned rule above constitutes a different, unpinned strategy requiring its own record and review.

## Related Wiki records

None. No Wiki Brain ingestion was performed for this record (Scout PR-only workflow performs no intake review or wiki writes).

## Sources

- https://www.fmz.com/strategy/440724 — canonical FMZ strategy publication (`RWI波动率反转策略|RWI Volatility Contrarian Strategy`, Created 2024-02-01 14:56:58; full Pine v4 block read byte-verbatim from the page fetched 2026-10-10; page-embedded backtest header `period: 1h`, `basePeriod: 15m`, `Futures_Binance BTC_USDT`, Jan-2024 window).
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/RWI波动率反转策略RWI-Volatility-Contrarian-Strategy.md — public GitHub mirror carrying the verbatim-identical Pine block (code © JMOZ 1337.ltd), `Detail` link back to FMZ 440724.
- https://www.tradingview.com/pine-script-reference/v5/ — Pine builtin semantics reference (v4-era `atr`/`nz`/`strategy.entry` behavior as observed in the source block).
