---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Patterns morning/evening star body-ratio reversal — BTCUSDT spot 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/OqjKbuRp-Patterns-Strategy-v1/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Patterns morning/evening star body-ratio reversal — BTCUSDT spot 1d independent derivative

## Provenance

- **Primary TradingView source:** dipalishah94, *Patterns Strategy v1*, published **2026-09-17** (`<time dateTime="Thu, 17 Sep 2026 06:58:01 GMT">`), public **open-source strategy** ID **OqjKbuRp**, page directly fetched and read as of **2026-10-26**: https://www.tradingview.com/script/OqjKbuRp-Patterns-Strategy-v1/. The publicly retrievable author description is the source of the source-reported facts below. The full Pine text, its revision, and its immutable code hash were **not retrieved**; do not assert lossless Pine equivalence, original TradingView fills, or original backtest metrics.
- **Frozen independent derivative identity:** `TV:OqjKbuRp:dipalishah94:2026-09-17 | independent-derived-v1:2026-10-26 | morning-star-35/55/50-completed-trio-entry | evening-star-35/55/50-completed-trio-exit | no-gap-rule | BinanceSpot:BTC-USDT:1d:LONG-FLAT:Q0.001BTC:close-effective-MARKET:trade_cost0.001:20bar-warmup`.
- **Source-native descriptive facts:** a price-action pattern strategy detecting four setups (bullish/bearish engulfing, Morning Star long setup, Evening Star short setup), each producing an entry trigger, stop loss and profit targets. **Morning Star:** three-candle pattern — strong bearish first candle, small-body middle candle, strong bullish third candle recovering at least the configured penetration percentage of the first candle's body; defaults: middle-candle body `≤ 35%` of its range, outer-candle bodies `≥ 55%`, third-candle penetration `50%`; entry above the third candle's high; SL below the entire three-candle pattern; targets `1.5R / 2R`. **Evening Star:** the stated reverse (strong bullish first, small middle, strong bearish third penetrating the first body; entry below the third low; SL above the pattern; `1.5R / 2R`). **Two entry modes:** Stop Order (resting order at the breakout trigger) and Market on Break (enter on the next bar after the break); an entry buffer in ticks is also described. No verified source-native warmup length, sizing, cost model, or Pine default-order settings were recovered.
- **Researcher-defined changes, not source facts:** this separately identified strategy freezes the inclusive comparators (`<= 0.35`, `>= 0.55`, `>= 50%` midpoint recovery), allows either star-candle color (the source states "small-body middle candle" with no color requirement), requires no inter-candle gaps (the source states no gap rule at all, so no gap adaptation is needed), trades only Binance BTC-USDT spot on UTC `1d`, enforces LONG/FLAT with one 0.001 BTC unit, simulates completed-close MARKET fills instead of the source stop-order / next-bar-break entries, **disables** the source pattern-low SL and `1.5R/2R` targets (intrabar, unmodelable on the pinned close-simulation primitive) and instead exits LONG only on a completed Evening Star trio, explicitly disables the source short setups, sets 20 contiguous completed-bar warmup, gives exits priority, and defines data-failure and re-entry semantics. These changes may alter source-native trade events and economics (notably the removed downside protection). This record is **not** an admission claim for the author's original Pine program.

Pre-write duplicate check against the actual `main` tree at `db657deed4eec299a2153b7615091d693162bac33`, repo-wide grep and the ten open `research/*` PRs: no record or open PR with TradingView script ID `OqjKbuRp`, author `dipalishah94`, or this immutable derived identity. The only `Morning Star` mention in `main` is a passing reference inside `wick-reversal-hammer-shooting-star-long-flat-btcusdt-1d-2026-10-16.md` to the closed October-15 Scout PR **#220** (`research: TA-Lib morning-star evening-star gap-penetration flip two-sided on BTCUSDT 1d`, closed NOT_LOSSLESS): that PR used TA-Lib `CDLMORNINGSTAR/CDLEVENINGSTAR` gap-penetration semantics with a perpetual two-sided flip, while this derivative uses the unrelated TradingView body-ratio arithmetic (35/55/50, no gaps), spot LONG-FLAT only, and an evening-star close exit with no reversal — materially different source, mechanism, market and position model, not a reopen or paraphrase. The `alorse-bb-winner-lite-candle-penetration-long-20261016.md` "penetration" is a Bollinger-band zone rule, not a three-candle star pattern. The ten open `research/*` PRs (Heracles KCD, ClucMay72018, AdxSmas, forven CCI, Swift 2yMA, SSL channel, Chandelier Exit, SuperTrend flip, Gauss StochRSI, Larry Williams streak) contain no star-pattern rule.

## Economic mechanism

### Source-reported

A three-candle Morning Star (long directional bar, small star bar, confirmation bar recovering half the first body) is presented as a bullish reversal setup; the Evening Star mirror is presented as a bearish reversal setup. Breakout triggers above/below the pattern with pattern-extreme stops and `1.5R/2R` targets frame the described payoff. These are hypotheses, not demonstrated profits.

### Research interpretation

This derivative buys a *completed* body-ratio Morning Star trio and holds until a *completed* body-ratio Evening Star trio. It is neither a single-candle wick trade nor a moving-average system. Because the source SL/targets are disabled, a continued decline after entry may leave the long position exposed indefinitely; the only risk control is the opposite-pattern close exit.

## Signal

Let `O[t], H[t], L[t], C[t]` be a **fully completed** UTC daily OHLC bar with positive finite `C[t]` and `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]>0`. For any bar `b`, `body(b)=|C-O|`, `range(b)=H-L`; any trio bar with `range<=0` forces both predicates false (no division by zero). Require at least twenty contiguous completed validated bars before trading (the trio need is three; twenty is the independently declared conservative warmup).

1. **Entry predicate `M[t]`** on completed trio `(t-2, t-1, t)`: `C[t-2]<O[t-2]` AND `body(t-2)/range(t-2)>=0.55` AND `body(t-1)/range(t-1)<=0.35` (star color unrestricted; a doji star with ratio `0` qualifies) AND `C[t]>O[t]` AND `body(t)/range(t)>=0.55` AND `C[t]>=(O[t-2]+C[t-2])/2` (50% penetration = close at or beyond the first-body midpoint). A doji first or third candle fails its strict color comparison, so zero-body outer candles can never trigger; this is arithmetic, not a special case.
2. **Exit predicate `E[t]`** on completed trio `(t-2, t-1, t)`: `C[t-2]>O[t-2]` AND `body(t-2)/range(t-2)>=0.55` AND `body(t-1)/range(t-1)<=0.35` AND `C[t]<O[t]` AND `body(t)/range(t)>=0.55` AND `C[t]<=(O[t-2]+C[t-2])/2`.
3. `M[t]` and `E[t]` are **mutually exclusive by construction**: they require opposite strict colors of the shared first candle (`C[t-2]<O[t-2]` vs `C[t-2]>O[t-2]`); a doji first candle satisfies neither. Fuzz-verified over 20,000 random trios with zero joint triggers. On a valid completed bar, process **EXIT before ENTRY** as a standing rule (moot under exclusivity, binding if inputs ever change).
4. Direction and state: only `FLAT` or `LONG(0.001 BTC)`, initially FLAT. If LONG and `E[t]`, issue one full-quantity SELL. Else if FLAT and `M[t]`, issue one BUY. Otherwise hold. Never short; no pyramiding, scaling, averaging, BO/SO, DCA, reverse orders, hedges, or simultaneous position/executor exposure. An entry predicate while LONG is a no-op; an exit while FLAT is a no-op. Re-entry is allowed on a **future completed bar** with a fresh eligible entry predicate only after SELL fill confirmation. No cooldown, no pending limit orders. At most one outstanding MARKET action; never infer a fill from mere order submission.
5. No stop-loss, take-profit, trailing stop, maximum holding period, forced end-of-sample liquidation, equity-based sizing, leverage, margin, funding payment, or session/date restriction. These are **explicitly disabled researcher decisions** (the source SL/targets need intrabar fills the pinned primitive cannot model), not asserted Pine defaults. Unclosed positions at the predetermined research end remain marked open and must not be represented as realized PnL.

## Required data

- One Binance **spot** market `BTC-USDT`, interval `1d`, UTC day boundary, `open/high/low/close` and original candle-open timestamp. No volume, external security, order book, trades, futures funding, mark/index price, higher/lower timeframe, ML model, shared capital, or portfolio synchronization is used.
- Each exchange candle's timestamp labels its **OPEN**, not its completed-close availability. Define `decision_ts[t] = candle_open_ts[t] + 86400` seconds; use the completed candle only when all its OHLC values are available. Feed prepared engine rows with the effective **completed-close timestamp**, never the original open timestamp for decision or simulated fill. Check monotonicity and exactly contiguous 86400-second UTC daily opens.
- The first **20** fully completed, contiguous, validated bars are warmup-only and cannot trigger orders. No centered windows, future extrema, negative shifts, incomplete daily bar, full-sample preprocessing or repainting.
- A missing, nonfinite, nonpositive or inconsistent OHLC, absent completed close, zero-range trio bar, timestamp gap, or unsorted bar blocks that bar's trio decisions **and fill**. Do not synthesize candles or substitute a prior price. Resume decisions only after 20 new contiguous valid completed bars; an existing LONG stays open during the gap, with no fictitious stop/exit or fee. A pending unconfirmed order must be reconciled from its real simulated fill ledger before any further action; never invent completion. Such gaps can prolong unprotected exposure.

## Execution assumptions

**Pinned baseline:** Hummingbot package label `20260920`, `hummingbot/VERSION = dev-2.17.0`, pinned `HCH725/hummingbot` source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly fetched and read these pinned files at that commit (not an unpinned online API or current main):

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` — `_parse_rest_candles` reads REST `row[0]` as the **open timestamp** (`ensure_timestamp_in_seconds(row[0])`) with OHLC values; `.../constants.py` explicitly supports interval `1d`.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` — `BacktestingEngineBase.simulate_execution` loops row-wise over timestamped prepared rows (`for i, row in processed_features.iterrows()`), calls `controller.determine_executor_actions()`, and routes each `CreateExecutorAction` to the executor simulator with the forward slice **starting at the current row** (`processed_features.loc[i:max_ts]`); `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60*60` seconds; `BacktestPositionHold` nets same-pair BUY/SELL average-cost, realized gross PnL and cumulative quote fees.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` — `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, BUY/SELL, base amount 0.001 fills at the **first supplied row's close** (`fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close at fill_timestamp`), records `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, then reports `CloseType.POSITION_HOLD`. Together with the current-row forward slice, a completed-close signal at `decision_ts` produces a same-effective-timestamp MARKET-close **simulation** on that prepared row. This is the actual pinned close-effective **backtest** primitive, not an exchange close auction, a next-open fill, a stop-order break, or an intrabar fill. The researcher-defined controller would be a strategy-specific `DirectionalTradingController` emitting these actions; **it is not implemented or deployed**.

**Critical fill/position-state setting:** instantiate `BacktestingEngineBase(terminated_executors_window=None)` so the controller can see fill-confirmed executors on subsequent daily decisions. The pinned default is only 3600 seconds and may hide the previous daily fill from `controller.executors_info`; the engine still has an internal stopped ledger. Maintain explicit controller-side fill-confirmed quantity, pending-action suppression, and position cost/fee ledger; never equate `POSITION_HOLD` with a fresh unfilled order or assume an order was filled when submitted. This model convention does **not** establish causal executable live close fills. A future execution path that cannot honor the same effective-timestamp model must be revalidated as a distinct derivative.

**Cost and capital:** research `initial_quote_cash=10000 USDT`, fixed `amount=0.001 BTC`, `trade_cost=0.001` of quote notional **per simulated BUY and SELL fill**, modeled slippage `0` as an expressly artificial simulation assumption. Do not describe this 0.1% as a measured exchange fee or the zero modeled slippage as realized slippage. Require sufficient simulated cash including modeled BUY fee; if not, no BUY. SELL only confirmed available base quantity. Unleveraged spot has no perpetual-futures funding contract; **no claim of zero realized futures funding** is made. Actual maker/taker schedules, lot/tick rounding, min notional, spread, latency and partial fills are not verified and are not authorized for Paper/Testnet/Live. Model net realized quote PnL as `BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote`, **not** the gross-only executor PnL field. No fabricated prices or fills. Float rounding residuals must not create a second position.

The existing independently reviewed **PR #414** documented a wheel/source mapping for this pinned source family; the wheel-to-commit binary hash was **not revalidated in this Scout cycle**. Gate 5 relies on the directly inspected pinned code path and the existing reviewed evidence, not a claim of fresh wheel-byte identity or an implemented controller. No futures/margin/shared-capital/new data primitive is needed.

## Evidence

### Source-reported

TradingView `OqjKbuRp`, dipalishah94, 2026-09-17: four-pattern strategy (bullish/bearish engulfing, Morning Star long setup, Evening Star short setup); Morning Star three-candle rule with middle body `≤35%` of range, outer bodies `≥55%`, penetration `50%`; entry above third-candle high, SL below the pattern, `1.5R/2R` targets; Evening Star mirror; Stop Order and Market-on-Break entry modes with tick buffer. No sizing, warmup, cost or Pine default-order settings recovered. Public page marks the script open-source, but full Pine code/revision bytes were not retrieved.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen `M[t]`/`E[t]` inequalities plus the FLAT/LONG state machine were executed over hand-constructed boundary trios and 20,000 seeded random trios: exact-`0.55`/`0.35`/midpoint-equality trios fire; strictly-below-threshold trios do not; doji outer candles never trigger while a doji star is allowed; zero-range/inconsistent/nonpositive bars block without exceptions; the walk `BUY → hold-through-repeat → SELL → noop` holds; `M` and `E` never co-fire. **Engine-code inspection only, not a strategy backtest:** pinned Hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was read file-by-file for the Binance spot `1d` candle parser (open-timestamp rows), the row-wise engine action loop with current-row forward slices, MARKET-first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, `hummingbot/VERSION` and 3600-second vs `None` terminated-executor visibility. The candidate's trade events, TradingView Pine outputs, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

- No full Pine revision or Pine default-order/commission setting is available from the retrieved source page; **source-native/lossless equivalence is unverified**. The independent derivative is evaluated against its own frozen rules only.
- Closed Scout PR #220 used TA-Lib gap-penetration two-sided flip semantics on perpetual markets — a different source, different arithmetic (gaps vs body ratios), different market and position model; it is not this candidate and does not validate it.
- No verified stop-order break fill, live close fill, partial fill, market impact, exchange fee schedule, futures funding or venue order-size permission. None is silently imputed.

## Falsification plan

1. Hand-construct completed daily OHLC trios for body ratios at `0.549/0.55`, `0.35/0.351`, penetration just below/at midpoint equality, wrong-color and doji outer candles, doji and oversized stars, and zero-range trio bars. Verify trigger/no-trigger, strict first-candle color exclusivity, and exit-before-entry ordering.
2. Check warmup bars 1–20, missing/invalid OHLC, nonmonotone/gapped timestamps, FLAT/LONG/pending order transitions, fill-ledger persistence across 86400 seconds, and no same-bar re-entry after a SELL.
3. If formally selected downstream, build the minimal strategy-specific controller/recipe and validate **representative event-level Qlib/Hummingbot parity for this execution primitive** before broad Qlib screening if that primitive has not already been independently validated. Compare timestamp, signal, action, confirmed fill, quantity, fee and position-cost state. A model capability failure is an engineering hold, not a retroactive profitability or admission decision. No performance/Sharpe/OOS claim is made here.

## Crypto portability

Only `BTC-USDT` Binance spot `1d` is pinned in this research record. Other assets, timeframes, market types, and the downstream seven-coin × three-timeframe × leverage/DCA research campaign are **separate experiments**, not HB_READY admission requirements or silently equivalent original source behavior. Applying BO/SO overlays or futures economics changes this frozen trade-event/economic model and requires an explicitly declared derivative.

## Limitations

- A Morning Star trio can print repeatedly through a crash; without SL/TP/time stop this strategy can hold through substantial adverse moves, and the source downside protection was deliberately removed as unmodelable.
- The source short setups, stop-order/next-bar-break entries, tick buffer, pattern-extreme SL and `1.5R/2R` targets are not reproduced; entries/exits happen at the simulated trio-completion close, which changes events versus any original Pine configuration.
- Exact source Pine revision, source-native fill clock, original sizing/cost settings and profitability are unknown. The simulated completed-close fill is a **backtest convention**, not a live execution guarantee.
- The modeled 0.1%-per-side research cost, zero modeled slippage, fixed base size and absence of futures funding do not prove actual Binance trade economics. A long position can remain exposed during data outages. No Qlib parity, survivor status or trading approval follows from HB_READY.

## Implementation status

`not-implemented`: no candidate-specific controller, Qlib executable artifact, backtest, deployment, Paper/Testnet/Live run or position exists. The pinned Hummingbot MARKET/POSITION_HOLD **capability** is demonstrated; candidate implementation and reproducible replay remain future downstream work, not a second admission gate.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, subject to an **independent Hermes Auditor GitHub Webhook Review** of this exact PR head. Only that reviewer may remediate source-verifiable facts, exact-head merge on six-gate PASS, or close the Scout PR as NOT_LOSSLESS. No autonomous adoption, order placement, Qlib/Hummingbot execution, or README edit.

## Related Wiki records

None created or modified. Future research may link an existing Hermes Wiki Brain record after independent approval; this PR changes only this one root-level strategy record.

## Sources

1. https://www.tradingview.com/script/OqjKbuRp-Patterns-Strategy-v1/ — dipalishah94, *Patterns Strategy v1*, published 2026-09-17; primary descriptive strategy rules, inspected 2026-10-26.
2. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py — pinned MARKET fill and fee path.
3. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py — pinned row loop, current-row forward slice, position/cost ledger and terminated-executor visibility.
4. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py — pinned Binance spot open-timestamp OHLC parser.
5. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py — pinned `1d` interval.
6. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION — pinned `dev-2.17.0`.
7. https://github.com/HCH725/alpha-strategy-research/pull/414 — previously reviewed package/source identity evidence; **not** a fresh binary hash verification.
