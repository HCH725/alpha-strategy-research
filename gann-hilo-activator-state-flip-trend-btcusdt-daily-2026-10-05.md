---
schema: strategy-research-record-v1
title: Gann HiLo Activator state-flip trend system on BTCUSDT daily bars
created: 2026-10-05
updated: 2026-10-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-30
sources:
  - https://github.com/fmzquant/strategies
  - https://www.fmz.com/strategy/427070
  - https://www.tradingview.com/pine-script-docs/language/declaration-statements/
  - https://www.tradingview.com/pine-script-docs/concepts/time/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Strategy prose states the effective start time defaults to the full period, but the pinned code defaults Begin from start? to false and therefore gates every order on time >= timestamp(2017, 1, 1, 00, 00), so the default excludes all bars before 2017-01-01."
  - "Strategy prose states the upper and lower bands are weighted moving averages of highest and lowest prices, but the pinned code computes ta.sma(high, 3) and ta.sma(low, 3), which are simple arithmetic means."
  - "Strategy prose Risk item 2 asserts improper parameters may cause frequent stop loss and re-entries, but the pinned code contains no stop loss, take profit, trailing or time exit of any kind, while the Optimization item simultaneously proposes adding a trailing stop loss as future work."
  - "The artifact Strategy Arguments table prints Offset, From Month and From Day defaults as true, but the pinned code declares all three with input.int(1, ...), so the table and the code disagree on three parameter defaults."
---

# Gann HiLo Activator state-flip trend system on BTCUSDT daily bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; this is the repository head at research time).
- Exact file path: `干浪激活器策略Gann-HiLo-Activator-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%B9%B2%E6%B5%AA%E6%BF%80%E6%B4%BB%E5%99%A8%E7%AD%96%E7%95%A5Gann-HiLo-Activator-Strategy.md )
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/427070

Primary-source checksums pinned 2026-10-05 from a shallow clone of that single commit:

- File 5070 bytes, SHA-256 `bc3f451e4699b2d0b61392febdf5a5665fea1d5cd7834a8fb35c24202c27e54e`, 4199 characters, 195 lines.
- Whitespace-collapsed variant 4100 characters, SHA-256 `ebfc20c8929912355a55df9f7bc3299817dac241a6000b5fa4f81fce1d6d57de`.
- The fenced Pine block alone: 43 lines, 1439 characters, SHA-256 `2aa373e8163c7ce0a2bf6f38311b71ff74120721eefe78b8e81dde37267e645d`.

Artifact structure as printed: `> Name` (Gann HiLo Activator Strategy, with the mirrored Chinese title rendered as 干浪激活器策略), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English set inside one `[trans]` block), `> Strategy Arguments` table, `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/427070, `> Last Modified` = 2023-09-17 18:36:01.

Licence and rights: the pinned Pine block itself prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the original author credit `// © starbolt`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page read directly in a browser session on 2026-10-05 (public, no login required for the description layer): browser title `🐴 Gann HiLo Activator Strategy | FMZ`, heading `Gann HiLo Activator Strategy`, author account `ChaoZhang`, `Created: 2023-09-17 18:36:01`, `Last modified: 3 years ago`, `Copy: 0`, `Hits: 1226`, the English Overview / Strategy Logic / Advantages / Risks / Optimization / Summary prose identical to the mirror's English block, the same `/*backtest*/` header printed in the open, the six Strategy parameters listed (Length, Offset, Begin from start?, From Year, From Month, From Day), and the Pine body truncated right after the Pine version-5 declaration comment, behind the literal string `Login to view full source`. Consequence: the complete source is publicly reachable only through the GitHub mirror at the pinned SHA, and the landing shows no performance table, no equity curve and no trade list.

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2022-09-10 00:00:00
end: 2023-09-16 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source.

Pre-write dedup (2026-10-05): a hidden-inclusive search of the whole working tree excluding `.git` for `fmzquant/strategies`, `fmz.com/strategy/427070`, `Gann HiLo`, `HiLo Activator` returned 0 matches, and the loose probe `gann` also returned 0 matches. `git ls-remote --heads origin 'research/*'` returned no refs, so there is no open `research/*` branch. `origin/main` was at `50cbaed` and contains 0 strategy records after the 2026-10-04 pool reset, so the dedup set of current `main` records plus open research PRs is empty. One mechanism-adjacent record, `gann-angle-support-resistance-es-intraday-ssrn-6918818-2026-09-29.md`, existed in repository history and was deleted by reset commit `2799e34`; it is a different source (SSRN 6918818), a different mechanism (session-anchored Gann fan angle support/resistance event study), a different signal construction (1-ATR proximity events on 1-minute ES bars) and a different market, so it is not a duplicate. Five-axis distinction against it: mechanism, signal construction, universe, horizon and material data dependency all differ.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview: "Strategy based on the Gann HiLo Activator indicator for simple trend following operations. It goes long when price closes above the upper band and goes short when price closes below the lower band."
- Strategy Logic, as printed: (1) calculate weighted moving averages of highest and lowest prices for a specified period to get upper and lower bands; (2) when close is higher than the upper band, go long; (3) when close is lower than the lower band, go short; (4) closing prices breaking the bands in reverse signal exits; (5) allows selecting effective start time of strategy, default is full period.
- Advantages, as printed: simple parameters; clear trading signals from band breakouts; flexible selection of effective strategy timeframe; simple and clear logic; "Good backtest results, pairs well with trending markets".
- Risks, as printed: "Unlimited loss risk as a short strategy"; improper parameters may cause frequent stop loss and re-entries; "Ineffective in range-bound choppy markets, prone to being trapped"; "Needs additional filters besides just indicator to avoid failures".
- Optimization, as printed: optimize parameter combinations; add trailing stop loss to ensure risk control; add EMA etc. to determine market condition and entry timing; combine volume to avoid false breakouts in choppy conditions; implement time filtering to narrow strategy effective period.
- Summary, as printed: the strategy achieves simple trend following through Gann HiLo bands but can be improved further through enhancing indicator logic, parameter optimization and risk control.

Two of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the "weighted moving averages" claim (the code uses simple arithmetic means) and the "default is full period" claim (the code defaults to a 2017-01-01 gate).

### Research interpretation

Falsifiable mechanism hypothesis: daily BTC returns exhibit short-horizon trend persistence, and a close outside a displaced short-window average-high / average-low band marks a change in local drift; holding that reading as a persistent state until the close crosses the opposite band acts as a whipsaw filter that converts a level-crossing test into a two-state machine, so only state flips trade rather than every crossing of a level. Candidate behavioural or structural channels are slow diffusion of directional information in a 24/7 market with no closing auction, and herding or positioning feedback after a visible break of a short-term range. This is a ported technical-analysis hypothesis: the source supplies no economic rationale and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Regime / trend state: the persistent `hilo` state machine built on SMA(high, 3) and SMA(low, 3) each displaced by 1 bar.
- Entry signal: state transition -1 to +1 for long, +1 to -1 for short.
- Confirmation filter: none. The source explicitly lists adding an EMA filter, a volume filter and time filtering as future work.
- Risk / exit: none. Exit is exclusively the opposite-side state transition.

No component is assumed to contribute alpha; ablation is required by the falsification plan. Because `hilo` only changes on a close beyond the opposite band, and because there is no flat state after the first transition, this is a full-time directional exposure rule rather than a conditional-allocation rule: once started it is always long or always short. That property is derived from the pinned code, not asserted by the prose.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (the `period: 1d` value in the pinned backtest header).
- Inputs at decision bar `t`: `close[t]`, `high[t]`, `high[t-1]`, `high[t-2]`, `low[t]`, `low[t-1]`, `low[t-2]`, `hilo[t-1]`, and `time[t]`.
- Order timing: market orders created by `strategy.entry`; the declaration sets `process_orders_on_close=true`, so the order created while evaluating bar `t` fills at the close of bar `t`. This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Intra-bar recalculation: `calc_on_every_tick` is not present in the pinned declaration. Official TradingView declaration-statement documentation states the parameter defaults to `false`, i.e. the strategy executes strictly once per bar on the closing tick. This is recorded as source-declared-by-language-default, not as a research-proposed choice.
- Timezone: the only time reference is `time[t]` compared with `timestamp(backtest_year, backtest_month, backtest_day, 00, 00)`. Pine time functions with an omitted `timezone` argument use the symbol's exchange time zone, and the artifact pins no timezone, so the gate boundary is `underspecified`. This is immaterial for any evaluation window whose first bar opens on or after 2017-01-02, because the gate is then unconditionally true for every exchange time zone within 14 hours of UTC.

**Lookback, formulas and warmup**

- `Length` is declared verbatim as `len = input.int(3, 'Length', step=1, minval=1)` → 3.
- `Offset` is declared verbatim as `displace = input.int(1, 'Offset', step=1, minval=0)` → 1.
- The bands are declared verbatim as `hi = ta.sma(high, len)` and `lo = ta.sma(low, len)`, i.e. `hi[t] = ta.sma(high, 3)` = arithmetic mean of `high` over bars `t-2 .. t` inclusive, and `lo[t] = ta.sma(low, 3)` = arithmetic mean of `low` over bars `t-2 .. t` inclusive.
- The rule compares against `hi[t-1]` and `lo[t-1]`, so the effective reference window is bars `t-3 .. t-1`.
- State machine, exact:

```text
hilo[0] = na
hilo[t] = close[t] > hi[t-1] ? +1 : (close[t] < lo[t-1] ? -1 : hilo[t-1])
```

  While `hilo[t-1]` is `na` and neither crossing condition holds, `hilo[t]` stays `na`.
- Warmup, derived from the pinned code because the source declares none: `hi[t-1]` first exists at bar index 3 (0-based) and `hilo[t-1]` first exists at bar index 4, so the earliest possible state-transition entry is the 5th completed bar. `max_bars_back` is not declared.

**Entry**

- Long entry: `hilo[t] == +1` AND `hilo[t-1] == -1` AND `time[t] >= start_time`.
- Short entry: `hilo[t] == -1` AND `hilo[t-1] == +1` AND `time[t] >= start_time`.
- Both conditions are mutually exclusive, so conflict priority is provably irrelevant.
- The initial `na` state satisfies neither condition, so no order is possible until a full `-1` to `+1` or `+1` to `-1` transition has been observed in the series.
- Start gate, exact: `start_time = from_start ? 0 : timestamp(backtest_year, backtest_month, backtest_day, 00, 00)` with declared input defaults `from_start = input(false, 'Begin from start?')` → false, `backtest_year = input(2017, 'From Year')` → 2017, `backtest_month = input.int(01, 'From Month', minval=1, maxval=12, step=1)` → 1, `backtest_day = input.int(01, 'From Day', minval=1, maxval=31, step=1)` → 1. The default therefore gates orders on bar time at or after 2017-01-01 00:00 in the exchange time zone.
- Ties and simultaneous signals: impossible by construction (mutually exclusive transitions, one order per bar).

**Exit**

- The pinned code contains exactly two order calls, both `strategy.entry`. Censuses over the whole artifact: `strategy.close` 0, `strategy.close_all` 0, `strategy.exit` 0, `strategy.stop` 0, `strategy.order` 0.
- Therefore the only exit is the opposite-side `strategy.entry`. With `pyramiding=0`, that single same-bar-close fill closes the open trade and opens the opposite trade at the new order's size.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none. Flat / all-cash state after the first transition: unreachable.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by state persistence; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1, enforced by `pyramiding=0`.
- Same-direction re-entry: unreachable, because returning to the same side requires an intermediate opposite-side order.
- Cooldown: none declared. With pyramiding 0 and transition-only triggers, no repeated or same-bar entry can occur, so cooldown semantics are provably irrelevant rather than missing.

**Parameters, sizing and pyramiding**

- All strategy parameters are declared in source with these defaults: `Length 3`, `Offset 1`, `Begin from start? false`, `From Year 2017`, `From Month 1`, `From Day 1`. The pinned declaration reads verbatim: `strategy('Gann HiLo Activator Strategy', overlay=true, pyramiding=0, default_qty_type=strategy.percent_of_equity, default_qty_value=20, initial_capital=1000, process_orders_on_close=true)`, i.e. `pyramiding=0`, `default_qty_value=20`, `initial_capital=1000`, `process_orders_on_close=true`, `overlay=true`.
- The artifact's `Strategy Arguments` table disagrees with the code on three of them (`Offset`, `From Month`, `From Day` printed as `true`) and is recorded as a contradiction; the code block is treated as authoritative because it is the executable text.
- Sizing: each entry order is `20%` of current strategy equity at order time → compounding, not fixed. Account `currency` is not declared in source.
- Reversal sizing: the opposite-side order is again 20% of current equity, and official TradingView documentation states the resulting position size equals the order size, so the reversal does not scale to the prior position's notional.
- Leverage: `margin_long` and `margin_short` are absent from the declaration; official TradingView documentation states both default to `100`, i.e. 100% margin and 1:1 leverage, so the source assumes no borrowed funds. Recorded as source-declared-by-language-default.
- Direction: both sides explicit. Spot is not applicable to the short leg, so the declared market type is perpetual (see Required data).

**Reconstruction status**

Every field required to replay the rule — indicator variant, source prices, lookback, displacement, thresholds, comparison direction, state transitions, conflict priority, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe and warmup — is explicit in the pinned source. The residual `underspecified` items are the exchange time zone of the start gate, the account currency, the exact Binance contract, and the cost model; none of them alters the signal, and the last two are recorded as `data gap` rather than filled.

## Required data

- Instrument: BTCUSDT on Binance USDT-margined futures, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking.
- Market type: perpetual. The source explicitly runs on a margined futures venue and the rule shorts, so a margined long/short instrument is required. The artifact does not distinguish the perpetual from a dated future, which is `data gap`; it is immaterial to an OHLCV-only signal but must be pinned before any execution work.
- Spot applicability: not applicable to the short leg, because spot would require naked shorting. The long leg alone could run on spot, but that would be a modified strategy and is not proposed.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, from `period: 1d`. The same header prints `basePeriod: 1h`; the pinned script contains 0 `request.*` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align.
- Fields used: `high`, `low`, `close` of the decision bar and `high`/`low` of the two preceding bars, plus bar time for the start gate. Volume is not an input: the token `volume` occurs once in the artifact and only inside the Optimization prose.
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state.
- Point-in-time: every input at bar `t` is contemporaneous or lagged (`hi[t-1]`, `lo[t-1]`, `hilo[t-1]`); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow`, and no `security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: bar open time compared with `timestamp(2017, 1, 1, 00, 00)`; the timezone argument is omitted, so Pine resolves it to the symbol's exchange time zone, and the artifact pins no timezone → `underspecified` boundary convention only.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here.
- Funding, fee and spread needs: none specified. Word-boundary census of the pinned 4199-character artifact gives commission 0, slippage 0, fee 0, funding 0, leverage 0, margin 0, spread 0, impact 0, turnover 0, capacity 0. These are `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration):

- Order type: market order, created only by `strategy.entry`. There is no limit order, no stop order and no conditional order anywhere in the rule.
- Fill model: `process_orders_on_close=true` → the order created while evaluating bar `t` is filled at the close of bar `t`; `calc_on_every_tick` defaults to `false` per official documentation, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled in the same completed-bar close.
- Reversal semantics: an opposite-side `strategy.entry` under `pyramiding=0` produces one fill that closes the open trade and opens the opposite trade at the order size.
- Position limits: one position at a time; 20% of current equity per entry; no pyramiding; no scaling, grid or martingale layer.
- Leverage and margin: absent from the declaration; documented default is 100% margin, i.e. 1:1, so the source assumes no borrowed funds and therefore no dependency on unsupported leverage effects.
- Shorting and borrow: the source assumes a margined futures venue. Borrow availability and any stock-loan analogue are not addressed → `data gap`, and spot shorting is explicitly out of scope.
- Costs: no commission, no slippage, no spread, no market-impact and no funding model appears anywhere in the artifact → `data gap`. The source's own simulated results therefore embed undeclared engine defaults, which the source never states; this record does not adopt them as a validated zero-cost assumption.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F10.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code or official TradingView documentation. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 4199-character artifact: sharpe 0, drawdown 0, cagr 0, profit 0, return 0, win rate 0, annualized 0, trade 0, trades 0, commission 0, slippage 0, fee 0, funding 0, leverage 0, margin 0, capacity 0, turnover 0. The substring `backtest` occurs 8 times, all inside the `/*backtest ...*/` header, the `backtest_year` / `backtest_month` / `backtest_day` identifiers and two `// backtest ... window` comments. There is no `**backtest**` image block, no equity curve, no trade list, no table and no figure anywhere in the artifact.

What the source does report:

- Configuration only, from the pinned header: backtest start 2022-09-10 00:00:00, end 2023-09-16 00:00:00, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- Parameter defaults as listed under Signal, plus the six exposed Strategy parameters (Length, Offset, Begin from start?, From Year, From Month, From Day) confirmed both in the artifact table and on the public landing page.
- One qualitative performance claim, verbatim: "Good backtest results, pairs well with trending markets", carrying no sample, no metric, no baseline and no figure → unverifiable as printed and recorded as a bare claim, not as evidence.
- Landing metadata read 2026-10-05: Created 2023-09-17 18:36:01, Last modified "3 years ago", Copy 0, Hits 1226.
- Research-computed, not printed: the header window spans about 371 calendar days, i.e. roughly 371 daily bars on a 24/7 market; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact and of its Pine block, whitespace-normalization digests, extraction and line counting of the Pine block, a whole-artifact term and word-boundary census, enumeration of `strategy.*` call sites, reading of the public FMZ landing page, and record-side enumeration of the printed header values. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, profit, return, win rate and trade counts are all 0 occurrences.
2. The single performance claim ("Good backtest results") is unaccompanied by any sample, metric or baseline, so it cannot be checked as printed.
3. The only configured backtest window is about one year (2022-09-10 to 2023-09-16) on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. No cost model at all: commission, slippage, fee, spread, impact and funding all return 0 word-boundary hits, so any edge claim is unpriced.
5. No risk layer of any kind: stop loss, take profit, trailing stop and time exit are all absent from the code, while the source's own Optimization block proposes adding a trailing stop as future work.
6. The source's own Risks block states "Unlimited loss risk as a short strategy" and "Ineffective in range-bound choppy markets, prone to being trapped".
7. The source's own Risks block states the rule "Needs additional filters besides just indicator", i.e. the published rule is explicitly presented as a bare template.
8. The source's own Risks block refers to a stop loss that the pinned code never implements (recorded contradiction 3).
9. Prose claims the bands are weighted moving averages; the code uses simple arithmetic means (recorded contradiction 2).
10. Prose claims the default effective period is the full period; the code defaults to a 2017-01-01 gate (recorded contradiction 1).
11. The artifact's own Strategy Arguments table prints three integer defaults as `true`, contradicting the code (recorded contradiction 4).
12. After the first state transition the system is never flat, so it carries permanent long-or-short exposure with no cash fallback and no drawdown control.
13. The lookback is extremely short (3-bar SMA of high and low, displaced 1 bar), which mechanically maximizes flip frequency and whipsaw exposure in ranges.
14. Holding period is unbounded and there is no exit other than an opposite signal, so a stale position can persist indefinitely if the state stops flipping.
15. The full source is behind a login on the FMZ landing page and is publicly reachable only through a third-party mirror repository, leaving a single point of provenance.
16. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; only the script's own MPL-2.0 notice is printed inside the block.
17. Authorship is layered and unverified: the mirror records `Author: ChaoZhang`, the code prints `// © starbolt`, and neither identity is independently confirmed; peer-review status is not stated in source.
18. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows a single "Last modified" timestamp.
19. FMZ landing statistics (Copy 0, Hits 1226 as read 2026-10-05) show no community adoption signal, and no third-party study of this exact artifact was identified.
20. The base-K-line field `basePeriod: 1h` in the header sits next to a `1d` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
21. The start-gate timezone is not pinned by the source, so the exact boundary of the 2017-01-01 gate is `underspecified`.
22. The exact Binance contract (perpetual versus dated future) is not distinguished by the source, and no missing-data, halt or partial-fill handling is specified.
23. No independent replication, no competing study and no contrary external evidence specific to this artifact was found; absence of contrary literature is not evidence of robustness.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, the identical `hilo` state sequence and an identical ordered list of entry bars and sides (exact match, zero differing bars after the first possible entry at bar index 4). Action: any mismatch means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`hi[t-1]`, `lo[t-1]`, `hilo[t-1]`, `close[t]`, `time[t]`), with zero occurrences of future bars, negative shifts, `timenow`, session recalculation, or any lower-timeframe request. Action: any future reference found ⇒ NOT_LOSSLESS, close the record.
- **F3 — Cost ladder.** Threshold (research-defined): apply 0 / 1 / 2 / 5 / 10 bps per side plus a commission leg and, for the perpetual, a funding accrual leg; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side. Action: fail ⇒ the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F4 — Parameter perturbation.** Threshold (research-defined): sweep `Length` over 2, 3, 4, 5, 8, 13, 20 and `Offset` over 0, 1, 2 with everything else frozen; fail if the sign of net return over the full sample flips for the published cell or if fewer than half of the 21 cells produce positive net return. Action: fail ⇒ parameter-lottery diagnosis, no adoption.
- **F5 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility (low / mid / high) and, separately, by a 60-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail ⇒ the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F6 — Always-in-market placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 random flip sequences that preserve the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution. Action: fail ⇒ no evidence that the band-flip timing carries information.
- **F7 — Start-gate sensitivity.** Threshold (research-defined): run the frozen rule with the gate exactly as declared and again with `from_start = true`; fail if more than 50% of total net PnL is attributable to the gate choice. Action: fail ⇒ the result is a window artifact, not a mechanism.
- **F8 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1d BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail ⇒ reject for adoption; do not rescue by re-tuning.
- **F9 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side. Action: fail ⇒ single-asset overfit diagnosis.
- **F10 — Capacity and liquidity.** Threshold (research-defined): fail if required notional at 20% of equity exceeds 5% of the trailing 30-day median daily volume of the instrument. Action: fail ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F11 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F4 × F9 cell family; fail if the published cell does not survive. Action: fail ⇒ treat the published configuration as one draw among many, no adoption.
- **F12 — Risk-layer ablation.** Threshold (research-defined): since the source contains no stop, take-profit or time exit, measure maximum drawdown and the worst single position run; fail if maximum drawdown exceeds 40% on the frozen sample or if any single holding period exceeds 365 daily bars. Action: fail ⇒ document the unbounded-exposure failure and keep research-only.
- **F13 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `Length 3`, `Offset 1`, the `hilo` state machine, the transition-only entry rule, the opposite-entry-only exit, `pyramiding 0`, 20% percent-of-equity compounding sizing, `process_orders_on_close` same-bar-close fills, the single `1d` timeframe, the BTCUSDT perpetual instrument and the 2017-01-01 start gate are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1d`, so the instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `high`, `low`, `close` and bar time, all available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal.
- Shorting requires a margined instrument; the source already uses a futures venue, so the perpetual is the natural target and spot is out of scope for the short leg.
- The start gate is a plain bar-time comparison and does not depend on a market session, so the 24/7 clock changes only the exact first eligible bar near 2017-01-01.
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual (never mentioned, `data gap`), the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and liquidity or market-impact differences at 20% of equity sizing (`data gap`).
- Timestamp and candle boundaries are exchange-defined UTC daily bars on Binance; the record does not assume any other boundary convention.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no cost model, no latency model, no fill-failure model, no missing-data handling, no capacity statement, no exact contract pin, no account currency, no performance output.
- `underspecified`: the exchange time zone of the 2017-01-01 start gate; the precise Binance contract; whether the FMZ backtest engine's `basePeriod: 1h` field influenced any published number (the script itself makes no cross-timeframe call).
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity and forward performance.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review and a layered, unverified authorship; the landing hides the full source behind a login.
- Reproducibility limitation: because FMZ hides the full source and prints no results, the only immutable, publicly auditable artifact is the mirror at the pinned SHA, and there is no way to verify the claim of good backtest results.
- Identification limitation: the rule is price-only and unfalsified; nothing in the source separates trend persistence from a beta or from a drawdown-carrying always-in-market exposure.
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust, and Copy 0 suggests no demonstrated community reuse.
- Incremental-write check: this is the first record in the repository for this source identity after the 2026-10-04 pool reset, and no Wiki Brain page exists for it, so this is not ordinary duplicate material.
- A four-item contradiction set is recorded in frontmatter. All four are prose-versus-code or table-versus-code conflicts inside one artifact, and in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and its verification script.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family or by execution and validation discipline rather than by source identity; none of them shares the Gann HiLo Activator source, the band state-machine signal, or the BTCUSDT daily single-pair scope:

- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/tradingview-volume-weighted-supertrend-dual-confirmation-2026-09-16]]
- [[quant/tradingview-proborsa-rsi-supertrend-double-dip-strategy-2026-08-24]]
- [[quant/tradingview-choppiness-donchian-breakout-filter-2026-09-16]]
- [[quant/crypto-perpetual-regime-aligned-right-tail-trend-cost-hurdle-2026-09-13]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]
- [[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]

## Sources

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `干浪激活器策略Gann-HiLo-Activator-Strategy.md`; the complete primary source read end to end on 2026-10-05, SHA-256 `bc3f451e4699b2d0b61392febdf5a5665fea1d5cd7834a8fb35c24202c27e54e`.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%B9%B2%E6%B5%AA%E6%BF%80%E6%B4%BB%E5%99%A8%E7%AD%96%E7%95%A5Gann-HiLo-Activator-Strategy.md — percent-encoded form of the same pinned file.
- https://www.fmz.com/strategy/427070 — FMZ landing page, read 2026-10-05; confirms title, author account, creation timestamp, English description, backtest header, exposed parameters, and that the full source requires login.
- https://www.tradingview.com/pine-script-docs/language/declaration-statements/ — official first-party documentation used only for language-level semantics of the pinned declaration (`calc_on_every_tick` default false, `margin_long` / `margin_short` default 100, opposite-direction entry producing a position equal to the order size).
- https://www.tradingview.com/pine-script-docs/concepts/time/ — official first-party documentation used only for the default time zone of time functions with an omitted `timezone` argument.
