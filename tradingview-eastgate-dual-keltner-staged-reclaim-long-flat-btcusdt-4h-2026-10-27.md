---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Eastgate dual-Keltner outer breach to inner reclaim, BTC-USDT spot 4h (independent derivative)
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-03-23
sources:
  - https://www.tradingview.com/script/M6YPrmR2-Dual-Keltner-Channels-Strategy-Eastgate3194/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Eastgate dual-Keltner staged reclaim — independent BTC-USDT spot 4h derivative

## Provenance and immutable identity

- **TradingView public primary source:** eastgate3194, *Dual Keltner Channels Strategy [Eastgate3194]*, published **2025-03-23**, stable TradingView script ID **M6YPrmR2**, directly inspected 2026-10-27: https://www.tradingview.com/script/M6YPrmR2-Dual-Keltner-Channels-Strategy-Eastgate3194/
- **Source-native facts actually verifiable in the public page text:** two nested Keltner channels are used for countertrend trading. A LONG has two *ordered* steps: (1) close crosses **under outer lower** Keltner band; (2) close crosses **over inner lower** Keltner band. The source also describes mirrored SHORT steps: close crosses over outer upper, then under inner upper. The page labels the script open-source.
- **Source-access boundary:** the original Pine code, input defaults, indicator smoothing, order timing, exits, sizing, pyramiding, cooldown and fee rules were **not** visible in the accessible page text. None of those facts is asserted as source-native or silently guessed. No original Pine trade-event parity or lossless reproduction is claimed. The page's two-step mechanism, rather than an invented source implementation, is the only native fact adopted.
- **Immutable derived identity:** `TV:M6YPrmR2 | eastgate3194 | published:2025-03-23 | independently-derived:v1:2026-10-27 | Binance BTC-USDT spot | UTC 4h | EMA20/Wilder-ATR14 inner1.5 outer2.5 | outer-breach arm, inner-reclaim entry | basis/2ATR/20bar close exits | one 0.001 BTC long | next-bar-close idealized fills`. Any changed parameter, rule, cost or clock is a *different* derived revision.
- **Researcher-defined changes (not the author's Pine):** all channel lookbacks/multipliers and seeding; the BTC-USDT spot/4h market and long-only stance (original describes short too); arm lifetime; basis/ATR/time exits; fixed quantity, no DCA or concurrency; bar-close-only decisions and next-bar-close historical fills; warmup; research fee/cash ledger. Every decision-critical alteration is defined below. This record is independently derived, not an adaptation misrepresented as source-native.
- **Dedup at main SHA `7c9d91d8b34f70f79b14d5f60c21b8eaa77bb22c`:** root-level strategy count 383 equals README count 383. GitHub main searches for `M6YPrmR2`, `eastgate3194` and `two-stage keltner` returned no source identity; the 10 open research/* PRs contained none. Closest admitted Keltner mechanisms are FMZ momentum-gated **outer breakout** (`keltner-momentum-breakout-gated`), Forven ADX-gated **outer breakout** (`forven-keltner-adx-gated-breakout`), and Eterna one-bar **lower-band touch plus reclaim with EMA50 gate** (`eterna-keltner-20-10-2p0-pullback-reclaim`). This record instead requires a **persistent two-stage state** (outer-lower *close crossunder* followed on a later bar by inner-lower *close crossover*) and exits on **upperward basis recovery** or fixed close-risk/time conditions. Neither a mere parameter variation nor the Eterna same-bar touch trigger. Count equality alone is not a complete 383-file PASS-frontmatter audit.

## Economic mechanism

**Source-reported:** an overshoot below the wider volatility envelope arms a countertrend opportunity; recovery above the narrower envelope triggers a long (short mirror described but disabled in this derivative). No source performance or source-native risk/economic claim is adopted.

**Research interpretation:** a two-step overshoot/recovery state machine avoids buying the first downward band break; the separate inner-band reclaim is the confirming event. It can miss fast V-shaped reversals or remain exposed to further declines. No return, win-rate, or Sharpe forecast is made.

## Signal — complete independent derivative v1

All prices are **real observed completed Binance BTC-USDT spot 4h OHLCV bars**; index `t` is a completed UTC-aligned 4h bar. Required values must be finite, positive where applicable, and timestamp-contiguous. Reject the research run rather than interpolate missing bars or substitute a synthetic price.

1. **EMA20:** `B[0]=C[0]`; for `t>=1`, `B[t]=(2/21)*C[t]+(19/21)*B[t-1]`. No adjusted/window EMA or later re-seeding.
2. **True range:** `TR[0]=H[0]-L[0]`; `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))` for `t>=1`. **Wilder ATR14:** `A[13]=mean(TR[0..13])`; `A[t]=(13*A[t-1]+TR[t])/14` thereafter; undefined before index 13. If `A[t]<=0` at a decision, fail closed rather than arm/enter on collapsed bands.
3. **Channel:** `outerLower[t]=B[t]-2.5*A[t]`, `innerLower[t]=B[t]-1.5*A[t]`. The upper bands and SHORT are not used. All comparisons use unrounded source prices and current/previous **completed** bars.
4. **Outer breach:** `breach[t]=(C[t-1]>=outerLower[t-1]) AND (C[t]<outerLower[t])`. Strict current-side crossunder; equality on previous side qualifies, current equality does not.
5. **Inner reclaim:** `reclaim[t]=(C[t-1]<=innerLower[t-1]) AND (C[t]>innerLower[t])`. Strict current-side crossover; previous equality qualifies.
6. **Flat/unarmed → armed:** on a qualifying `breach[a]` after warmup, store `arm_bar=a`. **No order** at arm. While armed, ignore further breach events (do not reset the clock). Evaluate reclaim on **subsequent** bars `a+1..a+12` inclusive; a reclaim outside this window cannot enter. If no reclaim by the end of `a+12`, clear arm. A fresh breach is then required on a later completed bar.
7. **Armed → pending BUY:** on the first `reclaim[t]` inside the arm window, clear arm and emit exactly one BUY intent for **next completed bar `t+1`**. Ignore all signals while pending. If that bar's real close is missing/nonpositive or fill/account constraints fail, abort the research run rather than manufacture a fill. Confirm one `0.001 BTC` long at observed `C[t+1]`; set `entry_price=C[t+1]`, `entry_atr=A[t+1]`, `entry_bar=t+1`. If entry ATR is invalid, abort.
8. **Long exit decision:** only from completed bar `j>=entry_bar+1`, in priority order: **(a)** close-risk `C[j]<=entry_price-2*entry_atr`; **(b)** basis recovery `C[j]>=B[j]`; **(c)** time limit `j-entry_bar>=20`. Equality triggers these level conditions. The first true condition emits exactly one SELL intent for the **next completed bar `j+1`**; hold the long and suppress all other signals while pending. The close-risk rule is a **bar-close signal**, not an intrabar protective stop or guaranteed loss cap. The basis condition is a level-hold condition, not a crossover requirement.
9. **Pending SELL → flat:** sell the entire confirmed base position at observed `C[j+1]`; record fee and realized net economics, clear position and pending flags. No entry on the same bar as a fill. A **new** outer breach on a later completed bar is mandatory for re-entry; no fixed cooldown. If no next bar exists, leave an explicitly open position at the sample boundary and report mark-to-market separately, not a fabricated exit.
10. **Collision and disabled behaviors:** flat/armed/long/pending are mutually exclusive states; exit priority is risk > basis > time; no same-bar entry+exit, short, reversal, pyramiding, safety order/DCA, trailing order, exchange-native SL/TP, stop-limit, maker, intrabar high/low trigger, discretionary/manual override, cross-asset exposure, capital compounding, session filter, or hidden controller default. One concurrent position maximum, one pending order maximum. A canceled arm has no exposure. Invalid input or unresolved partial fill fails closed.

## Required data, warmup and point-in-time clock

- One instrument, **Binance spot BTC-USDT**, UTC 4h, 4h bars with actual open/high/low/close/volume and unique strictly increasing 4h open timestamps. Validate `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, `O,H,L,C>0`; reject gaps, duplicates, non-finite values or missing observed close. Volume is feed provenance, **not** a signal gate.
- **100 complete bars** of warmup (indices 0..99); initial arm/entry decisions only at `t>=100` after previous band values exist. This includes ATR seed and prior-bar crossover. All pre-warmup states are flat/unarmed. No future extremes, look-ahead, negative shifts, higher-timeframe unfinished bars, global fitting, or repainting.
- Binance REST Kline `row[0]` / Hummingbot candle `timestamp` is the **bar OPEN**, not its close. For 4h bar `t`, decision inputs become available only at `E[t]=open_ts[t]+14400 seconds`. The intent from completed `t` cannot execute earlier than `E[t+1]` using the actual next bar close. Native executor row timestamps must be normalized to this economic availability/fill clock. No source next-open parity is claimed.

## Execution assumptions — inspected pinned Hummingbot engine

**Pinned source benchmark directly inspected via connected GitHub (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, repository `hummingbot/VERSION=dev-2.17.0`, repository policy package `20260920`. Source pin is verified; an installed wheel/container image digest is **not** independently rehashed in this Scout. Relevant exact paths at that commit:

- `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` supports `4h` (verify interval availability before materialization); `binance_spot_candles.py::_parse_rest_candles` maps Binance REST `row[0]` to opening timestamp and `row[1..5]` to OHLCV. Only actual observed rows are allowed.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, then `CreateExecutorAction` simulation. A **future candidate-specific** controller (not yet implemented) must preserve arm/pending/position state, dispatch on the intended `t+1` row, and never consume `C[t+1]` at decision `t`.
- `hummingbot/strategy_v2/executors/order_executor/data_types.py` declares `OrderExecutorConfig` and `ExecutionStrategy.MARKET`. For this research lane the candidate controller must issue `connector_name=binance`, `trading_pair=BTC-USDT`, `side=BUY/SELL`, `amount=Decimal("0.001")` (SELL the actually held quantity), `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. No generic API name alone establishes candidate implementation.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py::simulate`: MARKET selects the first supplied row; the actual `df_filtered.loc[fill_timestamp,"close"]` is the modeled fill, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, `CloseType.POSITION_HOLD`. Thus dispatch on `t+1` yields an **idealized t+1 close fill**, not an actual exchange order guaranteed to fill there. No invented next-open, intrabar path or queue fill.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::BacktestPositionHold` nets confirmed opposite-side base quantities and separately accumulates `cum_fees_quote`; its realized PnL is **gross**. Maintain complete confirmed-fill history and explicit cash/inventory net ledger. For BUY at `Pb`, `cash-=0.001*Pb*(1+f)`; SELL at `Ps`, `cash+=0.001*Ps*(1-f)`; round-trip realized net `=0.001*(Ps-Pb)-f*0.001*(Pb+Ps)`. Do not label engine gross PnL net. Preserve full history (do not silently prune fills needed for state).
- **Research cost pin:** `f=0.001` quote-notional per side, a **hypothetical** 0.1% fee, not a verified Binance account tier. The pinned MARKET historical close-fill simulator does not reproduce spread, liquidity, latency, partial fills or live slippage; **no assertion that actual slippage equals zero**. If these are required for a different claim, the path is not verified and cannot be silently substituted. Spot funding is **not applicable** (not a fabricated zero perpetual funding). No leverage, borrowing, interest, liquidation or perpetual settlement model.
- **Fail-closed:** `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py::get_price_by_type` can return `Decimal("1")` when the price key is absent. This fallback is explicitly forbidden; require observed positive close and exchange trading-rule/precision/min-notional validation before any simulated fill. Do not assume a market-size quantum, fee tier, execution liquidity or realized fill. If those validations or exact book state cannot be established, block execution/qualification rather than invent economics.

## Evidence and six-gate assessment (proposal; independent Auditor owns PASS review)

1. **Determinism:** exact EMA seed, Wilder TR/ATR seed, 20/14/1.5/2.5 band arithmetic, strict cross inequalities, 12-bar arm expiry, priority and frozen v1 identity.
2. **Direction:** Binance BTC-USDT **spot LONG/FLAT**; the source's short mirror is explicitly disabled, not described as lossless.
3. **Entry/exit/risk:** ordered two-stage entry, fixed ATR-entry close-risk, basis level exit and 20-bar time exit, with no unmentioned intrabar/protective orders.
4. **Position/re-entry:** fixed one 0.001 BTC long, single pending intent, no DCA/pyramiding/short, full state transition and rearm rule; no compounding or cooldown.
5. **Pinned engine:** exact GitHub commit/version, real Binance spot candle parser, `CreateExecutorAction` → MARKET first-row actual close, `POSITION_HOLD` base ledger and separately modeled quote fees, spot-only economics; explicitly blocked missing-price/precision/partial-fill paths. Future candidate controller not yet materialized.
6. **Causality:** 100 completed 4h warmup bars, `E[t]` close-availability time, `t` signal → `t+1` close model fill, no future bar data in signal, no intrabar ordering ambiguity.

**Source-reported performance:** none. **Independently reproduced strategy performance, Pine parity, Qlib/Hummingbot event parity, installed-image identity, OOS, Survivor or HB Certified:** none. The direct inspection here is a bounded engine-source capability check, not a backtest. A candidate-specific controller and strict market-data validator remain future implementation work, not a second HB_READY gate.

## Falsification plan and limitations

If separately authorized, implement only the minimal candidate-specific controller on the pinned path; test exact stage timing and expiration (including equality), bar-close availability, ATR seed, gap rejection, next-close fill, open-end mark-to-market, cash/inventory/fee ledger and trading rules. Obtain representative Qlib/Hummingbot event-level parity for any newly unverified execution primitive before large-scale Qlib screening. No such implementation, test, trading or deployment is authorized by this record. No profitability or live-trading approval is implied.
