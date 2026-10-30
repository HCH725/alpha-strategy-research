---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BinHV45 BB40 penetration microstructure tail-gated BTCUSDT spot 1m long-flat close-bracket derivative
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-31
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BinHV45.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BinHV45 BB40 penetration microstructure — independent BTC-USDT spot 1m long-flat derivative

## Provenance

**Primary public GitHub identity:** `freqtrade/freqtrade-strategies`, file `user_data/strategies/berlinguyinca/BinHV45.py`, class `BinHV45(IStrategy)` (the only class in the file). Pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, verified as the repository HEAD via `git ls-remote` this cycle (2026-10-31). GitHub blob SHA `c03bd418a95daddddc6f76cc320ffee9151627a5`, 2641 bytes, 71 lines; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` — the entire file was read, not sampled.

**The file's own words (quoted for gate evidence, never extended):** `INTERFACE_VERSION: int = 3`; `minimal_roi = { "0": 0.0125 }`; `stoploss = -0.05`; `timeframe = '1m'`. Indicators are `qtpylib.bollinger_bands(dataframe['close'], window=40, stds=2)` with `upper`/`mid`/`lower` columns read, plus `bbdelta = (mid-lower).abs()`, `pricedelta = (open-close).abs()`, `closedelta = (close-close.shift()).abs()`, `tail = (close-low).abs()`. Entry is the six-leg conjunction setting `enter_long = 1`: `lower.shift().gt(0)`, `bbdelta.gt(close*buy_bbdelta.value/1000)`, `closedelta.gt(close*buy_closedelta.value/1000)`, `tail.lt(bbdelta*buy_tail.value/1000)`, `close.lt(lower.shift())`, `close.le(close.shift())`, with pinned `buy_params = { "buy_bbdelta": 7, "buy_closedelta": 17, "buy_tail": 25 }`. The exit block writes `dataframe.loc[:, 'exit_long'] = 0` under the docstring `no sell signal` — the signal-exit column is never set on any bar. No `startup_candle_count`, no `trailing`, no `max_open_trades`, no `position_adjustment`, no `order_types`, no `can_short`, no `leverage`, no `funding`/`mark_price` ships anywhere in the 71 lines.

**Dead code fenced (read, never gated):** the module-level `def bollinger_bands(stock_price, window_size, num_of_std)` helper (lines 12–17) is never called — the only band source is the `qtpylib` call; its pandas sample-σ body has no downstream effect. `pricedelta` is computed but never read by the entry conjunction. `import talib.abstract as ta` and `import numpy as np` are never referenced after import. None of these contribute any leg, threshold, or exit.

**Band arithmetic pinned source-faithful:** the call resolves through `freqtrade.vendor.qtpylib` → `technical` `vendor/qtpylib/indicators.py` (`technical@00190d7f`, 19724 bytes): `bollinger_bands(series, window, stds)` = `ma = rolling_mean(series, window, min_periods=1)`, `std = rolling_std(series, window, min_periods=1)` (pandas `rolling(window, min_periods=1)` path: mean plus sample σ, ddof=1), `upper = ma+std*stds`, `lower = ma-std*stds`, `mid = ma`, returned as `upper`/`mid`/`lower`. This record adopts exactly that arithmetic for fully seeded windows (see Signal) and does **not** adopt the source runtime's degenerate early regime (`min_periods=1` lets bands print on 1–39 bars); pre-seed bars are warmup, disclosed below as a researcher hardening, not source order semantics.

**Non-adopted source machinery (disclosed, never silently re-based):** the single-leg `minimal_roi` (`"0": 0.0125`) is Freqtrade intrabar time-ROI machinery and the `-0.05` stoploss is Freqtrade intrabar low-touch machinery; neither is adopted as an intrabar semantic.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 1m, long/flat only**; pin close-feed BB40 sample-σ ×2, the six-leg entry with pinned 7/17/25, **no signal exit** (source-faithful: the exit column is identically zero), derived **close-confirmed** fixed bracket TP `+1.25%` / SL `−5%` evaluated from the next completed bar (close evaluation replaces the non-modeled intrabar ROI/stop machinery; both levels reuse the source's own numbers — disclosed researcher replacements, not source order semantics), fixed 0.001 BTC, no trailing, single position, safety orders/DCA explicitly disabled, and the state/timing/cost rules below. All changes are part of this **separate strategy**, not evidence that the source file is expressible unchanged.

**Immutable research identity:** `FT-Berlinguyinca-BinHV45-f3340ce | derived-v1-BB40s2-close-6leg-7-17-25-no-signal-exit | BTC-USDT-binance-spot-1m | close-bracket-TP1p25-SL5p0 | 2026-10-31`. Changing any component changes the derivative identity.

**Pre-write dedup:** main `6da4f0d1`, 466 root-level strategy Markdown records; README static count 466. Working-tree search for `BinHV45`/`binhv45` returns nothing. Twelve open `research/*` PRs examined by title and source — none uses this file or rule. Nearest families are materially different: `freqtrade-binhv27-rsi-adx-di-regime` (5m RSI/ADX/DI regime with SMA240 trend states and a signal exit — a different indicator family, no bands); `freqtrade-low-bb-98-sub-band-dip` (1m single-condition 0.98-depth discount, BB20, no microstructure gates); `freqtrade-bband-rsi-dip-buy` (1h RSI<30 AND typical-price-BB20 conjunction with RSI>70 exit); `freqtrade-combined-binh-cluc` (5m dual-leg penetration with body/tail guards and pump cap); `freqtrade-bandtastic-1sig` (15m lower-band/MFI conjunction); `fmz-483087-triple-bollinger` (simultaneous triple-band breach); `forven-bb-edge-fade` / `forven-bb-squeeze` (edge-fade and squeeze-breakout, not penetration-plus-expansion). This candidate is the only BB40 penetration with band-expansion, momentum, and tail-cap microstructure and no signal exit on 1m. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar whose close penetrates below the prior bar's lower BB(40, 2σ) band while the band is expanded (`bbdelta` above 0.7% of price), the bar moved (`closedelta` above 1.7% of price), the lower wick is short (`tail` below 2.5% of half-width), and the close did not rise — a volatility-expanded washout print with no lower shadow reclaim; no signal exit is ever printed; a flat 1.25% time-ROI and a −5% stoploss backstop every position under Freqtrade execution. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

A six-key washout catcher, long-only. Unlike single-condition dip records (depth touch) it demands expansion plus motion plus shape: the band must be stretched, the bar must have travelled, and the close must sit at the low with a stub wick — refusing shallow tags, drift penetrations in dead bands, and long-tailed rejections alike. Because the source never prints a signal exit, the position's entire fate under this derivative rests on the declared close bracket: underwater drift that never reaches −5% at a close is held, not forgiven; chop between the levels holds the book long. The coded consequence is a buyer of confirmed expanded-band weakness that harvests only measured close-confirmed recoveries.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 1m OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 60 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback.

**BB40 (source-faithful, sample σ):** for `t>=39`, `basis[t]=sum(C[t-39..t])/40`; `sigma[t]=sqrt(sum((C[i]-basis[t])^2 for i=t-39..t)/39)` (sample divisor 39, pandas `.std()` ddof=1); `lower[t]=basis[t]-2*sigma[t]`; `mid[t]=basis[t]`; `upper[t]=basis[t]+2*sigma[t]`. Single close feed. For `t<39` all five stay NaN and every comparison on them is false — no leg can fire early. The `min_periods=1` degenerate regime is never traded (warmup below).

**Microstructure columns:** `bbdelta[t]=|mid[t]-lower[t]|` (=`2*sigma[t]`); `closedelta[t]=|C[t]-C[t-1]|`; `tail[t]=|C[t]-L[t]|`. All NaN until their inputs are valid; NaN comparisons are false.

**Completed-bar long entry predicate `E[t]`** (all six true, strictness exactly as coded — no epsilon): `lower[t-1] > 0` (positivity guard), `bbdelta[t] > C[t]*7/1000`, `closedelta[t] > C[t]*17/1000`, `tail[t] < bbdelta[t]*25/1000`, `C[t] < lower[t-1]` (strict penetration against the prior completed band), `C[t] <= C[t-1]` (non-strict — an unchanged close still fires), and `t>=100`, every required feature valid, no pending order, FLAT and re-arm state true. No RSI/MACD/volume/funding read anywhere in the gating path.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. Zero short tokens ship in the source file.

**Derived close bracket (Gate 3):** upon confirmed BUY at observed `entry_close=C[t]`, freeze `tp=1.0125*entry_close`, `sl=0.95*entry_close`. Require both finite with `sl>0`; otherwise no entry. Starting at the **next completed bar** after entry, while LONG, request full SELL if `C[t]<=sl` (stop, checked first) else if `C[t]>=tp` (target). TP/SL regions are disjoint so check order is immaterial and both can never trigger on the same close. Hold otherwise. **Both are close-confirmed MARKET research exits, not intrabar touches or resting protective stop/limit orders** — the pinned backtest path below offers no verified intrabar-stop semantic, so none is claimed. No signal exit (source-faithful zero exit), no trailing (source has none configured), no time stop, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default. All bracket levels are **close-price returns**, never leveraged/net returns (spot, leverage 1).

**State (Gate 4):** `FLAT_DISARMED`, `FLAT_ARMED`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT_ARMED` after 100 valid completed bars **only if E without the state clause was false on the immediately prior completed bar**; otherwise wait for a false bar to arm. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET POSITION_HOLD fill at that same completed close transitions to LONG and freezes entry price/levels. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT_DISARMED. Once flat, require at least one **subsequent** completed bar with the non-state entry predicate false to re-arm. No same-bar SELL+BUY, no pyramiding, **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding, no session/cooldown. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous completed 1m bars before the first actionable bar; covers the 40-bar band seed, the one-bar shift reads, and the arming rule. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Unseeded windows stay NaN and every NaN comparison is false — no leg can fire early.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and derived band become available no earlier than `T[t]+60s`. All decisions and the synthetic model fill are effective at that **completed-bar close**. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of the local checkout HEAD; `hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`, content read this cycle). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, INTERVALS read this cycle) supports `1m`. Connector `binance`, pair `BTC-USDT`, one spot 1m stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.update_processed_data` → `prepare_market_data` → per-row `update_state` → `determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`. A **strategy-specific, not-yet-implemented** controller must calculate the exact band/state and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, code read this cycle) fills at the first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar stop fill. The pinned `PositionExecutorSimulator` is **not** used because its stop tests candle `low` and its TP uses a strict `>` on fee-adjusted close returns — semantics this record does not claim; the derived bracket is evaluated by the controller on completed closes and executed as MARKET closes instead. On confirmed fills, `BacktestPositionHold` nets base amounts, tracks weighted entry, realized gross PnL and fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view for 1m bars.
- **Fees and accounting:** pin `trade_cost=0.0002` per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount_quote`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. The pinned engine's `summarize_results.net_pnl_quote` for POSITION_HOLD can reflect **gross** matched PnL while reporting fees separately; its `pnl_timeseries` also does **not** guarantee a complete fee-inclusive cumulative equity series after flat transitions. **Never** call either output fee-inclusive net equity without reconstructing from actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Price integrity:** validate every observed finite positive `close_bt` before order creation; `BacktestingDataProvider.get_price_by_type` returns `Decimal("1")` for a missing pair (line read this cycle) and must **never** supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships no sample, window, trade count, fee basis, or performance figure of any kind. No source-reported performance is adopted or restated.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

Cousins fenced as different constructions (none trades a six-leg BB40 penetration-plus-expansion with a tail cap and no signal exit on `1m`): the admitted BinHV27 sibling is an RSI/ADX/DI regime system with SMA240 trend states on `5m`; the admitted Low_BB sibling is a single-condition 0.98-depth discount on BB20 with no microstructure gates; the admitted BbandRsi sibling requires an RSI<30 conjunction with an RSI>70 signal exit on `1h`. Changing any pinned constant (7/17/25), band window/σ convention, frame, bracket levels, or adding any signal exit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

- F1 — Microstructure relevance: the plain penetration rule (only `C[t] < lower[t-1]` with the same bracket/state/cost) must not improve net expectancy; fail ⇒ the expansion/momentum/tail gates add nothing over a touch.
- F2 — Bracket necessity: holding to a stop-only flat (no `+1.25%` target, only the `−5%` close stop) must not improve net expectancy; fail ⇒ the fixed target is not the harvesting leg.

## Crypto portability

Binance BTC-USDT spot 1m only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here.

## Limitations

Researcher-chosen (not source-native): full-window seeding with the degenerate `min_periods=1` early regime excluded from trading, `+1.25%` close target and `−5%` close evaluation replacing intrabar ROI/stop machinery, 0.001 BTC size, 100-bar warmup, 0.0002/side hypothetical cost, re-arm restriction. No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- Primary: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BinHV45.py (commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, blob `c03bd418a95daddddc6f76cc320ffee9151627a5`, 2641 bytes / 71 lines, verified this cycle)
- Band arithmetic: `technical@00190d7f` `technical/vendor/qtpylib/indicators.py` (19724 bytes; `bollinger_bands`/`rolling_mean`/`rolling_std` read this cycle)
- Engine: Hummingbot package `20260920`, VERSION `dev-2.17.0`, `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (file blobs cited inline, verified this cycle)
