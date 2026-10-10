---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Fibonacci retracement 0.618-reclaim long with 0.236-rail exit on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-03
sources:
  - https://www.fmz.com/strategy/430984
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E5%9B%9E%E6%92%A4%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5%E8%84%9A%E6%9C%AC.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fibonacci retracement 0.618-reclaim long with 0.236-rail exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-10):

- Canonical page: https://www.fmz.com/strategy/430984 (page title `斐波那契回撤交易策略脚本 | FMZ`, publisher account `Zer3192`, `Created: 2023-11-03 15:30:58`, equal to the mirror `Last Modified`). Fetched over HTTPS during this cycle (714132 bytes): the page embeds the full Pine block quoted below exactly once (page-wide counts read `strategy.entry` 1 / `strategy.close` 1 / `strategy.exit` 0 / `strategy.order` 0, with zero `stop=` / `limit=` anywhere) plus the porter's `/*backtest*/` header (`period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT`, 2 hits each). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Profit Factor` 0, `Sharpe` 0, `Max Drawdown` 0, `Win Rate` 0, `Annualized` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2023-11-03 from the page Created stamp, which equals the mirror `Last Modified`).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800, subject `update`; verified repository head at research time via the GitHub commits API — the same head pin as the merged Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray and ActionZone admissions), exact file path `斐波那契回撤交易策略脚本.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 1522 bytes, blob SHA `315ba0a9e8b4990fba10d9dab0e9f3c1cd79ea98` (verified against the GitHub contents API at the pinned commit — size and SHA both match; content bytes re-downloaded at the pin are byte-identical, sha256 `6f68499001cb612c2b6b75af263d2c4ebdf2df7f72984a90d25d9ee54d902dfe`). The mirror prints `> Detail` = https://www.fmz.com/strategy/430984 and `> Last Modified` = 2023-11-03 15:30:58 (equal to the page Created stamp). The mirror ships no prose strategy section beyond the argument table — there are no prose-only extras to fence; the code block is the whole rule.
- Full `//@version=5` block read in full (code lines from `/*backtest` through the final `plot`, strategy declaration `strategy("斐波那契回撤交易策略", overlay=true, initial_capital=10000)`). The page-embedded `/*backtest*/` header (`start: 2022-10-27 00:00:00`, `end: 2023-11-02 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`) is byte-present on both the canonical page and the mirror block — market (`BTC_USDT` Binance futures) and decision frame (`1d`, 1h execution granularity) are therefore source-native, never researcher-chosen. With market entry and full-close legs only (no stop/limit/intrabar legs anywhere), the 1h base granularity is immaterial to fills (24 native 1h bars per 1d bar on a 24/7 venue); this record keeps the source-native 1d/1h frame with no frame derivation.
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("Buy", strategy.long, when=longCondition)` — market entry, no price argument, no quantity) / 1 `strategy.close` (`strategy.close("Buy", when=shortCondition)` — full close, no quantity qualifier) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`qty` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open` (the rule reads `high`/`low`/`close` only) / exactly 4 `input(` (`length = input(50)`, `fib1 = input(0.236)`, `fib2 = input(0.382)`, `fib3 = input(0.618)` — all pinned at defaults; `fib2` feeds only a display `plot`, fenced below). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission_*`, `slippage` and sizing are unset throughout (Pine language defaults apply — quoted verbatim in census). The 3 `plot` calls (the three fib rails) feed no order condition; order logic reads exactly the two signal booleans.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs. The 0.236-rail close posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by Zer3192; the pinned code block carries no licence header of its own (the FMZ page is the publication vehicle). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly three: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere, quoted verbatim in census); (2) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers the 50-bar extreme windows plus cross-reference margin — see Required data); (3) house sizing/capital replacing the source economics stub (`initial_capital=10000` ships verbatim with no quantity, commission, fee, slippage, or margin assumption anywhere — see Execution assumptions). Market (BTCUSDT Binance futures), decision frame (`1d`, 1h base), the pinned `50 / 0.236 / 0.382 / 0.618` literals, the level arithmetic, both cross triggers, order IDs, direction handling, the full close leg, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `fibonacci`, `fiblevel`, `retracement` (whole-word), `430984`, and `Zer3192` return zero admitted rules using this source, author strategy, indicator, or mechanism — the only `retracement` hit anywhere is the plain English word inside `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` prose (an RSI level rule, never a Fibonacci construction), and no `fibonacci`/`fibLevel`/`430984`/`Zer3192` hit exists outside this record. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closed research PRs (#1–#112 reviewed by title) contain no Fibonacci record. Closest pool records are different mechanism classes: `donchian-20-10-breakout-btcusdt-1h` trades raw rolling-extreme breaks themselves (highest-high entry, lowest-low exit — never interior fractional levels); `darvas-box-breakout-long-btcusdt-1d` trades frozen consolidation-box rails that require a formation filter (never a rolling 50-bar range); `dual-thrust-open-range-breakout-two-sided-btcusdt-1d` trades same-day open-range expansion (never a 50-bar retracement grid). Five-axis distinction: mechanism differs (interior fractional-rail reclaim of a rolling range — entry on reclaiming the deep 0.618 rail, exit on losing the shallow 0.236 rail — versus raw-extreme breaks, frozen formation boxes, or open-range expansion), signal construction differs (`ta.highest`/`ta.lowest` 50-bar range scaled by fixed Fibonacci fractions 0.236/0.618 with `ta.crossover`/`ta.crossunder` close crosses — no pool record computes `highLevel - range * 0.618`), trigger differs (reclaim-cross entry plus rail-loss exit on one long-only unit), and source identity differs (fmzquant pin `7853bb2` port of Zer3192's FMZ 430984 release versus other FMZ IDs and authors).

## Economic mechanism

### Source-reported

Rolling-range Fibonacci retracement reclaim (mirror argument table plus code, no prose section ships): the highest high and lowest low of the last 50 bars freeze a rolling range; fixed Fibonacci fractions mark interior rails below the range top; a close reclaiming the deep 0.618 rail buys the resumption of the range-top advance, and the first close losing the shallow 0.236 rail ends the trade. The design bets that a dip which holds above the 61.8% retracement and reclaims it resolves back toward the range top, while a close back under the 23.6% rail admits the resumption failed.

### Research interpretation

Range-interior mean-trend hybrid with an explicit flat state, long-only. Unlike raw-extreme systems (Donchian) that buy every new N-bar high, this system never buys the high itself: it buys only the recovery cross back above the deep interior rail after weakness — a strictly rarer, dip-conditioned entry at the cost of missing straight-line breakouts that never retrace 61.8% first. Unlike frozen-formation systems (Darvas) that wait for consolidation to certify a rail, the rails here re-freeze every bar from the rolling 50-bar window, so entries can fire on the first V-shaped reclaim without any formation lag — at the cost of rails that breathe with the window. Unlike always-in-market holders, the system rests flat before the first 50-bar window exists and after every 0.236-rail exit, and it never shorts: rail breaks while flat are no-ops. The bet is on resumption *within* a live 50-bar range, not on any oscillator level, volatility band, or calendar effect.

## Signal

Exact rule as pinned (`length=50`, `fib1=0.236`, `fib2=0.382`, `fib3=0.618` frozen — the four inputs at defaults; any other value is a different, unpinned rule):

- Declaration (derived): `strategy("斐波那契回撤交易策略", overlay=true)` with same-bar-close execution adopted for the derived record (no such argument ships in the source) and house sizing replacing the source economics stub (see Execution assumptions). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). No commission, margin, fee, or slippage assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Level arithmetic (pinned): `highLevel = ta.highest(high, 50)`; `lowLevel = ta.lowest(low, 50)`; `range1 = highLevel - lowLevel`; `fibLevel1 = highLevel - range1 * 0.236`; `fibLevel2 = highLevel - range1 * 0.382` (display only — plotted, never read by any order leg); `fibLevel3 = highLevel - range1 * 0.618`. All three rails recompute every bar from the rolling window (step functions that breathe with the window, never frozen).
- Entry long: `strategy.entry("Buy", strategy.long, when=longCondition)` with `longCondition = ta.crossover(close, fibLevel3)` — fires on the single bar where the close crosses strictly up through the deep 0.618 rail, with same-bar-close execution under the derived declaration.
- Exit: `strategy.close("Buy", when=shortCondition)` with `shortCondition = ta.crossunder(close, fibLevel1)` — full close of the long on any bar whose close crosses strictly down through the shallow 0.236 rail (no quantity qualifier), with same-bar-close execution under the derived declaration. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only with an explicit flat state. No short leg exists anywhere; before the first 50-bar window both rails are `na` so both signals are `na` (no trade by construction). On a spot venue the rule expresses unchanged (see Crypto portability).
- Display isolation: the 3 `plot` calls (the three fib rails) render only and cannot change any order; the `fib2 = 0.382` input exists solely to position the middle plot.

## Required data

- Completed `1d` bars of BTCUSDT: `high` (rolling range top), `low` (rolling range bottom), `close` (both rail crosses). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1h` equals native 1h execution granularity — 24 1h bars per 1d bar on a 24/7 venue — and with market-entry/full-close legs only, no intrabar path exists for the base to affect). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: the extreme windows need 50 completed `1d` bars and each cross reads one prior bar. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 50-bar window plus cross-reference margin), reinforced by the structural na-guard (`ta.highest`/`ta.lowest` are `na` until the window fills, and `ta.crossover`/`ta.crossunder` against `na` never fires). `ta.highest`/`ta.lowest` are exact window functions with no seed transient, so no decay margin is required. No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. The current bar's `high`/`low` enter the window only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source-native per the header's `Futures_Binance BTC_USDT`; venue transfer from `BTC_USDT` to `BTCUSDT` spot-symbol spelling is naming only, never presented as a market change).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity. Entry and exit legs are evaluated in source order (entry block before exit block): on the rare bar where a window update makes both conditions true at once (see Negative evidence), the derived execution fills the entry at the close and closes it at the same close, ending flat; no ordering resolution beyond source order is required.
- Sizing/capital/costs: the source ships `initial_capital=10000` with no quantity, commission, fee, slippage, or margin assumption anywhere (quoted verbatim) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace the source economics here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one long unit under the fixed order ID `Buy`; entry refires while already long are no-ops by the language default, the 0.236-rail close exits in full, an exit while flat is a no-op, and re-entry is allowed immediately on the next 0.618-reclaim cross after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no short side exists to conflict; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (50-bar high/low windows, range arithmetic, fixed 0.236/0.382/0.618 fractions, `ta.crossover` entry, `ta.crossunder` exit, fixed `Buy` order ID), the active `strategy(...)` declaration, the `斐波那契回撤交易策略` title, and the page-embedded 1d/1h November-2022→November-2023 backtest header. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`qty` — the sole position-closing path is the coded 0.236-rail `strategy.close("Buy")` leg. The absence is coded (the order block ends with the close leg and only display plots follow).
2. Display-only input fenced: `fib2 = input(0.382)` is read by exactly one line (the middle `plot`) and by zero order-gating lines — retuning or removing it changes no trade; it is pinned as display-only, never as a signal parameter.
3. The entry buys a reclaim, never the extreme: a straight-line breakout that never dips to the 0.618 rail prints no entry by code, not by venue choice — disclosed, not repaired.
4. Exit-leg conditionality, admitted plainly: a long opened on a 0.618-reclaim cross exits only on the next 0.236-rail crossunder. A market that grinds sideways between the rails, or that tops without ever crossing under the shallow rail, never exits until the rail breaks — there is no stop, no time-stop, and no opposite-signal exit beyond the 0.236 rail (a fresh 0.618-reclaim cross while long only refires a no-op entry). This is the coded trade, disclosed, not a tunable parameter here.
5. Degenerate dual-leg bars via window updates: because both rails recompute every bar, a bar whose window update reshapes the grid (prior close wedged exactly at a collapsed flat-range point with `range1[1] = 0`, current bar with `range1 > 0` and the close strictly inside the new grid) can satisfy `longCondition` and `shortCondition` together; source order (entry block before exit block) fills the long at the close and closes it at the same close, ending flat with two fills and no overnight exposure. This is the coded ordering, disclosed as the record's principal microstructure edge case.
6. Degenerate flat ranges: when `range1 = 0` (50 identical highs and lows), all three rails equal that print and a close breaking the flat line fires the corresponding cross leg by the documented `ta.crossover`/`ta.crossunder` strict definitions — deterministic, disclosed, not guarded.
7. The `length=50` literal, the `0.236 / 0.382 / 0.618` fraction set, the rolling (never frozen) rail semantics, the strict cross (not touch) triggers, the fixed order ID, the long-only posture, the full close leg, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning the length, converting a cross into a touch, adding a stop/target/filter/cooldown, enabling a short side, or trading the 0.382 rail would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; market, timeframe, every literal, the level arithmetic, both triggers, the close leg, and the risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open 1d/1h source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `length=50` / 0.236-0.618 fraction set / rolling rails / reclaim-cross entry / rail-loss exit / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Entry relevance: replacing the 0.618-reclaim cross entry with the always-live rail-state hold (long whenever the last rail signal was a reclaim cross, flat otherwise — i.e. the rule without the cross timing) must not improve net expectancy; fail ⇒ the cross timing adds nothing over holding the rail state.
- F2 — Exit relevance: removing the 0.236-rail close leg (holding the long through rail losses — buy-and-hold from the first qualifying reclaim, since no opposite signal exists) must not improve net expectancy; fail ⇒ the explicit rail exit is dominated by simply staying positioned.
- F3 — Fraction relevance: replacing the fractional interior rails with the raw rolling extremes (enter on `ta.crossover(close, highLevel)`-style range-top break, exit on `ta.crossunder(close, lowLevel)`-style range-bottom break at the same 50-bar window) must not improve net expectancy; fail ⇒ the Fibonacci fractions add nothing over the naked Donchian-style extreme.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source-native venue family). The high/low/close arithmetic ports across perpetual venues without structural change; the rule is long-only with no short leg, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base Binance-futures backtest; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the shallow 0.236 rail, which recomputes every bar and can drop with the window; a close that never crosses under the rail is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- Breathing rails: unlike frozen-formation systems, both rails re-freeze every bar from the rolling window, so a slow range-top decay can drag the 0.236 exit rail down with the market and delay the exit, while a fast window turnover can whip entries on marginal reclaims. The breathing is the coded construction, disclosed, not smoothed.
- No source cost declaration: no commission, fee, slippage, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (Zer3192, Created 2023-11-03): https://www.fmz.com/strategy/430984
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `315ba0a9e8b4990fba10d9dab0e9f3c1cd79ea98`, 1522 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E5%9B%9E%E6%92%A4%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5%E8%84%9A%E6%9C%AC.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
