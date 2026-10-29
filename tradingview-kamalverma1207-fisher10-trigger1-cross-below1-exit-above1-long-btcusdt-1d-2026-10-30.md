---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "kamalverma1207 Fisher/lag-trigger below-1 entry above-1 exit — BTC-USDT spot 1d independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-08-04
sources:
  - https://www.tradingview.com/script/oVoigpVw-Fisher-Crossover-Strategy/
  - https://www.tradingview.com/script/qhXwZvJ2-Fisher-Transform-Indicator-by-Ehlers-Backtest-v-2-0/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fisher / one-bar trigger threshold-separated crossover — independent derivative v1

## Provenance

**Primary immutable source identity:** TradingView public open-source strategy ID **oVoigpVw**, *Fisher Crossover Strategy*, author **kamalverma1207**, dated and updated **2025-08-04**, public first-party page https://www.tradingview.com/script/oVoigpVw-Fisher-Crossover-Strategy/, inspected 2026-10-30. The **2025-08-04 release notes**, rather than the broader introductory paragraph, explicitly state: Fisher line versus its **one-bar lag** trigger; **long entry** on Fisher crossing **above** its trigger while Fisher is **below 1**; **long exit** on Fisher crossing **below** its trigger while Fisher is **above 1**; **one trade at a time**, decisions on **completed candle close**, and fixed **INR 20,000** cash allocation. The earlier general introduction describes generic up/down crosses without these threshold gates; the release-note-specific gates take precedence. The public text does not expose the original Pine bytes, indicator length/initialization, native order-fill flag, fee settings, quantity precision or native stop/target calls. No original Pine revision/hash or source-native execution equivalence is claimed.

**Secondary TradingView mathematical provenance:** HPotter's 2016-12-23 *Fisher Transform Indicator by Ehlers Backtest v 2.0*, ID **qhXwZvJ2**, https://www.tradingview.com/script/qhXwZvJ2-Fisher-Transform-Indicator-by-Ehlers-Backtest-v-2-0/, states the Fisher warp 0.5*ln((1+x)/(1-x)). Its **zero-sign trading strategy is NOT imported**. The following 10-bar hl2 range, recursive smoothing, neutral flat-range behavior and all initialization details are **researcher-selected** and do not claim to reproduce kamalverma1207's unseen Pine or HPotter's complete original implementation.

**Explicit independent derivative, not source-native:** preserve only the first author's distinctive lag-trigger cross plus the asymmetric **below-1 entry / above-1 exit** requirements and one-position long intent. Independently specify Fisher implementation, BTC-USDT spot 1d, USD quote cash, fixed BTC amount (instead of INR 20,000), warmup, delayed next-completed-close idealized MARKET fills, fee, no stop/target, state machine and error handling. All alterations are disclosed here; do not attribute them to the source. Frozen identity: TV:oVoigpVw | kamalverma1207 | release-2025-08-04 | independent-derived-v1-20261030 | Fisher-hl2-10-recursion-0.33/0.67-0.5/0.5 | lag1 | entry-crossup-F<1 | exit-crossdown-F>1 | BinanceSpot-BTC-USDT-UTC1d | 0.001BTC-10000USDT | t-decision-t+1-completed-close-MARKET | fee0.001 | warmup120 | no-DCA.

**Dedup on main SHA `5a3d1297d0d0516efca3e38c0531c7286112ebaf`:** untruncated tree **450** root strategy Markdown records; README count **450**; 18 spread-out frontmatter samples PASS, **not** a full 450-record census. GitHub main search found no oVoigpVw, kamalverma1207 or same source; open research/* PRs were checked (including #593 and Hermes research PRs) and no same-source/crossover-threshold PR was found. The nearest main record `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` follows Fisher **zero-sign two-sided reversal** with no one-bar trigger or ±1 asymmetric gates. This candidate instead requires **Fisher/lagged-Fisher turning-point crosses plus disjoint <1 and >1 filters**, is **long/flat only**, and can hold through any cross that fails the >1 exit gate. These are materially different event rules, not a trivial parameter retune. Other Fisher-related records use volume/Fisher combinations, inverse Fisher RSI, or unrelated cross/zero mechanisms.

## Economic mechanism

### Source-reported

A Fisher-transformed price oscillator seeks to amplify turning points; the **one-bar lag crossover** indicates a possible momentum inflection. The published release notes use an entry below +1 and an exit above +1, not an unconditional zero-sign regime. No independently reproduced return, win rate, profit factor or market advantage is established.

### Research interpretation

A threshold-separated **turning-point** strategy: buy when the transformed oscillator begins rising versus its previous value while still below +1; sell only when the oscillator begins falling versus its previous value **above +1**. A bearish turn below or at +1 does **not** force an exit; risk of indefinite hold and large drawdown is deliberately preserved. This differs structurally from the pool's zero-sign Fisher reversal.

## Signal

**Researcher-pinned indicator, all calculations on fully completed UTC 1d candles:** index t=0,1,...; x[t]=(H[t]+L[t])/2; for t>=9 compute lo[t]=min(x[t-9..t]), hi[t]=max(x[t-9..t]). If hi>lo, u[t]=(x[t]-lo)/(hi-lo); if hi==lo, u[t]=0.5 (explicit researcher neutral tie, not claimed source behavior). Require 0<=u<=1; reject nonfinite/invalid input. Initialize previous n and Fisher values to **0** before t=9. For each t>=9, n[t]=0.66*(u[t]-0.5)+0.67*n[t-1]; v[t]=max(-0.999,min(0.999,n[t])); F[t]=0.5*ln((1+v[t])/(1-v[t]))+0.5*F[t-1]. For t=9 use n[t-1]=F[t-1]=0. This is a deterministic, chosen recursive Fisher variant; no external fit, TA-Lib default, dynamic period, or undisclosed preprocessing.

**Trigger and exact cross semantics:** trigger[t]=F[t-1] for t>=10. At t>=11, `UP[t]` iff F[t]>F[t-1] **and** F[t-1]<=F[t-2]; `DOWN[t]` iff F[t]<F[t-1] **and** F[t-1]>=F[t-2]. Equality on the **prior** comparison qualifies; equality on current comparison fails. **BUY signal** iff UP[t] and F[t]<1 while FLAT and no pending action. **SELL signal** iff DOWN[t] and F[t]>1 while LONG and no pending action. Exact F[t]==1 fails both gates. This compares Fisher with its lagged value, **not** Fisher with zero, an EMA or a fixed ±1 crossover. Source release-note conditions are preserved; all numerical Fisher preprocessing is a disclosed derivative.

**Warmup:** completed t=0..119 (120 full candles) are indicator-only, initial state FLAT, zero inventory; first eligible signal t=120, with all t-2 dependencies already defined. No signal during warmup is queued or replayed. All calculations use bars <=t; no request.security, future extrema, repainting, negative shift, full-sample normalization or incomplete bar input.

## Required data

Actual contiguous Binance spot **BTC-USDT 1d** UTC OHLCV, with strictly increasing exchange **candle-open** timestamps T[t] exactly 86400 seconds apart. Validate finite positive O/H/L/C, H>=max(O,C), L<=min(O,C), nonnegative finite base volume, no duplicate/missing/out-of-order/partial rows; abort on malformed input before feature preparation. Signal uses H/L only, fills and marks use actual observed close C; volume is validated but not a signal. The completed t decision becomes available at E[t]=T[t]+86400 seconds, **not** at T[t]. No funding, OI, order book, off-exchange data, higher/lower timeframe, cross-pair alignment or synthetic/future price is required.

## Execution assumptions

**Market/size:** unleveraged Binance BTC-USDT **spot**, LONG/FLAT only; initial 10,000 USDT cash and zero BTC; one fixed Q=Decimal("0.001") BTC per full trade, one pair, one pending order, no shared-capital portfolio. This replaces the source's INR 20,000 notional; source cash allocation and source execution are **not** reproduced.

**FLAT -> PENDING_BUY:** eligible BUY signal at completed E[t] queues one MARKET BUY for the **next actually observed completed** candle t+1. Dispatch only on row t+1; simulator full-fill price is that row's **actual C[t+1]**, economically labeled E[t+1], not its raw candle-open timestamp. Check cash>=Q*C[t+1]*(1+0.001). Confirm complete fill, fee and quantity before entering LONG. No same-signal-bar fill or next-open assumption.

**PENDING_BUY -> LONG:** debit Q*P*(1+0.001) quote, credit Q base on confirmed fill; store fill bar j; ignore all entry/exit triggers on j. On later t>j, only the exact DOWN[t] AND F[t]>1 rule can queue exit. No stop, target, time limit, trailing, opposite zero-sign or risk rescue. Holding may persist to sample end.

**LONG -> PENDING_SELL -> FLAT:** qualifying completed exit at E[t] queues one full Q MARKET SELL for next observed completed t+1. On confirmed full fill at actual C[t+1], debit Q BTC and credit Q*C[t+1]*(1-0.001) USDT; reconcile engine position and fee ledger. Ignore all signals on sell fill bar; after becoming FLAT, a **new later UP cross with F<1** is necessary for re-entry. Pending orders suppress all new signals; no pyramiding or same-bar reversal. If t+1 is absent at sample end, leave pending unfilled, never invent a fill; if LONG remains, mark only to last observed actual close.

**Failure/disabled behaviors:** missing price, nonfinite indicator, fee/quantity discrepancy, partial/failed fill, insufficient cash or irreconcilable position => **abort** rather than assume success. No DCA, safety orders, BO/SO, leverage, margin, futures, shorts, partial exits, hedges, simultaneous positions, discretionary orders, maker/limit/resting orders, intrabar stop/target, forced terminal liquidation, compounding, extra cooldown or additional filters. Cooldown consists only of pending and fill-bar suppression.

**Costs and risk:** fixed hypothetical `trade_cost=0.001` (0.1% each filled side), **not verified Binance taker fees**; fee-net round trip Q*(P_sell-P_buy)-0.001*Q*(P_buy+P_sell). No separate slippage model in this historical simulator path; this is **not** evidence of zero real spread, slippage, latency, impact or partial fills. The delayed completed-close fill is a retrospective engine convention, **not** an achievable guarantee of obtaining a close already observed. Spot has no perpetual funding settlement; this record makes **no claim** about zero futures funding, margin or liquidation.

## Pinned Hummingbot compatibility (Gate 5)

Pinned package **20260920**, VERSION **dev-2.17.0**, source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. This Scout directly read immutable `hummingbot/VERSION`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `.../backtesting_data_provider.py`, `.../executors_simulator/order_executor_simulator.py`, `hummingbot/strategy_v2/executors/order_executor/data_types.py`, and Binance spot candle parser/constants through the GitHub app. Prior Alpha PR **#414** reports package/source wheel correspondence; this Scout **did not** independently hash a local wheel or run the engine. Auditor must verify the inherited correspondence if needed.

**Real feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` exposes Binance `/api/v3/klines` and supported daily candles; `binance_spot_candles.py::_parse_rest_candles` maps exchange row[0] to **open timestamp** and row[1..5] to OHLCV. `BacktestingDataProvider.get_candles_df` serves the pinned connector/pair/interval. Prevalidate all source candles because engine preparation may drop missing values. All Fisher inputs are causal transformations of these rows, not unverified native indicator data.

**Actual controller/executor path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, then `simulate_executor` for `CreateExecutorAction`. A future strategy-specific controller (NOT supplied or implemented here) must latch signal t and submit the action on **row t+1** only. `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, BUY/SELL, Q=Decimal("0.001"), `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. The inspected `OrderExecutorSimulator.simulate` MARKET branch fills at the **first supplied row**, with **that row's close** as price, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, `CloseType.POSITION_HOLD`. This is verified pinned simulator math, not inferred from an API name. Raw row timestamp is candle-open; reporting must normalize effective decision/fill times to **E[t]** and must not claim the exchange traded at the raw open timestamp.

**Position/cost accounting:** pinned `BacktestPositionHold` aggregates confirmed opposing BUY/SELL exposures; engine `update_executors_info` and final flush handle POSITION_HOLD with a one-update handoff. Keep the full terminated-executor ledger and reconcile gross PnL, separately charged fees and an explicit Decimal base/quote cash ledger; never label gross PnL as net equity. `BacktestingDataProvider.get_price_by_type` may fall back to Decimal("1") for missing prices: **never use that fallback** for fills, marks or trade decisions; fail closed. Precision/min-notional, true venue fees, order acceptance, dynamic slippage, live fills and actual profitability are not verified. No multi-asset, futures funding or unsupported intrabar primitive is required. This is a **bounded idealized historical path**, not live execution certification.

**Required engine wiring for the already-declared daily confirmed-fill path (source-verifiable):** instantiate `BacktestingEngineBase(terminated_executors_window=None)` and call `run_backtesting(..., backtesting_resolution="1d", trade_cost=0.001)`. The pinned method defaults to `backtesting_resolution="1m"`; daily signal/feed declarations alone do not change the simulation tick interval. The pinned terminated-executor controller-view default is **3600 seconds**, distinct from the complete internal `stopped_executors_info` results ledger. A MARKET fill created on daily row j is first collected by `update_executors_info` on the following daily update; its recorded close timestamp is row j, so the default view prunes it before `controller.determine_executor_actions()` can observe its confirmation. Merely retaining the complete internal ledger is not equivalent to exposing confirmations to the controller. `terminated_executors_window=None` is the source-documented full-history controller-view option and preserves those confirmations for the already-required pending/fill and cash-ledger reconciliation. Process each confirmed executor ID once; do not substitute the later `positions_held` handoff for the declared fill confirmation. Full-history controller scans can be O(n^2) in executor count; this is a disclosed engine-view cost, not a new strategy rule or performance claim. Evidence: pinned `backtesting_engine_base.py`, `BacktestingEngineBase.__init__`, `run_backtesting`, `simulate_execution`, `_record_terminated_executor`, `_prune_terminated_executors_view`, and `update_executors_info`. No source-native equivalence or change to the declared signal, sizing, delayed fill, or state transitions is introduced.

## Evidence

### Source-reported

TradingView author kamalverma1207, dated 2025-08-04 release notes: Fisher vs its one-bar lag, UP with Fisher below 1 for long entry, DOWN with Fisher above 1 for long exit, one position and completed-candle confirmation, INR 20,000 source allocation. Secondary TradingView author HPotter, 2016-12-23, supplies Fisher logarithmic transformation concept, **not** this strategy's trade events. No source performance statistics are adopted.

### Independently reproduced

Not independently reproduced. No TradingView, Qlib or Hummingbot backtest executed; no trade-level parity or profitability claim.

### Negative evidence

No original kamalverma1207 Pine bytes/commit hash or native fill/fee settings available in the public extracted page; no assertion of source-native equivalence. A cross failing the <1 entry or >1 exit condition must **not** trade. No Fisher zero-cross signal, RSI filter, hidden stop/target, unverified VWAP, future data or synthetic fill is inserted. A no-range window is explicitly neutralized as researcher behavior. If independent review cannot verify any required pinned path or source fact, reject as NOT_LOSSLESS, do not relabel the original strategy or merge.

## Falsification plan

Independent reviewer should verify the source release-note precedence, separate source-native/derived claims, Fisher initialization and flat-range tie, two-prior-value cross boundary, <1 versus >1 gating, no-stop indefinite hold, full-fill pending transitions, 1d UTC timestamp availability, t+1 close simulator semantics, fee-net base/quote ledger, inherited package/wheel correspondence and missing-price failure. Later, before any large-scale Qlib screening of a new strategy/execution primitive, establish representative Qlib/Hummingbot **event-level** parity; HB_READY alone does not prove parity or profitability.

## Crypto portability

BTC-USDT Binance spot 1d is the only **declared derivative** here. Other assets/timeframes, futures/leverage, different cost/fill models and INR source allocation are unverified separate experiments, not silently admitted.

## Limitations

No verified original Pine source, no source-native timing, no observed returns, no live fee/slippage/precision validation and no candidate-specific implementation. Source-specific Fisher variant is unknown, so this is explicitly an **independent** signal implementation sharing the author's published trigger/threshold hypothesis, not a reconstruction. No protective stop exists and risk may be severe.

## Implementation status

`not-implemented` refers to a dedicated executable/controller artifact; this research record does not create one. PASS is a **Scout proposal** subject to independent Hermes Auditor six-gate review of the exact PR head, not an independently approved admission or a Qlib runnable strategy.

## Adoption boundary

`research-only`, `not-approved`: no Survivor, Qlib parity, Paper, Testnet, Live, trade authorization or investment advice. No backtest or environment change performed. Only the independent Hermes Auditor may PASS-merge or NOT_LOSSLESS-close this PR; only the existing signed webhook receiver may update the README counter after a confirmed merge.

## Related Wiki records

Nearest existing Alpha record: `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` (different Fisher zero-sign two-sided reversal). No Wiki edits.

## Sources

- Primary: https://www.tradingview.com/script/oVoigpVw-Fisher-Crossover-Strategy/ — kamalverma1207, 2025-08-04 release notes, TradingView ID oVoigpVw.
- Mathematical background: https://www.tradingview.com/script/qhXwZvJ2-Fisher-Transform-Indicator-by-Ehlers-Backtest-v-2-0/ — HPotter, 2016-12-23, TradingView ID qhXwZvJ2.
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 .
