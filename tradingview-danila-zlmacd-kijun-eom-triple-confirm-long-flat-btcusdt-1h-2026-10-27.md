---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "danila_leontyev Zero-Lag MACD Kijun-sen EOM triple-confirm BTC-USDT spot 1h long-flat independent derivative"
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
source_as_of: 2025-06-10
sources:
  - https://www.tradingview.com/script/MseOgvtC-Zero-Lag-MACD-Kijun-sen-EOM-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Zero-Lag MACD / Kijun / EOM — independently specified three-confirmation long-flat research derivative

## Provenance

**First-party TradingView source:** danila_leontyev, *Zero Lag MACD + Kijun-sen + EOM Strategy*, published **2025-06-10**, stable public script ID **MseOgvtC**, inspected **2026-10-27**: https://www.tradingview.com/script/MseOgvtC-Zero-Lag-MACD-Kijun-sen-EOM-Strategy/ . Public page identifies the script as open-source, but complete Pine bytes, revision hash, defaults and the internal implementation of the author's **Zero Lag MACD Enhanced Version 1.2** were not retrievable from the public text. No source-native, Pine-identical or author-performance reproduction is claimed.

**Verified source-description facts:** long entry requires a zero-lag MACD bullish signal, price above Kijun-sen and Ease of Movement (EOM) positive; the author's short setup reverses those filters. The page describes next-candle-**open** entries, ATR-based stop distance **2.5 ATR**, and fixed **1:1.2 risk/reward** take-profit. It describes customizable MACD/Kijun/ATR settings but does not expose their exact defaults, Zero Lag MACD formula, EOM smoothing, intrabar order flags, fee, or original position-state behavior in the accessible page. The phrase describing the bullish MACD crossover/histogram location is not mathematically precise; no exact crossover semantics are attributed to the author.

**Explicit independent derivative, NOT lossless source reproduction:** The researcher chooses a fully defined double-EMA zero-lag MACD 12/26/9, Kijun26, SMA14-smoothed EOM, Wilder ATR14, MACD-negative bullish histogram-zero cross, Binance BTC-USDT **spot UTC 1h**, LONG/FLAT only, fixed 0.001 BTC, 10,000 USDT initial research cash, completed-close signal to next completed-close historical MARKET fill, ATR bracket as **close-triggered exit signals** (not source intrabar protective orders), and hypothetical 0.1% fee per filled side. Original next-open execution, shorts, unspecified MACD Enhanced v1.2 internals and source order semantics are **not** claimed or emulated. These choices materially change trade events and economics and are researcher-authored.

**Frozen derived identity:** `TV:MseOgvtC|danila_leontyev|2025-06-10|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC1h|ZLDEMA-MACD12-26-SignalEMA9|Kijun26|EOM-SMA14|hist-crossup-zero-MACDneg-long|ATR14-2p5SL-3p0TP-close-bracket+filter-exit|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup120`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The author combines faster momentum reversal, a Kijun trend filter and volume-normalized price movement to confirm entries, with ATR-scaled asymmetric exits. The 2.5 ATR stop and 1:1.2 reward ratio are **source descriptions**, not a verified realized return.

### Research interpretation

This independent derivative tests a new negative-zone MACD momentum turn only when price is above the rolling 26-bar range midpoint and positive EOM confirms movement. A 2.5 ATR downside / 3.0 ATR upside **closing-price trigger** is not a protective order; modeled exit fills may exceed the trigger distance. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **UTC 1h** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be UTC hour-aligned and T[t+1]-T[t]=3600 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>0 for every row. Abort on gaps, duplicates, missing prices/volume, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+3600, not at T[t].
2. **EMA definition, exact seed:** for a sequence X first valid at index a, EMA_n(X) is undefined until a+n-1; seed there with the arithmetic mean of X[a..a+n-1], then EMA[t]=alpha*X[t]+(1-alpha)*EMA[t-1], alpha=2/(n+1), with float64 calculations and no intermediate rounding. On C, calculate EMA1_12, EMA2_12=EMA12(EMA1_12), EMA1_26, EMA2_26=EMA26(EMA1_26). `ZL12=2*EMA1_12-EMA2_12` valid from t=22; `ZL26=2*EMA1_26-EMA2_26` valid from t=50. `M[t]=ZL12[t]-ZL26[t]` valid from t=50. `S=EMA9(M)` seeded at t=58 from M[50..58]; `HIST=M-S`. This is **researcher-selected double-EMA lag reduction**, not a verified reconstruction of the author's Enhanced v1.2.
3. **Kijun26:** `K[t]=(max(High[t-25..t])+min(Low[t-25..t]))/2`, valid from t=25; current completed bar included. No displaced Ichimoku plots or forward shifts.
4. **Ease of Movement:** for t>=1, midpoint `mid[t]=(High[t]+Low[t])/2`; `rawEOM[t]=(mid[t]-mid[t-1])*(High[t]-Low[t])/Volume[t]`. `EOM14[t]=mean(rawEOM[t-13..t])`, valid from t=14. Volume is actual base-asset Binance spot candle volume; the conventional arbitrary positive scale factor is fixed at 1 because only sign is tested. Zero volume invalidates the sample, never becomes a fabricated zero EOM.
5. **Wilder ATR14:** `TR[0]=High[0]-Low[0]`; for t>=1, `TR[t]=max(High-Low,abs(High-Close[t-1]),abs(Low-Close[t-1]))`. `ATR[13]=mean(TR[0..13])`; `ATR[t]=(13*ATR[t-1]+TR[t])/14` thereafter. Require finite ATR>0 at any entry.
6. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..119; first possible completed-bar decision is t=120. A bullish entry event at t is `HIST[t-1]<=0 && HIST[t]>0 && M[t]<0 && Close[t]>K[t] && EOM14[t]>0`; all inequalities strict except the previous-histogram tie. This precise below-zero crossover is a **researcher-defined interpretation** of the source's imprecise MACD wording. No entry on persistent positive histogram without a fresh cross. All inputs are from completed bars <=t.
7. **BUY scheduling:** if FLAT, no pending order, and t is strictly later than any prior exit-fill bar, store exactly one BUY instruction from the completed t signal. Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close, valid size/rules and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
8. **Frozen bracket:** upon confirmed full BUY at t+1, set LONG with entry P=Close[t+1], `A=ATR[t]` **frozen from signal t**, `stop=P-2.5*A`, `target=P+3.0*A`. Require 0<stop<P<target, else abort. These are completed-close signal thresholds, **not** exchange stop/limit orders. No exit evaluation on the BUY fill bar.
9. **Exit and priority:** at each later completed bar u while LONG and no pending order, evaluate in this order: (i) `Close[u]<=stop` => STOP_SIGNAL; (ii) `Close[u]>=target` => TARGET_SIGNAL; (iii) `HIST[u-1]>=0 && HIST[u]<0` => MOMENTUM_EXIT; (iv) `Close[u]<K[u]` => KIJUN_EXIT; (v) `EOM14[u]<0` => EOM_EXIT; otherwise HOLD. Equality at stop/target triggers, while equality at Kijun/EOM does not. The filter/momentum exits are **researcher-added**, not attributed to the source. Schedule a full SELL at row u+1, idealized MARKET fill at its actual observed close effective E[u+1]; the stop/target price is never substituted for the real observed close. No same-bar roundtrip.
10. **Order and re-entry state:** one position and at most one pending order. A confirmed full SELL returns to FLAT, records its fill bar and clears bracket; no new entry until a **new** qualifying histogram cross on a strictly later completed bar. Ignore, do not queue, signals while LONG/pending. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. No cooldown beyond the post-exit new-signal rule. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
11. **Explicitly disabled:** short/borrow, futures/perpetuals, margin/leverage/funding, pyramiding, DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding, maker/limit/next-open orders, intrabar protective stops, intrabar high-low trigger, trailing, time exit, source-specific unknown MACD internals, and hidden executor defaults. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1h OHLCV feed; no external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All indicators use only <=t completed data. Zero/negative volume or missing candles aborts.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Direct connector inspection of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, `binance_spot_candles.py`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, and `hummingbot/strategy_v2/executors/order_executor/data_types.py`. Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1h`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's signal/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** `OrderExecutorSimulator.simulate` MARKET path chooses the first supplied candle row, fills at that row's **actual close**, computes `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. Dispatch on t+1 yields an idealized **t+1 close** fill, not a source next-open fill or achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, invalid trading rules, unsupported precision/min-notional, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, live minimum order/precision, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

TradingView danila_leontyev (2025-06-10) describes three-way Zero Lag MACD/Kijun/EOM confluence, long and short filters, next-candle-open entries, ATR×2.5 stop and 1:1.2 risk/reward target. No original Pine backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No Pine parity, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **existing pinned source-code engine/data/executor/fee paths** were directly inspected via GitHub connector. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

Original Zero Lag MACD Enhanced v1.2 source bytes/defaults unavailable; the researcher's double-EMA MACD, histogram sign rule, Kijun/EOM/ATR periods, source next-open-to-next-close substitution, filter exits, spot-only position, fixed quantity, fees and close-triggered bracket are **explicit alterations**, not source-native rules. A nominal 2.5 ATR stop can lose more due to close-trigger/next-close fill. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: fully pinned double EMA seeds, MACD histogram, Kijun26, EOM14, Wilder ATR14, thresholds, ties and warmup.
2. Direction: Binance BTC-USDT spot LONG/FLAT; original short explicitly disabled.
3. Entry/exit/risk: exact three-confirmation cross, frozen 2.5/3.0 ATR close-bracket, ordered filter exits and disabled paths.
4. State: fixed 0.001 BTC, one pending order/position, cash and fees, no DCA/concurrency, fresh cross after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1h feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; no unsupported next-open/intrabar/funding assumption.
6. Causality: 120 completed-bar warmup, t completed signal -> t+1 completed-close economic fill, no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=982612ed51ca8345968bae8d301df9325b64fa94`, README static pool count and root Markdown strategy count were both **382** (excluding two READMEs). GitHub main code searches for `MseOgvtC` and `danila_leontyev` returned no matching strategy; all ten open `research/*` PR titles/bodies were checked for source identity. Existing zero-lag MACD zero-axis and EOM-zero-cross families do **not** combine zero-lag MACD negative-zone reversal, Kijun26 trend and EOM14 participation in this three-way gate. Existing 382 strategies were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, EMA seeds and equality cases, EOM positive-volume requirement, frozen ATR bracket, post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1h is researcher-selected, not a TradingView author-validated outcome or admission whitelist. Any futures, 3×/5×, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No original Pine bytes/revision; source-native equivalence unverified. Derived signal/exits and next-close fill materially differ from author description. Idealized close fills and assumed fees do not prove exchange execution or protective risk limits. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://www.tradingview.com/script/MseOgvtC-Zero-Lag-MACD-Kijun-sen-EOM-Strategy/ — danila_leontyev, first-party public strategy, 2025-06-10; inspected 2026-10-27.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source, inspected through connected GitHub app 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
