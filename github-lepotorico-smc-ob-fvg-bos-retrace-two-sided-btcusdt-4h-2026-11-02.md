---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LePotoRico SMC OB-FVG BOS-retrace OB-edge swing-exit two-sided on BTCUSDT 4h bars
created: 2026-11-02
updated: 2026-11-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-02
sources:
  - https://github.com/LePotoRico2105/pine-script-strategies/blob/e8bb2935b98ca446ad1063fb75a500410d344c5a/strategies/smc_ob_fvg.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SMC Order-Block + FVG BOS-retrace with OB-edge stops and swing exits — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `LePotoRico2105/pine-script-strategies` commit **`e8bb2935b98ca446ad1063fb75a500410d344c5a`** (2026-04-03 — still the repo HEAD, verified live this cycle), file **`strategies/smc_ob_fvg.pine`**, blob `4ca0960d633c345419d098ce56318fec2026e424`, **3,606 bytes / 109 lines**, Pine v5, `strategy("SMC Order Block + FVG", ...)` — a real strategy with native entries and exits, not an indicator. Raw bytes re-downloaded this cycle hash to sha256 `f37a7d87ce0daa7d291dae101a839adc2aec5fa325a15712818aa12318726cbf`, byte-identical to the working copy. Permalink above. Repo license is **MIT** — short-literal citation only, no source block reproduced.

**Order-affecting logic read verbatim (code governs):** source defaults `obLookback = 20` / `fvgMinSize = 0.5` (ATR multiple) / `atrLen = 14` / `bosLookback = 50`, with `obLookback` and `bosLookback` **declared but never referenced** in the body (dead inputs — fenced as inert, disclosed; the live constants are the hardcoded `2` ATR strong-move multiple, `0.5` ATR stop buffer, `30`-bar BOS recency and `20`-bar FVG persistence); ATR `atr = ta.atr(14)`; structure pivots on the once-shifted series `ta.pivothigh(high[1], 5, 5)` / `ta.pivotlow(low[1], 5, 5)` with last-swing latching and `close[1]`/`close[2]` BOS crosses; order blocks `bullOB = (open[2], close[2])` armed when `close[1] - open[1] > atr * 2` with `close[2] < open[2]` (mirrored bear); FVG `low[1] > high[3]` with size `> atr * 0.5` (mirrored bear) held by `ta.barssince(...) > 20` expiry; entries `longCondition = bullOBActive and recentBullFVG and low[1] in bullOB and barssince(bullBOS) < 30` (mirrored short); exits `strategy.exit(..., stop = OB edge ∓ atr * 0.5, limit = lastSwingHigh/Low)` with one-shot `bullOBActive := false` / `bearOBActive := false` on entry; opposite-direction `strategy.entry` reverses under Pine defaults (no `pyramiding` set — disclosed).

**Pine-block census (109-line fence):** 1 `strategy(`; 2 `strategy.entry` / 2 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`; 0 `request.*` / 0 `security(` / 0 `lookahead` / 0 `input.session` / 0 `timeframe.*` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` / 0 `process_orders_on_close` — all recorded as absent, never filled in. Default bar-close calculation (no intrabar engine) with every predicate reading `[1]`/`[2]`/`[3]`-shifted confirmed data only — the repo's "anti-repainting" header claim holds for the ported legs (verified by construction, disclosed as code fact, not adopted marketing). The README's backtest figures (win rates, profit factors, "10 years of M1" coverage) have no table/figure/section traceability in the pinned source and are **explicitly not adopted** — none appears below.

**Structural facts carried over exactly:** (a) BOS-gated structure context (entries need a break-of-structure within 30 bars); (b) the order block is the last opposite-body candle before a `>2×ATR` single-bar move; (c) the FVG is a 3-bar gap `>0.5×ATR` with 20-bar memory; (d) entries are retrace touches of the zone body on confirmed data; (e) stops sit `0.5×ATR` beyond the zone edge and targets are the last confirmed swing — both source-arithmetic, not researcher risk; (f) single chart, single timeframe, OHLC-only, no session/timezone/MTF anywhere.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the market/timeframe pin (source tested forex M15 per its README; this record pins Binance BTC-USDT futures 4h), fixed **0.01 BTC** sizing (source: 2% of equity), close-decided next-bar-open fills for the stop/limit legs (Pine fills `strategy.exit` stops/limits intrabar — the research-model timing convention differs, disclosed), flat-tie hold on same-bar dual fire (Pine would sequence two opposite entries — engine sequencing, not signal; researcher tie-break, disclosed), strict-uniqueness pivot-tie pin (below, disclosed), and the degenerate-geometry skip (below, disclosed) are researcher adaptations. All are completely specified here; original claims are kept separate above.

**Immutable derivative identity:** `GH:LePotoRico-e8bb293|smc-OB2ATR_FVG0.5-20b_BOS30b_OBedge0.5ATR_SL_swing-TP|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|entries-dominate-stopfirst-tiehold|warmup200|2026-11-02`. Changing any formula, length, multiple, recency, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Smart-Money-Concepts confluence: an imbalance leg (order block + fair value gap) marks where large size displaced price; a break of structure confirms the directional intent; the edge is entering on the retrace into the unmitigated zone with the stop beyond it and the target at the structure extreme that the displacement left behind.

### Research interpretation

Unlike pool FVG siblings — the FMZ two-bar range-gap **breakout** (`fair-value-gap-breakout-long-btcusdt-1h-2026-10-10.md`), the TagsTrading aged-zone **mitigation-recovery** long-only spot derivative, and the one-bar gap record — this machine never trades the gap itself: it trades the **retrace into an order-block body**, and only with a fresh FVG flag plus a fresh BOS behind it. Unlike pool reversal records that fade extremes, this follows the displacement after confirmation. The pool contains **zero** SMC order-block / BOS-confluence records at the pre-write snapshot — this is a fresh signal family, not a parameter variant. Live-window rate is extreme-selective by construction: 2 post-warmup predicate bars per 1,499 4h bars (1 bull / 1 bear), each producing exactly one round trip — the confluence is structural, not tuned.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals/anchors/closes, `H[t]`/`L[t]` for gap/zone/box-touch legs, `O[t]` for fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All constants are source-default literals.

- **ATR(14) (causal, per-bar):** Wilder RMA of true range, SMA-seeded over the first 14 TRs (researcher seeding pin — the 200-bar warmup renders seeding immaterial post-warmup, disclosed).
- **Structure pivots (causal, per-bar, Pine-faithful with one disclosed tie pin):** `swingHigh[t] = H[t-6]` iff `H[t-6]` is **strictly** greater than every other bar in `H[t-11..t-1]` (mirrored lows) — the strictness answers Pine's `highestbars/lowestbars` tie suppression (a non-strict `==` check phantom-fires on every flat bar; verified during self-check and rejected). `lastSH`/`lastSL` latch on confirmation, updated before BOS evaluation each bar (script order preserved).
- **BOS:** `bullBOS[t] = C[t-1] > lastSH and C[t-2] <= lastSH` (mirrored bear); recency `t - lastBOS < 30` (`na`-never counts as stale-false, source-exact `barssince` semantics).
- **Order blocks:** `strongBull[t] = C[t-1]-O[t-1] > atr[t]*2 and C[t-2] < O[t-2]` arms `bullOB = (O[t-2], C[t-2])` top/bottom (mirrored bear); one-shot — consumed (set absent) only by an actual entry.
- **FVG memory:** `bullFVG[t] = L[t-1] > H[t-3] and L[t-1]-H[t-3] > atr[t]*0.5` sets a flag consumed by `t - lastFVG <= 20` (mirrored bear).
- **Predicates (actionable only t ≥ 200, at bar `t`'s close):** `long[t] = bullOB and recentBullFVG and L[t-1] <= top and L[t-1] >= bottom and BOSfreshBull` (mirrored `short[t]`). Pre-warmup bars flat by record rule; every na/degenerate bar is an explicit neither-fire hold.
- **Source-arithmetic risk (latched at entry, never moved):** long `SL = bottom - 0.5*atr`, `TP = lastSH`; short mirrored `SL = top + 0.5*atr`, `TP = lastSL`.
- **Degeneracy guard (explicit researcher pin):** entries require non-`na` TP with `TP > C[t]` / `SL < C[t]` (long, mirrored short); otherwise neither-fire hold. Pine would submit `na`/inverted legs — the guard is disclosed and never attributed to source.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite setup first (reversal dominates: close then re-enter; tie bars keep box legs only), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Flat with both legs firing is an explicit neither-fire hold (researcher tie-break — constructible on wide-range bars, verified on tape). Single position, no adds: same-side refire is consumed with the zone (one-shot).

## Required data / Gate 6 causality

**Warmup:** minimum 200 contiguous valid completed 4h bars; covers the 12-bar pivot-confirmation lag, the 30-bar BOS recency, the 20-bar FVG memory and ATR(14) seeding plus researcher margin. No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; row[0] open-time parsing, 4h-boundary alignment verified live this cycle). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (every predicate reads `[1]`-or-older data except `atr[t]`, which is complete at bar `t`'s close); fills at next-bar open; SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention differing from Pine intrabar exit fills, disclosed). No incomplete bar, future extremum, repainted level, MTF call, session template, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `BacktestingEngineBase.run_backtesting` + `determine_executor_actions` in controller bases, `OrderExecutorSimulator` class byte-present in `backtesting/executors_simulator/order_executor_simulator.py`, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session, no second symbol). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the pivot/BOS/OB/FVG state machine with one-shot zones, the source-arithmetic latched stop/limit, and the entries-dominate stop-first tie-hold pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈785.9 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided level legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 109-line strategy ships the complete confluence: ATR(14) context, `[1]`-shifted 5/5 pivots with last-swing latching, `close[1]`/`close[2]` BOS crosses, `>2×ATR` order-block arming off the prior opposite body, 3-bar `>0.5×ATR` FVG flags with 20-bar memory, zone-retrace entries with 30-bar BOS recency, OB-edge `∓0.5×ATR` stops with swing targets, and one-shot zones. It ships no timeframe/market claim usable for futures (README says forex M15 — not adopted as a 4h/crypto claim), no sizing beyond 2%-of-equity (not adopted — fixed 0.01 BTC pinned here), and no performance figure of any kind — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/latch/state pipeline (Pine-faithful pivots/BOS/OB/FVG, source-arithmetic stops/targets, code-order entries-dominate stop-first tie-hold resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** MICRO-SL tape prints 1 bull predicate driving 1 open / 1 SL close ending flat (digest `1388ec6682d2c910`); MICRO-TP tape prints 1 bull predicate driving 1 open / 1 TP close ending flat (digest `70022bcb2e78e803`); MICRO-REV tape prints 1 bull / 1 bear predicate driving 2 opens / 1 reversal close ending short-held (digest `66ebace344c0da0c`); MICRO-TIE tape prints 1 bull / 1 bear predicate with a both-legs spanning bar driving 0 opens ending flat (digest `e3b0c44298fc1c14`). Tapes caught and fixed two genuine replication defects pre-write (non-strict pivot phantom-fires on flat ties; reversal-side selection) — the shipped logic is the fixed version, double-run identical.

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,499 completed bars 2026-02-25→2026-11-02, last close 78,593.3):** 1 post-warmup `LE` and 1 post-warmup `SE` predicate bar drive 2 state-machine opens / 2 closes (1 SL-touch / 1 TP-touch, 0 reversals) ending FLAT (digest `26f17623ce1d6dbc`); sub-window bars 300–999 print 1 `LE` / 1 `SE` driving 2 opens / 2 closes (1 SL / 1 TP, 0 reversals) ending FLAT, same honest cut (digest `b0970eae13394f3d`). 0.01 BTC ≈ 785.9 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@c5b48910`, the root Git tree contained **514** strategy Markdown records (516 files minus two READMEs). Exact-identity working-tree searches for `smc_ob` / `lepotorico` / `LePotoRico` / `orderblock` / literal `Order Block` (one hit — the TagsTrading FVG-mitigation record, four-axis distinct: different source, zone-mitigation vs OB-retrace+BOS signal, long-only spot 1h vs two-sided futures 4h) return **zero** same-construction records. Fifteen open `research/*` PRs were inspected by per-PR title/head — no collision (nearest open lanes are EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams — none an SMC OB+BOS confluence). Closed-PR scan surfaces no member of this family. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen SMC book against (a) no-BOS twins (zone+FVG retrace without the 30-bar structure-recency gate — isolating BOS; researcher variation), (b) OB-only / FVG-only twins (isolating each confluence leg; researcher variation), (c) 0.3×/1.0× FVG-size twins (isolating the imbalance threshold; researcher variation), and (d) swing-target vs fixed-2R twins (isolating the source-arithmetic exits; researcher variation — never attributed to source). Check event rate, SL/TP/reversal attribution, hold-time distribution, warmup sensitivity (200 vs 300), and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only. Stated plainly: the machine needs completed-bar OHLC plus the 200-bar admission warmup (pivot/BOS/FVG-memory bound); the entries are zone-retrace touches with a live-window rate of ~2 predicate bars per 1,499 4h bars; the exits are source-arithmetic latched stop/limit levels with reversal dominance and tie-hold; 4h slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap-regime dependence (the source is session-free; forex-to-crypto market change is a disclosed researcher adaptation), so 24/7 crypto continuous trading introduces no session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The market/timeframe pin (source tested forex M15 — not adopted), sizing (0.01 BTC vs 2%-of-equity), cash, leverage, warmup, display drop, constant fence, 0.05% research fee, close-decided next-open resolution (differs from Pine intrabar exit fills), tie-hold (differs from Pine same-bar order sequencing), strict-uniqueness pivot ties, float-exact zone comparisons, and the degenerate-geometry skip are researcher pins, never attributed to the source. The dead `obLookback`/`bosLookback` inputs are fenced inert — any rule using them is a different unpinned strategy. The README's backtest figures are rejected for lack of traceable provenance. Probe windows end flat — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. The live window's 2-event sample exercises SL and TP legs only; reversal and tie legs are exercised on planted tapes, not live tape. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/LePotoRico2105/pine-script-strategies/blob/e8bb2935b98ca446ad1063fb75a500410d344c5a/strategies/smc_ob_fvg.pine (commit `e8bb2935b98ca446ad1063fb75a500410d344c5a`, 2026-04-03, still HEAD verified live 2026-11-02; blob `4ca0960d633c345419d098ce56318fec2026e424`; Pine v5, 109 lines / 3,606 bytes; raw sha256 `f37a7d87ce0daa7d291dae101a839adc2aec5fa325a15712818aa12318726cbf` verified live 2026-11-02; MIT — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,499 completed bars 2026-02-25→2026-11-02, 1 LE / 1 SE → 2 opens / 2 closes, plant digests `1388ec66`/`70022bcb`/`66ebace3`/`e3b0c442`, window digests `26f17623ce1d6dbc`/`b0970eae13394f3d`), fetched live 2026-11-02
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Nearest pool lineages (different sources/mechanisms, unmerged-proof never claimed): FVG-mitigation `tradingview-tagstrading-fvg60-age20-mitigation-recovery-long-btcusdt-1h-2026-10-30.md`; FVG-breakout `fair-value-gap-breakout-long-btcusdt-1h-2026-10-10.md`; ChoCh-regime `fmz-446538-vector-candle-choch-count-long-flat-btcusdt-1h-2026-10-27.md`
- Pine reference: v5 `[1]`/`[2]`/`[3]`-shifted causal reads, `ta.pivothigh/low` confirmation lag, `ta.barssince` expiry idiom, default (non-intrabar) strategy calculation
