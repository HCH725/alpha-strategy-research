---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "eemani123 RSI of VWAP — independent UTC-session VWAP RSI14/EMA200 momentum entry and 90-cross/5pct-close exit BTC-USDT spot 1h long-flat"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-11-04
sources:
  - https://www.tradingview.com/script/OUzp2NR6-RSI-of-VWAP/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI of UTC-session VWAP with EMA200 gate — independent executable research derivative v1

## Provenance and immutable derivative identity

**Primary first-party source:** TradingView public open-source *RSI of VWAP* strategy, author **eemani123**, stable script ID **OUzp2NR6**, published **2020-11-03**, release notes **2020-11-04**, source description directly read **2026-10-29**: https://www.tradingview.com/script/OUzp2NR6-RSI-of-VWAP/ . The author explicitly says RSI is applied to VWAP; entry occurs on RSI(VWAP) crossing **above 70** while price is above **EMA200**; the original text describes partial profit-taking at RSI(VWAP) **90**, an earlier full-exit level **30**, a **5%** stop, and 10% equity-at-risk sizing. The 2020-11-04 notes say the sell level was changed/defaulted from **30 to 90**, while also mentioning partial exits. This is a **source-description ambiguity**, not silently reconciled here. The author describes RSI length **14**. No full original Pine bytes, revision hash, VWAP session calendar, Pine order-processing flags, partial-exit fraction, or original fills were accessible in the public text interface; **no source-native event equivalence is claimed**.

**Explicitly independent researcher-designed derivative:** take the author's distinctive RSI-of-VWAP >70 crossover with EMA200 price filter as a hypothesis, but independently define the **UTC-midnight-anchored, close-weighted session VWAP**, Wilder RSI14 seeding, EMA200 seeding, **LONG/FLAT only**, an **entire-position** RSI(VWAP) **cross-under 90** exit or **completed-close 5% stop trigger** (whichever first), one fixed 0.001 BTC position, 10,000 USDT initial quote cash, Binance BTC-USDT spot **1h**, 300 completed-bar warmup, one-completed-bar-delayed idealized MARKET-close fills, and hypothetical 0.1% fee on each side. The author's partial profits, 30 full exit, original risk-based sizing, native VWAP anchor, native stop-order execution, native timing, and any other unspecified Pine behaviors are **not preserved**. All differences are intentionally researcher-defined, can materially change trade events and risk, and are not attributed to eemani123. The source's backtest statistics are not reproduced or adopted.

**Frozen identity:** `TV:OUzp2NR6|eemani123|2020-11-04-public-description|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC1h|UTC00-session-close-volume-VWAP|WilderRSI14-of-VWAP|EMA200-close-SMA-seed|entry-crossup70-and-close-above-EMA200|exit-crossdown90-or-entry-frozen-close-stop5pct|long-flat|next-completed-close-MARKET|Q0.001BTC-cash10000USDT|fee0.001-each-side|warmup300|noDCA`. Any alteration is a different strategy identity.

**Dedup on main and open research PRs:** current prewrite `main` SHA `bef475c0d22ab0a7ace910e854d82f328b90cbc1`, untruncated Git tree **444** root-level strategy Markdown records; README count **444**; ten distributed sampled frontmatters PASS (not a 444-record full audit). Connected GitHub main code searches for `OUzp2NR6`, `RSIofVWAP`, `RSI(VWAP)`, and `eemani123` yielded no match. Eleven open PRs were reviewed for source and mechanism; no open `research/*` PR used this script or this normalized rule. Existing VWAP + ordinary price RSI filters, e.g. thetraderlodge pivot/VWAP/RSI3 and Forven VWAP pullback, do **not** apply Wilder RSI to a **daily-reset session VWAP series** and then enter on its 70 crossing and exit on its 90 crossing. This is a different transformed-input signal, not a trivial RSI-length retune. This is a bounded dedup review, not an exhaustive proof of semantic non-equivalence for every file.

## Research hypothesis, not reproduced performance

RSI of a session-anchored volume-weighted price can emphasize directional participation instead of raw price momentum; EMA200 selects a positive medium-term regime. A 90-down-cross full exit tests whether an extreme participation impulse reverses; a completed-close stop tests a separate adverse-price guard. Daily session resets can introduce sharp discontinuities in VWAP and hence RSI; they are deliberate, causal features of this derivative and can create whipsaws. No profitability, Survivor, Qlib parity, source-native replication, Paper, Testnet, or Live claim.

## Exact signal, data and initialization (Gates 1, 2, 6)

**Single feed:** actual Binance spot `BTC-USDT` UTC-aligned `1h` REST candles, each with open timestamp `T[t]`, positive finite O/H/L/C, finite **base-asset** volume `V[t]>0`, high >= max(open,close), low <= min(open,close), high >= low, strictly increasing contiguous 3600-second timestamps. Reject duplicate, missing, zero-volume, malformed, nonfinite, out-of-order, or incomplete candles; **abort** the research run, including if already LONG, rather than fabricate/forward-fill data or fill prices. The sample starts at a UTC 00:00 session boundary so no partial opening session is silently treated as a complete one.

**Session VWAP:** UTC calendar session starts at each 00:00 UTC. For each fully completed hour `t`, `S(t)` is the first 00:00 UTC bar in the same UTC day. `VWAP[t] = sum(C[i]*V[i], i=S(t)..t) / sum(V[i], i=S(t)..t)`; reset numerator and denominator exactly at UTC 00:00. Use **close** as VWAP price input, not HLC3; base volume weights; no lookahead, smoothing, cross-session carry, volume fallback, synthetic price or future hour. Denominator is positive by validated `V>0`. The first hourly VWAP of each UTC day equals that hour's close. This UTC anchor is a researcher pin, **not** a claim about the author's native TradingView exchange-session settings.

**Wilder RSI14 of session VWAP:** let `d[t]=VWAP[t]-VWAP[t-1]` for t>=1, `g[t]=max(d[t],0)`, `l[t]=max(-d[t],0)`. At `t=14`, seed `G[14]=sum(g[1..14])/14`, `L[14]=sum(l[1..14])/14`. For t>14, `G[t]=(13*G[t-1]+g[t])/14`, `L[t]=(13*L[t-1]+l[t])/14`. If `L>0`, `RSI[t]=100-100/(1+G/L)`; if `L=0,G>0`, RSI=100; if `G=L=0`, RSI=50; if `G=0,L>0`, RSI=0. No RSI defined before index 14. The VWAP change across UTC-midnight resets is **included** in the continuous RSI recursion; RSI itself does not reset daily. This is researcher-defined and fully deterministic.

**EMA200 of close:** `EMA200[199]=sum(C[0..199])/200`; for t>=200, `EMA200[t]=(2/201)*C[t]+(199/201)*EMA200[t-1]`. No EMA before 199. Calculate indicators in chronological float64 without per-step rounding; signal comparisons use full computed values.

**Entry cross:** `UP70[t] = RSI[t-1] <= 70 AND RSI[t] > 70`. `ENTRY[t] = UP70[t] AND C[t] > EMA200[t]`. Equality on current RSI or price fails; equality on previous RSI permits the crossing. Do not require an EMA crossover or any other filter.

**Exit cross and close stop:** `DOWN90[t] = RSI[t-1] >= 90 AND RSI[t] < 90`; equality on current RSI does not cross. At the confirmed BUY fill `j` at actual modeled close `P=C[j]`, freeze `STOP=0.95*P` (not 5% from the earlier signal close). For a LONG position and completed decision bar `t>j`, `EXIT[t] = (C[t] <= STOP) OR DOWN90[t]`. If both true, classify as STOP first; otherwise classify RSI90. This is a **close-triggered** risk condition, not an intrabar resting stop or guaranteed maximum loss; subsequent next-close exit can lose more than 5%.

**Warmup:** first **300** contiguous fully completed UTC hours (indices 0..299) are indicator-only; first decision may occur at t=300 with both current and prior RSI and EMA defined. All features at t use bars <=t only. A bar is decision-available at `E[t]=T[t]+3600 seconds`, never at its Binance open timestamp. No future prices, unconfirmed higher timeframe, repainting, trained model, full-sample normalization or hindsight optimization.

## Trade events, risk, cash and state (Gates 2–4)

- **Market/side:** unleveraged Binance `BTC-USDT` **spot LONG/FLAT**; shorts, borrowing, margin, leverage, perpetual funding, cross-asset capital and hedging are disabled. One strategy, one pair, one position, one pending action maximum.
- **FLAT -> PENDING_BUY:** on a fresh eligible `ENTRY[t]` at E[t], queue a fixed `Q=Decimal("0.001")` BTC MARKET BUY for the **next completed candle close** `C[t+1]` at E[t+1]. Do not inspect t+1 to decide t's signal. At that row, require actual positive finite C, exact full fill confirmation, and quote cash >= `Q*C*(1+0.001)`; otherwise abort/fail closed, never invent a fill, deferred order or partial fill.
- **PENDING_BUY -> LONG:** after confirmed full modeled BUY at E[j], debit quote notional plus modeled fee, credit Q BTC, freeze STOP from actual C[j], and set `fill_index=j`. Ignore all new entry/exit decisions on the fill bar j.
- **LONG -> PENDING_SELL:** at an eligible completed t>j, evaluate STOP first then DOWN90; if either true queue full Q MARKET SELL for next completed candle close at E[t+1]. Do not sell at STOP or 90 threshold price; do not assume a limit/stop touched intrabar. While LONG ignore ENTRY, and while pending ignore all new signals.
- **PENDING_SELL -> FLAT:** on a confirmed full SELL fill, debit Q BTC and credit quote proceeds less modeled fee. The SELL fill bar is not a new entry decision. Only a **fresh subsequent UP70** with EMA200 filter can re-enter; no queued stale signal reuse.
- **Explicitly disabled:** partial profit-taking (including the author's original 90 partial), original 30 exit, original risk-budget sizing, take-profit limit, trailing stop, time exit, stop-market/resting intrabar orders, DCA/safety orders, pyramiding, averaging, concurrent positions, cooldown beyond pending/fill-bar suppression, reverse-to-short, maker/limit/next-open fills, synthetic final liquidation. A LONG at dataset end remains open and is marked unrealized at the last **actual** valid close; pending orders without a real next candle remain unfilled.
- **Error policy:** missing candle, fill, fee, timestamp, sufficient cash, inventory, or position confirmation **fails the run** rather than assuming success, zero fees or a price. No silently repeated order on partial/failed fill. The absence of a protective exchange stop is a significant research risk.

## Pinned Hummingbot engine/data/fill/cost compatibility (Gate 5)

**Frozen engine identity:** Hummingbot package label **`20260920`**, `hummingbot/VERSION=dev-2.17.0`, immutable source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Direct GitHub-connector reads this cycle confirmed VERSION and the actual files below at that commit. Existing independently merged Alpha PR **#414** documents 902/902 matching wheel Python files and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`. This cycle did **not** rehash installed wheel bytes or a running image; the auditor must verify applicability of that inherited package/source evidence. The source `setup.py` version string must not be mistaken for proof of package-label identity.

**Real pinned data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `1h`; `binance_spot_candles.py::_parse_rest_candles` reads Binance `/api/v3/klines` and maps `row[0]` to candle **open** timestamp and `row[1..5]` to O/H/L/C/base volume. `BacktestingDataProvider.get_candles_df(connector_name="binance",trading_pair="BTC-USDT",interval="1h")` supplies those rows. VWAP/RSI/EMA are **strategy-specific causal feature calculations** over these same verified OHLCV rows; no session-vwap API, order-book, non-OHLCV or multi-timeframe path is assumed.

**Real pinned controller/executor path:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` updates per-row controller state and processes `CreateExecutorAction` via `simulate_executor`. `hummingbot/strategy_v2/executors/order_executor/data_types.py::OrderExecutorConfig` supports Binance spot `TradeType.BUY/SELL`, `PositionAction.OPEN/CLOSE`, `ExecutionStrategy.MARKET`, fixed amount Q and leverage 1. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py::simulate` for MARKET uses the **first supplied row**, actual `close` as fill price, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and `CloseType.POSITION_HOLD`. This is **more than an API-name inference**: the actual fill calculation was read at the immutable commit. The future **strategy-specific** controller (NOT implemented in this Scout) must latch the decision from row t, emit the action only on row t+1, and expose its event at **E[t+1]**, never incorrectly at the raw Binance open timestamp T[t+1]. This is a bounded **idealized retrospective close-fill model**, not a claim a real market order can be submitted after knowing the close and receive that exact price.

**Accounting and fees:** start `cash=Decimal("10000")` USDT, `inventory=Decimal("0")` BTC, fixed Q. Research-only `run_backtesting(trade_cost=0.001)` books **hypothetical** 0.1% of filled quote amount on each side, **not a verified Binance taker fee**. BUY at real modeled P: `cash -= Q*P*(1+0.001)`, `BTC += Q`; SELL at P: `cash += Q*P*(1-0.001)`, `BTC -= Q`. Modeled round-trip net quote PnL = `Q*(P_sell-P_buy)-0.001*Q*(P_sell+P_buy)`. Pinned `BacktestPositionHold` nets opposite POSITION_HOLD fills and tracks realized gross PnL and fees separately; maintain a Decimal cash/inventory ledger from **confirmed full fills**, reconcile each terminated executor and fees against hold/position state, and preserve complete terminated-executor visibility (`terminated_executors_window=None`) plus the one-update POSITION_HOLD lag. Never use a float dust balance as authority or mistake gross executor PnL for fee-net equity. Abort on unreconciled quantities/fees/fills rather than silently repair. Final open inventory is valued only at the last actual observed close.

**Data and economic boundaries:** `BacktestingDataProvider.get_price_by_type` may default to `Decimal("1")` on missing price; **never** use this fallback for fills, stops, cash or marks. Real tick/lot/min-notional constraints, live order acceptance, spread, latency, slippage, impact, partial fills and actual fee tiers are **not established** by this historical simulator. No additional slippage is modeled by the pinned MARKET-close simulator; this is an explicitly idealized modeling limitation, **not** a real-world zero-slippage claim. Spot has no perpetual funding; no fictitious zero futures funding, futures margin, mark-price, liquidation or leverage cash flows are imported. The only execution primitive is the previously reviewed single-pair Binance spot 1h OHLCV -> delayed controller action -> MARKET-close OrderExecutorSimulator -> POSITION_HOLD cost/position ledger path. No new data/execution primitive is asserted.

## Six-gate Scout proposal (subject to independent Hermes Auditor)

1. **G1 deterministic:** exact UTC-session close-volume VWAP, Wilder RSI14, EMA200, SMA seeds, strict crossings, 300-bar warmup, validation and no fitted inputs.
2. **G2 direction:** BTC-USDT spot LONG/FLAT only; short/futures paths explicitly disabled.
3. **G3 entry/exit/risk:** RSI(VWAP) UP70 plus EMA200 entry; RSI(VWAP) DOWN90 or entry-frozen 5% completed-close stop exit; no other exit or hidden risk behavior.
4. **G4 position/state:** fixed 0.001 BTC, 10,000 USDT cash, one pending/full-fill state machine, no DCA/pyramiding/partial exits, no same-fill-bar re-entry.
5. **G5 pinned compatibility:** exact package/VERSION/source, verified Binance 1h OHLCV and MARKET-close simulator mechanics, delayed controller dispatch, hypothetical fees, confirmed fill/position/Decimal cash reconciliation, explicit real-world limitations and missing-price fail-closed rule.
6. **G6 causality:** UTC hourly completed decision at open+3600, next completed close fill at t+1, no future data, session reset and RSI recursion fully causal.

**Independent audit focus:** source release-note ambiguity about 90 partial/full versus 30 exit; derivative disclosure; exact UTC-session VWAP reset and first-session completeness; RSI zero-denominator and midnight behavior; full-exit versus source partials; stop overshoot; fill-bar suppression; raw open timestamp versus effective close timestamp; inherited package-to-source proof; POSITION_HOLD/fee reconciliation. `hb_ready_status: PASS` is this Scout's **proposed** eligibility for the explicitly derived strategy only, not an independent audit result or authorization to implement/trade. If the auditor cannot establish any required Gate 5 path, this research must not enter main.

## Limitations and downstream boundary

No original Pine bytes/revision, original-event parity, independently reproduced TradingView backtest, Qlib/Hummingbot backtest, live fee, slippage, venue acceptance, profit claim, survivor result, or trading authorization. No Qlib executable/controller is included. Before large-scale Qlib screening of any newly required primitive, run one representative event-level Hummingbot/Qlib parity validation; this Scout performs no tests or engine changes. Keep non-PASS findings outside main; independent exact-head Auditor review controls admission.
