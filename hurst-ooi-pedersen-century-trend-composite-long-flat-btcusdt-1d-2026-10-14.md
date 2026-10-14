---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Hurst-Ooi-Pedersen century multi-horizon trend composite long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2017-10-31
sources:
  - https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/AQR-JPM-Fall-2017.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hurst-Ooi-Pedersen century multi-horizon trend composite long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (AQR-hosted published PDF fetched and verified 2026-10-14, 16 pages, 2,752,830 bytes, SHA-256 `d2b96b73e6b7e90c244562822e98455c110796bc03056d12fff17fb1bf825dfa`; identity cross-checked against the journal header `THE JOURNAL OF PORTFOLIO MANAGEMENT FALL 2017 VOLUME 44, NUMBER 1` and the Portfolio Management Research listing `Vol 44 Issue 1, Fall 2017, pp. 15–29`):

- Hurst, Ooi, Pedersen, `A Century of Evidence on Trend-Following Investing`, Journal of Portfolio Management 44(1), 15–29 (Fall 2017; journal article page dated October 31, 2017 — adopted as `source_as_of` 2017-10-31). Working-paper version circulated as SSRN abstract `2993026` (posted 2017-06-28); this record pins the published JPM PDF above, never the draft.
- Pinned headline spec (Construction section, verbatim in sense): "we construct an equal-weighted combination of 1-month, 3-month, and 12-month time series momentum strategies for the 67 markets cited above — from as far back as January 1880 to December 2016. The strategy is rebalanced each month as follows. For each of the three time-series momentum strategies, the position taken in each market is determined by assessing the past excess return in that market over the relevant look-back horizon. A positive past excess return is considered an 'up' trend and leads to a long position; a negative past excess return is considered a 'down' trend and leads to a short position. Therefore, each strategy always holds either a long or short position in every market." Aggregation and sizing (same section, fenced): "Each position is sized to target the same amount of volatility … The positions across the three strategies are aggregated each month and scaled such that the combined portfolio has an annualized ex ante volatility target of 10%."
- Data universe fenced (DATA section): monthly returns for 67 markets (29 commodities, 11 equity indices, 15 bond markets, 12 currency pairs) on end-of-month prices; strategy returns run January 1880 to December 2016 (three-year volatility-estimation warmup precedes 1880). The 67-market averaging, the hand-collected 1877–1951 CBOT commodity data, the futures-roll simulation, and every portfolio-level performance claim are fenced off, never carried.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's per-market 1m/3m/12m equal-weighted sign composite ported to one crypto asset with fixed sizing and a long-flat projection — not a lossless reproduction of the paper's 67-market, vol-targeted, always-in-position long-short portfolio. Researcher-declared adaptations are exactly six: (1) direction pin long-only majority-vote (each source leg is always long-or-short per market; here a non-positive composite maps to flat and the short permission is explicitly unused — rationale: an always-in-position two-sided perpetual deployment carries unverifiable historical funding under reviewer precedent, while the long-flat form holds genuine flat months — see Execution assumptions); (2) single-asset BTCUSDT Binance perpetual (all cross-market averaging, crisis-alpha, correlation-regime, and fee/transaction-cost-simulation claims are fenced, never carried — see Negative evidence 1); (3) fixed 100%-equity single-position sizing replacing the paper's per-market ex-ante-vol targeting plus 10% portfolio scaling (rationale: one asset needs no cross-market vol aggregation; the 3-year rolling-covariance scaler is fenced, never computed); (4) total-return sign replacing the paper's excess-over-risk-free return sign (fenced; the financed-cash-index construction is never carried — see Limitations); (5) calendar-month decision grid on completed `1d` closes with next-open fills (the paper trades monthly formation/rebalance; the monthly cadence is source-native, the daily-bar mechanics are the declared port); (6) an adopted 12-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's simulated-cost/2-and-20 accounting. The 1/3/12-month horizons, the equal weighting (expressed as the sign-majority vote), the monthly rebalance, the strict sign rule, and the no-stop/no-target/no-trailing signal-only-exit posture (the paper ships no stop concept anywhere) are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `hurst`, `century` (sole hit: the word `half-century` inside the unrelated DeBondt-Thaler record), `equal-weighted combination`, `majority`, `unanim`, `1-month, 3-month`, and `hurst-ooi` return zero competing strategy records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` conditions a monthly-held position on the sign of a single 12-month formation (one horizon, no composite, no vote); `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` fires on price relative to a 10-month moving-average level, never on trailing-return signs; `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` is a pure calendar-seasonal hold with no return-conditioned leg. Five-axis distinction: no pool record and no open PR conditions a monthly-held position on the majority vote of three trailing 1/3/12-month return signs.

## Economic mechanism

### Source-reported

Multi-speed trend continuation: each market's own past 1-, 3-, and 12-month excess return predicts its next-month direction, and averaging the three horizons diversifies across trend speeds instead of betting on one formation length. The paper attributes trends to long-standing behavioral biases (anchoring, herding) plus nonprofit-seeking participants (central-bank intervention, corporate hedging) slowing information incorporation; it reports the composite "surprisingly consistent" across 137 years including the Great Depression, wars, stagflation, and the global financial crisis, with the first 10 decades framed as out-of-sample evidence relative to the literature (PERFORMANCE OVER A CENTURY section — portfolio-level claims, fenced, never adopted here).

### Research interpretation

Equal-weight sign-vote as a noise-averaging port: the 1-month leg reacts fast but whipsaws, the 12-month leg is stable but exits late, and the 3-month leg sits between — the majority vote only lets exposure trigger (or persist) when at least two speeds agree, so a single-horizon head-fake cannot trade by itself. Unlike single-horizon TSMOM (12m sign) there is no one-formation bet: the signal is the consensus of three nested trailing returns. Unlike moving-average level rules (Faber GTAA) there is no smoothing-variant or band choice: the signal is three raw price-ratio signs. Unlike calendar-seasonal holds there is no date-conditioned leg at all. The bet, as derived, is purely on multi-speed BTCUSDT return-continuation consensus at monthly cadence, never on a level, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (horizons 1/3/12 calendar months, strict signs, majority vote — any other value is a different, unpinned rule):

- Formation (pinned): at the close of the last completed `1d` bar dated in calendar month T (decision bar), compute `R1 = C_T / C_{T−1} − 1`, `R3 = C_T / C_{T−3} − 1`, `R12 = C_T / C_{T−12} − 1`, where `C_{T−k}` is the close of the last completed `1d` bar dated in calendar month T−k. Total-return signs on closes; the paper's excess-return construction is fenced by declared adaptation (4).
- Leg signs (pinned): `s(x) = +1` if `x > 0`, else `−1` (an exact-zero formation is pinned to the down leg — measure-zero on live tape, no tie semantics beyond this).
- Position target for calendar month T+1 (pinned majority vote): `s(R1) + s(R3) + s(R12) >= +1` → long (at least two of three horizons strictly positive); otherwise → flat. The short side of the paper's rule is explicitly disabled, not underspecified.
- Orders (pinned): at most one order event per month, placed for the first `1d` open of month T+1 (next-open fill after the decision bar): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next month-end composite mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a month-long adverse move is ridden in full by construction.
- Direction: long-only (derived pin). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` closes of BTCUSDT only: four month-end closes per decision (`C_T`, `C_{T−1}`, `C_{T−3}`, `C_{T−12}`; intermediate closes are never read). No `open` (except as fill price), no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar month. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of the new month). All formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: twelve full calendar months of `1d` bars before the first decision (the base close `C_{T−12}` must exist). Bars before the first decidable month-end are flat by record rule; no signal before the thirteenth month-end may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (month membership is the UTC calendar date of each daily bar — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared port of the paper's monthly rebalance): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are month-boundary market entry/close-all orders, and at most one order exists per month — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative replacing the paper's per-market vol targeting plus 10% portfolio scaling (fenced). The paper reports simulated-cost/2-and-20 performance, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-flat form holds genuine flat months between a non-positive composite and the next positive one, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next positive composite (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the full construction adopted here: equal-weighted 1/3/12-month sign composite with monthly rebalance (Construction section); always-long-or-short per market per leg with vol-targeted sizing aggregated to a 10% annualized ex-ante target (same section, sizing fenced); 67 markets over January 1880–December 2016 on end-of-month prices (DATA section). Qualitative robustness context with exact provenance, adopted as context only: each of the three horizons "delivered positive returns in each decade" (Exhibit 2 discussion, p. 16); the lagged-one-month implementation variant "also deliver[s] positive returns in most decades, but the performance naturally deteriorates with the lagging, especially for the shorter-term signals" (same paragraph); the per-market legs delivered "positive average returns in each market, with an average Sharpe ratio of approximately 0.4" (Exhibit 3 note). It ships zero adopted performance numbers for this record: every Sharpe/return/crisis-alpha/fee-net claim describes the 67-market vol-targeted portfolio, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Portfolio claims fenced: every headline number in the paper (century Sharpe, decade tables, 60/40-crisis smile, correlation-regime analysis, fee-net simulations, spot-vs-roll decomposition) belongs to the cross-asset vol-targeted portfolio — none transfers to a single-asset BTCUSDT derivative, and none is adopted. This record is never evidence that the paper's portfolio passes anything.
2. No hidden risk layer: the paper ships no stop/target/trailing concept — the sole position-closing path is the next month-end composite. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
3. Fully exposed inside the holding month: once long for month T+1, the system rides the entire adverse excursion with no guardrail — a −30% month is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
4. Excess-vs-total boundary fenced: the paper's legs use excess returns over the risk-free rate; the derivative uses total-return signs on perpetual closes. On high-volatility BTC tape at multi-month scale the signs agree far more often than not, but agreement is asserted nowhere — the difference is a declared derivation boundary, and a replication dispute on near-zero formations would be decided against this record's pin, never patched silently.
5. Majority-vote projection fenced: the source aggregates vol-scaled long/short positions across 67 markets; the derivative's per-horizon sign-majority vote is the equal-weight sign projection of that aggregation onto one asset with the short leg mapped to flat. This projection is researcher-declared (adaptations 1–3), never claimed as lossless source reproduction.
6. Formation-window indexing fenced: the paper's monthly prose labels the same completed-calendar-months-ending-at-decision windows this record pins as `C_T / C_{T−k} − 1` for k in {1, 3, 12}; any off-by-one relabeling of a window edge, any skip-month insertion, or any unanimity (3-of-3) substitution would each be a different, unpinned rule — the Signal section governs, never the prose indexing.
7. The 1/3/12 horizons / strict signs / majority vote / month-end decision / next-open / single-position long-flat / signal-only exit stance is pinned, not removed: dropping a horizon, reweighting horizons, adding vol-scaled sizing, adding a stop/target/filter/cooldown, re-enabling the short leg, trading intra-month, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1/3/12 horizons / strict signs / majority vote / month-end decision / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Composite relevance: replacing the pinned three-horizon majority vote with the single 12-month sign (the existing TSMOM shape) must not improve net expectancy; fail ⇒ the multi-speed consensus carries no advantage over the slow leg alone.
- F2 — Majority-threshold relevance: requiring unanimity (3-of-3 positive) for long must not improve net expectancy; fail ⇒ the majority pin is doing unacknowledged filtering work and the threshold choice matters.
- F3 — No-lag relevance: lagging the composite one extra month (trade at end of T+1 on the month-T signal, the paper's own lagged robustness variant) must not improve net expectancy; fail ⇒ the paper's no-lag timing adds nothing over the delayed implementation.
- F4 — Fixed-size relevance: replacing fixed 100%-equity sizing with ex-ante-vol-targeted sizing must not improve risk-adjusted expectancy; fail ⇒ the declared sizing simplification costs nothing — or the record's size pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid calendar-month on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets, horizons, or vote thresholds would be a different, unpinned claim.

## Limitations

- Researcher direction pin: the paper is always-in-position two-sided per market — long-flat majority-vote is a researcher choice; two-sided economics would differ by construction.
- Single-asset port: the paper's evidence is portfolio-level across 67 futures markets over 137 years; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Dropped vol targeting: fixed 100%-equity sizing concentrates risk in high-vol regimes where the paper would have scaled down; month-level drawdowns are therefore structurally larger than anything the paper's construction would print.
- Total-return signs: near-zero formations could flip under the paper's excess-return convention; exact-zero is decided by record rule (down leg), disclosed, not source-proven.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is weeks away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Unused cost silence: the paper reports simulated-cost/2-and-20 performance; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first twelve calendar months are flat by record rule, so any textbook composite completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Hurst, Ooi, Pedersen, A Century of Evidence on Trend-Following Investing, Journal of Portfolio Management 44(1), 15–29 (Fall 2017), AQR-hosted published PDF (verified 16 pages, 2026-10-14): https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/AQR-JPM-Fall-2017.pdf
- Bibliographic cross-check: https://www.pm-research.com/content/iijpormgmt/44/1/15 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026
