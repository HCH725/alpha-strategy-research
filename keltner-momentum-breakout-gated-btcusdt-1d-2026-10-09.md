---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Keltner-channel momentum-gated breakout two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-02-10
sources:
  - https://fmz.com/strategy/481364
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Keltner-channel momentum-gated breakout two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ canonical strategy page plus its full embedded Pine block, fetched 2026-10-09):

- Canonical page: https://fmz.com/strategy/481364 (`Momentum-Driven Keltner Channel Breakout Trading Strategy`, FMZ `Common strategy`, author nickname `ChaoZhang`, page `Created: 2025-02-10 15:03:16`, adopted as `source_as_of`; page tags `ATR, EMA, MOM, KC`). The same author publishes other FMZ strategies, but no pool record or open PR shares this canonical URL or its Keltner-plus-momentum mechanism (see dedup below).
- Page-embedded backtest header (verbatim substance): `period: 15m`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, window `2025-02-02 00:00:00` to `2025-02-09 00:00:00`. The window is cited as provenance only: the page ships no returns, win rate, profit factor, trade count, or cost basis anywhere — this record claims no source-reported performance (see Evidence).
- Full Pine `//@version=5` block read from the page-embedded source (decoded artifact sha256 `3c7f213fabfd928522757de7cee6afb1fcff99f6064323dd0db2c4a05c66ce7d`, 56 lines including the backtest header). Verbatim source declaration (note the absences it discloses, load-bearing for the derived status below): `strategy("Keltner Channels + Momentum Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=200)` — no `process_orders_on_close`, no `calc_on_every_tick`, no `pyramiding`, no `commission_*`, no `initial_capital` lines. Source fills are therefore next-bar-open by Pine default at 200%-of-equity sizing; this record's same-bar-close execution and house sizing are separately identified researcher adaptations, never presented as source-native (see Execution assumptions).
- Pinned source inputs: `lengthKC = input.int(20)`, `mult = input.float(1.5)`, `src = input(close)`, `lengthMomentum = input.int(14)`. This record pins all four defaults; retuning any of them would be a different, unpinned rule.
- Text census over the pinned block: 2 `strategy.entry` / 2 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `volume` / 0 `open`. Live order calls are exactly four (`strategy.entry("Long", strategy.long)`, `strategy.entry("Short", strategy.short)`, `strategy.close("Long")`, `strategy.close("Short")`); display calls (`plot` x4, `hline` x1) touch no order condition.
- Prose-vs-code sizing fact, admitted honestly: the executable sizing is `percent_of_equity` 200 (2x notional, compounding by code), while the page prose discusses only qualitative risk guidance ("reasonable risk control", "dynamic position size") with no coded stop, target, or trailing leg. This record replaces the 200% sizing with the explicit house overlay (see Execution assumptions), never presenting prose guidance as a coded rule.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) research market/timeframe BTCUSDT `1d` (the script reads only `high`/`low`/`close` and is symbol-agnostic; the page header ran 15m BTC_USDT Binance futures); (2) same-bar-close fills via `process_orders_on_close=true` (the source fills next-bar-open); (3) an explicit atomic-bar evaluation order — exits before entries, entries reverse opposite positions — which reproduces the source's net position transitions exactly in every reachable state (proven in Negative evidence), specified here because the source leaves intrabar order interaction to broker-emulator ordering. All three adaptations are predeclared here, confined to Provenance, Signal, Execution assumptions, and Limitations, with every original claim kept separate above. Indicator formulas, lookbacks, multiplier, momentum definition, cross semantics, pyramiding default, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree searches for `481364`, `ta.mom(close, 14)`, `upperKC`, `lowerKC`, `emaKC`, and word-boundary `keltner` return zero strategy records using this source, author strategy, or mechanism — the only `keltner` hits are passing dedup-prose mentions inside the Donchian record (a highest-high/lowest-low channel, different construction), and the only `ta.mom` hits are `ta.mom(close, 25)` Chikou-displacement legs inside Ichimoku-family conjunctions (different length, different role, never paired with any channel breakout). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (17-family reconstruction batch, unmerged), and #63 (SuperTrend ATR-flip trend long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` breaks raw highest-high/lowest-low price extremes with no volatility normalization and no momentum gate; `sideways-dmi-bollinger-breakout-long` (where pooled) is a standard-deviation band system, not an EMA-plus-ATR envelope; the three Ichimoku records embed momentum only as a 25-bar displacement leg inside 4–6-leg conjunctions with cloud/DMI/RSI, never as a sign gate on a channel breakout. Five-axis distinction: mechanism differs (ATR-normalized EMA-envelope breakout AND-gated with a 14-bar momentum-sign filter, two-sided with reversal, versus raw-extreme breaks, stddev bands, or cloud conjunctions), signal construction differs (no pool record evaluates `ta.ema(close,20) ± 1.5*ta.atr(20)` with `ta.crossover`/`ta.crossunder` events AND `ta.mom(close,14)` sign), exits differ (mid-EMA recross OR momentum-sign-flip dual close versus opposite-band, time, or trailing exits), source identity differs (FMZ 481364 ChaoZhang Feb-2025 versus TV authors or other FMZ IDs), and direction handling differs (symmetric two-sided with reversal versus long-only, short-only, or flat-alternative systems).

## Economic mechanism

### Source-reported

Volatility-normalized breakout with momentum confirmation: a close crossing outside the ATR-scaled EMA envelope marks an expansion strong enough to clear 1.5 average true ranges of noise, and the momentum-sign gate (`ta.mom(close,14)`, i.e. `close[t] - close[t-14]`) requires the 14-bar rate of change to agree with the breakout direction before any entry. The position is held until price recrosses the envelope midline or momentum flips sign — the midline recross is the entire stop logic (the author calls the midline the stop reference) and the momentum flip is the entire trend-exhaustion exit. The author ships no fixed stop, no target, no trailing order: exits are signal-only by construction. Risk guidance is prose-only ("set maximum position limits", "dynamic parameter adjustment") and specifies no executable rule.

### Research interpretation

Two-sided expansion harvesting. Unlike Donchian records, the breakout level breathes with volatility (ATR scaling), so identical price moves trigger entries in calm regimes and are ignored as noise in wild ones; unlike RSI-gated records, the confirmation is an unsmoothed rate-of-change sign rather than a bounded oscillator level, so the gate adds no smoothing lag beyond the 14-bar differencing window. The exit pair (midline recross OR momentum flip, per side) bounds adverse excursion without any price-level stop: a failed breakout that falls back through the midline, or whose 14-bar momentum turns against the position, is closed on the next eligible bar. No leverage, sizing, or cost edge is embedded in the signal; the 200%-equity sizing line is replaced by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy("Keltner Channels + Momentum Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=200, process_orders_on_close=true)` — the first lines are the source verbatim except `process_orders_on_close=true`, which is the predeclared researcher adaptation (source declaration carries no such argument), and except sizing, which the house overlay replaces (see Execution assumptions). `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned, opposite-direction entry reverses — load-bearing here, pinned explicitly, see Execution assumptions). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar) and `calc_on_order_fills` is unset (default false).
- Envelope (lengths pinned): `emaKC = ta.ema(src, lengthKC)` with `src = close`, `lengthKC = 20`; `atrKC = ta.atr(lengthKC)` (v5 RMA-smoothed true range over the same 20 bars); `upperKC = emaKC + mult * atrKC`, `lowerKC = emaKC - mult * atrKC` with `mult = 1.5`. When `atrKC` is zero (twenty identical ranges) the bands collapse onto the midline; cross events remain strict and entries remain mutually exclusive (see Negative evidence).
- Momentum gate (pinned): `momentum = ta.mom(close, lengthMomentum)` with `lengthMomentum = 14`, i.e. `close[t] - close[t-14]`. Strict sign only: `> 0` long-side, `< 0` short-side; exact zero on either side fires nothing and holds.
- Entry long: `longCondition = ta.crossover(close, upperKC) and momentum > 0` — strict cross semantics (`close[1] <= upperKC[1]` and `close > upperKC`) AND strict positive 14-bar momentum. Live via `if (longCondition)` → `strategy.entry("Long", strategy.long)`, evaluated on the completed-bar close with same-bar-close execution under the derived declaration.
- Entry short: `shortCondition = ta.crossunder(close, lowerKC) and momentum < 0` — strict mirror. Live via `if (shortCondition)` → `strategy.entry("Short", strategy.short)`.
- Exit long: `exitLong = ta.crossunder(close, emaKC) or momentum < 0`. Live via `if (exitLong)` → `strategy.close("Long")` on the same completed-bar close.
- Exit short: `exitShort = ta.crossover(close, emaKC) or momentum > 0`. Live via `if (exitShort)` → `strategy.close("Short")`.
- Direction: symmetric two-sided by pinned code path; flat is entered only via the exit legs (no standalone flat signal). A short-side instrument is required for the short legs; on a spot-only venue they are inexpressible and the record would not be the same rule (see Crypto portability).
- Evaluation order (predeclared specification, net-transition-identical to the source — proof in Negative evidence): on each completed bar, evaluate both exit legs first, then both entry legs; an entry against an open opposite position reverses it (Pine pyramiding-0 parity). Same-side entry/exit pairs can never co-fire (proven), so the order specification only resolves cross-side co-firing, where it reproduces the source net exactly.
- Display isolation: `plot`/`hline` calls render the three bands, the midline, and momentum only — no display call feeds any order condition.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low` (true-range path inside `ta.atr`), `close` (EMA source, cross comparisons, momentum differencing). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1d` is adopted as the research frame because it is a campaign timeframe — never presented as anything beyond that (see Limitations).
- Warmup: the EMA-20/ATR-20 pair is only full from the 20th completed `1d` bar, momentum needs `close[t-14]` (15 bars), and each cross event reads one prior bar, so the first signal-eligible bar is the 21st completed `1d` bar. Pre-warmup bars are flat by language semantics (`na` conditions never open or close anything). No repainting, no negative shift, no future reference, no full-sample normalization; `calc_on_every_tick=false` gives exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (the rule reads OHLCV only; venue transfer from the page's 15m Binance-futures header is never presented as source-native semantics).
- Order timing (predeclared derivation): `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (declaration carries no such argument — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. 0 `strategy.exit` calls, hence no stop/limit order and no same-bar TP/SL ordering ambiguity anywhere in the rule; the only ordering specification is the predeclared exits-before-entries atomic evaluation, proven net-identical to the source (see Negative evidence).
- Sizing/capital: the source declaration codes `percent_of_equity` 200 (2x notional compounding), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned; opposite-direction entry reverses). The default is load-bearing and therefore pinned explicitly: repeat entry-condition bars during an open same-side position are rejected no-ops, and re-entry is allowed immediately on the next qualifying cross after any exit (no cooldown specified — explicitly none, not invented). `strategy.close("Long")`/`strategy.close("Short")` with no matching open position are deterministic no-ops. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships the Keltner construction (EMA-20 midline, ±1.5x ATR bands), the 14-period momentum definition, the two AND-gated breakout entry rules, the midline-recross/momentum-flip exit pair, the 15m BTC_USDT Binance-futures backtest header with its 2025-02-02–09 window, and prose risk guidance. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`profit=`/`loss=` — the midline-recross/momentum-flip close pair is the sole exit path by construction, and the prose promises no stop or target.
2. Entries are mutually exclusive on every bar: `longCondition` needs `close > upperKC` while `shortCondition` needs `close < lowerKC` with `upperKC >= lowerKC` always (strict `>` unless ATR is exactly zero, in which case both need `close` strictly above and strictly below the same midline value — impossible). No single close satisfies both, so no same-bar long/short entry conflict exists to resolve.
3. Same-side entry/exit pairs can never co-fire: a long entry requires `momentum > 0` while `exitLong` requires `momentum < 0` or a midline crossunder (impossible on a bar that crossed above the upper band, since `upperKC > emaKC` whenever ATR > 0, and impossible under ATR = 0 as shown above); the short mirror holds. The evaluation-order specification therefore only ever resolves cross-side co-firing.
4. Cross-side co-firing reproduces the source net exactly: a long entry always co-fires `exitShort` (via `momentum > 0`), and vice versa. Under source next-open semantics the entry reverses an open short (or opens from flat) while the same-bar opposite close is a no-op without that position — net long either way; under this record's exits-first atomic order the opposite close lands first (flattening a held short, no-op when flat) and the entry then opens long — net long either way. All four flat/long/short × long-entry/short-entry reachable combinations were walked with identical nets; the order specification invents no transition.
5. Boundary ties, zero momentum, and flat ranges fire nothing: strict `ta.crossover`/`ta.crossunder` (equality on either compared bar is not a cross); `momentum == 0` satisfies neither side's entry nor exit leg (hold); a zero 20-bar ATR collapses the bands but preserves strictness and mutual exclusion per (2); `na` warmup bars open and close nothing.
6. Flat-state determinism: both `strategy.close` legs with no matching open position are no-ops; same-side repeat entries while positioned are rejected under pinned pyramiding 0; opposite-side entries reverse; the seed bars satisfy no order condition by themselves (each cross needs a settled prior bar, momentum needs `close[t-14]`).
7. The lengths, multiplier, source series, momentum definition, two-sided direction, reversal semantics, and no-stop/no-target/no-cooldown posture are pinned, not removed: retuning 20/1.5/14, dropping the momentum gate, adding a stop/target/cooldown/session filter, or disabling a side would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` research frame, same-bar-close fills, the exits-first atomic evaluation order, and house sizing — all predeclared above; every signal, threshold, default, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open 15m source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: KC(20, 1.5x ATR on close) / `ta.mom(close,14)` sign gate / strict cross entries / midline-or-flip exits / two-sided with reversal / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Gate relevance: dropping the momentum-sign conjunct (pure Keltner-band-cross entries and midline exits) must not improve net expectancy; fail ⇒ the 14-bar momentum filter adds nothing over a plain envelope breakout.
- F2 — Envelope relevance: replacing the ATR-scaled envelope with a fixed-multiple-of-price band around the same EMA-20 (same cross/flip event structure) must not reproduce-or-beat net expectancy; fail ⇒ the record is a volatility-label variant of a plain MA-band breakout.
- F3 — Exit relevance: holding each entry for a fixed research-defined bar count instead of the midline-recross/momentum-flip pair must not improve net expectancy; fail ⇒ the dual close adds nothing over time exits.

## Crypto portability

Pinned to BTCUSDT under the house overlay. The OHLCV-only logic ports across perpetual venues without structural change; the short legs require a shortable instrument, so a spot-only deployment cannot express this rule (disabling the short side would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no session, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (`open` is never referenced), so session-gap behavior is simply absent rather than approximated. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing and frame: the source fills next-bar-open on 15m bars; this record executes same-bar-close on `1d` bars. Backtest economics of the two timings and frames differ by construction — the adaptations are disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop: adverse excursion after entry has no guardrail beyond the midline recross or the momentum flip; a vertical-against move exits only when the envelope midline is reclaimed or the 14-bar momentum turns, which can be far.
- Whipsaw in compression: when ATR compresses, the bands tighten and boundary crosses print frequently; the momentum gate filters some but not all of these — the source provides no further filter and this record invents none.
- Warmup cost: the EMA/ATR pair needs 20 completed bars plus one prior bar for the cross, so the system is blind for the first 20 bars of any 1d evaluation window.
- Performance evidence is absent: the canonical page reports no numbers at all (its 7-day 15m header is a run window, not a result); nothing here is calibrated, fitted, or tuned to any backtest.
- Seven-day source window: the page's own header covers a single 7-day 15m span; this record adopts none of its economics and pins a different research frame — any resemblance of future results to that span would be coincidence, not validation.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical strategy page (fetched 2026-10-09): https://fmz.com/strategy/481364
- Pine v5 strategy semantics (declaration defaults, order calls, close-evaluated execution): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine strategy concepts: https://www.tradingview.com/pine-script-docs/concepts/strategies/
