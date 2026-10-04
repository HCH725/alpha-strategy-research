---
schema: strategy-research-record-v1
title: LazyBear Wave Trend wt1/wt2 oscillator cross system on BTCUSDT 1h bars
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
  - https://www.fmz.com/strategy/435853
  - https://www.tradingview.com/pine-script-reference/v4/
  - https://www.tradingview.com/pine-script-reference/v6/
  - https://www.tradingview.com/pine-script-docs/language/declaration-statements/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
  - https://www.tradingview.com/support/solutions/43000628599-strategy-properties/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Both language versions of the Strategy Logic state that a WT1 cross under WT2 goes short, but the pinned code's short entry is commented out and the crossunder instead closes the long, so the executable system is long-only."
  - "Both language versions state that WT1 and WT2 are generated from the wave-trend line by simple moving averages, but the pinned code sets wt1 equal to tci directly, which is the EMA output with no smoothing, and only wt2 is sma of wt1 over 4 bars."
  - "The artifact exposes six date-range inputs plus a Show Date Range input, computes start and finish timestamps and comments that window() creates a function 'within window of time', but window() is defined to return true unconditionally, so no order is ever time-gated and all seven inputs are inert."
  - "The prose says the strategy identifies overbought and oversold market conditions to generate trade signals, but the four overbought and oversold level inputs are referenced only by plot() calls and never by any entry, exit or filter condition; the sole trigger is the wt1/wt2 cross."
---

# LazyBear Wave Trend wt1/wt2 oscillator cross system on BTCUSDT 1h bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/fmzquant/strategies
- Full commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, committer date 2025-04-30T03:10:28Z, subject `update`). This was confirmed as the repository head at research time by an unauthenticated GitHub commits API call, which returned the same SHA for `commits?per_page=1`.
- Exact file path: `基于波浪趋势的交易策略The-Wave-Trend-Trading-Strategy-Based-on-LazyBear.md` (the non-ASCII filename is preserved verbatim; percent-encoded blob URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8E%E6%B3%A2%E6%B5%AA%E8%B6%8B%E5%8A%BF%E7%9A%84%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5The-Wave-Trend-Trading-Strategy-Based-on-LazyBear.md )
- Relevant source URL recorded inside the artifact: https://www.fmz.com/strategy/435853

Primary-source checksums pinned 2026-10-05 from a clone of that commit:

- File 8659 bytes, SHA-256 `d74eb1d600829ff58b5225d61ce3318ef09861d26df3729eb7199b9744545edd`, 7209 characters, 214 newline characters, file ends with a newline.
- Whitespace-collapsed variant 6068 characters, SHA-256 `e14c4c56912fc147fc74291c2fd44d508918e9680c80b31ce89acc92ba0b71bd`.
- The fenced Pine block alone: 67 lines, 2673 characters and 2673 bytes, SHA-256 `80604eb5ca86f17d50208a480cc37faa5a8161584572e0c8fddca3bc33117b0c`.
- A byte-level fetch of the raw file at that same SHA returned HTTP 200 with 8659 bytes and SHA-256 `d74eb1d600829ff58b5225d61ce3318ef09861d26df3729eb7199b9744545edd`, identical to the local pin, so the mirror copy read and the remote blob at the pinned SHA agree.

Artifact structure as printed: `> Name` (The Wave Trend Trading Strategy Based on LazyBear, with the mirrored Chinese title 基于波浪趋势的交易策略), `> Author` = ChaoZhang, `> Strategy Description` (a Chinese section set and an English section set inside one `[trans]` block), `> Strategy Arguments` table of thirteen inputs, `> Source (PineScript)` fenced block preceded by an FMZ `/*backtest ...*/` header, `> Detail` = https://www.fmz.com/strategy/435853, `> Last Modified` = 2023-12-19 12:07:14.

Licence and rights: the pinned Pine block carries no licence header and no copyright notice. It opens with an author-credit comment naming LazyBear and a request that anyone using the code in its original or modified form drop the author a note. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

FMZ landing page fetched directly over unauthenticated HTTPS on 2026-10-05 with a desktop browser user agent (HTTP 200, 782720 bytes): document title `The Wave Trend Trading Strategy Based on LazyBear | FMZ`, `og:title` identical, meta description beginning with the English Overview sentence, category `Common strategy`, `Created : 2023-12-19 12:07:14`, `Last modified : 3 years ago`, `Copy : 1`, `Hits : 1596`, author account ChaoZhang, and the literal string `Login to view full source` present in the rendered UI. Two provenance consequences are recorded rather than smoothed over:

- The rendered UI gates the source behind login, but the HTML served to an unauthenticated client does embed the Pine source text: within that payload `ap = hlc3` occurs once, `wt2 = sma` once, `strategy.entry` twice, `window()` three times and `process_orders_on_close` once. A line-by-line comparison of the 29-line payload span from `ap = hlc3` through the commented short-entry line against the same 29 lines of the pinned Pine block matched on content; the only differences were the payload's escaped newline and quote characters on the three lines that contain quoted string literals, plus a trailing React-Router session-data tail appended to the final line. The landing payload is therefore corroborating but not immutable, so the pinned GitHub SHA remains the only immutable auditable artifact.
- The landing page exposes no performance material: `Net Profit`, `net profit`, `Sharpe`, `ROI`, `Max Drawdown`, `win rate`, `Profit Factor`, `Total Closed Trades`, `Strategy Tester` and the `**backtest**` image marker each occur zero times in the served HTML.

FMZ backtest header printed verbatim inside the pinned artifact:

```text
start: 2023-11-18 00:00:00
end: 2023-12-18 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
```

Provenance gaps (stated, not repaired): no DOI, no version tag, no repository for the rule itself, no test suite, no issue tracker entry, no peer-review statement and no performance output anywhere; peer-review status is not stated in source.

Pre-write dedup (2026-10-05, run at Asia/Taipei 03:18): a hidden-inclusive search of the whole working tree for `wave trend`, `WaveTrend`, `LazyBear`, `435853`, `波浪趋势` and `T!M - Wave` returned 0 matching files; the loose probe `wt1` matched only four files, all of them compressed objects inside `.git/objects`, and no tracked Markdown file; the positive control `gann` matched 13 files, so the scan is live. `git ls-remote --heads origin 'research/*'` and `gh pr list --state open` both returned nothing, so there is no open `research/*` branch and no open PR. `origin/main` was at `c1b54c3` with a clean tracked worktree and contains exactly 1 strategy record after the 2026-10-04 pool reset, `gann-hilo-activator-state-flip-trend-btcusdt-daily-2026-10-05.md`. Five-axis distinction against that record: mechanism (momentum-oscillator level cross versus displaced band state flip), signal construction (EMA/SMA envelope-ratio oscillator crossing its own 4-bar mean versus a two-state close-beyond-band machine), horizon (1h versus 1d), direction (long-only versus two-sided) and parameterization all differ, and the source identity differs (FMZ 435853 versus FMZ 427070). Repository history was also scanned across all refs: the only mechanism-adjacent hit was `tradingview-crypto-squeeze-momentum-total-market-filter-2026-09-18.md`, which credits LazyBear's Squeeze Momentum indicator, a different indicator, a different source and a different universe, so it is not a duplicate.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview, as printed: "This is a trading strategy based on LazyBear's Wave Trend indicator. The strategy identifies market sentiment through computing the wave trend of price fluctuations, and makes long and short decisions accordingly."
- Strategy Logic, as printed: (1) calculate the average price (AP), the exponential moving average of AP (ESA) and the exponential moving average of the absolute price movement (D); (2) use ESA and D to calculate the Volatility Index (CI); (3) feed CI through an exponential moving average to generate the Wave Trend line (WT); (4) process WT into WT1 and WT2 using simple moving averages; (5) "When WT1 crosses over WT2, it triggers the golden cross and goes long. When WT1 crosses under WT2, it triggers the death cross and goes short."
- Advantage Analysis, as printed: identifies market sentiment clearly; simple trading logic on golden and death crosses; customizable parameters; flexibility to add further filters such as a trading time window.
- Risk Analysis, as printed: "As a trend following strategy, it can generate many false signals during range-bound markets"; "The lagging nature of WT may cause missed turns"; "Default parameters may not suit all products and cycles"; and, verbatim, "No stop loss mechanism, holding period can be very long".
- Optimization Directions, as printed: tune WT parameters; use different parameter sets per cycle; add indicators like volume or volatility for confirmation; add stop loss and take profit; enrich trading logic like pyramiding or grid trading; explore machine-learning features.
- Summary, as printed: a simple wave-trend-following template with room for improvement in sensitivity and stability, which "also needs additional filters and logic to avoid false signals".

Three of those printed statements contradict the pinned code and are recorded in frontmatter `contradictions`: the short-side claim, the WT1/WT2 smoothing claim, and the overbought/oversold gating claim. The source's own Risk item 4, "No stop loss mechanism", agrees with the code and is therefore not a contradiction.

### Research interpretation

Falsifiable mechanism hypothesis: over a short trailing window, the typical price of BTC tends to sit away from its own exponentially weighted mean by an amount that scales with recent dispersion, so the normalized quantity `(hlc3 - EMA(hlc3,10)) / (0.015 * EMA(|hlc3 - EMA(hlc3,10)|, 10))` is a bounded, mean-reverting oscillator; smoothing it with a 21-bar EMA and comparing it with its own 4-bar simple average converts level information into a direction-of-travel test, so a cross is read as a change in the sign of short-horizon drift in the typical price. Candidate behavioural or structural channels are herding around a visibly mean-reverting intraday range in a 24/7 market with no closing auction, and slow diffusion of directional information across hourly bars with no session boundary to reset it. This is a ported technical-analysis hypothesis: the source supplies no economic rationale and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Regime / oscillator: `wt1` (the 21-bar EMA of the normalized dispersion ratio) and `wt2` (its 4-bar simple average), forming a self-referential fast/slow pair rather than a price/indicator pair.
- Entry signal: `crossover(wt1, wt2)`, a long entry.
- Confirmation filter: none. `window()` is defined to return `true`, so the date-range inputs provide no filter, and the four overbought/oversold levels are plot-only. The source explicitly lists adding volume or volatility confirmation as future work.
- Risk / exit: none. The only exit is `strategy.close` on `crossunder(wt1, wt2)`.

No component is assumed to contribute alpha; ablation is required by the falsification plan. Because `wt1` and `wt2` are both functions of the same series, the system is a same-series fast/slow cross rather than an indicator-versus-price cross, which mechanically raises cross frequency relative to an indicator-versus-price design; that property is derived from the pinned code, not asserted by the prose.

## Signal

Everything below is read from the pinned Pine block and from the official TradingView references cited in `## Sources`. Nothing in this section is `research-proposed`.

**Formation timestamp and tradability**

- Decision series: completed `1h` bars of the pinned instrument (the `period: 1h` value in the pinned backtest header).
- Inputs at decision bar `t`: `high`, `low` and `close` of bar `t` through the recursive history of the two EMA chains, i.e. `hlc3` values back to the seed window.
- Order timing: market orders created by `strategy.entry` and `strategy.close`; the declaration sets `process_orders_on_close=true`, and the official v4 reference states that when this is true the broker emulator executes market orders created on a bar's close "before the next bar's open". This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Intra-bar recalculation: `calc_on_every_tick=false` is declared verbatim. Official documentation states the default is `false` and that `false` means the strategy executes strictly once per bar, on the closing tick. `calc_on_order_fills` is not declared and the official default is `false`, so there is no recalculation after a fill.
- Timezone: no order condition references wall-clock time. `start` and `finish` are computed from `timestamp(...)` but are never read by any order, and `window()` returns `true`, so no time-zone boundary can alter a trade.

**Lookback, formulas and warmup**

- `Channel Length` is declared verbatim as `n1 = input(10, "Channel Length")` to 10. `Average Length` is declared verbatim as `n2 = input(21, "Average Length")` to 21.
- The indicator chain, verbatim from the pinned block: `ap = hlc3`; `esa = ema(ap, n1)`; `d = ema(abs(ap - esa), n1)`; `ci = (ap - esa) / (0.015 * d)`; `tci = ema(ci, n2)`; `wt1 = tci`; `wt2 = sma(wt1,4)`.
- `hlc3` is defined by the official v4 reference as "a shortcut for (high + low + close)/3".
- `ema(source, length)` is defined by the official v4 reference as `EMA = alpha * x + (1 - alpha) * EMA[1]` with `alpha = 2 / (y + 1)`, and the reference prints the equivalent seeding implementation in which the value is `sma(src, length)` while the previous EMA value is `na` and the alpha recursion afterwards. So the first non-`na` EMA value sits at bar index `length - 1` (0-based) and equals the simple average of the first `length` inputs.
- `sma(source, length)` is defined by the official v4 reference as the sum of the last `length` values of the source divided by `length`.
- The oscillator constant `0.015` is a literal in the pinned code and is not an input.
- Warmup, derived from the pinned code and the official seeding rule because the source declares none: `esa` first exists at bar index 9; `d` first exists at bar index 18 (its input is `na` until bar 9 and the seed then needs 10 values); `ci` first exists at bar index 18; `tci` first exists at bar index 38; `wt1` first exists at bar index 38; `wt2` first exists at bar index 41; `crossover(wt1, wt2)` needs both series on the current and previous bar, so the earliest possible long-entry decision is bar index 42, the 43rd completed bar. `max_bars_back = 200` is declared verbatim, which is well beyond that chain.
- A division edge case is recorded, not repaired: if `d` evaluates to 0 the quotient `ci` is undefined. The official operators page, the FAQ pages and the errors overview state no division-by-zero value, so the behaviour on that path is a `data gap`. Reaching it requires `hlc3` to be identical to its own 10-bar EMA across a whole 10-bar EMA window, i.e. a perfectly flat 10-hour typical price; no such bar is asserted to exist and none is asserted not to.

**Entry**

- Long entry: `longCondition and window()` where `longCondition = crossover(wt1, wt2)` and `window()` is defined verbatim as `window()  => true`, so the condition reduces to the crossover alone.
- Short entry: the only short call in the artifact, `strategy.entry(id="Short Entry", long=false, when=shortCondition)`, is commented out. It is not executable. The active code contains exactly one `strategy.entry` and it passes `long=true`, so direction is long-only by construction and no short order can be produced.
- Conflict priority: `crossover` requires `wt1 > wt2` on the current bar and `crossunder` requires `wt1 < wt2` on the current bar, so the two conditions are mutually exclusive and an entry and an exit can never be requested on the same bar. Proof of this exclusivity makes conflict priority provably irrelevant rather than unspecified.
- Ties and simultaneous signals: a second same-direction `strategy.entry` while a long is open is reachable only if `wt1` equals `wt2` exactly on an intervening bar, so that neither cross function fires, and the series then separates upward. Under `pyramiding = 0` the official reference states that additional same-direction entry orders are rejected, so the open size is unchanged on that path.

**Exit**

- The exit is `strategy.close("Long Entry", when=shortCondition and window())`, which with `window()` constant reduces to `crossunder(wt1, wt2)`.
- The official v4 reference states that `strategy.close` is a command to exit from the entry with the specified ID, uses a market order, and "If there are no open entries with the specified ID by the moment the command is triggered, the command will not come into effect", so a crossunder while flat is a no-op.
- Censuses over the whole artifact: `strategy.entry` 2 (one active, one commented out), `strategy.close` 1, `strategy.exit` 0, `strategy.close_all` 0, `strategy.stop` 0, `strategy.limit` 0, `strategy.order` 0, `strategy.cancel` 0.
- Therefore the only exit is the crossunder close, and the trade reverses to cash, not to a short.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none. The source's own Risk Analysis states "No stop loss mechanism, holding period can be very long", which agrees with the code.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by how long `wt1` stays above `wt2`; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1, enforced by `pyramiding = 0` declared verbatim.
- Same-direction re-entry: after `strategy.close` flattens the position, the next `crossover` places a fresh `strategy.entry`. The official concepts page states that once the number of open trades reaches the pyramiding limit the strategy does not execute new orders from subsequent calls "until at least one of those trades closes", and the official Help Center states that when pyramiding is disabled the strategy can only open one long or short position even if entry conditions are met. Both are quoted here rather than paraphrased into a choice.
- Cooldown: none. Pine's strategy framework exposes no cooldown parameter, and the official Help Center enumerates the strategy properties as Initial Capital, Base Currency, Order Size, Pyramiding, Commission, Verify Price For Limit Orders, Slippage, Margin, Recalculate and Fill orders, with no cooldown entry. The artifact declares no `strategy.risk.*` restriction either. Cooldown is therefore explicit absence rather than an unspecified field.

**Parameters, sizing and pyramiding**

- All strategy inputs are declared in source with these defaults: `From Month 1`, `From Day 1`, `From Year 2021`, `Thru Month 1`, `Thru Day 1`, `Thru Year 2112`, `Show Date Range true`, `Channel Length 10`, `Average Length 21`, `Over Bought Level 1 60`, `Over Bought Level 2 53`, `Over Sold Level 1 -60`, `Over Sold Level 2 -53`. Seven of them are inert, as recorded in frontmatter `contradictions`.
- The pinned declaration reads verbatim: `strategy(title="T!M - Wave Trend Strategy", overlay = false, precision = 8, max_bars_back = 200, pyramiding = 0, initial_capital = 1000, currency = currency.NONE, default_qty_type = strategy.cash, default_qty_value = 1000, commission_type = "percent", commission_value = 0.1, calc_on_every_tick=false, process_orders_on_close=true)`.
- Sizing: `default_qty_type = strategy.cash` with `default_qty_value = 1000`, which the official v4 reference defines as "amount of cash in currency of the symbol" converted into quantity, so each entry order is 1000 units of the symbol currency. `initial_capital = 1000`, so the first entry deploys the whole initial balance. Because the order size is a constant cash amount and not a percentage of equity, sizing is fixed, not compounding; this is explicit, not inferred.
- Account currency: `currency = currency.NONE`, which the official v4 reference defines as "Unspecified currency". The residual reporting currency is `data gap`; it does not change the order quantity, which is defined in symbol currency by `strategy.cash`.
- Pyramiding: `pyramiding = 0`. The official v4 and v6 references both state: the parameter is the maximum number of entries allowed in the same direction, and if the value is 0, only one entry order in the same direction can be opened and additional entry orders are rejected. The references also disagree about the parameter's default (the v4 and v6 references print 0, the declaration-statements page prints 1), which is irrelevant here because the artifact pins 0 explicitly.
- Commission: `commission_type = "percent"` with `commission_value = 0.1`, i.e. 0.1 percent of the cash volume of each order. The official v4 reference lists `strategy.commission.percent` as "a percentage of the cash volume of order"; the artifact passes the equivalent bare string.
- Slippage: not declared. The official declaration-statements page states that if the `slippage` argument is 0, which is the default, the strategy fills orders at their expected prices without simulating any slippage. Recorded as source-declared-by-language-default, not as a research choice.
- Leverage and margin: `margin_long` and `margin_short` are absent; the official v4 reference states the default value for both is 100, i.e. 100 percent margin and 1:1 leverage, so the source assumes no borrowed funds. Recorded as source-declared-by-language-default.
- Irrelevant-by-language settings: `close_entries_rule` defaults to `FIFO` and `backtest_fill_limits_assumption` defaults to 0; with a single open trade and no limit or stop orders, neither can change a fill.
- Direction: long-only, with the short side disabled by commented-out code. Spot is therefore applicable and no naked shorting is required (see Required data).

**Reconstruction status**

Every field required to replay the rule — indicator variant, source prices, lookbacks, smoothing method, the normalization constant, thresholds, comparison semantics, state logic, conflict priority, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe and warmup — is explicit in the pinned source or in the official reference. Two boundaries remain and are recorded rather than chosen: the exact-tie wording of `crossover` and `crossunder` across reference editions (see F1 and Limitations), and the division-by-zero value of `ci` when `d` is 0. Neither is filled with `research-proposed`.

## Required data

- Instrument: BTCUSDT on Binance USDT-margined futures, taken verbatim from the pinned header `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. Single pair, single instrument, no basket, no ranking.
- Market type: the source pins a margined futures venue. Because the executable rule is long-only, spot is also directly applicable and no naked shorting is required; the artifact does not distinguish the perpetual from a dated future, which is `data gap` and is immaterial to an OHLCV-only signal but must be pinned before any execution work.
- Spot applicability: applicable to the full rule as written, since there is no short leg.
- Venue: Binance only. No cross-venue state, no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1h`, from `period: 1h`. The same header prints `basePeriod: 15m`; the pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align.
- Fields used: `high`, `low` and `close` of the decision bar and of the bars in the two EMA seed windows and the 4-bar SMA window, combined as `hlc3`. `volume` occurs once in the artifact and only inside the Optimization prose; `open` occurs zero times as an identifier.
- Fields not required and not used, each absent from the pinned artifact by word-boundary census: `open interest` 0, `mark price` 0, `funding` 0, `leverage` 0, `margin` 0, `spread` 0, `market impact` 0, `latency` 0, `capacity` 0, `turnover` 0, `liquidation` 0, `crypto` 0, `bitcoin` 0, `ethereum` 0, `perpetual` 0. Also absent by identifier count: `strategy.exit` 0, `strategy.close_all` 0, `strategy.order` 0, `strategy.cancel` 0, `request.` 0, `security(` 0, `varip` 0, `timenow` 0, `slippage` 0, `margin_long` 0, `margin_short` 0, `use_bar_magnifier` 0.
- Point-in-time: every input at bar `t` is contemporaneous or lagged (`hlc3` at `t`, plus the EMA and SMA histories ending at `t` and the one-bar lookbehind inside the cross functions); there is no future reference, no negative shift, no future extrema, no full-sample normalization, no `timenow` and no `security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: no order condition reads wall-clock time, so no boundary convention can alter a trade; the inert `timestamp(...)` expressions are recorded as contradiction 3.
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here.
- Funding, fee and spread needs: commission is source-declared at 0.1 percent of order cash volume; slippage is source-declared-by-language-default at 0 ticks. Funding, spread, market impact, borrow and capacity are not specified anywhere → `data gap`, never a modeled zero.

## Execution assumptions

Source-declared (quoted or read from the pinned declaration and from the official references):

- Order type: market order, created only by `strategy.entry` and `strategy.close`. There is no limit order, no stop order and no conditional order anywhere in the rule, so `backtest_fill_limits_assumption` and Verify Price For Limit Orders are provably irrelevant.
- Fill model: `process_orders_on_close=true` fills market orders created on the bar's close before the next bar's open; `calc_on_every_tick=false` gives exactly one evaluation per completed bar; `calc_on_order_fills` defaults to `false`. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled within the same completed-bar close.
- Exit semantics: `strategy.close` closes the whole trade identified by the entry ID at that bar's close, and is inert when no such trade is open.
- Position limits: one position at a time; 1000 units of symbol cash per entry; `pyramiding = 0` forbids adding; no scaling, grid or martingale layer.
- Leverage and margin: absent from the declaration; documented default is 100 percent margin, i.e. 1:1, so the source assumes no borrowed funds and therefore no dependency on unsupported leverage effects.
- Shorting and borrow: there is no short leg, so no borrow or short-availability assumption exists.
- Costs: commission 0.1 percent per filled order is declared; slippage 0 ticks is source-declared-by-language-default. Spread, market impact and perpetual funding accrual are not modeled anywhere in the artifact → `data gap`. The source prints no result, so no cost-embedded claim exists to adopt.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F9.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Cost-model scope of the declared commission: the official Help Center states that commission is applied on both entries and exits and that when a percentage is used the calculated commission varies with the value of the transaction. Recorded so the 0.1 percent figure is not read as entry-only.
- Scout-vs-source split: every item above marked source-declared comes from the pinned declaration, the pinned code or official first-party TradingView documentation. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 7209-character artifact: `sharpe` 0, `drawdown` 0, `cagr` 0, `return` 0, `win rate` 0, `annualized` 0, `profit factor` 0, `leverage` 0, `margin` 0, `funding` 0, `capacity` 0, `turnover` 0, `spread` 0, `market impact` 0, `latency` 0, `open interest` 0, `liquidation` 0. `profit` occurs 2 times and both are the prose phrase "take profit"; `trade` occurs 1 time and `trades` 1 time, both prose; `stop loss` occurs 3 times and all three are prose; `commission` occurs 0 times as a standalone word because the declaration uses the identifiers `commission_type` and `commission_value`, each of which occurs once; `slippage` occurs 0 times in any form. There is no `**backtest**` image block, no equity curve, no trade list, no table and no figure anywhere in the artifact.

What the source does report:

- Configuration only, from the pinned header: backtest start 2023-11-18 00:00:00, end 2023-12-18 00:00:00, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`.
- The thirteen input defaults and the pinned declaration, listed under Signal, confirmed both in the artifact table and on the public landing page.
- Landing metadata read 2026-10-05: Created 2023-12-19 12:07:14, Last modified "3 years ago", Copy 1, Hits 1596.
- Landing performance census: `Net Profit`, `Sharpe`, `ROI`, `Max Drawdown`, `Profit Factor`, `Total Closed Trades` and `Strategy Tester` each occur 0 times in the served HTML, so no third-party-visible result exists to quote.
- Research-computed, not printed: the header window spans exactly 30 calendar days, i.e. roughly 720 hourly bars on a 24/7 market; this is our arithmetic on the printed dates and must not be read as a source-reported sample size.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact and of its Pine block, a whitespace-normalization digest, extraction and line counting of the Pine block, a whole-artifact term and word-boundary census, enumeration of `strategy.*` and other identifier occurrences, a raw-blob fetch at the pinned SHA, reading of the public FMZ landing page over unauthenticated HTTPS, a line-by-line comparison of the landing payload span against the pinned block, rendering of the official TradingView v4 and v6 reference manuals, the declaration-statements and strategies documentation pages, the strategy-properties Help Center article and the migration guides, and record-side enumeration of the printed header values. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers: `sharpe`, `drawdown`, `cagr`, `return`, `win rate` and `annualized` are all 0 word-boundary occurrences, so there is nothing to reproduce.
2. The landing page also prints no performance section at all, so no third-party-visible result can be checked either.
3. The only configured backtest window is exactly 30 days (2023-11-18 to 2023-12-18) on a single instrument, with no train/test split, no out-of-sample section and no walk-forward.
4. Cost model is partial: commission is declared at 0.1 percent, but slippage is 0 by language default and spread, impact and perpetual funding are never mentioned, so any edge claim would still be underpriced.
5. The source's own Risk Analysis states "No stop loss mechanism, holding period can be very long", i.e. unbounded exposure by design.
6. The source's own Risk Analysis states "As a trend following strategy, it can generate many false signals during range-bound markets".
7. The source's own Risk Analysis states "The lagging nature of WT may cause missed turns".
8. The source's own Risk Analysis states "Default parameters may not suit all products and cycles".
9. The source's own Summary states the strategy "also needs additional filters and logic to avoid false signals", i.e. the published rule is explicitly presented as a bare template.
10. The Optimization block proposes adding volume or volatility confirmation and adding stop loss and take profit as future work, so neither exists in the rule.
11. The Optimization block proposes adding pyramiding and grid trading as future work; the pinned `pyramiding = 0` therefore is not an author-tuned risk control but the no-add default.
12. Prose claims the strategy goes short on the death cross; the code's short entry is commented out (recorded contradiction 1).
13. Prose claims both WT1 and WT2 are simple-moving-average outputs of the wave-trend line; the code sets `wt1 = tci` with no smoothing (recorded contradiction 2).
14. The date-range inputs and their computed `start` and `finish` timestamps are inert because `window()` returns `true` (recorded contradiction 3), so the artifact's own Arguments table advertises seven parameters that cannot change a trade.
15. The four overbought and oversold levels are plot-only and never gate an order (recorded contradiction 4).
16. Seven of the thirteen exposed inputs are inert, so the effective rule has only `Channel Length`, `Average Length` and the declaration constants.
17. Both `wt1` and `wt2` are functions of the same series, which mechanically raises cross frequency relative to an indicator-versus-price design, and there is no filter to suppress the resulting whipsaws.
18. After the first entry the system alternates only between long and flat, with no drawdown control of any kind.
19. Holding period is unbounded and the only exit is the crossunder, so a stale position can persist indefinitely while `wt1` stays above `wt2`.
20. The full source is gated behind login on the rendered FMZ landing page, leaving the third-party mirror at the pinned SHA as the single immutable point of provenance, with the landing payload as a non-immutable corroborating copy.
21. The mirror repository ships no LICENSE file and the Pine block carries no licence header, so redistribution status of the mirror as a whole is not stated in source.
22. Authorship is layered and unverified: the mirror records `Author: ChaoZhang` while the code's own credit comment names LazyBear; neither identity is independently confirmed and peer-review status is not stated in source.
23. There is no repository, no version tag, no test suite, no issue tracker and no changelog for the rule; the FMZ landing shows a single "Last modified" timestamp.
24. FMZ landing statistics (Copy 1, Hits 1596 as read 2026-10-05) show minimal community adoption, and no third-party study of this exact artifact was identified.
25. The `ema` entry of the official v4 reference carries the remark "Please note that using this variable/function can cause indicator repainting", while the official repainting concept page locates the mechanism in using values that fluctuate during a real-time bar; this record records both statements and does not adjudicate between them, and gate F2 exists to test it.
26. The official references disagree on two language-level details that bear on reconstruction: the `crossover` and `crossunder` prior-bar comparison (strict in the v4 manual, inclusive in the v6 manual) and the default value of `pyramiding` (0 in both reference manuals, 1 on the declaration-statements page). The migration guides document only the move of these functions into the `ta` namespace and record no semantic change.
27. The base-K-line field `basePeriod: 15m` in the header sits next to a `1h` decision period; although the script contains no `request.*` call and therefore no cross-timeframe dependency, a reader could mistake the header for a multi-timeframe design.
28. Division by zero in `ci` when `d` is 0 has no documented value anywhere in the official documentation consulted.
29. No independent replication, no competing study and no contrary external evidence specific to this artifact was found; absence of contrary literature is not evidence of robustness.

## Falsification plan

All thresholds below are `research-defined falsification threshold` values chosen by this Scout; none of them is source-reported. All test inputs (data vendor, sample window, benchmark definitions, cost model) are `research-proposed` test scaffolding and are not part of the strategy rule.

- **F1 — Semantic reconstruction gate.** Threshold: an independent reimplementation of the pinned rule must reproduce, on a reference OHLCV series, an identical `wt1` and `wt2` sequence and an identical ordered list of entry bars and exit bars (exact match, zero differing bars, including the first possible entry at bar index 42), and the tie case `wt1[t-1] == wt2[t-1]` must be exercised explicitly so that the strict-versus-inclusive prior-bar wording of the two official reference editions is resolved by observation rather than by preference. Action: any mismatch, or an inability to resolve the tie case from a primary source, means the record is not 1:1 reconstructible and must be withdrawn from admission review rather than repaired by interpretation.
- **F2 — Causality and repaint audit.** Threshold: every input used at bar `t` must be dated at or before `t` (`hlc3[t]`, EMA and SMA histories ending at `t`, the one-bar lookbehind inside the cross functions), with zero occurrences of future bars, negative shifts, `timenow`, `security`, session recalculation or any lower-timeframe request; and the `ema` repainting remark recorded in negative evidence 25 must be shown to be inapplicable under `calc_on_every_tick = false` and `process_orders_on_close = true`. Action: any future reference, or any observed difference between the historical and the real-time evaluation of a completed bar, means NOT_LOSSLESS, close the record.
- **F3 — Division-by-zero determinism.** Threshold: construct a synthetic 10-hour window in which `hlc3` is constant so that `d` is 0, and confirm that the reimplementation and the reference agree on the resulting `ci`, `wt1`, `wt2` and order state. Action: disagreement, or any undefined-but-divergent behaviour, means the record is not 1:1 reconstructible; withdraw rather than patch.
- **F4 — Cost ladder.** Threshold (research-defined): apply the declared 0.1 percent commission plus 0, 1, 2, 5 and 10 bps per side, and for the perpetual an additional funding accrual leg; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side. Action: fail means the edge is cost-dependent, record remains research-only and must not be proposed for any adoption.
- **F5 — Parameter perturbation.** Threshold (research-defined): sweep `Channel Length` over 5, 8, 10, 13, 16, 20 and `Average Length` over 10, 14, 21, 28, 34, 42, with the normalization constant frozen at 0.015; fail if the sign of net return over the full sample flips for the published cell or if fewer than half of the 36 cells produce positive net return. Action: fail means parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold (research-defined): split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day ADX(14) trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split. Action: fail means the rule requires a regime gate that the source does not contain, so it cannot be admitted as-is and must stay research-only.
- **F7 — Whipsaw and flat-exposure placebo.** Threshold (research-defined): compare against buy-and-hold BTCUSDT on the identical window and against 1000 shuffled-cross sequences preserving the observed holding-time distribution; fail if the observed net Sharpe does not exceed the 95th percentile of the placebo distribution, or if the system is invested for less than 5 percent or more than 95 percent of the sample. Action: fail means no evidence that cross timing carries information.
- **F8 — Out-of-sample requirement.** Threshold (research-defined): at least 5 years of 1h BTCUSDT bars with a frozen chronological split and no re-tuning; fail if out-of-sample net Sharpe is 0 or below. Action: fail means reject for adoption; do not rescue by re-tuning.
- **F9 — Capacity and liquidity.** Threshold (research-defined): fail if the required notional of 1000 units of symbol cash exceeds 5 percent of the trailing 30-day median hourly traded volume of the instrument. Action: fail means capacity-capped, record the ceiling and block any size scaling.
- **F10 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side. Action: fail means single-asset overfit diagnosis.
- **F11 — Long-only ablation.** Threshold (research-defined): compare the pinned long-only system against the short side the prose describes but the code disables, using the mirrored entry rule; fail if the disabled short side would have contributed more than 60 percent of the gross absolute PnL of the two-sided variant. Action: fail means the source's own direction choice is the dominant design decision and the long-only artifact must be reported as materially incomplete relative to its prose.
- **F12 — Multiplicity control.** Threshold (research-defined): apply Benjamini-Hochberg at q = 0.10 across the full F5 × F10 cell family; fail if the published cell does not survive. Action: fail means treat the published configuration as one draw among many, no adoption.
- **F13 — Frozen forward window.** Threshold (research-defined): forward test from 2026-10-05 to 2027-10-04 with every parameter frozen; fail if forward net Sharpe at 2 bps per side is 0 or below. Action: fail means reject; no parameter may be changed to re-run it.

Global no-retuning rule: `Channel Length 10`, `Average Length 21`, the normalization constant `0.015`, the `hlc3` source price, the EMA and SMA seeding rule, `wt1 = tci` with no extra smoothing, `wt2 = sma(wt1, 4)`, the crossover and crossunder entry and exit, the long-only direction, `pyramiding 0`, the fixed 1000-unit-of-symbol-cash sizing, `process_orders_on_close` same-bar-close fills, the declared 0.1 percent commission, the single `1h` timeframe, the BTCUSDT instrument and the absence of any time gate are frozen. No gate may be rescued by changing a parameter, widening a window, switching vendor, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The cited source itself configures the rule on Binance USDT-margined BTCUSDT futures at `period: 1h`, so instrument, venue and market type are already crypto and no porting change is required to express the rule. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- The rule consumes only `high`, `low` and `close`, all available on any 24/7 crypto venue; there is no session, holiday or opening-auction dependency, and no order condition reads wall-clock time, so the 24/7 clock cannot alter a decision boundary.
- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, so none of those crypto-specific inputs can invalidate the signal.
- The rule is long-only, so spot, dated futures and perpetual are all applicable with no borrow or short-availability assumption.
- Risks that remain crypto-specific and unmodeled by the source: perpetual funding accrual (never mentioned, `data gap`), the choice of mark versus last price for valuation (`data gap`), contract specification and tick-size differences between venues (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), hourly candle boundary conventions across venues (`data gap`), and liquidity or market-impact differences at 1000 units of symbol cash per entry (`data gap`).
- Timestamp and candle boundaries are exchange-defined UTC hourly bars on Binance; the record does not assume any other boundary convention.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: spread, market impact, funding, latency, fill-failure and missing-data handling, capacity, the exact Binance contract, the residual account reporting currency, and the division-by-zero value of `ci`.
- `underspecified`: the exact-tie prior-bar wording of `crossover` and `crossunder` across reference editions, and the redistribution status of the mirror as a whole. Both are recorded with their primary sources and neither is chosen here.
- `unproven`: profitability, robustness, regime robustness, cross-instrument robustness, capacity, forward performance and the disabled short side.
- Source-quality limitation: a single community mirror entry with no repository, no tests, no versioning, no peer review and layered, unverified authorship; the rendered landing page gates the full source behind login.
- Reproducibility limitation: because FMZ prints no results, there is no claim of good backtest results to check, and the only immutable, publicly auditable artifact is the mirror at the pinned SHA.
- Identification limitation: the rule is price-only and unfalsified; nothing in the source separates oscillator timing from a beta or from a whipsaw-carrying long-or-flat exposure.
- Publication-bias limitation: a public strategy mirror selects for presentable, not for robust, and Copy 1 suggests negligible community reuse.
- Documentation limitation: the official references themselves disagree on two language-level details (the cross prior-bar comparison and the `pyramiding` default), so an exact reconstruction must resolve them from primary sources rather than from prose.
- Incremental-write check: this is the first record in the repository for this source identity after the 2026-10-04 pool reset, and no Wiki Brain page exists for it, so this is not ordinary duplicate material.
- A four-item contradiction set is recorded in frontmatter. All four are prose-versus-code or table-versus-code conflicts inside one artifact, and in every case the pinned code is the executable and unambiguous text, so none of them leaves the signal itself ambiguous.

## Implementation status

`not-implemented`. Nothing has been implemented in our research stack. No Pine was executed, no backtester was run, no Hummingbot package `20260920` or `dev-2.17.0` backtest was attempted, no Qlib job was created, no indicator was coded, and no Paper, Testnet or Live workflow was touched. The only artifacts produced by this run are this Markdown record and its verification script.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. Presence of this record does not mean: passed LOSSLESS HB_READY review; merged to `main`; entered Hermes Wiki Brain; entered any candidate pool; completed a Hummingbot or Qlib full backtest; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for Paper; approved for Testnet; approved for Live. HB_READY itself, if it were ever granted, means semantic and backtest expressibility only. No record may promote itself by wording, evidence count, confidence or schedule behavior.

## Related Wiki records

No Wiki Brain page exists for this source identity, and this run writes none. The following existing pages were checked on disk and are related by mechanism family or by execution and validation discipline rather than by source identity; none of them shares the Wave Trend source, the `wt1`/`wt2` self-cross signal, or the BTCUSDT 1h single-pair scope:

- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/tradingview-choppiness-donchian-breakout-filter-2026-09-16]]
- [[quant/tradingview-volume-weighted-supertrend-dual-confirmation-2026-09-16]]
- [[quant/tradingview-keltner-ema200-adx-volume-volatility-breakout-2026-09-16]]
- [[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]
- [[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]]
- [[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]

## Sources

- https://github.com/fmzquant/strategies — pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `基于波浪趋势的交易策略The-Wave-Trend-Trading-Strategy-Based-on-LazyBear.md`; the complete primary source read end to end on 2026-10-05, SHA-256 `d74eb1d600829ff58b5225d61ce3318ef09861d26df3729eb7199b9744545edd`.
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8E%E6%B3%A2%E6%B5%AA%E8%B6%8B%E5%8A%BF%E7%9A%84%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5The-Wave-Trend-Trading-Strategy-Based-on-LazyBear.md — percent-encoded form of the same pinned file.
- https://www.fmz.com/strategy/435853 — FMZ landing page, fetched over unauthenticated HTTPS on 2026-10-05; confirms title, author account, creation timestamp, category, Copy and Hits counters, English description, thirteen exposed parameters, the presence of `Login to view full source` in the rendered UI, the absence of any performance section, and an embedded copy of the Pine source in the served HTML.
- https://www.tradingview.com/pine-script-reference/v4/ — official first-party Pine v4 language reference, rendered in a browser on 2026-10-05; used only for language-level semantics of the pinned script: `hlc3`, `ema` and its seeding implementation, `sma`, `crossover` and `crossunder`, `strategy.entry`, `strategy.close`, and the `strategy()` declaration parameters `pyramiding`, `default_qty_type`, `default_qty_value`, `currency`, `slippage`, `commission_type`, `commission_value`, `process_orders_on_close`, `calc_on_every_tick`, `calc_on_order_fills`, `close_entries_rule`, `backtest_fill_limits_assumption`, `margin_long` and `margin_short`.
- https://www.tradingview.com/pine-script-reference/v6/ — official first-party Pine v6 language reference, rendered in a browser on 2026-10-05; used only to record the current wording of `crossover`, `crossunder` and `pyramiding` and to expose the disagreement with the v4 wording.
- https://www.tradingview.com/pine-script-docs/language/declaration-statements/ — official first-party documentation used only for language-level semantics: the `strategy()` signature, the `pyramiding` default, `calc_on_every_tick` default false, `calc_on_order_fills` default false, `process_orders_on_close` behaviour, and the `slippage` default of 0.
- https://www.tradingview.com/pine-script-docs/concepts/strategies/ — official first-party documentation used only for the `pyramiding` limit semantics (rejection lasting until a trade closes), the broker emulator's same-bar-close behaviour, `commission_type` and `commission_value`, `default_qty_type`, and `margin_long` / `margin_short` defaults of 100.
- https://www.tradingview.com/support/solutions/43000628599-strategy-properties/ — official first-party Help Center article used only for the enumeration of strategy properties (which contains no cooldown), the statement that commission applies to both entries and exits, and the statement that when pyramiding is disabled the strategy can only open one long or short position.
- https://www.tradingview.com/pine-script-docs/concepts/repainting/ — official first-party documentation used only to record the mechanism attributed to repainting, in connection with the `ema` remark quoted in negative evidence 25.
- https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-5 and https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6 — official first-party migration guides, read to confirm that they document only the move of `crossover` and `crossunder` into the `ta` namespace and record no semantic change.
