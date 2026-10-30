---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FSample RSI-edge TEMA-BBmid slope BTCUSDT spot 1h long-flat derivative
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FSample RSI-edge TEMA-BBmid slope — independent BTC-USDT spot 1h long-flat derivative

## Provenance

**Primary public GitHub identity:** `freqtrade/freqtrade-strategies`, file `user_data/strategies/futures/FSampleStrategy.py`, class `FSampleStrategy(IStrategy)` (the only class in the file). Pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`), returned as the repository `main` HEAD by the GitHub commits API this cycle (2026-10-31). GitHub blob SHA `cb55a9253473697fb7ccb71c8a8fe3454929cd92`, 5413 bytes, 162 lines; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` (SHA-256 `3fcbe2ed16dd097fd6e4548172acbde871bdfe64c5a7341f337f19caf3daa225`) — the entire file was read, not sampled. The file's last-touch commit is `1fea9264fe912d72f1508953edf99ec8ec407e6a` (`2023-02-09T22:39:44Z`, process-candles flag); the bytes are identical at the pinned HEAD, so no newer file revision exists to diverge from.

**The file's own words (quoted for gate evidence, never extended):** `INTERFACE_VERSION: int = 3`; `timeframe = "1h"`; `startup_candle_count: int = 30`; `process_only_new_candles = True`; `minimal_roi = {"0": 1}` (plus a commented-out `{"60": 0.1, "30": 0.2, "0": 0.2}` alternative); `stoploss = -0.05`; `can_short = True`; `trailing_stop = False` with the trailing-only/positive/offset lines present only as comments. Indicators are exactly `ta.ADX`, `ta.RSI`, `ta.STOCHF` (`fastd`/`fastk`), `ta.MACD` (`macd`/`macdsignal`/`macdhist`), `ta.MFI`, `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` into `bb_lowerband`/`bb_middleband`/`bb_upperband` plus derived `bb_percent`/`bb_width`, `ta.SAR`, `ta.TEMA(dataframe, timeperiod=9)` into `tema`, and `ta.HT_SINE` into `htsine`/`htleadsine`. Long entry is the four-way AND of `qtpylib.crossed_above(dataframe["rsi"], 30)`, `tema <= bb_middleband`, `tema > tema.shift(1)`, `volume > 0` setting `enter_long`; short entry is the mirrored `crossed_above(rsi, 70)`, `tema > bb_middleband`, `tema < tema.shift(1)`, `volume > 0` setting `enter_short`. Long exit repeats the short-entry conjunction verbatim setting `exit_long`; short exit repeats the long-entry conjunction verbatim setting `exit_short`.

**Full-file token census (verified by search over the 162 lines this cycle):** 0 `*Parameter(` (the `BooleanParameter`/`CategoricalParameter`/`DecimalParameter`/`IntParameter` names appear only in the dead import block — zero instantiations, zero `.value`, zero `.range`; every trading constant is a file literal); 0 `informative_pairs` / 0 `resample` / 0 `merge_informative`; 0 `position_adjustment` / 0 `adjust_trade_position` / 0 `custom_stake` / 0 `leverage(` / 0 `protections` / 0 `cooldown`; 0 `funding` / 0 `mark_price` / 0 `markprice`; 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `ignore_roi_if_entry_signal` / 0 `order_types` / 0 `order_time_in_force` (framework defaults apply, disclosed below); 1 `startup_candle_count` (`30`); 1 `process_only_new_candles` (`True`); 1 `enter_short` / 1 `exit_short` (legs exist, disabled below); 2 `minimal_roi` (one active `{"0": 1}`, one commented alternative); 1 active `stoploss`; 1 `can_short` (`True`). The file ships no sample, window, trade count, fee basis, win rate, or performance figure of any kind — no source-reported performance is adopted or restated.

**Out-of-file calls pinned (all resolved by name, all literal-or-default):** `ta.RSI(dataframe)` (TA-Lib default `timeperiod=14` pinned by call — live entry/exit edge); `ta.TEMA(dataframe, timeperiod=9)` (explicit 9 — live positional and slope legs); `qtpylib.typical_price` (`(high+low+close)/3`) with `qtpylib.bollinger_bands(..., window=20, stds=2)` returning `mid` into `bb_middleband` (live both legs) with `lower`/`upper` computed but never read by either gating leg (dead columns, fenced below); `qtpylib.crossed_above(series, scalar)` (the verified edge primitive, `technical@78061e9` vendor `indicators.py`, 20422 bytes, blob `2fd7fe263555be9fbd0ca638d70178c482afd71c`, read this cycle — scalar ints are wrapped to a constant Series, so `crossed_above(rsi, 30)` is exactly `(rsi[t]>30)&(rsi[t-1]<=30)`). `ta.ADX` / `ta.STOCHF` / `ta.MACD` / `ta.MFI` / `ta.SAR` / `ta.HT_SINE` outputs plus `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width` are computed but never read by any entry/exit leg — dead columns, never gating evidence. `numpy`/`pandas` are imported but only the `DataFrame` type is used; the `BooleanParameter`-family imports are fully dead (zero uses after import).

**Non-adopted source machinery (disclosed, never silently re-based):** the `{"0": 1}` ROI ladder (+100% target — coded but economically inert) and the `-0.05` stoploss are Freqtrade time/profit machinery; neither is adopted as an intrabar semantic. The file names no market, venue, fill-timing flag, position size, or warmup beyond the 30-bar seed. `can_short = True` is an explicit file literal enabling the short legs — explicitly disabled below.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 1h, long/flat only**; pin the file-literal RSI(14)/TEMA9/BBmid(20,2-on-typical) construction and both `crossed_above` long/short edges; keep the file's long-exit conjunction (identical to the short-entry conjunction) as the **sole** signal exit; explicitly disable the short legs (`enter_short`/`exit_short` never armed) and the entire ROI/stop block (the exit leg needs no profit trigger; trailing is already `False` in source); fix one `0.001 BTC` base-size position, one-position-only, no DCA, no cooldown; fix a 60-completed-bar warmup (researcher hardening over the file's 30-bar seed); and the state/timing/cost rules below. All changes are part of this **separate strategy**, not evidence that the source file is expressible unchanged. This follows the admitted `futures/TrendFollowingStrategy` and `futures/FOttStrategy` sibling precedents (long-only, risk block disabled, signal-exit-only).

**Immutable research identity:** `FT-FSampleStrategy-f3340ce | derived-v1-RSI14-x30-TEMA9-BBmid20-slope-edge | BTC-USDT-binance-spot-1h | signal-exit-only | 2026-10-31`. Changing any component changes the derivative identity.

**Pre-write dedup:** main `3b012bc9`, 468 root-level strategy Markdown records. Working-tree search for `FSample`/`fsample` returns nothing. Twelve open `research/*` PRs examined by title and source — none uses this file or rule. Nearest families are materially different: `freqtrade-quickie-tema-slope-bbmid-adx-gated` (5m level-state system — `adx>30`/`adx>70` strength gates plus `sma_200>close` filter, no RSI edge, different exits, different frame); `forven-tema-cross` (dual-TEMA 12/26 pure edge-cross, no Bollinger rail, no RSI gate, no slope-vs-mid conjunction); `freqtrade-multima-tema-stack-trend` (multi-MA TEMA stack trend, no RSI-edge/BBmid-slope conjunction); the RSI-cross pool records gate on RSI thresholds without the TEMA9-vs-BBmid positional-plus-slope conjunction. This candidate is the only RSI14-edge × TEMA9-vs-BBmid-positional × TEMA-slope triple conjunction with a mirrored signal exit on `1h`. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where short-horizon momentum crosses up through oversold (RSI crossing above 30) while lag-reduced trend sits beneath its own mean but turns up (TEMA9 at or below the 20-bar Bollinger midline and rising bar-over-bar), and stand aside when the mirror overheated print arrives (RSI crossing above 70 with TEMA9 above its midline and falling); a +100% ROI target and a −5% stoploss backstop positions under Freqtrade execution, with the short side mirroring both prints. The file ships no market, sample, or performance claim — this record adopts no source-reported performance (see Evidence).

### Research interpretation

A turn-gated mean-position buyer with an oscillator key: the RSI edge refuses stale oversold (a bar that has sat below 30 without crossing prints nothing), the positional leg refuses extended recoveries (a TEMA already stretched above its midline prints nothing on the long side), and the slope leg refuses falling knives (a sub-mid TEMA still falling prints nothing). All three must agree on the same completed bar. The exit is the exact mirror — an overheated RSI edge with an above-mid falling TEMA — so a long is carried through ordinary chop that never prints the full overheated conjunction, and surrendered only on the Washout-to-euphoria mirror print. Disabling the +100%/−5% risk block removes the file's inert profit target and leaves the position's entire fate on the declared signal exit — an underwater drift that never prints the mirror conjunction is held, not forgiven.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 1h OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 3600 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback.

**Features (source-faithful, file literals):** `rsi[t]=TA-Lib RSI(C,14)` (default period pinned by call, Wilder smoothing); `tema[t]=TA-Lib TEMA(C,9)` (explicit 9); `typical[t]=(H[t]+L[t]+C[t])/3`; `bbmid[t]=SMA(typical,20)[t]` (explicit window 20, 2-std bands computed but unused). NaN-leading comparisons and edges are false, so pre-seed bars could never fire in any case.

**Completed-bar long entry predicate `E[t]`** (exact conjunction, no epsilon): `XUP(rsi,30)[t] & (tema[t]<=bbmid[t]) & (tema[t]>tema[t-1]) & (V[t]>0)` with `XUP(a,b)[t]=(a[t]>b)&(a[t-1]<=b)` (the verified `crossed_above` scalar primitive), `t>=60`, every required feature valid, no pending order, FLAT and re-arm state true. No funding/OI/mark-price read anywhere in the gating path.

**Signal exit `X[t]`** (mirrored conjunction, strict): `XUP(rsi,70)[t] & (tema[t]>bbmid[t]) & (tema[t]<tema[t-1]) & (V[t]>0)` — true only on bars printing the full overheated conjunction. An open LONG closes on the first `X[t]` bar with `t` past the entry fill bar.

**Co-fire pin (proven mutually exclusive, disclosed, not repaired):** `E[t]` needs `tema<=bbmid` plus rising slope while `X[t]` needs `tema>bbmid` plus falling slope — position and slope are each strictly complementary, so no bar can satisfy both even when RSI jumps from `<=30` to `>70` in one bar. Entry and exit therefore never execute on the same bar in the same direction of travel. ROI/stop legs do not exist in this derivative, so no further ordering is invented.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. The file's `enter_short`/`exit_short` legs are explicitly disabled despite the file-literal `can_short = True`.

**Risk (Gate 3, explicit):** the mirrored-conjunction signal exit is the sole position-ending path (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — the exit fires even at a loss; disclosed defaults, never file literals). The file's `{"0": 1}` ROI ladder and `-0.05` stoploss are explicitly disabled (see Provenance) — no profit trigger, no stop level, no trailing (already `False` in source), no time stop, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default.

**State (Gate 4):** `FLAT_DISARMED`, `FLAT_ARMED`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT_ARMED` after 60 valid completed bars **only if E without the state clause was false on the immediately prior completed bar**; otherwise wait for a false bar to arm. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET fill at the next completed close transitions to LONG. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT_DISARMED. Once flat, require at least one **subsequent** completed bar with the non-state entry predicate false to re-arm. No same-bar SELL+BUY, no pyramiding, **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding, no session/cooldown. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 60 contiguous completed 1h bars before the first actionable bar; covers the RSI14 Wilder seed, the TEMA9 triple-EMA seed, the 20-bar Bollinger seed, the one-bar slope/edge lookback, and the arming rule, plus margin over the file's 30-bar seed. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Unseeded windows stay NaN and every NaN comparison is false — no leg can fire early. The file's own `process_only_new_candles = True` is preserved (one evaluation per completed bar).

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and every derived line become available no earlier than `T[t]+3600s`. All decisions and fills are effective at completed-bar closes. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used — every lag call is `shift(1)` or the one-bar edge lookback, all strictly backward. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (verified an ancestor of the local checkout `2dbc844` this cycle; `hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`, content read this cycle). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`, verified at the pinned commit this cycle) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, INTERVALS `"1h"` entry read this cycle) supports `1h`. Connector `binance`, pair `BTC-USDT`, one spot 1h stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision beyond the trivial `V>0` liveness guard, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6` (chain names and `trade_cost=0.0002` default read this cycle). A **strategy-specific, not-yet-implemented** controller must calculate the exact RSI/TEMA/BBmid state and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` (`hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, code read this cycle) fills at the first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar stop fill. Explicitly no stop/limit/maker order is ever queued, so the disabled file-level stop can never leak back through an executor semantic. On confirmed fills, the hold nets base amounts with weighted entry and realized gross PnL plus recorded fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end.
- **Fees and accounting:** pin `trade_cost=0.0002` (the default on the pinned `run_backtesting` signature, line read this cycle) per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount_quote`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. Never treat engine PnL outputs as fee-inclusive net equity without reconstructing from the actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Price integrity:** validate every observed finite positive `close_bt` before order creation; `BacktestingDataProvider.get_price_by_type` returns `Decimal("1")` for a missing pair (line 140 read this cycle) and must **never** supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships no sample, window, trade count, fee basis, or performance figure of any kind. No source-reported performance is adopted or restated. The only commented alternative is the `{"60": 0.1, "30": 0.2, "0": 0.2}` ROI ladder — disclosed as a comment, never a live leg.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

Cousins fenced as different constructions (none trades an RSI14-edge × TEMA9-vs-BBmid-positional × TEMA-slope triple conjunction with a mirrored signal exit on `1h`): the admitted `freqtrade-quickie-tema-slope-bbmid-adx-gated` is a 5m persistent level-state system gated by `adx>30`/`adx>70` plus an `sma_200>close` filter with no RSI edge anywhere; the admitted `forven-tema-cross` is a dual-TEMA pure edge-cross with no Bollinger rail and no RSI gate; the admitted `freqtrade-multima-tema-stack-trend` is a multi-MA stack trend with no RSI-edge/BBmid-slope conjunction; the admitted `freqtrade-supertrend-triple-agreement` requires three supertrend agreements plus a volume gate; every RSI-threshold pool record fires on RSI levels without the TEMA9-vs-BBmid positional-plus-slope conjuncts. Changing any pinned constant (RSI period/thresholds, TEMA period, BB window/stds, typical-price source), frame, book, or re-enabling any risk/short leg would each be a different, unpinned rule — none is admitted here.

## Falsification plan

- F1 — Oscillator-key necessity: replacing the `XUP(rsi,30)` edge with an always-true oscillator leg (same TEMA positional/slope/exit/state/cost) must not improve net expectancy; fail ⇒ the RSI-edge key adds nothing over the pure TEMA/BBmid system.
- F2 — Slope-leg relevance: replacing the `tema>tema.shift(1)` rising-slope conjunct (and its mirror) with position-only legs (same RSI edges, same BBmid rails, same exits) must not improve net expectancy; fail ⇒ the slope turn-gate adds nothing over a static sub-mid/over-mid system.

## Crypto portability

Binance BTC-USDT spot 1h only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here.

## Limitations

Researcher-chosen (not source-native): long-only disablement of the file's short legs despite file-literal `can_short = True`, full disablement of the `{"0": 1}` ROI ladder and `-0.05` stoploss, 60-bar warmup hardening over the file's 30-bar seed, 0.001 BTC size, 0.0002/side hypothetical cost, re-arm restriction, full-sample indicator evaluation. TA-Lib version sensitivity of RSI/TEMA/BB beyond the pinned call semantics is unverified. No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- Primary: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py (commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, blob `cb55a9253473697fb7ccb71c8a8fe3454929cd92`, 5413 bytes / 162 lines, verified this cycle; file last touched by `1fea9264fe912d72f1508953edf99ec8ee407e6a`)
- Edge primitive: `technical@78061e9` `technical/vendor/qtpylib/indicators.py` (20422 bytes, blob `2fd7fe263555be9fbd0ca638d70178c482afd71c`; `crossed`/`crossed_above` scalar handling read this cycle)
- Engine: Hummingbot package `20260920`, VERSION `dev-2.17.0`, `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (file blobs cited inline, verified this cycle)
