---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "danieltrinidad497 Q-Trend 200-close-range ATR14 ratchet BTC-USDT spot 1h long-flat independent derivative"
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
source_as_of: 2026-10-27
sources:
  - https://www.tradingview.com/script/VapgznSq-Q-Trend-w-SL-Trailing-Stop/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Author prose mentions VIDYA, Two Pole Oscillator and delta-volume confirmation; the publicly displayed Pine v5 execution block contains none of those indicators or filters. Only the visible code is used as source-fact evidence."
  - "The visible source uses strategy.exit stop=atr*atr_mult_stop, an absolute ATR-derived price rather than entry-price-minus-ATR; its intrabar stop/trailing behavior is NOT adopted by this independent close-signal-only derivative."
---

# Q-Trend 200-bar close-range midpoint / lagged ATR ratchet — independent long-flat derivative

## Provenance

**TradingView primary source:** danieltrinidad497, *Q-Trend w/ SL+Trailing Stop*, stable public script ID **VapgznSq**, first-party page https://www.tradingview.com/script/VapgznSq-Q-Trend-w-SL-Trailing-Stop/ . Page displays **Mar 16** without a visible publication year, labels the script open-source and prints a Pine **v5** strategy code block in the publicly readable description. Inspected 2026-10-27. The page is not a cryptographically immutable source revision; no Pine hash, later-revision equality, TradingView fills or source backtest statistics are claimed.

**Directly verified code-level lineage:** source defaults are close, trend period 200, ATR period 14, ATR multiplier 1, Type A, EMA smoothing disabled; the source constructs a rolling highest/lowest-of-source midpoint, uses the **previous** ATR and a persistent midpoint/epsilon ratchet, sets B/S side memory on up/down threshold events, and submits long/short strategy entries. The published source also has date gating (2024-01-01 through 2026-12-31), 100%-equity sizing, short entries and an ATR-based stop/trailing exit. The author description mentions VIDYA, a Two Pole Oscillator and delta-volume, but the displayed executable code does not compute or use those filters. The source declares stop=ATR*2 as an absolute price argument; that is not an entry-relative protective stop. Do not conflate prose, source order behavior or backtest results with this derivative.

**Researcher-defined independent derivative v1, NOT source-native:** preserve the distinctive 200-close-range midpoint seed, lagged ATR14 epsilon, recursive ratchet and B/S memory concept, but explicitly define a simpler one-time midpoint initialization and subsequent recurrence, BTC-USDT spot UTC 1h LONG/FLAT, B-flip entry, S-state full exit, no source short/date window/100%-equity sizing/intrabar stop/trailing, fixed 0.001 BTC, initial 10,000 USDT, hypothetical 0.1% fee per filled side, and completed-bar signal to next completed-bar-close historical MARKET fill. These choices **materially change** original trade events and economics. The source's 200-bar rolling midpoint is used **only for initial seed** in this derivative; no claim is made that the subsequent recursive sequence is bar-for-bar Pine-identical.

**Frozen independent identity:** TV:VapgznSq|danieltrinidad497|public-Pine-v5-Mar16-year-unshown|derived-v1-20261027|BinanceSpot-BTC-USDT-UTC1h|close-range200-midpoint-seed-at199|WilderATR14-prevbar-epsilon1|ratchet-updown-strict|B-flip-BUY-S-state-SELL|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup220. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

A 200-close-range midpoint supplies an initial anchor. Thereafter the reference ratchets by one prior-bar ATR only when the completed close clears an upper or lower ATR offset. A bullish regime transition opens a spot position; bearish state closes it. This tests trend-state persistence with volatility-sized movement thresholds, not the source's ATR protective-stop system. No profitability or survivor assertion is made; an unprotected position can suffer substantial losses.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTC-USDT spot UTC **1h** candles indexed t=0,1,... . Native opening time T[t] must be UTC hour-aligned and T[t+1]-T[t]=3600 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C), and finite nonnegative base volume V. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed close or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+3600, not T[t]. Use float64 chronological indicator arithmetic with no intermediate rounding.
2. **Wilder ATR14:** TR[0]=H[0]-L[0]. For t>=1, TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1])). ATR[13]=mean(TR[0..13]); ATR[t]=(13*ATR[t-1]+TR[t])/14 for t>13. If any ATR used below is nonfinite or <=0, abort the research segment. The epsilon at decision t is **ATR[t-1]**, not current-bar ATR.
3. **Initial 200-close midpoint:** after exactly 200 complete candles, at t=199 define M[199]=(max(C[0..199])+min(C[0..199]))/2. Prior M is undefined. Initial side state R[199]=N (neutral); there is no pre-seed trading. This researcher-defined deterministic initialization deliberately avoids the original Pine's earlier dynamic midpoint/na bootstrap.
4. **Recursive ratchet for t>=200:** let B=M[t-1] and e=ATR[t-1]. Define UP[t]=(C[t]>B+e), DOWN[t]=(C[t]<B-e); equality triggers neither. With e>0 they cannot both hold. Set M[t]=B+e on UP, M[t]=B-e on DOWN, otherwise M[t]=B. Set R[t]=BULL on UP, BEAR on DOWN, otherwise R[t]=R[t-1]. All M/R states are updated on **every** completed bar, even during warmup, pending orders or a position. This fully specified recurrence is researcher-authored, inspired by the source's midpoint/epsilon ratchet, not asserted to be a lossless implementation of its nested reassignment.
5. **Warmup:** bars t=0..219 are **220 completed-bar no-trade warmup**; seed and update M/R normally from t=199 onward. First eligible decision is t=220. If R already equals BULL at the end of warmup, do **not** invent an entry; require a fresh BULL transition at t>=220.
6. **Entry:** when FLAT with no pending action, t>=220, t strictly later than the last SELL-fill bar, and R[t]=BULL with R[t-1]!=BULL, queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
7. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with R[u]=BEAR, queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. This is a **bearish state** exit, not necessarily a fresh flip: a BEAR transition during a pending BUY still forces exit on the next eligible bar. No stop, target, trailing, time exit or protective intrabar order is present. Do not substitute the signal threshold for the actual SELL fill price.
8. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. On a pending/fill bar ignore new order signals but continue updating M/R. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires a **later fresh BULL flip**; a persistent BULL regime does not re-enter. Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
9. **Disabled:** source short/borrow, futures/perpetuals, margin/leverage/funding, source date-window gate and date-close, source 100%-equity sizing, EMA smoothing, Type B cross variant, unused source strong-buy/strong-sell/VIDYA/TwoPole/delta-volume prose, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker/next-open fills, intrabar stops/TP/trailing, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTC-USDT spot 1h OHLCV feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All indicator inputs at decision t are from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected via connected GitHub app on 2026-10-27:** HCH725/hummingbot commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, package label **20260920**, VERSION **dev-2.17.0**. Inspected immutable VERSION, BinanceSpotCandles constants/parser, BacktestingEngineBase, BacktestingDataProvider, OrderExecutorSimulator and OrderExecutorConfig. Existing Alpha PR #414 documents prior independent package/source correspondence; the installed wheel/image digest was not rehashed in this run.

- **Data:** pinned BinanceSpotCandles declares 1h and reads Binance REST kline opening timestamp plus actual OHLCV. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** BacktestingEngineBase.simulate_execution iterates completed rows, calls update_state(row), then controller.determine_executor_actions(), simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain R/M, FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path uses the **first supplied row's actual close**, not next-open or a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1].
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PR #519 records a bounded synthetic primitive exercise at Q0.001, prices 30100/32000, fee 0.001 and 1e-12 diagnostic tolerance; PR #529 independently reused the bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's BacktestingDataProvider.get_price_by_type fallback Decimal("1") on missing prices is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### First-party source facts

Publicly readable TradingView Pine v5 text directly establishes author/script identity, default p=200/ATR14/mult=1, close input, Type A, disabled EMA smoothing, midpoint/lagged ATR threshold and B/S memory, original short/date/percent-equity and stop/trailing instructions. It does **not** establish source-native equality for the independently simplified recurrence, LONG/FLAT risk behavior, fill timing, economics or source strategy results.

### Independently reproduced

No strategy backtest, Pine event parity, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the immutable pinned Hummingbot feed/controller/action/MARKET/POSITION_HOLD/fee source paths and reused prior independent primitive evidence (#519/#529), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** exact 200-close midpoint seed, lagged Wilder ATR14, strict threshold, ratchet, side memory, float64, warmup and priority.
2. **Direction:** BTC-USDT spot LONG/FLAT; source shorts expressly disabled.
3. **Entry/exit/risk:** new BULL flip BUY; BEAR state SELL; all source stop/trailing/date/TP and hidden defaults expressly disabled.
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, fail-closed fill reconciliation, fresh flip after exit, no DCA or concurrency.
5. **Pinned compatibility:** actual 1h Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar or futures funding claim.
6. **Causality:** t>=220 completed-bar decision, t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

**Dedup:** current main at 52adc0fccb12a2962ee2775b5b61c698c7a4abd5 has 387 root strategy Markdown records and README count 387; direct GitHub code searches for VapgznSq, danieltrinidad497 and Q-Trend returned no same-source strategy. All ten open research/* PR titles/bodies and PR search for the source ID/author were checked; none matched. Similar ATR-ratchet families (e.g. FMZ Abraham Trend Trader) use distinct WMA-true-range/inset high-low rails and state rules, not this 200-close-range midpoint and lagged-ATR recurrence. Existing root records were not re-audited individually in this Scout; #529's independent 386/386 PASS census plus current compare from its base shows only that reviewed PASS strategy addition and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test threshold equality, initialization at 199/200, warmup-edge suppression, pending-bar regime changes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Limitations

Source code is publicly printed but has no immutable TradingView revision hash or visible year in its date label; the researcher-derived recurrence is intentionally not Pine-identical. The original source's absolute-price ATR stop/trailing and short/date behavior are excluded. Pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. No performance, survivor, live or Qlib parity claims.

## Implementation and adoption

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Sources

- https://www.tradingview.com/script/VapgznSq-Q-Trend-w-SL-Trailing-Stop/ — danieltrinidad497, first-party open-source Pine v5 text, page shows Mar 16 without year, inspected 2026-10-27.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected through connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
