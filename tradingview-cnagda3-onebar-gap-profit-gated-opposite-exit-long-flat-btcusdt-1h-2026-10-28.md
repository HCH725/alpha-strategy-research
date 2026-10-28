---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: cnagda3 one-bar true-gap long with profitable opposite-gap close exit, independent BTC-USDT spot 1h derivative
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-08-23
sources:
  - https://www.tradingview.com/script/NTbbqM57-Imbalance-No-SL/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# One-bar true-gap / profitable opposite-gap exit — independent research derivative

## Provenance and immutable identity

**First-party public source:** cnagda3, *Imbalance No SL*, TradingView public open-source strategy, published **2025-08-23**, script identity **NTbbqM57**, primary URL https://www.tradingview.com/script/NTbbqM57-Imbalance-No-SL/ (page description inspected 2026-10-28). The publicly readable first-party description defines bullish imbalance as current LOW > prior HIGH and bearish imbalance as current HIGH < prior LOW; repeated same-side BUY/SELL can average the position, and an existing long is closed on bearish imbalance **only if price is above average entry**. No fixed stop loss. The original also allows short positions and averaging. Its Pine source bytes, exact Pine version, qty default, original order-processing configuration, and full original strategy state were **not accessible in the retrieved page text**. Do not infer them or claim source-native trade equivalence. The public page is the primary source, not a backtest verification.

**Independently derived, not source-native and not a lossless port:** retain the *one-bar, strict, non-overlapping high/low gap construction* and *profitable opposite-gap exit* as source-backed mechanism. Researcher explicitly chooses (a) Binance BTC-USDT **spot 1h** rather than any original market, (b) LONG/FLAT only, disabling the source's short leg, (c) **one fixed 0.001 BTC unit**, disabling the source's same-direction averaging and all DCA, (d) **fully completed candle-close decision and idealized same-row close MARKET fill**, not an assertion about original Pine fills, (e) gross entry-close profit threshold, (f) 24-bar warmup, cash ledger, cost model and failure fences. These changes materially alter signals, exposure, and economics; all source-default claims outside the first-party description remain unknown. No original author endorsement, source Pine hash, independently reproduced statistics, Qlib parity, Survivor or live suitability is asserted.

**Frozen strategy identity:** TV:NTbbqM57:cnagda3:2025-08-23:public-description | independent-derived-v1:2026-10-28 | Binance BTC-USDT spot UTC 1h | bullish true gap L[t]>H[t-1] entry | bearish true gap H[t]<L[t-1] AND C[t]>entryFillPrice exit | long-flat fixed 0.001 BTC | no adds | completed-close MARKET simulator | research fee 0.001 per side. Changing the gap lag, gap inequalities, profit predicate, fill convention, averaging, direction, size or risk behavior defines another version.

**Dedup at main b443823b44c4c1962f6a1887446c462879e9a159:** 411 root-level strategy records; README counter 411. Connected GitHub code search for NTbbqM57 and cnagda3 returned no matching record; GitHub PR search for those identifiers returned no PR, and the eleven open PRs were checked for TradingView source identity. The closest existing *fair-value-gap-breakout-long* uses a TWO-bar lag and an extra prior-close confirmation with opposite gap exit (not profit-gated); *forven-gap-fill-gapdown* tests current OPEN versus prior CLOSE and has a different gap-recovery rule; *hashem UTC candle breakout* uses a fixed daily anchor. This strategy's strict adjacent-bar HIGH/LOW non-overlap **plus conditional profitable opposite-gap exit** is materially different, not a parameter-only clone. A matching numeric README counter is not represented as a 411-file status audit; 12 spread-sample root records had PASS frontmatter.

## Economic mechanism and research hypothesis

A strict upward gap (the new bar's LOW exceeds the previous bar's HIGH) is treated as evidence of discontinuous upward pressure. The long is held until a strict downward gap appears **and** the current completed close exceeds the actual filled entry close; an adverse opposite gap is ignored. This may produce extremely long losing holds and very few signals on continuous crypto markets. The profit condition is **gross**, so a positive exit-vs-entry price difference may still yield negative net PnL after fees. The hypothesis is testable and not a profitability assertion.

## Signal, parameters, state and risk

**Single source of market data:** real Binance BTC-USDT spot **1h** OHLCV, exchange UTC-aligned opening timestamp T[t]. Candle t is usable only after completion at E[t]=T[t]+3600 seconds. O/H/L/C must be finite, strictly positive, H>=max(O,C), L<=min(O,C), volume finite/nonnegative; timestamps must increase by exactly 3600 seconds with no gaps/duplicates. Missing, incomplete, malformed, noncontiguous or stale data **abort the research run**, not forward-fill or substitute prices. A closed candle's OHLCV is immutable in this model. No secondary market, external feed, funding, order book, news, fitted model, synthetic candles or higher timeframe is read.

**Warmup and initial conditions:** require 24 contiguous completed valid 1h candles, start FLAT with cash=Decimal(10000 USDT), BTC=0, no pending orders, no inferred earlier trade. First decision is on completed bar t>=24 (zero-based); the previous bar t-1 is then known. Warmup is a researcher pin, not a source-native requirement. The strategy never uses unclosed bars.

**Exact predicates:** BULL[t] := Low[t] > High[t-1]; BEAR[t] := High[t] < Low[t-1]. Both are strict; equality is false. They cannot both hold on a valid candle pair: BULL implies Low[t]>High[t-1]>=Low[t-1], while BEAR would imply High[t]<Low[t-1], contradicting High[t]>=Low[t]. No percentage threshold, body, volume, RSI, ATR or trend gate exists. All comparisons use completed actual price values, not chart drawings or implied intrabar gaps.

**FLAT -> LONG:** if and only if BULL[t] and no pending order, issue one MARKET BUY for Q=Decimal(0.001 BTC). Historical simulator fills at the same processed row's **actual close[t]**; interpret economic fill time as E[t], not raw opening timestamp T[t]. Require confirmed full fill and cash >= Q*C[t]*(1+f) with f=Decimal(0.001) assumed quote fee. On success cash debits Q*C[t]*(1+f), BTC becomes Q, entryFillPrice is the confirmed actual C[t], and LONG starts. If cash is insufficient, remain FLAT and log skipped signal (no fictitious fill). Missing price, rejected/partial/unknown fill or fee data abort this bounded run. An already-LONG bullish gap is a no-op, **never an additional buy**.

**LONG -> FLAT:** on a subsequent completed bar t, if and only if BEAR[t] **AND** C[t] > entryFillPrice (strict gross-price profit), issue one MARKET SELL for all confirmed Q. The pinned simulator fills at that row's actual C[t] with effective economic time E[t]. On confirmed full fill, cash credits Q*C[t]*(1-f), BTC becomes 0, position and entryFillPrice clear. A bearish gap at or below entry price **does not exit**; a non-gap bearish candle **does not exit**. A flat-state bearish gap does not open a short. No same-bar entry/exit is possible because BULL and BEAR are mutually exclusive, and exit requires an already confirmed earlier BUY. If a SELL is partial/rejected/unknown, abort; do not silently mark FLAT. Subsequent BULL on a later completed bar may re-enter immediately; **no cooldown** and no remembered gap anchor.

**Risk/disabled behaviors:** no fixed SL, TP, trailing stop, ATR bracket, time limit, stop-after-loss, drawdown circuit breaker, averaging, pyramiding, safety order, DCA, scale-in/out, hedge, simultaneous position, short, borrow, leverage, margin, cross-asset capital allocation, discretionary override, or hidden Hummingbot exit. Exactly one long or flat state and at most one pending action. No terminal forced liquidation: any open BTC at sample end is marked at the **actual final observed close**, with unrealized gross PnL and separately reported paid fees; no invented exit fill. Profit-gated exit is not a protective stop. Re-entry is only after confirmed flat state and a new BULL event.

**Numerical accounting:** use Decimal for Q, cash, fees and state predicates based on the actual finite historical prices, not rounded display prices. Record Q*entry and Q*exit in USDT. For each fully matched trade, gross PnL=Q*(Pexit-Pentry), quote fees=f*Q*(Pentry+Pexit), net=gross-fees. Reconcile simulator confirmed quantities and fee ledger before declaring position transitions. Diagnostic tolerances at most 1e-9 BTC quantity and 1e-8 USDT fee reconciliation are **reporting tolerances only**, never a way to change strict signal comparisons or force a fill. Cash cannot go negative; do not silently borrow spot quote capital.

## Required pinned Hummingbot path — inspected in GitHub

**Pinned engine:** package **20260920**, VERSION **dev-2.17.0**, repository source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. GitHub Connector read VERSION, BinanceSpotCandles constants/parser, BacktestingEngineBase, OrderExecutorSimulator, OrderExecutorConfig, BacktestingDataProvider on 2026-10-28. Prior PR #414 records 902/902 package-wheel/source byte correspondence; **wheel bytes or installed image were not independently rechecked this cycle**. This claim is pinned *source-model expressibility*, not a currently implemented strategy controller.

- **Feed/market:** pinned BinanceSpotCandles declares 1h interval; its REST parser reads row[0] as opening timestamp and row[1..5] as actual O/H/L/C/V. The 1-bar gap predicate needs only that single completed candle feed and its previous row. Validate continuity **before** BacktestingEngineBase.prepare_market_data can drop NaN rows; no synthetic gap across missing rows.
- **Controller/action:** pinned BacktestingEngineBase.simulate_execution iterates processed rows, invokes update_state(row), then controller.determine_executor_actions(), dispatching CreateExecutorAction to simulate_executor. A dedicated minimal controller for these frozen gap and profit predicates is **not implemented**. OrderExecutorConfig permits connector_name='binance', trading_pair='BTC-USDT', side=BUY/SELL, amount=Decimal('0.001'), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1.
- **Actual fill semantics:** pinned OrderExecutorSimulator.simulate(MARKET) selects the first supplied processed row, labels its fill with that row's opening timestamp, fills at its actual close, sets filled_amount_quote=Q*close, cum_fees_quote=trade_cost*Q*close, and terminates as POSITION_HOLD. The simulator does **not** provide a real intrabar or next-open price path. Effective causal time of a close-based decision and this idealized fill is **opening timestamp+3600s**; the raw label is not the information-availability time. Never claim a live after-close order can execute at the historical close.
- **Position/fees:** pinned BacktestPositionHold nets opposite confirmed BUY/SELL quantities, computes gross realized/unrealized quote PnL, and separately accumulates cum_fees_quote. The controller must read confirmed executor fills rather than equating submitted actions with position transitions. Set terminated_executors_window=None or maintain a complete persistent fill ledger so historical confirmed fills remain visible.
- **Cost/funding:** run_backtesting(trade_cost=0.001) pins a **hypothetical 0.1% per filled side**, not verified Binance historical tariffs. MARKET simulator models **no additional slippage**, an idealization rather than evidence of zero realized slippage; spread, latency, market impact, venue filters, historical precision and partial-fill behavior are not proven live. BTC-USDT **spot** has no perpetual funding obligation; no fictitious zero-funding observation or futures margin is reported. Fees are accounted in the quote cash ledger and deducted from gross PnL.
- **Missing-price/failure fence:** pinned BacktestingDataProvider.get_price_by_type may default missing prices to Decimal('1'); **never** use that fallback for an order, mark or signal. Require the actual valid close in the processed historical row; abort otherwise. No LIMIT/MAKER queue, bracket/intrabar path, multi-asset join, cross-market capital, or non-OHLCV dependency is required for this derivative.

## Six-gate Scout evidence — pending independent Auditor

1. **Determinism:** strict adjacent-candle H/L non-overlap, gross-price-gated bearish-gap exit, fixed Q, cash/fee assumptions, warmup, state, equality and missing-data rules; no trained model or unknown indicator.
2. **Direction:** BTC-USDT Binance spot LONG/FLAT; source short path deliberately disabled, not represented as source-native.
3. **Entry/exit/risk:** BULL completed-close entry, BEAR+profitable-close exit, all stop/TP/trailing/time/default risks explicitly disabled; gross-profit criterion is not a net-profit promise.
4. **Position/DCA/re-entry:** one Q=0.001 BTC position, confirmed-fill ledger, no averaging/DCA/pyramiding/concurrency, no cooldown, flat re-entry on a later BULL, abort unsupported partial fills.
5. **Pinned engine:** actual 1h Binance REST OHLCV parser, controller/action path, same-row MARKET close fill, POSITION_HOLD net/fees and hypothetical trade_cost demonstrated from pinned source. No inferred funding, next-open, live spread or missing-price fallback.
6. **Causality:** t-1 and completed t only; effective time T[t]+3600; continuous valid candles; no future highs/lows, repainting, unclosed HTF, full-sample normalization, fitted lookahead or intrabar fill assumptions.

## Evidence limits and falsification plan

**Source-backed:** cnagda3's strict one-bar gap predicates, same-side averaging possibility, profit-only opposite-gap exit and absence of fixed SL. **Researcher-defined:** spot long-only, disabling averaging and short, Q, warmup, fee/cash/price/timing/failure model, and all state priority. **Independently reproduced:** none; no TradingView Pine event replay, no Hummingbot/Qlib backtest, no event-level parity, no net returns, no OOS/Survivor/HB Certified or deployment. The complete Pine text was not retrieved; this is not evidence that original source-native strategy passes.

**Future falsification (not run):** gap equality, BULL/BEAR exclusivity, consecutive BULL while LONG, BEAR below/equal entry (must hold), profitable BEAR (must close), post-exit new BULL, one-bar gap after a missing candle (abort), warmup boundary, cash shortage, last-row open position, gross-positive/net-negative exit, raw opening-label versus effective completion time, and exact filled-quantity/fee ledger. Before large-scale Qlib screening, reuse verified close-MARKET primitives and validate any newly required execution path with representative Hummingbot/Qlib event-level parity. No change to the six HB_READY gates is requested.

**Primary source:** https://www.tradingview.com/script/NTbbqM57-Imbalance-No-SL/
**Pinned engine:** https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
**Prior wheel/source evidence:** https://github.com/HCH725/alpha-strategy-research/pull/414
