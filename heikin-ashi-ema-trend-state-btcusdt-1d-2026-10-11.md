---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Heikin-Ashi EMA trend state two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-09
sources:
  - https://www.fmz.com/strategy/362000
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Heikin-Ashi-Trend.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Heikin-Ashi EMA trend state two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/362000 (fetched live over HTTPS during this cycle with HTTP 200, 740629 bytes of landing HTML). Author token `ChaoZhang` × 2; prose describes an EMA-based Heikin-Ashi trend line with green-to-red color-flip alerts (`Heikin` 18, `heikinashi` 12, each of `Futures_Binance`, `BTC_USDT` byte-present twice on the page, matching the executable stanza venue). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Profit Factor` 0, `Take profit` 0, `Stop Loss` 0 — the sole `return` token is site-chrome JavaScript, not a performance figure. The page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository head via `git ls-remote` during this cycle — the same head pin as the merged Bollinger, PVT-EMA, KDJ, STARC, T3-Tillson, WaveTrend, Qstick, Aroon, SQZMOM-LB, TRIX, Schaff, KST, OBV-EMA and further admissions), exact file path `Heikin-Ashi-Trend.md` (pure-ASCII filename, no encoding ambiguity). File 2412 bytes, blob SHA `0cc1ffb6ab52fc3bb97443606fbe8e42705745db` (verified with `git hash-object` reproducing the identical SHA on re-download, and matching the GitHub contents API `sha`/`size` at the pinned commit). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/362000, `> Last Modified` = `2022-05-09 14:33:57` (date part adopted as `source_as_of`), the script prose quoted above, and the three-row Strategy Arguments table (`EMA = 77`, `EMA Smoothing = 21`, debug flag) matching the code defaults exactly. Original Pine authorship is credited in-code to `backslash-f`, MPL-2.0, 2022.
- Full `//@version=5` block read in full (order-affecting lines: the two `ta.ema(open/close, 77)` declarations, the two `request.security(heikinashi, timeframe.period, …)` pulls, the two `ta.ema(…, 21)` smoothing lines, the `trend := …` latch, and the `if trend / else` order pair; everything else is declaration plumbing or dead variables).
- Text census over the pinned code block: 1 `indicator(` (`Heikin-Ashi Trend Alert`/`overlay=true` plumbing only) / 0 `study(` / 2 `strategy.entry` (`"Enter Long"`/`strategy.long`, `"Enter Short"`/`strategy.short`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.close` / 0 active `stop=`/`limit=`/`profit=`/`loss=` / 0 `ta.crossover` / 0 `ta.crossunder` / 0 `alertcondition` / 0 `alert(` / 0 `plot` (the "line" is described in prose but no `plot` call ships — nothing visual gates any order) / 4 `ta.ema` (the full indicator stack: 77 on open, 77 on close, 21 smoothing × 2) / 2 `request.security` (both with `timeframe.period`, i.e. the chart's own frame — no second timeframe anywhere) / 1 `ticker.heikinashi` / 1 `syminfo.tickerid` / 2 `timeframe.period` / 1 bare `open` (the `ta.ema(open, 77)` line; `ema_open`/`heikinashi_open` identifier substrings excluded) / 1 bare `close` (the `ta.ema(close, 77)` line) / 0 bare `high` / 0 bare `low` / 0 `volume` / 3 `input(` (77, 21, debug flag) / 2 `var ` (`trend`, `last_trend`) / 0 `nz(` / 0 `na` / 0 `barstate` / 0 `lookahead` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `initial_capital` / 0 `commission` / 0 `calc_on_every_tick`. The debug input (`shouldShowDebugInfo`, 1 hit — its own declaration line) is read by no other line, and `last_trend` (1 hit — its own declaration line) is read by no other line — both counted in census, excluded from the rule, disclosed. No portable economics beyond the two bare order calls ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- Licence and rights: the Pine block carries the original MPL-2.0 header credited to `backslash-f`; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the executable `/*backtest*/` stanza itself backtests `Futures_Binance BTC_USDT` at `period: 4h` — this pin transfers the venue to the house research frame `1d`; the `15m` basePeriod is the stanza's sub-bar granularity, not a second decision frame, and only the symbol spelling is normalized, disclosed here, never presented as source-native); (2) completed-bar decisions with same-bar-close fills (the source ships no execution-timing argument — the file's executable context is the FMZ platform per its `/*backtest*/` stanza, and the `indicator(` wrapper means there is no TV-style next-bar-open source timing to preserve, disclosed here; the prior PSAR admission documents the same wrapper pattern); (3) an adopted 300-bar warmup with pre-warmup bars flat by record rule (covers the EMA77 seed plus the stacked EMA21 smoothing plus the Heikin-Ashi recursion with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The `77`/`21` inputs, the HA-context EMA construction, the `>=` trend latch, the `if trend / else` order pair, the `"Enter Long"`/`"Enter Short"` order paths, the two-sided always-in-market stance, and the no-stop/no-target posture are source-native and unmodified. No tie-break had to be invented: the `if/else` admits no third branch, and each bar's outcome is a single deterministic event.

Pre-write dedup (2026-10-11): working-tree case-insensitive filename search for `heikin` returns no strategy record — the thirteen `heikin` substring hits across the pool are census-boilerplate mentions in unrelated records (twelve single zero-count listings plus the UT Bot record, which explicitly freezes its Heikin-Ashi branch OFF with `h = false`, so no live Heikin-Ashi rule exists anywhere in `main`). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. FMZ page `362000` and mirror file `Heikin-Ashi-Trend.md` are cited by no existing record. Closest pool relatives (`super-guppy`, `tema-dema-hma-cross`, `t3-tillson`, `ema-20-50-cross`, UT Bot) are all regular-candle EMA/ATR constructions — none reads a Heikin-Ashi feed, none smooths HA-context EMAs, none latches a `>=` HA state. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Heikin-Ashi trend-week filtering with double EMA damping (prose plus code): raw candles are replaced by their Heikin-Ashi transform (recursive averaging that stretches consecutive same-color runs and compresses chop), then the HA open and HA close are each passed through a slow EMA77, then smoothed again with EMA21 — two layers of damping on top of an already-averaged feed. The `>=` comparison of the two smoothed lines is the color of the original alert script: green while smoothed HA-close holds above smoothed HA-open, red otherwise. The design bets that triple-averaged trend color persists at the multi-month scale and flips only when the averaged consensus genuinely turns; it ships no stop, no target, and no flat state — the book is always carrying the last color.

### Research interpretation

Always-in-market state machine, edge-free, two-sided, latch-driven. Unlike cross-based records (Bollinger upper-break, PSAR dot-flip, Gann HiLo cross) there is no trigger bar: the same `if/else` re-asserts the standing color every bar, so entries after the first signal are either no-ops (color unchanged, no pyramiding ships anywhere) or full reversals (color flipped, one-step close-and-reverse). Unlike oscillator-latch systems (Fisher zero-sign, RAVI threshold latch) the state variable is not a bounded oscillator but the sign of a spread between two heavily smoothed HA-context averages — whipsaw cost concentrates in long sideways grinds where the two lines braid, while trending stretches print nothing but the initial entry. Unlike the UT Bot record its Heikin-Ashi leg is the entire signal, not a fenced-off option. The bet is on triple-smoothed HA color persistence under a 77/21 leg pair, not on any price level, band penetration, volatility ruler, second indicator, slope test, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`ema_input = 77` frozen, `ema_smoothing = 21` frozen, debug frozen `false` — any other value is a different, unpinned rule):

- Declarations (derived): always-in-market long/short machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; flat exists only before the first post-warmup order.
- HA-context average block, pinned verbatim: `ema_open = ta.ema(open, 77)` and `ema_close = ta.ema(close, 77)`, each evaluated inside the `ticker.heikinashi(syminfo.tickerid)` symbol context via `request.security(heikinashi, timeframe.period, …)` — i.e. the EMA77 of the HA open series and the EMA77 of the HA close series on the chart's own frame (both `request.security` calls carry `timeframe.period`, so the derived rule is single-frame by construction).
- Smoothing block, pinned verbatim: `heikinashi_open_smooth = ta.ema(heikinashi_open, 21)`; `heikinashi_close_smooth = ta.ema(heikinashi_close, 21)`.
- Trend latch, pinned verbatim: `trend := heikinashi_close_smooth >= heikinashi_open_smooth` (recomputed every bar over the `var trend = false` seed; `>=` means exact equality holds long — pinned as written, not invented).
- Orders, pinned verbatim: `if trend` → `strategy.entry("Enter Long", strategy.long)`; `else` → `strategy.entry("Enter Short", strategy.short)`, evaluated on every completed bar. From flat the first post-warmup bar opens; from the same side the call is a no-op under the default no-pyramiding construction (no `pyramiding` argument ships anywhere); from the opposite side the call reverses the full unit in one step — reversal is the sole exit path, with no separate exit leg (zero `strategy.exit`/`strategy.close` legs anywhere).
- Exits and risk, pinned verbatim: there are none besides reversal — zero `strategy.exit`/`strategy.close` legs, zero `stop=`/`limit=`/`profit=`/`loss=` qualifiers anywhere. No take-profit, no trailing, no time exit, no flat signal — pinned as written, explicitly none, not invented.
- Direction: two-sided with resting exposure. A long-only or flat-capable reading would contradict the `else`-branch short leg and is explicitly not this record.

## Required data

- Completed `1d` bars of BTCUSDT: `open` and `close` only (the EMA77 seed pair; `high`/`low` enter solely inside the venue's Heikin-Ashi transform of those same completed bars — no bare `high`/`low` series is read by any code line, and no `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read anywhere).
- Single decision timeframe `1d` (derived pin; both `request.security` calls carry `timeframe.period`, so no second evaluated frame exists by construction — the `15m` basePeriod is FMZ sub-bar execution granularity, not a signal input).
- Warmup: the binding seed stack is EMA77 (77 completed bars) feeding EMA21 smoothing feeding the HA recursion. The adopted warmup is the first 300 completed `1d` bars flat by record rule (predeclared researcher choice — ~4× the slow length with margin for the stacked smoothing and the recursive HA seed; no traded bar reads a seeded value). Without the warmup the `var trend = false` seed plus `na`-seeded averages would print the `else`-branch short on the earliest bars by Pine `if na` semantics — the warmup absorbs that structurally, disclosed, never a researcher tie-break. No repainting, no negative shift, no future reference, no full-sample normalization, no `lookahead`, no `barstate`-gated order path; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue — venue transfer, symbol spelling, and the `4h`→`1d` frame transfer are disclosed here, never presented as source-native). The short leg needs a venue with short permission; futures satisfies this — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source ships no execution-timing argument and its `indicator(` wrapper defines no strategy fill timing — this record claims neither FMZ-stanza timing nor any intrabar behavior. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere and a single `if/else` producing at most one order event per bar, there is no same-bar ordering ambiguity.
- Sizing/capital/costs: the source ships no portable economics of any kind (no capital amount, no commission/slippage/funding/margin argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-unit machine by default no-pyramiding construction — at most one unit long or short; same-side re-assertion prints nothing. No cooldown ships anywhere (explicitly none, not invented). No flat state is reachable after the first post-warmup order except by reversal; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (the `77`/`21` inputs, the HA-context `ta.ema(open/close, 77)` pair, the two `request.security(heikinashi, timeframe.period, …)` pulls, the two `ta.ema(…, 21)` smoothing lines, the `>=` trend latch, the `if trend / else` long/short order pair, and the 2021-05-08→2022-05-07 `4h`/`15m` Binance backtest header), the author/title stamps, the three-row arguments table, and the prose describing the EMA-based HA line with color-flip alerts. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden risk layer: the body contains zero `strategy.exit`/`strategy.close` legs and zero `stop=`/`limit=`/`profit=`/`loss=` qualifiers. The no-stop/no-target always-in-market posture is prescribed, explicitly none, never hidden.
2. No third branch: the `if trend / else` pair is exhaustive — every bar resolves to exactly one order event, so no precedence, cooldown, or arbitration rule was invented.
3. Edge-not-latch fenced the other way: unlike cross systems there is no trigger bar at all — the order pair re-asserts standing state every bar, so no bar can open twice (no pyramiding ships anywhere) and no flip can be missed between evaluations.
4. `>=` equality fenced: exact equality of the two smoothed lines holds long by the pinned operator — a strict-`>` reading would contradict the code and is explicitly not this record.
5. Dead-code fenced: `last_trend` (1 hit) and `shouldShowDebugInfo` (1 hit) are each read by no other line — neither gates any order, and no debug display code ships at all. A reader mistaking them for signal inputs would contradict the census. Disclosed, not hidden.
6. Seed behavior fenced: before the EMA/HA seeds resolve, Pine `na` comparisons keep the latch false-y and the `else` branch would print short — the adopted 300-bar flat absorbs the entire seed stack structurally, so no seeded or `na` value ever trades. Structural, disclosed, never a researcher tie-break.
7. Single-frame fenced: both `request.security` calls carry `timeframe.period` — there is no MTF pull, no `request.*` cross-symbol pull beyond the same-venue HA transform, and no `lookahead`. The HA transform itself is a causal function of completed regular bars (recursive average of prior HA value and current bar), computable point-in-time with no future leakage — stated plainly.
8. No future leakage in the stack, stated plainly: at decision bar `t` the slowest inputs are the EMA77 values resolving at bar `t`'s close, smoothed by EMA21 resolving at the same close — every input is complete at the close. No negative index, no offset, no full-sample normalization, no `barstate`-gated order path, no `plot`/`alertcondition` gating any order (none ships that gates).
9. Order-id completeness fenced: the sole long id is `"Enter Long"` and the sole short id is `"Enter Short"` — with no pyramiding anywhere there is at most one unit to reverse, so the opposite-side `strategy.entry` provably flattens-and-reopens in one step. No partial-fill residue is reachable by code.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, completed-bar same-bar-close fills, the adopted 300-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the `77`/`21` inputs, the HA-context EMA77 pair, the EMA21 smoothing pair, the `>=` latch, the `if/else` order pair, single-unit no-pyramiding state, the two-sided always-in-market stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, length pair, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (2412 bytes, blob SHA recorded, `git hash-object` identical on re-download, contents-API `sha`/`size` matched); the FMZ canonical page verified live the title, the `ChaoZhang` token, the EMA-based HA trend prose, the `Futures_Binance BTC_USDT` backtest stanza, and the absence of any performance numbers — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `77` / `21` / HA-context EMA pair / `>=` latch / `if trend / else` long/short pair / no-stop-no-target posture / two-sided always-in-market single-unit / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — HA-feed relevance: replacing the Heikin-Ashi-context EMA77 pair with regular-candle EMA77 on the same `open`/`close` (same 21 smoothing, same latch, same risk posture) must not improve net expectancy; fail ⇒ the HA transform adds nothing over plain-candle averaging.
- F2 — Slow-length relevance: replacing the 77 slow length with a 21 slow length (same HA context, same smoothing, same latch, same risk posture) must not improve net expectancy; fail ⇒ the pinned slow leg adds nothing over a fast leg.
- F3 — Smoothing relevance: removing the EMA21 smoothing pair (latching the raw HA-context EMA77 pair directly, same risk posture) must not improve net expectancy; fail ⇒ the second damping layer adds nothing over the single slow average.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue). The HA transform plus EMA arithmetic ports across perpetual venues without structural change — no volume read means venue volume-reporting differences touch nothing, disclosed as a robustness property, not a portability proof. The two-sided stance requires a short-capable venue (futures satisfies this); a spot deployment would express only the long half and is a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source ships no execution-timing argument; this record executes completed-bar same-bar-close on `1d` BTCUSDT and claims no stanza timing. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market and frame: the stanza backtests `Futures_Binance BTC_USDT` at `period: 4h` (`15m` basePeriod is sub-bar granularity, not a second decision frame); this record pins `BTCUSDT 1d`. The 77/21 leg pair spans ~3 months at daily scale versus ~2 weeks at the stanza scale — regime behavior differs by construction. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or base period.
- Always-in-market risk: there is no flat signal and no stop — adverse excursion reverses only on the next opposite color, chop braids the two smoothed lines into alternating full reversals, and whipsaw is the coded cost of the design, disclosed, not smoothed, not supplemented.
- No source economics: the source ships no capital amount, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the EMA77/EMA21/HA seed stack settles within hundreds of bars; the first 300 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.
- Indicator-wrapper timing: the file declares `indicator(` yet closes with `strategy.entry` calls (the FMZ-porter pattern previously admitted with disclosure in the PSAR record) — under TradingView Pine the wrapper would not compile as a strategy; the executable context here is the FMZ stanza plus this record's derived Hummingbot timing. Disclosed, not hidden.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (EMA-based HA trend prose plus `Futures_Binance BTC_USDT` backtest stanza verified live via HTTP-200 page record): https://www.fmz.com/strategy/362000
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `0cc1ffb6ab52fc3bb97443606fbe8e42705745db`, 2412 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Heikin-Ashi-Trend.md
- Pine strategy semantics (v5 order calls, `request.security`/`ticker.heikinashi`/`ta.ema` built-ins): https://www.tradingview.com/pine-script-reference/v5/
