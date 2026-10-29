---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "xvelox_ arctan-normalized EMA160 slope NTZ8/delta3.2 BTC-USDT spot 1h long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/RNxThUtE-EMA-Slope-RSI-Oscillator-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The public description lists exit-confirmation defaults as both 1 and 6 bars, and standard ATR trailing factors as 5.1 and 4.7; none of those ambiguous original execution defaults is adopted."
  - "Public release notes mention v1.3.10 on Apr 5 and v1.3.8 on May 4; source revision/hash and full Pine bytes were not independently retrieved."
---

# Arctan-normalized EMA160 slope +8 NTZ breakout with delta confirmation — independent long-flat derivative

## Provenance

**Primary first-party publication:** TradingView, *EMA Slope - RSI Oscillator Strategy*, by **xvelox_**, stable public script ID **RNxThUtE**, https://www.tradingview.com/script/RNxThUtE-EMA-Slope-RSI-Oscillator-Strategy/ . Public page inspected 2026-10-30; displays **Mar 31** publication and **May 4** update without explicit year beside those dates, plus April 2026 release notes. Page labels the script open-source but its complete Pine source bytes and exact current revision were **not retrieved**. No Pine hash, TradingView order/fill equivalence or independently reproduced performance is claimed.

**Source-reported facts:** the author's public description explicitly states `maDF = longMA - longMA[smoothBars]` and `normalizedSlope = (100/pi)*atan(maDF/stdev(maDF,lookback))`, a long NTZ-cross entry above +8 with normalized-slope delta >=3.2, optional short-MA/long-MA trend confirmation, 40/160 EMA defaults, multiple additional entry methods, and ATR trailing or optional NTZ re-entry exits. It lists inconsistent later defaults for exit confirmation and trailing stops; this record does not resolve or silently inherit them.

**Researcher-designed, independent derived strategy v1 (NOT source-native):** retain only the distinctive arctan-normalized EMA-slope and +8 NTZ-cross/delta concept; independently pin EMA160/EMA40 recursive seeds, slope difference lag **4** bars, population standard-deviation window **40**, zero-variance rule, strict EMA40>EMA160 trend filter, BTC-USDT spot UTC 1h LONG/FLAT, NTZ-state close-only exit, 220-bar warmup, queued next-completed-bar-close MARKET fill, fixed 0.001 BTC, 10,000 USDT starting cash and hypothetical 0.1% per-side fees. Disable original RSI, acceleration, divergence, oscillator, short/reversal, stretch and ATR trailing subsystems. These changes **materially alter source signals, exits, timing, sizing and costs**. They are disclosed choices, not source-native facts or auditor-invented repairs.

**Immutable derived identity:** `TV:RNxThUtE|xvelox_|public-description-asof-20261030|independent-v1-20261030|BinanceSpot-BTC-USDT-UTC1h|EMA40-160-close-seed0|Dlag4-popstd40-zeroVar0|arctan100pi|NTZ+8-cross-delta3p2-EMA40gt160|Sle8-exit|next-completed-close-MARKET|Q0.001BTC-cash10000USDT-fee0.001|warmup220|long-flat-noDCA`. Any decision-critical modification requires a separately identified revision.

**Dedup snapshot:** main `85b5854077f8e79a91dd0a45b19ef5ae0715ae77` has a complete, untruncated Git tree with 449 root-level strategy Markdown records and README count 449. Seventeen evenly spaced root records' frontmatter were sampled as PASS; **not** a full 449-record admission audit. GitHub default-branch searches for `RNxThUtE`, `xvelox_`, `arctan`, `normalizedSlope` found no same-source/main record. Eleven open `research/*` PRs were inspected by metadata, and open-PR searches for source ID, author and arctan/strategy title returned no match. Other MA-slope and threshold records exist, but none found with this arctan/stdev-normalized EMA160 slope + NTZ/delta mechanism; exhaustive semantic equivalence is not asserted.

## Economic mechanism

### Source-reported

The author normalizes a long moving-average slope with its own recent dispersion using arctangent, then applies a no-trade-zone threshold and momentum-delta confirmation. The full original combines additional RSI, divergence and trailing modules, which this record does **not** reproduce.

### Research interpretation

The independent derivative tests whether an unusually strong, dispersion-adjusted long-EMA upslope crossing +8, with a concurrent positive EMA40/EMA160 regime, can define a single long exposure until that slope returns to the +8 boundary. It is a trend-persistence hypothesis, not a validated alpha, source-native reconstruction, stop-protected strategy or profitable result.

## Signal

1. **Clock and input:** single actual Binance spot `BTC-USDT` UTC `1h` OHLCV sequence indexed `t=0,1,...`. Raw exchange timestamp `T[t]` is the **candle open**, aligned to UTC hours, with exactly `T[t+1]-T[t]=3600` seconds. Completed candle t becomes usable only at `E[t]=T[t]+3600`. Require real finite positive O/H/L/C, `L<=min(O,C)<=max(O,C)<=H`, finite base volume >=0, no duplicates, gaps, out-of-order or incomplete candles. Reject a segment with missing/nonfinite actual prices or broken continuity; never interpolate, forward-fill or fabricate prices.
2. **Deterministic EMA:** for `N=40,160`, `EMA_N[0]=C[0]`; `alpha_N=2/(N+1)`; for `t>=1`, `EMA_N[t]=alpha_N*C[t]+(1-alpha_N)*EMA_N[t-1]`. Float64 chronological arithmetic, no adjusted full-sample EMA or intermediate rounding. Source defaults specify 40/160 EMA; the seed is researcher-defined.
3. **Slope difference:** `D[t]=EMA160[t]-EMA160[t-4]` for `t>=4`; before that undefined. The lag of four completed bars is a **researcher-defined** parameter, not attributed to the original source.
4. **Dispersion and arctan:** for `t>=43`, calculate `mu[t]=sum(D[t-39..t])/40` and population `sigma[t]=sqrt(sum((D[k]-mu[t])^2,k=t-39..t)/40)`. If `sigma[t]>0`, `S[t]=(100/pi)*atan(D[t]/sigma[t])`, in **degrees-free numeric oscillator points**, with mathematical pi and ordinary radian atan. If `sigma[t]=0`, define `S[t]=0` (researcher-defined deterministic zero-variance convention); reject negative/nonfinite sigma. S is undefined for t<43. No current/future full-sample statistics.
5. **Momentum and filter:** `delta[t]=S[t]-S[t-1]`; bullish trend filter `EMA40[t]>EMA160[t]` (strict). The +8 NTZ boundary and minimum delta 3.2 are source-described defaults; the choice to require the optional trend filter and ignore all other filters is **researcher-defined**.
6. **Entry edge at E[t]:** after warmup, when FLAT and no pending order, `S[t-1]<=8` AND `S[t]>8` AND `delta[t]>=3.2` AND `EMA40[t]>EMA160[t]` queues exactly one BUY. Equality at +8 is outside the entry zone; equality at 3.2 passes. If already above +8 at warmup end or after a SELL fill, do **not** enter without a fresh upward cross. No t+1 information can qualify the t decision.
7. **Exit state at E[u]:** on the first completed bar `u` strictly **after the confirmed BUY-fill bar**, when LONG and no pending order, if `S[u]<=8` queue one full-position SELL. This is a **researcher-defined close-only NTZ re-entry exit**, not the source's ATR stop/trailing execution. It may fire on a state already <=8 after a pending BUY; no fresh cross is required. No stop, TP, trailing, time exit or opposite-short reversal.
8. **Warmup:** calculate all features from t=0 but permit no order decisions through t=219; the first eligible decision is t=220, after **220 preceding fully completed 1h bars**. Ensure t=219 S is available and pre-warmup regime does not cause a carried-over entry. If no 220-bar contiguous history exists, do not shorten warmup or trade.
9. **Position state and priorities:** `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`, one 0.001 BTC spot position and at most one pending action. A pending order has priority; on its fill row update indicators but suppress all new signals. No BUY and SELL on the same fill row. After a confirmed SELL, the fill row is ineligible for re-entry; a later fresh +8 upward cross is required. No cooldown beyond these explicit state transitions. Never reverse into short.
10. **Fill convention:** a signal on completed row t is queued and dispatched **only** on the next actual completed row t+1; the pinned simulator's MARKET action uses that row's **observed close `C[t+1]`** for a historical idealized full fill, effective at `E[t+1]`. This is NOT next-open, same-signal-close, intrabar or achievable post-close live fill. If no next row exists, pending action remains unfilled; if the row/price/fill is missing, partial, inconsistent or fails reconciliation, abort rather than assume a fill. Do not use t+1 features to revise the original signal.
11. **Cash, position and terminal:** initial cash `Decimal("10000")` USDT and zero BTC. `Q=Decimal("0.001")` BTC per complete BUY and SELL, no compounding. Before BUY require modeled cash >= `Q*actualFillPrice*(1+f)`, with `f=Decimal("0.001")`. Book confirmed BUY cash debit `Q*Pb*(1+f)`, inventory +Q; confirmed SELL cash credit `Q*Ps*(1-f)`, inventory -Q. Net realized roundtrip = `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. If LONG at sample end, mark open inventory to the last **actual** completed close and report it separately; do not force a fictitious liquidation.
12. **Explicitly disabled:** source RSI/smoothed RSI, oscillator crosses, NTZ opposite-side reversals, acceleration, RSI/price divergences, stretch gate, slope-RSI exhaustion, source ATR initial/trailing stops and grace periods, short/borrow, pyramiding, DCA/safety orders, concurrent markets/shared capital, margin/futures/funding, maker/limit/next-open/intrabar execution, partial exits, hidden executor stop defaults, date-window forced exit and discretionary overlays.

## Required data

Only one actual Binance spot BTC-USDT 1h OHLCV feed with at least 220 validated **pre-decision** candles. The strategy computes causal EMA and rolling slope dispersion solely from completed closes; no fitted model, RSI, external data, other symbol, second timeframe, order book, tick feed, funding or future extrema. The raw historical buffer and continuity must be verified **before** the pinned engine's `merge_asof` / `dropna` step; a configured `max_records` does not prove delivered warmup. A missing fill price cannot use the provider's fallback price.

## Execution assumptions

**Pinned benchmark inspected through connected GitHub app on 2026-10-30:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, Hummingbot package label **20260920**, `hummingbot/VERSION` **dev-2.17.0**. GitHub source was read at this immutable commit: BinanceSpotCandles constants/parser, `BacktestingDataProvider`, `BacktestingEngineBase`, `OrderExecutorSimulator`, `OrderExecutorConfig`, `BacktestPositionHold`. Alpha PR #414 previously reported independent wheel/source correspondence; **this run did not rehash the wheel or verify a running image**. If that inherited correspondence is false, Gate 5 fails pending verification.

- **Real pinned data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` supports `1h` and REST `/api/v3/klines`; `binance_spot_candles.py::_parse_rest_candles` reads exchange kline open timestamp and actual O/H/L/C/base volume. `BacktestingDataProvider.get_candles_feed` requests `start - max_records*interval`; `get_candles_df` slices run window. The provider's `get_price_by_type` can fall back to `Decimal("1")` when price is missing; that path is **prohibited** for this derivative's fill, fee and valuation.
- **Controller / timestamp path:** `BacktestingEngineBase.prepare_market_data` uses backward `merge_asof(timestamp_bt,timestamp)`, copies real OHLCV, sets index to raw candle **open** timestamp and drops NaNs. `simulate_execution` calls `update_state(row)` then `controller.determine_executor_actions()` then `simulate_executor`. A future **minimal candidate-specific controller**, not yet implemented, must validate history before feature merge, compute E[t] separately, latch the E[t] signal and dispatch at the t+1 row; the engine's open-time row label is not a claim that the candle close was known at its open.
- **Proven simulator fill path, not merely an API name:** for `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`, the pinned `OrderExecutorSimulator.simulate` MARKET branch selects the **first supplied row** and `entry_price=df_filtered.loc[fill_timestamp,"close"]`, records `filled_amount_quote=float(Q)*actualClose` and `cum_fees_quote=trade_cost*filled_amount_quote`, then returns `CloseType.POSITION_HOLD`. Dispatch on t+1 therefore gives the specified idealized t+1 **completed-close** price, not a fabricated stop/next-open fill. Confirm the actual executor outcome before any ledger transition.
- **Costs, funding and position accounting:** `run_backtesting(trade_cost=0.001)` is an explicit **hypothetical** 0.1% quote-notional fee per filled side, **not** a verified Binance fee tier, realized fee or proof of spread/slippage. `BacktestPositionHold` aggregates BUY/SELL exposure and gross realized PnL separately from `cum_fees_quote`; its float-to-Decimal base reconstruction can leave rounding dust, so `is_closed` alone cannot define this derivative's FLAT state. Preserve confirmed executor history (`terminated_executors_window=None` or equivalent), account for the POSITION_HOLD one-tick processing lag, reconcile each executor's Q, price, side and fee against a separate Decimal cash/inventory ledger. Abort on missing/partial/duplicate fills or material mismatch (inventory >1e-9 BTC or fees >1e-8 USDT tolerance), rather than silently rounding to a profitable trade. Spot funding, leverage and liquidation are **inapplicable**; no perpetual funding=0 is assumed.
- **Capability boundary:** single-pair spot OHLCV and causal EMA/rolling stdev features; controller-latched next-row MARKET-close OrderExecutor and separate modeled fee/cash ledger use an already inspected pinned-engine primitive. No claim of real Binance fill, tick/lot/min-notional enforcement, latency, partial fill, live slippage, spread, exact source Pine behavior, implementation, backtest or Qlib/Hummingbot event-level parity. A genuinely new execution primitive must receive representative parity validation before large-scale screening.

## Evidence

### Source-reported

xvelox_ first-party TradingView publication RNxThUtE provides the arctan-normalized slope formula, NTZ +8, delta >=3.2, 40/160 EMA defaults, optional trend confirmation, optional NTZ re-entry exit and other explicitly excluded subsystems. Source version/default conflicts are disclosed above. No source backtest results are represented as independently reproduced.

### Independently reproduced

**Not independently reproduced.** No strategy performance, Pine replay, actual fills, fee tier, Qlib/Hummingbot event-level parity, Survivor status or trade outcome was generated in this Scout cycle. Direct static GitHub inspection verified the named pinned source-code execution/data/accounting paths only.

### Negative evidence

Complete Pine bytes/current immutable Pine revision not retrieved; source default `smoothBars` and stdev `lookback` not established; original exit confirmation and trailing defaults conflict in prose. The derivative explicitly defines its own lag/window and disables original trailing/RSI branches. Static pinned-engine source inspection is not an executable candidate controller or empirical fill test. Spot real-market economics remain unverified.

## Falsification plan

After separately authorized implementation, test EMA seed, Dlag4, population vs sample stddev, zero-variance handling, strict NTZ cross/equality, delta equality, EMA trend gate, 220-bar warmup, no inherited warmup signal, signal reversal during pending BUY, exit on first eligible post-fill S<=8, re-entry after SELL, missing t+1 candle, fee reconciliation, float/Decimal dust, and timestamp E[t] vs raw T[t]. Validate one representative pinned Hummingbot/Qlib event sequence **before mass screening of any new unverified execution primitive**; do not convert this Scout into a backtest.

## Crypto portability

Research identity is **BTC-USDT Binance spot 1h only**, a chosen derivative scope, **not** an HB_READY single-pair/timeframe prerequisite. Other pairs/timeframes, short/futures, fee tiers, lot sizes, and capital overlays would require separately declared assumptions and capability checks. The optional seven-coin 1h/4h/1d DCA 6/6/6 downstream campaign is not silently embedded here.

## Limitations

No protective stop or fixed time limit; exposure can sustain large drawdowns. The model assumes a complete next-completed-close MARKET fill and hypothetical fee, not a realizable after-close order. The zero-variance fallback and lag/window/exit are researcher-defined. Exact original Pine event equivalence is **not claimed**. Missing prices, data gaps or fill/accounting inconsistencies fail closed.

## Implementation status

`implementation_status: not-implemented`. This is a six-gate **research-only admission proposal**, not a deployed controller, Qlib recipe, runnable strategy, or additional implementation gate.

## Adoption boundary

`hb_ready_status: PASS` here is **Scout-proposed and subject to independent Hermes Auditor exact-head review**, not an independently certified result. `status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. No Qlib/Hummingbot execution, Paper/Testnet/Live trading, survivor promotion or README/main mutation is authorized. Only the existing independent reviewer may remediate/merge/close, and only the signed existing webhook receiver performs post-merge README bookkeeping.

## Related Wiki records

None linked. No Wiki, registry, pipeline, README or existing strategy record was modified by this candidate.

## Sources

- First-party TradingView strategy by xvelox_: https://www.tradingview.com/script/RNxThUtE-EMA-Slope-RSI-Oscillator-Strategy/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior wheel/source verification evidence (not rerun): https://github.com/HCH725/alpha-strategy-research/pull/414
- Repository admission policy: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
