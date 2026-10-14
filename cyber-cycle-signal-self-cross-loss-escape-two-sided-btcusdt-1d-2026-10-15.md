---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Cyber Cycle signal self-cross with 8-bar loss-escape reversal two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2018-09-13
sources:
  - https://www.tradingview.com/script/yrCo4RtN-Ehlers-Cyber-Cycle-Strategy/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cyber Cycle signal self-cross with 8-bar loss-escape reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (TradingView canonical strategy page plus its full open-source block, fetched 2026-10-15 in a real browser session):

- Canonical page: https://www.tradingview.com/script/yrCo4RtN-Ehlers-Cyber-Cycle-Strategy/ (`Ehlers Cyber Cycle Strategy` by `Tr0sT`, `OPEN-SOURCE SCRIPT`, page stamp Sep 13 2018, adopted as `source_as_of`). Page description verbatim in substance: `Ehlers Cyber Cycle Strategy by John Ehlers from his book "Cybernetic Analysis for Stocks and Futures".` Page tags: Centered Oscillators, ehlers, Exponential Moving Average (EMA), strategy. Original-authorship lineage (John Ehlers, book) is preserved here, never claimed by the page publisher. The page carries no performance table, figure, trade count, date range, or cost basis in its prose — this record claims no source-reported performance (see Evidence).
- Full 37-line `//@version=3` block read in the page's source viewer (line-numbered viewer shows lines 1–37 with the `View in Pine Editor・37 lines` affordance). Verbatim source declaration, with the absences it discloses load-bearing for the derived status below: `strategy("Ehlers Cyber Cycle Strategy",overlay=false, default_qty_type = strategy.percent_of_equity, default_qty_value = 100.0, pyramiding = 1, commission_type = strategy.commission.percent, commission_value = 0.1)` — no `process_orders_on_close`, no `calc_on_every_tick`, no stop/limit/profit/loss argument. Source fills are therefore next-bar-open by Pine default evaluated once per completed bar; this record's same-bar-close execution is a separately identified researcher adaptation, never presented as source-native (see Execution assumptions).
- Pinned source inputs (all four, defaults frozen): `src = input(hl2, title = "Source")`, `alpha = input(.07, title = "Alpha")`, `lag = input(9, title = "Lag")`, `oppositeTrade = input(true)`. Retuning any of them, or flipping `oppositeTrade` off, would each be a different, unpinned rule.
- Text census over the pinned block: 1 `strategy("` declaration / 2 `strategy.entry` (`"Long"` with `strategy.long`, `"Short"` with `strategy.short`, no price/qty/when argument) / 1 `strategy.close` (the `strategy.close_all()` escape leg) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open` / 0 bare `close` (the rule reads `high`/`low` only via `hl2` and its lags — neither close, open, nor volume appears anywhere) / 1 `position_size` read (the counter-reset guard) / 1 `openprofit` read (the escape leg) / 1 `crossover(` + 1 `crossunder(` (both live, both gating orders) / 2 `plot(` + 1 `plot(0` + 1 `fill(` (render only — none gates any order).
- Licence and rights: the canonical page is an open-source publication by Tr0sT. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the script takes no symbol, timeframe, session, or venue input and reads only `high`/`low` via `hl2`; the author's demo chart shows BITMEX XBTUSD 1D, which is display context, never a rule); (2) same-bar-close fills (the source fills next-bar-open — no execution-timing argument ships anywhere, quoted verbatim in census); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 10th completed bar — see Required data); (4) house sizing/capital/costs replacing the `percent_of_equity 100.0` / `0.1%` commission declaration (see Execution assumptions). Market choice, fill timing, warmup length, and economics are therefore never presented as source-native. Cycle recursion, smoothing constants, signal-EMA construction, the inverted self-cross mapping under pinned `oppositeTrade=true`, order IDs, the `barsSinceEntry` counter, the 8-bar open-loss escape, `pyramiding = 1`, two-sided direction, and the no-stop/no-target posture are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive filename search for `cyber-cycle`, `yrCo4RtN`, `Tr0sT`, `oppositeTrade`, and `barsSinceEntry` returns zero strategy records using this source identity, author, switch, or counter — the sole `cyber`-mention pool-wide is a prose fence inside the bandpass-filter record naming this family as excluded, never this file. Content search for `signal, signal[1]`, `strategy.openprofit < 0`, and `Ehlers Cyber Cycle Strategy` returns zero records using this combo (the `openprofit` pool hits are census negations of the form `0 openprofit` — no pool record conditions any order on unrealized profit). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `bandpass-filter-reversed-cycle-sign-two-sided-btcusdt-1h-2026-10-11.md` trades the sign of an Ehlers cosine-derived first-order IIR bandpass resonator with pure reversal and no flat state (FMZ 439878); this record trades an inverted self-cross of an EMA-of-cycle signal line and rests flat after a performance-gated escape (TV yrCo4RtN) — different filter, different trigger, different exit, different source. `mama-fama-hilbert-state-flip-two-sided-btcusdt-30m-2026-10-12.md` trades Ehlers MAMA/FAMA Hilbert-transform state (different Ehlers construction, no signal self-cross, no loss escape). `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` warps normalized prices through the Fisher nonlinearity and signals on zero-sign (different transform, different event, no counter, no escape). Five-axis distinction: source identity differs (Tr0sT TV Sep-2018 `yrCo4RtN` Ehlers-book-Ch.4 lineage versus FMZ/ChaoZhang HPotter ports or other TV authors), signal construction differs (smoothed second-difference cycle recursion plus EMA signal line, nothing in the pool computes it), trigger differs (inverted self-cross `signal` vs `signal[1]` under pinned `oppositeTrade=true`), exit differs (the 8-bar open-loss `close_all` escape plus reversal is pool-unique), and position state differs (explicit flat-after-escape with a parked counter versus always-in-market latches).

## Economic mechanism

### Source-reported

Cycle-reversal trading against the lagged signal (page description plus code structure): the Cyber Cycle smooths price into a cyclic component, an EMA of that cycle (`signal`) generates the desired lag, and — per Ehlers' book construction — the trade is taken in the *opposite* direction of the naive cross (pinned `oppositeTrade=true`), because the lagged signal would otherwise fire exactly wrong into the next cyclic turn. The escape leg (`openprofit < 0` held more than 8 bars → flat) is the coded admission that the awaited cyclic reversal may never come when the market takes off in a trend.

### Research interpretation

Inverted cycle-state reversal with a performance-gated neutral state. Unlike always-in-market holders (Qstick, AC, bandpass records) that must be long or short after warmup, this system can rest flat — but only via the escape leg, never via signal disagreement: every signal cross fires an order, and flat exists solely as the post-escape residue until the next cross. Unlike level-cross systems (StochRSI, CCI, Fisher-zero records) that compare an oscillator against a fixed threshold, the trigger here compares the signal line against its own one-bar-ago value — a turning-point detector, not a level detector — and then deliberately inverts the naive side. The 8-bar loss escape converts unrealized pain into the sole risk control: there is no stop price, no target, no trailing, no time exit. Sparse flat stretches are the honestly priced cost (see Negative evidence).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy("Ehlers Cyber Cycle Strategy", overlay=false, ...)` with `pyramiding = 1` pinned (source-native: at most one entry per direction; same-direction refires while positioned are rejected no-ops; opposite-direction entry closes and reverses). `process_orders_on_close=true` is the predeclared researcher adaptation (no such argument ships in the source). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar — so the `openprofit` escape reads the completed-bar mark, never an intrabar tick).
- Smoothing (pinned): `smooth = (src + 2*src[1] + 2*src[2] + src[3]) / 6` with `src = hl2`.
- Cycle recursion (pinned, `alpha = 0.07`): `cycle = na` seeded; `if na(cycle[7]): cycle := (src - 2*src[1] + src[2]) / 4`, else `cycle := (1-.5*alpha)^2 * (smooth - 2*smooth[1] + smooth[2]) + 2*(1-alpha)*cycle[1] - (1-alpha)^2*cycle[2]`. Deterministically seeded from known bars only (see Required data).
- Signal line (pinned, `lag = 9`): `alpha2 = 1 / (lag + 1) = 0.1`; `signal = na` seeded; `signal := alpha2*cycle + (1-alpha2)*nz(signal[1])`.
- Counter (pinned): `barsSinceEntry = 0` seeded; `barsSinceEntry := nz(barsSinceEntry[1]) + 1` every bar; parked at `0` while flat (`if strategy.position_size == 0: barsSinceEntry := 0`); reset to `0` on every entry bar and every escape bar.
- Entry long (pinned, `oppositeTrade=true` branch): `crossunder(signal, signal[1])` → `strategy.entry("Long", strategy.long)` — the signal line turning down through its own prior value opens long (the deliberate inversion; with the switch off this same event would open short — disclosed-as-disabled path, never the admitted rule). Same-bar-close execution under the derived declaration.
- Entry short (pinned, `oppositeTrade=true` branch): `crossover(signal, signal[1])` → `strategy.entry("Short", strategy.short)` — mirror terms. The two cross predicates are mutually exclusive on every bar by definition, so at most one entry call fires per bar under any evaluation order — no same-bar long/short conflict exists to resolve.
- Escape flat (pinned): `if strategy.openprofit < 0 and barsSinceEntry > 8: strategy.close_all()` — a position held more than 8 bars and sitting at an unrealized loss at the completed-bar mark is closed in full at the adopted fill. `openprofit` is `na` while flat, which falsifies the comparison, so the leg cannot fire without a position. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: symmetric two-sided with an explicit post-escape flat state. A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `plot(0)`, the two signal plots, and `fill(...)` feed no order condition; order logic reads exactly the two entry conditions plus the escape condition.

## Required data

- Completed `1d` bars of BTCUSDT: `high` and `low` only (via `hl2` and its lags `src[1..3]`; the recursion reads `smooth[1..2]` and `cycle[1..2]`, all own-prior outputs). No `open`, no `close` series, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (researcher-declared; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: `smooth` needs `src[3]` (4th bar); the seed branch needs `src[2]` (3rd bar) and yields numbers from the 3rd bar on; `cycle[7]` is first non-`na` on the 9th completed bar, so the recursive branch — and the first fully-constructed combo state — starts on the 10th completed bar. `signal` seeds via `nz` and `crossover`/`crossunder` need two numeric signal prints (available from the 4th bar, but gated by the combo minimum above). Structural minimum is therefore the 10th completed `1d` bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared per the derived declaration; venue/symbol spelling is naming only, never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. The two entry legs are mutually exclusive every bar (see Signal), and the escape leg fires only when a position exists with `barsSinceEntry > 8`, so no ordering resolution is required.
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` candles (`high`/`low` plus same-bar `hl2`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. The escape comparison reads the completed-bar mark-to-market unrealized of the open position under house fills (`calc_on_every_tick` unset pins once-per-bar evaluation, so no intrabar `openprofit` path is ever modeled). That is the same single-frame completed-bar path as the admitted `1d` records; the cycle/signal recursion advances deterministically from known bars with `na`/`nz` seeds, so no hidden lookahead is ever modeled. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source's `percent_of_equity 100.0` / `0.1%` commission declaration is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. Historical funding is flagged per the house baseline: no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: `pyramiding = 1` is source-pinned — at most one unit per side under fixed order IDs `Long`/`Short`; repeat same-cross-direction entries while positioned are rejected no-ops, the opposite-cross entry reverses (closes the current side and opens the opposite in one transition), and the escape leg closes all via the coded flat leg. Re-entry is allowed immediately on the next qualifying cross after any flat (no cooldown specified — explicitly none, not invented). The counter parks at 0 while flat and can only exceed 8 while a position survives that long. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction (4-bar weighted smoothing, second-difference cycle recursion with the `cycle[7]` seed gate, EMA signal line with `alpha2 = 1/(lag+1)`, the `oppositeTrade` inversion switch defaulting true, the `barsSinceEntry` counter with flat-parking, the two inverted self-cross order legs with their order IDs, the 8-bar open-loss `close_all` escape, `pyramiding = 1`, and the Ehlers-book lineage note). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order` — the sole position-closing paths are the coded `close_all` escape leg and opposite-cross reversal. The absence is coded (the order block ends with the escape leg before the display calls), disclosed in Signal for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar by Pine definition (`crossover(a,b)` and `crossunder(a,b)` of the same pair cannot both be true), even though they sit in separate `if` statements — so no single bar can satisfy more than one order leg.
3. Escape-leg conditionality, admitted plainly: a position opened on a cross exits only on the opposite cross or on the 8-bar open-loss escape. A market that trends with the position never exits until a counter-cross prints — there is no target to bank a run, and a choppy signal whipsawing around its own prior value can compound consecutive reversal losses. This is the coded trade, disclosed, not a tunable parameter here.
4. Flat is escape-only: signal disagreement never produces flat (every cross fires); only the escape leg parks the system flat, and the very next cross re-enters. Long evaluation windows in smooth trends may contain few or zero escape events; this record treats that asymmetry as the strategy's honest shape, never as a reason to add a stop/target (which would be a different, unpinned rule).
5. Boundary ties hold their side: an exactly-equal signal print (`signal == signal[1]`) is neither a cross nor an under-cross, so no entry fires and the book carries the prior state; `openprofit` exactly zero falsifies `< 0`; `barsSinceEntry` exactly 8 falsifies `> 8` (escape needs 9+ held bars); a zero-range `hl2` window still evaluates arithmetically (no division anywhere in the order path); warmup bars are flat by record rule.
6. The smoothing weights (1/2/2/1 over 6), seed formula, recursion coefficients (`alpha = 0.07`), `lag = 9` (`alpha2 = 0.1`), `hl2` source, inverted mapping, fixed order IDs, counter semantics, `pyramiding = 1`, symmetric entries, the escape leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a constant, disabling `oppositeTrade`, gating entries on flat-only, adding a stop/target/cooldown, switching source series, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT `1d` market/frame choice, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; every signal, constant, threshold, comparison, transition, counter rule, flat leg, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open demo-chart source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: smoothing weights / seed formula / `alpha = 0.07` / `lag = 9` / `hl2` / inverted self-cross / `barsSinceEntry` counter / 8-bar open-loss escape / `pyramiding = 1` / symmetric entries / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Inversion relevance: replacing the inverted mapping with the naive mapping (`oppositeTrade=false`: long on `crossover`, short on `crossunder`) must not improve net expectancy; fail ⇒ the Ehlers inversion adds nothing over the naive cross.
- F2 — Escape relevance: removing the `close_all` escape leg (holding through open losses until the opposite cross) must not improve net expectancy; fail ⇒ the performance-gated flat state is dominated by simply staying positioned.
- F3 — Signal relevance: replacing the cycle-signal construction with the raw `smooth` series self-cross (same inverted mapping, same escape) must not improve net expectancy; fail ⇒ the Cyber Cycle recursion adds nothing over its own input.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (researcher-declared venue family). The `high`/`low`-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond completed `1d` bars, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market/frame: the source pins no symbol, venue, or timeframe (its demo chart shows BITMEX XBTUSD 1D — display context only); BTCUSDT `1d` is a researcher choice. Results on any other market or frame are a different, unpinned claim.
- Derived fill timing: the source fills next-bar-open evaluated once per completed bar; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Escape-mark semantics: the source's `strategy.openprofit` is read once per completed bar (source-default evaluation) and compared gross at the bar mark; this record evaluates it at the completed-bar close under house fills with house costs carried by the overlay. Any intrabar interpretation of the escape would be a different, unpinned rule — none is admitted here.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the opposite cross or the 8-bar open-loss escape, which arrives late by design (9+ held bars); signal self-cross whipsaw around flat stretches can compound consecutive reversal losses. This is the coded posture, disclosed as the record's principal risk.
- Source cost declaration replaced: the source declares `percent_of_equity 100.0` with `0.1%` commission; derived evaluation carries the full house cost load instead, and this record reports no net performance of any kind.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any `1d` evaluation window (structural minimum 10).
- Performance evidence is absent: neither the page prose nor the open-source block reports any number; nothing here is calibrated, fitted, or tuned to any window.
- Licence: the canonical page is an open-source Tr0sT publication of an Ehlers-book construction — downstream implementation must honor its House-Rules terms; this record copies no code block.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical TradingView strategy page (fetched 2026-10-15 in a real browser session; title/author/date/description/tags read; full 37-line `//@version=3` block read end to end in the page source viewer; no order logic invented): https://www.tradingview.com/script/yrCo4RtN-Ehlers-Cyber-Cycle-Strategy/
- Pine Script strategy semantics reference (evaluation defaults only — `process_orders_on_close`, `calc_on_every_tick`, `pyramiding`, `crossover`/`crossunder`, `nz`/`na` — never a source of strategy facts): https://www.tradingview.com/pine-script-docs/concepts/strategies/
