---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade MultiRSI triple-RSI cross-timeframe spread long-flat on BTCUSDT 5m bars
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/MultiRSI.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade MultiRSI triple-RSI cross-timeframe spread — independently derived executable research rule

## Provenance and immutable identity

- Primary GitHub identity: repository `freqtrade/freqtrade-strategies` (open-source Freqtrade strategy collection); exact file path `user_data/strategies/berlinguyinca/MultiRSI.py`; class `MultiRSI(IStrategy)` (the only class in the file); pinned commit SHA `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`, verified as the repository HEAD via `git ls-remote` plus the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2326 bytes, 71 lines, SHA-256 `0bd453350bdf32db4355277d79a3c7268d166d043bab59e30403a1e97687aa06`, matching the GitHub blob (`sha 0ddcb5b6b7f7bf925d6b363d5a90fe446de64fd7`, size 2326 via the contents API at the pinned commit) — the entire file was retrieved and inspected end to end.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = {"0": 0.01}`; `stoploss = -0.05`; indicators are exactly `dataframe['sma5'] = ta.SMA(dataframe, timeperiod=5)`, `dataframe['sma200'] = ta.SMA(dataframe, timeperiod=200)`, `resample_to_interval(dataframe, 10)` / `resample_to_interval(dataframe, 8 * 5)` with `ta.RSI(..., timeperiod=14)` on the base frame and on both resampled frames, `resampled_merge` twice, then `dataframe.ffill(inplace=True)`; long entry is `(sma5 >= sma200) & (rsi < resample_40_rsi - 20)`; long exit is `(rsi > resample_10_rsi) & (rsi > resample_40_rsi)`. No short legs exist anywhere in the file. Header credits `author@: Gert Wohlgemuth`, `based on work from Creslin`.
- Full-file token census (verified by search over the 71 lines this cycle): 0 hyperopt parameter of any kind (`IntParameter`/`DecimalParameter`/`CategoricalParameter`/`BooleanParameter`/`RealParameter` — every trading literal is hardcoded, nothing is fitted or selected); 1 `INTERFACE_VERSION` (`3`); 0 `startup_candle_count`; 0 `process_only_new_candles`; 0 `can_short`; 0 `informative_pairs` (higher-timeframe data arrives via `resample_to_interval`/`resampled_merge`, never via an informative-pair subscription); 0 `position_adjustment` / 0 `leverage` / 0 `custom_stoploss` / 0 `custom_exit` / 0 `protections` / 0 `cooldown`; 0 `volume` (no volume read, not even a nonzero guard); 0 `open` / 0 `high` / 0 `low` (only `close` and the `date` clock enter any predicate); 0 `trailing_stop`; 0 `use_exit_signal` / 0 `exit_profit_only` (framework defaults untouched and unrelied-upon — this record pins its own state machine below); 0 `fee` / 0 `slippage` / 0 `funding` (no economics anywhere). No performance number of any kind ships anywhere.
- Licence and rights: the file ships no licence header line; the repository root ships a `LICENSE` file (35147 bytes at the pinned commit). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.
- **Not source-native / not a lossless Freqtrade reproduction.** The source pins the `5m` frame, the SMA5/SMA200 gate, the triple-RSI14 construction over `5m`/`10m`/`40m`, the `-20` spread entry and the dual-superiority exit — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule, and its `1%` ROI leg plus `-5%` stoploss assume an intrabar-capable execution engine this record does not claim.
- **All researcher-defined differences/choices, declared in advance:** (1) fix Binance BTCUSDT **spot** `5m` candles (the file names no market); (2) same-decision-bar **close-price MARKET fills** on completed bars, instead of claiming the source engine's next-open fill convention; (3) the file's entire risk block (`minimal_roi = {"0": 0.01}` and `stoploss = -0.05`) is explicitly disabled — the signal-exit leg is the sole position-ending path, so no profit-trigger or stop-trigger definition is required anywhere in this record; (4) fix one `0.001 BTC` base-size position, one-position-only, no DCA, no cooldown (the file ships no cooldown — explicitly none, not invented); (5) pin the SMA/RSI recurrences and the UTC-epoch HTF aggregation below exactly (no TA-Lib/pandas version is relied upon); (6) fix a 600-completed-bar warmup, a declared controller-memory state machine, and the cost/clock model below. No other source-native execution or cost equivalence is claimed.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold a long only while the fast average sits at or above the slow average and the base-frame RSI has collapsed at least 20 points beneath the 40-minute RSI (a washed-out dip inside an intact moving-average regime); exit when the base RSI reclaims superiority over both higher-timeframe RSIs. A flat `1%` ROI and a `-5%` stoploss backstop every position in the source file; neither is carried into this derivative (see above).

### Research interpretation

Research hypothesis only: a deep base-RSI discount to the higher-timeframe RSI inside an SMA-regime filter marks a micro washout rather than a regime break, and requiring the base RSI to beat both higher-timeframe RSIs on exit keeps the position through weak single-frame flickers. Unlike single-frame RSI-threshold records, no fixed RSI level ever appears — every comparison is RSI-against-RSI across frames. Unlike EMA/price-cross records, no price average is ever crossed; the SMA pair is a level gate, not an edge. Unlike trailing/ratchet records, this derivative carries no adaptive exit at all. No return, Sharpe, win-rate, drawdown, or other independently reproduced statistic is asserted.

## Signal — fully specified derived rule

Data are UTC Binance BTCUSDT spot `close` on **completed** `5m` candles. Only `close` enters any predicate. Let bar index `t` refer to the current completed candle. All comparisons are strict except the SMA gate, which admits equality exactly as coded.

```text
sma(N)[t]      = mean of close[t-N+1 .. t]                                   // N in {5, 200}
rsi14(S)[t]    = Wilder RSI(14) over series S ending at t:                    // exact TA-Lib ta.RSI recurrence
                 seed avgGain/avgLoss = mean one-bar gain/loss over first 14 changes;
                 avgGain[t] = (avgGain[t-1]*13 + max(close[t]-close[t-1],0))/14 (same for loss);
                 RSI = 100 - 100/(1 + avgGain/avgLoss); 100 if avgLoss == 0
htf_close(F)[t] = close of the last F-minute bar fully completed at/before     // F in {10, 40}
                 bar t's close; the still-forming F-minute bar never contributes.
                 F-minute bars are UTC-epoch aligned (10 = 2x5, 40 = 8x5), so every
                 10m/40m close coincides with a 5m close — no second feed, no partial bar.
rsi5[t]  = rsi14(5m closes)[t]
rsi10[t] = rsi14(htf_close(10) series)[t]
rsi40[t] = rsi14(htf_close(40) series)[t]
entry_edge[t] = (sma(5)[t] >= sma(200)[t]) and (rsi5[t] < rsi40[t] - 20)
exit_edge[t]  = (rsi5[t] > rsi10[t]) and (rsi5[t] > rsi40[t])
```

- HTF-merge note (exact-equivalence reduction, not an approximation): the source computes RSI on the resampled frames and forward-fills the merged columns, so at base bar `t` each informative value derives solely from HTF bars completed strictly before `t`'s close. The derived `htf_close(F)[t]` plus `rsi14` reproduces exactly that causal content without pinning any pandas/freqtrade library version. Leading-unavailable HTF values read as no-signal (fail-closed), matching the source's unfilled leading NaNs under `ffill`.
- Comment/code mismatch, fenced (source-verifiable, no rule change): the entry block carries the comment `# must be bearish`, but the coded gate is `sma5 >= sma200` (bullish alignment). Code governs; the comment is recorded here as a stale annotation, never as a second rule.
- State transitions are evaluated **once after the bar is complete**, using the state carried *into* the bar:
- `FLAT + entry_edge[t]` -> MARKET BUY exactly `0.001 BTC` at that completed bar's close, then `LONG` with entry bar `t`.
- `LONG + (t > entry_bar) + exit_edge[t]` -> MARKET SELL the entire recorded `0.001 BTC` at that bar's close, then `FLAT`.
- Otherwise hold the previous state. A held position never adds, even if a fresh entry edge prints (consecutive-bar entry repeats are rejected no-ops). The entry bar **cannot** be its own exit (additionally enforced by the `t > entry_bar` arm).
- Entry and exit predicates are evaluated against disjoint states (entry only from `FLAT`, exit only from `LONG`), so no same-bar conflict ordering is ever required even on a cofire bar.
- After an exit, a fresh qualifying entry edge on a later bar may enter immediately; no cooldown (the source ships none — explicitly none, not invented).
- All pre-warmup and pre-first-entry bars are FLAT. Missing/invalid candles cause **no signal and no fill**, not synthetic price or forced entry. On the final data bar, a remaining position is reported as open; no fabricated terminal liquidation.
- Direction is LONG/FLAT only; the file contains no short legs to disable. ROI ladder, stop loss, trailing stop, take profit, partial exits, stop/limit/maker orders, averaging, safety orders/DCA, and time-based exits are all **disabled by this derived specification**. No hidden executor defaults supply any of them.

## Required data, warmup, causality

- One market, one `5m` UTC candle feed: `close` only (trend construction, regime gate, and all three RSI legs). No `open`/`high`/`low`/`volume` reads, no L2, funding, cross-asset, mark/index, calendar events, or other non-OHLCV data are read by any signal. The `10m`/`40m` legs are deterministic UTC-epoch aggregations of the same `5m` closes (exact multiples `2x`/`8x`), not a second feed and never a partially formed bar.
- Derived warmup is **600 completed bars** and no trade before it: covers the SMA200 seed (200 bars), the base RSI14 seed (15 closes), and the 40-minute RSI seed (14 completed 40m bars = 560 `5m` bars) with margin. Pre-warmup bars are FLAT by record rule.
- Every signal on bar `t` depends solely on bars `<= t`, and every HTF input on HTF bars completed strictly before `t`'s close. A bar is only made available after its `5m` close; the close is never treated as known at that bar's open. No repainting, lookahead, negative shift, full-sample fitting, future pivot, or partial higher-timeframe candle.
- Equalities on a strict RSI leg fail; equality on the SMA gate passes (`>=`, pinned as coded).

## Execution assumptions — pinned Hummingbot capability evidence

**Pinned contract:** Hummingbot package `20260920`, `hummingbot/VERSION = dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The exact engine source paths below were established by the sibling-cycle read of this commit's object store (same pinned commit as the merged 2026-10-25 freqtrade derivative) and are cited as *code-level primitives*, not a strategy-specific live/testnet run:

1. **Data/venue:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `5m` in `INTERVALS`. `binance_spot_candles/binance_spot_candles.py` uses Binance spot klines, passes `interval` to REST (`"interval": self.interval`), parses `row[0]` as candle **open timestamp** and parses OHLC plus volume (`row[1..5]`). The research decision clock is explicitly **open_timestamp + 300 seconds**, the completed `5m` bar's effective availability time; raw Hummingbot candle timestamps remain open-time labels and must not be mistaken for close-time decisions.
2. **Fill:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `OrderExecutorSimulator.simulate`: `ExecutionStrategy.MARKET` fills at the first supplied row, uses that row's **close** as `entry_price`, records `filled_amount_quote = amount * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and terminates with `POSITION_HOLD`. The engine's raw `fill_timestamp` is the supplied row's **open-time label**; the declared causal event time for audit/parity is the separately normalized close-effective time `open_timestamp + 300`. Neither the engine's raw label nor a close-based fill is represented as an actual exchange execution timestamp. This is a **research backtest convention**, not a live guaranteed close fill.
3. **Controller and ledger:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` executes `update_state(row)` then `controller.determine_executor_actions()` (method pinned on `controller_base.py:465`), accepts `CreateExecutorAction` with `OrderExecutorConfig`, and uses `BacktestPositionHold` to net executed BUY/SELL base exposure and separately accumulate realized gross PnL and fees. The derived controller's own persistent `FLAT/LONG(entry_bar, Q)` state and fill ledger (not the engine's bounded terminated-executor view or a delayed `positions_held` snapshot) gate entries/exits. The 10m/40m aggregations and the three RSI recurrences are pure deterministic functions of the pinned `5m` closes computed inside that controller memory — they require no second feed, no shared capital, and no cross-market synchronization. A controller implementing exactly these transitions is **not yet implemented** and is a downstream engineering artifact, not a second HB_READY admission criterion.
4. **Cost/position model:** one `Q=0.001 BTC` BUY/SELL unit on Binance **spot**, no leverage/margin/liquidation/futures funding; funding is **not applicable**, not silently set to a fictitious realized zero-funding stream. Pinned backtest fee is `trade_cost=0.001` **per side**, applied to each simulated fill's quote notional; modeled slippage is `0.0` because this pinned MARKET simulator fills at its close input, **not** a claim of actual zero market slippage. Per completed trade, fee-adjusted research PnL is `realized_gross_quote - sum(cum_fees_quote)`; the executor `net_pnl_quote` alone is not accepted as fee-adjusted cash/equity. The simulator uses binary floats for amount*price, no verified exchange tick/lot rounding, so tiny float residues and real-world precision/slippage discrepancies are limitations, not hidden fills.
5. **Timing constraints:** no next-open, intrabar stop, maker queue, partial fill, shared capital, simultaneous multi-asset semantics, or incomplete-bar HTF reads are required by this derivative. The single-row MARKET-close primitive is reused, and the `5m` `+300s` normalization is mandatory before comparing event timestamps. No missing bar's close is invented; a missing `5m` bar blocks that bar's decision/fill.

These exact engine source paths and restrictions provide **static code-path compatibility evidence** for the defined derived rule. No Qlib/Hummingbot strategy backtest, runtime deployment, trade, or event-level Qlib/HB parity was performed in this Scout cycle. Independent Hermes Auditor must independently verify Gate 5 and all other gates against the pinned code before any merge. Representative engine-path parity remains required before screening if the path is not already validated; PASS is not profitability, Qlib materialization, Survivor, HB Certified or trading authorization.

## Six-gate HB_READY evidence for independent review

1. **Deterministic:** hardcoded literals only (zero hyperopt parameters); exact SMA/Wilder-RSI recurrences with seeds; UTC-epoch HTF aggregation with forming-bar exclusion; strict legs with explicit equality handling; state-gated transitions with entry-bar arm; all researcher choices pinned above.
2. **Direction:** BTCUSDT Binance spot LONG/FLAT only; the file contains no short legs at all.
3. **Entry/exit/risk:** entry on the completed spread-plus-regime bar, exit on the completed dual-superiority bar; source ROI/stop legs expressly disabled and enumerated, so no profit/stop-trigger definition is missing; terminal position handling explicit. No protective/partial/other exit exists in this derivative.
4. **State:** one fixed `0.001 BTC` unit, no adds/DCA, state-disjoint legs (no same-bar conflict possible), entry-bar arm, no cooldown beyond it, deterministic transitions.
5. **Engine:** exact Hummingbot package/version/commit, BinanceSpotCandles `5m` feed, in-controller deterministic HTF aggregation (exact multiples, boundary-coincident, no second feed), controller state, OrderExecutor MARKET-close fill, raw/open vs effective/close timestamps, spot accounting, fee/slippage/precision limitations and BacktestPositionHold netting identified by actual immutable code paths; no unverified specialized execution requirement is introduced.
6. **Causality:** 600 completed-bar warmup, point-in-time completed-bar evaluation, completed-HTF-bar-only merge, no future access, normalized event times and missing-bar fail-closed behavior.

## Evidence and negative evidence

**Primary-source reported:** `MultiRSI.py` at `f3340ce` (71 lines) expressly prints the `5m` frame, the SMA5/SMA200 pair, the triple RSI14 construction over `5m`/`10m`/`40m` with `resampled_merge` plus `ffill`, the `(sma5 >= sma200) & (rsi < resample_40_rsi - 20)` entry, the `(rsi > resample_10_rsi) & (rsi > resample_40_rsi)` exit, the `1%` ROI and `-5%` stoploss, and the Gert Wohlgemuth / Creslin credits. The file ships no market, no fill timing, no warmup, no sizing, and no performance number of any kind — this record claims no source-reported performance.

**Independently reproduced:** determinism-and-reachability check only (not a backtest, no PnL statistic): a dependency-free re-implementation of the pinned recurrences was executed this cycle over 700 live Binance BTCUSDT `5m` klines fetched over HTTPS — two full passes byte-identical (deterministic); with the 600-bar warmup, 100 eligible bars print 46 entry bars and 17 exit bars with 0 cofire bars (both legs reachable, no hidden unreachability). No win rate, expectancy, or profitability is claimed.

**Dedup (main HEAD `430e70b`, 393 records, 2026-10-28):** working-tree filename/content search for `MultiRSI` / `Creslin` returns only the sibling-fence prose of `freqtrade-technical-cmf-sign-state-long-flat-btcusdt-5m-2026-10-22.md` (different pinned file, different gates — never admitted here); search for `resample_40` / `resample_10` / informative-merge RSI returns zero strategy records. Closest pool records differ in mechanism class: `alorse-mtf-rsi14-ema900-long-flat-syntax-normalized-20261016.md` is single-frame despite its name (zero higher-timeframe calls) with an RSI30-level entry against an EMA900 regime anchor; `forven-ema-rsi-pullback-reclaim-long-flat-solusdt-1h-2026-10-17.md` gates a single-frame EMA pullback by fixed RSI thresholds; `tradingview-connorgeary150-rsi14-bb20-dip-midline-or-rsi50-exit-long-btcusdt-1d-2026-10-26.md` buys Bollinger dips with RSI exits; `freqtrade-crossema-28-48-stochrsi-threshold-long-flat-btcusdt-1h-2026-10-26.md` crosses two price EMAs with a StochRSI threshold; `freqtrade-cofibit-stochf-ema-rail-adx-gated-long-flat-btcusdt-5m-2026-10-21.md` combines Fast-Stoch, an EMA rail and an ADX gate — none conditions entries on a base-RSI versus higher-timeframe-RSI spread, and none exits on dual higher-timeframe RSI superiority. All currently open `research/*` PRs were inspected for the same source and mechanism (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant.

**Negative evidence:**

1. No hidden legs: 0 hyperopt parameters, 0 short legs, 0 trailing/custom-exit/protection/cooldown lines — the signal-exit arm plus the disabled risk block are the complete position-ending story by construction.
2. Reachability proven, not assumed: both predicates fire on live data (46/17 bars per 100 eligible), and cofire needs no ordering rule because legs are state-disjoint.
3. The `# must be bearish` comment contradicts the coded `>=` gate; code governs and the comment changes no event.
4. No volume read anywhere: thin-print bars still signal — disclosed, not smoothed.
5. Derivation boundary fenced: the only non-source-native behaviors are the BTCUSDT-spot market pin, same-bar-close fills, the disabled ROI/stop legs, the 600-bar warmup, and house sizing/costs — all predeclared above; every edge, input, default, and ordering is source-verbatim. This record is therefore never evidence that the original next-open full-risk source itself passes.
6. Retuning any frozen literal (SMA lengths, RSI length, the `-20` offset, `AND` versus `OR` on the exit, the frame, or the fill convention) would be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA5/SMA200 gate / RSI14 x3 / `-20` spread / dual-superiority exit / long-only single-unit / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Spread relevance: entering on the regime gate plus a fixed single-frame washout (`rsi5 < 30`, no higher-timeframe spread) with the same exit and pins must not improve net expectancy; fail ⇒ the cross-timeframe discount adds nothing over a plain oversold level.
- F2 — Regime-gate relevance: entering on the bare spread (`rsi5 < rsi40 - 20`) with the SMA gate removed (same exit, same pins) must not improve net expectancy; fail ⇒ the SMA5/SMA200 alignment adds nothing over the naked spread.
- F3 — Exit-conjunction relevance: exiting on either superiority (`rsi5 > rsi10` OR `rsi5 > rsi40`) instead of the coded conjunction (same entry, same pins) must not improve net expectancy; fail ⇒ requiring both higher-timeframe confirmations adds nothing over a single-frame reclaim.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The close-only long-flat logic ports to perps without structural change for the long legs (no short legs exist to port); no funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, and every 10m/40m boundary coincides with a 5m boundary on the UTC epoch, so resample alignment needs no session-gap normalization. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- Pinned primary rule (commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, path `user_data/strategies/berlinguyinca/MultiRSI.py`): https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/MultiRSI.py
- Collection repository: https://github.com/freqtrade/freqtrade-strategies
- Pinned Hummingbot VERSION: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Existing admission contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
