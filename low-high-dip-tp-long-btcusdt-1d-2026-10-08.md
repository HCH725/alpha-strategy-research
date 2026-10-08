---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Low-High dip-recovery long with EMA200 gate and fixed 8% take-profit on BTCUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2025-04-30
sources:
  - https://www.fmz.com/strategy/432972
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/低价买入-高价止盈策略Low-High-Trend-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ page prose (overview plus exit section) presents the fixed take-profit leg and the highest-price-crossdown leg as co-available exits joined by OR semantics ('closes when price falls below the highest price OR the take-profit condition is met'), but the pinned Pine block wires the two legs through one exclusive boolean (`TakeProfitInput`, default true): exactly one leg is live at a time, and under the pinned default the highest-price leg is provably dead code. The admitted rule pins the code (TP-only exit). The prose OR-semantics system is recorded as a source-internal contradiction, not repaired."
---

# Low-High dip-recovery long with EMA200 gate and fixed 8% take-profit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page live plus GitHub mirror cross-check):

- FMZ strategy: https://www.fmz.com/strategy/432972 (`低价买入-高价止盈策略|Low-High-Trend Strategy`, Pine title `Low-High-Trend Strategy`, `//@version=5`, `// Author = TradeAutomation`, page author `ChaoZhang`, created 2023-11-23).
- FMZ backtest block pinned on the page: `start: 2022-11-16 00:00:00`, `end: 2023-11-22 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1d` figure is the script decision timeframe adopted as the research frame.
- Live re-verification (2026-10-08): the FMZ page returns HTTP 200 (806,683 bytes); the page title, the `ChaoZhang` author line, the full embedded Pine block (`strategy(title="Low-High-Trend Strategy", ..., process_orders_on_close=true, ...)`, `lowcriteria = ta.lowest(close, input(20, ...))[1]`, `highcriteria = ta.highest(close, input(10, ...))[1]`, `TakeProfit = ta.crossover(close, strategy.position_avg_price*(1+(.01*input.float(8, ...))))`, `ema = ta.ema(close, input(200, ...))`, the four gated `strategy.entry`/`strategy.close` lines, and the backtest header) all match the mirror line for line. No live-page fact contradicts the mirror.
- Mirror: `fmzquant/strategies` file `低价买入-高价止盈策略Low-High-Trend-Strategy.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30), carrying the same Pine block and a `Detail` link back to FMZ 432972.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe(` 0, `strategy.exit` 0, `strategy.order` 0, `input.time` 0, `volume` 0. Series read: `close` only (plus `time` solely inside the provably always-true `InDateRange` gate below). `plot` lines never execute trading logic.

Licence and rights: the pinned block carries an MPL-2.0 header. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `432972`, `Low-High`, and `lowcriteria` return 0 admitted rules — the one hit is a passing sibling-family mention inside `cumulative-rsi-dual-threshold-long-btcusdt-1h-2026-10-08.md`, which admits a different (cumulative-RSI) mechanism. Open `research/*` PRs: only #48 (Larry Williams 3-EMA channel streak long) and #49 (Gaussian channel StochRSI-gated breakout long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` (Donchian-channel breakout on `1h` with channel-stop exit), `triple-ema-volstop-tp-long-btcusdt-1d-2026-10-08.md` (triple-EMA simultaneous-cross conjunction entry with a dual-leg OR exit), `ema-cloud-7-20-trend-btcusdt-1d-2026-10-07.md` (dual-EMA cloud). Five-axis distinction: mechanism differs (dip-recovery cross back over the prior 20-bar low, EMA200 uptrend gate, single-leg fixed-percentage take-profit hold), signal construction differs (`crossover(close, lowest(close,20)[1])` AND `close > ema(close,200)` versus channel breaks or EMA-vs-EMA crosses), exits differ (one live 8% TP leg, no stop, no opposite-signal leg under pinned defaults), horizon is `1d` BTCUSDT, source identity differs (FMZ 432972, `ChaoZhang`).

## Economic mechanism

### Source-reported

A long-only buy-the-dip system: it tracks the lowest close of the last 20 daily bars and buys when price recovers back above that washed-out level — but only when the broad trend (price above its 200-day EMA) agrees — then holds for a fixed 8% take-profit measured off the entry price.

### Research interpretation

Dip-recovery entry with a single-leg close-evaluated hold. The `[1]` offset on the lowest/highest lines excludes the current bar, so the entry trigger is strictly historical; the EMA200 gate suppresses counter-trend dip-buys. The hold has exactly one live leg (the 8% TP crossover on the daily close) — there are 0 `strategy.exit` calls, hence no stop/limit order, no intrabar touch fill, and no same-bar TP/SL ordering ambiguity. If price never reaches +8%, the position is held indefinitely — the code is explicit about this (no stop, no time limit), and this record pins the behavior rather than "fixing" it. No leverage, sizing, or cost edge is embedded in the signal; the source `initial_capital`/`default_qty_*`/`commission_*`/`slippage` lines are capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Inputs: `Lowest Price Lookback = 20`, `Highest Price Lookback = 10` (dead under pinned default, see below), `TakeProfitInput = true`, `Take Profit % = 8` (step 0.25), `TrendFilterInput = true`, `EMA Length = 200`. `Start Time`/`End Time` display inputs exist but `InDateRange` is hardcoded `true`, so the date gate is provably always-true and the inputs are inert.
- Levels: `lowcriteria = ta.lowest(close, 20)[1]` (lowest close of the 20 bars strictly before the current bar); `highcriteria = ta.highest(close, 10)[1]` (computed and plotted, but read only by the dead exit branch — inert under the pinned default); `ema = ta.ema(close, 200)` on `close`; `TrendisLong = (close > ema)` with strict `>` (equality fails the gate).
- Take-profit trigger: `TakeProfit = ta.crossover(close, strategy.position_avg_price * (1 + 0.01 * 8))` — strict prior-bar semantics (prior close at/below the +8% level, current close above it).
- Entry long (live leg): `strategy.entry("Long", strategy.long, when = ta.crossover(close, lowcriteria) and TrendisLong)` — recovery back above the prior 20-bar lowest close while above EMA200.
- Exit long (live leg): `strategy.close("Long", when = TakeProfit)` — the single TP crossover. Flat-book `strategy.close` is a deterministic no-op.
- Direction: long-only. Zero short entries exist in the pinned block; the short side is explicitly disabled (no short rule to implement).
- Stop-loss / trailing / time limit / opposite-signal exit: explicitly none under pinned defaults (0 `strategy.exit`, 0 `stop=`/`limit=`, no short side, no time-limit construct, `strategy.close_all()` guarded by the always-false `not InDateRange`).
- Inert code, provably excluded: the `TrendFilterInput==false` entry branch, the `TakeProfitInput==false` (`crossunder(close, highcriteria)`) exit branch, `highcriteria` (dead-branch-only read), `StartTime`/`EndTime` inputs, `InDateRange`/`close_all` gate, and all `plot` lines.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (lowest/highest lines, EMA200, both crosses, TP level), and `time` solely for the always-true `InDateRange` gate. No `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read.
- Single decision timeframe `1d` (backtest `period: 1d`). `basePeriod: 1h` is FMZ demo-execution granularity; with 0 intrabar orders and close-gated evaluation it cannot alter any admitted event.
- Warmup: longest live lookback is 200 bars (EMA200); the `crossover` prior-bar reference needs one further bar and `lowest(close,20)[1]` needs 21. First fully-defined evaluation at 201 completed `1d` bars; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the house overlay runs Isolated futures at 3×/5×, long-only for this record since the short side is disabled as coded — no naked-spot construction needed).
- Order timing: both live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. `calc_on_every_tick` is unset (default false). No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: `initial_capital = 25000`, `margin_long/margin_short = 50`, `default_qty_type = strategy.percent_of_equity`, `default_qty_value = 110`, `commission_type/value = cash_per_order 1`, and `slippage = 3` are event-neutral capital/accounting configuration (single-position, close-evaluated exits — fill price and event sequence do not depend on size), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (Pine v5 default 0: no additional same-direction entry while the single `Long` position is held). At most one open long; re-entry is allowed immediately after a TP close whenever the entry conjunction fires again (no cooldown specified — explicitly none, not invented). No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and mirror ship one backtest-chart image with no numeric caption — no ROI, Sharpe, win rate, drawdown, or trade-count figures are cited anywhere in this record. The prose makes only qualitative claims ("can perform well under certain conditions") plus its own risk warnings. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position `strategy.position_avg_price` is `na`, so the TP `crossover` RHS is `na` (false) — the exit leg cannot fire flat; only a genuine dip-recovery cross can open.
2. Boundary ties are defined: `close == lowcriteria` fails the strict `crossover`; `close == ema` fails the strict `TrendisLong` (`>`); `close == avg*1.08` fails the strict TP `crossover`.
3. Same-bar entry/exit co-fire resolves deterministically at the single close price (open-and-flat at one price, no P&L): on the entry bar `strategy.position_avg_price` equals the fill (the same close), so `crossover(close, avg*1.08)` is false by construction — the exit cannot co-fire on the entry bar.
4. The dead-branch inputs are pinned, not removed: flipping `TakeProfitInput`, `TrendFilterInput`, or any lookback/percentage would each be a different, unpinned rule — none is admitted here.
5. Indefinite-hold exposure is pinned as written: a position that never prints +8% on a daily close is never exited by this rule — no stop is invented to rescue it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `lowest(close,20)[1]` recovery cross AND `close > ema(close,200)`, 8% TP off average price, long-only, `1d` BTCUSDT, same-bar-close fills are frozen.

- F1 — Trend-gate relevance: removing the `close > ema(close,200)` conjunction (pure dip-recovery entry) must not improve net expectancy; fail ⇒ the EMA200 gate adds nothing.
- F2 — Exit relevance: replacing the 8% TP leg with a fixed 30-bar time exit (entry kept) must not improve net expectancy; fail ⇒ the fixed-TP leg is decorative.
- F3 — Entry relevance: replacing the dip-recovery cross with a plain `crossover(close, ema(close,200))` (TP leg kept) must not improve net expectancy; fail ⇒ the lowest-20 recovery construction adds nothing.
- F4 — Parameter sensitivity: the (20, 200, 8%) set must not be dominated net of costs by both the (10, 100, 4%) and (30, 250, 12%) neighbor sets; fail on both sides ⇒ the set choice is arbitrary rather than structural.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The long-only close-derived logic ports to perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Spot deployment needs no modification for the long side (no shorting required).

## Limitations

- No adverse-stop protection: the single exit evaluates at the completed daily close and only in the profitable direction, so an adverse drift exits never — the position can be held through arbitrarily large unrealized loss, and on `1d` bars gap risk is fully retained. The source's own risk section concedes the lack of stop-loss control.
- Fixed 8% TP caps every winner at 8% above average entry regardless of trend strength; in one-sided trends this truncates the right tail by construction — the record pins the value as written rather than "fixing" it.
- Dip-recovery-plus-uptrend entries are selective by design; long droughts with zero exposure are the normal state, not a malfunction.
- Whipsaw regime: in range-bound chop above EMA200, price can dip under and recover over the 20-bar low repeatedly; the gate attenuates but cannot eliminate repeated entries.
- Source demo window is about one year (2022-11-16 → 2023-11-22); full-history behavior is unreported by the source and unclaimed here.
- FMZ prose advertises an OR-semantics dual exit that the code does not implement; anyone deploying on prose alone would trade a different system.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/432972 (live page re-verified 2026-10-08, HTTP 200, 806,683 bytes; backtest block 2022-11-16 → 2023-11-22, `period: 1d`, Binance USDT-M BTC).
- Mirror: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/低价买入-高价止盈策略Low-High-Trend-Strategy.md (same Pine block line for line, links back to FMZ 432972; commit date 2025-04-30).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
