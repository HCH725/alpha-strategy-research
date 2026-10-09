---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Schaff Trend Cycle band-edge reversal two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-26
sources:
  - https://www.fmz.com/strategy/365905
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Schaff-Trend-Cycle.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Schaff Trend Cycle band-edge reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/365905 (`Schaff Trend Cycle`, author nickname `ChaoZhang`, `Created: 2022-05-26 17:20:52`). The canonical page itself was fetched over HTTP during this cycle: its body carries the strategy-argument table (MACD fast/slow 23/50, cycle 10, two %D lengths 3/3, source close, bands 75/25, highlight-breakouts true — identical to the mirror's table) and the page-embedded backtest header (`start: 2022-04-25 00:00:00`, `end: 2022-05-24 23:59:00`, `period: 45m`, `basePeriod: 5m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`); its executable block sits behind the site login wall, so no code was taken from the canonical page itself. The page ships no performance numbers of any kind (the only counters on the page are site `Copy: 7` / `Hits: 1495` tallies, named here as unusable water, never performance).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API), exact file path `Schaff-Trend-Cycle.md` (pure-ASCII filename, no encoding ambiguity). File 4180 bytes, blob SHA `32af71bfbf3b8b49c47312efbf6588b3101341b8`, SHA-256 `ce30797165b7b2b5bd8ae8c90d2b0b41c94cfe5139a685fc95d08793a4d3f957`. The mirror prints `> Detail` = https://www.fmz.com/strategy/365905 and `> Last Modified` = 2022-05-26 17:20:52 (adopted as `source_as_of`).
- Full Pine `//@version=4` block read in full (`study("Schaff Trend Cycle", shorttitle="STC")`, byline `Copyright (c) 2018-present, Alex Orekhov (everget)`, MIT licence note — no `strategy(` declaration, no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no `commission_*`, no `initial_capital`/`default_qty_*` lines). The two live order calls are FMZ-harness-style appends at the very end of the block (`if buySignal` / `strategy.entry("Enter Long", strategy.long)` / `else if sellSignal` / `strategy.entry("Enter Short", strategy.short)`). Source fills are therefore next-bar-open at language-default sizing under single evaluation per completed bar; this record's same-bar-close execution and house sizing are separately identified researcher adaptations, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `fastLength=23`, `slowLength=50`, `cycleLength=10`, `d1Length=3`, `d2Length=3`, `src=close`, `upper=75`, `lower=25`, `highlightBreakouts=true` (display-only). This record pins all effective defaults; retuning any of them, or switching `src` to high/low/open/hl2/hlc3/hlcc4/ohlc4, would be a different, unpinned rule.
- Text census over the pinned block: 2 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` reference. The only price series read anywhere in order-gating code is `close` (via the two EMAs); the single file-level text match for `high`/`low`/`open` outside code is the argument-table description string `Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4` plus the word `Highlight` — display/prose text, never a series read.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit lines and no risk prose on either the mirror or the canonical page. The reversal-only exit posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention — but unlike the merged TRIX record (whose Risk section states the missing stop-loss outright) there is no source sentence declaring the absence, which is fenced honestly in Limitations for the reviewer.
- Page/mirror performance language is absent entirely (no qualitative praise, no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the mirror block carries the everget MIT byline. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the script reads only `close` and is symbol-agnostic; the page header ran 45m/5m BTC_USDT Binance futures); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (required because `nz`-seeding makes the oscillator live from bar 1 — see Required data; structural minimum is 70 bars); (4) house sizing/capital replacing language-default sizing (see Execution assumptions). The single-entry-per-bar exclusivity is source-native (`if`/`else if`), not an adaptation. All four adaptations are predeclared here, confined to Provenance, Signal, Required data, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, thresholds, trigger semantics, pyramiding default, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree word-boundary searches for `schaff`, `stc`, `365905`, and `Schaff-Trend-Cycle` return zero strategy records using this source, author strategy, or mechanism — the sole `schaff`/`stc` hit anywhere is the word `schaff` inside the merged TRIX record's own dedup paragraph (a searched-but-absent term, never a mechanism). Same-author ChaoZhang records exist (Aroon FMZ 438795, TRIX FMZ 428683) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (ML/portfolio reconstruction batch — file list verified, no Schaff/STC record), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `stochastic-ott-dual-trend-btcusdt-1d` is a price-rank %K/%D stochastic plus OTT trailing system, `fisher-zero-cross-reversal-btcusdt-1d` is a normalized nonlinear-transform zero-cross system, `vidya-cmo-adaptive-slope-trend-btcusdt-1h` is an adaptive-average slope system. Five-axis distinction: mechanism differs (MACD-of-double-stochastic Schaff cycle oscillator with asymmetric band-edge contrarian entries, two-sided with reversal), signal construction differs (no pool record evaluates `ema(nz(fixnan(stoch(ema(ema(nz(fixnan(stoch(ema(close,23)-ema(close,50),10)),3),10)),3))),clamped 0-100` against the 25/75 band edges), exits differ (opposite band-edge reversal only, no trailing/band-cross/tick exits), source identity differs (FMZ 365905 May-2022 versus other FMZ IDs or TV authors), and direction handling differs (asymmetric two-sided: longs on lower-band bounce, shorts on upper-band rejection — versus symmetric or long-only records).

## Economic mechanism

### Source-reported

None beyond the construction itself: the mirror and canonical page ship no mechanism prose (no cycle-theory paragraph, no regime claim). The coded economics are readable directly — the Schaff Trend Cycle compresses MACD momentum through two stochastic normalizations so the oscillator snaps between 0 and 100 faster than MACD alone; crossing up through the 25 lower band prices an oversold bounce (long), crossing down through the 75 upper band prices an overbought rejection (short). Each side is held until the opposite band-edge signal reverses it. No stop, no target, no trailing order ships anywhere.

### Research interpretation

Two-sided snap-back harvesting on a bounded cycle oscillator. Unlike stochastic records that trade %K/%D crosses mid-range, both entries here are band-edge events: the long needs the oscillator to have visited oversold (at/below 25) and turned up; the short needs a visit to overbought (at/above 75) and a turn down. The double-stochastic construction makes the oscillator spend most of its time pinned near the rails, so signals are rarer and more selective than a raw MACD cross — at the cost that a position opened on one rail's bounce exits only on the opposite rail's rejection, which may never arrive (see Limitations). The exit is deliberately absent by code: adverse excursion has no guardrail except the reversal leg, so this record must be read as a pure reversal system, never as a risk-managed one.

## Signal

Exact rule as pinned (defaults quoted — effective inputs unmodified, `highlightBreakouts` display-only):

- Declaration (derived): `study("Schaff Trend Cycle", shorttitle="STC")` with `process_orders_on_close=true` adopted for the derived record (the source declaration carries no such argument) and house sizing replacing language-default sizing (see Execution assumptions). `pyramiding` is unset (v4 language default 0: no additional same-direction entry while positioned, opposite-direction entry reverses — load-bearing here, pinned explicitly). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar).
- Oscillator (pinned): `macd = ema(close,23) - ema(close,50)`; `k = nz(fixnan(stoch(macd,macd,macd,10)))`; `d = ema(k,3)`; `kd = nz(fixnan(stoch(d,d,d,10)))`; `stc = ema(kd,3)`; `stc := max(min(stc,100),0)`. Both `stoch` calls normalize a series against itself over 10 bars (pure cycle position, 0-100); `fixnan` carries the last non-`na` value forward and `nz` seeds leading `na` as 0, so the oscillator is defined (seeded) from the first bar — never `na`-gated, which is why the adopted warmup is a record rule rather than language semantics.
- Entry long: `buySignal = crossover(stc,lower)` i.e. `stc[1] <= 25 and stc > 25` → `strategy.entry("Enter Long", strategy.long)` — lower-band bounce, evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Entry short: `sellSignal = crossunder(stc,upper)` i.e. `stc[1] >= 75 and stc < 75` → `strategy.entry("Enter Short", strategy.short)` — upper-band rejection, mirror terms. The `if`/`else if` chain makes the two legs mutually exclusive on every bar by construction (both conditions additionally require contradictory `stc[1]` levels, so no single bar can satisfy both even outside the chain).
- Exits: none coded. The sole exit path is opposite-entry reversal under pinned pyramiding 0 (a short signal while long reverses to short and vice versa); same-side repeat triggers while positioned are rejected no-ops. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: asymmetric two-sided by pinned thresholds (longs key off 25, shorts off 75); flat is entered only transiently via reversal (no standalone flat signal). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Display isolation: `stcColor*`/`plot`/`fill`/`hline(50)`/`plotshape`/`alertcondition`/`highlightBreakouts` feed no order condition; the six `upperCrossover`/`upperCrossunder`/`lowerCrossover`/`lowerCrossunder` band-cross variables beyond the two order signals drive alerts/plots only. Order logic reads exactly `buySignal`/`sellSignal`.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (via EMA23/EMA50). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: EMA50 needs 50 bars for a full slow window; the first `stoch` needs 10 MACD values and the second `stoch` needs 10 `d` values, so all rolling windows are full from the 70th completed `1d` bar (EMA seeds decay beyond that). Structural minimum is therefore the 70th completed bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — the language would trade seeded early signals because `nz`/`fixnan` never emit `na`). No repainting, no negative shift, no future reference, no full-sample normalization; `calc_on_every_tick=false` gives exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads `close` only and is symbol-agnostic; venue transfer from the page header's 45m/5m BTC_USDT Binance-futures backtest is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (a `study` block has no execution argument at all — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity; the source-native `if`/`else if` chain already guarantees at most one entry call per bar.
- Sizing/capital: language-default sizing (the appended harness lines carry no `qty`) is replaced here by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v4 default 0: no same-direction add while positioned; opposite-direction entry reverses). The default is load-bearing and therefore pinned explicitly: repeat trigger bars during an open same-side position are rejected no-ops, and re-entry is allowed immediately on the next qualifying opposite signal after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full double-stochastic STC construction (lengths 23/50/10/3/3, bands 75/25, close source), the two band-edge order signals, the appended long/short entry pair, and the page-embedded 45m/5m backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.close`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the opposite-entry reversal is the sole exit path by construction. The absence is coded (the block simply ends after the two entries), though no source sentence declares it — fenced in Limitations for the reviewer rather than upgraded into a source claim.
2. Entry legs are mutually exclusive on every bar twice over: the `if`/`else if` chain admits at most one call, and the conditions themselves contradict (`stc[1] <= 25` versus `stc[1] >= 75` with pinned 25/75) — no same-bar long/short conflict exists to resolve under any evaluation order.
3. Exit-leg conditionality, admitted plainly: a long opened on a lower-band bounce exits only on a later `crossunder(stc,75)`, which requires the oscillator to first travel above 75. Sideways decay (oscillator sagging back into mid-range without reaching the opposite rail) strands the position until the next opposite signal — there is no time-stop to cut it. This is the coded trade, disclosed, not a tunable parameter here.
4. Boundary ties and flat ranges fire nothing: `crossover`/`crossunder` are strict edge triggers; equality holds no signal; an STC pinned exactly flat fires neither entry; warmup bars are flat by record rule.
5. Flat-state determinism: with no open position both entry legs are live candidates each bar (edge-triggered, so resting flat between signals is the norm); same-side repeat triggers while positioned are rejected under pinned pyramiding 0; opposite-side triggers reverse.
6. The lengths (23/50/10/3/3), the bands (75/25), the close source, the double-`stoch`-of-self construction, the `nz`/`fixnan` seeding, the 0-100 clamp, the asymmetric band-edge entries, the two-sided reversal posture, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, symmetrizing the bands, adding a stop/target/cooldown/midline exit, switching `src`, or disabling a side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; every signal, threshold, default, transition, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open 45m/5m source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA23/EMA50 MACD / double-10-bar self-stochastic / 3/3 %D smoothings / 75/25 band edges / asymmetric bounce-vs-rejection entries / reversal-only exits / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Oscillator relevance: replacing the double-stochastic STC with raw MACD(23,50) cross signals must not improve net expectancy; fail ⇒ the Schaff normalization adds nothing over a plain MACD system.
- F2 — Band-edge relevance: replacing the 25-bounce/75-rejection entries with any-STC-turn entries (direction change without band contact) must not improve net expectancy; fail ⇒ the band edges add nothing over trading every oscillator turn.
- F3 — Reversal-exit relevance: adding a time-stop (flat after N bars without an opposite signal) must not improve net expectancy; fail ⇒ the pure-reversal holding rule is dominated by simply cutting stranded positions.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The close-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open`/`high`/`low` are never referenced), so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on a 45m-decision/5m-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings, frames, and bases differ by construction — the adaptations are disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the opposite rail's rejection signal, which may never arrive; a rail-to-rail round trip that never completes leaves the position open indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Undeclared absence: unlike merged predecessors whose pages state the missing stop-loss outright, this source is silent about risk — the no-stop reading rests on the code (the block ends after the entries) rather than on any source sentence. The reviewer should weigh this silence as documented here.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any 1d evaluation window (structural minimum 70).
- Performance evidence is absent: neither the mirror nor the canonical page reports any number (its praise, such as it is, is a bare backtest-image link with no readable metric); nothing here is calibrated, fitted, or tuned to any backtest.
- Seeded early bars: before the warmup completes, `nz`/`fixnan` seeding fabricates oscillator values (leading zeros) that could print band-edge-looking turns; the record-rule pre-warmup flat exists precisely to fence this off — any evaluation that counts pre-warmup bars is not this record.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical FMZ strategy page (fetched 2026-10-09; argument table and backtest header read; executable block behind login, no code taken): https://www.fmz.com/strategy/365905
- Immutable mirror file actually executed against (full Pine v4 block read end to end; 4180 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Schaff-Trend-Cycle.md
