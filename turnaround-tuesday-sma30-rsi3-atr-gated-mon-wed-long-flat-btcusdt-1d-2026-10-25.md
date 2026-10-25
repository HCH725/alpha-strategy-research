---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Turnaround Tuesday SMA30-RSI3-ATR-gated Mon-Wed long-flat on BTCUSDT spot 1d derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-04-30
sources:
  - https://www.fmz.com/strategy/449948
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Turnaround Tuesday SMA30-RSI3-ATR-gated Mon–Wed long-flat — independent BTCUSDT spot 1d derivative

## Provenance

- **Primary FMZ publication:** *周二反转策略(周末过滤) / Turnaround-Tuesday-Strategy-Weekend-Filter*, author token **ChaoZhang**, canonical page https://www.fmz.com/strategy/449948 . Page HTML fetched and read on **2026-10-25** (HTTP 200, 787,104 bytes): `<title>` confirms `周二反转策略(周末过滤) | 发明者量化`; token counts over the whole landing HTML: `Turnaround` 4, `449948` 20, `muikol` 2 (original Pine author, see code header), `ChaoZhang` 2, `周二反转` 16; word-boundary counts for `Sharpe` / `Win Rate` / `Max Drawdown` / `Annualized` / `Profit Factor` are all **0** — the page ships no performance number of any kind for this strategy. No performance figure of any kind is transcribed from the page.
- **Pinned executable artifact (immutable public mirror, read end to end):** repository https://github.com/fmzquant/strategies at full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` this cycle — the same head pin as the merged RVI, WaveTrend, KST, Schaff and further admissions), exact file path `周二反转策略周末过滤-Turnaround-Tuesday-Strategy-Weekend-Filter.md` (8,497 bytes, blob SHA `1170a6fe23210607a8ab62d525d2d44d23ad97b9`, verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The file carries `> Last Modified` = `2024-04-30 16:07:45` (date part adopted as `source_as_of`) and `> Detail` = the canonical FMZ URL above.
- **Complete Pine block (decoded in full from the mirror, no line skipped):** the `Source (PineScript)` fence holds a complete `//@version=5` program headed `// © muikol` under the Mozilla Public License 2.0. Census over the pinned block: 1 `strategy(` (`strategy("Turnaround Tuesday", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.035)` — percent-of-equity sizing and a source-declared 0.035% commission, both recorded here and both replaced by disclosed researcher pins below) / 0 `study(` / 0 `indicator(` / 1 active `strategy.entry` (`"Buy"`, `strategy.long`, only direction leg in the file) / 1 active `strategy.close` (`"Buy"`, Wednesday leg naming the exact entry id) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `pyramiding` argument (Pine default `0` governs — recorded as source-declared-by-default) / 0 `process_orders_on_close` (language default governs — recorded likewise; this record's fill convention is a predeclared derivation) / 0 `calc_on_every_tick` / 0 `request.*` / 0 `security(` / 6 `input(` calls (`ma_period = 30`, three `true` filter toggles, `start_date`/`end_date` timestamps) / 1 `ta.sma` / 1 `ta.atr` / 1 `ta.rsi` / 2 `dayofweek` reads / 1 `month` read / 0 `volume` / 0 bare `open` / no `high`/`low` read outside `ta.atr`. Direct series reads are `close` (plus `high`/`low`/`close` inside ATR) and bar-calendar fields only.
- **Order legs read verbatim:** `entryCondition = isMonday and bear and notMay and filter_1 and filter_2` where `isMonday = (dayofweek == dayofweek.monday)`, `bear = close[1] < MA_tt[1]` with `MA_tt = ta.sma(close, 30)`, `filter_1 = rsi3[1] < 51` with `rsi3 = ta.rsi(close, 3)` (strict), `filter_2 = close[1]/atr10[1] < 95` with `atr10 = ta.atr(10)` (strict), `notMay = (month != 5)`; `if entryCondition and inTestPeriod` → `strategy.entry("Buy", strategy.long)`; `if (dayofweek == dayofweek.wednesday) and strategy.position_size > 0 and inTestPeriod` → `strategy.close("Buy")`. `inTestPeriod = true` is hardcoded — the two date inputs are declared but read by no active line and are inert, so no cherry-picked test window is carried into the executable logic. The program ships zero stop, zero target, zero trailing, zero time-stop leg — the no-risk-leg posture is explicit, not invented.
- **Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) market/frame pin `BTCUSDT` Binance **spot `1d`** (the mirror backtest stanza pins `period: 2h`, `basePeriod: 15m`, `Futures_Binance BTC_USDT` over 2024-03-01→2024-03-31 — that stanza is the mirrorer's FMZ plumbing for a timeframe-agnostic Pine program, fenced and never adopted); (2) source default next-bar-open fills converted to the disclosed same-bar-close research convention (see Execution assumptions); (3) an adopted **60-bar** warmup with pre-warmup bars flat by record rule (structural minimum is 31 completed bars — 30 for the first SMA value plus 1 prior bar for the `[1]` refs — see Signal); (4) fixed `0.001 BTC` spot sizing with research `trade_cost=0.001` per side replacing the source 100%-equity sizing and 0.035% commission (both recorded above, never carried); (5) UTC weekday/month derivation pinned to bar open timestamps for 24/7 crypto bars (the Pine names no timezone; crypto has no session template); (6) the Wednesday exit pinned to the first valid Wednesday-completed bar while LONG, with data-gap carry rules fenced in Signal. Entry conjunction, strict inequalities, length 30/3/10 coefficients, the May exclusion, the long-only stance, and the Mon→Wed hold are source-native and unmodified.
- **Immutable identity:** `FMZ-449948-muikol-TurnaroundTuesday-MA30-RSI3 LT51-closeATR LT95-noMay | independently-derived-v1-longflat | BinanceSpot-BTC-USDT-1d | 2026-10-25`. Any change to filters, thresholds, months, weekdays, market, clock, fill, or position state constitutes a different derivative.

## Economic mechanism

### Source-reported

Gated weekend-effect reversal (prose plus code): a Monday is bought only when the prior close sits below its 30-bar average (downtrend/weak-weekend posture), short-horizon sentiment is soft but not washed out (`RSI3 < 51`), the price level is not detached from recent volatility (`close/ATR10 < 95`), and the calendar is outside May ("Sell in May" avoidance); the position is held through Tuesday's session and liquidated on Wednesday. The design bets that a pessimistic-but-orderly Monday open resolves upward over the following two sessions often enough to carry an unprotected two-day hold.

### Research interpretation

Hypothesis only: the five-leg conjunction selects "soft Monday, no panic, no May" tapes and rents Tuesday's well-documented turnaround drift with a hard Wednesday guillotine. Unlike the pool's pure-calendar records (`monday-drift-weekly-calendar-hold`, a price-blind 24-hour Mon→Tue hold; `sell-in-may-seasonal-hold`, a price-blind September→May month hold), every leg here except the weekday/month rails reads price — the calendar gates the trade but never triggers it. Unlike indicator-reversal records (RSI/connors washout fades that exit on indicator reclaim), the exit is a fixed weekday, so a Monday entry that meets a two-day slide realizes the full adverse excursion — there is no stop, no target, no trailing, and no opposite-signal exit by explicit source construction.

## Signal

**Frozen independent derivative (Gates 1–4).** Single UTC-aligned, consecutive **86,400-second** Binance BTC-USDT spot OHLCV stream. Each bar `t` is labeled by its open timestamp `T[t]`; its complete OHLCV is available for decisions only at `T[t]+86400`. No other asset, time frame, order-book, or non-OHLCV feed.

- `SMA30[t] = mean(close[t-29..t])` (exact 30-bar window, no recursion seed).
- `ATR10[t]` = Wilder RMA of true ranges over 10 bars (`max(high-low, |high-close[t-1]|, |low-close[t-1]|)`), seeded by the SMA of the first 10 true ranges; `RSI3[t]` = Wilder RSI over 3 closes, seeded by the SMA of the first 3 gains/losses. Both seeds are researcher-pinned here and absorbed by the warmup below — disclosed, never source prose.
- `DOW[t]` = UTC weekday of `T[t]` (Monday…Sunday); `MON[t]` = UTC calendar month of `T[t]`.
- **Entry, only if FLAT on a bar with `DOW[t] == Monday` and `MON[t] != 5`:** `close[t-1] < SMA30[t-1]` **and** `RSI3[t-1] < 51` **and** `close[t-1]/ATR10[t-1] < 95` (all strict; a print landing exactly on a threshold is not an entry). On entry create one simulated MARKET BUY of **0.001 BTC**.
- **Exit, only if LONG on a bar with `DOW[t] == Wednesday`:** close the full `0.001 BTC` with one simulated MARKET SELL. Later Wednesday bars while FLAT are no-ops; a week whose Wednesday bar is missing/invalid carries the position to the next valid Wednesday-completed bar (never an invented fill).
- **Same-bar exclusivity:** a bar cannot be both Monday and Wednesday, so entry and exit are mutually exclusive on one bar by construction. Exactly one action maximum per bar; no reversal, no same-bar entry/exit.
- **State machine:** initially FLAT; first eligible decision after **60 consecutive valid completed 1d bars**. After a filled exit, the next eligible later Monday may re-enter without cooldown; repeated eligible Mondays while LONG are no-ops (single-position posture carried over from the single-`"Buy"`-id source).
- **Position/risk:** one spot LONG or FLAT, no short (the source ships no short leg — source-native, not an adaptation), leverage 1, no margin, no pyramiding (Pine default `0` plus flat-gated entries), no DCA, no safety orders, no concurrency, no partial orders/fills, no portfolio allocation, no stop loss, no take profit, no trailing stop, no time exit beyond the Wednesday leg, no liquidation, no maker/limit/intrabar orders, no forced final-bar liquidation. If LONG at end of dataset, hold 0.001 BTC and mark at last valid close without inventing a terminal SELL. No capital compounding.
- **Input validity:** every bar must have expected UTC 1d open-time spacing, finite positive O/H/L/C, `high >= max(open,close)`, `low <= min(open,close)`. Invalid/missing candles reset the 60-consecutive-bar warmup and suppress both entry and exit until 60 new contiguous valid completed candles; existing LONG exposure remains held, not liquidated at an invented fill. No forward filling, no price substitution, no silently spanning gaps. Indicator windows and `[1]` refs must be wholly within the current valid segment.

## Required data

Single Binance BTC-USDT spot 1d OHLCV series with exact open timestamps; calendar rails (`DOW`, `MON`) are pure functions of those timestamps — no external calendar feed. `close` drives SMA/RSI and the ATR-ratio numerator; `high`/`low` feed ATR only; `open` feeds solely the validity gate; `volume` is read by no line. 30 completed bars for the first SMA value plus 1 prior bar for the `[1]` refs, plus margin: the conservative 60-bar consecutive warmup covers the Wilder RSI/ATR seeds as well. No cross-symbol synchronization, external model, training, future extrema, funding series, or secondary time frame.

## Execution assumptions

- **Pinned admission identifiers:** Hummingbot policy package label `20260920`, repository `hummingbot/VERSION=dev-2.17.0`; inspected **HCH725/hummingbot** at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (raw files read line-level this cycle, 2026-10-25). These are separate identifiers; no setup.py distribution version is claimed as a build digest or deployed-package proof. The claim is bounded to **the pinned commit's research simulation semantics**, not an installed container.
- **Actual data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` explicitly lists `1d`; `binance_spot_candles.py` line 82 parses Binance Kline `row[0]` as timestamp and `row[1..5]` as O/H/L/C/V. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` processes rows through `update_state(row)` (`close_bt` pricing, lines 364–366) and `controller.determine_executor_actions()` with `CreateExecutorAction` routed to `simulate_executor` (lines 284–287). A strategy-specific controller/feature implementation **does not yet exist**; it must calculate the declared SMA/RSI/ATR formulas, derive UTC weekday/month from bar open timestamps, and preserve entry-conjunction, state, and validity rules, rather than claim that the generic engine already contains this strategy.
- **Fill model:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` handles `ExecutionStrategy.MARKET` with the first supplied row's timestamp as fill time (lines 22–24) and that row's `close` as full-fill price (line 56), `filled_amount_quote = Q * close` (lines 59–60), `cum_fees_quote = trade_cost * filled_amount_quote` (line 62), and `CloseType.POSITION_HOLD` (lines 67–70). The intended controller issues exactly one `CreateExecutorAction` with `OrderExecutorConfig` for Binance BTC-USDT, `MARKET`, BUY/SELL, `Q=0.001 BTC`, leverage 1; the controller must maintain an immediate filled-position state rather than rely on delayed `positions_held` conversion to suppress duplicate orders.
- **Effective time and causal restriction:** the raw `timestamp_bt` is a **bar-open** label. The engine uses backward `merge_asof` and `dropna` in feature preparation (lines 466–478), which **alone do not establish data availability**. The required strategy-specific implementation must expose the current OHLCV only after the completed bar and normalize both effective decision and research fill event to `T[t]+86400`, while using the declared same-row close simulator fill. Entry additionally reads only `[1]`-lagged indicator values plus the current bar's calendar rails (knowable at its open), so the close-time evaluation is a causal superset — no future leakage. This is a **simulation convention**; it does not assert that a real order submitted after observing the Monday close can execute at that exact close. A future deployment requiring next-open/intrabar/maker realism is a new, separately verified engine path.
- **Costs and position ledger:** fix research `trade_cost=0.001` (**0.1% per filled side**), full fill `Q=0.001 BTC`, with modeled BUY cash outflow `Q*P_buy*(1+0.001)` and SELL inflow `Q*P_sell*(1-0.001)`. Compute realized net PnL as gross matched SELL–BUY less **both** fill fees; mark open BTC at last valid close, carrying already paid buy fee. The source-declared 0.035% commission and 100%-equity sizing are recorded above and **not** adopted — the 0.1% rate is a conservative researcher research-cost assumption, never a source fact. **Spot funding is not applicable**; no fictitious futures funding=0. The simulator has no separately applied slippage in this model; this means **zero modeled additional slippage**, not evidence of real zero slippage. Exchange min-notional/lot precision, partial fills, real spreads, latency, and realized commission are unverified and not represented as exchange-valid.
- **Reused representative capability:** admitted TradingView PR **#417** (ChartArt NR7, merged 2026-10-25) independently reviewed this exact pinned Binance spot 1d / MARKET-close / POSITION_HOLD research execution path, including fee-ledger limitations and event-time normalization; PRs **#421/#423** reviewed the same MARKET-close/POSITION_HOLD primitive, and PRs **#433/#435** (Coinrule MA100 dip; LazyBear TTF, both merged 2026-10-25) re-verified the identical 1d spot path on the same pinned commit. This is reusable **engine-path evidence only**, not proof that this new candidate was implemented, backtested, profitable, or Qlib/Hummingbot-parity tested. No novel execution primitive is introduced (UTC weekday/month arithmetic is deterministic controller logic over already-supplied bar timestamps, of the same kind as the admitted `monday-drift` and `sell-in-may` calendar records).

## Evidence

### Source-reported

FMZ `449948` page read 2026-10-25 (ChaoZhang authorship, muikol original-code credit, Turnaround-Tuesday rule prose; no performance numbers on the page). Immutable mirror file read 2026-10-25 (8,497 bytes, blob SHA pinned above: MA 30, RSI 3 < 51, close/ATR10 < 95, May exclusion, Monday entry / Wednesday exit, long-only, zero risk legs, MPL-2.0 muikol header). The mirror backtest stanza (`2h`/`15m`, Binance futures BTC, March 2024) and the 0.035%/100%-equity economics are recorded but fenced, never adopted.

### Independently reproduced

**None for this candidate.** The Gate-5 expressibility argument is static pinned-code inspection plus reusable independently reviewed engine-path evidence, not a strategy backtest, Qlib parity run, or independent reproduction of author metrics.

### Negative evidence

The source ships no stop/target/trailing of any kind — a Monday entry sliding through Tuesday realizes the full excursion until Wednesday; the record holds it unprotected by explicit source construction, never by omission. The `filter_2` (`close < 95×ATR10`) passes on virtually every modern BTC daily bar and bites only in detached/parabolic or dust-era tapes — carried verbatim, never tuned. The date-range inputs are dead code (`inTestPeriod = true`), so no window selection survives into the executable rule. Weekend (Sat/Sun) crypto bars exist but carry no order leg; Monday `[1]` refs therefore read Sunday values — deterministic, disclosed. Research fills/fees are not real-world order economics.

## Falsification plan

Only after separate downstream approval, freeze this identity and compare against (a) the same five-leg rule with the May exclusion removed, and (b) the same entry with a Tuesday-close exit instead of the Wednesday leg, each on predetermined IS/OOS partitions without OOS tuning. Any new engine primitive requires representative Qlib/Hummingbot event-level validation before mass Qlib screening. **No backtest or trading was performed in this Scout cycle.**

## Crypto portability

Current declared instance is Binance BTC-USDT spot 1d only, without a universe restriction as an HB_READY prerequisite. A different pair/frame, derivatives funding/margin model, or BO/SO campaign overlay is a separately specified derivative or downstream research experiment; none is silently incorporated here.

## Limitations

PASS in frontmatter is a **proposed six-gate research admission claim pending independent Hermes Auditor review**, not an auditor's decision. No lossless source-native equivalence is claimed for market, frame, fills, sizing, costs, timezone derivation, or Wilder seeds (all disclosed derivatives); no independently reproduced returns; no deployment build digest; no live fill precision or slippage validation; no Qlib parity; no survivor or production approval. Exact package identity remains a boundary; reviewer must not invent a package-to-commit mapping.

## Implementation status

`not-implemented`: strategy-specific controller and data-gap/feature logic are not committed or deployed. Pinned simulator primitives were read only.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. This record does not authorize Paper, Testnet, Live, Qlib/Hummingbot backtests, n8n, containers, cron, or other runtime changes.

## Related Wiki records

None asserted.

## Sources

- https://www.fmz.com/strategy/449948 — ChaoZhang, public strategy page read 2026-10-25 (title/authorship/muikol-credit prose; no performance numbers).
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/周二反转策略周末过滤-Turnaround-Tuesday-Strategy-Weekend-Filter.md — immutable mirror file read 2026-10-25 (8,497 bytes, blob `1170a6fe23210607a8ab62d525d2d44d23ad97b9`, full Pine v5 block).
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source read via raw-file fetch this cycle.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — previously independently reviewed same 1d spot research execution primitive (merged 2026-10-25).
