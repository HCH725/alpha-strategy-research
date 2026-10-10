---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Sell-in-May seasonal hold long on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-02
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/-Sell%20in%20May%2C%20buy%20in%20September--Strategy.pine
  - https://tradingview.com/script/C2qlt3mi-Sell-in-May-buy-in-September-Strategy
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Sell-in-May seasonal hold long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (pinned immutable GitHub file, live raw fetch 2026-10-10 at pin):

- Canonical file: https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/-Sell%20in%20May%2C%20buy%20in%20September--Strategy.pine (repo `hasnocool/tradingview-pine-scripts`, file commit `e031cab2819a7d56fb8bb9d000252f51439986e2` dated 2023-09-02 — the sole commit touching this path; record `source_as_of` is that commit date, never the fetch date. Script author `DynamicSignalLab`; TradingView canonical page `"Sell in May, buy in September"-Strategy`, open-source strategy: https://tradingview.com/script/C2qlt3mi-Sell-in-May-buy-in-September-Strategy).
- Pinned blob SHA `f14e286e2ee760524bd21e41854cd266522e372b`, 825 bytes on disk; the copy fetched at the pinned commit is byte-identical (`cmp` clean) to the copy inspected, SHA-256 `1d5ff7ff6bf4ce87341b244689c9834b9b1f9fd58b206e9f0d7fd6426c558073`.
- The file is a TradingView page scrape whose embedded verbatim Pine v5 block is the complete 15-line program (`Expand (15 lines)`; `//@version=5`, `strategy("Sell in May, buy in September Strategy", overlay=false)` — a real executable `strategy(`, not an indicator). Full census of the pinned bytes: 1 `strategy(` / 0 `study(` / 1 `strategy.entry` (`"long"`, `strategy.long`) / 1 `strategy.close` (`"long"`, `when=closecondition`) / 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.close_all` / 0 `input(` / 2 `month` reads (`longCondition = month==9`, `closecondition = month==5`) / 0 `crossover` / 0 `crossunder` / 0 `ta.*` / 0 `request.*` / 0 `security(` / 0 ` dayofweek` / 0 `year` / 0 `time` / 0 `process_orders_on_close` (language default governs, recorded as source-declared-by-default) / 0 `pyramiding` (default `0` governs, recorded likewise) / 0 `calc_on_every_tick` (default `false` governs) / 0 stop/limit/profit/trail reads of any kind.
- State rule read verbatim: `if longCondition` → `strategy.entry("long", strategy.long)` on every September (`month==9`) bar; `if closecondition` → `strategy.close("long", when=closecondition)` on every May (`month==5`) bar. No other order path exists. The author's description ships the whole thesis in two sentences: "This script applies the classic traders mantra of \"Sell in May, buy in September\". Not much else to it to be honest."
- Corroboration only (never a gate fact): FMZ strategy 426460 independently describes the same rule ("it only uses the month to determine when to enter longs and when to close all positions. Longs are entered when the month switches to September, and all longs are closed when it becomes May") — cited as lineage corroboration, not evidence.
- The TradingView page itself was not opened this run (extraction backend unnecessary); the pinned file's embedded verbatim block carries every gate fact, and the TV URL is fenced as lineage/identity-only.

Licence and rights: the embedded block carries the author's MPL-2.0 header (`© DynamicSignalLab`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) same-bar-close fills on the traded market's own `1d` bars (the source sets no `process_orders_on_close`, so TradingView fills the September entry next-bar-open by default; this record pins completed-bar decision with same-bar-close execution for 1:1 pinned-backtester compatibility, predeclared — the calendar events are unchanged, only the fill convention); (2) research market BTCUSDT Binance spot `1d` (the pinned rule names no market in-code; long-only needs no margin, so spot is the minimal realistic venue — no source-market equivalence is claimed); (3) a pinned zero-bar warmup with pre-first-signal flat by record rule (the rule reads no lookback — `month` of the completed bar is known at its close; see Required data); (4) the per-bar September-entry / per-bar May-close idempotence pinned under Pine-default `pyramiding = 0` (repeat signals while holding / while flat are no-ops — recorded as source-declared-by-default plus researcher pin); (5) house sizing/capital/costs replacing the wholly absent source economics (see Execution assumptions). The `month==9` entry / `month==5` close / long-only stance / no-risk-leg posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `sell-in-may`, `sell in may`, `halloween`, and `month==` return zero strategy records using this source, author script, or month-seasonality signal (the only calendar record in the pool is `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` — a weekday-axis rule keyed on `dayofweek`, 24-hour Monday→Tuesday holds, Forven S01512 source; three-axis distinction: calendar axis differs (month-of-year vs day-of-week), holding differs (~8-month September→May seasonal hold vs 24-hour weekly hold), and source identity differs (DynamicSignalLab TV strategy `C2qlt3mi` vs Forven `monday_drift.pine`). The `month`/`seasonal` hits inside that record are its own dedup prose and mechanism discussion, not a month signal). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #58 (reconstruction batch — all 17 file paths verified, no calendar record), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit stop-flip long), and #92 (SSL channel state reversal) — different mechanisms, indicators, and sources. Closed research PRs (#1–#98 reviewed by title) contain no Sell-in-May or month-seasonality record.

## Economic mechanism

### Source-reported

The classic "Sell in May" (Halloween indicator) mantra: hold risk exposure through the seasonally strong September→April stretch, stand aside through the seasonally weak May→August stretch. The author claims no channel beyond the mantra itself ("Not much else to it to be honest. Seems to work though :-).") — no behavioural, structural, or risk-premium mechanism ships in-source.

### Research interpretation

Seasonal risk-premium timing on a pure calendar gauge. Unlike every indicator record in the pool, the rule never looks at price, volume, or volatility — the bet is that the November→April seasonal drift documented in equity-market literature ports, in long-only form, to BTC daily rotation strongly enough to carry an ~8-month hold. The failure mode is made plain: with no stop, no trailing, no regime filter, and no price read of any kind, a September entry that meets a multi-month drawdown realizes the full adverse excursion until the May close fires — the May exit is a calendar guillotine, not risk control. Corroborating caution (FMZ 426460, fenced): fixed-month trading "completely ignores actual market conditions" and "may exit profitable positions prematurely during bull markets, or fail to cut losses in time during bear markets" — quoted as third-party commentary, not evidence.

## Signal

Exact rule as pinned (`month==9` entry / `month==5` close frozen — any other month pair is a different, unpinned rule):

- Declaration (derived): Pine v5 program (`//@version=5`) with v5 semantics observed. Zero-indicator by construction (0 `ta.*`, 0 `input(`, 0 `request.*` / 0 `security(`). The `overlay=false` display flag gates no order. The single-side stance is source-coded: no short leg exists anywhere.
- State (pinned, source-verbatim): `longCondition = month==9`; `closecondition = month==5`, where `month` is the calendar month of the completed bar's time (exchange timezone; Binance is UTC — see Required data).
- Orders (source-coded, derivation only in fill timing, market, warmup, and idempotence pin): a bar with `month==9` → enter long one unit (`strategy.entry("long", strategy.long)`); a bar with `month==5` → close the long in full (`strategy.close("long", when=closecondition)`). Under Pine-default `pyramiding = 0`, the September entry fires on every September bar but opens only the first (already-long bars are no-ops — no adds, never averaged); the May close fires on every May bar but closes only the first (already-flat bars are no-ops). The source declares no pyramiding — the default governs, recorded as source-declared-by-default.
- No entry/exit ambiguity exists anywhere in this record: `month==9` and `month==5` are mutually exclusive on every bar, so conflict priority is provably irrelevant. Non-signal months are explicit no-ops with position carried (June→April after entry: hold long; June→August after exit: stay flat). Pre-first-signal bars are flat (no standing position exists until the first September bar).
- Risk posture (pinned): no stop-loss, no take-profit, no trailing, no time exit beyond the May calendar close, no cooldown (no stop/limit/profit/trail text of any kind exists anywhere in-source — each risk leg is explicitly none, not invented).
- Direction: long-only. The short side is explicitly absent (0 short orders anywhere); spot venue suffices and no margin-short permission is needed.

## Required data

- Completed `1d` bars of BTCUSDT: bar timestamps only (both order-gating reads are `month` of bar time; `open`/`high`/`low`/`close`/`volume` are read by no order-gating line — the rule never looks at price). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request.*` / 0 `security(` anywhere; 0 `time` reads — `month` is a direct bar-time builtin).
- Single decision timeframe `1d` (researcher choice — the pinned rule names no timeframe). One evaluation per completed bar; both signal reads reference the completed bar's own calendar month only; no intrabar path is read.
- Month semantics pinned: `month` resolves in the exchange timezone (Binance venues run UTC), so the September/May boundaries fall on the UTC-date month of each completed `1d` bar. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behaviour needs no approximation.
- Warmup: pinned zero-bar warmup — the rule carries no lookback, no seeding, and no recursive state (`pos`/`nz(`/`[]` history reads: none), so the very first bar is already fully defined; pre-first-September bars are flat by record rule (no standing position until the first `month==9` bar). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot under the house overlay (researcher choice — the pinned rule names no market in-code, and no source-market equivalence is claimed). Long-only needs no leverage and no margin-short permission, realistic on any spot venue.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for the September entry and the May close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source sets no `process_orders_on_close` (TradingView default fills the entry next-bar-open); this record does not claim any source fill convention. The calendar events (which September/May bar) are unchanged — only the fill convention is adapted.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule. No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the source ships no sizing, capital, fee, slippage, or funding concept of any kind (no `default_qty_*`, no `initial_capital`, no `commission_*`, no `slippage` anywhere). The explicit house overlay (Base 6% + Safety 6% + Safety 6% sizing frame where applicable to a single-unit long, pinned house cost assumptions — fees plus historical funding; no hypothetical zero funding claimed — the source declares no cost treatment at all) applies to the derived evaluation here, with the single-unit/no-add position pin from Signal, never presented as source-native behavior. Spot venue carries no funding leg; any perpetual-ported evaluation must carry the full house funding load instead.
- Concurrency: at most one long position at any time after the first September entry; the May close returns to flat in full in one step; re-entry after a close needs only the next September bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The pinned file ships the full construction (Pine v5 `strategy(` declaration, the `month==9` / `month==5` condition pair, the September-entry / May-close order pair, plus the author's two-sentence mantra description and MPL-2.0 header). The file ships zero performance numbers of its own: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No risk leg anywhere, admitted bluntly: no stop/limit/profit/trail text of any kind exists in-source — each explicitly none. A September entry followed by a one-way drawdown realizes the full adverse excursion until the May calendar close; gap-through sequences have no bound in this record. This is the coded posture minus nothing, disclosed as the record's principal risk.
2. Fill-timing derivation, admitted plainly: with no `process_orders_on_close` in-source, TradingView fills the entry next-bar-open by default — this record's same-bar-close fills are a researcher adaptation for pinned-backtester compatibility, disclosed, not source timing. The calendar event set is identical under either convention.
3. Price-blindness, admitted plainly: no order-gating line reads any price, volume, or volatility value — the rule cannot see bubbles, crashes, or trends. The May exit closes winners and losers alike; the September entry buys dips and tops alike. Disclosed, not smoothed over.
4. Repeat-signal idempotence, disclosed: the entry block fires on every September bar and the close block on every May bar; only the first of each acts, under Pine-default `pyramiding = 0` — pinned, not repurposed into adds or scales.
5. Source basis fenced: the pinned rule names no market or timeframe. The BTCUSDT-spot-`1d` choice, same-bar-close fills, zero-bar warmup with record-rule pre-signal flat, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
6. Derivation boundary fenced: the only non-source-native behaviours in this record are same-bar-close fills, the BTCUSDT-spot-`1d` market choice, the adopted zero-bar warmup with pre-signal flat, and house sizing/costs — all predeclared above; the `month==9` / `month==5` literals, the every-qualifying-bar order blocks, the long-only stance, and the no-risk-leg posture are source-verbatim. This record is therefore never evidence that the original script itself passes.
7. Lineage limit: the TradingView page was not opened this run (unnecessary — the pinned file's embedded verbatim block is complete at 15 lines); lineage rests on the pinned file's own author/version stamps and the stable TV URL — every gate fact is from the pinned block itself, corroborated only by the FMZ prose description fenced above.
8. The `month==9` / `month==5` literals, the hold-through-all-other-months posture, the full close (never partial), and the long-only stance are pinned, not removed: retuning any month, adding any TP/SL/trailing/cooldown leg, adding a short leg, or trading partial size would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `month==9` entry / `month==5` close / full close / long-only / `1d` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — Month relevance: replacing the September→May hold with the complementary May-close→September-entry schedule (hold only the four stood-aside months, same mechanics) must not improve net expectancy; fail ⇒ the specific seasonal window adds nothing over generic time-in-market.
- F2 — Exit relevance: replacing the May calendar close with a fixed-horizon close (exit N bars after each September entry, same entries) must not improve net expectancy; fail ⇒ the May guillotine adds nothing over time-based risk control.
- F3 — Direction relevance: running the identical calendar inverted (short each September→May window on a margin venue, same fills) must not improve net expectancy; fail ⇒ the long-seasonality direction adds nothing over the calendar mask itself.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision frame researcher-chosen `1d`; arithmetic over bar timestamps only with no venue-specific read). The construction ports across spot and perpetual venues with full timestamped `1d` feeds without structural change (a perpetual port must additionally carry the house funding load — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read, so session-gap behaviour needs no approximation — the UTC-month boundaries are the complete specification. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No risk leg anywhere: loss is bounded only by the May calendar close; the record carries no stop-loss/trailing/time-exit/cooldown by design — disclosed as the principal risk, not a gap to be quietly repaired later.
- Derived fill timing: same-bar-close execution is a researcher choice over logic that defaults (in TradingView) to next-bar-open; backtest economics of other timings differ by construction — the adaptation is disclosed, not hidden.
- Researcher market/frame: the pinned rule names no market or timeframe — BTCUSDT spot `1d` is a researcher choice; signal timing on other markets or frames would differ by construction.
- Position-state pin: repeat-signal behaviour executes nowhere in-source beyond the default; the single-unit/no-add pin under Pine-default `pyramiding = 0` is recorded as source-declared-by-default plus researcher pin, disclosed.
- No source cost declaration: no capital, commission, fee, or slippage assumption ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Price-blindness cost: textbook breakdowns, halvings, and regime breaks inside the hold window are deliberately untraded-around — pinned, not recovered.
- Warmup cost: none — but symmetrically, any September bar in the evaluation's first calendar year enters immediately with no history requirement, by record rule.
- Lineage limit: the TradingView page was not opened this run (unnecessary); lineage rests on the pinned file's own author/version stamps and the stable TV URL — every gate fact is from the pinned block itself.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Sell in May, buy in September-Strategy [DynamicSignalLab] pinned GitHub mirror at commit `e031cab2819a7d56fb8bb9d000252f51439986e2` (sole commit touching this path, 2023-09-02): https://github.com/hasnocool/tradingview-pine-scripts/blob/e031cab2819a7d56fb8bb9d000252f51439986e2/-Sell%20in%20May%2C%20buy%20in%20September--Strategy.pine
- Sell in May, buy in September-Strategy [DynamicSignalLab] canonical TradingView page, lineage-only (page not opened this run): https://tradingview.com/script/C2qlt3mi-Sell-in-May-buy-in-September-Strategy
