---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: MA-regime RSI-gated dip-cross trend-following long on ETHUSDT 1h bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2021-06-10
sources:
  - https://www.tradingview.com/script/XAiEh7nb-Maximized-Scalping-On-Trend-by-Coinrule/
  - https://help.coinrule.com/articles/407566-maximized-scalping-on-trend
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Maximized%20Scalping%20On%20Trend%20(by%20Coinrule).pine
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MA-regime RSI-gated dip-cross trend-following long on ETHUSDT 1h bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, live browser read 2026-10-08):

- Canonical page: https://www.tradingview.com/script/XAiEh7nb-Maximized-Scalping-On-Trend-by-Coinrule/ (`Maximized Scalping On Trend (by Coinrule)`, Strategy by Coinrule, `OPEN-SOURCE SCRIPT`, updated Jun 10 2021, adopted as `source_as_of`; first published Jun 9 2021).
- Page-chart context at read time: BINANCE ETH/USDT on a 1h chart — a display context, not a strategy rule (the script takes no symbol, timeframe, session, or venue input).
- Page-stated rules (verbatim substance): entry needs MA50 above MA100, RSI above 50, then the order is placed when the price crosses the MA9; the trade closes in profit when RSI exceeds 70 and otherwise when RSI falls below 30; each order uses 30% of available capital with one trade open at a time; a 0.1% fee aligned to the Binance base fee is assumed; the 1-hour timeframe returned the best results on average (15-minute also mentioned for higher frequency). The page's prose body says "crosses above the MA9" in one line — see the resolved discrepancy below; it is not admitted as a rule.
- Decisive first-party resolution of the above/below wording: the author's own Jun 9 2021 release note on the same page states that "entering the trade when the price crosses below the MA9 improves the results on average by 2.5 times on the 1-hour time frame". The author's official help article (https://help.coinrule.com/articles/407566-maximized-scalping-on-trend) likewise instructs "The price crosses below the MA9", and the published open-source block implements `crossunder(close, movingaverage_fast)`. Two executable/authoritative witnesses (code plus help article) plus the release note agree on below-MA9; only the marketing prose line says above. The admitted rule is the below-MA9 crossunder — documented here as a resolved, source-backed reading, not an invention.
- First-party help article further states the strategy "tends to open trades frequently, closing them on average in one and a half days" and reports "60.53% net profit on BNB/USDT on the 1Hour timeframe from January 2022 – November 2022" (source-reported figure with section provenance in that article; not independently reproduced — see Evidence).
- Immutable code provenance: hasnocool mirror file `Maximized Scalping On Trend (by Coinrule).pine` at pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (verified still the remote HEAD via `git ls-remote` this run), blob `6665c36bdb3081bf79b179232efbfe74002cb03f`, 3289 bytes. The mirror header (`Script Name`, `Author: Coinrule` / `© Coinrule`) matches the canonical page, and the embedded Pine v4 block is line-for-line identical to the live page's published Source-code tab as read this run (declaration, 2019-01-10 window defaults, 9/50/100 SMAs, `crossunder(close, movingaverage_fast)`, RSI 14/50/70/30, both order lines — code governs).
- Censuses over the pinned block: `strategy.entry` 1, `strategy.close` 1, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, `request.*` 0, `security(` 0, `timeframe(` 0, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `pyramiding` 0, `calc_on_every_tick` 0, `calc_on_order_fills` 0, `varip` 0, `volume` 0, `heikin` 0. Series read by order logic: `close` plus bar `time` inside the deterministic date window (causal, never future). `open`, `high`, `low`, and `volume` occur 0 times in any order-gating line. `plot` lines are display-only and never gate an order.

Licence and rights: the canonical page is an open-source publication by Coinrule. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `XAiEh7nb` and `Maximized Scalping` return 0 strategy records using this source or signal. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888), plus reconstruction-lane #58 — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `golden-cross-sma-regime-gated-long-btcusdt-1h-2026-10-08.md` (MA9/MA50 cross event with MA100 gate and reverse-cross exit — no price/MA cross, no RSI anywhere), `oversold-rsi-tight-sl-long-btcusdt-1h-2026-10-07.md` (RSI dip entry with an explicit price stop — this record has no price stop of any kind), `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` (pure RSI level reversal, no moving-average regime or cross event), `sideways-dmi-bollinger-breakout-long-btcusdt-4h-2026-10-07.md` (DMI sideways gate with Bollinger-band cross entry/exit — no SMA regime stack, no RSI). Five-axis distinction: mechanism differs (pullback dip-cross under MA9 inside an MA50/MA100 uptrend with an RSI-50 momentum gate, long-only), signal construction differs (no pool record fires on `crossunder(close, sma(close, 9))`; the entry event is unique on `main`), exits differ (dual RSI-threshold signal closes, 70/30, with Pine `or`/`and` precedence — no reverse-cross, no price level, no stop order), source identity differs (Coinrule TV Jun-2021 `XAiEh7nb` plus hasnocool blob `6665c36b`, plus the author's help article and release note), and research frame is ETHUSDT `1h` (the page's own display context and its stated best timeframe).

## Economic mechanism

### Source-reported

A short-horizon trend-riding dip buyer: the MA50-above-MA100 stack plus RSI above 50 establishes that a genuine uptrend with momentum is in place, and the cross of the price back under the fast MA9 times the entry as a pullback inside that trend rather than a breakout chase. The author calls the RSI legs a dynamically adapting stop/take-profit: RSI above 70 books the trade before the pull-back, RSI below 30 admits the trend has weakened. No fixed price stop, target, trailing, or time leg exists anywhere.

### Research interpretation

Regime-gated pullback timing with momentum-threshold bookkeeping. The slow stack (MA50 vs MA100) is sticky state that permits entries only in established uptrends; the RSI-50 gate is a coincident momentum filter on the same bar; the MA9 crossunder is the fast trigger converting a standing regime into an event. Because exits are pure RSI-threshold closes evaluated at the bar close, the whole book is fully determined by completed bars with no intrabar path dependence. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (1000 capital, 30%-of-equity sizing, 0.1% commission — the page's own 30%/0.1% framing confirms their accounting nature), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v4, defaults quoted — inputs unmodified):

- Declaration: `strategy(shorttitle='Maximized Scalping On Trend', title='Maximized Scalping On Trend (by Coinrule)', overlay=true, initial_capital=1000, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=30, commission_type=strategy.commission.percent, commission_value=0.1)`. `calc_on_every_tick` is unset (default false); `pyramiding` is unset (v4 language default 0: no additional same-direction entry while positioned — corroborated by the page's "opens a trade at a time", and it is load-bearing here, see Execution assumptions).
- Date window: `start = timestamp(2019, 1, 10, 00, 00)`, `finish = timestamp(2112, 1, 1, 23, 59)`, `window() => time >= start and time <= finish` — deterministic, causal (bar `time` only), true for every bar of the research horizon. Input defaults pinned (From Day 10 / From Year 2019 / Thru 2112-01-01); altering them would be a different, unpinned rule. `showDate = input(defval=true, ...)` is defined but never read by any line — write-only display state, provably inert (0 reads outside its declaration).
- Averages (all first-party deterministic `sma` on `close`, no variant/smoothing/source choice left open): `movingaverage_fast = sma(close, 9)`, `movingaverage_mid = sma(close, 50)`, `movingaverage_slow = sma(close, 100)` (length inputs pinned at 9/50/100).
- Momentum: `RSI = rsi(close, 14)` (length pinned 14); entry gate `RSI > 50` (strict; exactly 50 fails); exit thresholds `TP = 70`, `SL = 30` (inputs pinned).
- Entry: `strategy.entry(id="long", long=true, when=Bullish and Momentum and RSI > 50 and window())` where `Bullish = crossunder(close, movingaverage_fast)` (strict v4 semantics — prior-bar close at/above MA9, current-bar close below it; touching without crossing fires nothing) and `Momentum = movingaverage_mid > movingaverage_slow` (strict; equality fails the gate).
- Exit: `strategy.close("long", when=longStopPrice or longTakeProfit and window())` where `longTakeProfit = RSI > TP`, `longStopPrice = RSI < SL`. Pine `and` binds tighter than `or`, so the admitted semantics is exactly `longStopPrice or (longTakeProfit and window())`: the RSI-below-30 close is window-independent, the RSI-above-70 close requires the window. Both legs are completed-bar RSI-threshold closes — no stop/limit order, no price level, no trailing, no time limit. The author's "stop loss / take profit" prose names these two RSI legs; nothing else in the block can close a position.
- Direction: long-only, explicitly. No short entry exists anywhere in the block; the short side is disabled by construction.
- Inert code, provably excluded: `showDate`, all three `plot` lines (display only; MA plots never enter any order condition).

## Required data

- Completed `1h` bars of ETHUSDT: `close` (all three SMAs, RSI, both cross/level legs) plus bar `time` for the pinned date window. No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1h` is adopted as the research frame because it is the source-stated best timeframe (page pro-tip) and the page's own display context (BINANCE ETHUSDT 1h) — never presented as anything beyond that (see Limitations).
- Warmup: longest causal chain is `sma(close, 100)` (first defined at the 100th completed bar) plus the crossunder prior-bar reference. First fully-defined evaluation at the 101st completed `1h` bar; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: ETHUSDT under the house overlay (the canonical page's own display context was BINANCE ETHUSDT 1h and ETH is inside the house universe — never presented as source-native venue semantics; the rule reads `close` only).
- Order timing: the declaration sets `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration's 30%-of-equity sizing, 1000 initial capital, and 0.1% commission lines are pure event-neutral accounting (the page's own 30%/0.1%/"one trade at a time" framing confirms their accounting nature), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v4 default 0: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: the MA50>MA100 regime and RSI>50 gate can persist across many bars while long, and repeat MA9 crossunders can print before any RSI exit — the admitted rule blocks every such add and holds. Re-entry is allowed immediately after any RSI close whenever the entry conjunction fires again (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships prose plus release notes: 300+ backtests claim, average 1.5-day holding claim, 30%/"one trade at a time"/0.1% accounting notes, 1h pro-tip, and the Jun 9 2021 release note documenting the below-MA9 entry (2.5x improvement claim). The author's help article reports 60.53% net profit on BNB/USDT 1h from January 2022 to November 2022. All figures are recorded here as source-reported claims with traceable section provenance (page prose/release notes; help article body) — none is independently reproduced and this record claims no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Above/below-MA9 wording is resolved, not assumed: the prose body's single "crosses above the MA9" line is outvoted by three concurring witnesses — the executable block (`crossunder`), the author's help article ("crosses below"), and the author's own release note (below-MA9 entry, 2.5x). The admitted rule follows the concurring witnesses; the stale prose line is excluded and named here.
2. Exit precedence is exact, not smoothed over: the close condition is admitted strictly as `RSI < 30 or (RSI > 70 and window())` per Pine operator precedence. The window-independent RSI-30 leg is harmless in practice (no position can exist outside the window because entries require it) but it is recorded as written, not parenthesized away.
3. "Stop loss / take profit" prose names RSI-threshold closes, not orders: 0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=` anywhere in the block, so no price-triggered exit can exist by construction. The RSI-70 leg is the only profit-taking path and the RSI-30 leg the only loss-cutting path.
4. Boundary ties fire nothing: `crossunder` without a strict cross, `MA50 == MA100`, `RSI == 50/70/30` all hold rather than trade — ties never invent an order.
5. Display-code isolation: `showDate` is never read and all `plot` lines never enter any order condition, so display toggling cannot alter any admitted event.
6. The window inputs are pinned, not removed: moving the 2019-01-10 floor, retuning any length/threshold, adding a side, or adding a price stop/target/cooldown would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA 9/50/100 on close / RSI 14 with 50/70/30 thresholds / crossunder-MA9 trigger with MA50>MA100 gate / RSI-threshold exits with the admitted precedence / long-only / `1h` ETHUSDT / same-bar-close fills are frozen.

- F1 — Dip-trigger relevance: entries on the regime plus RSI-50 gate alone (MA9 crossunder leg removed, first qualifying bar per regime takes the trade) must not improve net expectancy; fail ⇒ the dip-cross trigger is decorative and the system is a pure regime holder.
- F2 — RSI-gate relevance: entries without the RSI>50 coincident gate must not improve net expectancy; fail ⇒ the momentum filter adds nothing over the MA stack plus dip-cross.
- F3 — RSI-exit relevance: holding each entry until the opposite regime state (MA50 <= MA100) instead of the RSI 70/30 closes must not improve net expectancy; fail ⇒ the "dynamic stop/TP" legs add nothing over regime holding.

## Crypto portability

Pinned to ETHUSDT under the house overlay. The `close`-only long-only logic ports to perps or spot without structural change (no short side exists to disable). No funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Extension to other house-universe assets would be a different, unpinned claim; the author's BNB figure is source-reported evidence only, not an admitted multi-asset claim.

## Limitations

- Source-frame transfer: the source's stated best frame is 1h and its display context is ETHUSDT 1h, but hourly ETH behavior is asserted by the source, not proven to Hermes — backtest evidence stays source-reported until downstream reproduction.
- Warmup cost: the SMA-100 leg needs 100 completed bars, so the system is blind for the first 100 bars of any evaluation window and reacts slowly to newborn uptrends on hourly bars.
- Regime persistence: the MA50>MA100 stack can hold for long stretches, so a trend that decays without printing RSI>70 is ridden until RSI<30 admits weakness; with no price stop by construction, adverse excursion has no guardrail.
- Always-in-regime entries: while the regime and RSI-50 gate persist, every MA9 dip-cross re-enters immediately after an RSI-70 book — rapid re-entry chains are admitted rule behavior, not an implementation artifact.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.tradingview.com/script/XAiEh7nb-Maximized-Scalping-On-Trend-by-Coinrule/ (Strategy by Coinrule, open-source, updated Jun 10 2021; page rules, 1h pro-tip, 30%/"one trade at a time"/0.1% accounting notes, Jun 9 2021 below-MA9 release note, and BINANCE ETHUSDT 1h display context all live-verified 2026-10-08; published Source-code tab read line-for-line this run).
- First-party documentation: https://help.coinrule.com/articles/407566-maximized-scalping-on-trend (below-MA9 entry instruction, 1h tip, BNB 1h Jan–Nov 2022 figure, 1.5-day holding note).
- Immutable code mirror: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Maximized%20Scalping%20On%20Trend%20(by%20Coinrule).pine (pinned HEAD verified as remote HEAD this run via `git ls-remote`; blob `6665c36bdb3081bf79b179232efbfe74002cb03f`, 3289 bytes; header and Pine block match the canonical page's published source line for line, code governs).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
