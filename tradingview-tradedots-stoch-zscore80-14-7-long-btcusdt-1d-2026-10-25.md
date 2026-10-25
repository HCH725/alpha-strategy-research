---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradeDots Stochastic Z-Score 80/14/7 blended oversold long-flat BTCUSDT 1d independent derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-04-28
sources:
  - https://www.tradingview.com/script/Nft2YKWq-Stochastic-Z-Score-Oscillator-Strategy-TradeDots/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradeDots Stochastic Z-Score composite oversold-to-zero — independently specified long-flat derivative

## Provenance

**First-party source:** TradingView open-source strategy publication, *Stochastic Z-Score Oscillator Strategy [TradeDots]*, author **tradedots** (TradeDots), published **2024-04-28**, stable public script ID **Nft2YKWq**, directly read 2026-10-25: https://www.tradingview.com/script/Nft2YKWq-Stochastic-Z-Score-Oscillator-Strategy-TradeDots/ . This public page labels the work a strategy and says that it is open-source, but the complete Pine source bytes, source revision/hash, strategy properties and executable order calls were **not retrieved** in this cycle. No lossless Pine equivalence is asserted.

**Facts actually supplied by the author in the public description:** trailing close-price Z-score = (close minus rolling mean) divided by rolling standard deviation; a stochastic oscillator is normalized to approximately [-4,+4] and averaged with Z-score; oversold/overbought thresholds govern signals; exit when Z-score returns to zero; cooldown prevents repeated signals. Author's example defaults for **EURAUD 1h** are rolling window **80**, threshold **2.8**, signal cooldown **5**, stochastic length **14**, smoothing **7**, commission **0.01%**, initial capital **USD 10,000**, and equity per trade **40%**. The page does not resolve the exact stochastic variant, smoothing implementation, zero-cross comparator, bar-order/fill timing, Pine revision, stop/target logic, or partial-fill behavior. Those unknowns are not silently attributed to the author.

**Independent derivative, not source-native reconstruction:** the researcher explicitly chooses (1) Binance BTC-USDT **spot 1d**, LONG/FLAT rather than an unverified source direction/order map; (2) population rolling standard deviation, raw high-low stochastic and SMA7 smoothing with the exact affine [-4,+4] map defined below; (3) strict composite cross-under -2.8 as the LONG entry and strict Z-score zero recovery as the LONG exit; (4) a precisely counted five-bar post-exit cooldown; (5) fixed 0.001 BTC instead of source example 40%-of-equity sizing, with no compounding; (6) no stop/target/trailing/time exit, no DCA and no short; (7) 100 valid completed daily bars of warmup, data-gap treatment and close-effective MARKET simulator fills; (8) source example 0.01% commission carried as a **hypothetical research fee rate**, not an actual Binance tariff. All researcher-selected order rules and disabled behaviors belong to this independent derivative alone.

**Immutable strategy identity:** TV-Nft2YKWq-tradedots | derived-v1-stoch-z80-n14-sma7-crossunder-2p8-zrecover0-cd5 | BinanceSpot-BTC-USDT-1d | 2026-10-25. Any changed input, smoothing, clock, threshold, position rule, cost or fill model creates a different derivative.

## Economic mechanism

The source hypothesizes that statistically unusual downside close-price deviations, corroborated by an oversold stochastic oscillator, can mean-revert toward the rolling close-price mean. This derivative buys only on a fresh extreme of the **blended** oscillator and exits only when the **unblended Z-score** recovers to zero. It is not a proven edge; long exposure can lose substantially and the declared derivative has no protective stop. No TradingView reported performance is reproduced or independently claimed.

## Signal

**Gate 1: fully frozen, deterministic formulas.** Use one consecutive UTC daily BTC-USDT spot OHLCV stream; bar t opens at UTC timestamp T[t], with all O/H/L/C/V only available for decisions at effective timestamp T[t]+86400 seconds. Rolling windows include the current **completed** bar and exclude all future bars.

- Mean80[t] = arithmetic average of close[t-79] through close[t]. SD80[t] = square root of the sum of (close[i]-Mean80[t]) squared over the same 80 bars divided by **80** (population denominator, not sample 79). Z[t] = (close[t]-Mean80[t])/SD80[t].
- HH14[t] = maximum high[t-13..t], LL14[t] = minimum low[t-13..t]. RawK14[t] = 100*(close[t]-LL14[t])/(HH14[t]-LL14[t]). SmoothK7[t] = arithmetic mean of RawK14[t-6..t], requiring all seven finite values.
- ScaledK[t] = (SmoothK7[t]-50)*0.08, mapping stochastic 0 to -4, 50 to 0, and 100 to +4. Composite[t] = (Z[t]+ScaledK[t])/2.
- If SD80 is zero or HH14 equals LL14, that bar's dependent indicator is undefined (not replaced by zero). Any entry/exit requiring undefined current or previous values is false. Missing/invalid OHLCV is never interpolated or forward-filled.
- **LONG entry from FLAT only:** Composite[t-1] >= -2.8 AND Composite[t] < -2.8, with both finite, after the 100-bar warmup and only when the post-exit cooldown has fully expired.
- **LONG exit:** Z[t-1] < 0 AND Z[t] >= 0, with both finite. This is the researcher's exact operationalization of the source-described return-to-zero exit; it is NOT claimed as the author's exact Pine comparison.
- If an exit condition occurs while FLAT it is a no-op; if an entry condition occurs while LONG it is a no-op. Exit has priority over entry in the state machine, although with ScaledK in [-4,+4], Composite < -2.8 mathematically requires Z < -1.6, so a simultaneous entry and zero-recovery exit cannot occur on valid data. At most one filled order per completed bar.
- Start FLAT; require **100 consecutive valid completed daily candles** before the first decision (80-bar Z-score, 14+6-bar smoothed stochastic and prior-bar cross are covered). A gap, duplicate/non-monotonic timestamp, invalid OHLCV, or broken UTC daily cadence resets warmup for fresh entries and exits; if already LONG, hold without inventing gap fills and resume exit evaluation after a fresh 100-bar valid segment. Undefined indicator values suppress only signals dependent on them.
- **Cooldown:** after a filled SELL on bar t, bar t+1 through t+5 (five subsequent completed daily decision bars) prohibit BUY; first eligible BUY is bar t+6, and it still requires a **new** composite cross-under. No queued signals or retrospective entries.
- **Position state:** FLAT -> PENDING_BUY -> LONG only on confirmed simulator full-fill BUY; LONG -> PENDING_SELL -> FLAT only on confirmed full-fill SELL. Pending states suppress all additional actions. The pinned simulator's MARKET path fills fully at the first supplied close; a sent action is not falsely equated to a fill in controller state. The controller must persist fill-derived state independent of the delayed positions_held view. Re-entry after cooldown requires a fresh trigger, not a level hold.
- **Risk and disabled behaviors (Gates 2–4):** exactly one spot LONG of **0.001 BTC** or FLAT; no short, margin, leverage, pyramiding, DCA, safety orders, simultaneous exposure, fractional/partial orders, scaling, stop loss, take profit, trailing stop, timeout, forced liquidation, maker/limit orders or end-of-sample SELL. No additional opposite-signal leg. No reinvestment/compounding. If still LONG on the final available completed bar, mark the position at the last valid close without inventing an exit trade.

## Required data and causality

**Gate 6:** Binance BTC-USDT spot 1d O/H/L/C/V with strictly increasing UTC midnight bar-open timestamps 86400 seconds apart. Each valid bar has finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), and finite nonnegative volume. All 80-bar Z windows, 14-bar stochastic extrema and seven-bar smoothing inputs use only bars at or before t; crossover comparisons require t-1, never future data, unconfirmed intrabar values, request.security lookahead, model fitting or hindsight pivot detection. Missing close prices block signals and fills rather than defaulting to synthetic prices. One asset, one decision timeframe, no cross-asset synchronization, futures funding, external indicators, ML artifacts or order-book inputs.

## Execution assumptions and pinned Hummingbot compatibility

**Gate 5 is bounded to a real inspected pinned simulation path, not a deployment claim.** Admission policy identifies Hummingbot package label **20260920**, VERSION **dev-2.17.0**. The independently inspected source is **HCH725/hummingbot at commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3**; its hummingbot/VERSION file reads dev-2.17.0. A package build digest was not available and this record does **not** claim that package 20260920 was byte-for-byte matched to this source commit or deployed. The engine-path claim is limited to this pinned source and previously reviewed matching research semantics.

- **Market/data:** BinanceSpotCandles constants.py lists the **1d** interval and REST /api/v3/klines; binance_spot_candles.py parses exchange row[0] timestamp and row[1..5] O/H/L/C/V. A strategy-specific controller must compute the declared features, verify contiguous completed bars and supply a single BTC-USDT spot 1d stream. The engine does not magically implement this composite signal.
- **Controller/action/executor:** BacktestingEngineBase.simulate_execution iterates processed rows, calls update_state(row), controller.determine_executor_actions(), and CreateExecutorAction -> simulate_executor; OrderExecutorConfig with ExecutionStrategy.MARKET and BUY/SELL side routes to OrderExecutorSimulator. The latter fills at its first supplied row timestamp and **close** price, sets filled_amount_quote = 0.001*close, cum_fees_quote = trade_cost*filled_amount_quote, and CloseType.POSITION_HOLD. Full fill at one close is an explicit simulator convention, not proof of actual executable spot fills.
- **Timestamp caveat:** source candle timestamp is the **bar OPEN label**. BacktestingEngineBase.prepare_market_data uses merge_asof and raw timestamp_bt; backward as-of joining alone does not establish that a completed close was known at the open. The required derivative controller gates the completed bar until T[t]+86400, and the resulting research event/fill ledger is explicitly normalized to that **close-effective** timestamp while using the simulator's same-row close price. This does not claim a real post-close order can fill at the already-observed close. No next-open/intrabar or lower-timeframe path is assumed.
- **Position and ledger:** BacktestPositionHold nets equal-base BUY and SELL, tracks average entry price, gross matched realized PnL and accumulated fees separately. The engine's positions_held conversion is delayed; pin terminated_executors_window=None and use persistent pending/fill-confirmed controller state to avoid duplicate orders or losing prior fills. After a 0.001 BTC BUY at P_b and a 0.001 BTC SELL at P_s, modeled net quote PnL = 0.001*(P_s-P_b) - 0.0001*0.001*(P_b+P_s); do not misreport gross native net_pnl_quote or pnl_timeseries as fee-inclusive equity. An open position's marked equity carries the already-paid BUY fee.
- **Costs:** pin simulator trade_cost=**0.0001 per filled side** (0.01%, matching the TradingView author's published *example* commission); this is **research cost input only**, not verified Binance realized commission. No separate simulator slippage is added, which is **zero additional modeled slippage**, not evidence of zero actual spread/latency/slippage. Spot funding is inapplicable (no fabricated futures funding). Binance minimum notional, lot/tick precision, exchange commissions, partial fills, liquidity and real trading viability remain unverified; do not infer live admissibility.
- **Reused independent path review:** HCH725/alpha-strategy-research PR **#417** received an independent HB_READY: PASS review on 2026-10-24/25 after inspection of this same pinned Binance spot 1d / MARKET first-close / POSITION_HOLD and fee-ledger research path. That verifies an **engine primitive**, not this new indicator, trade series, profitability, package digest or candidate-specific parity. This cycle also read the pinned VERSION, Binance spot candle parser/constants, backtesting engine update/executor routing, OrderExecutorSimulator and BacktestPositionHold code through the connected GitHub app.

## Evidence and six-gate summary

1. **Deterministic signals:** complete 80-bar population Z, 14-bar high-low stochastic, SMA7, [-4,+4] scale, blend, strict thresholds and invalid-data rules defined above; the unverified Pine implementation is never called identical.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT only, no short/margin.
3. **Entry/exit/risk:** composite oversold cross-under BUY, Z recovery SELL, all other stop/target/trailing/time legs disabled; no hidden defaults.
4. **Position:** fixed 0.001 BTC, single pending/filled state, five-bar cooldown, new-cross re-entry, no DCA/concurrency.
5. **Pinned engine:** concrete source commit, 1d Binance candle path, controller action, MARKET full-close fill, timestamp normalization, fee and POSITION_HOLD ledger limitations; no novel unverified execution primitive used.
6. **Causality:** 100 completed-bar warmup, finite/gap guards, no future reads, decision and research-fill effective at completed bar close.

**Source-reported:** only the author, public date/ID, concept, formula-level Z-score description, stochastic rescaling/averaging, mean-zero exit concept and example parameter/cost values stated in Provenance. **Researcher-designed:** every operational comparator, indicator variant, position/risk/clock rule, market/timeframe and cost transfer identified above. **Independently reproduced backtest performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed.

## Deduplication

Main at initial immutable SHA **6b16ac75e1a14af51e4f4a57f7d5d54940e64dfe** contained **332** root strategy records; README static count **332**. Main filenames and code search contained no TradingView ID Nft2YKWq or TradeDots Stochastic Z-Score; ten open research/* PRs were checked and none had that primary source or this composite 80/14/7 blended entry plus five-bar cooldown. Existing forven-zscore-mean-reversion (20-bar sample Z with level entry below -2 and level exit above zero) and forven-zscore-mean-reclaim (20-bar sample Z with EMA34 reclaim) are **not equivalent**: neither computes stochastic, rescales it, averages it with Z, requires a composite -2.8 crossing, or enforces a five-bar post-exit cooldown.

## Falsification plan

After separate downstream research authorization, compare the frozen composite with an ablation omitting stochastic, on predeclared IS/OOS partitions; verify that the new blend actually changes entry event times. Any new or unverified execution/data primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. Do not tune on OOS. No backtest was run by Scout.

## Limitations and adoption boundary

Frontmatter PASS is a **Scout-proposed six-gate research eligibility claim**, subject to independent Hermes Auditor review, not an independently approved merge. This is **not** a source-native Pine recreation, actual Binance economics, profitable strategy, Qlib parity, HB Certified, survivor, deployment or Paper/Testnet/Live approval. Implementation_status is not-implemented: no candidate-specific controller, feature module or replay artifact was created; only pinned generic engine semantics were inspected. The disclosed derived model must be implemented exactly if selected downstream. No secrets, paid content, copied Pine block or private information included.

## Sources

- https://www.tradingview.com/script/Nft2YKWq-Stochastic-Z-Score-Oscillator-Strategy-TradeDots/ — TradeDots, public TradingView source, published 2024-04-28; source prose read 2026-10-25; full Pine revision not retrieved.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source (read via connected GitHub app).
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent review of the same pinned spot 1d MARKET-close POSITION_HOLD research primitive.
