---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TSMOM 12-month sign monthly long-flat on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2012-01-01
sources:
  - https://w4.stern.nyu.edu/facdir/lpederse/papers/TimeSeriesMomentum.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TSMOM 12-month sign monthly long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (author-hosted final PDF fetched and verified 2026-10-10, 23 pages):

- Moskowitz, Ooi, Pedersen, `Time Series Momentum`, Journal of Financial Economics 104(2), 228–250 (2012), doi `10.1016/j.jfineco.2011.11.003` (article history: received 2010-08-16, accepted 2011-08-12, available online 2011-12-11 — adopted as `source_as_of` 2012-01-01). Canonical file: https://w4.stern.nyu.edu/facdir/lpederse/papers/TimeSeriesMomentum.pdf (NYU Stern author page mirror of the published paper; identical title/authors/journal/DOI block verified in-text). Bibliographic cross-check: https://ideas.repec.org/a/eee/jfinec/v104y2012i2p228-250.html.
- Pinned headline spec (§3.2 → §4, verbatim in sense): "the 12-month time series momentum strategy with a 1-month holding period (e.g., k=12 and h=1), which we refer to simply as TSMOM." Formation/holding grid (§3.2): "For each instrument s and month t, we consider whether the excess return over the past k months is positive or negative and go long the contract if positive and short if negative, holding the position for h months." Overlapping-hold construction follows Jegadeesh and Titman (1993): for h=1 the month-t position rests on the sign of the past return ending at t−1, and the pooled regressions (§3.1, Fig.1 Panels A–C, Table 2 Panel A cell (12,1) t = 6.61, the row maximum) motivate the k=12 choice.
- Sizing/vol legs verified and fenced (§2.4 + §3.2): position size "inversely proportional to the instrument's ex ante volatility, 1/σ", σ from exponentially weighted lagged squared daily returns with weight center of mass 60 days, "the volatility estimates at time t−1 applied to time-t returns" (no look-ahead). Dropped by predeclared adaptation, never carried (see Derived-record declaration).
- No immutable GitHub mirror is claimed; provenance rests on the author-hosted published-paper PDF, an eligible public source. Licence and rights: the paper is a published Elsevier journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's single-instrument TSMOM(12,1) long leg ported to one crypto asset with fixed sizing — not a lossless reproduction of the paper's diversified 58-futures portfolio. Researcher-declared adaptations are exactly six: (1) direction pin long-only (source-native goes short on negative formation; here a non-positive formation maps to flat — rationale: an always-in-position two-sided perpetual deployment carries unverifiable historical funding under reviewer precedent #20, while the long-flat form has genuine flat months — see Execution assumptions); (2) single-asset BTCUSDT Binance perpetual (the 58-instrument cross-asset averaging `rTSMOM`, the speculator/hedger CFTC analysis, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (3) fixed 100%-equity single-position sizing replacing the paper's monthly 1/σ ex-ante-vol targeting (rationale: one asset needs no cross-asset vol aggregation; the EW-60-day vol model of §2.4 is fenced, never computed); (4) total-return sign replacing the paper's excess-over-T-bill return sign (fenced; the T-bill/excess-return futures construction of §2.1 is never carried — see Limitations); (5) calendar-month decision grid on completed `1d` closes with next-open fills (the paper trades monthly futures formation/holding; the monthly cadence is source-native, the daily-bar mechanics are the declared port); (6) an adopted 12-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's pre-cost excess-return accounting (the paper reports gross-of-cost strategy returns; see Execution assumptions). The k=12 formation, the h=1 holding, the strict sign rule, the month-end decision point, and the no-stop/no-target/no-trailing posture (the paper ships no stop concept anywhere — exits are signal-driven only) are source-faithful.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `tsmom`, `time.series.momentum`, `moskowitz`, `ooi`, `pedersen` return zero strategy records (the only `12-month` hits pool-wide are passing window mentions in the EMA-20/50 and Donchian records, never a formation rule). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `golden-cross-sma-regime-gated-long-btcusdt-1h-2026-10-08.md` fires on a fast/slow moving-average cross, never on a trailing-return sign; `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08.md` chains three lower highs AND lower lows under an EMA5 gate, never a 12-month return sign; `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` keys off consecutive daily close direction, never a multi-month formation; `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` and `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` are pure calendar-seasonal holds with no return-conditioned leg. Five-axis distinction: no pool record and no open PR conditions a monthly-held position on the sign of the trailing 12-month return.

## Economic mechanism

### Source-reported

Single-asset return continuation: a security's own past 12-month excess return predicts the next month's direction (positive auto-covariance drives the effect, §3.1 decomposition), consistent with initial under-reaction followed by delayed over-reaction; the sign-only construction (§3.1 eq.3, §3.2) is the paper's deliberately simplest tradable expression of that predictability, and the diversified TSMOM portfolio "delivers substantial abnormal returns with little exposure to standard asset pricing factors and performs best during extreme markets" (Abstract — portfolio-level claim, fenced, never adopted here).

### Research interpretation

Slow month-cadence trend-following port: the 12-month formation acts as a low-pass filter that only lets persistent multi-quarter drift trigger exposure, while the monthly hold with no intra-month trading makes whipsaws structurally impossible inside the holding month — the strategy can be wrong for a whole month but can never overtrade one. Unlike moving-average crosses (Golden Cross) there is no smoothing-variant or length-pair choice: the signal is the raw 12-month price ratio sign. Unlike streak/chain patterns (Three-Down, ETF-3day) the formation window is twelve times longer and the holding period is fixed at one month regardless of what the tape prints mid-month. The bet, as derived, is purely on BTCUSDT 12-month return-continuation at monthly cadence, never on a level, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (k=12 calendar months, h=1 calendar month, strict sign — any other value is a different, unpinned rule):

- Formation (pinned): at the close of the last completed `1d` bar dated in calendar month T (decision bar), compute `R_T = C_T / C_{T−12} − 1`, where `C_T` is that bar's close and `C_{T−12}` is the close of the last completed `1d` bar dated in calendar month T−12. Total-return sign on closes; the paper's T-bill-excess construction is fenced by declared adaptation (4).
- Position target for calendar month T+1 (pinned, strict): `R_T > 0` → long; `R_T <= 0` → flat (the equality leg is pinned to flat — measure-zero on live tape, no tie semantics beyond this). The short side of the paper's rule is explicitly disabled, not underspecified.
- Orders (pinned): at most one order event per month, placed for the first `1d` open of month T+1 (next-open fill after the decision bar): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next month-end signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a month-long adverse move is ridden in full by construction.
- Direction: long-only (derived pin). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` closes of BTCUSDT only: thirteen month-end closes per decision (`C_T` plus the `C_{T−12}` base; intermediate closes are never read). No `open` (except as fill price), no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar month. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of the new month). All formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: twelve full calendar months of `1d` bars before the first decision (the base close `C_{T−12}` must exist). Bars before the first decidable month-end are flat by record rule; no signal before the thirteenth month-end may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (month membership is the UTC calendar date of each daily bar — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared port of the paper's monthly cadence): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are month-boundary market entry/close-all orders, and at most one order exists per month — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative replacing the paper's monthly 1/σ vol targeting (fenced §2.4 model). The paper reports pre-cost excess returns, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-flat form holds genuine flat months between a non-positive signal and the next positive one, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next positive month-end signal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the full construction adopted here: sign of the past k-month return → long/short, hold h months (§3.2); the headline pin k=12/h=1 "which we refer to simply as TSMOM" (§4 lead); monthly 1/σ sizing with the t−1 vol estimate (§3.2 + §2.4, fenced); the (12,1) cell carrying the strongest all-asset alpha t-statistic (6.61, Table 2 Panel A). It ships zero adopted performance numbers for this record: the Sharpe>1/diversified-portfolio/speculator claims describe the 58-instrument portfolio, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Portfolio claims fenced: every headline number in the paper (diversified Sharpe, alphas, factor regressions, speculator/hedger VAR, spot-vs-roll decomposition, far-contract robustness) belongs to the cross-asset portfolio or to futures-market microstructure analysis — none transfers to a single-asset BTCUSDT derivative, and none is adopted. This record is never evidence that the paper's portfolio passes anything.
2. No hidden risk layer: the paper ships no stop/target/trailing concept — the sole position-closing path is the next month-end signal. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
3. Fully exposed inside the holding month: once long for month T+1, the system rides the entire adverse excursion with no guardrail — a −30% month is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
4. Excess-vs-total boundary fenced: the paper's signal uses excess returns over T-bill on futures; the derivative uses total-return sign on perpetual closes. On high-volatility BTC tape at 12-month scale the signs agree far more often than not, but agreement is asserted nowhere — the difference is a declared derivation boundary, and a replication dispute on near-zero formations would be decided against this record's pin, never patched silently.
5. Formation-window indexing fenced: the paper's J&T-style prose ("past return from t−k−1 to t−1") labels the same 12-completed-months-ending-at-decision window this record pins as `C_T / C_{T−12} − 1`; any off-by-one relabeling of the far window edge would be a different, unpinned rule — the calendar-month definition in Signal governs, never the prose indexing.
6. Derivation boundary fenced: the only non-paper behavior is the six declared adaptations (long-only pin, single asset, fixed sizing, total-return sign, daily-bar monthly grid, warmup + house costs); k=12, h=1, the strict sign rule, month-end cadence, and the no-stop/signal-only-exit posture are source-faithful. This record is therefore never evidence that the paper's two-sided vol-targeted portfolio passes.
7. The k=12 / h=1 / strict-sign / month-end-decision / next-open / single-position long-flat / signal-only-exit stance is pinned, not removed: shortening the formation, adding the skip-month, vol-scaling size, adding a stop/target/filter/cooldown, re-enabling the short leg, trading intra-month, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: k=12 / h=1 / strict sign / month-end decision / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Formation-length relevance: replacing the pinned k=12 with k=6 must not improve net expectancy; fail ⇒ the 12-month low-pass carries no advantage over the faster formation.
- F2 — No-skip relevance: inserting the classic cross-sectional skip (formation ending one month before decision, 12-1 style) must not improve net expectancy; fail ⇒ the paper's no-skip timing adds nothing over the skipped convention.
- F3 — Fixed-size relevance: replacing fixed 100%-equity sizing with monthly 1/σ vol-targeted sizing must not improve risk-adjusted expectancy; fail ⇒ the declared sizing simplification costs nothing — or the record's size pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid calendar-month on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Researcher direction pin: the paper is two-sided — long-flat is a researcher choice; two-sided economics would differ by construction.
- Single-asset port: the paper's evidence is portfolio-level across 58 futures; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Dropped vol targeting: fixed 100%-equity sizing concentrates risk in high-vol regimes where the paper would have scaled down; month-level drawdowns are therefore structurally larger than anything the paper's construction would print.
- Total-return sign: near-zero formations could flip under the paper's excess-return convention; ties and near-ties are decided by record rule (flat at exactly zero), disclosed, not source-proven.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is weeks away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Unused cost silence: the paper reports pre-cost excess returns; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first twelve calendar months are flat by record rule, so any textbook 12-month formation completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Moskowitz, Ooi, Pedersen, Time Series Momentum, Journal of Financial Economics 104(2), 228–250 (2012), author-hosted final PDF (verified 23 pages, 2026-10-10): https://w4.stern.nyu.edu/facdir/lpederse/papers/TimeSeriesMomentum.pdf
- Bibliographic record (DOI 10.1016/j.jfineco.2011.11.003): https://ideas.repec.org/a/eee/jfinec/v104y2012i2p228-250.html
