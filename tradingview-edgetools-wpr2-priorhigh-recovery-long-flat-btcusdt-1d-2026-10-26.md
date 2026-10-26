---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: EdgeTools Williams %R2 extreme-oversold hold with prior-high or %R recovery exit, independent BTC-USDT spot 1d long-flat derivative
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
source_as_of: 2024-10-15
sources:
  - https://www.tradingview.com/script/WgrZZgCZ/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EdgeTools Williams %R2 oversold hold with prior-high / oscillator recovery exit — independent BTC-USDT spot 1d derivative

## Provenance

**Primary TradingView publication:** EdgeTools, *Williams %R Strategy*, published **2024-10-15**, public/open-source strategy listing, stable script ID **WgrZZgCZ**, directly inspected **2026-10-26**: https://www.tradingview.com/script/WgrZZgCZ/ . The accessible first-party page describes an SPY mean-reversion LONG when Williams %R falls **below -90**, and an exit when **current close > previous day's high OR Williams %R > -30**. It says the oscillator's high/low lookback can be adjusted from **2 to 25 days** and mentions 2 days as a favorable shorter setting. These are **author-described facts**, not a verified Pine-default configuration. The complete Pine source bytes/version and executable TradingView order settings were not retrieved. The page's profit-factor claim has no independently reproduced tester trace here and is not adopted as performance evidence.

**Independent derived strategy — NOT source-native or lossless Pine:** Researcher choices are: Binance **BTC-USDT spot** UTC **1d** rather than the author's SPY market; **Williams %R length 2** chosen from the author's disclosed lookback domain (not asserted as a Pine default); strict level comparisons and a defined zero-range failure; **completed-bar close-effective MARKET** historical simulation (the source Pine's exact fill convention is unverified); fixed **0.001 BTC**, 10,000 USDT unborrowed initial cash, hypothetical **0.1% per-side** fees, 60-bar warmup, exit-first/no-same-bar-reentry, explicit pending-fill/failure state, and no stop/DCA/short/other exit. These choices can change source trades, are not claimed to be EdgeTools' native implementation, and are evaluated only as this independently specified executable research strategy.

**Immutable identity:** `TV:WgrZZgCZ:EdgeTools:2024-10-15 | independent-derived-v1:2026-10-26 | WPR2-highlow-close:level<-90 ENTER | close>prior-high OR WPR>-30 EXIT | BinanceSpot:BTC-USDT:UTC1d:LONG-FLAT:0.001BTC | completed-close-MARKET:trade_cost=0.001`. Any change in lookback, predicates, priority, market, clock, size, cost, state, or fill model is a different research version.

**Deduplication on main SHA `102b7a186ba219fe10d265781ff075eef4e89313`:** Current main has **354** root-level strategy Markdown records and README pool count **354** (count agreement alone does not certify all historical frontmatters). GitHub main code search and PR search for **WgrZZgCZ** returned **zero**; all **10** currently open `research/*` PRs were inspected at title/source-summary level and none cites this source or its dual exit. Closest main mechanisms are (a) Julien_Exe `williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md`, **14-bar cross-up -80 entry / cross-down -20 exit**, no prior-high exit; (b) EdgeTools Ultimate Oscillator `ultimate-oscillator-oversold-breakout-long-btcusdt-1d-2026-10-10.md`, **weighted 6/14/20 buying-pressure ratio <30** entry with prior-high-only exit; (c) Forven Williams %R/EMA recovery and Williams %R/ADX-gated rules, which use trend filters and different recovery exits. This candidate instead buys **persistent %R2 below -90** and exits on **either** one-bar price recovery above the preceding high **or** %R2 above -30. This is a different oscillator construction, entry-state type, and dual-exit event mechanism, not a trivial threshold-only variant. No duplicate source or materially identical normalized rule was identified.

## Economic mechanism

**Source-reported hypothesis:** an extreme Williams %R reading indicates short-term exhaustion; a later close above yesterday's high or oscillator recovery above -30 signals that the rebound has matured. The author's original SPY framing and claimed results are not transferred to BTC or reproduced.

**Derived research hypothesis (unverified):** on a two-day high/low window, a BTC close near the bottom of its observed range may revert quickly. The prior-day-high close test is a direct price-action recovery exit; the -30 oscillator level is an alternative exhaustion-reversal exit. Repeated low readings do **not** pyramid, and no protective stop is present.

## Signal

**Market/data clock:** exactly one actual Binance spot `BTC-USDT` UTC **1d** OHLCV stream. Each exchange opening timestamp `T[t]` labels a daily bar whose data become available only at **T[t]+86400 seconds**. Require consecutive opening timestamps separated by 86400 seconds; O/H/L/C finite and positive, H>=max(O,C), L<=min(O,C), V finite and nonnegative. No incomplete bar, forward-fill, future bar, or synthetic price is accepted.

**Frozen arithmetic:** for t>=1, `HH2[t]=max(H[t-1],H[t])`, `LL2[t]=min(L[t-1],L[t])`, `WPR2[t]=-100*(HH2[t]-C[t])/(HH2[t]-LL2[t])`. If `HH2==LL2`, WPR is undefined and the run is data-incomplete; never replace it with 0 or an old value. No smoothing, indicator normalization, ML, future pivots, or other filters. `ENTRY[t] = WPR2[t] < -90` (a **level**, not a crossover). `EXIT_PRICE[t] = C[t] > H[t-1]`; `EXIT_OSC[t] = WPR2[t] > -30`. All three comparisons are **strict**: equality never triggers. Exit = EXIT_PRICE OR EXIT_OSC. `H[t-1]` is yesterday's **observed high**, never today's high.

**Warmup:** require **60 consecutive fully completed valid UTC daily bars**, counting the first input as bar 0, before the first eligible decision. The structural minimum is two bars, but 60 is a declared researcher warmup choice. Begin with 10,000 USDT, zero BTC, FLAT, no pending order, and no pre-warmup inferred position. First eligible t is 59 if its 60-bar history is complete and WPR is defined.

**Deterministic per-completed-bar order/state machine:**
1. At most one outstanding order. Reconcile any prior simulated executor's actual confirmed fill/failed status before evaluating new actions; creating an order alone never changes the confirmed position. No trade decision before the bar's completion time.
2. If confirmed LONG and a SELL retry is outstanding after a failed previous exit, issue exactly one new SELL of the confirmed held quantity on the **next valid completed bar**; do not require the original exit predicate to persist. If LONG with no retry and either exit condition holds, issue one SELL for the full confirmed BTC position. If both exit legs hold, log EXIT_PRICE as primary and EXIT_OSC as simultaneous secondary, but send only one SELL. Ignore entry on every exit bar.
3. If confirmed FLAT and no SELL occurred this bar, if ENTRY is true and the available quote cash covers `0.001*C[t]*(1+0.001)`, issue one BUY for 0.001 BTC; otherwise stay FLAT. This is a **level-hold** entry: after a failed BUY, re-evaluate the same level on the next valid bar without a hidden cooldown; no intra-bar retries.
4. An idealized full confirmed BUY fill sets LONG and deducts cash; a rejected/failed BUY leaves FLAT. An idealized full confirmed SELL sets FLAT and credits net cash; a rejected/failed SELL leaves LONG and sets the next-bar retry flag. Partial or indeterminate fills are outside the verified bounded model and **abort as unsupported**, never silently assume full size or fabricate a price. There is no same-bar exit-and-reentry; a new BUY is eligible only on a later completed bar if still oversold. A confirmed LONG ignores further entry signals.
5. If neither action is due, HOLD. No discretionary/manual action. On the final available bar, mark any still-open LONG at the **last observed valid close** for research valuation; do not invent a terminal SELL.

**Explicitly disabled:** SHORT, perpetual/futures, leverage, margin/borrowing, funding, BO/SO/DCA, pyramiding, averaging, partial targets, simultaneous positions, cross-asset/shared-capital decisions, stop-loss, take-profit limit, trailing stop, time exit, maker/limit/next-open/intrabar orders, dynamic sizing, compounding, session filter, hidden controller risk defaults, and forced end-of-data liquidation. The two described close exits are the only risk exits. Missing a protective stop is a material loss risk, not an implicit engine default.

**Data failure:** a missing, duplicate, invalid, nonconsecutive or undefined required bar after warmup invalidates the entire research run. Abort; do not let an engine `dropna` erase a gap, fall back to a constant price, or assume a fill.

## Required data

Single real Binance BTC-USDT **spot UTC 1d** OHLCV with exchange **open timestamps** and actual O/H/L/C/V; only the current completed and previous completed candle are used in the signal. No lower/multi-timeframe alignment, cross-market series, external fundamentals, order book, funding, mark price, fitted model, or future price is required. One market is a deliberate derivative scope, **not** a policy admission whitelist.

## Execution assumptions

**Pinned Hummingbot engine directly inspected via connected GitHub on 2026-10-26:** package `20260920`, VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Prior independent package/source mapping evidence is in Alpha PR #414/#417; this cycle did **not** rehash the package wheel and does not assert fresh binary identity.

**Actual bounded data and controller path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` maps `1d`; `binance_spot_candles.py::_parse_rest_candles` maps exchange `row[0]` open timestamp and `row[1..5]` OHLCV. `strategy_v2/backtesting/backtesting_engine_base.py::run_backtesting` initializes feed/controller, then `simulate_execution` iterates processed rows, calls `update_state(row)`, `controller.determine_executor_actions()`, and `simulate_executor()`. `OrderExecutorConfig` in `strategy_v2/executors/order_executor/data_types.py` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=TradeType.BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A strategy-specific controller is **not implemented**; these are verified primitives, not a claim that this record is already wired into Hummingbot.

**Fill/position model directly verified:** `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET path uses the first supplied historical row's actual `close` as full-fill price; `filled_amount_quote = amount*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. `BacktestPositionHold` in `backtesting_engine_base.py` nets opposing BUY/SELL base fills, tracks weighted average cost, gross realized/unrealized PnL, and fees **separately**. A MARKET SELL reduces the same BTC spot inventory; no short inventory is opened. The engine's raw candle timestamp is the **opening label**, so the economic decision and simulated fill must be recorded as **opening timestamp+86400**, not as an open-time executable trade. This is an idealized **historical completed-close** convention only; real post-close market orders cannot be assumed to fill at that past close.

**Cash and costs:** pass explicit `run_backtesting(trade_cost=0.001)`, a hypothetical **0.1% quote-notional fee per side**; this is not a measured Binance fee schedule or an EdgeTools source parameter. Maintain independent unborrowed cash `cash_after_buy=cash_before-Q*Pbuy*(1+0.001)` and `cash_after_sell=cash_before+Q*Psell*(1-0.001)`, Q=0.001 BTC, and require sufficient cash before BUY. Net realized matched PnL `Q*(Psell-Pbuy)-0.001*Q*(Pbuy+Psell)`; do not mistake gross `BacktestPositionHold.realized_pnl_quote` for net-of-fee performance. Real exchange fee tier, quantity/price precision, min notional, slippage, spread, latency, and partial fills remain **unverified** and are not simulated as realized zero costs. Spot funding is **not applicable**; do not label zero perpetual funding as observed. No futures leverage/margin claim is made.

**Required engine safeguards:** `BacktestingEngineBase` exposes terminated executors to controllers for only **3600 simulated seconds** by default; use `terminated_executors_window=None` or an equivalent full-run confirmed-fill ledger so multi-day fill state is not lost. `prepare_market_data` calls `dropna`, so continuity/validity must be checked before entering the engine. `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` when a price is missing; **prohibit this path** for strategy fills and abort on missing observed prices. No unverified maker, next-open, intrabar, perpetual or real-time fill path is claimed.

## Evidence

### Source-reported
The first-party EdgeTools TradingView page dated **2024-10-15** states Williams %R below -90 LONG, and current close above the prior day's high **OR** Williams %R above -30 EXIT, with a 2–25-day adjustable range and 2 days highlighted as a short setting. It does not establish the inaccessible Pine defaults, order timestamps, fee schedule, position size, or native source trade history.

### Independently reproduced
**No original-Pine trade reproduction, Qlib/Hummingbot backtest, event-level parity, return, Sharpe, or survivor claim.** This cycle verified the listed pinned Hummingbot source files and existing research-only MARKET/POSITION_HOLD/fee primitives; no runtime test, wheel rehash, trade, Paper/Testnet/Live or deployment was performed.

### Negative evidence and six-gate matrix
1. **Gate 1 — deterministic:** 2-bar highest/lowest WPR formula, no smoothing, strict -90/-30/previous-high comparisons, zero-range rule, 60-bar warmup and state priority fully frozen. Length 2 and comparison details are explicitly derived, not source-native Pine defaults.
2. **Gate 2 — direction:** spot LONG/FLAT, no short or leverage.
3. **Gate 3 — entry/exit/risk:** level<-90 BUY; close>prior-high OR WPR>-30 SELL; all stops/targets/trailing/time exits and risk defaults explicitly disabled.
4. **Gate 4 — position:** 0.001 BTC one position, no DCA/pyramiding, cash check, confirmed-fill transitions, failed-order handling, no same-bar reentry and no cooldown pinned.
5. **Gate 5 — pinned-engine:** real pinned spot 1d feed/parser, controller action order, MARKET full-close fill, POSITION_HOLD cost ledger, explicit 0.001 hypothetical fee and cash accounting checked. Scope excludes unverified live/slippage/funding/margin/partial fills and forbids missing-price fallbacks.
6. **Gate 6 — causal:** t/t-1 completed candles only; daily open label is not decision time; effective decisions/fills at T+86400; warmup, continuity and no-future-data constraints explicit.

**Known limitations:** complete original Pine source revision unavailable; original SPY trade equivalence is **not** claimed. All researcher modifications are disclosed. A future controller must actually preserve the specified completed-close timestamp and confirmed-fill semantics; no currently deployed strategy implementation is claimed. An independent Auditor may reject if the pinned model cannot express any material requirement.

## Falsification plan

After independent admission and downstream selection, test equality at -90/-30 and prior high, two-bar zero-range, consecutive oversold no-pyramiding, simultaneous exit priority, failed BUY/SELL and next-day retry, confirmed fill vs order intent, missing UTC day, initial warmup boundary, raw-open vs completed-close clock, cash insufficiency and fee separation. If the execution primitive/path proves new or unverified, perform one representative Hummingbot/Qlib event-level comparison **before** large-scale screening; otherwise reuse verified primitives. Test IS/OOS net-of-declared-cost profitability separately from HB_READY.

## Crypto portability

Only the declared independent **BTC-USDT spot 1d** version is assessed. SPY session/gap behavior, equities corporate actions, seven-coin 1h/4h/1d and 3x/5x futures/DCA campaign assumptions are **not** imported. Any leverage, funding, market, timeframe, DCA, or execution change requires a separately declared derived research identity; no blanket admission bans are inferred from these choices.

## Limitations

Research-only, no executable controller, no Pine byte hash, no source-native trade equivalence, no verified realized market fee/slippage, no partial-fill or live-price guarantee, no independently reproduced performance, no Qlib parity. A no-stop strategy can suffer large losses. The historical same-close fill is a pinned **simulation convention**, not proof of real tradability. HB_READY PASS is a **Scout admission proposal pending independent Hermes Auditor review**, not a self-certified deployment or profit claim.

## Implementation status

**not-implemented.** No strategy-specific executable, Qlib recipe, backtest, container action or trading action was created.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** The independent Hermes Auditor GitHub Webhook Review owns exact-head PASS merge, verifiable source-fact remediation or NOT_LOSSLESS close. Scout never approves, merges, closes, edits README or bypasses review.

## Related Wiki records

None asserted; no Wiki change.

## Sources

- EdgeTools, *Williams %R Strategy*, TradingView stable ID **WgrZZgCZ**, published **2024-10-15**: https://www.tradingview.com/script/WgrZZgCZ/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Independent package/source review evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
- Distinct main WPR cross family: https://github.com/HCH725/alpha-strategy-research/blob/102b7a186ba219fe10d265781ff075eef4e89313/williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md
- Distinct main EdgeTools Ultimate Oscillator: https://github.com/HCH725/alpha-strategy-research/blob/102b7a186ba219fe10d265781ff075eef4e89313/ultimate-oscillator-oversold-breakout-long-btcusdt-1d-2026-10-10.md
