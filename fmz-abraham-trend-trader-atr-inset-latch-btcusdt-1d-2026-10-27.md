---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Andrew Abraham Trend Trader ATR-inset dual-latch — independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-27
sources:
  - https://www.fmz.com/strategy/438053
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Andrew Abraham Trend Trader ATR-inset dual-latch — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**First-party FMZ identity:** [Andrew-Abraham趋势追踪策略](https://www.fmz.com/strategy/438053), author **ChaoZhang**, directly inspected **2026-10-27**. The page mirrors the HPotter TradingView script **"Trend Trader Strategy"** (copyright header `HPotter v1.0 12/01/2017`), which implements the indicator from Andrew Abraham's article **"Trading the Trend"**, *Technical Analysis of Stocks & Commodities*, September 1998. The full Pine v2 source (strategy block, Length/Multiplier/reverse inputs, avgTR/highestC/lowestC/hiLimit/loLimit/ret/pos logic, both `strategy.entry` calls) is embedded on the page and was verified present by direct read. The page's backtest header declares `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT`; those are source context, not adopted.

**Immutable mirror pin:** `fmzquant/strategies@7853bb2bf262c4567ac238d3552d97f0e50cb801` (2025-04-30), file `Andrew-Abraham趋势追踪策略Andrew-Abraham-Trend-Tracking-Strategy.md` (6430 bytes, SHA-256 `bc46a7e7…`), byte-identical mechanism to the FMZ page. No newer commit is substituted.

**This is a fully specified, independently researcher-designed executable derivative v1, NOT the author's live configuration and NOT a lossless reconstruction.** The source is a two-sided futures script with a `reverse` input; every market, side, fill, sizing, warmup and cost rule below is a researcher-defined choice pinned in this record. `reverse` is pinned **false** (the source default); the `reverse=true` variant is explicitly excluded. No source-reported performance is imported.

**Immutable derived identity:** FMZ:438053 | HPotter Trend-Trader v1.0 | TASC-1998-Abraham | derivative:v1:2026-10-27 | BTC-USDT Binance spot UTC 1d | Length21 Multiplier3 reverse-false | WMA21-of-TR avgTR | HH21/LL21 inset rails | ret/pos dual latch | 0.01 BTC | close-price MARKET research model | 100-bar warmup.

**Dedup at main SHA 1eaaeb8:** main had 379 root-level strategy Markdown records and README counter 379. Filename/title/content search found no abraham/hpotter/trend-trader identity; all 10 open research/* PR titles and source descriptions were checked (Heracles, ClucMay72018, AdxSmas, Forven-CCI, Swift-2YMA, SSL, Chandelier, SuperTrend, Gauss-StochRSI, Larry-Williams — none is this mechanism). Nearest main relatives use different constructions: Eterna Chandelier 22/3.0 dual-stop state-flip and Forven Chandelier long-stop-cross ratchet a highest-high-since-entry stop, while Keltner records break EMA-centered bands; HPotter KAMA21 shares only the Pine author, not the indicator. This proposal's **WMA-smoothed raw true-range estimator, inset-from-rolling-extremes rails, and the dual-threshold ret/pos latch state machine** (a ret re-anchor requires the close to clear BOTH rails; pos can also flip across a retained ret without either dual-rail escape) is not a parameter variant of any of them.

## Economic mechanism

### Source-reported

A volatility-normalized channel inset from recent extremes: the rails sit 3 average-true-ranges inside the 21-bar highest high / lowest low, so only a close that escapes both rails re-anchors the reference level. The ret reference persists until another dual-rail escape, but pos is determined separately by close versus the current ret: crossing a retained ret can reverse pos without an opposite dual-rail escape; equality retains the previous pos. These are descriptive source facts, not verified original trades.

### Research interpretation

A new, testable hypothesis: after volatility-adaptive confirmation (a close beyond both inset rails), the side latch persists through ordinary pullbacks that do not cross the retained ret, potentially cutting whipsaw versus a plain band-breakout. Exit follows pos == -1, which can occur on a close below a retained ret without an opposite dual-rail escape. Profitability and whipsaw reduction are unknown.

## Signal

All rules below are **researcher-authored derivative v1**, fully pinned; t is a zero-based completed daily UTC candle index with finite positive O[t]/H[t]/L[t]/C[t] and H[t]>=L[t]. Evaluate once per completed candle. All arithmetic is chronological IEEE-754 float64; no whole-sample fitting, optimizers or future data.

1. **True range:** TR[t] = max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1])) for t>=1. ATR1[t] = TR[t] (Pine `atr(1)` equals raw true range).
2. **Smoothed range:** avgTR[t] = sum_{k=0..20} (21-k)*ATR1[t-k] / 231 for t>=21 (Pine `wma(...,21)`, weights 21..1, divisor 231).
3. **Extremes:** HH[t] = max_{k=0..20} H[t-k]; LL[t] = min_{k=0..20} L[t-k], for t>=20 (Pine `highest`/`lowest` include the current bar).
4. **Inset rails:** hiLimit[t] = HH[t-1] - 3*avgTR[t-1]; loLimit[t] = LL[t-1] + 3*avgTR[t-1], for t>=22 (all inputs prior-bar, causal).
5. **Reference latch:** ret[t] = 0 for t<22 (mirrors Pine `nz(ret[1],0)` seed). For t>=22: if C[t]>hiLimit[t] AND C[t]>loLimit[t] then hiLimit[t]; elif C[t]<loLimit[t] AND C[t]<hiLimit[t] then loLimit[t]; else ret[t-1]. Strict comparisons; equality holds the prior level.
6. **Side state:** pos[t] = 0 for t<22. For t>=22: if C[t]>ret[t] then +1; elif C[t]<ret[t] then -1; else pos[t-1]. Equality holds the prior side.
7. **Entry gate:** bars t=0..99 are exactly **100 completed-bar no-trade warmup** (covers the 22-bar definition lag plus latch settling), with all indicator/latch histories computed when defined. Start FLAT at t=100; a BUY at t>=100 requires FLAT, pos[t]==+1, pos[t-1]!=+1 (a fresh flip edge), sufficient modeled quote cash, and no pending order. A +1 side already latched at t=99 does **not** create a warmup-edge trade at t=100.
8. **Exit:** if LONG at eligible bar t and pos[t]==-1, SELL the entire actual filled quantity. No other exit. Entry (+1 edge) and exit (-1 state) are mutually exclusive on the same bar by construction, so no same-bar conflict can occur. On a SELL bar do not also BUY. If flat, an exit predicate is a no-op.
9. **State/re-entry:** update ret[t]/pos[t] on every completed bar, including when LONG, FLAT or pending. After exit, re-enter only on a **new** flip edge at a later bar, never merely because pos remains +1. No other cooldown. Rejected/skipped orders are not queued or retro-filled; a fresh later flip edge is required. Pending action prevents duplicate submissions and clears only when the simulator's fill/failure is reconciled.
10. **Trade direction and disabled behavior:** Binance BTC-USDT **spot LONG/FLAT** only; the source SHORT side, `reverse` mode, borrowing, futures, leverage, margin, pyramiding (Pine default pyramiding=0 already stacks nothing), scaling, DCA/safety orders, partial close, trailing, fixed stop, fixed take-profit, time stop, intrabar protective orders, discretionary overrides, and end-of-sample forced liquidation are **all disabled**. Thus adverse loss is not bounded by a stop. No multi-market exposure, portfolio synchronization or shared capital.

**Position/economics:** starting research cash 100000 USDT, BTC inventory 0. On a successful BUY acquire **0.01 BTC** at the model close; debit 0.01*C[t] plus 0.1% modeled quote fee. If cash is insufficient, skip the order without changing position. On a successful SELL reduce exactly the filled 0.01 BTC, credit 0.01*C[t] less 0.1% modeled quote fee; one net spot position maximum. Ledger records fill, entry price, gross realized PnL, separate buy/sell fees, net realized PnL, remaining quote cash, inventory and marked-to-last-observed-close unrealized PnL. No reinvestment or fractional sizing. These capital/fee values are research assumptions, not the author's or Binance's live terms.

## Required data

- Single Binance BTC-USDT spot UTC **1d** OHLCV feed, with only completed positive finite candles used for signal arithmetic. Volume is not an input. No multi-timeframe, funding, mark/index, order book, trade tape, news, fitted model, cross-symbol or other data dependencies.
- Binance REST kline timestamp is **open time** T[t]; O/H/L/C[t] and all signals derived from them become available no earlier than E[t]=T[t]+86400 seconds. Enforce unique strictly consecutive daily opens and the full closed-bar condition. An incomplete current candle is excluded; an absent, duplicated, zero/negative or non-finite O/H/L/C, H<L, missing interval, unavailable fill price or invalid timestamp **fails the segment closed**, rather than interpolation, forward-fill, synthetic prices or silent skipping.
- All computations use only the prefix ending at t, with explicit seeds, 100-bar warmup and no repainting, future extrema, negative shift or full-sample normalization. A new data segment must re-warm from FLAT, not stitch unseen latch state.

## Execution assumptions

**Pinned Hummingbot admission model:** package **20260920**, VERSION **dev-2.17.0**, inspected immutable source commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. This cycle read VERSION and each exact source path below directly at the pin. Package-to-source byte equivalence is inherited from prior independent pinned-baseline evidence, **not rehashed in this cycle**; no newer build is silently substituted.

- **Feed/data:** hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py explicitly maps 1d; binance_spot_candles.py _parse_rest_candles reads row[0] as open timestamp and row[4] as close. Prevalidate contiguity and completeness **before** BacktestingEngineBase.prepare_market_data() merges features using backward merge_asof and dropna; do not allow dropna to conceal a missing candle.
- **Controller path:** a future **strategy-specific**, not-yet-implemented controller supplies prefix-only TR/avgTR/rail/latch features and CreateExecutorAction events to BacktestingEngineBase.simulate_execution(), which updates state before determine_executor_actions(). No controller or Qlib implementation is claimed to exist today.
- **Executor/fills:** OrderExecutorConfig with connector_name=binance, trading_pair=BTC-USDT, side BUY or SELL, amount Decimal(0.01), execution_strategy=MARKET, price=None, leverage=1, position_action OPEN on BUY / CLOSE on SELL. The inspected executors_simulator/order_executor_simulator.py MARKET path fills at the **first supplied candle timestamp**, entry price = close at fill, filled_amount_quote=amount*close, cum_fees_quote=trade_cost*notional and CloseType.POSITION_HOLD. Only a single filled action per bar is allowed. Do not interpret a SELL as initiating a naked spot short.
- **Clock/causality boundary:** the simulator's raw timestamp corresponds to candle **open**, while its modeled fill price is the **same completed candle close**. The strategy uses the engine's explicitly **historical same-completed-close accounting convention**, with economic decision/fill availability labeled E[t] in research event output. It does **not** claim a live market order sent after observing C[t] can obtain C[t], or that the raw T[t] is a causal close-signal time. No next-open, intrabar, maker or stop-fill capability is inferred.
- **Position/cost accounting:** BacktestPositionHold (in backtesting_engine_base.py) nets opposite-side amounts, tracks average entry and gross realized PnL from matched volume, and aggregates cum_fees_quote; net quote PnL must subtract **both** filled-side fees from gross, and independent cash/inventory accounting must reconcile. trade_cost=0.001 per side is **explicitly hypothetical**, not an exchange-observed rate. Spot funding is **not applicable**, rather than a zero-funded perpetual assumption. No simulated spread/slippage/latency/partial fills or exchange min-notional/precision verification is asserted; future production use requires those checks.
- **Ledger ordering:** update_state refreshes prior executor/position state before the new action, so an in-flight action and the next update/terminal flush must reconcile fills before considering exposure FLAT again. Retain the authoritative executor ledger or disable short terminated-executor pruning; otherwise an old filled action may disappear from a controller's view. Any missing/unconfirmed fill fails closed, not fabricated.

### Six-gate evidence (Scout proposal; independent Auditor still required)

1. **Determinism:** complete TR/WMA21/HH21/LL21 recurrences and seeds, prior-bar rails, strict dual-threshold ret latch, pos state machine, fresh-flip edge, input validation and 100-bar warmup; Length=21/Multiplier=3 are the author's published defaults, not fitted values.
2. **Direction:** only spot BUY to open LONG and SELL to close LONG; source SHORT side and reverse mode explicitly disabled.
3. **Entry/exit/risk:** exact fresh-flip entry; full exit on opposite flip; no stop/TP/intrabar or other hidden defaults (the source likewise carries no stops).
4. **Position:** 0.01 BTC, 100000 USDT, fee-aware cash ledger, one in-flight action, no DCA/pyramiding/concurrency, deterministic fresh-edge re-entry, same-bar conflict excluded by construction.
5. **Pinned model:** source-inspected Binance spot 1d candles, OrderExecutor MARKET close-price fill, CreateExecutorAction, POSITION_HOLD netting and fees, with clock/precision/economic limits disclosed; source commit and VERSION pinned.
6. **Causality:** prefix-only completed bars (all rails prior-bar shifted), 100-bar no-trade seed, open-to-close availability correction, no missing-price invention or future lookahead, same-close fill explicitly a research convention.

**PASS is proposed eligibility for the precise derivative's historical model, not a self-approved audit, source-native replication, Qlib parity, profitability or permission to trade.**

## Evidence

### Source-reported

FMZ strategy 438053 (ChaoZhang, inspected 2026-10-27; mirror fmzquant/strategies@7853bb2): HPotter "Trend Trader Strategy" Pine v2 implementing Abraham TASC-Sep-1998 — WMA(ATR(1),21), 21-bar highest/lowest, ±3×avgTR inset rails, ret/pos latch, long/short entries with optional reverse, declared 1d backtest context on Futures_Binance BTC_USDT. No reproducible returns, fee assumptions or live terms are claimed.

### Independently reproduced

**None.** No Hummingbot/Qlib backtest, event-level parity, real fills, performance figures or live economics reproduced. Pinned Hummingbot source **compatibility inspection** is not a strategy backtest.

### Negative evidence

Original TradingView page/revision hash not retrieved; original signal/exit events not known; exact package wheel not rehashed; no dedicated controller; no exchange precision, actual fee, spread/slippage, partial-fill or production cash enforcement; no Qlib/Hummingbot event-level parity. All unverified source details (futures venue, short side, reverse mode) are explicitly replaced by researcher-authored derivative rules, not silently attributed to the author.

## Falsification plan

After separate approved strategy-specific materialization, replay representative closed-candle sequences through pinned Hummingbot and Qlib with identical data, fees and modeled same-close semantics. Compare each TR/avgTR/rail/ret/pos transition, BUY/SELL timestamp at E[t], side, price, size, fee, inventory and cash. Resolve event-level divergences before mass Qlib screening. Then compare the frozen derived hypothesis with a plain Donchian-21 breakout control under identical costs and sample; poor net expectancy or unstable cross-window behavior rejects the economic hypothesis, **not** the six-gate admission.

## Crypto portability

Only BTC-USDT Binance spot UTC 1d is claimed for this immutable derived version. Other pairs, frames, perpetuals, the short side, reverse mode, DCA overlays, real protective orders and leverage change execution/economic assumptions and require explicit separate capability validation; the optional downstream campaign is not an HB_READY entry gate.

## Limitations

This is an FMZ/HPotter-inspired **independent derivative**, not source-native Pine. Same-completed-close market fills are historical simulator bookkeeping, not attainable guaranteed real executions. An opposite-flip exit is not a protective stop; severe gaps may exceed any expected loss. Fee/slippage/precision economics are incomplete for trading; no backtest or profit claim exists.

## Implementation status

**not-implemented**: research specification only. A future selected candidate needs a minimal dedicated controller/executable recipe and representative event-level engine parity before screening on an unverified path. No new admission registry, generic compiler or workflow is introduced.

## Adoption boundary

**research-only / not-approved / research-only approval scope**. Independent Hermes Auditor GitHub Webhook Review alone may verify exact-head six-gate PASS and merge; a failure must not be promoted. The existing signed webhook receiver alone owns post-merge README count bookkeeping. No trading, backtest, deployment or other repo modifications are authorized by this record.

## Related Wiki records

None created or changed. Distinct from Eterna/Forven Chandelier stop records, Keltner band records, and HPotter KAMA21 (shared Pine author only).

## Sources

- Primary: https://www.fmz.com/strategy/438053
- Immutable mirror: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Andrew-Abraham%E8%B6%8B%E5%8A%BF%E8%BF%BD%E8%B8%AA%E7%AD%96%E7%95%A5Andrew-Abraham-Trend-Tracking-Strategy.md
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Admission contract: https://github.com/HCH725/alpha-strategy-research/blob/1eaaeb8d20307baf1ac8fe1b2988c17b5b182a/.github/HB_READY_REVIEW.md
