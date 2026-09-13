---
schema: strategy-research-record-v1
title: "SEC Form 10-12B Corporate Spin-Off Post-Distribution Drift: Empirical Falsification of Forced-Selling Excess Returns and Structural Anomaly Decay in Modern US Equities"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-catalyst
  - corporate-actions
  - spinoff-drift
  - structural-flow
  - forced-selling
  - market-friction
  - anomaly-decay
  - falsification
  - negative-results
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "Primary audit decision record: JonathanBeck1, 'Decision: Spin-off Post-Event Drift (T42)', research/spinoff_drift_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/spinoff_drift_decision.md"
  - "Primary pre-registration: JonathanBeck1, 'Pre-registration: Spinoff Post-Event Drift (T42)', research/spinoff_drift_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/spinoff_drift_preregistration.md"
  - "Primary empirical code: JonathanBeck1, 'src/trader/catalysts/spinoff_drift.py', 'scripts/run_spinoff_drift_study.py', and 'tests/financial/test_spinoff_drift.py' (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63)"
  - "Primary research synthesis: JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 4.1, 4.2, 8.1, Table 1, and Table 2 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
  - "Historical academic foundation: Patrick J. Cusatis, James A. Miles, and J. Randall Woolridge, 'Restructuring Through Spinoffs: The Stock Market Pays', Journal of Financial Economics, Vol. 33, No. 3 (1993), pp. 293–311. DOI: 10.1016/0304-405X(93)90005-B"
  - "Historical investment foundation: Joel Greenblatt, 'You Can Be a Stock Market Genius: Uncover the Secret Hiding Places of Stock Market Profits', Simon & Schuster, New York (1997), Chapter 3 (The Spinoff Phenomenon), pp. 47–84."
  - "Post-2000 empirical re-evaluation: John J. McConnell, Scott B. Sibley, and Wei Xu, 'Spinoffs: 20 Years Later', Journal of Financial Economics, Vol. 116, No. 1 (2015), pp. 118–137. DOI: 10.1016/j.jfineco.2014.12.001"
  - "Anomaly decay literature: R. David McLean and Jeffrey Pontiff, 'Does Academic Research Destroy Stock Return Predictability?', The Journal of Finance, Vol. 71, No. 1 (2016), pp. 5–32. DOI: 10.1111/jofi.12365"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SEC Form 10-12B Corporate Spin-Off Post-Distribution Drift: Empirical Falsification of Forced-Selling Excess Returns and Structural Anomaly Decay in Modern US Equities

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`).
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`).
- **Commit Date:** 2026-09-08T21:47:53Z (`source-reported`).
- **Source As-Of Date:** 2026-09-08 (`source-reported`).
- **Primary Source Documents & Code Directly Audited:**
  - `research/spinoff_drift_preregistration.md`: Pre-registered research protocol detailing the directional hypothesis, SEC EDGAR Form 10-12B filing universe, survivorship-safe registration tracking, SPY market-adjusted cumulative abnormal return (CAR) framework ($\beta = 1$), execution friction baseline (20 bps round-trip), temporal split (IS: $\le 2019$, OOS: $\ge 2020$), two distinct placebo controls (same-name random windows and pooled random windows), and falsification kill criteria (`source-reported`).
  - `research/spinoff_drift_decision.md`: Official audit decision record recording the outright `KILL` verdict, the empirical sample size ($N = 104$), the primary 1-month window performance ($-0.07\%$ gross, $-0.27\%$ net, $t = -0.03$), the secondary 3-month window ($+1.91\%$, $t = +0.58$), the IS/OOS sign instability, the clean pooled placebo null ($-0.01\%$, $t = -0.01$), and contributor ablation results (`source-reported`).
  - `src/trader/catalysts/spinoff_drift.py`: Pure Python analytical module executing event-time CAR computation (`compute_event_metrics`), abnormal return series generation (`_abnormal_return`), same-name pseudo-event placebo sampling (`placebo_cars`), metric aggregation (`aggregate`), top contributor removal (`drop_top_contributors`), and the 5-criterion formal gate verification (`evaluate_gate`) (`source-reported`).
  - `scripts/run_spinoff_drift_study.py`: End-to-end operational pipeline querying the SEC EDGAR full-text search API (`efts.sec.gov/LATEST/search-index`) for Form 10-12B filers (2015–2025), mapping CIK to ticker via `display_names`, querying Yahoo Finance for spinco and SPY price history, establishing $t_0$ as the first regular-way close, generating placebo distributions, and evaluating the pre-registered gate (`source-reported`).
  - `tests/financial/test_spinoff_drift.py`: 19 deterministic, network-free unit tests validating $t_0+1$ ex-ante entry alignment, abnormal return calculation, 75% daily glitch guard rejection, placebo window gap boundaries, after-cost subtraction, and gate evaluation logic (`source-reported`).
  - `research/PAPER_DRAFT.md`: Formal research manuscript (§4.1, §4.2, §8.1, Tables 1 & 2) categorizing test T42 as Class 1 (Decay Into Noise) and synthesizing its role within the broader 50-strategy empirical campaign (`source-reported`).
- **Historical Academic Precedents:**
  - Patrick J. Cusatis, James A. Miles, and J. Randall Woolridge (1993), *"Restructuring Through Spinoffs: The Stock Market Pays"*, *Journal of Financial Economics*, establishing that spun-off subsidiaries and their parent companies significantly outperformed market benchmarks by $+18.2\%$ to $+22.9\%$ over 1- to 3-year holding periods post-spinoff (`source-reported`).
  - Joel Greenblatt (1997), *"You Can Be a Stock Market Genius"*, popularized the retail implementation of the spin-off anomaly, arguing that structural institutional constraints force indiscriminate liquidation of distributed spinco shares, creating persistent multi-month undervaluation (`source-reported`).
  - John J. McConnell, Scott B. Sibley, and Wei Xu (2015), *"Spinoffs: 20 Years Later"*, *Journal of Financial Economics*, re-evaluating the Cusatis et al. sample and demonstrating that the post-spinoff abnormal return premium was heavily concentrated in the pre-2000 epoch and decayed substantially in the post-2000 era (`source-reported`).
  - R. David McLean and Jeffrey Pontiff (2016), *"Does Academic Research Destroy Stock Return Predictability?"*, *The Journal of Finance*, showing that capital flows and institutional arbitrage systematically compress cross-sectional equity anomalies post-publication (`source-reported`).
- **Underlying Sample & Universe:**
  - Universe: Every distinct filer of an SEC Form 10-12B (registration of a new security class under Section 12(b) of the Securities Exchange Act of 1934, the primary filing utilized when a parent company spins off an independent publicly traded entity) filed between 2015-01-01 and 2025-06-30, deduped to the earliest filing date per CIK (`source-reported`).
  - Total filers with ticker mapped via EDGAR `display_names`: $N = 127$ (`source-reported`).
  - Usable spincos with complete price histories in Yahoo Finance: $N = 104$ (`source-reported`).
  - Exclusions: 18 filers dropped due to missing Yahoo Finance price series (unmappable ticker changes, immediate post-spin acquisition, or transient timestamp anomalies) and 5 filers dropped due to glitch-guard threshold violation ($>75\%$ single-day abnormal return) (`source-reported`).
  - Survivorship safety: Form 10-12B filings represent regulatory registrations filed prior to trading initiation; tracking filers by registration CIK ensures that subsequent bankruptcies and delistings (such as Armstrong Flooring, `AFIIQ`, or Baudax Bio, `BXRXQ`) remain in the evaluated sample, precluding survivorship bias (`source-reported`).
- **Temporal Sample Span:**
  - Overall study period: 2015-01-01 to 2025-03-31 (providing $\ge 2$ months of subsequent price series through mid-2025) (`source-reported`).
  - In-Sample (IS): First-trade date on or before 2019-12-31 ($N = 47$) (`source-reported`).
  - Out-of-Sample (OOS): First-trade date on or after 2020-01-01 ($N = 57$) (`source-reported`).
- **Repository Deduplication Audit:**
  - A comprehensive search of the `alpha-strategy-research` repository confirmed zero existing records investigating corporate spin-offs, SEC Form 10-12B post-distribution drift, or campaign test T42.
  - Existing corporate event and structural flow records (`buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13.md` [Form 8-K Item 8.01 buybacks], `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` [index reconstitution], and `sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05.md` [Form 4 insider buying]) address entirely distinct corporate filings, participant motivations, execution horizons, and empirical datasets.

## Economic mechanism

### Source-reported

1. **The Classic Indiscriminate Forced-Selling Thesis:**
   - When a parent corporation distributes shares of a newly independent subsidiary ("spinco") pro-rata to existing equity holders, the distributed shares land in portfolios whose investment mandates do not permit holding them (Cusatis, Miles & Woolridge 1993; Greenblatt 1997) (`source-reported`).
   - Three specific investor cohorts face non-fundamental liquidation pressures upon distribution:
     - **Index and Benchmark Funds:** The parent firm may be a constituent of the S&P 500 or Russell 1000, while the spinco is not included in the index at distribution; index-tracking managers are legally or contractually mandated to liquidate the spinco shares immediately upon receipt (`source-reported`).
     - **Institutional Mandate Restrictions:** Active institutional managers holding the parent firm may have market-capitalization minimums (e.g., large-cap only), sector boundaries, or liquidity restrictions that the newly minted small- or mid-cap spinco violates (`source-reported`).
     - **Retail Odd-Lot Dumping:** Retail investors who receive small fractional or low-dollar spinco positions frequently liquidate them indiscriminately to simplify portfolio holdings (`source-reported`).
   - Because this supply flow is mechanical and price-insensitive, it temporarily drives the spinco's market price below its intrinsic or fair value. Concurrently, informed fundamental buyers are slow to step in because newly listed spincos initially lack sell-side research coverage, historical accounting baselines, and commercial visibility, creating an extended post-event abnormal return drift over the subsequent 1 to 3 months (`source-reported`).

2. **The Falsification Hypothesis & Arbitrage Decay:**
   - While the forced-selling mechanism was historically profitable in pre-2000 data, several structural market transformations over the last two decades have systematically degraded the anomaly:
     - **Commercial Spin-Off Arbitrage Products:** The launch of targeted spin-off exchange-traded funds (such as the Invesco S&P Spin-Off ETF, ticker `CSD`, launched in December 2006) and dedicated institutional special-situations hedge funds actively warehouse and arbitrage distribution-day selling pressure (`source-reported`).
     - **Index Fast-Tracking:** Modern index providers (such as S&P Dow Jones and FTSE Russell) established fast-track rules to incorporate qualifying spincos into relevant index families without prolonged exclusion windows (`source-reported`).
     - **Algorithmic Anticipation:** Institutional market makers and quantitative desks anticipate corporate distributions via EDGAR Form 10-12B and Form 8-K filings weeks in advance, pricing the event risk before regular-way trading commences (`source-reported`).
   - Consequently, the modern prior (2015–2025) is that post-distribution drift has decayed toward statistical zero, and any gross residual return is eliminated by execution frictions on newly listed, wider-spread securities (`source-reported`).

### Research interpretation

- The hypothesized edge is an event-driven structural supply-imbalance alpha. For the hypothesis to be tradeable, price-insensitive distribution flow must generate downward price dislocation that resolves via positive drift over an intermediate horizon ($[+1, +21]$ or $[+1, +63]$ trading days) (`research-proposed`).
- If modern execution venues and institutional liquidity providers efficiently absorb initial distribution volume within opening trading sessions ($t_0$), subsequent daily-bar forward returns will exhibit zero excess drift relative to market benchmarks (`research-proposed`).
- Furthermore, newly listed spun-off entities incur substantial bid-ask spreads and liquidity premiums; thus, a valid evaluation must evaluate after-cost cumulative abnormal returns against both broad market benchmarks and randomized non-event controls drawn from the same assets (`research-proposed`).

## Signal

### Source-reported

- **Universe Identification:** All corporate entities filing an initial SEC Form 10-12B registration between 2015-01-01 and 2025-06-30 (`source-reported`).
- **Anchor Timestamp ($t_0$):** The first regular-way trading day available in daily historical pricing (the initial trading date recorded by Yahoo Finance) (`source-reported`).
- **Trade Entry:** Position entry is executed at the closing price of day $t_0$ (`source-reported`).
- **Look-Ahead Protection:** Filing existence and the first regular-way trading session are fully observable ex-ante; the measurement window begins strictly at $t_0+1$ (the open of the subsequent session), ensuring that no future return data leaks into event cohort selection (unlike naive event studies that condition on day-0 return magnitudes) (`source-reported`).
- **Holding Horizon & Measurement Windows (Trading Days):**
  - **PRIMARY Window (`car_p1_p21`):** Days $[t_0+1, t_0+21]$ inclusive (~1 calendar month), representing the core holding period where forced-selling resolution should manifest (`source-reported`).
  - **Secondary Horizon (`car_p1_p63`):** Days $[t_0+1, t_0+63]$ inclusive (~3 calendar months, the classical Greenblatt holding horizon) (`source-reported`).
  - **Robustness Horizon (`car_p0_p21`):** Days $[t_0+0, t_0+21]$ inclusive, capturing the initial trading session return for sensitivity analysis (`source-reported`).
- **Benchmark / Abnormal Return Calculation:**
  - Daily abnormal return for spinco $i$ on day $\tau$:
    $$\text{AR}_{i, \tau} = R_{i, \tau} - R_{\text{SPY}, \tau}$$
    where $R_{i, \tau}$ is the split- and dividend-adjusted close-to-close return of the spinco and $R_{\text{SPY}, \tau}$ is the total return of SPY (market proxy with assumed $\beta = 1$) (`source-reported`).
  - Cumulative abnormal return over event window $[a, b]$:
    $$\text{CAR}_i[a, b] = \sum_{\tau = t_0 + a}^{t_0 + b} \text{AR}_{i, \tau}$$
    (`source-reported`).
- **Glitch Guard:** Any event observation exhibiting an absolute single-day market-adjusted return $|\text{AR}_{i, \tau}| > 75\%$ ($0.75$) within the analyzed window span is flagged as a likely unadjusted split or corporate-restructuring pricing error and excluded from the cohort ($N = 5$ dropped) (`source-reported`).
- **Position Sizing:** Equal-weighted across all qualifying spinco events (`source-reported`).

### Research-proposed (Operational Extensions)

- **Execution Timing:** Market-on-Close (MOC) order on day $t_0$ or Market-on-Open (MOO) on day $t_0+1$ (`research-proposed`).
- **Portfolio Overlay:** Dollar-neutral hedging against SPY via equivalent short notional established at $t_0$ close and liquidated at $t_0+21$ close (`research-proposed`).
- **Rebalance Cadence:** Non-overlapping or multi-asset rolling tranche allocations; position sizing scaled inversely to 20-day historical volatility of the parent firm (`research-proposed`).

## Required data

- **Regulatory Filing Data:** SEC EDGAR full-text search index API (`efts.sec.gov/LATEST/search-index`) querying Form 10-12B filings with date ranges 2015-01-01 to 2025-06-30 (`source-reported`).
- **Filer Metadata:** CIK identifier, corporate legal entity name, filing date, and ticker extracted from `display_names` (`source-reported`).
- **Equity Price History:**
  - Primary Instrument: Daily adjusted close prices (`auto_adjust=True`) for all identified spinco tickers (`source-reported`).
  - Market Benchmark: Daily adjusted close prices for SPY (SPDR S&P 500 ETF Trust) (`source-reported`).
- **Point-in-Time Availability:** Form 10-12B is filed publicly weeks in advance of distribution; first-trade execution occurs on day $t_0$, and entry occurs at $t_0$ close, guaranteeing zero look-ahead bias (`source-reported`).
- **Data Hygiene & Survivorship:** The sample is anchored on SEC registration documents, preserving bankruptcies, liquidations, and delistings (e.g., Armstrong Flooring `AFIIQ`, Baudax Bio `BXRXQ`), avoiding survivorship bias inherent in active equity databases (`source-reported`).
- **Missing Data Handling:** If a spinco possesses fewer than $t_0+63$ trading bars or Yahoo Finance cannot resolve historical prices, the event is recorded as dropped and omitted from forward metrics ($N = 18$ dropped) (`source-reported`).

## Execution assumptions

- **Execution Mode:** Long spinco position entered at the closing price of day $t_0$ and exited at the closing price of day $t_0+21$ (`source-reported`).
- **Round-Trip Transaction Friction:** Fixed at **20 bps** ($0.0020$) per trade cycle, representing double the baseline 10 bps friction applied to large-cap S&P constituents to reflect wider bid-ask spreads and lower market depth in newly listed small-cap spinco issues (`source-reported`).
- **Friction Stress Model:** A secondary sensitivity stress of **40 bps** ($0.0040$) round-trip is evaluated (`source-reported`).
- **Borrow & Shorting:** Long-only execution on the spinco; benchmark SPY hedge assumed fully borrowable at general collateral rates ($\le 25\text{ bps/yr}$, negligible over 21 days) (`research-proposed`).
- **Execution Fill Model:** Immediate fill at the reported closing bar without simulated market impact or price slippage beyond the declared fee allowance (`source-reported`).

## Evidence

### Source-reported

The primary empirical study evaluated $N = 104$ qualifying spinco events across the 2015–2025 period using the pre-registered protocol (`research/spinoff_drift_decision.md`):

1. **Primary Window Performance (`car_p1_p21` = $[t_0+1, t_0+21]$ trading days):**
   - Sample Size ($N$): **104** usable events (`source-reported`).
   - Gross Mean CAR: **$-0.07\%$** ($-0.0007$) (`source-reported`).
   - After-Cost Mean CAR (at 20 bps round-trip): **$-0.27\%$** ($-0.0027$) (`source-reported`).
   - $t$-statistic: **$-0.03$** (statistically indistinguishable from zero; well below the $|t| \ge 2.0$ gate threshold) (`source-reported`).
   - Median CAR: **$+0.17\%$** (`source-reported`).
   - Win Rate (% positive): **$52\%$** (54 positive, 50 negative; equivalent to random coin tossing) (`source-reported`).

2. **Temporal Partitioning & Regime Stability:**
   - **In-Sample (IS, 2015–2019):**
     - Sample Size ($N$): $47$ (`source-reported`).
     - Mean CAR: **$-0.22\%$** (`source-reported`).
     - $t$-statistic: **$-0.06$** (`source-reported`).
   - **Out-of-Sample (OOS, 2020–2025):**
     - Sample Size ($N$): $57$ (`source-reported`).
     - Mean CAR: **$+0.05\%$** (`source-reported`).
     - $t$-statistic: **$+0.01$** (`source-reported`).
   - **Verdict:** OOS sign instability (IS negative, OOS slightly positive), with both subperiods statistically zero. No positive abnormal return drift existed in either regime (`source-reported`).

3. **Matched-Control & Placebo Distributions:**
   - **Pooled Random-Window Placebo:**
     - Sample Size ($N$): $513$ random non-event windows drawn across the ticker and calendar space (`source-reported`).
     - Mean CAR: **$-0.01\%$** (`source-reported`).
     - $t$-statistic: **$-0.01$** (a clean statistical null) (`source-reported`).
     - **Comparison:** The cohort mean ($-0.07\%$) does not exceed the pooled placebo mean ($-0.01\%$), confirming that spin-off events generate zero excess return above unconditioned equity drift (`source-reported`).
   - **Same-Name Post-Event Placebo:**
     - Sample Size ($N$): $515$ random non-event windows drawn from the same spincos' histories $\ge 60$ trading days after $t_0$ (`source-reported`).
     - Mean CAR: **$-1.57\%$** (`source-reported`).
     - $t$-statistic: **$-2.24$** (`source-reported`).
     - **Finding:** Newly listed spincos tend to drift downward during their first operational year; the event window fails to outperform even this negative baseline once transaction frictions are deducted (`source-reported`).

4. **Secondary Horizon & Contributor Ablation:**
   - **3-Month Window (`car_p1_p63`):** Gross mean CAR is **$+1.91\%$** with $t = +0.58$ and median $+0.92\%$. While nominally positive, the effect is statistically indistinguishable from zero ($|t| < 2.0$) and falls entirely within the placebo noise band (`source-reported`).
   - **Top-5 Contributor Removal (`drop_top_contributors`, $k = 5$):** Removing the 5 largest absolute contributors reduces the cohort to $N = 99$, yielding a gross mean CAR of **$-0.47\%$** ($t = -0.24$). The absence of positive skew confirms that no latent edge was masked by idiosyncratic negative outliers (`source-reported`).
   - **Friction Sensitivity:** Net CAR at 20 bps is $-0.27\%$; net CAR at 40 bps stress collapses to **$-0.47\%$** (`source-reported`).

5. **Official Gate Evaluation (`evaluate_gate`):**
   - $N \ge 30$: **PASS** ($N = 104$) (`source-reported`).
   - After-Cost Expectancy $>0$ with $|t| \ge 2.0$: **FAIL** (Net $-0.27\%$, $t = -0.03$) (`source-reported`).
   - OOS Sign Stability (Both $N \ge 10$, same sign): **FAIL** (IS $-0.22\%$, OOS $+0.05\%$, sign flip) (`source-reported`).
   - Placebo Null & Superiority: **FAIL** (Cohort $-0.07\%$ does not beat pooled placebo $-0.01\%$) (`source-reported`).
   - Too-Good Tripwire: Not triggered (`source-reported`).
   - **Final Verdict:** **KILL (Decayed Effect / Anomaly in Noise)** (`source-reported`).

### Independently reproduced

- Not independently reproduced. The empirical metrics cited above represent the primary source's auditable codebase and outputs, verified through direct inspection of `JonathanBeck1/falsification-campaign` at commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`.

### Negative evidence

- The classical Cusatis, Miles & Woolridge (1993) and Greenblatt (1997) spin-off abnormal return has decayed to complete statistical noise in modern US equity markets (2015–2025) (`source-reported`).
- Institutional capitalization and specialized arbitrage vehicles (e.g., ETF `CSD`) actively front-run or warehouse distribution-day supply imbalances, eliminating multi-week post-distribution excess drift (`source-reported`).
- Newly listed spincos incur meaningful bid-ask spreads (modeled at 20 bps to 40 bps round-trip), converting gross noise into guaranteed net losses (`source-reported`).
- Post-event drift across the broader first year exhibits systematic negative performance ($-1.57\%$, $t = -2.24$), demonstrating that unselected spincos underperform the broader market (`source-reported`).

## Falsification plan

To falsify this negative verdict and demonstrate that a deployable spin-off anomaly persists, future empirical research must satisfy the following pre-declared test suite:

1. **Sub-Cohort Institutional Constraint Partitioning:**
   - **Test Design:** Segment the Form 10-12B universe into spincos where parent institutional ownership $>70\%$ and parent is an S&P 500 constituent, but the spinco market capitalization falls below the S&P 600 SmallCap cutoff ($<\$1\text{B}$), maximizing forced selling asymmetry (`research-proposed`).
   - **Threshold:** The constrained sub-cohort ($N \ge 30$) must achieve an after-cost net CAR $> +1.50\%$ with $t \ge +2.50$ across $[t_0+1, t_0+21]$ under a realistic 50 bps execution friction model (`research-defined falsification threshold`).
   - **Action:** If the sub-cohort passes, the anomaly survives as a narrow microcap structural flow effect rather than a broad market anomaly (`research-proposed`).

2. **Intraday Liquidity Absorption Horizon Test:**
   - **Test Design:** Measure abnormal returns over minute-bar intraday horizons on day $t_0$ ($[t_0^{\text{open}}, t_0^{\text{10:30}}]$ vs $[t_0^{\text{10:30}}, t_0^{\text{close}}]$) (`research-proposed`).
   - **Threshold:** Falsification of decay requires demonstrating that selling pressure is concentrated in the opening 60 minutes, yielding an intraday rebound with annualized Sharpe $\ge 1.50$ net of maker/taker execution fees (`research-defined falsification threshold`).
   - **Action:** If intraday mean-reversion is statistically confirmed, the drift horizon has compressed from weeks to hours (`research-proposed`).

3. **Parent vs Spinco Stub Value Spread:**
   - **Test Design:** Construct a market-neutral long spinco / short parent stub arbitrage portfolio formed at announcement ($t_{\text{announce}}$) through completion ($t_0$) (`research-proposed`).
   - **Threshold:** Annualized spread Sharpe $> 1.0$ net of borrow fees on the parent and transaction friction on the spinco (`research-defined falsification threshold`).
   - **Action:** If positive, value creation occurs during the pre-spin distribution announcement phase rather than post-distribution trading (`research-proposed`).

## Crypto portability

- **Portability Classification:** `not applicable` (direct) / `adapted` / `unproven` (synthetic analogy).
- **Direct Portability Barrier:** Corporate spin-offs via SEC Form 10-12B are legally defined corporate reorganizations governed by US securities law; they have no direct equivalent in decentralized spot or perpetual crypto markets (`research-proposed`).
- **Synthetic Analogy — Token Hard Forks & Ecosystem Airdrops:**
  - The closest structural mechanisms in digital assets are **blockchain hard forks** (e.g., BTC/BCH, ETH/ETC) and **ecosystem token airdrops** (e.g., governance token distributions to protocol liquidity providers) (`research-proposed`).
  - In both crypto instances, recipients receive a new asset pro-rata to existing holdings with zero acquisition cost, creating severe initial liquidation pressure from market participants who view the token as unearned cash flow (`research-proposed`).
- **Empirical Crypto Hazards:**
  - Unlike equity spincos which are operating corporate entities, newly airdropped tokens frequently suffer hyper-inflationary sell-offs and continuous token unlock dilution, resulting in sharp, persistent negative drift rather than recovery (`research-proposed`).
  - Without SEC disclosure protections, wash trading and predatory MEV front-running at decentralized pool inception severely distort opening bar prices (`research-proposed`).
  - Portability of the equity forced-selling thesis to token airdrops remains completely unproven and historically prone to catastrophic capital loss (`research-proposed`).

## Limitations

- **Coarseness of 10-12B Filing Filter:** Form 10-12B is an SEC registration document that encompasses certain non-pro-rata corporate carve-outs, equity reorganizations, and spinco holding company restructurings alongside classic tax-free pro-rata dividend distributions (`source-reported`).
- **Missing Ticker Resolution:** 18 filers were dropped due to Yahoo Finance ticker mapping failures or historical unmappability following corporate mergers, representing a missingness limitation (`source-reported`).
- **When-Issued Market Contamination:** Certain high-profile spincos trade on a "when-issued" basis prior to distribution; entering at $t_0$ close mitigates when-issued noise but may miss opening-session dislocations (`source-reported`).
- **Lack of Multi-Factor Benchmarking:** The study utilizes a single-factor SPY market adjustment ($\beta = 1$); however, given that the crude unadjusted CAR is negative ($-0.07\%$), richer multi-factor models (e.g., Fama-French 5-factor) would not rescue the strategy (`source-reported`).
- **Falsification Scope:** The findings falsify the tradeability of broad spin-off drift on retail-accessible daily data from 2015–2025; they do not disprove historical pre-2000 profitability or complex fundamental distressed activism (`source-reported`).

## Implementation status

- **Status:** `not-implemented`.
- No prototype, backtest harness, or live trading components have been constructed in PyBroker, NautilusTrader, or related production repositories.
- This research record captures an empirical falsification from external peer research; implementation is neither requested nor authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record represents an authoritative negative result documenting the post-publication decay of a famous equity market anomaly. It does not constitute approval for live capital deployment, paper trading, or backtest integration.

## Related Wiki records

- [[quant/sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05]] — Empirical analysis of SEC regulatory filings (Form 4 insider trading) as potential equity alpha catalysts.
- [[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]] — Empirical falsification of structural index-fund flow anomalies and modern index-effect decay.
- [[quant/buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13]] — Empirical falsification of SEC Form 8-K Item 8.01 corporate share repurchase drift as a small-cap illiquidity mirage.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] — Empirical falsification of corporate earnings event options strategies under realistic bid-ask friction.

## Sources

- Jonathan Beck (`JonathanBeck1`), *"A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced"*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: https://github.com/JonathanBeck1/falsification-campaign
- Jonathan Beck, *"Decision: Spin-off Post-Event Drift (T42)"*, `research/spinoff_drift_decision.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/spinoff_drift_decision.md
- Jonathan Beck, *"Pre-registration: Spinoff Post-Event Drift (T42)"*, `research/spinoff_drift_preregistration.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/spinoff_drift_preregistration.md
- Jonathan Beck, Python Implementation Files: `src/trader/catalysts/spinoff_drift.py`, `scripts/run_spinoff_drift_study.py`, and `tests/financial/test_spinoff_drift.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`).
- Jonathan Beck, *"The negative result: an empirical falsification of retail-accessible trading edges"*, `research/PAPER_DRAFT.md`, Section 4.1, 4.2, 8.1, Tables 1 & 2 in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md
- Patrick J. Cusatis, James A. Miles, and J. Randall Woolridge, *"Restructuring Through Spinoffs: The Stock Market Pays"*, *Journal of Financial Economics*, Vol. 33, No. 3 (1993), pp. 293–311. DOI: 10.1016/0304-405X(93)90005-B
- Joel Greenblatt, *"You Can Be a Stock Market Genius: Uncover the Secret Hiding Places of Stock Market Profits"*, Simon & Schuster, New York (1997), Chapter 3, pp. 47–84. ISBN: 978-0684840048
- John J. McConnell, Scott B. Sibley, and Wei Xu, *"Spinoffs: 20 Years Later"*, *Journal of Financial Economics*, Vol. 116, No. 1 (2015), pp. 118–137. DOI: 10.1016/j.jfineco.2014.12.001
- R. David McLean and Jeffrey Pontiff, *"Does Academic Research Destroy Stock Return Predictability?"*, *The Journal of Finance*, Vol. 71, No. 1 (2016), pp. 5–32. DOI: 10.1111/jofi.12365
