---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ichimoku-regime RSI-gated two-sided reversal system on BTCUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-08
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts
  - https://www.tradingview.com/script/2OfRyQSy-Ichimoku-Cloud-with-RSI-By-Coinrule/
  - https://www.tradingview.com/pine-script-reference/v5/#fun_rsi
  - https://www.tradingview.com/pine-script-reference/v5/#fun_mom
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v5/#fun_timestamp
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The stable page states 'Chikou-Span is above the close of 26 bars ago', but the pinned code implements the Chikou leg as ta.mom(close, cs_offset - 1) with cs_offset = 26, i.e. close[t] > close[t-25] (25 bars, not 26). The code governs."
  - "The stable page states 'Long/Short orders are placed when three basic signals are triggered', but the pinned code ANDs four legs per side (Tenkan/Kijun state, Chikou momentum, Kumo position, RSI gate). The code governs."
  - "The stable page prints 'RSI is greater less than 50' for the long leg (a typo); the pinned code is RSI < 50 for Long entries and RSI > 50 for Short entries (strict). The code governs."
  - "The stable page suggests SOL (45m), BNB (1h) and ETH (1h) while this record pins a BTCUSDT 1d run as the explicit single-pair research market under the house overlay. The pin is a Scout-declared research choice, not a source claim."
  - "The stable page states the script 'provides good returns' with zero numeric performance claims anywhere on the page (no return, Sharpe, drawdown, win-rate or trade-count figure), so there is nothing to reproduce."
---

# Ichimoku-regime RSI-gated two-sided reversal system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/hasnocool/tradingview-pine-scripts
- Full commit SHA: `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (commit date 2024-09-18T04:39:33-0600, subject `Automated commit: Synced local changes to 'tradingview-pine-scripts' via script`). A `git ls-remote` of origin HEAD on 2026-10-08 returned this same SHA, so it is still the repository head at research time.
- Exact file path: `Ichimoku Cloud with RSI (By Coinrule).pine` (spaces and parentheses preserved verbatim; percent-encoded blob URL: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Ichimoku%20Cloud%20with%20RSI%20(By%20Coinrule).pine ).
- Pinned artifact: blob `5558c0c6a64f83a5d3cd2831f6f990722dd8fc51`, 3515 bytes (Contents API reports the same size), SHA-256 `0ba1db7f7f93a5ec7ec02209f7d82df1d8dc97018a910a7b170dada7ff23d54e`, 133 lines. The file embeds the TradingView page chrome around the code (`Script Name`, `Author: Coinrule`, line numbers, `Expand (70 lines)`); the executable Pine was read from the `//@version=5` line through the last `strategy.close` call and censused separately from the chrome.
- Licence and rights: the pinned code prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` and the author credit `// © Coinrule`. The mirror repository ships no LICENSE file, so the redistribution status of the mirror as a whole is not stated in source; this record therefore cites and normalizes the rule and reproduces no source code block.

Canonical origin (corroborating, read live on 2026-10-08): https://www.tradingview.com/script/2OfRyQSy-Ichimoku-Cloud-with-RSI-By-Coinrule/ — page title `Ichimoku Cloud with RSI (By Coinrule) — Strategy by Coinrule`, badge `OPEN-SOURCE SCRIPT`, `Updated Aug 9, 2022`, author `Coinrule`. The page description, the Long/Short bullet lists, the `30% of the available coins` sizing line, the `0.1%` fee line, the `backtested from 1 June 2022` line and the SOL-45m / BNB-1h / ETH-1h suggestions were read live and match the mirror code's parameters (RSI 14 with `< 50` Long / `> 50` Short, `percent_of_equity` 30, 0.1 percent commission, gate from 2022-06-01) except for the four page-versus-code contradictions recorded in frontmatter, where the code governs.

Executable-code census of the pinned artifact (chrome excluded where noted): `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.cancel` 0, `strategy.entry` 2, `strategy.close` 2, `request.*` 0, `security(` 0, `ta.crossover` 0, `ta.crossunder` 0, `crossover(` 0, `crossunder(` 0, `ta.ema` 0, `macd` 0, `calc_on_every_tick` 0, `calc_on_order_fills` 0, `pyramiding` 0, `process_orders_on_close` 1, `timenow` 0, `timestamp(` 1, `input.session` 0, `strategy.position_size` 0, `position_avg_price` 0, `lookahead` 0, `use_bar_magnifier` 0, `input.time` 0, `/` division operators in executable code 0. `input.*` calls: 8 (`showDate`, `ts_bars`, `ks_bars`, `ssb_bars`, `cs_offset`, `ss_offset`, `long_entry`, `short_entry`); the RSI length (14) is a hardcoded constant, not an input.

Pre-write dedup (2026-10-08): whole-tree search for `2OfRyQSy`, `Ichimoku Cloud with RSI`, `5558c0c6` returned 0 matches. The pool record `ichimoku-cloud-adx-trend-filter-btcusdt-1d-2026-10-06` is the sibling Coinrule script `Ichimoku Cloud with ADX` (canonical URL `.../je5bIJeR-Ichimoku-Cloud-with-ADX-By-Coinrule/`): its signal is a six-leg AND with a `ta.dmi(14, 14)` triple and an asymmetric ADX-45 gate (`avg_dm < 45` Long / `> 45` Short, strict DI dominance) with date gate 2022-01-01, while this candidate is a four-leg AND with no DMI at all and a hardcoded `ta.rsi(close, 14)` 50-gate of opposite polarity (`RSI < 50` to enter Long inside a bull regime, `RSI > 50` to enter Short inside a bear regime) with date gate 2022-06-01 — a materially different normalized signal with a different event sequence, not a trivial parameter variant. The long-only `octa-ema-ichimoku-trend-long` pool record is an EMA-ribbon plus Ichimoku-variant filter (long-only, no RSI, no cloud-displacement signal) and differs in direction handling and construction. No other pool record combines an Ichimoku regime with an RSI gate. Open `research/*` PRs at write time: #48 (Larry Williams streak, FMZ 451075), #49 (Gaussian channel plus StochRSI, FMZ 482888) — different sources and mechanisms. `git ls-remote --heads origin 'research/*'` shows no ichimoku-RSI head.

## Economic mechanism

### Source-reported

The source states the mechanism only descriptively; it gives no behavioural, structural or risk-premium channel.

- Overview, as printed: the Ichimoku reading guide (five lines, cloud support/resistance, above-cloud uptrend / below-cloud downtrend with cloud-direction confirmation) plus "This strategy combines the Ichimoku Cloud with the RSI indicator to better enter trades."
- Long Position bullets, as printed: Tenkan above Kijun; Chikou above the close of 26 bars ago; close above the Kumo cloud; RSI "greater less than 50". Short Position bullets are the mirror with RSI above 50 — subject to recorded contradictions 1–3, where the code governs.
- Sizing/fee/date notes, as printed: 30 percent of available coins per order "to make the results more realistic", 0.1 percent fee "aligned to the base fee applied on Binance", "backtested from 1 June 2022 and provides good returns" (recorded contradiction 5: zero numbers), SOL-45m / BNB-1h / ETH-1h suitability suggestions (recorded contradiction 4).

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, a fully-aligned Ichimoku regime (conversion above base, lagging momentum positive, price above the displaced cloud) marks an established directional state, and requiring the 14-bar RSI to still sit on the "weak" side of 50 (below 50 for longs, above 50 for shorts) times entry toward countertrend-softened prints inside that regime rather than chasing extended prints; the bet is that regime persistence plus unextended momentum produces cleaner continuation than late-chase entries. The exit is not a level but the mirror-image regime event. This is a ported technical-analysis hypothesis: the source supplies no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles:

- Primary signal: the four-leg Ichimoku-plus-RSI AND per side (regime triple plus contrarian RSI gate).
- Volatility normalizer: none. No ATR, standard-deviation or range scaling appears anywhere in the live legs.
- Trend / regime filter: the Ichimoku triple itself (Tenkan/Kijun state, Chikou momentum, Kumo position).
- Risk / exit: none. The only exit is the opposite-direction entry (position reversal); stop loss, take profit, trailing stop and time exit are all absent.
- Sizing: 30 percent of available equity per position, declared in the strategy declaration, i.e. compounding without scaling.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`. All statements hold at the pinned source defaults (`ts_bars=9`, `ks_bars=26`, `ssb_bars=52`, `cs_offset=26`, `ss_offset=26`, `long_entry=true`, `short_entry=true`, `showDate=true`, hardcoded `lengthRSI=14`, `percent_of_equity` 30, 0.1 percent commission, gate from 2022-06-01); any other input combination is a different, unpinned rule.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (research-pinned single decision timeframe; the script itself is timeframe-agnostic — 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency to align).
- Inputs at decision bar `t`: `high[t-25..t]` and `low[t-25..t]` (through `ta.lowest`/`ta.highest` and the 25-bar displaced-cloud lookup), `close[t-25..t]` (through `ta.mom(close, 25)`, `ta.rsi(close, 14)` and `close` versus cloud), and bar `time[t]` (date gate only). `open` is never read by the trading logic and `volume` occurs 0 times in the whole artifact.
- Order timing: the live order calls are two `strategy.entry` and two `strategy.close`, all market orders (no `limit`/`stop` arguments anywhere — 0 occurrences of each), and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true the broker emulator processes orders "on the closing tick of each bar", and for market orders "executes them before the next bar's open". This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false`. Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Date gate: `showDate = input(defval=true, title='Show Date Range')` (display only) and `timePeriod = time >= timestamp(syminfo.timezone, 2022, 6, 1, 0, 0)`. Both live entries carry `and timePeriod`; both live closes do not carry it directly but can only fire after an entry opened a position, so no position can exist before 2022-06-01 under this pin. Explicit consequence, recorded rather than repaired: bars before 2022-06-01 (including 2017–2021 Binance history) can never carry an entry under this pin, so the effective backtest scope starts 2022-06-01; the gate has no end date, so eligibility never expires. `timenow` occurs 0 times. The `timestamp()` call passes `syminfo.timezone` explicitly, so the boundary is the symbol's exchange timezone by source declaration.

**Lookback, formulas and warmup**

- Parameters as declared: `ts_bars=input.int(9, minval=1)`, `ks_bars=input.int(26, minval=1)`, `ssb_bars=input.int(52, minval=1)`, `cs_offset=input.int(26, minval=1)`, `ss_offset=input.int(26, minval=1)`, `long_entry=input(true)`, `short_entry=input(true)`, `lengthRSI = 14` (hardcoded constant, not an input), `RSI = ta.rsi(close, 14)` (official v5 `ta.rsi` reference fixes the RMA-based Wilder variant on `close`). The official v5 `ta.mom` reference fixes `ta.mom(close, cs_offset - 1)` = `close[t] - close[t-25]`. The rule contains 0 `crossover`, 0 `crossunder`, 0 `ta.cross`, 0 `ta.ema`, 0 `ta.sma`, 0 `ta.dmi`, 0 `macd`, 0 `request.*`, 0 `security(` and 0 division operators in executable code, so none of the tie-semantics, multi-timeframe, smoothing-variant, MACD-missing or zero-divisor blockers arise in the live legs.
- Exact formulas, verbatim structure at defaults:
  - `middle(len) => math.avg(ta.lowest(len), ta.highest(len))` (average of the lowest low and highest high over `len` bars per the official `ta.lowest`/`ta.highest`/`math.avg` references).
  - `tenkan = middle(9)`, `kijun = middle(26)`, `senkouA = math.avg(tenkan, kijun)`, `senkouB = middle(52)`.
  - `ss_high = math.max(senkouA[25], senkouB[25])`, `ss_low = math.min(senkouA[25], senkouB[25])` (the cloud plotted `ss_offset - 1 = 25` bars forward for display, read back 25 bars for the signal — a past reference, not a future reference; the Chikou `plot(close, offset=-cs_offset+1)` is display-only and never read by an order).
  - `tk_cross_bull = tenkan > kijun`, `tk_cross_bear = tenkan < kijun` (strict; equality is neither).
  - `cs_cross_bull = ta.mom(close, 25) > 0` (i.e. `close[t] > close[t-25]`), `cs_cross_bear = ta.mom(close, 25) < 0` (strict; equality is neither).
  - `price_above_kumo = close > ss_high`, `price_below_kumo = close < ss_low` (strict; touching the cloud edge is neither).
  - `bullish = tk_cross_bull and cs_cross_bull and price_above_kumo`.
  - `bearish = tk_cross_bear and cs_cross_bear and price_below_kumo`.
  - Long gate adds `RSI < 50` (strict; exactly 50 is neither); short gate adds `RSI > 50` (strict).
  - No other signal variable exists in the artifact; census gives `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.cancel` 0, `limit =` 0, `stop =` 0.
- Mutual exclusivity: `bullish` requires `tenkan > kijun`, `mom > 0`, `close > ss_high` while `bearish` requires the strict opposite on all three legs (`<`, `<`, `close < ss_low` with `ss_low <= ss_high` by `min`/`max` construction), so both legs can never fire on the same bar — every equality case fires neither, and the RSI gates (`< 50` vs `> 50`) are likewise disjoint. There is no dual-signal bar, no call-order dependence, and no priority choice anywhere in the rule.
- Warmup, derived from the pinned code because the source declares none: no order can be created before the first bar on which all of `middle(52)`, the 25-bar cloud lookup, `ta.mom(close, 25)` and `ta.rsi(close, 14)` are defined (a function of the 52/26/25/14 lookbacks from bar 0, dominated by the 52-bar Senkou-B window plus its 25-bar displacement). A boolean `na` in a `when=` cannot open an order, so pre-warmup bars are flat by language semantics. `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically, and the rule references no lag beyond the windows above.
- Same-bar accounting: at most one of the two live entries can fire per bar (mutual exclusivity above); from flat an entry opens a one-sided position, from the opposite side the new entry reverses it, and while on the same side a repeated entry signal is rejected under the default `pyramiding` rule below. Orders fill on the same bar they are created, so no unfilled order survives into the next bar.

**Entry**

- Long entry: `strategy.entry("Long", strategy.long, when=bullish and long_entry and RSI < 50 and timePeriod)` — all four legs strictly defined, no OR branch, no alternative id.
- Short entry: `strategy.entry("Short", strategy.short, when=bearish and short_entry and RSI > 50 and timePeriod)` — mirror image, no OR branch, no alternative id.
- Both statements omit `qty`. Official reference: `qty` "The default is na, which means that the command uses the default_qty_type and default_qty_value parameters of the strategy declaration statement to determine the quantity" — here `strategy.percent_of_equity` with value `30`.
- Both statements omit `limit` and `stop`; official reference: `limit`/`stop` "The default is na, which means the resulting order is not of the limit or stop-limit type", so both are market orders.

**Exit**

- The pinned code contains exactly four order calls: 2 `strategy.entry`, 2 `strategy.close`. At pinned defaults (`long_entry=true`, `short_entry=true`) both closes are inert by construction: `strategy.close("Long", when=bearish and not short_entry)` is `bearish and false` = never, and `strategy.close("Short", when=bullish and not long_entry)` is `bullish and false` = never. Exits therefore occur exclusively through opposite-side entries (a fresh `bearish` bar reverses a long into a short; a fresh `bullish` bar reverses a short into a long).
- Stop loss: none in executable code. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none (the date input bounds entry eligibility from 2022-06-01 only, with no end). Flat state: reachable before the first entry and whenever neither leg fires — the system is otherwise always in the market once the first entry fires. This is recorded, not repaired: adding a stop, target, trailing or time exit would be a rule change.
- The `strategy.close` pair is not redundant: if a chart user flips `short_entry` to false (or `long_entry` to false), the corresponding close becomes the signal exit for the remaining side. At the pinned defaults both are disabled, which is why the record pins the defaults explicitly.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by waiting for the next opposite-alignment bar; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration, so the value comes from the language default: the v5 reference states the default is 0, meaning only one entry order in the same direction can be opened and additional same-side entries are rejected. With one live entry id per side (`"Long"`, `"Short"`), mutually exclusive entry legs, and same-bar-close fills, there is no second same-side position that could stack, and net exposure is always exactly one side. The record therefore records `pyramiding` as source-declared-by-language-default, and F3 forces the executing engine to confirm it.
- Same-direction re-entry: after an opposite-side reversal the system holds the new side, so the next same-alignment bar while already on that side is rejected under the default above; a fresh entry in that direction requires first being reversed to the other side (or flattened in a non-default input configuration). Orders fill on the same bar they are created, so no unfilled order survives into the next bar.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. A fresh entry requires a fresh full four-leg event while on the opposite side or flat, so cooldown semantics are provably irrelevant rather than missing.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy("Ichimoku Cloud with RSI (By Coinrule)", overlay=true, initial_capital=1000, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=30, commission_type=strategy.commission.percent, commission_value=0.1)`. (`overlay` is display only per the official `strategy()` signature.)
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0`, `margin_long`/`margin_short` at the v5 default, `pyramiding` (convergence above), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (moot: one live entry id per side with full reversals), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` (no price-dependent orders exist) and `use_bar_magnifier=false`.
- Sizing: `strategy.percent_of_equity` with value 30, i.e. each entry is 30 percent of available equity — declared in the code, therefore explicit and compounding.
- Direction: two-sided at pinned defaults (both inputs true). Because a short path is live, spot is deterministically inapplicable to the short leg (see Required data); the pinned run is a perpetual single-pair run.
- Nothing else is declared: `currency`, `slippage`, `margin_*`, `pyramiding`, `close_entries_rule`, `calc_*`, `max_bars_back` and `use_bar_magnifier` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variants and their parameters, source prices (high/low for the Ichimoku legs, close for Chikou/cloud/RSI), lookbacks (9/26/52/26/26/14), smoothing (the official `ta.rsi` RMA variant and `math.avg`/`math.max`/`math.min`/`ta.mom`, no custom average), thresholds (RSI 50 strict with opposite polarity per side), comparison logic, AND structure, direction inputs, entries, exits, risk semantics (explicitly none live), sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults and functions. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE` and the latency/fill-failure model beyond the declared 0.1 percent commission; neither alters the signal, and both are recorded as `data gap` or boundary convention rather than filled. There is no perpetual-versus-dated question beyond the pinned perpetual run because the short leg requires a shortable instrument and the signal uses OHLCV only.

## Required data

- Instrument: BTCUSDT perpetual, research-pinned as the single-pair run of a venue-agnostic rule. The source script declares no venue, no exchange and no symbol (it runs on whatever chart it is attached to); because the pinned rule shorts at defaults, a shortable instrument is deterministically required and spot is excluded for the short leg. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: perpetual. The rule holds both long and short positions at defaults, so a margined long/short instrument is required. The artifact does not distinguish the perpetual from a dated future, which is `data gap`; it is immaterial to an OHLCV-only signal but must be pinned before any execution work. Funding itself is never read by the rule (0 occurrences) and the edge does not depend on funding PnL; funding as a cost is `data gap`.
- Spot applicability: not applicable to the pinned two-sided rule, because spot would require naked shorting. The long leg alone could run on spot, but that would be a modified single-side strategy and is not proposed.
- Venue: any venue listing BTCUSDT perpetual; no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, research-pinned for this record. The pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: `high`/`low` (Ichimoku `middle()` windows and the displaced-cloud lookup), `close` (Chikou `mom`, `close` versus cloud, RSI), bar `time` (date gate only). `open` and `volume` are never read by the trading logic.
- Fields not required and not used, each absent from the pinned live legs: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state. The calendar is gated only by the explicit from-2022-06-01 `timePeriod` expression (see Signal). DMI/ADX, EMA/SMA, MACD and Bollinger inputs are absent from the pinned code (0 occurrences of each) and are therefore not data dependencies of this record.
- Point-in-time: every input at bar `t` is contemporaneous or a deterministic function of bars at or before `t` (Ichimoku windows ending at `t`, cloud values from `t-25`, `mom` over `[t-25, t]`, RSI over `[t-13, t]`, `time[t]`); there is no future reference (the Senkou/Chikou forward offsets are display-only and the signal reads the cloud back), no negative shift in any order input, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: bar open times of a 1-day BTCUSDT perpetual series compared against the explicitly exchange-timezone-resolved 2022-06-01 origin (`timestamp(syminfo.timezone, ...)` by source declaration).
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. The `na` rule that matters is the language one: indicator outputs are `na` until their lookbacks are satisfied, and a boolean `na` in `when=` cannot open an order — this is what fixes the warmup.
- Funding, fee and spread needs: the source declares a 0.1 percent commission per the code and the stable page; spread, slippage beyond the documented 0-tick default, impact, funding accrual and latency are `data gap`, never a modeled zero. Word-boundary census of the pinned 3515-byte artifact gives sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, profit factor 0, backtest 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, take profit 0, trailing 0, margin 0, equity 1 (the `percent_of_equity` token), commission 3 (type, value, and the stable-page-corroborated 0.1).

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market orders, created only by the two live `strategy.entry` calls (the two `strategy.close` calls are inert at pinned defaults and become signal exits only in non-default input configurations). There is no limit order, no stop order, no stop-limit, no OCA group and no conditional price order anywhere in the live rule (0 `strategy.exit`, 0 `strategy.order`, 0 `limit`/`stop` order arguments), so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumptions are never exercised, because they apply only to price-dependent orders.
- Fill model: `process_orders_on_close=true` → official documentation: orders are processed "on the closing tick of each bar", and for market orders "the broker emulator executes them before the next bar's open". `calc_on_every_tick` and `calc_on_order_fills` default to `false`, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled on the same completed-bar close; the engine's "Order execution delay" override defaults to 0 ticks.
- Dual-signal bar: impossible by construction — `bullish` and `bearish` are mutually exclusive on the same bar's inputs (state table under Signal); the position ends in exactly one deterministic state in all cases.
- Position limits: one net position at a time, 30 percent of available equity per entry, no same-side add-on (default `pyramiding`, convergence recorded above), no scaling, no grid, no martingale, no hedge (opposite entries reverse, they do not hedge).
- Leverage and margin: unset in code → v5 defaults; sizing is equity-percentage, so the rule never sizes by leverage and has no leverage-dependent edge. Perpetual margin mechanics beyond sizing are `data gap`.
- Costs: `commission_type=strategy.commission.percent` with `commission_value=0.1`, i.e. 0.1 percent of order cash volume charged on each fill — source-declared, corroborated by the stable page; `slippage` defaults to 0 ticks per the official reference. No spread, no market-impact model, no funding-accrual model appears anywhere in the artifact → the remaining cost legs are `data gap`; this record does not adopt a validated zero-cost assumption beyond the documented defaults.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F8.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (timeframe, symbol, initial capital, currency, pyramiding, commission, dates, order size, order execution delay, long/short toggles) are not part of the pinned source; the code-declared values plus documented defaults above are the recorded strategy.
- Scout-vs-source split: the venue-agnostic script is evaluated here as one explicit single-pair run (BTCUSDT perpetual, `1d`); every other item above marked source-declared comes from the pinned declaration, the pinned code, or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 3515-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0; `time` occurs in the `timePeriod`/`timestamp()` gate only; `timeframe` occurs 0 times; `macd` occurs 0 times; `dmi`/`adx` occur 0 times. There is no equity curve, no trade list, no table and no figure anywhere in the artifact. The stable page likewise prints zero numeric performance claims — only the qualitative "provides good returns" line.

What the source does report:

- Configuration only, from the pinned code: `//@version=5`, `middle()` over 9/26/52, offsets 26/26, `ta.mom(close, 25)`, hardcoded `ta.rsi(close, 14)`, strict four-leg ANDs with opposite-polarity RSI-50 gates (`< 50` Long / `> 50` Short), gate from 2022-06-01, `percent_of_equity` 30, `process_orders_on_close=true`, 0.1 percent commission.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: the Ichimoku reading guide, the combination claim, the 30-percent realism note, the 0.1-percent fee note, the "backtested from 1 June 2022 and provides good returns" line, the SOL-45m / BNB-1h / ETH-1h suggestions — unverifiable as printed and recorded as bare claims, not as evidence.
- Research-computed, not printed: at the pinned defaults the rule is a strict-inequality four-leg AND per side, so its trigger rate is set by joint Ichimoku-plus-RSI alignment rarity, not by any fixed price distance; and the two sides are mutually exclusive on every bar.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above. Third-party pages that re-host this script's statistics are not cited and contribute no number to this record.

### Independently reproduced

Not independently reproduced.

Only the following were performed: SHA-256 checksumming of the pinned artifact; confirmation that the fresh clone HEAD equals the remote HEAD (`69969aeaf271b2f7b5a7632a1bde43069a0cbe26`) plus blob-id/size cross-check via the Contents API (blob `5558c0c6a64f83a5d3cd2831f6f990722dd8fc51`, 3515 bytes); a whole-artifact term and word-boundary census; enumeration of `strategy.*`, `input*`, `timestamp`, `ta.rsi`/`ta.mom`/`ta.lowest`/`ta.highest` call sites and of identifier occurrence counts; verification that no live leg contains a division operator; a same-bar mutual-exclusivity walk; live reading of the canonical TradingView page (badge, title, author, update date, full description, sizing/fee/date lines and Long/Short bullet lists — matching except the recorded contradictions); and live reading over HTTPS of the official TradingView documentation pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized, roi and trade counts are all 0 occurrences.
2. The performance-sounding prose ("provides good returns", SOL/BNB/ETH suitability) carries no sample, no metric and no baseline, so it cannot be checked as printed.
3. The stable page advertises sub-hourly altcoin timeframes while the pinned rule evaluated here is a `1d` BTCUSDT run (recorded contradiction 4) — a reader following the prose would trade a different market and timeframe than this record.
4. The stable page's Long/Short bullets describe a "three signals" rule and a 26-bar Chikou lookback that do not match the pinned code (recorded contradictions 1–2) — a reader following the prose would trade a different signal than this record.
5. The live rule has no stop, no target and no time exit, so adverse excursion on either side is unbounded until the opposite alignment prints.
6. Cost model is the declared 0.1 percent commission with 0-tick slippage default and no spread, impact, funding-accrual or latency model — so any edge claim is only partially priced by the source.
7. Sizing is 30 percent of available equity per entry with no cash buffer, no volatility targeting and no risk layer of any kind; consecutive reversals compound turnover at full size.
8. Holding is unbounded: with no time exit and no level exit beyond the opposite-alignment event, exposure persists indefinitely until the mirror event — and if alignment never recurs, the position never closes.
9. The 2022-06-01 start gate excludes all pre-2022-06 history by source rule; any evaluation on earlier bars would contradict the pin.
10. No train/test split, no out-of-sample section and no walk-forward exists anywhere in the source.

## Falsification plan

All thresholds below are research-defined tests, never substitutes for the execution rules above (which are frozen: `middle(9/26/52)`, offsets 26/26, `ta.mom(close, 25)`, hardcoded `ta.rsi(close, 14)`, strict four-leg ANDs with opposite-polarity RSI-50 gates, `long_entry=true`, `short_entry=true`, gate from 2022-06-01, `percent_of_equity` 30 compounding, same-bar-close fills, 0.1 percent commission, 0-tick slippage, single `1d` timeframe, BTCUSDT perpetual).

- **F1 — Signal presence.** Threshold: at least 30 entries per side and at least 10 reversals per side on `1d` BTCUSDT perpetual bars from 2022-06-01; fail ⇒ the rule never trades this instrument/timeframe, record stays research-only.
- **F2 — Mutual-exclusivity audit.** Threshold: confirm on every bar that `bullish` and `bearish` never fire jointly and post-bar state is deterministic in all cases including all equality edges; fail ⇒ the exclusivity claimed above does not replay, pin the discrepancy and keep research-only.
- **F3 — Engine-default audit gate.** Threshold: the executing engine must confirm every recorded declaration and language default end to end — 30 percent equity sizing, same-bar-close fills, 0.1 percent commission, 0-tick slippage, once-per-bar evaluation, same-side entries rejected while on that side, opposite entries reversing, `na`-warmup with no pre-definition order, 2022-06-01 first eligible entry bar, both `strategy.close` calls inert at pinned defaults; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold: apply 0 / 1 / 2 / 5 / 10 bps of extra spread/slippage per side above the source-declared 0.1 percent, plus a separate funding-accrual sensitivity leg for the perpetual run; fail if net annualized return turns non-positive at 2 bps extra per side or net Sharpe falls to 0 or below at 5 bps extra per side ⇒ cost-dependent edge, no adoption.
- **F5 — Parameter perturbation.** Threshold: sweep Tenkan/Kijun over (9, 26), (7, 22), (12, 30), Senkou-B over 44/52/60, Chikou/mom lookback over 20/25/30 and RSI gate over 45, 50, 55 with everything else frozen; fail if the sign of net return flips for the published cell or if fewer than half the cells produce positive net return ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold: split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day simple trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split ⇒ the rule requires a regime gate the source does not contain, no adoption.
- **F7 — Placebo.** Threshold: compare against buy-and-hold BTCUSDT on the identical window and against 1000 random entry-date sequences preserving the observed holding-time and side distribution; fail if observed net Sharpe does not exceed the 95th percentile of the placebo distribution ⇒ no evidence the Ichimoku-plus-RSI timing carries information.
- **F8 — Capacity and liquidity.** Threshold: fail if the required notional (30 percent of equity per entry) exceeds 5 percent of the trailing 30-day median daily volume of BTCUSDT perpetual ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F9 — Cross-instrument generalization.** Threshold: run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual pair chosen before inspection; fail if 0 of 2 produce positive net return after the source commission plus 2 bps per side ⇒ single-asset overfit diagnosis.
- **F10 — Frozen forward window.** Threshold: forward test from 2026-10-08 to 2027-10-08 with every parameter frozen; fail if forward net Sharpe at source commission plus 2 bps per side is 0 or below ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `middle(9/26/52)`, offsets 26/26, `ta.mom(close, 25)`, `ta.rsi(close, 14)`, strict four-leg ANDs with opposite-polarity RSI-50 gates, both direction inputs true, the from-2022-06-01 gate, no stop/take-profit/time exit, `pyramiding` at its documented default (one open same-side entry), `percent_of_equity` 30 compounding sizing, `process_orders_on_close` same-bar-close fills, 0.1 percent commission and 0 ticks slippage, the single `1d` timeframe and the BTCUSDT perpetual instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching venue, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The rule consumes only daily-bar high/low/close (plus bar time for the explicit date gate) and trades two-sided market orders at bar closes with equity-percentage sizing, all natively available on any 24/7 crypto perpetual venue; there is no session, holiday or opening-auction dependency, and the only calendar expression in the source is the explicit from-2022-06-01 eligibility gate. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, and none can invalidate the signal; the short leg requires a shortable perpetual, but no borrow, margin-call or funding-accrual logic enters the signal.
- Risks that remain crypto-specific and unmodeled by the source: spread and market-impact differences for 30-percent-equity market orders (`data gap`), venue fee-schedule differences versus the declared 0.1 percent (`data gap`), funding-accrual drag on the perpetual run (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and stablecoin-peg or quote-currency events (`data gap`).
- Timestamps are exchange-defined UTC daily candles; the 2022-06-01 origin is resolved in the symbol's exchange timezone per the explicit `syminfo.timezone` declaration.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, funding-accrual, latency or fill-failure model; no missing-data handling; no capacity statement; no account-currency pin; no performance output; no dated-versus-perpetual distinction beyond the pinned perpetual run.
- `underspecified`: the quote currency resolved by `currency.NONE` (chart currency). Nothing else: venue class, symbol, timeframe, direction inputs, sizing, commission and date origin are pinned explicitly above, not left open.
- `contested`: the five page-versus-code contradictions in frontmatter; the pinned code at pinned defaults governs.
- The two-sided pin follows the two live entry paths at defaults, not a Scout preference: disabling a side is a rule change outside this record, and the long leg alone on spot would be a different strategy.
- The four-leg AND plus the contrarian RSI gate means signals are rare by construction and a position can persist indefinitely while alignment is absent; missed trends during unaligned stretches are the mechanism's known cost, stated here, not a defect to repair.

## Implementation status

- `implementation_status: not-implemented`. No Hummingbot, Qlib, n8n, Paper, Testnet or Live work has been performed from this record.
- Reproduction checklist for a future implementer (all values pinned above): `middle(9)`/`middle(26)`/`middle(52)` Ichimoku components with 25-bar displaced-cloud lookup and `ta.mom(close, 25)` Chikou leg plus hardcoded `ta.rsi(close, 14)` on `1d` BTCUSDT perpetual bars; strict `tenkan > kijun and mom > 0 and close > ss_high and RSI < 50` Long entry and strict `tenkan < kijun and mom < 0 and close < ss_low and RSI > 50` Short entry at bar close with `long_entry=true`, `short_entry=true`, gate from 2022-06-01; 30 percent equity market orders; 0.1 percent commission; no dual-signal bar possible; both `strategy.close` calls inert at defaults (reversal-only exits).

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`. This record is a normalized research artifact admitted (if passed) only for LOSSLESS HB_READY semantic expressibility; it is not profitability validation, not survivor promotion, and not Paper, Testnet, Mainnet or live-trading approval.
- Downstream performance work must apply the house execution overlay explicitly and must not misrepresent it as source-native behaviour; F-gates above must run before any adoption discussion.

## Related Wiki records

- No Wiki Brain write or ingestion was performed from this run (Scout boundary). No Wiki record is cited.

## Sources

- https://github.com/hasnocool/tradingview-pine-scripts (`Ichimoku Cloud with RSI (By Coinrule).pine` @ `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `5558c0c6a64f83a5d3cd2831f6f990722dd8fc51`, 3515 bytes)
- https://www.tradingview.com/script/2OfRyQSy-Ichimoku-Cloud-with-RSI-By-Coinrule/
- https://www.tradingview.com/pine-script-reference/v5/#fun_rsi
- https://www.tradingview.com/pine-script-reference/v5/#fun_mom
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v5/#fun_timestamp
- https://www.tradingview.com/pine-script-docs/concepts/strategies/
