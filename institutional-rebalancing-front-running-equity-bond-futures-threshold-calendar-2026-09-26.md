---
schema: strategy-research-record-v1
title: "Front-Running Institutional Rebalancers: Threshold/Calendar 60-40 Weight-Deviation Signals Timed Across S&P 500 vs 10-Year Treasury Futures (NBER WP 33554)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-asset
  - equity-bond
  - futures
  - institutional-flow
  - price-pressure
  - rebalancing
  - calendar-effect
  - front-running
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-01-14
sources:
  - "Campbell R. Harvey, Michele G. Mazzoleni, Alessandro Melone, 'The Unintended Consequences of Rebalancing', NBER Working Paper No. 33554, Issue Date March 2025, Revision Date January 2026. https://www.nber.org/papers/w33554"
  - "https://doi.org/10.3386/w33554 (NBER DOI; resolves to the working-paper landing)"
  - "https://www.nber.org/system/files/working_papers/w33554/w33554.pdf (pinned primary PDF read end-to-end for this record: 76 pages, 667,944 bytes, SHA-256 adb7ad35d5a5bdc18f6f75801132391331e33711c19ce944f569b0a9d345e158, retrieved 2026-09-26)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Front-Running Institutional Rebalancers: Threshold/Calendar 60-40 Weight-Deviation Signals Timed Across S&P 500 vs 10-Year Treasury Futures (NBER WP 33554)

## Provenance

- **Primary-source author(s), exactly as source:** **Campbell R. Harvey** (Duke University, Fuqua School of Business, and NBER), **Michele G. Mazzoleni** (Capital Group), **Alessandro Melone** (The Ohio State University) — affiliations as printed in the byline block of the PDF. Author order as printed on the NBER PDF cover and confirmed by the NBER landing-page `citation_author` meta tags (`Campbell R. Harvey`, `Michele G. Mazzoleni`, `Alessandro Melone`); the copyright line reads "© 2025 by Campbell R. Harvey, Michele G. Mazzoleni, and Alessandro Melone" — no other authors appear anywhere in the pinned PDF.
- **Paper title:** *The Unintended Consequences of Rebalancing*.
- **Version / date (primary-source checksum):** NBER **Working Paper 33554**; PDF cover reads **"March 2025, Revised January 2026"**; NBER landing page `Issue Date: March 2025`, `Revision Date: January 2026`, `citation_date 2025/03/10`, DOI `10.3386/w33554` (all read directly on 2026-09-26). SSRN citation line inside the search-visible metadata of the Fisher/Dice mirror gives "Date Written: January 14, 2026" — used here only as the `source_as_of` date.
- **Publication status:** **working paper, not peer reviewed.** The PDF cover states verbatim: "NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications." The acknowledgements list presentation at the AFA 2026 Annual Meeting, NBER Asset Pricing Spring 2025 Meeting, CEPR Paris Symposium 2025, SFS Cavalcade 2025, Red Rock Finance Conference 2025 and other venues — conference presentation is not peer review.
- **Version landscape (recorded, not smoothed):** public search metadata on 2026-09-26 shows **two SSRN mirrors** — `abstract_id=5122748` (Fisher College of Business WP 2025-03-001 / Charles A. Dice Center WP 2025-01, "Last revised: 15 Jan 2026", 76 pp.) and `abstract_id=5172097` (NBER WP mirror, "Last revised: 8 Mar 2026", 76 pp.) — plus an American Finance Association PDF version dated **December 15, 2025**. **None of those mirrors was opened directly this run** (SSRN sits behind Cloudflare for non-browser clients), so **every number in this record is taken solely from the pinned NBER PDF (revised January 2026)**; cross-mirror numeric equivalence is a `data gap`.
- **Primary-source inspection for this record:** the NBER PDF was downloaded directly and its full 76-page text extracted and read (pypdf page-by-page plus a whole-document pass). Read in full: Abstract, Introduction, §1.1–§1.3, §2.1.1–§2.1.3, §2.2, §2.3, §3.1–§3.5, **§4 Front-Running Rebalancers**, §5, §6, Internet Appendix A (data sources), **Internet Appendix B (signal construction, Eqs. B.1–B.2)**, Appendix C (Tables C.1–C.2), Appendix D figure/table captions, and Tables 1–6 with their notes. The **transaction-cost treatment was checked specifically in §4, §2.1.1, §5 and Appendix A–B** (see *Execution assumptions* and *Evidence*).
- **Sample / data as-of:** main sample **daily, 1997-09-10 to 2023-03-17** (6,226 observations; start = first date of E-mini S&P 500 price data, Internet Appendix A). Long-sample check runs **1961-06-16 to 2023-03-17** (Table 4, 15,291 obs.). A footnote in §3.4 states the authors "extended the sample through 2025 and find that the results become even stronger" — the extended numbers are **not tabulated** (`data gap`).
- **Universe / instruments:** E-mini S&P 500 futures (ES) and 10-year U.S. Treasury note futures (TY), continuous series built from Bloomberg excess-return price indices of the first- and second-nearest contracts (ES1/ES2, TY1/TY2), rolling from the front to the second contract at the end of the month preceding the contract's expiry month (Internet Appendix A). Long-sample replication instead uses Kenneth French daily U.S. equity total returns plus Gürkaynak–Sack–Wright 10-year Treasury total returns (Table 4 note).
- **Repository deduplication audit (2026-09-26, deterministic, before writing):** ripgrep across the **entire repository — 2,557 `*.md` files hidden-inclusive** (`.mimo-worktrees/`, `.agents/`, `.hermes/`), of which **991 are `git`-tracked**, plus **`coverage_manifest.csv` (5,808 lines)**, for each of `10\.3386/w33554`, `w33554`, `Unintended Consequences of Rebalancing`, `Mazzoleni`, `Melone`, `5122748`, `5172097`, `Front-Running Rebalancers`, `Threshold Signal`, `Calendar Signal`, `Harvey, Campbell` → **0 files for every identity pattern**, and **0 hits in `coverage_manifest.csv`** for `w33554`, the exact title, `Mazzoleni`, `5122748`. The only near pattern, `rebalancing signal`, hit **3 files that are all copies of one unrelated record** (`bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` plus its two `.mimo-worktrees` copies, using the phrase about RODHL-cycle rebalancing); generic `front-running` hits 87 files and `60/40` hits 13 files, all cleared as different sources/mechanisms below. `git log --oneline -20` was inspected separately as a convenience glance only and is not treated as dedup evidence.
- **Material-distinctness statement (independent record):** closest existing records differ in **source identity** and in at least one material axis:
  - `leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03.md` (arXiv `2608.03703`) — mechanism = *scheduled end-of-day hedging flow of leveraged ETFs* inside the equity cash session, event-study reversal; here the mechanism is *state- and calendar-dependent 60/40 equity–bond target rebalancing* across two futures markets, traded as a daily cross-asset timing book.
  - `loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02.md` (arXiv `2608.22768`) — feedback/stability analysis of LETF rebalancing with a reported **null** on deep venues; different source, different (matrix vs scalar) construction, different market set.
  - `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` — announced index reconstitution (cross-sectional add/delete events) versus unannounced, aggregate target-weight rebalancing with no event date.
  - `mutual-fund-redemption-forced-sale-residual-supply-absorption-premium-2026-09-24.md` (arXiv `2605.30672`) — cross-sectional residual-supply *pricing factor* at 1–12 month horizons; this record is a **time-series** next-day cross-asset signal with no cross-section.
  Axes on which this record is materially distinct: **mechanism** (coordinated uninformed target-weight rebalancing flow, market-level, not cross-sectional), **signal construction** (simulated 60/40 threshold/calendar weight deviation, Eqs. B.1–B.2), **universe/market type** (ES + 10Y Note futures, single cross-asset pair), **horizon/regime** (next-day, reverting within ~2 weeks; month-end/quarter-end seasonality).

## Economic mechanism

### Source-reported

The authors' stated chain: a large share of institutional money (pensions, sovereign funds, mutual funds, target-date funds) targets a stable equity/bond mix (commonly 60/40) and therefore **sells recent winners and buys recent losers** on a *Threshold* rule (rebalance when the weight drifts beyond a band, e.g. 2 percentage points) or a *Calendar* rule (rebalance on a schedule, typically month-end). Because past returns jointly determine *both* the direction and the timing of these trades, the trades are coordinated without any information content, and that coordination moves prices: "When stocks are overweight, funds sell stocks and buy bonds, leading to a decrease in equity returns of 17 basis points over the next day" (Abstract). The paper describes this as rebalancers acting as **macro-contrarians**, and states the pressure "conveys little information about market fundamentals" and reverts (§2.1.2, §6). The same predictability "enables certain market participants to profit by front-running the orders of large institutional funds" (Abstract), and §4 turns that into a tradable portfolio.

### Research interpretation

Falsifiable mechanism: **uninformed-but-coordinated aggregate demand shock against an inelastic demand curve** (the inelastic-markets / preferred-habitat account the paper cites: Gabaix & Koijen; Vayanos & Vila; Gromb & Vayanos), not an informational signal. If true, then (i) next-day equity-minus-bond returns should be negatively predictable from a *point-in-time* reconstruction of 60/40 weight deviation, (ii) the effect should be strongest exactly when mechanical rebalancers are documented to trade (last week of the month, quarter-end, large state deviations), (iii) it should be absent where no institutional target exists (the paper's own value-vs-growth falsification), and (iv) a portfolio that leans against the deviation should earn a risk premium that survives modest costs and is larger in high-friction (illiquid, high-vol) states where liquidity providers are constrained.

Component roles (as in the source's §4 construction):

```text
Seasonality / state filter: Calendar signal active only in the last week of the month
                            (week4) plus the first business day of the next month;
                            Threshold signal active on any day the 60/40 weight is off target
Primary signal:             average of modified Threshold and Calendar weight-deviation signals
                            (Appendix B, Eqs. B.1-B.2) -> portfolio weight w_t
Trade:                      long S&P 500 futures vs short 10-year Treasury note futures
                            (or the reverse) proportional to w_t
Risk / exit:                none specified by the source - no stop, no vol target,
                            no position limit, no drawdown control (explicit gap)
```

The paper does not claim every component contributes equally: it reports that the Threshold leg alone is significant (Table 2, column 3) and that Calendar works only in the month-end window (Table 2, columns 1–2), so an ablation of the two legs is required before attributing alpha to the combination.

## Signal

All of the following is `source-reported` unless marked.

- **Formation timestamp / tradability:** both signals are functions of **trailing close-to-close futures returns**, computed at the end of day *t*; the predictive regressions and the strategy are written for *t+1* (`R_t+1 = (R^{S&P500}_{t+1} − R^{10-y}_{t+1}) · w_t^Strategy`), i.e. the position formed on *t* earns the next day's cross-asset return (§1.2, §4, Appendix B). **The exact order time and execution price (close of day *t*, next open, or VWAP) is never stated** → `data gap`; any concrete execution convention adopted for replication is `research-proposed`.
- **Timezone / session convention:** not stated in the source; the data are U.S. futures daily bars on the U.S. trading calendar with a documented holiday rule (both front contracts N/A) and the 9/11 closures, but the **timezone, clock source and timestamp precision are `data gap`** — a replication must pin them (`research-proposed`: exchange-local session close, America/Chicago, millisecond UTC timestamps, out-of-order records dropped).
- **Portfolio recursion (Appendix B):** start at 60% equity / 40% bond; each day update weights with realized ES and TY returns; under **Threshold**, reset the equity weight to 60% whenever the post-return weight deviates from 60% by **≥ δ**; under **Calendar**, reset to 60% on the **last business day of every month**. Signals are the weight deviations from target: `Threshold signal_t = w^T_t − 60%` (Eq. B.1), `Calendar signal_t = w^C_t − 60%` (Eq. B.2).
- **Threshold aggregation:** the headline Threshold signal is the **average of the δ-specific signals over δ = 0% to 2.5% in 0.1% increments** (Eq. 2). The paper motivates this grid from institutional practice (δ = 0 → 252 rebalances/yr; δ = 1.1% → ~monthly; δ = 2.5% → ~quarterly) and shows predictive t-stats peaking around δ ≈ 2% and weakening above 2.5% (Figure 2). Footnote 10 states qualitatively similar results for δ ∈ [0%, 2%] and δ ∈ [0.1%, 2.5%], and that re-estimating on the **first half of the sample only** gives qualitatively similar results.
- **Calendar window:** predictability concentrates in the final days of the month (Figure 3, peak over the last four days); the paper therefore interacts Calendar with a **last-5-trading-day dummy ("week4")** (§1.2, Eq. 3).
- **Strategy weight (§4):** `w_t^Strategy` = average of two *modified* signals:
  1. **Threshold leg = −ThresholdSignal_t / 1.5%** (the paper's printed formula: "rescaling to − Threshold Signal_t / 1.5%"), i.e. the weight deviation is divided by 1.5 percentage points and sign-flipped, "because a positive Threshold value indicates that the S&P 500 is overweight relative to the 10-year Treasury note". §4 states that after this rescaling "both signals exhibit an annualized volatility of **11.6%**" in the sample.
  2. **Calendar leg = `sign(−CalendarSignal_t)` when *t* is in the last week of the month**; on the **first business day of a new month** it is set to `sign(CalendarSignal_{t−4})` to capture the documented early-month reversal (Figure 4); **zero on all other days**.
- **Position:** take a long (or short) S&P 500 futures position and the opposite 10-year Treasury note futures position in proportion to `w_t^Strategy` (§4, Table 6). **Exposure arithmetic is ours, not the source's:** with the Threshold leg equal to `−signal/1.5%`, a ±1.5-percentage-point weight deviation maps to a leg value of ∓1.0, and because both modified legs flip sign together in the same direction they add constructively in the daily average (e.g. legs of −1.0 and −1.0 average to −1.0; −1.33 and −1.0 average to ≈−1.17) — so **gross exposure on the cross-asset spread is of order ±1 on large-deviation days and materially smaller on ordinary days when the Calendar leg is zero** (the Calendar leg is non-zero only in the last week of the month and on the first business day). The source itself never prints an exposure, leverage, notional or vol-target number; its only exposure diagnostic is the reported 9.17% annualized strategy volatility (Table 6 Panel A). **Leverage cap, notional cap and volatility target are `underspecified`.**
- **Holding period / rebalancing cadence:** re-evaluated **every trading day**; no maximum holding period, no deadband beyond the δ grid, no explicit exit rule other than the weight turning over as the signals evolve. The horizon evidence (Figure 4: coefficient trough at day 4 (Threshold) / day 2 (Calendar), statistically indistinguishable from zero by day 9 / day 6, full reversion within roughly two months) implies a **1–2 week effective horizon**.
- **Ties / simultaneous signals:** not addressed by the source (`underspecified`).
- **Parameters and their source:** δ grid (0–2.5%, 0.1% steps) and 1.5% rescaling constant — **source-specified**; all three are *chosen by the authors with the full main sample available* (the first-half re-estimate in footnote 10 is the only stated protection) → treat any re-tuning as in-sample unless re-derived point-in-time.
- **Position sizing / risk overlay:** **none in the source.** Any vol targeting, stop, drawdown brake or per-instrument position cap used in our own tests must be labelled `research-proposed`.

## Required data

- **Instruments:** E-mini S&P 500 futures and 10-year Treasury note futures; a continuous, roll-adjusted **excess-return** series for both, with the contract-expiry calendar (roll front → second at the end of the month preceding expiry; Internet Appendix A). The paper's series comes from **Bloomberg**.
- **Universe / market type:** single cross-asset pair, **US futures** (equity index + government bond); no cross-section, no stock selection.
- **Timeframe:** daily bars, U.S. trading calendar; timestamps must be aligned to the futures session close because signals are close-to-close.
- **Fields needed:** daily excess returns of ES and TY (enough for the recursion and both signals); contract roll/expiry dates. Long-sample replication additionally needs French daily equity total returns and GSW 10-year Treasury yields.
- **Funding / fee / spread needs:** none are consumed by the signal itself (the source models no cost field at all). A tradable replication still needs, per leg and per day: quoted spread or bid/ask, commission/fees, roll spread on contract switch, initial/margin rate and financing rate, and an impact/participation estimate — **all absent from the source → `data gap`, never defaulted to zero** (see *Execution assumptions*).
- **Validation-only data (not needed to trade):** CFTC COT and Large Trader Net Position Changes, ANcerno institutional trades, ICI mutual-fund flows (Figure 5); VIX, MOVE, EPU, ADS, news sentiment, aggregate retail attention (controls in Tables 1, 2, 3); CRSP returns for idiosyncratic volatility and BofA GFSI liquidity risk (Table 6 Panel C regimes); MSCI ACWI ex USA (international check, Table D.14); Russell 1000/2000 and Value/Growth (Table 5).
- **Point-in-time / availability:** tradable signals use only lagged returns — no look-ahead in the signal itself. The **controls and friction regimes are same-period research variables** and are not tradable inputs; using them in a live rule would be look-ahead. Publication/availability of the paper itself (Mar 2025 → rev. Jan 2026) is *after* most of the main sample.
- **Missing-data assumptions:** Bloomberg holidays identified when both front contracts (TY1 and ES1) are reported N/A; **September 12–14, 2001 explicitly marked as exchange closures** because ES1 had no prices and ES2 appeared to carry stale values (Internet Appendix A). No imputation beyond that is described.

## Execution assumptions

**Source-reported:**

- Instrument/venue: **futures** (liquid, exchange-traded, two legs), daily rebalancing, direction set by the sign of `w_t^Strategy`.
- **Transaction costs:** the *only* statement about strategy-level costs is one sentence in §4: "Importantly, our strategy is robust to the inclusion of transaction costs. **Following the conservative assumptions of Harvey et al. (2018), we estimate that the Sharpe ratio net of transaction costs remains close to 1.**" (Harvey et al. (2018) = *The Impact of Volatility Targeting*, JPM 45:14–33.) **No basis-point parameter, no turnover, no net return series and no cost table is printed anywhere in the paper** → the Table 6 figures must be read as **gross-of-cost** performance with an unverified net-of-cost claim attached (`data gap`, never treated as 0).
- **Not modelled / absent from the paper (all `data gap`, never zero):** bid-ask spread, slippage, market impact, commissions/fees, contract **roll cost**, **margin/collateral financing**, borrow (not applicable to futures but unstated), latency, fill assumptions, partial fills, participation/ADV caps, **capacity**, and **turnover**. A full-text scan of the pinned PDF returns **zero** occurrences of "bid-ask", "slippage" and "margin"; "transaction cost" appears only in the institutional-rebalancing-cost discussion (§2.1.1, §5), not as a strategy cost model.
- Separate from the strategy, §2.1.1 prices the **rebalancers' own** implicit cost: Calendar ≈ |−0.39| × 1% × 12 ≈ **5 bps/yr**; Threshold **6–27 bps/yr across δ ∈ [0%, 2.5%], average 15 bps** (11 bps under the conservative pre-breach timing assumption); average of the two ≈ **8 bps/yr**, scaled to ≈ **$16 bn/yr (~$200 per U.S. household)** on >$20 tn of retirement assets. **These are costs borne by rebalancers, not costs of the front-running strategy** and must not be mixed.
- Implied leverage: the cross-asset spread position with |w| of order 1 in two futures markets is implicitly levered to futures margin; **margin requirements, financing rate and leverage limits are never discussed** → `data gap`.

**Research-proposed (our replication choices, not the source's):**

- Signal computed after the close of day *t*; order sent at the **next session open** (or next close if open is unavailable); market orders, full fill assumed at the quoted price.
- Cost ladder of **0 / 0.25 / 0.5 / 1 / 2 bps one-way** on traded notional, plus an explicit roll-spread charge on contract switches and financing on margin balance at the effective fed funds rate.
- Gross exposure capped at **±1.0** per leg and scaled to a **10% annualized vol target** (`research-proposed` risk overlay, clearly separate from any alpha claim).
- Participation cap of **10% of 5-minute ES/ZN volume** for the capacity test (`research-proposed`).

## Evidence

### Source-reported

All figures below are third-party claims from the pinned NBER WP 33554 PDF (rev. January 2026), main sample **daily 1997-09-10 → 2023-03-17**, and are **not independently reproduced**.

**Strategy performance — Table 6, Panel A** (annualized %):

| Series | Excess return | Volatility | Sharpe | Skewness |
|---|---|---|---|---|
| S&P 500 (`R^SP500`) | 7.11 | 20.05 | 0.35 | −0.08 |
| 10-year note (`R^10T`) | 2.92 | 6.13 | 0.48 | 0.03 |
| **Strategy (`R^Strategy`)** | **10.20** | **9.17** | **1.11** | **5.23** |

- **Table 6, Panel B — alphas (% p.a., heteroskedasticity-consistent s.e. in parentheses):** CAPM **9.61 (1.77)\*\*\***, Carhart-4 **9.64 (1.78)\*\*\***, Fama–French-5 **9.49 (1.74)\*\*\***, Hou–Xue–Zhang-q **9.43 (1.75)\*\*\***; §4 text: "t-statistic above 4 for all combinations of factor models".
- **Table 6, Panel C — strategy return in high (H) vs low (L) friction halves (% p.a.):** idiosyncratic volatility **15.68 (3.44)\*\*\*** vs **5.09 (1.28)\*\*\***; BofA GFSI liquidity risk **17.96 (3.33)\*\*\*** vs **3.79 (1.85)\*\***; VIX **16.50 (3.44)\*\*\*** vs **3.91 (1.11)\*\*\***; MOVE **14.85 (3.32)\*\*\*** vs **5.55 (1.43)\*\*\***; EPU **15.16 (3.26)\*\*\*** vs **5.24 (1.56)\*\*\***.
- **§4 net-of-cost claim:** Sharpe "net of transaction costs remains close to 1" under Harvey et al. (2018) assumptions (parameters not printed → `data gap`).
- **§4 crisis ablation:** excluding September 2008–March 2009 and March 2020, the strategy **Sharpe remains 0.90**.
- **Figure 6 display convention (source-stated):** the cumulative curve is built from `R^Strategy_t` **"rescaled to match the volatility of `R^SP500_t`"** — so the plotted path is a vol-matched illustration, **not** the raw strategy return stream; the only raw-return statistics are Table 6 Panel A (10.20% / 9.17% / 1.11).

**Predictive evidence — Table 1 (dependent variable = next-day S&P 500 minus 10-year note futures return, N = 6,226):**

- Column (1): Threshold **−0.4144 (0.1148)\*\*\***, Calendar × week4 **−0.3029 (0.0808)\*\*\***, Momentum 0.0023 (0.0006)\*\*\*, adjusted R² 0.0239.
- Column (5) (all controls: VIX, MOVE, EPU, ADS, sentiment): Threshold **−0.4226 (0.1139)\*\*\***, Calendar × week4 **−0.3033 (0.0808)\*\*\***, Momentum 0.0024 (0.0007)\*\*\*, adjusted R² **0.0248** (the 0.0243 adjusted R² belongs to column (3)).
- **§2.1.1 economic size:** a **one-standard-deviation decrease** in Threshold (Calendar) predicts a next-day cross-asset return **"about 20 bps (19.2 bps)"** (source wording); the Abstract/§1 states a one-SD *increase* lowers **equity** returns by ≈16 bps (Threshold) / ≈17 bps (Calendar) and raises **bond** returns by ≈4 bps / 2 bps.
- **Table 3 (disaggregated legs, with controls):** one-SD decrease → **equity +15.9 bps (Threshold) / +16.9 bps (Calendar)** and **bond −4.1 bps / −2.3 bps** next day (equity and bond move oppositely as the mechanism requires).
- **Table C.1 (signal summary stats, annualized):** Threshold mean 0.49, SD 0.08, AR(1) 0.61, skew −0.98, excess kurtosis 2.69; Calendar mean 0.18, SD 0.16, AR(1) 0.91, skew −1.43, excess kurtosis 6.27; Threshold–Calendar correlation **0.605**, Threshold–momentum correlation **0.676** (Table C.2).
- **Horizon (Figure 4):** coefficients trough at **day 4 (Threshold)** / **day 2 (Calendar)**, become insignificant at 5% by **day 9 / day 6**, and (§1) pressures "revert almost entirely within two weeks"; the longer-horizon estimates "completely revert within less than two months".

**Seasonality and scope (Tables 2, 4, 5):**

- **Table 2 Panel A (month-end seasonality, verified cell-by-cell):** Threshold −0.3281 (0.1113)\*\*\* / −0.4144 (0.1148)\*\*\* / −0.4789 (0.1308)\*\*\* across the three specifications; `Calendar × week4` −0.3029 (0.0808)\*\*\* in column (2) and −0.3511 (0.0963)\*\*\* in column (3); `Threshold × week4` 0.2137 (0.1620), **insignificant**, in column (3); adjusted R² 0.0130 / 0.0239 / 0.0244; N = 6,226. §3.1's reading: Calendar's predictability "concentrates at month-end" while Threshold's does not (the month-end interaction is a Calendar phenomenon). The table caption states Constant, Calendar, week4, Momentum and one-day trailing returns are **not** tabulated, so any further Panel A cell is a `data gap`.
- **Table 2 Panel B (months of each quarter, N = 2,078 / 2,052 / 2,097):** Threshold **−0.2723 (0.2075) — insignificant in the 1st month** → −0.4153 (0.1666)\*\* (2nd) → −0.5845 (0.2083)\*\*\* (3rd); `Calendar × week4` −0.2509 (0.1590) → −0.3487 (0.1062)\*\*\* → −0.3400 (0.1300)\*\*\*; adjusted R² 0.0110 / 0.0234 / 0.0469.
- Table 4 (long sample, French/GSW data): **1961–1997 subsample null** (Threshold −0.0157 (0.0576); Calendar × week4 −0.0284 (0.0596)); **1997–2023** Threshold −0.3685 (0.1103)\*\*\*, Calendar × week4 −0.2569 (0.0670)\*\*\*. Footnote 32: extension through 2025 makes results "even stronger" (not tabulated).
- Table 5 (Russell 1000 vs 2000, 90/10 target, from 2006-08): Threshold −0.2054 (0.0597)\*\*\*, Calendar × week4 −0.1174 (0.0683)\*; **value-vs-growth falsification is a null** (−0.0339 (0.0478), −0.0678 (0.0654), both insignificant).
- Table D.14 (international, MSCI ACWI ex USA with one-day lag and 2-day U.S. control): both signals negative and significant, R² ≈ 2.5%.
- **§5 Discussion (utility paragraph, immediately before §6 Conclusion):** for risk aversion γ = 3, threshold rebalancing generates utility gains of approximately **18 bps** and calendar rebalancing about **10 bps** relative to buy-and-hold (`Ū = r̄ − 0.5γσ̄²`) — the *benefit* side borne by the rebalancer, not the front-runner's return.

**Flow validation (Figure 5) and institutional corroboration:** the four datasets — CFTC COT positions (2006–2023; hedgers **negatively** correlated with the lagged signals, speculators positively), CFTC Large Trader Net Position Changes (asset managers vs leveraged funds, report period Jan 2009–May 2011, figure window 2009–2011), ANcerno daily institutional equity trades restricted to the Jan 1999–Sep 2011 span where **pension plan sponsors** are identifiable and to S&P 500 constituents (1999–2011), and ICI mutual-fund equity-vs-bond flows (2007–2023) — are reported as **broadly consistent** with the signals' sign (source: §2.2 summary + Figure 5). §2.3 reports a **19 June 2024 roundtable with 16 public pensions (~$2 tn AUM)** in which participants acknowledged being aware of front-running of their own rebalancing ("all pensions in our roundtable sample rebalance mechanically based on Calendar and Threshold rules").

- **Rebalancing-cost evidence for the incumbent side (§2.1.1):** Calendar ≈ 5 bps/yr (`|−0.39| × 1% × 12`), Threshold **6–27 bps across δ ∈ [0%, 2.5%] with an average of 15 bps** and **≈11 bps under the conservative pre-breach timing assumption**, blended ≈ **8 bps/yr** → ≈ **$16 bn/yr (≈$200 per U.S. household) on a market "potentially exceeding $20 trillion"**; a **randomly dated** monthly rebalance (10,000 simulations, Figure D.5: `Mean = −0.6 bps`) has an average cost of **0.6 bps (median 0.5 bps)** — i.e. predictable *dates*, not rebalancing itself, generate the cost — at the price of ≈**35 bps of tracking error (≈3% of the portfolio's 12% annualized volatility; §5)**.

### Independently reproduced

`not independently reproduced`. This run performed only: (a) direct download and full read of the pinned NBER PDF, (b) landing-page metadata verification (DOI, issue/revision dates, author meta tags), (c) table/section provenance for every number above, and (d) repository-wide source-identity dedup. **No regression, portfolio, Sharpe, alpha or cost figure was recomputed; no futures data was obtained; the strategy was not backtested.**

### Negative evidence

1. **Pre-1997 null (source-reported, Table 4 column 2):** over 1961–1997 neither Threshold (−0.0157, s.e. 0.0576) nor Calendar × week4 (−0.0284, s.e. 0.0596) predicts next-day cross-asset returns. The entire effect lives in the last ~26 years — consistent with the authors' own TDF-legislation story, but it also means the result is **regime-contingent and of unverified stationarity**.
2. **Scope null (source-reported, Table 5 column 2):** no predictability between value and growth — the mechanism only operates where institutional targets exist.
3. **Crisis / friction concentration (source-reported, Table 6 Panel C + §4):** H-half returns (15.16–17.96% p.a.) run **3–4× the L-half** (3.79–5.55% p.a.); skewness 5.23; §4 names the GFC and the COVID crash as "significant contributors", and removing them drops Sharpe from 1.11 to 0.90. A large part of the headline is conditional on stressed, illiquid states.
4. **Multiplicity not controlled (source-reported):** Figure 2 scans the δ grid and Figure 3 scans the day-to-month-end grid; both captions state their dashed line is "the 1% critical value **assuming a single test**". No family-wise or false-discovery correction is applied anywhere in the paper.
5. **No out-of-sample design (source-reported):** all strategy statistics are full-sample inferences over 1997–2023 with calibration choices (δ range, week4 window, 1.5% rescaling) made on that sample; there is **no holdout, no walk-forward, no pre-registration**, and the "extended through 2025" result is asserted only in a footnote.
6. **Cost claim unverifiable (source-reported gap):** the strategy's net-of-cost evidence is a single sentence pointing at Harvey et al. (2018), with **no parameters, no turnover and no net return series**; everything tabulated in Table 6 must therefore be treated as gross.
7. **Source's own risk caveat (source-reported, §4):** "we emphasize that front-running the rebalancing is not a risk-free strategy. Trading ahead of rebalancers is risky due to uncertainty in both the timing and magnitude of the rebalancing trades (e.g., Dou, Kogan, and Wu, 2023)."
8. **Horizon give-back (source-reported, Figure 4 / §1):** pressures revert within ~2 weeks, so holding beyond the reversal window converts the edge into a loss; the strategy has no explicit exit rule tied to that decay.
9. **Cross-record contrary / contextual evidence (different source identities already in this repository):** `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (Chen & Welch, *What Useful Alphas?*, arXiv:2607.06502 — post-2005 investable large-cap **7 bp median** anomaly return with a luck-adjusted null) — a reminder that published equity-market predictability rarely survives honest cost and multiplicity treatment; `leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03.md` and `loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02.md` — flow-front-running effects that decay or vanish once venue depth and execution are taken seriously; `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` — scheduled-flow event effects that weakened post-publication; `mutual-fund-redemption-forced-sale-residual-supply-absorption-premium-2026-09-24.md` — flow-based pressure that only prices under specific market-clearing conditions.
10. **Publication status:** NBER working paper, explicitly not peer reviewed (cover disclaimer), so none of the above has survived refereeing.

## Falsification plan

Every threshold below is a `research-defined falsification threshold`; every operational choice not printed in the source is `research-proposed`.

- **F1 — Point-in-time signal replication.** Rebuild Threshold/Calendar signals from lagged ES/TY closes over 1997-09-10 → 2023-03-17 exactly per Appendix B (no re-tuning of δ or week4). *Fail if* the next-day cross-asset coefficient on either signal has the wrong sign or |t| < 3.0 in the joint specification (Table 1 column 5 analogue).
- **F2 — Frozen forward window.** Hold out **2023-04-01 → 2026-06-30**, never used by the paper's calibration. *Fail if* the forward-window strategy Sharpe (gross) < 0.50 or either signal's forward coefficient is non-negative; passing F1 and failing F2 ⇒ classify as in-sample.
- **F3 — Cost ladder.** Re-run at 0 / 0.25 / 0.5 / 1 / 2 bps one-way plus roll spread plus margin financing. *Fail if* net Sharpe < 0.50 at 0.5 bps one-way, or if break-even one-way cost < 0.25 bps.
- **F4 — Turnover audit.** Report annual one-way turnover of the strategy. *Fail if* turnover exceeds 500%/yr and break-even cost is simultaneously < 0.25 bps (i.e. the result sits on an unmeasured cost assumption).
- **F5 — Placebo / null distribution.** 1,000 circular-shift (by 21–252 days) and sign-shuffled draws of both signals. *Fail if* the real strategy Sharpe is not above the 95th percentile of the placebo distribution.
- **F6 — Subperiod stability.** 1997–2007 / 2008–2015 / 2016–2023 / 2023-forward. *Fail if* fewer than 2 of the 3 in-paper subperiods are positive **or** the forward window is negative.
- **F7 — Crisis ablation.** Exclude 2008-09 → 2009-03 and 2020-03. *Fail if* Sharpe < 0.60 (source reports 0.90) ⇒ the edge is a crisis-carry, not a daily signal.
- **F8 — Multiplicity.** Recompute the Figure 2 (δ ∈ 0–4%, 0.1% steps) and Figure 3 (1–10 days to month-end) grids with Benjamini–Hochberg. *Fail if* q ≥ 0.10 for the headline Threshold / Calendar × week4 cells.
- **F9 — Mechanism ablations.** (a) Replace real month-end dates with the paper's *random rebalancing day* control (Figure D.5 design); (b) orthogonalize both signals against 5-day and 5-year reversal and against momentum (Table D.8/D.10 analogue); (c) drop each strategy leg. *Fail the mechanism claim* if the signal coefficients shrink > 50% under (b), or if the random-date control produces an economically similar Sharpe under (a), or if one leg alone explains > 90% of the return under (c) while the paper markets the combination.
- **F10 — Capacity / impact.** Execute at 10% and 20% of 5-minute ES/ZN volume with a square-root impact model. *Fail if* net-of-impact Sharpe drops > 0.30 relative to the frictionless figure, or if required notional exceeds the stated impact budget.
- **F11 — Execution-timing robustness.** Compare next-open, next-close and TWAP-next-day entries. *Fail if* the sign of the strategy return flips under any executable timing ⇒ the result depends on an unstated execution convention.
- **F12 — Roll-rule robustness.** Rebuild the continuous futures series with roll at expiry vs roll 5 business days before expiry. *Fail if* sign or significance of the headline coefficients flips ⇒ result is a roll-construction artifact.

**Action on failure:** any of F1–F3 failing ⇒ keep record as research-only, do not promote; F5/F8 failing ⇒ treat as data-snooped; F10/F11/F12 failing ⇒ mark non-implementable regardless of statistics.

## Crypto portability

**unproven.** The mechanism is a *ported hypothesis*, not crypto evidence: the source studies only U.S. equity index and Treasury futures and never analyses crypto markets.

- **What could port in form:** a target-weight two-asset book with mechanical rebalancing exists in crypto-adjacent products (crypto index funds/ETPs, BTC–ETH "60/40" style mandates, treasury-style DAOs rebalancing BTC vs stables). A Threshold/Calendar weight-deviation signal could be written on, e.g., a BTC-vs-stablecoin or BTC-vs-ETH target mix, traded on perpetuals or spot.
- **What breaks the mechanism:** there is no evidence of *large, coordinated, calendar-anchored* institutional rebalancing in crypto at a size that moves aggregate prices; sessions are **24/7** so "month-end week" liquidity events do not concentrate the same way; venues are fragmented (signal measured on one venue, fill on another); **funding** on perps creates a carry that the equity/bond spread analogue does not have; mark/index price and liquidation mechanics differ from futures settlement; no closing-auction concentration; custody/withdrawal risk and stablecoin de-peg add failure modes absent from the source.
- Adjacent repository evidence: `loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02.md` reports a **null** for leveraged-ETP rebalancing pressure on deep crypto venues — a concrete warning that mechanical-flow front-running can evaporate where depth is ample.
- Anything beyond "the form can be written down" — including the specific 60/40 crypto target, thresholds, funding treatment and venue policy — is `research-proposed` and untested.

## Limitations

- **`data gap` — strategy transaction-cost model:** one sentence, no parameters, no turnover, no net series (§4). The Table 6 headline is **gross**.
- **`data gap` — execution convention:** order time and price for forming `w_t` are never stated; fills, latency and partial fills are absent.
- **`data gap` — leverage/financing:** margin, collateral cost and leverage limits for a futures spread position of order ±1 are never discussed.
- **`data gap` — capacity/impact:** no participation or notional limits; Table 6 Panel C is the only friction analysis and it is a *regime* split, not an impact model.
- **`data gap` — turnover:** never reported, so round-trip frequency and cost sensitivity cannot be read off the paper.
- **`data gap` — extended sample:** the "through 2025" extension (footnote 32) is asserted without tables.
- **`data gap` — cross-version equivalence:** only the NBER revised-Jan-2026 PDF was read; the two SSRN mirrors (rev. Jan 2026 / Mar 2026) and the Dec-2025 AFA version were not opened, so version-to-version numeric drift is unknown.
- **`underspecified`:** tie handling, the exact gross-exposure normalization implied by the 1.5% rescaling, whether the strategy is vol-scaled (Table 6 reports 9.17% vol but no targeting rule is stated), and any risk overlay.
- **`unproven` / `not independently reproduced`:** all performance figures; in-sample calibration of δ, the week4 window and the rescaling constant; no holdout, no walk-forward, no multiple-testing correction; pre-1997 null; single cross-asset pair, single market (U.S.), futures-only.
- **Source quality:** NBER working paper, explicitly **not peer reviewed**; one author is affiliated with an asset manager whose clients rebalance mechanically (disclosed in the cover note: views "do not necessarily reflect those of … Capital Group") — not an undeclared conflict, but a positioning caveat.
- The record's own numbers are **equity/bond futures evidence** and must never be presented as crypto evidence.

## Implementation status

`implementation_status: not-implemented`. No signal code, no data pipeline, no backtest, no Qlib run, no production card and no Paper/Testnet/Live activity exists in our research stack as of 2026-09-26. This document is a normalized research capture only; the falsification plan above has not been executed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, or is approved for implementation, paper trading, testnet or live trading. No performance claim here is our own verified result.

## Related Wiki records

Wiki Brain `kb_search` run on 2026-09-26 (read-only; **nothing written**): `institutional rebalancing front-running equity bond price pressure` → 0 results; `rebalancing stock bond 60/40 institutional flows` → 0 results; `cross-asset futures timing signal equity bond relative return prediction` → 2 results; `price pressure demand shock predictable trading` → 1 result. Only verified pages are linked:

- [[quant/bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01]] — mechanism-adjacent: documented aggregate flow → next-day price drift, in crypto ETFs.
- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]] — adjacent cross-asset/regime routing with explicit hysteresis, unlike this source's unstated exits.

No other related Wiki page was found; absence is a search result, not a claim that none exists. Zero repository records share this source identity (see Provenance).

## Sources

1. Campbell R. Harvey, Michele G. Mazzoleni, Alessandro Melone. *"The Unintended Consequences of Rebalancing."* **NBER Working Paper No. 33554**, Issue Date March 2025, **Revision Date January 2026**. DOI `10.3386/w33554`. Landing: https://www.nber.org/papers/w33554 (authors, DOI, issue/revision dates and `citation_*` meta verified 2026-09-26).
2. Same paper, **pinned primary PDF**: https://www.nber.org/system/files/working_papers/w33554/w33554.pdf — 76 pages, 667,944 bytes, **SHA-256 `adb7ad35d5a5bdc18f6f75801132391331e33711c19ce944f569b0a9d345e158`**, retrieved and read end-to-end 2026-09-26. Provenance for the Abstract, §1–§6, Internet Appendices A–D, Tables 1–6 and C.1–C.2, and Figures 2–6.
3. https://doi.org/10.3386/w33554 — DOI resolution for the working paper.
4. Version landscape (identification only, **not opened this run**; SSRN is Cloudflare-protected for non-browser clients): SSRN `abstract_id=5122748` (Fisher/Dice working-paper mirror, last revised 15 Jan 2026) and SSRN `abstract_id=5172097` (NBER mirror, last revised 8 Mar 2026), plus the AFA 2026 conference PDF dated 15 Dec 2025 — recorded so a future run can verify cross-version numeric equivalence.
5. Harvey, C. R., Hoyle, E., Korgaonkar, R., Rattray, S., Sargaison, M., Van Hemert, O. (2018). *"The Impact of Volatility Targeting."* Journal of Portfolio Management 45:14–33 — cited **by the source** as the basis of its net-of-transaction-cost statement; not read for this record.
