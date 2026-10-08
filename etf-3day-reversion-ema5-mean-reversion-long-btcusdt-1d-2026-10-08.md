---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: 3-day high/low-chain EMA5 mean-reversion long on BTCUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2022-06-17
sources:
  - https://www.tradingview.com/script/Cvi9Zf0q-ETF-3-Day-Reversion-Strategy/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/ETF%203-Day%20Reversion%20Strategy.pine
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 3-day high/low-chain EMA5 mean-reversion long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, fetched 2026-10-08):

- Canonical page: https://www.tradingview.com/script/Cvi9Zf0q-ETF-3-Day-Reversion-Strategy/ (`ETF 3-Day Reversion Strategy`, Strategy by TradeAutomation, `OPEN-SOURCE SCRIPT`, page `updated_at` 2022-06-17, adopted as `source_as_of`; first-version stamp on the same page 2022-01-04).
- Page-stated lineage (verbatim substance): "a modification of the 3-day Mean Reversion Strategy from the book High Probability ETF Trading by Larry Connors and Cesar Alvarez"; the book rules are quoted on the page (1-day timeframe; price above the 200-day SMA and below the 5-day SMA; lower lows and lower highs 3 consecutive days; buy on the close; exit when the close crosses above the 5-day SMA). The author discloses two deliberate deviations from the book: an EMA trend-line replaces the book's SMA ("consistently works better when using an EMA"), and the exit EMA length is adjustable. The page prose further claims the system is "up nearly 10% YTD going long on QQQ and SPY" — prose only, with no Strategy Tester table/figure provenance anywhere on the page; this record treats that sentence as unverified page prose, not evidence (see Evidence).
- Page/chart context at read time is an equity-ETF display setting, not a strategy rule: the pinned script takes no symbol, timeframe, session, or venue input and reads only `high`/`low`/`close` plus bar `time`.
- Immutable code provenance: hasnocool mirror file `ETF 3-Day Reversion Strategy.pine` at pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (verified still the remote HEAD via `git ls-remote` this run), blob `8165d5650290d43d99e6f980092f1d7397b3d28f`. The mirror header (`Script Name: ETF 3-Day Reversion Strategy`, `Author: TradeAutomation`, Connors/Alvarez lineage in Description) matches the canonical page, and the embedded Pine block carries the exact declaration, date-window inputs, Rule1/Rule2/Rule3 lines, dual EMA-5 computation, and the two live order calls plus the out-of-window `close_all` quoted under Signal. The mirror text carries no explicit `//@version` pragma; its call namespaces (`ta.ema`, `ta.crossover`, `input.time`, `input.bool`, `input.int`, `strategy.commission.cash_per_order`, `strategy.close_all`) match the v5 surface used across this pool's records.
- Text census over the pinned block: 0 `request.*`, 0 `security(`, 0 `timeframe(`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`, 0 `alert(`/`alertcondition`, 0 `strategy.short`, 0 `volume`, 0 `open`. Live order calls are exactly two inside the in-window branch (`strategy.entry("Long", strategy.long, ...)`, `strategy.close("Long", when=...)`) plus one `strategy.close_all()` in the out-of-window branch.

Licence and rights: the canonical page is an open-source publication by TradeAutomation (a declared modification of the Connors/Alvarez book rule). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `connors`, `alvarez`, `Cvi9Zf0q`, `3-day reversion`, `ExitEMA`, and `lower highs` return no strategy record using this source, author-page, or signal — the only `TradeAutomation` hits are FMZ-port author credits on unrelated mechanisms (`cumulative-rsi-dual-threshold-long-btcusdt-1h-2026-10-08.md`: summed-RSI accumulation thresholds; `low-high-dip-tp-long-btcusdt-1d-2026-10-08.md`: low/high dip with fixed take-profit; `vidya-cmo-adaptive-slope-trend-btcusdt-1h-2026-10-05.md`: VIDYA+CMO slope trend). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` counts three consecutive lower *closes* for entry and three consecutive higher *closes* for exit (no range extremes, no moving-average leg anywhere), while this record enters on three consecutive lower *highs AND* lower *lows* under a below-EMA5 gate and exits on a close crossing back over EMA5; `ibs-mean-reversion-short-ethusdt-1h-2026-10-06.md` is an internal-bar-strength range-position ratio (short side, threshold exit — no sequential chains, no average); oscillator mean-reversion records (`rsi-classic`, `cumulative-rsi`, `catching-the-bottom`) fire on indicator levels, never on high/low chains. Five-axis distinction: mechanism differs (3-day high/low contraction under a short-average gate with average-recross exit, long-only, versus close-count chains, IBS ratios, or oscillator levels), signal construction differs (no pool record evaluates `high<high[1] and low<low[1]` chains or `ta.crossover(close, EMA5)` exits), exits differ (average-recross close versus mirror counts, ratio thresholds, or reversal netting), source identity differs (TradeAutomation TV Jun-2022 `Cvi9Zf0q` plus hasnocool blob `8165d565`), and research frame is BTCUSDT `1d` (the book's own daily design timeframe).

## Economic mechanism

### Source-reported

A short-horizon pullback catcher for up-trend-filtered markets: after three straight days of lower highs and lower lows printed under the 5-day average, the decline is judged exhausted and a long is bought on the close; the position is held until strength is proven by the close crossing back over the 5-day average. The author's stated reason for the EMA substitution is better backtest behavior than the book's SMA; the adjustable exit length exists so the release point can be tuned. The author ships no stop, no target, no trailing order: the average-recross close is the entire risk control.

### Research interpretation

Contraction-plus-location mean reversion. Rule3 is a pure range-contraction chain (each day's range sits strictly inside the prior day's on both rails, three days running) — a volatility-compression footprint, not a close-momentum count. Rule2 (`close < EMA5`) adds location: the contraction must occur while price is already soft relative to its own 5-day average, so the entry buys weakness-inside-weakness rather than compression near highs. The exit (`crossover(close, EMA5)`) is the mirror: the trade is alive only while price remains under its short average, and the first close that reclaims it ends the trade. Because both the entry gate and the exit reference the same EMA-5 series, entry and exit are mutually exclusive on any single bar by construction (see Negative evidence). No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (10M capital, 100%-of-equity sizing, $1 cash-per-order commission), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration: `strategy(title="ETF 3-Day Reversion Strategy", shorttitle="ETF 3-Day Reversion Strategy", process_orders_on_close=true, overlay=true, commission_type=strategy.commission.cash_per_order, commission_value=1, initial_capital=10000000, default_qty_type=strategy.percent_of_equity, default_qty_value=100)`. `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned — load-bearing here, pinned explicitly, see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar) and `calc_on_order_fills` is unset (default false).
- Date window (inputs pinned): `StartTime = input.time(defval=timestamp('01 Jan 2012 05:00 +0000'))`, `EndTime = input.time(defval=timestamp('01 Jan 2099 00:00 +0000'))`, `InDateRange = time>=StartTime and time<=EndTime` — deterministic, causal (bar `time` only), true for every bar of the research horizon. Altering the bounds would be a different, unpinned rule.
- Averages (lengths pinned): `DayEMA5 = ta.ema(close, 5)` (entry gate line); `QEMA = ta.ema(close, input.int(200, ...))` (qualifier line, default-off — see dead leg below); `ExitEMA = ta.ema(close, input.int(5, ...))` (exit line; at defaults the identical series to `DayEMA5`, computed twice).
- Qualifier (input pinned): `EMAQualInput = input.bool(false, ...)` → at default, `Rule1 = close>0`, i.e. unconditionally true. The `EMAQualifier = close>QEMA` leg is computed but unread at defaults — dead code at the pinned configuration, recorded as such, never admitted.
- Entry long: `Rule2 = close<DayEMA5`; `Rule3 = high<high[1] and low<low[1] and high[1]<high[2] and low[1]<low[2] and high[2]<high[3] and low[2]<low[3]` (six strict comparisons = three consecutive lower highs AND three consecutive lower lows); live via `if (InDateRange)` → `strategy.entry("Long", strategy.long, when = Rule1 and Rule2 and Rule3)`. Equalities on any rail break the chain and fire nothing.
- Exit: `strategy.close("Long", when = ta.crossover(close, ExitEMA))` in the same in-window branch — evaluated on the completed-bar close under `process_orders_on_close=true`; strict cross semantics (touch without crossing fires nothing).
- Out-of-window: `if (not InDateRange)` → `strategy.close_all()` — a deterministic no-op on every in-horizon bar; the book is never forced flat inside the research window.
- Direction: long-only by code (sole `strategy.long` entry, zero short calls of any kind). The short side is explicitly absent, not inferred; flat is the only alternative state.
- Inert code, provably excluded: all three `plot` lines (display only; never read by any order condition); the `QEMA`/`EMAQualifier` computation at default-off (see above); the `close>0` arm of `Rule1` is a tautology gate, admitted as written.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` (Rule3 chains), `close` (EMA gates, crossover exit), plus bar `time` for the pinned date window. No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is the book's and the author's own design timeframe (1-day) and a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: longest causal chain is `Rule3` (`high[3]`/`low[3]`) plus the crossover prior-bar reference. First fully-defined signal evaluation at the 4th completed `1d` bar; the EMA-5 lines stabilize over the first few bars and the default-off EMA-200 qualifier leg over ~200 bars. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads OHLCV only; venue transfer is never presented as source-native semantics).
- Order timing: `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill. 0 `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule.
- Sizing/capital: the declaration's 100%-of-equity sizing, 10M initial capital, and $1 cash-per-order commission lines are pure event-neutral accounting, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned). The default is load-bearing and therefore pinned explicitly: repeat Rule1/2/3 bars during an open long are rejected no-ops, and re-entry is allowed immediately on the next qualifying bar after any exit (no cooldown specified — explicitly none, not invented). `strategy.close("Long")` with no open long, and `strategy.close_all()` on any in-window bar, are deterministic no-ops. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the book-rule quotation, the author's two declared deviations (EMA-for-SMA substitution, adjustable exit EMA length), the plot legend (green exit average, blue entry average), and one prose performance sentence ("up nearly 10% YTD going long on QQQ and SPY"). That sentence carries no Strategy Tester table, figure, trade count, date, or cost basis anywhere on the page — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the EMA-5-recross close is the sole exit path by construction, and the prose promises no stop or target.
2. Entry and exit are mutually exclusive on every bar: both reference the same default EMA-5 series, so `close<EMA5` (required for entry) and `ta.crossover(close, EMA5)` (required for exit, implying close above the line) cannot hold simultaneously — no same-bar entry/exit ordering ambiguity exists to resolve.
3. Dead qualifier leg named: at pinned `EMAQualInput=false` the `close>QEMA` (EMA-200) branch is unreachable; enabling it would be a different, unpinned rule (a regime-filtered adaptation), not this record.
4. Boundary ties fire nothing: six strict `<` comparisons in Rule3 (any equality breaks the chain), strict `ta.crossover` on exit, strict `>=`/`<=` window edges — ties never invent an order.
5. Flat-state determinism: `strategy.close("Long")` with no open position and in-window `strategy.close_all()` are no-ops; `strategy.entry` while already long is rejected under pinned pyramiding 0. No bar can produce an undefined position transition.
6. Seed cannot print a ghost: `Rule3` needs six settled prior-rail comparisons and the crossover needs a prior bar — the leading `na` bars satisfy no order condition by themselves.
7. Display isolation: the three `plot` lines never enter any order condition; toggling visibility cannot alter any admitted event.
8. The window, lengths, qualifier toggle, and long-only direction are pinned, not removed: moving the 2012/2099 bounds, retuning 5/200, enabling the qualifier, or adding a stop/target/cooldown/short side would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 3-day high/low chains / below-EMA5 gate / EMA-5-recross exit / long-only / qualifier-off / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Chain relevance: entry on 2-day chains (drop the `[2]<[3]` pair) must not improve net expectancy; fail ⇒ the third contraction day is decorative and the system is a plain 2-day pullback holder.
- F2 — Exit relevance: holding each entry for a fixed research-defined bar count instead of the EMA-5 recross must not improve net expectancy; fail ⇒ the average-reclaim release adds nothing over time exits.
- F3 — Gate relevance: entry on Rule3 alone (drop the `close<EMA5` location gate) must not improve net expectancy; fail ⇒ buying contraction anywhere beats buying weakness-inside-weakness and the location gate is decorative.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The OHLCV-only long/flat logic ports to perps or spot without structural change (no short side exists to disable for spot-only deployment). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The book's equity-ETF daily origin transfers as mechanism only: 24/7 crypto has no opens/gaps/sessions for the rule to read, so overnight-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Source-frame transfer: the rule was designed for daily equity index ETFs (QQQ/SPY per the page prose); daily-BTC behavior is asserted by mechanism transfer, not proven to Hermes — backtest evidence stays absent until downstream reproduction.
- Long-only flat states: bear regimes print no signal and the book sits flat; sustained downtrends are simply unharvested by construction.
- No price stop: adverse excursion after entry has no guardrail beyond the EMA-5 recross; a vertical-against move exits only when the average is reclaimed, which can be far.
- Warmup cost: the default-off EMA-200 leg aside, the live chain needs ~4 completed bars, so the system is blind for the first few days of any 1d evaluation window.
- Performance prose is not evidence: the page's "nearly 10% YTD on QQQ/SPY" sentence has no table/figure provenance and is cited here only to be disclaimed, never relied upon.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-08): https://www.tradingview.com/script/Cvi9Zf0q-ETF-3-Day-Reversion-Strategy/
- Pinned mirror at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (remote HEAD, verified via `git ls-remote` this run), blob `8165d5650290d43d99e6f980092f1d7397b3d28f`: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/ETF%203-Day%20Reversion%20Strategy.pine
- Book lineage as cited by the strategy page: Larry Connors and Cesar Alvarez, "High Probability ETF Trading" (3-day mean-reversion rule; author-declared EMA modification recorded above).
- Pine v5 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
