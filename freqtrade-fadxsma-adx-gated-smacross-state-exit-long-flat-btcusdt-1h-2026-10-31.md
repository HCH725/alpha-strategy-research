---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FAdxSma ADX-gated SMA-cross state-exit BTCUSDT spot 1h long-flat derivative
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FAdxSmaStrategy.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FAdxSma ADX-gated SMA-cross state-exit — independent BTC-USDT spot 1h long-flat derivative

## Provenance

**Primary public GitHub identity:** `freqtrade/freqtrade-strategies`, file `user_data/strategies/futures/FAdxSmaStrategy.py`, class `FAdxSmaStrategy(IStrategy)` (the only class in the file). Pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`), returned as the repository `main` HEAD by the GitHub commits API this cycle (2026-10-31). GitHub blob SHA `3bb13caf079e8360a959c3ad4dd2b2507f3045c0`, 4091 bytes, 130 lines; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` (SHA-256 `43ae02ecca4553b8a609d4533cb4d5b6517292d35b41fc4c77f54f8e959ced89`) — the entire file was read, not sampled. The file's last-touch commit is `d2e8721595931d9c5f4504acfeea381bc3f416e4` (`2025-12-20T14:11:06Z`, explicit space parameters); the bytes are identical at the pinned HEAD, so no newer file revision exists to diverge from.

**The file's own words (quoted for gate evidence, never extended):** `INTERFACE_VERSION: int = 3`; `timeframe = "1h"`; `startup_candle_count: int = 14`; `process_only_new_candles = True`; `minimal_roi = {"60": 0.075, "30": 0.1, "0": 0.05}` (plus a commented-out `{"0": 1}` alternative); `stoploss = -0.05`; `can_short = True`; `trailing_stop = False` with the trailing-only/positive/offset lines present only as comments. Hyperopt spaces are exactly `pos_entry_adx = DecimalParameter(15, 40, decimals=1, default=30.0, space="buy")`, `pos_exit_adx = DecimalParameter(15, 40, decimals=1, default=30.0, space="sell")`, `adx_period = IntParameter(4, 24, default=14, space='buy')`, `sma_short_period = IntParameter(4, 24, default=12, space='buy')`, `sma_long_period = IntParameter(12, 175, default=48, space='buy')`. Long entry is the two-way AND of `dataframe["adx_14"] > 30.0` and `qtpylib.crossed_above(sma_short_12, sma_long_48)` setting `enter_long`; short entry mirrors with `crossed_below` setting `enter_short`. Both exits are the single state leg `dataframe["adx_14"] < self.pos_entry_adx.value` — the **entry** parameter's value, not `pos_exit_adx` — setting `exit_long` and `exit_short`.

**Full-file token census (verified by search over the 130 lines this cycle):** 5 `*Parameter(` instantiations (2 Decimal + 3 Int, all default-pinned below); 0 `informative_pairs` / 0 `resample` / 0 `merge_informative`; 0 `position_adjustment` / 0 `adjust_trade_position` / 0 `custom_stake` / 0 `leverage(` / 0 `protections` / 0 `cooldown`; 0 `funding` / 0 `mark_price` / 0 `markprice`; 0 `volume` (no volume read anywhere in the gating path — pure price-derived); 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `order_types` / 0 `order_time_in_force` (framework defaults apply, disclosed below); 1 `startup_candle_count` (`14`); 1 `process_only_new_candles` (`True`); 1 `enter_short` / 1 `exit_short` (legs exist, disabled below); 1 `crossed_above` / 1 `crossed_below` (the two entry edges); 3 `minimal_roi` (one active ladder, one commented alternative, one design comment); 1 active `stoploss`; 1 `can_short` (`True`). `.value` is read 7 times and only from four parameters — `pos_exit_adx.value` is **never** read anywhere (dead search-space declaration, fenced below). `.range` is read 3 times, only to precompute the full hyperopt indicator grids whose non-default columns are never gating evidence. The file ships no sample, window, trade count, fee basis, win rate, or performance figure of any kind — no source-reported performance is adopted or restated.

**Out-of-file calls pinned (all resolved by name, all literal-or-default):** `ta.ADX(dataframe, timeperiod=14)` (TA-Lib abstract default over high/low/close, Wilder smoothing — live gate and exit); `ta.SMA(dataframe, timeperiod=12/48)` (TA-Lib abstract default over close — live edge pair); `qtpylib.crossed_above/crossed_below(series, series)` (the file imports Freqtrade's vendored copy; this record does not rely on the vendor — it **defines** `XUP(a,b)[t]=(a[t]>b[t])&(a[t-1]<=b[t-1])` and `XDN(a,b)[t]=(a[t]<b[t])&(a[t-1]>=b[t-1])`, the exact series-series semantics read this cycle in `technical@78061e9` vendor `indicators.py`, 20422 bytes, blob `2fd7fe263555be9fbd0ca638d70178c482afd71c`, still that repository's HEAD). `functools.reduce` only ANDs the condition lists; `numpy`/`pandas` carry no gating logic.

**Non-adopted source machinery (disclosed, never silently re-based):** the three-rung ROI ladder and the `-0.05` stoploss are Freqtrade time/profit machinery; neither is adopted as an intrabar semantic. The file names no market, venue, fill-timing flag, position size, or warmup beyond the 14-bar seed. `can_short = True` is an explicit file literal enabling the short legs — explicitly disabled below. `pos_exit_adx` (default 30.0, space `sell`) is declared but never read — its value can never influence any leg; the exit threshold is the entry parameter's 30.0 by file literal, preserved as such.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 1h, long/flat only**; pin the file-default ADX(14)/SMA12/SMA48/30.0 construction and the `crossed_above` long edge; keep the file's ADX-below-30 state leg as the **sole** signal exit; explicitly disable the short legs (`enter_short`/`exit_short` never armed) and the entire ROI/stop block (the exit leg needs no profit trigger; trailing is already `False` in source); fix one `0.001 BTC` base-size position, one-position-only, no DCA, no cooldown; fix a 60-completed-bar warmup (researcher hardening over the file's 14-bar seed); and the state/timing/cost rules below. All changes are part of this **separate strategy**, not evidence that the source file is expressible unchanged. This follows the admitted `futures/TrendFollowingStrategy`, `futures/FOttStrategy`, and `futures/FSampleStrategy` sibling precedents (long-only, risk block disabled, signal-exit-only).

**Immutable research identity:** `FT-FAdxSmaStrategy-f3340ce | derived-v1-ADX14x30-SMA12-48-XUP | BTC-USDT-binance-spot-1h | signal-exit-only | 2026-10-31`. Changing any component changes the derivative identity.

**Pre-write dedup:** main `fc4dc6ae`, 469 root-level strategy Markdown records. Working-tree search for `FAdxSma`/`fadxsma` returns nothing. Twelve open `research/*` PRs examined by title and source — none uses this file or rule. Nearest families are materially different: open PR #331 (`berlinguyinca/AdxSmas.py`, 61 lines, 1784 bytes) is an SMA3/6 fast cross gated by ADX(14) `> 25` whose exit needs an **edge** — `ADX < 25` AND an opposite `crossed_above(long, short)` on the same bar — with a long-only source, single-rung `{"0": 0.1}` ROI and `-0.25` stop; this candidate is an SMA12/48 slow cross (4–8× the horizon memory) gated by ADX `> 30.0` whose exit is a **pure level state** (`ADX < 30.0`, no cross required, fires on any soft bar), from a different 130-line file with hyperopt spaces, present-but-disabled short legs, a three-rung ROI ladder, `-0.05` stop, `startup_candle_count = 14` and `process_only_new_candles = True`. Different exit class (state vs edge), different horizon, different threshold, different lineage and risk block. The EMA-cross-ADX-regime pool crosses EMAs (not SMAs) under regime gates; the ADXMomentum record gates on DI polarity (not an ADX level); Quickie/Strategy004 gate TEMA/BB/CCI constructions with no SMA-cross-plus-ADX-state shape. This candidate is the only ADX14-level × SMA12/48-edge × ADX-state-exit conjunction on `1h`. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where a 12-bar average crosses up through a 48-bar average while 14-bar trend strength reads above 30; stand aside on any bar where trend strength reads below 30 (the exit reuses the entry threshold by file literal); mirror for shorts; a three-rung ROI ladder and a −5% stoploss backstop positions under Freqtrade execution. The file ships no market, sample, or performance claim — this record adopts no source-reported performance (see Evidence).

### Research interpretation

A strength-gated slow-rotation buyer: the ADX level refuses chop (a cross printed while ADX sits at or below 30 prints nothing — most fast whipsaws die here), and the 12/48 edge refuses stale trends (a market that has ridden above its slow average without a fresh cross prints nothing). Entry therefore fires only on a slow-average rotation confirmed by contemporaneous trend strength. The exit is deliberately dumber than the entry — a pure strength readout with no MA geometry — so a long is surrendered the first bar strength fades, without waiting for the slow opposite cross that could take dozens of bars to arrive. Disabling the ROI/stop block removes the file's profit triggers and leaves the position's entire fate on the declared signal exit — a drift that holds strength above 30 without printing the exit state is held, not forgiven.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 1h OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 3600 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback. (`V` is validated for feed integrity only — no volume-derived feature enters any leg.)

**Features (source-faithful, file defaults pinned):** `adx[t]=TA-Lib ADX(H,L,C,14)` (Wilder smoothing); `sShort[t]=TA-Lib SMA(C,12)`; `sLong[t]=TA-Lib SMA(C,48)` (both over close). The full hyperopt grids (`adx_4..24`, `sma_short_4..24`, `sma_long_12..175`) are never materialized in this derivative — only the three default columns exist. NaN-leading comparisons and edges are false, so pre-seed bars could never fire in any case.

**Completed-bar long entry predicate `E[t]`** (exact conjunction, no epsilon): `(adx[t]>30.0) & XUP(sShort,sLong)[t]` with `XUP(a,b)[t]=(a[t]>b[t])&(a[t-1]<=b[t-1])`, `t>=60`, every required feature valid, no pending order, FLAT and re-arm state true. No funding/OI/mark-price read anywhere in the gating path.

**Signal exit `X[t]`** (pure level state, strict): `(adx[t]<30.0)` — true on any bar printing sub-30 strength, with no cross or slope requirement. An open LONG closes on the first `X[t]` bar with `t` past the entry fill bar. The file-literal quirk is preserved exactly: the threshold is the entry parameter's 30.0 (the declared-but-unread `pos_exit_adx` can never relocate it).

**Co-fire pin (proven mutually exclusive, disclosed, not repaired):** `E[t]` needs `adx>30.0` while `X[t]` needs `adx<30.0` — strictly complementary, so no bar can satisfy both; a bar printing exactly `30.0` satisfies neither (held, never forced). Entry and exit therefore never execute on the same bar. ROI/stop legs do not exist in this derivative, so no further ordering is invented.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. The file's `enter_short`/`exit_short` legs are explicitly disabled despite the file-literal `can_short = True`.

**Risk (Gate 3, explicit):** the ADX-state signal exit is the sole position-ending path (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — the exit fires even at a loss; disclosed defaults, never file literals). The file's three-rung ROI ladder and `-0.05` stoploss are explicitly disabled (see Provenance) — no profit trigger, no stop level, no trailing (already `False` in source), no time stop, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default.

**State (Gate 4):** `FLAT_DISARMED`, `FLAT_ARMED`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT_ARMED` after 60 valid completed bars **only if E without the state clause was false on the immediately prior completed bar**; otherwise wait for a false bar to arm. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET fill at the next completed close transitions to LONG. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT_DISARMED. Once flat, require at least one **subsequent** completed bar with the non-state entry predicate false to re-arm. No same-bar SELL+BUY, no pyramiding, **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding, no session/cooldown. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 60 contiguous completed 1h bars before the first actionable bar; covers the SMA48 seed, the ADX14 Wilder seed, the one-bar edge lookback, and the arming rule, plus margin over the file's 14-bar seed. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Unseeded windows stay NaN and every NaN comparison is false — no leg can fire early. The file's own `process_only_new_candles = True` is preserved (one evaluation per completed bar).

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and every derived line become available no earlier than `T[t]+3600s`. All decisions and fills are effective at completed-bar closes. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used — every lag call is `shift(1)` or the one-bar edge lookback, all strictly backward. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (verified an ancestor of the local checkout `2dbc844` this cycle; `hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`, content read this cycle). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`, verified at the pinned commit this cycle) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, INTERVALS `"1h"` entry read this cycle) supports `1h`. Connector `binance`, pair `BTC-USDT`, one spot 1h stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision (no volume feature exists), no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6` (chain names and `trade_cost=0.0002` default read this cycle). A **strategy-specific, not-yet-implemented** controller must calculate the exact ADX/SMA state and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` (`hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, code read this cycle) fills at the first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar stop fill. Explicitly no stop/limit/maker order is ever queued, so the disabled file-level stop can never leak back through an executor semantic. On confirmed fills, the hold nets base amounts with weighted entry and realized gross PnL plus recorded fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end.
- **Fees and accounting:** pin `trade_cost=0.0002` (the default on the pinned `run_backtesting` signature, line read this cycle) per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount_quote`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. Never treat engine PnL outputs as fee-inclusive net equity without reconstructing from the actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Price integrity:** validate every observed finite positive `close_bt` before order creation; `BacktestingDataProvider.get_price_by_type` returns `Decimal("1")` for a missing pair (line 140 read this cycle) and must **never** supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships no sample, window, trade count, fee basis, or performance figure of any kind. No source-reported performance is adopted or restated. The only commented alternative is the `{"0": 1}` ROI ladder — disclosed as a comment, never a live leg.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

Cousins fenced as different constructions (none trades an ADX14-level × SMA12/48-edge × pure-ADX-state-exit conjunction on `1h`): open PR #331 (`berlinguyinca/AdxSmas.py`) is an SMA3/6 fast cross gated by ADX `> 25` with an **edge-gated** opposite-cross exit, long-only source, single-rung ROI and `-0.25` stop; the admitted `forven-ema-cross-adx-regime` crosses EMAs (not SMAs) under regime gates with no ADX-state exit; the admitted `freqtrade-adx-momentum-di-gated` gates on DI polarity (not an ADX level) with no SMA cross; the admitted `freqtrade-quickie-tema-slope-bbmid-adx-gated` is a 5m TEMA/BB level-state system with no SMA cross edge; the admitted `freqtrade-strategy004-adx-cci-dual-stoch-recross` is a 5m ADX/CCI/dual-Stoch recross system with no SMA pair. Changing any pinned constant (ADX period/threshold, SMA periods, typical-price source), frame, book, or re-enabling any risk/short leg would each be a different, unpinned rule — none is admitted here.

## Falsification plan

- F1 — Strength-gate necessity: replacing the `adx>30.0` entry guard with an always-true guard (same SMA12/48 edge, same ADX-state exit/state/cost) must not improve net expectancy; fail ⇒ the ADX gate adds nothing over the pure slow-cross system.
- F2 — Edge-vs-level relevance: replacing the `XUP(sShort,sLong)` edge with the persistent `sShort>sLong` level (same ADX guard, same exits) must not improve net expectancy; fail ⇒ the cross edge adds nothing over a static above-average holding rule.

## Crypto portability

Binance BTC-USDT spot 1h only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here.

## Limitations

Researcher-chosen (not source-native): long-only disablement of the file's short legs despite file-literal `can_short = True`, full disablement of the three-rung ROI ladder and `-0.05` stoploss, default-pinning of all five hyperopt spaces (including the never-read `pos_exit_adx` declaration, which can never relocate the exit threshold), 60-bar warmup hardening over the file's 14-bar seed, 0.001 BTC size, 0.0002/side hypothetical cost, re-arm restriction, full-sample indicator evaluation. TA-Lib version sensitivity of ADX/SMA beyond the pinned call semantics is unverified. No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- Primary: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FAdxSmaStrategy.py (commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, blob `3bb13caf079e8360a959c3ad4dd2b2507f3045c0`, 4091 bytes / 130 lines, verified this cycle; file last touched by `d2e8721595931d9c5f4504acfeea381bc3f416e4`)
- Edge primitive: `technical@78061e9` `technical/vendor/qtpylib/indicators.py` (20422 bytes, blob `2fd7fe263555be9fbd0ca638d70178c482afd71c`; `crossed`/`crossed_above`/`crossed_below` series-series semantics read this cycle)
- Engine: Hummingbot package `20260920`, VERSION `dev-2.17.0`, `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (file blobs cited inline, verified this cycle)
