---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: NR7 volatility-contraction price-breakout long with 10-day time exit on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-10
sources:
  - https://oxfordstrat.com/trading-strategies/price-breakout-nr7-entry/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# NR7 volatility-contraction price-breakout long with 10-day time exit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (public research page fetched over HTTPS and verified 2026-10-10):

- Oxford Capital Strategies, `Price Breakout with NR7 Pattern | Trading Strategy (Setup & Entry)`: https://oxfordstrat.com/trading-strategies/price-breakout-nr7-entry/ (page code `matlab/crabel/nr7-price-breakout/`). Developer line: Toby Crabel (setup: NR7 pattern); Laurence A. Connors, Linda B. Raschke (entry: price breakout with NR7). Cited origins: (i) Crabel, T. (1990), *Day Trading with Short Term Price Patterns and Opening Range Breakout*, Traders Press; (ii) Connors, L. A., Raschke, L. B. (1995), *Street Smarts — High Probability Short Term Trading Strategies*, M. Gordon Publishing Group. Concept: volatility cycles. Research goal: study different price entry thresholds (`Channel_Length`).
- Pinned setup (verbatim in sense): "The current daily range is narrower than the previous six days' daily ranges compared individually" (`NR_Length = 6; Default Value`; sensitivity grid `NR_Length = [1, 20]`).
- Pinned entry (verbatim in sense): "The next day after the setup, a buy stop is placed one tick above the UpperChannel[Yesterday]" (long) / "a sell stop is placed one tick below the LowerChannel[Yesterday]" (short); "The first stop that is traded is the position. The other stop is the protective stop. If both stops are triggered during the same day, we account only for one entry and one exit (no reversals) and assume the trade was a loser." Auxiliary: `UpperChannel(Channel_Length)` = highest high over `Channel_Length`; `LowerChannel(Channel_Length)` = lowest low over `Channel_Length`; tested grid `Channel_Length = [1, 30]`, Step 1.
- Pinned exit (verbatim in sense): "Time Exit: Nth day at the close" with `N = 10` fixed for this variant; "Stop Loss Exit: ATR(ATR_Length)" with `ATR_Length = 20`, `ATR_Stop = 6` ("A sell stop is placed at [Entry − ATR(ATR_Length) * ATR_Stop]" for longs). Sizing context: `Initial_Capital = $1,000,000`, `Fixed_Fractional = 1%`, 42-US-futures portfolio, 36 years of data (1980-01-01–2016-01-31), MATLAB platform; sensitivity runs at $0 and $50 round-turn commission/slippage.
- Source sensitivity summary (verbatim in sense): "(i) The NR7 pattern performs better when NR_Length ≥ 6; (ii) Once the cost of trading is applied, the pattern is not currently tradeable without some additional rules; (iii) The NR7 pattern with price breakout performs better when Channel_Length ≥ 10." Finding (ii) is adopted as negative evidence; no performance number of any kind is adopted (see Evidence).
- Licence and rights: a public research summary page — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, code, or extended prose. The out-of-print books are cited bibliographically only; every pinned literal above comes from the public page itself.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the page's NR7-setup / price-breakout-entry / N=10-time-exit / ATR(20)×6-stop construction ported to a single crypto asset with close-based fills — not a lossless reproduction of the page's 42-futures stop-order backtest. Researcher-declared adaptations are exactly six: (1) direction pin long-only (the short leg with its sell-stop/protective-stop pair is explicitly disabled, not underspecified — rationale: a two-sided perpetual deployment with 10-day holds carries unverifiable historical funding under reviewer precedent, while the long leg keeps genuine flat/no-trade days — see Execution assumptions); (2) single-asset BTCUSDT Binance perpetual (the 42-futures portfolio, the 1% fixed-fractional sizing, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (3) `Channel_Length` pinned at 10, the minimum of the source-recommended `≥ 10` range (the page tests a grid with no single default; values 11–30 are fenced, never carried — see Negative evidence 5); (4) stop-order legs converted to completed-bar close-confirmed legs (buy-stop-above-channel → enter at the close if `close` exceeds the channel; sell-stop ATR level → exit at the close if `close` breaches the level; the one-tick offset is absorbed by the strict close comparison — rationale: no intrabar-path-dependent fill is assumed anywhere in this record); (5) fixed single-position sizing replacing the 1% fixed-fractional portfolio sizing (fenced); (6) an adopted 30-bar warmup flat by record rule plus house fees/funding treatment (the page's $0/$50 cost variants are fenced — see Execution assumptions). The NR7 setup definition (`NR_Length = 6` default), the next-day breakout timing, the `N = 10` time exit, the `ATR_Length = 20` / `ATR_Stop = 6` protective level, the strict comparisons, the single-position/no-reversal posture, and the complete entry/exit/risk inventory are source-faithful.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `nr7`, `crabel`, `narrow-range`, `narrow range`, `inside bar`, `inside day`, `opening range breakout` return zero strategy records using this source, setup, or signal (the only `ORB`-letter hits pool-wide are the English words "absorb/absorbed" in unrelated prose; verified by context print). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` buys every close above the rolling 20-bar high with a 10-bar-low signal exit and no contraction precondition of any kind; `darvas-box-breakout-long-btcusdt-1d-2026-10-09.md` gates entries on a box-consolidation formation (new-high event confirmed `boxp-2` bars later with decaying short-window highs, frozen rails) with an opposite-rail exit and no time stop; `sqzmom-lb-squeeze-release-ema100-two-sided-btcusdt-1d-2026-10-09.md` keys squeeze-release off its oscillator/band construction, never off a narrowest-range-of-seven comparison. Five-axis distinction: no pool record and no open PR conditions entries on the current daily range being the narrowest of the last seven sessions, and none pairs a range-contraction gate with a fixed 10-day time exit plus an ATR-multiple protective level.

## Economic mechanism

### Source-reported

Volatility cycles: volatility contracts before it expands — an unusually quiet day (narrowest range of the last seven sessions) is a coiled spring, and the stop order means the trade is paid for only when the spring actually releases (breakout beyond the prior channel). The time exit (`N = 10`) plus the ATR-multiple stop bounds every trade's life and loss without any opposite-signal concept.

### Research interpretation

Contraction-gated breakout with a fixed lifespan, long-only. Unlike raw-extreme systems (Donchian) that buy every new N-bar high, this system buys only breakouts that emerge immediately after a 7-session range minimum — a strictly rarer, more selective entry that refuses trend legs already in motion for days. Unlike formation-gated systems (Darvas box) the gate is a pure range comparison with no level, rail, or confirmation-lag state: the setup prints on a single bar and expires the next day if the breakout close never comes. Unlike oscillator squeeze systems (SQZMOM-LB) there is no band, basis line, or momentum leg — contraction is measured in raw high-minus-low only. The bet, as derived, is purely on BTCUSDT next-day continuation after a daily-range minimum at a 10-session channel scale, never on a level hold, an oscillator reading, a calendar effect, or a funding anchor.

## Signal

Exact rule as pinned (`NR_Length = 6` / `Channel_Length = 10` / `N = 10` / `ATR_Length = 20` / `ATR_Stop = 6` — any other value is a different, unpinned rule):

- Definitions (all on completed `1d` bars): `R[t] = high[t] − low[t]` (daily range); `UC[t] = highest high over bars t−9..t` (10-bar channel high); Wilder ATR(20): `TR[t] = max(high[t] − low[t], |high[t] − close[t−1]|, |low[t] − close[t−1]|)`, RMA-smoothed with seed = SMA of the first 20 TRs (TradingView `ta.atr` convention, pinned explicitly — the page's MATLAB ATR construction detail is fenced, never claimed identical beyond the standard definition).
- Setup (pinned, strict): bar T is an NR7 setup iff `R[T] < R[T−i]` for every `i = 1..6` (compared individually — six strict inequalities; a tie on any prior bar voids the setup — pinned, no tie-break beyond this).
- Entry long (declared close-based port of the buy stop): on the single bar T+1 following a setup bar T, if `close[T+1] > UC[T]` (strict; the one-tick offset is absorbed by the strict comparison), buy 100% equity at that close (same-bar-close fill). If the comparison fails there is no trade — the conditionality essence (pay only when the spring releases) is preserved on closes. The setup expires after bar T+1: a breakout close two or more bars later is a different, unpinned event and trades nothing.
- Exits (either leg closes the full position; both equal full-close so same-bar dual-fire needs no ordering rule):
  - Time exit (pinned): close of the 10th completed `1d` bar after the entry bar (entry bar + 10 bars, `N = 10`), at that close.
  - Protective level (declared close-based port of the ATR sell stop): on any completed bar after entry (including the time-exit bar), if `close < entry_fill − 6 × ATR(20)` (ATR read on the same bar — causal, completed-bar value), close all at that close. An intrabar pierce of the level exits nothing — the close must confirm beyond it (precedent: bar-close protective semantics, explicitly not a stop order).
  - Self-exit on the entry bar is impossible by construction (`close < close − 6×ATR` is unsatisfiable for positive ATR), so the entry bar can never self-exit — disclosed, not missing.
- Risk legs (pinned posture): no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing paths are the two legs above. The absence of a target/trailing leg is the source's posture (the page ships time + ATR-stop only), disclosed, not invented.
- Direction: long-only (derived pin). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `high` (ranges, 10-bar channel), `low` (ranges, ATR true-range leg), `close` (breakout comparison, fills, protective-level comparison, ATR leg). No `open` (except as nothing — fills are closes), no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: completed daily bar, one evaluation per bar. Entry fills land on the qualifying breakout bar's own close; the protective level and the time exit are evaluated on each subsequent completed close. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: 30 completed `1d` bars flat by record rule (covers the 7-bar setup window, the 10-bar channel, and the 20-TR ATR seed with margin — mirrors the standing 30-bar record-rule precedent), reinforced by the structural guard (setup/channel/ATR are `na` until their windows fill, and strict comparisons against `na` never fire). No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the page's 42-futures test universe; no cross-venue equivalence claimed).
- Order timing (declared port of the page's next-day stop timing): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are breakout-close market entries and close-confirmed full exits — there is no same-bar dual-fire whose ordering could change economics (both exits equal full-close at the same close).
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative replacing the page's 1% fixed-fractional portfolio sizing (fenced). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-only form holds genuine flat stretches between setups, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; NR7 setups printing while positioned are ignored (no adds, no overlap, no reversal — the page's no-reversal/single-trade accounting ported to the single-position book); after any exit the next qualifying setup-plus-breakout-close may re-enter immediately (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short/protective-stop pair requires no margin-short modeling.

## Evidence

### Source-reported

The page ships the full construction adopted here: the NR7 setup definition with the `NR_Length = 6` default, the next-day channel-breakout entry with the `Channel_Length = [1, 30]` grid, the `N = 10` time exit, the `ATR(20) × 6` stop, the single-trade/no-reversal accounting, and the three sensitivity findings quoted in Provenance. It ships zero adopted performance numbers for this record: the finding that matters most — "(ii) Once the cost of trading is applied, the pattern is not currently tradeable without some additional rules" — is a non-tradeability verdict, and every chart/table number on the page belongs to the 42-futures stop-order portfolio, never to a single-asset BTCUSDT close-based derivative. This record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Portfolio claims fenced: every performance number, sensitivity surface, and rating on the page (profit factor, Sharpe, ulcer index, CAGR, drawdown, percent-profitable, commission/slippage comparisons) belongs to the 42-futures stop-order portfolio over 1980–2016 — none transfers to a single-asset BTCUSDT close-based derivative, and none is adopted. This record is never evidence that the page's portfolio passes anything.
2. Cost verdict adopted as-is: the page's own finding (ii) says the pattern with costs is "not currently tradeable without some additional rules" — this record adds no such rules and claims no net expectancy of any kind.
3. Fully exposed inside the hold: once entered, the position rides every adverse excursion until the close breaches the ATR level or the 10th bar prints — a gap-free −20% drift with closes always above the level is held to expiry by construction. This is the coded trade, disclosed, not a tunable parameter here.
4. Breakout-close strictness costs trades the stop version takes: a day whose high pierces the channel but whose close falls back inside enters nothing here while the source stop would have filled — the close filter is deliberately stricter (fewer, later fills), disclosed as the derivation's principal behavioral difference.
5. Parameter-grid boundary fenced: `NR_Length` values other than 6 and `Channel_Length` values 1–9 / 11–30 were sensitivity-tested on the page, never adopted; `Channel_Length = 10` is the minimum of the source-recommended `≥ 10` range (researcher pin among tested values, predeclared — never presented as a page default). Any neighboring-grid claim would be a different, unpinned rule.
6. ATR-convention boundary fenced: the protective level follows Wilder RMA ATR(20) seeded with the SMA of the first 20 true ranges; the page's MATLAB ATR internals are not verified identical beyond the standard definition — a replication dispute on the seed would be decided against this record's pin, never patched silently.
7. Derivation boundary fenced: the only non-page behavior is the six declared adaptations (long-only pin, single asset, `Channel_Length = 10` grid pin, close-confirmed fills, fixed sizing, warmup + house costs); the NR7 setup, next-day breakout timing, `N = 10` expiry, `ATR(20) × 6` level, strict comparisons, single-position/no-reversal posture, and the no-target/no-trailing stance are source-faithful. This record is therefore never evidence that the page's two-sided stop-order portfolio passes.
8. The NR7-gate / next-day-breakout-close / 10-bar expiry / ATR(20)×6 close-confirmed level / single-position long-only / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: widening the setup window, adding the short leg, restoring intrabar stop fills, adding a target/trailing/filter/cooldown, trading the setup bar itself, or holding past the 10th bar would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: NR7-six / Channel-10 / breakout-close entry / N=10 expiry / ATR(20)×6 close level / single-position long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Setup-length relevance: replacing the pinned NR7 (`NR_Length = 6`) setup with NR3 (narrowest of the last 3) must not improve net expectancy; fail ⇒ the 7-session contraction depth carries no advantage over the shallower gate.
- F2 — Channel-length relevance: replacing the pinned `Channel_Length = 10` with `Channel_Length = 20` must not improve net expectancy; fail ⇒ the source-recommended-range minimum adds nothing over the longer channel.
- F3 — Protective-level relevance: removing the ATR(20)×6 close-confirmed level (time-exit-only holding) must not improve net expectancy; fail ⇒ the protective leg costs more in premature exits than it saves in loss-cutting — or the record's risk pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; high/low/close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (the futures "one tick" offset of the source is absorbed by the strict close comparison — deterministic on any continuously traded tape). Extension to other house-universe assets, lookbacks, or timeframes would be a different, unpinned claim.

## Limitations

- Researcher direction pin: the page is two-sided — long-only is a researcher choice; two-sided economics (including the protective-stop pair and the both-triggered-loser accounting) would differ by construction.
- Grid pin: `Channel_Length = 10` is the minimum of the recommended range, not a page default — neighboring values are unevidenced here by construction.
- Single-asset port: the page's evidence is portfolio-level across 42 futures; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Close-confirmation lag: entries fill at the breakout close (later and at worse prices than the source stop in fast expansions) and the protective level exits a full bar later than the source stop in crashes; gap-through-level moves are exited at the post-gap close, never at the level.
- Setup expiry: a breakout close two bars after the NR7 day trades nothing — slow-release expansions are missed by record rule, disclosed, not recovered.
- Dropped cost silence: the page's cost variants are fenced — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 30 daily bars are flat by record rule, so any textbook NR7-plus-breakout completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Oxford Capital Strategies, Price Breakout with NR7 Pattern | Trading Strategy (Setup & Entry) (setup/entry spec, exit table with N=10 / ATR(20)×6, sensitivity grids and findings; verified live 2026-10-10): https://oxfordstrat.com/trading-strategies/price-breakout-nr7-entry/
- Bibliographic origins cited by the page (not independently fetched; every pinned literal comes from the page above): Crabel, T. (1990), *Day Trading with Short Term Price Patterns and Opening Range Breakout*, Traders Press; Connors, L. A., Raschke, L. B. (1995), *Street Smarts — High Probability Short Term Trading Strategies*, M. Gordon Publishing Group.
