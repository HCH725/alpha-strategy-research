---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "NewTrader1123 SMA200-gated RSI30 recross with fixed ATR14 close bracket — independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-02-21
sources:
  - https://www.tradingview.com/script/71WjJNd8-NSE-Index-Strategy-with-Entry-Exit-Markers/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# NewTrader1123 SMA200-gated RSI30 recross with fixed ATR14 close bracket — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary first-party TradingView source inspected 2026-10-27:** NewTrader1123, *NSE Index Strategy with Entry/Exit Markers*, publicly published **2025-02-21**, stable TradingView script ID **71WjJNd8**, labeled open-source strategy: https://www.tradingview.com/script/71WjJNd8-NSE-Index-Strategy-with-Entry-Exit-Markers/ . The public description explicitly states a **200-period SMA** trend gate (price above SMA), RSI crossover above a configurable oversold threshold, ATR-based stop and target prices calculated from close plus/minus ATR times a multiplier, and **10% of equity** default sizing. The page text shows the relevant Pine expressions in prose but **the complete Pine source bytes, Pine version, revision identifier, actual RSI/ATR lengths, oversold default, ATR multiplier, intrabar order semantics, commission default, and exit-order update behavior were not retrieved**. Those unknown facts are not attributed to the author.

**Explicitly independent derived executable strategy — NOT source-native/lossless:** This record deliberately selects Binance BTC-USDT **spot UTC 1d** rather than NSE index trading, LONG/FLAT only, RSI14 Wilder crossing above **30**, SMA200(close) trend gate, ATR14 Wilder frozen **at the entry signal**, symmetrical **2.0 ATR** fixed completed-close exit thresholds, 0.001 BTC fixed size, 10,000 USDT initial cash, 250-bar warmup, and 0.1% per-side modeled fee. The source describes ATR exit prices relative to close, not a proven frozen-at-entry close bracket; this change, together with market, indicator parameters, order clock, direction, sizing, no intrabar stops and fee assumptions, is **researcher-designed** and intentionally changes possible trade events. Original TradingView backtest returns and its 10%-equity economics are not reproduced or claimed equivalent.

**Immutable research identity:** TV:71WjJNd8 | NewTrader1123 | publication:2025-02-21 | independent-derivative-v1:2026-10-27 | Binance:BTC-USDT:spot:UTC1d | SMA200(close), WilderRSI14 crossing above 30 | frozen WilderATR14 x2 symmetric completed-close bracket | LONG/FLAT, 0.001 BTC, no adds | 250-bar warmup | same-completed-close MARKET simulation | fee=0.001/filled-side. The source ID identifies provenance, not unseen Pine bytes; any decision-critical parameter, execution clock or bracket change creates a new derived identity.

**Dedup before write on main SHA 639021a9690db26cd641156672bca99e7e9e9302:** Connected GitHub search returned no 71WjJNd8 or exact NSE Index Strategy record, and open research/* PR search returned no same source or matching SMA200/RSI recross/ATR fixed-bracket mechanism. Nearest families are materially different: the admitted Coinrule oversold-RSI tight-stop record uses an RSI **below** 30 level entry, no SMA200 trend gate and fixed 1%/7% close exits; the admitted connorgeary150 RSI14/BB20 dip record requires price below the lower Bollinger band and exits via RSI50 or BB-midline reclaim; the admitted Donchian50/SMA200/ATR14 reversion record enters from price-channel location, not an RSI30 recovery cross. Distinct entry predicates and exits; not a trivial parameter variant. GitHub code-search pagination is limited and no claim of a complete independent re-audit of every existing record is made.

## Economic mechanism

### Source-reported

The author combines a 200-period trend filter with a recovery through an RSI oversold level and uses ATR-based price risk bands. The intended mechanism is buying a momentum rebound only while the longer trend is positive. No independently verified return, Sharpe, win rate, or risk statistic is adopted.

### Research interpretation

This derived test asks whether a strict RSI14 recovery **edge** (prior <=30, current >30) during a positive SMA200 regime captures rebounds with positive fee-net expectancy under a symmetric, frozen ATR14 close-only bracket. Freezing the bracket at the modeled entry, rather than recomputing it from each later close, prevents an ill-defined moving threshold. This is a new research choice, not a reconstruction of uninspected Pine.

## Signal

All rules below define the **researcher-authored independent derivative v1** and are frozen.

1. Input is one chronological, contiguous series of finite, strictly positive completed Binance BTC-USDT UTC 1d candles, indexed t=0,1,..., with open O[t], high H[t], low L[t], close C[t], volume V[t]. Require 0<O,C,H,L, L<=min(O,C)<=max(O,C)<=H and finite nonnegative V. Indicator calculations use deterministic chronological float64; modeled orders/accounting use Decimal amounts and observed candle close, with no fitting, full-sample normalization or future data.
2. SMA200[t] is the arithmetic mean of C[t-199] through C[t], first valid at t=199. Strict trend predicate is C[t]>SMA200[t]; equality does not pass.
3. Wilder RSI14(close): for t>=1 define delta=C[t]-C[t-1], gain=max(delta,0), loss=max(-delta,0). At t=14 seed average gain/loss as the simple means of the 14 differences at t=1..14; for t>=15 recursively update each average as (13*previous+current)/14. RSI=100-100/(1+avgGain/avgLoss) when both positive; if avgLoss=0 and avgGain>0 set 100, if avgGain=0 and avgLoss>0 set 0, if both zero set 50. No alternative EMA seed, rounding or adaptive threshold.
4. Wilder ATR14: TR[0]=H[0]-L[0]; for t>=1 TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1])). ATR[13] is the mean TR[0..13]; ATR[t]=(13*ATR[t-1]+TR[t])/14 for t>=14. An entry requires finite ATR[t]>0. The seed convention is an explicit research pin, not an asserted Pine default.
5. First 250 **completed** daily bars t=0..249 are no-trade warmup, starting FLAT with zero inventory. First eligible decision t=250. Calculate prior RSI and SMA normally during warmup but do not infer an earlier open position.
6. On eligible completed bar t, while FLAT with no outstanding order, enter LONG only if RSI[t-1]<=30 **and** RSI[t]>30 **and** C[t]>SMA200[t], with valid ATR[t] and sufficient modeled cash. This is a fresh crossing event, not merely RSI remaining above 30. Issue one MARKET BUY for exactly 0.001 BTC at the **observed close C[t] in the bounded historical simulator**, effective no earlier than that bar's completion. Upon confirmed full fill, freeze entry price P=C[t], entry ATR A=ATR[t], stop S=P-2*A, target T=P+2*A; require 0<S<P<T. If S<=0 or invalid, do not issue the BUY. No other entry condition, optional filter or source short leg is enabled.
7. While LONG, only on **later** completed bars t>entry_bar: if C[t]<=S, issue one full-quantity MARKET SELL at C[t] labeled CLOSE_STOP; else if C[t]>=T, issue one full-quantity MARKET SELL at C[t] labeled CLOSE_TARGET; otherwise HOLD. Exact equality triggers; stop has formal priority. High/low touching S/T does **not** trigger an order. The bracket levels never trail or recalculate, and an RSI reversal, SMA failure or opposite signal does not exit.
8. On successful SELL, return to FLAT. No same-bar BUY after SELL, no same-entry-bar SELL, no automatic re-entry from a stale crossing. Only a fresh qualifying RSI crossing on a later completed bar may re-enter. Crossings observed while LONG are ignored, not queued. One outstanding order at most; a rejected, partial, missing, or ambiguous fill **aborts the research segment** without inventing a position, fill price or repeated order.
9. End-of-sample open inventory is valued at the final actually observed completed close, with unrealized value separately reported; no fictitious forced liquidation or exit fee is booked. No session calendar filter beyond contiguous UTC daily candles, no signal on an incomplete final bar.

**Trade direction and disabled behavior:** Binance BTC-USDT unleveraged spot LONG/FLAT only. Short, borrow, perpetual funding, margin, liquidation, hedging, pyramiding, DCA/safety orders, scaling, partial exit, trailing stop, time exit, discretionary override, intrabar stop/limit, maker queue, multi-pair exposure and shared-capital synchronization are explicitly **disabled**. There is no hidden controller default stop or TP.

**Position/cash ledger:** Start with 10,000 USDT cash and zero BTC; BUY exactly Q=Decimal("0.001") BTC only if cash>=Q*C[t]*(1+f), f=Decimal("0.001"), with no compounding or leverage. Debit Q*C[t]+f*Q*C[t] on full BUY; credit Q*C[t]-f*Q*C[t] on full SELL. A full SELL nets the filled Q, never creates a short. Store FLAT/LONG, entry bar/P/A/S/T, cash, filled quantity, fees and pending flag. No additional cooldown beyond a fresh RSI cross. Exchange lot/tick/min-notional rules are not assumed satisfied in production: fail closed if an applicable rule cannot be verified for a future executable path.

## Required data

Exactly one real Binance BTC-USDT **spot 1d** completed OHLCV feed. No lower/higher timeframe, order book, external model, index/mark price, funding, volume signal, alternative exchange, portfolio join or derived future candle. Raw Binance kline timestamp T[t] is the **open** timestamp; the current candle close is available only at E[t]=T[t]+86400 seconds. Strictly validate timestamps increase by exactly 86400 seconds, no duplicates/gaps, positive finite OHLC and observed real close, **before** any backtesting-engine merge or dropna; abort rather than interpolate, forward-fill, omit a gap or use a placeholder fill price. Last incomplete candle is excluded. If a segment restarts, restart FLAT and require a new 250-bar contiguous warmup; no silent position carry.

Every signal, ATR freeze and exit predicate depends on completed prefix data only. The historical MARKET close-fill convention is a **research simulator** assumption at effective time E[t], not an assertion that a real order submitted after E[t] could receive the historical C[t]. Raw T[t] must never be reported as the causal decision/fill time.

## Execution assumptions

**Exact bounded engine:** Hummingbot package **20260920**, VERSION **dev-2.17.0**, immutable source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. This Scout read the pinned VERSION and the following native files through the connected GitHub app on 2026-10-27: BinanceSpotCandles constants.py and binance_spot_candles.py, strategy_v2/backtesting/backtesting_engine_base.py, backtesting_data_provider.py, executors_simulator/order_executor_simulator.py, and executors/order_executor/data_types.py. Previously independently reviewed PR #414 reports 902/902 package-wheel/source byte identity; **this Scout did not rehash the installed wheel or run its tests**, so package mapping is inherited, not a fresh byte audit.

**Verified bounded source path:** BinanceSpotCandles INTERVALS explicitly contains 1d; its REST parser maps Binance row[0] to open timestamp, row[1..5] to O/H/L/C/V. BacktestingEngineBase.run_backtesting initializes Binance connector trading rules, historical candle feed and controller; prepare_market_data merges features where needed and then dropna (therefore the strict raw-candle validation above is mandatory before this stage). simulate_execution iterates prepared rows, update_state(row) sets current close and processed features, then determine_executor_actions() may produce CreateExecutorAction(OrderExecutorConfig). A dedicated, **not-yet-implemented** controller would compute the declared RSI/SMA/ATR and state and emit exactly the required actions; no existing generic controller is falsely claimed to implement this strategy.

**Order model:** OrderExecutorConfig accepts connector_name=binance, trading_pair=BTC-USDT, side=BUY/SELL, amount=Decimal("0.001"), execution_strategy=MARKET, price=None, leverage=1 and explicit OPEN/CLOSE intent. OrderExecutorSimulator MARKET branch fills on the first supplied candle at its actual **close**, with filled_amount_quote=Q*close and cum_fees_quote=trade_cost*notional; it returns CloseType.POSITION_HOLD. This is a deterministic **historical close-price fill model**, not real exchange execution, next-open pricing, stop-market protective order or guaranteed spread/slippage model. The simulator stamps the raw candle **open timestamp**: downstream event-time normalization to E[t] is mandatory, or the result would have lookahead in its labels.

**Position/cost path:** BacktestPositionHold._process_order nets opposite-side BUY/SELL amounts, tracks weighted entry and **gross** realized PnL; add_executor accumulates quote fees separately. Net realized quote PnL for one round trip is Q*(exitClose-entryClose)-f*Q*(entryClose+exitClose). Explicit run trade_cost=0.001 per filled side is a **research assumption**, not a source-author commission or real Binance fee tier. Maintain independent cash/inventory/fee reconciliation, and retain durable fills/positions (e.g., terminated_executors_window=None or an explicit authoritative ledger), since a default one-hour terminated-executor view can expire between daily decisions. Final-tick ledger flushing exists in the pinned engine. Spot funding is **not applicable**, not an invented zero-funded perpetual result. No margin/futures model is invoked.

**Economic and precision limitations:** No claim of actual live fills, maker queue, partial fills, latency, order-book spread, slippage, realized exchange fee, lot precision, exchange minimums, or funding on derivatives. A source-code acceptance of OrderExecutorConfig is not by itself proof of live executability; this admission is bounded to the inspected **spot 1d MARKET close-fill and fee-net position-hold simulation**. Reject invalid/missing prices rather than using any provider fallback such as Decimal("1"). A representative Qlib/Hummingbot event-level capability check is required before using a genuinely unverified execution path in mass screening; this record itself has not been backtested.

### Six-gate HB_READY assessment — proposed Scout PASS, independent audit required

1. **Deterministic:** exact SMA200, Wilder RSI14/ATR14 seeds, RSI edge and ties, frozen 2ATR bracket, 250-bar warmup, invalid-data rules and no fitting.
2. **Direction:** BTC-USDT Binance spot LONG/FLAT; all shorts and borrowing disabled.
3. **Entry/exit/risk:** strict RSI30 up-cross plus SMA200 trend gate; fixed close-only ATR14 x2 stop/target from modeled entry; full exit precedence and all other exits explicitly disabled.
4. **Position/state:** fixed Q, cash/fee ledger, single pending/full-fill state, no DCA/concurrency, no same-bar round-trip, fresh-cross re-entry, abort on unresolved fill.
5. **Pinned compatibility:** directly inspected exact Hummingbot source's Binance spot 1d data, controller/action loop, MARKET close-price fill, POSITION_HOLD netting and per-side fee accounting, with raw timestamp and price/precision limitations.
6. **Point-in-time:** completed contiguous UTC daily bars, 250-bar warmup, prefix-only indicators, raw open timestamp corrected to close-availability time, no future extrema or partial-bar signal.

Proposed frontmatter PASS is **not Scout self-approval**. Only Hermes Auditor exact-head review determines admission.

## Evidence

### Source-reported

NewTrader1123's first-party TradingView publication 2025-02-21 states SMA200 trend filter, RSI oversold crossover, ATR-based stop/target formulas relative to close and 10%-equity default sizing. Full Pine code, defaults and order mechanics were not available in the inspected text; no source backtest statistics were independently reproduced.

### Independently reproduced

**Not independently reproduced.** No Pine replay, Hummingbot/Qlib backtest, strategy-specific fill/event parity, Sharpe, return, drawdown, OOS, survivor or HB certification. This cycle only inspected the immutable pinned Hummingbot **source paths** for bounded model compatibility; prior package identity evidence is cited, not rerun.

### Negative evidence

No inspected complete Pine bytes or immutable TradingView source revision; no source-native equivalence of frozen bracket, timeframe, fill, fee or sizing; no actual spot fills, precision proof, trading controller, exchange cost schedule, realized PnL or Qlib parity. The independent derivative defines its own missing decisions explicitly rather than attributing invented defaults to the original author.

## Falsification plan

When separately authorized for downstream implementation, compare representative pinned Hummingbot and Qlib event sequences for RSI14 seed/ties, 30-cross, SMA200 equality, ATR14 freeze, stop/target equality, one-order-per-bar, post-exit fresh-cross re-entry, insufficient cash, fee-net ledger, final-tick position, missing day, rejected fill and UTC open-to-close timestamp correction. Compare against a same-gate RSI-only recross control under identical research cost assumptions. Negative fee-net expectancy or unexplained event divergence falsifies the derivative's downstream research hypothesis. **No tests or backtests run in this Scout cycle.**

## Crypto portability

The derived Binance BTC-USDT spot 1d market is a researcher choice, not a TradingView author-tested crypto market or HB_READY whitelist. Other assets, 1h/4h, 3m, short, isolated futures 3x/5x and house BO/SO 6/6/6 are **optional downstream separately declared experiments**, not admission requirements. Any event-changing overlay requires its own explicit derivative/cost/causality specification and verified engine capability.

## Limitations

Original source is NSE-index-oriented and its complete Pine code was not inspected. A close-only bracket can exit far beyond the nominal 2ATR stop on a gap, and it is not protective intrabar risk management. Same-completed-close MARKET fills are idealized simulator economics, not guaranteed live fills. Actual exchange precision, spread, slippage, fees and liquidity are unverified. No profitability or implementation approval is implied.

## Implementation status

**not-implemented.** This is a frozen, inspectable research specification, not an existing Hummingbot controller, Qlib executable recipe, deployed bot or strategy replay. An approved downstream selection may need minimal strategy-specific materialization and representative capability validation, not a second admission registry.

## Adoption boundary

**research-only; not-approved; approval_scope: research-only.** Independent Hermes Auditor owns source-fact review and exact-head PASS merge or NOT_LOSSLESS close. Only the existing signed GitHub webhook receiver owns post-merge README bookkeeping. No merge, trading, Paper, Testnet, Live, deployment or Qlib/Hummingbot backtest is authorized by this record.

## Related Wiki records

None created or modified. The three comparison families in Provenance are existing distinct strategy identities, not a new registry or shared implementation.

## Sources

- TradingView first-party: https://www.tradingview.com/script/71WjJNd8-NSE-Index-Strategy-with-Entry-Exit-Markers/ (NewTrader1123, published 2025-02-21, inspected 2026-10-27).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent package/source mapping and engine primitive evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Admission policy: https://github.com/HCH725/alpha-strategy-research/blob/639021a9690db26cd641156672bca99e7e9e9302/.github/HB_READY_REVIEW.md
