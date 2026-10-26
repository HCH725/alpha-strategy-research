---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "gpsrosario RSI29 recovery with BB20 upper-rail crossunder exit — independent spot long-flat derivative"
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-07-27
sources:
  - https://www.tradingview.com/script/5VupZDbT/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI29 recovery / Bollinger upper-band crossunder exit — independent BTC-USDT spot daily long-flat derivative

## Provenance

- **Primary public TradingView source:** gpsrosario, *RSI+BOLLINGER (LONG & SHORT)*, published **2025-07-27**, stable script ID **5VupZDbT**, directly inspected 2026-10-26: https://www.tradingview.com/script/5VupZDbT/ . The publicly readable description identifies (i) buy on RSI crossing **above 29** (its stated default), (ii) short on RSI crossing below **71**, (iii) close a long when price crosses **below the upper Bollinger Band**, (iv) close a short when price crosses **above the lower band**, and (v) a cascade filter suppressing consecutive trades when favorable movement is insufficient. The page labels the indicator open-source but did **not** expose the full Pine source to this research reader. Exact original RSI lookback, BB length/multiplier/variance convention, cascade formula, Pine fill behavior and precedence were **not** verified. None is attributed to the author below.
- **Explicit independent derivative, NOT source-native or lossless Pine:** Preserve only the author's *RSI oversold recross → long entry; upper-BB crossunder → long exit* signal pairing and the published 29 threshold. Researcher independently chooses RSI(14) with explicitly seeded Wilder RMA, BB(20,2) population standard deviation on close, BTC-USDT Binance **spot 1d UTC**, short side disabled, cascade filter disabled, single fixed 0.001 BTC position, 10,000 USDT initial cash, 60 completed-bar warmup, strict complete-candle continuity, explicit exit-over-entry priority, no stops/targets/DCA, synthetic completed-row close MARKET fills, and fixed hypothetical 0.1% per-side fees. **Every one of these choices may change source-native trade events**; no original-code or source-equivalent performance claim is made.
- **Immutable research identity:** `TV:5VupZDbT|gpsrosario:2025-07-27|derived-v1-RSI14-RMA-crossup29-BB20-2-pop-close-crossdown-upper|BinanceSpot:BTC-USDT:1d|long-flat:0.001BTC|synthetic-row-close:fee0.001|2026-10-26`. Changing any component requires a new explicitly identified research revision, not a silent update.
- **Pre-write dedup:** GitHub connector searches on current `main` SHA `e952b3cfeaf9a6c5a79e430561908118040cc89e` found no `5VupZDbT` or `gpsrosario`; open PR search found neither. Main already includes ChartArt's *simultaneous RSI50 and lower/upper BB joint-cross two-sided reversal*, Freqtrade's *RSI<30 AND below lower BB dip with RSI>70 exit*, and Forven's *upper-BB breakout with RSI<30 and midline/RSI70 exit*. This derivative instead enters solely on **RSI29 recross** and exits solely on **upper-BB downward recross**; neither band position nor RSI is an entry conjunction with the other indicator. This is a materially different signal/exit topology, not a mere threshold or timeframe variant.

## Economic mechanism

### Source-reported

The author proposes RSI recovery from oversold as a bullish reversal entry and a later downward crossing of the upper Bollinger rail as the long-closing event. The author also proposes a short-side mirror and a cascade filter, neither of which this derivative retains. The source reports no independently validated profitability, fill statistics or net-of-fee result in the accessible description.

### Research interpretation

A recovery entry can remain exposed while price trends upward through a volatility-adjusted upper rail; the first subsequent downward recross of that rail realizes the exit. If price never trades above the rail and then recrosses it, this position may remain open indefinitely. This asymmetric exposure and the missing protective stop are deliberate properties of the disclosed derivative, not claims of safety or a verified edge.

## Signal

Frozen, causal formulas on the completed daily candle at index `t`, with UTC candle opening timestamp `o_t`:

1. `delta_t = close_t - close_(t-1)`; `gain_t = max(delta_t,0)`; `loss_t = max(-delta_t,0)`. For RSI14 seed at `t=14`, set `avgGain_14 = mean(gain_1..gain_14)` and `avgLoss_14 = mean(loss_1..loss_14)`; thereafter `avgGain_t = (13*avgGain_(t-1)+gain_t)/14` and likewise for loss. RSI = `100 - 100/(1 + avgGain/avgLoss)`; if loss=0 and gain>0, RSI=100; if gain=0 and loss>0, RSI=0; if both zero, RSI=50. No alternate EMA/TA-Lib seeding is silently substituted.
2. `basis_t = mean(close_(t-19)..close_t)`; `sd_t = sqrt(sum((close_i-basis_t)^2 for i=t-19..t)/20)`; `upper_t = basis_t + 2*sd_t`. The lower band is irrelevant to this long-only derivative. All comparisons use unrounded numerical values; no plotted offsets.
3. `entry_t = (RSI_(t-1) <= 29) AND (RSI_t > 29)` — strict current-bar cross above the source-reported 29 level. RSI exactly 29 on the current bar does not enter.
4. `exit_t = (close_(t-1) >= upper_(t-1)) AND (close_t < upper_t)` — strict downward price cross of the current upper band, using both completed bars. A touch at the current upper band does not exit.
5. **Priority and state:** evaluate exit first. If LONG and `exit_t`, submit a full-quantity SELL. If FLAT and `exit_t`, remain flat and **suppress an entry on that same bar** even if `entry_t` is true. Otherwise, FLAT and `entry_t` submits a BUY. While LONG, any new entry is a no-op. No same-bar exit/re-entry. Pending BUY/SELL states forbid any additional order until the simulated fill is confirmed. After confirmed SELL, re-entry requires a **later** completed bar with a fresh RSI upward crossing; no extra cooldown.
6. **Disabled behaviors:** SHORT and reverse, cascade filter, stop-loss, take-profit, trailing stop, time limit, profit lock, additional entries, partial exits, DCA/SO, pyramiding, shared capital, other pairs, leverage, margin and end-of-series forced liquidation are **all disabled**. The upper-band downward cross is the **only** long exit, including when losing money. If it never occurs, remain LONG through the end.

The source's short/cascade functionality and its undisclosed Pine settings are not reconstructed; the signal is evaluated **as an independent derivative**.

## Required data

- Exactly one Binance spot `BTC-USDT` 1d UTC OHLCV feed. Signal math reads only `close`; `open/high/low/volume` are validated for candle integrity and may be retained as feed metadata, never used to invent a fill. Each candle opening timestamp must increase by exactly 86,400 seconds, with finite positive OHLC, `high >= max(open,close)`, `low <= min(open,close)`, and finite nonnegative volume. Missing, incomplete, duplicate, out-of-order, gapped, nonpositive or nonfinite candles **invalidate the run**; no forward fill, interpolation, gap compression, synthetic price or automatic dropping of a bad interval.
- Warmup: first **60 fully completed** contiguous daily candles, indices 0..59, are flat with no orders. First eligible signal is index 60, after its full close is known; RSI14 and BB20 and their previous-bar comparisons are already seeded. Indicator recurrence uses only preceding and current completed data. No full-sample fitting, `security()`, external series, future extremum, negative shift, repainting or partial higher-timeframe candle.
- Decision clock: Binance REST candle `timestamp` is the **opening** label `o_t`, not the instant its close becomes known. The derivative's decision and synthetic economic fill clock are `o_t + 86400s` after the complete candle, never `o_t`. The Hummingbot engine may retain the opening label internally; the resulting trade report must distinguish that label from the economic availability time and must not pretend an actual market order was sent at `o_t`.

## Execution assumptions

- **Pinned benchmark:** Hummingbot distribution package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly read `hummingbot/VERSION` and the source paths below through the GitHub connector on 2026-10-26. Prior independently reviewed alpha PR **#414** supplies the distribution-to-source byte-equivalence evidence; **this Scout did not rehash the wheel**. If that evidence cannot be relied on by the independent auditor, Gate 5 must fail pending a real pin verification, not be guessed.
- **Pinned feed path actually inspected:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` maps `1d` to `1d`; `.../binance_spot_candles.py::_parse_rest_candles` takes REST `row[0]` as candle-open timestamp and OHLCV from `row[1..5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` exposes `timestamp_bt`, `close_bt` and OHLCV on the processed row, and calls `dropna`. That `dropna` **does not guarantee continuity**: the above strict full-series preflight is mandatory before evaluation.
- **Pinned controller/executor path actually inspected:** `BacktestingEngineBase.simulate_execution` walks processed rows, calls `update_state` then `controller.determine_executor_actions`, and simulates `CreateExecutorAction`. `OrderExecutorConfig` supports `connector_name=binance`, `trading_pair=BTC-USDT`, BUY/SELL, `amount=Decimal("0.001")`, `leverage=1`, `execution_strategy=MARKET`, `price=None`. `OrderExecutorSimulator.simulate` for MARKET selects the **first supplied row's close** as fill price and its **opening-labeled timestamp** as internal fill label; records `filled_amount_quote = 0.001*close`, `cum_fees_quote = trade_cost*filled_amount_quote`, and `POSITION_HOLD`. This is a bounded **synthetic same-processed-row close** fill, not real post-close executable liquidity or actual intrabar pricing. No maker, limit, next-open or partial-fill assumption is required by this derivative.
- **Position/cost compatibility actually inspected:** `BacktestPositionHold._process_order` nets the opposite 0.001 BTC SELL against the held BUY and computes gross realized quote PnL, with `cum_fees_quote` tracked separately. A dedicated (not-yet-implemented) controller must keep `FLAT/PENDING_BUY/LONG/PENDING_SELL` states and executor IDs, reconcile only confirmed simulated fills, and prevent duplicate orders while confirmation is pending. It must not rely on the one-hour-pruned terminated-executor view for multi-day position memory.
- **Frozen research economics:** unborrowed starting cash **10,000 USDT**; one BUY only when `cash >= 0.001*close_t*(1+0.001)`; BUY debit `0.001*close_t*(1+0.001)`; SELL credit `0.001*close_t*(1-0.001)`; `trade_cost=0.001` **per side** in the engine, corresponding to a fixed hypothetical **0.1%** research fee, not an observed Binance fee. Net realized quote PnL of a closed trade = `0.001*(sellClose-buyClose) - 0.001*0.001*(buyClose+sellClose)`. Do not subtract fees twice from the engine's gross realized PnL. If an entry is unaffordable, remain FLAT and await a later *fresh* RSI crossing. A MARKET fill missing its actual close price or failing state reconciliation invalidates the run; no fill is invented. No futures contract, borrowing, leverage, margin or funding: **spot funding is inapplicable**, not fictitious zero futures funding.
- **Limits:** The pinned backtest assumes fills at the processed candle's close, with **no separately modeled spread/impact/slippage**; that is a limitation of the synthetic research model, **not a claim of real zero slippage**. Real exchange fees, minimum notional, tick/lot precision, partial fills, latency and order rejection are not validated. The controller and cash guard are declared specifications, not proof of deployed code. HB_READY is expressibility on this bounded path, not profitability, real-world execution equivalence, Qlib parity or live permission.

## HB_READY six-gate evidence — Scout proposal only

1. **Determinism:** complete Wilder RSI14 seed/recurrence, BB20 population deviation, threshold 29, explicit crossings, priority and frozen model.
2. **Direction:** long/flat on spot; source's short leg is **explicitly disabled** as a material derived change.
3. **Entries/exits/risk:** RSI upward recross entry, upper-BB downward recross exit, same-bar conflict rule; all protective and discretionary behaviors explicitly off.
4. **Position/state:** one 0.001 BTC position, cash check, pending-order reconciliation, no DCA, concurrency, pyramiding or cooldown, later-bar re-entry.
5. **Pinned compatibility:** directly inspected Binance spot daily feed, backtest row/controller loop, MARKET close-fill/fee simulator, and position netting at the exact pinned commit; prior #414 package binding disclosed rather than falsely reverified. Spot economics and synthetic fill limits declared.
6. **Causality:** 60 contiguous completed-bar warmup, previous/current comparisons only, opening label separated from completion clock, no future data, incomplete candle blocked.

**`hb_ready_status: PASS` is a proposed Scout assessment, subject to independent Hermes Auditor exact-head review.** It is not a claim that the source's complete Pine script, cascade behavior, profitability, Qlib event-level parity, HB certification or trading approval has been reproduced.

## Evidence

### Source-reported

TradingView description, gpsrosario, 2025-07-27: long RSI crossing above oversold default 29; short RSI crossing below overbought default 71; long close on price crossing below upper Bollinger Band; short close on price crossing above lower band; an additional cascade filter exists. No independently verified Pine source, original BB/RSI lookbacks, full cascade formula, native order precedence, trade count or realized performance were available in the page text.

### Independently reproduced

**Not independently reproduced.** No TradingView trade-by-trade replication, Qlib/Hummingbot backtest, fill-level parity or performance calculation occurred.

### Negative evidence

- No original full Pine listing obtained; never claim source-native equivalence.
- Existing main README advertises **347** root strategy records at initial SHA `e952b3cfeaf9a6c5a79e430561908118040cc89e`; recursive main tree contains **347** root-level strategy Markdown records. Count equality alone does not prove all 347 have independently valid PASS frontmatter; no count-integrity incident is asserted from equality alone.
- Dedup searched main for `5VupZDbT`, `gpsrosario` and related RSI/Bollinger mechanisms and open research PRs for the exact source identity; no matching source or materially identical entry/exit pairing was found.

## Falsification plan

Before large-scale Qlib screening, independently recompute RSI and BB on contiguous 1d Binance spot bars and compare the exact ordered entry/exit event list, including RSI=29 ties, upper-band ties, simultaneous entry/exit signals, first eligible bar, insufficient cash, pending confirmation, and final open positions. Validate one representative Qlib/Hummingbot event-level path if any new execution primitive is introduced; reuse already verified close-MARKET path otherwise. Any mismatched signal timing, fee ledger, quantity or state invalidates the declared derivative until corrected; do not re-label as a profitable survivor.

## Crypto portability

The frozen record is single-market Binance BTC-USDT spot daily long/flat. Different assets, shorter intervals, futures margin/funding, multi-market synchronization, or DCA 6/6/6 are **separate downstream research configurations/derived experiments**, not prerequisites for this HB_READY admission and not silently inherited.

## Limitations

The public page does not reveal all Pine implementation details. The original short and cascade filter are disabled; RSI/BB variant, tie priority, market, size, warmup, fill and cost rules are researcher-defined and can materially alter trades. No stop may cause large drawdown or indefinite holds. Synthetic same-row-close MARKET fills and fixed research fees do not model production execution economics. No performance, Qlib parity, HB certification or live readiness is claimed.

## Implementation status

**not-implemented.** No controller, executable Qlib recipe, deployment, backtest or trade was created. Future strategy-specific materialization, if selected, uses the existing IMPLEMENTATION_NEEDED route without adding a new admission flag.

## Adoption boundary

**research-only / not-approved / approval_scope: research-only.** No Paper, Testnet, Live, container, cron or workflow changes are authorized.

## Related Wiki records

None added or modified.

## Sources

- TradingView primary public page: https://www.tradingview.com/script/5VupZDbT/ (gpsrosario, published 2025-07-27; read 2026-10-26).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed package/source pin evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
