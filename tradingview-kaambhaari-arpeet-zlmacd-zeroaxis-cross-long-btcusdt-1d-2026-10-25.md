---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: KaamBhaari Arpeet zero-lag MACD zero-axis gated cross, independent BTC-USDT spot 1d long-flat derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-05
sources:
  - https://www.tradingview.com/script/HnQ6hKLG-Arpeet-MACD/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Arpeet zero-lag MACD zero-axis cross — explicitly independent BTC-USDT spot 1d derivative

## Provenance

- **Primary TradingView source:** *Arpeet MACD*, by **KaamBhaari**, published **2025-02-05**, stable public script ID **HnQ6hKLG**, open-source listing: https://www.tradingview.com/script/HnQ6hKLG-Arpeet-MACD/ . Author's public description directly inspected 2026-10-25. The complete Pine source, its script revision hash and execution defaults were **not** retrievable from the readable publication; do not attribute any undocumented defaults to the author.
- **Verified source-description facts:** fast/slow EMA-or-SMA choices default to lengths 12 and 26; the author describes a *double-smoothed zero-lag* fast/slow construction, MACD as their difference, signal smoothing default length 9 (EMA or SMA), **buy on MACD/signal upward cross below zero** and **sell on downward cross above zero**. The page does not unambiguously specify the mathematical zero-lag transform, precise crossover-axis equality, position sizing, bar-fill convention, risk orders or fees.
- **Not source-native / not a lossless Pine reconstruction.** This is a separately defined executable **derivative**. Researcher-defined choices are: exact double-EMA compensation formula and initialization, EMA rather than optional SMA, the strict both-lines zero-zone test, Binance BTC-USDT spot daily data, LONG/FLAT (sell closes rather than opens a short), 120-bar contiguous warmup, completed-bar close decision/fill, one fixed 0.001 BTC unit, 10,000 USDT unborrowed starting cash, explicit modeled fee, missing-data handling, and all disabled behaviors. They are not claimed to be Pine facts.
- **Immutable strategy identity:** `TV-HnQ6hKLG | KaamBhaari-2025-02-05 | independent-derived-v1-DEMA12-26-EMA9-bothLinesZeroGatedCross-longflat | BinanceSpot-BTC-USDT-1d | 2026-10-25`. Changing smoothing, axis tests, timing, exits, venue, sizing or risk creates a new derived identity.

## Economic mechanism

Hypothesis only: a zero-lag-compensated fast/slow momentum difference crossing its own smoothed signal *while both are negative* may identify an early recovery from negative momentum; a bearish cross with both above zero closes after positive-momentum exhaustion. This asymmetric zero-zone filter can leave a position open through other MACD crosses. No profitability or backtest result is asserted.

## Signal

**Causal input:** contiguous valid Binance spot BTC-USDT **1d UTC** candles `(T,O,H,L,C,V)`, where `T` is the daily **opening** Unix timestamp. A completed candle's information is available only at `T+86400` seconds. No signal uses the unfinished current candle. Require finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, nonnegative finite V and exactly 86400 seconds between successive opening timestamps. Never forward-fill or fabricate missing prices.

**Pinned formula, entirely researcher-defined where the author description is incomplete:**

1. For `n in {12,26}`, define `E_n[t] = EMA_n(C)[t]`. Seed its first valid value at `t=n-1` as the arithmetic mean of `C[0..n-1]`; subsequently `E_n[t] = (2/(n+1))*C[t] + (1-2/(n+1))*E_n[t-1]`. Before its seed the value is undefined.
2. Define a second EMA `F_n[t] = EMA_n(E_n)[t]` seeded at `t=2*n-2` with the arithmetic mean of the first `n` defined `E_n` values (`t=n-1..2*n-2`), and then recursively with the same `2/(n+1)` multiplier. Define the *researcher's explicit zero-lag-compensated average* `Z_n[t] = 2*E_n[t] - F_n[t]`. This exact double-EMA formula is **not** claimed to have been recovered from the unavailable Pine code.
3. `M[t] = Z_12[t] - Z_26[t]`, defined from index 50 onward. `S[t] = EMA_9(M)[t]`, seeded at index 58 as the mean of `M[50..58]`, then recursively with alpha `2/10`. No rounding, alternative TA-library initialization, interpolation or full-sample normalization is allowed.
4. **Entry trigger:** `UP[t] = (M[t-1] <= S[t-1]) AND (M[t] > S[t]) AND (M[t] < 0) AND (S[t] < 0)`. This is a confirmed strict upward cross with **both** lines strictly below zero. Touch at the current bar or either current value equal to zero does not qualify.
5. **Exit trigger:** `DOWN[t] = (M[t-1] >= S[t-1]) AND (M[t] < S[t]) AND (M[t] > 0) AND (S[t] > 0)`. This is a confirmed strict downward cross with **both** lines strictly above zero. Other bearish crosses do not exit; no unconditional `M<0` stop is invented.
6. **Decision state:** start `FLAT`. At the end of each valid fully closed bar after warmup: `FLAT+UP` places one modeled BUY of `Q=0.001 BTC` if affordable; `LONG+DOWN` places one modeled SELL of the complete `Q`. All other combinations HOLD. SELL/exit takes priority if conditions somehow conflict (they cannot for finite M/S). Signals while already in the requested state are ignored; no same-bar reversal. After a full SELL the next qualifying `UP` on a **later** completed bar may re-enter; zero-bar cooldown.
7. **Disabled:** shorting, borrowing/leverage/margin, pyramiding, DCA, BO/SO, partial exits, other concurrent positions, fixed or trailing SL/TP, time-based exits, discretionary exit, maker/limit/next-open/intrabar orders, compounding, forced end-of-data liquidation and any cross-market portfolio logic. This derivative explicitly accepts the risk of an indefinite LONG without a stop.
8. **Warmup and invalid data:** require **120 consecutive valid completed 1d bars** before the first decision, exceeding the index-58 minimum and supplying prior-cross history. At a missing/invalid/out-of-order bar, stop generating orders, discard indicator seeds and require a fresh 120 valid contiguous bars before any new decision. An existing LONG is **not** sold at a fabricated price; the run is flagged data-incomplete and cannot yield claimable performance across the gap. No future data may be used to repair the gap or infer an earlier signal.

## Required data

Only one Binance BTC-USDT **spot** daily OHLCV feed with UTC opening timestamps and completed-bar closes. No funding stream, perpetual mark/index price, order book, higher/lower timeframe alignment, second market, fitted model, repainting pivot, future extrema or intrabar reconstruction. Computation at bar `t` uses only candles `0..t`. At dataset end an open position is valued at the last **valid available close**; it is not fictitiously liquidated.

## Execution assumptions — pinned Hummingbot compatibility

**Immutable engine pin:** Hummingbot policy package `20260920`, `VERSION=dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly fetched the VERSION and the following source files at that exact commit on 2026-10-25. Separate wheel-to-source byte identity is supported by the **previously merged, independently reviewed Alpha PR #414**, which reports 902/902 wheel Python files matched the immutable source and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`. This cycle did **not** independently rehash any installed package.

- **Real candle path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` contains `"1d":"1d"`; `binance_spot_candles.py::_parse_rest_candles` converts exchange `row[0]` to opening seconds and maps OHLCV from `row[1..5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` exposes the actual `open_bt/high_bt/low_bt/close_bt/volume_bt` and unsuffixed fields. A strategy-specific controller can calculate the pinned recursive EMA values from those fields. **Validate original candle continuity before the engine's `dropna`**, which otherwise could hide missing rows; do not invent or silently backfill a close.
- **Controller/order path:** `BacktestingEngineBase.simulate_execution` iterates each processed row, invokes `update_state(row)`, then `controller.determine_executor_actions()`, and dispatches `CreateExecutorAction` to the real `OrderExecutorSimulator`. `OrderExecutorConfig` supports `connector_name=binance`, `trading_pair=BTC-USDT`, BUY/SELL, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A dedicated controller/recipe is **not yet implemented**; this is bounded static model expressibility, not a claim of an already executable artifact.
- **Fill/timestamps:** the pinned `order_executor_simulator.py` MARKET path fills on the first supplied processed row at that row's **close**, computes `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote` and returns `CloseType.POSITION_HOLD`. The engine uses the **opening-time index** as raw fill timestamp; normalized economic/event decision and fill time in this derivative is **opening time + 86400 seconds**. This is a simulator same-close convention, **not** a live achievable post-close execution claim. The modeled MARKET path has full fill and no queue/partial fill; no claim of real liquidity or slippage measurement.
- **Position/cost:** `BacktestPositionHold._process_order` nets opposite-side base quantities and computes **gross** realized quote PnL; `add_executor` accumulates `cum_fees_quote`. Controller must use its own fill-confirmed FLAT/LONG state, not lagged `positions_held` snapshots, and must enforce the fixed cash budget. Initial cash `10,000 USDT`; BUY only if `cash >= 0.001*fill_close*(1+0.001)`. Research fee **assumption** `trade_cost=0.001` per side, deducted on both BUY and SELL, never attributed to the source or represented as an observed exchange fee. `net_roundtrip_PnL = Q*(sell_close-buy_close) - 0.001*Q*buy_close - 0.001*Q*sell_close`. Marked equity while LONG is cash plus `Q*last_valid_close`, already net of paid BUY fee, without hypothetical SELL. Spot funding is **not applicable** (not invented as zero perpetual funding). Simulator has no extra modeled spread/impact/slippage, which is a limitation, not proof those costs are zero in reality.
- **Precision and boundary:** preserve Decimal quantities/cash and distinguish tiny float conversion residue from a tradable quantity. Exchange minimums, tick/lot rounding, latency, partial fills and realized fees are **unverified**, so this is not production exchange certification. No unsupported maker/next-open, cross-asset, perpetual margin or funding path is used. The spot daily MARKET close-fill/position ledger is the same previously independently reviewed **engine primitive**, not an assertion of strategy-specific backtest parity.

## HB_READY six-gate evidence (Scout proposal; independent review required)

1. **Determinism:** exact double EMA compensation, both seeds, MACD/signal recursion, inequalities, axis predicates, warmup, data invalidation and action priority frozen; unknown Pine choices explicitly derivative.
2. **Direction:** one Binance spot BTC-USDT LONG/FLAT unit, SHORT disabled.
3. **Entries/exits/risk:** negative-zone upward cross enters, positive-zone downward cross exits; all other exits and stops explicitly disabled, including potentially prolonged exposure.
4. **Position/state:** one 0.001 BTC unit, nonborrowed 10,000 USDT affordability, no DCA/pyramiding/concurrency, complete exit, re-entry on later fresh UP, zero cooldown, gap fail-closed.
5. **Real pinned model:** immutable 1d Binance spot feed, inspected controller/order action and close-fill paths, fee-aware netted position ledger and timestamp normalization; no fabricated price/funding, unverified live precision clearly excluded. Package binding cited to independently merged PR #414.
6. **Point-in-time:** 120 completed UTC bars, only present/past prices, explicit seed and cross prior bar, no incomplete candle, future shift, leakage or missing-price substitution.

## Evidence

### Source-reported
KaamBhaari's 2025-02-05 TradingView page describes 12/26 zero-lag double smoothing, signal length 9, upward crossover below zero as buy and downward crossover above zero as sell. It does **not** establish the exact derivative formula, author trade-size/cost/fill conventions or any independently reproduced return.

### Independently reproduced
**None.** No TradingView, Qlib or Hummingbot strategy backtest, event-level parity run, trading, paper/testnet/live order, wheel rehash or deployment occurred this cycle. Read-only inspection of pinned engine source is evidence of *model capability*, not executed strategy equivalence.

### Negative evidence and deduplication
Pre-write `main` SHA `b453b438b2bdcbe9ff60c2e7a1bbee48ae735480` held **324** root-level strategy Markdown records and README displayed **324**. Count agreement alone does not establish a new independent frontmatter audit of every existing record. GitHub code search for `HnQ6hKLG` found no main record; PR search for the same script ID found no open PR. The ten open `research/*` PRs were inspected for source/rule overlap and none used this source or double-EMA zero-axis-gated MACD. Existing `macd-signal-cross-reversal-btcusdt-1d-2026-10-09.md` uses classic **uncompensated** MACD(12,26,9) with naked two-sided reversal, whereas this derivative uses a **double-EMA zero-lag compensation** on both legs, *both-lines negative-zone* entry and *both-lines positive-zone* exit to FLAT. This changes the core oscillator, event gate, position state and trade event set; not a trivial parameter variant.

## Falsification plan

Downstream only after independent admission and formal selection: compare the frozen double-EMA zero-zone derivative against a standard EMA(12,26,9) with identical axis gates and against the same double-EMA construction without the axis gates, using identical contiguous data and explicit costs. No experiment or performance claim is made here; only new unverified engine primitives require representative capability validation before mass screening.

## Crypto portability

The source description does not prove a BTC-specific result. This derivative is **BTC-USDT spot 1d only** by researcher choice. Other coins, timeframes, perpetual contracts, DCA BO/SO 6/6/6 or leverage are optional **separate downstream experiments** and may change events and cost paths; none is an HB_READY admission prerequisite or silently authorized here.

## Limitations

No fully readable original Pine block or revision hash; therefore no claim of lossless/source-native implementation. The double-EMA formula and axis strictness are explicit researcher interpretations, not verified author code. Spot MARKET same-close fills are simulator conventions and may be unattainable in live trading; true fees, spreads, slippage, lot/tick constraints and partial fills are not established. No stop may cause large drawdown. Package/source binding cites earlier independent review rather than a new installed-wheel hash. HB_READY is not profitability, Qlib parity, historical Survivor status or deployment approval.

## Implementation status

`not-implemented`: no controller or Qlib executable recipe added. A formally selected admitted record may later require a minimal strategy-specific implementation, without creating a second admission flag or registry.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Only independent Hermes Auditor review of the exact PR head may authorize a PASS merge. Scout must not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- TradingView, KaamBhaari, *Arpeet MACD*, 2025-02-05: https://www.tradingview.com/script/HnQ6hKLG-Arpeet-MACD/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged package/source binding and representative validation: https://github.com/HCH725/alpha-strategy-research/pull/414
