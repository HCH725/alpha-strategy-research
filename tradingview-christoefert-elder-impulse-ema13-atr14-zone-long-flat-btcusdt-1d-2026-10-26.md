---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: christoefert Elder impulse green plus EMA13 1ATR entry zone - independent BTC-USDT spot 1d long-flat derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2021-09-29
sources:
  - https://www.tradingview.com/script/YEx0gnq6-Elder-Impulse-System-ATR-Bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# christoefert Elder impulse + 1ATR entry zone — independently defined long-flat spot derivative

## Provenance

**Primary source:** christoefert, *Elder Impulse System + ATR Bands*, TradingView public/open-source **script ID YEx0gnq6**, published **2021-09-29**, directly inspected 2026-10-26: https://www.tradingview.com/script/YEx0gnq6-Elder-Impulse-System-ATR-Bands/ . The readable first-party publication explains EMA13/EMA26, ATR14 bands around EMA13 at 1×/2×/3×, green/red/blue Elder impulse bars based on EMA13 slope and MACD-histogram slope, a suggested green-bar long filter above both EMAs, a suggested entry inside the 1ATR zone, and optional blue-bar or EMA13-break exits. The full Pine bytes, code hash, actual defaults for MACD, position sizing, and strategy execution semantics were **not** accessible in the inspected text. This is an **indicator with multiple suggested discretionary trading styles**, not a verified original executable strategy.

**Source-native facts, not invented defaults:** Green means EMA13 and MACD histogram both rise against the prior completed bar; red means both fall; blue is any other alignment. EMA13 and EMA26 are trend references; ATR14 defines 1×/2×/3× bands around EMA13. The author discusses green and close above both EMAs as long opportunities, avoiding overextension by considering the 1ATR zone, and exiting a trend long on blue or on a close below EMA13. The publication also describes other optional intrabar stop, 2ATR/3ATR risk, 2ATR target, short, countertrend, and multi-timeframe choices; those are **not** silently carried into this derivative.

**Independent derivative, not lossless Pine:** Researcher freezes MACD(12,26,9) with the explicit rolling EMA seed below (original page does not verify MACD defaults); chooses the conjunction of green, close above both EMAs and at most one ATR above EMA13 as an entry **state**; chooses first non-green or EMA13-close breakdown as the exit **state**; adopts BTC-USDT Binance spot 1d, LONG/FLAT only, no intrabar orders or protective stops, a next-completed-close idealized MARKET fill, 0.001 BTC size, 10,000 USDT starting cash and an explicit 0.1%-per-side research fee. All choices are researcher-defined; this does not claim to reproduce christoefert's Pine orders or Elder's full Triple Screen method.

**Immutable research identity:** `TV:YEx0gnq6|christoefert|2021-09-29|independent-derived-v1|EMA13/26-MACD12,26,9-green|C>EMA13,26|0<C-EMA13<=RMA-ATR14|non-green-or-C<EMA13-exit|rolling250-seeds|next-completed-close-MARKET|BinanceSpot-BTC-USDT-1d|0.001BTC|10000USDT|fee0.001-per-side|2026-10-26`. Changing any decision formula, warmup, state, venue, quantity, fee or fill clock creates a new derivative.

**Dedup, main `102b7a186ba219fe10d265781ff075eef4e89313`:** 354 root-level strategy Markdown records, README static count 354. Main code search for `YEx0gnq6` and `Elder Impulse ATR Bands` returned no matches; open research PR source/phrase searches returned no matches, and all 10 open PRs were inspected by title, source and head. Closest existing `elder-impulse-dual-slope-state-flip-two-sided-btcusdt-1d-2026-10-10.md` uses Elder EMA13+MACD-histogram **dual-slope alone**, two-sided persistent state with blue-bar hold and opposite-impulse flip; this derivative instead has a **distinct ATR14 1× volatility-distance admission band plus EMA26 price gate**, LONG/FLAT, and **blue-bar/EMA13 immediate exit**. That changes entry regime, holding behavior and risk exposure, not merely indicator lengths. The two READMEs and reviewer policy are aligned on PASS-only main; count agreement alone is not a re-audit of every old frontmatter.

## Economic mechanism

Source describes impulse as joint trend/momentum acceleration and the ATR band as a volatility-aware overextension gauge. This derivative tests whether restricting green-impulse entries to a close within 1ATR above EMA13 avoids buying extended moves, while exiting on the first loss of impulse confirmation. No claimed returns, hit rates or source backtest statistics are independently reproduced.

## Signal

**Input tape and clock:** a single real Binance **BTC-USDT spot 1d** historical OHLCV stream with consecutive UTC-aligned exchange candle **open** timestamps `T[t]` spaced exactly 86,400 seconds. A candle's O/H/L/C/V and every indicator using it are only available at its **effective close** `T[t]+86400`. Reject gaps, duplicates, incomplete final candles, NaN/inf, O/H/L/C <= 0, H < max(O,C), L > min(O,C), or V < 0; do not forward-fill, interpolate, fabricate or skip rows. All indicators use only completed current/past rows; no other symbol, lower timeframe, external price, mark or funding data.

**Deterministic finite-window indicators (researcher-specified, not TradingView/Pine equivalence):** For each decision bar `t`, independently calculate the indicators from the exact 250-row trailing window `t-249..t`; for `t-1`, calculate from its own trailing 250-row window. On a window indexed `j=0..249`, `EMA_n` of close for `n in {12,13,26}` is seeded at `j=n-1` with the arithmetic mean of closes `j=0..n-1`, then recursively `E_n[j]=(2/(n+1))*C[j]+(1-2/(n+1))*E_n[j-1]`. Define `M[j]=EMA12[j]-EMA26[j]` for `j>=25`; seed MACD signal EMA9 at `j=33` with arithmetic mean `M[25..33]`, recurse with alpha `2/10`, and set `HIST[j]=M[j]-SIGNAL9[j]` for `j>=33`. `HIST[t]` is the window's final histogram. For true range, `TR[0]=High[0]-Low[0]` (explicit finite-window boundary convention); for `j>=1`, `TR[j]=max(High[j]-Low[j],abs(High[j]-Close[j-1]),abs(Low[j]-Close[j-1]))`. Seed `ATR14[13]=mean(TR[0..13])`, then `ATR14[j]=(13*ATR14[j-1]+TR[j])/14`. All calculations use unrounded IEEE-754 double precision; invalid/nonfinite outputs abort the run. The 250-row rolling reseed is a **declared derivative choice**, not original Pine's infinite-history EMA.

**Impulse:** `GREEN[t] = EMA13[t] > EMA13[t-1] AND HIST[t] > HIST[t-1]`. `RED[t] = EMA13[t] < EMA13[t-1] AND HIST[t] < HIST[t-1]`. All other bars, including equality, are `BLUE`. Here `EMA13[t-1]` and `HIST[t-1]` are computed on the preceding 250-row window, never from a future row.

**Entry state (LONG only):** `ENTRY_OK[t] = GREEN[t] AND C[t] > EMA13[t] AND C[t] > EMA26[t] AND 0 < (C[t]-EMA13[t]) <= ATR14[t]`. No additional trend or signal-cross edge is required. Enter only if confirmed FLAT with no pending order; one attempt may be scheduled from each eligible decision bar when flat.

**Exit state (close-only):** `EXIT_OK[t] = (NOT GREEN[t]) OR (C[t] < EMA13[t])`. Exit all held BTC on first eligible completed decision bar while confirmed LONG. A green close below EMA13 still exits; equality with EMA13 alone does not exit unless the bar is non-green. A blue/red bar always exits. Exits have priority over entries; no reversal or same-bar exit/re-entry.

**Warmup:** at least **251** consecutive fully completed candles; the first permitted decision is zero-based bar `t=250`, so both `t` and `t-1` possess independent full trailing-250 windows. Before that, cash=10,000 USDT, position=0, state=FLAT, no orders; no synthetic prehistory, pre-warmup holding or fitted parameters.

## Required data

One complete exchange-sourced Binance BTC-USDT **spot 1d** OHLCV tape, its original UTC open timestamps, and validated real close prices for fills/valuation. Only the same tape is used for signal and simulated fill; no maker book, order-flow, higher timeframe, multi-asset synchronization, perpetual funding or non-OHLCV feed. Require explicit genuine candle coverage through each scheduled fill; abort rather than synthesize a missing next close.

## Execution assumptions

**Pinned engine/source inspected directly via connected GitHub app 2026-10-26:** Hummingbot package **20260920**, VERSION **dev-2.17.0**, immutable `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Files read at that commit: `hummingbot/VERSION`; `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (1d interval), `.../binance_spot_candles/binance_spot_candles.py` (Binance REST kline open timestamp and real OHLCV fields), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (controller actions, OrderExecutorSimulator, POSITION_HOLD, fees and holding ledger), `.../executors_simulator/order_executor_simulator.py` (MARKET fills at supplied first candle's **close**, fee `trade_cost * amount * close`, `POSITION_HOLD`), `.../backtesting_data_provider.py` (including unsafe missing-price fallback), and `hummingbot/strategy_v2/executors/order_executor/data_types.py` (MARKET OrderExecutorConfig fields). Previous independent Alpha PR **#414** reports 902/902 wheel/source byte identity and representative assertions; **this Scout did not rerun binary hashes or tests**. No dedicated controller or executable recipe for this derivative is claimed.

**Concrete supported bounded path:** a strategy-specific directional controller supplies completed-candle features to `BacktestingEngineBase.simulate_execution` and emits `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,position_action=OPEN/CLOSE,execution_strategy=MARKET,amount=Decimal("0.001"),leverage=1,price=None))`. The `OrderExecutorSimulator` idealizes a full fill at the first supplied historical row's actual close, and `BacktestPositionHold` nets buys/sells, tracks weighted cost, gross realized PnL and separately aggregated fees. This is a **historical full-fill spot close model**, not proof of real-world market execution or source-native Pine fills.

**Causality fence:** when signal `t` becomes known at `T[t]+86400`, queue the corresponding action for **next completed bar `t+1`**; use its observed `C[t+1]` as the model fill **only at effective time `T[t+1]+86400`**. Process that queued fill before any further signal; skip signal evaluation on fill bar `t+1`, resume no earlier than `t+2`. The engine labels the simulated row with its **open timestamp**, even when using the close; any controller/replay MUST shift signal by one full bar, explicitly store effective close times and never interpret the engine's open-timestamp event as a real trade at that open. A live MARKET order cannot be assumed to fill at a historical close. End-of-sample pending action without a next real completed candle is cancelled with **no fabricated fill**.

**Capital, costs, precision:** start with 10,000 USDT cash, zero BTC, no borrow, leverage=1, size exactly 0.001 BTC per entry, one open position maximum. `trade_cost=0.001` on each fully filled side is an **explicit research fee assumption** (0.1% quote notional, not a verified Binance tier); cash decreases by `Q*P*(1+0.001)` on BUY and increases by `Q*P*(1-0.001)` on SELL. Net realized round-trip cash PnL `=Q*(Psell-Pbuy)-0.001*Q*(Pbuy+Psell)`; mark open inventory with **last observed real close** only. Do not count gross `POSITION_HOLD` PnL as net without subtracting both fees. Spot funding is **not applicable**, not assumed zero futures funding; no slippage, spread, latency, impact, partial fills, borrow, futures margin or real exchange fee tier is modeled. Real min-notional, price/amount step, tick and lot rules must be read from the selected venue rules before implementation; if 0.001 BTC is invalid, hold/fail rather than silently round. This is model-consistent research only.

**Order/position state and safeguards:** `FLAT -> pending BUY -> confirmed LONG -> pending SELL -> FLAT`, one pending action maximum. Before BUY require actual available cash >= `0.001*observed_next_close*1.001`; insufficient cash rejects that attempted entry without fill, and next eligible **later** decision may try again. SELL quantity equals confirmed held BTC, never an inferred signal position. If SELL fails, remain LONG and retry on the next valid completed close until confirmed; suspend fresh signals during unresolved exits. Any partial/ambiguous fill, missing next close, invalid timestamp, cost or unreconciled `POSITION_HOLD` is a **run failure**, not a synthetic success. Explicitly set `terminated_executors_window=None` or preserve a full-run confirmed-fill ledger (default window is one hour and can hide fills across daily decisions). `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` for a missing price; prohibit that fallback and abort. Validate consecutive raw candles before `prepare_market_data`, which can drop invalid rows. No exit-and-reentry on one bar. No cooldown other than pending/confirmation restrictions; re-entry is allowed when FLAT and a new eligible completed bar occurs. No DCA, SO, pyramiding, shared capital, partial TP, leverage, SHORT, limit/maker, intrabar stops, hard SL/TP, trailing, time stop, forced sample-end liquidation or hidden risk defaults. **No protective stop exists; this is a material risk.** If the controller cannot enforce the stated timing/ledger safeguards, Gate 5 is an engineering hold rather than permission to invent fills.

## Evidence

**Primary-source evidence:** christoefert's first-party TradingView page, 2021-09-29, specifies EMA13/EMA26, ATR14 bands, green/blue/red impulse and discusses 1ATR entry zones and blue/EMA13 exits. Its recommendations are not a unique mechanical source strategy; this file freezes a **separate** one. No complete Pine code or original backtest has been independently reproduced.

**Pinned-model evidence:** immutable HCH725/hummingbot source read for Binance spot 1d candles, first-row MARKET close, controller/executor dispatch, fee ledger, POSITION_HOLD and open-time timestamp caveat. Prior PR #414 binary evidence is reused only as previously reported, not freshly reproduced. No strategy backtest, Qlib parity or live execution was run.

**Six gates — proposed PASS for independent audit:** (1) exact rolling-250 EMA/MACD/ATR algorithms, comparisons, priority, price input and seed; (2) Binance spot LONG/FLAT, SHORT disabled; (3) green+1ATR+EMA gate entry, blue/EMA breakdown exit and all optional risk paths explicitly disabled; (4) single fixed 0.001 BTC position, cash check, pending/confirmed fills, retry and re-entry state, no DCA/concurrency; (5) inspected pinned 1d spot feed, MARKET executor, POSITION_HOLD, modeled fee/cost and timestamp safeguards with unsupported economic paths excluded; (6) 251 completed-bar warmup, strictly past/current data, next-completed-close fill and explicit no-lookahead fence. Independent Hermes Auditor must verify the exact PR head; Scout cannot approve or merge.

## Falsification plan

When separately authorized for downstream work, compare indicator outputs and decision/fill effective timestamps against an independent reference for synthetic contiguous candles, including EMA/ATR seed boundaries, equal slopes, zero volume, blue transitions, next-bar gaps, fee debit/credit, failed buys and end-of-sample pending fills. Only after representative Hummingbot/Qlib event-level parity on this execution path may large-scale Qlib screening reuse it. No such work is performed in this Scout.

## Crypto portability

The concept is market-generic, but this **specific derivative** is frozen to BTC-USDT Binance spot 1d. Other assets, intervals, perpetuals, DCA and margin economics require separately declared derivatives or proven engine paths; no whitelist is an admission prerequisite.

## Limitations

Not lossless christoefert Pine; no source code bytes or original MACD settings verified. Researcher-chosen MACD12/26/9, rolling250 reseed, green/ATR/EMA conjunction, close-only exit, 0.001 BTC, fee and next-completed-close fill materially change events. Spot MARKET backtest close fills are idealized; live fee tier, slippage, precision and partial fills unverified. No stop means potentially severe loss; PASS is not a profitability, Qlib parity, survivor, Paper/Testnet/Live or trading authorization. README static count agreement does not prove all prior strategies were individually re-audited this run.

## Implementation status

`not-implemented` — strategy-specific controller/recipe has not been built. Research admission is separate from implementation and is not a second eligibility flag.

## Adoption boundary

`not-approved` / `research-only`; this PR is a proposal for independent exact-head six-gate review, not approval to trade.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/YEx0gnq6-Elder-Impulse-System-ATR-Bands/
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- https://github.com/HCH725/alpha-strategy-research/pull/414
