---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TASC 2025.05 Rule 1: OLS40 slope-sign trend flip, derived BTC-USDT spot 1d long-flat"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/nTdxANi4-TASC-2025-05-Trading-The-Channel/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TASC 2025.05 Rule 1 — OLS40 slope-sign trend flip (derived BTC-USDT spot 1d long-flat)

## Provenance

Primary source: TradingView public open-source script page, PineCodersTASC, "TASC 2025.05 Trading The Channel", published 2025-04-17, stable script identity nTdxANi4, directly inspected 2026-10-25: https://www.tradingview.com/script/nTdxANi4-TASC-2025-05-Trading-The-Channel/ . The publication explicitly attributes the three-channel-method discussion to Perry J. Kaufman's May 2025 TASC article; that is background attribution, not an independently inspected executable source.

**Source-native facts verified from the public page (not from inaccessible Pine text):** its Rule 1, "Trade the trend", opens/reverses when the linear-regression slope changes sign: negative-to-positive closes short and enters long; positive-to-negative closes long and enters short. The described channel period default is 40 and regression source default is close. The page also describes two *other* modes (channel breakout and channel-zone mean reversion), which are not used here. The page says the long-only option is deselected by default; the optional percentage stop is disabled by default; default automatic position sizing is defined for equities/futures, with Manual selection needed for other instruments; commission and slippage are not specified by default. These are source statements, not claims that this researcher retrieved every Pine order instruction.

**Independent derived strategy, NOT source-native/lossless:** This record selects Rule 1 only; fixes a precise 40-close ordinary-least-squares slope formula and zero/tie state machine; ports to Binance BTC-USDT spot daily candles; disables short entries/reversals so positive-to-negative becomes long exit to flat; adopts 50-bar no-trade warmup, fixed unit and cash, explicit no-pyramiding/no-DCA/no-stop/no-TP, research-close fill timing and fixed research costs. Every one of these is a **researcher-defined executable specification**, not an assertion about the uninspected Pine code, its execution settings, or the published performance. No numerical backtest claim is adopted.

**Immutable identity:** TV script nTdxANi4 / public publication 2025-04-17 / selected described Rule 1 / derived spec v1 (2026-10-25) / OLS40-close slope sign / BTC-USDT Binance spot 1d / long-flat / close-fill model / fixed 0.001 BTC. The public page does not expose a verified Pine version number or immutable script-code hash in this inspection; the stable public script ID and publication date pin provenance, while the complete derived decision rules below pin this candidate independently. Later TradingView code changes must not silently alter this derivative.

**Dedup (current main bddfb49b573f0ab86f293feafc2968014eaaa7d6):** no nTdxANi4/TASC 2025.05 source match in repository code search or the open research/* PR search. Closest main cousins: linreg-channel-band-touch-two-sided-btcusdt-1d-2026-10-12.md uses slope-gated residual-band *touches* with EMA50 and midline exits; forven-linreg-channel-breakout-long-flat-btcusdt-1h-2026-10-17.md buys a +2-sigma *breakout* and exits below the midline; chande-forecast-oscillator-zero-cross-two-sided-btcusdt-1d-2026-10-15.md crosses a price-versus-regression forecast *deviation*, not the fitted slope sign. This candidate uses the 40-bar OLS *slope's sign transition alone* to enter/exit, without channel bands, deviation threshold, EMA, oscillator or price crossover. Same vocabulary does not make the decision rule materially identical. All ten open research/* PRs found at intake were different sources/mechanisms. Dedup is limited to the checked snapshot and is re-evaluated by the independent reviewer.

## Economic mechanism

Source-reported: Rule 1 treats a sign change in fitted linear-regression slope as a trend-direction change. Research interpretation: long-only directional persistence; buy the first verified negative-to-positive slope regime flip, hold through positive slope, exit on the first positive-to-negative flip. No claim of expected profitability, source-native risk protection, or original TASC performance.

## Signal

**Frozen derived arithmetic (all decision-critical rules):**

- Input: a strictly ordered contiguous sequence of *completed* Binance spot BTC-USDT UTC 1d candle closes C[t], finite and strictly positive. No future bars, adjusted historical series, model fitting on the full sample, or cross-market features.
- For each t >= 39, take the trailing 40 closes C[t-39] through C[t], indexed j = 0,...,39. Define xmean=19.5, denominator D=sum((j-19.5)^2)=5330. Define S[t] = sum((j-19.5)*C[t-39+j], j=0..39)/5330. This is the ordinary-least-squares regression slope of the trailing 40 closes against increasing bar index, in quote units per daily bar; intercept/channel bounds are not traded.
- Define sign[t] = +1 if S[t]>0, -1 if S[t]<0, and 0 if S[t]==0. No arbitrary epsilon. A zero does not cause a trade or overwrite last_nonzero_sign; it carries the previous nonzero sign until a nonzero observation appears. If no previous nonzero sign exists, no sign-flip order can occur.
- Maintain last_nonzero_sign from *completed* observations. If prior last_nonzero_sign == -1 and sign[t] == +1, emit one BUY signal (enter if FLAT). If prior last_nonzero_sign == +1 and sign[t] == -1, emit one SELL signal (close if LONG). Otherwise emit NONE. After evaluating an eligible bar, update last_nonzero_sign to sign[t] when nonzero. Strict polarity flips are mutually exclusive; a zero plateau cannot create phantom reversals.
- Seed sign state using completed bars t=39..49; **the first 50 completed candles are no-trade warmup**, regardless of sign changes. First order-eligible decision is t=50 (the 51st completed bar), using only the trailing 40 closes then available. If the seed was positive and never previously negative, do not enter merely because the sign is positive. The last bar does not trigger an invented forced liquidation.
- All signals are computed once per completed daily bar. Flat+SELL and LONG+BUY are no-ops; there is no same-bar round-trip, no simultaneous positions, and no order when input is invalid.

This precise slope formula, zero-plateau memory, startup posture and entry suppression are **researcher pins** filling gaps in the publicly readable prose; they are not attributed to the original Pine implementation. Other periods, sources, sign tie conventions, or startup semantics are different derived versions.

## Direction, exits, risk and position state

- Venue: Binance BTC-USDT **spot**; direction LONG or FLAT only. Shorts, leverage, margin borrowing, hedge and simultaneous markets explicitly disabled.
- Position: initial quote cash 10,000 USDT, no borrowed funds; fixed order amount 0.001 BTC, one long unit maximum, no pyramiding, partial scale, DCA, safety orders, compounding, concurrency or rebalance. The full unit exits on the first eligible positive-to-negative slope flip. No take-profit, stop-loss, trailing stop, timed exit, profit gate, opposite short order, or discretionary override; all are explicitly disabled for this derivative. This is risk disclosure, not a recommendation to trade without a stop.
- BUY only if model state is FLAT, 0.001 BTC positive price exists, and available quote cash covers 0.001*C[t]*(1+0.001); otherwise skip without fabricated credit or fill. A skipped sign-flip does **not** create an artificial later entry: another genuine -1-to-+1 flip is required. SELL only if the recorded filled long unit exists; it closes exactly that unit. No cooldown: after an exit, a future positive flip can re-enter. No forced end-of-sample close; mark an open long to the final valid close and report it separately.
- Controller state is FLAT/LONG plus an in-flight action flag, last_nonzero_sign, and filled-unit/quote-cash ledger. At most one action per daily bar. A controller implementation must reconcile successful simulated fills before changing the filled-unit ledger and must not infer same-tick exposure from a stale positions_held or a bounded terminated-executor window. Rejected/invalid order => fail closed, no phantom exposure. No controller is implemented by this research record.

## Required data and point-in-time causality

- Single 1d Binance spot OHLCV feed; **only close and candle-open UTC timestamp enter the decision**, with OHLCV row integrity used to reject bad data. Exactly 86400-second consecutive UTC open-time increments are required. Duplicate, missing, nonmonotonic, NaN, zero/negative price or partial/incomplete bars invalidate the research segment and abort that run rather than interpolating, forward-filling, fabricating a price, or silently skipping an unobserved sign flip. Validate gaps on raw feed *before* feature joins/dropna.
- The Binance REST candle timestamp is the **bar OPEN** timestamp T[t]. The signal only becomes available at completed bar time E[t] = T[t] + 86400 seconds UTC. Record both decision time and effective model-fill time as E[t], not T[t]. The pinned simulator's same-candle MARKET-close fill is a **research accounting convention**, not a promise that a real order placed after E[t] could receive C[t]. The original TradingView strategy's order-fill behavior is not verified; the timing change is openly derived.
- The 40-bar regression and sign state are computed solely from prefix data through t. No higher-timeframe unfinished candle, lookahead, repainting, future extrema, external data, ML artifact, or hindsight optimizer. No signal before the 50-completed-bar warmup; any terminal open long is valued at observed final close only.

## Execution assumptions — six-gate pinned Hummingbot model

**Immutable engine baseline:** policy package 20260920 / VERSION dev-2.17.0 / HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3. This Scout independently fetched the VERSION, Binance spot interval/parser, BacktestingEngineBase, OrderExecutorSimulator, and OrderExecutorConfig files at that exact commit via the GitHub app. Separate package-to-source verification is **inherited as prior independent evidence** from accepted Alpha PR #414 (902/902 shipped Python files and wheel SHA256 ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148); no wheel bytes were rehashed in this cycle.

- Data: binance_spot_candles/constants.py supports 1d; binance_spot_candles.py parses REST kline open-time and OHLCV; BacktestingEngineBase.prepare_market_data() exposes close_bt and close after candle-feed assembly. A dedicated, not-yet-implemented strategy-specific controller can compute the OLS40 sign state from completed candle rows. Validate raw timestamp gaps *before* prepare_market_data's dropna and feature joins.
- Controller/action: BacktestingEngineBase.simulate_execution() updates each processed row, calls controller.determine_executor_actions(), dispatches CreateExecutorAction to simulate_executor(). OrderExecutorConfig allows connector_name=binance, trading_pair=BTC-USDT, BUY or SELL, amount=Decimal("0.001"), execution_strategy=MARKET, price=None, leverage=1; use SELL as a full close of an existing spot unit. No unsupported short/maker/intrabar/next-open path is claimed.
- Fill: pinned OrderExecutorSimulator.simulate() MARKET branch fills on the first supplied candle at its **close**, with filled_amount_quote=amount*close and cum_fees_quote=trade_cost*filled_amount_quote, returning POSITION_HOLD. The simulator indexes the fill with candle open-time; the derivative explicitly corrects event interpretation to open+86400s. Never treat this as an actual exchange fill, never substitute an absent price, and do not assert real-world same-close executability.
- Position/cost: BacktestPositionHold._process_order() nets opposite-side amounts, tracks average cost and **gross** realized PnL; add_executor() accumulates both-side fees. Compute research net quote PnL separately as realized gross minus both-side cum_fees_quote. Use fixed research trade_cost=0.001 per filled side (0.1% of quote notional) **as a disclosed model assumption reused from independently accepted PR #414**, not as a sourced live Binance fee schedule, not as the TradingView author's commission and not as an observed charge. BUY debits notional+fee, SELL credits notional-fee; account cash and marked inventory reconcile independently. Spot funding is **not applicable**; never replace perpetual funding with invented zero funding. The simulator does not price spread/impact/latency/slippage: zero *additional simulated* slippage is a model limitation, not an empirical zero. Exchange tick/lot precision, minimum-notional, partial fills and actual costs are not verified; no live execution claim follows.
- Model-bound scope: one spot pair, one daily frame, completed-close MARKET simulator, fixed unit and explicit fee accounting only. No actual dedicated controller, Qlib executable recipe, model run or performance result is claimed. No inference that the simulator supports unrelated fills, cross-asset portfolios, funding, leverage, or production exchange execution.

## Six-gate admission evidence (research proposal; independent Auditor decides)

1. Determinism: 40-close OLS slope exact sum/denominator, strict sign, zero-state, seeding and missing-input behavior are fully frozen; no model training or tunable unseen parameters.
2. Direction: explicit BTC-USDT spot LONG/FLAT, with all short orders disabled as a declared departure from source Rule 1.
3. Entry/exit/risk: negative-to-positive enters; positive-to-negative exits; stop/target/trailing/timed exits explicitly absent; precedence and terminal position specified.
4. State: 0.001 BTC, 10,000 USDT, one position, no DCA/pyramiding/concurrency/cooldown, skipped-entry behavior, no same-bar double actions, and fill reconciliation specified.
5. Engine: inspected pinned 1d spot feed, MARKET OrderExecutor close-fill, CreateExecutorAction path, POSITION_HOLD netting, both-side fee and effective timestamp; precise package/commit identity supported by prior independent wheel audit, with economic/precision limitations disclosed.
6. Causality: trailing prefix-only OLS, 50-bar no-trade warmup, UTC candle-close availability, gap fail-closed and no future features. Model close-fill is distinguished from live executable timing.

These six items are **Scout-submitted evidence, not self-approved independent PASS review**. The frontmatter PASS is a proposed admission status and cannot authorize merge without the separate Hermes Auditor exact-head review.

## Evidence

### Source-reported

PineCodersTASC TradingView page (2025-04-17): Rule 1 trades changes in linear-regression slope sign, default period 40, default regression source close; default optional stop disabled and automatic sizing equities/futures oriented. No numerical strategy performance is adopted.

### Independently reproduced

**None.** Read-only primary-source inspection and pinned-engine static code inspection were performed; no TradingView run, Hummingbot/Qlib backtest, strategy-specific event parity, profitability study, Paper/Testnet/Live or deployment was performed. Prior PR #414's isolated primitive validation is cited as historical engine evidence, not falsely re-run.

## Limitations and falsification

The complete original Pine script and its exact order-fill defaults were not independently retrieved; source-native/lossless reproduction is NOT claimed. The derivative's 40-bar OLS formula, zero tie memory, warmup, long-only choice, market/frame, fixed unit and costs are researcher-defined. A future original Pine inspection showing materially different Rule 1 logic would require explicit provenance reassessment, not silent rewriting. Same-close model fills, absent spread/impact, simplified lot/tick behavior, fixed research fee and no stops can materially distort economic results. No fee-adjusted returns, drawdown, Sharpe, historical Survivor status or Qlib parity are asserted.

A subsequent **separately authorized** representative Qlib/Hummingbot event-level parity check must precede mass Qlib screening if this execution primitive/path has not already been validated for the selected implementation. No such check is part of Scout.

## Implementation and adoption

Implementation: not-implemented (no dedicated controller, Qlib recipe or run artifact added). Adoption: not-approved; approval_scope: research-only. No trading authorization, no live capital commitment, no repo-to-engine deployment.

## References

- Primary TradingView source: https://www.tradingview.com/script/nTdxANi4-TASC-2025-05-Trading-The-Channel/ (PineCodersTASC, 2025-04-17, inspected 2026-10-25).
- Immutable pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent package/source and primitive review: https://github.com/HCH725/alpha-strategy-research/pull/414
