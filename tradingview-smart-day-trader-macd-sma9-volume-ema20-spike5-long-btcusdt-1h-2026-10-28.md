---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Smart-Day-Trader MACD SMA-signal crossover with recent high-volume confirmation — independent BTCUSDT spot 1h derivative
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-10-23
sources:
  - https://www.tradingview.com/script/kFSPpZbG-smart-macd-volume-trader/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD SMA9 crossover with five-bar volume-spike memory — independently derived spot strategy

## Provenance

- **First-party public source:** *Smart MACD Volume Trader*, **Smart-Day-Trader**, published **2025-10-23**, stable TradingView script ID **kFSPpZbG**: https://www.tradingview.com/script/kFSPpZbG-smart-macd-volume-trader/ . Public open-source **indicator** description inspected 2026-10-28. Complete Pine source bytes, Pine revision/version and an immutable author-code digest were not accessible; this record does **not** assert a source-native Pine port or original strategy performance.
- **Verified author-description facts:** fast EMA(close,12), slow EMA(close,26), MACD=fast-slow, **SMA** (not the usual EMA) of MACD over 9 bars as signal, EMA(volume,20), high volume at **2.0 times** the volume EMA, a **5-bar recent high-volume** lookback, buy on bullish MACD/signal crossing with recent high volume, sell on bearish crossing with recent high volume. Crypto uses its own chart volume rather than the author's CME/COMEX cross-asset mapping. The page calls this an indicator and explicitly recommends additional risk controls; it does not define a complete standalone automated trade/fee/position model.
- **Explicitly independent derived executable strategy:** This record turns the indicator's buy/sell signals into a fully specified LONG/FLAT BTC-USDT Binance spot 1h state machine. Researcher choices (NOT author facts) are: first-observation EMA seeds, inclusive five-bar high-volume window and tie semantics, positive-volume-baseline requirement, long-only orders, bearish confirmed signal as the sole exit, no protective stop/target/trailing/time exit, one 0.001 BTC position, 10,000 USDT initial cash, 120-bar warmup, UTC 1h completed-bar decision/idealized same-close MARKET fill, gap/cash/fee/ledger rules, and disabling the original alert-session and forex/commodity volume mapping. These change event and economic semantics; this is **not** a lossless original indicator/strategy conversion.
- **Frozen strategy identity:** `TV:kFSPpZbG|Smart-Day-Trader|2025-10-23|independent-derived-v1-20261028|BinanceSpot-BTC-USDT-UTC1h|MACD-EMA12-26-SMA9-cross|volume-EMA20-ge2x-in-last5|LONG-FLAT|same-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup120`. Any modification to these rules, seeds, timeframe, market, execution clock or costs is a different derivative.

## Economic mechanism

### Source-reported

The author describes a MACD momentum cross conditioned on a recent high-volume print, with an unusual SMA-smoothed MACD signal line and native crypto volume. The publication provides no independently reproduced return evidence here. Its multi-market CME/COMEX mappings are **not** part of this derivative.

### Research interpretation

Hypothesis only: a bullish MACD rotation accompanied by a volume spike in the current or preceding four completed bars may be more selective than a naked MACD cross. A bearish cross without the same recent volume gate does **not** exit; the strategy can hold a loss for an unbounded period. This is a research hypothesis, not a demonstrated edge or protective risk control.

## Signal

**Frozen independent derivative; six-gate proposal, not self-approval.** One Binance BTC-USDT spot **1h** UTC-aligned OHLCV stream. Bar `t` has UTC open timestamp `T[t]` and is not decision-available until `E[t]=T[t]+3600 seconds`.

- **EMA seeds and recursion (researcher pin):** For any series `x`, `EMA_n(x)[0]=x[0]`; for `t>0`, `EMA_n(x)[t]=(2/(n+1))*x[t]+(1-2/(n+1))*EMA_n(x)[t-1]`. Compute independently on each contiguous valid segment, not using future values or whole-sample normalization.
- `fast[t]=EMA_12(close)[t]`, `slow[t]=EMA_26(close)[t]`, `macd[t]=fast[t]-slow[t]`. `signal[t]=(macd[t]+...+macd[t-8])/9` (nine-term **simple** average, defined from the ninth completed bar onward). `vmean[t]=EMA_20(volume)[t]`.
- `spike[t]=(vmean[t]>0 && volume[t]>=2.0*vmean[t])`. A positive volume-EMA floor is an explicit researcher-added guard against treating an all-zero-volume window as a spike; the author page does not specify that edge case. All finite comparisons are exact; equality passes the 2.0x threshold.
- `recentSpike[t]=OR(spike[t],spike[t-1],spike[t-2],spike[t-3],spike[t-4])` over **five** completed bars including the current bar; no future bars, no delayed volume confirmation, no external futures volume.
- `bullCross[t]=(macd[t-1]<=signal[t-1] && macd[t]>signal[t])`; `bearCross[t]=(macd[t-1]>=signal[t-1] && macd[t]<signal[t])`. Current equality does not fire; previous equality permits a fresh edge. Both cannot occur simultaneously.
- **FLAT → LONG:** at an eligible completed bar with `bullCross[t] && recentSpike[t]`, and enough cash for the declared full BUY plus fee, create one modeled MARKET BUY of exactly **0.001 BTC** at the bar's actual `close[t]`. If funds are insufficient, stay FLAT and do not fabricate an execution or defer the expired cross.
- **LONG → FLAT:** at an eligible completed bar with `bearCross[t] && recentSpike[t]`, create one modeled MARKET SELL of the entire filled 0.001 BTC at `close[t]`. Exit is **not** conditioned on profitability or any additional trend filter. A bearish cross without recentSpike is a HOLD, not a deferred exit.
- **Position state and disabled behaviors:** initial FLAT, no short/borrow/leverage, max one long, no pyramiding, DCA/safety orders, partial entries/exits, simultaneous orders, cross-pair shared capital, rebalancing, cooldown, trailing, SL, TP, time exit, session gate, intrabar/stop/limit/maker fills or final forced liquidation. One action per completed bar; a LONG+buy flag and FLAT+sell flag are no-ops. After a filled SELL, the **next** later eligible bar can re-enter only on a new qualified bullish cross. At end of data, any LONG remains marked at last valid close, without invented SELL.
- **Warmup and invalid inputs:** first **120 consecutive valid completed 1h bars** are FLAT (no signals/orders); start testing at the 121st completed bar. Validity requires exact one-hour UTC spacing, finite positive O/H/L/C, `high>=max(open,close)`, `low<=min(open,close)`, finite nonnegative volume and no duplicate timestamp. Any invalid/missing candle stops new signals/fills, resets the 120-bar warmup and EMA seeds for the next contiguous segment, and leaves an already filled LONG held without synthetic liquidation. No interpolation, forward fill or invented price. Historical state is never recomputed from future bars.

## Required data

Binance spot BTC-USDT 1h open-timestamped O/H/L/C/volume. Only `close` and `volume` enter signals; O/H/L validate candle integrity. No second symbol, higher/lower timeframe, external futures/FX volume, OI, funding, order book, model artifact, training set, calendar or current incomplete candle. 120 completed contiguous bars cover EMA26 and SMA9 seeding, EMA20 volume, the five-bar spike window and one-bar crossover lookback.

## Execution assumptions

- **Pinned engine identifiers (Gate 5):** Hummingbot policy package **`20260920`**, VERSION **`dev-2.17.0`**; source inspected via connected GitHub at **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. `setup.py` in that source history reports a different distribution version string; that is **not** concealed or treated as a package digest. Previously independent Auditor-reviewed PR #414 documents wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148` and 902-file byte correspondence with the pinned commit. **This Scout did not independently re-download or hash that wheel**; Auditor must decide whether the prior evidence applies to this exact path.
- **Actual candle path inspected:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1h`; `binance_spot_candles.py` `_parse_rest_candles` maps REST row `[0]` to the **bar-open** timestamp and row `[1..5]` to OHLCV. `backtesting_data_provider.py` retrieves the configured candle interval. `BacktestingEngineBase.simulate_execution` iterates prepared rows, invokes `controller.determine_executor_actions()` and handles `CreateExecutorAction`. A strategy-specific controller for this record is **not implemented**; it must enforce the exact signal, state, gap and effective-time rules.
- **Actual execution path inspected:** `OrderExecutorConfig` supports `ExecutionStrategy.MARKET`, `TradeType.BUY/SELL`, amount, connector, trading pair and leverage=1. `OrderExecutorSimulator.simulate` fills MARKET on the first supplied row using **that row's close**, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates with `CloseType.POSITION_HOLD`. This is a bounded historical **close-fill** simulation, not proof of exchange close-price execution. Controller state is based on confirmed simulated fill events; do not infer inventory from terminated-executor display windows or rely on delayed POSITION_HOLD aggregation.
- **Causal clock:** Hummingbot's raw candle timestamp is an **opening** label; it must **never** be interpreted as permission to see the future closing price at bar open. Controller feature availability and modeled decision/fill are normalized to `E[t]=T[t]+3600` only after the bar is complete. The same-row close-fill is an explicit idealized historical convention, not a real executable post-close price guarantee. No next-open, intrabar or maker semantics are claimed. Missing actual close prices stop the candidate; `backtesting_data_provider.get_price_by_type` has a `Decimal("1")` fallback that is explicitly **forbidden** as a substitute for absent trade prices.
- **Costs, capital and accounting:** initial unborrowed cash `10000 USDT`, initially zero BTC, fixed `Q=0.001 BTC`, hypothetical `trade_cost=0.001` (**0.1% per full BUY/SELL side**), no additional simulated slippage in this chosen path (not an assertion of actual zero slippage). Each BUY debits `Q*P*(1+0.001)` USDT and adds Q BTC; each SELL removes Q BTC and credits `Q*P*(1-0.001)` USDT. Track realized net PnL as matched gross proceeds minus both fees, open mark-to-market as remaining BTC times last valid close, and reconcile against simulator per-fill quote/fee events. Simulator uses float quote arithmetic; keep a separate Decimal cash/BTC ledger and fail closed on unexplained material residuals or missing/failed/partial fills, rather than invent prices or silently count gross-only `net_pnl_quote` as fee-inclusive. Spot funding is **not applicable**; futures funding, margin, liquidation and borrow fees are **not modeled or asserted zero**. Tick/lot/min-notional, real spreads, latency, partial fills and actual exchange fee tier are **not verified** and no exchange-valid/live guarantee is made.
- **Reused capability, not new backtest:** prior independently reviewed PRs #414, #421 and #423 establish representative pinned Binance spot OHLCV/MARKET-close/POSITION_HOLD research primitives and the fee/clock limitations. This record adds only a controller-side causal MACD/volume predicate using existing OHLCV, not a new data or execution primitive. It has **not** been implemented or backtested; representative Qlib/Hummingbot event-level parity is still required before mass Qlib screening of an unverified strategy/execution path.

## Evidence

### Source-reported

TradingView Smart-Day-Trader first-party public description dated 2025-10-23, directly inspected 2026-10-28: MACD EMA12/26 with **SMA9** signal, volume EMA20, 2.0x threshold, five-bar lookback, bullish/bearish cross gated by recent high volume, and native volume for crypto. This is an **indicator**, not an independently verified executable strategy. No original Pine source digest, author trade fills, Sharpe, return, or backtest figures are claimed.

### Independently reproduced

**None for this candidate.** Direct source-description verification, pinned Hummingbot source-path inspection and prior independent engine primitive audit references are evidence of proposed expressibility only, not a strategy run, independent reproduction of original results, Qlib parity or Hermes PASS.

### Negative evidence

Original Pine bytes and original author trade-state/risk defaults are unavailable; no source-native equivalence. Original indicator advises external stops and optional session filters; this independent derivative explicitly **does not** implement those and may sustain unlimited drawdown. Volume feeds and EMA seed choices can shift signal bars. Zero modeled slippage is a bounded simulation assumption, not economic realism. No deployed strategy controller or package artifact was reverified in this cycle.

## Falsification plan

Only in separately approved downstream research, freeze this record and compare its qualified crosses against naked MACD crosses and against same-bar-only volume confirmation on predetermined IS/OOS periods. Do not select by OOS or claim source profits. Before large-scale Qlib screening of a novel execution path, perform representative Hummingbot/Qlib event-level parity; this Scout performed **no backtest**.

## Crypto portability

Current declared derivative is **BTC-USDT Binance spot 1h**; this is a selected research instance, not a universal HB_READY pair/timeframe restriction. Futures, other pairs/frames, the BO/SO 6/6/6 experiment and external volume mappings would be separately specified changes and require their own model/economic evidence.

## Limitations

`hb_ready_status: PASS` is the **Scout's proposed six-gate research-admission claim pending independent Hermes Auditor review**, not an audit outcome. It does not certify source-native Pine equivalence, profitability, actual fill prices/fees, a deployed implementation, Qlib parity, survivor status or Paper/Testnet/Live authorization. Auditor must independently validate the source facts, the pinned wheel/source evidence and the complete state/clock/fee semantics; otherwise reject as `NOT_LOSSLESS` without weakening main.

## Implementation status

`not-implemented`: no dedicated strategy controller, deployment artifact or Qlib executable recipe is claimed to exist. This is not a second admission gate.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. Scout never approves/merges/closes, writes README, backtests, trades, deploys or changes any workflow.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/kFSPpZbG-smart-macd-volume-trader/ — Smart-Day-Trader, 2025-10-23; author description inspected 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected via GitHub connector.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — independently reviewed pinned wheel/source identity and MARKET/ledger primitive.
- https://github.com/HCH725/alpha-strategy-research/pull/421 — independently reviewed Binance spot 4h MARKET-close path.
- https://github.com/HCH725/alpha-strategy-research/pull/423 — independently reviewed same bounded engine primitive.
