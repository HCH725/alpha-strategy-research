---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "szymonsobkowiak AI Volume Strategy — volume-EMA20 impulse, price-EMA50 and bullish candle, five-bar timed exit; independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-12
sources:
  - https://www.tradingview.com/script/hQ00TVw5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume EMA20 impulse / EMA50 bullish-bar five-bar hold — independent derivative

## Provenance and immutable identity

- **Primary source:** TradingView public open-source *AI Volume Strategy*, author **szymonsobkowiak**, published **2025-04-12**, stable TradingView script ID **hQ00TVw5**, source description inspected **2026-10-29**: https://www.tradingview.com/script/hQ00TVw5/ . This is a first-party public TradingView **strategy** page. No complete Pine source bytes, Pine version, revision hash or independently reproduced TradingView trades were retrievable from the accessible page; this record does not claim a source-native/lossless port.
- **Source facts actually verified:** the author describes an EMA of volume to detect abnormal volume spikes against a user-defined multiplier; a **50-period price EMA** trend filter; a **bullish/green candle** for buy and a **bearish/red candle** for sell; and an **exit after X bars, default five**. The description does **not** specify the volume EMA length, default multiplier, indicator seeding, exact order timing, cash, fee, position sizing, or what happens if an opposite signal appears before the five-bar timeout.
- **Independent researcher-defined executable derivative (NOT source-native):** choose EMA20(volume), strict volume > **2.0×** current volume EMA, EMA50(close), long-only spot BTC-USDT 1h, bullish-bar/above-EMA entry, **time exit only** after five fully completed post-fill bars, next-completed-bar-close historical MARKET fills, 0.001 BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 120-bar warmup and explicit fail-closed state. The original bearish SELL signal is **disabled as an early exit or short entry**; the source's exact unknown volume parameters, original Pine execution timing and any other native risk defaults are **not** attributed to this derivative. These researcher choices change trade events and economics.
- **Frozen identity:** `TV:hQ00TVw5|szymonsobkowiak|2025-04-12|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC1h|EMA20-volume-SMA-seed|V>2xVEMA|EMA50-close-SMA-seed|C>O-and-C>EMA50|long-flat|five-full-postfill-bars-time-exit|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup120`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

**Source-reported:** unusual current-bar volume relative to a volume EMA, direction of the candle and price relative to a 50-bar EMA combine to identify directional participation. The original page suggests a five-bar default holding horizon. It provides no verified result for this exact derivative.

**Research hypothesis only:** a strong bullish volume impulse above the medium-term trend may persist for several bars. The fixed holding horizon limits exposure duration but is **not a protective stop**; adverse price gaps can cause large losses. No performance, profitability, Qlib parity or historical Survivor claim.

## Signal — fully pinned independent rules (Gate 1, 2, 3, 4)

- **Market and clock:** one continuous, UTC-aligned Binance **BTC-USDT spot 1h** OHLCV sequence. Bar index `t` has exchange **open** timestamp `T[t]`, and its complete O/H/L/C/V become decision-available only at `E[t]=T[t]+3600 seconds`. Only complete historical bars are eligible; no future, partially formed or higher-timeframe candles.
- **Input validation:** strictly increasing, gap-free 3600-second UTC open timestamps; finite positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, finite `V>=0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.
- **Volume EMA20:** `VEMA20[19]=sum(V[0..19])/20`; for `t>=20`, `VEMA20[t]=(2/21)*V[t]+(19/21)*VEMA20[t-1]`. No value before index 19. This length and SMA seed are **researcher-selected**, not verified source defaults. Calculate with chronological float64 arithmetic from the first valid bar; no full-sample normalization.
- **Price EMA50:** `PEMA50[49]=sum(C[0..49])/50`; for `t>=50`, `PEMA50[t]=(2/51)*C[t]+(49/51)*PEMA50[t-1]`. No value before index 49. EMA50 length is source-reported; its close input and seed are researcher-pinned.
- **Entry predicate:** `volumeImpulse[t]=(VEMA20[t]>0 && V[t]>2.0*VEMA20[t])`; `bullBar[t]=(C[t]>O[t])`; `upTrend[t]=(C[t]>PEMA50[t])`. Strict `>` throughout: equality fails. `BUY_SIGNAL[t]=volumeImpulse[t] && bullBar[t] && upTrend[t]`. The 2.0 multiplier is a **researcher choice** because the source describes a user-defined multiplier without publishing its default. No bullish crossover or edge is required: it is a level condition, eligible only while FLAT and with no pending order.
- **Warmup:** first **120** valid fully completed 1h bars, indices 0–119, are indicator-only, FLAT, and never emit orders. First signal may occur at index 120, after both seeded EMAs are available. No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]`, if FLAT and BUY_SIGNAL is true, queue exactly one fixed `Q=Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f=t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)`. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A successful confirmed full fill sets LONG and `fill_index=f`. No additional signal is evaluated on the fill bar.
- **SELL state / five-bar timer:** LONG never evaluates fresh entry signals or opposite bearish signals. Count **five fully completed bars AFTER the BUY fill bar**, indices `f+1,...,f+5`. At `E[f+5]`, queue exactly one MARKET SELL for the next completed bar `s=f+6`; use its real `C[s]` as the idealized historical full-fill price at `E[s]`, sell all Q, and set FLAT. This explicitly defines the five-bar timer and the extra next-close execution delay; it is not a guarantee of exit after exactly five hours of exposure. No time exit is executed if the required future bar is absent; the pending order remains unfilled at sample end. No signal on the SELL fill bar; earliest re-entry decision is a **later** eligible bar.
- **State priority:** at most one pending action and one position; pending BUY/SELL takes precedence over new signals, and a timed SELL is the only exit. The original bearish signal is intentionally ignored, including on a LONG bar. If FLAT and no pending order, only BUY_SIGNAL may act. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital cross-asset concurrency, SL, TP, trailing, profit-triggered exit, session filter, intrabar stop/limit/maker or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetic liquidated.

## Required data and causal timing (Gate 6)

Only actual Binance BTC-USDT spot UTC 1h O/H/L/C/V. Price EMA, volume EMA, candle color and signal use bar t's **completed** inputs at E[t]. The queued order's fill at E[t+1] is not used retroactively in signal selection. The timer starts at the **confirmed full-fill** index, not the signal bar; the five subsequent completed bars must all exist. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Missing/invalid bars abort rather than silently continuing an inconsistent position ledger.

## Execution assumptions and pinned-engine evidence (Gate 5)

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION=dev-2.17.0`, bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. Inspected the immutable source directly via connected GitHub app on 2026-10-29. The repository `setup.py` distribution-version text and the package label are not assumed equivalent; this cycle **did not re-download or hash the wheel**. Prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`; the independent Auditor must confirm this evidence applies to the pinned package and path.
- **Actual feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists interval `1h`; `binance_spot_candles.py::_parse_rest_candles` maps REST `row[0]` to the **open** timestamp and `row[1..5]` to OHLCV. `backtesting_data_provider.py` loads historical candles. This derivative explicitly shifts completed-bar **decision availability** to `E[t]` instead of mistaking row open time for the time its close/volume became known.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of an already deployed controller or exchange-accepted order.
- **Actual fill path:** `OrderExecutorSimulator.simulate` for MARKET chooses the **first supplied row** and uses its real `close` as `entry_price`; sets `filled_amount_quote=float(amount)*close` and `cum_fees_quote=trade_cost*filled_amount_quote`; returns `CloseType.POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model must report the **effective historical fill event** as `E[fill_row]`, not claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange order acceptance.
- **Cash, inventory and fee model:** hypothetical `fee=Decimal("0.001")` per BUY and SELL side, `trade_cost=0.001` on each simulated executor. Initial USDT=10,000, BTC=0. On confirmed full BUY at P, debit `Q*P*(1+fee)` and credit Q BTC; on confirmed full SELL at P, debit Q BTC and credit `Q*P*(1-fee)` USDT. Realized net PnL for a completed round trip is `Q*(P_sell-P_buy)-fee*Q*(P_buy+P_sell)`. Track independent Decimal cash/BTC ledger from confirmed full fills, reconcile simulator quote/fee events, and distinguish gross simulator `net_pnl_quote` from fee-inclusive portfolio economics. Never infer a position solely from delayed `positions_held` or float-derived dust; reject mismatched fill amount, contradictory side, stale order or material ledger residual instead of pretending a fill occurred.
- **Missing price and economic limitations:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` when price is absent; **never** use this fallback for fills or marking. Require actual positive observed candle close. No **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** This uses only the already reviewed single-pair Binance spot 1h OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550**. The new strategy changes only controller-side EMA/volume/candle predicates and a deterministic five-bar timer, not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Six-gate summary for independent Auditor

1. **G1 deterministic:** pinned EMA20(volume), EMA50(close), seeds, strict thresholds, bullish candle, fixed volume multiplier and timer.
2. **G2 direction:** BTC-USDT unleveraged spot LONG/FLAT; shorts explicitly disabled.
3. **G3 entries/exits/risk:** complete volume/trend/candle entry, five-post-fill-bar timed exit, no hidden stop/target/trailing or opposite-signal exit.
4. **G4 position:** Q=0.001 BTC, cash=10,000 USDT, single pending action/position, no DCA/pyramiding/cooldown, explicit re-entry and last-bar handling.
5. **G5 pinned engine:** exact pinned Binance spot 1h feed, MARKET close simulator, controller/action path, effective-time normalization, fee/cash ledger and unsupported economic assumptions identified. Package/source provenance relies on prior reviewed wheel correspondence, not a new wheel hash.
6. **G6 causality:** 120 completed-bar warmup; signal at E[t], queued fill at E[t+1], timer from confirmed fill, no future leakage, no fabricated gap/price.

## Evidence, dedup and falsification

**Source-reported:** szymonsobkowiak's TradingView public description dated 2025-04-12 supports volume EMA spike, price EMA50 trend, candle-color confirmation and five-bar default time exit. It does **not** publish the volume EMA length/multiplier, exact seeds, original Pine bytes, or this derivative's spot timing/cost/position semantics. These are all explicitly researcher-defined above. The word “AI” in the title is not evidence of a trained model; this derivative contains **no ML**.

**Independently reproduced:** **none** for this candidate's TradingView trades, Hummingbot/Qlib events, performance, OOS or realized fees. Only first-party prose and immutable pinned-engine source paths were inspected; prior PR engine proof is referenced with limitations.

**Dedup 2026-10-29:** pre-write `main@8442b11376a5f28e86c8e153d681c44cc31bbf04` has **442** root-level strategy records and README counter **442** (full non-truncated tree, excluding two READMEs). GitHub code search for exact script ID `hQ00TVw5` and author `szymonsobkowiak` returned no current-main record; GitHub PR search for both returned no existing PR. Eleven open `research/*` PRs were inspected by source/title/body; none use this source or the same volume-EMA20 + EMA50 + bullish-bar + five-post-fill-bar time-exit rules. Existing `tradingview-ai-volume-quadruple-atr-cooldown-...` uses **different author/script Fk7JtbC9**, fourfold **previous-bar** volume ratio, SMA20/ATR and signal cooldown. Existing `tradingview-smart-day-trader-macd-sma9-volume-ema20-spike5-...` uses **different script kFSPpZbG**, MACD/SMA9 crossover and five-bar **volume-memory**, not a bullish candle/EMA50 gate with five-bar **holding timer**. Thus this is not a parameter-only clone. Six sampled existing frontmatter statuses were attempted (five PASS; one mistyped/nonexistent sample path), **not** a complete 442-record status audit.

**Falsification plan (future authorized research only):** EMA seed/equality tests, volume EMA zero case, green candle equality, missing candle abort, warmup 119/120, signal t versus fill f, five post-fill bars f+1..f+5 and sell fill f+6, signal on buy/sell fill bar suppression, insufficient cash, last-bar pending, full-fill fee ledger and float/Decimal reconciliation. No backtest, trading, deployment or cron change here.

## Implementation and adoption boundary

`implementation_status: not-implemented`, `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. Auditor alone may source-fact remediate exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Sources

- https://www.tradingview.com/script/hQ00TVw5/ — szymonsobkowiak, *AI Volume Strategy*, public open-source TradingView strategy, 2025-04-12.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected through connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
