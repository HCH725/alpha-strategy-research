---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView Yesid fractional EMA sequential 13/48.5/200 crossover — independent BTC-USDT spot 4h long-flat derivative"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/adstHm9N/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fractional EMA sequential three-stage trend entry — independent long-flat derivative

## Provenance

- **Primary TradingView source:** [Fractional EMA Cross Backtest Strategy](https://www.tradingview.com/script/adstHm9N/), author **Yesid_Correa_Cano**, stable script identity **adstHm9N**, publicly listed as an **open-source strategy**. Direct public listing read on **2026-10-25**; its relative publication label displayed **"2 days ago"** on that check (approximately 2026-10-23, **not** an independently verified absolute publication timestamp). The page description was readable; complete Pine source, source-revision hash and exact Pine-language version were **not** accessible from the public page view. These unavailable original-code facts are not represented as verified.
- **Source-native mechanism supported by the author's text:** configurable fractional-period EMA via alpha = 2/(length+1), a **sequential** three-EMA long entry: fast crosses above intermediate to arm; a later intermediate-above-slow crossover triggers; crossing back through fast/intermediate before completion cancels the pending setup. A two-EMA mode and mirror-image shorts also exist. The author describes next-available-tick/usually next-open fills, 10%-equity position allocation, $0.10 fixed commission/order, no pyramiding, fill-anchored stop and 3.5R target, and 30-session maximum hold. No native trade-level equivalence is claimed here.
- **THIS RECORD IS A SEPARATELY SPECIFIED DERIVED STRATEGY, NOT A LOSSLESS REPRODUCTION.** It freezes a three-EMA-only, long/flat, same-completed-bar-close, fixed-base-quantity, crossover-exit variant. It removes the author's fill-anchored SL/TP and time exit; it replaces source equity allocation and flat order fee with the research model below. Its EMA seed, equality, ordering, warmup, venue, timeframe, cancellation, close behavior, costs and account ledger are explicitly **researcher-defined**, not inferred Pine defaults.
- **Immutable candidate identity:** `TradingView:adstHm9N | independent-derivative:v1 | Binance-spot:BTC-USDT:4h | EMA(close;13,48.5,200;first-close-seed) | staged-long-entry | fast-under-intermediate-exit | fixed-0.001-BTC | close-fill | warmup-600 | fee-0.001-per-side`. Any material change to this frozen specification requires a separately disclosed revision; the TradingView script ID identifies lineage, not immutable Pine bytes.

## Economic mechanism

### Source-reported

The original sequential three-EMA mode waits for a fast/intermediate bullish crossover and then for a later intermediate/slow bullish crossover; the intermediate step is intended to distinguish staged trend formation from a one-bar simultaneous crossover. The unusual fractional length allows a smoothing constant between those of adjacent integer EMAs. This is the author's described trading hypothesis, **not** evidence of positive net returns.

### Research interpretation

The independent long/flat variant asks whether staged acceleration from EMA13 over EMA48.5 followed by EMA48.5 over EMA200 yields a distinct BTC spot trend-entry mechanism, and whether a fast/intermediate bearish cross supplies a deterministic trend-decay exit. Unlike a conventional simultaneous two-EMA crossover or static EMA-stack filter, the **ordered, cancelable arming state** is essential to this candidate. No profitability, risk-adjusted return or source-native trade matching is asserted.

## Signal

**All rules below are the complete, frozen DERIVED decision contract.** Inputs are one consecutive UTC-aligned Binance spot BTC-USDT **4h** candle stream, with finite positive `O,H,L,C`, nonnegative `V`, unique open timestamps `T[t]` separated by exactly **14,400 seconds**. A candle is usable only after its close time `T[t]+14400`. All comparisons are strict unless written otherwise; no forward-filled missing candles, synthetic prices, or partial-bar signals.

1. **Fractional EMA arithmetic and preprocessing (research-defined seed).** For `n` in `{13.0,48.5,200.0}`, `alpha(n)=2/(n+1)`; `E_n[0]=C[0]`; `E_n[t]=alpha(n)*C[t]+(1-alpha(n))*E_n[t-1]` for `t>=1`, using full floating-point arithmetic without intermediate rounding. Denote `F=E_13`, `M=E_48.5`, `S=E_200`. The fractional 48.5 is **not** rounded to 48 or 49; there is no EMA/SMA library substitution. This seed and exact length triple are researcher pins; the author's page provides the alpha formula and an example 13/48.5/200 combination, not this complete execution configuration.
2. **Warmup.** Compute all three EMA states from the first contiguous bar, but **do not trade or arm** during indices `0..599` inclusive. At the start of index `600`, state is explicitly `FLAT, unarmed` regardless of pre-warmup crosses. First eligible comparison is `t=600` against `t-1=599`. If any candle is missing/invalid or a 4h gap occurs, **stop decisions** until a new 601-consecutive-bar run is available, then restart the EMAs from that run's first close, and restart `FLAT/unarmed` only after an actual flat book is established; never silently erase or liquidate an existing holding. A held position on feed loss enters **NO-NEW-ACTIONS** until data is restored and state reconciled; no invented forced fill.
3. **Cross predicates:** `up(A,B,t) := A[t-1] <= B[t-1] AND A[t] > B[t]`; `down(A,B,t) := A[t-1] >= B[t-1] AND A[t] < B[t]`. Exact equality at `t` is not a cross. Values are evaluated once per confirmed bar. No multi-timeframe or intrabar inspection.
4. **Flat-state arming.** At each eligible completed bar while flat, retain `armed_at` (integer index or NONE). If already armed and `F[t] <= M[t]`, **cancel** `armed_at` before checking an entry (the explicit equality cancellation is researcher-defined). If a previously armed setup survives, and `t > armed_at`, `up(M,S,t)` and `F[t]>M[t]`, **BUY 0.001 BTC** and clear the arm. Otherwise, if flat and `up(F,M,t)`, set `armed_at=t`. The second-stage cross on the **same bar** as first-stage arming is ignored; a subsequent fresh M/S upward cross is required. An M/S cross that occurred before arming is ignored. The arm has no time expiry, but is cancelled on `F<=M`; there is no late entry without the second cross.
5. **Long-state exit.** If long and `down(F,M,t)`, **SELL the full actual 0.001 BTC research position** at the modeled completed-bar close and return to `FLAT, unarmed`. No same-bar re-arm/re-entry on an exit bar. Otherwise HOLD. A long position never creates another buy. No short or reversal orders.
6. **Decision priority:** existing LONG exit > previously armed FLAT cancellation > previously armed FLAT second-stage entry > new FLAT first-stage arm > HOLD. Orders are modeled as fully filled on the same eligible completed-bar close, with at most one action per bar. No stop loss, take profit, trailing, time stop, signal-based scale-out, partial TP, hedging, pyramiding, DCA/Safety Orders, discretionary overrides, hidden executor default exit, or forced end-of-history liquidation. These are **intentionally disabled derived behaviors**, not assertions about the original Pine.
7. **Capital state:** research starting ledger is **10,000 USDT cash / 0 BTC**, no deposits, leverage, borrowing, or concurrent markets. BUY is allowed only if modeled available USDT covers `0.001*C[t]*(1+0.001)`; if insufficient, skip that BUY, clear the arm, remain FLAT, and await a **new** full two-stage sequence. SELL releases the held base quantity and its modeled net proceeds. All fills use fixed base quantity 0.001 BTC, never 10% equity; no compounding or fractional safety orders. A rejected/unfilled order is **not** treated as an executed state transition; this model is a full-fill research assumption only, not a claim of live execution reliability.

## Required data

- Only Binance spot BTC-USDT OHLCV **4h** candles and their **open timestamps**, transformed into **close-available** rows. The trading formula reads **close only**; O/H/L/V are for source-row validity, not signal conditions. No external signals, order book, funding, mark/index price, lower timeframe, multi-asset alignment, ML fit, or lookahead data.
- Availability: raw kline open `T`; final `C[t]` and calculated EMAs become available at `T+14400` **after confirmation**. Normalize the decision/backtest row timestamp to `T+14400` (UTC) and never evaluate the still-forming candle. If the underlying feed/backtest alignment cannot enforce this rule, the run is invalid rather than implicitly allowed to peek ahead.
- A 600-bar warmup plus one previous EMA observation is required. The frozen no-trade boundary is `t<600`, with no trading across missing data or unconfirmed feed gaps.

## Execution assumptions

**Gate 5: pinned source/data/executor compatibility; research expressibility only, NOT implementation or real fills.**

- **Identity:** policy package **`20260920`** and in-package `hummingbot/VERSION=dev-2.17.0`. The immutable source inspected through the GitHub connector for this record is **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. In this cycle the pinned `hummingbot/VERSION`, Binance spot candle files, `backtesting_engine_base.py` and `order_executor_simulator.py` were directly read. The already-admitted `forven-adx-trend-di-cross-long-flat-btcusdt-1d-2026-10-25.md` on main documents a separate byte-level package-to-commit match: wheel `hummingbot-20260920-cp312-cp312-macosx_11_0_arm64.whl`, SHA-256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`, metadata package `20260920`, embedded VERSION `dev-2.17.0`, and **902/902** Python files matched to that immutable commit. **That wheel was not independently rehashed in this cycle; the mapping is cited existing evidence, not inferred from VERSION or an API name.**
- **Market/feed:** pinned `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` supports `4h` and `/api/v3/klines`; `binance_spot_candles.py` maps REST row 0 to the open timestamp and rows 1–5 to OHLCV. Research connector/pair `binance` / `BTC-USDT`, spot, 1×, LONG/FLAT; no perpetual, margin, short borrow or funding. The strategy-specific completed-bar gate and timestamp normalization in Required data must be implemented explicitly: merely selecting `4h` does **not** prove causal availability.
- **Controller/feature path:** pinned `strategy_v2/backtesting/backtesting_engine_base.py` calls `controller.determine_executor_actions()` per processed feature row, dispatches `CreateExecutorAction`, and tracks `BacktestPositionHold`. `prepare_market_data()` uses backward `merge_asof`, which is **not by itself** a guarantee against leaking incomplete bars. A minimal dedicated strategy controller (currently **not implemented**) can calculate only past/current completed EMA rows, track `FLAT/LONG/armed_at/cash`, normalize timestamps, and create one `OrderExecutorConfig` MARKET action per state change. The controller must use its own immediate filled-order ledger, not the potentially delayed `positions_held` view, to avoid duplicate actions. This is a strategy-specific materialization, **not** a proposed generic compiler or new framework.
- **Fill semantics:** pinned `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` for `ExecutionStrategy.MARKET` fills on the first supplied row timestamp, uses **that row's `close`** as `entry_price`, sets `filled_amount_quote = Q*close`, `cum_fees_quote = trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. On the normalized close-time row this supports the explicitly **idealized same-completed-bar-close research fill**. It does **not** demonstrate next-bar-open, maker queue, bid/ask, partial fills, live latency, exchange precision or intrabar TP/SL sequencing; this derivative requires none of those paths.
- **Research economics and accounting:** pass `trade_cost=0.001` per executed BUY and SELL, i.e. a **modeled 0.1% of quote notional per side**, NOT the author's native $0.10/order. On BUY at `P_b`, debit `Q*P_b*(1+0.001)`; on SELL at `P_s`, credit `Q*P_s*(1-0.001)`. A completed round trip has gross PnL `Q*(P_s-P_b)`, two fees `0.001*Q*(P_b+P_s)`, and net PnL = gross minus those fees. Mark an open 0.001 BTC holding at the last valid close, with the entry fee retained as a cost. The pinned `BacktestPositionHold` separately accumulates `realized_pnl_quote`, `cum_fees_quote`, `net_amount_base` and `avg_entry_price`; do not present `net_pnl_quote` or gross realized PnL as fee-inclusive equity without the explicit fee adjustment. **Spot funding is inapplicable**, not an assumed observed zero. Extra simulated spread/slippage is **not modeled**, not evidence of zero actual execution cost. Historical exchange fees, lot/tick/min-notional validation, liquidity, partial fills and settlement cash balances are not independently observed or certified for live orders.
- **No new engine primitive:** reuse the same independently admitted single-pair Binance spot 4h, completed-candle MARKET-close / POSITION_HOLD / fee-ledger capability cited in current main's TradingView research records and PRs #421/#423/#424/#425. The novel part is the **deterministic, cancelable three-EMA arming state**, which is controller logic, not a new feed, fill type, market or executor capability. This is an expressibility argument grounded in the inspected pinned code and existing distribution binding, **not** a performed Hummingbot strategy backtest or Qlib/HB parity test.

## Evidence

### Source-reported

The author's accessible TradingView page explicitly states fractional EMA smoothing `2/(length+1)`, a sequential 3-EMA entry, arming/cancellation behavior, example lengths 13/48.5/200, long/short options, pyramiding 0, next-tick fill convention, risk-percent sizing, 3.5R target, fixed per-order commission, and 30-session timeout. It does **not** establish this derivative's BTC-USDT 4h close-fill, 0.001 BTC size, 0.1% modeled per-side fee, no SL/TP, fast/intermediate exit, 600-bar warmup, or first-close EMA seed: those are independently declared research decisions.

### Independently reproduced

**Not independently reproduced.** No Pine execution, backtest, Hummingbot/Qlib run, order fill, profitability statistic, source trade matching or event-level parity was performed. The pinned GitHub source **was read** to verify the claimed engine primitives; the previously reviewed package/commit mapping is referenced rather than recomputed. The six-gate determination here is research-stage expressibility for the fully specified **derived** rule, subject to independent Hermes Auditor verification before any merge.

### Negative evidence

The TradingView public listing view did **not** expose the complete Pine source or immutable revision. Therefore source-native trade equivalence, the original script's exact internal EMA initialization and its historical next-open/stop/target behavior cannot be asserted. The derived specification deliberately does not depend on those unverified facts. Neither TradingView Strategy Tester statistics nor source-reported PnL are presented as reproduced evidence. No futures funding or actual spot execution data was collected.

### Six-gate evidence matrix

1. **Determinism:** frozen EMA13/48.5/200 recurrence, alpha, first-close seed, equality and cross definitions, 600-bar warmup, gap behavior, arming/cancellation/priority and capital checks in Signal.
2. **Direction:** BTC-USDT **spot LONG/FLAT** only; shorts, futures and leverage explicitly disabled.
3. **Entry/exit/risk:** staged F/M then M/S entry, F/M bearish-cross exit; SL/TP/trailing/time/intrabar/risk overlays explicitly disabled as derived changes, with no hidden default.
4. **Position/state:** single fixed 0.001 BTC holding, one action/bar, no pyramiding/DCA/concurrency, explicit arm, cancel, exit, insufficient-cash, re-entry and no-automatic-liquidation states.
5. **Pinned engine/data/cost:** exact wheel identity and previously reviewed wheel-to-commit evidence; this cycle's direct pinned-code inspection of Binance 4h feed, controller action loop, MARKET close-price fill, POSITION_HOLD ledger and per-fill `trade_cost`; explicit modeled spot cash, fees, fill and timestamp limitations. No unsupported execution primitive is silently assumed.
6. **Causality:** completed 4h bars, close-available timestamps, 600-bar warmup, backward-only EMA recurrence, no future bars, no unconfirmed higher-timeframe or intra-candle input, and declared idealized close-fill timing. Unenforced timestamp normalization blocks an actual run rather than permitting leakage.

## Falsification plan

- **Order-state distinctiveness:** compare frozen staged/cancelable 13/48.5/200 entries with a simultaneous EMA-stack or simple F/M crossover under the **same** modeled fill/cost/warmup convention. If event lists coincide except trivial startup effects, this candidate is not materially distinct and should be consolidated rather than counted as a new strategy.
- **Causal integrity:** deliberately insert a missing 4h candle and a same-bar first/second crossover; verify the former blocks new actions and the latter does **not** enter. Confirm no `T+14400` signal is emitted at raw `T`.
- **Ledger integrity:** on a controlled sequence, check at most one 0.001 BTC open holding, one BUY/SELL per edge, two 0.1% side fees, no phantom shorts, and cash/position reconciliation. These are future test cases, **not tests executed now**.
- **Downstream boundary:** when selected for Qlib mass screening, materialize a minimal strategy-specific executable recipe and reuse verified primitives; representative Qlib/Hummingbot event-level parity is required before any **new execution path** is mass-screened. The final survivor/HB certification later requires its own event/economic verification. Do not use OOS feedback to retune this frozen candidate.

## Crypto portability

The EMA ratios are in price units and the sequential-cross mechanism does not require a market session. This **particular identity** is only BTC-USDT spot 4h; other assets, periods, two-sided futures, alternate fees, house DCA/3×/5× overlays, or 1h/1d experiments are separate, explicitly declared derivatives or downstream research runs. None is an HB_READY entry prerequisite. No claim of stable behavior across markets is made.

## Limitations

- **Independent derivative, not lossless Pine.** Original next-tick fills, risk-sized stop/target, time exit, shorts and $0.10 commission were intentionally replaced/disabled. The author's description is primary evidence of the *idea*; this record is the fully frozen executable research variant.
- A same-close fill is an idealized pinned-simulator convention; market-close information and close fill coincide only in this declared research model. It is not a promise of attainable live fills.
- No source Pine hash, full Pine code, original performance replication, Qlib parity, spot fill observations, lot-size validation, actual spread/slippage or profit evidence.
- A dedicated controller and causal timestamp-normalization code are **not implemented**. A downstream run that lacks them is invalid, not implicitly HB_READY-certified execution.
- Fixed-quantity exposure and absence of protective stops may produce severe drawdowns; this is a research hypothesis, not a recommendation or risk-controlled deployment.

## Implementation status

**Not implemented.** This Markdown is an admission-stage, source-backed research specification only. No strategy controller, Qlib implementation, Hummingbot run, MLflow output, Paper/Testnet/Live trade or deployment is produced. Materialization is separate downstream engineering work after selection, not a second admission gate.

## Adoption boundary

**Research-only; not approved for adoption, capital allocation or trading.** `hb_ready_status: PASS` here is a proposed six-gate expressibility assessment for the **derived** contract, **not** independent Auditor approval, profitability, Qlib parity, Survivor, HB Certified or live permission. Hermes Auditor independently reviews the exact PR head before any possible merge; failures remain outside main.

## Related Wiki records

None claimed. No private Wiki Brain content or user account data is included.

## Sources

- https://www.tradingview.com/script/adstHm9N/ — Yesid_Correa_Cano, *Fractional EMA Cross Backtest Strategy*, public open-source listing read 2026-10-25; relative publication label "2 days ago" at read time; full Pine bytes unavailable.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned source, directly inspected 2026-10-25; specifically `hummingbot/VERSION`, `hummingbot/data_feed/candles_feed/binance_spot_candles/{constants.py,binance_spot_candles.py}`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`.
- https://github.com/HCH725/alpha-strategy-research/blob/18dfc58ab9c67b3cac6d622609e1b0ee455b827f/forven-adx-trend-di-cross-long-flat-btcusdt-1d-2026-10-25.md — existing independent wheel/commit identity evidence (902/902, package 20260920), reused, **not** rehashed this cycle.
- https://github.com/HCH725/alpha-strategy-research/pull/425 — existing independently reviewed 4h spot close-fill primitive reference; no claim of this candidate's own execution.
