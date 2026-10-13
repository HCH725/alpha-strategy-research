---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Jegadeesh 1990 one-month reversal monthly long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1990-07-01
sources:
  - https://ideas.repec.org/a/bla/jfinan/v45y1990i3p881-98.html
  - https://econpapers.repec.org/article/blajfinan/v_3a45_3ay_3a1990_3ai_3a3_3ap_3a881-98.htm
  - https://doi.org/10.1111/j.1540-6261.1990.tb05110.x
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Jegadeesh 1990 one-month reversal monthly long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end at the bibliographic and abstract level (RePEc mirrors fetched and read 2026-10-13):

- Jegadeesh, Narasimhan, `Evidence of Predictable Behavior of Security Returns` — The Journal of Finance, vol. 45, issue 3, 881–898, July 1990. DOI `10.1111/j.1540-6261.1990.tb05110.x`; RePEc handle `RePEc:bla:jfinan:v:45:y:1990:i:3:p:881-98`. Canonical record: https://ideas.repec.org/a/bla/jfinan/v45y1990i3p881-98.html with mirror https://econpapers.repec.org/article/blajfinan/v_3a45_3ay_3a1990_3ai_3a3_3ap_3a881-98.htm (suggested citation `Jegadeesh, Narasimhan, 1990. "Evidence of Predictable Behavior of Security Returns," Journal of Finance, American Finance Association, vol. 45(3), pages 881-898, July`).
- Pinned headline spec (publisher Abstract, read verbatim on both mirrors): `The negative first-order serial correlation in monthly stock returns is highly significant.` / `significant positive serial correlation is found at longer lags, and the twelve-month serial correlation is particularly strong.` / `Using the observed systematic behavior of stock return, one-step-ahead return forecasts are made and ten portfolios are formed from the forecasts.` / `The difference between the abnormal returns on the extreme decile portfolios over the period 1934-87 is 2.49 percent per month.` Sample window 1934–87 is an abstract-level fact, adopted; no table, figure, regression, or section beyond the Abstract is cited anywhere in this record.
- Access boundary (stated on both mirrors, disclosed, not worked around): `Access to full text is restricted to JSTOR subscribers.` The full paper was therefore NOT read; every source-reported number below carries Abstract provenance, and all table/figure-level claims are omitted by rule rather than reconstructed.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's negative-first-order monthly leg ported to one crypto asset as a long-or-flat monthly contrarian hold — not a lossless reproduction of the paper's cross-sectional decile-spread study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance perpetual (the ten-portfolio cross-section, the extreme-decile spread, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (2) formation fixed to one calendar-month close-to-close simple return sign (the paper's monthly grid and one-step-ahead forecast horizon are source-native; the plain-close definition with no distributions is the declared port — BTC pays none); (3) long-flat direction mapping (the paper's long-short spread leg is fenced; the short permission is simply unused — see Signal); (4) calendar-month decision grid on completed `1d` closes with next-open fills (the paper is a forecast study and ships no executable fill convention, so the causal port is declared, never implied); (5) an adopted two-full-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's abnormal-return (cost-free) accounting; (6) fixed 100%-equity single-position sizing with no leverage (the paper sizes decile portfolios, never a single-asset book). The 1-month formation, the 1-month holding period, the sign inversion (long exactly when the formation month is negative — the negative-first-order leg, nothing else), the monthly update, and the no-stop/no-target/no-trailing posture (signal-roll exits only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `jegadeesh`, `first-order serial`, `one-month reversal`, `1-month reversal`, `monthly reversal` return zero strategy records — the only hits are this run's search prose and the TSMOM record's Jegadeesh-Titman (1993) holding-construction citation, which that record's own text scopes as a construction reference, not a strategy. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` conditions its monthly hold on the sign of the trailing 12-month cumulative return with the SAME-direction mapping (long when positive — that record's §Provenance quotes its source rule `go long the contract if positive and short if negative`) — a 12-month momentum leg, opposite sign logic and twelve times the formation of this record; `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` conditions its monthly hold on the level of price against its own 10-month average — a level comparison with no return-ratio sign anywhere; the calendar holds (`sell-in-may`, `january-barometer`, `monday-drift`, `turn-of-month-4day`, `pre-holiday-drift`, `fomc-pre-announcement-drift`, `lunar-phase-new-moon-regime`) carry no price-conditioned leg at all; the indicator mean-reversion family (`etf-3day-reversion`, `connors-rsi2`, `cumulative-rsi`, `ibs-mean-reversion`, `catching-the-bottom-rsi-dip`, `oversold-rsi`, `three-down-three-up`, `turtle-soup-donchian-fade`, `inside-bar-failure-fade`) forms on 1–5-bar oscillator, pattern-failure, or streak constructions, never on a calendar-month total-return sign. Five-axis distinction: no pool record and no open PR holds next month long-or-flat on the inverted sign of the completed calendar month's close-to-close return from a published paper's negative-first-order serial-correlation leg.

## Economic mechanism

### Source-reported

Short-horizon return predictability, not trend riding: individual-stock monthly returns exhibit highly significant negative first-order serial correlation, so a month's return systematically forecasts the opposite-signed next step — while longer lags (twelve months particularly) run the other way (Abstract — mechanism framing fenced to the paper's 1934–87 equity sample, never adopted as a crypto claim here). The paper monetizes the pattern as an extreme-decile abnormal-return spread of 2.49 percent per month (Abstract — spread-level claim, fenced, never adopted here).

### Research interpretation

Monthly contrarian-regime port: the sign of one completed calendar month admits only post-decline months as exposure permission, while the once-a-month update makes intra-month overtrading structurally impossible — the strategy can be a whole month early or late but can never chase inside the holding month. Unlike return-sign momentum (TSMOM) the mapping is inverted by construction: red formation month means exposure, green means cash. Unlike moving-average regimes (Faber) there is no average anywhere: the signal is a bare return-ratio sign. Unlike oscillator/pattern mean-reversion there is no threshold, band, streak count, or failure shape: one monthly sign, re-decided monthly, held until the next month-end re-maps it. The bet, as derived, is purely on the paper's negative-first-order leg surviving the port to BTCUSDT at monthly cadence, never on a level, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (1-month formation, strict sign inversion, monthly grid — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in calendar month T (month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Formation (pinned): `R_T = C_T / C_{T-1} − 1` (simple close-to-close return, closes only — `C_T` is the close of the last completed daily bar dated in month T; no log/simple choice left open, no dividend or distribution adjustment exists for BTC).
- Position target for calendar month T+1 (pinned, inverted sign): `R_T < 0` → long; `R_T >= 0` → flat (the equality leg is pinned to flat — measure-zero on live tape, no tie semantics beyond this; the inversion is the paper's negative-first-order leg, not a researcher pin).
- Orders (pinned): at most one order event per month, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper ships no fill convention): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next month-end signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a month-long adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the paper's spread is long-short across deciles; the short leg is fenced and the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` closes of BTCUSDT only: two month-end closes per decision (no `open` except as fill price, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar month. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of the new month). All formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: two full calendar months of `1d` bars before the first decision (both month-end closes must exist). Bars before the first decidable month-end are flat by record rule; no signal before the third calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's monthly forecast grid): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's abnormal-return accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free abnormal-return spreads, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long months carry realized funding, flat months carry none, and the form holds genuine flat months so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next negative month-end sign (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The Abstract ships every adopted construction fact: the highly significant negative first-order serial correlation in monthly returns (the inverted-sign leg), the one-step-ahead monthly forecast horizon (the 1-month formation/holding grid), the ten-portfolio forecast sort (fenced cross-section, never ported), and the structural trade facts that the extreme-decile abnormal-return spread is 2.49 percent per month over 1934–87 with the twelve-month serial correlation running positive (the momentum leg, deliberately NOT ported — the pool's TSMOM record already covers that horizon and direction). It ships zero adopted performance numbers for this record: the 2.49 percent spread describes the paper's equity decile study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (decile sorts, forecast-model portfolios, the 2.49 percent spread) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Full-text boundary: the complete paper (methods, tables, figures, robustness) sits behind JSTOR-subscriber restriction and was not read; abstract-only provenance is disclosed as this record's principal evidence ceiling — any table-level dispute is decided against this record, never patched by inference.
3. No crypto sample anywhere: no 1934–87 equity evidence speaks to BTCUSDT behavior; single-asset crypto reversal is unevidenced by the source and may differ arbitrarily. Monthly-sign reversal can underperform a roaring one-way bull tape for years by construction (flat through every green month).
4. Cost silence fenced: the paper's spread is abnormal returns, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
5. Opposing-leg admission: the same Abstract documents positive serial correlation at longer lags (twelve months particularly) — a red 1-month formation can therefore coincide with a green 12-month backdrop, and this record follows the 1-month leg unconditionally, disclosed, not hedged.
6. Forecast-model gap: the paper's one-step-ahead forecasts come from an estimated serial-correlation model across stocks, not from a bare single-asset sign rule — the bare-sign mapping is the declared derivative simplification, and any loss of the model's conditioning information is accepted, not recovered.
7. Monthly latency: the grid can only react at month-end; a mid-month reversal is ridden (or missed) to month-end by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1-month formation / strict `<0`-long-else-flat / month-end decision / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Formation-length relevance: replacing the pinned 1-month formation with a 3-month formation sign (same inversion, same grid) must not improve net expectancy; fail ⇒ the paper's first-order leg carries no advantage over the slower stability-range neighbor.
- F2 — No-skip relevance: ending the 1-month formation one month before the decision bar (skip-latest-month variant) must not improve net expectancy; fail ⇒ the paper's no-skip month-end timing adds nothing over the skipped convention.
- F3 — Direction-twin relevance: the momentum-signed twin on the identical grid (long iff `R_T >= 0`, flat otherwise) must not outperform the pinned contrarian mapping; fail ⇒ the negative-first-order leg does not survive the port and the record's inversion is doing negative work.
- F4 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid calendar-month on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Bare-sign simplification: the paper forecasts from an estimated serial-correlation model; this record trades the bare formation-month sign. Any conditioning information in the paper's model is discarded by declared derivation, not silently carried.
- Cash without yield: flat months earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper is a forecast study with no fill convention; this record fills next open. On gapping month boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is weeks away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Monthly latency: the grid can only react at month-end; a mid-month regime break is ridden to month-end by construction — pinned, not recovered.
- Warmup cost: the first two calendar months are flat by record rule, so any textbook reversal completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Jegadeesh, Narasimhan, Evidence of Predictable Behavior of Security Returns (The Journal of Finance, vol. 45(3), 881–898, July 1990 — RePEc/IDEAS canonical record with full publisher Abstract, verified 2026-10-13; full text restricted to JSTOR subscribers, not accessed): https://ideas.repec.org/a/bla/jfinan/v45y1990i3p881-98.html
- EconPapers mirror (bibliographic cross-check, RePEc handle `RePEc:bla:jfinan:v:45:y:1990:i:3:p:881-98`): https://econpapers.repec.org/article/blajfinan/v_3a45_3ay_3a1990_3ai_3a3_3ap_3a881-98.htm
- DOI landing (source identity): https://doi.org/10.1111/j.1540-6261.1990.tb05110.x
