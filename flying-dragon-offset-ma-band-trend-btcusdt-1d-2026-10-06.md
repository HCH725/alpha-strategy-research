---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Flying Dragon offset moving-average band trend system on BTCUSDT 1d bars
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-07
sources:
  - https://github.com/fmzquant/strategies
  - https://www.fmz.com/strategy/431391
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The artifact Strategy Arguments table prints From Day / From Month / From Year and To Day / To Month / To Year inputs, but the pinned Pine declares no such inputs and calls timestamp() zero times, so there is no strategy-level date gate in code; the 2022-10-31 to 2023-02-14 window lives only in the FMZ backtest header comment. Code is authoritative."
  - "The prose Risk section warns of consecutive stop-loss exits and the inputs offer a Use Stop Loss switch, but the pinned default is useStop=false, so under the recorded default configuration no stop order can activate; the stop-exit calls are na-parameterised no-ops (see Signal)."
---

# Flying Dragon offset moving-average band trend system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (`ls-remote` HEAD check on 2026-10-06 confirms this is still the repository head; same pin as the Gann HiLo, VIDYA, Bookstaber, and P-Signal admissions).
- Exact file path: `飞龙趋势策略Flying-Dragon-Trend-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E9%A3%9E%E9%BE%99%E8%B6%8B%E5%8A%BF%E7%AD%96%E7%95%A5Flying-Dragon-Trend-Strategy.md )
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/431391
- GitHub blob SHA at the pinned commit: `e0c4f45efb3d714f0ab69a0cf745aaf78a147ed5`, size 14750 bytes.
- Byte-identity check: the file fetched from the GitHub contents API at the pinned commit is byte-identical (`cmp` clean) to the copy inspected; SHA-256 `25f20c6610df4092d1d44f9c06dd812c33c24a30837bfa2baa9aa35884d88963`, 14750 bytes, 260 lines.
- The `MarkoP010` author credit (the Pine block prints `// © MarkoP010 2023` under MPL-2.0; the mirror attributes the port to ChaoZhang) occurs in exactly one file in the repository, so there is no competing variant to choose between.
- Licence and rights: the pinned Pine block prints `// This source code is subject to the terms of the Mozilla Public License 2.0`; this record cites and normalizes the rule and reproduces no source code block.

Pre-write dedup (2026-10-06): a case-insensitive search of the working tree for `dragon`, `flying`, `431391`, `markop` returns 0 strategy records. `gh pr list --state open` is empty, so no open `research/*` PR shares this source or signal. Against the 11 PASS records on `main` plus the four closed research PRs (#6 Wave Trend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI): mechanism, signal construction, and source identity are all distinct. The closest relative is the EHMA range-band record, and the two differ on every axis that matters — EHMA is a custom borserman exponential-Hull recursion (Period 180, zero `ta.*` calls) with symmetric ±2 percent envelope bands, long-only at defaults, comparing the contemporaneous close against envelope levels; this record is built-in `ta.hma(35)` / `ta.sma(22)` with multi-bar historical offsets, dual-direction with opposite-signal reversal and `pyramiding=3`, comparing the close against a 6-bar-lagged Hull level at the pinned Medium risk level. Different smoothing family, different trigger construction (percentage envelope versus lagged-level crossing), different direction handling, different source file. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only a visual trend-band premise: two moving averages (fast MA1 with three offsets forming MA2/MA3, slow MA4) draw colored trend bands, green for uptrend and red for downtrend, and price crossing different bands at five selectable risk levels generates signals with different risk; offsets are called "where the magic happens". No behavioural, structural, or risk-premium channel is claimed.

### Research interpretation

Falsifiable hypothesis: a close holding above its own 6-bar-old Hull-smoothed level marks order flow strong enough to stay bid above a slow-moving consensus, and such displacements exhibit short-horizon directional persistence because the offset construction buys confirmation lag instead of band width — the signal fires only when price has outrun where the average stood almost a week ago, which filters chop that merely wiggles around a contemporaneous average. The mirror-image breakdown reverses to short on the same logic. This is a ported technical-analysis hypothesis; the source supplies no sample, no metric, and no evidence, so the mechanism is research interpretation, not source-reported fact.

## Signal

All symbols below are the program's own identifiers; all values are program defaults, pinned. Only the default configuration is this record — non-default MA types, lengths, offsets, risk levels, or directions are different variants, not this strategy.

Engine semantics (explicit in source): `process_orders_on_close=true`, `calc_on_order_fills=false`, `calc_on_every_tick` absent (language default false, same default the merged Gann HiLo record relies on), `pyramiding=3`, `strategy.risk.allow_entry_in(strategy.direction.all)` at the Both default. Completed-bar decision with same-bar-close execution; no intrabar evaluation.

Inputs (defaults):

```text
strDirection = "Both"          // Both | Long | Short
riskLevel    = "Medium"        // Highest | High | Medium | Low | Lowest
useStop      = false
stopPrct     = 10 (%)
MA1: type HMA, length 35, source close, offsets 0 / 4 / 6  (ma1, ma2, ma3)
MA4: type SMA, length 22, source close, offset 2          (ma4)
```

Formulas (exact, causal — positive `[n]` indexes history, never the future):

```text
ma1 = ta.hma(close, 35)[0]
ma2 = ma1[4]                   // HMA value 4 bars ago
ma3 = ma1[6]                   // HMA value 6 bars ago
ma4 = ta.sma(close, 22)[2]     // SMA value 2 bars ago
longCondition  = close > ma3   // Medium level; strict >
shortCondition = close < ma3   // Medium level; strict <
```

Trade events (the complete order-call set — two `strategy.entry` calls, two `strategy.exit` calls; zero `strategy.order` / `strategy.close` / `strategy.cancel` calls):

```text
if longCondition  -> strategy.entry("Long", strategy.long)
                     strategy.exit("Long Stop", "Long", stop=na)    // no-op under useStop=false
if shortCondition -> strategy.entry("Short", strategy.short)
                     strategy.exit("Short Stop", "Short", stop=na)  // no-op under useStop=false
```

Direction: both sides explicit at the Both default (`allow_entry_in(all)`). Source market in the FMZ header is `Futures_Binance BTC_USDT`, so the short leg is native, not naked; spot incompatibility does not arise.

Exits and risk (explicit): the only exit under the recorded defaults is opposite-signal reversal — a short entry while long nets flat-then-short through standard Pine netting, the same reversal construction the merged Gann HiLo record relies on. Stop loss, take profit, trailing stop, and time limit are absent/disabled: `useStop=false` forces both stop prices to `na`, and each `strategy.exit` call then carries no stop, limit, profit, loss, or trailing parameter with no same-ID exit anywhere else to cancel, so neither call can change any trade event under the recorded configuration. Recorded as explicitly disabled, not as defaults to be assumed.

Position and re-entry (explicit): `pyramiding=3` with one entry id per side means up to three same-side adds while the condition persists on consecutive bars; further same-side entries are engine-rejected at the cap, and after an opposite-signal reversal the count restarts on the new side. Re-entry after exit is fully specified (the next true condition bar enters) — no cooldown, no missing rule. The file reads `strategy.position_avg_price` only inside the na-disabled stop computation; no `position_size`, `openprofit`, or `opentrades` reference exists, so no live position-aware state conditions any signal or active exit.

Conflict priority (provably irrelevant): `longCondition` and `shortCondition` compare the same two scalars with strict `>` / `<`, so both can never fire on the same bar; exact equality fires neither leg and the position simply persists. No priority rule is needed and none is missing.

Determinism note for the reviewer: the rule uses no `crossover()` / `crossunder()` / `ta.cross` call — only strict scalar comparisons — so the Gate-6 tie-semantics precedent does not arise. The seven-way MA-type switch, the VWMA volume branch, and the ADX/Stochastic-style extras seen in neighbouring FMZ files are not in this program; the only `ta.*` calls reachable under the pinned defaults are `ta.hma` and `ta.sma`, both deterministic causal built-ins. The file contains zero `request.*`, `security()`, `barstate.*`, `alert()`, `import`, Heikin-Ashi, `rightBars`, or active stop/limit order arguments.

## Required data

- 1d bars of one pair: `close` only (the Hull/SMA chains and both comparisons read nothing else; `open/high/low/volume` never enter the trading logic). No indicators beyond the two deterministic offset moving averages computed from those candles.
- No funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, or cross-venue state is referenced or required.
- Warmup is derivable and exact: 46 bars (the HMA-35 chain first yields at ~40 bars, plus the 6-bar historical offset; the SMA-22 chain needs 24). Before that the lagged levels are `na`, both comparisons are false, and the backtest holds flat — deterministic, no invention.

## Execution assumptions

- Source execution semantics: `process_orders_on_close=true` on 1d bars — decided on the completed bar, filled at that same bar's close. Compatible with the pinned Hummingbot baseline lane; no conversion required. The FMZ runner header additionally prints `CalcOnTick=true` / `CalcOnorderFills=true`; those are that platform's runner flags, while the Pine declaration (`calc_on_order_fills=false`, once-per-bar, same-bar-close) is code-authoritative for this record.
- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1d` decision timeframe. The FMZ backtest header pins `period: 1d` with `Futures_Binance BTC_USDT` — the same header-to-timeframe reading the merged Gann HiLo record uses — and the script contains 0 `request.*` calls, so the neighbouring `basePeriod: 1h` field feeds no rule and there is no multi-timeframe dependency to align. No price-series substitution is performed: the record uses the same BTCUSDT futures klines the source configures.
- Source sizing (`strategy.percent_of_equity`, 5) and the source commission model (`cash_per_order` 10) are event-neutral accounting: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x, pinned Binance fees plus realized funding). The overlay changes no signal, event, or exit.
- The FMZ header window (2022-10-31 00:00:00 → 2023-02-14 00:00:00, roughly 106 daily bars on a 24/7 market — our arithmetic, not a source sample-size claim) is backtest scope, not signal. Downstream must state which scoping it applies; it must not silently re-tune scope or parameters on final OOS data.

## Evidence

### Source-reported

Nothing. The artifact prints no sample, no metric, no table, no figure, and no performance claim of any kind — only qualitative prose ("novel logic", "high practical utility", "worth researching"). Recorded as bare claims, not as evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No contradictory performance or failure report is printed in source. The absence of evidence is recorded as absence, not as support.

## Falsification plan

Research tests only — none of these substitutes for a missing rule (no rule is missing):

1. Offset ablation: run all offsets at 0 (contemporaneous HMA35/SMA22 cross-noise); if the edge survives without the 6-bar lag, the offset premise is decoration, not mechanism.
2. Risk-level sweep as robustness, not tuning: Highest/High/Low/Lowest must keep the same sign on a frozen split, or the Medium pin is cherry-picked.
3. MA-type swap: re-run MA1 as EMA/SMA at length 35; a sign flip means the record is HMA-specific curve-fit, not band logic.
4. Steady-state add accounting: verify the backtest holds 3 same-side units through long condition runs and reverses whole-then-rebuilds on flips; any deviation is an implementation bug, not a strategy property.
5. Cost sensitivity: re-run with round-trip costs doubled under the house overlay; a trend edge that needs near-zero costs is execution fiction, not signal.

## Crypto portability

`direct` — with the same narrow meaning as the merged Gann HiLo record: the cited source itself configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1d`, so instrument, venue, and market type are already crypto and no porting change is required to express the rule. `direct` is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result. Two port notes: (a) crypto 1d trends can sustain longer unbroken runs than equity charts the original author may have eyeballed, which exercises the pyramided 3-unit steady state more often — expected behavior, not a bug; (b) the 10% default stop distance is tuned for nothing in source and is OFF by default, so downstream must not silently enable it.

## Limitations

1. No protective stop exists under the recorded defaults; tail risk on vertical adverse moves is borne fully by the reversal exit. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop.
2. The FMZ header window is part of the pinned configuration scope. Any downstream run must state its scoping; re-tuning scope or the HMA35/SMA22/offsets/Medium pin on final OOS data is forbidden by the house overlay contract.
3. Only program defaults are pinned (HMA35/SMA22, offsets 0/4/6/2, Medium, Both, useStop=false). Non-default input combinations are different variants, not separate confirmations of this record.
4. Confidence is `medium` (interpretation confidence): the rule text is complete and unambiguous with exact offset arithmetic, but the source is a porter-cloned mirror file offering no performance output, no peer review, and no market-microstructure account of lagged-Hull persistence; the Strategy Arguments table disagrees with the code on the date inputs (see contradictions).
5. The exit no-op reading relies on Pine v5 `strategy.exit` semantics for all-na parameters under `useStop=false`; the calls carry unique ids with no other exit to disturb, so no trade event depends on the reading either way — flagged for the reviewer's engine check, not assumed silently.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable program file at pinned commit (all rules): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E9%A3%9E%E9%BE%99%E8%B6%8B%E5%8A%BF%E7%AD%96%E7%95%A5Flying-Dragon-Trend-Strategy.md
- Repository (project context): https://github.com/fmzquant/strategies
- FMZ strategy detail recorded inside the artifact: https://www.fmz.com/strategy/431391
