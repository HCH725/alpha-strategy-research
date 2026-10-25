---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: EdgeTools CMO9 oversold cross with five-day time exit - independently derived BTC-USDT spot 1d long-flat
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
source_as_of: 2024-10-17
sources:
  - https://www.tradingview.com/script/nFffJSl1/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EdgeTools CMO9 oversold cross and five-completed-day timeout — independent BTC-USDT spot 1d derivative

## Provenance

**First-party TradingView source:** EdgeTools, *Chande Momentum Oscillator Strategy*, published **2024-10-17**, public open-source strategy, stable script ID **nFffJSl1**, https://www.tradingview.com/script/nFffJSl1/ . Its first-party public strategy description was read on **2026-10-26**. The readable page does **not** expose the complete Pine revision, its version, exact Pine boolean expressions, order defaults, execution timing or a Pine content hash. No lossless Pine reproduction or original-Pine HB_READY PASS is claimed.

**Source-reported, not invented:** CMO is 100 times (sum of upward price changes minus sum of downward magnitudes) divided by their sum; the description identifies nine days as a common period, a LONG when CMO falls below -50, an exit when CMO rises above +50, and an alternative exit five days after the buy signal. The source does not prove whether the threshold is a crossing or a persistent level, the exact comparison at equality, the clock on which five days is counted, any stop, commission, fill price, position quantity, short permission, warmup or exchange. The prose's backtest-profit claim is author-reported and is not independently reproduced.

**Independent derived executable research specification, not source-native:** The researcher chooses exactly one Binance BTC-USDT **spot 1d UTC** stream, close-to-close nine-change CMO, a **cross-under -50** entry (not repeated purchases on every oversold bar), a strict **CMO > +50** exit or a **five-completed-daily-bar hold** exit, whichever first; LONG/FLAT only; idealized completed-close MARKET fills; one fixed 0.001 BTC leg; explicit fee/cash/state/failure rules; 30 valid daily candles of warmup; no other exit or risk leg. Nine days is a source-mentioned common length but **not proven to be the published Pine input default**; its adoption here is an explicit researcher choice. Every such selection may change source trades. The source itself has not been validated for native equivalence.

**Immutable research identity:** TV:nFffJSl1:EdgeTools:2024-10-17 | independent-derived-v1 | CMO(close,9,sum-of-deltas) | enter-crossunder(-50) | exit-CMO-gt(+50)-or-confirmed-entry-plus-5-completed-daily-bars | BinanceSpot:BTC-USDT:1d:LONG-FLAT:0.001BTC | completed-close-MARKET:trade-cost-0.001 | 2026-10-26. Any change to thresholds, formula, timing, time exit, market, fee, sizing or state constitutes a different derivative.

**Pre-write dedup on main SHA cbd906d33b0d4455a28d3a928b23c669225195a2:** README 337 and untruncated recursive Git tree 337 root-level strategy Markdown records. GitHub code search for nFffJSl1 and open-PR search for that source ID returned zero matches; 10 open research/* PR titles and source-bearing descriptions were reviewed and none used this URL or CMO9 five-bar timeout. The nearest admitted CMO record, chande-momentum-80-cross-reversal-two-sided-btcusdt-1d-2026-10-10.md, is the **different** burgercrisis TradingView s1uuFSdY CMO9 strategy: cross UP through -80 to LONG and cross DOWN through +80 to SHORT, two-sided reversal with no five-bar timeout. This derivative instead crosses DOWN through -50 to open a mean-reversion LONG, exits to FLAT at >+50 or on a five-bar time limit, never shorts. Not a paraphrase or parameter-only variant. Other CMO references are components of unrelated multi-indicator rules. Count agreement is not a claim of independent reinspection of all 337 historical PASS frontmatters.

## Economic mechanism

### Source-reported

The author describes oversold Chande momentum as a candidate for mean reversion, with an overbought or elapsed-time exit. References and claims of historical profitability on the source page are explanatory/source claims, not verified evidence of realized returns.

### Research interpretation

The derivative buys the *onset* of an unusually negative nine-day balance of signed close changes, seeking rebound within five further completed UTC daily bars. Unlike an oversold recovery entry or two-sided CMO reversal, it is an entry-on-deterioration, finite-horizon, long-only mean-reversion hypothesis. A continuing selloff is a clear falsifier; there is deliberately no protective stop.

## Signal

**Input and clock:** one actual Binance BTC-USDT spot UTC 1d OHLCV candle stream. A candle with exchange opening timestamp T[t] becomes a valid completed observation and decision input only at **T[t] + 86400 seconds**. Require consecutive daily UTC timestamps spaced exactly 86400 seconds, finite observed O/H/L/C > 0, H >= max(O,C), L <= min(O,C), and nonnegative finite V. A missing/duplicated/invalid candle is a data failure; no synthetic prices, forward fills or price fallback.

**Pinned CMO arithmetic:** Let d[t] = C[t] - C[t-1] for t>=1; u[t] = max(d[t],0); v[t] = max(-d[t],0). For t>=9, U9[t] = sum(u[t-8..t]), D9[t] = sum(v[t-8..t]), and CMO9[t] = 100*(U9[t]-D9[t])/(U9[t]+D9[t]). If U9+D9 = 0, CMO9 is undefined and must not be replaced with 0 or a previous value. No EMA/Wilder smoothing, lookahead, pivot or additional filter is used. EntryCross[t] = (CMO9[t-1] >= -50 AND CMO9[t] < -50); both readings must be valid. Equality at current -50 does not trigger. ExitOverbought[t] = (CMO9[t] > +50), strictly, whether or not a crossing occurs.

**Warmup and initialization:** 30 consecutive fully completed, validated UTC daily bars before first permitted decision, with valid CMO at t and t-1. Start with 10,000 USDT cash, 0 BTC and no pending order. Do not infer a pre-existing long from pre-warmup signals.

**Per-bar priority/state machine:** Exactly once per valid completed daily bar: (1) If an unresolved order exists, do not submit another; reconcile its real simulated confirmed fill/failure first. (2) If confirmed LONG, exit by one SELL of the **confirmed held base quantity** when ExitOverbought[t] OR t >= entry_fill_bar_index + 5. The entry bar itself counts as zero; t+1 through t+5 are the next five completed daily bars. If both exit reasons coincide, record overbought as primary and timeout as simultaneous secondary, with only one SELL. Entry predicates are ignored on exit bars. (3) If confirmed FLAT, and no exit was made on this bar, BUY exactly 0.001 BTC only if EntryCross[t] and available cash >= 0.001*C[t]*(1+0.001). No other entry.

**Fill-confirmed state:** Creating BUY makes pending=BUY, not LONG. Only a confirmed full fill sets LONG and records its actual fill-bar index. Failed/rejected/unfilled BUY clears pending and remains FLAT, without an automatic retry; a later *new* cross-under is required. Creating SELL makes pending=SELL and retains the held position until confirmed. Failed/rejected SELL leaves LONG and requires a retry on the **next completed valid daily bar**, irrespective of whether its original exit predicate persists. No same-bar exit-and-reentry; after successful exit, a fresh later cross-under is necessary. Cooldown is otherwise zero. One order at a time, one position, no scaling, no re-entry while held.

**Explicitly disabled:** SHORT, leverage, margin, perpetual funding, BO/SO/DCA, pyramiding, partial position targets, multiple positions, shared multi-asset capital, stop-loss, take-profit limit order, trailing stop, discretionary close, intrabar high/low triggers, maker/limit/next-open fills, fixed-profit exit, end-of-sample forced liquidation, time-of-day exceptions, hidden controller risk defaults and compounding. The CMO>+50 close and the five-bar close are the only risk/exit legs; no protective stop is provided. If the sample ends LONG, value inventory only at an actual last valid close; do not invent a SELL.

**Failure:** If the needed real daily price is absent, the candle is malformed, or the required indicator is undefined after warmup, stop and mark the entire research run data-incomplete. Never continue through missing bars, fabricate a price/fill, or silently reset position state.

## Required data

Single Binance spot BTC-USDT 1d UTC OHLCV, including true exchange **opening** timestamps and the actual close. CMO uses close only; OHLCV validity checking prevents accepting malformed feed rows. No funding, mark price, futures basis, order book, external service, cross-asset alignment, lower timeframe, higher timeframe, ML model or forward-looking label. 30 consecutive completed bars precede eligibility.

## Execution assumptions

**Pinned model inspected with connected GitHub on 2026-10-26:** Hummingbot package **20260920**, VERSION **dev-2.17.0**, source commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. The source pin is taken from existing independently reviewed Alpha PR #414/#417 evidence; this run directly re-read the pinned Binance spot candles constants/parser, backtesting engine, order executor simulator/config and backtesting data provider. The package-to-source wheel digest was **not** rehashed this run, so no fresh package byte-identity assertion is made.

**Verified bounded path:** BinanceSpotCandles constants include **1d**; Binance REST candle row[0] is the candle **open** timestamp and row[1..5] are OHLCV. BacktestingEngineBase.run_backtesting initializes the historical feed and controller, and simulate_execution iterates processed rows, calls update_state, then determine_executor_actions, then simulate_executor. OrderExecutorConfig supports connector_name="binance", trading_pair="BTC-USDT", side BUY or SELL, amount=Decimal("0.001"), position_action OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1. The pinned OrderExecutorSimulator MARKET path takes the first supplied row, fills its actual **close**, records filled_amount_quote = amount*close and cum_fees_quote = trade_cost*notional, and returns POSITION_HOLD. BacktestPositionHold nets opposite-side base fills, maintains weighted average cost and separately aggregates quote fees; it does not automatically make gross realized PnL net of fees.

**Causality qualification:** Raw historical row timestamp is **open**, even though the simulator sees that row's close. The only claimed valid model is a **completed-close historical research convention**, whose economic decision/fill time is **open+86400**, not the raw row timestamp. A future controller/Replay must prove that no open-time action or incomplete bar uses close[t]; labeling raw open-time engine events as real-time executable would FAIL Gate 5/6. This convention is idealized and does not imply a live market order can actually fill at the observed historical close. The controller is not yet implemented; its required causal gate and fill-confirmation behavior are specified here, not falsely reported as tested.

**Position/fee/cash:** The pinned simulator accepts explicit run_backtesting(trade_cost=0.001): **research-assumed 0.1% quote notional fee per fully filled side**, not a verified actual Binance fee schedule and not EdgeTools' documented fee. Start unborrowed cash 10,000 USDT; BUY cash -= Q*Pbuy*(1+0.001); SELL cash += Q*Psell*(1-0.001); net matched round-trip PnL = Q*(Psell-Pbuy)-0.001*Q*(Pbuy+Psell). Position cost and gross realized PnL are tracked separately from fees; mark open inventory at an observed close only. A single fixed Q=0.001 BTC order is the idealized full-fill research unit, not a claim that all real market/precision/min-notional constraints are met.

**Critical engine safeguards:** Specify terminated_executors_window=None or a persistent full-run fill ledger: the default one-hour terminated-executor view is insufficient for a five-day state machine. Update held quantity and entry-fill index from actual confirmed executor fills, not merely CreateExecutorAction. The backtesting data provider's get_price_by_type can return Decimal("1") when a requested price is missing: that fallback is explicitly **prohibited**, and missing actual prices abort the run. prepare_market_data can drop NaNs, so validate all contiguous input rows before the engine rather than allowing missing bars to vanish.

**Economic limits:** MARKET simulator assumes immediate full fills at historical close, with no separately modeled slippage/spread/latency/partial fills; zero simulator slippage is **not** a claim of zero realized slippage. Real fee tier, order-size/precision/min-notional constraints and live fills remain unverified. Spot funding is **not applicable** (never modeled as zero perpetual funding). No futures margin, maker fill, intrabar or next-open capability is claimed. A future execution path that requires one of these unverified primitives is not covered by this PASS proposal.

## Evidence

### Source-reported

EdgeTools, TradingView script nFffJSl1, **2024-10-17**, directly describes nine days as a common CMO period, oversold LONG below -50, overbought exit above +50, and an alternative five-day post-buy timeout. It gives no reliable Pine source revision bytes or audited historical performance; source backtest claims remain unverified.

### Independently reproduced

**No performance or event-level reproduction.** This Scout re-read the named pinned GitHub engine source paths to check bounded spot 1d OHLCV, completed-close MARKET simulation, fee application and POSITION_HOLD accounting. No TradingView Pine vs derivative replay, Qlib/Hummingbot run, wheel digest rehash, actual order execution, survivor assessment, Paper/Testnet/Live or profit/Sharpe result was performed.

### Negative evidence

The source's precise Pine version/defaults, exact crossing/state behavior, order placement, time-exit counting, fills and risk behavior cannot be verified from the readable page. All these choices are openly **researcher-defined** and must not be silently attributed to the source. The main pool's existing burgercrisis CMO9 +/-80 two-sided reversal is a different source and different mechanism; no exact source-ID or materially identical nine-day cross-under -50 plus five-day timeout was found on current main or open research/* PRs. README/root count 337/337 is bookkeeping agreement only, not a claim that every existing PASS frontmatter was individually re-audited.

**Six-gate pre-admission evidence (proposal, independent Auditor decides):** (1) CMO formula, nine-delta window, thresholds, equality, seed, warmup and priority pinned; (2) Binance spot LONG/FLAT with SHORT disabled; (3) two exits and every other risk behavior explicit; (4) one confirmed 0.001 BTC position, no DCA, time-index, pending/failure/re-entry fully specified; (5) actual pinned 1d spot feed, controller/action/OrderExecutor MARKET/POSITION_HOLD and fee/price ledger inspected, with completed-close and real-economics limitations declared; (6) 30 completed bars, strictly backward-looking deltas, five future bars **waited for** rather than read early, no incomplete candle, no future-data leakage.

## Falsification plan

After independent PASS and separate downstream selection, test strict cross-under equality and repeated-oversold non-reentry, zero-denominator CMO, t+5 vs earlier +50 exit priority, rejected BUY, failed SELL retry, confirmed-fill index, warmup boundary, daily UTC gaps and raw-open vs completed-close effective clock. Compare a representative Hummingbot event ledger against the Qlib research path before large-scale screening **if** the selected execution primitive/data path is new or unverified; reuse existing verified primitives without inventing candidate-by-candidate admission gates. Assess net-of-assumed-fee IS/OOS separately from admission.

## Crypto portability

This is only the independently frozen Binance BTC-USDT **spot 1d** derivative. Single-pair, 1d, OHLCV and completed-close are choices, not policy admission whitelists. Seven-coin 1h/4h/1d, 3x/5x futures, and BO/SO 6/6/6 are optional **downstream** campaigns; changing market, leverage, funding, DCA or fill semantics would require a separately disclosed research execution variant, not a claim of source-native equivalence.

## Limitations

No Pine revision bytes/hash, native parity, verified original defaults, live-close fill, slippage, real fees, precise exchange min-notional or package wheel digest this cycle. A missing protective stop can produce severe losses. A dedicated strategy controller and a causality-preserving Replay have not been implemented. If the later engine/controller cannot preserve completed-close timing, confirmed fill state or cost accounting, the candidate must be held for engineering remediation; it cannot be treated as a proven executable implementation. HB_READY PASS here is a **Scout proposal** for independent review, not self-certification of performance, Qlib parity or live readiness.

## Implementation status

**not-implemented.** No strategy-specific controller, Qlib executable recipe, test, run, deploy or trading action was created. This record documents a bounded candidate expressible in the inspected pinned research model; later executable materialization is a separate engineering step, not an additional HB_READY admission field.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head six-gate PASS merge or NOT_LOSSLESS close. Scout never approves, merges, closes, edits README or runs trading/backtests.

## Related Wiki records

None asserted; no Wiki edit.

## Sources

- Primary: EdgeTools, *Chande Momentum Oscillator Strategy*, published **2024-10-17**, TradingView stable ID nFffJSl1: https://www.tradingview.com/script/nFffJSl1/
- Pinned Hummingbot source (directly inspected paths above): https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Existing independent package/source-path audit evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
- Closest distinct CMO record: https://github.com/HCH725/alpha-strategy-research/blob/cbd906d33b0d4455a28d3a928b23c669225195a2/chande-momentum-80-cross-reversal-two-sided-btcusdt-1d-2026-10-10.md
