---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradeMan PSY(12) 70/30 flip, independent BTC-USDT spot 1d long-flat derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-04
sources:
  - https://www.fmz.com/digest-topic/10257
  - https://www.fmz.com/digest-topic/10263
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradeMan PSY(12) 70/30 flip — explicitly independent BTC-USDT spot 1d long-flat derivative

## Provenance

- **Primary FMZ source:** *PSY（心理线）因子升级与改造* (*PSY Factor Upgrade and Transformation*), by **作手君TradeMan** (作手君量化小屋, a Quant Developer writing CTA/HFT/Arbitrage strategies), Digest created **2023-11-04**, updated **2023-11-06**. Chinese canonical page https://www.fmz.com/digest-topic/10257 and English mirror https://www.fmz.com/digest-topic/10263 were both fetched live over HTTPS and read end to end during this cycle (each HTTP 200, ~640KB landing HTML, article body plus code block byte-present; seven article gallery images downloaded and visually inspected).
- **Verified source-description facts (byte-present in both language versions):** the initial PSY construction ships as explicit code — count closes strictly rising versus the prior close over the last `n` bars, `PSY=(count/n)*100` (`if (data[i] > data[i-1]) count++`; ties are not counted up — deterministic, no tie-break needed). PART4 builds the traded momentum strategy on fixed thresholds: **做多/Go long: `PSY[0] > 70`; 平多/Close long: `PSY[0] < 30`; 做空/Go short: `PSY[0] < 30`; 平空/Close short: `PSY[0] > 70`**. The traded factor parameter is **12**; the traded venue is **币安U本位合约 / Binance U-denominated (USDT-margined) contracts** on **BTC-USDT and ETH-USDT**; the source backtest window is **2020-02-01 to 2021-12-31** with FMZ-backtester settings **滑点/slippage 10** (unit uninterpretable from text — fenced, never ported), **手续费/transaction fee 万5/0.05%**, **10倍/10x leverage**, **每次仓位剩余本金5% / each position 5% of remaining principal**.
- **Not source-native / not a lossless reconstruction.** This is a separately defined executable **derivative** pinned to the article's *initial* PSY factor. Researcher-declared adaptations are exactly: initial-PSY(12) factor instead of the article's tested final PSY+PRICE+VOL factor (PART4's preface attributes the tested signals to the final transformed factor — disclosed here, never presented as the tested variant); Binance BTC-USDT **spot** daily data instead of U-margined contracts; **LONG/FLAT** (the `< 30` leg closes rather than opens a short); the explicitly open bar period pinned to **1d** (the article states `N周期代表选定的计算周期，可以是几天、几周或几个月等` — no fixed period is specified, so 1d is a researcher pin, not a source fact); 120-bar contiguous warmup; completed-bar close decision/fill; one fixed 0.001 BTC unit; 10,000 USDT unborrowed starting cash; explicit modeled fee; missing-data handling; and all disabled behaviors. None of these is claimed to be a source fact.
- **Immutable strategy identity:** `FMZ-10257 | TradeMan-2023-11-04 | independent-derived-v1-initialPSY12-70-30-longflat | BinanceSpot-BTC-USDT-1d | 2026-10-25`. Changing factor variant, N, thresholds, timing, exits, venue, sizing or risk creates a new derived identity.

## Economic mechanism

Hypothesis only: the count of up-closes over twelve daily bars reads persistent buying pressure without any magnitude input; a print above 70 means at least 9 of the last 12 closes rose versus their predecessors (crowded optimism — the source trades it as momentum continuation, entering long); a print below 30 means at most 3 rose (exhausted buying — the source closes the long). The 30–70 corridor holds the current state through chop. No profitability or backtest result is asserted.

## Signal

**Causal input:** contiguous valid Binance spot BTC-USDT **1d UTC** candles `(T,O,H,L,C,V)`, where `T` is the daily **opening** Unix timestamp. A completed candle's information is available only at `T+86400` seconds. No signal uses the unfinished current candle or any volume field. Require finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, nonnegative finite V and exactly 86400 seconds between successive opening timestamps. Never forward-fill or fabricate missing prices.

**Pinned formula (source-verbatim initial PSY, N=12):**

1. For each completed-bar index `t >= 12`, define `U[t] = #{ i in [t-11, t] : C[i] > C[i-1] }` with strict `>` (equal closes are not up, exactly as the printed `if (data[i] > data[i-1])`). `PSY12[t] = 100 * U[t] / 12`, taking values `{0, 8.33…, …, 100}` in steps of `100/12`. No smoothing, no rounding, no alternative initialization is allowed; the value is a pure function of closes `C[t-12..t]`.
2. **Entry trigger:** `LONG_SIG[t] = (PSY12[t] > 70)`, i.e. `U[t] >= 9`. A print of exactly 70 is impossible for N=12 (8/12=66.67, 9/12=75), so the strict inequality needs no measure-zero fence.
3. **Exit trigger:** `FLAT_SIG[t] = (PSY12[t] < 30)`, i.e. `U[t] <= 3`. A print of exactly 30 is likewise impossible (3/12=25, 4/12=33.33).
4. **Decision state:** start `FLAT`. At the end of each valid fully closed bar after warmup: `FLAT+LONG_SIG` places one modeled BUY of `Q=0.001 BTC` if affordable; `LONG+FLAT_SIG` places one modeled SELL of the complete `Q`. All other combinations HOLD, including the entire 30–70 corridor in either state. The two triggers are disjoint by construction, so no bar fires both and no priority rule is needed or invented. Signals while already in the requested state are ignored; no same-bar reversal. After a full SELL the next qualifying `LONG_SIG` on a **later** completed bar may re-enter; zero-bar cooldown.
5. **Disabled:** shorting (the source's symmetric short leg is fenced in Provenance, not expressed here), borrowing/leverage/margin (the source's 10x is fenced, not ported), pyramiding, DCA, BO/SO, partial exits, other concurrent positions, fixed or trailing SL/TP, time-based exits, discretionary exit, maker/limit/next-open/intrabar orders, compounding, forced end-of-data liquidation and any cross-market portfolio logic. This derivative explicitly accepts the risk of an indefinite LONG without a stop.
6. **Warmup and invalid data:** require **120 consecutive valid completed 1d bars** before the first decision, far exceeding the 13-close minimum and supplying state history. At a missing/invalid/out-of-order bar, stop generating orders, discard state and require a fresh 120 valid contiguous bars before any new decision. An existing LONG is **not** sold at a fabricated price; the run is flagged data-incomplete and cannot yield claimable performance across the gap. No future data may be used to repair the gap or infer an earlier signal.

## Required data

Only one Binance BTC-USDT **spot** daily OHLCV feed with UTC opening timestamps and completed-bar closes; only the `C` series gates orders (O/H/L/V are validity checks). No funding stream, perpetual mark/index price, order book, higher/lower timeframe alignment, second market, fitted model, repainting pivot, future extrema or intrabar reconstruction. Computation at bar `t` uses only candles `0..t`. At dataset end an open position is valued at the last **valid available close**; it is not fictitiously liquidated.

## Execution assumptions — pinned Hummingbot compatibility

**Immutable engine pin:** Hummingbot policy package `20260920`, `VERSION=dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout verified the VERSION string and the following source paths at that exact commit by read-only inspection on 2026-10-25 (no working-tree modification). Separate wheel-to-source byte identity is supported by the **previously merged, independently reviewed Alpha PR #414**, which reports 902/902 wheel Python files matched the immutable source and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`. This cycle did **not** independently rehash any installed package.

- **Real candle path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` contains `"1d":"1d"`; `binance_spot_candles.py::_parse_rest_candles` converts exchange `row[0]` (kline open time) to opening seconds via `ensure_timestamp_in_seconds` and maps OHLCV from `row[1..5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` exposes the actual `open_bt/high_bt/low_bt/close_bt/volume_bt` and unsuffixed fields, indexes rows by the opening-time-derived `timestamp_bt`, and applies `dropna`. A strategy-specific controller can count strict close-over-prior-close events from those fields. **Validate original candle continuity before the engine's `dropna`**, which otherwise could hide missing rows; do not invent or silently backfill a close.
- **Controller/order path:** `BacktestingEngineBase.simulate_execution` iterates each processed row, invokes `update_state(row)`, then `controller.determine_executor_actions()`, and dispatches `CreateExecutorAction` to the real `OrderExecutorSimulator` (irrelevant `StopExecutorAction` branch untouched). `OrderExecutorConfig` supports `connector_name=binance`, `trading_pair=BTC-USDT`, BUY/SELL sides, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A dedicated controller/recipe is **not yet implemented**; this is bounded static model expressibility, not a claim of an already executable artifact.
- **Fill/timestamps:** the pinned `order_executor_simulator.py` MARKET path fills on the first supplied processed row at that row's **close** (`entry_price` from `close`, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`) and returns `CloseType.POSITION_HOLD`. The engine uses the **opening-time index** as raw fill timestamp; normalized economic/event decision and fill time in this derivative is **opening time + 86400 seconds**. This is a simulator same-close convention, **not** a live achievable post-close execution claim. The modeled MARKET path has full fill and no queue/partial fill; no claim of real liquidity or slippage measurement.
- **Position/cost:** `BacktestPositionHold._process_order` nets opposite-side base quantities and computes **gross** realized quote PnL; `add_executor` accumulates `cum_fees_quote`. Controller must use its own fill-confirmed FLAT/LONG state, not lagged snapshots, and must enforce the fixed cash budget. Initial cash `10,000 USDT`; BUY only if `cash >= 0.001*fill_close*(1+0.001)`. Research fee **assumption** `trade_cost=0.001` per side, deducted on both BUY and SELL, never attributed to the source (the source's 万5/0.05% FMZ setting is fenced in Provenance, not ported). `net_roundtrip_PnL = Q*(sell_close-buy_close) - 0.001*Q*buy_close - 0.001*Q*sell_close`. Marked equity while LONG is cash plus `Q*last_valid_close`, already net of paid BUY fee, without hypothetical SELL. Spot funding is **not applicable** (not invented as zero perpetual funding). Simulator has no extra modeled spread/impact/slippage, which is a limitation, not proof those costs are zero in reality.
- **Precision and boundary:** preserve Decimal quantities/cash and distinguish tiny float conversion residue from a tradable quantity. Exchange minimums, tick/lot rounding, latency, partial fills and realized fees are **unverified**, so this is not production exchange certification. No unsupported maker/next-open, cross-asset, perpetual margin or funding path is used. The spot daily MARKET close-fill/position ledger is the same previously independently reviewed **engine primitive**, not an assertion of strategy-specific backtest parity.

## HB_READY six-gate evidence (Scout proposal; independent review required)

1. **Determinism:** strict close-over-prior-close count, N=12, 70/30 strict thresholds with unreachable equality landings, corridor-hold state machine, warmup, data invalidation and affordability frozen; all adaptations explicitly derivative.
2. **Direction:** one Binance spot BTC-USDT LONG/FLAT unit, SHORT disabled.
3. **Entries/exits/risk:** above-70 enters, below-30 exits to flat; corridor holds; all other exits and stops explicitly disabled, including potentially prolonged exposure.
4. **Position/state:** one 0.001 BTC unit, nonborrowed 10,000 USDT affordability, no DCA/pyramiding/concurrency, complete exit, re-entry on later fresh signal, zero cooldown, gap fail-closed.
5. **Real pinned model:** immutable 1d Binance spot feed, inspected controller/order action and close-fill paths, fee-aware netted position ledger and timestamp normalization; no fabricated price/funding, unverified live precision clearly excluded. Package binding cited to independently merged PR #414.
6. **Point-in-time:** 120 completed UTC bars, only present/past closes, no indicator recursion or seed convention at all, no incomplete candle, future shift, leakage or missing-price substitution.

## Evidence

### Source-reported

TradeMan's 2023-11-04 FMZ article (updated 2023-11-06) ships the initial-PSY code (`data[i] > data[i-1]` count, `(count/n)*100`), the 70/30 long/close/short/cover rule pair (both language versions byte-verified), N=12, Binance U-margined BTC-USDT/ETH-USDT contracts, the 2020-02-01–2021-12-31 window, and FMZ settings (slippage 10, fee 0.05%, 10x, 5%-of-remaining-principal sizing). It does **not** establish a fixed bar period, author trade-fill conventions, or any independently reproduced return.

### Independently reproduced

**None.** No FMZ, Qlib or Hummingbot strategy backtest, event-level parity run, trading, paper/testnet/live order, wheel rehash or deployment occurred this cycle. Read-only inspection of pinned engine source is evidence of *model capability*, not executed strategy equivalence.

### Negative evidence and deduplication

Pre-write `main` SHA `0257cd6` held **325** root-level strategy Markdown records and README displayed **325**. Count agreement alone does not establish a new independent frontmatter audit of every existing record. Working-tree searches for `psy12`, `psy-12`, `psychological`, `TradeMan`, `作手君`, `10257` and `10263` return no strategy record using this source, author, indicator or construction (the single `psychological` hit is lunar-mood prose in an unrelated calendar record, not the PSY indicator). Open `research/*` PR search for the same terms returns nothing; the ten open `research/*` PRs were inspected for source/rule overlap and none uses this source or a close-count oscillator. Nearest pool neighbors differ in core construction: `forven-connors-rsi-oversold-recross` trades an RSI-of-streak composite recross, not a raw up-close count against fixed 70/30 bands; `vzo-tactic1` trades a volume-signed EMA ratio against ±40 bands with volume input, while this derivative reads closes only; return-sign momentum records (TSMOM/Novy-Marx family) test past-return direction, not breadth-of-up-closes. This changes the core oscillator, event gate and trade event set; not a trivial parameter variant.

## Falsification plan

Downstream only after independent admission and formal selection: compare the frozen initial-PSY(12) 70/30 long-flat derivative against the same rule with N=24 and against a 50-midline flip (long above 50, flat below 50) using identical contiguous data and explicit costs. No experiment or performance claim is made here; only new unverified engine primitives require representative capability validation before mass screening.

## Crypto portability

The source tests BTC-USDT and ETH-USDT U-margined contracts without proving a BTC-specific result. This derivative is **BTC-USDT spot 1d only** by researcher choice. ETH, other coins, other timeframes, perpetual contracts, DCA BO/SO 6/6/6 or leverage are optional **separate downstream experiments** and may change events and cost paths; none is an HB_READY admission prerequisite or silently authorized here.

## Limitations

No lossless/source-native claim: the tested source variant uses the final PSY+PRICE+VOL factor (whose image-printed code additionally uses a Close-vs-Open bar convention and asymmetric volume weighting, fenced here and not carried), while this derivative pins the text-printed initial PSY(12); the 1d period, spot venue, long-flat posture, sizing and costs are explicit researcher choices. The article's two equity-curve images (legends showing long and short legs) carry performance prints whose date axes contradict the article's stated 2020–2021 window, so no number from them is transcribed or claimed here. Spot MARKET same-close fills are simulator conventions and may be unattainable in live trading; true fees, spreads, slippage, lot/tick constraints and partial fills are not established. No stop may cause large drawdown. Package/source binding cites earlier independent review rather than a new installed-wheel hash. HB_READY is not profitability, Qlib parity, historical Survivor status or deployment approval.

## Implementation status

`not-implemented`: no controller or Qlib executable recipe added. A formally selected admitted record may later require a minimal strategy-specific implementation, without creating a second admission flag or registry.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Only independent Hermes Auditor review of the exact PR head may authorize a PASS merge. Scout must not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- FMZ, 作手君TradeMan, *PSY（心理线）因子升级与改造*, 2023-11-04 (updated 2023-11-06): https://www.fmz.com/digest-topic/10257
- FMZ, TradeMan, *PSY Factor Upgrade and Transformation* (English mirror): https://www.fmz.com/digest-topic/10263
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged package/source binding and representative validation: https://github.com/HCH725/alpha-strategy-research/pull/414
