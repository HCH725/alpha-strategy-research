---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradeDots dual prior-20 price/volume maxima breakout with SMA50 trend and exit — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2024-05-17
sources:
  - https://www.tradingview.com/script/jc2hs2qK-Price-and-Volume-Breakout-Buy-Strategy-TradeDots/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradeDots-inspired simultaneous price and volume maxima breakout — independently derived BTC-USDT 1h research strategy

## Provenance

- **First-party public TradingView source:** *Price and Volume Breakout Buy Strategy [TradeDots]*, author **tradedots**, canonical public script ID **jc2hs2qK**, first published **2024-05-06**, updated **2024-05-17** (release note adds selectable Long/Short/Long-and-Short directions and bearish price/volume breakout). Primary URL: https://www.tradingview.com/script/jc2hs2qK-Price-and-Volume-Breakout-Buy-Strategy-TradeDots/ . Source page read on **2026-10-28**. Its public prose states a trade requires **both closing price and volume to exceed the maxima of a lookback window**, with price also above a trend moving average. It reports original example commission **0.01%**, initial capital **10,000 USD** and **70% equity per trade**; these are **source example settings**, not this derivative's costs/sizing.
- **Original Pine revision and complete source code not retrieved.** TradingView labels the script open-source, but the page's retrievable text does not expose full Pine, its version, exact lookback lengths, moving-average length/type, exit conditions, pyramiding, order timing or executable fee behavior. No source-native/lossless claim is made and no source backtest statistic is independently reproduced.
- **Deliberate independent derivative v1 (researcher choices, NOT attributed to tradedots):** Binance **BTC-USDT spot, UTC 1h**, previous **20** complete bars' **close** maximum and **base-volume** maximum (strictly prior bars), current-close **SMA50** trend filter, LONG/FLAT only, **close-below-SMA50 exit**, fixed **0.001 BTC** single-unit size, initial **10,000 USDT** cash, completed-bar same-row-close idealized MARKET fills, **0.1% per filled side** research fee, no extra modeled slippage, **100** complete-bar warmup, explicit gap reset and no-stop/no-DCA state. Original author does not supply or endorse these selected numbers, market, exit, costs, fill conventions or state rules. The 2024-05-17 author release allows both directions; this derivative explicitly disables shorts.
- **Immutable research identity:** `TV:jc2hs2qK|tradedots|2024-05-17|independent-derived-v1-20261028|BinanceSpot:BTC-USDT:UTC1h|C>max(prior20-C)|V>max(prior20-baseV)|C>SMA50(C-current)|exit:C<SMA50(C-current)|LONG-FLAT|Q=0.001BTC|cash=10000USDT|fee=0.001-side|MARKET-same-completed-close|warmup100|no-SL-TP-DCA`. Changing any source identity, market, frame, formula, threshold, exit, execution, or risk state creates a different derivative.

## Economic mechanism

### Source-reported
The author describes a joint breakout in closing price and traded volume above their respective historical maxima, gated by a moving-average trend. The proposed mechanism is momentum continuation accompanied by unusually strong participation. The author describes suitability for volatile assets such as BTC and ETH but does not prove profitability of this frozen derivative.

### Research interpretation
Requiring a **new 20-bar closing-price high AND a new 20-bar base-volume high on the same completed hour** is materially stricter than a price-only Donchian breakout, volume-above-mean gate, or prior-hour volume-multiple impulse. A 50-bar SMA gate seeks to exclude downward regimes; the SMA-level exit exits when the medium trend weakens. The resulting strategy may have few trades, miss sustained trends, and hold large drawdowns because no stop exists. This is an untested hypothesis, not a survivor or performance claim.

## Signal

**Gate 1 — complete deterministic formula and data contract.**

1. Input is one chronological series of real Binance spot BTC-USDT **UTC-aligned 1h OHLCV** candles indexed `t=0,1,...`. Exchange `T[t]` is the candle **opening** Unix timestamp; full `O[t],H[t],L[t],C[t],V[t]` become eligible at effective `E[t]=T[t]+3600 seconds`. `V[t]` is the actual Binance base-asset (BTC) volume, not quote volume or number of trades. All decisions require the completed candle.
2. A valid candle has a unique open timestamp at exactly consecutive 3600-second increments, aligned to UTC hours; finite positive `O,H,L,C`, `L<=min(O,C)<=max(O,C)<=H`, finite `V>=0`. Reject any missing, duplicate, out-of-order, non-consecutive, non-finite or impossible candle. Never synthesize a close, volume, or fill. A gap starts a fresh contiguous indicator segment, but does not fabricate liquidation of an already-held BTC position.
3. `Pmax20[t] = max(C[t-20],...,C[t-1])` for `t>=20` within the current contiguous segment. **Current close is excluded from its own breakout reference.** This use of *close* rather than high is a researcher-selected literal interpretation of the source's stated **closing-price maximum**.
4. `Vmax20[t] = max(V[t-20],...,V[t-1])` for `t>=20`, also strictly excluding current volume. Zero-volume historical bars remain valid zeros; no zero-denominator ratio or missing-volume fallback exists.
5. `SMA50[t] = (C[t-49]+...+C[t])/50` for `t>=49` in the contiguous segment. The current **completed** close participates. This SMA type, length and price input are researcher-pinned, not verified original Pine defaults.
6. `entryRaw[t] = (C[t] > Pmax20[t]) AND (V[t] > Vmax20[t]) AND (C[t] > SMA50[t])`, evaluated only after the 100-bar warmup. Every comparison is **strict**; equality fails. No `crossover` or one-bar momentum test is implied. No new event is emitted on NaN/undefined input.
7. `exitRaw[t] = (C[t] < SMA50[t])`, evaluated only after warmup. Equality to SMA50 is a HOLD; exit is not conditional on profit, a volume event, or an opposite short. `entryRaw` and `exitRaw` are mutually exclusive because one requires `C>SMA50` and the other `C<SMA50`; equality triggers neither.
8. State machine: start `FLAT` with 0 BTC, 10,000 USDT. On a completed eligible bar, `FLAT && entryRaw` submits **one** MARKET BUY for exactly 0.001 BTC at modeled actual `C[t]`, only if available cash covers `0.001*C[t]*(1+0.001)`. Insufficient cash means no fill, remain FLAT; no queued/retried order and no partial sizing. `LONG && exitRaw` submits **one** MARKET SELL of the entire 0.001 BTC at modeled actual `C[t]`; after confirmed fill return FLAT. `LONG && entryRaw`, `FLAT && exitRaw` and neither-signal are no-ops. State changes **only on confirmed simulated fills**; unexpected failures must fail closed, not assume a fill. One order maximum per completed bar. A qualifying new breakout may re-enter on any later bar after an exit; **no cooldown** or re-arm latch. If either action were to conflict due to an implementation bug, halt as an invariant violation rather than guess priority.
9. **Gate 2/3/4 — market, risk and position:** Spot LONG/FLAT only; short, borrowing, futures, funding, margin and leverage >1 disabled. Maximum one 0.001 BTC long and one open order, no pyramiding, DCA/safety orders, averaging, partial exits, shared portfolio allocation, concurrency across pairs, or order stacking. No fixed SL, TP, trailing stop, profit gate, time limit, intrabar stop/limit/maker order, discretionary override or forced sample-end close. These features are **intentionally disabled**; a long can remain open indefinitely until an exit signal. At sample end mark the remaining position using last valid observed close without fabricating a SELL.
10. **Warmup/invalidity:** First **100** consecutive valid completed 1h candles of each contiguous segment are indicator-only, no orders; first tradable candle is segment index 100 (101st complete candle). A gap/invalid bar stops all decisions, resets price/volume/SMA windows and requires another 100 valid completed candles before orders. If already LONG, preserve the actual 0.001 BTC position and last known valid mark during the gap, with no synthetic trade; resume exits only after re-warmup. No future or revised bars, negative shifts, whole-sample normalization, model training or intrabar lookahead.

## Required data

Only one Binance BTC-USDT **spot 1h** OHLCV stream, with exchange opening timestamps and actual historical closes/base volume. Historical `high/low/open` are used for validation, not trade conditions. No second asset, higher timeframe, cross-market join, L2 book, tick stream, on-chain, OI, funding, mark/index price, synthetic candle or external calendar input. No missing-price fallback is allowed. One completed bar per decision and one known real close per modeled order.

## Execution assumptions

**Gate 5 — pinned, inspected Hummingbot execution/data/cost model.**

- Policy pin: Hummingbot package **`20260920`**, VERSION **`dev-2.17.0`**, immutable source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. The source's `setup.py` package string `20260729` is **not** the policy package label. Independently reviewed [alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414) reports wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148` and **902/902 shipped Python files** byte-matched to the pinned source. This Scout directly inspected the pinned source paths but **did not** independently redownload the wheel or verify a deployed image; Auditor must check that prior wheel evidence applies, or fail Gate 5.
- Direct GitHub connector inspection on 2026-10-28: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1h`; `binance_spot_candles.py::_parse_rest_candles` maps Binance REST `row[0]` to candle **open** time, `row[1..5]` to O/H/L/C/**base V**; `BacktestingDataProvider.get_candles_df` reads a feed keyed by connector/pair/interval. A dedicated future controller must shift signal/fill effective time to `E[t]`; raw `timestamp=T[t]` is **not** the time that `C[t]` was known.
- Directly inspected `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: the engine advances historical rows, calls controller `determine_executor_actions()`, processes `CreateExecutorAction`, and maintains `BacktestPositionHold` netting/fee state. Directly inspected `hummingbot/strategy_v2/executors/order_executor/data_types.py`: `OrderExecutorConfig` accepts `connector_name=binance`, `trading_pair=BTC-USDT`, `TradeType.BUY/SELL`, `ExecutionStrategy.MARKET`, `amount=Decimal('0.001')`, `leverage=1`. This is a **proposed controller mapping**, not a claim that a dedicated implementation already exists.
- Directly inspected `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: MARKET fills on the **first supplied row's close**; `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and close type `POSITION_HOLD`. Feed **the decision bar's own fully completed row** into that simulator with effective event time `E[t]` to model idealized same-completed-close fills. This is a historical simulator convention, **not** a promise of an executable real-market close after data publication; next-open, maker, limit, intrabar or live partial-fill semantics are not claimed.
- **Research cash/fee ledger:** exact fixed `Q=Decimal('0.001') BTC`, starting `cash=Decimal('10000') USDT`, modeled `trade_cost=0.001` **per filled side** (0.1% of notional on both BUY and SELL). BUY cash debit `Q*C*(1+0.001)`; SELL cash credit `Q*C*(1-0.001)`. Track separate Decimal cash/BTC state and reconcile with actual simulator fill/fee and `BacktestPositionHold` netting events; do **not** confuse gross `net_pnl_quote`/summary labels with net-of-fee equity. Float-to-Decimal reconciliation tolerances: at most `1e-9 BTC` in quantity and `1e-8 USDT` in fee/cash residual, otherwise stop as unsupported rather than silently rounding away a material discrepancy. The simulator is a simplified historical model, not an exchange-accurate fill, tick, lot, minimum-notional or spread model.
- **Costs/economics:** additional **modeled** slippage = 0 under this expressly idealized close-price simulation; actual bid/ask, latency, slippage, exchange fees, rounding, order rejection and partial fills are **not verified** and must never be described as zero. If observed data or required simulated fill price is missing, **do not trade**. `BacktestingDataProvider.get_price_by_type` contains a `Decimal('1')` missing-price fallback; it is expressly prohibited for fills, PnL and marking here. Spot cash/BTC unleveraged accounting makes perpetual funding, liquidation and futures margin **inapplicable**, not hypothetically zero on a perpetual. The author's 0.01% example commission and 70% equity sizing are not this derivative's modeled fee or sizing.
- **Capability reuse, not new engine proof:** the same pinned single-market Binance spot 1h OHLCV, MARKET-close, POSITION_HOLD, and fee primitive has prior independent review evidence in PRs **#414, #550, #553 and #570**. The new joint previous-20 close/volume extrema and SMA50 are deterministic controller-side predicates; they require no new engine data, order type or portfolio primitive. This cycle ran **no** Hummingbot or Qlib backtest, did not build a controller, and did not validate any new execution path. If implementation requires a genuinely new primitive, representative Hummingbot/Qlib event-level parity is required **before** large-scale screening, not a seventh admission gate.

## Evidence

### Source-reported
Primary TradingView page by tradedots, published 2024-05-06, updated 2024-05-17: closing price and volume must **both** exceed prior-window maxima and price must be above a moving average. Author's illustrative settings: commission 0.01%, initial capital 10,000 USD, 70% equity per trade. The May 17 release note adds selectable trade directions and bearish breakout. No precise lookback/MA lengths, Pine-version proof, source-native exit, historical performance reproduction or fee/fill proof was obtained.

### Independently reproduced
**Not independently reproduced.** Only public source facts and pinned Hummingbot source-code capability paths were inspected; no candidate-specific TradingView/Pine, Qlib or Hummingbot replay, performance calculation or live trade was performed. Prior audited engine primitive evidence is **cited**, not claimed as this candidate's own experimental result.

### Negative evidence and deduplication
- At pre-write main SHA `3f2c0671a317e0ea47127b5c5f5e652c4f687522`, GitHub tree enumerated **415** root strategy Markdown records, README counter **415**. Fifteen evenly distributed records' frontmatter were directly sampled, all `hb_ready_status: PASS`; **not** a complete 415-file admission audit. No numerical mismatch was present.
- Connected GitHub default-branch search for `jc2hs2qK` returned no match; PR search for exact source ID returned none. Open research PRs were enumerated and none cited this TradingView script or this simultaneous **previous-20 closing-price maximum + previous-20 base-volume maximum + SMA50** entry and SMA50 exit. An unrelated TradeDots stochastic-Z-score PR #449 concerns a different source and signal.
- Nearest pool families differ materially: `forven-atr-volume-breakout-long-flat-ethusdt-1h-2026-10-17.md` uses a Donchian **high + ATR buffer** with volume versus **20-bar mean** and EMA12 exit; `tradingview-ai-volume-quadruple-atr-cooldown-long-btcusdt-1h-2026-10-28.md` uses **prior-bar 4x volume**, 1.5% price impulse, ATR cap and cooldown; `tradingview-fyntrade-zvr-utc-cumulative-volume-breakout-long-btcusdt-1h-2026-10-28.md` uses **same-elapsed-UTC-day cumulative-volume pacing**, not single-bar volume records; `gervais-kaniel-mingelgrin-high-volume-premium-long-flat-btcusdt-1d-2026-10-14.md` uses a high-volume event and fixed holding window without simultaneous closing-price breakout. The joint **record-high volume and record-high close** conjunction is a different construction, not a trivial parameter change.
- The author's Pine code and original executable exits are unavailable in the retrieved source text; **never** attribute this derivative's SMA50 exit, windows, sizing, warmup or MARKET-close model to the author. No source-native parity, profit or historical survivor evidence is asserted. A strategy can be HB_READY-model-expressible while remaining economically unprofitable.

## Falsification plan

Only in a separately authorized downstream campaign: freeze this exact rule, costs, input history and evaluation windows; compare (i) joint-max breakout against price-only prior20 max, (ii) prior20 **maximum** volume gate against volume-above-mean gate, and (iii) SMA50 exit against a predeclared alternative, using IS only for candidate selection and untouched OOS. Record trade-by-trade model timing/cost discrepancies; no hindsight tuning or OOS leakage. Do not claim Hummingbot certification before the separate canonical HB replay and economic reconciliation.

## Crypto portability

The frozen proposal is **BTC-USDT spot 1h** LONG/FLAT. BTC/ETH/BNB/SOL/XRP/DOGE/LINK, 1h/4h/1d, 3x/5x futures and BO/SO 6/6/6 are **optional downstream campaign settings**, not HB_READY entry gates. Adopting any different venue, interval, leverage, DCA, fill convention or cost model creates a distinct declared experiment with the corresponding execution/data/funding proof.

## Limitations

The TradingView description supplies the conceptual entry, **not** a complete verified Pine strategy. This independently specified derivative is the only object assessed for the six gates. Historical MARKET-close fills are idealized; no exchange-realistic post-close execution, tick/lot rounding, fee tier, slippage, partial-fill, or perpetual funding is claimed. No stop means a held position may suffer large losses. Missing candles suspend orders and require re-warmup. `hb_ready_status: PASS` is a **Scout proposal subject to independent exact-head Hermes Auditor verification**, not a self-approved admission, Qlib executable, survivor, profitability or trading authorization.

## Implementation status

`not-implemented`: no strategy-specific Hummingbot controller, Qlib executable recipe or deployment artifact was built. No second eligibility status is created; implementation is separate from six-gate research admission.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. The independent Hermes Auditor GitHub Webhook Review alone may remediate source-verifiable facts, exact-head PASS merge or NOT_LOSSLESS close. Scout never approves, merges, closes, edits main/README, runs backtests/trading or modifies workflows.

## Related Wiki records

None created or modified; adjacent existing root strategy families are identified in Negative evidence solely for deduplication.

## Sources

- https://www.tradingview.com/script/jc2hs2qK-Price-and-Volume-Breakout-Buy-Strategy-TradeDots/ — tradedots, first published 2024-05-06, updated 2024-05-17; public source concept.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned Hummingbot engine source inspected for this record.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — independently reviewed package-to-source byte evidence and engine primitive.
- https://github.com/HCH725/alpha-strategy-research/pull/553 — previously reviewed same spot 1h MARKET-close model.
- https://github.com/HCH725/alpha-strategy-research/pull/570 — previously reviewed same spot 1h MARKET-close model.
