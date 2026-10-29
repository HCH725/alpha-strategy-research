---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: SSL channel state-following reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2019-03-28
sources:
  - https://www.tradingview.com/script/xzIoaIJC-SSL-channel
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SSL channel state-following reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical TradingView page, fetched 2026-10-10):

- Canonical page: https://www.tradingview.com/script/xzIoaIJC-SSL-channel (page title `SSL channel — Indicator by ErwinBeckers — TradingView`, author `ErwinBeckers`, `OPEN-SOURCE SCRIPT`, `Updated Mar 28, 2019` — adopted as `source_as_of` 2019-03-28; category `Trend Analysis`). Read in a real browser session during this cycle: the `Source code` tab exposes the complete 13-line Pine block byte-verbatim — `//@version=3`, `study("SSL channel", overlay=true)`, the dead `period=input(title="Period", defval=10)`, the live `len=input(title="Period", defval=10)`, `smaHigh=sma(high, len)`, `smaLow=sma(low, len)`, the state line `Hlv = na` / `Hlv := close > smaHigh ? 1 : close < smaLow ? -1 : Hlv[1]`, the two display legs `sslDown = Hlv < 0 ? smaHigh: smaLow` / `sslUp = Hlv < 0 ? smaLow : smaHigh`, and `plot(sslDown, ...)` / `plot(sslUp, ...)` (`View in Pine Editor・13 lines`).
- Text census over the verbatim block: 1 `study(` / 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 2 `input(` (the dead `period` and the live `len`, both `defval=10`) / 2 `sma(` (`high` and `low`) / `close` read once (the flip comparator) / `high` once / `low` once / `open` 0 / `volume` 0 / 0 `request.*` / 0 `time(` / 0 `ta.crossover` / 0 `ta.crossunder` / 2 `plot(` (render only, gate no order). Pine v3 semantics (`study`, `sma`, `na`, `:=` reassignment, one evaluation per completed bar by language default).
- The page ships no performance output of any kind: it is an indicator publication (no Strategy Tester, no return, no win rate, no profit factor, no trade list, no equity curve). The `4.4K / 107 / 224950`-style counters on the page are community engagement figures, adopted here as no performance claim — this record claims no source-reported performance and no reproduced performance.
- The source names no market and no timeframe: it is a chart-agnostic overlay (`overlay=true`); at read time the page rendered on an FX daily chart, which is page chrome, not a strategy fact. Market (`BTCUSDT`) and decision frame (`1d`) are researcher-declared (predeclared below), never presented as source-native.
- No immutable GitHub mirror of this publication is claimed; provenance rests on the canonical TradingView page read verbatim this cycle, which is an eligible public source. No author licence header ships in the 13-line block; the page's open-source badge governs reuse, and this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Licence and rights: the canonical page is a public open-source TradingView publication. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source — the source is a pure indicator with zero order calls, so every order, fill, sizing, warmup, and market fact below is researcher-declared. Researcher-declared adaptations are exactly six: (1) indicator-to-order mapping — persistent state-following: `Hlv == 1` holds long (including the initial `na → 1` fix as the first long entry), `Hlv == -1` holds short (including the initial `na → -1` fix as the first short entry), `na` holds flat; every `1 → -1` flip reverses long-to-short in full and every `-1 → 1` flip reverses short-to-long in full; (2) same-bar-close fills on completed `1d` bars (the source declares no execution timing anywhere); (3) position-state pin — single-unit per side, repeat same-state bars are no-ops, reversals are full-unit in one step; (4) an adopted 15-bar warmup with pre-warmup bars flat by record rule (covers SMA-10 seeding plus margin — see Required data); (5) house sizing/capital/costs replacing the absent source economics (the source ships no capital, fee, slippage, margin, or funding text of any kind — see Execution assumptions); (6) market/frame declaration — `BTCUSDT` Binance perpetual on completed `1d` bars (the source is market-agnostic; naming a venue is the only market change, never presented as source-native). Band arithmetic (`sma(high,10)` / `sma(low,10)`), the `len = 10` literal, the ternary state line verbatim (including `na`-init and hold-else semantics), the long-leg ternary priority, the `==`/`na` hold edges, and the no-stop/no-target/no-cooldown posture are source-verbatim.

Pre-write dedup (2026-10-10): working-tree case-insensitive word-boundary searches for `ssl`, `semaphore`, and `mihkel` return zero hits anywhere — no admitted rule uses this source, author publication, indicator, or mechanism. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — single file verified), #49 (Gaussian channel StochRSI-gated breakout long — single file verified), #58 (reconstruction batch — file list verified, no SSL record), #63 (SuperTrend ATR-flip trend long — single file verified), and #89 (Chandelier Exit dual-stop state-flip long — single file verified) — different mechanisms, indicators, and sources. Closest pool record differs in mechanism class: `gann-hilo-activator-state-flip-trend-btcusdt-daily-2026-10-05.md` bands `sma(high,3)` / `sma(low,3)` displaced by one bar against the prior-bar band (`close[t]` vs `hi[t-1]`/`lo[t-1]`, effective window `t-3..t-1`), carries a strategy-native order layer (`strategy.entry` pair, `pyramiding=0`, 20%-of-equity compounding, `process_orders_on_close=true`, 2017-01-01 time gate), and admits entries only on a full `-1 → +1` / `+1 → -1` transition observed in-series (the initial `na` can never enter). Four-axis distinction: signal construction differs (undisplaced contemporaneous `t-9..t` SMA-10 bands vs 1-bar-displaced SMA-3 bands — different lengths and different reference windows), trigger differs (state-following where the initial `na → ±1` fix is itself the first entry vs transition-only-from-defined-state where `na` can never trade), order layer differs in kind (pure-indicator source with a fully researcher-declared order mapping vs source-native strategy order calls with sizing and gating), and source identity differs (TradingView `xzIoaIJC` by ErwinBeckers, March-2019 indicator vs FMZ 427070 by ChaoZhang/starbolt, September-2023 strategy).

## Economic mechanism

### Source-reported

The source states no mechanism beyond the title: a two-line channel of the 10-bar average high and average low whose relative position colors the regime — when the upper SSL line is above the lower line the reading is bullish, when below it is bearish. No behavioural, structural, or risk-premium channel is supplied; no prose strategy description ships on the page.

### Research interpretation

Edge-and-state two-sided reversal system with no price level, band-touch trigger, stop, target, or confirmation leg — always-in-market after the first `Hlv` fix, holding each regime until the close prints beyond the opposite band. The persistent `Hlv` state is the whipsaw filter: closes inside the channel change nothing, so only genuine band breaks trade rather than every touch of a level. Unlike zero-state holders (Coppock, Fisher) that re-assert a level every bar, this system trades only fix/flip bars and then holds through the regime: chop that alternates across opposite bands flips the full unit with no guardrail, while the 10-bar averaging delays both entries and reversals symmetrically. Unlike breakout systems with a volatility or range gate there is none — a break on a dead bar flips the position exactly as a high-conviction break does. Unlike the displaced-band Gann-HiLo pool record, the reference bands are contemporaneous (`t-9..t`), so the flip test reacts to the same bar's average rather than a lagged one. The bet is on BTCUSDT's own daily range-break persistence at the 10-bar horizon, never on a faster microstructure edge, a level, squeeze, calendar, or mean-reversion anchor.

## Signal

Exact rule as pinned (`len = 10` frozen — any other value is a different, unpinned rule; the dead `period` input is pinned as unread, never retuned):

- Declaration (derived): Pine v3 semantics (`study`, `sma`, `na`, `:=`, ternary). The block is an indicator: no `strategy(` declaration, no order call, no `calc_on_every_tick`/`max_bars_back`/commission/slippage text anywhere — pinned as unspecified-by-source, with house execution applying to the derived evaluation (see Execution assumptions). One evaluation per completed bar by language default.
- Indicator arithmetic (pinned, source-verbatim): `smaHigh = sma(high, 10)`; `smaLow = sma(low, 10)`; `Hlv = na`; `Hlv := close > smaHigh ? 1 : close < smaLow ? -1 : Hlv[1]` — all on BTCUSDT `1d` bars (predeclared market/frame declaration; operators, lengths, and nesting verbatim).
- State-following positions (predeclared indicator-to-order mapping): `Hlv == 1` → long (the initial `na → 1` fix opens the first long; each `-1 → 1` flip closes the full short and opens the full long in the same execution step); `Hlv == -1` → short (the initial `na → -1` fix opens the first short; each `1 → -1` flip closes the full long and opens the full short in the same step); `Hlv` is `na` → flat (pre-first-fix only, no position by construction). While the state holds, repeat same-state bars are no-ops by record rule (predeclared single-unit pin).
- `1`/`-1` are mutually exclusive on every bar by construction (the ternary yields exactly one of the three outcomes), so no bar can ever fire both legs — no same-bar ordering ambiguity exists anywhere in this record. Both-fire is additionally impossible by arithmetic: `high >= low` on every bar implies `smaHigh >= smaLow` always, so `close > smaHigh` and `close < smaLow` can never hold together; the ternary's long-leg priority is therefore provably unreachable, stated, not patched. The measure-zero edge (`close` exactly equal to a band, or a dead-inside bar) holds `Hlv[1]` and the position simply holds — stated, not patched. An `na` band (pre-seeding) fails both strict comparisons and propagates `na` — pinned as flat, never patched with a guard constant.
- Risk legs (pinned absence, not invented): 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.entry` ship anywhere — the derived posture is explicitly no stop, no target, no trailing, no time exit.
- Direction: two-sided long/short with symmetric full reversal. Futures venue required for the short leg (researcher-declared venue — pinned).
- Display isolation: both `plot(...)` legs render only and cannot change any order; the dead `period` input is read nowhere and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` (the sole series read by the two `sma` calls and the flip comparator in the derived record). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The record makes no live `request.*` call, so it is single-symbol single-frame by construction.
- Single decision timeframe `1d` (researcher-declared; the source is timeframe-agnostic). With state-following reversal legs only plus zero intrabar-conditional legs, no intrabar path exists anywhere in the rule.
- Warmup: each SMA-10 first exists on the 10th completed bar, and the first `Hlv` fix can print no earlier than that bar. The adopted warmup is the first 15 completed `1d` bars flat by record rule (predeclared researcher choice — covers 10-bar seeding plus 5 bars of margin); no position before bar 16 may trade. No repainting (`sma`/`close` read only completed bars), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (the source names no venue at all — market choice is entirely researcher-declared, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source declares no execution timing (indicator, no order calls); this record does not claim any source fill. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive state outcomes and no stop/target legs, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no sizing, capital, commission, fee, slippage, margin, or funding text of any kind. The explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, with the single-unit/no-add/reverse-full position pin from Signal, never presented as source-native behavior.
- Concurrency: at most one unit per side under the state-following map (predeclared pin); same-state bars while positioned are no-ops; the opposite fix/flip reverses in full in one step; re-entry after a reversal needs only the next opposite fix/flip (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full 13-line construction (`//@version=3` study declaration, dead `period` + live `len` inputs at `defval=10`, `sma(high,len)` / `sma(low,len)` bands, the `na`-init ternary `Hlv` state line, the `sslDown`/`sslUp` display legs, two render-only plots, `overlay=true`). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 order calls of any kind — the sole position-changing path is the opposite fix/flip reversing the full unit. The absence of any live stop is coded absence, disclosed, not a tunable parameter here.
2. Always-in-market exposure, admitted plainly: after the first `Hlv` fix the system is never flat — a market that alternates closes beyond opposite bands flips the full unit on every flip with no confirmation, no cooldown, and no cost guard. Adverse excursion between flips has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Lag at regime births: the flip test compares the close against 10-bar averages of the extremes — a sharp V-reversal must drag both smoothers across the gap before any fix/flip prints, so entries and reversals arrive strictly after the turn by code. The lag is the coded smoother, disclosed, not shortened.
4. Dead-input fence: the `period` input is declared and read nowhere — retuning it changes nothing; the live length is `len = 10` only. A variant driven by `period` would be a different, unpinned rule — none is admitted here.
5. Source basis fenced: the source is a venue-free, timeframe-free overlay indicator rendered on an FX daily chart at read time (page chrome, not strategy fact). The derived record trades BTCUSDT `1d` perpetual instead; any divergence between the indicator's informal use elsewhere and this record's event set belongs to the predeclared derivation, and this record is therefore never evidence that any other SSL-based system passes.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the indicator-to-order state-following map (including `na → ±1` fixes as first entries), same-bar-close fills, the single-unit/no-add/reverse-full position pin, the adopted 15-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the BTCUSDT-`1d` market/frame declaration — all predeclared above; band lengths, averaging operator, the ternary state line verbatim (including `na`-init, hold-else, and long-leg priority), the `==`/`na` hold edges, and the no-stop/no-target/no-cooldown posture are source-verbatim.
7. The `10` literal, the contemporaneous (undisplaced) band reference, the state-following entry semantics (fixes enter, flips reverse), the two-sided stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning the length, displacing the bands, converting state-following into level-hold or transition-only-from-defined-state, adding a stop/target/filter/cooldown/gate, dropping the short leg, or sizing partially instead of full-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `len = 10` / contemporaneous high/low SMA bands / `na`-init ternary state / state-following entries / full-unit reversal / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Memory relevance: replacing the persistent `Hlv` state machine with a memoryless level rule (long while `close > smaHigh`, short while `close < smaLow`, flat inside the channel) must not improve net expectancy; fail ⇒ the state memory (the whipsaw filter) adds nothing over level-holding.
- F2 — Band-structure relevance: replacing the dual high/low bands with a single midline cross (`close` vs `sma(close, 10)`, long above / short below with reversal on cross) must not improve net expectancy; fail ⇒ the high/low band structure adds nothing over a midline cross.
- F3 — Parameter relevance: replacing the pinned `len = 10` with any adjacent classic length must not improve net expectancy; fail ⇒ the pinned default carries no advantage over neighboring smoothings and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (market and frame researcher-declared; the source is venue-free and timeframe-free). The high/low/close arithmetic ports across perpetual venues without structural change. The short leg requires margin-short permission (realistic on perpetual venues; a spot-only deployment cannot express the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Indicator-to-order gap: the source draws two lines and trades nothing; every order, fill, sizing, and market fact in this record is researcher-declared — a reader trusting another SSL-based system (SSL Hybrid, MTF variants, different lengths) would reconstruct a different, unpinned rule.
- Derived fill timing: same-bar-close on `1d` BTCUSDT perpetual is a researcher choice over an indicator with no execution semantics — backtest economics of any other timing differ by construction, disclosed, not hidden.
- Position-state pin: live same-side-add and reversal-quantity behavior is unspecified-by-source (no order text exists at all); the single-unit/no-add/reverse-full pin is a researcher choice, disclosed, not source-verbatim.
- Dead input: the `period` input exists only as text — a reader mistaking it for a live parameter would reconstruct nothing tradeable from it.
- No price stop, no time stop, never flat after the first fix: adverse excursion after entry has no guardrail beyond the opposite fix/flip, which may arrive many bars later or after deep excursion; alternation across opposite bands flips the full unit repeatedly. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, commission, fee, slippage, margin, or funding text ships anywhere — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue choice only: the derived venue is Binance `BTCUSDT` perpetual over a venue-free source. Microstructure, tick size, fee, and funding differences are carried by the house overlay — no equivalence is claimed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView open-source indicator page by ErwinBeckers (updated 2019-03-28): https://www.tradingview.com/script/xzIoaIJC-SSL-channel
- Pine strategy semantics (order calls, default execution, built-ins): https://www.tradingview.com/pine-script-reference/v5/
