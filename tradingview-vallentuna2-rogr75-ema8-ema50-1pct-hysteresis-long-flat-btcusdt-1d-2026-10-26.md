---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Vallentuna2 RoGr75 EMA8/EMA50 1pct buffered-cross long-flat BTC-USDT spot 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-07
sources:
  - https://www.tradingview.com/script/z3zIFBRR-RoGr75-EMA-Cross-Signal-with-Buffer-and-Variable-Distance/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Vallentuna2 RoGr75 EMA8/EMA50 ±1% buffered-cross long-flat — independent research derivative

## Provenance

**Primary source (public TradingView only):** Vallentuna2, *RoGr75 - EMA Cross Signal with Buffer and Variable Distance*, stable TradingView script ID **z3zIFBRR**, first published **2025-01-31**, revised **2025-02-07** with author-labelled **v1.1**. Canonical URL: https://www.tradingview.com/script/z3zIFBRR-RoGr75-EMA-Cross-Signal-with-Buffer-and-Variable-Distance/ . First-party public page read on 2026-10-26. The page labels the work an **open-source indicator**, not a backtested executable strategy. Its February revision explicitly states the buy trigger as fast EMA crossing ABOVE slow EMA + buffer_distance, the sell trigger as fast EMA crossing BELOW slow EMA - buffer_distance; buffer_distance is a percentage of slow EMA. Published defaults are EMA8, EMA50, buffer 1.0%, ATR14 and ATR label-distance multiplier 2.0. The ATR affects label placement only, not the source's buy/sell predicate. The prose describes alerts, labels and background colors, not orders, fills or trade profitability.

**Source evidence boundary:** The TradingView public description and release notes were directly readable, but the actual Pine source-code tab bytes were **not** retrieved. Thus there is no claim of a Pine revision hash, source-native initialization/na-handling, executable Pine order semantics, stop, fees or full script parity. The decision-critical indicator crossover and defaults above are verified from the author's v1.1 release notes. This record is a **separately specified independent derived trading strategy** using those signals, never a lossless conversion of an executable TradingView strategy.

**Researcher-defined adaptations (all declared, not attributed to the author):** BTC-USDT Binance **spot** on **UTC 1d** candles; SMA-seeded EMA8 and EMA50 mathematics; 200-completed-bar warmup and strict feed validity; interpretation of the indicator's BUY alert as a spot long entry and SELL alert as that long's exit (not a short entry); fixed 0.001 BTC, 10,000 USDT starting cash, full-fill pending states, no pyramiding/DCA, no other exits; idealized completed-bar-close MARKET simulator execution; 0.1% per-side hypothetical research fee; and no other modeled slippage. None of these choices is a source-native performance claim. Any altered EMA seed, buffer, direction, timing, risk or sizing is a different derived identity.

**Dedup checked at pre-write main SHA a9e5f43d8e1e8da9d59034bc14c7256a88dfa05a (2026-10-26):** GitHub connector code search on main for z3zIFBRR, RoGr75, Vallentuna2 and buffer_distance returned no matching strategy. Open research PR search for this source ID returned no matches; open research/* PRs were inspected. The closest admitted EMA20/50 cross record enters at the zero-distance EMA cross, while ActionZone enters on a two-EMA-and-price zone transition; neither requires **EMA8 crossing EMA50×1.01** and later **crossing EMA50×0.99**. The PFE hysteresis record is a fractal-efficiency oscillator, not buffered moving averages. The exact source identity and materially different dual buffered crossing rules are not already present in those checks. A mere EMA-period retuning would not count as novelty; the ±1% separated entry/exit rails change the event mechanism.

## Economic mechanism

### Source-reported

A two-moving-average trend indicator uses a **1.0% slow-EMA-relative dead band** to suppress small crosses and reduce whipsaws. The short EMA must escape above the upper band for a BUY alert and below the lower band for a SELL alert. ATR14 × 2.0 is for visual signal-label displacement, **not** a stop or signal gate. The source provides no verified return, drawdown, fill, trade or fee statistics for this derived trading system.

### Research interpretation

An explicit long/flat **hysteresis** position machine: enter only on an upward breach of the upper rail and stay long through the interior ±1% band until a later downward breach of the lower rail. This is not a plain EMA8/50 cross and not a continuously retested level rule. Delayed exits may increase adverse exposure; reducing cross noise does not establish positive expectancy.

## Signal

**Data and deterministic preprocessing:** exactly one Binance BTC-USDT spot **1d** UTC OHLCV stream. Let t be the 0-based index of a **completed**, consecutive daily candle. Require strictly increasing timestamps with 86,400-second spacing; finite O,H,L,C strictly >0, high >= max(open,close), low <= min(open,close), volume finite >=0; reject duplicates, missing candles, undefined closes, impossible OHLC or non-finite indicator results. Abort the research run as data-incomplete on any such defect, including while positioned; do not bridge gaps, manufacture prices or continue with fictitious fills.

**EMA seed pinned by this researcher, not asserted to match inaccessible Pine:** EMA8[7] = arithmetic mean(close[0..7]); for t>=8, EMA8[t] = (2/9)×close[t] + (7/9)×EMA8[t-1]. EMA50[49] = arithmetic mean(close[0..49]); for t>=50, EMA50[t] = (2/51)×close[t] + (49/51)×EMA50[t-1]. Prior values undefined. All calculations use actual completed closes, never forward data. No fitted parameters, optimization, repainting or higher-timeframe calls.

**Rails:** U[t] = 1.01×EMA50[t]; L[t] = 0.99×EMA50[t]. The fixed source-described 1% buffer is measured relative to EMA50, not close, EMA8 or ATR.

**Crosses, strict and reproducible:**
- BUY_ALERT[t] iff EMA8[t-1] <= U[t-1] **and** EMA8[t] > U[t].
- SELL_ALERT[t] iff EMA8[t-1] >= L[t-1] **and** EMA8[t] < L[t].
- Equality on the current bar is NOT a cross. Previous equality followed by a strict escape IS a cross. An already-above-upper EMA8 does not cause repeated BUY alerts; an already-below-lower EMA8 does not cause repeated SELL alerts.
- The current fast EMA cannot be strictly > U and strictly < L on one bar because L < U for positive EMA50; simultaneous BUY/SELL is impossible. No implicit conflict arbitration.
- ATR14 and label-distance 2.0 are **explicitly excluded from all trade decisions**: visual-only source settings, not missing strategy inputs.

**Warmup:** require **200 consecutive fully completed valid 1d bars** before the first actionable cross (earliest t=199), with valid current and previous EMA/rails. This is a researcher-chosen stabilization floor for both EMA seeds; not claimed to be the source's exact warmup. Signals before t=199 are ignored, starting inventory is FLAT, and a pre-warmup alert is never replayed retrospectively.

**Position state and exact transition priority:**
1. States: FLAT, PENDING_BUY, LONG, PENDING_SELL. Initial FLAT with 10,000 USDT and 0 BTC. Pending states issue no additional orders; creating an action alone does NOT constitute a fill.
2. When FLAT after warmup, BUY_ALERT causes exactly one MARKET BUY for 0.001 BTC only if actual modeled available cash >= 0.001×observed close×(1+0.001). On confirmed full simulated fill, debit cash and enter LONG. If the BUY cannot be filled, remain FLAT and require a **new later** BUY_ALERT; no same-signal retry.
3. When LONG, SELL_ALERT causes exactly one MARKET SELL of **the confirmed 0.001 BTC inventory**, entering PENDING_SELL; on confirmed full fill, credit cash and return FLAT. If SELL fails without a valid close, abort the run instead of inventing a fill; otherwise a non-filled SELL remains pending and must be resolved before further actions. The pinned MARKET simulator normally fills immediately on a valid first row.
4. While LONG, ignore all BUY alerts (no pyramiding); while FLAT, SELL alerts are no-ops. Re-entry after a completed exit requires a **fresh later** upper-rail upward cross. Cooldown is zero bars; no same-bar exit-and-reentry.
5. **Disabled explicitly:** SHORT, leverage, futures/perpetuals, funding, borrowing, pyramiding, BO/SO/DCA, safety orders, concurrent positions, compounding, partial exits, limit/maker/next-open/intrabar orders, protective stop, take profit, trailing stop, timed exit, end-of-sample forced liquidation, portfolio-level risk filters, ATR stop, additional indicator gates, and discretionary action. If still LONG at the final actual valid close, mark open inventory at that observed close and do not invent a SELL.

## Required data

Only **observed** Binance BTC-USDT spot UTC 1d O/H/L/C/V and the derived EMA8/EMA50 series; the trading predicate reads closes, but OHLCV integrity checks are required. No order book, on-chain feed, cross-pair synchronization, future funding, ML model, higher/lower timeframe or assumed missing-price replacement. For source provenance, the author also defines ATR14 as **visual-only**, deliberately not needed for the derived order predicate.

## Execution assumptions

**Pinned admission model (inspected via connected GitHub on 2026-10-26):** Hummingbot package label **20260920**, VERSION **dev-2.17.0**, inspected implementation **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. The pinned VERSION file, BinanceSpotCandles constants/parser, BacktestingEngineBase, OrderExecutorConfig, OrderExecutorSimulator and BacktestingDataProvider were read in this cycle. Prior independently reviewed Alpha PR **#414** records a 902/902 wheel-file byte comparison and representative engine-path tests; this Scout does **not** independently rehash a wheel/image or assert a current deployment digest.

- **Actual candle path:** BinanceSpotCandles constants map 1d and /api/v3/klines; REST parser maps row[0] to candle **opening** timestamp and row[1..5] to OHLCV. Require the complete row and verify contiguous data **before** BacktestingEngineBase.prepare_market_data, which uses backward merge_asof and dropna and must not silently hide missing bars.
- **Actual action and fill path:** A future strategy-specific controller would evaluate the exact frozen signal on a completed row and submit CreateExecutorAction with OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY or SELL, amount=Decimal("0.001"), position_action=OPEN or CLOSE, execution_strategy=MARKET, price=None, leverage=1). Pinned BacktestingEngineBase.simulate_execution iterates update_state -> determine_executor_actions -> simulate_executor, dispatching OrderExecutorConfig to OrderExecutorSimulator. Pinned simulator MARKET fills **fully on the first supplied row at its actual close**, sets filled_amount_quote = 0.001×close, cum_fees_quote = trade_cost×filled_amount_quote, and CloseType.POSITION_HOLD. This is a demonstrated **historical full-close simulator convention**, not a claim of executable real-market post-close fills or a pre-existing candidate controller.
- **Causality and effective clock:** Raw Binance candle timestamp T[t] denotes **open**, whereas close[t] is available only at **T[t]+86,400 seconds**. A correct derived controller/event adapter must withhold this bar's signal until completion and label its decision, simulated full-close fill and accounting event with that close-effective time; the native merge_asof/open-timestamp label alone does NOT establish causality. No implementation may treat close[t] as known at T[t]. A controller/ledger that cannot enforce this effective-clock contract is **not** an authorized realization of this PASS proposal; the independent auditor must reject if the pinned path cannot actually support it. The assumed historical close fill is deliberately idealized and not an assertion of a fill after seeing the close.
- **Actual position and cost path:** BacktestPositionHold in backtesting_engine_base.py nets filled BUY/SELL base amounts, records weighted entry cost, gross matched realized PnL and accumulated fees **separately**. The engine's terminated executor controller view is bounded by default; require terminated_executors_window=None or equivalent persistent fill-confirmed state/ledger. An order action is never silently equated to filled inventory. Never use BacktestingDataProvider.get_price_by_type's fallback Decimal("1") when a real price is absent: fail data validation instead.
- **Pinned research economics, not source or live facts:** start unborrowed 10,000 USDT cash, trade exactly 0.001 BTC, research trade_cost = **0.001** per filled side (0.1% hypothetical fee; no assertion this is Binance's actual commission). Cash after BUY at Pb: cash -= 0.001×Pb×1.001; after SELL at Ps: cash += 0.001×Ps×0.999. Gross matched quote PnL = 0.001×(Ps-Pb); fee-inclusive net = gross - 0.001×0.001×(Pb+Ps). Open mark-to-market equity = remaining cash + held 0.001×last **observed** close; BUY fee already debited. Native gross position PnL is not misreported as fee-inclusive equity. Additional simulator slippage is unmodeled, **not verified zero actual slippage**. Real exchange spread, partial fills, fee tiers, latency, liquidity, lot/tick precision, minimum notional and execution viability are unverified. Spot funding is **not applicable**, not an invented zero perpetual funding rate.
- **Scope:** this establishes bounded pinned historical **spot 1d / MARKET full-close / POSITION_HOLD** expressibility only. No candidate-specific code, backtest, Qlib parity, trading permission or profitability is claimed. A new unverified primitive would need representative engineering validation before mass screening.

## Evidence

### Source-reported

Vallentuna2's **2025-02-07 v1.1** release notes explicitly state fast-EMA crossover of **slow EMA + percentage buffer** for BUY and crossunder of **slow EMA - percentage buffer** for SELL. Defaults **8/50**, **1.0%** buffer, **ATR14** and label distance **2.0** are first-party page facts; ATR is a drawing offset. The script is an **indicator**, with no author-reported performance of this derived spot trading machine.

### Independently reproduced

**Not independently reproduced.** No TradingView/Pine signal replay, Qlib/Hummingbot strategy backtest, trade-level parity, simulated profitability reproduction, Survivor/HB certification, deployment or live trade. This Scout inspected relevant pinned Hummingbot source paths, not a candidate executable or deployed wheel. Prior PR #414 is representative engine-path evidence only, not a new strategy certification.

### Negative evidence

Complete Pine bytes and exact original indicator EMA initialization are unavailable. The SMA seeds, warmup, BTC spot 1d universe, LONG/FLAT mapping, fill/cash model, disabled risk legs and state machine are explicitly researcher-designed. The source itself warns of false signals, EMA lag and buffer sensitivity. A hypothetical full-close simulator cannot establish post-close real fillability; fee assumptions are not verified tariffs. No source performance claim can be transferred to this derivative.

**Six-gate submission summary (pending independent Hermes Auditor):** (1) deterministic EMA seeds, ±1% moving rails, strict crosses and fixed data guards; (2) spot LONG/FLAT with short disabled; (3) exact cross-entry/cross-exit and all other risk legs disabled; (4) fixed 0.001 BTC, full-fill pending states, no DCA/concurrency, fresh-cross re-entry, no cooldown; (5) pinned actual Binance 1d candle, MARKET order simulator, POSITION_HOLD cost ledger, fee and timestamp path with bounded modeling limits; (6) 200 completed-bar warmup, contiguous point-in-time closes, explicit close-effective decision/fill convention and no future data. PASS is a Scout **proposal**, not independent approval.

## Falsification plan

Independently compare the author's v1.1 Pine alerts, if its source tab becomes readable, with this frozen derived EMA seed/rail implementation on the same historical candles; log any divergences rather than relabeling as source-native. Audit strict threshold/equality and fresh-cross behavior, 200-bar warmup, gap abort, fee-inclusive ledger, close-effective timestamps and full-fill state. Before broad Qlib screening of an unverified path, demonstrate representative Qlib/Hummingbot event-level parity of the execution primitive; subsequent Survivor/HB economics are separate. No such run is performed by Scout.

## Crypto portability

BTC-USDT spot 1d is the **researcher-selected** market/frame for a bounded verified engine path, not an HB_READY whitelist or a source-native chart constraint. Other pairs, frames, futures, DCA overlays and leverage require their own explicit executable/economic semantics and are not silently inherited.

## Limitations

Indicator-only provenance; inaccessible complete Pine source; independently chosen EMA seed and position rules; no native stop; potential long drawdown; idealized close fills; unverified real exchange precision/fees/slippage; no installed candidate implementation; no candidate performance, Qlib parity, Survivor or trading approval. Do not convert this PASS research proposal into a deployment claim.

## Implementation status

**not-implemented** — no dedicated strategy controller, executable Qlib recipe, deployed artifact or backtest produced. This is not a second admission status; future implementation is a separate engineering handoff.

## Adoption boundary

**research-only; adoption: not-approved; approval_scope: research-only.** An independent Hermes Auditor must verify the precise source facts, six gates and pinned engine contract before an exact-head merge. Scout does not approve, merge or alter README. Signed existing webhook receiver owns post-merge README bookkeeping.

## Related Wiki records

None claimed; no private Wiki data accessed or copied.

## Sources

1. Vallentuna2, TradingView *RoGr75 - EMA Cross Signal with Buffer and Variable Distance*, public script ID z3zIFBRR, published 2025-01-31, v1.1 update 2025-02-07: https://www.tradingview.com/script/z3zIFBRR-RoGr75-EMA-Cross-Signal-with-Buffer-and-Variable-Distance/
2. Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
3. Previously independently reviewed engine primitive and package-source comparison: https://github.com/HCH725/alpha-strategy-research/pull/414
