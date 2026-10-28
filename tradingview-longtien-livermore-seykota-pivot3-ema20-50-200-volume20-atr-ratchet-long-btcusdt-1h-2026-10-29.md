---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "longtien Livermore-Seykota pivot breakout + EMA20/50/200 and volume20 + delayed ATR trail — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-05-19
sources:
  - https://www.tradingview.com/script/RwdDiWV5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Confirmed pivot breakout, triple-EMA regime, volume gate and delayed ATR trailing exit — independent derivative

## Provenance and immutable identity

- **First-party source:** TradingView public **Livermore-Seykota Breakout Strategy**, by **longtien**, published **2025-05-19**, public script identifier **RwdDiWV5**, labeled **open-source** at https://www.tradingview.com/script/RwdDiWV5/ (read 2026-10-29). Its first-party description explicitly specifies long entry on a close above a recent pivot high, close above EMA50, EMA20 > EMA200, and volume > SMA20(volume); a mirrored short entry below a pivot low with inverse EMA filters; stop at ATR × 3 from entry and trailing-stop offset ATR × 2. It provides no independently verified performance.
- **Unretrieved source details:** the web-readable publication does **not** expose the full Pine source bytes, Pine version, pivot lookback/tie handling, ATR length/smoothing, trailing activation and update semantics, exact order timing, sizing, fees, commission, position state or original fill rules. Do **not** attribute any of those to longtien, and do not claim source-native/lossless reconstruction or original event parity.
- **Explicitly independent researcher-derived strategy:** retain the *idea* of a confirmed pivot-high breakout gated by EMA20/EMA50/EMA200 and SMA20 volume, with an ATR×3 initial risk reference and ATR×2 trailing distance. **Researcher-defined changes**: pivot left/right 3 with strict ties and one-bar activation delay, BTC-USDT Binance **spot 1h** Long/Flat (original short side disabled), EMA/ATR seeds, strict crossing edge and pivot-consumption ledger, fixed 250-bar warmup, delayed-next-completed-close historical MARKET fills, **close-only** initial stop and **close-only** trailing stop activated only after +2 ATR favorable close, frozen ATR at entry signal, one fixed 0.001 BTC position, 10,000 USDT initial cash, hypothetical 0.1% each-side fee, no forced end exit. **These changes can materially alter trade events** versus the source; especially close-only delayed stops are NOT source intrabar stop orders.
- **Immutable identity:** TV:RwdDiWV5|longtien|2025-05-19|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC1h|strict-pivot-3L3R-confirmed-next-active-consumed|EMA20-EMA50-EMA200-close|volume-gt-current-SMA20|ATR14-Wilder-initial3-trail2-activation2|next-completed-close-MARKET|Q0.001BTC-cash10000USDT-fee0.001|long-flat-noDCA|warmup250. Any alteration is a new identity.
- **Dedup snapshot:** pre-write main `9fa4fe54417bd2e91e2db0872e425143db76df3f`: complete Git tree contains **423** root strategy Markdown records; README count **423**. Twelve evenly spaced records' frontmatter were checked and were PASS; this is **not** a full 423-record status audit. Connected GitHub code search for source ID `RwdDiWV5` and `Livermore-Seykota`, and all 10 open `research/*` PR metadata, revealed no same-source entry. Nearest pool relatives differ materially: `forven-atr-volume-breakout` uses a prior-20 high **plus ATR buffer**, volume >=1.2×SMA20 and EMA12 exit, without confirmed 3/3 pivots or triple EMA regime; `thetraderlodge-pivot3-vwap-rsi3-volume-momentum` uses pivot3 with **VWAP/RSI3/momentum** filters and a fixed ATR bracket, without EMA20>EMA200/EMA50, or delayed activated ATR ratchet. Not a trivial parameter variant; exhaustive semantic equivalence is not asserted.

## Signal: deterministic derivative (Gates 1, 2 and 6)

1. **Data and clock:** one Binance `BTC-USDT` spot `1h` UTC-aligned OHLCV feed. For bar t, raw kline timestamp `T[t]` is **opening time**, divisible by 3600; data become usable only at the completed close `E[t]=T[t]+3600`. Require exactly contiguous 3600-second increments, actual finite positive O/H/L/C, finite base-BTC volume V>=0, L<=min(O,C)<=max(O,C)<=H, no duplicate, missing, incomplete or future bars. Invalid/missing data **abort** the run (even while holding or pending); never forward-fill, synthesize a candle, assume a fill or substitute a price.
2. **EMA seeds and variants:** for N=20,50,200 independently, EMA_N[0]=C[0], alpha_N=2/(N+1), EMA_N[t]=alpha_N*C[t]+(1-alpha_N)*EMA_N[t-1]. No adjusted/batch/future-data EMA. At completed close t, trend gate is `C[t]>EMA50[t]` AND `EMA20[t]>EMA200[t]` (strict).
3. **Volume gate:** `VolSMA20[t]=sum(V[t-i],i=0..19)/20`, inclusive of the just-completed t; require VolSMA20[t]>0 AND `V[t]>VolSMA20[t]` (strict). Equality fails. No volume unit substitution.
4. **Wilder ATR14:** `TR[0]=H[0]-L[0]`; `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))` for t>=1. `ATR[13]=mean(TR[0..13])`, `ATR[t]=(13*ATR[t-1]+TR[t])/14` thereafter. Require ATR[t]>0 finite at entry signal. No intrabar future or rolling lookahead.
5. **Strict 3/3 pivot:** a high at center j>=3 is a pivot iff `H[j]>H[j-k]` AND `H[j]>H[j+k]` for **every** k=1,2,3. Equal highs invalidate it. It is only **confirmed** after bar j+3 closes and becomes **active starting bar j+4**; never trade the visually plotted center j. Keep latest activated high `PH[t]` and its unique center index. A new activated high replaces the previous and clears that side's consumed flag; before any active pivot no entry.
6. **Cross edge:** `UP[t]=(C[t-1]<=PH[t] AND C[t]>PH[t])` using the *same currently active* PH for both comparisons, and only if that pivot is unconsumed. Strict current >, prior <=; no entry from an already-above state. A new pivot's activation can permit a new edge, but no order without a fresh UP.
7. **Warmup:** first eligible decision requires **250 preceding** consecutive completed, validated 1h bars, with EMA200, ATR14, volume SMA20, active confirmed pivots and previous close actually present. Seed EMA/ATR only at the start of that contiguous buffer; do not use full-sample prehistory, adjust to future data, silently shorten warmup or count an incomplete candle.

## Entries, exits, risk and state (Gates 2–4)

- **Book:** one Binance BTC-USDT spot long or flat; no short, futures, margin, leverage, hedge or cross-asset shared capital. Initial modeled quote cash Decimal("10000") USDT, BTC=0. Exactly Q=Decimal("0.001") BTC per buy and full Q per sell. Max one pending action and one position. No compounding, pyramiding, DCA, safety orders, limit/maker orders, discretionary action or intrabar fills.
- **Entry decision at E[t]:** only while FLAT, warm, no pending action, and unconsumed UP[t] AND both EMA trend conditions AND volume gate AND ATR[t]>0. Latch pending BUY for the **next actually completed bar t+1**. Do not check t+1's indicators to retrospectively approve the t decision; do not create an entry at T[t] or at the next bar's open.
- **Entry fill at E[t+1]:** one simulated MARKET BUY using **actual C[t+1]** as price P, after confirmed full fill. Require cash >= Q*P*(1+f), f=Decimal("0.001"), actual finite positive P, and actual recorded executor fill/fee; otherwise **abort**, not fake success. Set entryBar=t+1, entryPrice=P, frozen A=ATR[t] (signal-bar ATR), initialStop=P-3*A; if initialStop<=0, abort rather than assume an invalid reference. Set maxClose=P, trailInactive, mark the signal pivot consumed. No exit/entry evaluation on the fill bar.
- **Trailing state while LONG:** for each *later* completed bar u>entryBar with no pending action, update `maxClose=max(previousMaxClose,C[u])`. The **researcher-defined activation threshold** is maxClose>=P+2*A. Before activation the only close-stop reference is `P-3*A`. Once activated, `trail[u]=max(trail[u-1] if active else -infinity, maxClose-2*A)`; activeStop=max(P-3*A,trail[u]). Both the activation threshold and trailing **close-only** ratchet are researcher choices; the source does not state them. Do not use intrabar H/L to activate, ratchet or fill.
- **Exit decision at E[u]:** if `C[u]<=activeStop`, latch one pending full-Q SELL for **next actually completed close C[u+1]**. No immediate execution at the threshold, at u's close or at u+1 open; any gap may cause realized loss much larger than the 3×ATR initial reference. Pending SELL suppresses all other decisions. No opposite-pivot signal exit, fixed profit target, separate time exit, break-even order, liquidation, or forced terminal close.
- **Exit fill and re-entry:** on E[u+1], confirm MARKET SELL full fill at actual C[u+1], book actual modeled fee and return FLAT. The SELL fill bar cannot also enter. The old entry pivot stays consumed; only a newly activated, unconsumed pivot and a later fresh crossing can re-enter. No additional cooldown. Entry while LONG and exit while FLAT are no-ops. Never claim a pending order filled if the dataset ends before the next completed bar.
- **Terminal:** pending unfilled intents are reported unfilled, not filled; if LONG, report real last-close mark-to-market and open exposure separately, without a fabricated SELL. Missing/partial/failed executor fills, fee inconsistencies, missing close or inconsistent inventory cause fail-closed abort, never a silent fill assumption.

## Required data

One validated 1h Binance spot BTC-USDT OHLCV stream with actual exchange candle opens and base volumes, including at least 250 **pre-decision** complete bars. No multi-market, extra timeframe, order book, tick feed, mark price, funding rate, session calendar, ML inference, future pivot or future high is required. Fetch enough raw historical buffer and verify coverage **before** the pinned provider trims to the run window; configured max_records is not evidence of delivered history.

## Execution assumptions — pinned Hummingbot Gate 5

- **Exact immutable engine:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, Hummingbot package label `20260920`, `hummingbot/VERSION` = `dev-2.17.0`. Connected GitHub source reads on **2026-10-29** directly verified VERSION and paths below. Independently reviewed Alpha PR **#414** previously reported 902/902 shipped wheel Python files byte-identical to this commit and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`; this Scout did **not** download or rehash that wheel or verify a running image. If that inherited wheel binding is invalid, Gate 5 must be blocked by the Auditor.
- **Feed:** pinned `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1h` and REST `/api/v3/klines`; `binance_spot_candles.py::_parse_rest_candles` maps row[0] to open timestamp and row[1..5] to O/H/L/C/base volume. `BacktestingDataProvider.get_candles_feed` requests start minus max_records*interval; `get_candles_df` returns a truncated run-window slice. A strategy-specific controller must validate raw pre-run history, consecutive completed closes and no missing prices before features are generated. `get_price_by_type` can return Decimal("1") on missing price: this path is explicitly **forbidden** for fills, fees or valuation.
- **Engine/controller:** `BacktestingEngineBase.prepare_market_data` backward `merge_asof(timestamp_bt,timestamp)` and rewrites `timestamp` to the raw candle-open index. `simulate_execution` runs controller `update_state` → `determine_executor_actions` → `simulate_executor`. A future minimal **strategy-specific** controller (not built here) must map each feature to the correct raw open T[t], retain logical availability E[t], latch signals at E[t] and dispatch pending action only on the t+1 simulator row. Simulator row labels are raw opens, **not** a claim that the close was known at the open.
- **Order and actual fill path:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. The inspected `OrderExecutorSimulator.simulate` MARKET branch chooses the **first supplied row** and `entry_price=df_filtered.loc[fill_timestamp,"close"]`; it sets `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote` and `CloseType.POSITION_HOLD`. Thus a pending action must be emitted on the t+1 row (not t), and confirmed executor results drive the strategy-owned fill/cash/position ledger. An executor class name or an accepted config **alone** is not claimed to prove fill compatibility.
- **Costs, funding and ledger:** `run_backtesting(trade_cost=0.001)` is an explicit **hypothetical** 0.1% each filled side, not observed Binance fees. BUY debits Q*P*(1+f); SELL credits Q*P*(1-f); realized net round-trip USDT PnL is Q*(P_sell-P_buy)-f*Q*(P_sell+P_buy). Pinned `BacktestPositionHold` nets buy/sell base exposure and separately tracks gross PnL and cum_fees_quote. Reconcile each confirmed executor fill, cash, inventory and fees; report float/Decimal rounding dust and abort beyond 1e-9 BTC inventory or 1e-8 USDT fee tolerance. Preserve complete terminated-executor visibility and handle one-tick POSITION_HOLD lag. Missing, partial, inconsistent or nonfinite fills abort. The historical MARKET-close path does not simulate observed spread, market impact, latency, tick/lot/min-notional acceptance, partial fills or actual slippage: these are **unverified real economics**, not claims of zero observed costs. Spot perpetual funding/margin/liquidation are **inapplicable**, not modeled as zero futures funding.
- **Bounded capability:** single verified 1h spot feed, OHLCV-only causal indicators and confirmed-pivot state, queued next-completed-close MARKET/POSITION_HOLD actions, and hypothetical quote fees use an **existing previously reviewed pinned-engine primitive**. No unsupported intrabar stop/maker/next-open/multi-asset path is claimed. This is static expressibility evidence, **not** an implemented controller, an actual candidate backtest, real exchange fill or strategy-specific Hummingbot↔Qlib event-level parity.

## Six-gate research assessment (subject to independent Auditor)

1. **Deterministic:** exact 3L/3R confirmed strict pivot, EMA20/50/200 seeds, volume20, Wilder ATR14, frozen A, trail activation/ratchet and explicit signal priority.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; original short leg explicitly removed as a disclosed derivative.
3. **Complete execution/risk:** pivot cross plus triple EMA/volume gate; initial close stop 3ATR, activated close trail 2ATR after +2ATR favorable close; no TP, opposite signal or hidden intrabar orders.
4. **Position/state:** one 0.001 BTC position, full fills, pending next-close buy/sell, consumed pivots, no DCA/pyramiding/concurrency/cooldown beyond stated state.
5. **Pinned compatibility:** source-inspected 1h feed, controller iteration/merge, first-row actual-close MARKET executor, POSITION_HOLD, fee and accounting; inherited wheel pin with stated limitations.
6. **Causality:** only complete contiguous 1h bars, 250 prior warmup, pivot confirmation j+3 and activation j+4, signal E[t], next completed-close fill E[t+1], no future extrema or same-row pre-close fills.

## Evidence, negative evidence and falsification

**Source-reported only:** first-party TradingView RwdDiWV5 publication by longtien, 2025-05-19, names pivot breakout, EMA50, EMA20>EMA200, volume SMA20, ATR×3 initial stop and ATR×2 trailing offset; mirrored short side. The source's actual pivot/Pine/order semantics and original backtest numbers were **not** recovered; all additions above are explicitly **independent researcher definitions**, not source-native facts.

**Independently reproduced strategy performance:** **none**. No Pine replay, candidate Qlib/Hummingbot backtest, fill, Sharpe, profitability, Survivor or live outcome was reproduced. A later separately authorized falsification should test pivot tie/confirmation timing, EMA seeds, volume equality, ATR warmup, pending buy at a regime reversal, trailing activation and gap-through, consumed-pivot re-entry, missing t+1, fee reconciliation and missing-price fallback. Representative Hummingbot↔Qlib event-level parity is required **before large-scale screening of any newly unverified execution primitive**, not as an extra HB_READY gate.

**Boundary:** `hb_ready_status: PASS` is the Scout's **proposed six-gate research assessment**, not independent approval; `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. Only independent Hermes Auditor GitHub Webhook Review may source-fact-remediate, exact-head PASS merge or NOT_LOSSLESS close. Only the existing signed GitHub webhook receiver updates README after a confirmed merge. This Scout writes one candidate record on its research branch only.

## References

- TradingView primary publication: https://www.tradingview.com/script/RwdDiWV5/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent pinned wheel/engine review: https://github.com/HCH725/alpha-strategy-research/pull/414
