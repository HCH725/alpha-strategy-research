---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradersPost Raschke 80-20 wide-bar climax-fade two-sided on BTCUSDT 4h bars
created: 2026-11-02
updated: 2026-11-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-07-23
sources:
  - https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/raschke-patterns.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 80-20 wide-bar climax-fade + avg-price 2%/4% box — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `TradersPost/pinescript-agents` commit **`ebc382f88b6103fcda2569fe666a38b00fe714c5`** (2026-07-23T20:22:51Z — still the repo HEAD, verified live this cycle via the commits API), file **`projects/raschke-patterns.pine`**, blob `b6d473b8b7f6bfb3538471f5a786cd3c228778db` (contents API at the pinned ref, size 27536), **27,536 bytes / 506 lines**, Pine v6 (`//@version=6`), `indicator("Raschke Patterns", ...)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `92287b6fde409d57539878b07a5b615b0d926abf9b4cfcb0ca17ae720a8f08ce`, byte-identical to the working copy. Permalink above. This is the same file the admitted Turtle-Soup sibling (#701) was ported from; that record explicitly fenced the 80-20 family OUT, so none of its predicates is pinned there.

**Order-affecting logic read verbatim (code governs; indicator ships no orders):** bar range `rng = high - low` (line 134); ATR `atrVal = ta.atr(atrLen)` (line 135; `atrLen = input.int(14, ...)` default 14, line 83); intrabar locations `locOpen = rng > 0 ? (open - low) / rng : 0.5` / `locClose = rng > 0 ? (close - low) / rng : 0.5` (lines 163–164); wide gate `wideOK = not wide8020 or rng >= atrVal * wideMult` (line 165; `wide8020 = input.bool(true, ...)` default true, line 76; `wideMult = input.float(1.5, ...)` default 1.5, line 80); setups `is8020Bull = en8020 and wideOK and locOpen >= 0.8 and locClose <= 0.2` (“Opened high / closed low → potential UP reversal (bullish setup)”, line 167) and `is8020Bear = en8020 and wideOK and locOpen <= 0.2 and locClose >= 0.8` (“Opened low / closed high → potential DOWN reversal (bearish setup)”, line 169); `en8020 = input.bool(true, "80-20 Bar", ...)` default true (line 57). Header doctrine (lines 12–13): “80-20 Bar — opens within 20% of one extreme, closes within 20% of the other (reversal expected the OPPOSITE way)”; `TIP_8020` expectation: “A fade setup — look for a reversal the opposite way on the next bar. Tag above the bar = watch for a move down; below = watch for up.” Bull tag plots `location.belowbar`, bear tag `location.abovebar` (lines 346–347, 361–362).

**Pine-block census (this cycle, over the pinned bytes):** 1 `indicator(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 0 `request.*` / 0 `security(` / 0 `input.session` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` — all recorded as absent, never filled in; `timeframe.period` appears only inside alert/log display strings (lines 469, 486), never in signal math (disclosed); per-bar `alert()` uses `alert.freq_once_per_bar_close`; Pine Logs writes are gated on `barstate.isconfirmed`; the file's own header warns “detections use the bar's CLOSE; on the live (forming) bar a signal can appear/disappear until the bar closes” and states “All patterns use the chart timeframe” (chart-agnostic, no market pinned). The 80-20 legs join the shared `sigBull`/`sigBear` marker ORs only (lines 293–294, display triggers, never orders — disclosed). All markers/plotcandle/boxes/lines/legend/table/recolor/display-only inputs are dropped, disclosed. The other eight pattern families in the file (Turtle Soup, TS+1, Inside Bar, FIB, ODUP/ODDN, NR4/NR7, Bar Gap Reversal, Holy Grail) are explicitly fenced OUT — none of their predicates, state, or parameters is pinned here (disclosed). No LICENSE file ships in the repo — short-literal citation only, no source block reproduced.

**Structural facts carried over exactly:** (a) single-bar open/close location within the bar's own range (no multi-bar extreme memory); (b) the 1.5× ATR-14 wide-range climax gate at source defaults; (c) strict 0.8/0.2 location thresholds with the rng-zero → 0.5 neutral pin; (d) bull-setup = climactic down-bar expecting UP (long side), bear-setup = climactic up-bar expecting DOWN (short side); (e) no MTF, no session/timezone, no gap dependence, no intrabar semantics anywhere in the ported legs.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the two source 80-20 setup predicates to two-sided fade entries on confirmed bars (disclosed promotion, same strict semantics and polarity); (2) latched avg-price −2%/+4% box with reversal-dominate stop-first resolution (fully researcher-designed risk/state — the source has no exits; disclosed); (3) fixed **0.01 BTC** sizing (≈785.9 USDT at probe close 78,593.3, above verified 50-USDT min-notional and 0.001 min-qty; 10,000 USDT cash; Isolated 1×); (4) 100-bar warmup with pre-warmup bars flat (14 = structural ATR scale, +86 researcher margin for RMA convergence); (5) display drop (markers, candles, boxes, lines, legend, table, alerts, logs); (6) constant fence (0.8/0.2/1.5/ATR-14/two-sided/box-on — any other value is a different unpinned rule); (7) explicit **0.05%/side research cost**, slippage unmodeled (disclosed); (8) close-decided entries filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (the source's close-decided intent preserved; the intrabar-instability warning is answered by pin, disclosed).

**Immutable derivative identity:** `GH:TradersPost-ebc382f|raschke-8020-wide1.5-atr14_loc0.8-0.2_fade_SL2-TP4-avgpx-latched|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|reversal-dominate-stopfirst|warmup100|2026-11-02`. Changing any formula, length, multiple, threshold, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Climactic single-bar exhaustion fade (Raschke short-term setup): a wide-range bar that opens near one extreme and closes near the other fills ~80%+ of its range — the move expended itself inside the bar, so price often reverses the other way next. The file's expectation is an explicit fade: tag below a down-bar watches for up, tag above an up-bar watches for down.

### Research interpretation

Unlike the Turtle-Soup sibling ported from the same file (prior-20 extreme sweep plus reversal close with a 4-bar age gate — a two-bar multi-window level event), this machine keys off **single-bar anatomy**: where the bar opened and closed inside its own range, gated on range-vs-ATR climax. No extreme is swept, no age is tracked, no prior window exists — the only memory in the signal is the ATR-14 denominator. Unlike pool cross/trend records there is no line, no cross, no band, and unlike pool breakout records there is no level to break: the bar's own shape is the signal and 1.5× ATR is the only threshold. The pool contains **zero** 80-20 records at the pre-write snapshot — this is a fresh signal family, not a parameter variant of anything admitted. Live-window rate is 51 post-warmup predicate bars per 1,399 4h bars (25 bull / 26 bear), with 10 of 41 closes coming from opposite-setup reversals — the fade-and-reverse character is structural, not tuned.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals/anchors/closes, `H[t]`/`L[t]` for range/box-touch legs, `O[t]` for locations/fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All constants are source-default literals.

- **ATR-14 (causal, Pine-faithful):** `TR[t] = max(H-L, |H-C[t-1]|, |L-C[t-1]|)` (first bar `H-L`); `ATR` is the RMA(14) of TR seeded with the SMA of the first 14 TRs (researcher seeding pin — Pine `ta.atr` is RMA-based; the 86-bar warmup margin renders seeding immaterial post-warmup, disclosed).
- **Predicates (actionable only t ≥ 100, at bar `t`'s close):** `rng[t]=H[t]-L[t]`; `locO[t]=(O[t]-L[t])/rng[t]`, `locC[t]=(C[t]-L[t])/rng[t]` (rng-zero bars pin both to 0.5, neither fires); `wide[t]=rng[t]>=1.5*ATR[t]` (non-finite ATR fires nothing); `bull[t]=wide and locO>=0.8 and locC<=0.2` → LONG setup; `bear[t]=wide and locO<=0.2 and locC>=0.8` → SHORT setup. Pre-warmup bars flat by record rule; every na/degenerate bar is an explicit neither-fire hold. Bull and bear can never co-fire (one `locO` value cannot satisfy both ≥0.8 and ≤0.2; rng-zero pins 0.5/0.5) — proven, no tie-break needed.
- **Latched box (researcher-designed, fixed at fill-average `A`, never moved):** long `SL=A×0.98`, `TP=A×1.04`; short mirrored `SL=A×1.02`, `TP=A×0.96`.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite setup first (reversal dominates, old box dies), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Single position, no adds: same-side refire is a no-op.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous valid completed 4h bars; covers the 14-bar ATR structural scale plus an 86-bar researcher margin for RMA convergence (disclosed). No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; forming-bar drop verified live this cycle). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (researcher once-per-bar pin answering the source's own close-warning; `alert.freq_once_per_bar_close` + `isconfirmed` logs show the source's close-decided intent, disclosed); fills at next-bar open; SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention, disclosed). No incomplete bar, future extremum, repainted graphic, MTF call, session template, gap state, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session, no second symbol, no gap feed). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the two 80-20 location predicates with the ATR wide-gate, the new-position avg-price 2%/4% latch, and the reversal-dominate stop-first state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈785.9 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided box legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 506-line fence ships the complete 80-20 construction: the 0.8/0.2 location arithmetic with the rng-zero 0.5 neutral pin, the 1.5× ATR-14 wide gate at source defaults, the bull/bear polarity with the stated fade expectation, and the close-decided alert/log intent. It ships no orders, no sizing, no exits, and no performance figure of any kind — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/latch/state pipeline (Pine-faithful locations, ATR wide-gate, avg-price latch, code-order reversal-dominate stop-first resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** MICRO-SL tape prints 2 post-warmup bull legs driving 1 open / 1 SL close ending flat (digest `17468ba73fb7b7c4`); MICRO-TP tape prints 1 bear leg driving 1 open / 1 TP close ending flat (digest `97430c4e9d1331eb`); MICRO-REV tape prints 1 bull / 1 bear driving 1 open / 1 reversal close ending short-held (digest `6a4e6ba56322224a`).

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,499 completed bars 2026-02-25→2026-11-02, last close 78,593.3):** 25 post-warmup bull and 26 post-warmup bear predicate bars drive 41 entries (31 fresh + 10 reversals) / 41 closes (26 SL-touch / 5 TP-touch / 10 reversals) ending FLAT (digest `291a5191721b1794`); sub-window bars 300–999 print 12 bull / 11 bear driving 19 entries / 18 closes (11 SL / 2 TP / 5 reversals) ending LONG, same honest cut (digest `5fd431ec986b90e2`). 0.01 BTC ≈ 785.9 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@a2a11e2a`, the root Git tree contained **516** strategy Markdown records (518 files minus two READMEs). Exact-identity working-tree searches for `8020` / `80-20` / `eighty` return **zero** records (the only `80-20` prose hits are fence mentions inside the Turtle-Soup sibling and the wick-reversal record — never a traded 80-20 system; the sibling's own dedup paragraph confirms the family was unpinned there). Fifteen open `research/*` PRs were inspected by per-PR title/head — no collision (nearest open lanes are EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams — none an 80-20 fade). Closed-PR scan surfaces only the #701 sibling. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen 80-20 box book against (a) no-box twins (pure setup-to-opposite-setup reversal — isolating the percent box), (b) wide-gate-off twins (0.8/0.2 locations without the 1.5× ATR filter — isolating the climax gate; researcher variation), (c) 1%/2% and 3%/6% box twins (isolating the 2R choice; researcher variation), and (d) location-threshold twins at 0.7/0.3 (isolating the 80-20 strictness; researcher variation — never attributed to source). Check event rate, SL/TP/reversal attribution, hold-time distribution, warmup sensitivity (100 vs 200), and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only. Stated plainly: the machine needs completed-bar OHLC plus the 100-bar admission warmup (ATR-bound); the entries are single-bar 80-20 climax fades with a live-window rate of ~51 predicate bars per 1,399 4h bars; the exits are a researcher-latched 2%/4% avg-price box with reversal dominance; 4h slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap dependence (the file's session-sensitive gap leg is fenced out, disclosed), so 24/7 crypto continuous trading introduces no Year-2024-style anchor or session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The indicator→strategy promotion, market/timeframe pin (source is chart-agnostic), sizing, cash, leverage, warmup, display drop, constant fence, 0.05% research fee, close-decided next-open resolution, and once-per-bar evaluation are researcher pins, never attributed to the source. The eight non-ported pattern families (TS, TS+1, IB, FIB, OD, NR4/NR7, gaps, HG) are fenced out — enabling any of them creates a different unpinned rule. The repo ships no LICENSE — this record cites short literal lines only and reproduces no source block; research-only use asserted, no commercial claim. Pine RMA seeding is adopted explicitly with an 86-bar convergence margin inside the 100 warmup. Entries read completed-bar closes only; SL/TP legs are close-decided against completed-bar H/L with next-open fills (research-model convention, disclosed). Probe windows end flat (full-window) and holding LONG (sub-window) — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/raschke-patterns.pine (commit `ebc382f88b6103fcda2569fe666a38b00fe714c5`, 2026-07-23, still HEAD verified live 2026-11-02; blob `b6d473b8b7f6bfb3538471f5a786cd3c228778db`; Pine v6, 506 lines / 27,536 bytes; raw sha256 `92287b6fde409d57539878b07a5b615b0d926abf9b4cfcb0ca17ae720a8f08ce` verified live 2026-11-02; no LICENSE — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,499 completed bars 2026-02-25→2026-11-02, 25 bull / 26 bear → 41 entries / 41 closes, plant digests `17468ba7`/`97430c4e`/`6a4e6ba5`, window digests `291a5191`/`5fd431ec`), fetched live 2026-11-02
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): Turtle-Soup sweep-fade sibling `github-traderspost-turtle-soup-sweep-fade-two-sided-btcusdt-4h-2026-11-02.md`; naked-cross `github-traderspost-ema921-naked-percent-box-two-sided-btcusdt-4h-2026-11-02.md`; Q-Trend-KVO confluence https://github.com/HCH725/alpha-strategy-research/pull/697
- Pine reference: v6 causal calls (`ta.atr`, close-decided legs), `alert.freq_once_per_bar_close`, `barstate.isconfirmed` log gating
