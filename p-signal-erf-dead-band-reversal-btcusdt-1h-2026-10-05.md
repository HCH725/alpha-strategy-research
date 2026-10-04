---
schema: strategy-research-record-v1
title: P-Signal erf dead-band reversal system on BTCUSDT 1h bars
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
  - https://www.fmz.com/strategy/440338
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-docs/language/declaration-statements/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
  - https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ/English prose states the system 'goes short when the P-signal reverses from positive to negative, and long when it reverses from negative to positive', but the pinned code never orders on a zero crossing: it orders short only while nPSignal is strictly greater than +dead-band and falling, and long only while nPSignal is strictly less than -dead-band and rising, so a sign change through zero with a small magnitude produces no order at all."
  - "The FMZ/English prose states that 'Observation time controls the start time of the strategy', but the pinned code declares tStartDate and then never references it (the identifier occurs exactly once, at its declaration); the only gate that reaches an order is the constant bool isStartDate = true, so the exposed Start date input is inert and the rule has no time gate."
  - "The artifact's own Strategy Arguments table prints the Delta-Erf default as 'false' while the pinned code declares input.float(title='|Delta Erf|:', defval=0, minval=0, maxval=1, step=0.01), i.e. numeric 0; the executable code block is treated as authoritative."
---

# P-Signal erf dead-band reversal system on BTCUSDT 1h bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30T11:10:28+08:00, subject `update`; confirmed still the repository head at research time through `gh api repos/fmzquant/strategies/commits/HEAD`).
- Exact file path: `P-信号反转策略P-Signal-Reversal-Strategy.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/P-%E4%BF%A1%E5%8F%B7%E5%8F%8D%E8%BD%AC%E7%AD%96%E7%95%A5P-Signal-Reversal-Strategy.md , which was opened in a browser on 2026-10-05 and returned the correct file at the pinned SHA).
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/440338

Primary-source checksums pinned 2026-10-05:

- File 9277 bytes, SHA-256 `35c6997c7045d8295f00f86cf0fb08691fb502c86c3dcb30c3183fb5617979bf`, 7962 characters, 184 newline characters (185 split lines).
- Whitespace-collapsed variant 7771 characters, SHA-256 `a52c699a4dbbaae91143d488409d2a796c29e51e8a6b28df413779d41c2333bf`.
- The fenced Pine block alone: 3351 characters, 62 newline characters, SHA-256 `859c7469ba040de37a6c4010cfb7a374c60952093ee8892620f7fdcc97da3792`.
- Independent remote check: the git blob id of that path at the pinned commit is `a0bfbdf924c3f5b8fb20d4ca0b251f1da6ed7a4b`, and the blob fetched back from the GitHub API by that id is byte-identical to the local artifact (identical SHA-256), so the pinned bytes are the bytes GitHub serves.

Artifact structure as printed: `> Name` (P-信号反转策略P-Signal-Reversal-Strategy), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English set inside one `[trans]` block), `> Strategy Arguments` table with three rows, `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/440338, `> Last Modified` = 2024-01-29 14:44:56.

Licence and rights: the pinned Pine block itself prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// P-Signal Strategy RVS © Kharevsky`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page read directly in a browser session on 2026-10-05 (public, no login for the description layer): browser title `🐴 P-Signal Reversal Strategy | FMZ`, heading `P-Signal Reversal Strategy`, badge `Common strategy`, `Created: 2024-01-29 14:44:56`, `Last modified: 3 years ago`, `Copy: 0`, `Hits: 1020`, author account `ChaoZhang`, zero comments, the English Overview / Strategy Principles / Advantage / Risk / Optimization / Summary prose identical to the mirror's English block, a rendered `Source / Pine` section showing the `/*backtest*/` header, the `//@version=5` line, the MPL-2.0 notice and the author line before the literal string `Login to view full source`, and the three exposed Strategy parameters (`Cardinality:`, `|ΔErf|:`, `Start date:`). Word-boundary counts over the landing page's rendered text: `net profit` 0, `sharpe` 0, `roi` 0, `max drawdown` 0, `profit factor` 0, `total closed trades` 0, `strategy tester` 0, `annualized` 0, `win rate` 0, `equity curve` 0, `backtest result` 0 — the landing shows no performance table, no equity curve and no trade list. Two provenance notes, stated rather than repaired: (a) although the UI hides the source behind a login, the page's own JavaScript payload embeds the complete Pine text; that embedded payload was extracted and compared line by line against the pinned GitHub Pine block — both contain 60 non-blank lines in the same order and are equal once JSON backslash escapes are normalized, the only differing line being the `exchanges: [...]` line inside the `/*backtest*/` comment, which differs purely in quote escaping — so the landing page corroborates the mirror rather than replacing it as the immutable artifact; (b) the landing's displayed `Last modified: 3 years ago` (read 2026-10-05) predates its displayed creation timestamp of 2024-01-29, i.e. the relative label is internally inconsistent and is recorded exactly as displayed.

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source; the mirror's author field (`ChaoZhang`) and the code's own credit (`© Kharevsky`) are two different identities and neither is independently confirmed.

Pre-write dedup (2026-10-05): tracked-content search of `origin/main` for `p-signal`, `psignal`, `kharevsky`, `440338`, `\berf\b`, `error function` returned 0 matches; the loose probe `reversal` returned only two README filename examples and two lines inside the already-merged Gann HiLo record about reversal-order sizing, none of which shares this source, signal or universe. The same four identifier probes returned 0 matches in the open PR #6 record `wave-trend-lazybear-wt1-wt2-cross-btcusdt-1h-2026-10-05.md`. `git ls-remote --heads origin 'research/*'` returned exactly two refs (`research/hermes-gann-hilo-activator-20261005-0148`, already squash-merged as PR #5, and `research/hermes-wave-trend-lazybear-20261005-0318`, open PR #6), and `gh pr list --state open` returned only PR #6, so the dedup set is one record on `main` plus one open research PR. Five-axis distinction against both: mechanism (Gann HiLo band state flip; LazyBear EMA-smoothed oscillator cross) versus this erf-of-standardized-price-change dead-band reversal, signal construction (displaced SMA band flip / wt1-wt2 crossover versus erf(nSma/nStDev/√2) sign-and-slope logic), direction (two-sided like Gann, unlike the long-only Wave Trend), horizon (Gann is `1d`), and source identity all differ. The still-existing but deleted-by-reset historical record `gann-angle-support-resistance-es-intraday-ssrn-6918818-2026-09-29.md` is a different source (SSRN 6918818), a different mechanism and a different market, so it is not a duplicate either.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview, as printed: the strategy is "built based on statistical parameters and error functions to construct a probabilistic signal space", "dynamically acquires trading signals by tracking the extreme value distributions of a series of K-lines to capture market reversal points".
- Strategy Principles, as printed: the P-signal "combines the statistical parameters of moving averages and standard deviations and maps them to the range of -1 to 1 through the Gaussian error function"; "It goes short when the P-signal reverses from positive to negative, and long when it reverses from negative to positive"; "Strategy parameters include Cardinality, ΔErf and Observation Time. Cardinality controls the sample size, ΔErf controls the dead band of the error function to reduce trading frequency. Observation time controls the start time of the strategy."
- Advantage Analysis, as printed: the signal is "built on the probability distributions of statistical parameters", "incorporates more market information and makes more comprehensive and reliable judgements", and its parameterized design "guarantees the strategy's adaptability and flexibility".
- Risk Analysis, as printed: it "relies too much on the parameters for the probability distribution, which is easily affected by abnormal data resulting in misjudgements", and "the risk-reward ratio of reversal strategies generally low, with limited single profit"; mitigation proposed is a larger Cardinality and a wider ΔErf range.
- Optimization Directions, as printed: add other indicators to filter anomalies (volume surges); "Validate signals across multiple timeframes to enhance judgment stability"; "Increase stop loss strategies to reduce single loss"; optimize parameters; incorporate machine learning for dynamic parameter adjustment.
- Summary, as printed: a quantitative framework that "effectively judges the market's statistical characteristics, captures reversal opportunities", "can be further enhanced in stability and profitability through multiple indicator verification and stop loss optimization".

Two of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the zero-crossing description of the reversal and the claim that Observation time controls the strategy start time.

### Research interpretation

Falsifiable mechanism hypothesis: short-horizon changes in the 1-hour midpoint price of a single crypto perpetual are locally scale-stationary, so the standardized first difference of `ohlc4` over a short window is a bounded, mean-reverting statistic; mapping that standardized statistic through a smooth saturating function (the error-function approximation) and smoothing it produces a slow sign-carrying series whose excursion beyond a dead band, while already moving back toward the other side, marks an overextended short-horizon move that is likely to revert. The bet is therefore distributional mean reversion of price *changes*, not trend persistence: the rule buys a negative standardized change that has begun to recover and sells a positive standardized change that has begun to decay, and it holds that side until the standardized change crosses the dead band on the opposite side with the opposite slope. Candidate behavioural channels are short-horizon overreaction plus liquidity replenishment in a 24/7 market with no closing auction, and herding exhaustion after a stretch of one-directional price-change drift. This is a ported statistical-technical hypothesis: the source supplies no economic rationale and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Primary signal: `nPSignal`, the 3-bar simple average of `fErf(ta.change(ohlc4), 3)`, where `fErf` returns a pinned rational approximation of the error function applied to `nSma / nStDev / √2`.
- Confirmation filter: the dead band `ndErf` (declared default 0) plus the sign of `nPSignal − nPSignal[1]`, which together must agree with the side being taken.
- Regime filter: none. The source lists volume filtering and multi-timeframe validation as future work.
- Risk / exit: none. Exit is exclusively the opposite-direction entry (position reversal); stop loss, take profit, trailing stop and time exit are all absent while the source's own Optimization block proposes adding a stop loss.

No component is assumed to contribute alpha; ablation is required by the falsification plan. Because the erf map saturates, a sufficiently extreme standardized change contributes no additional signal magnitude — a property of the pinned function, not an assertion by the prose.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1h` bars of the pinned instrument (the `period: 1h` value in the pinned backtest header).
- Inputs at decision bar `t`: `open[t]`, `high[t]`, `low[t]`, `close[t]` (through `ohlc4[t]`), `ohlc4[t-1]`, `nPSignal[t-1]`.
- Order timing: the only two order calls are `strategy.entry` market orders, and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true "the emulator fills the order immediately on the bar's close instead of waiting for the next bar's opening tick". This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false`, that with all four calculation parameters false "the strategy executes strictly once per bar, on each bar's closing tick", and that `calc_on_every_tick` "does not affect the strategy's executions on historical bars". Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Timezone: the rule contains no time comparison at all — the only `timestamp(...)` literal sits inside the `tStartDate` input, which is declared and never referenced (identifier count 1, declaration only). Timezone conventions are therefore immaterial to the trades, and the `underspecified`-timezone problem that affects time-gated rules does not arise here.

**Lookback, formulas and warmup**

- Parameters as declared: `nPoints = input.int(title='Cardinality:', defval=4, minval=4, maxval=200, ...)` → 4; `ndErf = input.float(title='|ΔErf|:', defval=0, minval=0, maxval=1, step=0.01, ...)` → 0; `tStartDate = input(title='Start date:', defval=timestamp('30 Dec 1957 00:00 +0300'), ...)` → 1957-12-30 00:00 +0300 but inert. `int nIntr = nPoints - 1` → 3.
- `ohlc4` is, per the official v5 reference, "a shortcut for (open + high + low + close)/4".
- `ta.change(ohlc4)` compares the current value with the value `length` bars ago and returns the difference, and "na values in the source series are included in calculations and will produce an na result". The pinned code uses the single-argument overload; the v5 reference entry for `ta.change` prints the one-argument overload `ta.change(source)` but does not print a default for `length`, while the current official reference prints `length ... Optional. The default is 1.` for the merged signature. The 1-bar reading (`ohlc4[t] − ohlc4[t−1]`) is the one used here; the v5 documentation gap is recorded rather than silently resolved, and F1 makes it a reconstruction gate.
- `fPSignal(ser, int)` is declared verbatim as `nStDev = ta.stdev(ser, int)`, `nSma = ta.sma(ser, int)`, `nStDev > 0 ? fErf(nSma / nStDev / math.sqrt(2)) : math.sign(nSma)`.
  - `ta.sma(source, length)` is "the sum of last y values of x, divided by y", with na values ignored.
  - `ta.stdev(source, length, biased)` — the third argument is optional and "The default is true", and "If biased is true, function will calculate using a biased estimate of the entire population" (divide by `length`), "if false - unbiased estimate of a sample". The pinned call therefore uses the population estimator, not the n−1 estimator.
  - The zero-variance branch returns `math.sign(nSma)`, documented as "zero if number is zero, 1.0 if number is greater than zero, -1.0 if number is less than zero".
- `fErf(x)` is a fixed 10-coefficient rational (Horner) approximation of the error function, with coefficients `1.0 / (1.0 + 0.5 * |x|)` and `1.26551223, 1.00002368, 0.37409196, 0.09678418, -0.18628806, 0.27886807, -1.13520398, 1.48851587, -0.82215223, 0.17087277`, with sign symmetry `x >= 0 ? nAns : -nAns`. Exact reproduction requires implementing these coefficients verbatim; substituting a library `erf` is a different signal and is disallowed by F1.
- Derived series, exact:
  - `fPSignal[t] = fErf( mean₃(Δohlc4)[t] / (sd_pop₃(Δohlc4)[t] · √2) )` when `sd_pop₃ > 0`, else `sign(mean₃(Δohlc4)[t])`.
  - `nPSignal[t] = mean₃( fPSignal[ t-2 .. t ] )`.
  - `ndPSignal[t] = sign( nPSignal[t] − nPSignal[t-1] )`, i.e. `+1`, `0` or `−1`.
- Warmup, derived from the pinned code because the source declares none: `ta.change(ohlc4)` is `na` at bar index 0, so the 3-value `stdev`/`sma` first exist at bar index 3 (0-based); the outer 3-value `sma` first exists at bar index 5; `nPSignal[t-1]` first exists at bar index 6, so `ndPSignal` first exists at bar index 6 and the earliest possible entry is the 7th completed bar. `max_bars_back` is not declared; official documentation states the required buffer is automatically detected, and the rule references exactly one lag, so the requirement is trivially satisfied.
- Order of strategy calls within a bar: the `short` entry statement precedes the `long` entry statement, but their conditions are mutually exclusive (`nPSignal > ndErf ≥ 0` with a negative slope versus `nPSignal < −ndErf ≤ 0` with a positive slope cannot both hold, including the default `ndErf = 0` where `nPSignal = 0` satisfies neither), so at most one order is created per bar and conflict priority is provably irrelevant.

**Entry**

- Short entry: `isStartDate and nPSignal > ndErf and ndPSignal < 0`, with `isStartDate` the constant `true` and `ndErf = 0` by default.
- Long entry: `isStartDate and nPSignal < -ndErf and ndPSignal > 0`.
- Both statements pass their condition through the `when` argument. Official first-party documentation for the v6 migration states: "The `when` parameter for order creation functions was deprecated in v5 and is removed in v6. An order is created only if the `when` condition is `true`, which is its default value." The pinned script is `//@version=5`, so `when` is live and equivalent to wrapping the call in an `if`.
- The `Strategy Arguments` table row for `Start date` corresponds to the inert `tStartDate`; it gates nothing (contradiction 2), so the effective condition is the three-part formula above with no calendar filter.
- Ties and simultaneous signals: impossible by construction (mutually exclusive conditions, one order per bar).

**Exit**

- The pinned code contains exactly two order calls, both `strategy.entry`. Censuses over the whole 9277-byte artifact: `strategy.close` 0, `strategy.close_all` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.cancel` 0, `strategy.cancel_all` 0, `strategy.risk.*` 0.
- Therefore the only exit is the opposite-direction `strategy.entry`. Official documentation for `strategy.entry` states: "By default, when a strategy executes an order from this command in the opposite direction of the current market position, it reverses that position", with the worked example that a short order of 5 shares against an open long of 5 shares "triggers the sale of 10 shares to close the long position and open a new five-share short position". With `pyramiding=0` the same single same-bar-close fill performs the close and the new open.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none. Flat state: reachable only before the first entry signal; after that the system is always 1 unit long, 1 unit short, or flat only if it has never signalled.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by the persistence of `nPSignal`'s side and slope; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1, enforced by the explicitly declared `pyramiding=0`. Official documentation: with `pyramiding` 0 "only one entry order in the same direction can be opened, and additional entry orders are rejected", and pyramiding governs orders created by `strategy.entry`, so repeated same-side signals while a position is open are rejected rather than accumulated.
- Same-direction re-entry: unreachable without an intermediate opposite-side order.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. With pyramiding 0 and mutually exclusive per-bar conditions, no repeated or same-bar entry can occur, so cooldown semantics are provably irrelevant rather than missing. The engine's separate "Order execution delay" setting is a user override whose default is 0 ticks, i.e. no delay.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy('P-Signal Strategy RVS.', precision=3, process_orders_on_close=true, pyramiding=0, commission_type=strategy.commission.percent, commission_value=0.2)`. So the code-declared values are `precision=3` (display formatting only), `process_orders_on_close=true`, `pyramiding=0`, `commission_type=strategy.commission.percent`, `commission_value=0.2`.
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `default_qty_type=strategy.fixed` and `default_qty_value=1` (v5 reference: "The default is strategy.fixed", "The default is 1"), `initial_capital=1000000` (both official pages print 1000000), `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0` (both official pages print 0), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (irrelevant: at most one open trade and no `strategy.close` call exists), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` and `use_bar_magnifier=false` (no price-dependent orders and no lower-timeframe fill data).
- Sizing: `strategy.fixed` with value 1, i.e. each entry order is 1 unit — one contract/share/lot as defined by the chart symbol — fixed and equity-independent, therefore non-compounding. Nothing in the artifact overrides the size. This is the single most important language-default dependency in the record: the sizing value is not written in the code, it is recoverable only from official first-party Pine documentation, and the exact contract multiplier the Binance instrument maps one "unit" to is `data gap`.
- Two official pages disagree on two unset defaults, and both conflicts are recorded rather than resolved: (i) `pyramiding` — the v5 language reference prints "Optional. The default is 0." while the declaration-statements page prints "The default argument is 1"; immaterial here because the pinned code sets `pyramiding=0` explicitly. (ii) `margin_long` / `margin_short` — the v5 language reference prints "Optional. The default is 0, in which case the strategy does not enforce any limits on position size", while the declaration-statements page prints "The default margin_long and margin_short arguments are 100, meaning that the strategy must cover 100% of each long and short position using its simulated account balance ... 100% margin is equivalent to 1:1 leverage" and warns that zero "effectively has infinite leverage". Materiality analysis for this rule: because size is a fixed 1 unit and never scales with equity, the two readings produce identical fills unless simulated equity falls below the notional of one base unit, i.e. only after a drawdown deep enough that a 1-unit order can no longer be 100%-collateralised (about 96% at the header window's price level against the documented 1,000,000 start capital). F3 is the gate that forces this to be pinned before any adoption.
- Direction: both sides explicit (two `strategy.entry` statements, one per side). Spot is not applicable to the short leg, so the declared market type is perpetual (see Required data).
- Nothing else is declared: `initial_capital`, `currency`, `slippage`, `margin_*`, `calc_on_*`, `close_entries_rule`, `max_bars_back` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variant and its coefficients, source price, lookback, smoothing, thresholds, comparison and sign logic, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults. The residual `underspecified` items are: the exact contract multiplier behind "1 unit" of the Binance instrument, the v5 documentation gap on the default length of `ta.change(source)`, and the `margin_long`/`margin_short` default conflict. None of the three changes the signal; the third changes tradeability only after an extreme drawdown, and the first changes notional only.

## Required data

- Instrument: BTCUSDT on Binance USDT-margined futures, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking.
- Market type: perpetual. The source explicitly runs on a margined futures venue and the rule shorts, so a margined long/short instrument is required. The artifact does not distinguish the perpetual from a dated future, which is `data gap`; it is immaterial to an OHLCV-only signal but must be pinned before any execution work.
- Spot applicability: not applicable to the short leg, because spot would require naked shorting. The long leg alone could run on spot, but that would be a modified strategy and is not proposed.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1h`, from `period: 1h`. The same header prints `basePeriod: 15m`; the pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. The `15m` field is an FMZ backtester data field, not a rule input.
- Fields used: `open`, `high`, `low`, `close` of the decision bar and of the previous decision bar (through `ohlc4` and `ta.change`). Volume is not an input: the token `volume` occurs once in the artifact and only inside the Optimization prose.
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state, and the calendar (no time gate exists).
- Point-in-time: every input at bar `t` is contemporaneous or lagged (`ohlc4[t]`, `ohlc4[t-1]`, `nPSignal[t-1]`); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage. The plotting code uses no displacement offset either (the only `offset` tokens are absent; `hline`/`plot`/`table` calls are display-only and occur 4 / 1 / 4 times respectively).
- Timestamp and timezone: bar open times of a 1-hour BTCUSDT series; because the rule compares no timestamps, no boundary convention affects trades.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. The `na` rules that do matter are the language ones: `ta.change` returns `na` on the first bar and "na values ... will produce an na result", while `ta.sma`/`ta.stdev` ignore `na` and require `length` non-`na` values — these are what fix the warmup at bar index 6.
- Funding, fee and spread needs: none specified beyond commission. Word-boundary census of the pinned 9277-byte artifact gives commission 3 (all three occurrences are the commission declaration), slippage 0, fee 0, funding 0, leverage 0, margin 0, spread 0, capacity 0, turnover 0, equity 0, open interest 0. Slippage 0 and commission 0.2% come from declaration and language default, not from measurement; spread, impact and funding are `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market order, created only by `strategy.entry`. There is no limit order, no stop order, no stop-limit and no conditional price order anywhere in the rule (0 `strategy.exit`, 0 `strategy.order`).
- Fill model: `process_orders_on_close=true` → official documentation: "the emulator fills the order immediately on the bar's close instead of waiting for the next bar's opening tick". `calc_on_every_tick` and `calc_on_order_fills` default to `false` per official documentation, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled on the same completed-bar close; the engine's "Order execution delay" override defaults to 0 ticks.
- Reversal semantics: an opposite-direction `strategy.entry` under `pyramiding=0` produces one fill that closes the open trade and opens the opposite trade at the new order's size (1 unit), per the official `strategy.entry` documentation quoted above.
- Position limits: one position at a time, 1 fixed unit per entry, `pyramiding=0`, no scaling, no grid, no martingale, no add-on.
- Leverage and margin: unset in the code; the two official pages disagree (100 = 1:1 versus 0 = unlimited), both readings recorded above with the materiality condition and gated by F3. Under either reading the rule never sizes by leverage, so it has no leverage-dependent edge; only the collateral refusal path could differ after an extreme drawdown.
- Shorting and borrow: the source assumes a margined futures venue. Borrow availability and any stock-loan analogue are not addressed → `data gap`, and spot shorting is explicitly out of scope.
- Costs: commission `strategy.commission.percent` `0.2` — official documentation: "the broker emulator now applies a commission of 1% of the transaction size to each filled order by default" for `commission_value = 1`, i.e. the same percent-of-transaction mechanism applies to *every* filled order, so 0.2% of order cash volume is charged on the entry fill and again on the closing/reversal fill. No slippage (`slippage` default 0 ticks per both official pages), no spread, no market-impact and no funding model appears anywhere in the artifact → the remaining cost legs are `data gap`; this record does not adopt a validated zero-cost assumption beyond the declared commission.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F10.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (initial capital, currency, pyramiding, commission, margin, order size, order execution delay) are not part of the pinned source; the code-declared values plus documented defaults above are the recorded strategy.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code, or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 9277-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, trade 0, trades 0, slippage 0, fee 0, funding 0, leverage 0, margin 0, spread 0, capacity 0, turnover 0, equity 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0; `profit` occurs once, in the prose sentence "with limited single profit"; `impact` occurs once, in "reduce the impact of data anomalies" (not a market-impact model); `volume` occurs once, in Optimization prose; `backtest` occurs once, inside the `/*backtest ...*/` header. There is no equity curve, no trade list, no table and no figure anywhere in the artifact, and the landing page shows none either (its own word-boundary counts for the same metrics are all 0, listed in Provenance).

What the source does report:

- Configuration only, from the pinned header: backtest start 2023-12-01 00:00:00, end 2023-12-31 23:59:59, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- Parameter defaults as listed under Signal, plus the three exposed Strategy parameters (`Cardinality`, `|ΔErf|`, `Start date`) confirmed both in the artifact table and on the public landing page.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: "effectively judges the market's statistical characteristics, captures reversal opportunities", "built on the probability distributions of statistical parameters ... incorporates more market information", and the Advantage/Risk/Optimization items quoted under Economic mechanism → unverifiable as printed and recorded as bare claims, not as evidence.
- Landing metadata read 2026-10-05: Created 2024-01-29 14:44:56, Last modified "3 years ago", Copy 0, Hits 1020, 0 comments.
- Research-computed, not printed: the header window runs from 2023-12-01 00:00:00 to 2023-12-31 23:59:59, i.e. it covers 31 calendar dates with an elapsed span of 30 days 23:59:59, which is 744 hourly bars when both endpoint hours are counted on a 24/7 market; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact, of its Pine block and of a whitespace-normalized variant; a byte-identical re-fetch of the git blob by id from the GitHub API; extraction and line-by-line comparison of the FMZ landing page's embedded Pine payload against the pinned Pine block; a whole-artifact term and word-boundary census; enumeration of `strategy.*` and `input*` call sites and of identifier occurrence counts; reading of the public FMZ landing page in a browser; and live reading of the official TradingView pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized and trade counts are all 0 occurrences, and the landing page shows no performance block either.
2. The three performance-sounding prose claims carry no sample, no metric and no baseline, so they cannot be checked as printed.
3. The only configured backtest window is 744 hourly bars (2023-12-01 00:00:00 to 2023-12-31 23:59:59, 31 calendar dates) on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. Cost model is commission-only: 0.2% per filled order, with slippage 0 by language default and no spread, impact or funding model, so any edge claim is only partially priced.
5. Sizing is not written in the code at all; it is `strategy.fixed` × 1 purely because those are Pine's documented defaults, and the contract multiplier for one "unit" of the Binance instrument is unstated (`data gap`). A consumer that assumes percent-of-equity or cash sizing would misprice every trade.
6. The strategy contains no stop loss, no take profit, no trailing stop and no time exit, while the source's own Optimization block proposes adding a stop loss — the published rule is explicitly acknowledged by its author as incomplete on risk.
7. Holding is unbounded: with no time exit, a stale position persists indefinitely while `nPSignal` stays on one side of the dead band with the same slope sign.
8. After the first signal the system is long, short or never-started: no drawdown control, no cash-fallback rule, no volatility targeting.
9. Prose claims entries trigger on a zero crossing; the code requires the signal to be beyond the dead band *and* moving back (recorded contradiction 1), so the actual behaviour is materially different from the description a reader would take away.
10. Prose claims Observation time controls the strategy start time; the `tStartDate` input is dead and the rule has no start gate (recorded contradiction 2), so the strategy trades the entire available history rather than the window a reader would expect.
11. The artifact's own Strategy Arguments table prints the ΔErf default as `false` while the code declares numeric 0 (recorded contradiction 3).
12. Default `ndErf = 0` means the dead band is empty at defaults, so the "dead band to reduce trading frequency" described in the prose is inactive out of the box; entries then require only a nonzero standardized change with the right slope, which maximizes signal frequency.
13. `ta.stdev` runs with `biased=true` (population estimator) by default; any reconstruction that uses the n−1 sample estimator changes every `fPSignal` value and therefore every trade.
14. `fErf` is a pinned rational approximation with ten hardcoded coefficients, not a library error function; using `math.erf` or a different approximation yields a different signal.
15. The zero-variance branch (`nStDev == 0` → `sign(nSma)`) is defined only by the code; no prose, help text or comment explains it, so its behaviour on flat windows is a code-only edge case that F1 must reproduce.
16. The v5 language reference does not print a default for the one-argument `ta.change(source)` overload, leaving a strategy-critical transform documented only indirectly (the current reference prints 1).
17. Two official TradingView pages disagree on the `pyramiding` default (0 versus 1) and on the `margin_long`/`margin_short` defaults (0 versus 100); both conflicts are recorded above rather than resolved by preference.
18. The source has no volume, volatility, spread or regime filter despite the Optimization block proposing them, so the rule is presented as a bare single-statistic template.
19. The error-function map saturates, so beyond a few standardized deviations the signal stops distinguishing degrees of extremity; the mechanism therefore has a built-in information ceiling.
20. The full source is behind a login on the FMZ landing page and is publicly reachable only through a third-party mirror repository, leaving a single point of provenance (the embedded landing payload corroborates it but is not an immutable artifact).
21. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; only the script's own MPL-2.0 notice is printed inside the block.
22. Authorship is layered and unverified: the mirror records `Author: ChaoZhang`, the code prints `© Kharevsky`, and neither identity is independently confirmed; peer-review status is not stated in source.
23. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows creation and a relative modification label that are mutually inconsistent.
24. FMZ landing statistics (Copy 0, Hits 1020, 0 comments as read 2026-10-05) show no community adoption signal, and no third-party study of this exact artifact was identified.
25. The base-K-line field `basePeriod: 15m` sits next to a `1h` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
26. No independent replication, no competing study and no contrary external evidence specific to this artifact was found; absence of contrary literature is not evidence of robustness.
27. Distributional fragility: the statistic is a mean-over-standard-deviation ratio over a 3-change window, which is noisy by construction and assumes local scale stability; in a heavy-tailed or volatility-clustering window the sign can flip without any economic event, producing whipsaw reversals that each pay commission twice.
28. Because reversal is the only exit, every side change pays the full 0.2% commission on both the closing and the opening leg, so trade frequency is directly cost-amplifying and the default-empty dead band (item 12) works against that.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, the identical `fPSignal` / `nPSignal` / `ndPSignal` series to floating-point tolerance and an identical ordered list of entry bars and sides, including the first possible entry at bar index 6, the `biased=true` population standard deviation, the verbatim ten erf coefficients, the `nStDev == 0` branch, the `na` propagation rules and the 1-bar reading of `ta.change`. Action: any mismatch means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`ohlc4[t]`, `ohlc4[t-1]`, `nPSignal[t-1]`), with zero occurrences of future bars, negative shifts, `timenow`, session recalculation, `calc_on_order_fills=true`, `calc_on_every_tick=true`, `use_bar_magnifier=true` or any lower-timeframe request. Action: any future reference or intrabar dependence found ⇒ NOT_LOSSLESS, close the record.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the executing engine must confirm all five recorded language defaults end to end — order size exactly 1 unit (fixed, equity-independent), slippage 0 ticks, commission 0.2% of order cash volume on *both* the entry and the closing/reversal fill, fill price equal to the decision bar's close, and same-direction entries rejected while a position is open. Action: fail if any of the five differs from the record, or if the `margin_long`/`margin_short` default resolves in a way that can refuse a 1-unit entry before a 96% drawdown; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold (research-defined): apply the declared 0.2% commission plus 0 / 1 / 2 / 5 / 10 bps per side and, for the perpetual, a funding accrual leg; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side. Action: fail ⇒ the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F5 — Parameter perturbation.** Threshold (research-defined): sweep `nPoints` over 4, 5, 8, 13, 21, 34 and `ndErf` over 0, 0.05, 0.1, 0.2, 0.4 with everything else frozen; fail if the sign of net return over the full sample flips for the published cell (4, 0) or if fewer than half of the 30 cells produce positive net return. Action: fail ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail ⇒ the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F7 — Placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 random side-assignment sequences that preserve the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution. Action: fail ⇒ no evidence that the erf timing carries information.
- **F8 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1h BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail ⇒ reject for adoption; do not rescue by re-tuning.
- **F9 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side. Action: fail ⇒ single-asset overfit diagnosis.
- **F10 — Capacity and liquidity.** Threshold (research-defined): fail if the notional of one base unit exceeds 1% of the trailing 30-day median hourly traded volume of the instrument. Action: fail ⇒ capacity-capped, record the ceiling and block any size scaling (sizing is fixed, so scaling would already be a rule change).
- **F11 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F5 × F9 cell family; fail if the published cell does not survive. Action: fail ⇒ treat the published configuration as one draw among many, no adoption.
- **F12 — Risk-layer ablation.** Threshold (research-defined): because the source contains no stop, take-profit or time exit, measure maximum drawdown and the longest single holding period; fail if maximum drawdown exceeds 40% on the frozen sample or if any single holding exceeds 30 days (720 hourly bars). Action: fail ⇒ document the unbounded-exposure failure and keep research-only.
- **F13 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `nPoints 4`, `ndErf 0`, the verbatim ten-coefficient erf approximation, the `biased=true` population standard deviation, the 3-change and 3-average windows, the sign-and-dead-band entry rule, the reversal-only exit, `pyramiding 0`, fixed 1-unit sizing, `process_orders_on_close` same-bar-close fills, 0.2% commission per filled order, the single `1h` timeframe and the BTCUSDT perpetual instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1h`, so the instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `open`, `high`, `low`, `close` of 1-hour bars, all available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency, and no calendar gate exists to interact with the 24/7 clock.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal — although funding accrual is also absent from the cost model, which for a strategy that can hold a perpetual position indefinitely is a real carry cost (`data gap`).
- Shorting requires a margined instrument; the source already uses a futures venue, so the perpetual is the natural target and spot is out of scope for the short leg.
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual (never mentioned, `data gap`), the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and liquidity or market-impact differences for a one-unit order (`data gap`).
- Timestamps are exchange-defined UTC hourly candles on Binance; because no rule element compares timestamps, the record does not depend on any boundary convention.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency, funding or fill-failure model; no missing-data handling; no capacity statement; no exact contract multiplier for one unit; no performance output.
- `underspecified`: the exact Binance contract behind "1 unit"; the v5 documentation gap on the default length of `ta.change(source)`; which of the two conflicting official statements about `margin_long`/`margin_short` defaults the target engine implements; whether the FMZ backtest engine's `basePeriod: 15m` field influenced any published number (the script itself makes no cross-timeframe call).
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity and forward performance.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review and a layered, unverified authorship; the landing hides the full source behind a login.
- Reproducibility limitation: because FMZ hides the full source and prints no results, the only immutable, publicly auditable artifact is the mirror at the pinned SHA; the landing's embedded payload corroborates it line by line but is neither immutable nor versioned.
- Identification limitation: the rule is a purely price-difference statistic with no control for volatility regime, volume or funding, so nothing in the source separates a mean-reversion effect from a beta or from cost-amplified whipsaw.
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust, and Copy 0 suggests no demonstrated community reuse.
- Incremental-write check: this is the first record in the repository for this source identity after the 2026-10-04 pool reset, no open research PR shares it, and no Wiki Brain page exists for it, so this is not ordinary duplicate material.
- A three-item contradiction set is recorded in frontmatter. All three are prose-versus-code or table-versus-code conflicts inside one artifact, and in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous; two of them do leave a naive reader's mental model of the rule wrong, which is why `contested: true` is set.
- Two additional conflicts live in the official documentation itself rather than in the source (the `pyramiding` default and the `margin_*` defaults) and are recorded under Signal instead of being resolved by preference.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and its verification script.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family (short-horizon mean reversion, standardized/threshold signals), by execution and cost discipline, or by overfitting control rather than by source identity; none of them shares the P-Signal source, the erf dead-band signal construction, or this exact BTCUSDT 1-hour single-pair scope:

- [[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]]
- [[quant/btc-weekly-range-sweep-reclaim-mean-reversion-2026-09-14]]
- [[quant/crypto-rolling-close-quantile-threshold-source-code-audit-2026-09-14]]
- [[quant/crypto-inj-dual-rsi-dca-profit-armed-exit-source-code-audit-2026-09-15]]
- [[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]
- [[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]]
- [[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]

## Sources

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `P-信号反转策略P-Signal-Reversal-Strategy.md`; the complete primary source read end to end on 2026-10-05, SHA-256 `35c6997c7045d8295f00f86cf0fb08691fb502c86c3dcb30c3183fb5617979bf`; the same bytes were re-fetched from the GitHub API by blob id `a0bfbdf924c3f5b8fb20d4ca0b251f1da6ed7a4b`.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/P-%E4%BF%A1%E5%8F%B7%E5%8F%8D%E8%BD%AC%E7%AD%96%E7%95%A5P-Signal-Reversal-Strategy.md — percent-encoded form of the same pinned file, opened successfully in a browser on 2026-10-05.
- https://www.fmz.com/strategy/440338 — FMZ landing page, read 2026-10-05; confirms title, badge, author account, creation timestamp, statistics, English description, backtest header, the three exposed parameters, the login gate, the absence of any performance block, and an embedded Pine payload that matches the pinned Pine block line for line after escape normalization.
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy — official first-party language reference used only for declaration-parameter semantics and defaults (`pyramiding` 0, `default_qty_type` `strategy.fixed`, `default_qty_value` 1, `initial_capital` 1000000, `currency` `currency.NONE`, `slippage` 0, `commission_*` defaults, `process_orders_on_close` default false, `close_entries_rule` "FIFO", `calc_on_order_fills` / `calc_on_every_tick` defaults false, `margin_*` printed as 0, `max_bars_back` auto-detection, `use_bar_magnifier` default false).
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry — official first-party documentation used for pyramiding rejection of same-direction entries and for opposite-direction entries reversing the position.
- https://www.tradingview.com/pine-script-docs/language/declaration-statements/ — official first-party documentation used for the `process_orders_on_close = true` fill semantics ("fills the order immediately on the bar's close"), the once-per-bar execution rule when the calculation flags are false, `initial_capital` 1000000, `slippage` 0, and for the conflicting `pyramiding` (1) and `margin_long` / `margin_short` (100) default statements recorded above.
- https://www.tradingview.com/pine-script-docs/concepts/strategies/ — official first-party documentation used for the commission mechanism ("applies a commission of ... each filled order") and for the Strategy Tester / strategy-properties context.
- https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/ — official first-party documentation used for the `when` parameter semantics ("deprecated in v5", "An order is created only if the `when` condition is `true`") and its removal in v6.
- https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}stdev , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}sma , https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}change , https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}sign — official first-party documentation used for `biased=true` population standard deviation, the simple-average definition, the change/na rules (with the v6 reference cited only where it prints the default `length = 1` that the v5 entry omits), and the sign function.
