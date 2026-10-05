---
schema: strategy-research-record-v1
title: DMI Swings contrarian ADX-45 trend-exhaustion system on BTCUSDT 1d bars
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
  - https://www.tradingview.com/script/PDkNPkky-DMI-Swings-by-Coinrule/
  - https://www.tradingview.com/pine-script-reference/v4/#fun_dmi
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v4/#fun_input
  - https://www.tradingview.com/pine-script-reference/v4/#fun_timestamp
  - https://www.tradingview.com/pine-script-docs/v4/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The published script page states 'Our backtests suggest that this script performs well for very short-term scalping strategies on low time frames, such as the 1-minute', while this record pins a single `1d` evaluation run. The pinned code contains 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references and 0 `input.timeframe`, so the rule is timeframe-agnostic and the `1d` run is a research-pinned declaration exactly as in the already-admitted EHMA and Kaufman-pivot records — not a source claim about the optimal timeframe."
  - "The published page frames the premise as spotting 'extremely oversold and overbought conditions' where 'the trend has overextended and may be about to reverse', which implies a reversal edge with managed risk, but the pinned code contains no stop loss, no take profit, no trailing stop and no time exit of any kind (0 `strategy.exit`, 0 `strategy.stop`, 0 `strategy.order`, 0 `limit`/`stop` arguments); the only exit is the mirror-image DMI cross-side event. Any realized reversal payoff is emergent from that signal exit, not a rule."
---

# DMI Swings contrarian ADX-45 trend-exhaustion system on BTCUSDT 1d bars

## Provenance

Immutable GitHub source (this is the primary source actually read end to end):

- Repository URL: https://github.com/hasnocool/tradingview-pine-scripts
- Full commit SHA: `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (commit date 2024-09-18T10:39:33Z). The GitHub `ls-remote` for HEAD returned this same SHA on 2026-10-06, so it is still the repository head at research time.
- Exact file path: `DMI Swings (by Coinrule).pine` (spaces and parentheses in filename preserved verbatim).
- Relevant stable public URL of the mirrored script: https://www.tradingview.com/script/PDkNPkky-DMI-Swings-by-Coinrule/ (`DMI Swings (by Coinrule) — Strategy by Coinrule`), found by web search on 2026-10-06; its published title, author, description paragraphs and ENTRY/EXIT blocks are verbatim identical to the mirror file's `Script Name:` / `Author:` / `Description:` headers, which corroborates the mirror rather than replacing it as the immutable artifact.

Primary-source checksums pinned 2026-10-06:

- File 2378 bytes, SHA-256 `3da54378e48662eb0417fbf9fa098c6bb489b36ca674a92577d401b3f5971804`.
- Independent remote check: the GitHub Contents API for that path at the pinned ref lists blob `5e782e3f1aba5fcfb63cbb0048dc691ee5fdbb7f` with size 2378, and the raw file fetched back by the pinned commit SHA is byte-identical to the local mirror artifact (identical SHA-256), so the pinned bytes are the bytes GitHub serves.

Artifact structure as printed: a `Script Name:` line (`DMI Swings (by Coinrule)`), an `Author:` line (`Coinrule`), a `Description:` paragraph (Directional Movement Index premise, +DI/-DI/ADX reading guide, contrarian overextension premise), a `PineScript code:` section with a line-numbered dump, and an `Expand (24 lines)` trailer. The executable Pine block is 24 lines (`//@version=4`, one `strategy()` declaration, seven `input()` declarations, two `timestamp()` assignments, the `window()` function, one `dmi()` call, one `strategy.entry`, one `strategy.close`). Everything gate-relevant below is read from those 24 lines. The artifact uses non-breaking spaces (277 U+00A0 occurrences) as ordinary whitespace; no token reading depends on them.

Licence and rights: the pinned block carries no licence header and no author-credit line inside the code (authorship is in the mirror `Author:` header and the stable page). This record cites and normalizes the rule and reproduces no source code block beyond single-line declarations already quoted for gate evidence.

Pre-write dedup (2026-10-06): a word-boundary search of the current working tree (excluding `.git`) for `dmi`, `coinrule`, `PDkNPkky` and `directional movement` returned 0 signal-construction matches — the only `adx` hits in the six records on `main` are falsification-gate diagnostics (trailing ADX-tercile regime splits used as measurement tools in the Bookstaber, P-Signal, VIDYA and Gann records, never as signal inputs) plus a passing mention inside the EHMA record's census; `gh pr list --state open` returned an empty list, so there is no open `research/*` PR to deduplicate against. The dedup set is therefore the six records on `main` (Gann HiLo, VIDYA CMO-adaptive, P-Signal erf, Bookstaber ATR, Kaufman pivot breakout, EHMA range band) plus the four closed research PRs (#6 LazyBear Wave Trend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI). Five-axis distinction: mechanism differs (contrarian ADX-45 trend-exhaustion long versus ATR-standardized change sign / displaced average-band flip / CMO-adaptive slope / erf dead-band / confirmed-pivot storage / Hull range band / oscillator cross / dual-EMA cross / MACD zero-cross / Ichimoku cloud), signal construction differs (first-party `dmi(14, 14)` triple with strict `+DI < -DI` entry / `+DI > -DI` exit, no crossover of two series anywhere), horizon is `1d` (coincides with Gann HiLo, Bookstaber, Kaufman pivot and EHMA, whose mechanisms differ), source identity differs in all cases (hasnocool `DMI Swings (by Coinrule).pine` versus FMZ 430857 / 427070 / 430552 / 440338 / hasnocool `Pivot Point Breakout.pine` / `EHMA Range Strategy.pine` and the four closed sources), and direction handling is long-only at pinned inputs (no direction input exists at all) versus two-sided or input-gated records.

## Economic mechanism

### Source-reported

- Premise, as printed: "The Directional Movement Index is a handy indicator that helps catch the direction in which the price of an asset is moving. It compares the prior highs and lows to draw three lines: Positive directional line (+DI), Negative directional line (-DI), Average direction index (ADX)."
- Reading guide, as printed: "When +DI > -DI, it means the price is trending up. On the other hand, when -DI > +DI, it means the price is trending down."
- Contrarian edge, as printed on the stable page: "This script aims to capture swings in the DMI, and thus, in the trend of the asset, using a contrarian approach. Trading on high values of ADX, the strategy tries to spot extremely oversold and overbought conditions. Values of ADX above 45 may suggest that the trend has overextended and is may be about to reverse."
- ENTRY, as printed on the stable page: "-DI is greater than +DI" and "ADX is greater than 45."
- EXIT, as printed on the stable page: "+DI is greater than -DI" and "ADX is greater than 45."
- Cost realism, as printed on the stable page: "The script considers a 0.1% trading fee to make results more realistic" — matches the pinned `commission_value=0.1` exactly.
- Timeframe suggestion, as printed on the stable page: "Our backtests suggest that this script performs well for very short-term scalping strategies on low time frames, such as the 1-minute" (recorded contradiction 1; no sample, metric, baseline or figure accompanies it).
- No sample, no metric, no table, no figure and no performance number of any kind is printed anywhere in the artifact (census under Evidence).

### Research interpretation

Falsifiable mechanism hypothesis: on a single 24/7 crypto instrument, an ADX reading above 45 marks a trend that has consumed most of its directional energy (overextension), and when that overextended trend is downward (-DI dominant) the contrarian long buys the exhaustion point where late sellers are spent; the mirror-image event (+DI reclaiming dominance while ADX is still hot) marks the exhaustion swing completing, which closes the long. The bet is post-overextension snap-back, not trend continuation and not a moving-average state. The fixed 45 threshold is a noise filter bought with selectivity (ADX rarely exceeds 45); the exit is not a level but the mirror-image event (a fresh +DI-dominant hot-ADX bar). This is a ported technical-analysis hypothesis: the source supplies the contrarian attribution but no behavioural argument, no sample and no evidence, so the mechanism is research interpretation, not source-reported fact.

Component roles, stated plainly because the source offers no composite structure:

- Primary signal: strict inequalities of the current bar's DMI triple (`avg_dm > 45 and pos_dm < neg_dm` to enter, `avg_dm > 45 and pos_dm > neg_dm` to exit).
- Strength filter: the ADX>45 leg itself — no separate regime filter exists.
- Trend / regime filter: none beyond ADX.
- Direction gate: none exists — the artifact declares no direction input; the only order id is `"long"` with `long=true`, which is what makes the pinned rule long-only and spot-applicable.

## Signal

Everything below is read from the pinned Pine block. Nothing in this section is `research-proposed`. All statements hold at the pinned source defaults (date inputs 2021-01-01 → 2112-01-01, `dmi(14, 14)`, ADX threshold 45, percent_of_equity 100, 0.1 percent commission); any other input combination is a different, unpinned rule.

**Formation timestamp and tradability**

- Decision series: completed `1d` bars of the pinned instrument (research-pinned single decision timeframe; the script itself is timeframe-agnostic — 0 `request.*` calls, 0 `security(` calls, 0 `timeframe` references, 0 `input.timeframe` — so exactly one decision timeframe is declared by this record, `1d`, with no multi-timeframe dependency to align).
- Inputs at decision bar `t`: `pos_dm[t]`, `neg_dm[t]`, `avg_dm[t]` (the DMI triple, exact functions of the high/low/close series per the official `dmi()` reference) and bar `time[t]` (date gate only). `open` is never read by the trading logic and `volume` occurs 0 times in the whole artifact (there are no `plot*` calls at all in this 24-line script).
- Order timing: the live order calls are one `strategy.entry` and one `strategy.close`, both market orders (no `limit`/`stop` arguments anywhere — 0 occurrences of each), and the declaration sets `process_orders_on_close=true`. Official first-party documentation states that when this parameter is true the broker emulator processes orders "on the closing tick of each bar", and the reference adds "If the orders are market orders, the broker emulator executes them before the next bar's open." This is exactly a completed-bar decision with same-bar-close execution; there is no next-bar-open fill anywhere in the rule.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the pinned declaration (0 occurrences of each). Official documentation states both default to `false`. Recorded as source-declared-by-language-default, not as a research-proposed choice; it also means no intrabar re-evaluation can create a second order on the same bar.
- Date gate: the artifact contains 7 `input()` declarations (fromMonth/fromDay/fromYear defaults 1/1/2021, thruMonth/thruDay/thruYear defaults 1/1/2112, showDate default true) combined as `start = timestamp(fromYear, fromMonth, fromDay, 00, 00)`, `finish = timestamp(thruYear, thruMonth, thruDay, 23, 59)`, `window() => time >= start and time <= finish ? true : false`, and both live order calls carry `and window()`. At the pinned defaults the gate admits every bar from 2021-01-01 through 2112-01-01. Explicit consequence, recorded rather than repaired: bars before 2021-01-01 (including 2017–2020 Binance history) can never carry a signal under this pin, so the effective backtest scope starts 2021-01-01; after `finish` both legs stop firing, so a position still open at 2112-01-01 would freeze. `timenow` occurs 0 times. The `timestamp()` calls omit the timezone argument, so Pine resolves them to the symbol's exchange timezone (same boundary convention as the already-admitted Gann HiLo and EHMA records).

**Lookback, formulas and warmup**

- Parameters as declared: `dmi(14, 14)` — `diLength = 14`, `adxSmoothing = 14` positionally. The official v4 `dmi()` reference fixes the variant: it returns the `[(+DI, -DI, ADX)]` triple computed from the high/low/close series. The rule contains 0 `crossover`, 0 `crossunder`, 0 `ta.cross`, 0 `ta.ema`, 0 `request.*`, 0 `security(` and 0 division operators in executable code (all `/` characters in the file sit inside `//` comments), so none of the tie-semantics, multi-timeframe, seeding-conflict or zero-divisor blockers that closed earlier PRs arise here.
- Derived conditions, exact, at defaults:
  - Long entry condition: `strategy.entry(id="long", long=true, when = avg_dm > 45 and pos_dm < neg_dm and window())`.
  - Long exit condition: `strategy.close("long", when = avg_dm > 45 and pos_dm > neg_dm and window())`.
  - No other order call exists in the artifact: census gives `strategy.close_all` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.stop` 0, `strategy.cancel` 0, `strategy.risk.*` 0, `limit =` 0, `stop =` 0, `strategy.long`/`strategy.short` constants 0 (direction is carried by the v4 `long=true` argument, not the strategy.* constants).
- Mutual exclusivity (stronger than the #21 dual-signal table): entry requires `pos_dm < neg_dm` and exit requires `pos_dm > neg_dm` on the same bar's single triple, so both legs can never fire on the same bar — the equality case fires neither. There is no dual-signal bar, no call-order dependence, and no priority choice anywhere in the rule.
- Warmup, derived from the pinned code because the source declares none: `dmi()` is `na` until its lookbacks are satisfied, and a boolean `na` in a `when=` cannot open an order, so no order can be created before the first bar on which the full triple is defined (a function of the 14/14 lookbacks from bar 0). `max_bars_back` is not declared; official documentation states the required history buffer is detected automatically, and the rule references no lag beyond the DMI lookbacks.
- Same-bar accounting: at most one of the two live calls can fire per bar (mutual exclusivity above); from flat an entry opens a long, from long the exit closes it, and while long a repeated entry signal is rejected under the default `pyramiding` rule below. No third state exists.

**Entry**

- Long entry: the single `strategy.entry` above, `when = avg_dm > 45 and pos_dm < neg_dm and window()` — all three legs strictly defined, no OR branch, no alternative id.
- Short entry: none exists anywhere in the artifact. Direction is therefore long-only: one live `strategy.entry` with `long=true`, zero short paths.
- The statement omits `qty`. Official reference: `qty` "The default is na, which means that the command uses the default_qty_type and default_qty_value parameters of the strategy declaration statement to determine the quantity" — here `strategy.percent_of_equity` with value `100`.
- The statement omits `limit` and `stop`; official reference: `limit`/`stop` "The default is na, which means the resulting order is not of the limit or stop-limit type", so it is a market order.

**Exit**

- The pinned code contains exactly two order calls: 1 `strategy.entry`, 1 `strategy.close`. At defaults exactly one close is live: `strategy.close("long", ...)` on `avg_dm > 45 and pos_dm > neg_dm and window()`.
- Stop loss: none. Take profit: none. Trailing stop: none. Time limit or maximum holding period: none (the date inputs bound *signal eligibility* only, and admit everything 2021→2112 at defaults). Flat state: reachable before the first entry and after every cross-side exit; the system is otherwise long. This directly contradicts the description's implied managed-reversal design (contradiction 2).

**Holding period, overlap and re-entry**

- Holding period: unbounded and determined entirely by waiting for the next hot-ADX cross-side bar; the source states no maximum or expected holding period.
- Maximum same-side concurrency: 1. `pyramiding` is not written in the declaration, so the value comes from the language default: the v4 reference states the default is 0, meaning only one entry order in the same direction can be opened and additional same-side entries are rejected. With a single live entry id (`"long"`), mutual-exclusive entry/exit legs, and same-bar-close fills, there is no second position that could stack. The record therefore records `pyramiding` as source-declared-by-language-default, and F3 forces the executing engine to confirm it. This is the same convergence treatment the PASS reviews of PRs #12, #21 and #22 accepted.
- Same-direction re-entry: after a cross-side exit the system is flat, so the next `-DI-dominant hot-ADX` bar opens a fresh long; while long, a further entry signal is rejected under the default above, and orders fill on the same bar they are created, so no unfilled order survives into the next bar.
- Cooldown: none declared, and Pine's v4 strategy declaration exposes no cooldown field. A fresh entry requires a fresh `avg_dm > 45 and pos_dm < neg_dm` event while flat, so cooldown semantics are provably irrelevant rather than missing.

**Parameters, sizing and pyramiding**

- Declared verbatim in the pinned declaration: `strategy(shorttitle='DMI swings', title='DMI swings', overlay=true, initial_capital=100, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1)`. (`overlay` is display only per the official `strategy()` signature.)
- Declaration parameters the code leaves unset, each recorded as source-declared-by-language-default with the official page that documents it: `currency=currency.NONE` ("in which case the chart's currency is used"), `slippage=0`, `initial_capital` is set (100), `margin_long`/`margin_short` at the v4 default 0, `pyramiding` (convergence above), `calc_on_order_fills=false`, `calc_on_every_tick=false`, `close_entries_rule="FIFO"` (moot: a single live entry id with full closes), `max_bars_back` auto-detected, `backtest_fill_limits_assumption=0` (no price-dependent orders exist) and `use_bar_magnifier=false`.
- Sizing: `strategy.percent_of_equity` with value 100, i.e. each entry is 100 percent of available equity — declared in the code, therefore explicit and compounding.
- Direction: long-only (see Entry). Spot is therefore the deterministic market type and no margined instrument is required (see Required data).
- Nothing else is declared: `currency`, `slippage`, `margin_*`, `pyramiding`, `close_entries_rule`, `calc_*`, `max_bars_back` and `use_bar_magnifier` all occur 0 times in the artifact.

**Reconstruction status**

Every field required to replay the rule — indicator variant and its parameters, source prices, lookback, smoothing (the official `dmi(14, 14)` triple, no custom average), thresholds (ADX 45, DI dominance, the 2021/2112 date gate), comparison logic, direction, entry, exit, risk semantics, sizing, pyramiding, concurrency, cooldown, timeframe, fill timing and warmup — is explicit either in the pinned source or in official first-party documentation of the pinned source's own language defaults and functions. The residual `underspecified` items are the exact quote currency of the account under `currency.NONE`, the exchange timezone of the 2021/2112 date gate, and the latency/fill-failure model beyond the declared 0.1 percent commission; none alters the signal, and all are recorded as `data gap` or boundary convention rather than filled. There is no perpetual-versus-dated question here because the pinned rule is long-only spot.

## Required data

- Instrument: BTCUSDT on spot, research-pinned as the single-pair run of a venue-agnostic rule. The source script declares no venue, no exchange and no symbol (it runs on whatever chart it is attached to); because the pinned rule never shorts, uses no margin and uses no leverage, spot is deterministically applicable and no futures, perpetual-or-dated, distinction can arise. Single pair, single instrument, no basket, no ranking, no cross-sectional step.
- Market type: spot. Long-only; naked shorting is never required because no short path exists.
- Spot applicability: fully applicable — the complete pinned rule (long entries, cross-side closes, 100 percent equity sizing) executes on spot.
- Venue: any venue listing BTCUSDT spot; no venue-selection rule, no listing or survivorship rule (the artifact states none).
- Timeframe: exactly one decision timeframe, `1d`, research-pinned for this record. The pinned script contains 0 `request.*` calls and 0 `security(` calls, so no lower- or higher-timeframe series is referenced by the rule and there is no multi-timeframe dependency to align. `use_bar_magnifier` is at its documented `false` default, so no lower-timeframe data is used for fills either.
- Fields used: the DMI triple at bar `t` (exact functions of the high/low/close series) and bar `time[t]` (date gate only). `open` and `volume` are never read by the trading logic (the script contains no `plot*` calls at all).
- Fields not required and not used, each absent from the pinned artifact: open interest, funding, mark or index price, basis, order book or depth, trade or aggressor feed, liquidation feed, on-chain data, options or Greeks, sentiment or news, macro series, cross-venue state, borrow data, margin state. The calendar is gated only by the explicit 2021/2112 `window()` expression (see Signal).
- Point-in-time: every input at bar `t` is contemporaneous (the DMI triple at `t`, `time[t]`) or a deterministic function of bars at or before `t`; there is no future reference, no negative shift in any order input, no future extrema, no full-sample normalization, no `timenow` (0 occurrences), and no `security` call of any kind, so the pinned rule contains no look-ahead leakage.
- Timestamp and timezone: bar open times of a 1-day BTCUSDT spot series compared against the exchange-timezone-resolved 2021-01-01/2112-01-01 defaults; the timezone argument is omitted, so Pine resolves it to the symbol's exchange timezone, and the artifact pins no timezone → `underspecified` boundary convention only (same treatment as the admitted Gann HiLo and EHMA records).
- Missing data: no gap, halt or stale-bar handling is specified anywhere in the source → `data gap`. Imputation would be `research-proposed` and is not proposed here. The `na` rule that matters is the language one: `dmi()` is `na` until its lookbacks are satisfied, and a boolean `na` in `when=` cannot open an order — this is what fixes the warmup.
- Funding, fee and spread needs: the source declares a 0.1 percent commission per the code and the stable page; spread, slippage beyond the documented 0-tick default, impact and latency are `data gap`, never a modeled zero. Word-boundary census of the pinned 2378-byte artifact gives sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, profit factor 0, backtest 0 (outside the inert `//Backtest dates` comment), funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, pyramiding 0, take profit 0, trailing 0, short 0, margin 0, equity 1 (the `percent_of_equity` token), commission 3 (type, value, and the stable-page-corroborated 0.1).

## Execution assumptions

Source-declared (quoted or read from the pinned declaration, the pinned code, or official first-party documentation of that same language):

- Order type: market orders, created only by the one live `strategy.entry` and the one live `strategy.close`. There is no limit order, no stop order, no stop-limit, no OCA group and no conditional price order anywhere in the rule (0 `strategy.exit`, 0 `strategy.order`, 0 `limit`/`stop` arguments), so there is no intrabar-path dependence and no maker/taker asymmetry to model. The broker emulator's documented intrabar assumptions are never exercised, because they apply only to price-dependent orders.
- Fill model: `process_orders_on_close=true` → official documentation: orders are processed "on the closing tick of each bar", and for market orders "the broker emulator executes them before the next bar's open". `calc_on_every_tick` and `calc_on_order_fills` default to `false`, so there is exactly one evaluation per completed bar. Completed-bar decision with same-bar-close execution.
- Signal-to-order delay: none. The order is created and filled on the same completed-bar close; the engine's "Order execution delay" override defaults to 0 ticks.
- Dual-signal bar: impossible by construction — entry and exit legs are mutually exclusive on the same bar's single DMI triple (state table under Signal); the position ends in exactly one deterministic state in all cases.
- Position limits: one position at a time, 100 percent of available equity per position, no same-side add-on (default `pyramiding`, convergence recorded above), no scaling, no grid, no martingale, no hedge, no shorting.
- Leverage and margin: unset in code → v4 defaults (`margin_long`/`margin_short` 0 → no position-size limit and no margin call); sizing is equity-percentage, so the rule never sizes by leverage and has no leverage-dependent edge. Spot cash only.
- Costs: `commission_type=strategy.commission.percent` with `commission_value=0.1`, i.e. 0.1 percent of order cash volume charged on the entry fill and again on the exit fill — source-declared, corroborated by the stable page; `slippage` defaults to 0 ticks per the official reference. No spread, no market-impact model appears anywhere in the artifact → the remaining cost legs are `data gap`; this record does not adopt a validated zero-cost assumption beyond the documented defaults.
- Latency: not modeled in source → `data gap`.
- Participation and capacity: not modeled in source → `data gap`; tested by the research-defined gate F8.
- Failure handling (partial fills, rejects, downtime): not addressed in source → `data gap`. The pinned rule places whole market orders only, and no partial-fill-dependent condition exists.
- Engine-settings overrides a chart user could apply (timeframe, symbol, initial capital, currency, pyramiding, commission, dates, order size, order execution delay) are not part of the pinned source; the code-declared values plus documented defaults above are the recorded strategy.
- Scout-vs-source split: the venue-agnostic script is evaluated here as one explicit single-pair run (BTCUSDT spot, `1d`); every other item above marked source-declared comes from the pinned declaration, the pinned code, or official TradingView documentation of that language. Nothing in this section is a Scout-added execution rule; every pass/fail cutoff used later is labeled `research-defined`.

## Evidence

### Source-reported

The artifact prints no performance result of any kind. Word-boundary census over the pinned 2378-byte artifact: sharpe 0, drawdown 0, cagr 0, return 0, win rate 0, annualized 0, roi 0, net profit 0, max drawdown 0, profit factor 0, strategy tester 0, open interest 0, funding 0, leverage 0, spread 0, capacity 0, turnover 0, cooldown 0, pyramiding 0, take profit 0, trailing 0; `time` occurs in the `window()`/`timestamp()` date-gate lines only; `timeframe` occurs 0 times. There is no equity curve, no trade list, no table and no figure anywhere in the artifact.

What the source does report:

- Configuration only, from the pinned code: `//@version=4`, `dmi(14, 14)`, ADX threshold 45 with `pos_dm < neg_dm` entry / `pos_dm > neg_dm` exit, date gate 2021-01-01 → 2112-01-01, `percent_of_equity` 100, `process_orders_on_close=true`, 0.1 percent commission.
- Qualitative claims, verbatim, with no sample, no metric, no baseline and no figure: the DMI reading guide, the contrarian overextension premise ("may suggest that the trend has overextended and is may be about to reverse"), the 1-minute-scalping backtest suggestion, the 0.1% fee realism note — unverifiable as printed and recorded as bare claims, not as evidence.
- Research-computed, not printed: at the pinned defaults the rule is a strict-inequality test of the current DMI triple, so its trigger rate is set by how often ADX exceeds 45, not by any fixed price distance; and the entry/exit legs are mutually exclusive on every bar.

No source-reported figure in this record comes from any other paper, article or repository; every claim is attributed to the single pinned artifact above. Third-party pages that re-host this script's statistics are not cited and contribute no number to this record.

### Independently reproduced

not independently reproduced

Only the following were performed: SHA-256 checksumming of the pinned artifact; a byte-identical re-fetch of the file by the pinned commit SHA from GitHub (identical SHA-256) plus blob-id cross-check via the Contents API; a whole-artifact term and word-boundary census; enumeration of `strategy.*`, `input*`, `timestamp`, `dmi` call sites and of identifier occurrence counts; a same-bar mutual-exclusivity walk; reading of the public TradingView stable page header, description and ENTRY/EXIT blocks (title/author/description/rules match only); and live reading over HTTPS of the official TradingView documentation pages cited under Sources. No market data was downloaded, no backtest was run, no Pine or third-party code was executed, and no statistic was recomputed from data.

### Negative evidence

1. The artifact prints zero performance numbers, so there is nothing to reproduce: sharpe, drawdown, cagr, return, win rate, annualized, roi and trade counts are all 0 occurrences.
2. The performance-sounding prose claims (overextension reversal, 1-minute scalping fitness) carry no sample, no metric and no baseline, so they cannot be checked as printed.
3. The source's own page advertises short-timeframe scalping while the pinned rule evaluated here is a `1d` run (recorded contradiction 1) — a reader following the prose would trade a different timeframe than this record.
4. The source implies a managed reversal edge while the code contains no stop, no target and no time exit (recorded contradiction 2).
5. Cost model is the declared 0.1 percent commission with 0-tick slippage default and no spread or impact model — so any edge claim is only partially priced by the source.
6. Sizing is 100 percent of available equity on every position: full-equity concentration, no cash buffer, no volatility targeting, no risk layer of any kind.
7. Holding is unbounded: with no time exit and no level exit beyond the mirror cross-side event, exposure persists indefinitely until the next hot-ADX cross-side bar — and if ADX never exceeds 45 again, the position never closes.
8. The 2021-01-01 start gate excludes all pre-2021 history by source rule; any evaluation on earlier bars would contradict the pin.
9. A long opened late in a steep decline can sit through further decline with no stop: the contrarian premise buys directly into -DI dominance, so adverse excursion is the mechanism's known cost, stated here, not a defect to repair.
10. No train/test split, no out-of-sample section and no walk-forward exists anywhere in the source.

## Falsification plan

All thresholds below are research-defined tests, never substitutes for the execution rules above (which are frozen: `dmi(14, 14)`, ADX 45, strict DI-dominance legs, 2021-01-01 → 2112-01-01 date gate, percent_of_equity 100 compounding, same-bar-close fills, 0.1 percent commission, 0-tick slippage, single `1d` timeframe, BTCUSDT spot).

- **F1 — Signal presence.** Threshold: at least 30 long entries and at least 10 cross-side exits on `1d` BTCUSDT spot bars from 2021-01-01; fail ⇒ the rule never trades this instrument/timeframe, record stays research-only.
- **F2 — Mutual-exclusivity audit.** Threshold: confirm on every bar that entry and exit legs never fire jointly and post-bar state is deterministic in all cases; fail ⇒ the exclusivity claimed above does not replay, pin the discrepancy and keep research-only.
- **F3 — Engine-default audit gate.** Threshold: the executing engine must confirm every recorded declaration and language default end to end — 100 percent equity sizing, same-bar-close fills, 0.1 percent commission, 0-tick slippage, once-per-bar evaluation, same-side entries rejected while long, `na`-warmup with no pre-triple order, 2021-01-01 first eligible bar; fail ⇒ pin the discrepancy in writing and keep research-only, no adoption.
- **F4 — Cost ladder.** Threshold: apply 0 / 1 / 2 / 5 / 10 bps of extra spread/slippage per side above the source-declared 0.1 percent; fail if net annualized return turns non-positive at 2 bps extra per side or net Sharpe falls to 0 or below at 5 bps extra per side ⇒ cost-dependent edge, no adoption.
- **F5 — Parameter perturbation.** Threshold: sweep DI length / ADX smoothing over (10, 10), (14, 14), (20, 20), (14, 21) and ADX threshold over 40, 45, 50 with everything else frozen; fail if the sign of net return flips for the published cell (14, 14, 45) or if fewer than half the cells produce positive net return ⇒ parameter-lottery diagnosis, no adoption.
- **F6 — Regime breakdown.** Threshold: split the sample into thirds by trailing 60-day realized volatility and, separately, by a 60-day simple trend-strength tercile; fail if net Sharpe is negative in at least two of three terciles in either split ⇒ the rule requires a regime gate the source does not contain, no adoption.
- **F7 — Placebo.** Threshold: compare against buy-and-hold BTCUSDT on the identical window and against 1000 random entry-date sequences preserving the observed holding-time distribution; fail if observed net Sharpe does not exceed the 95th percentile of the placebo distribution ⇒ no evidence the overextension timing carries information.
- **F8 — Capacity and liquidity.** Threshold: fail if the required notional (100 percent of equity) exceeds 5 percent of the trailing 30-day median daily volume of BTCUSDT spot ⇒ capacity-capped, record the ceiling and block any size scaling.
- **F9 — Cross-instrument generalization.** Threshold: run the identical frozen rule on ETHUSDT spot and on one further major spot pair chosen before inspection; fail if 0 of 2 produce positive net return after the source commission plus 2 bps per side ⇒ single-asset overfit diagnosis.
- **F10 — Frozen forward window.** Threshold: forward test from 2026-10-06 to 2027-10-05 with every parameter frozen; fail if forward net Sharpe at source commission plus 2 bps per side is 0 or below ⇒ reject; no parameter may be changed to re-run it.

Global no-retuning rule: `dmi(14, 14)`, ADX 45, strict DI-dominance legs, the 2021/2112 date gate, no stop/take-profit/time exit, `pyramiding` at its documented default (one open same-side entry), `percent_of_equity` 100 compounding sizing, `process_orders_on_close` same-bar-close fills, 0.1 percent commission and 0 ticks slippage, the single `1d` timeframe and the BTCUSDT spot instrument are frozen. No gate may be rescued by changing a parameter, widening a window, switching venue, dropping a cost leg or re-defining a metric after seeing results.

## Crypto portability

`direct` — with a narrow meaning. The rule consumes only the DMI triple of daily bars and trades long-only market orders at bar closes with full-equity sizing, all natively available on any 24/7 crypto spot venue; there is no session, holiday or opening-auction dependency, and the only calendar expression in the source is the explicit 2021/2112 eligibility gate. `direct` refers only to mechanism, signal and instrument applicability; it is explicitly not a claim of crypto performance, which is `unproven` because the artifact prints no result.

Portability-relevant facts:

- No funding, open interest, mark or index price, liquidation feed, order book, aggressor side, on-chain data or options input is used, and none can invalidate the signal; no shorting means no borrow, no margin call and no funding accrual exist anywhere in the pinned rule.
- Risks that remain crypto-specific and unmodeled by the source: spread and market-impact differences for a full-equity market order (`data gap`), venue fee-schedule differences versus the declared 0.1 percent (`data gap`), listing and delisting churn for anything other than BTCUSDT (`data gap`), venue fragmentation and custody risk (`data gap`), and stablecoin-peg or quote-currency events (`data gap`).
- Timestamps are exchange-defined UTC daily candles; the 2021-01-01 start bound is resolved in the symbol's exchange timezone per the omitted-timezone convention (`underspecified` boundary only).

Crypto portability is not authorization to trade and not evidence that the mechanism survives in crypto.

## Limitations

- `not independently reproduced`. Nothing in this record has been recomputed from data.
- `data gap`: no spread, impact, latency or fill-failure model; no missing-data handling; no capacity statement; no account-currency pin; no performance output.
- `underspecified`: the quote currency resolved by `currency.NONE` (chart currency) and the exchange timezone of the 2021/2112 date gate. Nothing else: venue, symbol and timeframe are research-pinned explicitly above, not left open.
- `contested`: the two page-versus-code contradictions in frontmatter; the code at pinned defaults governs.
- The long-only pin follows the absence of any short path in the source, not a Scout preference: adding a short leg is a rule change outside this record.
- The ADX-45 filter means signals are rare by construction and a position can persist indefinitely while ADX stays cool; missed trends during low-ADX stretches are the mechanism's known cost, stated here, not a defect to repair.

## Implementation status

- `implementation_status: not-implemented`. No Hummingbot, Qlib, n8n, Paper, Testnet or Live work has been performed from this record.
- Reproduction checklist for a future implementer (all values pinned above): `dmi(14, 14)` on `1d` BTCUSDT spot bars; strict `avg_dm > 45 and pos_dm < neg_dm` long entry and strict `avg_dm > 45 and pos_dm > neg_dm` long close at bar close; 2021-01-01 → 2112-01-01 eligibility gate; 100 percent equity market orders; 0.1 percent commission; no dual-signal bar possible.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`. This record is a normalized research artifact admitted (if passed) only for LOSSLESS HB_READY semantic expressibility; it is not profitability validation, not survivor promotion, and not Paper, Testnet, Mainnet or live-trading approval.
- Downstream performance work must apply the house execution overlay explicitly and must not misrepresent it as source-native behaviour; F-gates above must run before any adoption discussion.

## Related Wiki records

- No Wiki Brain write or ingestion was performed from this run (Scout boundary). No Wiki record is cited.

## Sources

- https://github.com/hasnocool/tradingview-pine-scripts (`DMI Swings (by Coinrule).pine` @ `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `5e782e3f1aba5fcfb63cbb0048dc691ee5fdbb7f`, 2378 bytes)
- https://www.tradingview.com/script/PDkNPkky-DMI-Swings-by-Coinrule/
- https://www.tradingview.com/pine-script-reference/v4/#fun_dmi
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
- https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
- https://www.tradingview.com/pine-script-reference/v4/#fun_input
- https://www.tradingview.com/pine-script-reference/v4/#fun_timestamp
- https://www.tradingview.com/pine-script-docs/v4/concepts/strategies/
