---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "PresentTrading BBP21 Z252 +1.618/zero-cross BTC spot 1d long-flat — independent research derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/yk59dFEX/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PresentTrading BBP21 Z252 positive-extreme cross / zero-cross exit — independent BTC spot 1d derivative

## Provenance

- **TradingView primary source:** PresentTrading, *BullBear with Volume-Percentile TP - Strategy [presentTrading]*, publicly listed open-source strategy, published **2025-01-05**, stable TradingView script identifier **yk59dFEX**: https://www.tradingview.com/script/yk59dFEX/ . First-party public description directly read 2026-10-30. Pine source bytes, an immutable Pine revision, and source order-processing configuration were **not** retrieved; no Pine-byte or original-event-equivalence claim is made. The first-party page does not state a numbered script version.
- **Source facts actually visible:** EMA baseline (default length 21), Bull/Bear Power (BBP) standardized using a 252-bar rolling mean and standard deviation, long on Z-score crossing above +1.618, short on crossing below -1.618, long exit on Z-score crossing below zero, short exit on crossing above zero. Its defining additional layer is an enabled-by-default ATR20, volume/price-percentile-adjusted **multiple-target take-profit** system; volume MA100 and percentile lookback100 are described. The prose renders some Pine formula snippets only as "Pine Script®", so exact BBP arithmetic, standard-deviation convention, EMA seed and source order processing cannot be verified from those snippets.
- **Independent derivative (only this exact derivative is proposed for HB_READY):** researcher defines conventional Elder-style BBP as `(high-EMA21(close))+(low-EMA21(close))`, explicitly chooses population-SD Z252, BTC-USDT Binance **spot** UTC 1d LONG/FLAT, source's positive-Z long crossing and zero-cross long exit, and a fully declared historical next-completed-close MARKET execution/state/cost model. **Disables the source's short side and entire ATR/volume-percentile multi-target take-profit layer**, along with any unverified Pine order defaults, and uses fixed quantity rather than unknown source sizing. Those choices can materially alter trade events and performance; the original source strategy is NOT being reproduced or asserted PASS.
- **Frozen identity:** `TV:yk59dFEX|PresentTrading|2025-01-05|independent-derived-bbp21-z252-long-v1-20261030|BBP=(H-EMA21C)+(L-EMA21C)|Z=population252|entry-cross+1.618|exit-cross0|BinanceSpot:BTC-USDT:UTC1d|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup300|no-TP-DCA`.
- **Pre-write duplicate check (2026-10-30):** current `main` at `15521acb235226495e3f86f5cea4e88a6f7ee79b` has 456 root-level strategy records, README count 456; GitHub code search for `yk59dFEX`, `presentTrading`, `bbp_mean`, `zLength` and GitHub PR search for `yk59dFEX`, `BullBear Volume Percentile`, `BBP zscore` returned no identical source/derived record or PR. The existing Forven Elder-Ray Bull-Power cross uses a different signal (Bull Power vs its EMA), while Hummingbot `macd_bb_v1`'s `BBP` is Bollinger **percent B**, not Bull+Bear Power Z252. Neither is this source or rule. Eleven open research PRs were reviewed for source identity; none cited this script.

## Economic mechanism

### Source-reported
The author frames BBP Z-score extreme crossings as trend/momentum evidence and presents an ATR/volume-percentile multi-target exit overlay. These are author explanations, **not** independently demonstrated return or risk statistics.

### Research interpretation
This derivative tests whether an unusually positive combined bull/bear pressure reading, normalized by its own trailing distribution, predicts continuation until the pressure Z-score crosses back below zero. It deliberately **does not** test the source's novel volume-percentile take-profit mechanism. No win rate, profitability, Qlib parity, or survivor status is asserted.

## Signal

All arrays are UTC daily **completed** Binance spot BTC-USDT OHLCV bars, zero-based indices `t`; all prices must be positive finite, `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]>0`, volume finite and nonnegative. Require contiguous, nonduplicate daily opens, no missing/incomplete bars, no synthetic OHLC values. Invalid tape **aborts the research segment**, not a fabricated flat trade or fabricated price.

1. **EMA21 researcher-pinned variant:** `EMA21[20] = mean(C[0..20])`; for `t>20`, `EMA21[t]=(2/22)*C[t]+(20/22)*EMA21[t-1]`. EMA undefined for `t<20`. No optimization, re-fitting, or full-sample seed.
2. **BBP researcher-pinned variant:** `bull[t]=H[t]-EMA21[t]`, `bear[t]=L[t]-EMA21[t]`, `BBP[t]=bull[t]+bear[t]=H[t]+L[t]-2*EMA21[t]`, for `t>=20`. This conventional formula is an explicit **researcher definition**; inaccessible original Pine bytes do not prove source formula identity.
3. **Rolling Z252:** for `t>=271`, `mu[t]=sum(BBP[t-251..t])/252`, `sigma[t]=sqrt(sum((BBP[i]-mu[t])^2 for i=t-251..t)/252)` (population SD, divisor 252), `Z[t]=(BBP[t]-mu[t])/sigma[t]` if `sigma[t]>0` and finite. If variance is zero, nonfinite, or any input invalid, `Z[t]` is undefined and no crossing is generated; invalid OHLCV itself aborts rather than skips.
4. **Entry:** `E[t] = isfinite(Z[t],Z[t-1]) AND Z[t] > 1.618 AND Z[t-1] <= 1.618`. This is a **strict cross above**; equality at the current bar does not trigger.
5. **Exit:** `X[t] = isfinite(Z[t],Z[t-1]) AND Z[t] < 0 AND Z[t-1] >= 0`. This is a **strict cross below**; equality at the current bar does not trigger. `E` and `X` cannot co-fire on one valid bar; standing priority is EXIT before ENTRY.
6. **Warmup:** completed bars indices `0..299` are indicator-state-only, with **no** orders or pending signal. First decision at `t=300`, using `Z[299]` and `Z[300]`. Indicator arithmetic is prefix-only, not fitted on the future tape. Do not carry a crossing from warmup into the first eligible decision.
7. **Position state:** initially FLAT; if FLAT and `E[t]`, schedule one BUY; if LONG and `X[t]`, schedule one full-position SELL. Entry while LONG, exit while FLAT and all other bars are no-ops. Exactly one position and at most one pending MARKET action; no simultaneous orders, pyramiding, averaging, DCA, safety orders, partial scale-out, hedge, reverse, short, borrowing or leverage. No cooldown except the explicit fill-bar skip below; after a completed exit, a **new future crossing** is required to re-enter.
8. **Risk:** source's ATR/percentile targets are **explicitly disabled** in this independent derivative. Protective stop, independent take-profit, trailing, time exit, date/session filter, equity-based size, forced sample-end liquidation, automatic reverse, and hidden executor stop/time defaults are all **disabled**. A position may remain open for an indefinite drawdown until `X` occurs; report this risk.

## Required data

One Binance Spot `BTC-USDT` UTC `1d` OHLCV feed. The order-gating features require `high`, `low`, `close` and completed-bar chronology only; `open` is used to validate candle integrity. No order book, OI, funding, mark price, cross-asset synchronization, multi-timeframe candle, future extreme, or private feed is needed. Price must come from the **actual** validated bar close, never the data provider's `Decimal("1")` missing-price fallback.

## Execution assumptions — pinned real engine path, bounded historical model

- **Pinned Hummingbot:** policy package `20260920`, VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. GitHub Connector directly re-read `hummingbot/VERSION`, `data_feed/candles_feed/binance_spot_candles/{constants.py,binance_spot_candles.py}`, `strategy_v2/backtesting/{backtesting_engine_base.py,backtesting_data_provider.py,executors_simulator/order_executor_simulator.py}`, and `strategy_v2/executors/order_executor/data_types.py` this cycle. Existing independently merged Alpha PR #414 documents pinned package/source and representative execution primitive evidence; **no wheel rehash or candidate-specific engine run was performed this cycle**.
- **Data and controller:** BinanceSpotCandles `INTERVALS` supports `1d`; REST parser maps exchange Kline opening timestamp plus actual O/H/L/C/V. `BacktestingEngineBase.simulate_execution` iterates prepared rows, calls `update_state(row)` then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction` through `simulate_executor`. A future dedicated controller would implement this frozen deterministic decision and pending-order ledger; `not-implemented` means it does **not** exist yet.
- **Order primitive:** `OrderExecutorConfig` with `connector_name="binance"`, `trading_pair="BTC-USDT"`, BUY/SELL, `amount=Decimal("0.001")` (SELL equals the recorded full filled inventory), `execution_strategy=MARKET`, `price=None`, `leverage=1`, appropriate OPEN/CLOSE action. Pinned `OrderExecutorSimulator.simulate` takes the **first supplied row's actual close** as MARKET fill, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`. `BacktestPositionHold` nets the opposite sides, while controller cash/inventory accounting must remain independently explicit and fee-net.
- **Causal timing:** raw daily `timestamp` is the **opening** time `T[t]`, whereas `C[t]` is only available at effective completed-close time `T[t]+86400s`. At the close of decision bar `t`, store side/quantity only; on bar `t+1` the controller dispatches the stored action and the historical MARKET simulator fills at **`C[t+1]`**, effective `T[t+1]+86400s`. No `t+1` price/indicator is consulted to choose the `t` signal. **Do not evaluate a new signal on the fill bar**; earliest next decision is `t+2`. Missing next bar means no fill. This is an idealized retrospective next-completed-close execution convention, **not** original Pine next-open execution, nor a live guarantee of retroactive close fills.
- **Exact research ledger:** initial cash `10000 USDT`, base inventory zero, fixed BUY `0.001 BTC`, single full-fill-only action, `trade_cost=0.001` **hypothetical per filled side**. BUY at actual next-close `P`: require `cash>=0.001*P*(1+0.001)`, then `cash-=0.001*P*(1+0.001)`, `base+=0.001`; if insufficient cash, consume the BUY intent without fill, leave FLAT and require a new crossing. SELL: require exactly `base=0.001`, `cash+=0.001*P*(1-0.001)`, `base=0`; invalid inventory aborts. Round-trip fee-net quote PnL `=0.001*(Pexit-Pentry)-0.001*0.001*(Pentry+Pexit)`. Use `Decimal` arithmetic on recorded close strings for the controller ledger; do not treat native gross position PnL as fee-net equity or rely on truncated terminated-executor views.
- **Scope of compatibility:** this is a **bounded idealized research full-fill** spot model, not a claim of real Binance historical order acceptance. Exchange-specific lot/tick precision, minimum order size/notional, real fee tier, order-book liquidity, latency, partial fills and spread/slippage are **not inputs or validation gates** of this frozen research model; no live-exchange acceptance, quantize helper or historical trading-rule lookup is invoked to decide these modeled events. Zero **modeled** slippage is an explicit limitation, not a measurement. Spot has no perpetual funding or margin/liquidation leg; do not invent zero funding observations on futures. No real-time paper/testnet/live deployment is approved.
- **Fail closed:** validate raw contiguous candles, finite positive real closes, complete UTC days, and enough warmup **before** engine `dropna` or simulation. Never substitute a missing price, silently shift a fill, fabricate a fee/funding observation, silently accept partial fills or convert invalid data to a PASS trade.

## Evidence

### Source-reported
First-party TradingView public description (PresentTrading, 2025-01-05, stable ID yk59dFEX) gives BBP/EMA21/Z252, +1.618/-1.618 entry crossings, zero-cross exits, and enabled default ATR20 volume/percentile take-profit layer. Its example BTCUSD 6h screenshot and prose are **not** independently reproduced performance evidence. Exact Pine formula bytes and native order settings are unavailable from the text inspection.

### Independently reproduced
None of this strategy's Pine trades, return statistics, Hummingbot candidate event sequence, Qlib parity, OOS or survivor status has been reproduced. The pinned Hummingbot **source execution/data/accounting paths** were inspected; prior accepted primitive evidence #414 is reused, without claiming this candidate's controller exists.

### Negative evidence
No `yk59dFEX` main record or open research PR found. No identical combined-Bull+Bear Power Z252 +1.618 entry / zero-cross exit rule found; Elder-Ray Bull Power alone and Bollinger `%B` are different indicators. The original Pine source's precise EMA seed, BBP formula, population/sample SD choice, fill timing, fee/precision rules, multi-target fills and full source-native state are **not** verified; all needed derivative choices above are explicitly researcher-defined. Do not auto-repair this proposal into a source-native claim.

## Six-gate assessment — Scout proposal only, independent Auditor decides

1. **Deterministic:** fixed EMA21 SMA seed, BBP arithmetic, population Z252, strict cross/tie semantics, zero-variance guard, 300-bar warmup, no fitted parameters.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; short, leverage and borrowing disabled.
3. **Entry/exit/risk:** +1.618 upward cross to enter, zero downward cross to exit, every other risk/exit mode explicitly disabled, including source's volume-percentile ATR targets.
4. **Position:** fixed 0.001 BTC, initial 10000 USDT, exact cash/inventory, one pending, fill-bar skip, no DCA/pyramid/cooldown, no phantom end fill, new-cross re-entry only.
5. **Pinned engine:** directly inspected real Binance spot daily feed, row/controller/action/MARKET close-fill/POSITION_HOLD path and modeled quote fees at fixed source commit; this is **only** the idealized research model stated, not actual exchange-valid order economics.
6. **Causality:** complete daily bars, prefix-only indicator, warmup, opening timestamps converted to close-availability times, t decision to t+1 close historical fill, no future data used for signals.

**PASS is a Scout admission proposal** for this explicitly independent research derivative, **not** an independent six-gate verdict, source-native identity, profit finding, Qlib parity, implemented strategy, HB Certified survivor, or trading authorization.

## Falsification plan

Not executed: check EMA21 first valid index20, Z252 first valid index271, decision starts300; zero variance, threshold ties, first-cross and warmup boundary, simultaneous signals impossible, pending fill-bar skip, insufficient cash, sample-end pending, fee-net cash reconciliation, gaps/duplicate/missing closes, native row timestamp vs completed close time. Compare this signal-only derivative with its no-Z normalization ablation on frozen IS; never describe it as a test of the original author's volume-percentile TP layer.

## Crypto portability

BTC-USDT spot daily is an independent research selection, not an HB_READY market/timeframe whitelist. Source BTCUSD 6h illustration is not assumed to have identical trades on BTC-USDT 1d. House BO/SO 6/6/6 and isolated 3x/5x futures are optional downstream **separately declared** experiments, not silently inherited.

## Limitations

The TradingView public text does not expose the complete Pine implementation or original order defaults. The researcher-specified BBP formula/EMA seed/SD variant and removal of source's ATR-volume-percentile multi-target exits mean the candidate may differ substantially from the original source. No protective stop; prolonged losses and indefinite holding are possible. Historical next-completed-close full fills and zero modeled slippage are idealized; actual exchange precision/order validity, fees, liquidity, and fill behavior are not verified. No strategy-specific Hummingbot/Qlib implementation, event-level parity, backtest or independent performance evidence exists. Validate any new primitive with representative parity evidence before large-scale Qlib screening; downstream HB certification requires strategy-specific event/economic reconciliation.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable artifact, strategy backtest or deployment. Research admission is not executable materialization.

## Adoption boundary

`research-only`; `not-approved`. No Paper/Testnet/Live or capital authorization. Independent Hermes Auditor GitHub Webhook Review alone determines exact-head PASS merge, source-fact remediation or NOT_LOSSLESS close; the existing signed webhook receiver alone updates README after accepted merges.

## Sources

- TradingView first-party: https://www.tradingview.com/script/yk59dFEX/ (PresentTrading, 2025-01-05; public description read 2026-10-30).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed pinned-engine primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
