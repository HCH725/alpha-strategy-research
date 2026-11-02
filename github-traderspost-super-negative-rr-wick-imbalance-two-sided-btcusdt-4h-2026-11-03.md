---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradersPost Super-Negative-RR wick-imbalance ratio-gated two-sided on BTCUSDT 4h bars
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-03
sources:
  - https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/super-negative-rr.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Super-Negative-RR wick-imbalance 2x-ratio ATR-gated 0.3-RR box — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `TradersPost/pinescript-agents` commit **`ebc382f88b6103fcda2569fe666a38b00fe714c5`** (2026-07-23 — still the repo HEAD, verified live this cycle), file **`projects/super-negative-rr.pine`**, blob `9f2b8ba64fae4eb198e8cd786548585ef25fcbe0`, **11,897 bytes / 340 lines**, Pine v6, head `// built with PineScript Agents by TradersPost` / `//@version=6`, declaration `strategy("Super Negative R:R Wick Strategy", shorttitle="Negative RR", ..., initial_capital=5000, default_qty_type=strategy.fixed, default_qty_value=1, margin_long=0, margin_short=0, calc_on_every_tick=true, use_bar_magnifier=true, commission_type=strategy.commission.cash_per_order, commission_value=1, slippage=2)`. Raw bytes downloaded this cycle hash to sha256 `acddacebca5582983b4967e3abfe690d88c3dfe76a09997f83bd319115651281`, matching the API blob SHA above. Permalink above.

**Order-affecting logic read verbatim (code governs):** ATR `atr = ta.atr(atrLength)` with fenced default `atrLength = input.int(14)` and one-bar-older `prevAtr = atr[1]`; prior-bar OHLC `prevHigh = high[1]` / `prevLow = low[1]` / `prevOpen = open[1]` / `prevClose = close[1]`; body/wick split `prevMaxBody = math.max(prevOpen, prevClose)` / `prevMinBody = math.min(prevOpen, prevClose)` / `prevBodySize = prevMaxBody - prevMinBody` / `prevUpperWick = prevHigh - prevMaxBody` / `prevLowerWick = prevMinBody - prevLow` / `prevTotalWick = prevUpperWick + prevLowerWick`; the three entry gates at source defaults `wickRatioThreshold = input.float(2.0)` / `minBodyAtr = input.float(0.1)` — `wickSizeCondition = prevTotalWick > prevAtr`, `upperWickDominant = prevUpperWick > prevLowerWick * wickRatioThreshold`, `lowerWickDominant = prevLowerWick > prevUpperWick * wickRatioThreshold`, `notDoji = prevBodySize >= prevAtr * minBodyAtr` — with source-declared polarity `longSignal = wickSizeCondition and upperWickDominant and notDoji and strategy.position_size == 0` and mirrored `shortSignal` (LONG on upper-wick dominance, SHORT on lower-wick dominance; body side/direction is never conditioned, only body size — disclosed); entries `strategy.entry("Long", strategy.long)` / `strategy.entry("Short", strategy.short)`; exits `strategy.exit("Long Exit", "Long", profit=tpTicks, loss=slTicks)` / mirrored short, where `slTicks = riskAmount / (tickValue * qty)` / `tpTicks = rewardAmount / (tickValue * qty)` from fenced dollar defaults `riskAmount = input.float(1000)` / `rewardAmount = input.float(300)` (RR 0.3:1, source-computed break-even `100 / (1 + currentRR)` ≈ 76.9% — disclosed); `qty = strategy.default_entry_qty(close)` (fixed 1 contract).

**Pine-block census (340-line fence):** 1 `strategy(` declaration; 2 `strategy.entry` calls (+1 comment mention); 2 `strategy.exit` calls; 0 `strategy.close`; 0 real `strategy.order` (1 `{{strategy.order.alert_message}}` template placeholder only); 0 `request.*`; 0 `input.session`; 1 `calc_on_every_tick` (=`true` — intrabar recalc, NOT ported, disclosed); 1 `bar_magnifier` (=`true` — intrabar magnifier exits, NOT ported, disclosed); 0 `pyramiding` (Pine default 0, entries additionally gated on `position_size == 0` — single-position, disclosed); 2 `alertcondition` entries (+1 comment mention, dropdown conveniences only); 2 `alert()` calls with `alert.freq_once_per_bar` (close-decided intent, disclosed). Cash-per-order $1 commission and slippage 2 are source backtest assumptions, dropped and replaced by the researcher fee pin below (disclosed). All plots/table/colors display-only — dropped, disclosed. No LICENSE file ships in the repo — short-literal citation only, no source block reproduced.

**Structural facts carried over exactly:** (a) ATR(14) denominator with the one-bar-older `atr[1]` reference; (b) total-wick-beats-ATR volatility-expansion gate (strict `>`); (c) 2.0x opposing-wick dominance ratio (strict `>` both sides); (d) 0.1x-ATR anti-doji body floor (body size only, no body-direction condition); (e) source-declared long-on-upper / short-on-lower polarity; (f) flat-only entries (single position, no adds); (g) the 0.3 risk-reward identity (1000/300). No MTF, no session/timezone, no gap dependence anywhere in the ported legs (disclosed).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source's dollar exits are symbol-specific (pointvalue/mintick of an undeclared contract) and its backtest timing is intrabar (every-tick recalc plus bar-magnifier exits). Researcher-declared adaptations are exactly nine: (1) dollar SL/TP mapped to a ratio-preserving latched percent box — long `SL=A×0.98`, `TP=A×1.006`, short mirrored (RR 0.3 kept; the sibling-house 2%/4% box would destroy the negative-RR identity — disclosed); (2) intrabar timing answered by close-decided once-per-completed-bar evaluation with next-bar-open MARKET fills (research-model convention; magnifier-early exits are not modeled — disclosed); (3) fixed **0.01 BTC** sizing (≈774.8 USDT at probe close 77,482.9, above verified 50-USDT min-notional and 0.001 min-qty; 10,000 USDT cash; Isolated 1×); (4) 100-bar warmup with pre-warmup bars flat (14 = structural ATR scale, +86 researcher margin for RMA-seed convergence); (5) display drop (shapes, ATR line, metrics table, alerts, colors); (6) constant fence (14/2.0/0.1/2%/0.6%/two-sided/box-on — any other value is a different unpinned rule); (7) explicit **0.05%/side research cost**, slippage unmodeled (disclosed); (8) code-order resolution — opposite setup first (reversal dominates), else SL-touch, else TP-touch, SL+TP co-fire closes flat (stop wins), same-side refire is a no-op; (9) RMA seeding pin (SMA of first 14 TRs; warmup absorbs it — disclosed).

**Imbalance co-fire proof:** bull needs `UW > 2·LW` and bear needs `LW > 2·UW` on the same prior bar — jointly implying `UW+LW < 0` for nonnegative wicks, impossible. Both-legs firing is provably unreachable; the flat tie-hold branch is coded defensively only (disclosed).

**Immutable derivative identity:** `GH:TradersPost-ebc382f|supernegRR_wick2.0_ATR14_body0.1_SL2-TP0.6-avgpx-latched|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|reversal-dominate-stopfirst-noop|warmup100|2026-11-03`. Changing any formula, length, ratio, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

High RR-reversal scalping with deliberately negative risk-reward: risk $1,000 to make $300 per contract (0.3:1), so the machine must win ≈76.9% of trades to break even. Edge is claimed from wick-imbalance bars — a prior candle whose combined wick exceeds one ATR, with one wick at least twice the other and a non-doji body — traded in the source-declared polarity (long after upper-wick dominance, short after lower-wick dominance). No performance figure ships in the file — none adopted.

### Research interpretation

Unlike pool hammer/shooting-star records (fixed candle shapes, long-only) and pool doji records (doji as veto or anchor), this machine keys off a **normalized wick-imbalance ratio**: total wick versus ATR(14), opposing-wick dominance at exactly 2.0x, and an ATR-fraction body floor that admits only decisive bars. Body direction plays no role — the trigger is volatility expansion plus one-sided rejection, traded two-sided in the source polarity. Unlike pool ATR-box siblings (ATR sets stop distance), here ATR normalizes the *signal*, while risk keeps the source 0.3-RR identity via the percent-box map. Live-window rate is 65 post-warmup predicate bars per 1,499 4h bars (31 long-leg / 34 short-leg), closing 63 trades with a 52-TP / 10-SL / 1-reversal split — the negative-RR asymmetry (many small wins, few large losses) is structural, not tuned.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals/anchors/closes, `H[t]`/`L[t]` for wick/box-touch legs, `O[t]` for fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All constants are source-default literals except the percent box (researcher ratio-preserving map, disclosed).

- **ATR (causal, per-bar, Pine-faithful):** Wilder RMA of true range with length 14, seeded with the SMA of the first 14 TRs (researcher seed pin; 100-bar warmup absorbs seeding — disclosed). `prevAtr[t] = ATR[t-1]`.
- **Wick split (prior bar, Pine-faithful):** `body=|C-O|`, `UW=H-max(O,C)`, `LW=min(O,C)-L`, `TOT=UW+LW`, all on bar `t-1`.
- **Predicates (actionable only t ≥ 100, at bar `t`'s close):** `long[t] = (TOT>prevAtr) and (UW>2.0·LW) and (body≥0.1·prevAtr)`; `short[t] = (TOT>prevAtr) and (LW>2.0·UW) and (body≥0.1·prevAtr)`. Pre-warmup bars flat by record rule; every na/degenerate bar is an explicit neither-fire hold. Strict inequalities match source exactly (equality never fires).
- **Latched box (researcher-designed, fixed at fill-average `A`, never moved):** long `SL=A×0.98`, `TP=A×1.006`; short mirrored `SL=A×1.02`, `TP=A×0.994`.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite setup first (reversal dominates: close old and open new at the same next open; tie bars defensively hold per the impossibility proof), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Single position, no adds: same-side refire is a no-op (verified on tape).

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous valid completed 4h bars; covers the 14-bar ATR scale plus the `[1]`-offset prior-bar reference and an 86-bar researcher margin for RMA-seed convergence (TR seeding is defined from bar 0 — the margin renders seeding immaterial post-warmup, disclosed). No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; forming-bar dropped, completed-only probe verified live this cycle). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (researcher once-per-bar pin answering the source's every-tick recalc; `alert.freq_once_per_bar` shows the source's close-decided alert intent, disclosed); fills at next-bar open; SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention, disclosed). No incomplete bar, future extremum, repainted graphic, MTF call, session template, gap state, magnifier intrabar fill, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `BacktestingEngineBase.run_backtesting` + `determine_executor_actions` in controller bases, `OrderExecutorSimulator` class byte-present in `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session, no second symbol, no gap feed). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the ATR-RMA plus prior-bar wick-split predicates with strict-inequality semantics, the new-position avg-price 2%/0.6% latch, and the reversal-dominate stop-first no-op state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈774.8 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided box legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 340-line fence ships the complete wick-imbalance construction: ATR(14) with the `[1]`-offset reference, the exact body/wick split, the three gates at 2.0/0.1 defaults with strict inequalities, the long-on-upper / short-on-lower polarity with flat-only gating, tick-derived dollar exits from the 1000/300 defaults with the ≈76.9% break-even identity, and fixed-1-contract sizing. It ships no performance figure of any kind — none adopted. Its intrabar backtest timing (every-tick recalc, bar magnifier) is fenced OUT of the derivative and answered by the once-per-bar pin (disclosed).

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/latch/state pipeline (Pine-faithful wick split, strict gates, avg-price latch, code-order reversal-dominate stop-first no-op resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** MICRO-SL tape prints 1 post-warmup long leg driving 1 open / 1 SL close ending flat (digest `ecf3a94def28`); MICRO-TP tape prints 1 short leg driving 1 open / 1 TP close ending flat (digest `6f7be2658a5b`); MICRO-REV tape prints 2 long / 1 short legs driving 2 opens / 1 reversal close ending short-held with the same-side refire correctly a no-op (digest `cc94ad49baec`); MICRO-TIE tape prints a neither-fire doji driving 0 opens ending flat (digest `4f53cda18c2b`).

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,499 completed bars 2026-02-25→2026-11-02, forming bar dropped, last close 77,482.9):** 31 post-warmup `LE` and 34 post-warmup `SE` predicate bars drive 63 state-machine opens / 63 closes (10 SL-touch / 52 TP-touch, 1 reversal) ending FLAT (digest `253682a3389a`); sub-window bars 300–999 print 13 `LE` / 19 `SE` driving 30 opens / 30 closes (9 SL / 20 TP / 1 reversal) ending FLAT, same honest cut (digest `cc05e42353a3`). 0.01 BTC ≈ 774.8 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@db669c91`, the root Git tree contained **523** strategy Markdown records (525 files minus two READMEs). Exact-identity working-tree searches for `wick-ratio` / `wickRatio` / `wick.*dominant` / `super-negative` / `superneg` / `negative-rr` / `negativerr` / `9f2b8ba64fae` return **zero** records. The five pool wick-adjacent records are different mechanisms (freqtrade hammer-gated oversold long-only 5m; bearish-wick as long-exit 1d; long-legged-doji anchored breakout long-flat 1d; five-bar doji-veto long 1d; hammer/shooting-star long-flat 1d) — none a two-sided opposing-wick dominance ratio with ATR-normalized total wick and ATR-fraction body floor. Sixteen open `research/*` PRs were inspected by per-PR title/head — no collision (nearest open lanes are Alpha57-VWAP, EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams — none a wick-imbalance). Closed-PR scan surfaces no member of this family. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen wick-imbalance box book against (a) no-box twins (pure setup-to-opposite-setup reversal — isolating the percent box), (b) house 2%/4% box twins (isolating the ratio-preserving 0.3-RR choice; researcher variation), (c) ratio/floor twins at 1.5x/3.0x dominance and 0.05/0.20 body floors (isolating the 2.0/0.1 constants; researcher variation — never attributed to source), and (d) ATR-length twins at 7/21 (isolating the 14 scale; researcher variation). Check event rate, SL/TP/reversal attribution, hold-time distribution, warmup sensitivity (100 vs 200), and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only. Stated plainly: the machine needs completed-bar OHLC plus the 100-bar admission warmup (lookback-bound); the entries are ATR-normalized wick-imbalance legs with a live-window rate of ~65 predicate bars per 1,499 4h bars; the exits are a researcher-latched 2%/0.6% avg-price box with reversal dominance; 4h slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap dependence (the file ships zero session logic, disclosed), so 24/7 crypto continuous trading introduces no Year-2024-style anchor or session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The dollar-to-percent box map, market/timeframe pin (source is chart-agnostic), sizing, cash, leverage, warmup, RMA seed, display drop, constant fence, 0.05% research fee, close-decided next-open resolution, reversal dominance, stop-wins-tie, same-side no-op, and once-per-bar evaluation are researcher pins, never attributed to the source. The source's every-tick recalc and bar-magnifier exits are fenced out — a live/magnifier run of the original would exit earlier intrabar than this close-decided derivative; no parity is claimed. Both-legs co-fire is mathematically impossible under the 2.0x ratio (proof above); the tie-hold is defensive code only. The repo ships no LICENSE — this record cites short literal lines only and reproduces no source block; research-only use asserted, no commercial claim. Pine RMA seeding is adopted explicitly with an 86-bar convergence margin inside the 100 warmup. Entries read completed-bar closes only; SL/TP legs are close-decided against completed-bar H/L with next-open fills (research-model convention, disclosed). Probe windows end flat — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/super-negative-rr.pine (commit `ebc382f88b6103fcda2569fe666a38b00fe714c5`, 2026-07-23, still HEAD verified live 2026-11-03; blob `9f2b8ba64fae4eb198e8cd786548585ef25fcbe0`; Pine v6, 340 lines / 11,897 bytes; raw sha256 `acddacebca5582983b4967e3abfe690d88c3dfe76a09997f83bd319115651281` verified live 2026-11-03; no LICENSE — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,499 completed bars 2026-02-25→2026-11-02, 31 LE / 34 SE → 63 opens / 63 closes; plant digests `ecf3a94d`/`6f7be265`/`cc94ad49`/`4f53cda1`, window digests `253682a3389a`/`cc05e42353a3`), fetched live 2026-11-03
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): wick-reversal hammer/shooting-star `wick-reversal-hammer-shooting-star-long-flat-btcusdt-1d-2026-10-16.md`; long-legged-doji breakout `tradingview-kingshukghosh71-longleg-doji-anchored-breakout-long-flat-btcusdt-1d-2026-10-28.md`; sweep-fade sibling https://github.com/HCH725/alpha-strategy-research/pull/711
- Pine reference: v6 causal offsets (`high[1]`, `atr[1]`), Wilder RMA (`ta.atr`), `alert.freq_once_per_bar`, flat-gated entries (`position_size == 0`)
