---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Botnet101 three-lower-closes entry and prior-bar-high recovery exit, independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/vrQolvsm-Consecutive-Bearish-Candle-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Botnet101 three lower closes / prior-high recovery exit (independent BTC-USDT spot 1h derivative)

## Provenance

- **Primary source:** Botnet101, *Consecutive Bearish Candle Strategy*, TradingView public open-source **strategy**, published **2025-01-22**, stable script ID **vrQolvsm**: https://www.tradingview.com/script/vrQolvsm-Consecutive-Bearish-Candle-Strategy/ . Direct first-party public page inspected **2026-10-30**. No separately dated code revision was established; the embedded Pine bytes were not obtained. Source facts below are supported by the author's publicly accessible description, **not** a claim of byte-exact Pine replication.
- **Source-native, verified from author's description:** buy after at least `Lookback` consecutive closes strictly lower than the preceding close (default `Lookback=3`); entry is constrained by user-configurable Start/End Time; sell when the completed close is strictly above the preceding candle's **high** (`close > high[1]`). This is a **long** reversal strategy. The page does not expose enough code to establish native order clock, commission, quantity, date defaults, stop/target, or all Pine state details.
- **Immutable independent derivative identity:** `TV:vrQolvsm|Botnet101|published-2025-01-22|derived-close-v1-20261030|BinanceSpot:BTC-USDT:UTC1h|downCount(C[t]<C[t-1])>=3|exit:C[t]>H[t-1]|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup20`. Changes to any predicate, session, market, fill clock, amount or cost constitute a different derivative.
- **Researcher-defined choices, not source-native claims:** Binance BTC-USDT **spot** on UTC 1h (source is market/timeframe-agnostic); continuous 24/7, **time-window filter disabled** (source's time-window inputs not replicated); one fixed `0.001 BTC` LONG or FLAT; full-bar-close decisions, **next completed candle close** historical MARKET fills (not a claim of the source's Pine fill convention); `10000 USDT` initial cash, hypothetical 0.1% fee each side, no additional modeled slippage, 20 completed-bar warmup, no protective SL/TP/trailing/time exit/DCA; full position/pending state and failure policy below. This is a separately specified executable research model, **not** a source-native repair or a lossless translation.

**Dedup at main `5ea39e93c0901800aae89b2884890f815e8862fa`:** GitHub connector full tree untruncated: 455 root strategy Markdown records, README static count 455; eleven distributed main frontmatter samples `PASS`, not a full 455-file audit. GitHub main search for exact `vrQolvsm` and source title found no same source; checked 11 open `research/*` PR summaries plus exact-source/title PR search (no collision). Closest `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` buys after 3 lower closes but **requires 3 higher closes to exit**, whereas this candidate exits on a **single completed close exceeding the previous bar's high**; the different exit event predicate and holding-period distribution are material, not a parameter variant. The existing Botnet101 `tradingview-botnet101-bearish-wick-prior7high-exit-long-btcusdt-1d-2026-10-26.md` instead buys a -1% lower wick and exits above the **highest of seven prior highs**, not this three-close/one-prior-high mechanism.

## Economic mechanism

### Source-reported

Three consecutive declining closes are treated as a possible short-horizon oversold sequence. A subsequent close above the previous bar's high signals recovery and liquidates the long. This is an economic hypothesis, not a verified positive expectancy, profit or survivor result.

### Research interpretation

This derived system purchases a three-bar close-to-close selloff, then waits for a **one-bar prior-high close breakout** to exit. It is intentionally different from a symmetrical three-down/three-up counter strategy. A persistent downtrend can create severe drawdown or an indefinite holding period because there is no protective stop.

## Signal

**Data and time:** one real, contiguous Binance BTC-USDT spot UTC **1h** OHLCV sequence. For bar index `t`, `T[t]` is the exchange candle's **open** timestamp, and its completed OHLCV becomes decision-available at `E[t]=T[t]+3600 seconds`. Only completed bars can contribute. Strict finite/positive OHLC validation and gap policy below.

**Exact indicators and comparisons (no hidden smoothing):**

- Initialize `downCount[0]=0`; for each `t>=1`, `downCount[t]=(C[t]<C[t-1]) ? downCount[t-1]+1 : 0`. Equality **resets to zero**. The count is computed on every validated completed bar even if the position is LONG or an order is pending; it does not cap at 3.
- `entry[t] = (downCount[t] >= 3)`. It is a **level**, not a crossover. `C[t]` and `C[t-1]` are completed closes, and the preceding three strict declines must be consecutive.
- `exit[t] = (C[t] > H[t-1])`. Only the immediately previous **completed** bar high qualifies. Equality does **not** exit; current-bar high alone is not a signal. There is no `highest(7)` or 3-up-close requirement.
- If LONG and `exit[t]`, queue exactly one full SELL. If FLAT and `entry[t]`, queue exactly one BUY. If both predicates happen to be true, the **position state** chooses the only permitted action (SELL when LONG; BUY when FLAT); no same-bar reversal. Entry is ignored while LONG and exit ignored while FLAT.
- **No other exits:** no protective stop, separate take profit, trailing, time limit, end-of-sample liquidation, opposite short, position scaling, DCA, ROI ladder, cooldown or session filter. They are **explicitly disabled** in this derivative, not attributed to source defaults.

**Warmup:** indices `0..19` (20 completed contiguous candles) are nontrading; first decision `t=20`. The 3-down counter requires only 4 candles and prior-high exit requires 2; the 20-bar warmup is an independently declared conservative fixed choice. All inputs are available at or before `E[t]`; no repaint, centered window, negative shift, future extrema, higher timeframe, or full-sample fit.

**Position / pending state:**

1. Start `FLAT`, `cash=Decimal("10000")` USDT, `inventory=Decimal("0")` BTC; at most one pending MARKET action or one LONG of exactly `Q=Decimal("0.001")` BTC. No borrowing, leverage, margin, shorting, pyramiding, partial fills or simultaneous orders.
2. At decision `E[t]`, queue a BUY/SELL for bar `f=t+1`. At `E[f]`, the idealized historical simulator fills **exactly Q** at the **actual observed** `C[f]` (not a fabricated price or `C[t]`). No `f` means no fill; a pending SELL leaves the existing inventory open and marked to the last valid close.
3. A BUY fills only if `cash >= Q*C[f]*(1+fee)`. If insufficient, **consume** that action without a fill, remain FLAT, and do not partially fill or defer it. SELL fills the existing Q; reject a mismatched inventory. On the fill candle `f`, **suppress signal decisions**; earliest next decision is `f+1`. After a SELL, re-entry requires a fresh eligible `downCount>=3` on a later decision bar. No cooldown beyond the fill-bar exclusion.
4. `fee=Decimal("0.001")` per side of executed quote notional. BUY: `cash-=Q*P*(1+fee); inventory+=Q`. SELL: `cash+=Q*P*(1-fee); inventory-=Q`. Marked equity on a valid completed bar is `cash+inventory*C[t]`. Use `Decimal(str(actual_close))`, never `Decimal(float)`. Round-trip net PnL = `Q*(P_sell-P_buy)-fee*Q*(P_buy+P_sell)`. Do not infer position truth from native float dust, terminated executor history or gross-only PnL.
5. Reconcile simulator side, base amount, quote amount and quote fee with the exact ledger for each full fill; float reconciliation tolerance `max(1e-8, 1e-12*Q*P)` quote units. A mismatch aborts with `ENGINE_MISMATCH`, never silently fixes cash, position or fees.

## Required data

- Single Binance spot `BTC-USDT` real 1h O/H/L/C (volume is supplied but not a decision predicate); strictly UTC-aligned candle **open** timestamps 3600 seconds apart. Check all O/H/L/C are finite positive, `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, finite nonnegative volume, no duplicates, no gaps and no incomplete candles.
- On any missing, invalid, unsorted or discontinuous bar **abort this research replay**; no interpolation, forward-fill, synthetic quote, default `Decimal("1")` price, fabricated execution or silently skipped trading event. Pending orders are not filled from missing data.
- No funding, mark/index price, lower/MTF candles, order book, trade tape, shared capital, sentiment, training set or external model. Binance spot has no perpetual funding or liquidation; do not describe unknown perpetual funding as zero.

## Execution assumptions

- **Pinned engine identity:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout independently re-read pinned GitHub source for `binance_spot_candles/constants.py` (`1h` and `/api/v3/klines`), `binance_spot_candles.py` (REST `row[0]` **open** time and OHLCV parsing), `backtesting_engine_base.py` (`update_state` then `determine_executor_actions` / `CreateExecutorAction`, `OrderExecutorConfig` routing and `POSITION_HOLD`), `order_executor_simulator.py` (MARKET fills at **first supplied row's actual close**, `amount_quote=float(amount)*close`, `cum_fees_quote=trade_cost*amount_quote`), `order_executor/data_types.py` (MARKET side, amount, `price=None`, leverage 1), and `backtesting_data_provider.py` (external trading-rule load and missing-price fallback). The engine's raw `timestamp` labels the candle open; the derivative's economic availability is `E[t]`, not the raw label.
- **Specific minimal controller route (future implementation only):** on each validated completed `t`, compute the two predicates, hold the pending action without inspecting `C[t+1]`; only when the next validated completed row `t+1` is processed, emit `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1))`. The pinned OrderExecutorSimulator consumes the **actual close** of that supplied row. No future price is consulted to choose the earlier signal. This is a **historical completed-close** convention, not a live ability to submit an order after a candle closes and fill at that past price.
- **Bounded, previously reviewed idealized research primitive:** reuse independently reviewed same pinned spot MARKET-close path in alpha PR #414, #550 and exact-head independent PASS review of #632. The simulator does **not** enforce historical exchange lot/tick/min-notional acceptance, liquidity, spread, latency, or partial fills; **none is an additional event-conditional branch of this deliberately idealized full-fill model**, and no real exchange order-validity claim is made. Provider may fetch external trading rules, but this derivative does not call `quantize_order_amount` or use unpinned rules to determine simulated fills. Realistic/live exchange acceptance requires separate verification and is **not** implied by this research PASS. Missing real prices and any engine/ledger mismatch abort.
- **Research economics:** `trade_cost=0.001` each side is a declared hypothetical fee, not a verified Binance tier. No **additional modeled** slippage is applied; this is not an assertion of zero actual slippage. Spot has no perpetual funding. Compute net marked equity from exact Decimal ledger; do not use native gross-only summary as net performance. No wheel hash, deployed image, full engine replay, Qlib parity, Testnet or Live claim is made here.
- **Gate 5 scope:** the pinned engine's source path, actual candle parsing, row dispatch, MARKET close-fill, quote fee and position hold were examined, rather than inferred from API names. Dedicated strategy controller is `not-implemented` and needs separate engineering only when selected downstream; it is not a second HB_READY admission flag. Representative Hummingbot↔Qlib event-level parity is required before large-scale Qlib screening of any new strategy/execution path.

## Evidence

### Source-reported

TradingView primary page by Botnet101 (2025-01-22) explicitly supplies three consecutive lower closes (default lookback 3) as long entry, a time-window input, and `close>high[1]` as the long exit. Source-reported performance statements were not independently reproduced.

### Independently reproduced

No source Pine bytes, original TradingView strategy fills, actual Binance fills, Qlib/Hummingbot parity, backtest statistics, OOS or profitability were independently reproduced. Only pinned engine source semantics and repository dedup/policy evidence were inspected.

### Negative evidence

The original Pine version and native trade execution/cost defaults were not available from the first-party prose. The derivative **discloses**, rather than silently guesses, its 24/7 session choice, spot market, completed-close clock, sizing, costs, warmup and risk/state policy. Its stopless entry can remain underwater indefinitely. Prior PR #629/#630 were rejected for treating unfixed real exchange acceptance as an event-critical condition; this record instead uses the explicitly bounded, idealized full-fill simulator path independently accepted for #632, and does not claim real order acceptance. Independent Auditor must still reject `NOT_LOSSLESS` if any six-gate fact or pinned model is not supported.

## Falsification plan

Later, only if separately authorized: synthetic tests for the first 20 warmup candles, exactly three lower closes, equality reset, a fourth/fifth lower close level signal, `C[t]==H[t-1]` no exit, `C[t]>H[t-1]` exit, exit-vs-entry state, next-row actual close, fill-bar exclusion, failed cash check, last-bar pending, gaps/invalid data abort, and exact Decimal fee/position reconciliation. Validate exchange acceptance as a **separate realistic model** if that scope is ever required. No research backtest or trading in this Scout.

## Crypto portability

This derivative is pinned only to Binance BTC-USDT **spot**, UTC 1h, LONG/FLAT. Porting to other assets, timeframes, sessions, futures, leverage or DCA alters event/cost assumptions and requires an explicit new research identity plus actual engine compatibility evidence. BO/SO 6/6/6 and 3×/5× are downstream optional campaign settings, not admission requirements.

## Implementation status

`implementation_status: not-implemented`. The six-gate `PASS` here is a **Scout proposal pending independent Hermes Auditor**, not proof of an existing strategy controller, source-native parity, profitability, Survivor, HB Certified, Qlib parity or execution authorization.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. No Qlib/Hummingbot runs, trading, Paper/Testnet/Live, main/README modification, container, n8n, cron or workflow edits. Independent Hermes Auditor owns exact-head PASS merge or NOT_LOSSLESS close; the existing signed GitHub webhook receiver alone owns post-merge README count reconciliation.

## Sources

- https://www.tradingview.com/script/vrQolvsm-Consecutive-Bearish-Candle-Strategy/ — Botnet101, *Consecutive Bearish Candle Strategy*, published 2025-01-22, first-party description inspected 2026-10-30.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned source; specific paths listed under Execution assumptions.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — reviewed engine primitive lineage.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — reviewed spot MARKET-close/ledger lineage.
- https://github.com/HCH725/alpha-strategy-research/pull/632 — independent exact-head PASS of same bounded idealized spot primitive.
