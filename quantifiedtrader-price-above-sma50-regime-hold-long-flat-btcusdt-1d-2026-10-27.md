---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QuantifiedTrader PriceAboveSMA SMA50 regime-hold BTCUSDT spot 1d long-flat derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-27
sources:
  - https://quantifiedtrader.com/backtest/strategies/price-above-sma
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PriceAboveSMA SMA50 regime-hold — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary public research-library identity:** QuantifiedTrader strategy-library page *Price Above SMA*, https://quantifiedtrader.com/backtest/strategies/price-above-sma, read live end to end this cycle (2026-10-27, HTTP 200, 42,694 bytes HTML). No login, paywall, or private content was involved.

**The page's own words (quoted for gate evidence, never extended):** backtested on **daily OHLCV** across major US equity indices and ETFs; entry/exit signals generated with **no lookahead bias**; **trades execute at the open of the bar following the signal**; performance metrics computed per symbol; transaction costs and **slippage are not modeled**. Signal prose: *Simple trend filter: long when price is above its N-period SMA, flat when below. Acts as a regime filter — only holds positions when price is in an uptrend relative to its own moving average.* Pinned decision code, in full: `n = 50`; `self.sma = self.I(_sma, self.data.Close, self.n)`; entry `if self.data.Close[-1] > self.sma[-1] and not self.position: self.buy()`; exit `elif self.data.Close[-1] < self.sma[-1] and self.position: self.position.close()`. Whole-page token census: 1 `self.buy()` / 1 `position.close()` / 0 short/sell-short calls / 0 `crossover` / 0 stop/target/trailing/time calls / 0 sizing literals / 0 `pyramiding` / 0 `request.`/`security(` / 0 commission / 0 volume reads in the rule (Close is the only price array read). The 19 `stop|trail` substring hits are site chrome and sibling-page boilerplate, never part of this strategy's rule.

**Unpinned-helper gap (disclosed, not repaired):** the page calls a shared site helper `_sma(Close, 50)` whose `def` body is printed nowhere on this page (verified: `_sma` occurs exactly once, at the call site) — the same disclosed situation as the admitted QuantifiedTrader disparity-index sibling, which froze the textbook definition as an explicit researcher choice. This record likewise freezes the textbook definition — arithmetic mean of the 50 completed closes — owned below as a researcher choice, never attributed to the site author. Unlike ATR/RMA-seeded helpers this choice carries no seeding ambiguity: a simple moving average over completed closes is arithmetically exact from the first full window, so no framework-equivalence question arises beyond the disclosed formula.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 1d, long/flat only** (the source ships no short leg — faithful); pin SMA(50) arithmetic-mean construction with strict `>`/`<` level comparators; adopt **close-effective** MARKET simulator fills instead of the source next-open execution (same disclosed adaptation as the admitted disparity-index sibling); fixed 0.001 BTC on unborrowed cash with hypothetical 0.0002-per-side research cost (the source models no costs — no fee value is attributed to it); 100-bar warmup; no stop/target/trailing/time exit, no DCA, no short; and the state/timing/cost rules below. All changes are part of this **separate strategy**, not evidence that the source page's backtest is reproducible unchanged.

**Immutable research identity:** `QT-price-above-sma | derived-v1-SMA50-strict-level-hold | Binance-BTC-USDT-spot-1d | close-effective-MARKET-0p001BTC-cost0p0002 | 2026-10-27`. Changing any component changes the derivative identity.

**Pre-write dedup:** main SHA `7c9d91d8b34f70f79b14d5f60c21b8eaa77bb22c`, 383 root-level strategy Markdown records; README static count 383. Working-tree and GitHub PR searches for `PriceAboveSMA`/`price-above-sma` return zero records and zero PRs. Ten open `research/*` PRs examined by title and source — none uses this URL or rule (nearest, #331 AdxSmas, is an ADX-gated dual-SMA 3/6 *cross* on 1h; #251 Swift 2YMA is a 2-year-MA multiplier *zone* system — both fenced below). Nearest pool families are materially different: `golden-cross-sma-regime-gated` (dual-MA 9/50 *cross* plus SMA100 level gate, 1h); `forven-rsi-s00139-washout-cross` (Forven RSI-momentum: SMA20-gated RSI washout-cross with RSI-overbought exit, 1h); `mayer-multiple-below-2p4-regime` (price-to-200DMA *ratio* value threshold, opposite side); `quantifiedtrader-disparity-index-14` (14-bar *normalized percentage-distance* cross-up edge with sub-zero exit — different indicator, window, and entry form); `nvi/pvi-255ema-regime` (volume-index-gated, different gate). No pool record holds long purely on a strict close-vs-single-SMA level on one timeframe. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source hypothesizes only what its prose prints: a close above its own 50-bar average marks an uptrend regime worth holding; falling back below the average ends the thesis. The page ships no trade count, window, or cost basis with its figures — this record adopts no source-reported performance (see Evidence).

### Research interpretation

A single-average regime hold, long-only. Unlike dual-average cross records (fast-vs-slow turn detectors), there is no second average and no turn edge: every above-average close while flat is a buy, so entries can print far from any cross after a flat spell. Unlike ratio/multiple records (value zones below a scaled average), the trigger is the raw average itself with a symmetric exit — the position's entire fate rests on whether the close stays above its 50-day mean. Unlike oscillator-gated records, no momentum, volume, or volatility read exists anywhere in the gating path. The coded consequence is a slow trend-following hold that sits out sub-average regimes entirely and compounds no pyramiding while riding.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 1d OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 86400 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback.

**SMA50 (researcher-pinned, exact):** for `t>=49`, `sma[t]=sum(C[t-49..t])/50` (arithmetic mean, divisor 50). Single close feed; no shifted average or fitted input. Undefined (NaN) for `t<49`; every NaN comparison is false — no leg can fire early.

**Completed-bar long entry predicate `E[t]`** (both true): `C[t] > sma[t]` (strict — a close exactly on the average does not fire), and `t>=100`, every required feature valid, no pending order, FLAT and re-arm state true. No volume/volatility/funding read anywhere in the gating path. NOTE (verified equivalence, not a second rule): because the only exit is the symmetric strict level below, FLAT can only follow a sub-average close, so the next firing bar is definitionally a reclaim — the source-faithful level form and an edge form coincide exactly here; this record evaluates the level form.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. Zero short calls ship in the source rule.

**Signal exit (Gate 3):** while LONG, on each subsequent completed bar request full SELL if `C[t] < sma[t]` (strict — a close exactly on the average holds). Entry and exit predicates are mutually exclusive on one close (`>` vs `<` with equality holding), so no priority ordering is needed. **Close-confirmed MARKET research exit, not an intrabar touch or resting stop/limit order** — the pinned backtest path below offers no verified intrabar semantics, so none is claimed. No stop, target, trailing, time stop, partial exit, averaging, forced end-of-data liquidation, or silent executor default. All exits are **close-price** levels, never leveraged/net returns (spot, leverage 1).

**State (Gate 4):** `FLAT_DISARMED`, `FLAT_ARMED`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT_ARMED` after 100 valid completed bars **only if E without the state clause was false on the immediately prior completed bar**; otherwise wait for a false bar to arm. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET POSITION_HOLD fill at that same completed close transitions to LONG. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT_DISARMED. Once flat, require at least one **subsequent** completed bar with the non-state entry predicate false to re-arm. No same-bar SELL+BUY, no pyramiding, **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding, no session/cooldown. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous completed 1d bars before the first actionable bar; covers the 50-bar average seed and the arming rule. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Unseeded windows stay NaN and every NaN comparison is false.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and derived average become available no earlier than `T[t]+86400s`. All decisions and the synthetic model fill are effective at that **completed-bar close**. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`, content `dev-2.17.0`, re-verified this cycle against the pinned commit). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated. The `20260920` package label is retained as a policy label only; no package-to-commit mapping is invented.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`, re-verified this cycle) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, INTERVALS re-read this cycle) supports `1d`. Connector `binance`, pair `BTC-USDT`, one spot 1d stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision, no multi-market or mixed-timeframe synchronization.
- **Controller path (row path re-verified line-level this cycle):** `BacktestingEngineBase.run_backtesting` → per-row `update_state` → `determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`. A **strategy-specific, not-yet-implemented** controller must calculate the exact average/state and perform time gating. The generic executor does not calculate the strategy. No novel execution primitive is introduced beyond the independently-reviewed MARKET OrderExecutor → POSITION_HOLD representative path.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` at `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, code re-read this cycle) fills fully at first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar fill. The pinned `PositionExecutorSimulator` is **not** used because this record claims no stop/TP/trailing semantics. On confirmed fills, `BacktestPositionHold` nets base amounts, tracks weighted entry, realized gross PnL and fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view for 1d bars.
- **Fees and accounting:** pin `trade_cost=0.0002` per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount*observed_close`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. The pinned engine's `summarize_results.net_pnl_quote` for POSITION_HOLD can reflect **gross** matched PnL while reporting fees separately; its `pnl_timeseries` also does **not** guarantee a complete fee-inclusive cumulative equity series after flat transitions. **Never** call either output fee-inclusive net equity without reconstructing from actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Price integrity:** validate every observed finite positive `close_bt` before order creation; `BacktestingDataProvider.get_price_by_type` returns `Decimal("1")` for a missing pair (line re-read this cycle) and must **never** supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The page displays per-symbol backtest metrics (Sharpe, return, drawdown, win rate) computed over 20 equity indices with 5 years of daily data, no costs modeled. No exact empirical figure is restated here: per the traceable-provenance rule, figures without pinned table/figure/section values in this read are omitted. No source-reported performance is adopted.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

Cousins fenced as different constructions (none holds long purely on a strict close-vs-single-SMA50 level on `1d`): the admitted disparity-index sibling trades a 14-bar normalized-distance cross-up edge with a sub-zero exit; the admitted golden-cross record trades a 9/50 dual cross plus SMA100 gate on `1h`; the admitted Forven S00139 record trades an SMA20-gated RSI washout-cross with an RSI-overbought exit on `1h`; the admitted Mayer record trades a below-ratio value threshold on a 200DMA multiple. Changing the 50-bar window, the strict comparators, the frame, the size, or adding any oscillator/volatility gate or risk leg would each be a different, unpinned rule — none is admitted here.

## Falsification plan

- F1 — Average-length relevance: replacing SMA50 with SMA20 (same level form, bracket/state/cost unchanged) must not improve net expectancy; fail ⇒ the 50-bar regime choice adds nothing over a faster average.
- F2 — Exit necessity: holding to a 20-bar time exit instead of the sub-average signal exit (same entry/state/cost) must not improve net expectancy; fail ⇒ the symmetric average exit is not the risk leg.

## Crypto portability

Binance BTC-USDT spot 1d only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here.

## Limitations

Researcher-chosen (not source-native): SMA arithmetic-mean freeze (the site's helper body was never printed — only its call is source fact), close-effective fills replacing next-open execution, 0.001 BTC size, 100-bar warmup, 0.0002/side hypothetical cost, re-arm restriction, BTC-USDT spot 1d market pin. No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- https://quantifiedtrader.com/backtest/strategies/price-above-sma (read 2026-10-27; HTTP 200; 42,694-byte page embedding the pinned `n = 50` SMA regime decision code quoted in Provenance)
