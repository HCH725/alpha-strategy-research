---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PSY12 sentiment-cross contrarian long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-01
sources:
  - https://algogene.com/community/post/477
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PSY12 sentiment-cross contrarian — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary source (fetched live over HTTPS this cycle, HTTP 200, 82,035 bytes):** ALGOGENE community tutorial **`https://algogene.com/community/post/477`**, title "Build Your First Sentiment Strategy: Psychological Line (PSY) in Python on ALGOGENE", author **TingTing**, `datePublished` `2026-10-01` (both read from page metadata this cycle). Source market is pinned in prose and code: long-only **BTCUSD on daily bars**, "It does not short". The page carries zero adopted performance figures — its backtest section is instructional ("Check the cumulative P&L chart … before you change anything") with no numbers.

**Order-affecting logic (full Python `AlgoEvent` class on the page, cited with short literals only):** parameters `myinstrument = 'BTCUSD'`, `timeperiod = 12`, `num_bar = 14`, `psy_buy = 30`, `psy_sell = 70`, `volume = 0.01`, `max_hold_days = 20`, `sl_distance = None`, `tp_distance = None`, state `net_pos = 0  # +1 long / 0 flat`. Indicator `PSY_cal` counts strict up-closes (`if prices[i-j] > prices[i-j-1]`) over the window, returns `100.0 * up / timeperiod`, with the first `timeperiod` slots `None` (warm-up). Decision callback evaluates once per daily timestamp (debounced by `last_tradeTime`), skips when history is shorter than 14 bars or either of the last two PSY values is `None`, then: `buy_signal = PSY[-2] > psy_buy and PSY[-1] < psy_buy` (cross DOWN through 30); `sell_signal = PSY[-2] < psy_sell and PSY[-1] > psy_sell` (cross UP through 70); `if net_pos == 0 and buy_signal: open_position(1, price)` / `elif net_pos > 0 and sell_signal: close_position()`. Orders are `ordertype = 0  # market` with `volume`, stamped `holdtime = max_hold_days * 24 * 3600` seconds when `max_hold_days > 0` (platform auto-close after N days); stop/target legs are attached only when not `None`, and both ship as `None`. Position state syncs from the platform (`net_pos` 1/0/−1) so a filled buy cannot double-buy.

**Stale-comment fence (non-operative, never adopted):** the two signal lines carry outdated trailing comments ("cross down through 15" / "cross up through 85"). The operative facts — `psy_buy = 30` / `psy_sell = 70` in `__init__`, the `>30`/`<30` and `<70`/`>70` comparisons, and the prose ("crosses down through 30", "crosses up through 70", "Start with the defaults: timeperiod = 12, psy_buy = 30, psy_sell = 70") — agree unanimously on 30/70. Any 15/85 reading is unpinned.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the page's venue is ALGOGENE BTCUSD with streaming-market fills, platform-seconds holdtime, an NAV-broke halt, and no stated fee model. Researcher-declared adaptations are exactly seven: (1) venue port to **BTCUSDT Binance spot** (same daily-bar close-sign arithmetic, disclosed); (2) close-decided signals filled **next-bar-open MARKET** (research-model timing convention, never a live-engine claim) replacing streaming `lastPrice` market orders; (3) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed) — the source states no fee/slippage figure; (4) **300-bar warmup** with pre-warmup bars flat (source minimum is 14 bars with a `None`-guard; PSY(12) has finite 12-bar memory so any warmup ≥ 14 prints the identical post-warmup event set — the 300 margin is convention, fenced); (5) time-exit translation: the source's `20×86400`s platform holdtime becomes exit-at-next-open once **20 completed daily bars** have elapsed since the entry bar (calendar bars count, gaps included — the faithful bar-grid rendering of seconds-since-fill); (6) the source's NAV≤0 halt has no equivalent — fills are **unconditional** (research-model convention, disclosed); (7) the fixed `0.01` lot is retained numerically as **0.01 BTC** (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above verified 5-USDT min-notional and 0.00001 min-qty, step-exact).

**Immutable derivative identity:** `ALGOGENE:post477-TingTing|psy12_strict-count_30-crossdown_70-crossup_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|timeexit20d|warmup300|2026-11-04`. Changing any window, threshold, cross sense, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@b0d0908d` (553 root strategy records, READMEs excluded; this file is the 554th). Filename search for `psy` returns zero signal records (the single prose hit is a dedup paragraph inside an unrelated Harami record, fenced below). Whole-word content search for a PSY rule returns zero records; `psy_buy` / `psy_sell` / `PSY_cal` return zero records. No open `research/*` PR is this file, author, construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Prior closed PR #439 ("TradeMan PSY12 70-30 flip", FMZ digest-topic/10257, closed NOT_LOSSLESS 2026-10-25) is a different source with a different rule (70/30 level-hold flip with discard-state gap handling, fenced in Negative evidence 11) — not this record, not in `main`, not open. Five-axis distinction vs nearest pool neighbors: different input and event vs all RSI/stochastic band records (smoothed magnitude oscillators with level-hold states, never a strict close-sign count, never cross-only events); different math vs AR popularity #741 (30-day H/O/L positional ratio level-band vs 12-close sign-count cross machine); different construction vs all streak/count records (run-length or streak-gated states vs windowed up-day frequency with cross-through gating); different data vs all volume-flow records (this rule reads zero volume); different mechanism vs all MA/ATR-trailing flip records (no average, no band, no trailing stop). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

PSY measures crowd mood as the market's recent win rate: the percentage of bars in the lookback that closed above the prior close. 50% means up/down closes balance; 75%/25% mark conventional extremes on the 12-bar setting. Every bar votes equally regardless of size, so the line is deliberately blind to magnitude — twelve small up closes score higher than eleven large ones — isolating persistence, which magnitude-weighted gauges blur together, while staying robust to single outlier candles (at most one step each).

### Research interpretation

Unlike pool oscillators that weigh move sizes (RSI's averaged gains/losses, stochastics' range position, AR's summed reaches), this machine trades pure persistence: it buys only when pessimism *accelerates through* the 30 line (a cross, not a level — sitting below 30 without a fresh cross emits nothing, the source's anti-spam design) and holds through stretched optimism until optimism *accelerates through* 70, with a 20-day time stop as the only backstop. The economics ported to BTCUSDT spot daily bars is a bounded contrarian-scalp claim fenced as a limitation, with no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other window, threshold, cross sense, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series: `C[t]` is the sole signal input via strict comparisons. `H[t]`/`O[t]`/`L[t]` are validity and fill-economics only (fills price at opens; notionals reference closes). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- R3 — PSY composite (source function, frozen): `PSY[t] = 100 × (#{i ∈ [t−11, t] : C[i] > C[i−1]}) / 12`. One value needs 13 closes; a cross pair needs 14. Values are 1/12-quantized in [0, 100].
- R4 — Events (source comparisons, strict inequalities pinned): `Buy[t] = (PSY[t−1] > 30 ∧ PSY[t] < 30) while FLAT`; `Sell[t] = (PSY[t−1] < 70 ∧ PSY[t] > 70) while LONG`. Branch order follows the source `if/elif` (buy branch first); both signals on one bar are arithmetically impossible (`PSY[t]` cannot be both `<30` and `>70`), and state gating would separate them regardless. Equalities hold (`==30` / `==70` never triggers). Mere residence below 30 or above 70 without a cross emits no event. At most one fill decision per bar by construction.
- R5 — Position (source machine): `LONG`/`FLAT` single-unit book. If FLAT and `Buy[t]` (post-warmup) → request LONG at the next open. If LONG and `Sell[t]` → exit the whole book at the next open.
- R6 — Time exit (source `max_hold_days = 20`, bar-grid translation): let `entry_bar` be the bar whose open filled the entry. At the first decision close with `(t − entry_bar) ≥ 20`, exit the whole book at the next open. Calendar bars count, including gap-frozen ones (rendering of seconds-since-fill). A bar where both Sell and time-exit apply prints a single whole-book exit (identical outcome).
- R7 — Risk legs (pinned source defaults, not invented): stop-loss and take-profit are `None` — explicitly disabled. No trailing, no other exit. The 20-day time exit (R6) is the sole backstop, exactly as shipped.
- R8 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none. No pyramiding: while LONG no new Buy can add (entry needs FLAT). No cooldown: after any exit, a fresh cross may re-enter at the next signal. Fills are unconditional (adaptation 6). Invalid bars (nonfinite/non-positive OHLC) emit no signal — explicit hold. Missing-bar stretches freeze evaluation at the prior target — the LONG book, its `entry_bar`, and ledger are retained across the freeze; evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat. This single path admits no reset-to-FLAT/pyramiding ambiguity by construction.
- R9 — Warmup: flat until 300 completed `1d` bars (convention margin over the source 14-bar minimum; finite 12-bar memory ⇒ any warmup ≥ 14 prints the identical post-warmup event set, fenced).
- R10 — Invariant identifier: `ALGOGENE:post477-TingTing|psy12_strict-count_30-crossdown_70-crossup_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|timeexit20d|warmup300|2026-11-04` (any window, threshold, cross sense, direction, sizing, fill, time-exit, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `close` (sole signal input), `open` (fills), `high`/`low` (validity only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used. Every live input is frozen at the decision close — point-in-time clean.
- Warmup: flat until 300 completed bars (structural). No repainting (all inputs read closed-bar closes only over a fixed 12-bar window; finite memory, no recursive seed), no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (source strategy never sells short). Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03 — the 11-04 bar was still forming at cycle time — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (local checkout `2dbc844fadb9d863b3ab0af1b8ab100472102e42` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. The 12-bar strict-count plus cross-gated state machine with a bar-counted time exit is a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The live page ships every adopted headline fact quoted in Provenance: the strict-count PSY formula with the `None`-slot warm-up, `timeperiod = 12` / `num_bar = 14` / `psy_buy = 30` / `psy_sell = 70` / `volume = 0.01` / `max_hold_days = 20` / `sl_distance = None` / `tp_distance = None` defaults, the `PSY[-2] > 30 ∧ PSY[-1] < 30` buy-cross and `PSY[-2] < 70 ∧ PSY[-1] > 70` sell-cross with the `if net_pos == 0 / elif net_pos > 0` state machine, market `ordertype = 0`, seconds `holdtime` on open orders, tradeID-tracked closes, the once-per-bar debounce, the 14-bar and `None` guards, the long-only BTCUSD-daily framing with no short path. It ships zero performance figures — none adopted; all frozen trading semantics beyond the machine are researcher pins disclosed above.

### Independently reproduced

No strategy-level independent reproduction: no strategy backtest, no event-level Qlib/Hummingbot parity, no live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. Researcher formula-sanity probe only (2026-11-04, disclosed, not strategy evidence): PSY(12) recomputed with the source-exact algorithm from live Binance BTCUSDT `1d` klines prints finite 1/12-quantized in-range values over completed bars only (trailing 41.67, 33.33, 41.67, 41.67, 33.33, 41.67; latest cross pair 33.33 → 41.67 emits no event under R4), confirming the composite is computable on the pinned grid; no trade event, fill, or performance inference is drawn from it.

### Negative evidence

1. Stale-comment fence: the in-code "through 15" / "through 85" comments contradict the operative 30/70 params, comparisons, and prose; this record follows the operative facts only. An implementation trading 15/85 prints a different, unpinned event set.
2. Equality fence: `PSY == 30` never buys and `PSY == 70` never sells (strict inequalities pinned). An implementation using `<=`/`>=` prints a different, unpinned event set.
3. Mutual-exclusion fence: both cross signals on one bar are arithmetically impossible, and the source `if/elif` order plus state gating are pinned regardless. An implementation evaluating sells while FLAT (or buys while LONG) prints a different, unpinned event set.
4. First-signal fence: the machine is cross-based — the first post-warmup bar needs a valid two-value PSY pair, and residence at an extreme without a cross never enters. Absorbed by the warmup; shorter warmups print different early event sets and are unpinned.
5. Window-minimum fence: one PSY value needs 13 closes, a cross pair 14; the 300-bar warmup strictly dominates. Any warmup < 14 prints a different, unpinned early event set.
6. Time-exit translation fence: the source counts platform seconds from order; this record counts 20 completed calendar bars from the entry bar (gaps included). Any other counting (evaluated-bars-only, 20 signals, trailing 20 closes) is unpinned.
7. NAV-halt fence: the source skips decisions when platform NAV ≤ 0; this record has no equivalent and fills unconditionally. A broke-account halt is a different, unpinned rule.
8. Threshold-tunability fence: the page invites tweaking one parameter at a time — this record freezes the shipped 12/30/70/20 set anyway; any retuned set is a different, unpinned derivative.
9. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
10. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (venue port, next-open fills, 0.1% cost overlay, 300-bar warmup, bar-counted time exit, unconditional fills, retained 0.01 sizing); the count formula, 12-window, 30/70 pair, cross senses, state machine, market-order type, 20-day backstop, and disabled stop/target are source-faithful. This record is therefore never evidence that any author strategy passes.
11. Prior-closed-PR fence: closed PR #439 used FMZ digest-topic/10257 (TradeMan) with 70/30 level-hold flip semantics plus discard-state gap handling and was closed NOT_LOSSLESS on Gate 4 gap-state ambiguity. This record uses a different primary source (ALGOGENE post/477), a different event (cross-through, not level-hold), and single-path freeze gap semantics with no discard-state (R8). Nothing from #439's review is relied upon or re-litigated here.
12. Page-drift fence: this record follows the page content as fetched 2026-11-04 (published 2026-10-01). If the page is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: PSY(12) strict-count / cross-down-30 buy / cross-up-70 sell / long-only / no-stop-no-target / 20-bar time exit / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 300-bar warmup are frozen.

- F1 — Cross relevance: a level-hold twin (enter FLAT when PSY<30, exit LONG when PSY>70, same rest) must not improve net expectancy; fail ⇒ cross gating adds nothing over level residence.
- F2 — Window relevance: a PSY(24) twin (same rest) must not improve net expectancy; fail ⇒ the shipped 12-bar window carries no information.
- F3 — Band relevance: a symmetric 50-cross twin (buy FLAT on cross-up through 50, exit LONG on cross-down through 50, same rest) must not improve net expectancy; fail ⇒ the published 30/70 contrarian asymmetry is decoration.
- F4 — Warmup relevance: a 350-bar-warmup twin must print the identical post-350 event set (finite 12-bar memory ⇒ structural identity is expected); fail ⇒ seed or ramp transients leak past the declared warmup.
- F5 — Exit relevance: a no-time-exit twin (PSY-sell exits only, same rest) must not improve net expectancy; fail ⇒ the 20-day backstop adds nothing over signal-only exits.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; close-only signal input — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously so no equity-calendar port artifact). The source venue is ALGOGENE BTCUSD daily; the Binance spot port is a disclosed researcher adaptation. Extension to other house-universe assets, timeframes, windows, thresholds, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The page is © ALGOGENE / its author (cited with short literals only, never copied in bulk); the venue port, next-open fills, warmup, bar-counted time exit, unconditional fills and cost overlay are researcher adaptations disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- The source's own limitation transfers: PSY is magnitude-blind by design (twelve small up closes outscore eleven large ones) and extremes can peg in trends — the cross gate mitigates spam but a cross can still fire repeatedly in choppy tape; thresholds are shipped defaults frozen here without tuning.
- Cross-equality handling, first-signal pairing, gap freezing, time-exit counting and the stale 15/85 comments are implementation-defined (Negative evidence 1–6, 12); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (300) is a researcher margin at 25× the frozen window 12; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://algogene.com/community/post/477 ("Build Your First Sentiment Strategy: Psychological Line (PSY) in Python on ALGOGENE", author TingTing, datePublished 2026-10-01; HTTP 200 verified this cycle, 82,035 bytes fetched 2026-11-04; strict-count PSY(12) formula, 30-cross-down buy / 70-cross-up sell machine, long-only BTCUSD daily framing, 0.01 sizing, 20-day holdtime, None stop/target — cited with short literals, never bulk-copied)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (TRADING; `PRICE_FILTER tickSize 0.01`; `LOT_SIZE minQty/stepSize 0.00001/0.00001`; `NOTIONAL minNotional 5.0`; last completed daily close 77,453.86 on 2026-11-03; the 11-04 bar was still forming and no provisional value is used)
