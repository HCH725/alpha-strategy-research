---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Parabolic SAR stop-and-reverse flip two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-31
sources:
  - https://github.com/fmzquant/strategies/blob/master/Parabolic-SAR.md
  - https://www.fmz.com/strategy/366942
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Parabolic SAR stop-and-reverse flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ public strategy mirror plus its embedded Pine block, fetched 2026-10-09):

- Canonical file: https://github.com/fmzquant/strategies/blob/master/Parabolic-SAR.md (`Parabolic-SAR`, FMZ mirror of ChaoZhang's FMZ strategy https://www.fmz.com/strategy/366942, FMZ page stamp Last Modified 2022-05-31, adopted as `source_as_of`). File prose attributes the indicator to J. Welles Wilder's "New Concepts in Technical Trading Systems" (1978) and the Pine code to Alex Orekhov (everget), GPL-3.0, 2019.
- Pinned commit: `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` (latest commit touching this path, 2024-03-03); the file at that commit is byte-identical to the live file (3746 bytes, blob `7ed586252622b076273ccb53cb14bf908f92e23e`, verified by diff before writing). Page-stated FMZ backtest block: `Futures_Binance BTC_USDT`, period `5m`, basePeriod `1m`, 2022-04-30 to 2022-05-29 — FMZ-platform execution context, never presented as Hummingbot semantics (see derived declaration).
- Page-stated rule (verbatim substance): "Parabolic SAR was originally developed by J. Welles Wilder ... It is a trend-following indicator that can be used as a trailing stop loss", with signal inputs Start 0.02 / Increment 0.02 / Maximum 0.2 and Buy/Sell labels on dot-side flips. The page carries no performance table, figure, trade count, or cost basis in its prose — this record claims no source-reported performance (see Evidence).
- Full `//@version=4` block read to the last line. Load-bearing declaration disclosed verbatim: the script declares `study("Parabolic SAR", shorttitle="PSAR", overlay=true)` — an indicator wrapper — yet closes with `if buySignal / strategy.entry("Enter Long", strategy.long) / else if sellSignal / strategy.entry("Enter Short", strategy.short)`. Under TradingView Pine the `strategy.*` calls inside a `study` do not compile; the file's executable context is the FMZ platform (see backtest block above). There is therefore no TV-style next-bar-open source timing to preserve — the same-bar-close execution in this record is a separately identified researcher adaptation, never presented as source-native (see Execution assumptions).
- Pinned signal inputs: `start = 0.02`, `increment = 0.02`, `maximum = 0.2`. This record pins all three defaults; retuning any AF value would be a different, unpinned rule.
- Text census over the pinned block: 0 `request.*`, 0 `security(`, 0 `timeframe(`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=`, 0 `pyramiding`, 0 `process_orders_on_close`, 0 `commission_*`, 0 `default_qty_*`, 0 `volume`, 0 `open` (order-gating reads only `high`/`low` via `sar()` and `close` via the dot-side comparison; `ohlc4` appears solely in a `display.none` plot). Live order calls are exactly two (`strategy.entry("Enter Long", strategy.long)`, `strategy.entry("Enter Short", strategy.short)`). Display-only calls are one `plot` (SAR dots), four `plotshape` (start dots plus Buy/Sell labels), one hidden `ohlc4` plot, one `fill`, and three `alertcondition` lines — none gates any order.
- Licence and rights: upstream Pine is GPL-3.0 (everget); FMZ page is a public strategy mirror. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly two: (1) research market/timeframe BTCUSDT `1d` (the script takes no symbol, timeframe, session, or venue input and reads only `high`/`low`/`close`; the FMZ block's `5m`/`1m` Futures_Binance context is FMZ-platform execution, not HB-modelable source timing); (2) same-bar-close fills on completed-bar decisions (the source has no portable fill timing: a `study` wrapper plus FMZ-engine execution). Both adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formula, AF triple, dot-side latch, flip exclusivity, two-sided direction, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `parabolic`, `psar`, `ta.sar`, `= sar(`, and `sar(` return zero strategy records computing or trading a Parabolic SAR series (the sole prose hit is the word "parabolic" inside an Ichimoku record's hypothesis paragraph, not a strategy). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-family ML/portfolio reconstruction batch, unmerged), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `gann-hilo-activator-state-flip-trend-btcusdt-daily-2026-10-05.md` latches the side of a Hilo-Activator moving-average extreme channel (state-flip, but the trail is a rolling high/low mean, never an accelerating stop); PR #63's SuperTrend flips on ATR-multiplier bands (volatility-scaled range envelopes, no acceleration factor, no extreme-point ratchet). This record instead trades Wilder's accelerating stop-and-reverse dot: an AF-ratcheted SAR series with extreme-point capture, signalled on the side of the dot relative to close with a one-bar flip latch, reversing two-sided — no pool record evaluates `sar(0.02, 0.02, 0.2)`, latches `psar < close`, or reverses long/short on that event. Five-axis distinction: mechanism differs (AF-accelerated stop-and-reverse with EP ratchet, two-sided reversal, versus MA-extreme channels, ATR bands, level-holds, or oscillator crosses), signal construction differs (formula above with the pinned AF triple, nothing in the pool computes it), exits differ (opposite-flip reversal is the sole exit path, no level-recross/time/trailing variant matches), source identity differs (FMZ/ChaoZhang mirror of everget GPL PSAR at pinned commit `87a415e` versus HPotter, Julien_Exe, TV authors, or paper sources), and direction handling differs (both sides live by the source's own two entries versus long-only or gated records).

## Economic mechanism

### Source-reported

Accelerating trailing-stop reversal: the SAR dot starts far from price and accelerates toward it as the trend extends (AF stepping 0.02 → 0.20 cap, extreme point ratcheting each bar), so a flip of the dot from one side of price to the other reads as trend exhaustion-plus-reversal in a single event. The author ships no stop, no target, no trailing order beyond the SAR logic itself: the opposite flip is the entire risk control, and the prose offers the indicator "as a trailing stop loss" with no executable stop rule.

### Research interpretation

Stop-and-reverse state latch with an accelerating trail. Unlike channel-flip records (Donchian/Hilo/SuperTrend), the trail is not a fixed-lookback extreme or a volatility multiple: it is path-dependent, accelerating with trend age and resetting to the prior extreme on every flip, so whipsaw cost concentrates in sideways markets (rapid flip pairs) while trending markets ride one side with a tightening implicit stop. The `dir` latch makes the system state-driven: the book always carries the last flip conviction, long or short, with flat existing only before the first flip. No leverage, sizing, or cost edge is embedded in the signal; sizing lines are absent from the source, so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- SAR series (AF triple pinned): `psar = sar(0.02, 0.02, 0.2)` — Wilder's SAR over `high`/`low` with start 0.02, increment 0.02, maximum 0.20.
- Dot-side latch: `dir = psar < close ? 1 : -1` — strictly below close reads long-conviction, strictly above (or equal-touch edge, which falls to −1 by the comparison) reads short-conviction. The comparison is total on every bar with a valid SAR print, so `dir` is never undefined past seeding.
- Flip events (mutually exclusive by construction — both require opposite consecutive latches, so both can never fire on one bar): `buySignal = dir == 1 and dir[1] == -1`; `sellSignal = dir == -1 and dir[1] == 1`.
- Entries (derived timing): `if buySignal` → long entry at the completed-bar close; `else if sellSignal` → short entry at the completed-bar close. Because both flip conditions are evaluated every bar and pyramiding defaults to a single entry per direction, the first opposite-flip bar closes-and-reverses the position in one step — reversal is the sole exit path by construction.
- Display isolation: the `plot` (SAR dots), all four `plotshape` calls (start dots, Buy/Sell labels), the hidden `ohlc4` plot, the `fill`, and all three `alertcondition` lines gate no order condition; restyling, hiding, or removing any of them cannot alter any admitted event.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` (inside `sar()`) and `close` (dot-side comparison) only. No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe and the classic daily design frame for Wilder systems — never presented as anything beyond that (see Limitations).
- Warmup: no flip can fire before the 2nd completed bar (`dir[1]` is undefined on the first bar, so both comparisons are false and nothing fires). This record adopts a 5-bar warmup so the AF/EP recursion is seeded before any admitted event. No repainting, no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads high/low/close only; venue transfer is never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is FMZ-platform execution under a `study` wrapper (quoted verbatim in Provenance) — this record does not claim any TV next-bar-open source timing. No maker-touch, queue, or intrabar-path-dependent fill. 0 `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule.
- Sizing/capital: the source carries no quantity or capital line at all, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (Pine default: one open entry per direction). The default is load-bearing and therefore pinned explicitly: repeat same-side bars during an open position are rejected no-ops, and the opposite-flip bar closes-and-reverses in a single step (no separate exit call exists or is needed). Re-entry after any pre-first-flip flat state occurs on the next flip bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page ships the Wilder lineage, the AF input triple (0.02/0.02/0.2), the dot-side Buy/Sell label logic, the two-sided entry construction, and the FMZ backtest block (Futures_Binance BTC_USDT, 5m/1m, 2022-04-30→05-29) with a backtest-chart image but no readable performance table in the mirrored text. This record claims no source-reported performance numbers and no reproduced performance, and does not rely on the page's image. (This record adopts BTCUSDT `1d` as a predeclared research frame and claims no source-venue or source-timeframe semantics.)

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the opposite-flip entry is the sole exit path by construction, and the prose promises no stop or target beyond the SAR logic itself.
2. Flip exclusivity proven: `buySignal` requires `dir==1 and dir[1]==-1` while `sellSignal` requires `dir==-1 and dir[1]==1` — both cannot hold on one bar, so the `if/else-if` ordering never selects between competing signals; no priority rule is needed or invented.
3. First-bar determinism: on the first bar `dir[1]` is undefined, both comparisons are false, and nothing fires — the book starts flat, never a phantom side; the adopted 5-bar warmup additionally fences AF/EP seeding.
4. Equal-touch edge named: `psar == close` falls to `dir = -1` by the strict `<` comparison — deterministic, pinned, and symmetric with the source verbatim (no smoothing or tolerance invented around it).
5. Display-free gating: `plot`/`plotshape`/`fill`/`alertcondition`/hidden-`ohlc4` calls appear in no order condition; the Buy/Sell labels visualize the same flip booleans the entries consume, adding no independent condition.
6. Price-field minimalism: `open` and `volume` are absent from the entire block, so session gaps, opens, and volume reporting cannot influence any admitted event — gap behavior is absent rather than approximated.
7. The AF triple, dot-side latch, flip definitions, pyramiding default, and two-sided direction are pinned, not removed: retuning start/increment/maximum, thresholding the SAR distance, gating on ADX/labels/alerts, adding a stop/target/cooldown/session filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame and same-bar-close fills, both predeclared above; every signal, threshold, default, state transition, and risk posture is source-verbatim. This record is therefore never evidence that the FMZ-platform source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: AF triple 0.02/0.02/0.2 / dot-side latch / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Acceleration relevance: trading the flip of a non-accelerating trailing stop (fixed-distance SAR with start == increment == maximum, same latch and reversal) must not reproduce-or-beat net expectancy; fail ⇒ the AF acceleration adds nothing over a plain trailing-dot flip.
- F2 — Reversal relevance: holding each flip entry for a fixed research-defined bar count instead of the opposite-flip reversal must not improve net expectancy; fail ⇒ the always-in reversal adds nothing over time exits.
- F3 — SAR relevance: trading close-vs-own-average crosses (plain SMA cross with a research-defined length, same two-sided reversal) must not reproduce-or-beat net expectancy; fail ⇒ the SAR construction adds nothing over a basic trend-cross and the record is a label variant of one.

## Crypto portability

Pinned to BTCUSDT perps under the house overlay. The high/low/close two-sided logic ports to perps without structural change; a spot-only deployment would require disabling the short side and would be a different, unpinned rule. No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (`open`/`volume` are never referenced); `close` is the completed-bar print, so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source executes under FMZ-platform semantics inside a `study` wrapper; this record executes same-bar-close. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Always-in exposure: after the first flip the latch never returns to flat, so the book carries overnight/weekend-equivalent risk on every bar with no neutral stance available by construction.
- No price stop: adverse excursion after entry has no guardrail beyond the opposite flip; a vertical-against move reverses only when the dot changes side, which the AF cap (0.20) can delay in extended parabolic runs.
- Chop whipsaw: in a sideways market the dot alternates side on consecutive bars, printing long-short reversal pairs with no structural filter — the source provides none and this record invents none.
- Warmup cost: the adopted 5-bar warmup blinds the first bars of any 1d evaluation window (deterministic seeding, but incomplete AF/EP history).
- Performance evidence is absent: the mirrored page reports no readable numbers; nothing here is calibrated, fitted, or tuned to any backtest.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- FMZ strategy mirror, pinned commit `87a415edf7b08065fbcbfbfefb7351cd929e4dbd` (fetched 2026-10-09): https://github.com/fmzquant/strategies/blob/master/Parabolic-SAR.md
- FMZ canonical strategy page (ChaoZhang, 2022-05-31): https://www.fmz.com/strategy/366942
- Pine strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
