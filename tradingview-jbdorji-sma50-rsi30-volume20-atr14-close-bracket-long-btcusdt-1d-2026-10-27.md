---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "jbdorji SMA50/RSI14/volume20/rising-ATR14 confluence with fixed close-bracket — independent BTC-USDT spot 1d long-flat derivative"
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
source_as_of: 2025-01-28
sources:
  - https://www.tradingview.com/script/pBKov6w7-SMA-RSI-Volume-ATR-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# jbdorji SMA50/RSI14/volume20/rising-ATR14 confluence with fixed close-bracket — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**First-party TradingView publication inspected 2026-10-27:** jbdorji, *SMA + RSI + Volume + ATR Strategy*, published **2025-01-28**, stable public script ID **pBKov6w7**, https://www.tradingview.com/script/pBKov6w7-SMA-RSI-Volume-ATR-Strategy/ . The public description states a 50-period SMA, RSI below 30 for a long, close above SMA50, volume above its average, ATR increasing, a long-side **1.5% take-profit** and **0.5% stop-loss**, and a separate short setup when price is below SMA50 and RSI above 70. The description does not provide complete Pine bytes, exact RSI/ATR/volume averaging lengths, indicator initialization, original order-processing flags, position sizing, pyramiding, intrabar fill precedence, commission, or revision hash. None of those unknowns are claimed as source facts.

**Explicitly independent derived executable strategy, NOT source-native/lossless:** This record selects Binance BTC-USDT **spot UTC 1d**, LONG/FLAT only, Wilder RSI14, Wilder ATR14, 20-bar volume SMA, the author's SMA50 and strict four-way confluence, a researcher-defined **false-to-true confluence edge**, fixed 0.001 BTC full-size orders, a one-completed-bar delayed MARKET close-fill model, a **completed-close signal** at the source-described 0.5%/1.5% bracket (not intrabar protective orders), a 100-completed-bar warmup, and a hypothetical 0.1% fee per filled side. All additions/changes are researcher-defined and may change trade events. The original short, intrabar stops, original position sizing, original Pine defaults and original backtest economics are **not** reproduced.

**Immutable strategy identity:** TradingView:pBKov6w7 | jbdorji | source-publication:2025-01-28 | independent-derivative-v1:2026-10-27 | binance:BTC-USDT:spot:UTC1d | SMA50(C), WilderRSI14(C)<30, V>SMA20(V), WilderATR14 rising | false-to-true entry edge | full-quantity fixed 0.5%-stop/1.5%-target close-trigger | signal-completed-bar s -> next bar s+1 modeled CLOSE fill | 0.001 BTC | 100-bar warmup | modeled fee=0.001 per side. Any alteration of signal, risk, fill clock or size changes this derivative identity.

**Dedup at main SHA b73b37441f0d4a75d2377eaaab0c5917143a965d:** Connected GitHub default-branch searches for pBKov6w7, jbdorji and the named source returned no matching source record. Open research/* PRs (10 listed) and open PR searches for source ID, author and mechanism returned no matching candidate. Nearest main records are materially distinct: NewTrader1123 requires an **RSI30 upward recross** with SMA200 and ATR-distance exits, not persistent RSI<30 plus volume and rising-ATR filters; Catching-the-Bottom requires RSI fall and SMA50/100 down-cross; the Forven ATR-volume breakout does not use RSI oversold plus SMA50 confluence. No claim that a simple RSI parameter variant constitutes a new family.

## Economic mechanism

### Source-reported

The author describes an oversold long during an SMA50-positive regime only when volume is above average and ATR is rising, followed by asymmetric percent-based exits. This combines trend regime, countertrend oscillator, participation and volatility expansion. No source performance number is adopted.

### Research interpretation

The independent derivative tests whether a **newly formed** four-way confluence (rather than every persistent oversold bar) has positive fee-net expectancy under fixed, delayed completed-close exits. The 0.5%/1.5% levels are nominal *decision thresholds*, not a guarantee of bounded realized loss or a replica of Pine stop/limit fills.

## Signal

All clauses below are the complete **researcher-authored derivative v1**; source-native facts are separated above.

1. Use one chronological, gap-free Binance BTC-USDT spot **UTC 1d** OHLCV sequence indexed t=0,1,..., with finite strictly positive O,H,L,C, finite V>=0, L<=min(O,C)<=max(O,C)<=H. Validate each observed bar's opening timestamp T[t] is UTC midnight and T[t+1]-T[t]=86400 seconds, with no duplicates. No interpolation, forward-fill, synthetic prices, unseen final incomplete bar, or full-sample fitted parameters. Calculate indicators sequentially in float64 without interim rounding; use Decimal for modeled fills, cash and fees.
2. SMA50[t] = arithmetic mean(C[t-49..t]), valid at t>=49. VolumeSMA20[t] = arithmetic mean(V[t-19..t]), valid at t>=19. The current bar is included in each completed-bar indicator. Strict C[t]>SMA50[t] and V[t]>VolumeSMA20[t]; equality fails.
3. Wilder RSI14(C): delta[t]=C[t]-C[t-1] for t>=1; gain=max(delta,0), loss=max(-delta,0). At t=14 seed average gain and loss with the arithmetic means of 14 differences t=1..14; thereafter each average=(13*previous+current)/14. RSI=100-100/(1+avgGain/avgLoss) when both positive; set 100 if only gain positive, 0 if only loss positive, 50 if both zero. Require RSI[t]<30 strictly. This 14/seed convention is researcher-defined, not an alleged retrieved Pine default.
4. Wilder ATR14: TR[0]=H[0]-L[0]; TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1])) for t>=1. Seed ATR[13]=mean(TR[0..13]); ATR[t]=(13*ATR[t-1]+TR[t])/14 thereafter. Require finite ATR[t]>0 and **ATR[t]>ATR[t-1]** strictly. The ATR length/seed and comparison are derivative pins.
5. Define B[t]=(C[t]>SMA50[t]) AND (RSI14[t]<30) AND (V[t]>VolumeSMA20[t]) AND (ATR14[t]>ATR14[t-1]) with all inputs valid. Entry event E[t]=B[t] AND NOT B[t-1]; this **edge** is a declared derivative, not a claim about the original Pine. Warmup bars t=0..99 are NO-TRADE, initially FLAT with zero BTC; the first eligible signal decision is t=100, comparing B[100] and B[99]. Missing/invalid required data aborts the entire segment rather than silently skipping a bar.
6. When FLAT, with no pending order and t strictly later than the last exit-fill bar, an eligible completed-bar E[t] schedules **one** BUY at the *next* full bar t+1. The pinned historical OrderExecutor MARKET simulation fills exactly Q=Decimal("0.001") BTC at the **actual observed C[t+1]**, effective no earlier than T[t+1]+86400; signal t must not read O/H/L/C/V[t+1]. If there is no t+1 bar, leave the signal unfilled, with no phantom trade. Reject insufficient cash, missing price, invalid fill or unverified trading rules; never invent a fill.
7. On confirmed full BUY fill at bar f=t+1 with actual simulated entry price P=C[f], set LONG, quantity Q, and **freeze** stop S=P*Decimal("0.995") and target G=P*Decimal("1.015"). Require 0<S<P<G. These are close-trigger thresholds, not standing stop-market/limit orders; no exit is evaluated on entry-fill bar f. Do not use intrabar high/low to claim a stop/target touch.
8. On a later completed bar u>f while LONG and with no pending order, if C[u]<=S, schedule full-quantity SELL at bar u+1 close (reason STOP_SIGNAL); else if C[u]>=G, schedule full SELL at bar u+1 close (reason TARGET_SIGNAL); else HOLD. Stop has explicit priority, although with 0<S<G both price conditions cannot hold simultaneously. Equality triggers. The next-bar fill is C[u+1] even if it gaps through the threshold; it is not filled at S or G. Source short-side signals, RSI reversal, SMA failure, time exit and all other exits are disabled.
9. After a full SELL fill, set FLAT and record the exit-fill bar. Do not enter on the same bar as an exit fill. Require a **new** E[t] on a later completed bar t>exit_fill_bar; B[t] remaining true without a new edge never re-enters. Entry edges while LONG or pending are ignored, not queued. At most one pending order and one long position; no pyramiding, Safety Orders, DCA, partial fills, scaling, cooldown timer, concurrent markets or portfolio allocation. On partial, rejected, duplicate, missing or ambiguous fills **abort** the research segment instead of fabricating state. A pending exit is never silently retried.
10. At sample end, discard unfillable pending signals; mark any open inventory at the final **observed completed** close, reporting unrealized value separately. No invented final liquidation, fee, price or realized PnL. A segment restart resets FLAT and requires the full 100-bar warmup, never carries unobserved inventory.

**Position/cash and costs:** Initial modeled cash=Decimal("10000") USDT, inventory=0 BTC, no compounding/leverage. BUY only if cash>=Q*P*(1+f), with f=Decimal("0.001") per filled side; cash -= Q*P*(1+f). SELL exactly filled Q, cash += Q*P*(1-f). Net realized round-trip PnL = Q*(sell_price-buy_price)-f*Q*(buy_price+sell_price). Maintain persistent filled-quantity, pending, entry P, S, G, last fill-bar, cash and fee ledger. One pair only; no shared-capital synchronization. The research fee is hypothetical, not an asserted Binance tier or source fee. Spot perpetual funding is **not applicable**, not an invented zero-funding series.

**Disabled:** short/borrow, margin/perpetuals, leverage, liquidation, maker/limit/next-open fills, intrabar stops, trailing, opposite-signal exits, rebalancing, multiple pairs, DCA, Safety Orders, discretionary overrides and hidden controller defaults.

## Required data

One **real**, contiguous, completed Binance BTC-USDT spot UTC daily candle feed with O/H/L/C/V and raw Binance open timestamp. The only external requirement is that historical candles are actually retrievable; if not, this derivative is unexecutable on that segment. RSI14, SMA50, VolumeSMA20 and ATR14 use no non-OHLCV, multi-timeframe, order-book, funding or future data. Every signal at bar t uses only <=t and is available at **T[t]+86400**. The bar t+1 close fill becomes economically known only at **T[t+1]+86400**, even though the native simulator labels its row with open timestamp T[t+1]. Reject timestamp misuse, gaps, unobserved prices and unverified price/amount precision; never treat a missing-price fallback as market data.

## Execution assumptions

**Pinned actual engine inspected via GitHub app 2026-10-27:** HCH725/hummingbot at immutable commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, Hummingbot package label **20260920**, repository `hummingbot/VERSION` = **dev-2.17.0**. The package/source mapping and prior 902/902 byte-identity check were reported in independently merged Alpha PR #414; this Scout inspected pinned source directly but **did not rehash an installed wheel** or execute its tests.

- **Real data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1d`; `binance_spot_candles.py` REST parser maps Binance kline row[0] to opening timestamp and row[1..5] to O/H/L/C/V. `BacktestingDataProvider` can initialize `binance_BTC-USDT_1d` candles. Validate completeness and actual prices **before** `BacktestingEngineBase.prepare_market_data()` merges features with backward `merge_asof` and `dropna`; otherwise missing bars/features can disappear silently.
- **Controller/action path:** `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="1d",trade_cost=0.001)` initializes connector trading rules and the candle feed; `simulate_execution` visits rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, and dispatches `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`. A **future minimal candidate-specific controller** must calculate the stated indicators/state and use strictly prior completed signal features for any delayed action; **no such controller exists yet** and a generic controller is not misrepresented as implementing it.
- **Exact execution primitive:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. In pinned `order_executor_simulator.py`, MARKET fills on the **first supplied candle** at its actual `close`, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*notional`, and returns `CloseType.POSITION_HOLD`. It is an idealized full-fill close-price research model, **not** a real post-close executable market price, next-open order, slippage model or stop order.
- **Causality guard:** `update_state(row)` already exposes the current row close, and the simulator stamps the fill with that row's **open timestamp**. For a signal at completed t, the future controller may emit only the stored t decision at row t+1 and must never use t+1 values for that decision. Record modeled fill effective time as the **t+1 close availability**, not the raw open timestamp. The simulator's row timestamp is a historical index, not evidence that C[t+1] was available at its opening. Do not let a newly filled order trigger another same-bar action.
- **Position/cost compatibility:** `BacktestPositionHold._process_order` in `backtesting_engine_base.py` nets opposite BUY/SELL base quantities and computes **gross** matched realized PnL; `add_executor` accumulates fees separately. Reconcile cash, net realized PnL and final marked inventory explicitly from full-fill ledger; do not call gross realized PnL fee-net. Preserve complete fills/position state (e.g. `terminated_executors_window=None`) rather than relying on a one-hour controller view across daily bars. The engine performs final-tick ledger flush.
- **Fail-closed constraints:** `BacktestingDataProvider.get_price_by_type` has a `Decimal("1")` missing-price fallback: it is explicitly **forbidden** for this derivative. Validate real C before every action; abort if unavailable. Binance spot trading-rule initialization and amount quantization exist, but real minimum notional, precision, spread, liquidity, partial fills, exchange fees and live order acceptance are **not proven** by the backtester. A future materialization must check these instead of assuming market execution. Funding/margin accounting is outside this unleveraged spot-only version.

**Gate 5 boundary:** Verified reusable primitives are one real Binance spot 1d OHLCV feed, deterministic one-order-per-event MARKET historical close fills, explicit modeled fee accumulation and POSITION_HOLD netting. No claim that the unimplemented candidate controller or actual live trading path is verified. This bounded strategy uses no additional unverified engine primitive. A new execution capability needs one representative Hummingbot/Qlib event-level validation before mass Qlib screening, not a new strategy-admission gate.

## Evidence

### Source-reported

The 2025-01-28 first-party TradingView page reports SMA50-positive long regime, RSI below 30, above-average volume, rising ATR and 0.5% stop/1.5% target; its short setup is separate. No source Pine bytes or author backtest statistics are represented as independently reproduced.

### Independently reproduced

**Not independently reproduced.** No Pine replay, candidate-specific Hummingbot/Qlib backtest, event-level parity, installed-package rehash, real fills, profitability, OOS, Survivor status or HB Certified result. Pinned Hummingbot source compatibility was inspected; historical PR #414's separate engine test evidence is cited only as prior primitive evidence.

### Negative evidence

Unretrieved Pine revision and defaults, unknown source RSI/ATR/volume lengths, source order flags and original fee/position behavior; therefore no source-native equivalence claim. The derived entry-edge filter, next-bar-close timing, spot long-only restriction, fixed amount, nominal fee and close-trigger stop/target are explicit changes. A 0.5% stop **signal** can realize losses greater than 0.5% due to next-close execution. Real Binance fills/precision/costs and futures funding are unverified.

### Six-gate HB_READY proposal (independent Auditor must decide)

1. **Determinism:** exact SMA50, VolumeSMA20, Wilder RSI14 and ATR14 seeds/ties, strict confluence rising edge, no fitting, fixed warmup.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; original short explicitly disabled.
3. **Entries/exits/risk:** four-way edge entry; fixed P*0.995/P*1.015 completed-close exit signals with stop priority; no hidden SL/TP orders.
4. **Position/state:** fixed 0.001 BTC, fee/cash accounting, one pending full-fill order, no DCA, concurrency or same-bar re-entry, new edge required after exit.
5. **Pinned engine:** directly inspected Binance spot 1d feed, controller/action dispatch, MARKET close-fill, POSITION_HOLD netting, fee accumulation, missing-price guard and effective timestamp limitation at immutable 20260920/dev-2.17.0 source.
6. **Point-in-time:** contiguous completed daily bars, 100-bar warmup, t signal -> t+1 modeled close fill, no future inputs or early open-timestamp claims.

`hb_ready_status: PASS` is a **Scout submission**, not self-approval; independent Hermes Auditor controls exact-head admission.

## Falsification plan

If separately authorized for implementation, compare source-description predicates against the derivative's explicit SMA50/RSI14/VolumeSMA20/ATR14 seeds and edge, strict equality, initial warmup, no-trade confluence persistence, rejected/partial fill abort, cash/fee netting, 0.5%/1.5% close-threshold gaps, next-bar close-effective timestamp, no same-bar re-entry and final open inventory. Before broad Qlib screening on an unverified execution path, demonstrate representative Hummingbot/Qlib event-level parity including prices, sizes, fills and costs. A negative fee-net expectation or unexplained event mismatch falsifies downstream hypotheses. **No test or backtest run here.**

## Crypto portability

BTC-USDT spot 1d is a declared **research choice**, not a source-tested crypto claim or admission whitelist. Other coins, shorter bars, isolated 3x/5x futures, BO6/SO6/SO6 or different fills are optional separately specified research derivatives and require appropriate engine/economic verification. No automatic DCA overlay is asserted event-neutral.

## Limitations

Source description is not complete Pine; original strategy and this independent derivative can trade differently. Nominal bracket thresholds are not protective exchange orders. Historical next-bar-close full fills ignore actual spread, slippage, partial fills, latency and fee tiers. No Qlib materialization, realized funding, backtest profitability, OOS, survivor certification or live approval is implied.

## Implementation status

**not-implemented.** The record is an inspectable, immutable research specification; there is no dedicated Hummingbot controller, Qlib recipe, deployed bot or strategy replay. Downstream selection may require minimal strategy-specific materialization, without a second eligibility registry.

## Adoption boundary

**status: research-only; adoption: not-approved; approval_scope: research-only.** Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README count synchronization. Scout does not approve/merge/close, touch main/README, run a backtest or trade.

## Related Wiki records

None created or modified. No private Wiki material or private user data is included.

## Sources

- jbdorji, *SMA + RSI + Volume + ATR Strategy*, TradingView first-party public page, published 2025-01-28, script ID pBKov6w7, inspected 2026-10-27: https://www.tradingview.com/script/pBKov6w7-SMA-RSI-Volume-ATR-Strategy/
- Immutable pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent pinned engine evidence (not this candidate's backtest): https://github.com/HCH725/alpha-strategy-research/pull/414
- Canonical review contract: https://github.com/HCH725/alpha-strategy-research/blob/b73b37441f0d4a75d2377eaaab0c5917143a965d/.github/HB_READY_REVIEW.md
