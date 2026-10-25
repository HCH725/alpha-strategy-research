---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader Twiggs Money Flow 21 zero-cross long-flat BTCUSDT 1d independent derivative
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
  - https://quantifiedtrader.com/backtest/strategies/twiggs-money-flow
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QuantifiedTrader Twiggs Money Flow 21 zero-cross — independently specified long-flat derivative

## Provenance

**First-party source:** QuantifiedTrader public strategy-library page, *Twiggs Money Flow*, read live 2026-10-25 (42,903 bytes HTML fetched this cycle): https://quantifiedtrader.com/backtest/strategies/twiggs-money-flow . The page prints its full methodology and indicator/decision code inline; no login, paywall, or private content was involved.

**Facts actually supplied by the source page:** the strategy is backtested on **daily OHLCV** price data across major US equity indices and ETFs; entry/exit signals are generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics are computed per symbol; **transaction costs and slippage are not modeled**. The signal prose states Twiggs Money Flow is a refined Chaikin Money Flow that uses true range instead of high-low range and **enters long when TMF crosses above zero**. The pinned decision code is exactly: `n = 21`; `tp = (h+l+c)/3`; `mf = tp.diff() * v / (h-l).replace(0,1e-10)`; `tmf = mf.rolling(21).sum() / (v*(h-l).replace(0,1e-10)).rolling(21).sum()` with `.fillna(0)`; entry `tmf[-1] > 0 and tmf[-2] <= 0 and not position -> buy()`; exit `tmf[-1] < 0 and position -> position.close()`. No short/sell-short call, no stop/target/trailing/time call, and no sizing literal ship anywhere in the rule.

**Prose-vs-code gap (disclosed, not repaired):** the page prose claims a *true-range* construction, but the pinned code computes plain `(h-l)` with a `0 -> 1e-10` zero-guard. This derivative follows the **code** exactly and adopts no true-range reading.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than the source equity-index universe; (2) the code-exact TMF(21) construction below with the `1e-10` zero-guard and `0`-for-undefined treatment preserved; (3) strict cross-up `prev <= 0 AND curr > 0` LONG entry and strict level `curr < 0` LONG exit; (4) **close-effective** MARKET simulator fills instead of the source next-open execution; (5) fixed **0.001 BTC** sizing with no compounding instead of the framework-default share sizing; (6) no stop/target/trailing/time exit, no DCA and no short; (7) 30 valid completed daily bars of warmup, data-gap treatment and re-entry rules below; (8) pinned simulator `trade_cost = 0.0001` per filled side as a **researcher-selected house research input** — the source models no costs, so no fee value is attributed to it. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** QT-twiggs-money-flow | derived-v1-tmf21-crossup0-exitbelow0 | BinanceSpot-BTC-USDT-1d | 2026-10-25. Any changed input, window, comparator, clock, position rule, cost or fill model creates a different derivative.

## Economic mechanism

The source hypothesizes that volume-weighted money-flow momentum crossing from distribution into accumulation marks the start of a durable advance, and that losing the zero line means the thesis has failed. This derivative buys only the fresh zero cross-up and exits on the first sub-zero print. It is not a proven edge; long exposure can lose substantially and the declared derivative has no protective stop. No QuantifiedTrader reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. Rolling windows include the current **completed** bar and exclude all future bars.

- TP[t] = (high[t]+low[t]+close[t])/3. RNG[t] = high[t]-low[t]; the divisor for bar i is RNG[i] except exactly `0`, which uses `1e-10` (code-faithful zero-guard, never invented).
- MF[t] = (TP[t]-TP[t-1])*volume[t]/GuardedRNG[t], requiring TP[t-1]; bar 0 has no MF print.
- NUM[t] = sum of MF[i] for i in t-20..t (21 trailing bars). DEN[t] = sum of volume[i]*GuardedRNG[i] for i in t-20..t.
- TMF[t] = NUM[t]/DEN[t]; when the window is incomplete (fewer than 21 bars) or DEN[t] equals 0, TMF[t] is 0 (the code's `.fillna(0)` treatment, preserved exactly — undefined never interpolates, never forward-fills, never reads a future bar).
- **LONG entry from FLAT only:** TMF[t-1] <= 0 AND TMF[t] > 0, after the 30-bar warmup. Strict on both sides: exactly `0.0` on the current bar never enters.
- **LONG exit:** TMF[t] < 0. Strict: exactly `0.0` never exits; the exit is a level, not a cross — the first sub-zero print after entry closes the unit.
- Entry and exit can never co-fire: entry needs TMF[t] > 0 while exit needs TMF[t] < 0 on the same bar, disjoint by arithmetic, so no tie-break pin is required. If an exit condition occurs while FLAT it is a no-op; if an entry condition occurs while LONG it is a no-op. At most one filled order per completed bar.
- Start FLAT; require **30 consecutive valid completed daily candles** before the first decision (21-bar rolling sums, one-bar typical-price-difference seeding, and the one-bar cross lookback are covered with margin). A gap, duplicate/non-monotonic timestamp, invalid OHLCV, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 30-bar valid segment.
- **Cooldown:** none specified — explicitly none, not invented. Re-entry after any exit requires a **new** cross-up (prev <= 0, curr > 0), never a level hold. No queued signals or retrospective entries.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. The pinned simulator's MARKET path fills fully at the first supplied close; a sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view. Re-entry after exit requires a fresh cross-up trigger.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), high >= low, and finite nonnegative volume. TMF needs only the current plus trailing 21 bars (typical-price difference reaches one bar further back); crossover comparisons require t-1, never future data, unconfirmed intrabar values, lookahead joins, model fitting, or hindsight detection. The zero-guard and zero-for-undefined treatments are coded source behavior, not researcher smoothing. Missing close/volume prices block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0 (verified this cycle via raw fetch at the pin). A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py maps the **1d** interval (INTERVALS bidict) and REST /api/v3/klines with symbol/interval/limit params (all verified this cycle at the pin); binance_spot_candles.py parses REST row[0] as timestamp with row[1..5] as O/H/L/C/V and WS kline keys o/h/l/c/v (verified this cycle). A strategy-specific controller must compute the declared TMF(21) features, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this money-flow signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls update_state(row), controller.determine_executor_actions(), and CreateExecutorAction -> simulate_executor; OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator (row path verified this cycle at the pin). The latter fills at its first supplied row timestamp and **close** price, sets filled_amount_quote = 0.001*close, cum_fees_quote = trade_cost*filled_amount_quote, and CloseType.POSITION_HOLD. Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. BacktestingEngineBase.prepare_market_data uses merge_asof on timestamp_bt (verified this cycle); backward as-of joining alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This is a disclosed adaptation away from the source next-open execution and does not claim a real post-close order can fill at the already-observed close. No intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume"), tracking average entry price, gross matched realized PnL and accumulated fees separately (verified this cycle at the pin). The engine's positions_held conversion is delayed; pin terminated_executors_window=None and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, researcher-selected house research input — the source models no costs and no rate is attributed to it); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** merged 2026-10-24 after independent HB_READY review of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle additionally re-read the pinned VERSION, Binance spot candle constants/parser, backtesting engine row/action routing, OrderExecutorSimulator and BacktestPositionHold code at the pin.

## Evidence and six-gate summary

1. **Deterministic signals:** complete TP/RNG/MF/NUM/DEN/TMF(21) construction with code-faithful zero-guard and zero-for-undefined rules, strict cross-up entry and strict sub-zero exit defined above; no Pine/framework equivalent is claimed.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT only, no short/margin.
3. **Entry/exit/risk:** TMF zero cross-up BUY, sub-zero SELL, all other stop/target/trailing/time legs disabled; no hidden defaults.
4. **Position:** fixed 0.001 BTC, single pending/filled state, no cooldown (explicitly none), fresh-cross re-entry, no DCA/concurrency.
5. **Pinned engine:** concrete source commit re-read this cycle, 1d Binance candle path, controller action, MARKET full-close fill, timestamp normalization, fee and POSITION_HOLD ledger limitations; no novel unverified execution primitive used.
6. **Causality:** 30 completed-bar warmup, finite/gap guards, no future reads, decision and research-fill effective at completed bar close.

**Source-reported:** only the page identity, daily-OHLCV/no-lookahead/next-open methodology, unmodeled-costs disclaimer, true-range-vs-code wording, TMF(21) code rule and long-only stance stated in Provenance. **Researcher-designed:** every market/timeframe/fill/sizing/warmup/cost transfer identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed.

## Deduplication

Main at immutable SHA **3a0e6e3b11b27c6a07f1b8a6054737cfe6527745** contained **333** root strategy records; README static count **333**. Working-tree filename/content search for `twiggs` returns zero strategy records (only prose mentions of Colin Twiggs as the author of unrelated Volatility-Stops/PVI pages). GitHub issue/PR search for `twiggs` across this repository returns zero items ever; ten open research/* PRs were checked and none carries this primary source or a Twiggs rule. Nearest money-flow neighbors are **not equivalent**: `freqtrade-technical-cmf-sign-state` trades Chaikin close-location CMF(21) persistent sign-states on 5m with a 1% ROI rung and a -5% stop — this record trades a typical-price-**change**-weighted TMF(21) one-bar cross-up edge on 1d with indicator-only exits and no price-based legs (a doji pinned at its range top prints CMF near +1 yet TMF near 0); `cmf-velocity-zero-cross-ema200` adds a velocity readout plus an EMA200 bracket and is two-sided; `forven-chaikin-mf-threshold-cross` is a threshold-cross, not a zero-cross; `forven-adl-ema-cross` trades a cumulative level against its EMA; NVI/PVI records trade volume-direction-filtered cumulative indices against a 255 EMA. Different formula, different edge-vs-state construction, different risk set, different horizon: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After separate downstream research authorization, compare the frozen TMF(21) cross-up/level-down pair against a same-horizon Chaikin CMF(21) cross-up/level-down ablation on predeclared IS/OOS partitions; verify that the change-weighted construction actually changes entry/exit event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Crypto portability

Native crypto venue by declaration (Binance BTC-USDT spot 1d); no equity-to-crypto portability transform is asserted beyond the disclosed derivative identity. Spot semantics remove funding; minimum-notional, precision, liquidity and live viability remain unverified limitations, never assumed.

## Implementation status

Not implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine files were read. The disclosed derived model must be implemented exactly if selected downstream.

## Adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-engine reproduction, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. No secrets, paid content, copied code block or private information included.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/twiggs-money-flow — QuantifiedTrader public strategy-library source; methodology and decision code read live 2026-10-25 (42,903 bytes HTML); page carries no publication date so source_as_of is the read date.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (VERSION, spot candle constants/parser, backtesting engine, order simulator, position-hold ledger re-read this cycle).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
