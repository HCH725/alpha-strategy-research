---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: ChopFlow CI14 OBV10 trend-onset ATR14 close-bracket BTC-USDT 1h long-flat independent derivative
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
source_as_of: 2025-05-06
sources:
  - https://www.tradingview.com/script/TgcbEl6W-ChopFlow-ATR-Scalp-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ChopFlow CI14/OBV10 regime-onset with fixed ATR14 close bracket — independent BTC-USDT spot 1h derivative

## Provenance and frozen identity

**First-party TradingView source:** TheFuturesPlaybook, *ChopFlow ATR Scalp Strategy*, public **open-source strategy** script ID **TgcbEl6W**, originally published **2025-04-30**, updated **2025-05-06** (two same-date release notes: EMA/default one-contract setting and visual annotations). First-party public description inspected **2026-10-28**: https://www.tradingview.com/script/TgcbEl6W-ChopFlow-ATR-Scalp-Strategy/ . Author describes Choppiness Index (CI) below threshold plus OBV above/below its SMA within a custom futures trading session, and ATR-multiple stop/target. Author's suggested settings are ATR(14) ×1.5, CI(14) <60 and OBV SMA(10). The updated release also mentions EMA but does **not** specify its role in the accessible text. Complete Pine source bytes, Pine language version, exact updated EMA rule, original session schedule, exact stop/target fill behavior, order-processing flags and original position rules were **not independently retrievable**; the page's script ID and 2025-05-06 published revision are a source identity, **not** a cryptographic Pine source hash.

**Independently derived strategy, NOT source-native or lossless:** retain only the author-described CI regime, OBV-versus-SMA confirmation and ATR-sized bracket concept. Researcher defines every unverified behavior: Binance BTC-USDT **spot 1h** rather than NQ futures, continuous UTC 24/7 instead of custom exchange session, LONG/FLAT only (disable short), no additional EMA gate, **first-ready edge** rather than every qualifying bar, fixed 0.001 BTC, locked ATR14 ×1.5 symmetric **close-triggered** exit thresholds, optional filter-failure exit, next-completed-bar-close idealized MARKET simulation, 100-bar warmup, 10,000 USDT research cash, explicit fee/ledger and abort rules. These choices change signal events, risk and execution; no source-native equivalence, author endorsement, reported performance, historical Survivor status or real-trading authorization is claimed.

**Immutable derivative identity:** `TV:TgcbEl6W:TheFuturesPlaybook:2025-05-06:public-description | independent-derived-v1:2026-10-28 | BTC-USDT:BinanceSpot:1h:UTC | CI14-lt60-and-OBV-gt-SMA10-first-ready-edge | exit-CI-ge60-or-OBV-le-SMA10-or-frozen-ATR14x1p5-close-bracket | Q0p001-LONG-FLAT | decision-close-next-row-close-MARKET | fee0p001-per-side`. Any changed seed, inequality, state, source, interval, execution, size or risk is a **different** derivative.

**Dedup at main `50f5fb91dec5de4ad9affcdee90c825c33522efb`:** complete nontruncated Git tree shows 413 root-level strategy Markdown records (excluding two READMEs), README static count 413. Ten distributed root records sampled directly have `schema: strategy-research-record-v1` and `hb_ready_status: PASS`; this is **not** a complete 413-file frontmatter audit. GitHub main code search for `TgcbEl6W`, `ChopFlow`, `Choppiness OBV` and `OBV SMA10` returned no identical record; PR search for the source ID/CI+OBV returned none, and the ten open `research/*` PR titles/source bodies were checked. Nearest existing records: BVLabs Alpha Supertrend Vector uses a Supertrend direction flip with CHOP+ADX, BullByte Williams %R uses a W%R cross with CHOP+volume, and Forven OBV uses an OBV-vs-EMA crossover with SMA-price gate. None has **CI14 trending onset AND OBV>SMA10 with frozen ATR14 close bracket**; this is not a trivial parameter retune.

## Hypothesis and exact signal mathematics

The hypothesis is that a *newly established low-choppiness regime* with positive cumulative volume pressure may offer a directional spot entry. Frozen ATR-sized exits test whether the onset is persistent. This is a falsifiable research hypothesis, **not** a profitability claim.

**Input/clock:** exactly one actual Binance BTC-USDT **spot 1h OHLCV** feed, UTC-aligned. Row `t` carries exchange **opening** timestamp `T[t]`; full row is available only at `E[t]=T[t]+3600s`. Require every adjacent `T[t+1]-T[t]=3600`, strictly increasing, no duplicates/gaps, and actual finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, finite `V>=0`. Any missing, stale, malformed, partial, noncontiguous or synthetic row **aborts** the bounded research run before feature dropna/joins; no interpolation, forward-fill, invented price or incomplete candle.

**Researcher-pinned indicators (all calculations deterministic float64 in chronological index order):**
1. `TR[0]=H[0]-L[0]`; for `t>=1`, `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`.
2. `ATR14[13]=sum(TR[0..13])/14`; for `t>=14`, `ATR14[t]=(13*ATR14[t-1]+TR[t])/14` (Wilder RMA). Undefined before 13. A nonpositive or nonfinite ATR at a proposed entry **aborts**, never sets a fictitious bracket.
3. For `t>=13`, `range14=max(H[t-13..t])-min(L[t-13..t])`, `sumTR14=sum(TR[t-13..t])`; `CI14[t]=100*log10(sumTR14/range14)/log10(14)`. If `range14<=0`, `sumTR14<=0` or result nonfinite, abort (no invented CHOP value). CI is undefined before t=13.
4. `OBV[0]=0`; for `t>=1`, `OBV[t]=OBV[t-1]+V[t]` if `C[t]>C[t-1]`, `OBV[t-1]-V[t]` if `C[t]<C[t-1]`, else unchanged. `OBVSMA10[t]=sum(OBV[t-9..t])/10` for t>=9. All volume is actual base-asset volume, never synthetic.
5. `READY[t]=(CI14[t]<60) AND (OBV[t]>OBVSMA10[t])`, strict inequalities. `ENTRY_EDGE[t]=READY[t] AND NOT READY[t-1]`. Equal CI 60 or equal OBV/SMA is **not ready**. The edge detector updates on **all** completed bars, including order-fill bars, but never uses an unfinished bar or sends a signal on a fill bar.
6. Require **100 consecutive completed valid bars** indexed 0..99 for warmup, no orders/positions during warmup; first eligible signal index t=100, starting FLAT/cash=10,000 USDT/BTC=0. The edge at t=100 uses READY[99]. No inherited prior trades.

**FLAT → pending BUY:** at completed signal bar `s>=100`, if `ENTRY_EDGE[s]` and FLAT/no pending, save `entryATR=ATR14[s]` and queue one BUY for next row `s+1`. At `s+1`, issue one MARKET `BUY Q=Decimal("0.001") BTC` against the actual observed row close `Pbuy=C[s+1]`, effective fill time `E[s+1]`, and do not evaluate a new trading decision on this fill bar. On confirmed full fill, require `cash>=Q*Pbuy*(1+f)` with `f=Decimal("0.001")`, debit cash, credit Q BTC, enter LONG and set **frozen** `STOP=Pbuy-1.5*entryATR`, `TARGET=Pbuy+1.5*entryATR`. Require `0<STOP<Pbuy<TARGET`; otherwise abort rather than invent levels. If no `s+1` exists, pending order is **unfilled** and excluded; no terminal synthetic execution. Unexpected partial/failed fill, insufficient cash, wrong side or unknown fee aborts; do not assume a fill.

**LONG → pending SELL:** on each completed bar `t` **strictly after** confirmed BUY fill row, evaluate one OR predicate: `CI14[t]>=60` OR `OBV[t]<=OBVSMA10[t]` OR `C[t]<=STOP` OR `C[t]>=TARGET`. If true, queue a SELL of the full confirmed Q for the **next** row `t+1` at its actual close `Psell=C[t+1]`, effective time `E[t+1]`; the first matching reason is recorded with priority STOP, TARGET, CI, OBV (priority is diagnostic only; exactly one SELL). Thresholds are **close-triggered decisions**, not intrabar stop/limit orders; prices can gap beyond them, so no guaranteed 1.5×ATR loss bound. On confirmed full SELL, credit `Q*Psell*(1-f)`, debit Q BTC, clear STOP/TARGET/entryATR, return FLAT; no new signal on the SELL fill bar. A pending SELL at the sample end has no invented fill; the remaining position is marked at the actual final close and separately reported as unrealized.

**Re-entry, state and disabled behaviors:** only FLAT, PENDING_BUY, LONG, PENDING_SELL; at most one action and one position. READY is updated on all valid completed rows, so a subsequent entry requires a **fresh false→true edge**, even if a bracket exit occurred while READY stayed true. No cooldown beyond that edge, no simultaneous exposure, pyramiding, scale-in/out, DCA, safety orders, partial exits, compounding, leverage, margin, borrow, futures funding, short, hedging, intrabar trigger, trailing, discretionary session gate, original EMA filter, forced end-of-run liquidation or implicit Hummingbot risk default. Opposite short signal never opens a short. No hidden order placed on the same decision row.

**Numerical accounting:** cash/inventory/fees use Decimal and confirmed full-fill prices/amounts. Each BUY debits `Q*Pbuy*(1+f)`; each SELL credits `Q*Psell*(1-f)`. Matched gross PnL `Q*(Psell-Pbuy)`; fee `f*Q*(Pbuy+Psell)`; net = gross − fee. Use the exact configured Decimal Q as inventory authority and verify against confirmed executor fill quote/price; `BacktestPositionHold` float dust is not a state transition. Diagnostic reconciliation tolerances max `1e-12 BTC` and `1e-8 USDT` (never round a signal, create a fill or conceal a discrepancy). Require full terminated-executor ledger and fail closed on reconciliation mismatch. Mark an open terminal position at real last C, with no invented SELL or realized PnL.

## Pinned Hummingbot Gate 5 path — connector source inspection

**Engine identity:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0` (VERSION directly fetched). Pinned source inspected **2026-10-28** via GitHub Connector: `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `hummingbot/strategy_v2/executors/order_executor/data_types.py`. Prior Alpha PR #414 reports **902/902 wheel/source byte identity**, but this cycle **did not recheck installed wheel bytes/image**. No candidate-specific executable controller or test was created.

- **Feed:** pinned BinanceSpotCandles parses actual REST kline row[0] opening timestamp and row[1..5] OHLCV, with `1h` interval support. All CI/OBV/ATR features need only this single contiguous completed feed. Reject gaps before `prepare_market_data` can drop missing feature rows.
- **Controller:** pinned `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, then `simulate_executor`. A future minimal dedicated controller (NOT implemented) maintains the four frozen states and dispatches queued action **only on the following row** using `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1))`. No action uses a future price in its decision.
- **Fill semantics:** pinned `OrderExecutorSimulator.simulate(MARKET)` fills at the **first supplied row's actual `close`**, records the row's **opening timestamp**, computes `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*amount_quote`, and returns `POSITION_HOLD`. Dispatching on `s+1` deliberately produces **one-bar-delayed historical close fills**, effective causal fill time `T[s+1]+3600`; never confuse raw open-time label with availability or claim real-world after-close execution at that historical close.
- **Positions:** pinned `BacktestPositionHold` nets opposite fills but can carry float residual dust. Separate confirmed-fill Decimal cash/BTC ledger governs FLAT/LONG; reconcile against engine executor fill and fee values with the above tolerances, and retain all terminated executors (`terminated_executors_window=None` or equivalent).
- **Costs:** explicitly pass `run_backtesting(trade_cost=0.001)` — **hypothetical** 0.1% per filled side, not verified historical Binance fee tier. Simulator has no additional modeled spread/impact/latency slippage; this is an idealized limitation, **not** evidence that realized slippage was zero. Spot has no perpetual funding liability; do not fabricate zero observed futures funding. No futures margin or liquidation model is used. Live tick/lot/min-notional acceptance is **not verified**.
- **Price safety:** pinned `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` for missing price; explicitly forbid this fallback. Require actual positive finite row close for every order/mark, otherwise abort. No maker, limit queue, next-open, intrabar high/low stop fill, multi-asset synchronization or unverified external data path is required.

## Six-gate Scout evidence — independent review pending

1. **Determinism:** frozen TR/ATR14 Wilder seed, CI14 window/log formula, OBV initial condition and SMA10, strict READY edge, fixed close bracket, fee and state priorities; no fitted model or ambiguous parameter.
2. **Direction:** explicit Binance BTC-USDT spot LONG/FLAT, shorts and futures disabled; original NQ futures/session path not asserted.
3. **Entries/exits/risk:** edge-triggered BUY; close-triggered frozen stop/target and CI/OBV invalidation SELL; all omitted risk/session/EMA behaviors expressly disabled, no hidden default.
4. **Position/DCA:** exact Q/cash, single position/pending order, full-fill-only transitions, no DCA/pyramiding/concurrency, no cooldown, fresh READY edge for re-entry.
5. **Pinned model:** directly inspected actual 1h Binance REST feed, controller/action sequence, delayed-row MARKET actual-close fill, POSITION_HOLD/fee ledger, bounded Decimal reconciliation and missing-price guard; unsupported live/futures/intrabar semantics excluded.
6. **Causality:** 100 complete-bar warmup, signal at E[s], next-row idealized fill at E[s+1], first exit decision after fill row, no lookahead, repainting, future pivots, unclosed higher-timeframe or fabricated price.

## Evidence limits and later falsification

**Source-reported only:** author/date/script ID, CI/OBV confirmation and ATR-multiple bracket concept, recommended parameter values, futures session and subsequent EMA release note. **Researcher-defined:** all precise indicator seeds, ready edge, spot/timeframe, disabled short/session/EMA, fixed close-based risk, filter-failure exit, next-row fill, cash/fee/position and failure semantics. **Independently reproduced results: none.** No Pine source-event parity, Hummingbot/Qlib backtest, empirical return, OOS, Survivor, HB Certified, Paper/Testnet/Live or deployment is claimed.

Future falsification (NOT performed): CI log/range equality and zero-range abort, OBV tie/zero-volume seed, READY edge across fill bars, ATR freeze, stop/target equal close, simultaneous invalidation priority, insufficient cash, rejected/partial fills, last-row pending order, delayed timestamp labeling, missing-price fallback, fee/Decimal residual reconciliation and terminal unrealized inventory. Before large-scale Qlib screening, reuse only verified execution primitives; any new execution capability requires one representative HB↔Qlib event-level parity validation.

**Sources:** TradingView first-party https://www.tradingview.com/script/TgcbEl6W-ChopFlow-ATR-Scalp-Strategy/ ; pinned Hummingbot source https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 ; prior wheel/source evidence https://github.com/HCH725/alpha-strategy-research/pull/414 .

**Adoption boundary:** `hb_ready_status: PASS` here is a **Scout research admission claim for independent Auditor review**, not independent approval. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. Only Hermes Auditor GitHub Webhook Review may remediate source facts, merge an exact-head PASS or close NOT_LOSSLESS. Only the existing signed webhook receiver may reconcile README after a confirmed merge.
