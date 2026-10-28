---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "djthefreeway close/open VWMA35 crossing — independent BTC-USDT spot 1d long-flat research derivative"
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
source_as_of: 2025-04-18
sources:
  - https://www.tradingview.com/script/IwESIAB9-Close-v-Open-Moving-Averages-Strategy-Variable-divonn1994/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Close-versus-open volume-weighted average crossing — explicitly independent research derivative v1

## Provenance and frozen strategy identity

**Primary source:** TradingView public open-source strategy **Close v Open Moving Averages Strategy (Variable) [divonn1994]**, author **djthefreeway**, immutable public script ID **IwESIAB9**, first published **2022-08-15**, latest public release notes **2025-04-18** (v2 on 2025-03-06, v3 on 2025-03-17, further MA types added 2025-04-18), accessed **2026-10-29**: https://www.tradingview.com/script/IwESIAB9-Close-v-Open-Moving-Averages-Strategy-Variable-divonn1994/. This first-party text explicitly compares moving averages of bar **opening** and **closing** prices; the close average moving above the open average opens a long, and the reverse cross exits the long (optional shorts added in v2). It explicitly lists **BTCUSD BitStamp 1d, VWMA length 35** among the author's historical example settings; the April 2025 release notes still list VWMA as a selectable MA. No author's return multiple is adopted as a reproduced result.

**Source-native facts, narrowly bounded:** two different price series (open and close) each averaged with the selected MA; crossing direction controls long entry and exit; VWMA and length 35 are a first-party **example configuration**, not a verified default; optional short trades exist in later revisions. **Full executable Pine bytes, declaration defaults, exact revision hash, order execution flags, original trade sizing, fee settings and other original source rules were not retrievable from the public text interface.** The latest release-note version is documented, not a claim that the underlying Pine bytes were verified. This is not a lossless Pine reconstruction.

**Independent derivative (only this derivative is proposed as HB_READY PASS):** adopt the author's publicly documented **VWMA35** comparison mechanism and long/exit direction, but independently define Binance BTC-USDT spot UTC 1d, raw exchange O/C/base volume (not BitStamp BTCUSD), exact weighted-average math, strict cross predicates, 100-bar warmup, one-bar delayed idealized MARKET-close simulator fills, a fixed 0.001 BTC order, 10,000 USDT starting quote cash, one long position, no short/pyramiding/DCA, hypothetical 0.1% fee per filled side and explicit ledger/failure handling. All these execution and venue choices are **researcher-defined** and must not be attributed to djthefreeway or presented as source-native. Any parameter, price source, timing, market, sizing or cost change is a different frozen strategy identity.

**Dedup:** inspected 422 root-level Markdown strategy records on prewrite `main` SHA `98f685033fb1e66349b5c710617bd09e9e246dc2` by complete Git tree, README counter 422, and all 10 open PR metadata (the open `research/*` heads included in the set). GitHub connector searches on main for `IwESIAB9`, `"close vs open"`, `"vwma(open"`, `"VWMA35"` and `"opening moving average"`, plus open PR source-ID/title search, yielded no same-source candidate. Nearest `heikin-ashi-ema-trend-state-btcusdt-1d-2026-10-11.md` uses **Heikin-Ashi** transformations, EMA77 plus EMA21 smoothing and a two-sided trend latch, **not raw O/C VWMA35 strict crossings**. Ordinary close-only SMA/EMA cross families compare different lengths of one close series, not volume-weighted raw open against close at the same 35-bar length. This is a different causal event mechanism, not a mere timeframe/parameter retune. Dedup is a research check, not a claim of exhaustive semantic equivalence across every source.

## Signal — complete deterministic frozen mathematics (Gate 1)

One feed: Binance spot `BTC-USDT` `1d` UTC candles indexed by contiguous UTC calendar day `t`; each record has actual finite `O[t]>0, H[t]>=max(O[t],C[t]), L[t]<=min(O[t],C[t]), C[t]>0` and **finite base-asset volume `V[t]>=0`**. Reject malformed OHLCV, duplicates, out-of-order days, any missing day, nonfinite numbers, negative volume or missing actual close; do not interpolate, backfill, or synthesize price/volume. After any gap, reset all indicators and rewarm 100 contiguous completed bars.

For `t>=34`, let `D[t] = sum(V[i], i=t-34..t)`; require `D[t]>0`, otherwise no signal and reset/re-warm on invalid data. Define `VWMA_C[t] = sum(C[i]*V[i], i=t-34..t)/D[t]` and `VWMA_O[t] = sum(O[i]*V[i], i=t-34..t)/D[t]`, using the **same base-volume weights** and the **same inclusive 35-bar window**. No shifted inputs, no alternative MA, no fitted parameters, no rounding of indicator values before comparison.

Define `UP[t] = VWMA_C[t] > VWMA_O[t] AND VWMA_C[t-1] <= VWMA_O[t-1]`; `DOWN[t] = VWMA_C[t] < VWMA_O[t] AND VWMA_C[t-1] >= VWMA_O[t-1]`. Strict current inequality, inclusive previous equality; current equality fires neither. Both predicates cannot be true simultaneously. All calculations use only completed bars through `t`; no current incomplete candle or future extrema.

**Warmup:** require 100 consecutive fully closed, validated daily bars and both current/prior VWMA35 values before the first decision; no order before this point. Indicator availability is based on UTC daily **close**, not the Binance kline's open-time label. Display/alerts/histogram, original backtest date controls, optional short toggle and all other source UI features are **excluded** from this independently frozen derivative.

## Trade direction, entry/exit, risk and state (Gates 2–4)

- **Venue/side:** Binance `BTC-USDT` spot, **LONG/FLAT only**. No shorts, futures, margin, borrowing, hedges, leverage, shared capital or other assets; leverage=1.
- **Flat → pending BUY:** only on a fresh `UP[t]` at the completed-bar decision time `E[t]`, if warm, valid and no order pending. Reserve one `Q=Decimal("0.001")` BTC MARKET BUY for **next completed candle close** `C[t+1]`, not `O[t+1]`; insufficient actual quote cash for `Q*C[t+1]*(1+0.001)` aborts the candidate run without fictional fills.
- **Pending BUY → long:** only after one verified full fill, fee booking and inventory reconciliation at `E[t+1]`. A signal or state flip during the pending/fill bar is not acted on; do not pretend the fill was known earlier.
- **Long → pending SELL:** only on a fresh `DOWN[t]` at a later eligible completed bar with no pending action. Queue full `Q` MARKET SELL for `C[t+1]`; no partial close, no discretionary exit. A DOWN on the BUY fill bar is intentionally ignored; the next eligible **new** DOWN crossing is required.
- **Pending SELL → flat:** only on confirmed full sell fill, quote fee and inventory reconciliation; the SELL fill bar generates no new order. A fresh later `UP` is required to re-enter. An UP on the SELL fill bar is intentionally ignored.
- **Priority and guards:** if invalid data, price, quantity, insufficient balance, failed/partial/unconfirmed fill, or irreconcilable position/fee accounting appears, **abort/fail closed**, never assume an execution or silently resubmit. One pending action at most; one 0.001 BTC position at most. If last dataset bar has a signal but no real next candle, no simulated fill. Final still-open position is marked unrealized using the last real positive close, not silently closed.
- **Explicitly disabled:** stop-loss, take-profit, trailing stop, time exit, reverse-on-signal, repeated entry while long, pyramiding, DCA/safety orders, cooldown beyond pending/fill-bar suppression, intra-bar stop orders, maker/limit/next-open fills, synthetic bars, leverage and funding. **Risk:** a downtrend without a new strict DOWN crossing can remain long; there is no protective stop. This is deliberate derived research behavior, not a source-native safety claim.

## Execution assumptions — pinned Hummingbot model (Gate 5)

**Exact pinned baseline:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, admission package label **`20260920`**, directly read `hummingbot/VERSION` = **`dev-2.17.0`** via GitHub connector on 2026-10-29. Existing independently reviewed Alpha **PR #414** records package/wheel-to-source identity evidence for this pin; this Scout did **not** rehash installed wheel bytes or verify a running image. If that inherited identity is invalid, the pinned path is unverified and the Auditor must block Gate 5.

**Data path directly inspected at immutable commit:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` contains `1d` and Binance `/api/v3/klines`; `binance_spot_candles.py::_parse_rest_candles` maps Binance kline row 0 to **open** timestamp and row 1..5 to actual O/H/L/C/base volume. `BacktestingDataProvider.get_candles_df(connector_name="binance",trading_pair="BTC-USDT",interval="1d")` supplies the feed. The provider's `get_price_by_type` can return a default `Decimal("1")` on missing price; **never use this fallback** for fill, valuation or fee: abort if actual positive finite candle close is unavailable.

**Controller/executor path directly inspected:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` iterates prepared rows, `update_state(row)`, then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction` to `simulate_executor`. A future minimal **strategy-specific** controller (not created in this Scout) computes the exact O/C VWMA signals, latches pending actions, and dispatches the action **only on row t+1** after a decision on t. `hummingbot/strategy_v2/executors/order_executor/data_types.py::OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=TradeType.BUY/SELL`, `amount=Decimal("0.001")`, `position_action=PositionAction.OPEN/CLOSE`, `execution_strategy=ExecutionStrategy.MARKET`, `price=None`, `leverage=1`. These names alone are not the proof: directly inspected `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py::OrderExecutorSimulator.simulate` chooses the **first supplied row** for MARKET and fills at that row's actual `close`, records `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, then `CloseType.POSITION_HOLD`. No maker queue, limit touch, intrabar price, next-open fill or real exchange orderbook is used.

**Effective timestamp:** Binance daily candle `t` raw `T[t]` is UTC **open**; decision and valid close-based indicators become available at `E[t]=T[t]+86400s`. The backtest's raw timestamp/index and backward merge must be normalized/lagged so row t's O/C/V is never treated as known at T[t]. Decision at E[t] creates a queued intent, MARKET simulated fill uses **actual C[t+1] at E[t+1]**, and the fill bar is not simultaneously used for a new decision. This is a **bounded idealized historical close-fill model**, not a claim that a live market order can be placed after seeing and receiving the same close.

**Accounting:** starting `cash=Decimal("10000")` USDT and `inventory=0` BTC, fixed `Q=Decimal("0.001")`. Call pinned `run_backtesting(trade_cost=0.001)` for a **declared hypothetical 0.1% fee per filled side**, not a verified Binance fee. At real BUY fill P, debit `Q*P*(1+0.001)` quote, credit Q base; at real SELL fill P, debit Q base, credit `Q*P*(1-0.001)` quote. Round-trip modeled net quote PnL = `Q*(P_sell-P_buy)-0.001*Q*(P_sell+P_buy)`. The inspected `BacktestPositionHold` nets opposite POSITION_HOLD fills, tracks gross PnL and fees separately; float-derived quote/base conversion may leave dust. Maintain confirmed-executor **Decimal** inventory/cash authority and reconcile every terminated executor, gross PnL, fees and hold against it, tolerances at most `1e-9 BTC` and `1e-8 USDT` for diagnostics only (never forgive a missing fill). Preserve complete executor visibility (e.g. `terminated_executors_window=None`) and handle hold-ledger one-tick lag before further actions. Last real close marks any still-open position as unrealized.

**Cost/market boundary:** simulator does not establish real exchange spread, impact, latency, slippage, partial fills, tick/lot/min-notional acceptance or actual fee tier. Those are unverified real-world economics, **not zero-cost claims**. Spot has no perpetual funding payment; no futures funding, mark price, margin, liquidation or financing assumption is imported. No second asset, extra timeframe, cross-asset synchronization or unsupported engine path is needed.

## Six-gate Scout evidence (proposal only; independent review required)

1. **Determinism:** exact 35-day base-volume VWMA of O and C, same weights, strict UP/DOWN with previous equality, 100-bar warmup, finite data guards and frozen state.
2. **Direction:** BTC-USDT spot LONG/FLAT; shorts disabled explicitly.
3. **Entry/exit/risk:** UP fresh crossing queues BUY; DOWN fresh crossing queues full SELL; no SL/TP/trailing/time exits, all disabled explicitly.
4. **State:** one fixed 0.001 BTC position, 10,000 USDT initial cash, pending/full-fill transitions, no DCA, pyramiding, concurrent orders or hidden re-entry.
5. **Actual pinned compatibility:** inspected 1d Binance O/C/V feed, controller action iteration, MARKET first-row actual-close fill, POSITION_HOLD and modeled quote fee path, missing-price guard, Decimal reconciliation; inherited wheel/source identity bounded by PR #414.
6. **Causality:** 100 consecutive completed UTC days, strictly past/current 35-bar windows, bar-open vs completed-close timestamps distinguished, decision E[t] and next real close fill E[t+1], pending-bar suppression, no lookahead or repaint.

## Negative evidence, limitations, downstream boundary

The public page documents the **concept and an example configuration**, not a complete accessible Pine source. This is an **independent derivative**; no original exact Pine execution equivalence, original defaults, performance, profitable return, Qlib parity, OOS, Survivor, HB Certified, or Paper/Testnet/Live approval is asserted. No candidate backtest, controller implementation or live trade was performed. Source-reported extraordinary profit examples are **not independently reproduced** and must not enter admission evidence. The hypothetical close-fill/fee model is not actual exchange execution.

Future separately authorized falsification: equal VWMA rails, zero-volume denominator, differing open/close with same volume weights, partial/failing fills, missing 1d candle, last-bar pending signal, pending BUY crossdown, pending SELL crossup, quote-fee ledger dust, cash guard, no-stop drawdown, and exact E[t] timestamps. Before mass Qlib screening of a newly introduced execution/data primitive, validate representative Hummingbot↔Qlib event-level parity; this is not another HB_READY gate.

**Adoption boundary:** `hb_ready_status: PASS` is the Scout's **proposed six-gate research assessment**, **not** independent Auditor approval. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. Only independent Hermes Auditor GitHub Webhook Review may remediate source-verifiable facts, exact-head PASS merge or NOT_LOSSLESS close. Only existing signed GitHub webhook receiver updates README after accepted merge. No Qlib/Hummingbot testing, environment, cron, README, main, trade or other file change in this Scout.

## References

- First-party TradingView source, djthefreeway, 2022-08-15, latest documented update 2025-04-18: https://www.tradingview.com/script/IwESIAB9-Close-v-Open-Moving-Averages-Strategy-Variable-divonn1994/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent pinned-wheel identity evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
