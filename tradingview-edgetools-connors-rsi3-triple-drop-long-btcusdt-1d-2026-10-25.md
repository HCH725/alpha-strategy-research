---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView EdgeTools Connors RSI2 three-day declining-streak pullback, BTCUSDT spot 1d, explicitly derived long-flat research strategy
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
source_as_of: 2024-09-07
sources:
  - https://www.tradingview.com/script/QJSXeJnv/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EdgeTools Connors RSI2 three-day declining-streak pullback — independently derived BTC-USDT spot 1d strategy

## Provenance

- **TradingView primary source:** [Larry Connors RSI 3 Strategy](https://www.tradingview.com/script/QJSXeJnv/), author **EdgeTools**, published **2024-09-07**, public open-source listing. Script ID `QJSXeJnv`. The author description was read directly on 2026-10-25; the complete Pine source was **not** recoverable in the readable page. No Pine language version, undocumented author default, original fill convention or backtest statistic is asserted.
- **Source-description facts, and only these:** the published rule describes a daily price above the 200-day simple moving average, a **two-period** RSI, three consecutive daily RSI declines starting from an RSI value above 60, the resulting RSI below 10 for entry, and an RSI above 70 for exit. The title says “RSI 3” but the author's description explicitly says **RSI length 2** and **three-day decline**; those are different quantities.
- **Explicit independent derivative, NOT lossless/source-native execution:** the research record fixes Binance BTC-USDT spot 1d, a precise Wilder RSI(2) seed/zero-denominator convention, strict boundary comparisons and three-drop indexing, 220-bar warmup, gaps, one fixed position, cash constraint, same-row completed-close simulator fills, fee and position accounting. These are researcher-defined choices where the public description lacks executable details. No claim is made that the unavailable Pine source implements these exact choices. All source-native statements are confined to the preceding bullet.
- **Immutable derived strategy identity:** `TV-QJSXeJnv | EdgeTools-2024-09-07 | derived-v1-WilderRSI2-3strictDrops-fromAbove60-below10-SMA200-long-exitRSIabove70 | BinanceSpot-BTC-USDT-1d | 2026-10-25`. Changing RSI initialization, thresholds, signal bar, venue, fill convention, exit or capital rule creates a different derivative.

## Economic mechanism

Hypothesis only: in an SMA200 uptrend, a three-session acceleration into RSI2 oversold territory may represent temporary selling exhaustion; the RSI>70 recovery is the defined mean-reversion exit. This is **not** a measured performance or profitability claim. The long may lose heavily without a protective stop.

## Signal

**Input:** consecutive UTC Binance spot BTC-USDT daily candles, each `(T, open, high, low, close, volume)`; `T` is the UTC daily **open** timestamp and the entire bar is available only at effective time `T+86400 seconds`. No signal uses an incomplete bar. Require finite OHLCV, `high >= max(open,close) > 0`, `low <= min(open,close)`, `low>0`, `volume>=0`, and exact 86400-second spacing. Otherwise the sequence is invalid; see gap rule.

1. `SMA200[t] = (close[t] + ... + close[t-199])/200`, arithmetic mean of **200 completed daily closes**. No forward fill.
2. Wilder RSI(2), a **researcher-pinned interpretation** of the source's “2-period RSI”: `delta[t]=close[t]-close[t-1]`, `gain[t]=max(delta[t],0)`, `loss[t]=max(-delta[t],0)`. At index 2 of a fresh valid run, initialize `G[2]=(gain[1]+gain[2])/2`, `L[2]=(loss[1]+loss[2])/2`. For `t>=3`, `G[t]=(G[t-1]+gain[t])/2`, `L[t]=(L[t-1]+loss[t])/2`. If `G>0,L=0`, RSI=100; if `G=0,L>0`, RSI=0; if both are zero, RSI is **undefined** and no entry/exit is emitted on that bar; otherwise `RSI[t]=100*G[t]/(G[t]+L[t])`. Never divide by zero or substitute a fabricated oscillator value. No intermediate rounding.
3. `threeDrop[t] = RSI[t-3]>60 AND RSI[t-3]>RSI[t-2] AND RSI[t-2]>RSI[t-1] AND RSI[t-1]>RSI[t]`. All four RSI observations must be defined and based on completed candles. This pins the “first drop from above 60” as the reading **before** the first of exactly three consecutive strict daily declines; a fourth earlier decline does not disqualify the last three.
4. `enter[t] = close[t]>SMA200[t] AND threeDrop[t] AND RSI[t]<10`. Equality to the MA or 10 fails; the source's threshold prose does not supply equality conventions, so strictness is part of this derivative.
5. `exit[t] = RSI[t]>70` regardless of the current SMA200 state. Equality to 70 holds the position. No extra trend-filter exit, reversal, trailing stop or threshold-cross requirement is silently added.
6. **State machine:** initial `FLAT`; after warmup, `FLAT + enter` buys `Q=0.001 BTC` once if sufficient quote cash, and transitions to `LONG` on the simulated full fill. `LONG + exit` sells exactly the held `Q`, and transitions to `FLAT` on the simulated full fill. Otherwise HOLD. Exit has priority if a conflict ever arises (these RSI<10 and RSI>70 predicates cannot coincide). Entry signals while LONG and exits while FLAT are ignored. At most one order per completed bar. Re-entry requires a **later** fresh qualifying three-drop signal; no same-bar flip.
7. **Disabled behaviors:** SHORT, margin/leverage, pyramiding, DCA/BO/SO, partial exits, additional concurrent positions, stop-loss, take-profit, time-based exit, trailing exit, maker/limit/intrabar orders, portfolio allocation, compounding and scheduled forced liquidation. Cooldown is zero completed bars after an exit. At dataset end a remaining LONG is marked at the last **valid available** close, with no invented sale.
8. **Warmup and gaps:** first possible decision only after **220 contiguous valid completed 1d bars** from the start of the current uninterrupted run, including 200 for SMA and all RSI seeds/streak history. A missing daily timestamp, invalid OHLCV, missing close or nonfinite indicator resets indicator seeds and the 220-bar consecutive count; no signal or synthetic fill during suspension. If already LONG, keep that position without inventing a protective liquidation; trading resumes only after a fresh 220-bar contiguous run. No use of a future bar to repair the gap.

## Required data

Single-asset Binance BTC-USDT **spot 1d OHLCV** only; signals actually consume close and UTC timestamps, while OHLCV validity checks protect the data path. No funding, perpetual mark/index price, order book, multi-market synchronization, lower-timeframe fill reconstruction, intrabar data, future extrema, ML training or `request.security` is required. For every `t`, features use only the prefix ending at `t`; the causal/effective decision and model-fill time is `T[t]+86400`, never the source feed's open-time label `T[t]`.

## Execution assumptions — pinned Hummingbot compatibility

**Pinned benchmark:** policy package `20260920`, VERSION `dev-2.17.0`, immutable `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle independently fetched that commit's `hummingbot/VERSION` (returns `dev-2.17.0`), Binance spot 1d constants/parser, `backtesting_engine_base.py`, `order_executor_simulator.py`, `order_executor/data_types.py`, and validation code through GitHub. The separate **package-to-source byte identity** was independently reviewed in accepted [Alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414): wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`, 902/902 shipped Python files matched that immutable source. This Scout **did not** rehash the installed wheel and does not claim it did.

- **Real data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `"1d":"1d"`. `binance_spot_candles.py` maps REST kline `row[0]` to open-time seconds and `row[1..5]` to OHLCV; `BacktestingEngineBase.prepare_market_data()` exposes `open_bt/high_bt/low_bt/close_bt/volume_bt` and unsuffixed OHLCV to the processed rows. A strategy-specific controller can compute the fully specified SMA/RSI/streak from these real fields. The input-validation/gap policy above must run on the original timestamp series **before** any `dropna`/feature merge could hide a gap.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution()` iterates rows, calls `update_state(row)`, then `controller.determine_executor_actions()`; `CreateExecutorAction` dispatches to `simulate_executor`. `OrderExecutorConfig` supports `connector_name=binance`, `trading_pair=BTC-USDT`, BUY/SELL, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A dedicated controller is **not yet implemented**; the claim is model expressibility using this inspected path, not that an executable recipe already exists.
- **Fill semantics:** the pinned `OrderExecutorSimulator.simulate()` MARKET branch fills on the **first supplied processed candle** at its `close`, computes `filled_amount_quote=amount*close`, charges `cum_fees_quote=trade_cost*filled_amount_quote`, and returns `POSITION_HOLD`. The raw simulator fill timestamp equals the candle's **open-time index**, so downstream event/replay timestamps must explicitly be normalized to **open+86400 seconds**. This is a declared **research close-fill convention**, not a guarantee that a live market order sent after seeing the close can receive that same price. No next-open/maker/intrabar capability is assumed.
- **State/accounting:** `BacktestPositionHold._process_order()` nets opposite BUY/SELL quantities and realizes matched gross quote PnL; `add_executor()` accumulates both sides' `cum_fees_quote`. The dedicated controller must keep immediate simulated fill-confirmed FLAT/LONG state; do not infer permission to re-enter from the one-tick-lagged `positions_held` or bounded terminated-executor view. Use `Decimal` position/cash records; tiny float-conversion residue (<1e-12 BTC) is accounting tolerance, **not** a new order or a true position.
- **Declared economics:** fixed research initial quote cash **10,000 USDT**, one `0.001 BTC` unit, no borrowing; a BUY requires `cash >= Q*close*(1+0.001)`, otherwise skips without debt or synthetic fill. Simulate `trade_cost=0.001` **per side** (0.1% of each filled quote notional); cash decreases by BUY notional plus fee and increases by SELL notional minus fee. Realized **net** quote PnL for a round trip = `Q*(sell_close-buy_close) - fee_buy - fee_sell`; unrealized mark uses last valid close, with paid fees already reflected in cash, and no hypothetical liquidation fee. `BacktestPositionHold.realized_pnl_quote` is **gross**; never mislabel its value or a generic `net_pnl_quote` summary as complete fee-after-equity. Spot funding is **not applicable**, not an invented zero futures funding stream. Simulator adds no spread/impact/slippage; zero *additional modeled* slippage is a stated limitation, not a market observation. Lot/tick rounding, exchange minimums, partial fills, actual spreads, latency and production affordability remain unverified and are **not** represented as live-compatible.
- **Primitive boundary:** single completed-candle signal + same-row-close MARKET OrderExecutor + one spot netted position is the previously independently reviewed model capability (e.g. accepted PR #414 and #425). No new non-OHLCV, shared-capital, next-open or funding primitive is claimed. Any later Qlib large-scale screening must reuse a verified representative execution primitive; no per-candidate performance/parity proof is claimed here.

## HB_READY six-gate evidence (researcher's claim; independent audit still required)

1. **Determinism:** full Wilder RSI seed/recursion, undefined cases, SMA200, three-drop indexing, strict inequalities, warmup, gap handling and priority are frozen; the absence of Pine code is disclosed, with all extra choices explicitly derivative.
2. **Direction:** BTC-USDT spot LONG/FLAT; shorts and leverage disabled.
3. **Entry/exit/risk:** trend+three-drop+RSI<10 entry, RSI>70 exit, every other exit/risk behavior explicitly disabled.
4. **State:** 0.001 BTC at most once, 10,000 USDT nonborrowed cash budget, full exit, no pyramiding/DCA/concurrency/compounding, zero cooldown and explicit re-entry/invalid-bar behavior.
5. **Pinned engine:** verified immutable 1d spot candle columns and timestamp, real MARKET close-fill OrderExecutor dispatch, POSITION_HOLD netting, both-side fees, spot no-funding boundary and explicit precision limitations; package/source binding is cited to a prior independent accepted review rather than reasserted.
6. **Causality:** 220 completed daily bars, no future data, no incomplete candle, gap fail-closed, and the simulator's open-label timestamp is corrected to the causal close-time for event interpretation.

## Evidence

### Source-reported
The TradingView author description specifies SMA200 uptrend, RSI length 2, three daily RSI declines starting above 60, entry below RSI10 and exit above RSI70. It does **not** supply independently readable Pine execution defaults or a verifiable numerical backtest. Do not attribute the researcher-pinned RSI initialization, sizing, fees, gaps, strictness or fills to EdgeTools.

### Independently reproduced
**Not independently reproduced.** This cycle performed read-only primary-page inspection and pinned-engine static source inspection, not an original TradingView strategy run, Hummingbot backtest, Qlib parity run, profitability calculation or live trade.

### Negative evidence and deduplication
At pre-write `main` SHA `18dfc58ab9c67b3cac6d622609e1b0ee455b827f`, the GitHub tree contained **318** root-level strategy Markdown files and README advertised **318**; count equality is not a fresh independent frontmatter audit of all 318. GitHub code search for script ID `QJSXeJnv` returned no admitted file; GitHub PR search found no same-source PR, and the open `research/*` PRs inspected carried different sources/rules. Nearby admitted `connors-rsi2-ma70-fade-two-sided-btcusdt-1d-2026-10-10.md` uses a **70-bar MA, two-sided RSI2 90/10 tail fade without a three-day decline**; `forven-connors-rsi-oversold-recross-long-flat-btcusdt-1h-2026-10-18.md` uses a **three-component Connors RSI(3/2/100) composite crossing back above 10**, not the EdgeTools daily RSI2 three-strict-decline sequence. This candidate is not a mere renamed or reparameterized duplicate.

## Falsification plan

Downstream only, if independently admitted and formally selected: freeze the above exact derivative and compare its 3-drop entry sequence against a same-SMA200/RSI2<10 entry without the decline condition, using the same fees, fill model and contiguous IS/OOS periods. A separate model-consistent execution/parity capability check is needed if any **new** primitive is introduced. No experiment was run in this Scout cycle.

## Crypto portability

The author's public description is generic, not a verified BTC backtest. This derivative restricts to BTC-USDT spot daily candles; application to other pairs, futures or intervals is a **new declared experiment** and must not be presumed equivalent to the author or to the fixed admission record. The optional seven-coin, 1h/4h/1d and BO/SO 6/6/6 downstream campaign is not an entry gate and would change events if applied here.

## Limitations

Full original Pine source and its broker/fill defaults unavailable; no source-native/lossless claim. A strict RSI2 three-day decline from >60 to <10 may be rare; absence of a stop exposes capital to prolonged drawdowns and data gaps. The Hummingbot simulator's same-close market fill, fixed fee and no added slippage do not reproduce real exchange latency, precision, liquidity or spreads. The package binding relies on existing independent review rather than a wheel rehash this cycle. This record is neither a historical Survivor nor a trading authorization.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller or Qlib executable recipe was added. After independent admission, downstream selection may require a minimal strategy-specific implementation; this is not a second HB_READY admission gate.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor must verify the exact PR head, all six gates and PASS-only main invariant before any merge. Scout does not approve, merge, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- TradingView EdgeTools, *Larry Connors RSI 3 Strategy*, published 2024-09-07: https://www.tradingview.com/script/QJSXeJnv/
- Immutable Hummingbot code inspected: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent package/source binding and primitive review: https://github.com/HCH725/alpha-strategy-research/pull/414
