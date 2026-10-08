---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Williams %R level-cross mean-reversion long on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-06-08
sources:
  - https://www.tradingview.com/script/4TKWH069-Williams-R-Strategy/
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Williams %R level-cross mean-reversion long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (TradingView canonical strategy page plus its full open-source block, fetched 2026-10-09):

- Canonical page: https://www.tradingview.com/script/4TKWH069-Williams-R-Strategy/ (`Williams %R Strategy`, Strategy by Julien_Exe [MOD tag on page], `OPEN-SOURCE SCRIPT`, page `updated_at` 2023-06-08, adopted as `source_as_of`; first-version stamp on the same page 2023-06-07; release note 2023-06-09 `enable short positions`, which added the short legs quoted below with their guard defaulting to off).
- Page-stated rule (verbatim substance): the Williams %R momentum oscillator compares the current close with the highest high and lowest low over a lookback; a buy signal fires when %R crosses above the oversold level (upward price movement expected); a sell signal fires when %R crosses below the overbought level. Position management per the page: a long is initiated on a buy signal and closed when a sell signal is generated. The page carries no Strategy Tester table, figure, trade count, date range, or cost basis anywhere — this record claims no source-reported performance (see Evidence).
- Full 33-line `//@version=5` block read in the page's source viewer. Verbatim source declaration (note the absence it discloses, load-bearing for the derived status below): `strategy("Williams %R Strategy", overlay=true, initial_capital=100000, shorttitle="W%R Strategy")` — no `process_orders_on_close`, no `calc_on_every_tick`, no `pyramiding`, no `default_qty_*`, no `commission_*` lines. Source fills are therefore next-bar-open by Pine default; this record's same-bar-close execution is a separately identified researcher adaptation, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `length = input(14, "Length")`, `overboughtLevel = input(-20, "Overbought Level")`, `oversoldLevel = input(-80, "Oversold Level")`, `enableShort = input(false, "Enable Short Positions")`. This record pins all four defaults; enabling shorts or retuning any level/length would be a different, unpinned rule.
- Text census over the pinned block: 0 `request.*`, 0 `security(`, 0 `timeframe(`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`, 0 `alert(`/`alertcondition`, 0 `volume`, 0 `open`, 0 `plot`. Live order calls are exactly four (`strategy.entry("Buy", strategy.long)`, `strategy.close("Buy")`, `strategy.entry("Sell", strategy.short)`, `strategy.close("Sell")`), of which the two `Sell` legs are provably dead at the pinned `enableShort=false` (see Signal).
- Prose-vs-code sizing discrepancy, admitted honestly: the page prose says "the position size is set to 10% of the initial capital", but the pinned code carries no `default_qty_*` line at all, so no 10%-of-equity rule exists in the executable source. This record treats sizing as unspecified source accounting and replaces it with the explicit house overlay (see Execution assumptions), never presenting the prose sentence as a coded rule.

Licence and rights: the canonical page is an open-source publication by Julien_Exe. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly two: (1) research market/timeframe BTCUSDT `1d` (the script takes no symbol, timeframe, session, or venue input and reads only `high`/`low`/`close`); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open). Both adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Direction (long-only at the source default), indicator formula, lookback, thresholds, cross semantics, pyramiding default, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `ta.wpr`, `4TKWH069`, `Julien`, `Williams %R`, and `Williams Percent` return zero strategy records using this source, author, or oscillator (earlier broad `williams` hits are only dedup prose citing the Larry Williams 3-EMA channel streak of open PR #48). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-family reconstruction batch, unmerged), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `stochastic-ott-dual-trend-btcusdt-1d-2026-10-06.md` is a dual-OTT trailing-stop trend system whose stochastic leg is disabled by default and whose entries/exits are trend-line flips, never a single-oscillator level cross; `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` holds a Wilder `rma`-smoothed gain/loss ratio below 30 for entry (level-hold, not a cross) with its own exit construction, while this record fires only on strict `ta.crossover`/`ta.crossunder` events of an unsmoothed range-position ratio; `cumulative-rsi-dual-threshold-long`, `oversold-rsi-tight-sl-long`, and `catching-the-bottom-rsi-dip-reversal-long` are likewise RSI-family level/accumulation rules with stops or dip-confirmation legs this source never has. Five-axis distinction: mechanism differs (unsmoothed 14-bar range-position exhaustion cross, long-only, signal-line close exit, versus smoothed-ratio holds, dual-trend flips, or count chains), signal construction differs (no pool record evaluates `-100*(highest(high,14)-close)/(highest(high,14)-lowest(low,14))` with `-80`/`-20` cross events), exits differ (overbought-recross close versus opposite-threshold, time, or trailing exits), source identity differs (Julien_Exe TV Jun-2023 `4TKWH069` versus FMZ/ChaoZhang, hasnocool mirrors, or other TV authors), and direction handling differs (long-only at the pinned source default versus both-direction or short systems).

## Economic mechanism

### Source-reported

Short-horizon exhaustion reversal: when %R crosses back above −80 the market has printed an extreme low within its 14-bar range and is judged likely to rebound; the long is held until %R crosses back below −20, i.e. the close has reclaimed the top of its range and the oversold edge is spent. The author ships no stop, no target, no trailing order: the overbought-recross close is the entire risk control. Risk guidance is prose-only ("adjust the position size based on the available capital", "in conjunction with other technical analysis tools") and specifies no executable rule.

### Research interpretation

Unsmoothed range-position mean reversion. Unlike RSI-family records, %R performs no averaging of gains or losses: it is a pure positional readout of where the close sits inside the trailing 14-bar high/low range, so the entry buys the first bar that leaves the bottom quintile of that range and the exit sells the first bar that re-enters the top quintile from above. The signal is event-driven (two strict cross events) rather than state-driven (holding while below a level), which bounds holding time by construction: a trade can only survive while %R oscillates between the two levels without touching either. No leverage, sizing, or cost edge is embedded in the signal; sizing lines are absent from the source declaration, so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy("Williams %R Strategy", overlay=true, initial_capital=100000, shorttitle="W%R Strategy", process_orders_on_close=true)` — the first three lines are the source verbatim; `process_orders_on_close=true` is the predeclared researcher adaptation (source line carries no such argument). `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned — load-bearing here, pinned explicitly, see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar) and `calc_on_order_fills` is unset (default false).
- Oscillator (length pinned): `williamsR = -100 * (ta.highest(high, length) - close) / (ta.highest(high, length) - ta.lowest(low, length))` with `length = 14`. Bounded in `[-100, 0]` whenever the 14-bar range is non-zero; when `highest == lowest` (fourteen identical ranges) the quotient is `na` and fires nothing (see Negative evidence).
- Thresholds (pinned): `oversoldLevel = -80`, `overboughtLevel = -20`.
- Entry long: `buySignal = ta.crossover(williamsR, oversoldLevel)` — strict cross semantics: `williamsR[1] <= -80` and `williamsR > -80`; touches, holds below, and `na` bars fire nothing. Live via `if buySignal` → `strategy.entry("Buy", strategy.long)`, evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Exit: `sellSignal = ta.crossunder(williamsR, overboughtLevel)` — strict: `williamsR[1] >= -20` and `williamsR < -20`. Live via `if sellSignal` → `strategy.close("Buy")` on the same completed-bar close.
- Direction: long-only by pinned code path (`enableShort = false`): the sole live entry is `strategy.long`; the short side is explicitly absent at this configuration, not inferred; flat is the only alternative state.
- Dead legs, provably excluded: `if enableShort and sellSignal` → `strategy.entry("Sell", strategy.short)` and `if enableShort and buySignal` → `strategy.close("Sell")` are unreachable at the pinned default — dead code at this configuration, recorded as such, never admitted. Enabling them would be a different, unpinned rule.
- Display isolation: the block contains zero `plot`/`plotshape`/`bgcolor` calls — there is no display layer capable of influencing any order condition.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`lowest-high` (range top), `low` (range bottom), `close` (range position). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe and the oscillator's classic daily design frame — never presented as anything beyond that (see Limitations).
- Warmup: the 14-bar high/low window is only full from the 14th completed `1d` bar, and each cross event reads one prior bar, so the first signal-eligible bar is the 15th completed `1d` bar. No repainting, no negative shift, no future reference, no full-sample normalization; `calc_on_every_tick=false` gives exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads OHLCV only; venue transfer is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (declaration carries no such argument — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. 0 `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule.
- Sizing/capital: the source declaration carries only `initial_capital=100000` accounting with no quantity rule (the prose 10% sentence has no coded counterpart), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned). The default is load-bearing and therefore pinned explicitly: repeat `buySignal` bars during an open long are rejected no-ops, and re-entry is allowed immediately on the next qualifying cross after any exit (no cooldown specified — explicitly none, not invented). `strategy.close("Buy")` with no open long is a deterministic no-op. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the indicator definition, the cross-above-oversold / cross-below-overbought rule pair, the close-on-opposite-signal position management, the `enableShort` option (default off), and prose risk guidance. It ships zero performance numbers: no return, no win rate, no profit factor, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance. (A third-party mirror may carry academic-flavored citations around %R thresholds; none of that prose appears on the canonical page and none of it is relied upon here.)

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the overbought-recross close is the sole exit path by construction, and the prose promises no stop or target.
2. Entry and exit are mutually exclusive on every bar: entry requires `williamsR[1] <= -80` while exit requires `williamsR[1] >= -20` — no single prior-bar value satisfies both, so no same-bar entry/exit ordering ambiguity exists to resolve.
3. Dead short legs named: at pinned `enableShort=false` both `Sell` order lines are unreachable; enabling them would be a different, unpinned rule (a both-direction adaptation), not this record.
4. Boundary ties and flat ranges fire nothing: strict `ta.crossover`/`ta.crossunder` (equality on either side is not a cross); a zero 14-bar range yields `na`, and `na` conditions never open or close anything.
5. Flat-state determinism: `strategy.close("Buy")` with no open position is a no-op; `strategy.entry("Buy")` while already long is rejected under pinned pyramiding 0; the seed bars satisfy no order condition by themselves (each cross needs a settled prior bar).
6. Display-free source: zero plot-family calls exist anywhere in the block, so no visualization toggle can alter any admitted event.
7. The window, lengths, thresholds, short toggle, and long-only direction are pinned, not removed: retuning 14/−80/−20, enabling shorts, or adding a stop/target/cooldown/session filter would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame and same-bar-close fills, both predeclared above; every signal, threshold, default, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: %R(14) / −80 cross entry / −20 cross exit / long-only / shorts-off / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Entry relevance: entering on any bar merely printing %R below −80 (level-hold) instead of the strict cross above −80 must not improve net expectancy; fail ⇒ the cross event adds nothing over naive oversold holding.
- F2 — Exit relevance: holding each entry for a fixed research-defined bar count instead of the −20 recross must not improve net expectancy; fail ⇒ the overbought-reclaim release adds nothing over time exits.
- F3 — Oscillator relevance: replacing %R(14) with a same-threshold slow-stochastic %K cross (the closest range-position cousin) must not reproduce-or-beat net expectancy; fail ⇒ the record is an indicator-label variant of an already-pooled mechanism class.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The OHLCV-only long/flat logic ports to perps or spot without structural change (no short side exists to disable for spot-only deployment). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open` is never referenced), so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open; this record executes same-bar-close. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Long-only flat states: %R spends most bars mid-range printing no signal and the book sits flat; sustained downtrends are simply unharvested by construction.
- No price stop: adverse excursion after entry has no guardrail beyond the −20 recross; a vertical-against move exits only when the range top is reclaimed, which can be far.
- Warmup cost: the range window needs 14 completed bars plus one prior bar for the cross, so the system is blind for the first 14 bars of any 1d evaluation window.
- Performance evidence is absent: the canonical page reports no numbers at all; nothing here is calibrated, fitted, or tuned to any backtest.
- Single-oscillator whipsaw: in a choppy range %R can cross −80 and −20 in quick succession, printing entry-exit pairs with no structural filter — the source provides none and this record invents none.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-09): https://www.tradingview.com/script/4TKWH069-Williams-R-Strategy/
- Pine v5 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
