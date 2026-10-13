---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Gervais-Kaniel-Mingelgrin 2001 high-volume return premium 50-day-max 20-day-hold long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2001-06-01
sources:
  - https://doi.org/10.1111/0022-1082.00349
  - https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00349/abstract
  - https://sites.duke.edu/sgervais/research/gervais-kaniel-mingelgrin-2001/
  - https://ideas.repec.org/a/bla/jfinan/v56y2001i3p877-919.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gervais-Kaniel-Mingelgrin 2001 high-volume return premium 50-day-max 20-day-hold long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata plus publisher abstract landing, author page, and RePEc record, all read 2026-10-14):

- Gervais, Simon & Kaniel, Ron & Mingelgrin, Dan H., `The High-Volume Return Premium` — Journal of Finance, vol. 56, no. 3, 877–919 (June 2001). DOI `10.1111/0022-1082.00349`. Crossref record pins title `The High‐Volume Return Premium`, container `The Journal of Finance`, volume `56`, issue `3`, pages `877-919`, authors Gervais / Kaniel / Mingelgrin, print publication June 2001.
- Pinned headline spec (publisher abstract landing, read verbatim): `The idea that extreme trading activity contains information about the future evolution of stock prices is investigated. We find that stocks experiencing unusually high (low) trading volume over a day or a week tend to appreciate (depreciate) over the course of the following month. We argue that this high-volume return premium is consistent with the idea that shocks in the trading activity of a stock affect its visibility, and in turn the subsequent demand and price for that stock. Return autocorrelations, firm announcements, market risk, and liquidity do not seem to explain our results.`
- Bibliographic corroboration (author page and RePEc, disclosed as corroboration only): Duke author page cites `Gervais, Simon, Ron Kaniel, and Dan Mingelgrin, 2001, "The High-Volume Return Premium," Journal of Finance 56, 877–919`; RePEc pins `Journal of Finance, American Finance Association, vol. 56(3), pages 877-919, June` with the same DOI. No table, figure, or section number is cited anywhere in this record.
- Access boundary (disclosed, not worked around): the publisher full text and JSTOR page sit behind subscription/access walls; abstract-level and bibliographic facts above are the entire adopted source evidence. No full-text table cell, decile cut, t-statistic, alpha, formation threshold, or holding-day count beyond the quoted `day or week` / `following month` phrasing is adopted anywhere in this record. Any construction dispute beyond the quoted abstract phrasing is decided against this record, never patched by inference.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's high-volume continuation leg ported to one crypto asset as a volume-shock-event-gated 20-trading-day long-or-flat hold — not a lossless reproduction of the paper's cross-sectional equity study. Researcher-declared adaptations are exactly seven: (1) single-asset BTCUSDT Binance venue (the equity cross-section, every decile sort, every winner-minus-loser spread, and every return/alpha/t-statistic claim are fenced off, never carried — see Negative evidence 1); (2) volume-shock proxy: a strict trailing-50-trading-day volume maximum replaces the paper's `unusually high` sorts — the central declared invention, with the paper's exact cutoff fenced, never read (see Signal and Limitations); (3) formation pinned to the 1-day event only (the paper allows `over a day or a week`; the week-formation variant is fenced, never read); (4) holding pinned to twenty trading daily bars as the executable port of the paper's `following month` (calendar-month vs 20-bar mapping declared here, never implied); (5) long-flat direction mapping on the high-volume event only (the paper's low-volume depreciate leg and any short are fenced — see Signal); (6) sequential non-overlapping 20-bar sleeves with ignore-while-holding (the paper holds monthly cross-sectional portfolios; any overlapping/event-time diversification property is fenced — see Limitations); (7) a fifty-bar warmup flat by record rule, next-open fills, fixed 100%-equity single-position 1× sizing, and house fees/funding treatment replacing the paper's cost-free equity accounting, with the 20-bar timer as the sole position-closing path (no stop/target/trailing/opposite exit — explicitly none).

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `gervais`, `kaniel`, `mingelgrin`, `high-volume`, `high_volume`, `volume-premium`, `volume_premium` return no strategy record in the main tree. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: the volume-oscillator family (`obv-ema-crossover`, `pvo-signal-cross`, `mfi-threshold-divergence`, `cmf-velocity-zero-cross`, `chaikin-oscillator`, `ease-of-movement-14-zero-cross`, `force-index-100-zero-state`, `klinger-volume-oscillator`, `alma-cross-volume-gate`, `percent-b-mfi-dual-thrust`) all trade oscillator-level cross/recross/state rules evaluated bar by bar with signal/opposite exits (this record trades no oscillator, no level, and no cross anywhere — one strict 50-bar volume-maximum event opening one fixed 20-bar time-held sleeve closed only by timer expiry); `bll-trb-200-percent-band-fixed-10d` holds a fixed 10-day sleeve like this record but its event is a price breakout above a 200-day close extremum with a percent band (price-level breakout, no volume read anywhere); `turtle-soup-donchian-fade` and `nr7-price-breakout` are price-range events with bracket exits (no volume gate, no fixed time exit); the momentum formation family (`jegadeesh-titman-6m-6m`, `novy-marx-12-7`, `tsmom-12m`, `liu-tsyvinski-1w`, `cooper-gutierrez-hameed`, `debondt-thaler-36m`) reads price returns over multi-month windows (no volume input anywhere); the calendar holds carry no volume-conditioned leg.

## Economic mechanism

### Source-reported

Visibility-driven continuation, not reversal: `extreme trading activity contains information about the future evolution of stock prices` — stocks with `unusually high (low) trading volume over a day or a week tend to appreciate (depreciate) over the course of the following month`, because `shocks in the trading activity of a stock affect its visibility, and in turn the subsequent demand and price for that stock`. `Return autocorrelations, firm announcements, market risk, and liquidity do not seem to explain` the premium. (All mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here.)

### Research interpretation

Volume-shock attention sensor: one violent print of participation — the single largest daily volume in fifty trading days — acts as the visibility shock the paper describes, arming exactly one twenty-bar drift sleeve while every ordinary-volume bar prints flat. Unlike oscillator volume rules the book never reads a level, a cross, or a divergence — chop with elevated-but-not-record volume holds nothing. Unlike price momentum the trigger carries no return sign: a record-volume down day still arms the same long sleeve, because the ported bet is on post-shock visibility demand, never on direction continuation. Unlike breakout holds the event is a volume extremum, never a price extremum — a slow grinding rally on thin prints holds nothing for months. The bet, as derived, is purely on the paper's high-volume leg surviving the port to BTCUSDT at daily cadence with a strict 50-day-maximum proxy standing in for `unusually high`, never on a price level, band, return sign, calendar season, or funding anchor.

## Signal

Exact rule as pinned (strict 50-bar volume maximum, 1-day event only, 20-bar fixed hold, ignore-while-holding, next-open fills, long-flat — any other value is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. Bar membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape. One evaluation per bar close, in bar-close order.
- Volume definition (pinned): `V_t` is the base-asset volume printed on the completed daily bar `t` (not quote volume, not turnover, not detrended, not normalized — the raw candle volume field, so the rule is a pure OHLCV read with no external input).
- Event (pinned): `E_t = true` iff all of the following hold, else false: (a) at least fifty completed daily bars exist through `t` inclusive (warmup satisfied); (b) all fifty volumes `V_{t-49}..V_t` are present and strictly greater than zero (any missing or non-positive volume forces `E_t = false` — the zero-guard, pinned, not a parameter); (c) `V_t` is strictly greater than every one of the prior forty-nine (`V_t > max(V_{t-49}..V_{t-1})` — strict inequality; ties pin to false, so there is no tie semantics beyond this; the paper's exact `unusually high` cutoff is fenced, never read).
- Position target (pinned): a true event at close `t` while flat arms a twenty-trading-bar long sleeve covering bars `t+1..t+20` inclusive. While a sleeve is active (bars remaining > 0), every new event is ignored — no extension, no add, no re-trigger, no pyramiding (ignore-while-holding is pinned, never a choice at runtime). When the twentieth holding bar closes, the sleeve expires: the close of bar `t+20` is evaluated fresh as `E_{t+20}` under the same definition — true starts a new twenty-bar sleeve at the next open, false reverts the target to flat. There is no second decision inside the sleeve for any reason including large adverse excursion.
- Orders (pinned): at most one order event per bar boundary, placed for the next bar's open (next-open fill after the decision bar — the declared causal port; the paper forms monthly portfolios with no executable fill convention, so the sequential next-open fill is declared, never implied): flat→long target buys 100% equity at the next open; long→flat target closes all at the next open; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials. At most one order exists per bar open, so there is no same-bar dual-fire to sequence.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing concept for the premium leg — the sole position-closing path is the twenty-bar timer expiry mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no opposite-signal exit, no calendar exit; a fully ridden post-shock slide is absorbed exactly as printed by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: `open` as fill price only, `close` as fill-reference only, base-asset `volume` as the sole signal input (no `high`, no `low`, no quote volume, no turnover, no detrended/normalized volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on the next daily bar's open. All event inputs are completed-bar volumes — no provisional intrabar volume is ever used.
- Warmup: fifty full daily bars before the first decision (all fifty volumes must exist and be positive). Bars before the first decidable close are flat by record rule; no signal before the fifty-first bar's open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's month-formation starts): completed-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per bar boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long bars carry realized funding, flat bars carry none, and the form holds genuine flat stretches so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after expiry needs only a fresh strict-50-bar-maximum event on the expiry close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping sleeves (the paper's monthly portfolio construction is replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the extreme-activity information claim, the `unusually high (low)` day-or-week formation phrasing, the `following month` holding phrasing, the visibility→demand→price mechanism, and the autocorrelation/announcement/market-risk/liquidity non-explanation. It ships zero adopted performance numbers for this record: every return spread, alpha, and t-statistic in the paper describes its equity cross-sectional study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (volume sorts, high-minus-low spreads, visibility tests, autocorrelation/announcement/risk/liquidity spanning) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Full-text access boundary: the publisher full text sits behind subscription restrictions and was not taken from the publisher; abstract-level and bibliographic facts are this record's evidence ceiling — any table-level dispute beyond the quoted abstract phrasing is decided against this record, never patched by inference.
3. Volume-proxy admission: the paper's `unusually high` is a cross-sectional sort concept; this record feeds a strict single-asset trailing-50-day maximum into the same words. Any breadth, ranking, detrending, turnover-scaling, or low-volume-leg property of the true sort is discarded by declared derivation, not silently carried.
4. Day-pinned formation: the paper allows `a day or a week`; this record pins the 1-day maximum event only. Any diversification, smoothing, or persistence property of the week formation is discarded by declared derivation, not carried.
5. Month-to-20-bar port: the paper's `following month` is a calendar-month equity concept; this record holds twenty trading daily bars on a 24/7 tape. Any month-boundary, holiday-calendar, or trading-day-count property of the source holding is discarded by declared derivation, not carried.
6. No crypto sample anywhere: no equity evidence speaks to BTCUSDT behavior; single-asset crypto post-volume drift is unevidenced by the source and may differ arbitrarily — including inverting (record-volume capitulation continuing down for the full twenty bars). A fully ridden post-shock slide is a live possibility by construction.
7. Cost silence fenced: the paper's spreads are cost-free returns, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
8. Overlap admission: the source holds monthly cross-sectional portfolios while this record holds one sequential sleeve with ignore-while-holding — a declared material timing change; any turnover, smoothing, or diversification property of the portfolio construction is discarded, not carried.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: strict 50-bar volume maximum / base-asset raw volume / zero-guard flat / 1-day event only / 20-bar fixed hold / ignore-while-holding / bar-close decision / next-open fills / single-position sequential long-flat / timer-only exit / `1d` BTCUSDT are frozen.

- F1 — Event-gate relevance: an always-long 20-bar-cycling twin (identical 20-bar sleeves chained with no volume gate, same grid and fills) must not improve net expectancy; fail ⇒ the 50-day-maximum volume gate carries no advantage over unconditional time-cycling on the same tape.
- F2 — Lookback relevance: a 20-bar-maximum twin under the identical 20-bar hold (same event definition on a 20-bar window, same ignore-while-holding, same grid) must not improve net expectancy; fail ⇒ the fifty-bar window carries no advantage over the twenty-bar window under the same hold.
- F3 — Hold-length relevance: a 10-bar-hold twin under the identical 50-bar-maximum event (same event, same ignore-while-holding, same grid, expiry re-evaluated at 10 bars) must not improve net expectancy; fail ⇒ the following-month-length read carries no advantage over the half-length hold.
- F4 — High-vs-low asymmetry relevance: the mirror low-volume twin (long iff the bar prints a strict 50-bar volume minimum under the identical 20-bar hold, flat otherwise) must not outperform the pinned high-volume mapping; fail ⇒ the paper's high-appreciates/low-depreciates asymmetry inverts on this tape and the event points the wrong way.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid daily-bar closes on `1d` base-asset volume; fills at next-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (trading days are daily bars — deterministic on any continuously traded tape). Extension to other house-universe assets, other volume windows, or other holding lengths would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Volume-proxy invention: the strict 50-day maximum is a researcher-declared stand-in for `unusually high`; any ranking, detrending, or turnover information in the paper's sort is lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Sequential-holding deviation: the source's monthly portfolios are replaced by one sequential sleeve with ignore-while-holding; turnover smoothing and cohort diversification are lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Bare-event simplification: the paper studies high-vs-low volume spreads; this record trades only the high-volume event long-or-flat. Any distributional information in the paper's spread is discarded by declared derivation, not silently carried.
- Cash without yield: flat stretches earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper starts monthly portfolios with no fill convention; this record fills next open. On gapping bar boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-sleeve exit: adverse excursion inside the twenty-bar sleeve has no guardrail; the next decision is at timer expiry by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Warmup cost: the first fifty daily bars are flat by record rule, so any textbook volume shock completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` base-asset volume, next-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Gervais, Simon & Kaniel, Ron & Mingelgrin, Dan H. (2001). The High-Volume Return Premium. Journal of Finance 56(3), 877–919. https://doi.org/10.1111/0022-1082.00349 (Crossref-verified 2026-10-14; publisher abstract https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00349/abstract; author page https://sites.duke.edu/sgervais/research/gervais-kaniel-mingelgrin-2001/; RePEc https://ideas.repec.org/a/bla/jfinan/v56y2001i3p877-919.html)
