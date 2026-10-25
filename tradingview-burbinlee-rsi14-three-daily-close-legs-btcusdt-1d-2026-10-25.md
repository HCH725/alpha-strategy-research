---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "BurbinLee RSI14 oversold-cross three-consecutive-daily-close DCA, BTCUSDT spot 1d — independently derived"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2025-09-14
sources:
  - https://www.tradingview.com/script/LS6Jsy63-RSI-DCA-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BurbinLee RSI14 oversold-cross, three daily close-fill legs — independent BTC-USDT spot research derivative

**Frozen strategy identity:** `TV-LS6Jsy63 | BurbinLee | 2025-09-14 | derived-rsi14-three-daily-close-legs-tp4-sl3 | BTC-USDT-binance-spot-1d | v1 | 2026-10-25`. This is one bounded, **independently specified derivative**, NOT an assertion of source-native Pine/TradingView broker-emulator equivalence, profit, Qlib parity or trading permission.

## Provenance

Primary public TradingView page: [RSI DCA Strategy](https://www.tradingview.com/script/LS6Jsy63-RSI-DCA-Strategy/) by **BurbinLee**, published **2025-09-14**, inspected **2026-10-25**. The page labels the script open-source, but the public text rendered to this researcher did **not** expose the executable Pine source or a source-code version identifier. Script ID `LS6Jsy63`, author, title, date and source-described mechanism are the stable provenance; do not pretend the unavailable Pine bytes were verified.

**Source-native statements actually visible:** RSI crosses below 30 to trigger oversold; up to three consecutive daily entries, one per day, dividing user-configured capital equally; TP/SL as user-configurable percentages of **average entry price**; exit on TP or SL. The optional monthly performance table is visualization, not a decision input.

**Researcher-defined changes (NOT attributed to BurbinLee):** RSI length 14 and exact Wilder initialization; UTC Binance BTC-USDT spot daily bars; a strict completed-bar RSI cross; trigger-day + next two daily **close** MARKET buys; **fixed 0.001 BTC per leg** rather than the source-described equal quote-capital slices; TP +4% / SL -3% checked only at completed **daily close** instead of unverified intrabar broker stops; exit-before-add priority, early-exit cancellation of remaining legs, deterministic gap handling, 10,000 USDT nonborrowed initial cash, modeled 0.1% fee per side, and all state/cooldown/disabled rules below. These changes alter possible trade events and cost; this version is **not** lossless. No author performance numbers are used.

## Economic mechanism

### Source-reported

An oversold RSI crossing begins a bounded, daily staggered accumulation, with mean-reversion exit barriers tied to the average paid price. This is a mechanism hypothesis, not evidence of a profitable edge.

### Research interpretation

A close-confirmed RSI14 oversold cross initiates at most three fixed-base purchases on successive completed daily candles. The position exits in full at the first later completed close at least 4% above, or at least 3% below, its **current pre-decision weighted average entry**. No price-path-dependent intrabar fill is claimed.

## Signal

All arithmetic uses only finite, strictly valid **completed** Binance spot BTC-USDT `1d` OHLCV. Bar index `t` is UTC daily-open timestamp `T[t]`, with effective decision and research fill time `T[t]+86400` seconds. Inputs are not visible as complete before that time.

**RSI14 exact calculation:** `delta[t]=C[t]-C[t-1]`; `gain=max(delta,0)`; `loss=max(-delta,0)`. At `t=14`, seed `avgGain` and `avgLoss` with arithmetic means of the first 14 deltas. Thereafter Wilder RMA: `avgGain[t]=(13*avgGain[t-1]+gain[t])/14`, likewise loss. `RSI=100-100/(1+avgGain/avgLoss)`; if loss=0 and gain>0, RSI=100; if gain=0 and loss>0, RSI=0; if both=0, RSI=50. No EMA-seed or alternate TA-library behavior silently substituted. RSI first defined at `t=14`; the first eligible cross is `t=15` (16 valid closes).

**Fresh entry trigger while FLAT:** `RSI[t] < 30 AND RSI[t-1] >= 30`. Strict current comparison; equality on previous RSI is allowed. No trigger if either RSI undefined. There is no trend, volume, ML, external data or multi-timeframe filter.

**Frozen position and exit machine:**

1. Start FLAT, `cash=10000 USDT`, `heldBTC=0`, `legs=0`, `firstEntryIndex=null`. Each buy leg requests exactly `Q=Decimal("0.001") BTC` at that day's modeled MARKET close, with fee `0.001*Q*C[t]` USDT. If `cash < Q*C[t]*(1+0.001)`, skip that buy **permanently for that scheduled slot**, without negative cash or a synthetic fill. A skipped first buy consumes that trigger and remains FLAT until a **fresh later RSI cross**.
2. If FLAT and trigger true and affordable, issue exactly one BUY on `t`, mark LONG immediately after the simulator's modeled fill, set `legs=1` and `firstEntryIndex=t`. Do not evaluate exit on the same entry bar.
3. On every **later** valid completed bar while LONG, calculate the pre-action volume-weighted average price `A=(sum filled BUY Q_i*C_i)/(sum filled BUY Q_i)` from **actual simulated fills**. If `C[t] >= 1.04*A`, SELL **all** actually held BTC at `C[t]` and cancel remaining scheduled buys. Else if `C[t] <= 0.97*A`, SELL all and cancel remaining buys. The two barriers cannot both hold for positive A. The check is **before** any possible new buy, so there is no same-bar add-and-exit ambiguity.
4. Only if no exit: if `t==firstEntryIndex+1` or `t==firstEntryIndex+2`, and `legs<3`, attempt one additional `Q=0.001 BTC` MARKET buy at `C[t]`, subject to cash; skipped slot never retries. Do not open a new independent position. On other bars hold. There are **at most three** buys on exactly the trigger day and next two UTC daily bars, max `0.003 BTC`.
5. After a full SELL, reset FLAT, all DCA scheduling and average-price state. **No same-bar re-entry**. Starting on the next bar, a **new** strict RSI cross can trigger another cycle; no additional cooldown. RSI signals while LONG are ignored, not queued.
6. No forced exit on final historical bar; mark held BTC at last valid close, with paid fees reflected in cash. No unearned hypothetical final sell or fee. At most one open aggregate long position. Shorting, leverage, borrowing, compounding, unrelated pairs, hedging, grid, trailing, time exits, liquidation, intrabar stop/target, maker orders and additional safety orders are **disabled**. The only protective exit is the declared close-checked -3% threshold; a gap can overshoot it.

**Single-action priority per bar:** if LONG, TP/SL exit > scheduled add > hold; if FLAT, fresh entry > hold. Exactly one BUY or SELL executor action at most per daily candle. The RSI cross does not reset an already active three-leg schedule.

## Required data

Binance `binance` connector, `BTC-USDT` **spot**, UTC `1d` OHLCV. No perpetual marks, funding, order-book, non-OHLCV inputs, shared portfolio capital or cross-asset synchronization. Require finite O/H/L/C/V; O/H/L/C strictly positive, `H>=max(O,C)>=min(O,C)>=L`, volume nonnegative, unique increasing daily-open UTC timestamps exactly 86400 seconds apart, and no incomplete most recent daily candle. **Reject the whole proposed run on any missing/duplicate/malformed bar or gap** before feature generation or `dropna`; do not fabricate a close, bridge a gap or compress the DCA schedule to the next available day. RSI warmup needs 16 consecutive closes before the first trigger. Historical feed and fee-tier realism are not claimed.

## Execution assumptions

**Pinned engine identity:** Hummingbot policy package `20260920`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION=dev-2.17.0`. GitHub read-only inspection on 2026-10-25 confirmed the immutable commit and the actual source paths below. The separate package/wheel-to-source byte mapping was previously independently reviewed in accepted [Alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414) (902/902 Python files, reported wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`); **this Scout did not rehash an installed package**.

**Actual data/controller route:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly maps `1d`; `binance_spot_candles.py::_parse_rest_candles` parses REST kline `row[0]` open-time and `row[1..5]` OHLCV. `BacktestingEngineBase.prepare_market_data` exposes `timestamp_bt` and `open_bt/high_bt/low_bt/close_bt/volume_bt` and unsuffixed OHLCV, with a `merge_asof`/`dropna` path that **does not itself guarantee causality or gap detection**. A dedicated strategy-specific controller must validate the original series first and compute the above exact RSI/state. `simulate_execution` iterates rows, invokes `update_state(row)` then `controller.determine_executor_actions()`; `CreateExecutorAction` dispatches through `simulate_executor` to `OrderExecutorSimulator`. This is a verified *path*, not a claim that the RSI-DCA controller already exists.

**Real fill and DCA cost/position path:** each leg uses `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001") for each BUY or the actually held base amount for SELL,execution_strategy=MARKET,price=None,leverage=1)`, with an explicit unique executor ID and no simultaneous actions. The pinned `order_executor_simulator.py` MARKET branch fills at the **first processed row's close**, computes `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates as `POSITION_HOLD`. `BacktestingEngineBase._update_positions_from_stopped_executors` routes these fills into `BacktestPositionHold.add_executor`; its `_process_order` **adds same-side BUY amounts at weighted average cost**, then matches a reducing SELL to realize gross PnL. Thus three independent daily MARKET BUY executors and one aggregate full SELL have a concrete pinned net-position/cost path; this is not merely an API or executor-name assertion. Controller must maintain **immediate post-fill** `cash/heldBTC/legs/average/scheduled days`, not wait for one-tick-delayed `positions_held` or a truncated terminated-executor view. Confirm fill quantity/price from the simulator; no synthetic partials.

**Timestamps:** native simulation indexes rows and fill events with Binance candle **open** timestamp, although the model uses that candle's **close**. For causal research reporting, normalize decision and fill event timestamps to `T[t]+86400`; never represent an open-label event as a trade known at that day's open. This same-close MARKET research convention is not an executable live after-close fill guarantee; no next-open, intrabar, resting order or slippage-path primitive is assumed.

**Cash, fees, funding and precision:** `trade_cost=0.001` (0.1% per executed side) is a frozen **research assumption**, not source-reported or an observed Binance fee. BUY cash outflow `Q*P*(1+0.001)`; SELL cash inflow `Q*P*(1-0.001)`; weighted average BUY cost excludes fees, which are recorded separately. Realized **net** round-trip quote PnL is `sum SELL quote - sum BUY quote - all BUY/SELL fees`; unrealized account equity is `cash + heldBTC*last_valid_close`, not native `BacktestPositionHold.realized_pnl_quote` alone (that is gross). Spot perpetual funding is **not applicable**, not a fabricated zero futures funding series. No additional slippage is applied **in this research model**, not a claim of zero real spread/impact. Engine full fills, fixed `0.001 BTC` amount and Decimal-ledger accounting are simulation boundaries; historical tick/step/min-notional, actual exchange fee tier, partial fills, market impact, live latency and order rejection are **not independently verified** and no exchange-realism claim is made. A later campaign with futures leverage or house 6/6/6 quote sizing is a separate disclosed experiment, not this admission.

**Reused capability:** previously independently reviewed [Alpha PR #417](https://github.com/HCH725/alpha-strategy-research/pull/417) and [#414](https://github.com/HCH725/alpha-strategy-research/pull/414) established the pinned 1d spot MARKET-close/position-hold/fee primitive. This candidate additionally relies on the **directly inspected** same-side weighted-cost `BacktestPositionHold._process_order` path for successive fills. No strategy-specific executable, backtest or parity run is claimed.

## Evidence

### Source-reported

The author's 2025-09-14 public description says RSI cross **below 30**, up to **three consecutive daily entries**, one per day, and TP/SL relative to **average entry price**. It does not expose to this researcher an RSI length, TP/SL default percentages, exact intrabar order semantics, first entry timing, actual fees or reproducible numerical performance. These are **not** silently attributed to the author.

### Independently reproduced

**Not independently reproduced.** This cycle inspected the public TradingView page and pinned Hummingbot source statically via GitHub. No TradingView strategy run, Qlib/Hummingbot backtest, sample trade reconstruction, profitability estimate, package rehash or Qlib/Hummingbot event parity test was performed.

### Negative evidence and deduplication

Pre-write `main` SHA `7dd10539173e10b8d73d19a8a8436cbf7e05d6b1` contained **322 root-level strategy Markdown records** (324 root `.md` files including the two READMEs); README advertised **322**. Count agreement is **not** asserted to be an exhaustive independent frontmatter audit. GitHub code search and all-state PR search for exact TradingView script ID `LS6Jsy63` found no matches; current open `research/*` PRs inspected carried other sources. A prior `TV-XuywwObg` RSI **volume ladder** PR has **volume surge + 1.5% price-spaced** additions and different exits/cooldown, not three **calendar-consecutive** buys from a single RSI cross. Existing `sonic-r-rsi-dual-leg` and `tradingview-edgetools-connors-rsi3-triple-drop` records also use materially different trigger and position machines. This is not a trivial parameter variant or a renamed copy.

## HB_READY six-gate evidence — researcher proposal, independent audit pending

1. **Deterministic signals:** Wilder RSI14 initialization, 30 strict cross, UTC 1d data, thresholds, three fixed scheduled indices, average-price recalculation, exit/add priority, validity and warmup are specified; all non-source choices disclosed as derived.
2. **Direction:** spot BTC-USDT LONG/FLAT only; SELL closes held long, no short or margin.
3. **Entries/exits/risk:** entry cross, up to two later scheduled adds, close-only +4% TP/-3% SL, cancellation and all disabled risk/other exit behavior explicit.
4. **Position/state:** at most three 0.001 BTC legs, one aggregate net position, immediate cash and weighted cost, one action per bar, no queued signals, no same-bar reentry, zero later cooldown and explicit skipped-slot handling.
5. **Pinned-engine compatibility:** actual Binance spot 1d candle parser, per-row controller action dispatch, MARKET-close full-fill `OrderExecutorSimulator`, same-side weighted `BacktestPositionHold`, two-sided fees, open-label timestamp normalization and no-funding spot boundary inspected. No new unverified intrabar or next-open primitive assumed.
6. **Point-in-time:** RSI only from 16+ completed contiguous daily closes, decisions at close-time, schedule based on fixed day indices, exit check before new add, fail closed on gaps; no future bar, repaint, partial higher-timeframe bar or missing-price substitution.

## Falsification plan

After **independent admission and separate downstream selection only**, freeze this exact v1 and compare three scheduled daily buys versus the same RSI14 trigger with only the first buy, on identical predeclared contiguous IS/OOS windows and the same fees. Measure how often early TP/SL cancels additions, net return, Sharpe, MDD, and fee sensitivity; never assert these were already tested. Representative event-level Qlib/Hummingbot parity must precede mass screening if the three-leg execution/cost path has not already been validated as a comparable primitive. OOS must not be fed back into optimization.

## Crypto portability

The author's source does not establish BTC-USDT results. This independent research version fixes Binance BTC-USDT spot `1d`. Other pairs, intraday schedules, futures funding/margin, variable quote-sized orders and BO/SO 6/6/6 are separately declared derivatives or downstream experiments, not HB_READY admission prerequisites.

## Limitations

Original Pine bytes/version unavailable; no source-native broker timing or economic equivalence. Same-completed-close research fills can be optimistic for live execution. Price gaps can exceed the -3% close stop. Fee, precision, latency, liquidity, spread, exchange rejection and slippage realism remain unverified. Package-source identity relies on existing independent audit, not a fresh wheel hash. No claim of profitability, Survivor, HB certification, Qlib parity or live safety. `hb_ready_status: PASS` is **a proposed six-gate eligibility record**, pending independent Hermes Auditor verification at exact PR head, not Scout self-approval.

## Implementation status

`not-implemented`: no RSI-DCA controller, Qlib executable recipe, exchange adapter, deployment or backtest artifact created. After independently accepted research admission, a separately selected downstream experiment may require minimal strategy-specific implementation; no new admission flag or registry.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns exact-head six-gate review, source-fact remediation, PASS merge or NOT_LOSSLESS close. Scout does not approve, merge, alter README, trade, backtest, deploy or change cron.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/LS6Jsy63-RSI-DCA-Strategy/ — BurbinLee, *RSI DCA Strategy*, public open-source listing, 2025-09-14, inspected 2026-10-25.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned Hummingbot source; `binance_spot_candles`, `backtesting_engine_base.py`, `order_executor_simulator.py`, `order_executor/data_types.py`, `validation.py` inspected 2026-10-25.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent package/source identity evidence and 1d spot primitive.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — prior independently reviewed 1d spot MARKET-close/position-hold execution primitive.
