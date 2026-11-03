---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Scalping PullBack PAC-recovery arrow long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-08
sources:
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Scalping%20PullBack%20Tool/Scalping%20PullBack%20Tool.pinescript4
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Scalping%20PullBack%20Tool/README.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Scalping PullBack PAC-recovery arrow — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (`Add 60 community MIT/MPL indicators from TakeProfit with guides`, author PavMedd, 2026-10-08T20:41:02Z, verified via GitHub API this cycle), file **`indicators/Scalping PullBack Tool/Scalping PullBack Tool.pinescript4`**, blob `26acaa47b856aab9933cbb5b3264e7e6639f286e`, **12,094 bytes / 475 lines**, `study(title="Scalping PullBack Tool R1.1 by JustUncleL", shorttitle="SCALPTOOL R1.1", overlay=true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle are byte-identical (second download `cmp`-matched); `git hash-object` of the working copy reproduces the API blob SHA exactly. The pinned port guide (`indicators/Scalping PullBack Tool/README.md`, 13,312 bytes, fetched at the pinned ref this cycle) confirms the original is R1.1 by JustUncleL in Pine Script v4, the Indie logic port is 1:1 (PAC channel, EMA ribbon, trend direction, fractals, HH/LH/HL/LL finder, pullback-recovery trade state, Buy/Sell arrow), calculations run on Heikin Ashi candles by default in the original, and the script header states no license (guide: "not stated in the script header (open-source script published on TradingView)").

**Order-affecting logic read verbatim (the ALERTING block governs; the study ships no orders):** inputs pinned at defaults `HiLoLen = 34`, `fastEMAlength = 89`, `mediumEMAlength = 200`, `slowEMAlength = 600`, `Lookback = 3`, `DelayArrow = false` (so `Delay = 0`), `filterBW = false`, `UseHAcandles = true` (adapted below). Series: `fastEMA = ema(haClose, 89)`, `mediumEMA = ema(haClose, 200)`, `slowEMA = ema(haClose, 600)` (plotted only — the header states "slow EMA(600) is not used in this Algo", and no signal line reads it), `pacC = ema(haClose, 34)`, `pacL = ema(haLow, 34)`, `pacU = ema(haHigh, 34)`. Trend gate: `TrendDirection = 1` iff `fastEMA > mediumEMA and pacL > mediumEMA`; `-1` iff `fastEMA < mediumEMA and pacU < mediumEMA`; else `0`. Recovery legs: `pacExitU = haOpen < pacU and haClose > pacU and barssince(haClose<pacC)<=Lookback`; `pacExitL` mirrors on `pacL`/`haClose>pacC`. Arrows: `Buy = TrendDirection == 1 and pacExitU`; `Sell = TrendDirection == -1 and pacExitL`. State machine (single-expression `:=` chain on the previous-bar value seeded by `nz(TradeDirection[1])`): `TD==1 and haClose<pacC ? 0 : TD==-1 and haClose>pacC ? 0 : TD==0 and Buy ? 1 : TD==0 and Sell ? -1 : TD`. Coded events: `Long = nz(TD[1])==0 and TD==1`, `Short = nz(TD[1])==0 and TD==-1` (the two `alertcondition(` legs). With `Delay = 0` the plotted arrow is exactly the 0→±1 transition on the closing bar.

**Pine-block census (475-line fence):** 1 `study(`; 0 `strategy.*` of any kind; 16 `input(`; 6 `ema(` (34/89/200/600/34/34); 4 `security(heikinashi(...), timeframe.period, ...)` (same-frame HA plumbing, bypassed by the normal-candle pin); 0 `request.*`; 0 `volume`; 2 `alertcondition(` (BUY/SELL); 1 `plotarrow(` (transition marker, display); fractals / HH-LL / barcolor / bgcolor / ribbon plots are display-only and read by no signal line.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is a display/alert indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly eight: (1) normal-candle pin (`UseHAcandles = false` equivalent — `haO/H/L/C := O/H/L/C`, bypassing the four same-frame `security(heikinashi(...))` legs, disclosed); (2) long-only pin with the short side explicitly disabled (Short events while flat are deliberate omissions, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at the cycle's last completed close 76,816.00 on 2026-11-02, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 600-bar warmup with pre-warmup bars flat (3× the longest used length 200, plus `barssince`/seed margin); (6) display drop (fractals, HH/LH/HL/LL, ribbon plots, barcolor/bgcolor, arrow marker — the `TradeDirection` state they visualize is kept); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim).

**Prior-screening answer (not a silent overrule):** the same-commit Madrid-ribbon record (2026-11-04) screened this tool out as "hand-drawn mini-trendline entries, Heikin-Ashi option, sub-15min scalping intent — discretionary". That reading conflates the header's hints prose with the coded machine, and this record answers it with code evidence: the hand-drawn mini-trendline / SweetSpot workflow lives only in the Setup-and-hints comment prose and feeds no order-gating line (fenced below — the same prose-vs-block separation the admitted TDI record applies to the same author's hint text); the executable ALERTING block (inputs → series → trend gate → recovery legs → TD state → two alertconditions) is fully deterministic with no manual input; the Heikin-Ashi leg is handled by adaptation 1 (normal-candle pin); and the header prose itself blesses higher timeframes ("it should work just as well on higher time frame charts for longer term trades"). What is adopted here is only the coded alert machine, never the discretionary workflow.

**Immutable derivative identity:** `GH:Indie-script-64f0494|scalping-pullback_pac34-ema89-200_lookback3-normal-candle_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup600|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@0fdea462` (547 root strategy records, READMEs excluded; this file is the 548th). Case-insensitive content search for `Scalping PullBack`, `pacExitU`, `SCALPTOOL` returns zero records (the only `Scalping PullBack Tool` hit anywhere is the Madrid record's own screening note answered above — a mention, not a record). No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors, all pullback/arrow-flavored: different source file/math/signal vs `tdi-pac-strength-tiered-alert-reversal-two-sided-btcusdt-2h` (same author JustUncleL and also PAC-plus-alerts, but a TDI RSI-13 composite with 34-bar 1.6185-sigma band, SMMA-5 PAC, strength tiers and body-direction witness, two-sided always-in reversal on 2h with same-close fills — here an EMA-ribbon trend gate with EMA-34 PAC, barssince-3 recovery legs and centerline-reset TD state, long-flat on 1d with next-open fills; trigger, exits, direction, TF and fills all differ); different channel/gate vs `forven-ema-rsi-pullback-reclaim-long-flat-solusdt-1h` (RSI-gated single-EMA reclaim on SOL 1h — no channel, no barssince bound, no TD state); different math vs `fmz-super-scalper-rsi-atr-band-dip-two-sided-btcusdt-5m` (RSI/ATR dip scalp on 5m futures, two-sided) and vs `ut-bot-atr-trailing-stop-flip-two-sided-btcusdt-1d` (ATR trailing-stop flip — no ribbon, no PAC, no recovery legs). No duplicate, paraphrase, or trivial parameter variant. Same-commit screenings held before writing: Stochastic OTT (identical math already ported on `main`); Volume Orderbook (POC leg needs representative capability validation, left for later); EWO Pro / TonyUX / UFF / VD binary pro 3 / Band Trend / Median Algorithm and five more (no Pine original pinned at this commit — `.indie5` only — provenance-insufficient, same fence as prior cycles).

## Economic mechanism

### Source-reported

Scalping PullBack Tool R1.1 (per its header and the port guide): a Price Action Channel of EMAs (34) of high/low/close plus an EMA ribbon (89/200/600) classifies trend direction (up when fast EMA and PAC low sit above medium EMA, down when both sit below); a pullback is price starting outside the PAC then pulling back into it across the center line; a Buy/Sell arrow prints when price recovers back out of the channel in trend direction within the lookback. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool fade machines that short overextension (turtle-soup's Donchian fade, LuxAlgo sweep fade) and unlike pool reversal machines that flip on opposite alerts (the TDI record's always-in reversal), this machine is a trend-filtered continuation machine: it only buys recoveries that exit the channel on the trend side (open inside → close outside, within three bars of a centerline cross), and it holds while closes stay above the channel center, exiting the first close that loses it. Unlike pool cross machines there is no line-cross entry; unlike pool slope/state machines there is no regime to hold — there is only a gated recovery arrow to enter on and a centerline to exit on. The bet, as derived, is purely that this ribbon-gated PAC-recovery-then-centerline alternation ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series (normal-candle pin, adaptation 1): `O/H/L/C[t]` are the venue bars (an Heikin-Ashi-sourced twin is a different, unpinned rule). No volume read exists in this rule.
- R3 — Channel and ribbon (source formulas, pinned): `pacC[t] = ema(C,34)`, `pacL[t] = ema(L,34)`, `pacU[t] = ema(H,34)`, `fastEMA[t] = ema(C,89)`, `mediumEMA[t] = ema(C,200)` (Pine `ema`, α = 2/(n+1), seeded per language semantics; `slowEMA(600)` is never read by any signal line — pinned absence, not invented).
- R4 — Trend gate (source formula, pinned): `Trend[t] = 1` iff `fastEMA[t] > mediumEMA[t] AND pacL[t] > mediumEMA[t]`; `-1` iff `fastEMA[t] < mediumEMA[t] AND pacU[t] < mediumEMA[t]`; else `0` (strict inequalities — equality on any leg yields transition state `0`, disclosed).
- R5 — Bullish recovery leg (source formula, pinned): `pacExitU[t] = O[t] < pacU[t] AND C[t] > pacU[t] AND barssince(C<pacC)[t] <= 3` (strict both sides; equality on either rail is no event — pinned source-faithful boundary, disclosed).
- R6 — Bearish recovery leg (source formula, pinned): `pacExitL[t] = O[t] > pacL[t] AND C[t] < pacL[t] AND barssince(C>pacC)[t] <= 3`.
- R7 — Arrows (source formulas, pinned): `Buy[t] = Trend[t]==1 and pacExitU[t]`; `Sell[t] = Trend[t]==-1 and pacExitL[t]` (mutually exclusive by construction — opposite trend requirements — at most one fires per bar).
- R8 — State (source machine, pinned): `TD[t] = TD[t-1]==1 and C[t]<pacC[t] ? 0 : TD[t-1]==-1 and C[t]>pacC[t] ? 0 : TD[t-1]==0 and Buy[t] ? 1 : TD[t-1]==0 and Sell[t] ? -1 : TD[t-1]` (single-expression semantics on the previous-bar value — a bar that resets 1→0 cannot also set 0→1; re-entry waits for a fresh later Buy, source-faithful, disclosed).
- R9 — Position (promoted machine, adaptation 2): `LONG`/`FLAT` single-unit book. If FLAT and `Long[t] = (TD[t-1]==0 and TD[t]==1)` → request LONG at the next open. If LONG → exit the whole book at the next open when `TD[t]==0` (i.e. `C[t] < pacC[t]` — the centerline reset, source rule R8). Sell/Short events while FLAT are explicit holds (short side disabled); Sell events while LONG never flip the book by source construction (no opposing-arrow exit — an implementation exiting on Sell arrows prints a different event set, fenced in Negative evidence).
- R10 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R11 — Position state: one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none. No pyramiding: while LONG no new Buy can set state (R8 needs `TD[t-1]==0`) — pinned absence, not invented.
- R12 — Warmup and gaps: flat until 600 completed `1d` bars (3× the longest used length 200, plus `barssince`/seed margin). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold.
- R13 — Invariant identifier: `GH:Indie-script-64f0494|scalping-pullback_pac34-ema89-200_lookback3-normal-candle_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup600|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (recovery tests, validity), `high`/`low` (channel rails, validity), `close` (all legs, state reset, validity). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used. The `DelayArrow = false` default means arrows mark the closing bar (a `delay_arrow = true` twin is a different, unpinned rule).
- Warmup: flat until 600 completed bars (structural). No repainting (all legs read closed-bar values; `barssince` scans closed history; `TD` state is append-only recursion seeded by the source's own `nz(TD[1])`), no negative shift, no future reference, no full-sample normalization. Every live input is frozen at the decision close — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 on 2026-11-02 — the 11-03 bar was still forming at cycle time — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (local checkout `2dbc844` carries `VERSION` file `2.17.0`, verified live this cycle); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. EMA-ribbon/PAC state is a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 475-line fence ships every adopted headline fact quoted in Provenance: the `input(34/89/200/600)` defaults, the `Lookback = input(3)` default, `DelayArrow = false`, the six EMA definitions, the strict trend-gate inequalities, the strict recovery inequalities with the `barssince(...)<=Lookback` bound, the `Buy`/`Sell` conjunctions, the single-expression TD state chain, the `nz(TradeDirection[1])` seed, the two `alertcondition(Long/Short)` legs, the `study(` (not strategy) declaration, and the header's own "slow EMA(600) is not used in this Algo" plus "should work just as well on higher time frame charts" lines. It ships zero orders, zero sizing, zero exits, zero performance figures — none adopted; all trading semantics are researcher pins disclosed above. The pinned port guide additionally reports the 1:1 logic port (channel, ribbon, trend, fractals, trade state, arrows), the HA-on-by-default note, and the full 16-parameter default table — cited as source-reported port evidence, not as Hermes reproduction.

### Independently reproduced

Not independently reproduced. No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. No executable probe ran in this unattended cycle; logic assertions above are static readings of the pinned fence, fenced in Negative evidence where implementations may differ.

### Negative evidence

1. Discretionary-prose fence: the header's Setup-and-hints workflow (hand-drawn mini trendlines on fractal/HH-LL points, SweetSpot Gold RN overlay, per-alert eyeball evaluation, sub-15min session advice) feeds no order-gating line and is adopted nowhere — an implementation trading trendline breaks prints a different, unpinned event set, flagged as an implementation obligation, never strategy behavior.
2. HA-pin fence: the source default computes on Heikin Ashi via same-frame `security(heikinashi(...))`; this derivative pins normal candles (adaptation 1) so fills model real OHLC tape — an HA twin is a different, unpinned claim requiring its own data-requirement validation.
3. na-seed fence: `barssince` is na before the first centerline cross and every EMA is na during its seed window; post-600-bar-warmup a missing cross inside the window is implausible on BTC daily tape but an implementation must hold flat on na conditions (the source's own `nz(TD[1])` seed self-heals stray na to flat) — flagged as an implementation obligation, never a strategy claim.
4. Equality/FP silence fenced: strict inequalities decide everything — exact rail/centerline touches are no-ops; floating-point EMA comparisons may disagree across implementations on degenerate flat input — fenced as an implementation obligation; live tape carries no constant stretches so no live event turns on it.
5. Opposing-arrow boundary fenced: `Sell` events never exit a LONG book in source construction — any record exiting LONG on opposing arrows is a different, unpinned claim; the `DelayArrow = true` shifted-arrow variant is likewise unpinned here.
6. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
7. Derivation boundary fenced: the only non-source behavior is the eight declared adaptations (normal-candle pin, long-only pin, fixed sizing, disabled risk, 600-bar warmup, display drop, 0.1% cost overlay, next-open fills); the PAC/ribbon math, lengths, inequalities, lookback, state chain, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ema(C,34)/ema(H,34)/ema(L,34)` PAC / `ema(C,89/200)` ribbon gate / strict inequalities / `barssince <= 3` recovery / centerline-reset exits / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 600-bar warmup are frozen.

- F1 — Trend-gate relevance: a no-ribbon twin (recovery legs alone, same rest) must not improve net expectancy; fail ⇒ the EMA-ribbon gate is decoration on channel recoveries.
- F2 — Lookback relevance: a `Lookback = 10` twin (same rest) must not improve net expectancy; fail ⇒ the 3-bar staleness bound discards the better half of the recoveries.
- F3 — Exit relevance: an exit-also-on-Sell twin (opposing arrows also exit LONG, same rest) must not improve net expectancy; fail ⇒ the centerline-only exit is decoration on arrow churn.
- F4 — Warmup relevance: a 900-bar-warmup twin must print the identical post-900 event set; fail ⇒ EMA/`barssince` transients leak past the declared warmup.
- F5 — PAC-length relevance: a PAC-21 twin (same ribbon, same rest) must not improve net expectancy; fail ⇒ the 34-bar channel width is decoration on generic band recoveries.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The source is a TradingView alert indicator (no license stated in the script header — cited, not copied); every trading semantic (normal-candle pin, anchor exits, venue, sizing, warmup, no-box risk, next-open fills, cost overlay, long-only pin) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- Centerline-cross timing, na-seed behavior and degenerate-input FP behavior are implementation-defined (Negative evidence 3–4); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (600) is a researcher margin over the 200-bar longest used length; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Scalping%20PullBack%20Tool/Scalping%20PullBack%20Tool.pinescript4 (canonical pinned source; commit `64f0494a84273138b2e6a0f15821b18ba1616056`, blob `26acaa47b856aab9933cbb5b3264e7e6639f286e`, 12,094 bytes / 475 lines, sha256 `f37350e595e706de9a041090ba917924c790b8c90b8057bc54040cbfdebad50e`)
- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Scalping%20PullBack%20Tool/README.md (port guide: JustUncleL R1.1 Pine v4 original, 1:1 logic port, HA-on-by-default, 16-parameter default table, no license stated in script header)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; last completed daily close 76,816.00 on 2026-11-02)
