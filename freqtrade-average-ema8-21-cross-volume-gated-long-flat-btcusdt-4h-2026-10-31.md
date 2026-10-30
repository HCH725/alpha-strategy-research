---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Average EMA8/21 cross volume-gated long-flat BTCUSDT 4h derivative
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Average EMA8/21 cross volume-gated — independent BTC-USDT spot 4h long-flat derivative

## Provenance

**Primary public GitHub identity:** `freqtrade/freqtrade-strategies`, file `user_data/strategies/berlinguyinca/AverageStrategy.py`, class `AverageStrategy(IStrategy)` (the only class in the file; verified by `^class ` count of 1 over the full 79 lines this cycle). Pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`), returned as the repository `main` HEAD by the GitHub commits API this cycle (2026-10-31). GitHub blob SHA `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, 2630 bytes, 79 lines; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` (SHA-256 `63606866fdf1cb3d71dc39a951ed0784a31686690b1c4014c12d2481c8dbf094`) — the entire file was read, not sampled. The file's last-touch commit is `7f91ff52bb664423ae673092a6a18d76c50c2c29` (`2022-07-10T09:44:41Z`, adding `INTERFACE_VERSION` to all strategies); the blob at that commit is byte-identical (`dbb0ba65…`, 2630 bytes), so no newer file revision exists to diverge from.

**The file's own words (quoted for gate evidence, never extended):** `INTERFACE_VERSION: int = 3`; `timeframe = '4h'`; `minimal_roi = {"0": 0.5}`; `stoploss = -0.2`; `buy_range_short = IntParameter(5, 20, default=8)`; `buy_range_long = IntParameter(20, 120, default=21)`. Indicators precompute `dataframe[f'ema{val}'] = ta.EMA(dataframe, timeperiod=val)` for every value in the union of the two parameter ranges. Long entry is the conjunction of `qtpylib.crossed_above(dataframe[f'ema{self.buy_range_short.value}'], dataframe[f'ema{self.buy_range_long.value}'])` and `(dataframe['volume'] > 0)` setting `enter_long`. Long exit mirrors with `crossed_above(long-leg, short-leg)` and `(dataframe['volume'] > 0)` setting `exit_long`. The file's own idea comment is candid: buys and sells on crossovers — proof of concept, does not perform that well. No market, venue, fill-timing flag, position size, or warmup appears anywhere in the file.

**Full-file token census (verified by search over the 79 lines this cycle):** 2 `IntParameter(` instantiations (both default-pinned below); 0 `informative_pairs` / 0 `resample` / 0 `merge_informative`; 0 `position_adjustment` / 0 `adjust_trade_position` / 0 `custom_stake` / 0 `leverage(` / 0 `protections` / 0 `cooldown`; 0 `funding` / 0 `mark_price` / 0 `markprice`; 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `order_types` / 0 `order_time_in_force` / 0 `trailing_stop` / 0 `process_only_new_candles` / 0 `startup_candle_count` / 0 `can_short` (framework defaults apply, disclosed below); 2 `crossed_above` (one entry edge, one exit edge); 1 `enter_long` / 1 `exit_long`; 0 `enter_short` / 0 `exit_short` / 0 `crossed_below`; 2 `volume` reads (one per leg, both strict `> 0`); 1 active `minimal_roi`; 1 active `stoploss`. `.value` is read 4 times (2 per leg, both parameters); `.range` is read on a single loop line covering both parameters, only to precompute the full hyperopt indicator grids whose non-default columns never gate any leg. The file ships no sample, window, trade count, fee basis, win rate, or performance figure of any kind — no source-reported performance is adopted or restated.

**Out-of-file calls pinned (all resolved by name, all literal-or-default):** `ta.EMA(dataframe, timeperiod=8/21)` (TA-Lib abstract default over close — live edge pair); `qtpylib.crossed_above(fast, slow)` (the file imports Freqtrade's vendored copy; this record does not rely on the vendor — it **defines** `XUP(a,b)[t]=(a[t]>b[t])&(a[t-1]<=b[t-1])`, the exact series-series semantics read in `technical@78061e9` vendor `indicators.py`, still that repository's HEAD via `ls-remote` this cycle). `functools.reduce` is imported but never used in any gating path; `CategoricalParameter`/`DecimalParameter` are imported but never instantiated (dead imports, fenced here).

**Non-adopted source machinery (disclosed, never silently re-based):** the single-rung `{"0": 0.5}` ROI and the `-0.2` stoploss are Freqtrade profit/backstop machinery; neither is adopted as an intrabar semantic. The file names no market, venue, fill-timing flag, position size, or warmup. Absent framework flags (`use_exit_signal`, `exit_profit_only`, `order_types`, `process_only_new_candles`, `startup_candle_count`, `can_short`) are Freqtrade framework defaults, disclosed below — never file literals, never invented legs.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 4h, long/flat only**; pin the file-default EMA(8)/EMA(21) construction and both `crossed_above` edges; keep the file's strict `volume > 0` conjunction on **both** legs verbatim; explicitly disable the entire ROI/stop block (both edge legs need no profit trigger); fix one `0.001 BTC` base-size position, one-position-only, no DCA, no cooldown; fix a 60-completed-bar warmup (researcher hardening; the file seeds nothing and the structural minimum is the 22nd bar); and the state/timing/cost rules below. All changes are part of this **separate strategy**, not evidence that the source file is expressible unchanged. This follows the admitted `berlinguyinca` Quickie/SmoothScalp sibling precedent (long-only, risk block disabled, signal-edge exits only).

**Immutable research identity:** `FT-AverageStrategy-f3340ce | derived-v1-EMA8-21-XUP-XDN-volgt0 | BTC-USDT-binance-spot-4h | signal-exit-only | 2026-10-31`. Changing any component changes the derivative identity.

**Pre-write dedup:** main `e453404a`, 470 root-level strategy Markdown records. Working-tree search for `AverageStrategy`/`averagestrategy`/`buy_range` returns nothing. Twelve open `research/*` PRs examined by title and source — none uses this file or rule. Nearest families are materially different: `ema-20-50-cross-btcusdt-1h` (Forven Pine, 1h, EMA20/50, no volume gate, Pine-input construction — different lineage, different timeframe/horizon, different lengths, no volume conjunction); `freqtrade-strategy001-ha-ema-cross` (berlinguyinca upstream pin, 5m, EMA20/50 **plus Heikin-Ashi color/position gates** — extra geometry this candidate never reads); `forven-ema-cross-adx-regime` (EMA cross **plus ADX regime gate** — extra oscillator this candidate never reads); `tradingview-sachinlanke-adaptive-supertrend-ema8-sma5-cross` (4h EMA8-involved but a Supertrend-plus-SMA5-cross machine — different indicator, different exit class); DEMA/HMA/TEMA/OBV/DPO cross records (different average constructions). No pool record conjoins a plain EMA8/EMA21 opposite-cross pair with a strict volume gate on 4h. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where an 8-bar average crosses up through a 21-bar average on positive volume; stand aside on the bar where the 21-bar average crosses back up through the 8-bar average on positive volume; a single 50% ROI rung and a −20% stoploss backstop positions under Freqtrade execution. The file's idea comment disclaims performance (proof of concept). No market, sample, or performance claim is adopted.

### Research interpretation

A fast-rotation 4h trend buyer: the 8/21 edge refuses stale trends (a market riding above its slow average without a fresh cross prints nothing) and the volume conjunction refuses dead prints (a cross printed on a zero-volume bar — effectively never on BTCUSDT 4h — prints nothing). Entry fires only on a fresh fast-over-slow rotation with a live tape; the exit is the symmetric slow-over-fast rotation, so a long is surrendered at the first opposite rotation without waiting for any profit target. Disabling the ROI/stop block removes the file's 50% profit trigger and −20% backstop and leaves the position's entire fate on the declared opposite edge — a drift that holds fast-above-slow without printing the exit edge is held, not forgiven.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 4h OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 14400 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback. (`V` is validity-checked feed-wide and additionally gates both legs strictly, exactly as coded.)

**Features (source-faithful, file defaults pinned):** `eFast[t]=TA-Lib EMA(C,8)`; `eSlow[t]=TA-Lib EMA(C,21)` (both TA-Lib abstract defaults over close). The full hyperopt grids (`ema5..ema20`, `ema20..ema120`) are never materialized in this derivative — only the two default columns exist. NaN-leading comparisons and edges are false, so pre-seed bars could never fire in any case.

**Completed-bar long entry predicate `E[t]`** (exact conjunction, no epsilon): `XUP(eFast,eSlow)[t] & (V[t]>0)` with `XUP(a,b)[t]=(a[t]>b[t])&(a[t-1]<=b[t-1])`, `t>=60`, every required feature valid, no pending order, FLAT. No funding/OI/mark-price read anywhere in the gating path.

**Signal exit `X[t]`** (exact conjunction, no epsilon): `XUP(eSlow,eFast)[t] & (V[t]>0)` — the symmetric opposite edge on positive volume. An open LONG closes on the first `X[t]` bar past the entry fill bar. A zero-volume bar suppresses even a geometrically valid edge on either leg (source-faithful; verified in the scratch self-check below).

**Co-fire pin (proven mutually exclusive, disclosed, not repaired):** `E[t]` needs `eFast[t]>eSlow[t]` with `eFast[t-1]<=eSlow[t-1]` while `X[t]` needs `eFast[t]<eSlow[t]` with `eFast[t-1]>=eSlow[t-1]` — jointly requiring the fast average strictly above AND strictly below the slow average on the same bar, impossible; a bar printing exact equality satisfies neither (held, never forced). Entry and exit therefore never execute on the same bar. ROI/stop legs do not exist in this derivative, so no further ordering is invented.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. The file contains no short leg anywhere (verified zero `enter_short`/`exit_short` tokens).

**Risk (Gate 3, explicit):** the opposite-edge signal exit is the sole position-ending path (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — the exit fires even at a loss; disclosed defaults, never file literals). The file's single-rung 50% ROI and `-0.2` stoploss are explicitly disabled (see Provenance) — no profit trigger, no stop level, no trailing (absent in source), no time stop, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default.

**State (Gate 4):** `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT` after 60 valid completed bars. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET fill transitions to LONG. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only a confirmed filled SELL of the complete 0.001 BTC returns to FLAT. The next entry needs a fresh `XUP` edge — no cooldown is specified (explicitly none, not invented), and no re-arm restriction is needed because edges, unlike level states, cannot persist true across bars. No same-bar SELL+BUY (proven impossible above), no pyramiding, **no DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no concurrency, no compounding. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 60 contiguous completed 4h bars before the first actionable bar; covers the EMA21 seed, the one-bar edge lookback, and margin over the structural 22-bar minimum (the file itself seeds nothing). No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Unseeded windows stay NaN and every NaN comparison is false — no leg can fire early.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLCV and every derived line become available no earlier than `T[t]+14400s`. All decisions and fills are effective at completed-bar closes. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used — every lag call is the one-bar edge lookback, strictly backward. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (verified an ancestor of the local checkout `2dbc844` this cycle; `hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`, content read this cycle). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`, verified at the pinned commit this cycle) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`, INTERVALS `"4h"` entry read this cycle) supports `4h`. Connector `binance`, pair `BTC-USDT`, one spot 4h stream. The `volume` column parsed from row[5] feeds only the signal-side `V[t]>0` gate — no volume-weighted fill, no depth model. No funding or perpetual margin/mark/index, no order-book decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6` (chain names and `trade_cost=0.0002` default read this cycle). A **strategy-specific, not-yet-implemented** controller must calculate the exact EMA8/21 edges with the volume gate and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` (the fixed initial and only unit size), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` (`hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, code read this cycle) fills at the first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar stop fill. Explicitly no stop/limit/maker order is ever queued, so the disabled file-level stop can never leak back through an executor semantic. On confirmed fills, the hold nets base amounts with weighted entry and realized gross PnL plus recorded fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end.
- **Fees and accounting:** pin `trade_cost=0.0002` (the default on the pinned `run_backtesting` signature, line read this cycle) per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount_quote`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. Never treat engine PnL outputs as fee-inclusive net equity without reconstructing from the actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Package/commit binding disclosure (Gate-5 #411/#424):** `setup.py` at the pinned commit assigns version `20260729`, not `20260920`; `hummingbot/VERSION` at the pin reads `dev-2.17.0`. No package-to-commit mapping is invented here — `20260920` is retained as the policy package **label only**, and Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET same-close primitive with no novel execution primitive (no stop/limit/trailing/next-open/intrabar leg is introduced). Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 2630-byte file ships the complete construction: the `4h` timeframe, the `(5, 20, default=8)` / `(20, 120, default=21)` hyperopt declarations, the EMA precompute loop, the entry conjunction (`crossed_above(ema{short}, ema{long})` with `volume > 0`), the mirrored exit conjunction, the long-only posture (zero short tokens), and the absence of any registry entry (the file is reached by class path, disclosed). It ships no timeframe beyond `4h`, no venue, no sizing, no capital, no fee, and no coded warmup. The idea comment disclaims performance (proof of concept). No source performance table, trade count, or date range exists anywhere in the file.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifact this run is a researcher self-check of the edge/volume/co-fire logic plus the derived FLAT/LONG machine on an 8-bar synthetic series (entry edge bar, volume-suppressed opposite edge, hold bars), run in scratch (never committed): `events: [('BUY', 3)]` then `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

### Negative evidence and deduplication

At the pre-write snapshot `main@e453404a`, the root Git tree contained **470** strategy Markdown records. Exact-identity working-tree searches for `AverageStrategy`, `averagestrategy`, and `buy_range` return **zero** records using this source file, class, or parameter names. Content searches for `ema8`/`EMA(8)`/`ema{8}` return only passing mentions of *other* records inside cousin dedup prose (a vallentuna2 EMA8/50 reference, a sachinlanke EMA8/SMA5 reference) — no order line reads an EMA8/21 pair. Twelve open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646) were inspected for source overlap; none uses this file or a plain EMA8/21 opposite-cross mechanism (the nearest, #331 AdxSmas, is an SMA3/6 fast cross gated by ADX25 with an edge-conjunction exit — different averages, different gate, different exit class). Pool cousins fenced as different mechanisms: `ema-20-50-cross` (different lineage/TF/lengths, no volume gate); `freqtrade-strategy001-ha-ema-cross` (extra Heikin-Ashi geometry); `forven-ema-cross-adx-regime` (extra ADX gate); Supertrend/DEMA/HMA/TEMA/OBV/DPO cross records (different average constructions or extra gates). This is a materially different signal conjunction (plain EMA8/21 opposite edges **with** a strict volume gate on 4h), not a trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen EMA8/21 volume-gated rule against (a) a no-volume-gate baseline (same edges, volume conjunction removed) and (b) a lengths-off baseline (EMA20/50 edges on the same 4h feed, same exits) on identical contiguous BTC-USDT 4h data with the same declared costs; check edge-event rate, volume-suppression rate, and sensitivity to the 60-bar warmup. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance spot 4h** only. Stated plainly: the 4h frame observes roughly six rotations per day of wall-clock tape; edge events arrive slower than any 1h/5m sibling and holding times stretch across days. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The 4h frame, venue, sizing, costs, warmup, same-close MARKET fills, and edge-only posture are researcher pins, never attributed to the source. The file's 50% ROI rung and −20% stoploss are disabled by declaration: adverse moves are held through with no cut, and winners are held until the opposite edge with no cap. A LONG whose opposite edge never arrives is held indefinitely with no time exit. Framework defaults (`use_exit_signal`, `exit_profit_only=False`, order types) are Freqtrade-conventional readings, never file literals. TA-Lib version sensitivity of EMA seeding beyond the pinned call semantics is unverified. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py (commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, blob `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, 2630 bytes / 79 lines, verified this cycle; file last touched by `7f91ff52bb664423ae673092a6a18d76c50c2c29`)
- Repository: https://github.com/freqtrade/freqtrade-strategies
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
