---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LePotoRico Bollinger-squeeze width-gated breakout bracket two-sided on BTCUSDT 1h bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-04
sources:
  - https://github.com/LePotoRico2105/pine-script-strategies/blob/e8bb2935b98ca446ad1063fb75a500410d344c5a/strategies/bollinger_squeeze.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Squeeze Breakout (width-gated, bracket exits) — independent BTC-USDT 1h two-sided derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `LePotoRico2105/pine-script-strategies` commit **`e8bb2935b98ca446ad1063fb75a500410d344c5a`** (2026-04-03 — still the repo HEAD, verified live this cycle via the commits API), file **`strategies/bollinger_squeeze.pine`**, blob `6137b9104ddd9cb2799192ad53c13ac634d1c908`, **1,778 bytes / 51 lines**, Pine v5, `strategy("Bollinger Squeeze Breakout", ...)` — a real strategy with native entries and exits, not an indicator. Raw bytes re-downloaded this cycle hash to sha256 `4b815e67144c437de11c384832e2b4df77d4ec83d263dc8c85762e7e4c18b778`, byte-identical to the working copy. Permalink above. Repo license is **MIT** — short-literal citation only, no source block reproduced. Same repository family as the merged `github-lepotorico-smc-ob-fvg` record (a different file, mechanism, and timeframe — fenced below).

**Order-affecting logic read verbatim (code governs):** source defaults `bbLen = 20` / `bbMult = 2.0` / `squeezeFactor = 0.75` / `lookback = 20`; declaration `strategy("Bollinger Squeeze Breakout", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=2)`; bands `basis = ta.sma(close[1], 20)`, `dev = 2.0 * ta.stdev(close[1], 20)`, `upper/lower = basis ± dev`; squeeze `bbWidth = upper - lower`, `avgWidth = ta.sma(bbWidth, 20)`, `isSqueeze = bbWidth < avgWidth * 0.75`, recency `recentSqueeze = ta.barssince(isSqueeze) < 5`; triggers `longSignal = recentSqueeze and close[1] > upper and close[2] <= upper[1]` (mirrored short); risk `distToMiddle = math.abs(close - basis)`, entries `strategy.entry("Long", strategy.long)` / `strategy.entry("Short", strategy.short)`, brackets `strategy.exit("Long Exit", "Long", stop=sl, limit=tp)` with `sl = basis`, `tp = close + distToMiddle * 2` (mirrored short). The README's strategy-details §4 prose matches the code (width < 20-period average × 0.75 gate, post-squeeze band-close breakout both sides, middle-band stop, 2× distance target, H1).

**Pine-block census (51-line fence):** 1 `strategy(`; 2 `strategy.entry` / 2 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`; 0 `request.*` / 0 `security(` / 0 `lookahead` / 0 `input.session` / 0 `timeframe.*` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` / 0 `process_orders_on_close` — all recorded as absent, never filled in. `wasSqueeze = isSqueeze[1]` is computed and never read (dead diagnostic — fenced as inert, disclosed). Zero `open` / `volume` reads (the rule consumes `close`/`high`/`low` only — `close` directly; `high`/`low` nowhere, the rule is pure-close arithmetic). Every predicate reads `[1]`/`[2]`-shifted confirmed data only — the repo's "anti-repainting" header claim holds for the ported legs (verified by construction, disclosed as code fact, not adopted marketing). The README's backtest figures (534 trades, 47.2% win, PF 1.52, MDD 13.1%, Sharpe 1.31, "10 years of M1", 2-pip-spread Backtrex methodology) have no auditable trade-level provenance in the pinned source and are **explicitly not adopted** — none appears below.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the market/timeframe pin (source tested forex H1 per its README; this record pins Binance BTC-USDT perpetual 1h), fixed **0.01 BTC** sizing with 10,000 USDT cash, **0.0005/side** researcher fee and Isolated 1× (source: 2% of equity), close-decided next-bar-open fills for the stop/limit legs (Pine fills `strategy.exit` stops/limits intrabar — the research-model timing convention differs, disclosed), the stop-first same-bar resolution with opposite-setup precedence (below, disclosed), the degenerate-straddle skip (below, disclosed), and the 60-bar warmup floor (below, disclosed) are researcher adaptations. All are completely specified here; original claims are kept separate above.

**Immutable derivative identity:** `GH:LePotoRico-e8bb293|bbsqueeze-BB20x2.0_width0.75xSMA20_recency5b_basis-SL_2R-TP|independent-derived-v1|BinanceFutures:BTC-USDT:1h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|opposite-first-stopfirst-tiehold|warmup60|2026-11-04`. Changing any formula, length, multiple, recency, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@8e15341a` (553 root strategy records, READMEs excluded; this file is the 554th). Filename search for `lepoto.*bb` / `bbsqueeze` / `bollinger_squeeze` returns zero signal records (the sole `bb_squeeze` hit is the Forven Python file, fenced below). Whole-word content search for `avgWidth` / `recentSqueeze` / `squeezeFactor` / `6137b91` returns zero records (bare `0.75` hits are unrelated ATR multipliers and formation bands, fenced in Negative evidence). No open `research/*` PR is this file, author file, or construction (17 open PRs enumerated — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Not a duplicate, paraphrase, or trivial parameter variant: five-axis distinction vs nearest pool neighbors is recorded in Negative evidence.

## Economic mechanism

### Source-reported

Volatility compression precedes expansion: when the Bollinger width compresses below 75% of its own 20-bar average the market is coiling; the strategy buys the close that breaks back above the upper band within 5 bars of a squeeze (mirror short), stops at the 20-bar middle band, and targets twice the entry-to-midline distance. No behavioural channel beyond this construction is claimed in the 51 lines.

### Research interpretation

Unlike pool squeeze records that gate on BB-inside-Keltner nesting (Forven, long-only, midline-hold exit) or on oscillator release with momentum-tick exits (SQZMOM-LB, LazyBear), this machine gates purely on the band's own width history (no second envelope, no oscillator, no trend filter) and exits purely on a latched 2R price bracket (no trailing exit, no opposite-cross exit, no time stop). The failure mode is plain: a squeeze that resolves into chop fires breakout entries that stop at the midline, and a vertical expansion without any preceding compression never enters at all.

## Signal

Index completed UTC 1-hour bars `t = 0, 1, ...` with real Binance BTC-USDT perpetual `C[t]` for every signal/risk leg. A bar with missing/nonfinite/non-positive close is invalid for signals. All constants are source-default literals; `ta.stdev` is pinned at its Pine default (biased/population, ÷N).

- **Bands (causal, per-bar):** `M[t] = SMA(C[t-1..t-20])`; `D[t] = 2.0 × pstdev(C[t-1..t-20])`; `U[t] = M[t]+D[t]`; `L[t] = M[t]−D[t]`; `W[t] = U[t]−L[t]`; `A[t] = SMA(W[t..t-19])`. First valid `M/D/U/L/W` is bar 20 (0-based; 21st completed bar); first valid `A` and `isSqueeze` is bar 39 (0-based; 40th completed bar).
- **Squeeze (source-exact):** `SQ[t] = W[t] < A[t] × 0.75` (unknown while `A[t]` is `na` — never fires); recency `RS[t] = (bars-since-last-`SQ` at t) < 5` (`na`-never counts as stale-false, source-exact `barssince` semantics).
- **Predicates (actionable only t ≥ 60, at bar `t`'s close):** `long[t] = RS[t] and C[t-1] > U[t] and C[t-2] <= U[t-1]`; `short[t] = RS[t] and C[t-1] < L[t] and C[t-2] >= L[t-1]`. Pre-warmup bars flat by record rule. Long/short legs are provably mutually exclusive on every bar (`U[t] ≥ L[t]` always since `D[t] ≥ 0`; `C[t-1]` cannot be both strictly above `U[t]` and strictly below `L[t]`) — no entry tie-break is required; flat with both legs is unreachable by construction.
- **Source-arithmetic risk (latched at signal bar `t`, never moved):** long `SL = M[t]`, `TP = C[t] + 2×|C[t]−M[t]|`; short mirror `SL = M[t]`, `TP = C[t] − 2×|C[t]−M[t]|`.
- **Degeneracy guard (explicit researcher pin):** entries require the bracket to straddle the reference (`SL < C[t] < TP` long, `TP < C[t] < SL` short); otherwise neither-fire hold. Pine would submit `na`/inverted legs — the guard is disclosed and never attributed to source. No division exists anywhere (zero-division impossible); the all-equal window (`D = 0`, `U = L = M`) fires nothing by the strict inequalities.
- **Resolution (explicit researcher pin):** entries/reversals fill next-bar-open MARKET. Each held bar `v` (fill bar +1 onward) is evaluated at its close in fixed order — opposite setup first (reversal dominates: close then re-enter at next open), else SL-touch (`L[v] <= SL` long / `H[v] >= SL` short), else TP-touch (`H[v] >= TP` long / `L[v] <= TP` short); SL+TP co-fire is one flat close (stop wins). Single position, no adds: same-side refire while positioned is a no-op under the pinned pyramiding-0 rule; re-entry re-arms on any qualifying post-exit signal with no cooldown (explicitly none, not invented).

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (every order-gating line reads `close` with fixed non-negative shifts; no `open`, no `high`/`low`, no `volume`, no funding/OI/mark-price leg, no calendar, no multi-asset input). Exit touches are evaluated against the completed bar's `H/L` range under the research-model convention (disclosed above).
- Warmup: 60 completed `1h` bars flat by record rule (structural minimum is the 40th completed bar — 20-bar band seed plus 20-bar width-average seed plus the prior-band cross reference — plus researcher margin).
- Point-in-time: every window trails over completed bars only; the signal bar's own close is the last input and the bracket-latch reference; fills at next-bar open. No repainting, no negative shift, no future reference, no full-sample normalization, no MTF call, no session template. Exactly one evaluation per completed bar.

## Execution assumptions

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (local checkout `2dbc844` verified this cycle: `BacktestingEngineBase.run_backtesting` present in `backtesting_engine_base.py`, `determine_executor_actions` in the controller bases, `OrderExecutorSimulator` class byte-present in `backtesting/executors_simulator/order_executor_simulator.py`, `INTERVALS "1h": 3600` in `binance_perpetual_candles/constants.py`). A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT perpetual, one 1h OHLC stream (single-feed design — no MTF, no session, no second symbol). Next-open MARKET fills for entries and reversals (source-native Pine default timing); the stop/limit bracket is resolved close-decided against completed-bar `H/L` with next-open fills (research-model convention differing from Pine intrabar exit fills, disclosed — same bracket class as the merged SMMA17 and SMC sibling records).
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the width-gated breakout state machine, the latched basis-SL/2R-TP bracket, and the opposite-first stop-first tie-hold pin. The generic executor does not calculate the strategy.
- **Sizing/capital (stated plainly):** fixed 0.01 BTC per position, 10,000 USDT cash admission, Isolated 1×, 0.0005/side researcher fee plus modeled funding with explicit limitations (modeled funding is never reported as realized funding; no hypothetical zero funding claimed). The downstream house overlay changes no trade event under the predeclared single-position rule — DCA is a downstream execution experiment, never an admission leg of this version.
- **Risk posture (explicit):** the latched stop+limit bracket is the sole position-ending path besides opposite-signal reversal. Trailing stop, breakeven move, time stop, partial exit, and averaging are absent in source and recorded as explicitly disabled, never defaulted. An end-of-sample open position is marked at the last real valid close, never closed with an invented fill. Missing trade prices are never fabricated (pre-warmup and invalid bars stay flat).

## Evidence

### Source-reported

The pinned 1,778-byte file ships the complete construction (frozen `bbLen 20` / `bbMult 2.0` / `squeezeFactor 0.75` / `lookback 20`, SMA midline, population-stdev bands, width-vs-average squeeze gate, 5-bar recency, confirmed-close band-cross triggers both sides, midline stop, 2× distance target, two-sided stance, pyramiding-0 default). It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: the file holds exactly one long predicate and one short predicate over shared series — no second decision path, no variant menu, no timeframe input to select between.
2. No estimator ambiguity: `ta.sma`/`ta.stdev`/`ta.barssince` are Pine built-ins with pinned default semantics; no ATR, no RMA/EWM, no Wilder alternative exists anywhere in the 51 lines.
3. `wasSqueeze` quarantine, stated plainly: computed on every bar and read by zero order-gating comparisons — treating it as a gate, filter, or exit leg would be a different, unpinned rule.
4. Sizing quarantine, stated plainly: the `strategy.percent_of_equity / 2` declaration is replaced by the fixed 0.01 BTC research sizing (see Execution assumptions) — position-size changes no signal, gate, trigger, or bracket arithmetic.
5. Pool squeeze cousins fenced, stated plainly: `forven-bb-squeeze-breakout-long-flat-btcusdt-1h` gates on prior-bar BB-inside-KC nesting (SMA-ATR Keltner pair), is long-only, and exits on midline recross with no bracket — different gate × different exit × different direction × different immutable source; `sqzmom-lb-squeeze-release-ema100-two-sided-btcusdt-1d` triggers on linreg-momentum transitions with momentum-tick exits plus an EMA100 gate — different trigger × different exit × different gate × different source; `forven-ttm-squeeze-momentum-release` is unadmitted and rides in no open `research/*` PR. Bare `0.75` literals elsewhere in the pool are ATR stop multipliers and formation-band widths, never a width-ratio squeeze gate.
6. Same-repo sibling fenced, stated plainly: `github-lepotorico-smc-ob-fvg-bos-retrace-two-sided-btcusdt-4h` cites `strategies/smc_ob_fvg.pine` (order-block + FVG + BOS confluence, 4h) — different file, different mechanism, different timeframe, different risk arithmetic. Consolidating the two into one record would erase load-bearing event differences.
7. README-figure fence, stated plainly: the README §4 results table and Backtrex methodology paragraph are named here only to show they were read and rejected — vendor backtest marketing without trade-level provenance is never evidence, and none of its numbers enters this record.
8. Researcher self-check (logic only, never a backtest, never committed — scratch tape, 78 synthetic 1h bars, volatile→compression→breakout): squeeze gate flags exactly the compression span, the breakout LONG fires inside the 5-bar recency with a straddling bracket latch, zero dual-fire bars, and the all-equal degenerate window fires nothing. `SELF-CHECK OK`. No Qlib/Hummingbot parity, no live/paper order, no profitability experiment occurred.

## Falsification plan

A pinned-engine replay that (a) recomputes `M/D/U/L/W/A/SQ/RS` from completed 1h closes and matches the specified long/short event bars exactly, (b) honors next-open fills with the latched bracket resolved opposite-first stop-first from fill-bar+1, and (c) preserves the warmup-60 flat prefix, falsifies this record if any event, price, or direction disagrees. Any parameter change (band length, sigma multiple, squeeze factor, width-average length, recency window), any gate substitution (Keltner nesting, oscillator release, trend filter), any exit substitution (midline hold, trailing stop, time stop), or any timing change (same-bar-close, intrabar fills) is a different derivative and does not falsify this one.

## Crypto portability

The rule reads `close` geometry only and ports to any continuously quoted BTCUSDT perpetual 1h feed. The short legs require a short-capable venue (Binance USDT-M perpetual satisfies this); on a spot-only venue the short legs are inexpressible and the record would not be the same rule. Min-notional/precision: 0.01 BTC notional exceeds the 5-USDT minimum by orders of magnitude at any plausible BTC price; quantity step is exact. No calendar, session, or venue-specific tick assumption conditions any signal.

## Limitations

- The stop/limit bracket timing is a disclosed research-model convention (close-decided, next-open fills), not Pine intrabar fills — live/historical slippage through the stop inside a wide-range bar is not modeled beyond the stop-first co-fire rule.
- Exits begin evaluating on fill-bar+1: a fill bar that spans the full bracket range holds through its close by record rule (disclosed, never a source claim).
- The README's forex H1 provenance means crypto-1h behavior is a venue port, not a source-tested claim; no profitability, Sharpe, or win-rate expectation is carried over.
- Single fixed-size position: concurrent-signal capacity, portfolio margin interaction, and multi-strategy capital contention are out of scope for this admission version.
- `ta.stdev` population semantics are pinned as written; substituting sample (÷(N−1)) stdev would be a different, unpinned rule.

## Implementation status

Not implemented. No controller, executor config, Qlib recipe, or deployment artifact exists for this derivative. Admission is an engineering-capability check on the bounded path above, not an executable materialization.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derivative is causally expressible on the pinned backtest model — not profitable, not Qlib-paritied, not survivor-certified, not authorized for any live capital.

## Related Wiki records

None.

## Sources

- https://github.com/LePotoRico2105/pine-script-strategies/blob/e8bb2935b98ca446ad1063fb75a500410d344c5a/strategies/bollinger_squeeze.pine (immutable rule source — read end to end this cycle)
- https://github.com/LePotoRico2105/pine-script-strategies (repository, MIT license, README strategy-details §4 prose — rules adopted, figures rejected)
- https://www.tradingview.com/pine-script-reference/v5/ (ta.sma / ta.stdev biased-default / ta.barssince na semantics / strategy.exit stop-limit / pyramiding-0 default)
- https://www.tradingview.com/pine-script-docs/concepts/strategies/ (broker-emulator default next-bar-open fills)
