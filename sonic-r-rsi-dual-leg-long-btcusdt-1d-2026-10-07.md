---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Sonic R EMA-channel plus RSI dip-recovery dual-leg long system on BTCUSDT 1d bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-23
sources:
  - https://www.fmz.com/strategy/433019
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ page title/author read `Dual-EMA-and-RSI-Combination-Strategy` by `ChaoZhang`, but the pinned executable Pine block is titled `Sonic R & RSI only BTCUSD D1 strategy` with Vietnamese comments crediting `t.me/beincypto_vn` — a repost/attribution mismatch. The executable block governs; both attributions are recorded here as printed."
  - "The page prose describes a fast-EMA34 / slow-longer-EMA cross system (`stand on fast EMA = buy, stand on slow EMA = sell`) plus generic `RSI high = sell`, but the pinned code contains no second EMA length, no crossover call of any kind (0 occurrences of crossover/crossunder/ta.cross), and the RSI leg is a dip-recovery ENTRY (3-bar lowest under 29 with RSI turning up through 30), not a high-RSI sell except for the separate per-leg exit. The prose is generic boilerplate and is recorded as contradicted; the code governs."
  - "Pine inline comments and the mirror description say `please use coinbase exchange time frame D1` on `BTCUSD`, but the FMZ backtest header pins `Futures_Binance` / `BTC_USDT` / `period: 1d` (2022-11-22 to 2023-11-22). Decision timeframe 1d is undisputed on both sides; the research market is pinned to BTCUSDT 1d perpetual to match the executable header exactly, and the Coinbase-spot mention is recorded as contradicted prose, never as semantics."
  - "The FMZ header pairs `period: 1d` with `basePeriod: 1h`. The 1h granularity is FMZ execution resolution, not signal logic: every rule reads completed daily-bar values under `process_orders_on_close=true` with no intrabar, MTF, or clock call. The record pins the 1d decision timeframe; no 1h signal is inferred."
---

# Sonic R EMA-channel plus RSI dip-recovery dual-leg long system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ public strategy page artifact, via the pinned local mirror of that page):

- FMZ strategy page: https://www.fmz.com/strategy/433019 (page title `Dual-EMA-and-RSI-Combination-Strategy`, author `ChaoZhang`, last modified `2023-11-23 16:37:38`).
- Executable artifact inside the page: a `//@version=5` Pine block titled `Sonic R & RSI only BTCUSD D1 strategy` with one live `strategy()` declaration, two `ta.ema` channel assignments, one `ta.rsi` assignment, four boolean condition assignments, two `strategy.entry` long legs (`buyEMA`, `buyRSI`), two per-leg `strategy.close` exits, and display-only `plot`/`fill` calls.
- FMZ backtest header printed verbatim in the artifact: `start: 2022-11-22 00:00:00`, `end: 2023-11-22 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. This header is the source's own executable scope (not a signal rule) and corroborates the pinned `1d` decision timeframe and the `BTCUSDT` research market; downstream must declare its own evaluation window rather than silently re-tuning it.
- Mirror bytes pinned 2026-10-07: file 8796 bytes, SHA-256 `5b09ef5342c190593f058d125a21a3729e87a4648f6436781c74499a0dc5aa97`. The mirror is the FMZ page scrape (`fmz-strat` corpus); no second immutable host (GitHub blob) exists for this strategy, so provenance is the FMZ stable URL plus these bytes — traceable and public, but without commit-SHA immutability, which is stated rather than hidden.

Pre-write dedup (2026-10-07): word-boundary search of the working tree for `sonic`, `433019`, `buyEMA`, and `buyRSI` returned 0 matches in any strategy record; `gh pr list --state open` shows only #36 (`reconstruction/legacy-family-quantaalpha`, a non-Scout QuantaAlpha family record — different source, different mechanism); the closed research PRs (#6 WaveTrend, #10 golden/dead cross, #17 MACD histogram, #20 Ichimoku-RSI, plus merged #5 Gann, #7 P-Signal, #9 VIDYA, #12 Bookstaber, #21 Kaufman pivot, #22 EHMA, #23 DMI, #25 Ichimoku-ADX, #28 DRM, #29 Monday-drift, #31 Donchian, #32 Flying-Dragon, #34 EMA-cross, #35 Stochastic-OTT, #37 IBS) contain no Sonic R channel, no EMA-of-high/low breakout-persistence leg, and no RSI dip-recovery long leg. Five-axis distinction: mechanism differs (daily close holding outside a 34-EMA high/low channel with two-bar persistence, plus an independent RSI-washout-recovery trigger — versus ATR breakouts, Hull bands, DMI crosses, erf dead-bands, Donchian channels, calendar holds, oscillator trails, or single-bar IBS fades), signal construction differs (`ta.ema(high,34)` / `ta.ema(low,34)` channel pair with `close[2]` confirmation plus fixed `ta.rsi(close,14)` with 3-bar-lowest / 5-bar-highest windows — no other record combines an EMA price channel with an RSI dip trigger), horizon is `1d` on BTC (no other record runs a dual-leg two-ID long-only book), source identity differs (FMZ 433019 versus all prior FMZ IDs, TV scripts and Forven pines), and direction handling is long-only across two independent entry IDs with per-leg closes versus two-sided or single-leg records.

## Economic mechanism

### Source-reported

- Premise, as printed: the 34-EMA of bar highs and the 34-EMA of bar lows form a trend cloud (the "Sonic R" dragon wave); a daily close printed above the upper edge means trend continuation, a close below the lower edge means the long leg is over. The RSI-14 leg buys washouts: RSI washing under 29 and turning back up through 30 marks seller exhaustion worth fading into a long.
- Persistence filter, as printed in code comments: each EMA leg requires not only the current close beyond the channel edge but also `close[2]` beyond the same edge — the breakout must survive two bars, filtering one-bar spikes.
- Risk stance, as printed: the page prose admits EMA/RSI false signals in violent markets and recommends (but does not code) stop-loss and position control — the coded edge is purely the two signal legs, with no risk-managed structure in the executable block.

### Research interpretation

- Falsifiable mechanism hypothesis: on daily crypto bars, a close that holds outside a slow EMA price channel for two consecutive prints marks an accepted trend extension (not a wick), so riding it captures the drift leg; the RSI washout-recovery trigger independently harvests sharp shakeouts inside or against that trend. The two legs are uncorrelated by construction (trend-persistence versus mean-reversion trigger) and each carries its own exit, so the book is a two-sleeve long-only system, not one blended signal. Either sleeve firing alone is independently falsifiable (F1 splits legs).
- The `close[2]` persistence leg matters: without it the channel leg would buy every one-bar channel touch including stop-run wicks; with it the rule selects only extensions the market confirms two bars later. Both parts of the conjunction are independently falsifiable.

## Signal

Exact executable semantics, read from the pinned block (nothing inferred, nothing added):

- Indicator variants: `ema34high = ta.ema(high, 34)`, `ema34low = ta.ema(low, 34)` (Sonic R channel pair, source prices `high`/`low`, classic EMA smoothing, fixed lookback 34); `rsi = ta.rsi(close, 14)` (Wilder RSI on `close`, fixed lookback 14); `ta.lowest(rsi, 3)` and `ta.highest(rsi, 5)` (fixed windows 3 and 5). No Heikin-Ashi, no volume, no external feed, zero `request.*`/`security(`/timeframe calls.
- Entry leg 1 (trend persistence): `dkienmua1 = close > ema34high and close[2] > ema34high` → `if dkienmua1` then `strategy.entry('buyEMA', strategy.long)`. Plain `>` comparisons — no `crossover`/`crossunder`/`ta.cross` anywhere (0 occurrences), so the #6 tie-semantics precedent does not apply; a close exactly equal to the channel edge is deterministically NOT an entry.
- Exit leg 1: `dkienban1 = close < ema34low and close[2] < ema34low` → `if dkienban1` then `strategy.close('buyEMA', comment='CloseEMA')`. Per-ID close: it flattens only the `buyEMA` sleeve, never `buyRSI`. No opposite-signal exit exists for this leg (the exit is channel-breakdown, not the negation of the entry).
- Entry leg 2 (RSI dip-recovery): `dkienmua2 = ta.lowest(rsi, 3) < 29 and rsi > rsi[3] and rsi > 30` → `if dkienmua2` then `strategy.entry('buyRSI', strategy.long)`. All three conjuncts are strict inequalities on current-or-past values; deterministic.
- Exit leg 2: `dkienban2 = ta.highest(rsi, 5) > 70 and rsi < 70` → `if dkienban2` then `strategy.close('buyRSI', comment='CloseRSI')`. Per-ID close: it flattens only the `buyRSI` sleeve. A bar that satisfies both legs' entries opens both sleeves (see Execution assumptions); a bar can likewise close one sleeve while the other stays open — each transition is documented as independent.
- Direction: long-only, explicitly. The only order-creating calls are the two `strategy.long` entries; zero short orders, zero direction/mode input. Short is disabled by construction (DMI-record pattern: one-sided at pinned code with no direction input).
- Risk semantics: no stop loss, no take profit, no trailing stop, no time exit — 0 `strategy.exit`, 0 `strategy.stop`, 0 `strategy.order`, 0 `limit`/`stop`/`profit`/`loss` order arguments. Recorded as explicitly absent per the source's own risk admission, never as silent defaults.
- Warmup: EMA-34 seeding dominates — deepest causal refs are `close[2]` / `rsi[3]` plus the 34-bar EMA seed and the 14-bar RSI seed; deterministic warmup is 36 bars (F2 forces the replay to demonstrate hold-on-na over the seed window rather than raising or inventing a fill). `max_bars_back=500` is code-declared history buffer, recorded as declared, never as signal.
- Display-only: two `plot` calls and one `fill` (channel cloud) plus `overlay=true`, `shorttitle`, and Vietnamese comments carry zero event effect.

## Required data

- 1d bars of one pair: `open/high/low/close` (signal reads `close`, `high`, `low`, `close[2]`, and RSI derived from `close`; `open` and `volume` are never read). `time` is never read — no date/session gate exists in code.
- No funding, OI, mark/index price, liquidation feed, trade/aggressor feed, L2/order book, on-chain, options/Greeks, sentiment/news, macro, or cross-venue state is referenced or required.
- Instrument: `BTCUSDT` 1d perpetual under the standard downstream overlay — this matches the FMZ executable header (`Futures_Binance` / `BTC_USDT` / `period: 1d`) exactly, so no spot→perpetual substitution is made and no contract-identity gap is declared. The contradicted `Coinbase BTCUSD` prose is not followed.
- Single pair, single instrument, no basket, no ranking, no cross-sectional step, no shared portfolio state.

## Execution assumptions

- Timing: `process_orders_on_close=true` is code-declared in the live `strategy()` declaration → completed-bar decision with same-bar-close fills. `calc_on_every_tick=false` is code-declared (no intrabar evaluation); `calc_on_order_fills=false` is code-declared (no fill-chained recalculation). Compatible with the pinned Hummingbot completed-bar/same-close convention; never approximated.
- Declaration, code-read verbatim: `strategy('Sonic R & RSI only BTCUSD D1 strategy', shorttitle='sonic R & RSI Strategy', overlay=true, close_entries_rule="FIFO", default_qty_type=strategy.percent_of_equity, max_bars_back=500, default_qty_value=100, calc_on_order_fills=false, pyramiding=1, commission_type=strategy.commission.percent, commission_value=0.2, process_orders_on_close=true, calc_on_every_tick=false)`.
- Maximum same-side concurrency: 2 long sleeves. `pyramiding=1` is code-declared: the v5 reference (`#fun_strategy`, via its mirrored text) states the value is the maximum number of same-direction entries, with 0 allowing a single entry — so 1 admits the second same-side entry (`buyEMA` + `buyRSI` coexist) and rejects a third while both are open. Each `strategy.close` flattens only its named sleeve (per-ID, FIFO-ordered by `close_entries_rule="FIFO"`); F3 forces the executing engine to confirm "two named sleeves, third same-side entry rejected, per-ID closes" end to end rather than asserted here.
- Re-entry/cooldown: no cooldown is declared (0 occurrences of any delay/counter input) → explicitly none. After a sleeve closes, the next bar's qualifying print re-enters that sleeve; while a sleeve is open, its repeated signals are absorbed by the pyramiding cap, not accumulated. No `position_size`/`opentrades`/`position_avg_price` read exists, so no position-aware state conditions any signal — sleeve identity is carried by order ID, not by engine-state reads.
- Sizing: code declares 100 percent-of-equity compounding (`default_qty_value=100`, `default_qty_type=strategy.percent_of_equity`). Replaced downstream by the explicit house overlay (6% + 6% + 6%, isolated) — event-neutral here because no rule reads equity, notional, or fill size; entries and exits are pure signal conditions. Never presented as source-native. Downstream must additionally map the two-sleeve book onto the overlay (sleeve-level base allocation) before any screening run; that mapping is downstream research design, not source semantics.
- Commission 0.2 percent (`commission_type=strategy.commission.percent`, `commission_value=0.2`) is code-declared source accounting, recorded as declared. Downstream applies pinned Binance non-VIP USDⓈ-M fees plus realized funding as pure accounting; funding accrues only while long and changes no event. F4 checks cost-dependence.
- `initial_capital`, `currency`, slippage, `max_bars_back` beyond the declared 500, and margin/leverage are unset or non-signal in code → language defaults or downstream overlay, each confirmed end to end by F3 rather than asserted here.

## Evidence

### Source-reported

- No traceable numeric performance is cited: the page shows one backtest-chart image with no readable table, figure, or section numbers recoverable from the artifact, so no ROI/Sharpe/win-rate/trade-count from the source is reproduced here. Anything beyond "the page displays a backtest chart image over 2022-11-22→2023-11-22 on BTC 1d" would be invention.
- Source-admitted negative facts (kept as boundary, not signal): EMA/RSI false signals in violent markets; trend-end reversals can cause large losses; single-parameter sensitivity; the prose's own stop-loss/position-control advice is NOT coded.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- Trend-persistence legs are regime-fragile by the source's own admission (range markets chop the channel leg; the RSI sleeve then carries the book alone). F1/F5 are designed to surface exactly this: absence of either sleeve's entries, or sleeves that never close, on BTC 1d history fails the record back to research-only.

## Falsification plan

- **F1 — Signal presence and leg split.** Threshold (research-defined): at least 30 `buyEMA` entries with at least 10 `CloseEMA` exits AND at least 15 `buyRSI` entries with at least 5 `CloseRSI` exits on `1d` BTCUSDT perpetual bars from 2020-01-01, with at least 5 bars on which both sleeves are simultaneously open. Fail on any leg ⇒ that leg never trades this instrument/timeframe (or is dead code in practice); record stays research-only.
- **F2 — Boundary and contradiction audit.** Threshold: replay must demonstrate (a) a bar with `close` exactly equal to `ema34high` does NOT enter (strict `>`), (b) a bar with `close > ema34high` but `close[2]` inside the channel does NOT enter (persistence leg is load-bearing), (c) warmup bars hold with no order and no error, (d) entries fire regardless of the contradicted Coinbase prose (venue-independent replay), (e) no short order exists on any bar, and (f) a `dkienban1` bar closes only `buyEMA` while an open `buyRSI` sleeve survives. Fail on any deviation ⇒ pin the discrepancy in writing, research-only, no adoption.
- **F3 — Engine-default audit gate.** Threshold (research-defined): the executing engine must confirm end to end — fill at the decision bar's close, once-per-bar evaluation, no fill-chained recalculation, max two coexisting same-side sleeves with a third same-side entry rejected, per-ID FIFO closes, immediate re-entry eligibility the next bar, and every unset declaration reading its Pine v5 language default. Fail if any recorded value differs ⇒ pin the discrepancy, research-only.
- **F4 — Cost ladder.** Threshold (research-defined): apply 0 / 1 / 2 / 5 / 10 bps per side plus a funding-accrual leg for the long side; fail if net annualized return turns non-positive at 2 bps per side or net Sharpe falls to 0 or below at 5 bps per side ⇒ the edge is cost-dependent, research-only, never proposed for adoption.
- **F5 — Cross-instrument generalization.** Threshold (research-defined): run the identical frozen rule on ETHUSDT perpetual 1d and on one further major perpetual chosen before inspection; fail if 0 of 2 produce positive net return after costs at 2 bps per side ⇒ single-asset overfit diagnosis.

## Crypto portability

- Native crypto rule in its own backtest (Binance futures BTC 1d, 24/7 tape) — no equity-session adjustment needed; the contradicted Coinbase mention changes nothing in code.
- 1d crypto bars are continuous (no close auction, no overnight gap concept); the `close[2]` persistence confirmation reads naturally on a 24/7 series.
- Long-only requires no margined venue for the signal itself, and runs natively under the house USDT-M perpetual overlay. Any spot-only downstream runs the identical rule with no modification — and with no short leg defined, no direction restriction is needed at all.

## Limitations

1. Dual-sleeve concurrency (up to 2 coexisting longs) must be mapped onto the house DCA overlay before screening; any consumer replaying raw 100%-equity compounding per sleeve instead of the overlay misstates notional.
2. EMA-34 seeding warmup (~36 bars) must be honored; replays starting mid-history without warmup misstate the channel.
3. No immutable commit-SHA provenance (FMZ page + mirror bytes only); if the author edits the page, this record's bytes no longer match live — re-verify before any downstream use.
4. Page prose (dual-EMA-cross description, Coinbase market, stop-loss advice) is boilerplate contradicted by the code and is never followed — listed above, not silently dropped.
5. Commission 0.2% in code is replaced by the house cost model downstream; any consumer replaying raw code costs instead of the overlay misstates PnL.
6. F-gates above are research tests, never substitutes for the (complete) source rules.

## Implementation status

- Not implemented. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- Research-only. Not approved for Paper, Testnet, Mainnet, or live trading. Only a `PASS` downstream selection plus satisfied F-gates may advance this toward screening, and satisfying F-gates is screening evidence, not trading approval.

## Related Wiki records

- None (no Wiki write was performed for this record).

## Sources

- https://www.fmz.com/strategy/433019 — primary source (code, header, prose, image all read from this page's artifact).
- https://www.tradingview.com/pine-script-reference/v5/#fun_strategy — Pine v5 `strategy()` declaration reference (pyramiding, order-function, and calculation-flag semantics).
- https://www.tradingview.com/pine-script-docs/concepts/strategies/ — strategy calculation/execution concepts (completed-bar evaluation, `process_orders_on_close`).
