---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: SpeculationLab Outside Day downside-close body-filtered three-bar fade, independent BTC-USDT spot 1d long-flat derivative
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-10-11
sources:
  - https://www.tradingview.com/script/X4ulJUXd/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SpeculationLab Outside Day downside-close three-bar fade — independent BTC-USDT spot daily research derivative

## Provenance

**First-party publication:** SpeculationLab, *LW Outside Day Strategy[SpeculationLab]*, public TradingView open-source strategy, published **2025-10-11**, stable script ID **X4ulJUXd**, inspected **2026-10-30**: https://www.tradingview.com/script/X4ulJUXd/ . The publicly readable author page gives the outside-bar geometry (current high exceeds prior high AND current low falls below prior low), a body-size significance filter, a LONG setup when the current close is below the preceding low, a SHORT setup when close is above the preceding high, confirmed-bar evaluation, optional stop modes (previous high/low with ATR buffer, ATR multiple, fixed pips), target modes (opposite swing, RR default 2:1, following-price-open), default 10% equity risk sizing, and reported commission 0.1% plus two ticks of slippage. Complete Pine revision bytes, exact original body-filter threshold, order settings and stop/target defaults were **not** independently retrieved. The page's description calls the close-below-prior-low long setup a bullish rejection; that interpretation is not mechanically assumed to be bullish.

**Independently derived, not source-native/lossless:** This version retains the **literal** source-described outside-bar geometry, close-below-previous-low LONG direction, confirmed-bar input and a body-significance concept. It independently pins the body filter to **current absolute body > 1.5 × previous absolute body**, selects BTC-USDT Binance **spot UTC 1d**, disables the source's short leg and all source stop/target/FPO choices, substitutes a **three-subsequent-completed-bar time exit**, fixed 0.001 BTC, 10,000 USDT initial cash, hypothetical 0.1% filled-side fee and idealized delayed close-MARKET fills. The source does not specify this body threshold or time exit. These alterations change trade events and risk; the original TradingView strategy is **not** asserted to pass HB_READY.

**Frozen identity:** TV:X4ulJUXd:SpeculationLab:2025-10-11 | independent-derived-v1:2026-10-30 | outside H>priorH L<priorL C<priorL body>1.5*priorBody | next-completed-close BUY | three-completed-bar scheduled-close SELL | BinanceSpot:BTC-USDT:UTC1d:LONG-FLAT:0.001BTC:cash10000:fee0.001. Any change to formula, state, timing, fees, risk or market creates a new version.

**Pre-write dedup:** GitHub connector snapshot main **f086fd5218fbcc1627022640914c019d09231d47**: complete non-truncated tree contains **451** root-level strategy Markdown records and README static count **451**. Eighteen spread-across-tree frontmatters were individually checked and all read PASS; this is **not** a claim of all-451 frontmatter verification. GitHub main code search for X4ulJUXd, SpeculationLab and outside-bar returned no matching record; open research PR search for X4ulJUXd returned none. The eleven open PRs were listed and no title presented this source/mechanism. Nearest pattern families differ: the existing *Inside Bar Failure* record requires inside-bar containment before a subsequent failure event and trades two-sided; the NR7 breakout record requires volatility contraction and a breakout above a channel. This derivative instead enters LONG after a **wide outside bar closing below the preceding low**, with a body ratio gate and fixed time exit. It is not a trivial parameter change to either.

## Economic mechanism

### Source-reported

The author presents outside-day extremes as possible reversal/continuation pressure, with body-size screening and configurable protective stops and profit exits. No profitability or portability conclusion is adopted from the author's claims.

### Research interpretation

An unusually large outside bar that ends below the previous day's low may represent a short-lived downside overshoot; a fixed-horizon LONG fade tests subsequent reversion. This is a researcher hypothesis, **not** the author's tested stop/target strategy and not evidence of positive expected returns.

## Signal

**Data and effective clock:** One observed Binance spot BTC-USDT **UTC daily OHLCV** sequence. Raw exchange candle timestamp T[t] denotes **bar opening**; the complete candle is available no earlier than T[t]+86400 seconds. Require consecutive T increments of exactly 86400 seconds, finite O/H/L/C > 0, H >= max(O,C), L <= min(O,C), finite V >= 0, and actual observed closing prices. No synthetic candles, forward fill, partial bars, alternative timeframes, external feeds or future information. If any required bar is absent/invalid, fail the research run rather than bridge the gap.

**Researcher-frozen deterministic setup:** For t >= 1, OUTSIDE[t] = (H[t] > H[t-1]) AND (L[t] < L[t-1]); DOWN_CLOSE[t] = (C[t] < L[t-1]); BODY[t] = abs(C[t]-O[t]); BODY_GATE[t] = (BODY[t] > 1.5 * BODY[t-1]). ENTRY_SIGNAL[t] = OUTSIDE[t] AND DOWN_CLOSE[t] AND BODY_GATE[t]. All comparisons are **strict**; equality fails. No smoothing, ATR, other indicators, fitted coefficients, repainting or future pivots. If the preceding body is zero, the gate still requires current BODY > 0. Volume is validated as data but is not a signal filter.

**Warmup:** Exactly **two** consecutive fully completed valid daily bars are the structural minimum; the first eligible setup is bar t=1. Start FLAT with 0 BTC, 10,000 USDT cash, no inherited position and no pending action. Never infer a position from pre-sample data.

**One-position event/state machine:**

1. At completed close t, if FLAT, no pending order, no fill/confirmation on that bar and ENTRY_SIGNAL[t] true, arm exactly one BUY for the **following completed daily close t+1**. The entry decision uses only data through t; the controller must not recompute entry using t+1 close. The later observed close is used solely as the historical MARKET fill price and to verify sufficient spot cash.
2. At t+1 completed close, if a real valid fill price exists and available cash >= 0.001 * C[t+1] * (1+0.001), issue one MARKET BUY of **0.001 BTC**. If cash is insufficient, consume the signal and remain FLAT, with no invented fill or retry. Any rejected/failed/unfilled executor remains pending until reconciled; never assume that merely creating an action changes inventory.
3. After the BUY fill is confirmed, LONG holds 0.001 BTC. Record the entry fill-bar index b=t+1. The **third subsequent fully completed bar** is b+3; the strategy schedules exactly one MARKET SELL of the entire confirmed quantity at the **close of bar b+3**. This exit is a precommitted calendar/bar-count event, independent of future prices or indicators. The three subsequent bars are b+1, b+2, b+3; the last is the exit-fill bar. No extra next-bar signal delay is added to the time exit.
4. Exit SELL confirmation returns to FLAT and credits cash net of its modeled fee. A failed/unfilled SELL never erases inventory; reissue only on the next valid completed bar, retaining one pending exit and never inventing a close. No same-bar entry after exit, no entry on any fill/confirmation bar, and no stacking. Fresh entry after confirmed exit requires a new later ENTRY_SIGNAL; otherwise zero additional cooldown.
5. End of sample: if a scheduled entry or exit requires a candle not present, record **pending/unrealized**, never fabricate a fill. Mark remaining actual BTC at the final observed valid close; do not force-liquidate. If an execution-critical actual price is absent, mark the run data-incomplete rather than substitute a default.

**Explicitly disabled:** SHORT, perpetual/futures/funding, leverage, margin/borrowing, pyramiding, BO/SO/DCA, compounding, multiple concurrent positions, partial fills, maker/limit/next-open/intrabar order models, discretionary exits, stop-loss, take-profit, ATR stop, prior-swing stop, fixed-pip stop, RR/PHL/FPO target, trailing stop, same-bar reversal, portfolio sharing, dynamic equity-risk sizing and any hidden controller risk defaults. Absence of a protective stop is a material risk, not a source fact.

## Required data

Only historical **real** Binance BTC-USDT spot 1d O/H/L/C/V with exchange opening timestamps and complete candle availability. No lower-timeframe reconstruction, order book, external calendar, fitted model, funding/mark/index data, or multi-asset alignment. The historical engine's market-close fill convention is idealized, not a promise of real market-close execution.

## Execution assumptions

**Pinned benchmark:** Hummingbot package **20260920**, VERSION **dev-2.17.0** per repository admission contract; source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. This Scout used the connected GitHub app to read the actual pinned BinanceSpotCandles constants/parser, BacktestingEngineBase, BacktestingDataProvider, OrderExecutorSimulator, OrderExecutorConfig and validation helpers on 2026-10-30. Package/wheel byte-to-source mapping is **not** rehashed this run; the prior independent package comparison is referenced by Alpha PR #414. Do not equate an accepted API schema with proven live fill fidelity.

- **Feed:** BinanceSpotCandles/constants.py includes interval **1d**. The Binance spot REST parser maps exchange row[0] to candle **open timestamp**, row[1..5] to O/H/L/C/V. Preflight contiguous UTC 86400-second timestamps and complete/finite prices **before** BacktestingEngineBase.prepare_market_data(), whose dropna could otherwise hide missing rows.
- **Controller/executor:** a future strategy-specific controller can maintain the above bar-index state and issue CreateExecutorAction with OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1). OrderExecutorConfig and its validators accept MARKET with no limit price. BacktestingEngineBase.simulate_execution updates state then determines actions and dispatches the actual OrderExecutorSimulator. **No dedicated implementation has been written.**
- **Fill semantics:** OrderExecutorSimulator.MARKET fills at the **first supplied row's actual close** with full base amount, filled quote = amount × close, and cum_fees_quote = trade_cost × quote notional; it terminates as POSITION_HOLD. For a t signal, arm on t and submit the order only at t+1 row, producing the **t+1 close** research fill. The scheduled b+3 SELL uses the b+3 row close without a price-dependent decision. Raw engine timestamps are candle **opens**; every decision/fill reported externally must use the effective **completed-close timestamp T+86400**, and bar-index scheduling must not rely on the engine's raw _time for elapsed-day calculations. This is retrospective close-price research, **not** executable live close-auction timing. A controller that consumes a current incomplete bar, executes entry on t itself, or treats raw T as close availability is nonconforming.
- **Position ledger:** pinned BacktestPositionHold nets opposing filled base amounts, tracks weighted cost and gross realized PnL, and accumulates fees separately. Reconcile from actual executor fill/termination ledger, not merely order intents; use terminated_executors_window=None (or equivalent complete ledger) to avoid losing confirmations. The engine's final tick flush exists for POSITION_HOLD fills. The BacktestingDataProvider price fallback Decimal("1") is **forbidden**: actual finite close or data-incomplete failure.
- **Cash and costs:** unborrowed 10,000 USDT, no borrowed assets; single spot long 0.001 BTC maximum. Explicit research trade_cost = **0.001** (0.1% of each filled side), a **hypothesis** not an independently verified Binance fee tier. BUY cash debit Q*Pb*(1+0.001); SELL credit Q*Ps*(1-0.001). Matched net quote PnL = Q*(Ps-Pb) - 0.001*Q*(Pb+Ps); deduct both filled-side fees from any equity/ROI claim, not just gross position PnL. Spot perpetual funding is **not applicable**, not fabricated zero realized funding.
- **Limits:** simulator assumes full-size historical close fills and has no observed bid/ask spread, latency, impact, partial fills, real slippage, fee tier, order-book depth or live exchange minimum-notional/precision guarantee. Its zero extra price-impact **model** must never be described as actual zero slippage. The source's two-tick slippage setting is **not** claimed to be reproduced. A failed market/order validation or unavailable price is not silently filled.

## Evidence

### Source-reported

TradingView's first-party public page identifies SpeculationLab, publication 2025-10-11, outside-bar H/L geometry, close-below-prior-low long setup, close-above-prior-high short setup, significant-body concept, confirmed-bar evaluation, configurable stop/target alternatives, default 10% equity risk, and reported commission/slippage. Those are author claims, not independently replayed results.

### Independently reproduced

**No strategy backtest, TradingView signal replay, Qlib/Hummingbot event-level parity, profitability test, wheel hash verification, Paper/Testnet/Live order or Survivor result was performed.** This Scout independently inspected the pinned GitHub engine code paths to bound the available one-spot-market, 1d, full-size MARKET-close and POSITION_HOLD fee/position research model. It is not proof of production trading or original Pine equivalence.

### Negative evidence

The complete original Pine revision and exact original body significance threshold, default selected stop/target mode and order/fill semantics were not available from the public page. This record intentionally supplies a **different, fully specified derivative** and never imputes those choices to SpeculationLab. The author's bullish-rejection label for a close below the prior low is a descriptive interpretation, not an independently verified bullish outcome. No source-reported backtest number is transferred to this derivative. No evidence of source-native stop/target fill equivalence or realized slippage is asserted.

**Scout six-gate submission (pending independent Auditor):** (1) exact two-bar outside geometry/body threshold, strict comparisons and deterministic scheduling; (2) Binance spot LONG/FLAT with SHORT disabled; (3) complete entry, three-bar scheduled exit and explicit absence of all protective/target legs; (4) one 0.001 BTC confirmed position, one pending action, cash checks, failure/confirmation/re-entry semantics, no DCA; (5) actual pinned Binance spot 1d candle/parser, MARKET OrderExecutorSimulator, POSITION_HOLD ledger, quote fee model and explicitly corrected effective-close clock, with economic limits disclosed; (6) completed bars only, two-bar warmup, no future inputs at signal, delayed entry and precommitted time exit. **PASS here is a research Scout claim requiring independent review, not approval or HB Certified status.**

## Falsification plan

After independent admission and separate downstream selection only: test equality boundaries for outside high/low, close-vs-prior-low and body ratio; zero prior body; two-bar warmup; missing/duplicate daily timestamps; t-to-t+1 order timing; b+3 time-exit index; end-of-sample pending state; rejected buys; failed exits; fee-inclusive cash/ledger netting; and the raw-open versus effective-close timestamp distinction. If a new unverified execution primitive is required, establish representative Hummingbot/Qlib event-level parity before mass Qlib screening; do not demand new parity for an already verified primitive.

## Crypto portability

Frozen to **BTC-USDT Binance spot 1d**. Single-pair, daily and OHLCV-only are choices, not HB_READY whitelist restrictions. Other pairs, leveraged futures, shorting, portfolio capital sharing or different candle calendars require separate capability and economic verification, not silent inheritance of this PASS claim.

## Limitations

A rare downside outside bar can keep falling; no protective stop is modeled. Three-bar time exit is independent research design, not the author's risk system. Historical close-MARKET full fills are idealized, and reported effective-close timestamps must be corrected from raw engine open labels. No real fee, spread, funding, precision, cash-balance enforcement or exchange execution performance is established. HB_READY does not establish expected returns, Qlib parity, Survivor qualification or trading authorization.

## Implementation status

Research-only record. Dedicated strategy controller, execution artifact, Qlib recipe and backtest are **not implemented**. Any future implementation must reproduce the frozen event state and pinned engine path or fail validation; no automatic admission of changed semantics.

## Adoption boundary

**Not approved** for Qlib campaign execution, Hummingbot deployment, Paper/Testnet/Live, or capital allocation merely by this Scout submission. Independent Hermes Auditor GitHub Webhook Review alone decides exact-head PASS merge or NOT_LOSSLESS closure. README bookkeeping remains the signed receiver's job.

## Related Wiki records

None required for this isolated research submission. Compare existing inside-bar failure-fade and NR7 price-breakout families only as distinct mechanism neighbors.

## Sources

- SpeculationLab, *LW Outside Day Strategy[SpeculationLab]*, TradingView public strategy, 2025-10-11, https://www.tradingview.com/script/X4ulJUXd/ .
- HCH725/hummingbot pinned source commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3, BinanceSpotCandles and strategy_v2/backtesting engine/executor/data-provider files, inspected through connected GitHub app 2026-10-30.
- HCH725/alpha-strategy-research README.md and .github/HB_READY_REVIEW.md at main f086fd5218fbcc1627022640914c019d09231d47, policy effective 2026-10-08.
