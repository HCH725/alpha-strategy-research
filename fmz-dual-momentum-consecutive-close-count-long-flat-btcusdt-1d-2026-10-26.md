---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FMZ Dual-Momentum consecutive-close-count state — BTCUSDT spot 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-10-09
sources:
  - https://www.fmz.com/strategy/428785
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Dual-Momentum consecutive-close-count state — BTCUSDT spot 1d independent derivative

## Provenance

- **Primary FMZ source:** ChaoZhang, *Dual-Momentum-Strategy* (Chinese title 双重动量策略), FMZ strategy page **428785**, created **2023-10-09 15:03:30**, last modified ~3 years ago, 1,219 hits as seen live this cycle: https://www.fmz.com/strategy/428785. This Scout fetched the live page on **2026-10-26** and verified the prose rules (consecutive rising/falling close counts with `LongEnterAfter`/`LongExitAfter`/`ShortEnterAfter`/`ShortExitAfter` parameters) plus the full Pine v4 program text, which matches the research-mirror capture byte-for-byte on all decision-critical lines (backtest header, four inputs with defaults, `Valid`/`LongEnter`/`LongExit`/`ShortEnter`/`ShortExit` criteria, four order lines, TradeSince gate).
- **Frozen source header (verbatim):** `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, author demo window `2022-10-02 00:00:00 → 2023-10-08 00:00:00`. The header's `1d` decision period plus the prose's "monitoring daily closing prices" is the Gate-2 timeframe evidence. The author's demo window and futures venue are disclosed source context, not this derivative's frame.
- **Frozen source defaults (verbatim):** `LongEnterAfter=2`, `LongExitAfter=1`, `ShortEnterAfter=2`, `ShortExitAfter=1`, `TradeSinceYear=2017`, `TradeSinceMonth=1`. The live program ships **no** `strategy()` declaration (the only `strategy(...)` line is commented out), no `strategy.exit`, no stop/limit/trailing/time-exit leg of any kind.
- **Frozen independent derivative identity:** `FMZ:428785:ChaoZhang:2023-10-09 | independent-derived-v1:2026-10-26 | rise2-fall1-long-leg-only | BinanceSpot:BTC-USDT:1d:LONG-FLAT:Q0.001BTC:close-effective-MARKET:trade_cost0.001:3bar-warmup`.
- **Researcher-defined changes, not source facts:** the source is two-sided (it also ships `ShortEnter`/`ShortExit` with `strategy.entry("short", ...)`); this record keeps the source long-entry/long-exit predicate expressions with frozen defaults and **explicitly disables the entire short leg** (never short, disclosed adaptation). The `Futures_Binance` header is replaced by a Binance **spot** frame (no funding contract by construction — no zero-funding claim is made). Pine `when=` next-tick order semantics are replaced by completed-close MARKET simulation (disclosed execution freeze, same primitive as the reviewed #417/#472 path). Missing `strategy()` sizing/pyramiding is frozen to the house frame (fixed 0.001 BTC unit, Pine documented default pyramiding 0 → repeat entries while LONG are no-ops) with 0.001 per-side modeled cost. The `TradeSince 2017-01` gate is dropped as verified-inert (all validated sample bars postdate it — see Evidence). `Valid = change(time)` is carried as verified always-true on contiguous bars (see Evidence). The author's 2022-10→2023-10 demo window is not reused; research uses the full validated history. This record is **not** an admission claim for the author's original two-sided futures backtest, and it is **not** Antonacci-style multi-asset Dual Momentum (no second asset, no lookback ranking, no regime switch — name collision disclosed, mechanism unrelated).
- **Rejected sibling mechanisms (disclosed, not proposed):** HPotter *Key Reversal Up Backtest* (FMZ 440103, read at source: intrabar pip-denominated `strategy.exit`-class SL/TP legs `low <= posprice − stoploss` / `high >= posprice + takeprofit` plus `strategy.close_all()` state handling on a `Futures_Binance` always-in-market book — stop/limit intrabar exits have no scalar net-fee mapping on the pinned path); 03.freeman *FTSMA Fourier* (FMZ 434326: nine-option MA-type string input plus TP/SL/trailing inputs — reviewer must not choose the variant; `strategy.exit` legs); ChaoZhang Kalman/Hull/MFI siblings (multi-mode inputs, EMA-family seeding, or always-in-market two-sided books).

Pre-write duplicate check against the actual `main` tree at `708c437` (353 root records), repo-wide grep and all ten open `research/*` PRs: no record or open PR with FMZ id `428785`, `LongEnterAfter`, or this derived identity. `dual-momentum`/`dual momentum` hits in `main` are zero; closed-PR search returns no 428785 candidate.

## Economic mechanism

### Source-reported

Short-horizon close-direction persistence: two consecutive rising daily closes mark a buyable micro-uptrend; a single falling close ends it. No volume, no volatility, no trend filter, no economics beyond "rising bars = momentum, falling bars = exit".

### Research interpretation

This derivative buys the second consecutive up-close and holds until the first down-close. It trades pure close-comparison counting with no indicator, no seeding, no stop, no target, and no regime gate — the only memory is the FLAT/LONG position state. Because entry needs two rises and exit needs one fall, the book whipsaws in chop (real-kline evidence: 438 round trips over ~8.2 years, median hold 1 bar) and the only risk control is the one-bar decline exit; a slow bleed of alternating closes still exits every down bar, but gap-through risk across a single daily bar is unprotected by construction.

## Signal

Let `C[t]` be a **fully completed** UTC daily close with finite positive OHLC and `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]>0`. Frozen independent-derivative numeric semantics (Pine built-in equivalence beyond these expressions is not claimed): `rising(C,2)` ⇔ `C[t]>C[t-1] AND C[t-1]>C[t-2]`; `falling(C,1)` ⇔ `C[t]<C[t-1]`; strict inequalities, equality on either comparison prints false.

1. **Entry predicate `E[t]`:** `rising(C,2)[t]` (source `LongEnter`, `LongEnterAfter` frozen at 2, `Valid` verified inert-true below).
2. **Exit predicate `X[t]`:** `falling(C,1)[t]` (source `LongExit`, `LongExitAfter` frozen at 1).
3. `E[t]` and `X[t]` are **mutually exclusive by construction**: entry requires `C[t]>C[t-1]`; exit requires `C[t]<C[t-1]`. Proven over 3,356 real-kline decisions with zero joint triggers. On a valid completed bar, process **EXIT before ENTRY** as a standing rule (moot under exclusivity, binding if inputs ever change).
4. Direction and state: only `FLAT` or `LONG(0.001 BTC)`, initially FLAT. If LONG and `X[t]`, issue one full-quantity SELL (source `strategy.close("long", ...)`). Else if FLAT and `E[t]`, issue one BUY (source `strategy.entry("long", strategy.long, when=LongEnter)`). Otherwise hold. Never short; no pyramiding (no live `pyramiding` argument — Pine documented default 0, repeat `E[t]` while LONG are no-ops), scaling, averaging, BO/SO, DCA, reverse orders, hedges, or simultaneous position/executor exposure. Re-entry is allowed on a **future completed bar** with a fresh `E[t]` only after SELL fill confirmation. No cooldown, no pending limit orders. At most one outstanding MARKET action; never infer a fill from mere order submission.
5. No stop-loss, take-profit, trailing stop, maximum holding period, forced end-of-sample liquidation, equity-based sizing, leverage, margin, funding payment, session/date restriction, or TradeSince gate. These are **explicitly disabled researcher decisions** (the source declares no `strategy.exit`, no stop, no target, no trailing; the TradeSince gate is verified inert and dropped with disclosure), not asserted script defaults. Unclosed positions at the predetermined research end remain marked open and must not be represented as realized PnL.

## Required data

- One Binance **spot** market `BTC-USDT`, interval `1d`, UTC day boundary, `open/high/low/close` and original candle-open timestamp. No volume, external security, order book, trades, futures funding, mark/index price, higher/lower timeframe, ML model, shared capital, or portfolio synchronization is used (the rule reads closes only; `Valid = change(time)` needs only distinct consecutive bar timestamps).
- Each exchange candle's timestamp labels its **OPEN**, not its completed-close availability. Define `decision_ts[t] = candle_open_ts[t] + 86400` seconds; use the completed candle only when all its OHLC values are available. Feed prepared engine rows with the effective **completed-close timestamp**, never the original open timestamp for decision or simulated fill. Check monotonicity and exactly contiguous 86400-second UTC daily opens.
- The first **3** fully completed, contiguous, validated bars are warmup-only and cannot trigger orders (`rising(C,2)` needs `C[t-2]`; `falling(C,1)` needs `C[t-1]`; decisions start at index 2). No centered windows, future extrema, negative shifts, incomplete daily bar, full-sample preprocessing or repainting.
- A missing, nonfinite, nonpositive or inconsistent OHLC, absent completed close, timestamp gap, or unsorted bar blocks that bar's decisions **and fill**. Do not synthesize candles or substitute a prior price. Resume decisions only after 3 new contiguous valid completed bars; an existing LONG stays open during the gap, with no fictitious stop/exit or fee. A pending unconfirmed order must be reconciled from its real simulated fill ledger before any further action; never invent completion. Such gaps can prolong unprotected exposure.

## Execution assumptions

**Pinned baseline:** Hummingbot package label `20260920`, `hummingbot/VERSION = dev-2.17.0` (read at pinned commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` this cycle — `VERSION` prints `dev-2.17.0`), pinned `HCH725/hummingbot` source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly read these pinned files at that commit (not an unpinned online API or current main):

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` — `_parse_rest_candles` reads REST `row[0]` as the **open timestamp** (`ensure_timestamp_in_seconds(row[0])`) with OHLC values; `.../constants.py` explicitly supports interval `1d` (`INTERVALS` bidict, line 24 — re-verified this cycle: `1d` present).
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` — `BacktestingEngineBase.simulate_execution` loops row-wise over timestamped prepared rows (`for i, row in processed_features.iterrows()`), calls `controller.determine_executor_actions()`, and routes each `CreateExecutorAction` to the executor simulator with the forward slice **starting at the current row** (`processed_features.loc[i:max_ts]`); `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60*60` seconds; `BacktestPositionHold` nets same-pair BUY/SELL average-cost ("Buys and sells of the same asset net out automatically"), realized gross PnL and cumulative quote fees.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` — `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, BUY/SELL, base amount 0.001 fills at the **first supplied row's close** (`fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close at fill_timestamp`), records `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, then reports `CloseType.POSITION_HOLD`. Together with the current-row forward slice, a completed-close signal at `decision_ts` produces a same-effective-timestamp MARKET-close **simulation** on that prepared row. This is the actual pinned close-effective **backtest** primitive, not an exchange close auction or an intrabar fill. The researcher-defined controller would be a strategy-specific `DirectionalTradingController` emitting these actions; **it is not implemented or deployed**.

**Critical fill/position-state setting:** instantiate `BacktestingEngineBase(terminated_executors_window=None)` so the controller can see fill-confirmed executors on subsequent daily decisions. The pinned default is only 3600 seconds and may hide the previous daily fill from `controller.executors_info`; the engine still has an internal stopped ledger. Maintain explicit controller-side fill-confirmed quantity, pending-action suppression, and position cost/fee ledger; never equate `POSITION_HOLD` with a fresh unfilled order or assume an order was filled when submitted. This model convention does **not** establish causal executable live close fills. A future execution path that cannot honor the same effective-timestamp model must be revalidated as a distinct derivative.

**Cost and capital:** research `initial_quote_cash=10000 USDT`, fixed `amount=0.001 BTC`, `trade_cost=0.001` of quote notional **per simulated BUY and SELL fill**, modeled slippage `0` as an expressly artificial simulation assumption. Do not describe this 0.1% as a measured exchange fee or the zero modeled slippage as realized slippage. Require sufficient simulated cash including modeled BUY fee; if not, no BUY. SELL only confirmed available base quantity. Unleveraged spot has no perpetual-futures funding contract; **no claim of zero realized futures funding** is made. Actual maker/taker schedules, lot/tick rounding, min notional, spread, latency and partial fills are not verified and are not authorized for Paper/Testnet/Live. Model net realized quote PnL as `BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote`, **not** the gross-only executor PnL field. No fabricated prices or fills. Float rounding residuals must not create a second position.

The existing independently reviewed **PR #417** documented the same pinned Binance spot `1d` / MARKET first-close / POSITION_HOLD research primitive (reused here with no novel execution primitive, as in merged #472); the wheel-to-commit binary hash was **not revalidated in this Scout cycle**. The package label `20260920` is retained as a policy label only; no package-to-commit byte mapping is invented. Gate 5 relies on the directly inspected pinned code path and the existing reviewed evidence, not a claim of fresh wheel-byte identity or an implemented controller. No futures/margin/shared-capital/new data primitive is needed.

## Evidence

### Source-reported

FMZ `428785`, ChaoZhang, 2023-10-09: consecutive rising/falling close-count momentum; frozen defaults enter-long-after-2-rises / exit-long-after-1-fall (short leg mirrored, explicitly disabled here); `strategy.entry` + `strategy.close` only, no `strategy.exit`, no stop/target/trailing; `TradeSince 2017-01` gate; `period: 1d` header on `Futures_Binance BTC_USDT` with author demo window 2022-10-02→2023-10-08. No returns, win-rate, or trade-count figures are claimed from the source page.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen `E[t]`/`X[t]` arithmetic plus the FLAT/LONG state machine were executed over a 3,358-decision walk over real Binance BTCUSDT `1d` klines (2017-08-17 → 2026-10-25, fetched from the public klines API this cycle; every bar validated finite/positive/consistent, day-step contiguity exact with zero gaps and zero invalid bars): decisions start at index 2 as predicted (3-bar warmup); `Valid = change(time)` verified nonzero on all 3,357 post-first bars (inert-true as frozen); TradeSince gate verified never binding (earliest sample bar 2017-08-17); **438 entries / 1,641 exit-events with zero same-bar co-fires**, **438 strictly alternating round trips ending FLAT** (1,203 exit-events while FLAT are state no-ops by rule); holds min/med/max 1/1/7 bars. Entry/exit provably disjoint (`C[t]>C[t-1]` vs `C[t]<C[t-1]` on the same close pair). No indicator, no seed, no float branch exists anywhere in this rule, so no seeding ablation applies. **Engine-code inspection only, not a strategy backtest:** pinned Hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was read file-by-file for the Binance spot `1d` candle parser (open-timestamp rows), the row-wise engine action loop with current-row forward slices, MARKET-first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, `hummingbot/VERSION` and 3600-second vs `None` terminated-executor visibility; `constants.py` `1d` membership re-verified live this cycle. The candidate's trade events, Pine outputs, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

- Pine `when=` next-tick fill semantics are **not** reproduced; the completed-close MARKET fill is a disclosed researcher freeze, and source-native/lossless equivalence of full trade events is unverified. The independent derivative is evaluated against its own frozen rules only. Researcher freezes (short-leg disablement, spot frame, house sizing/cost, 3-bar warmup, exit-before-entry, TradeSince drop, demo-window non-reuse) are disclosed above and change events versus the author's two-sided futures backtest by construction.
- The rejected siblings above (Key Reversal pip SL/TP, Fourier multimode, Kalman/Hull/MFI variants) were read at source and killed for stop/limit intrabar exits, reviewer-choice inputs, or always-in-market books; none validates this candidate.
- No verified live close fill, partial fill, market impact, exchange fee schedule, futures funding or venue order-size permission. None is silently imputed.

## Deduplication

Main at immutable SHA **708c437** contained **353** root strategy records; README static count **353**. Working-tree filename/content search for `428785`, `LongEnterAfter`, `dual-momentum` and `dual momentum` returns zero strategy records built on any consecutive-count rule from this source (the single `dual-` title hits are unrelated: dual-thrust, dual-bandpass, dual-leg state prose). GitHub title search returns no prior Dual-Momentum-428785 candidate; closed-PR search returns none. Ten open research/* PRs were checked (#48 Larry Williams 3-EMA-channel streak gate, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles KCD) — none carries this primary source or a close-count rule.

Nearest neighbors are **not equivalent**: `worldquant-alpha9-…` trades a **five-day** streak-gated sign assignment with a two-sided reversal-or-flatten book (mixed-window contrarian branch, next-open fills) — this record trades a **two-rise enter / one-fall exit** with a dedicated exit leg on a long-flat book and close-effective fills; `eight-day-run-sma5-…` anchors runs to an SMA(5) with an 8-bar qualification gate and reversal entries — this record reads raw closes with no average and no gate; `#48` (open) gates entries on a 3-EMA channel; `three-bar-reversal` / `1-3-1-red-green` / soldiers-crows / Harami / morning-evening-star records trade body/pattern constructions, not close-direction counts. Different source, different signal construction, different exit book: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

1. Hand-construct completed daily close paths for `C[t]==C[t-1]` equality (both predicates false), alternating 1-rise/1-fall chop (no entry), wrong-side persistence (all-fall stretches print exits only), and inconsistent/nonpositive bars. Verify trigger/no-trigger, strict-inequality exclusivity, and exit-before-entry ordering.
2. Ablate the 2-rise/1-fall windows (e.g. 3/1, 2/2) on predeclared IS/OOS partitions and verify the ablation actually changes entry/round-trip event times; do not tune on OOS.
3. Check warmup bars 0–2, missing/invalid OHLC, nonmonotone/gapped timestamps, `Valid` inertness, FLAT/LONG/pending order transitions, fill-ledger persistence across 86400 seconds, and no same-bar re-entry after a SELL.
4. If formally selected downstream, build the minimal strategy-specific controller/recipe and validate **representative event-level Qlib/Hummingbot parity for this execution primitive** before broad Qlib screening if that primitive has not already been independently validated. Compare timestamp, signal, action, confirmed fill, quantity, fee and position-cost state. A model capability failure is an engineering hold, not a retroactive profitability or admission decision. No performance/Sharpe/OOS claim is made here.

## Crypto portability

Only `BTC-USDT` Binance spot `1d` is pinned in this research record. Other assets, timeframes, market types, and the downstream seven-coin × three-timeframe × leverage/DCA research campaign are **separate experiments**, not HB_READY admission requirements or silently equivalent original source behavior. Applying BO/SO overlays or futures economics changes this frozen trade-event/economic model and requires an explicitly declared derivative.

## Limitations

- A two-rise entry can print into a top; without SL/TP/time stop a gap down across one daily bar bypasses the one-fall exit at a worse price, and the source specifies no protection to remove — exposure control is the decline exit alone.
- Real-kline evidence shows fast turnover (438 round trips over ~8.2 years, median hold 1 bar); whipsaw clusters in chop and fee drag under the 0.001 modeled cost are expected properties of the frozen 2/1 windows, not malfunction. Turnover is inherent to the frozen source defaults, not a tuned choice.

## Implementation status

Not implemented. No controller, recipe, Qlib artifact, or deployment exists. The pinned-path evidence above is code inspection plus a stdlib rule-logic self-check, not an executed backtest. `IMPLEMENTATION_NEEDED` applies if this record is formally selected for execution.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. No trading authorization is granted or implied by this record.

## Related Wiki records

None. No Wiki Brain write was performed for this Scout cycle.

## Sources

- FMZ primary source (verified live 2026-10-26): https://www.fmz.com/strategy/428785 — ChaoZhang, *Dual-Momentum-Strategy* (双重动量策略), created 2023-10-09, `period: 1d` header, frozen defaults LongEnterAfter=2 / LongExitAfter=1 (short leg disabled in this derivative).
- Pinned engine (inspected this cycle, no new capability): `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`VERSION = dev-2.17.0`); Binance spot `1d` candle parser, row-wise engine action loop with current-row forward slices, MARKET-first-row-close fill with quote-notional fees and POSITION_HOLD ledger; package label `20260920` retained as policy label only.
