---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Moreira-Muir 2017 volatility-managed inverse-variance long-only on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2016-04-01
sources:
  - https://www.nber.org/system/files/working_papers/w22208/w22208.pdf
  - https://doi.org/10.1111/jofi.12513
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2659431
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moreira-Muir 2017 volatility-managed inverse-variance long-only on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (NBER working-paper PDF text layer read firsthand 2026-10-13, 57 pages / ~110k characters; Semantic Scholar metadata record confirming title, authors, year, and DOI; Wiley landing confirming published citation — all three agree):

- Moreira, Alan & Muir, Tyler, `Volatility-Managed Portfolios` — NBER Working Paper No. 22208 (April 2016); published Journal of Finance, vol. 72, no. 4, 1611–1644 (August 2017). DOI `10.1111/jofi.12513`; SSRN abstract `2659431`. Canonical working-paper file: https://www.nber.org/system/files/working_papers/w22208/w22208.pdf (title page `VOLATILITY MANAGED PORTFOLIOS / Alan Moreira Tyler Muir / NBER Working Paper 22208 / April 2016`, abstract verified in-text).
- Pinned headline spec (§2.2 Portfolio formation, read verbatim from the text layer): `We construct our volatility managed portfolios by scaling an excess return by the inverse of its conditional variance. Each month our strategy increases or decreases risk exposure to the portfolio according to variation in our measure of conditional variance. The managed portfolio is then` Eq. (1) `f(sigma)_{t+1} = (c / sigma-hat^2_t(f)) f_{t+1}`, `where f_{t+1} is the buy-and-hold portfolio excess return`, `sigma-hat^2_t(f) is a proxy for the portfolio's conditional variance, and the constant c controls the average exposure of the strategy. For ease of interpretation, we choose c so that the managed portfolio has the same unconditional standard deviation as the buy-and-hold portfolio.` Motivation pin (same section): `The optimal portfolio weight is proportional to the attractiveness of the risk-return trade-off` under mean-variance, approximated `by the inverse of the conditional variance`.
- Pinned variance proxy (same section, read verbatim): `In our main results, we keep the portfolio construction even simpler by using the previous month realized variance as a proxy for the conditional variance`, Eq. (2) `sigma-hat^2_t(f) = RV^2_t(f) = (1/22) sum_{d=1..22} (f_{t+d} - mean)^2`, i.e. the demeaned variance of the past daily returns in month t (22 trading days). Real-time pin (same paragraph): `An appealing feature of this approach is that it can be easily implemented by an investor in real time and does not rely on any parameter estimation.`
- Pinned cost robustness (§3.2 Transaction costs, read verbatim): `we evaluate our volatility timing strategy for the market portfolio when including empirically realistic transaction costs` with `two strategies that cap the strategy's leverage at 1 and 1.5, respectively` — `The 1bp cost comes from Fleming et al. (2003); the 10bps comes from Frazzini et al. (2015) which assumes the investor is trading about 1% of daily volume; and the last column adds an additional 4bps to account for transaction costs increasing in high volatility episodes` calibrated on `a move in VIX from 20% to 40% which represents the 98th percentile of VIX`. Outcome pin: `the strategy survives transactions costs, even in high volatility episodes where such costs likely rise`; the break-even column backs out `the implied trading costs in basis points needed to drive our alphas to zero` — 56bps for the realized-variance market leg (Table 4 row, average absolute monthly weight change 0.73).
- Pinned no-leverage robustness (§3.3 Leverage constraints, read verbatim): `we consider our original strategy, but cap the weights to be below 1 or 1.5. Capturing a hard no-leverage constraint and a leverage of 50%, which is consistent with a standard margin requirement. Sharpe ratios do not change but of course the leverage constrained have lower alphas because risk weights are, on average, lower. Still alphas of all of these strategies are statistically significant.` Weight-distribution pin (same section): `The median weight is near 1. The 75th, 90th, and 99th percentiles are 1.6, 2.6, and 6.4.` — the capped-below-1 leg this record ports is the paper's own construction, never a researcher invention.
- Portfolio-level headline numbers fenced, never adopted here: Table 1 `The scaled market factor has an annualized alpha of 4.86% and a beta of only 0.6` (momentum leg `12.5`, market appraisal ratio `0.34`); `an overall 25% increase in the buy-and-hold Sharpe ratio`; Figure 3 `$1 in 1926` cumulative market comparison; monthly sample `1926-2015` for Mkt/SMB/HML/Mom — every cell describes the paper's equity-factor study, never a single-asset BTCUSDT derivative (see Negative evidence 1–2).
- Licence and rights: the working paper is a publicly distributed NBER working paper — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's monthly inverse-realized-variance exposure timing ported to one crypto asset as a sequential monthly-rebalanced long-only capped-1× hold — not a lossless reproduction of the paper's cross-factor volatility-managed study. Researcher-declared adaptations are exactly seven: (1) single-asset BTCUSDT Binance spot (the Mkt/SMB/HML/Mom/RMW/CMA/IA/ROE/carry cross-factor set and every portfolio-level alpha/Sharpe claim are fenced off, never carried — see Negative evidence 1); (2) long-only with the short permission explicitly unused and no cash-leg yield claim (the paper scales excess returns; this record scales a funded long position and the uninvested fraction earns nothing by record rule — see Signal/Execution); (3) the hard weight cap `min(1, .)` pinned to the paper's own §3.3 below-1 no-leverage leg, never a researcher risk overlay; (4) a causal trailing-12-calendar-month mean normalizer `c_T` replacing the paper's full-sample-matched constant `c` — the source `c` is in-sample calibrated (`same unconditional standard deviation as the buy-and-hold portfolio` can only be known after seeing the whole sample) and therefore cannot be carried into a causal record; the 12-month window is the record's single declared researcher-set window, frozen in Falsification; (5) calendar-month realized variance on the 24/7 tape with `N` = realized daily-bar count of that month (the paper's 22-trading-day divisor cannot be read on a market that never closes — the ratio form makes the divisor second-order, and the pinned convention is fixed, never re-tuned); (6) daily log close-to-close returns as the pinned return read (the paper's Eq. (2) writes daily `f` without naming log vs simple — this record pins log, disclosed here, never implied); (7) month-end-close decision with next-month-first-open fills plus an adopted thirteen-full-calendar-month warmup flat by record rule and house spot-fee treatment replacing the paper's cost-free/1bp–10bp equity accounting. Fixed 100%-equity-base fractional sizing with no leverage follows the capped construction; no stop/target/trailing exists in either the source or this record.

Pre-write dedup (2026-10-13): working-tree case-insensitive sweeps for `moreira`, `muir`, `volatility-managed`, `volatility managed`, `inverse variance`, `inverse-variance`, `realized variance`, `realized vol`, `volatility timing`, `volatility target`, `variance timing`, `managed portfolio` return no strategy record in the main tree — the only hits are prose fragments (the faber-gtaa record's own dedup sweep line recording zero hits for `moreira`/`muir`, and `no volatility targeting` disclaimers inside full-equity single-position records). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources; closed PRs carry no volatility-managed, Moreira, Muir, or variance-timing title. Closest pool records differ in mechanism class: `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` trades the sign of a 12-month cumulative return with a fixed-size 1-month hold (a past-change direction sensor — direction varies, size never does); `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` compares a price level against its own 10-month average (an average-crossing regime gate — on/off, never fractional); `bookstaber-atr-momentum-breakout-reversal-btcusdt-1d-2026-10-05.md` uses ATR only to place a reversal stop distance (a risk-distance read, never an exposure scaler); `p-signal-erf-dead-band-reversal-btcusdt-1h-2026-10-05.md` and every band/oscillator record gate entries on level crossings (entry triggers, never position fractions). No record in the pool varies position size on trailing realized variance while holding direction fixed — the variance-timing sensor class is absent.

## Economic mechanism

### Source-reported

Mean-variance timing of the risk-return trade-off, not return prediction: `Motivated by empirical evidence that volatility is highly variable, persistent, and does not predict returns, we approximate the conditional risk-return trade-off by the inverse of the conditional variance.` The paper's VAR evidence (§3.4/Figure 5): `in response to a variance shock, the conditional variance initially increases by far more than the expected return. A mean-variance investor would decrease his or her risk exposure by around 50% after a one-standard-deviation shock to the market variance.` Recession read (§3.1): `volatility for all factors tends to rise in recessions. Thus, our strategies decrease risk exposure in NBER recessions` — the managed leg mechanically de-risks into turbulence and re-levers only `as the spike in volatility receded` (all mechanism framing fenced to the paper's 1926–2015 factor sample, never adopted as a crypto claim here).

### Research interpretation

Variance-clock sizing port: the trailing realized variance is a slow clock that only the previous month's tape can set, so exposure for the coming month is fully known at the month-end close — a calm month earns the full book, a violent month earns a proportionally smaller book, and the cap binds the book at exactly 100% whenever the month was calmer than its own trailing year. There is no entry event, no exit leg, and no direction decision anywhere: the strategy is always long after warmup and the only thing that ever moves is the fraction. Unlike return-sign momentum (TSMOM-12m, Jegadeesh-Titman 6/6, Novy-Marx 12-7) the sensor is a second moment with no return arithmetic in the decision — a +40% month followed by calm prints full-size here while a −40% month followed by calm prints identically full-size; sign never enters. Unlike average-regimes (Faber GTAA) the reference is the asset's own trailing variance curve, never a price-vs-average comparison — price can sit far above its average in a dead-calm tape and print full-size here. Unlike stop-distance volatility reads (Bookstaber ATR) variance never sets a price level, only a fraction. The bet, as derived, is purely on the paper's `scale monthly returns by the inverse of their previous month's realized variance` surviving the port to BTCUSDT at monthly cadence with the paper's own no-leverage cap, never on a return, average, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (calendar-month realized variance, demeaned, log close-to-close, trailing-12M mean normalizer, hard 1× cap, monthly rebalance — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in calendar month T (month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Daily returns of month T: `r_d = ln(C_d / C_{d-1})` for every completed `1d` bar `d` dated in T, where the first bar of T reads `C_{d-1}` from the last completed bar of month T−1 (so month T contributes exactly `N_T` returns with `N_T` = number of daily bars dated in T, normally 28–31).
- Realized variance (pinned Eq. (2) port): `RV2_T = (1/N_T) sum_{d in T} (r_d - rbar_T)^2` with `rbar_T = (1/N_T) sum r_d` (demeaned sample variance, pinned `1/N` divisor).
- Normalizer (declared causal port of the paper's full-sample `c`, pinned): `c_T = (1/12) sum_{k=1..12} RV2_{T-k}` — the mean of the twelve complete calendar months before T; all twelve must exist as full months.
- Position fraction for calendar month T+1 (pinned §3.3 below-1 leg, guard spelled): `w_T = min(1, c_T / RV2_T)`; definitional guard `RV2_T <= 0 → w_T = 1` (a zero-variance month cannot print on a traded tape — the branch exists so the rule is total, never exercised). The `min(1, .)` spelling is the paper's own hard no-leverage constraint; the 12-month window is the record's one researcher-set window, frozen, never re-tuned.
- Orders (pinned): exactly one evaluation per month, executed at the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper rebalances at month beginnings with no executable fill convention, so the sequential next-open fill is declared, never implied): rebalance the spot position to `w_T` fraction of equity — buy the delta when `w_T` exceeds the carried fraction, sell the delta when below; a zero-delta month places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole exposure-changing path is the next month-end rebalance. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a violent month is ridden at the fraction set the previous month-end, in full, by construction.
- Direction: long-only always-in after warmup, derived-and-declared (`w_T > 0` on any traded tape since `c_T > 0` and `RV2_T` finite — there is no flat state in this record; the short permission is explicitly unused and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: daily `close` (return arithmetic and settlement) and `open` as fill price only. No `high`/`low` range read, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar months. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of the new month). All window inputs are completed-bar values — no provisional month-end variance is ever used.
- Warmup: thirteen full calendar months of `1d` bars before the first position (twelve months for `c_T` plus the formation month's own `RV2_T`). Bars before the first decidable month-end are position-free by record rule; no signal before the fourteenth calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot (declared port — spot is chosen deliberately so no funding leg exists to model; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's month-beginning rebalancing): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one rebalance order exists per month boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: the uninvested `(1 - w_T)` fraction earns nothing by record rule. No T-bill, stablecoin-lending, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield either.
- Sizing/capital/costs: fractional single position on a 100%-equity base at 1× with the hard cap (`w_T <= 1` — no margin concept, no leverage concept). The paper reports cost-free factor returns with 1bp–10bp equity robustness checks, so derived evaluation must carry the explicit house overlay (pinned house spot fees on each rebalance delta; no funding leg exists on spot — and this record claims no hypothetical zero funding on any venue where funding would apply). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; no pyramiding, no DCA, no cooldown (explicitly none, not invented — the monthly grid is the only state transition). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the monthly inverse-conditional-variance scaling Eq. (1) with the same-unconditional-std `c` pin, the previous-month-realized-variance proxy Eq. (2) with the 22-trading-day demeaned form, the real-time no-parameter-estimation claim, the §3.2 transaction-cost survival with the leverage-capped-at-1/1.5 legs (Table 4, break-even 56bps), the §3.3 hard no-leverage cap with unchanged Sharpe ratios and significant alphas (median weight ≈ 1; p75/p90/p99 1.6/2.6/6.4), the 1926–2015 monthly sample, and the expected-variance/1-RV robustness family. It ships zero adopted performance numbers for this record: the 4.86% market alpha, the 0.6 beta, the 12.51 momentum alpha, the 0.34 appraisal ratio, and the 25% Sharpe increase all describe the paper's equity-factor study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-factor fenced: every headline result (factor alphas, appraisal ratios, Sharpe gains, utility gains, VAR impulse responses, recession exposures, international panels) belongs to a multi-factor equity/FX study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. In-sample `c` fenced: the source constant is calibrated to match full-sample unconditional volatility — a look-ahead this record refuses; the trailing-12M mean normalizer is a declared researcher substitute with strictly less information, and any resemblance between the two normalizers' behavior is unevidenced here.
3. No crypto sample anywhere: no 1926–2015 factor evidence speaks to BTCUSDT behavior; single-asset crypto variance timing is unevidenced by the source and may differ arbitrarily. The always-in posture rides every post-warmup drawdown at whatever fraction the prior month set, with no exit by construction (a volatility explosion mid-month is absorbed in full until the next rebalance).
4. Cost silence fenced: the paper's 1bp–10bp equity cost checks describe equity-factor trading near 1% of daily volume, not crypto spot execution — derived evaluation must carry the full house spot-fee load, and this record reports no net performance of any kind.
5. Upper-tail exposure discarded: the source earns part of its result from levered weights up to 6.4× in dead-calm tapes; the §3.3 cap this record ports keeps Sharpe but lowers alpha by the paper's own account — the calm-tape upside of the unconstrained leg is deliberately left behind.
6. Researcher window: the 12-month normalizer length is a declared choice, not a source fact — a 3-month or 24-month normalizer would be a different, unpinned rule (see F2).
7. Return-read pin: log vs simple daily returns is fixed by record rule where the paper's Eq. (2) is silent; the ratio form makes the choice second-order, but replication disputes are decided against this record's pin, never patched silently.
8. Monthly latency: the grid can only resize at month boundaries on last month's variance; a fresh volatility regime is mistimed for up to a month by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: calendar-month demeaned log-return variance / trailing-12M mean normalizer / `min(1, .)` cap / month-end decision / next-open fills / single-position long-only always-in / rebalance-only changes / `1d` BTCUSDT spot are frozen.

- F1 — Variance-vs-volatility relevance: replacing the pinned `1/RV2` scaling with the paper's own `1/RV` robustness scaling (same normalizer form on standard deviations, same cap, same grid) must not improve net expectancy; fail ⇒ the squared-variance clock carries no advantage over the milder volatility clock on the same tape.
- F2 — Normalizer-window relevance: replacing the pinned 12-month mean normalizer with a 3-month mean on the identical grid must not improve net expectancy; fail ⇒ the annual smoothing is doing unacknowledged work — or the record's window choice is arbitrary leverage in disguise.
- F3 — Direction-of-timing relevance: the perverse twin sizing `w_T = min(1, RV2_T / c_T)` (more risk after violent months) on the identical grid must not outperform the pinned inverse mapping; fail ⇒ variance timing is doing negative work and the record's sensor points the wrong way.
- F4 — Sizing relevance: replacing the pinned fractional `w_T` with fixed full-size `w = 1` buy-and-hold on the identical grid must not improve net expectancy while also not raising realized volatility; fail on either clause ⇒ the variance clock is decoration — or the cap is the only thing working.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid calendar months on `1d` closes; variance-of-log-returns arithmetic with no venue-specific read). The arithmetic ports across spot venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no closes/sessions for the rule to read (month membership is the UTC calendar date of the daily bar, `N_T` is the realized bar count — deterministic on any continuously traded tape). Extension to other house-universe assets, vol-target overlays, expected-variance AR(1) forecasting per the paper's §3.5/Table 2, or holding horizons beyond one month per its Figure 6 would each be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across equity factors and FX carry; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Normalizer substitution: the source's full-sample-matched `c` is replaced by a trailing-12M mean; any mean-variance-optimality property tied to the matched constant is lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Researcher window: the 12-month normalizer length, the calendar-month grid, and the log-return read are record rules, not source facts — frozen, falsifiable, never re-tuned.
- Always-in posture: after warmup the book is never empty; the `(1 - w_T)` idle fraction earns nothing and the `w_T` fraction absorbs the month's full path — disclosed as the record's principal risk.
- Cap cost: weights that would print above 1× in dead-calm tapes are truncated by the paper's own no-leverage leg; the unconstrained upside is fenced, not carried.
- Cash without yield: the idle fraction earns nothing here while the paper's excess-return legs imply a cash benchmark — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper rebalances at month beginnings with no fill convention; this record fills next open. On gapping month boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is weeks away by construction. This is the source-faithful posture, disclosed as risk, not patched.
- Warmup cost: the first thirteen calendar months are position-free by record rule, so any textbook calm-tape print completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://www.nber.org/system/files/working_papers/w22208/w22208.pdf
- https://doi.org/10.1111/jofi.12513
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2659431
