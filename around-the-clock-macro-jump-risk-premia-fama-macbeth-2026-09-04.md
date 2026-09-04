---
schema: strategy-research-record-v1
title: "Around-the-Clock Macro Jump Risk Premia: Interpretable Systematic Jump Factor-Mimicking Portfolios"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - jump-risk
  - fama-macbeth
  - factor-mimicking-portfolio
  - high-frequency
  - around-the-clock
  - overnight-returns
  - macro-announcements
  - llm-reasoning
  - continuous-time
status: research-only
confidence: medium
source_as_of: 2026-04-15
sources:
  - https://arxiv.org/abs/2604.13458
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Around-the-Clock Macro Jump Risk Premia: Interpretable Systematic Jump Factor-Mimicking Portfolios

## Provenance

- **Primary Source**: arXiv:2604.13458v1 [q-fin.GN, q-fin.PM, q-fin.RM], submitted April 15, 2026.
- **Author**: Songrun He (Olin Business School, Washington University in St. Louis; email: `h.songrun@wustl.edu`).
- **Title**: "Interpretable Systematic Risk around the Clock"
- **Primary DOI / Canonical URL**: [https://doi.org/10.48550/arXiv.2604.13458](https://doi.org/10.48550/arXiv.2604.13458) / [https://arxiv.org/abs/2604.13458](https://arxiv.org/abs/2604.13458)
- **Full Text / TeX Source**: Full text HTML accessible at `https://arxiv.org/html/2604.13458v1`; LaTeX source package inspected at `https://arxiv.org/src/2604.13458` (`main.tex`, `references.bib`).
- **Data As-Of**: September 1, 1997 to May 31, 2020 (~23 years). High-frequency TAQ millisecond data merged with CRSP and Compustat (`idxcst_his` table) covering 3,488 unique S&P 1500 constituent firms; CME S&P 500 E-mini futures tick data; Dow Jones Newswires real-time text feed; BEA and BLS scheduled macroeconomic release schedules. Out-of-sample strategy evaluation window: January 2007 to May 2020 (161 monthly rebalances).

## Economic mechanism

### Source-reported

In standard continuous-time asset pricing theory (Merton, 1973; Aït-Sahalia, Jacod & Xiu, 2025; Bollerslev et al., 2016), systematic market risk comprises continuous (diffusive) price innovations and discontinuous jump innovations. Jump events represent sharp realizations of major aggregate shocks with high signal-to-noise ratios. Prior empirical literature focusing solely on regular U.S. intraday cash equity trading hours (9:30 a.m. to 4:00 p.m. ET) concluded that monetary policy news is the primary driver of priced jump risk (Aleti & Bollerslev, 2025).

He (2026) presents the first comprehensive "around-the-clock" analysis by coupling intraday cash equity returns with 24-hour S&P 500 E-mini futures. The author demonstrates that:
1. **Omitted Variable Bias of Intraday-Only Analysis**: Over 70% of aggregate systematic equity jumps occur outside regular cash trading hours (overnight and pre-market). In fact, U.S. macroeconomic data releases (Non-farm payrolls, CPI, PPI, GDP) are systematically published at 8:30 a.m. ET—one hour before the cash market opens. Consequently, intraday-only analyses omit the primary news cluster and misidentify or attenuate risk premia.
2. **Economic Heterogeneity Across Jump Narratives**: Using an open-source reasoning LLM (Qwen3-235B-A22B with test-time compute) to retrieve and categorize the news narratives driving 15-minute systematic jumps, the paper reveals sharp heterogeneity in risk compensation across five distinct economic categories:
   - *U.S. Macro Data Surprises*: Commands the largest and most persistent risk premium (annualized premium of +3.65%, Sharpe ratio 0.78), driven by intertemporal hedging demands against shocks to the stochastic investment opportunity set in an ICAPM economy.
   - *U.S. Policy Actions*: Displays large volatility and asymmetric positive skew (>78% of jumps are positive), consistent with a "Fed put" mitigating downside tail risk, but carries limited ex-ante compensation (+0.40% annualized) once macro jumps are controlled for.
   - *International Market Spillovers*: Generates the largest volume of jump events (32.88% of total jumps), but provides statistically insignificant risk compensation (+1.91% annualized, Sharpe 0.26).
   - *Corporate Bellwethers*: Accounts for 15.75% of jumps (+2.77% annualized return, Sharpe 0.48), reflecting granular origins of aggregate volatility, but is noisy and statistically insignificant.
   - *Geopolitical & Security Events*: Accounts for 12.05% of jumps with negative realized compensation (-0.92% annualized).
3. **Priced Jump Mechanism vs. Pre-Scheduled Calendar Announcements**: The macro jump premium does not merely replicate pre-scheduled announcement drift (Ai & Bansal, 2018; Lucca & Moench, 2015). A calendar-holding strategy earns a Sharpe ratio of only 0.33. The alpha arises specifically from the continuous-time factor-mimicking portfolio isolating stocks' differential beta sensitivity to large, realized macroeconomic surprises.

### Research interpretation

The strategy constructs a tradable pure-play factor-mimicking portfolio that isolates exposure to macroeconomic jump risk while immunizing the portfolio against continuous market beta and non-macro jump risks.
- **Cross-Sectional Dispersion in Macro Jump Sensitivity**: Assets exhibit persistent heterogeneity in their sensitivity ($\beta^{J,\text{macro}}$) to unexpected macroeconomic shocks (e.g. cyclical vs. defensive firms, capital-intensive vs. cash-flow-resilient firms).
- **Pure-Play Fama-MacBeth Projection**: Applying the continuous-time Fama-MacBeth projection matrix $W_t = \widehat{\beta}_t (\widehat{\beta}_t' \widehat{\beta}_t)^{-1}$ across the real-time S&P 1500 cross-section isolates unit exposure to the target jump risk with zero net continuous market exposure and zero net exposure to non-target jump categories, achieving the minimum $L_2$ norm of portfolio weights.
- **Real-Time Topic Allocation**: By dynamically selecting the most statistically significant jump risk topic (or locking into the structurally dominant Macro Data Surprise topic) at each annual horizon, an investor harvests the persistent intertemporal macro hedging premium while maintaining near-zero net market beta and low portfolio turnover (~10% per month).

## Signal

### Mathematical Formulation

1. **High-Frequency Jump Detection (Source-reported)**:
   For each 15-minute interval $i$ on day $t$ with sampling length $\Delta_n$, factor return $F_{t,i}$ is classified as a systematic jump if:
   $$|F_{t,i}| > u_n \times \tau_i \times \sqrt{TV_t} \times \Delta_n^{\varpi}$$
   and $|F_{t,i}| > 0.5\%$, where:
   - Truncation threshold parameter $u_n = 3$ (source-reported).
   - Exponent parameter $\varpi = 0.49$ (source-reported).
   - $\tau_i$ is the time-of-day diurnal volatility adjustment factor (source-reported).
   - $TV_t$ is the daily truncated variance:
     $$TV_t = \frac{\pi}{2} \frac{n}{n-1} \sum_{i=2}^n |F_{t,i-1}| |F_{t,i}| \quad \text{subject to } |F_{t,i}| \le u_n \Delta_n^{\varpi}$$

2. **LLM Narrative Retrieval & Topic Assignment (Source-reported)**:
   - For each jump interval, Dow Jones Newswires stories released in the contemporaneous 15-minute window are fed to the Qwen3-235B-A22B reasoning LLM (Thinking mode enabled).
   - **Prompt 1 (Retrieval)**: Identifies whether news caused the jump and generates a causal explanation.
   - **Prompt 2 (Taxonomy)**: Derives 5 mutually exclusive topic categories plus an unclassified category:
     1. *U.S. Policy Actions (Monetary, Fiscal, & Political)*
     2. *U.S. Macro Data Surprises*
     3. *Geopolitical & Security Events*
     4. *Corporate Earnings & Guidance*
     5. *International Market Spillovers*
     6. *None of the Above (Unclassified)*
   - **Prompt 3 (Assignment)**: Assigns each jump event timestamp $\tau$ to a specific category $k \in \{1, \dots, 5\}$.

3. **Two-Pass Beta Estimation (Source-reported)**:
   - **Continuous Beta ($\beta_t^C$)**: Estimated on 15-minute continuous (non-jump) factor and stock returns using a 1-month rolling window ($l = 1$ month, updated monthly):
     $$\widehat{\beta}_{m,t}^C = \frac{\sum_{s \in \mathcal{T}_t^C} dF_s dR_{m,s}}{\sum_{s \in \mathcal{T}_t^C} (dF_s)^2}$$
   - **Jump Beta ($\beta_t^{J,k}$)**: Estimated on isolated jump timestamps $\mathcal{T}^{J,k}$ using an expanding historical window of all jumps up to month-end $t$ (updated annually at December month-end, source-reported):
     $$\widehat{\beta}_{m,t}^{J,k} = \frac{\sum_{s \le t, s \in \mathcal{T}^{J,k}} dF_s dR_{m,s}}{\sum_{s \le t, s \in \mathcal{T}^{J,k}} (dF_s)^2}$$
   - Stack full beta matrix for all $N_t$ active assets:
     $$\widehat{\beta}_t = [\mathbf{1}, \widehat{\beta}_t^C, \widehat{\beta}_t^{J,1}, \dots, \widehat{\beta}_t^{J,K}] \in \mathbb{R}^{N_t \times (K+2)}$$

4. **Pure-Play Factor-Mimicking Weight Matrix (Source-reported)**:
   $$W_t = \widehat{\beta}_t (\widehat{\beta}_t' \widehat{\beta}_t)^{-1} \in \mathbb{R}^{N_t \times (K+2)}$$
   Each column $w_{t,j}$ corresponds to a pure-play portfolio satisfying:
   $$\mathbf{1}' w_{t,j} = 0, \quad \widehat{\beta}_t' w_{t,j} = e_j$$
   where $e_j$ is the $j$-th canonical basis vector. Thus, the portfolio has weights summing to 0 (dollar-neutral), unit beta exposure to factor $j$, and exactly zero beta exposure to all other $K+1$ factors.

5. **Real-Time Allocation Rule & Operational Parameters**:
   - **Strategy Mode A (Static Macro Jump Pure-Play)**: Allocate to column $k = 2$ (Macro Data Surprises pure-play portfolio) at all times (`source-reported`).
   - **Strategy Mode B (Real-Time Dynamic Topic Selection)**: At each December month-end, evaluate the historical annualized Sharpe ratio / $t$-statistic of each jump factor-mimicking portfolio using Equation (11). Allocate 100% to the topic with the maximum in-sample Sharpe ratio for the entirety of the next calendar year (`source-reported`).
   - **Rebalancing Cadence**: Monthly rebalance of portfolio weights based on rolling 1-month continuous betas and prevailing jump betas (`source-reported`).
   - **Signal Formation Timestamp**: Close of the last trading day of month $t-1$ (`source-reported`).
   - **Execution Timestamp**: First trading bar open of month $t$ (`research-proposed`; source evaluates on monthly holding return series).
   - **Position Sizing**: Dollar-neutral long/short weights from vector $w_{t,j}$. Standard portfolio scaling normalizes gross notional exposure $\sum_{m=1}^{N_t} |w_{m,t,j}| = 2.0$ (100% Long / 100% Short) (`research-proposed`).

## Required data

- **Universe**: S&P 1500 constituent firms, determined point-in-time via Compustat `idxcst_his` table, mapped to CRSP (share codes 10 and 11, NYSE/AMEX/NASDAQ) to eliminate survivorship and look-ahead bias (3,488 unique firms over 1997–2020).
- **Timeframe / Grid**: 15-minute sampled price grid from 09:30 to 16:00 ET for intraday cash equities; continuous 15-minute grid for CME S&P 500 E-mini futures.
- **Fields**:
  - Millisecond trade prints and NBBO quotes from WRDS TAQ (MTAQ 1997–2003, DTAQ 2003–2020) filtered by condition codes (A, B, H, O, R, W) and trade correction codes (00, 01).
  - Daily open, close, split, and dividend adjustments from CRSP.
  - S&P 500 E-mini continuous futures tick data from CME DataMine, rolled forward on liquidity crossover (trade count/volume) with notional contract ratio scaling $n_{t+1} = n_t \times (f_t^1 / f_t^2)$.
  - High-frequency real-time text stream: Dow Jones Newswires with millisecond timestamps.
  - Macro release calendar: Bureau of Labor Statistics (BLS) and Bureau of Economic Analysis (BEA) release dates for NFP, CPI, PPI, and GDP.
- **Missing Data Handling**: Forward-fill prices up to 15-minute grid boundary using previous-tick method; filter trades outside CRSP daily $[BIDLO, ASKHI]$ range (`source-reported`).

## Execution assumptions

- **Signal-to-Order Latency**: Month-end weight computation executed at opening auction of subsequent trading day (`research-proposed`; source calculates monthly calendar returns).
- **Execution Model**: Market-on-open (MOO) or VWAP across large/mid/small cap S&P 1500 universe (`research-proposed`).
- **Portfolio Turnover**: Approximately **10.0% per month** (0.10 monthly turnover fraction, source-reported in Table 7), because jump betas are updated annually via expanding window and continuous betas exhibit strong autocorrelation across monthly rolling windows.
- **Transaction Costs & Fees**:
  - Source reports gross returns and tests three realistic net cost tiers (Table 7) following Frazzini, Israel & Moskowitz (2018):
    - **10 bps** per dollar traded: net Sharpe ratio **0.93**, net annualized return **5.65%**, annual volatility 6.00%.
    - **20 bps** per dollar traded: net Sharpe ratio **0.91**, net annualized return **5.59%**, annual volatility 6.01%.
    - **50 bps** per dollar traded: net Sharpe ratio **0.85**, net annualized return **5.10%**, annual volatility 6.01%.
- **Short Borrow Constraints**: Primary source assumes unconstrained shorting across S&P 1500. `Research-proposed` operational friction hurdle: small-cap constituents in S&P 600 sleeve may incur positive borrow fees (estimated 30–80 bps annualized); long-short portfolio capacity is high for S&P 500 constituents but subject to borrow locate availability in smaller names.

## Evidence

### Source-reported

All figures below are directly extracted from Section 4 (Tables 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) of He (2026), evaluated over the sample period (September 1997 to May 2020) and out-of-sample trading window (January 2007 to May 2020, 161 monthly rebalances):

#### 1. Jump Distribution and News Attribution (Table 2, Sept 1997 – May 2020)
- Total systematic jumps detected: **730 jumps**.
- Vast majority (~70%) occur overnight.
- **Category Breakdown**:
  - *U.S. Policy Actions*: 51 jumps (6.99% of total), 78.43% positive, Mean return +0.63%, Std 1.12%, $R^2$ variance explained 13.68%.
  - *U.S. Macro Data Surprises*: 152 jumps (20.82% of total), 48.68% positive, Mean return -0.06%, Std 0.85%, $R^2$ variance explained 18.00%.
  - *Geopolitical & Security Events*: 88 jumps (12.05% of total), 40.91% positive, Mean return -0.25%, Std 0.95%, $R^2$ variance explained 13.92%.
  - *Corporate Earnings & Guidance*: 115 jumps (15.75% of total), 46.09% positive, Mean return -0.05%, Std 0.86%, $R^2$ variance explained 13.94%.
  - *International Market Spillovers*: 240 jumps (32.88% of total), 42.50% positive, Mean return -0.15%, Std 0.85%, $R^2$ variance explained 29.30%.
  - *None of the Above (Unclassified)*: 64 jumps (8.77% of total), 26.56% positive, Mean return -0.29%, Std 0.83%, $R^2$ 8.06%.
  - *Unattributable (No news identified)*: 20 jumps (2.74% of total), 50.00% positive, Mean return +0.01%, Std 0.99%, $R^2$ 3.09%.
- Over 97.26% (710 of 730) of systematic market jumps are successfully attributed to concurrent newswire stories.

#### 2. Risk Premia of Factor-Mimicking Portfolios (Table 4, Jan 2007 – May 2020, 161 Months)
- **Panel A: Around-the-Clock Specification**:
  - *Continuous Factor*: Annualized Risk Premium **4.14%** (SE 5.29%), Sharpe Ratio **0.21**.
  - *Policy Jump Factor*: Annualized Risk Premium **0.40%** (SE 1.79%), Sharpe Ratio **0.06**.
  - *Macro Jump Factor*: Annualized Risk Premium **3.65%** (SE 1.32%), $t$-statistic **2.77**, Sharpe Ratio **0.78**.
  - *Geopolitics Jump Factor*: Annualized Risk Premium **-0.92%** (SE 1.21%), Sharpe Ratio **-0.21**.
  - *Corporate Jump Factor*: Annualized Risk Premium **2.77%** (SE 1.59%), Sharpe Ratio **0.48**.
  - *International Jump Factor*: Annualized Risk Premium **1.91%** (SE 2.04%), Sharpe Ratio **0.26**.
  - **Realtime Selected Topic Portfolio**: Annualized Risk Premium **5.72%** (SE 1.64%), $t$-statistic **3.49**, Sharpe Ratio **0.95**.
  - *Benchmark Market Excess Return (Mkt-RF)*: Annualized Risk Premium **8.48%** (SE 4.35%), Sharpe Ratio **0.53**.
- **Panel B: Intraday-Only Analysis Failure**:
  - Continuous: 4.02% (SE 5.20%), SR 0.21.
  - Policy: 2.27% (SE 1.30%), SR 0.48.
  - Macro: 2.16% (SE 1.49%), SR 0.40 (statistically insignificant).
  - Geopolitics: 2.05% (SE 1.25%), SR 0.45.
  - Corporate: -0.78% (SE 1.08%), SR -0.20.
  - International: -1.23% (SE 0.81%), SR -0.42.
  - Realtime Topic: 2.69% (SE 1.26%), SR 0.58 (underperforms market; drops to 0.28 under monthly selection).

#### 3. Overnight vs. Intraday Risk Premia Decomposition (Table 5)
- In market excess returns, overnight holding earns **+7.68% / year** (SE 2.31%, $p < 0.01$), whereas intraday holding earns **-0.25% / year** (SE 3.39%, insignificant).
- Overnight jumps command **+7.96% / year** (SE 3.41%, $p < 0.05$), while intraday jumps command only **+0.51% / year** (SE 2.64%, insignificant).

#### 4. Factor Regressions and Alphas (Table 6, Jan 2007 – May 2020)
- **Macro Topic Pure-Play Factor**:
  - CAPM Alpha: **+0.30% / month** (SE 0.10%, $p < 0.01$, annualized ~3.60%).
  - Fama-French 3-Factor Alpha: **+0.31% / month** (SE 0.10%, $p < 0.01$).
  - Fama-French 6-Factor Alpha (Mkt, SMB, HML, RMW, CMA, MOM): **+0.28% / month** (SE 0.09%, $p < 0.01$, annualized ~3.36%).
- **Real-Time Selected Topic Factor**:
  - CAPM Alpha: **+0.48% / month** (SE 0.12%, $p < 0.01$, annualized ~5.76%).
  - Fama-French 3-Factor Alpha: **+0.41% / month** (SE 0.11%, $p < 0.01$).
  - Fama-French 6-Factor Alpha: **+0.29% / month** (SE 0.10%, $p < 0.05$, annualized ~3.48%).

#### 5. Net-of-Transaction-Cost Performance (Table 7)
- Turnover is stable at **10% monthly**.
- $c = 10$ bps: Net Sharpe **0.93**, Ann Return **5.65%**, Vol **6.00%**.
- $c = 20$ bps: Net Sharpe **0.91**, Ann Return **5.59%**, Vol **6.01%**.
- $c = 50$ bps: Net Sharpe **0.85**, Ann Return **5.10%**, Vol **6.01%**.

#### 6. Rigorous Control Benchmarks (Tables 8 & 9)
- **ChronoBERT (Strict Out-of-Sample / Pre-2000 Checkpoint)**: Macro Ann RP 3.10% (SE 1.28%, SR 0.68); Real-time topic Ann RP 4.02% (SE 1.62%, SR 0.68). Agreement with baseline is 75.4%.
- **LDA Topic Model (Word Counts)**: Real-time topic Sharpe ratio collapses to **0.28**, failing to outperform market.
- **Ablation of Reasoning (Qwen3 Non-Think)**: Attribution rate falls to 69.7%; Real-time topic Sharpe ratio collapses from **0.95** to **0.39**.
- **Placebo Test (Uniform Random Assignment)**: Mean placebo Sharpe ratio across 20 seeds is **0.31** (maximum 0.71), demonstrating that LLM narrative classification contains genuine economic information.

### Independently reproduced

Not independently reproduced. All metrics, coefficients, and tables are third-party empirical findings reported by Songrun He (arXiv:2604.13458v1, April 2026).

### Negative evidence

1. **Intraday-Only Data Collapse**: When restricted to regular U.S. trading hours (9:30 a.m. to 4:00 p.m. ET), the macroeconomic jump risk premium is attenuated from 3.65% ($t = 2.77$) down to 2.16% ($t = 1.45$, statistically insignificant), and the real-time strategy Sharpe ratio plummets from 0.95 to 0.28 (Table 4, Panel B). Strategies attempting to isolate macro jump risk using only cash-market intraday data fail.
2. **Pre-Scheduled Macro Announcements Failure**: Holding a passive market portfolio during pre-scheduled BLS/BEA macro announcement windows yields a Sharpe ratio of only 0.33. Factor-mimicking portfolios formed simply on pre-scheduled calendar announcement dates yield negligible and statistically insignificant alpha (+0.02%/month, $t = 0.12$, Table 11). The alpha requires conditioning on actual continuous-time price jumps and contemporaneous causal narratives rather than calendar dates.
3. **Traditional Word-Count / LDA Failure**: Traditional NLP topic models (LDA) yield noisy classifications with only 60% agreement with LLM ground truth, degrading real-time strategy Sharpe ratio to 0.28 (Table 8, Panel B).
4. **Non-Reasoning LLM Degradation**: Removing test-time reasoning compute (switching off thinking tokens) causes LLM news attribution failure for >30% of jumps and attenuates strategy Sharpe ratio to 0.39 (Table 9).

## Falsification plan

To falsify the hypothesis that around-the-clock macro jump risk earns a persistent, tradable risk premium:

1. **Post-2020 Out-of-Sample Audit**:
   - Reconstruct the high-frequency S&P 1500 and E-mini futures return panels over June 2020 to December 2025 (`research-proposed` out-of-sample window).
   - Re-estimate the Fama-MacBeth macro jump factor-mimicking portfolio $w_{t,\text{macro}}$.
   - `Research-defined falsification threshold`: Out-of-sample annualized Sharpe ratio $< 0.35$ or Fama-French 6-factor alpha $t$-statistic $< 1.96$ over a minimum 36-month test period.
2. **Placebo Shuffled-Narrative Permutation Test**:
   - Randomly permute the assigned jump category labels across the 730 jump events 500 times (`research-proposed`).
   - `Research-defined falsification threshold`: If the realized Sharpe ratio of the true LLM-classified macro portfolio falls below the 90th percentile of the randomized placebo distribution, reject the hypothesis that LLM narrative reasoning adds genuine economic value over random clustering.
3. **Execution Friction & Short-Borrow Stress Test**:
   - Apply realistic stock-level execution frictions: 10 bps round-trip trading costs for top 500 liquid stocks, 35 bps for remaining mid/small caps, plus annualized short-borrow rebate/fee of 50–150 bps on hard-to-borrow constituents (`research-proposed` stress test).
   - `Research-defined falsification threshold`: Net-of-friction Fama-French 6-factor alpha drops below 0.10% per month ($< 1.20\%$ annualized) or loses statistical significance ($t < 1.65$).
4. **Subperiod Stability & Recession Shock Breakdown**:
   - Split the sample into monetary tightening (2022–2023) vs. easing (2020–2021) regimes.
   - `Research-defined falsification threshold`: If macro jump factor returns exhibit sign-reversal (cumulative return $< -5.0\%$) over any consecutive 12-month window during macroeconomic distress, the thesis of stable intertemporal hedging premium is falsified.

## Crypto portability

- **Portability Status**: `adapted` / `unproven`.
- **Primary Source Demonstration**: The cited primary source investigates exclusively U.S. equities (S&P 1500) and CME equity index futures. Porting to cryptocurrency markets is a `research-proposed` adaptation and remains empirically unproven.
- **Crypto-Specific Adaptation Requirements**:
  1. *Continuous 24/7/365 Price Discovery*: In contrast to equities where regular trading hours are restricted and overnight futures serve as the off-hours proxy, crypto spot and perpetual markets trade 24/7/365. Bipower variation / truncated variance jump filters must be adapted to continuous rolling windows without market-open diurnal spikes.
  2. *Macro Sensitivity in Crypto*: High-frequency studies document that Bitcoin and major perpetual contracts exhibit extreme sensitivity to U.S. macro releases (NFP, CPI, FOMC rate announcements). A cross-sectional crypto factor-mimicking portfolio could be formed across the top 50 perpetual contracts (Binance/OKX/Bybit) to isolate cross-sectional macro jump beta ($\beta_i^{J,\text{macro}}$).
  3. *Perpetual Funding Rate Drag*: In crypto perpetuals, maintaining long/short pure-play positions across high-beta vs. low-beta tokens creates continuous 8-hour funding rate cash-flow obligations. The pure-play weighting matrix must incorporate funding rate constraints to prevent funding drag from eroding the jump premium.
  4. *Venue Fragmentation & Microstructure Noise*: Crypto trade prints across multiple decentralized and centralized venues suffer from fragmented order books and exchange outages during extreme macro releases, necessitating robust tick-level price median filtering.

## Limitations

- **Source Quality**: Primary source is a high-rigor academic working paper by Songrun He (Washington University in St. Louis, April 2026), built directly on forthcoming methodology in *The Review of Financial Studies* (Aït-Sahalia, Jacod & Xiu, 2025).
- **Execution Practicality**: The pure-play factor-mimicking portfolio requires holding a long-short portfolio across up to 1,500 individual equities. While monthly turnover is modest (~10%), shorting smaller-cap constituents of the S&P 1500 may incur borrow fees or locate constraints not modeled in the paper's baseline gross backtest (though confirmed robust at 50 bps transaction costs in Table 7).
- **Sample Termination in May 2020**: High-frequency constituent panel data terminated in May 2020 due to WRDS removal of Compustat's `idxcst_his` table; out-of-sample performance through the 2022–2024 inflation/rate cycle remains unverified in this paper.
- **Compute Overhead**: Real-time continuous narrative classification requires hosting a 235B-parameter reasoning LLM with multi-GPU infrastructure (4x H100 80GB), creating an operational barrier relative to simple rule-based technical indicators.

## Implementation status

- `not-implemented`. No implementation exists in our PyBroker or Nautilus research stacks.
- This research capture serves strictly as upstream theoretical and empirical documentation.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record does not constitute authorization for deployment in paper trading, testnet, or live trading environments. Any implementation requires subsequent independent data pipeline verification, cross-sectional portfolio construction testing, and formal risk review.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

1. Songrun He, *"Interpretable Systematic Risk around the Clock"*, arXiv preprint `arXiv:2604.13458v1 [q-fin.GN, q-fin.PM, q-fin.RM]`, submitted April 15, 2026. DOI: [10.48550/arXiv.2604.13458](https://doi.org/10.48550/arXiv.2604.13458). Full text: [https://arxiv.org/html/2604.13458v1](https://arxiv.org/html/2604.13458v1). LaTeX source: `https://arxiv.org/src/2604.13458`.
2. Y. Aït-Sahalia, J. Jacod, and D. Xiu, *"Continuous-time Fama-MacBeth regressions"*, *The Review of Financial Studies*, forthcoming 2025.
3. S. Aleti and T. Bollerslev, *"News and asset pricing: a high-frequency anatomy of the SDF"*, *The Review of Financial Studies*, Vol. 38, No. 3, pp. 712–759, 2025. DOI: [10.1093/rfs/hhae054](https://doi.org/10.1093/rfs/hhae054).
4. T. Bollerslev, S. Z. Li, and V. Todorov, *"Roughing up beta: continuous versus discontinuous betas and the cross section of expected stock returns"*, *Journal of Financial Economics*, Vol. 120, No. 3, pp. 464–490, 2016. DOI: [10.1016/j.jfineco.2016.02.008](https://doi.org/10.1016/j.jfineco.2016.02.008).
5. A. Frazzini, R. Israel, and T. J. Moskowitz, *"Trading costs"*, SSRN Working Paper No. 3229719, 2018. DOI: [10.2139/ssrn.3229719](https://doi.org/10.2139/ssrn.3229719).
