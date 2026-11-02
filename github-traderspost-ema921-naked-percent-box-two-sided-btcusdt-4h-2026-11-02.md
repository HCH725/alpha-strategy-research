---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradersPost EMA9/21 naked-cross percent-box two-sided on BTCUSDT 4h bars
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
  - https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/ema-crossover-strategy.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EMA9/21 naked cross + avg-price 2%/4% box — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `TradersPost/pinescript-agents` commit **`ebc382f88b6103fcda2569fe666a38b00fe714c5`** (2026-07-23), file **`projects/ema-crossover-strategy.pine`**, blob `b7a91d757f897e6f74da75791dc949d0c8bcd59e`, **9,712 bytes / 260 lines**, Pine v6, head `// built with PineScript Agents by TradersPost` / `//@version=6`, declaration `strategy("EMA Crossover Strategy", shorttitle="EMA Cross", ..., default_qty_type=strategy.percent_of_equity, default_qty_value=10, commission_type=strategy.commission.percent, commission_value=0.1, slippage=2)`. Raw bytes re-downloaded this cycle hash to sha256 `16038ca26a17cff7471c824bcb14426ba2f50fabe2e7fa0da8703f9aa5e19c01`, byte-identical to the working copy. Permalink: https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/ema-crossover-strategy.pine

**Order-affecting lines read verbatim (code governs):** `fastEma = ta.ema(close, fastLength)` / `slowEma = ta.ema(close, slowLength)` (defaults 9/21); `longCondition = ta.crossover(fastEma, slowEma) and barstate.isconfirmed` (mirrored short with `ta.crossunder`); `if strategy.position_size > 0 and strategy.position_size[1] == 0` → `longStopLoss := useStopLoss ? strategy.position_avg_price * (1 - stopLossPercent / 100) : na`, `longTakeProfit := useTakeProfit ? strategy.position_avg_price * (1 + takeProfitPercent / 100) : na` (mirrored short, defaults `useStopLoss=true`/`useTakeProfit=true`/`stopLossPercent=2.0`/`takeProfitPercent=4.0`); `if longCondition` → `strategy.entry("Long", strategy.long, qty=positionSize)` (unconditional — no position gate; mirrored short, `positionSize=10.0`); `if position_size > 0` → `strategy.exit("Long SL/TP", "Long", stop=longStopLoss, limit=longTakeProfit)` plus the `else if` TP-only leg (mirrored short pair). No `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick` argument ships anywhere (Pine defaults apply — recorded as absent, never filled in). The header `strategy.order.alert_message` token sits inside a `//@strategy_alert_message` comment — not an order call (disclosed).

**Pine-block census (260-line fence):** 1 `strategy(`; 2 `strategy.entry` (one `strategy.long`, one `strategy.short` — two-sided by construction); 4 `strategy.exit` (long combined, long TP-only, short combined, short TP-only — with fenced defaults only the two combined legs arm); 0 `strategy.close` code (3 `strategy.closedtrades` hits are perf-table display only — disclosed); 0 `strategy.order` code (1 alert-message comment token — disclosed); `ta.ema` ×2; `ta.crossover` ×1 + `ta.crossunder` ×1; 0 `request.` / 0 `security(`; 0 `timeframe.*`; `barstate.isconfirmed` ×2 (both entries); 10 `input.*` constructor calls (9/21/10.0/true/2.0/true/4.0 plus 3 visual-only color/toggle — fenced at defaults below); all plots/shapes/bgcolor/alertcondition/table blocks display-only — dropped, disclosed.

**Structural facts carried over exactly:** (a) naked EMA9/21 strict-cross entries on confirmed bars, fired unconditionally (flat, holding-same-side, or holding-opposite); (b) SL/TP levels LATCHED only on the new-position bar (`position_size[1]==0` → `position_avg_price` snapshot, `var` floats, never moved); (c) default no-add semantics (no `pyramiding` ships): same-side refires while holding are no-ops, opposite fires reverse in full; (d) no trailing, no time exit, no cooldown ships anywhere — explicitly none, never invented; (e) `qty=positionSize` explicit-qty semantics under a percent-of-equity declaration are ambiguous in isolation — fenced off and replaced by the fixed-size derivative below (disclosed).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction. Researcher-declared adaptations are exactly seven: (1) house sizing replacing the ambiguous percent/qty declaration (fixed **0.01 BTC** ≈ 780.2 USDT at probe close 78,021.8, above verified 50-USDT min-notional and 0.001 min-qty; 10,000 USDT cash; Isolated 1×); (2) 150-bar warmup with pre-warmup bars flat (structural first-defined index 21 — EMA21 — plus a 129-bar researcher margin for EMA seeding convergence); (3) display/alert/perf-table drop (plots, shapes, bgcolor, alerts, win-rate table carry no signal); (4) constant fence (9/21/naked/2%/4%/both-sides/SL-on/TP-on — any other value is a different unpinned rule; the TP-only/SL-only branches are fenced off, never pinned); (5) source commission `0.1%` + `slippage=2` treated as modeling zeros, never real-cost claims — the derivative pins an explicit **0.05%/side research cost** with slippage unmodeled (disclosed); (6) close-decided exits filled next-bar-open MARKET with code-order entries→SL→TP: same-bar SL+TP co-fire collapses to one flat close (stop wins by comment order), opposite-entry reversal dominates any same-bar SL/TP (entry side wins), same-side refire is a no-op (a research-model timing convention for `strategy.exit` intrabar stop/limit, never a claim the pinned engine queues live legs); (7) once-per-completed-bar evaluation (source timing class otherwise preserved, disclosed).

**Immutable derivative identity:** `GH:TradersPost-pinescript-agents-ebc382f|ema9-21_naked-cross_SL2-TP4-avgpx-latched|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|entries-dominate-stopfirst|warmup150|2026-11-02`. Changing any formula, length, gate, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported
Naked dual-EMA rotation capture with an entry-anchored percent box, two-sided: only strict EMA9-over-21 crosses (longs) and under-crosses (shorts) on confirmed bars may fire; each new position snapshots its own average price into a fixed −2%/+4% (longs, mirrored shorts) stop/limit box that never moves.

### Research interpretation
Unlike the pool FMZ dual-EMA9/21 sibling (`fmz-dual-ema9-21-rsi-rail-bracket` — EMA9/21 edges RAILED by RSI-14 `R<70`/`R>30`, 1.5%/1% box off signal-close `C[s]`, 1h), this machine is naked (no RSI read of any kind), risks a wider 2%/4% 2R box off fill-average (not signal close), and runs 4h. Unlike pool Donchian/ADX EMA-cloud siblings (band-stop exits, regime filters), the exit here is a latched avg-price percent box with entries-dominate reversal. Five-axis distinction holds on signal (naked cross vs RSI-railed cross), levels (avg-price 2R vs signal-close 1.5R), exits (strategy.exit stop/limit lifecycle vs ATR/signal-close boxes), state (flat-capable reversal with stale-level memory vs gated 1h book), and source identity (TradersPost GH pin `ebc382f` vs FMZ 472934).

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals/anchors, `H[t]`/`L[t]` for box-touch legs, `O[t]` for fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All constants are source-default literals.

- **EMAs (causal, per-bar):** `E9[t]=EMA9(C)`, `E21[t]=EMA21(C)` (Pine `ta.ema`, α=2/(L+1), SMA-seeded at first full window, na before); `up[t]` = `E9[t-1]<=E21[t-1] and E9[t]>E21[t]`, `dn[t]` = `E9[t-1]>=E21[t-1] and E9[t]<E21[t]` (strict cross semantics); no RSI, no volume, no second feed.
- **Predicates (actionable only t ≥ 150, at bar `t`'s close):** `longSig[t] = up[t]`, `shortSig[t] = dn[t]`. Pre-warmup bars flat by record rule; every na/degenerate bar is an explicit neither-fire hold.
- **Latched box (fixed at fill-average `A`, never moved):** long `SL=A×0.98`, `TP=A×1.04`; short mirrored `SL=A×1.02`, `TP=A×0.96`. Latched only on the new-position fill; reversal fills relatch from the new average (source-faithful). TP-only/SL-only branches never arm under the fence.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite entry first (reversal dominates, old box dies), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Opposite confluence while flat is impossible by construction (strict opposite inequalities — verified property).

## Required data / Gate 6 causality

**Warmup:** minimum 150 contiguous valid completed 4h bars; covers structural first-defined index 21 (EMA21 SMA-seed) plus a 129-bar researcher margin for EMA convergence. No warmup-bar trades; pre-warmup flat by record rule. Pine EMA seeding follows the disclosed probe convention (each EMA seeded with the SMA of its first length-many inputs); the margin renders the seeding choice immaterial post-warmup (disclosed).

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; row[0] open-time parsing, 4h-boundary alignment verified live this cycle). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (`barstate.isconfirmed` identically true on entries); fills at next-bar open (`process_orders_on_close` absent → default false); SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention for `strategy.exit` intrabar legs — disclosed). No incomplete bar, future extremum, repainted graphic, MTF call, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `determine_executor_actions` present in `backtesting_engine_base.py`, `OrderExecutorSimulator` byte-present in `executors_simulator/`, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session template, no second symbol). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the 9/21 EMA chain with strict cross semantics, the new-position avg-price 2%/4% latch, and the entries-dominate stop-first state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈780.2 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests.
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin (the source models `commission_value=0.1%` + `slippage=2` — disclosed modeling inputs, never real-cost claims); slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided box legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported
The pinned 260-line fence ships the complete construction: the strategy declaration (percent-of-equity-10 default with explicit `qty=positionSize`, `commission_value=0.1%`, `slippage=2`), the 9/21 EMA chain with strict confirmed-bar crosses, the unconditional two-sided entry block, the new-position-only avg-price 2%/4% latch pair with `var` floats, and the four-leg `strategy.exit` box (two armed under fenced defaults). It ships no performance figure of any kind — none adopted.

### Independently reproduced
**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the signal/latch/state pipeline (Pine-faithful EMA chain, strict crosses, avg-price latch, code-order entries-dominate stop-first resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS):** a 700-bar synthetic 4h-style tape with trend/shock legs prints 4 post-warmup `LE` and 5 post-warmup `SE` predicate bars driving 9 opens / 8 closes (1 SL-touched, 3 TP-touched, 4 reversals) ending SHORT (digest `41233802ab700df0`); two independent runs identical.

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,500 completed bars 2026-02-25→2026-11-02, last close 78,021.8):** 36 post-warmup `LE` and 36 post-warmup `SE` predicate bars drive 68 state-machine opens / 67 closes (13 SL-touch / 13 TP-touch, 41 reversals) ending SHORT with the position honestly held at the window edge (digest `1757eae298d7647d`); sub-window bars 300–999 print 16 `LE` / 16 `SE` driving 28 opens / 27 closes (5 SL / 5 TP / 17 reversals) ending LONG, same honest cut (digest `647384ce2ba3599e`). 0.01 BTC ≈ 780.2 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence
At the pre-write snapshot `main@9e636744`, the root Git tree contained **511** strategy Markdown records (513 files minus two READMEs). Exact-identity working-tree searches for `TradersPost` / `pinescript-agents` / `ema-crossover` / `b7a91d75` return **zero** records using this source (the two `TradersPost` hits are the Q-Trend-KVO confluence and MACD86 zero-gate records — different indicators, gates, exits, disclosed); `EMA9/21 cross` hits are the RSI-railed FMZ family and Donchian/ADX cloud lineages — five-axis distinction fenced above, none a naked EMA9/21 cross with an avg-price 2%/4% box. Fifteen open `research/*` PRs were inspected by per-PR title/head — no collision. A 300-deep closed-PR title scan returns only #530 (the merged Q-Trend-alone record — different mechanism, disclosed). Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen naked-cross box book against (a) RSI-railed twins (isolating the gate), (b) no-box twins (pure cross-to-cross reversal — isolating the percent box), (c) signal-close-anchored twins (isolating avg-price vs close anchoring), and (d) 1%/1.5% and 3%/6% box twins (isolating the 2R choice; researcher variation); check event rate, SL/TP/reversal attribution, hold-time distribution, warmup sensitivity, and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only. Stated plainly: the oscillator needs 9/21 closes plus the 150-bar admission warmup (EMA21-bound); the entries are naked crosses with a live-window rate of ~72 predicates per 1,500 4h bars; the exits are a latched 2%/4% avg-price box with reversal dominance; 4h slippage plus funding apply to every held span. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The market/timeframe pin (source is chart-agnostic), sizing, cash, leverage, warmup, display/alert/perf-table drop, constant fence, 0.05% research fee, close-decided next-open resolution, and once-per-bar evaluation are researcher pins, never attributed to the source. No percent-of-equity sizing is ported (replaced by fixed 0.01 BTC — disclosed). The source `0.1%` commission and `slippage=2` are fenced as modeling inputs (disclosed). The repository ships no LICENSE file — this record cites short literal lines only and reproduces no source block. Pine v6 EMA/cross causal semantics are adopted explicitly with a disclosed seeding probe convention (EMAs seeded with the SMA of their first length-many inputs; the 129-bar margin covers seeding/convergence). Entries read completed-bar closes only; SL/TP legs are close-decided against completed-bar H/L with next-open fills (research-model convention for `strategy.exit` intrabar legs — disclosed). Probe windows end holding except none — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/ema-crossover-strategy.pine (commit `ebc382f88b6103fcda2569fe666a38b00fe714c5`, 2026-07-23; blob `b7a91d757f897e6f74da75791dc949d0c8bcd59e`; Pine v6, 260 lines / 9,712 bytes; raw sha256 `16038ca26a17cff7471c824bcb14426ba2f50fabe2e7fa0da8703f9aa5e19c01` verified live 2026-11-02; no LICENSE — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,500 completed bars 2026-02-25→2026-11-02, 36 LE / 36 SE → 68 opens / 67 closes, plant digest `41233802ab700df0`, window digests `1757eae298d7647d`/`647384ce2ba3599e`), fetched live 2026-11-02
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): RSI-railed `fmz-dual-ema9-21-rsi-rail-bracket-two-sided-btcusdt-1h-2026-11-01.md`; Q-Trend-KVO confluence https://github.com/HCH725/alpha-strategy-research/pull/697; MACD86 zero-gate https://github.com/HCH725/alpha-strategy-research/pull/698
- Pine reference: v6 `ta.ema`/`ta.crossover`/`ta.crossunder`/`barstate.isconfirmed` causal semantics
