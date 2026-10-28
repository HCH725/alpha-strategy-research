---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "simwai RSI14+MFI14 dual-oversold simultaneous-rise long-flat — independent BTC-USDT spot 1h derivative"
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
source_as_of: 2026-10-29
sources:
  - https://www.tradingview.com/script/FP2kd7Fo-Fusion-MFI-RSI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dual-oversold RSI14 + MFI14 rising together, long-flat — independently specified derivative

## Provenance and immutable strategy identity

**Primary public TradingView source:** *Fusion MFI RSI*, author **simwai**, posted **2024-06-12**, public script ID **FP2kd7Fo**, directly read **2026-10-29**: https://www.tradingview.com/script/FP2kd7Fo-Fusion-MFI-RSI/ . The public page marks it open-source, but the accessible text did **not** expose the Pine source bytes or a revision hash; this record does not assert byte-verification, a Pine-version number, source-native execution equivalence, or an independently reproduced backtest.

**Source-native facts bounded to what the page actually says:** the author discusses RSI and volume-weighted MFI, both commonly 14-period; RSI oversold/overbought **30/70**, MFI **20/80**; MFI uses typical price (H+L+C)/3 and typical-price-signed volume. In the page's explicitly labeled *Fusion Application / Trading Rules*, the author **suggests** a long when **both RSI and MFI are below their oversold thresholds and start rising**, and an exit when **either reaches its overbought threshold**. The same page also discusses optional Hann/JMA/T3/Super Smoother, IFT, weighted fusion and short-side ideas; it does **not** unambiguously pin an executable Pine order strategy, exact RSI initialization, a smoothing selection, weights, fill timing, venue, stake, or risk controls. Its phrase “could be calculated” is not an exact executable fusion formula. No source performance is claimed.

**Explicit independent derivative (not source-native Pine):** implement the author's separately stated **raw RSI/MFI two-oscillator long idea** without any weighted fusion, IFT, Hann, JMA, T3, Super Smoother, or short-side logic. Researcher pins Wilder RSI14 initialization, 14-bar MFI arithmetic and denominator handling, the precise meaning of “start rising” (both strictly higher than their own previous values **on the same completed bar**), strict oversold thresholds, inclusive overbought exits, single BTC-USDT Binance spot UTC-1h stream, a 100-bar warmup, fixed 0.001 BTC, no protective orders or additions, and **t signal -> t+1 completed-close MARKET historical simulation**. These are researcher-designed specifications, **not** claims about inaccessible Pine source or the author's indicator defaults. The lack of IFT/fusion is a material difference and is never silently attributed to the original.

**Frozen independent identity:** `TV:FP2kd7Fo:simwai:20240612:public-description-read-20261029 | independent-derived-v1-20261029 | BTC-USDT:binance:spot:UTC1h | RSI14-Wilder-SMAseed:MFI14-typical-price-signed-volume | BUY-both-below-30-20-and-both-strictly-rising | SELL-RSI>=70-or-MFI>=80 | long-flat:0.001BTC:10000USDT | warmup100 | t-decision-to-t+1-completed-close-MARKET | fee0.001-each-filled-side | no-other-exits`. Any change to inputs, thresholds, boundary operators, market, time, risk, state, cost, or fill convention is a different derivative.

**Dedup before write:** main snapshot `6c65f27de60c53273a24a2b25361c054efc44d12`, recursive Git tree complete (not truncated), **424** root strategy Markdown records; README **424**. Eighteen distributed frontmatter samples read as PASS; **not** a 424-record exhaustive frontmatter audit. GitHub main code search for `FP2kd7Fo` found no record; all ten open PRs were examined by title/source and searches for `FP2kd7Fo`, `simwai`, `Fusion` found none. Nearest main relatives: `fmz-482880-rsi-bb-imi-mfi-quad-confluence-long-flat-btcusdt-1h-2026-10-27.md` additionally requires Bollinger/IMI confluence and uses different exit logic; `freqtrade-strategy003-rsi-fisher-mfi-washout-ema-gated-long-flat-btcusdt-5m-2026-10-21.md` requires Fisher/EMA/Stoch/SAR gates; `forven-mfi-threshold-cross-long-flat-btcusdt-1h-2026-10-19.md` uses an MFI-only recross. Here **both raw oscillators must be simultaneously oversold and increasing**, with an **either-overbought** exit; this is not a trivial parameter variant or paraphrase of those rules.

## Hypothesis and deterministic signals — Gate 1

**Hypothesis only:** simultaneous recovery in price momentum and signed dollar-flow while both remain oversold might distinguish a rebound from an isolated RSI bounce. No profitability, trade count, Qlib parity, Survivor status or historical results are claimed.

**Exact data:** one Binance spot BTC-USDT **1h** OHLCV series, ascending, UTC candle-open timestamp `T[t]` in seconds, `T[t+1]-T[t]=3600`; all O/H/L/C finite positive, `H>=max(O,C)`, `L<=min(O,C)`, finite volume >=0. No duplicates, gaps, partial candles, resampling, interpolation, missing/zero substituted prices, or silent row drops. Require a complete candle only after `E[t]=T[t]+3600`. Validate the full requested tape before indicators and verify exact row/timestamp preservation after engine feature merge (the pinned engine uses `merge_asof` and `dropna`, so neither must silently manufacture or erase decision bars). Float64 calculations in chronological order, no fitted parameters.

**Wilder RSI14 (researcher-pinned variant):** for `t>=1`, `d[t]=C[t]-C[t-1]`, `g[t]=max(d[t],0)`, `l[t]=max(-d[t],0)`. At `t=14` seed `AG[14]=sum(g[1..14])/14`, `AL[14]=sum(l[1..14])/14`; for `t>14`, `AG[t]=(13*AG[t-1]+g[t])/14`, analogously `AL`. If `AG>0,AL=0`, RSI=100; if `AG=0,AL>0`, RSI=0; if both zero RSI=undefined and no trade signal; otherwise `RSI=100-100/(1+AG/AL)`. Undefined before t=14. No EMA or SMA of RSI beyond the specified Wilder RMA.

**MFI14 (researcher-pinned variant):** `TP[t]=(H[t]+L[t]+C[t])/3`, `RMF[t]=TP[t]*V[t]`; for `t>=1`, `P[t]=RMF[t]` if `TP[t]>TP[t-1]`, else 0; `N[t]=RMF[t]` if `TP[t]<TP[t-1]`, else 0; equal TP contributes to neither. For `t>=14`, `PS[t]=sum(P[t-13..t])`, `NS[t]=sum(N[t-13..t])`. If PS>0 and NS=0 MFI=100; PS=0 and NS>0 MFI=0; both zero undefined/no signal; otherwise `MFI=100*PS/(PS+NS)`. This is mathematically the conventional ratio form but the zero-denominator rule is a researcher pin. Undefined before t=14. No IFT, fusion weights or other filters.

**Decision at completed bar t (first allowed t=100):**
- `BUY[t]=(RSI[t]<30) AND (MFI[t]<20) AND (RSI[t]>RSI[t-1]) AND (MFI[t]>MFI[t-1])`.
- `SELL[t]=(RSI[t]>=70) OR (MFI[t]>=80)`.
- All compared oscillator values must be finite/defined; otherwise the predicate is false. `BUY` and `SELL` cannot coincide. The author only said “begin to rise”; the two strict same-bar comparisons and exact boundary operators are **researcher-defined**. This is a state predicate, not an unmentioned crossover or latch; the first valid qualifying bar while FLAT can request entry, and qualifying bars while LONG do nothing.

## Direction, position, entries/exits and risk — Gates 2, 3, 4

**Market/direction:** Binance BTC-USDT **spot long/flat**; no naked shorts, borrow, derivatives, margin, leverage (1x spot), hedging or cross-asset shared capital. Fixed starting research cash **10,000 USDT**, one BUY of **0.001 BTC** only if actual available simulated quote cash covers notional plus the declared fee. SELL closes exactly the confirmed held base amount; no compounding, pyramiding, DCA/safety orders, partial exits, simultaneous positions or second pending orders. No implicit Hummingbot triple-barrier defaults.

**Finite state:** `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`. A valid BUY while FLAT queues one order for the **next** completed bar; SELL while LONG queues the full liquidation for the next completed bar. While pending or on the fill bar, all signals are ignored, never deferred. BUY in LONG and SELL in FLAT are no-ops. After a confirmed SELL, a fresh later qualifying BUY may re-enter without cooldown; no special one-shot lock or cooldown. A missing t+1 row means no fill; any missing/nonfinite actual price, insufficient cash, invalid lot/min-notional, failed, partial or unreconciled fill **aborts the run** rather than assuming a fill. No synthetic terminal liquidation. Terminal open inventory remains marked to the last **actual** valid close, not a fictional SELL.

**Exit and risk:** the sole exit is `RSI>=70 OR MFI>=80`. Stop-loss, fixed take-profit, trailing stop, break-even, maximum hold time, opposite-short reversal, session cutoff and discretionary override are **all intentionally disabled**. A losing long can persist indefinitely; this is an explicit drawdown limitation, not a safety guarantee.

## Pinned Hummingbot data/execution/cost evidence — Gate 5

**Engine:** mandatory Hummingbot package `20260920`, VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The actual pinned `hummingbot/VERSION` (blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`) was fetched through GitHub. Prior merged Alpha PR **#414** describes source/wheel 902/902 byte correspondence and 33-assert representative validation for this engine; **this cycle did not re-run tests or rehash a wheel**. If the referenced binary mapping changes, Gate 5 must be revisited.

**Market/data path inspected directly:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`) maps `1h` and uses Binance `/api/v3/klines`; `binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`) maps Kline row 0 to candle-**open** timestamp and rows 1..5 to real O/H/L/C/V. This one candle stream supplies both oscillators, with no external/multi-timeframe/non-OHLCV dependency. `BacktestingDataProvider` (blob `e3d3e087b4da7c0381fac9621d1a04dcb8de81cf`) loads candles/trading rules and exposes `quantize_order_amount`; quantity and minimum-order validity must be checked rather than assuming live historical exchange rules.

**Controller and actual fill path inspected directly:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`) runs `update_state(row)`, then `controller.determine_executor_actions()`, then routes `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`; `prepare_market_data` performs a backward `merge_asof`, requiring the above exact timestamp validation. `OrderExecutorConfig` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`) supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. `OrderExecutorSimulator.simulate` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`) for MARKET fills at the **first supplied row's actual close**, computes quote fill `amount*close`, and charges `trade_cost*amount*close` before `CloseType.POSITION_HOLD`. `BacktestPositionHold._process_order` nets spot BUY/SELL, tracks average cost, realized/unrealized PnL and accumulated quote fees. This is verified source behavior, not an API-name inference.

**Timing and model boundary:** the strategy-specific controller is **not implemented**; it must cache the decision from completed bar t and dispatch only when the next row t+1 is processed, using `C[t+1]` for the pinned simulator MARKET fill. Exchange timestamp `T[t+1]` labels the candle **open**; the modeled order cannot be said to be known/filled until effective time `E[t+1]=T[t+1]+3600`. No future close is read to decide at t. This idealized next-completed-close model is **not** TradingView's default next-open broker emulator, not a guaranteed real post-close fill, and not an intrabar, limit, maker or live market execution claim.

**Costs and positions:** explicit `trade_cost=0.001` per filled side (hypothetical **0.1%** each BUY/SELL), quote fee `0.001*notional`; no asserted Binance tier, maker/taker rebate, spread or realized slippage. The pinned simulator does not reproduce real bid/ask or slippage; these economics are **research-only idealized**. Spot BTC-USDT has no perpetual funding or liquidation; no zero-funding claim is made for futures. No futures contract, leverage, collateral or margin path is needed. The source does not specify a cash-account engine, so the declared fixed-cash affordability guard is a required controller-level rule, not falsely attributed to the built-in position ledger. No Qlib/Hummingbot strategy-specific event-level parity or live suitability is claimed.

## Warmup and point-in-time causality — Gate 6

Compute indicators sequentially from the first real candle. Indices 0..99 are **warmup-only**, first eligible decision at t=100, after 100 consecutive completed 1h bars; RSI/MFI t and t-1 are then fully defined or explicitly nontrading. Require `E[t]<=as_of` before using any completed bar; t decision never consumes t+1 OHLCV, a partial candle, future extrema, centered windows, negative shifts, fitted full-sample statistics, or post-event information. Features are timestamped to their **availability** E[t] for logical decision checks even if the Hummingbot data row is labeled T[t]. Reject missing candles/feature alignment instead of treating a backward merge or `dropna` as permission to use stale or synthesized prices.

## Admission scope, limitations and audit handoff

This is a **six-gate candidate PASS claim for this precisely frozen independent derivative**, not a claim that the original simwai Pine indicator or any fused/IFT variant passed. A separate independent Hermes Auditor must verify the source-native/derived boundary, exact formulas and equality behavior, warmup/row validation, single-position state, delayed-close semantics, actual pinned market/fee/position code paths and declared economic limitations before an exact-head merge. No backtest, implementation, order placement, Qlib parity, Survivor certification, Paper/Testnet/Live approval or deployment occurred. No repository-wide framework, runner, checker or additional eligibility flag is proposed.
