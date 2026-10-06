---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Ichimoku Cloud with ADX trend-filter system on BTCUSDT 1d bars
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-18
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts
  - https://www.tradingview.com/script/je5bIJeR-Ichimoku-Cloud-with-ADX-By-Coinrule/
  - https://www.tradingview.com/pine-script-reference/v5/#fun_dmi
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v5/#fun_input
  - https://www.tradingview.com/pine-script-reference/v5/#fun_timestamp
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The stable page's Long Position list requires '-DI is greater than +DI' with 'ADX is greater than 45' plus a 'MACD line crosses over the signal line', and its Short Position list requires '+DI is greater than -DI' with 'ADX is less than 45' plus a 'MACD line crosses under the signal line', while the pinned code contains 0 `macd` occurrences and fires its Long entry on the exact inverse DMI/ADX legs (`pos_dm > neg_dm and avg_dm < 45`) and its Short entry on (`pos_dm < neg_dm and avg_dm > 45`). The executable Pine block governs; the page prose is recorded as contradicted, not repaired."
  - "The stable page suggests the script 'also works well on MATIC (15m timeframe), ETH (5m timeframe), and SOL (15m timeframe)' with an `interval: 60` chart snapshot, while this record pins a single `1d` evaluation run. The pinned code contains 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references and 0 `input.timeframe`, so the rule is timeframe-agnostic and the `1d` run is a research-pinned declaration exactly as in the already-admitted EHMA, Kaufman-pivot and DMI records — not a source claim about the optimal timeframe."
  - "The pinned code declares `Stop_loss = input(1) / 100`, `Take_profit = input(5) / 100`, `longStopPrice = strategy.position_avg_price * (1 - Stop_loss)` and `longTakeProfit = strategy.position_avg_price * (1 + Take_profit)`, but neither `longStopPrice` nor `longTakeProfit` reaches any `strategy.*` call (0 order references outside their own definition lines). They are dead computations, not an exit rule; the only live exits are the reversal `strategy.close` calls documented under Signal, and no stop/target/trailing/time exit exists in executable code."
  - "The stable page states 'The script is backtested from 1 January 2022 and provides good returns' with no sample table, no metric, no baseline and no figure, while the pinned code gates every entry on `timePeriod = time >= timestamp(syminfo.timezone, 2022, 1, 1, 0, 0)`. The date origin matches (2022-01-01) but the returns claim is unverifiable as printed and is recorded as a bare claim, not as evidence."
---

# Ichimoku Cloud with ADX trend-filter system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/hasnocool/tradingview-pine-scripts
- Full commit SHA: `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (commit date 2024-09-18T10:39:33Z). The GitHub `ls-remote` for HEAD returned this same SHA on 2026-10-06, so it is still the repository head at research time.
- Exact file path: `Ichimoku Cloud with ADX (By Coinrule).pine` (spaces and parentheses in filename preserved verbatim).
- Relevant stable public URL of the mirrored script: https://www.tradingview.com/script/je5bIJeR-Ichimoku-Cloud-with-ADX-By-Coinrule/ (`Ichimoku Cloud with ADX (By Coinrule) — Strategy by Coinrule`), found by web search on 2026-10-06. Its published title, author (`Coinrule`), opening Ichimoku/DMI paragraphs, 30-percent sizing note and 0.1-percent fee note match the mirror file's `Script Name:` / `Author:` / `Description:` headers and the pinned declaration, which corroborates the mirror rather than replacing it as the immutable artifact. The page's Long/Short bullet lists contradict the pinned code on DMI direction, ADX side and MACD (recorded contradictions 1–4; the code governs).

Primary-source checksums pinned 2026-10-06:

- File 3928 bytes, SHA-256 `28936769ad613e568468da992bcd197d73a2fac6fb81a78c4ee433d5afa35177`, 143 lines as stored.
- Independent remote check: the GitHub Contents API for that path at the pinned ref lists blob `65f5c24063e6a24658ca15658bbdda9505be2c1c` with size 3928, and the raw file fetched back by the pinned commit SHA is byte-identical to the local mirror artifact (identical SHA-256 via `cmp`), so the pinned bytes are the bytes GitHub serves.

Artifact structure as printed: a `Script Name:` line (`Ichimoku Cloud with ADX (By Coinrule)`), an `Author:` line (`Coinrule`), a truncated `Description:` paragraph (Ichimoku collection premise; the mirror truncates with `The Ichimoku...`), a `PineScript code:` section with a line-numbered dump, and an `Expand (76 lines)` trailer. The executable Pine block is 76 lines (`//@version=5` with an MPL-2.0 header, one `strategy()` declaration, one `showDate` input, one `timestamp()` gate, two dead stop/target inputs plus two dead `position_avg_price` lines, six Ichimoku length/offset/direction inputs, the `middle()` function, five Ichimoku component lines, six plot/fill lines, two displaced-cloud lookback lines, one `ta.dmi(14, 14)` call, six signal-component lines, two `strategy.entry` calls and two `strategy.close` calls). Everything gate-relevant below is read from those 76 lines.

Licence and rights: the pinned block prints `// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/` with author credit `// © Coinrule`. This record cites and normalizes the rule and reproduces no source code block beyond single-line declarations already quoted for gate evidence.

Pre-write dedup (2026-10-06): a word-boundary search of the current working tree (excluding `.git`) for `ichimoku`, `je5bIJeR`, `coinrule`, `tenkan`, `kijun`, `senkou` and `kumo` returned 0 signal-construction matches — the only `ichimoku` hits in the seven records on `main` are passing mentions inside the EHMA, Kaufman-pivot and DMI dedup paragraphs about closed PR #20 (Ichimoku-RSI), never a signal input, and the only `coinrule` hits are the DMI record's own provenance; `gh pr list --state open` returned an empty list, so there is no open `research/*` PR to deduplicate against. The dedup set is therefore the seven records on `main` (Gann HiLo, VIDYA CMO-adaptive, P-Signal erf, Bookstaber ATR, Kaufman pivot breakout, EHMA range band, DMI Swings ADX-45) plus the closed research PRs (#6 LazyBear Wave Trend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI). Five-axis distinction: mechanism differs (five-line Ichimoku cloud position plus Chikou momentum plus asymmetric ADX trend-filter versus ATR-standardized change sign / displaced average-band flip / CMO-adaptive slope / erf dead-band / confirmed-pivot storage / Hull range band / contrarian ADX-only exhaustion / oscillator cross / dual-EMA cross / MACD zero-cross / Ichimoku-RSI), signal construction differs (strict six-leg AND of `tenkan/kijun`, `mom(close, 25)`, `close` versus displaced cloud, first-party `ta.dmi(14, 14)` triple with asymmetric `< 45` long / `> 45` short legs, no crossover of two series anywhere, no MACD anywhere), horizon is `1d` (coincides with Gann HiLo, Bookstaber, Kaufman pivot, EHMA and DMI, whose mechanisms differ), source identity differs in all cases (hasnocool `Ichimoku Cloud with ADX (By Coinrule).pine` @ `69969aea`, blob `65f5c24`, stable `je5bIJeR` versus hasnocool `DMI Swings`/`Pivot Point Breakout`/`EHMA Range Strategy` and FMZ 430857 / 427070 / 430552 / 440338 and the four closed sources), and direction handling is two-sided at pinned defaults (both `long_entry` and `short_entry` default true) versus the long-only DMI/EHMA/pivot records.

## Economic mechanism

### Source-reported

- Premise, as printed on the stable page: "The Ichimoku Cloud is a collection of technical indicators that show support and resistance levels, as well as momentum and trend direction. It does this by taking multiple averages and plotting them on a chart. It also uses these figures to compute a 'cloud' that attempts to forecast where the price may find support or resistance in the future."
- Authorship note, as printed: "The Ichimoku Cloud was developed by Goichi Hosoda, a Japanese journalist, and published in the late 1960s."
- Cloud reading guide, as printed: "The lines include a nine-period average, a 26-period average, an average of those two averages, a 52-period average, and a lagging closing price line." / "When the price is below the cloud, the trend is down. When the price is above the cloud, the trend is up." / "The above trend signals are strengthened if the cloud is moving in the same direction as the price."
- DMI reading guide, as printed: "DMI is simple to interpret. When +DI > -DI, it means the price is trending up. On the other hand, when -DI > +DI, the trend is weak or moving on the downside. The ADX does not give an indication about the direction but about the strength of the trend." / "Typically values of ADX above 25 mean that the trend is steeply moving up or down" / "Values of ADX above 45 may suggest that the trend has overextended and is may be about to reverse."
- Combination claim, as printed: "This strategy combines the Ichimoku Cloud with the ADX indicator to better enter trades." / "Long/Short orders are placed when these basic signals are triggered." The six-bullet Long/Short lists that follow contradict the pinned code (contradiction 1) and are not repeated as rules here.
- Cost realism, as printed: "The strategy assumes each order is using 30% of the available coins" and "A trading fee of 0.1% is also taken into account and is aligned to the base fee applied on Binance" — both match the pinned declaration (`default_qty_value=30`, `commission_value=0.1`).
- Date origin, as printed: "The script is backtested from 1 January 2022 and provides good returns." The date matches the pinned `timestamp(..., 2022, 1, 1, 0, 0)` gate; the returns phrase carries no sample, metric, baseline or figure (contradiction 4).
- No sample, no metric, no table, no figure and no performance number of any kind is printed anywhere in the artifact or on the stable page (census under Evidence).

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, a clean Ichimoku alignment (Tenkan above Kijun, close above the displaced cloud, close above its own 25-bar-ago print) marks a young uptrend that has cleared local supply, and requiring ADX to still be cool (`< 45`) with +DI dominant filters out late-stage parabolic extensions where reversals dominate; the mirror-image alignment (Tenkan below Kijun, close below the cloud, close below its 25-bar-ago print, ADX hot `> 45` with -DI dominant) marks a downtrend that has already consumed directional energy and is therefore the short side of the same filter. The bet is early-trend participation gated by a trend-strength ceiling on the long side and a trend-exhaustion floor on the short side — not a pure cloud breakout and not a pure ADX contrarian rule. The fixed 45 threshold is a selectivity filter bought with rarity on both sides. This is a ported technical-analysis hypothesis: the source supplies the component attribution but no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Primary signal: the six-leg AND at bar close (`tenkan/kijun` order, Chikou `mom` sign, `close` versus displaced cloud, DMI dominance, ADX side).
- Strength filter: the ADX leg itself (`< 45` for Long, `> 45` for Short) — asymmetric by source, not a research choice.
- Trend / regime filter: the Ichimoku legs (Tenkan/Kijun, Kumo position, Chikou) — no separate regime overlay exists.
- Direction gate: two boolean inputs (`long_entry`, `short_entry`, both default true) that enable/disable each side without altering the signal legs.
- Risk / exit: none. Exit is exclusively the opposite-side alignment event (position reversal); stop loss, take profit, trailing stop and time exit are all absent in executable code (the two `position_avg_price` lines are dead per contradiction 3).

No component is assumed to contribute alpha; ablation is required by the falsification plan. Because every leg is a strict inequality, equality on any leg fires neither side — a property of the pinned operators, not an assertion by the prose.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`. All statements hold at the pinned source defaults (`ts_bars=9`, `ks_bars=26`, `ssb_bars=52`, `cs_offset=26`, `ss_offset=26`, `long_entry=true`, `short_entry=true`, `showDate=true`, dead `Stop_loss=1`/`Take_profit=5`, `ta.dmi(14, 14)`, ADX threshold 45 asymmetric, `percent_of_equity` 30, 0.1 percent commission, gate from 2022-01-01); any other input combination is a different, unpinned rule.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (research-pinned single decision timeframe; the script itself is timeframe-agnostic — 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency to align).
- Inputs at decision bar `t`: `high[t-25..t]`, `low[t-25..t]` (through `ta.lowest`/`ta.highest` and the 25-bar displaced-cloud lookup), `close[t-25..t]` (through `ta.mom(close, 25)` and `close` versus cloud), `pos_dm[t]`, `neg_dm[t]`, `avg_dm[t]` (the DMI triple) and bar `time[t]` (date gate only). `open` is never read by the trading logic and `volume` occurs 0 times in the whole artifact.
- Order timing: the live order calls are two `strategy.entry` and two `strategy.close`, all market orders (no `limit`/`stop` arguments anywhere — 0 occurrences of each outside the dead stop/target variable names), and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true the broker emulator processes orders "on the closing tick of each bar", and for market orders "executes them before the next bar's open". This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false`. Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Date gate: `showDate = input(defval=true, title='Show Date Range')` (display only) and `timePeriod = time >= timestamp(syminfo.timezone, 2022, 1, 1, 0, 0)`. Both live entries carry `and timePeriod`; both live closes do not carry it directly but can only fire after an entry opened a position, so no position can exist before 2022-01-01 under this pin. Explicit consequence, recorded rather than repaired: bars before 2022-01-01 (including 2017–2021 Binance history) can never carry an entry under this pin, so the effective backtest scope starts 2022-01-01; the gate has no end date, so eligibility never expires. `timenow` occurs 0 times. The `timestamp()` call passes `syminfo.timezone` explicitly, so the boundary is the symbol's exchange timezone by source declaration.

**Lookback, formulas and warmup**

- Parameters as declared: `ts_bars=input.int(9, minval=1)`, `ks_bars=input.int(26, minval=1)`, `ssb_bars=input.int(52, minval=1)`, `cs_offset=input.int(26, minval=1)`, `ss_offset=input.int(26, minval=1)`, `long_entry=input(true)`, `short_entry=input(true)`, `[pos_dm, neg_dm, avg_dm]=ta.dmi(14, 14)` positionally (`diLength=14`, `adxSmoothing=14`). The official v5 `ta.dmi()` reference fixes the variant: it returns the `(+DI, -DI, ADX)` triple computed from the high/low/close series. The rule contains 0 `crossover`, 0 `crossunder`, 0 `ta.cross`, 0 `ta.ema`, 0 `ta.rsi`, 0 `macd`, 0 `request.*`, 0 `security(` and 0 division operators in executable code (the only 2 `/` characters outside comments sit in the dead `input(1) / 100` and `input(5) / 100` lines), so none of the tie-semantics, multi-timeframe, seeding-conflict, MACD-missing or zero-divisor blockers arise in the live legs.
- Exact formulas, verbatim structure at defaults:
  - `middle(len) => math.avg(ta.lowest(len), ta.highest(len))` (average of the lowest low and highest high over `len` bars per the official `ta.lowest`/`ta.highest`/`math.avg` references).
  - `tenkan = middle(9)`, `kijun = middle(26)`, `senkouA = math.avg(tenkan, kijun)`, `senkouB = middle(52)`.
  - `ss_high = math.max(senkouA[25], senkouB[25])`, `ss_low = math.min(senkouA[25], senkouB[25])` (the cloud plotted `ss_offset - 1 = 25` bars forward for display, read back 25 bars for the signal — a past reference, not a future reference).
  - `tk_cross_bull = tenkan > kijun`, `tk_cross_bear = tenkan < kijun` (strict; equality is neither).
  - `cs_cross_bull = ta.mom(close, 25) > 0` (i.e. `close[t] > close[t-25]`), `cs_cross_bear = ta.mom(close, 25) < 0` (strict; equality is neither).
  - `price_above_kumo = close > ss_high`, `price_below_kumo = close < ss_low` (strict; touching the cloud edge is neither).
  - `bullish = tk_cross_bull and cs_cross_bull and price_above_kumo and avg_dm < 45 and pos_dm > neg_dm`.
  - `bearish = tk_cross_bear and cs_cross_bear and price_below_kumo and avg_dm > 45 and pos_dm < neg_dm`.
  - No other signal variable exists in the artifact; census gives `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.cancel` 0, `limit =` 0 (outside dead names), `stop =` 0 (outside dead names).
- Mutual exclusivity: `bullish` requires `tenkan > kijun`, `mom > 0`, `close > ss_high`, `avg_dm < 45`, `pos_dm > neg_dm` while `bearish` requires the strict opposite on all five legs (`<`, `<`, `<`, `> 45`, `<`), so both legs can never fire on the same bar — every equality case fires neither. There is no dual-signal bar, no call-order dependence, and no priority choice anywhere in the rule.
- Dead code, stated so the reviewer need not guess: `Stop_loss`, `Take_profit`, `longStopPrice`, `longTakeProfit` occur only on their own four definition lines (census `position_avg_price` 2, both inside the dead lines) and reach 0 `strategy.*` calls; the two `/` divisions are inside those same dead lines. They alter no trade and are recorded as non-material dead computation, not as a missing rule.
- Warmup, derived from the pinned code because the source declares none: no order can be created before the first bar on which all of `middle(52)`, the 25-bar cloud lookup, `ta.mom(close, 25)` and the full `ta.dmi(14, 14)` triple are defined (a function of the 52/26/25/14 lookbacks from bar 0, dominated by the 52-bar Senkou-B window plus its 25-bar displacement). A boolean `na` in a `when=` cannot open an order, so pre-warmup bars are flat by language semantics. `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically, and the rule references no lag beyond the windows above.
- Same-bar accounting: at most one of the two live entries can fire per bar (mutual exclusivity above); from flat an entry opens a one-sided position, from the opposite side the new entry reverses it, and while on the same side a repeated entry signal is rejected under the default `pyramiding` rule below. Orders fill on the same bar they are created, so no unfilled order survives into the next bar.

**Entry**

- Long entry: `strategy.entry('Long', strategy.long, when=bullish and long_entry and timePeriod)` — all three legs strictly defined, no OR branch, no alternative id.
- Short entry: `strategy.entry('Short', strategy.short, when=bearish and short_entry and timePeriod)` — mirror image, no OR branch, no alternative id.
- Both statements omit `qty`. Official reference: `qty` "The default is na, which means that the command uses the default_qty_type and default_qty_value parameters of the strategy declaration statement to determine the quantity" — here `strategy.percent_of_equity` with value `30`.
- Both statements omit `limit` and `stop`; official reference: `limit`/`stop` "The default is na, which means the resulting order is not of the limit or stop-limit type", so both are market orders.

**Exit**

- The pinned code contains exactly four order calls: 2 `strategy.entry`, 2 `strategy.close`. At pinned defaults (`long_entry=true`, `short_entry=true`) both closes are inert by construction: `strategy.close('Long', when=bearish and not short_entry)` is `bearish and false` = never, and `strategy.close('Short', when=bullish and not long_entry)` is `bullish and false` = never. Exits therefore occur exclusively through opposite-side entries (a fresh `bearish` bar reverses a long into a short; a fresh `bullish` bar reverses a short into a long).
- Stop loss: none in executable code (the `Stop_loss`/`longStopPrice` lines are dead per contradiction 3). Take profit: none in executable code (same). Trailing stop: none. Time limit or maximum holding period: none (the date input bounds entry eligibility from 2022-01-01 only, with no end). Flat state: reachable before the first entry and whenever neither leg fires after a reversal has been flattened only by an opposite reversal — the system is otherwise always in the market once the first entry fires. This is recorded, not repaired: adding a stop, target, trailing or time exit would be a rule change.
- The `strategy.close` pair is not redundant: if a chart user flips `short_entry` to false (or `long_entry` to false), the corresponding close becomes the signal exit for the remaining side. At the pinned defaults both are disabled, which is why the record pins the defaults explicitly.

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by waiting for the next opposite-alignment bar; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration, so the value comes from the language default: the v5 reference states the default is 0, meaning only one entry order in the same direction can be opened and additional same-side entries are rejected. With one live entry id per side (`'Long'`, `'Short'`), mutually exclusive entry legs, and same-bar-close fills, there is no second same-side position that could stack, and net exposure is always exactly one side. The record therefore records `pyramiding` as source-declared-by-language-default, and F3 forces the executing engine to confirm it. This is the same convergence treatment the PASS reviews of PRs #12, #21, #22 and #23 accepted.
- Same-direction re-entry: after an opposite-side reversal the system holds the new side, so the next same-alignment bar while already on that side is rejected under the default above; a fresh entry in that direction requires first being reversed to the other side (or flattened in a non-default input configuration). Orders fill on the same bar they are created, so no unfilled order survives into the next bar.
- Cooldown: none declared, and Pine's v5 strategy declaration exposes no cooldown field. A fresh entry requires a fresh full six-leg event while on the opposite side or flat, so cooldown semantics are provably irrelevant rather than missing.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy('Ichimoku Cloud with ADX (By Coinrule)', overlay=true, initial_capital=1000, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=30, commission_type=strategy.commission.percent, commission_value=0.1)`. (`overlay` is display only per the official `strategy()` signature.)
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0`, `margin_long`/`margin_short` at the v5 default, `pyramiding` (convergence above), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (moot: one live entry id per side with full reversals), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` (no price-dependent orders exist) and `use_bar_magnifier=false`.
- Sizing: `strategy.percent_of_equity` with value 30, i.e. each entry is 30 percent of available equity — declared in the code, therefore explicit and compounding.
- Direction: two-sided at pinned defaults (both inputs true). Because a short path is live, spot is deterministically inapplicable to the short leg (see Required data); the pinned run is a perpetual single-pair run.
- Nothing else is declared: `currency`, `slippage`, `margin_*`, `pyramiding`, `close_entries_rule`, `calc_*`, `max_bars_back` and `use_bar_magnifier` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variants and their parameters, source prices (high/low for the Ichimoku legs, close for Chikou/cloud/DMI), lookbacks (9/26/52/26/26/14/14/25), smoothing (the official `ta.dmi(14, 14)` triple and `math.avg`/`math.max`/`math.min`/`ta.mom`, no custom average), thresholds (ADX 45 asymmetric, strict DI dominance, strict cloud and momentum inequalities, the 2022-01-01 gate), comparison logic, AND structure, direction inputs, entries, exits, risk semantics (explicitly none live), sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults and functions. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE` and the latency/fill-failure model beyond the declared 0.1 percent commission; neither alters the signal, and both are recorded as `data gap` or boundary convention rather than filled. There is no perpetual-versus-dated question beyond the pinned perpetual run because the short leg requires a shortable instrument and the signal uses OHLCV only.

## Required data

- Instrument: BTCUSDT perpetual, research-pinned as the single-pair run of a venue-agnostic rule. The source script declares no venue, no exchange and no symbol (it runs on whatever chart it is attached to); because the pinned rule shorts at defaults, a shortable instrument is deterministically required and spot is excluded for the short leg. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: perpetual. The rule holds both long and short positions at defaults, so a margined long/short instrument is required. The artifact does not distinguish the perpetual from a dated future, which is `data gap`; it is immaterial to an OHLCV-only signal but must be pinned before any execution work. Funding itself is never read by the rule (0 occurrences) and the edge does not depend on funding PnL; funding as a cost is `data gap`.
- Spot applicability: not applicable to the pinned two-sided rule, because spot would require naked shorting. The long leg alone could run on spot, but that would be a modified single-side strategy and is not proposed.
- Venue: any venue listing BTCUSDT perpetual; no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, research-pinned for this record. The pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: `high`/`low` (Ichimoku `middle()` windows and the displaced-cloud lookup), `close` (Chikou `mom`, `close` versus cloud, DMI triple), bar `time` (date gate only). `open` and `volume` are never read by the trading logic.
- Fields not required and not used, each absent from the pinned live legs: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state. The calendar is gated only by the explicit from-2022-01-01 `timePeriod` expression (see Signal). The page's MACD is absent from the pinned code (0 occurrences) and is therefore not a data dependency of this record.
- Point-in-time: every input at bar `t` is contemporaneous or a deterministic function of bars at or before `t` (Ichimoku windows ending at `t`, cloud values from `t-25`, `mom` over `[t-25, t]`, DMI triple at `t`, `time[t]`); there is no future reference (the Senkou forward offset is display-only and the signal reads it back), no negative shift in any order input, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: bar open times of a 1-day BTCUSDT perpetual series compared against the explicitly exchange-timezone-resolved 2022-01-01 origin (`timestamp(syminfo.timezone, ...)` by source declaration).
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. The `na` rule that matters is the language one: indicator outputs are `na` until their lookbacks are satisfied, and a boolean `na` in `when=` cannot open an order — this is what fixes the warmup.
- Funding, fee and spread needs: the source declares a 0.1 percent commission per the code and the stable page; spread, slippage beyond the documented 0-tick default, impact, funding accrual and latency are `data gap`, never a modeled zero. Word-boundary census of the pinned 3928-byte artifact gives sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, profit factor 0, backtest 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, take profit 0 (outside the dead variable names), trailing 0, margin 0, equity 1 (the `percent_of_equity` token), commission 3 (type, value, and the stable-page-corroborated 0.1).

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market orders, created only by the two live `strategy.entry` calls (the two `strategy.close` calls are inert at pinned defaults and become signal exits only in non-default input configurations). There is no limit order, no stop order, no stop-limit, no OCA group and no conditional price order anywhere in the live rule (0 `strategy.exit`, 0 `strategy.order`, 0 `limit`/`stop` order arguments outside dead names), so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumptions are never exercised, because they apply only to price-dependent orders.
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

The artifact prints no performance result of any kind. Word-boundary census over the pinned 3928-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0; `time` occurs in the `timePeriod`/`timestamp()` gate only; `timeframe` occurs 0 times; `macd` occurs 0 times. There is no equity curve, no trade list, no table and no figure anywhere in the artifact.

What the source does report:

- Configuration only, from the pinned code: `//@version=5`, `middle()` over 9/26/52, offsets 26/26, `ta.dmi(14, 14)`, asymmetric ADX 45 (`< 45` Long / `> 45` Short) with strict DI-dominance legs, gate from 2022-01-01, `percent_of_equity` 30, `process_orders_on_close=true`, 0.1 percent commission.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: the Ichimoku reading guide, the DMI/ADX reading guide, the combination claim, the 30-percent realism note, the 0.1-percent fee note, the "backtested from 1 January 2022 and provides good returns" line, the MATIC-15m / ETH-5m / SOL-15m suggestions — unverifiable as printed and recorded as bare claims, not as evidence.
- Research-computed, not printed: at the pinned defaults the rule is a strict-inequality six-leg AND per side, so its trigger rate is set by joint Ichimoku-plus-ADX alignment rarity, not by any fixed price distance; and the two sides are mutually exclusive on every bar.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above. Third-party pages that re-host this script's statistics are not cited and contribute no number to this record.

### Independently reproduced

Not independently reproduced.

Only the following were performed: SHA-256 checksumming of the pinned artifact; a byte-identical re-fetch of the file by the pinned commit SHA from GitHub (identical SHA-256 via `cmp`) plus blob-id cross-check via the Contents API; a whole-artifact term and word-boundary census; enumeration of `strategy.*`, `input*`, `timestamp`, `ta.dmi`/`ta.mom`/`ta.lowest`/`ta.highest` call sites and of identifier occurrence counts; verification that `longStopPrice`/`longTakeProfit` reach 0 order calls and that the live legs contain 0 divisions; a same-bar mutual-exclusivity walk; reading of the public TradingView stable page title, author, description, sizing/fee/date lines and Long/Short bullet lists (title/author/sizing/fee/date match; bullets contradict per frontmatter); and live reading over HTTPS of the official TradingView documentation pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized, roi and trade counts are all 0 occurrences.
2. The performance-sounding prose ("provides good returns", MATIC/ETH/SOL suitability) carries no sample, no metric and no baseline, so it cannot be checked as printed.
3. The stable page advertises sub-hourly altcoin timeframes while the pinned rule evaluated here is a `1d` BTCUSDT run (recorded contradiction 2) — a reader following the prose would trade a different market and timeframe than this record.
4. The stable page's Long/Short bullets describe MACD crosses and inverted DMI/ADX legs that do not exist in the pinned code (recorded contradiction 1) — a reader following the prose would trade a different signal than this record.
5. The source computes stop/target-style lines from `position_avg_price` but never wires them to an order (recorded contradiction 3); the live rule therefore has no stop, no target and no time exit, so adverse excursion on either side is unbounded until the opposite alignment prints.
6. Cost model is the declared 0.1 percent commission with 0-tick slippage default and no spread, impact, funding-accrual or latency model — so any edge claim is only partially priced by the source.
7. Sizing is 30 percent of available equity per entry with no cash buffer, no volatility targeting and no risk layer of any kind; consecutive reversals compound turnover at full size.
8. Holding is unbounded: with no time exit and no level exit beyond the opposite-alignment event, exposure persists indefinitely until the mirror event — and if alignment never recurs, the position never closes.
9. The 2022-01-01 start gate excludes all pre-2022 history by source rule; any evaluation on earlier bars would contradict the pin.
10. No train/test split, no out-of-sample section and no walk-forward exists anywhere in the source.

## Falsification plan

All thresholds below are research-defined tests, never substitutes for the execution rules above (which are frozen: `middle(9/26/52)`, offsets 26/26, `ta.mom(close, 25)`, `ta.dmi(14, 14)`, asymmetric ADX 45, strict six-leg ANDs, `long_entry=true`, `short_entry=true`, gate from 2022-01-01, `percent_of_equity` 30 compounding, same-bar-close fills, 0.1 percent commission, 0-tick slippage, single `1d` timeframe, BTCUSDT perpetual).

- **F1 — Signal presence.** Threshold: at least 30 entries per side and at least 10 reversals per side on `1d` BTCUSDT perpetual bars from 2022-01-01; fail ⇒ the rule never trades this instrument/timeframe, record stays research-only.
- **F2 — Mutual-exclusivity audit.** Threshold: confirm on every bar that `bullish` and `bearish` never fire jointly and post-bar state is deterministic in all cases including all equality edges; fail ⇒ the exclusivity claimed above does not replay, pin the discrepancy and keep research-only.
- **F3 — Engine-default audit gate.** Threshold: the executing engine must confirm every recorded declaration and language default end to end — 30 percent equity sizing, same-bar-close fills, 0.1 percent commission, 0-tick slippage, once-per-bar evaluation, same-side entries rejected while on that side, opposite entries reversing, `na`-warmup with no pre-definition order, 2022-01-01 first eligible entry bar, both `strategy.close` calls inert at pinned defaults; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold: apply 0 / 1 / 2 / 5 / 10 bps of extra spread/slippage per side above the source-declared 0.1 percent, plus a separate funding-accrual sensitivity leg for the perpetual run; fail if net annualized return turns non-positive at 2 bps extra per side or net Sharpe falls to 0 or below at 5 bps extra per side ⇒ cost-dependent edge, no adoption.
- **F5 — Parameter perturbation.** Threshold: sweep Tenkan/Kijun over (9, 26), (7, 22), (12, 30), Senkou-B over 44/52/60, Chikou/mom lookback over 20/25/30 and ADX threshold over 40, 45, 50 with everything else frozen; fail if the sign of net return flips for the published cell or if fewer than half the cells produce positive net return ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold: split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day simple trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split ⇒ the rule requires a regime gate the source does not contain, no adoption.
- **F7 — Placebo.** Threshold: compare against buy-and-hold BTCUSDT on the identical window and against 1000 random entry-date sequences preserving the observed holding-time and side distribution; fail if observed net Sharpe does not exceed the 95th percentile of the placebo distribution ⇒ no evidence the Ichimoku-plus-ADX timing carries information.
- **F8 — Capacity and liquidity.** Threshold: fail if the required notional (30 percent of equity per entry) exceeds 5 percent of the trailing 30-day median daily volume of BTCUSDT perpetual ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F9 — Cross-instrument generalization.** Threshold: run the identical frozen rule on ETHUSDT perpetual and on one further major perpetual pair chosen before inspection; fail if 0 of 2 produce positive net return after the source commission plus 2 bps per side ⇒ single-asset overfit diagnosis.
- **F10 — Frozen forward window.** Threshold: forward test from 2026-10-06 to 2027-10-05 with every parameter frozen; fail if forward net Sharpe at source commission plus 2 bps per side is 0 or below ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `middle(9/26/52)`, offsets 26/26, `ta.mom(close, 25)`, `ta.dmi(14, 14)`, asymmetric ADX 45, strict six-leg ANDs, both direction inputs true, the from-2022-01-01 gate, no stop/take-profit/time exit, `pyramiding` at its documented default (one open same-side entry), `percent_of_equity` 30 compounding sizing, `process_orders_on_close` same-bar-close fills, 0.1 percent commission and 0 ticks slippage, the single `1d` timeframe and the BTCUSDT perpetual instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching venue, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The rule consumes only daily-bar high/low/close (plus bar time for the explicit date gate) and trades two-sided market orders at bar closes with equity-percentage sizing, all natively available on any 24/7 crypto perpetual venue; there is no session, holiday or opening-auction dependency, and the only calendar expression in the source is the explicit from-2022-01-01 eligibility gate. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, and none can invalidate the signal; the short leg requires a shortable perpetual, but no borrow, margin-call or funding-accrual logic enters the signal.
- Risks that remain crypto-specific and unmodeled by the source: spread and market-impact differences for 30-percent-equity market orders (`data gap`), venue fee-schedule differences versus the declared 0.1 percent (`data gap`), funding-accrual drag on the perpetual run (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and stablecoin-peg or quote-currency events (`data gap`).
- Timestamps are exchange-defined UTC daily candles; the 2022-01-01 origin is resolved in the symbol's exchange timezone per the explicit `syminfo.timezone` declaration.

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, funding-accrual, latency or fill-failure model; no missing-data handling; no capacity statement; no account-currency pin; no performance output; no dated-versus-perpetual distinction beyond the pinned perpetual run.
- `underspecified`: the quote currency resolved by `currency.NONE` (chart currency). Nothing else: venue class, symbol, timeframe, direction inputs, sizing, commission and date origin are pinned explicitly above, not left open.
- `contested`: the four page-versus-code contradictions in frontmatter; the pinned code at pinned defaults governs.
- The two-sided pin follows the two live entry paths at defaults, not a Scout preference: disabling a side is a rule change outside this record, and the long leg alone on spot would be a different strategy.
- The six-leg AND plus the asymmetric ADX filter means signals are rare by construction and a position can persist indefinitely while alignment is absent; missed trends during unaligned stretches are the mechanism's known cost, stated here, not a defect to repair.

## Implementation status

- `implementation_status: not-implemented`. No Hummingbot, Qlib, n8n, Paper, Testnet or Live work has been performed from this record.
- Reproduction checklist for a future implementer (all values pinned above): `middle(9)`/`middle(26)`/`middle(52)` Ichimoku components with 25-bar displaced-cloud lookup and `ta.mom(close, 25)` Chikou leg on `1d` BTCUSDT perpetual bars; strict `tenkan > kijun and mom > 0 and close > ss_high and avg_dm < 45 and pos_dm > neg_dm` Long entry and strict `tenkan < kijun and mom < 0 and close < ss_low and avg_dm > 45 and pos_dm < neg_dm` Short entry at bar close with `long_entry=true`, `short_entry=true`, gate from 2022-01-01; 30 percent equity market orders; 0.1 percent commission; no dual-signal bar possible; both `strategy.close` calls inert at defaults (reversal-only exits).

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`. This record is a normalized research artifact admitted (if passed) only for LOSSLESS HB_READY semantic expressibility; it is not profitability validation, not survivor promotion, and not Paper, Testnet, Mainnet or live-trading approval.
- Downstream performance work must apply the house execution overlay explicitly and must not misrepresent it as source-native behaviour; F-gates above must run before any adoption discussion.

## Related Wiki records

- No Wiki Brain write or ingestion was performed from this run (Scout boundary). No Wiki record is cited.

## Sources

- https://github.com/hasnocool/tradingview-pine-scripts (`Ichimoku Cloud with ADX (By Coinrule).pine` @ `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `65f5c24063e6a24658ca15658bbdda9505be2c1c`, 3928 bytes)
- https://www.tradingview.com/script/je5bIJeR-Ichimoku-Cloud-with-ADX-By-Coinrule/
- https://www.tradingview.com/pine-script-reference/v5/#fun_dmi
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v5/#fun_input
- https://www.tradingview.com/pine-script-reference/v5/#fun_timestamp
- https://www.tradingview.com/pine-script-docs/concepts/strategies/
