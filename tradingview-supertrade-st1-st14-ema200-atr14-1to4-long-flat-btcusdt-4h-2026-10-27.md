---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "SupertradeOfficial ST1 Supertrend14x3 flip EMA200 filtered ATR14 1-to-4 close-bracket BTC-USDT spot 4h independent derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-05-09
sources:
  - https://www.tradingview.com/script/AyY3vB17-SuperTrade-ST1-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SuperTrade ST1 — independent Supertrend flip / EMA200 / 1:4 ATR close-bracket long-flat research derivative

## Provenance

**First-party TradingView publication:** SupertradeOfficial, *SuperTrade ST1 Strategy*, published **2025-05-09**, stable public script ID **AyY3vB17**, public page inspected **2026-10-27**: https://www.tradingview.com/script/AyY3vB17-SuperTrade-ST1-Strategy/ . The page labels the script **open source**, but its complete Pine bytes, revision/hash, actual default Supertrend ATR length/multiplier and order flags were **not retrieved**. No lossless/source-native Pine reproduction or source backtest reproduction is asserted.

**Verified source-description facts:** LONG only; bullish Supertrend direction flip, price close above the Supertrend line and above EMA200 as entry conditions; ATR-based entry stop at **1 ATR** below entry and target at **4 ATR** above entry (1:4 risk/reward). The author describes 10,000 USD initial account, 2% equity risk sizing, 0.1% commission and one tick of slippage, and suggests 1h/4h/daily charts. The page does **not** establish exact Supertrend seeds/ATR settings, whether stop/target orders are intrabar, fill timing, pyramiding, or Pine engine defaults. These unknowns are not silently supplied as author facts.

**Explicit independent derived strategy, NOT source-native/lossless:** The researcher freezes Supertrend using Wilder ATR14, factor 3, exact bands/initialization below; EMA200 with SMA seed; BTC-USDT Binance spot UTC 4h; fixed 0.001 BTC, 10,000 USDT modeled cash; one-bar-delayed historical MARKET close fills; ATR14 from the **entry-signal** candle frozen into the bracket at actual modeled entry fill; completed-close-triggered exits instead of source-described automatic stop/target orders; no 2%-of-equity sizing, no one-tick slippage, no short, no DCA, no trailing, and no other exits. All such decisions are **researcher-defined and event/economics-changing**. The source itself is not claimed to have passed HB_READY.

**Frozen derived identity:** `TV:AyY3vB17|SupertradeOfficial|2025-05-09|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC4h|ST-WilderATR14x3-bear-to-bull-flip|EMA200-SMAseed-closegt|signal-ATR14-frozen-1xSL-4xTP-close-only|t-signal-to-tplus1-modeled-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup250`. Changes to any element create a different derivative identity.

## Economic mechanism

### Source-reported

A bullish volatility-adjusted Supertrend reversal is traded only when price is above the longer-term EMA200, while a 1:4 ATR bracket seeks asymmetric reward versus risk. This is the author's stated hypothesis, not independently reproduced profitability.

### Research interpretation

The independent version tests a fully specified **completed-candle** trend-flip entry and fixed volatility-distance bracket on spot crypto. Delayed close-only exits are **not protective stop orders** and can realize substantially more loss than the nominal 1 ATR level. The 1:4 ratio applies to **trigger distances**, not guaranteed realized PnL.

## Signal

**Data and clock:** one real Binance BTC-USDT **spot 4h UTC OHLCV** series. Raw candle opening timestamp `T[t]` must increase exactly **14,400 seconds** per row; candle t is available for decisions only at or after `E[t]=T[t]+14,400`. Before the engine, reject missing/duplicate/out-of-order rows, nonfinite or nonpositive OHLC, `H<max(O,C)`, `L>min(O,C)`, negative/nonfinite volume, and any unavailable actual close. No partial candles, gap filling, forward fills, price substitution or external/fitted data.

**Researcher-pinned indicator mathematics and ties:**

1. For t>=1, `TR[t]=max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1]))`. Wilder `ATR14[14]=mean(TR[1..14])`; for t>14, `ATR14[t]=(13*ATR14[t-1]+TR[t])/14`. Prior values undefined; reject ATR<=0 where required.
2. `EMA200[199]=mean(C[0..199])`; for t>=200, `EMA200[t]=(2/201)*C[t]+(199/201)*EMA200[t-1]`. Before t=199 undefined.
3. At t=14, initialize `U[14]=(H[14]+L[14])/2+3*ATR14[14]`, `D[14]=(H[14]+L[14])/2-3*ATR14[14]`, `direction[14]=BEAR`, `ST[14]=U[14]`. For t>=15, `bu=(H[t]+L[t])/2+3*ATR14[t]`, `bd=(H[t]+L[t])/2-3*ATR14[t]`. Set `U[t]=bu` if `bu<U[t-1] || C[t-1]>U[t-1]`, else `U[t-1]`. Set `D[t]=bd` if `bd>D[t-1] || C[t-1]<D[t-1]`, else `D[t-1]`. If prior direction BEAR, current direction becomes BULL **only if** `C[t]>U[t]`; otherwise BEAR. If prior direction BULL, current direction becomes BEAR **only if** `C[t]<D[t]`; otherwise BULL. `ST[t]=D[t]` in BULL, `U[t]` in BEAR. Equalities never flip. This is a **researcher-pinned Supertrend variant**, not a claim of byte-identical `ta.supertrend()` output.
4. **Entry event on completed t:** `direction[t-1]==BEAR && direction[t]==BULL && C[t]>ST[t] && C[t]>EMA200[t]`. All comparisons strict. No entry from an already-bullish state without a new flip. A missing/invalid input aborts the research sample, never yields a false signal.
5. **Warmup:** begin FLAT with zero BTC and 10,000 USDT cash; no decisions or orders before **250 consecutive valid completed 4h candles** (first eligible index t=249). No assumed inherited inventory or inferred pre-sample signals.
6. **Entry scheduling:** when FLAT and no pending order, an entry event at E[t] stores one BUY instruction. It is **dispatched on the next actual completed row t+1**, with an idealized MARKET full fill at observed `P=C[t+1]` economically effective at `E[t+1]` (not at raw `T[t+1]`). Debit `0.001*P*(1+0.001)` USDT; require sufficient cash and a valid positive observed price, otherwise reject the order, remain FLAT and require a **new later flip**. On confirmed fill freeze `A=ATR14[t]` from the signal candle, `SL=P-A`, `TP=P+4*A`; require `A>0 && SL>0 && TP>SL`, else abort as invalid model input. No invented price or fill.
7. **Exit scheduling and precedence:** while confirmed LONG and no pending order, at completed t evaluate `C[t]<=SL || C[t]>=TP`. These frozen levels are **not intrabar exchange stop/limit orders**. If either is true, schedule one full-position SELL for the **next completed row t+1** at its actual modeled MARKET close `C[t+1]`, effective at E[t+1]; deduct `0.001*0.001*C[t+1]` quote fee. Since SL<TP, close-only stop/target triggers cannot both be true. No Supertrend bearish-flip, EMA-cross, time or discretionary exit is added. Ignore new entries while LONG/pending.
8. **Order/failure state:** signal creation alone does not change holdings. `pending=BUY/SELL` until the pinned executor reports full fill/failure; never double-submit. A failed BUY clears pending and needs a **fresh later** bearish-to-bullish flip; a failed SELL retains LONG and retries a SELL on the next valid completed bar even if the bracket predicate is no longer true. No same-bar round-trip, no re-entry on the exit bar; after a confirmed exit, a new flip on a later completed candle is required. No additional cooldown. A signal on the last observed candle cannot create a phantom next-row fill; open positions are valued only at the real final close.
9. **Explicitly disabled:** SHORT, futures/perpetuals, borrowing/leverage/margin/funding, pyramiding, DCA/BO/SO/averaging, simultaneous strategies/pairs/shared capital, compounding, partial fills/partial exits, trailing stop, opposite-signal exit, intrabar bracket execution, limit/maker/next-open orders, take-profit scaling, fixed-time exit, forced terminal liquidation, and hidden controller defaults. Absence of protective intrabar stops is a material risk.

## Required data

Single actual Binance spot BTC-USDT 4h OHLCV feed with contiguous UTC opening timestamps. No multi-asset synchronization, secondary timeframe, funding, index/mark price, order book, external indicators, model training or future extrema. Candle close and ATR at t are not available at T[t]; use E[t] as the earliest information time.

## Execution assumptions

**Pinned benchmark inspected through the connected GitHub app on 2026-10-27:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package **20260920**, `hummingbot/VERSION=dev-2.17.0`. Source paths read at that immutable commit: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, `binance_spot_candles.py`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `hummingbot/strategy_v2/executors/order_executor/data_types.py`, and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`. Existing independent package/source correspondence evidence is referenced in Alpha PR #414; no installed wheel hash or image digest was rechecked this cycle.

- **Real data path:** pinned `BinanceSpotCandles` declares `4h`; its REST parser maps `row[0]` to exchange **opening timestamp**, `row[1..5]` to real OHLCV. The provider/engine can load these rows; engine `prepare_market_data` uses `dropna`, hence a **pre-engine contiguous-candle/validity check** is mandatory to prevent silently discarded rows.
- **Real controller/action path:** `BacktestingEngineBase.simulate_execution` iterates rows, calls `update_state(row)`, `controller.determine_executor_actions()`, then `simulate_executor`. A later candidate-specific controller must keep the stored signal from t, and only on t+1 dispatch `CreateExecutorAction` with `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. The declared controller is **not implemented**; API schema alone is not used as proof of complete execution.
- **Real bounded fill model:** `OrderExecutorSimulator.simulate` MARKET branch selects the first supplied row timestamp and **that row's actual close** for price, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, `CloseType.POSITION_HOLD`. This supports a historical **t signal → t+1 row close** idealized full-fill model only if the controller delays dispatch and effective fill time is normalized to `T[t+1]+14,400`; it is **not** an achievable live post-close MARKET price guarantee. Missing close, missing row or price default is forbidden.
- **Real accounting path:** `BacktestPositionHold` in `backtesting_engine_base.py` nets opposing BUY/SELL base quantities, maintains weighted entry price, gross realized PnL and separate cumulative quote fees; final-tick flush exists. `terminated_executors_window=None` or an equivalent persistent confirmed-fill ledger is required for reliable state across long 4h gaps, rather than relying on a 3600-second truncated executor view. Do not treat an action as a fill.
- **Cost/equity boundary:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% quote-notional fee on each filled side**, not a verified exchange tier. Research net cash: BUY `-Q*Pb*(1+0.001)`; SELL `+Q*Ps*(1-0.001)`; net realized roundtrip `Q*(Ps-Pb)-0.001*Q*(Pb+Ps)`, with Q=0.001 BTC. Gross engine position PnL must not be presented as net. Mark open BTC only at last actual observed close. This derivative **does not model** the source's one-tick slippage; zero simulator slippage is a limitation, **not observed zero market slippage**. Spot funding is **not applicable**, not fabricated zero perpetual funding. Historical spread, partial fills, latency, dynamic fees, precision/step/min-notional and liquidity are **not independently validated**; any actual connector constraint failure must fail closed rather than silently produce a fill. No live-trading compatibility is claimed.
- **Data-provider hazard:** pinned `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` when price is absent. This fallback is **strictly prohibited** here: require a verified positive observed close or abort the research run. Any future implementation that uses open timestamps as close-availability timestamps or accepts a fabricated fallback fails Gates 5/6.

## Evidence

### Source-reported

TradingView SupertradeOfficial **2025-05-09**: long-only bullish Supertrend flip, close above Supertrend and EMA200, 1 ATR stop and 4 ATR target, author-described 2%-equity sizing, 0.1% fee, 1-tick slippage. No independently verified author performance figure.

### Independently reproduced

**None for strategy outcomes.** No Pine signal parity, candidate-specific Hummingbot replay, Qlib run, event-level Qlib/HB parity, performance statistics, historical fill validation, profitability, survivor status or trading. The connected GitHub inspection independently verifies the **bounded pinned-engine data/action/MARKET-close/POSITION_HOLD/fee paths**, not this strategy's implemented results.

### Negative evidence

Full original Pine bytes and exact author Supertrend settings/order semantics were unavailable. The chosen ST14×3 seed/recurrence, ATR freeze timing, stop/target as completed-close signals, t+1 close fill, spot venue, fixed size, warmup, fees, failure/re-entry state and all disabled behavior are **researcher-designed** and cannot be attributed to the author. The original 1-tick slippage and 2%-equity sizing are intentionally not reproduced.

**Six gates proposed for independent review:** (1) all indicator recurrences, ties, warmup, signals and bracket are frozen; (2) spot LONG/FLAT only; (3) entry, frozen close-only SL/TP and disabled exits complete; (4) fixed quantity/cash, one position/pending order, failure/re-entry, no DCA/concurrency; (5) pinned actual 4h feed, row/controller/MARKET close fill, position/fee model inspected with explicit limitations; (6) t completed-candle decision, t+1 completed-candle economic fill and no future/incomplete-bar leakage. This is a **Scout-proposed PASS pending independent Hermes Auditor exact-head review**, not self-approval.

**Dedup and main snapshot:** At prewrite `main=d353434dab7e682eaa6d2bd18c770060585cb61d`, README static pool count was **377**. GitHub main searches for `AyY3vB17`, `SuperTrade ST1` and source author returned no matching strategy. Ten open `research/*` PR titles/bodies contained no source identity. Nearby Supertrend records are materially different: Alorse's StochRSI crossover with ST/EMA200 as filters; BVLabs ST flip with CHOP/ADX/Plug; neither is the pure ST-flip + EMA200 + fixed 1:4 ATR bracket. Existing pool records were **not exhaustively re-audited** this cycle; the static count is not independently asserted as a full PASS census.

## Falsification plan

On future separately authorized work, replay the frozen formulas on contiguous spot 4h data, compare every decision/fill/fee/state transition against the pinned Hummingbot engine, verify effective timestamp offsets and ledger cash, and test boundary equalities, ATR initialization, missed rows, failed orders and end-of-sample signals. Only after representative execution-path Qlib/Hummingbot event-level parity may large-scale Qlib screening use this path. Evaluate net-of-assumed-fee IS/OOS separately; no claim is made now.

## Crypto portability

BTC-USDT Binance spot is a **researcher-selected** venue/pair, not an author-validated result. Porting to other symbols/timeframes or the downstream futures 3×/5× DCA campaign requires separately declared configuration/derived behavior and verification of new engine/cost/funding/margin paths. The campaign's BO/SO 6/6/6 and seven coins are **not admission prerequisites**.

## Limitations

No Pine source hash; no source-native order parity; no candidate implementation; no real stop protection; gap/latency/slippage/min-notional effects not reproduced; one-tick source slippage omitted; fee is assumed; a nominal 1:4 bracket does not guarantee 1:4 realized economics; no backtest or profitability. Source publication date is not a version-pinned Pine revision. A later contradictory primary-source fact must be independently reviewed, not silently rewritten.

## Implementation status

`not-implemented`: this is a research specification of a pinned-engine-expressible **independent derivative**, not a deployed controller, strategy runner or Qlib recipe. No backtest, container, n8n, paper, testnet, live or cron changes.

## Adoption boundary

`research-only` / `not-approved` / `approval_scope: research-only`. Scout does not merge, approve, close, change README or change existing strategies. Independent Hermes Auditor GitHub Webhook Review alone determines exact-head six-gate PASS merge, source-fact remediation or NOT_LOSSLESS close. Existing signed webhook receiver alone reconciles README after any accepted merge.

## Related Wiki records

None asserted; no new Wiki record or cross-system write.

## Sources

- https://www.tradingview.com/script/AyY3vB17-SuperTrade-ST1-Strategy/ — SupertradeOfficial, 2025-05-09, inspected 2026-10-27.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source, connected GitHub inspection 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned package/source correspondence evidence; not reverified this run.
