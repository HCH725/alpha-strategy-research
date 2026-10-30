---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Baltas-Kosowski statistically-meaningful-trend monthly gate; independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - paper
status: research-only
confidence: medium
source_as_of: 2011-12-10
sources:
  - https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2012-Barcelona/papers/EFMA2012_0485_fullpaper.pdf
  - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0019241
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Paper-internal tension: eq. (30) pins tk(beta) +/-2 with R2 >= 65%, while the cited Bryhn-Dimberg criterion is r2 >= 0.65 at p <= 0.05; for small k these are not identical. Record pins eq. (30) literally (see Limitations)."
---

# Baltas-Kosowski SMT monthly gate — independent derivative

## Provenance

- **Primary trading-rule source:** Akindynos-Nikolaos Baltas & Robert Kosowski, *Trend-following and Momentum Strategies in Futures Markets*, dated **December 10, 2011** on the title page (48-page PDF, EFMA 2012 Barcelona paper `EFMA2012_0485_fullpaper.pdf`), read in full this run via the stable EFMA URL above. No login, no paywall.
- **Source facts actually verified (PDF page numbers are 1-based extracted pages):**
  - §3.3 eq. (28) (p.17): the TREND regression `S(i)/S(t-NJ(t)) = alpha + beta*i + eps(i), i = 1..NJ(t)` over the lookback period.
  - §3.3 eq. (29) (p.17): `TREND(t-J,t) = +1 if t(beta) > +2; -1 if t(beta) < -2; 0 otherwise`, followed by the sentence *"In order to account for potential autocorrelation and heteroscedasticity in the price process, Newey and West (1987) t-statistics are used."*
  - §3.3 eq. (30) (p.18): *"split the lookback period in 4 to 10 intervals (i.e. 7 regressions per lookback period per asset) and decide upon a long/short position only if at least one of the regressions satisfies the above criteria"*; `SMT(t-J,t) = +1 if tk(beta) > +2 and R2_k >= 65% for some k; -1 if tk(beta) < -2 and R2_k >= 65% for some k; 0 otherwise`, `k = 1..7`. *"SMT and TREND constitute the only signals ... that allow for inactivity"*; *"On average, TREND generates activity for about 87% of the time and SMT for 63% of the time"* (p.18).
  - The five signals are *"first applied to the 12 futures contracts using a 12-month lookback period"* (p.18); monthly strategies *"perform portfolio rebalancing at the last trading day of each month"* (p.22, Jegadeesh-Titman overlapping methodology); sample is 12 futures, November 1999–October 2009 (abstract, p.2).
- **Method source (peer-reviewed):** Bryhn & Dimberg (2011), *An Operational Definition of a Statistically Meaningful Trend*, PLoS ONE 6(4): e19241, DOI `10.1371/journal.pone.0019241`, read this run: *"If one or several regressions concerning time and values in a time series, or time and mean values from intervals into which the series has been divided, yields r2 >= 0.65 and p <= 0.05, then the time series is statistically meaningful"*, with the series *"divided according to the equal time steps method"* (Methods; verified 7-observation equal-steps example present).
- **Independent researcher-defined executable derivative (NOT source-native):** the paper trades 12 futures with volatility-scaled sizing (eq. 3, `10%/sqrt(M)` target) and long/short/flat signals. This record pins single-asset Binance **BTC-USDT spot 1d**, **long-flat only** (paper `-1` maps to flat), fixed `Q = Decimal("0.001")` BTC with no volatility targeting, calendar-month decisions on completed 1d bars, plain bivariate-OLS `t_k` (Newey-West is stated only for TREND and its lag is unprinted; interval-mean OLS needs no stated lag), and idealized same-close MARKET fills. Every one of these researcher choices can change trade events and economics.
- **Frozen identity:** `BK-SMT|2011-12-10|eq30|derived-v1-20261030|BinanceSpot-BTC-USDT-UTC1d|12-complete-calendar-months|k4..10-equal-time-interval-means|t+-2-R2ge0.65|long-only|same-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The paper's mechanism is trend-quality filtering: among past-return sign (SIGN), moving-average (MA), EEMD trend extraction, TREND t-statistic and SMT, the trend-fitting signals *"maximise the out-of-sample performance while minimizing the portfolio turnover, hence dominating the ordinary momentum trading signal ... the sign of past return"* (abstract). SMT is *"a stricter signal than TREND and therefore would lead to more periods of inactivity"* (p.18) — it stays out when no interval regression clears the joint significance-plus-fit bar, *"in order to avoid eminent price reversals"* (p.3).

### Research interpretation

A monthly quality gate on trend, not a trend measurement: twelve months of daily closes must contain at least one time-scale (4–10 equal slices) whose interval-mean path is both steep (OLS |t| > 2) and clean (R² ≥ 0.65) before the record holds BTC; otherwise it stands flat. Unlike pooled 12-month time-series-momentum sign rules, direction alone never suffices — fit quality co-decides. The failure mode is plain: choppy-but-drifting years stay flat and lag a straight grind, while a smooth parabolic top holds long into the break until the next month-end vote releases it.

## Signal — fully pinned independent rules (Gate 1, 2, 3, 4)

- **Market and clock:** one continuous, UTC-aligned Binance **BTC-USDT spot 1d** OHLCV sequence. Bar index `t` has exchange **open** timestamp `T[t]`; its complete O/H/L/C become decision-available only at `E[t] = T[t] + 86400 seconds`. Only complete historical bars are eligible; no future, partially formed or higher-timeframe candles.
- **Input validation:** strictly increasing, gap-free 86400-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.
- **Decision months:** for calendar month `M` (UTC), the decision bar `t(M)` is the last 1d bar whose open timestamp falls in `M`. The lookback window `W(M)` is the ordered close series of the **12 complete calendar months** preceding `M` (months `M-12..M-1`), `N = |W|` closes (365 or 366 on 24/7 BTC). Months with no complete history never decide.
- **Interval-mean regressions:** for each `k` in `{4,5,6,7,8,9,10}`: split index range `[0,N)` into `k` equal-time intervals; interval `j` covers `[j*N/k,(j+1)*N/k)`; point `i` (0-based) contributes weight `w = overlap([i,i+1), interval)` (cell-overlap fractional boundary weights — the researcher's deterministic pin of the paper's *"equal time steps"* method on an even daily grid). Weighted mean index `Xj` and mean close `Yj` per interval; bivariate OLS on the `k` points gives slope `b` and `R2` (`R2 = SSR/SST`, clipped to `[0,1]`).
- **t-statistic (researcher-pinned plain OLS form):** with `df = k-2`: if all `Yj` equal (`SST = 0`, `R2` undefined) the regression casts **no vote**; else if `R2 >= 1-1e-12` then `t_k = +inf` (`b > 0`) or `-inf` (`b < 0`); else if `R2 <= 0` then `t_k = 0`; else `t_k = sign(b)*sqrt(R2*(k-2)/(1-R2))`. Newey-West is deliberately not used (paper states it only for TREND; no lag is printed for SMT) — a declared difference from one plausible reading.
- **Votes and signal:** `LONG_VOTE` iff some `k` has `t_k > +2` **and** `R2_k >= 0.65` (both strict/weak exactly as printed; `t_k = +2` exactly does not vote). `SHORT_VOTE` iff some `k` has `t_k < -2` **and** `R2_k >= 0.65`. `SMT(M) = +1` if `LONG_VOTE` without `SHORT_VOTE`; `-1` if `SHORT_VOTE` without `LONG_VOTE`; `0` otherwise — including a two-sided conflict, which the paper leaves silent and this record pins to flat (0 conflicts in the 98-decision verification sample below, so the pin is currently unexercised).
- **Direction (Gate 2):** long-flat. `+1` holds/establishes LONG; `0`/`-1` holds flat/closes to flat. The short side is explicitly disabled by researcher adaptation, not omitted by accident; spot market, no borrowing.
- **Entry/exit (Gate 3):** at each `E[t(M)]`: if FLAT and `SMT(M) = +1`, MARKET BUY exactly `Q = Decimal("0.001")` BTC at the real `C[t(M)]` (idealized same-close research convention, see Execution assumptions); if LONG and `SMT(M) <= 0`, MARKET SELL the full Q at `C[t(M)]`. At most one action per decision; decisions occur only at month-ends. There are no stop, take-profit, trailing, time-limit, opposite-signal-add, or partial legs — the paper specifies none and none is invented.
- **Position state (Gate 4):** initial FLAT, 10,000 USDT cash. Entries only from FLAT; no pyramiding, no adds, no DCA/safety orders, no cooldown, no averaging; simultaneous exposure is at most one fixed unit, so multi-position semantics are demonstrably irrelevant. Re-entry requires a later `+1` while FLAT. If cash cannot cover `Q*C*(1+fee)` in exact Decimal, consume the signal, remain FLAT, never invent a partial fill. An open LONG at sample end is valued at the last actual valid close, never force-liquidated.
- **Warmup (Gate 6):** the first 12 complete calendar months are data-only and never decide. With Binance listing 2017-08-17, the partial August 2017 never enters any window; first decision is `M = 2018-09` at `E[t(2018-09)]` (2018-09-30 close). No optimizer, ML, external feed, negative shift, future extremum, repaint, or fitted parameter exists anywhere in the rule.
- **Exact Decimal ledger (position truth):** all accounting uses `Decimal(str(x))` on observed closes, exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT with `fee = Decimal("0.001")` per side (explicit research assumption). `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly; no epsilon exists. If any simulator quote/fee cross-check disagrees beyond `max(1e-8, 1e-12*Q*P)`, **abort as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator.

## Required data

Only actual Binance BTC-USDT spot UTC 1d O/H/L/C. The signal uses completed closes of `W(M)` at `E[t(M)]`; the same-close fill price `C[t(M)]` is not used retroactively for the vote. No higher/lower timeframe, funding rate, order book, multi-asset feed, volatility estimate, external sentiment or ML inference. Missing/invalid bars abort rather than silently continuing an inconsistent ledger.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0`, bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle did not re-read engine bytes; it reuses exactly two already-reviewed primitives and no new one: (a) the single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive with the independent Decimal ledger, as reviewed in alpha PRs **#414** and **#550**; (b) the **1d spot** feed with completed-bar decision timing, as reviewed in the PASS `wick-reversal-hammer-shooting-star` 1d and `fmz-521670` 1d records. The SELL leg reuses the identical MARKET CLOSE path (no new executor, no stop/limit/trailing/time-limit primitive). The independent Auditor must confirm that evidence applies to the pinned package and path; per #424 bounded-commit-semantics, the package label is retained as a label only and **no package-to-commit mapping is invented**.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` at the month-end decision row only. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the decision row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[t(M)]`, not a claim a real order could execute at the completed close — the same-close fill is an idealized research convention consistent with the paper's own end-of-month-quote evaluation. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. The paper's volatility-scaled sizing is replaced by fixed-Q — a declared event-changing difference. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only already-reviewed primitives. The new strategy changes only the controller-side monthly SMT vote, the long-flat mapping, and the month-end cadence; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned 48-page PDF supports every constant cited above: eqs. (28)–(30) and the 4-to-10-interval / 7-regression construction (§3.3, pp.17–18), the ±2 cutoffs with `R2 >= 65%`, inactivity as a designed feature with *"TREND ... 87% ... SMT ... 63%"* activity (p.18), the 12-month application universe (p.18), last-trading-day-of-month rebalancing (p.22), and the Nov-1999–Oct-2009 12-futures sample (abstract). The PLoS ONE Methods page supports the `r2 >= 0.65 at p <= 0.05` criterion and the equal-time-steps interval construction. No source performance figure is relied upon for any gate.

### Independently reproduced

Signal-determinism verification only (no trade, Hummingbot/Qlib, performance, OOS or fee reproduction): the transcribed rule (fractional-boundary interval means, OLS `t_k`, eq. (30) votes, conflict→flat, long-flat mapping) was executed over **3,362 real Binance BTCUSDT 1d bars (2017-08-17→2026-10-30)** fetched this run via the public klines API: **98 month-end decisions (2018-09→2026-10)** yielding **LONG 40 / FLAT 36 / short-vote 22 (→flat)**, i.e. **62/98 = 63% active — exactly the paper's reported 63% SMT activity**; LONG months span **6 distinct years (2019, 2020, 2021, 2023, 2024, 2025)** with 8 long/flat transitions and **0 vote conflicts**; lookback windows are 365–366 bars. These are researcher verification figures, not source facts and not performance evidence. Otherwise: `Not independently reproduced.` for everything else (fills, costs, engine run).

### Negative evidence

Pre-write dedup at `main@42708a5c` (454 root-level strategy records): `Baltas`, `Kosowski`, `EFMA2012` return **zero** content hits; `statistically meaningful`, `Bryhn`, `interval mean` return **zero** signal hits (the lone pool `SMT`/`smt` string is an ADX-smoothing parameter in an unrelated record, not a signal); `R2`/`r-squared` hits (6 files) are performance prose or a corr²-penalized RSRS slope variant — none votes on an `R2 >= 0.65` interval-regression gate; `0.65` hits are t-statistics, confidence constants and profit factors, never an R² signal threshold. The 11 open `research/*` PRs were inspected by source/title/body — none uses this paper or an interval-regression signal. Nearest pool neighbors differ in mechanism: `tsmom-12m-sign-monthly` (12-month cumulative-return sign, no regression, no fit gate — possible substantial month overlap by construction family, disclosed in Limitations; pooled `hurst-ooi-pedersen-century` overlaps TSMOM yet stands as precedent for construction-distinct records), `tradingview-tasc-linreg40-slope-sign` (40-bar OLS slope sign, no R²/t gate), `faber-gtaa-10m-sma` (10-month SMA regime), `qrs-penalized-rsrs-zscore` (600-day standardized high-low slope × corr², cross-pair triggers — different object, different gate). Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only: February/leap-year window lengths (365 vs 366), month-boundary bar assignment (UTC), fractional-boundary weights vs whole-bar assignment, all-equal-window NaN path, `R2 = 1` infinite-t path, `t = ±2` / `R2 = 0.65` exact-boundary votes, conflict-month flat pin, signal-month vs fill-month separation, insufficient-cash consumption, last-bar open LONG valuation, `Decimal(str())` vs float reconciliation, ENGINE_MISMATCH abort path. No backtest, trading, deployment or cron change here.

## Crypto portability

Pinned to Binance BTC-USDT spot 1d only. Any other pair, venue, or timeframe replays a different event stream and is a different derivative, not covered by this record. Calendar months on 24/7 BTC hold 28–31 bars versus the paper's ~21 trading-day months — a disclosed adaptation, not an equivalence claim. A perpetual-ported variant would need the full funding/cost load and is not specified here.

## Limitations

- Derived, not source-native: single-asset fixed-Q long-flat replaces 12-futures vol-scaled long/short; paper `-1` maps to flat; trading-day months become 24/7 calendar months; fills are idealized same-close. All event-changing, all declared above.
- `t_k` is plain bivariate-OLS; the paper's Newey-West sentence attaches to TREND and no SMT lag is printed. If the Auditor reads NW as inherited, this record's votes change — flagged, not hidden.
- Eq. (30) vs `p <= 0.05` tension (`contested: true`): the record pins eq. (30); a strict-PLoS variant would differ on small-k months.
- Possible heavy month overlap with pooled 12-month momentum longs is a same-family resemblance, not an identity: the decision object (7 interval-mean R²/t gates) shares no computation with cumulative-return sign.
- Engine evidence is by reviewed-primitive lineage (#414/#550, wick/fmz-521670 1d records), not a new wheel hash or controller implementation this cycle.
- No slippage modeled; 0.1% fee assumed; live economics unverified.
- Long-only spot: no statement about short-side or margined behavior is made or implied.

## Implementation status

`implementation_status: not-implemented`, `status: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. Auditor alone may source-fact remediate exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. No live, Paper, Testnet, deployment, or downstream screening authorization is granted or implied by this record.

## Related Wiki records

None — the Scout performs no Wiki Brain write in this lane.

## Sources

- https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2012-Barcelona/papers/EFMA2012_0485_fullpaper.pdf — Baltas & Kosowski, *Trend-following and Momentum Strategies in Futures Markets*, dated December 10, 2011 (48 pp., read 2026-10-30; §3.3 eqs. (28)–(30) pp.17–18; rebalancing p.22).
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0019241 — Bryhn & Dimberg (2011), *An Operational Definition of a Statistically Meaningful Trend*, PLoS ONE 6(4): e19241, DOI `10.1371/journal.pone.0019241` (Methods: r2 ≥ 0.65 at p ≤ 0.05, equal-time-steps intervals; read 2026-10-30).
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source, inspected in prior reviewed cycles (see lineage above), not re-read this cycle.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
