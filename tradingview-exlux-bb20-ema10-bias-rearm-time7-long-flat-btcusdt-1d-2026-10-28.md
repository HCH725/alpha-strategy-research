---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView exlux Bollinger-reclaim EMA10 persistent-bias seven-bar rearm — BTCUSDT spot 1d independent derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-11-07
sources:
  - https://www.tradingview.com/script/QJfC4zEj-BB-SPY-Mean-Reversion-Investment-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# exlux Bollinger-reclaim EMA10 persistent-bias seven-bar rearm — independent BTC-USDT spot 1d derivative

## Provenance

- **First-party TradingView source:** exlux, *BB SPY Mean Reversion Investment Strategy*, published **2025-11-07**, open-source public strategy, stable ID `QJfC4zEj`, https://www.tradingview.com/script/QJfC4zEj-BB-SPY-Mean-Reversion-Investment-Strategy/ . Author's complete publicly readable **description** inspected 2026-10-28; full Pine source and Pine version were **not** independently recovered. Do not attribute any researcher-pinned number below to undisclosed original Pine defaults.
- **Source-reported mechanism:** long setup = close crosses **up** through lower Bollinger band AND green candle AND close above long EMA; short setup = close crosses **down** through upper band AND red candle AND close below short EMA AND ADX strength gate. Source also describes an optional adaptive volatility-of-volatility BB multiplier, optional regime filter, ATR stops/targets/breakeven/time exits, and a persistent last-confirmed-direction **bias memory** which re-arms same-side entries after stop/target/time exits until a true opposite setup. Its stated demo is SPY daily, 5%-equity sizing, 0.03% commission, 3 ticks slippage, `process_orders_on_close` on, pyramiding zero. No performance claim was provided or reproduced.
- **This is a deliberately independent derivative, NOT a lossless Pine reproduction:** preserve the *lower-band recross + candle + EMA* long setup and *opposite upper-band recross* bias cancellation plus the *persistent rearm after time exit* mechanism; replace the unspecified original indicator variants/defaults with fully declared BB20 population-variance, EMA10 SMA seed, and 7-bar close-confirmed time exit. Disable the author's adaptive band, short-side ADX gate, optional regimes, ATR stops/targets/breakeven and short trading. Select BTC-USDT spot UTC daily candles, fixed 0.001 BTC, no slippage in the **historical research simulation**, 0.1% research fee per side, 10,000 USDT starting cash, explicit model-clock and ledger. These are researcher-designed changes, including the bearish setup's use solely as long cancellation; they can materially change all trade events and economics.
- **Frozen derivative identity:** `TV:QJfC4zEj|exlux|publication-2025-11-07|independent-derived-v1-20261028|BB20-pop2.0-EMA10-SMAseed|lower-upcross-green-EMA-long|upper-downcross-red-EMA-bearbias|bias-latch-time7-rearm|BinanceSpot-BTC-USDT-UTC1d|long-flat-Q0.001|effective-close-MARKET|fee0.001-slippage0|warmup100`. Any changed rule/clock/market/size/cost creates a different research revision.
- **Dedup snapshot:** `main` SHA `6e13f7ee38afe0e2f4dd3cbb284a679f5ee03fe5`, 397 root-level strategy records and README 397; GitHub main code search and open-PR search for `QJfC4zEj` returned none; the ten open research PRs were inspected. Nearest admitted families include `tradingview-forexobroker-bb20-adx14-rsi14-range-reversal-btcusdt-4h-20261027.md` (ADX/RSI recent-band-touch with frozen ATR bracket), `tradingview-thetraderlodge-bb18-volume-sma80-reclaim-long-btcusdt-4h-2026-10-25.md` (volume/SMA-gated lower recross with upper-band exit), and `hummingbot-bollinger-v1-bbp-extreme-long-flat-btcusdt-1d-2026-10-28.md` (outside-band level entry/exit). **None has the defining persistent directional bias and unconditional post-time-exit re-entry without a fresh lower-band recross.** This is an event/state-machine distinction, not a trivial parameter change.

## Economic mechanism

### Source-reported

The source describes a mean-reversion lower-band reclaim aligned with a bullish candle and EMA, plus bias memory that repeatedly re-arms the previously confirmed direction after an exit until an opposite setup. It describes volatility-adaptive bands and ATR risk modules, but the accessible description does not pin their exact formulas/defaults.

### Research interpretation

This independent long/flat variant tests whether a confirmed lower-band rebound establishes a **persistent long bias** rather than a one-shot entry. Every completed seven-bar holding segment closes at its own seventh subsequent close; while long bias persists, the next completed bar re-enters even without a new lower-band cross. A confirmed bearish upper-band recross cancels the long bias and exits immediately. Frequent re-entries can accumulate fees and risk; no expected return or original-source backtest equivalence is asserted.

## Signal

**Input and index:** contiguous fully completed Binance BTC-USDT UTC daily bars `O[t],H[t],L[t],C[t],V[t]`, indexed `t=0,1,...`; open timestamp `T[t]` increments exactly 86,400 seconds. Require finite positive OHLC, `H>=max(O,C)>=min(O,C)>=L`, and finite nonnegative base volume. Missing/duplicate/out-of-order/invalid candles **abort the research run** without invented bars, forward-fill, interpolation, price fallback or phantom fills.

1. **Bollinger 20, researcher-pinned:** for `t>=19`, `M[t]=sum(C[t-19..t])/20`; `SD[t]=sqrt(sum((C[i]-M[t])^2 for i=t-19..t)/20)` (population denominator 20); `LOW[t]=M[t]-2*SD[t]`; `UP[t]=M[t]+2*SD[t]`. Degenerate zero-width bands are allowed; strict cross and candle/EMA gates still apply. No adaptive multiplier, percent-rank, volatility-of-volatility or regime filter.
2. **EMA10, researcher-pinned:** `EMA[9]=mean(C[0..9])`; for `t>=10`, `EMA[t]=(2/11)*C[t]+(9/11)*EMA[t-1]`. Values before `t=9` are undefined and cannot signal.
3. **Bull setup `B[t]`:** `C[t-1]<=LOW[t-1] AND C[t]>LOW[t] AND C[t]>O[t] AND C[t]>EMA[t]`. The prior inequality is non-strict; current is strict. A green candle is strictly `C>O`; doji is not green.
4. **Bear setup `S[t]`:** `C[t-1]>=UP[t-1] AND C[t]<UP[t] AND C[t]<O[t] AND C[t]<EMA[t]`. This source-described bearish recross is **only a long-bias cancellation/long exit** in the derivative; the source's short entry, ADX gate and short-side risk are disabled. A red candle is strictly `C<O`; doji is not red.
5. **Warmup:** bars `0..99` are feature preparation only, with **no orders and no stored trade bias**. First decision is completed `t=100`; initialize `bias=NONE`, `position=FLAT`, `entry_index=null` immediately before that decision. Warmup setups are never replayed. No ML, fitted parameters, other markets or future information.
6. **Bias transition at each eligible completed bar:** if `B[t]`, set `bias=LONG`; else if `S[t]`, set `bias=BEAR`; else retain prior bias. If both flags somehow occur, abort as an invariant failure. No unconfirmed intrabar event changes bias. A repeated Bull while already LONG leaves the position unchanged; Bear has priority over any time exit.
7. **Order state, at most one action per bar:** (a) if `position=LONG` and (`S[t]` OR `t-entry_index>=7`), request a full SELL; label reason `bear-cancel` over `time7` when both true. (b) Else, if `position=FLAT` and `bias=LONG`, request one BUY. (c) Else HOLD. A SELL never creates a same-bar BUY; when time exit occurs while bias remains LONG, **re-enter on the next completed bar** without requiring another Bull. When Bear cancels bias, no re-entry occurs until a later Bull. `entry_index` is the filled BUY's bar index; earliest time exit is the seventh subsequent completed bar. BUY/SELL update position and entry_index **only on confirmed simulated fills**; while pending, suppress all additional actions and abort on failed/missing/partial/ambiguous fills. No overlapping position or same-bar reversal.
8. **Explicit disabled behavior:** shorts, margin, leverage, futures, funding, pyramiding, DCA/safety orders, hedging, partial exits, intrabar stop/target, resting stop/limit, ATR-based exits, breakeven, trailing, cooldown, discretionary exit, and end-of-sample forced liquidation. Time7 and Bear are the **only** exits. If LONG at the fixed research end, leave it open and mark unrealized value at last valid close, never invent a terminal SELL.

## Required data

Only the pinned Binance Spot `BTC-USDT` `1d` UTC OHLCV series; signals use O/C and trailing C windows, while H/L/V validate bar integrity. No order book, tick feed, non-OHLCV, multiple pairs/timeframes, fitted model, external reference data, shared portfolio allocation or perpetual funding. All indicators and state are computed sequentially from completed bars.

## Execution assumptions

- **Pinned capability boundary:** Hummingbot policy package `20260920`, `hummingbot/VERSION=dev-2.17.0`, immutable `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This commit's `setup.py` declares `20260729`, not `20260920`; do not conceal that metadata difference. Reuse the existing independently audited PR #414 wheel mapping: SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`, `VERSION`, and 902/902 shipped Python files byte-identical to the pinned commit, as recorded in the merged independent review. This Scout **did not re-hash the wheel bytes**. Evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 .
- **Actual source paths inspected:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `1d`; `.../binance_spot_candles.py` REST parser uses Binance kline open timestamp `row[0]`, OHLC `row[1..4]`, base volume `row[5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` iterates prepared feature rows, invokes controller actions and simulates against the **current-row-forward slice**; `.../executors_simulator/order_executor_simulator.py` MARKET fills at first supplied row's **close** with `filled_amount_quote=float(amount)*close`, `cum_fees_quote=trade_cost*quote`, `POSITION_HOLD` close type. `BacktestPositionHold` nets BUY/SELL in base units, tracks gross realized quote and cumulative quote fees separately. These are **specific engine semantics**, not a claim that a generic executor name alone is compatible.
- **Historical effective-close clock:** REST timestamp `T[t]` is bar OPEN; only after bar completion is `C[t]` available. Build the prepared decision/fill row with `effective_ts[t]=T[t]+86400` seconds, and align **both** feature availability and the engine's actual decision/fill clock to this completed-close timestamp. A MARKET action for completed bar `t` consumes the same prepared row's close at that effective model time. Never expose `C[t]` at `T[t]`. This is an explicit **zero-latency historical close-fill research model**, not a guarantee of real execution at that price after REST delivery.
- **Fixed model accounting:** `Q=Decimal("0.001") BTC`; initial cash `Decimal("10000") USDT`; single MARKET BUY/SELL, no short or other capital claim. Research `trade_cost=0.001` per side (0.1% of executed quote), modeled slippage `0` (explicit optimistic research assumption, **not** source's 3 ticks and not realized Binance fees). BUY requires `cash>=Q*C[t]*(1+0.001)`; after fill `cash-=Q*C[t]*(1+0.001)`, `inventory+=Q`. SELL requires confirmed `inventory==Q`; after fill `cash+=Q*C[t]*(1-0.001)`, `inventory-=Q`. Fees are deducted in quote on both sides; net realized PnL equals matched gross price difference minus **both** fees; equity is cash + inventory times current valid close. Use independent Decimal fill-confirmed ledger and reconcile engine `POSITION_HOLD` after its final flush; never substitute the gross-only `total_pnl`/position summary for fee-net equity. Engine float conversions may leave diagnostic residue: require `abs(base_delta)<=1e-12 BTC` and `abs(quote_delta)<=1e-8 USDT`; otherwise abort. Do not silently round actual strategy inventory to hide a material discrepancy.
- **Engine limitations:** controller-specific signal/bias/time state is specified here but **not implemented**. Existing `BacktestingEngineBase` can call a compatible controller and OrderExecutor MARKET primitive; the record does not claim a dedicated controller already exists. `terminated_executors_window=None` must retain complete ledger visibility; `positions_held` is tick-lagged and is **not** the fill-confirmation oracle. A missing/failed fill, unavailable historical close, nonpositive/NaN price, unsupported execution path, or unreconciled cash/position is an **abort**, not an assumed fill. Spot has no perpetual funding contract; no futures funding assumption is introduced. Exchange tick/lot/min-notional rounding, partial fills, order-book liquidity, latency and live spread are **not** modeled or authorized.

## Evidence

### Source-reported

First-party 2025-11-07 TradingView author description states BB lower recross + green candle + EMA long setup, upper recross + red candle + EMA bearish setup, persistent directional bias rearm after stop/target/time exits, optional adaptive multiplier/ATR risk, daily SPY demo and 5%-equity/0.03%-fee/3-tick assumptions. Full Pine is unavailable as directly verified text, so **no source-native code equality** or unpublished default values are claimed.

### Independently reproduced

This Scout directly read the pinned immutable Hummingbot `binance_spot_candles` parser/constants, `OrderExecutorSimulator`, and `BacktestingEngineBase` including `BacktestPositionHold` logic; confirmed the specific 1d/open-timestamp, MARKET-first-close, fee and hold-netting source paths. Existing independent review on PR #414 supplies the wheel-to-commit mapping (not rehashed here). Signal formulas and finite state machine above are fully researcher-defined; no strategy performance, Pine trade stream, live fill, or Qlib/HB parity was reproduced this cycle.

### Negative evidence

No same source ID in current main code search or open research PR search. Other BB/EMA records use different entry gates/exits and lack this strategy's persistent post-time-exit bias rearm. No accessible full Pine listing to verify the source's exact adaptive formula, ADX defaults, array implementation or native stop/target ordering; none of these are silently inherited. No independently verified real-world fee/slippage/lot constraints, funding series or profitability evidence.

## Falsification plan

Before any large-scale screening, test hand-constructed boundary sequences for lower/upper cross equality, EMA seed, green/red/doji, bias LONG/BEAR flips, no same-bar reentry, exactly seven subsequent bars per holding segment, repeated rearm after time exit, no rearm after Bear, insufficient cash and final open exposure. Verify prefix invariance when future candles are appended; validate prepared effective-close timestamps, last-row final-flush ledger and fee-net equity with a representative pinned-engine event-level test. **No such backtest or trading was run in this Scout cycle.**

## Crypto portability

This derivative intentionally changes SPY daily to Binance BTC-USDT spot daily, equity-percent sizing to fixed base units, and source broker costs to a declared historical spot model. It is not an assertion that the original SPY strategy or optional short/ADX/adaptive features are HB_READY on the pinned engine. Seven-coin/1h/4h/1d campaign and 6/6/6 DCA are downstream experiments, not admission prerequisites.

## Limitations

The source's Pine revision and adaptive-band/ATR implementation are not reconstructed. Repeated entries on a persistent LONG bias can occur without fresh signal and may accumulate fee drag. Seven-bar time exit does **not** protect against price collapse; stops and TP are intentionally absent. Same-completed-close simulated fills with zero slippage are idealized and not exchange executable. No profit, Qlib parity, survivor, canonical live economics or model-independent result is claimed.

## Implementation status

`not-implemented`: the fully specified bias-memory controller is a research-only executable specification, not a deployed Hummingbot strategy. A dedicated implementation may be materialized downstream only after admission; no new runner/registry/checker is proposed.

## Adoption boundary

`hb_ready_status: PASS` is a **Scout six-gate research admission claim pending independent Hermes Auditor review**. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. No Qlib screening, trading, Paper/Testnet/Live, container or workflow permission follows from this PR.

## Related Wiki records

No related Wiki records asserted. Nearby Alpha strategy-family files are named in Provenance for deduplication only; historical Survivor claims do not establish HB_READY.

## Sources

- https://www.tradingview.com/script/QJfC4zEj-BB-SPY-Mean-Reversion-Investment-Strategy/ — exlux, public author description, published 2025-11-07.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source (paths above).
- https://github.com/HCH725/alpha-strategy-research/pull/414 — previously independently reviewed wheel mapping and primitive evidence.
