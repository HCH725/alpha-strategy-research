---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Coinrule buy-the-dips MA100 one-bar momentum-threshold long-flat on BTCUSDT spot 1d derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-18
sources:
  - https://www.tradingview.com/script/WT1uzChH-Buy-The-Dips-MA200-Optimised/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coinrule buy-the-dips one-bar momentum-threshold long-flat — independent BTCUSDT spot 1d derivative

## Provenance

- **Primary TradingView publication:** *Buy The Dips - MA200 Optimised*, **Coinrule**, stable public script ID **WT1uzChH**, open-source listing: https://www.tradingview.com/script/WT1uzChH-Buy-The-Dips-MA200-Optimised/ . Page HTML fetched and read on **2026-10-25** (HTTP 200, ~858KB): `<title>` and `og:title` confirm the script name and Coinrule authorship; `og:description` carries the author's rule prose ("combines a contrarian approach (buying the dips) with a trend-following logic (only when the price is above the MA200)" / "seeks to find the best times when buying the dips"); the page marks the script open-source. The served page HTML embeds **no Pine code** (zero hits for `MAinp`, `overall`, `strategy.entry`, `strategy.close`) and no publish-datetime meta — no formula line and no publication date is claimed from the page. No performance number of any kind is transcribed from the page.
- **Pinned executable artifact (immutable GitHub mirror, complete Pine block read end to end):** repository https://github.com/hasnocool/tradingview-pine-scripts at full commit SHA `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (commit date 2024-09-18, adopted as `source_as_of`; verified repository HEAD via the GitHub commits API this cycle — the same head pin as the merged CHOP-zone record), exact file path `Buy The Dips - MA200 Optimised.pine`, blob SHA `d75360d2185a0a87be6dc5d0c4812b99e05c538c`, 2,984 bytes. The local mirror copy hashes to the identical blob SHA and is byte-identical to the Contents-API payload decoded this cycle. The mirror wrapper carries `Script Name`, `Author: Coinrule`, and the author's description prose above the `//@version=4` code block.
- **Text census over the pinned Pine code block** (NBSP-normalized; wrapper prose excluded): 1 `strategy(` declaration (`overlay=false`, display only) / 1 `strategy.entry` (`id="long"`, v4 `long=true` — long-only is source-native, zero short leg) / 1 `strategy.close` (`id="long"`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=` / `limit=` / `profit=` / `loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / `timenow` / 0 `calc_on_every_tick` / 0 `crossover` / `crossunder` / `ta.cross` / 0 `ta.*` (single bare v4 `sma(` call only) / 0 `sum|highest|lowest|change|tr` / 0 `volume|high|low|open` series reads (order logic reads `close` and bar `time` only; "Lower Band" is an `hline` display string) / 0 `pyramiding` (Pine default: no same-direction adds) / 0 `process_orders_on_close` (Pine default: completed-bar evaluation, next-bar fills) / 0 `commission*` / 0 `default_qty_*` / 0 `initial_capital` (order economics absent — recorded as absent, never as zero-cost evidence). 9 `input(` calls with pinned defaults: `MAinp=100`, `inp_lkb=1`, from `2020-01-01`, thru `2112-01-01`, `showDate=true` (display only).
- **Corroborating republication (prose only, fenced):** FMZ page https://www.fmz.com/strategy/438063 (*Buying Dips - MA200 Optimized Strategy*) prints the same rule prose (dip = overall change below **-3%**; long-term average trend gate; risk analysis stating the largest risk is continued decline after the buy signal; optimization directions listing "add stop loss" as future work — confirming no stop ships). Its embedded Pine rule lines match the pinned mirror's entry/exit lines verbatim. Its FMZ demo backtest header (`1h`, one-month window, futures venue) is explicitly NOT adopted anywhere in this record.
- **Title-vs-code discrepancy, disclosed:** the script title and both prose pages say "MA200"/"200-day average", but the executable code default is `MAinp=100`. This record pins the **code default 100** (the only executable value) and never attributes 200 to the coded rule. The reviewer must not silently substitute 200.
- **Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) market/frame pin `BTCUSDT` Binance **spot `1d`** (the code names no market and no timeframe; the FMZ demo header is fenced above, never adopted); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default fills next-bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted **120-bar** warmup with pre-warmup bars flat by record rule (structural minimum is 101 completed bars for the MA100 leg — see Required data); (4) fixed `0.001 BTC` spot sizing with research `trade_cost=0.001` per side replacing the absent source economics (see Execution assumptions); (5) the date-window inputs pinned at their source defaults (`2020-01-01`–`2112-01-01`), inert over any realistic research span (see Signal). The MA100 default, 1-bar lookback, `-3`/`+1` thresholds, strict comparisons, native long-only posture, the single `strategy.close` exit leg, and the no-stop/no-target/no-trailing stance are source-native and unmodified.
- **Immutable identity:** `TV-WT1uzChH | independently-derived-v1-MA100-lkb1-dip-3-exit+1-longonly | BinanceSpot-BTC-USDT-1d | 2026-10-25`. Any change to signal, thresholds, market, clock, fill or position state constitutes a different derivative.

## Economic mechanism

### Source-reported

Contrarian dip-buying inside a long-term uptrend (author description plus FMZ principle prose): a short-horizon percentage washout marks the dip; the long moving average marks the trend; buys trigger only when both agree. The FMZ risk prose states the largest risk explicitly — price may keep falling after the buy signal, widening losses — and names stop-loss addition only as future optimization, so the shipped posture has no loss-limiting leg.

### Research interpretation

Hypothesis only: a single-day −3% washout that still closes above its 100-day average may mark short-term capitulation inside an intact slow uptrend, and a next-day +1% bounce may mark the snap-back. Unlike level-touch dip systems (the pool `low-high-dip-tp` record buys a 20-bar-low recovery with a fixed 8% take-profit), this system measures the dip as a **one-bar rate**, not a level, and exits on a symmetric one-bar rate, not a target. Unlike oscillator-gated dip systems (pool `freqtrade-bband-rsi-dip-buy`, `catching-the-bottom-rsi-dip-reversal`), no RSI/Bollinger/volume leg exists anywhere. This is neither a tested edge nor a loss-limiting strategy: back-to-back −3% days re-enter immediately after a +1% exit, and a grinding decline above a lagging average holds a full underwater position with no stop.

## Signal

**Frozen independent derivative (Gates 1–4).** Single UTC-aligned, consecutive **86,400-second** Binance BTC-USDT spot OHLCV stream. Each bar `t` is labeled by its open timestamp `T[t]`; its complete OHLCV is available for decisions only at `T[t]+86400`. No other asset, time frame, order-book or non-OHLCV feed.

- `MA100[t] = (1/100)*sum(close[t-i], i=0..99)` (bare v4 `sma`, unweighted arithmetic; no alternative smoothing).
- `overall[t] = 100*(close[t]-close[t-1])/close[t-1]` (1-bar percent change; `inp_lkb=1` pinned default; division requires `close[t-1] > 0`, enforced by the validity gate).
- `window[t] = true` for every in-span bar: the date inputs are pinned at source defaults (from `2020-01-01 00:00`, thru `2112-01-01 23:59`), so the gate is source-native and inert over any realistic research span — no researcher date choice.
- **Entry, only if FLAT:** `window[t] && overall[t] < -3 && close[t] > MA100[t]`. All three comparisons strict; an `overall` print of exactly `-3` or a close exactly on the average is not an entry.
- **Exit, only if LONG:** `window[t] && overall[t] > 1`. An `overall` print of exactly `+1` is not an exit; the MA gate does not condition the exit; losing the average while LONG is not an exit.
- **Same-bar exclusivity:** entry needs `overall < -3`, exit needs `overall > 1` — mutually exclusive on one bar by construction. The earliest exit is the bar after entry. Exactly one action maximum per bar; no reversal, no same-bar entry/exit.
- **State machine:** initially FLAT; first eligible decision after **120 consecutive valid completed 1d bars**. On each completed eligible bar, if FLAT test entry and create one simulated MARKET BUY of **0.001 BTC**; if LONG test exit and create one MARKET SELL of the full **0.001 BTC**. Otherwise HOLD. After a filled exit, the next eligible later bar may re-enter without cooldown; repeated entry signals while LONG are no-ops (Pine-default no-add posture carried over exactly).
- **Position/risk:** one spot LONG or FLAT, no short (source has zero short leg), leverage 1, no margin, no pyramiding, no DCA, no safety orders, no concurrency, no partial orders/fills, no portfolio allocation, no stop loss, no take profit, no trailing stop, no time exit, no liquidation, no maker/limit/intrabar orders, no forced final-bar liquidation. If LONG at end of dataset, hold 0.001 BTC and mark at last valid close without inventing a terminal SELL. No capital compounding.
- **Input validity:** every bar must have expected UTC 1d open-time spacing, finite positive O/H/L/C, `high >= max(open,close)`, `low <= min(open,close)`. `close[t-1] <= 0` is invalid (division guard). Invalid/missing candles reset the 120-consecutive-bar warmup and suppress both entry and exit until 120 new contiguous valid completed candles; existing LONG exposure remains held, not liquidated at an invented fill. No forward filling, no price substitution, no silently spanning gaps. Indicator windows must be wholly within the current valid segment.

## Required data

Single Binance BTC-USDT spot 1d OHLCV series with exact open timestamps; the signal reads `close` (formulas) and bar `time` (inert window gate) only — `open`/`high`/`low` feed solely the validity gate, `volume` is read by no line. 100 completed closes for MA100, 1 prior close for the rate, plus margin: the conservative 120-bar consecutive warmup covers both. No cross-symbol synchronization, external model, training, future extrema, funding series or secondary time frame.

## Execution assumptions

- **Pinned admission identifiers:** Hummingbot policy package label `20260920`, repository `hummingbot/VERSION=dev-2.17.0`; inspected **HCH725/hummingbot** at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (raw files read line-level this cycle, 2026-10-25). These are separate identifiers; the repository's `setup.py` distribution version `20260729` is not a verified build digest or proof of deployed package identity. The claim is bounded to **the pinned commit's research simulation semantics**, not an installed container.
- **Actual data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` explicitly lists `1d`; `binance_spot_candles.py` line 82 parses Binance Kline `row[0]` as timestamp and `row[1..5]` as O/H/L/C/V. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` processes rows through `update_state(row)` (lines 364–382, `close_bt` pricing, `BacktestPositionHold` aggregation into `positions_held`), `controller.determine_executor_actions()` with `CreateExecutorAction` (lines 284–287), and `simulate_executor` routing `OrderExecutorConfig` to the order simulator (lines 507–509). A strategy-specific controller/feature implementation **does not yet exist**; it must calculate the declared MA100/rate formulas and preserve state and validity rules, rather than claim that the generic engine already contains this strategy.
- **Fill model:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` handles `ExecutionStrategy.MARKET` with the first supplied row's timestamp as fill time (lines 22–24) and that row's `close` as full-fill price (line 56), `filled_amount_quote = Q * close` (lines 59–60), `cum_fees_quote = trade_cost * filled_amount_quote` (line 62), and `CloseType.POSITION_HOLD` (lines 67–70). The intended controller issues exactly one `CreateExecutorAction` with `OrderExecutorConfig` for Binance BTC-USDT, `MARKET`, BUY/SELL, `Q=0.001 BTC`, leverage 1; the controller must maintain an immediate filled-position state rather than rely on delayed `positions_held` conversion to suppress duplicate orders.
- **Effective time and causal restriction:** the raw `timestamp_bt` is a **bar-open** label. The engine uses backward `merge_asof` and `dropna` in feature preparation (lines 466–478), which **alone do not establish data availability**. The required strategy-specific implementation must expose the current OHLCV only after the completed bar and normalize both effective decision and research fill event to `T[t]+86400`, while using the declared same-row close simulator fill. This is a **simulation convention**; it does not assert that a real order submitted after observing the closing price can execute at that exact price. A future deployment requiring next-open/intrabar/maker realism is a new, separately verified engine path.
- **Costs and position ledger:** fix research `trade_cost=0.001` (**0.1% per filled side**), full fill `Q=0.001 BTC`, with modeled BUY cash outflow `Q*P_buy*(1+0.001)` and SELL inflow `Q*P_sell*(1-0.001)`. Compute realized net PnL as gross matched SELL–BUY less **both** fill fees; mark open BTC at last valid close, carrying already paid buy fee. `BacktestPositionHold` (lines 38–70: netted base exposure, matched-volume realized PnL, accumulated fees) tracks gross position cost and accumulated fees, but native `summarize_results.net_pnl_quote` / `update_state.total_pnl` must **not** be mistaken for fee-inclusive cash/equity without reconstructing fills. The source ships no commission concept — the 0.1% rate is a researcher research-cost assumption, never a source fact. **Spot funding is not applicable**; no fictitious futures funding=0. The simulator has no separately applied slippage in this model; this means **zero modeled additional slippage**, not evidence of real zero slippage. Exchange min-notional/lot precision, partial fills, real spreads, latency and realized commission are unverified and not represented as exchange-valid.
- **Reused representative capability:** admitted TradingView PR **#417** (ChartArt NR7, merged 2026-10-25) independently reviewed this exact pinned Binance spot 1d / MARKET-close / POSITION_HOLD research execution path, including fee-ledger limitations and event-time normalization; PRs **#421/#423** reviewed the same MARKET-close/POSITION_HOLD primitive. This is reusable **engine-path evidence only**, not proof that this new candidate was implemented, backtested, profitable, or Qlib/Hummingbot-parity tested. No novel execution primitive is introduced.

## Evidence

### Source-reported

TradingView `WT1uzChH` public author prose (Coinrule, page read 2026-10-25): contrarian dip-buying gated on price above a long-term moving average. FMZ `438063` principle prose: dip defined by overall change below **-3%**; long-average trend gate; risk prose naming continued post-signal decline as the largest risk; stop-loss named only as future optimization. Pinned mirror code defaults: MA length **100**, lookback **1**, entry `overall < -3` with `close > MA`, exit `overall > 1`, native long-only, no risk legs. No original numerical performance is transcribed or asserted.

### Independently reproduced

**None for this candidate.** The Gate-5 expressibility argument is static pinned-code inspection plus reusable independently reviewed engine-path evidence, not a strategy backtest, Qlib parity run or independent reproduction of author metrics.

### Negative evidence

Page HTML carries no Pine and no date — full rule provenance rests on the pinned mirror, not the page. The "MA200"/"200-day" title/prose conflicts with the coded default 100; this record pins the code and fences the prose. The FMZ demo backtest header (1h, one-month window, futures) is fenced, never adopted. The source ships no commission, sizing, timeframe or market — all are disclosed researcher pins, never source claims. Pine-default next-bar fills are converted to the disclosed same-bar-close research convention. Research fills/fees are not real-world order economics; the strategy has no protective stop and may hold large unrealized losses through consecutive washouts above a lagging average.

## Falsification plan

Only after separate downstream approval, freeze this identity and compare against (a) the same `-3`/`+1` rate pair with no MA100 gate, and (b) the same gated entry with a close-back-above-MA100 exit instead of the `+1` rate exit, each on predetermined IS/OOS partitions without OOS tuning. Any new engine primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. **No backtest or trading was performed in this Scout cycle.**

## Crypto portability

Current declared instance is Binance BTC-USDT spot 1d only, without a universe restriction as an HB_READY prerequisite. A different pair/frame, derivatives funding/margin model, or BO/SO campaign overlay is a separately specified derivative or downstream research experiment; none is silently incorporated here.

## Limitations

PASS in frontmatter is a **proposed six-gate research admission claim pending independent Hermes Auditor review**, not an auditor's decision. No lossless source-native equivalence is claimed for market, frame, fills, sizing or costs (all disclosed derivatives); no independently reproduced returns; no deployment build digest; no live fill precision or slippage validation; no Qlib parity; no survivor or production approval. Exact package identity remains a boundary; reviewer must not invent a package-to-commit mapping.

## Implementation status

`not-implemented`: strategy-specific controller and data-gap/feature logic are not committed or deployed. Pinned simulator primitives were read only.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. This record does not authorize Paper, Testnet, Live, Qlib/Hummingbot backtests, n8n, containers, cron or other runtime changes.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/WT1uzChH-Buy-The-Dips-MA200-Optimised/ — Coinrule, public open-source strategy page read 2026-10-25 (title/authorship/description prose; no Pine or date in served HTML).
- https://github.com/hasnocool/tradingview-pine-scripts/tree/69969aeaf271b2f7b5a7632a1bde43069a0cbe26 — pinned mirror (`Buy The Dips - MA200 Optimised.pine`, blob `d75360d2185a0a87be6dc5d0c4812b99e05c538c`, 2,984 bytes, byte-verified this cycle).
- https://www.fmz.com/strategy/438063 — corroborating republication prose only (rule principle, risk analysis, future-work stop-loss); demo backtest header fenced, not adopted.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source read via raw-file fetch this cycle.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — previously independently reviewed same 1d spot research execution primitive (merged 2026-10-25).
