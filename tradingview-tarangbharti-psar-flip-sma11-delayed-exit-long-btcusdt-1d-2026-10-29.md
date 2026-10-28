---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "tarangbharti18 PSAR up-flip entry with PSAR-down AND SMA11 delayed exit — independently derived BTC-USDT spot 1d long-flat"
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
source_as_of: 2025-08-06
sources:
  - https://id.tradingview.com/script/4wpplfPo-Parabolic-SAR-with-Early-Buy-MA-Based-Exit-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PSAR up-flip with SMA11-gated delayed exit — independent research derivative

## Provenance

- **First-party TradingView publication:** *Parabolic SAR with Early Buy & MA-Based Exit Strategy*, **tarangbharti18**, public script **4wpplfPo**, published **2025-08-06**, first-party page inspected **2026-10-29**: https://id.tradingview.com/script/4wpplfPo-Parabolic-SAR-with-Early-Buy-MA-Based-Exit-Strategy/ . The author says a long starts on a **Parabolic SAR reversal**, the bullish zone has SAR below price, and an existing long exits **only when SAR is above price AND price is below an 11-period SMA**. The author explicitly calls the original SAR implementation *custom* and says the method can be used on multiple instruments/timeframes. The page labels the script open-source, but retrievable public HTML does **not** expose complete Pine bytes, source revision/hash, custom SAR recursion, initialization, exact price comparisons, fill flags, sizing, commissions or performance evidence.
- **Independent derivative, NOT a lossless/source-native Pine port:** The author does not supply the complete PSAR calculation in accessible prose. This record **researcher-defines** a standard Wilder-style, two-bar-seeded SAR recursion, initial trend, strict candle-close price gates, BTC-USDT spot UTC **1d**, fixed **0.001 BTC**, starting **10,000 USDT**, **120-bar** warmup, idealized completed-close MARKET fills, **0.1%/side modeled fee**, no SL/TP/DCA, no exchange lot/tick filter and explicit pending/fill state. The source's original *custom* SAR must **not** be claimed equivalent to the standard SAR below. The **SMA11 AND SAR-above-price delayed-exit conjunction** and **PSAR reversal entry** are source-reported; all exact arithmetic, initialization, market, timing, sizing, costs and disabled behavior below are researcher choices. A second similarly titled author page exists under script ID f0EqNMhP; **4wpplfPo alone** is this immutable primary-source identity, not an interchangeable revision.
- **Frozen derivative identity:** `TV:4wpplfPo|tarangbharti18|2025-08-06|independent-derived-v1:2026-10-29|BinanceSpot:BTC-USDT:UTC1d|WilderSAR:seedC1>=C0-up:AF0.02:step0.02:max0.20:prev2-clamp|enter:DOWN-to-UP-and-SAR<C|exit:SAR>C-and-C<SMA11|LONG-FLAT|Q0.001BTC|cash10000USDT|fee0.001-per-side|idealized-MARKET-completed-close|warmup120|no-stop-target-DCA`. Any altered rule is a new strategy revision, not an undisclosed optimization.

## Economic mechanism

**Source-reported:** A bullish PSAR flip seeks early trend participation; an unfavorable PSAR reading alone does **not** force a long exit. The close must also fall below SMA11, intentionally delaying exits during short-lived PSAR reversals. This can reduce churn but can also hold a deteriorating long. No source performance number is accepted as reproduced.

**Research hypothesis:** A PSAR flip may mark momentum change; the SMA11 conjunction is a delayed exit filter. Unlike simple PSAR stop-and-reverse or PSAR+EMA entry filters, this derivative buys **only on a DOWN→UP SAR state transition**, then stays LONG through a bearish PSAR state until **both** bearish SAR price location and the SMA11 close test are satisfied. No claim of profitability, survivor status or deployability.

## Signal

**Gate 1 — exact, deterministic researcher-defined SAR and SMA:**

1. One real Binance **BTC-USDT spot 1d** chronological OHLCV sequence indexed `t=0,1,...`, aligned to UTC midnight. Binance exchange `T[t]` is the **candle OPEN timestamp** in seconds; the completed `O,H,L,C,V` becomes available only at `E[t]=T[t]+86400`. Require finite positive prices, `L<=min(O,C)<=max(O,C)<=H`, finite nonnegative base volume, and exactly consecutive 86400-second opening timestamps. Reject duplicates, gaps, malformed bars and missing prices. No synthetic OHLCV or fill price.
2. SAR parameters are researcher-fixed `AF_init=0.02`, `AF_step=0.02`, `AF_max=0.20`. On the **second** valid bar of a contiguous segment (index 1), set `trend[1]=UP` if `C[1]>=C[0]`, else `DOWN` (ties are UP). For UP: `SAR[1]=min(L[0],L[1])`, `EP[1]=max(H[0],H[1])`. For DOWN: `SAR[1]=max(H[0],H[1])`, `EP[1]=min(L[0],L[1])`. Set `AF[1]=0.02`. This is a **declared independent initialization**, not a recovered original Pine default.
3. For every `t>=2`, compute provisional `p=SAR[t-1]+AF[t-1]*(EP[t-1]-SAR[t-1])`. If previous trend UP, clamp `p=min(p,L[t-1],L[t-2])`. If previous trend DOWN, clamp `p=max(p,H[t-1],H[t-2])`. All comparisons use completed candles, never an unfinished current candle.
4. If previous trend UP and `L[t]<=p`, **reverse to DOWN**: `trend[t]=DOWN`, `SAR[t]=EP[t-1]`, `EP[t]=L[t]`, `AF[t]=0.02`. Otherwise stay UP: `SAR[t]=p`; `EP[t]=max(EP[t-1],H[t])`; `AF[t]=min(0.20,AF[t-1]+0.02)` only if `H[t]>EP[t-1]`, otherwise preserve AF. No second reversal within the same bar.
5. If previous trend DOWN and `H[t]>=p`, **reverse to UP**: `trend[t]=UP`, `SAR[t]=EP[t-1]`, `EP[t]=H[t]`, `AF[t]=0.02`. Otherwise stay DOWN: `SAR[t]=p`; `EP[t]=min(EP[t-1],L[t])`; `AF[t]=min(0.20,AF[t-1]+0.02)` only if `L[t]<EP[t-1]`, otherwise preserve AF. A reversal is decided from the *prior* trend only, so ambiguous intrabar high/low order never causes two reversals.
6. `SMA11[t]=(C[t-10]+...+C[t])/11` on **11 completed consecutive** bars, including the current completed close. Undefined before index 10. No rounding of indicator inputs or intermediate SAR/MA values; evaluate deterministic float64 arithmetic in the stated sequence. On a missing/invalid bar reset the entire SAR/SMA recursion and re-warmup, never backfill.
7. **Entry event** at eligible completed bar `t`: `trend[t-1]==DOWN && trend[t]==UP && SAR[t]<C[t]`. All predicates are required; an upward PSAR flip with `SAR==C` does not enter. This is an **edge**, not a perpetual bullish-state re-entry.
8. **Exit event** at eligible completed bar `t`: `SAR[t]>C[t] && C[t]<SMA11[t]`. Both are strict **levels**; either equality is HOLD. An unfavorable PSAR reading by itself is not an exit. An exit signal from FLAT does nothing. Entry and exit are mutually exclusive due to opposite SAR-versus-close signs; no intrabar high/low stop order is submitted.
9. **Warmup / causality:** the first **120 valid consecutive completed bars** of each segment are indicator-only; segment index 120 (121st completed bar) is first eligible. A data gap pauses all decisions, restarts the 120-bar warmup and SAR seed, but **never** fabricates a liquidation of an existing BTC position. Already-held BTC remains in the ledger during a gap; decisions resume only after re-warmup. No negative shift, forward extrema, lookahead, future session values, incomplete bar or fitted model.

**Gates 2–4 — directions, entries/exits, risk and state:**

10. Binance BTC-USDT **spot LONG/FLAT only**. Begin FLAT, cash `10000 USDT`, base `0 BTC`. When FLAT and an eligible entry event fires, issue exactly **one** `MARKET BUY 0.001 BTC` at the **actual observed decision bar close** in the explicitly idealized historical simulator, provided `cash >= 0.001*C[t]*(1+0.001)`; otherwise skip that event and remain FLAT. Do not queue/retry a skipped BUY without a **fresh future UP-flip**.
11. When LONG and an eligible exit event fires, issue exactly **one** `MARKET SELL 0.001 BTC` at that same completed close; on confirmed full simulated fill return FLAT. While an order is pending, issue no additional action; controller state must be reconciled to the simulator's terminated `POSITION_HOLD` fill before permitting another order. A missing, non-finite or inconsistent fill is a **hard stop of the research replay**, not an invented rejection, partial fill, alternative price or new signal. No simultaneous opposite orders.
12. At most one 0.001 BTC long, one pending order, one market and one strategy. **No shorts, borrowing, futures, margin, leverage >1, funding, pyramiding, DCA/safety orders, averaging, partial sizing, trailing, fixed SL/TP, intrabar stop/limit, maker orders, cooldown, time exit, discretionary risk overlay or forced sample-end liquidation.** Re-entry requires a new DOWN→UP flip after returning FLAT, never a standing UP state. If the sample ends LONG, mark remaining 0.001 BTC with the last **observed valid** close and do not fabricate a SELL. The absence of a stop is intentional and can permit severe drawdown.
13. **Historical fill scope explicitly bounded:** this derivative models **fractional, full-size, idealized close-price fills** in the pinned Hummingbot simulator, **without historical exchange tick/lot/min-notional rejection filters**. It does not claim to represent exchange-accepted live orders, historical exchange filter snapshots, partial fills, spread or latency. In particular, it does **not** make unspecified historical Binance precision/minimum filters a hidden eligibility condition; if real exchange filter compliance becomes a requirement, it is a **different, unverified engine/economic path** requiring separate evidence, not assumed here.

## Required data

One real, contiguous UTC Binance spot BTC-USDT **1d** OHLCV stream; H/L/C determine SAR, C determines SMA, O and V are validated for integrity. No other pair, secondary timeframe, portfolio state, tick/book, order-flow, funding, mark/index, external calendar or synthetic price. Exact open timestamp `T` and close-availability time `E` must be retained separately. Missing price is not replaced with 0, 1, prior close or an interpolated value.

## Execution assumptions

**Gate 5 — pinned Hummingbot capability path inspected via connected GitHub on 2026-10-29:**

- Policy package **`20260920`**, VERSION **`dev-2.17.0`**, immutable source **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. Directly read `hummingbot/VERSION`; `setup.py` still says `20260729` (not the policy package label). Previously independently audited Alpha [PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414) reports wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148` and 902/902 shipped Python files byte-matched. This Scout **did not independently rehash wheel bytes**; Auditor must validate applicability of that prior evidence, or fail Gate 5.
- Directly inspected `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (supports `1d`) and `binance_spot_candles.py::_parse_rest_candles` (Binance `row[0]` **open** time, `row[1..5]` real O/H/L/C/**base volume**). `BacktestingDataProvider.get_candles_df` reads a keyed connector/pair/interval feed. Preprocess real bars to carry both original `T[t]` and **effective completed time** `E[t]=T[t]+86400`, and feed the engine's event timestamp and aligned controller features at `E[t]`; never treat `T[t]` as close availability or use a later bar's data in an earlier decision.
- Directly inspected `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution/prepare_market_data/update_state`: it advances historical rows, calls `determine_executor_actions()`, processes `CreateExecutorAction`, and routes filled `POSITION_HOLD` orders into `BacktestPositionHold`. The hold's `_process_order` nets a SELL against an earlier BUY and accumulates realized **gross** price PnL; `cum_fees_quote` is separate. Controller must account for the one-row delayed visibility of just-created executor fills via explicit pending state.
- Directly inspected `hummingbot/strategy_v2/executors/order_executor/data_types.py`: `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET branch fills at the **first supplied historical row's actual close**, with `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*notional`, and `CloseType.POSITION_HOLD`. Proposed dedicated controller uses this **existing** single-pair completed-close execution path, not an unverified next-open/maker/intrabar executor.
- **Pinned research economics:** `trade_cost=0.001` each filled side (0.1% of executed quote notional, a **hypothesis**, not a verified Binance historical fee). Initial `Decimal("10000")` USDT cash; BUY debit `Decimal("0.001")*actual_close*(1+Decimal("0.001"))`; SELL credit `Decimal("0.001")*actual_close*(1-Decimal("0.001"))`. Reconcile modeled cash/BTC and `BacktestPositionHold` gross fills and separately accumulated fees; quantity residual > `1e-9 BTC` or quote cash/fee residual > `1e-8 USDT` stops replay. No fee-free net-PnL claim. Additional modeled slippage is **zero only as an idealized simulator assumption**, not a statement about actual spreads/latency. Funding and liquidation are **inapplicable to unleveraged spot**, not silently set to zero on futures.
- `BacktestingDataProvider.get_price_by_type` contains a `Decimal("1")` fallback on missing prices; this derivative **forbids that path** for fill/mark/PnL. Require real finite observed `close` in the supplied row, else stop. The simulator does not model historical lot/tick/min-notional filters or exchange-accurate partial fills; those are explicitly outside this **research-only** derivative. No dedicated strategy controller was built or deployed; `implementation_status: not-implemented` is intentional. Reuse the independently reviewed single-spot-market MARKET-close/POSITION_HOLD primitive from Alpha PRs #414 and #572, rather than pretending this is a new experimental replay.

## Evidence

**Source-reported:** TradingView `4wpplfPo` by tarangbharti18, dated 2025-08-06, reports PSAR reversal long entry and a **conjunctive** exit when SAR is above price and price below SMA11. It describes a custom PSAR calculation; its exact source formula was **not** retrieved. The derivative does **not** attribute its SAR seed, recursion, execution, sizing or fee to the author.

**Independently reproduced:** **No strategy backtest, Pine reproduction, live order, Qlib replay or event-level parity was performed**. Only first-party source facts, GitHub pinned Hummingbot source capability paths, repository policy and prior reviewed engine evidence were inspected. No source or derived win rate, return, Sharpe, MDD or Survivor claim is made.

**Dedup and admission preflight:** At stable pre-write `main` SHA `646a93b0297808f8b86f495a0850a1784c22262c`, the complete GitHub tree enumerated **416** root strategy Markdown records and README displayed **416**. Twelve evenly spaced frontmatter samples were directly checked, all `hb_ready_status: PASS`; this is **not** a full 416-file status audit. GitHub main search for `4wpplfPo`, `f0EqNMhP`, `tarangbharti18` and `PSAR SMA11` found no strategy record; all open `research/*` PRs were enumerated and none cites this source or the exact PSAR-up-flip plus **SAR-above-close AND close-below-SMA11** delayed-exit machine. Nearest existing `forven-parabolic-sar-cross-long-flat` and `psar-flip-stop-reverse` use **PSAR alone** for exit/reversal, not this conjunctive SMA11 delay; `eterna-parabolic-sar-ema50-filtered-reversal` uses a **trend entry filter** and two-sided reversal, not an SMA11 exit gate. A bare PSAR up-flip or a different PSAR parameter set alone is not claimed novel.

## Limitations and six-gate conclusion

1. **Gate 1:** PASS **for this independently specified derivative only**; fully pinned SAR seed, recurrence, EMA-free SMA11, strict tests, and deterministic data invalidation. The source's custom SAR is **not** proven equivalent.
2. **Gate 2:** PASS; BTC-USDT unleveraged spot LONG/FLAT, shorts disabled.
3. **Gate 3:** PASS; up-flip entry, conjunctive delayed exit, and all absent SL/TP/trailing/time legs explicitly disabled. No protection against indefinite adverse holding.
4. **Gate 4:** PASS; one 0.001 BTC position, cash/fee ledger, pending fill reconciliation, fresh-flip re-entry, no DCA/concurrency/cooldown. No unspecified historical exchange filter gates.
5. **Gate 5:** **Scout-submitted PASS claim subject to independent Auditor verification** of pinned package-to-source evidence and actual completed-close MARKET/POSITION_HOLD/cost accounting. Historical exchange precision, spread and live fills are outside the frozen idealized model, not silently asserted compatible. Any missing required engine path is a **NOT_LOSSLESS** blocker.
6. **Gate 6:** PASS; 120-bar warmup, close-effective timestamp alignment, prior-two-bar SAR clamp, completed-bar only, gap reset, no lookahead or fabricated prices.

**HB_READY is only model-consistent research admission**, not profitability, Qlib parity, historical exchange execution fidelity, Survivor or Paper/Testnet/Live authorization. Representative Qlib/Hummingbot event-level parity is required before mass screening any newly introduced execution primitive; this candidate proposes none. No system, container, backtest, trading or schedule changes are authorized.
