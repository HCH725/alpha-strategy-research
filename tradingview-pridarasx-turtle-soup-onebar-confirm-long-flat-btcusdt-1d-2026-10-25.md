---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Pridarasx Turtle Soup 20-bar sweep with strict next-bar reversal confirmation — derived BTC-USDT spot 1d long-flat"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/HxwwHIea-Turtle-Soup-Strategy-with-1-Bar-Confirmation/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pridarasx Turtle Soup — strict next-bar reversal confirmation (independent spot long-flat derivative)

## Provenance

**Primary TradingView source:** [Turtle Soup Strategy with 1-Bar Confirmation](https://www.tradingview.com/script/HxwwHIea-Turtle-Soup-Strategy-with-1-Bar-Confirmation/) by **Pridarasx**, public **open-source indicator** (not an executable TradingView strategy); page displays **Jun 19** as publication date without an independently exposed year; directly inspected **2026-10-25**. Stable TradingView script ID: `HxwwHIea`. The publicly readable page describes a *20-bar historical extreme*, a wick crossing that historical boundary, a latched setup with saved bar/high/low, and **only the immediately following bar** as a reversal-confirmation window; otherwise the pending setup expires. The bearish illustration explicitly says the next candle closes below the setup candle's low. Full Pine source, exact revision/hash, precise bullish mirror and original indicator tie/alert semantics were **not** independently accessible. The source's market-maker/stop-hunt narrative is a hypothesis, not verified order-flow evidence.

**Independent derivative, NOT source-native/lossless:** The publication is an *indicator*, not an order-generating strategy. The researcher separately defines the bullish mirror, strict 20-bar prior-extreme arithmetic, same-bar double-sweep rejection, no-new-setup-on-confirmation-bar rule, LONG/FLAT trade mapping, bearish confirmation as the full long exit, Binance BTC-USDT spot 1d market, 30-bar no-trade warmup, completed-close MARKET simulator fill, fixed 0.001 BTC, 10,000 USDT cash, research fees, and explicitly disabled stops, targets, DCA and shorts. None of those unverified choices is attributed to the author or claimed to match unavailable Pine. These changes materially affect order events. The author does **not** report the derivative's profitability.

**Immutable research identity:** `TV:HxwwHIea:Pridarasx:public-asof-20261025:derived-v1:prior20-wick-sweep:exact-nextbar-confirm:setup-highlow-break:longflat:BTC-USDT:Binance-spot:1d:close-MARKET:0.001BTC`. A future update to the TradingView script cannot silently change this frozen derived specification.

**Dedup on 2026-10-25 main SHA `466c2bc0536acfa43b6da59ec0c55b88f0789591`:** no root-level record or open research PR references script ID `HxwwHIea`; GitHub code search and PR search were negative. Existing `turtle-soup-donchian-fade-bracket-two-sided-btcusdt-1d-2026-10-13.md` instead **fades the 20-bar breakout immediately**, allows **four adverse 0.5-ATR adds**, uses per-unit 2.5-ATR brackets and 10-bar exits on **two sides**; this candidate **waits for exactly one subsequent candle to break the sweep bar's opposite extreme**, never adds, has no bracket, and uses the opposite confirmed pattern as exit. `wick-reversal-hammer-shooting-star-long-flat-btcusdt-1d-2026-10-16.md` is a wick/body-geometry hammer plus next-bar higher-low rule, not a 20-bar boundary-sweep with setup-high confirmation. Neither is a trivial parameter variant. Open research/* PRs checked: #353, #350, #331, #304, #251, #92, #89, #63, #49, #48; none shares the source or this rule.

## Economic mechanism

### Source-reported

A price wick crossing a preceding 20-bar extreme can indicate a failed breakout; the author requires a reversal confirmation on the **next bar only**, rather than accepting the sweep as an entry. The claim that this captures trapped breakout participants is a theory, not observed trade-flow proof.

### Research interpretation

The derivative buys only after a **low-side liquidity sweep** is followed immediately by a close **above the sweep candle's high**. This is a stricter one-bar reversal than merely closing back inside the old 20-bar channel. It remains long until the mirror **high-side sweep** is followed immediately by a close **below that sweep candle's low**. Confirmation-bar lag may miss sharp reversals, and a no-stop hold can incur large losses. No alpha, Sharpe, profitability, backtest performance or source-native equivalence is claimed.

## Signal

**Frozen derived parameters:** `N=20` completed bars for the extreme, `warmup=30` completed bars, `decision_tf=1d`, `unit=0.001 BTC`. All comparisons are strict; equality is **not** a sweep or confirmation. No tunable threshold, optimizer, learned model or hidden smoothing.

For each fully completed daily bar `t` (zero-based), use only **preceding** candles for historical levels:

```text
priorLow20[t]  = min(low[t-20], ..., low[t-1])
priorHigh20[t] = max(high[t-20], ..., high[t-1])
bullSweep[t]   = low[t]  < priorLow20[t]
bearSweep[t]   = high[t] > priorHigh20[t]
```

**Two-state trading machine:** `position=FLAT|LONG`, `pending=NONE|BULL|BEAR` with `setup_index`, `setup_high`, `setup_low`. The `pending` setup is valid **only** at `setup_index+1`. A pending setup is evaluated before any new setup search, then always cleared; **no fresh setup may be armed on that confirmation bar**. If `position=FLAT`, only BULL setups are considered; if LONG, only BEAR setups are considered. A candle that simultaneously satisfies `bullSweep` and `bearSweep` is ambiguous and **never** arms either setup. A single valid low-side sweep while FLAT arms BULL, saving the sweep bar's high/low; a single valid high-side sweep while LONG arms BEAR. Neither setup causes an order on the sweep bar.

At the *immediately next completed candle* `t=setup_index+1`:

- BULL confirmation: `close[t] > setup_high` and `close[t] > priorLow20[setup_index]`; if FLAT, request **one BUY** for 0.001 BTC. The second condition is redundant given ordinary valid OHLC but is retained as an explicit back-inside-old-boundary check. If not confirmed, clear pending without entry.
- BEAR confirmation: `close[t] < setup_low` and `close[t] < priorHigh20[setup_index]`; if LONG, request **one SELL** of the existing 0.001 BTC. If not confirmed, clear pending without exit.
- No two-bar or delayed confirmation, no same-bar reversal, no immediate sweep-bar trade, no partial order, no rearm on a confirmation bar. A failed setup leaves the existing position unchanged.

**Warmup:** first 30 fully completed candles (indices 0..29) compute and validate historical state but **cannot arm or confirm** a setup or trade. First eligible setup is bar `t=30`; first possible trade is bar `t=31`. Start FLAT, no inherited position. End-of-data LONG is marked at last observed close, not forcibly liquidated. No fabricated terminal fill.

## Required data

Exactly one Binance BTC-USDT **spot 1d** OHLCV feed; `high`, `low`, `close` and UTC candle-open timestamp are decision-critical. Require each bar's OHLC values finite and strictly positive with `low <= min(open,close) <= max(open,close) <= high`, and 86400-second contiguous increasing UTC open timestamps. Raw missing, duplicated, incomplete, nonmonotonic or invalid bars **fail closed / abort the segment**; do not forward-fill, interpolate, substitute prices, or silently compress a missing one-bar confirmation interval. No external market, order book, open interest, higher timeframe, realtime tick, adjusted close, model or future pivot is used.

A Binance kline timestamp `T[t]` is its **open** time; the fully completed daily candle becomes decision-available only at `E[t]=T[t]+86400 seconds UTC`. Both signal and modeled close-fill are labeled `E[t]` even though the pinned simulator internally indexes the row by open time. The same-candle close fill is a **backtest accounting convention**, not a claim that an order sent after close could trade at that already observed close. Sweep-bar highs/lows are never used until that bar has closed; the next-bar confirmation is never evaluated before its close. No lookahead, repainting, future extrema or full-sample data.

## Execution assumptions

**Pinned Hummingbot scope:** package `20260920`, VERSION `dev-2.17.0`, immutable `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Read through GitHub app at this commit: `hummingbot/VERSION`; `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (supports `1d`); `.../binance_spot_candles.py` (REST kline open-time/ OHLCV parsing); `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (completed feature-row updates, `determine_executor_actions` and `CreateExecutorAction` dispatch, `BacktestPositionHold` netting); `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (MARKET first supplied candle, **close** price, `POSITION_HOLD`, `filled_amount_quote`, `cum_fees_quote`); and `hummingbot/strategy_v2/executors/order_executor/data_types.py` (`OrderExecutorConfig`). Prior accepted Alpha PR #414 independently verified package/source wheel identity and representative primitive behavior; **not rehashed or rerun this cycle**. Exact code refs below.

A future **strategy-specific controller** (not implemented here) may compute the pending state on completed daily OHLC rows, then emit `CreateExecutorAction` with `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY|SELL, amount=Decimal("0.001"), execution_strategy=MARKET, price=None, leverage=1)`. SELL only reduces an existing fully filled spot long. The pinned `OrderExecutorSimulator.simulate()` MARKET branch fills on the first supplied row's `close`, not at a fabricated next-open or intrabar high/low. `BacktestPositionHold._process_order()` nets BUY/SELL and computes **gross** realized PnL; `add_executor()` accumulates both-side fees. A controller must retain an in-flight flag and reconcile simulated fills and its own filled-unit ledger, not infer immediate fills from stale `positions_held` or a pruned terminated-executor view.

**Research accounting pin:** initial 10,000 USDT quote cash, zero BTC; one full 0.001 BTC unit max, no leverage/borrow, no pyramiding, DCA, SO, concurrent pairs, partial scale or compounding. On BUY, require cash `>= 0.001*close*(1+0.001)`; on insufficient cash, invalid price or rejected order, **no fill and no phantom long**; pending expires, next entry requires a fresh two-bar setup. On SELL require a confirmed filled 0.001 BTC long; otherwise no-op/fail closed. Trade cost `0.001` **of filled quote notional per side** (0.1%) is a fixed *research assumption* reused from accepted PR #414, **not** an asserted actual Binance fee. Debit BUY notional+fee; credit SELL notional-fee. Net realized PnL = gross matched PnL minus accumulated entry and exit fees; track cash and marked inventory separately. Spot funding is **not applicable**; no invented perpetual funding, spread, slippage, margin or tick/lot precision. The simulator omits real spread/impact/latency/partial-fill modeling; zero *additional modeled* slippage is a limitation, **not** evidence that actual slippage is zero. Live exchange precision/min-notional and actual fees remain unverified.

All stop-loss, take-profit, trailing, time exits, order book/tick fills, maker/limit orders, intrabar triggers, shorting, cross-market synchronization and forced terminal liquidation are explicitly **disabled** in this derivative. No hidden executor default may add a trade leg. This is a *model-compatible research proposal* under a narrowly verified close-MARKET spot path, not a production trading strategy or profitability claim.

## Evidence

### Source-reported

Pridarasx's TradingView open-source **indicator** describes a 20-bar historical boundary, wick sweep, latched setup candle's high/low and exact-next-bar reversal confirmation; the bearish diagram explicitly specifies a next candle closing below the setup low. The original indicator is not demonstrated to place orders. No numerical performance claims are adopted.

### Independently reproduced

**None for this strategy.** GitHub-app read-only inspection of the immutable Hummingbot code paths above was performed; prior independent engine evidence in accepted PR #414 is cited as **prior** evidence, not re-executed. No Pine source hash, original strategy run, Qlib/Hummingbot backtest, event-level parity, fee-realism experiment or Paper/Testnet/Live test is claimed.

### Negative evidence

Original Pine source/version unavailable through the public text view; exact bullish indicator semantics and original alert/priority behavior unverified. Derived bullish mirror and all order mapping are **researcher-defined**, not silently attributed to Pridarasx. Same-close MARKET model fills may overstate executable edge; fixed fees omit live spread/impact and partial fills. The original author's market-maker narrative is not independently established.

## Falsification plan

First check source provenance if full Pine becomes accessible: distinguish indicator-native sweep/confirmation events from the independently specified order map; do not silently retrofit any divergence. After separate downstream authorization, a representative Qlib/Hummingbot event-level comparison must verify the two-bar setup/confirmation timestamps, pending expiry, no-new-setup-on-confirmation priority, actual BUY/SELL fills, cash/fees and position netting before any large-scale screening that depends on an unvalidated implementation path. Failed or missing prices, missing bars and conflicting sweeps must fail closed, never yield synthetic trades. None of those runs is performed by this Scout.

## Crypto portability

BTC-USDT spot daily is the **only pinned research instantiation**, not a whitelist or profitability recommendation. Other coins, pairs, timeframes, derivatives, next-open fills or DCA are separate declared variants needing their own causal data and pinned-engine compatibility evidence; this record asserts none of them.

## Limitations

The TradingView page is mutable and the complete Pine was not read. This is an explicitly independent derivative of a public indicator; it is **not** a source-native implementation of an author trading system. The bullish mirror, pending-state priority, opposite-signal exit, position sizing, costs, warmup and close-fill convention are independently specified. No stop-loss can mean unbounded mark-to-market drawdown within a long position; the backtest close-fill model does not represent live execution. `hb_ready_status: PASS` is **proposed for independent Auditor review**, not self-approval, Qlib parity, Survivor status or permission to trade.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller, Qlib executable recipe, backtest or deployment artifact was created. A PASS record describes a fully specified research candidate, not executable materialization.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Only independent Hermes Auditor exact-head six-gate review can permit merge; Scout must not approve, merge or close this PR. No Qlib/Hummingbot/pipeline/cron/market change is authorized.

## Related Wiki records

None asserted; no private Wiki, Survivor or performance evidence is imported.

## Sources

- Primary: https://www.tradingview.com/script/HxwwHIea-Turtle-Soup-Strategy-with-1-Bar-Confirmation/ (Pridarasx; page displays Jun 19; inspected 2026-10-25).
- Pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Pinned code: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Pinned code: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Prior accepted independent package/primitive review: https://github.com/HCH725/alpha-strategy-research/pull/414
