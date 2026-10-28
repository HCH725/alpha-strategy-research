---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "kingshukghosh71 long-leg doji anchored close breakout with SMA20 exit — independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-06-13
sources:
  - https://www.tradingview.com/script/jQohKDR0-Long-Leg-Doji-Breakout-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Long-leg doji anchored breakout, SMA20 cross exit — independently derived BTC-USDT spot long-flat strategy

## Provenance

**First-party TradingView publication:** kingshukghosh71, *Long-Leg Doji Breakout Strategy*, published **2025-06-13**, public open-source strategy, stable script ID **jQohKDR0**, https://www.tradingview.com/script/jQohKDR0-Long-Leg-Doji-Breakout-Strategy/ ; public publication prose inspected 2026-10-28. Source explicitly describes: a small doji body at most 0.1% of total candle range, upper and lower wicks each at least 2x body; an ATR-based pattern-significance filter; wait after the doji and enter long on a later close above its high or short on a close below its low; close a position when price crosses back through a 20-period simple moving average; and source 10%-of-equity sizing. **The full executable Pine source, ATR lookback/threshold, order-processing flags, precise pending-anchor replacement, stops, pyramiding, and fees were not available in the accessible first-party page.** Do not attribute any researcher choices below to the author or claim a lossless Pine reproduction.

**Explicit independent derivative (NOT source-native):** preserve the first-party doji geometry, the *subsequent* doji-high close breakout and SMA20 trend-cross exit concepts. Researcher choices: Binance BTC-USDT unleveraged spot **UTC 1d**, LONG/FLAT only (source short disabled); use body/range <=0.001 with exact OHLC geometry and positive two-sided wicks; **omit the source ATR significance filter** rather than invent its unknown parameters; keep only the latest eligible doji anchor, invalidate it on a close below its low, and ignore setups while already long; define exact SMA20 cross-under, no additional stops/targets; fixed 0.001 BTC instead of source 10% equity; initial 10,000 USDT, 0.1% modeled fee per filled side, 80-bar warmup, full-fill close-price MARKET research simulation and deterministic failed-fill/data policies. Omission of ATR changes signals materially and is openly part of this **separate strategy**, not an assertion that the original source passed HB_READY.

**Immutable strategy identity:** `TV:jQohKDR0:kingshukghosh71:2025-06-13 | independent-derived-v1:2026-10-28 | BTC-USDT-Binance-spot-UTC1d | body/range<=0.001,each-wick>=2body-and-positive,no-ATR | latest-doji-high-close-break,below-low-cancel | SMA20-close-crossunder-exit | LONG/FLAT-Q0.001-no-DCA | completed-close-MARKET | fee0.001/side | warmup80`. Any change in geometry, anchor state, exit, market, sizing, timing or costs is a different derivative.

**Dedup on GitHub connector snapshot:** `main@12308a0ec60bb318a332c3577e620ce87cf75e48`, untruncated 404 root-level strategy records and README static count 404. Main code search for `jQohKDR0`, `kingshukghosh71`, `long-leg doji` and `armed_high` found no strategy carrying this source or the same anchored breakout. The only `jQohKDR0` hit was a **dedup note** in an unrelated FMZ record, not a strategy record using this source. All ten open PRs were inspected by head/title/body and an open-PR search for `jQohKDR0` returned none. Closest mechanisms differ: `tradingview-masteraux101-fivebar-close-extreme-doji-veto-atr-bracket-long-btcusdt-1d-2026-10-26.md` uses a five-bar near-extreme count with a **doji veto**, not a doji anchor; `tradingview-chartart-nr7-inside-day-sma20-bullish-exit-long-btcusdt-1d-2026-10-25.md` uses narrow-range inside-day confirmation, not long-leg doji geometry and a retained high anchor. No trivial parameter-only duplicate. Count agreement is not a 404-file frontmatter audit.

## Economic mechanism

### Source-reported
A narrow-body, two-long-wick candle represents indecision. A subsequent close beyond its high/low represents a directional resolution; a 20-period SMA cross is used as a trend-based exit. The original ATR filter and short path are not represented as source-native executable logic here.

### Research interpretation
This derivative buys only a **completed-close upward break** of the most recent qualifying doji's high. A completed close below its low cancels the setup without opening a short. The 20-day SMA cross-under exits an existing long. No profitability, drawdown, win-rate or source-backtest equivalence is asserted.

## Signal

One contiguous sequence of **completed** Binance BTC-USDT Spot UTC daily OHLC candles `(O[t],H[t],L[t],C[t])`, indexed from `t=0`; all prices finite and >0, `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]`. No synthetic, missing, duplicated or out-of-order days.

1. `range[t]=H[t]-L[t]`; `body[t]=abs(C[t]-O[t])`; `upperWick[t]=H[t]-max(O[t],C[t])`; `lowerWick[t]=min(O[t],C[t])-L[t]`. A qualifying **derived doji** requires `range>0`, `body/range<=0.001`, `upperWick>0`, `lowerWick>0`, `upperWick>=2*body` and `lowerWick>=2*body`. Equality at 0.001 or 2x qualifies. A zero-body candle still requires positive wicks; a zero-range candle is not a setup. This explicit body/range interpretation and the positive-wick condition are researcher-defined operationalizations of the published geometry.
2. `SMA20[t]=sum(C[t-19..t])/20`, computed only on 20 consecutive completed finite closes. No ATR calculation or ATR gate exists in this derivative; that is an intentional, material divergence from the author's strategy.
3. During the first **80** complete daily candles (`t=0..79`) do not arm or trade; earliest eligible doji anchor is `t=80`, earliest breakout entry is `t=81`. No warmup setup is carried into live research decisions.
4. States are `FLAT_UNARMED`, `FLAT_ARMED(anchorHigh,anchorLow,anchorBar)`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initially `FLAT_UNARMED`. On each valid completed `t>=80` bar while FLAT and no order pending:
   - If already ARMED from a **strictly earlier** bar and `C[t]>anchorHigh`, emit one BUY at this completed bar, clear anchor on confirmed fill; this breakout has priority over identifying a new doji on the same bar.
   - Else if ARMED and `C[t]<anchorLow`, **cancel** the anchor, emit no order and do not rearm on that same bar; the source's bearish breakout/short is disabled.
   - Else if the current bar qualifies as a doji, set/replace the anchor to `(H[t],L[t],t)` without trading. If no new doji, retain the existing anchor indefinitely until breakout, cancellation or data abort. Equality at the anchor high/low is not a breakout/cancellation.
5. While LONG, **ignore all new doji anchors**. Exit on the first later completed bar satisfying `C[t-1]>=SMA20[t-1] AND C[t]<SMA20[t]`. This is a **strict close/SMA20 cross-under**; a touch at the current SMA is not an exit. The derivative does not use the source short entry, a cross-up short exit, or a mere below-SMA level as an exit. If no cross occurs, the long may persist without a protective stop.
6. On a confirmed SELL fill return to `FLAT_UNARMED`; earliest new doji arm is the next completed bar, and earliest next BUY is a still-later bar. Only one action per bar, with LONG exit before any possible FLAT setup; no same-bar entry/exit/re-entry. Pending orders suppress all signals. An absent, rejected, expired, partial, mismatched or unconfirmed fill **aborts the research run** without fabricating inventory or a completed trade. Do not silently convert an order submission into a fill.
7. **Explicitly disabled:** short/borrow, reversal into short, DCA/safety orders, pyramiding, multiple pairs, simultaneous positions, cooldown beyond the above state machine, stop-loss, take-profit, trailing/breakeven stops, time exit, funding, leverage/margin and forced final-bar liquidation. An open end-of-sample long is marked to the last **real** observed close and not assigned an imaginary SELL.

## Required data

Exactly one Binance Spot BTC-USDT `1d` candle feed; completed UTC daily O/H/L/C and exchange candle-open timestamp. The feed includes volume but volume is not a decision input. No order book, tick tape, multi-asset synchronization, lower/secondary timeframe, trained model, future extremum, synthetic price, index/mark price, perpetual funding or external feed. Validate continuous UTC daily spacing and OHLC geometry **before** the pinned engine's `dropna`; invalid/missing bars or prices fail closed and abort the research sample rather than filling gaps, carrying stale anchors through a gap or pretending an order filled.

## Execution assumptions

**Pinned engine:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Its historical `setup.py` version string is `20260729`, **not** the distribution pin. Previously reviewed Alpha PR #414 records a package-20260920 wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148` and 902/902 shipped Python-file byte match to this source commit; this Scout inspected the existing evidence and the immutable source paths below, **but did not rehash the wheel**. Auditor must reject Gate 5 if that mapping is invalid.

**Data/clock path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1d`; `binance_spot_candles.py` parses Binance REST row[0] as the **candle-open** timestamp and row[1..4] as O/H/L/C. An input completed candle `t` is available for this research only at `effective_ts[t]=open_ts[t]+86400s`. Normalize the controller decision row and historical fill row to this effective completed-close timestamp; do **not** read the completed close at the raw open timestamp. No incomplete daily candle is eligible.

**Controller/executor/fill path:** a strategy-specific, **not yet implemented**, ControllerV2 state machine would emit `CreateExecutorAction(OrderExecutorConfig(...))` with `ExecutionStrategy.MARKET`, connector `binance`, pair `BTC-USDT`, BUY or SELL, `Decimal("0.001")` base amount, leverage 1. The pinned `strategy_v2/backtesting/backtesting_engine_base.py` processes each prepared candle via `update_state` and `determine_executor_actions`, and `executors_simulator/order_executor_simulator.py` fills MARKET on the first actual supplied row's **close**, calculates filled quote notional `amount*close`, and terminates as `CloseType.POSITION_HOLD`. `BacktestPositionHold` nets BUY/SELL exposure and tracks realized **gross** PnL separately from `cum_fees_quote`. Set `terminated_executors_window=None` or maintain a complete fill-confirmed state ledger; the default 1-hour terminated-executor view is too short for daily decisions. Reconcile fill/inventory state after final engine flush. Never accept the data provider's `get_price_by_type` missing-price `Decimal("1")` fallback.

**Research economic model:** initial **10,000 USDT** unborrowed spot cash, fixed `Q=0.001 BTC`, single pair and one pending order; research fee `f=0.001` (0.1% **per filled side** of actual quote notional). BUY requires `cash>=Q*P*(1+f)`, then cash decreases by `Q*P*(1+f)`; SELL requires confirmed inventory `>=Q`, then cash increases by `Q*P*(1-f)`. Matched net realized USDT `=Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell)`; open inventory is marked separately, and gross `total_pnl` must not be labeled fee-net. Price and fee are drawn only from real valid candle closes; no fabricated or zero-priced fills. The pinned MARKET-close simulator assumes **zero additional modeled slippage**, not observed zero exchange spread/latency/slippage. The simulator's float quote arithmetic must be reconciled against the Decimal cash ledger; any material fill/fee/position mismatch aborts. Spot-only has no perpetual funding contract; do not present futures funding as zero. Exchange-specific fee tier, precision, lot/tick/min-notional checks, partial fills and live-market timing are **not verified or claimed**. The same-effective-close MARKET fill is an idealized historical model, **not** a live achievable after-close fill or original TradingView broker-emulator equivalence.

## Evidence

### Source-reported
The dated first-party TradingView page supplies long-leg doji body/wick concept, high/low anchored close-break entries, ATR significance filter, 20-SMA-cross exit and 10%-equity source sizing. It does **not** supply full accessible Pine bytes or complete ATR/position/order semantics. No source performance metrics are imported.

### Independently reproduced
**No candidate Pine, Hummingbot or Qlib backtest, PnL, fills, OOS, Survivor status or event-level parity was run or reproduced.** The existing pinned engine primitives and historical wheel binding were read as **capability evidence**, not as this candidate's performance or execution proof.

### Negative evidence
Source-native exact reproduction is **not claimable** because ATR gate parameters and Pine execution settings are missing. This separate derivative deliberately omits ATR, disables short and changes sizing, market, fill timing, risk and anchor state. The absence of protective stops permits unlimited holding time and potentially severe losses. Count agreement on main is not proof that every historical frontmatter was independently re-audited in this cycle.

## Six-gate assessment — proposal for independent Hermes Auditor

1. **Determinism:** exact OHLC doji geometry, SMA20 formula, strict boundary tests, anchor replacement/invalidation, bar priority and 80-bar warmup; no model training or hidden parameters.
2. **Direction:** one Binance BTC-USDT spot long or flat; all short-side behaviors explicitly disabled as researcher-derived.
3. **Entries/exits/risk:** anchored completed-close high break BUY, completed-close SMA20 cross-under SELL; ATR source filter omitted openly; no implicit stops/TP/trailing/time exits.
4. **Position:** fixed 0.001 BTC, unborrowed cash, one pending/full-fill position, no DCA/pyramiding/concurrency, defined failed-fill abort and re-entry rules.
5. **Pinned model:** actual 1d Binance spot data parser, completed-close timestamp normalization, ControllerV2 MARKET OrderExecutor and POSITION_HOLD gross/fee accounting, cash/precision constraints and missing-price rejection; prior PR #414 wheel/source binding is cited, not rehashed here. No unsupported intrabar, next-open, margin, funding or shared-capital requirement.
6. **Causality:** anchor must precede breakout, t-1/t completed SMA only, 80 complete bars, effective close availability, no future labels, repainting, incomplete candles or invented missing data.

**PASS frontmatter is a Scout research-admission proposal, not an independent audit verdict.** HB_READY is neither profitability nor Qlib parity nor Paper/Testnet/Live authorization. A new unverified execution primitive would require representative Qlib/Hummingbot event-level validation before mass screening; do not confuse a record with an implemented controller.

## Falsification plan

Future authorized tests (not performed here): body/range and wick boundary ties; zero-body/zero-range cases; next-bar-only breakout; latest-doji replacement; bearish-low cancellation; simultaneous new doji and prior-anchor breakout; long held below SMA without a fresh cross; first bar after warmup; gaps, missing prices, rejected fills and fee-net reconciliation. Compare this independent no-ATR derivative to a separately specified ATR-gated version **only if** an ATR formula/threshold is explicitly pinned; never call that comparison source-native by default.

## Crypto portability

The source mentions index options; this derivative is **BTC-USDT Binance spot UTC1d only**. Other markets, timeframes, shorts, DCA 6/6/6 or leveraged futures would change the executable model and require an explicitly reviewed derivative and applicable engine evidence; none is an admission prerequisite for this record.

## Limitations

Full Pine source and source ATR defaults unavailable; original event timing, trade count and profitability are not reproduced. No candidate-specific simulator run, controller implementation, wheel-byte rehash, exchange live fill or Qlib parity. A close-price historical MARKET fill is optimistic compared with orders placed after the candle closes; an unprotected long may remain exposed indefinitely.

## Implementation status

not-implemented; no code, container, backtest, Qlib/Hummingbot, n8n, deployment, cron or trading changes. Subsequent engineering materialization follows the existing `IMPLEMENTATION_NEEDED` path only if this independently audited strategy is later selected.

## Adoption boundary

Research-only; adoption not approved; approval scope research-only. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head six-gate PASS merge or NOT_LOSSLESS close. Scout never approves, merges or edits main/README.

## Related Wiki records

None asserted.

## Sources

- kingshukghosh71, *Long-Leg Doji Breakout Strategy*, TradingView, published 2025-06-13: https://www.tradingview.com/script/jQohKDR0-Long-Leg-Doji-Breakout-Strategy/
- HCH725/hummingbot pinned source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `executors_simulator/order_executor_simulator.py`, `hummingbot/data_feed/candles_feed/binance_spot_candles/{constants.py,binance_spot_candles.py}`.
- HCH725/alpha-strategy-research PR #414, prior wheel/source pin evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
