---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Low_BB 0.98 sub-lower-band dip BTCUSDT spot 1m long-flat close-bracket derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/Low_BB.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Low_BB 0.98× sub-lower-band dip — independent BTC-USDT spot 1m long-flat derivative

## Provenance

**Primary public GitHub identity:** `freqtrade/freqtrade-strategies`, file `user_data/strategies/berlinguyinca/Low_BB.py`, class `Low_BB(IStrategy)` (the only class in the file). Pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, verified as the repository HEAD via `git ls-remote` this cycle (2026-10-27). GitHub blob SHA `0a3c5401d605e1690d252ac8407e63cc349a6e61`, 3642 bytes, 109 lines; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` — the entire file was read, not sampled.

**The file's own words (quoted for gate evidence, never extended):** `author@: Thorsten`; idea: `buy after crossing .98 * lower_bb and sell if trailing stop loss is hit`; `INTERFACE_VERSION: int = 3`; `minimal_roi = { "0": 0.9, "1": 0.05, "10": 0.04, "15": 0.5 }`; `stoploss = -0.015`; `timeframe = '1m'`. Entry is the single condition `(dataframe['close'] <= 0.98 * dataframe['bb_lowerband'])` setting `enter_long = 1`. The exit block writes `dataframe.loc[(), 'exit_long'] = 1` — an **empty selector, so the signal-exit column is never set on any bar**. No `startup_candle_count`, no `trailing`, no `max_open_trades`, no `position_adjustment`, no `order_types`, no `can_short`, no `leverage`, no `funding`/`mark_price` ships anywhere in the 109 lines.

**Dead code fenced (read, never gated):** `populate_indicators` computes Bollinger bands twice — first over `qtpylib.typical_price(dataframe)`, then **overwritten** by the second computation over `dataframe['close']` (same `window=20, stds=2`); only the close-based assignment survives, so the typical-price block has no downstream effect and this record treats the rule as single-feed close-only. `ta.MACD` columns are computed but never read by any order line. `CCI`/`MFI`/`RSI(7)` lines are commented out and absent. The docstring's `trailing stop loss` has no trailing configuration in code — prose/code mismatch disclosed; no trailing is adopted.

**Non-adopted source machinery (disclosed, never silently re-based):** the four-leg `minimal_roi` ladder is non-monotonic (`"15": 0.5` demands 50% after 15 minutes) and is Freqtrade intrabar time-ROI machinery this record does not model; the `-0.015` stoploss is Freqtrade intrabar low-touch machinery. Neither is adopted as an intrabar semantic.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 1m, long/flat only**; pin close-based BB20 population-σ ×2, single entry `C ≤ 0.98 × lower`, **no signal exit** (source-faithful: the empty exit column), derived **close-confirmed** fixed bracket TP `+5%` / SL `−1.5%` evaluated from the next completed bar (close evaluation replaces the non-modeled intrabar ROI/stop machinery; the −1.5% level reuses the source's stop number, the +5% target reuses the source ladder's operative 1-minute leg — both disclosed researcher replacements, not source order semantics), fixed 0.001 BTC, no trailing, single position, safety orders/DCA explicitly disabled, and the state/timing/cost rules below. All changes are part of this **separate strategy**, not evidence that the source file is expressible unchanged.

**Immutable research identity:** `FT-Low_BB-Thorsten-f3340ce | derived-v1-closeBB20x2-pop-entry098-no-signal-exit | BTC-USDT-binance-spot-1m | close-bracket-TP5p0-SL1p5 | 2026-10-27`. Changing any component changes the derivative identity.

**Pre-write dedup:** main SHA `9dad4fa8580f711e09f9dc3dff15cec68e5f17ea`, 381 root-level strategy Markdown records; README static count 381. Working-tree search for `Low_BB`/`low-bb` returns only the sibling-fence mention in `freqtrade-technical-cmf-sign-state` (different pin, fenced there); search for `0.98` returns only unrelated constants (Cluc `0.985` discount leg, ATR/fee decimals). Ten open `research/*` PRs examined by title and source — none uses this file or rule. Nearest families are materially different: `freqtrade-bband-rsi-dip-buy` (1h, RSI<30 AND typical-price-BB20-lower conjunction, RSI>70 signal exit, +10%/−25%); `freqtrade-combined-binh-cluc` (5m dual-leg penetration with body/tail guards and pump cap, profit-gated midline exit); `freqtrade-cofibit` (5m stochf-rail ADX-gated system). This candidate is the only single-condition 0.98-depth discount trigger with no signal exit on 1m. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar whose close sits at least 2% beneath the lower BB(20, 2σ) band (a deep-band-washout dip, not a band touch); no signal exit is ever printed; a time-ROI ladder and a −1.5% stoploss backstop every position under Freqtrade execution. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

A one-key washout catcher, long-only. Unlike conjunction records (RSI AND band, ADX AND rail), the single depth condition fires on any sufficiently stretched close with no momentum confirmation — fewer, deeper prints. Unlike touch/reclaim records, 0.98× demands continuation past the band, refusing shallow tags. Because the source never prints a signal exit, the position's entire fate under this derivative rests on the declared close bracket: underwater drift that never reaches −1.5% at a close is held, not forgiven; chop oscillating between the levels holds the book long. The coded consequence is a buyer of confirmed deep-band weakness that harvests only measured close-confirmed recoveries.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 1m OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 60 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback.

**BB20 (researcher-pinned, population σ):** for `t>=19`, `basis[t]=sum(C[t-19..t])/20`; `sigma[t]=sqrt(sum((C[i]-basis[t])^2 for i=t-19..t)/20)` (population divisor 20); `lower[t]=basis[t]-2*sigma[t]`; `upper[t]=basis[t]+2*sigma[t]`. Single close feed; the source's overwritten typical-price block is not a second input. No shifted bands or fitted inputs.

**Completed-bar long entry predicate `E[t]`** (both true): `C[t] <= 0.98*lower[t]` (non-strict — a close exactly at 0.98× fires), and `t>=100`, every required feature valid, no pending order, FLAT and re-arm state true. No RSI/MACD/volume/funding read anywhere in the gating path.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. Zero short tokens ship in the source file.

**Derived close bracket (Gate 3):** upon confirmed BUY at observed `entry_close=C[t]`, freeze `tp=1.05*entry_close`, `sl=0.985*entry_close`. Require both finite with `sl>0`; otherwise no entry. Starting at the **next completed bar** after entry, while LONG, request full SELL if `C[t]<=sl` (stop, checked first) else if `C[t]>=tp` (target). TP/SL regions are disjoint so check order is immaterial and both can never trigger on the same close. Hold otherwise. **Both are close-confirmed MARKET research exits, not intrabar touches or resting protective stop/limit orders** — the pinned backtest path below offers no verified intrabar-stop semantic, so none is claimed. No signal exit (source-faithful empty exit), no trailing (source has none configured), no time stop, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default. All bracket levels are **close-price returns**, never leveraged/net returns (spot, leverage 1).

**State (Gate 4):** `FLAT_DISARMED`, `FLAT_ARMED`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT_ARMED` after 100 valid completed bars **only if E without the state clause was false on the immediately prior completed bar**; otherwise wait for a false bar to arm. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET POSITION_HOLD fill at that same completed close transitions to LONG and freezes entry price/levels. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT_DISARMED. Once flat, require at least one **subsequent** completed bar with the non-state entry predicate false to re-arm. No same-bar SELL+BUY, no pyramiding, **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding, no session/cooldown. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous completed 1m bars before the first actionable bar; covers the 20-bar band seed and the arming rule. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Unseeded windows stay NaN and every NaN comparison is false — no leg can fire early.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and derived band become available no earlier than `T[t]+60s`. All decisions and the synthetic model fill are effective at that **completed-bar close**. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`, content read this cycle). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, INTERVALS read this cycle) supports `1m`. Connector `binance`, pair `BTC-USDT`, one spot 1m stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.update_processed_data` → `prepare_market_data` → per-row `update_state` → `determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`. A **strategy-specific, not-yet-implemented** controller must calculate the exact band/state and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, code read this cycle) fills fully at first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar stop fill. The pinned `PositionExecutorSimulator` is **not** used because its stop tests candle `low` and its TP uses a strict `>` on fee-adjusted close returns — semantics this record does not claim; the derived bracket is evaluated by the controller on completed closes and executed as MARKET closes instead. On confirmed fills, `BacktestPositionHold` nets base amounts, tracks weighted entry, realized gross PnL and fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view for 1m bars.
- **Fees and accounting:** pin `trade_cost=0.0002` per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount*observed_close`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. The pinned engine's `summarize_results.net_pnl_quote` for POSITION_HOLD can reflect **gross** matched PnL while reporting fees separately; its `pnl_timeseries` also does **not** guarantee a complete fee-inclusive cumulative equity series after flat transitions. **Never** call either output fee-inclusive net equity without reconstructing from actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Price integrity:** validate every observed finite positive `close_bt` before order creation; `BacktestingDataProvider.get_price_by_type` returns `Decimal("1")` for a missing pair (line read this cycle) and must **never** supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships no sample, window, trade count, fee basis, or performance figure of any kind. No source-reported performance is adopted or restated.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

Cousins fenced as different constructions (none trades a single 0.98-depth close-band dip with no signal exit on `1m`): the admitted BbandRsi sibling requires an RSI<30 AND typical-price-band conjunction with an RSI>70 signal exit on `1h`; the admitted CombinedBinHAndCluc sibling requires penetration microstructure guards plus a pump cap with a profit-gated midline exit on `5m`; the admitted CofiBit sibling is a stochf-rail ADX-gated system on `5m`. Changing the 0.98 factor, band basis/σ convention, frame, bracket levels, or adding any signal exit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

- F1 — Depth relevance: replacing the 0.98 factor with a plain band touch (`C < lower`, same bracket/state/cost) must not improve net expectancy; fail ⇒ the depth margin adds nothing over a touch.
- F2 — Bracket necessity: holding to the next opposite entry-armless flat (signal-exit-free hold with only the −1.5% close stop, no +5% target) must not improve net expectancy; fail ⇒ the fixed target is not the harvesting leg.

## Crypto portability

Binance BTC-USDT spot 1m only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here.

## Limitations

Researcher-chosen (not source-native): population-σ band arithmetic (the author's runtime qtpylib internal rolling arithmetic was not byte-pinned — only the call `window=20, stds=2` is source fact), +5% close target replacing intrabar ROI machinery, close evaluation replacing intrabar low-touch stop semantics, 0.001 BTC size, 100-bar warmup, 0.0002/side hypothetical cost, re-arm restriction. No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.
