---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BBI four-SMA cross long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://github.com/mihakralj/QuanTAlib/blob/fc207de37dd2fd471c06b3af581d7e870c0dba81/lib/oscillators/bbi/bbi.pine
  - https://www.tradingview.com/script/QmGxhXJ7/
  - https://www.tradingview.com/script/hKQvERLU-BBI-Bollinger-Bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BBI four-SMA cross — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical code (fetched live over HTTPS this cycle, immutable pin):** `mihakralj/QuanTAlib` commit **`fc207de37dd2fd471c06b3af581d7e870c0dba81`** (committer date 2026-09-23T19:14:07Z, verified via GitHub API this cycle), file **`lib/oscillators/bbi/bbi.pine`**, blob `fb0abcf3b446656b5c190ae29078e324b587c6a3`, **2,817 bytes / 98 lines**, Apache License 2.0 (cited, not copied), `indicator("Bulls Bears Index (BBI)", "BBI", overlay=true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle are byte-identical (second download `cmp`-matched); `git hash-object` of the working copy reproduces the API blob SHA exactly. Defaults pinned in code: source `close`, `p1 = 3` (Ultra-Short), `p2 = 6` (Short), `p3 = 12` (Medium), `p4 = 24` (Long); return value `(sma1 + sma2 + sma3 + sma4) / 4.0`.

**Upstream convention (cited, not copied):** the live TradingView page `https://www.tradingview.com/script/QmGxhXJ7/` (BBI - Bull and Bear Index, author AgentC) returned HTTP 200 this cycle and states the formula `BBI = (3 days average price + 6 days average price + 12 days average price + 24 days average price) ÷ 4`, the regime frame (price above BBI = long market, below = short market), and the switch rule (a breakthrough against BBI is the long/short regime change) — all cited as source-reported prose, never adopted as crypto claims. The live TradingView page `https://www.tradingview.com/script/hKQvERLU-BBI-Bollinger-Bands/` (BBI Bollinger Bands, author xbj) returned HTTP 200 this cycle and states the construction (`an average of 4 SMAs (3, 6, 12, 24) as a cut-off of a bullish/bearish trend`) plus the executable core (`you can enter when close> BBI and exit when close<BBI`) — cited as the source-reported entry/exit sentence this derivative pins.

**Order-affecting logic read verbatim (the composite governs; the indicator ships no orders):** four hand-rolled circular buffers (`var array.new_float(p)`, head index, running sum, seen-count `cnt`); per bar `val = nz(source)`; eviction rule `old = get(buf, head)`: `na` old → `cnt += 1`, else `sum -= old`; then `sum += val`, store, advance head modulo `p`; leg value `sma = sum / max(1, cnt)`. Post-warmup (all four `cnt` capped at their `p`) each leg equals the exact arithmetic mean of the last `p` closes — identical to `ta.sma(close, p)` on valid history; pre-warmup legs are ramp-up partial means dividing by bars-seen, never `na` (fenced in Negative evidence 1). Input guards `runtime.error` on any period ≤ 0 or > 5000 — a pinned absence of degenerate lengths, not a trading rule.

**Pine-block census (whole-file fence):** 1 `indicator(`; 0 `strategy.*` of any kind; 5 `input.*` (1 source + 4 int); 0 `alertcondition(`; 0 `plotshape(`; 1 `plot(`; 0 `request.*` / `security(`; 0 `crossover` / `crossunder` / `ta.cross`; 0 `ta.sma` / `ta.ema` / `ta.rsi` / bare `sma(`/`ema(`/`rsi(` (the four averages are explicit circular buffers, no library moving-average call); 2 `runtime.error`; 4 `array.new_float`; 0 volume reads. Arithmetic corollary (not a new rule): with defaults, the most recent 3 closes each carry weight 15/96, bars 3–5 carry 7/96, bars 6–11 carry 3/96, bars 12–23 carry 1/96 — front-loaded vs a flat 1/24 single SMA, so the composite is not a relabeled SMA(24).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the pinned code is a display indicator and ships no entries, exits, sizing, or risk, and neither TradingView page ships sizing, costs, warmup, or fill timing. Researcher-declared adaptations are exactly seven: (1) long-only pin with the short side explicitly disabled (down-cross events exit LONG to FLAT and never open SHORT, disclosed); (2) fixed **0.01 BTC** spot sizing (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above verified 5-USDT min-notional and 0.00001 min-qty); (3) all risk legs (SL/TP/trailing/time) explicitly disabled — cross-exit-only risk, disclosed; (4) 240-bar warmup with pre-warmup bars flat (10× the longest leg 24; SMAs are finite-window exact so post-25 state is seed-free — fenced); (5) display drop (the single plot, colors, linewidth, overlay styling) plus explicit rejection of xbj's Bollinger-variation legs and extreme-sentiment markers and of zone-qualified (high/low-region) BBI readings, which carry no coded thresholds (fenced); (6) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (7) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim).

**Immutable derivative identity:** `TV:AgentC-QmGxhXJ7+xbj-hKQvERLU|quantalib-fc207de-bbi.pine|bbi_sma3-6-12-24_price-cross_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup240|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@f35a46c7` (550 root strategy records, READMEs excluded; this file is the 551st). Case-insensitive content search for `bbi` returns zero strategy records (only `forven/strategies/base.py` path-substring hits inside six forven Evidence paragraphs — provenance-citation artifacts, none a BBI-index record); filename search for `bbi` / `bull-bear` / `bullbear` / `four-sma` returns zero records. No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different filter and event vs all single-MA price-cross records (`fmz-smma17-price-cross`, `alma-cross-volume-gate`, `hull-ema-crossover-reversal` — one average each, never a four-SMA arithmetic composite); different math and event vs `tradingview-tasc-linreg40-slope-sign` (least-squares regression-endpoint slope sign — no mean, no price cross) and vs `github-indie-hull-suite-slope-state` (WMA-weighted Hull slope state — no SMA composite, no cross); different smoothing and exits vs `tradingview-systemsoverfeelings-kama40-slope-flip-close-bracket` (efficiency-ratio-adaptive KAMA with a −6%/+3% close-bracket box — here fixed SMA legs with flip-only exits and no box); different event vs all 39 `bb` records (band-touch / %B / bandwidth events — xbj's own Bollinger-variation legs are explicitly dropped here); different oscillator vs `tradingview-kaambhaari-arpeet-zlmacd-zeroaxis-cross` (zero-lag MACD axis cross — no price-vs-average event). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

BBI (per AgentC, xbj, and the pinned code header): the arithmetic mean of four simple moving averages (3/6/12/24) of close — a committee of ultra-short, short, medium and longer trends forced to agree on one number; price above the line reads as bull dominance, below as bear control, and the breakthrough is the regime boundary. xbj adds the executable sentence: enter when close > BBI, exit when close < BBI. xbj's Bollinger variations of BBI and its "possible entry and exit" extreme-fear/optimism markers are published as experimental ("for fun … not necessarily working yet") and are NOT adopted (fenced in Negative evidence 4).

### Research interpretation

Unlike pool single-MA crossers that follow one smoothing of price, and unlike pool slope-flippers that trade the derivative of an average (KAMA40, Hull suite, TASC linreg), this machine trades the price's position against a fixed four-horizon consensus mean — entering only on confirmed upward breakthroughs and exiting only on confirmed downward breaks, long-only, with no box, no slope condition, and no adaptive leg. The bet, as derived, is purely that this front-loaded consensus-cross alternation ports arithmetically to BTCUSDT spot daily bars, with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series: `C[t]` closes are the sole signal input. `O/H/L` are validity only. No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- R3 — BBI composite (source formula, pinned): `BBI[t] = (SMA(C,3)[t] + SMA(C,6)[t] + SMA(C,12)[t] + SMA(C,24)[t]) / 4`, each leg the exact arithmetic mean of the last N closes. Post-25-bar state equals the pinned circular-buffer code on valid history (ramp-up transient fenced); any period ≤ 0 or > 5000 is rejected by the pinned guards and is unpinned here.
- R4 — Events (promoted machine, adaptation 1, xbj sentence pinned to strict inequalities): `Buy[t] = C[t] > BBI[t] and C[t−1] <= BBI[t−1]`; `Sell[t] = C[t] < BBI[t] and C[t−1] >= BBI[t−1]` (mutually exclusive by construction — at most one fires per bar; an equality on the current bar emits no event and holds position, disclosed; first-valid-pair requirement fenced).
- R5 — Position (promoted machine, adaptation 1): `LONG`/`FLAT` single-unit book. If FLAT and `Buy[t]` (post-warmup) → request LONG at the next open. If LONG and `Sell[t]` → exit the whole book at the next open. Short-side events while FLAT are explicit holds (short side disabled). A prevailing above-BBI state with no fresh post-warmup `Buy` never enters (entry needs the cross, disclosed).
- R6 — Risk legs (adaptation 3, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls, zero `alertcondition(` legs).
- R7 — Position state: one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none. No pyramiding: while LONG no new Buy can add (entry needs FLAT, R5) — pinned absence, not invented.
- R8 — Warmup and gaps: flat until 240 completed `1d` bars (10× the longest leg 24; SMA legs are finite-window exact with no recursive seed, so any warmup ≥ 25 prints the identical post-warmup event set — the 240 margin is convention, fenced). Evaluated legs run from bar 1 so post-warmup state is deterministic. Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold (covers the pinned `nz(source)` substitution path by refusing it).
- R9 — Invariant identifier: `TV:AgentC-QmGxhXJ7+xbj-hKQvERLU|quantalib-fc207de-bbi.pine|bbi_sma3-6-12-24_price-cross_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup240|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `close` (sole signal input), `open`/`high`/`low` (validity only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used. Every live input is frozen at the decision close — point-in-time clean.
- Warmup: flat until 240 completed bars (structural). No repainting (all four legs read closed-bar closes only and are append-only; finite 25-bar memory, no recursive seed), no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03 — the 11-04 bar was still forming at cycle time — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. The four-SMA composite plus confirmed cross is a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned file ships every adopted headline fact quoted in Provenance: the `input.source(close)` + `input.int(3/6/12/24)` defaults, the four circular-buffer legs with their `cnt`-capped means, the `(sma1 + sma2 + sma3 + sma4) / 4.0` return, the `runtime.error` period guards, and the `indicator(` (not strategy) declaration. It ships zero orders, zero sizing, zero exits, zero cross logic, zero performance figures — none adopted; all trading semantics are researcher pins disclosed above. The live AgentC page additionally reports the (3+6+12+24)/4 formula, the above = long / below = short frame, and the breakthrough-switch rule; the live xbj page additionally reports the 4-SMA cut-off construction and the enter-on-above / exit-on-below sentence — cited as source-reported page evidence, not as Hermes reproduction.

### Independently reproduced

Not independently reproduced. No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. No executable probe ran in this unattended cycle; logic assertions above are static readings of the pinned fence, fenced in Negative evidence where implementations may differ.

### Negative evidence

1. Ramp-up fence: the pinned code's pre-warmup legs are partial means (sum divided by bars-seen, `nz(source)` for `na`) — never `na`. An implementation gating legs `na`-until-full (e.g. `ta.sma` style) prints different pre-25 values; the 240-bar warmup absorbs all of it and any shorter warmup is unpinned — flagged as an implementation obligation, never strategy behavior.
2. Equality fence: a current-bar `C == BBI` equality is neither Buy nor Sell; position holds. An implementation treating equality as a cross leg prints a different, unpinned event set.
3. First-valid-pair fence: a cross needs both `BBI[t]` and `BBI[t−1]` evaluated on valid history; the first evaluable bar alone emits no event. Absorbed by the warmup; shorter warmups print different early event sets and are unpinned.
4. Dropped-legs fence: xbj's Bollinger variations of BBI, its experimental extreme-sentiment markers, the cmoney-style high/low-zone qualifiers (no coded thresholds), and the published 5/10/15/20 variant lengths are adopted nowhere — an implementation trading any of them prints a different, unpinned event set.
5. `nz(source)` fence: the pinned code substitutes 0 for an `na` source; this record instead holds on any nonfinite/non-positive OHLC bar (R8) — the substitution path is refused, never strategy behavior.
6. FP fence: leg sums span at most 24 closes; cross-implementation summation order may differ in the last ulp on pathological input — fenced as an implementation obligation; live tape carries no constant stretches so no live event turns on it.
7. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
8. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (long-only pin, fixed sizing, disabled risk, 240-bar warmup, display/drop-leg rejection, 0.1% cost overlay, next-open fills); the four lengths, close source, composite mean, inequalities, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.
9. Mirror-vs-page drift fence: the code freeze is the QuanTAlib blob `fb0abcf3…`; the TradingView pages are cited for formula prose and the entry/exit sentence only. If a page's current code ever differs from the blob, this record follows the blob.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `SMA(3/6/12/24)` composite / strict confirmed cross / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 240-bar warmup are frozen.

- F1 — Composite relevance: a single-SMA(24) price-cross twin (same rest) must not improve net expectancy; fail ⇒ the four-horizon consensus is decoration on a plain MA cross.
- F2 — Length relevance: a (5/10/15/20)-leg twin (same rest) must not improve net expectancy; fail ⇒ the 3/6/12/24 convention carries no information.
- F3 — Cross relevance: a BBI-slope-sign twin (enter on BBI rising while above, exit on BBI falling) must not improve net expectancy; fail ⇒ the breakthrough cross adds nothing over slope state.
- F4 — Warmup relevance: a 300-bar-warmup twin must print the identical post-300 event set (finite 25-bar memory ⇒ structural identity is expected); fail ⇒ seed or ramp transients leak past the declared warmup.
- F5 — Entry-timing relevance: a state-entry twin (enter at the first post-warmup above-BBI open and hold like-for-like exits) must not improve net expectancy; fail ⇒ cross timing is decoration on buy-and-hold-above.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; close-only signal input — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The pinned code is Apache-2.0, © mihakralj (cited, not copied; short literals only); every trading semantic (long-only pin, cross exits, venue, sizing, warmup, no-box risk, next-open fills, cost overlay) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as any author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- Ramp-up behavior, equality handling, first-pair requirement, `nz(source)` refusal and degenerate-input FP behavior are implementation-defined (Negative evidence 1–3, 5–6); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (240) is a researcher margin at 10× the longest leg 24; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/mihakralj/QuanTAlib/blob/fc207de37dd2fd471c06b3af581d7e870c0dba81/lib/oscillators/bbi/bbi.pine (canonical pinned code; commit `fc207de37dd2fd471c06b3af581d7e870c0dba81`, blob `fb0abcf3b446656b5c190ae29078e324b587c6a3`, 2,817 bytes / 98 lines, sha256 `2d8304ef686e54151cb318a38f1911d86ab81cb5298294ba0dc3f212c2be2c92`)
- https://www.tradingview.com/script/QmGxhXJ7/ (upstream convention page, AgentC; HTTP 200 verified this cycle; (3+6+12+24)/4 formula, above-long / below-short frame, breakthrough-switch rule — cited not copied)
- https://www.tradingview.com/script/hKQvERLU-BBI-Bollinger-Bands/ (upstream entry/exit page, xbj; HTTP 200 verified this cycle; 4-SMA cut-off construction, enter-when-above / exit-when-below sentence — cited not copied)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; last completed daily close 77,453.86 on 2026-11-03)
