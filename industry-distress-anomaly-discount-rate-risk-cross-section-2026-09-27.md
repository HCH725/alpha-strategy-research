---
schema: strategy-research-record-v1
title: "Industry Distress Anomaly — Cross-Sectional Equity Return Spread and Competition-Distress Discount-Rate Feedback (NBER WP 35513, Chen, Dou, Guo, Ji, July 2026)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - industry-level
  - equity
  - distress-anomaly
  - discount-rate-risk
status: research-only
confidence: medium
source_as_of: 2026-07-01
sources:
  - "https://www.nber.org/papers/w35513 — NBER Working Paper 35513, 'Industry Distress Anomaly', by Hui Chen, Winston Wei Dou, Hongye Guo, and Yan Ji (July 2026)"
  - "https://doi.org/10.3386/w35513 — canonical DOI (resolves to full text PDF)"
  - "http://www.nber.org/system/files/working_papers/w35513/w35513.pdf — full text PDF (1,176,796 bytes, SHA-256 1a57635562c79ffc7936da03345b9b965bae7a653890869c220faa65c1c3e924, 63 pages)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Industry Distress Anomaly — Cross-Sectional Equity Return Spread and Competition-Distress Discount-Rate Feedback

## Provenance

- **Primary source:** Hui Chen, Winston Wei Dou, Hongye Guo, and Yan Ji, *"Industry Distress Anomaly"*, **National Bureau of Economic Research (NBER) Working Paper Series**, Working Paper 35513, July 2026; JEL No. C73, G12, L13, O33.
- **Canonical landing page:** `http://www.nber.org/papers/w35513`
- **Canonical DOI:** `10.3386/w35513` (`https://doi.org/10.3386/w35513`, HTTP 302 redirects to PDF).
- **Direct PDF source:** `http://www.nber.org/system/files/working_papers/w35513/w35513.pdf` (1,176,796 bytes, 63 pages, SHA-256 `1a57635562c79ffc7936da03345b9b965bae7a653890869c220faa65c1c3e924`, downloaded and directly inspected on 2026-09-27).
- **Online appendix:** `http://www.nber.org/data-appendix/w35513` (cited in source for auxiliary proofs and tables).
- **Author affiliations (printed on title page):** Hui Chen (MIT Sloan School of Management & NBER, `huichen@mit.edu`); Winston Wei Dou (University of Pennsylvania Wharton School & NBER, `wdou@wharton.upenn.edu`); Hongye Guo (The University of Hong Kong, `silver.hongye.guo@gmail.com`); Yan Ji (Hong Kong University of Science and Technology, `jiy@ust.hk`).
- **Institutional funding / acknowledgements:** Winston Wei Dou acknowledges financial support from Rodney L. White Center for Financial Research, Mack Institute for Innovation Management, and Golub Faculty Scholar Award at Wharton; Yan Ji acknowledges financial support from National Natural Science Foundation of China.
- **Publication status:** NBER working paper, July 2026 (working paper series, not yet peer-reviewed journal publication).
- **Whole-repository source-identity deduplication (inspected 2026-09-27 across all 1,011 `.md` files, `.mimo-worktrees/`, `.agents/`, `.hermes/`, and `coverage_manifest.csv`):**
  - `35513` = 0 hits;
  - `w35513` = 0 hits;
  - `Industry Distress Anomaly` = 0 hits;
  - `Hui Chen` = 0 hits;
  - `competition-distress feedback` = 0 hits;
  - Winston Wei Dou, Hongye Guo, and Yan Ji appear in isolated records for completely unrelated topics (fund trade predictability, earnings cycle correlation neglect, DEX priority gas auctions), with zero topical or methodological overlap.
  - No existing record in the repository or Hermes Wiki Brain carries this source identity or analyzes the industry-level distress anomaly.

## Economic mechanism

### Source-reported

- **The Puzzle:** The authors document that more distressed industries earn significantly lower expected equity returns than healthy industries, despite exhibiting higher leverage, higher default rates, higher credit spreads, and higher CDS spreads. While the firm-level distress anomaly (e.g. Campbell, Hilscher and Szilagyi 2008) is well known, the authors show that the industry-level distress anomaly is distinct: it survives controlling for firm-level distress, but disappears in synthetic placebo industries where firms are randomly reshuffled across industry boundaries.
- **Competition-Distress Feedback:** In oligopolistic product markets with repeated competition, firms face a dynamic trade-off between collusive high profit margins and short-run price undercutting to capture current customer base. When firms become financially distressed, shareholders discount future collusive rents heavily and place greater value on immediate cash flows. Consequently, distressed firms have stronger incentives to cut prices/margins aggressively. This undercutting compresses profit margins across all rivals in the industry, pushing them closer to insolvency and reinforcing aggressive competitive behavior.
- **Discount-Rate Sensitivity Amplification:** In bad aggregate economic states (recessions, elevated macroeconomic uncertainty), aggregate discount rates rise (innovations $\Delta \text{Discount\_rate}_t > 0$), which carries a negative market price of risk ($\zeta = 0.45$ in the calibrated model). A higher discount rate depresses continuation values, triggering two simultaneous effects:
  1. Firms default earlier, increasing financial distress.
  2. The discounted value of future cooperation plummets, breaking collusion and igniting price wars.
  - The competition-distress feedback therefore sharply amplifies the negative impact of discount-rate shocks on industry profit margins and equity values.
- **Cross-Industry Heterogeneity via Idiosyncratic Left-Tail Risk:** The central driver of cross-industry variation is the idiosyncratic left-tail risk ($\nu_{i,t}$) of firms' customer bases (representing creative destruction, disruptive technology, or sudden obsolescence):
  - In industries with **high idiosyncratic left-tail risk**, market leaders are perpetually exposed to large adverse shocks to customer capital. Because future cooperative survival is already precarious, these firms place lower value on future collusion; collusive margins are already depressed in steady state, and the competition-distress feedback loop is **weaker**. Hence, their profit margins and equity values respond **less negatively** to discount-rate shocks.
  - Since discount-rate shocks carry a **negative** market price of risk (countercyclical hedging premium), an asset that is *less negatively exposed* to discount-rate spikes offers less insurance against bad times and therefore demands a **lower expected equity return**.
  - Conversely, healthy industries with **low idiosyncratic left-tail risk** sustain high collusive margins in normal times but experience catastrophic price-war collapse when discount rates spike; this high negative beta to discount-rate shocks makes them risky in bad times, requiring a **higher expected equity return**.

### Research interpretation

- **Hypothesized mechanism (falsifiable form):** Cross-sectional variation in industry-level equity returns reflects differential exposure to aggregate discount-rate shocks mediated by product-market competition-distress feedback. The long-short spread (Long Q1 Healthy / Short Q5 Distressed) harvests a discount-rate risk premium generated by the collapse of collusive margins in healthy oligopolies during macroeconomic discount-rate spikes.
- **Component roles of the strategy:**
  - *Primary sorting signal*: Industry-level financial distress $\text{Distress}_{i,t}$, constructed as the sales-weighted average of firm-level 12-month failure probabilities (Campbell, Hilscher, Szilagyi 2008) across 4-digit SIC industries.
  - *Direction*: Long low-distress industries (Q1) / Short high-distress industries (Q5).
  - *Cross-industry conditioning filter (interaction)*: Market-share balance/imbalance among top firms ($T1 - T3$ imbalance) or ex-ante idiosyncratic left-tail risk ($\nu_{i,t}$). In industries with balanced market shares (tight oligopolies), the competition-distress feedback is strongest, amplifying the long-short spread.
  - *Risk / cost overlay*: Any stop-loss, position-sizing rule, capacity cap, or transaction-cost model is `not stated in source` and must be classified as `research-proposed`.

## Signal

All parameters, formulas, and sort definitions below are **source-reported** from NBER WP 35513 unless explicitly labeled `research-proposed`, `underspecified`, or `data gap`.

- **Signal formation timestamp:** Monthly portfolio formation at the end of month $t$, executed for returns over month $t+1$.
- **Reporting lag / point-in-time rules:**
  - Annual accounting data follows Fama-French (1993) convention: fiscal year ending in calendar year $t-1$ becomes available at the end of June of year $t$.
  - Quarterly accounting data follows Campbell, Hilscher, Szilagyi (2008): a mandatory **two-month reporting lag** is imposed based on the fiscal quarter-end month. For example, quarterly accounting data for fiscal quarters ending in March is first used in portfolios formed at the end of May and matched to June returns.
  - Daily/monthly stock returns and market equity from CRSP are measured up to the end of month $t$.
- **Firm-level distress construction ($\text{Distress}_{ij,t}$):**
  - Defined as the 12-month failure probability following Campbell, Hilscher, Szilagyi (2008), estimated using a dynamic logit model with 8 quarterly explanatory variables:
    $$\text{Distress}_{ij,t} = \frac{1}{1 + \exp(-P_{ij,t})}$$
    where $P_{ij,t}$ is a linear combination of:
    1. $\text{NIMTAAVG}$: exponentially decayed moving average of net income over market-valued total assets.
    2. $\text{TLMTA}$: total liabilities over market-valued total assets.
    3. $\text{EXRETAVG}$: exponentially decayed moving average of monthly log excess return over the S&P 500.
    4. $\text{SIGMA}$: annualized standard deviation of daily stock returns over the prior 3 months.
    5. $\text{RSIZE}$: log ratio of firm market equity to total S&P 500 market value.
    6. $\text{CASHMTA}$: cash and short-term investments over market-valued total assets.
    7. $\text{MB}$: market-to-book equity ratio.
    8. $\text{PRICE}$: log price per share, truncated from above at $\$15$.
- **Industry-level distress construction ($\text{Distress}_{i,t}$):**
  - Industry definition: 4-digit SIC code ($\text{SIC4}$).
  - Filter: at least 10 firms in the industry-year observation (sample average is 123 industries per year, 26.6 firms per industry).
  - Weighting within industry: sales-weighted average of firm-level failure probabilities:
    $$\text{Distress}_{i,t} = \sum_{j \in i} w_{ij,t}^{\text{sales}} \text{Distress}_{ij,t}$$
  - (Robustness check in paper: identical results obtained using the top six firms ranked by sales in each industry).
- **Portfolio construction & Sorting rule:**
  - In each month $t$, all eligible SIC4 industries are sorted into **quintiles (Q1 to Q5)** based on $\text{Distress}_{i,t}$.
  - Q1 = lowest distress industries (healthiest oligopolies).
  - Q5 = highest distress industries (most distressed oligopolies).
  - Within each industry $i$, firm equity returns are **market-capitalization weighted** to form industry equity excess return $R_{i,t+1} - R_{f,t+1}$.
  - Across industries within each quintile, portfolios are **equal-weighted** across industries.
- **Trading Signal / Direction:**
  - **Long:** Quintile 1 (Q1, lowest industry distress).
  - **Short:** Quintile 5 (Q5, highest industry distress).
  - **Holding period:** 1 month, rebalanced monthly.
  - Re-entry / portfolio turnover rules: `not stated in source` (`data gap`); any turnover minimization or buffer-band rule is `research-proposed`.
- **Alternative / Conditioned Signal Variants:**
  1. *Balanced Oligopoly Sort (Table 11 Panel B)*: Split industries into terciles of market-share imbalance ($| \ln(\text{Sales}_{T1}) - \ln(\text{Sales}_{T3}) |$ among the top 6 firms). In Group 1 (balanced market shares), sort into distress terciles T1 vs T3.
  2. *Ex-Ante Left-Tail Risk Sort ($\nu_{i,t}$, Table 5 Panel B)*: Sort industries into quintiles of ex-ante idiosyncratic left-tail risk $\nu_{i,t}$, predicted from panel regressions of realized industry left-tail cash-flow shock frequency on Campbell-Hilscher-Szilagyi industry variables. Long Q1 (low tail risk) / Short Q5 (high tail risk).
- **Reconstruction status:** The portfolio sorting rule, variable definitions, and reporting lags are fully specified; intra-month execution day, order type, and rebalancing turnover controls are `underspecified`.

## Required data

- **Universe:** All ordinary common shares traded on NYSE, Amex, and Nasdaq (CRSP share codes 10 and 11 implied; explicit share-code filter list `not stated in source` $\rightarrow$ `data gap`).
- **Exclusions:** Financial firms (SIC 6000–6999) and Utility firms (SIC 4900–4999) are excluded.
- **Industry screen:** Each industry-year must include at least 10 firms ($\ge 3$ firms for credit spread analyses due to bond data sparsity).
- **Primary data vendors & databases:**
  - **CRSP:** Monthly stock returns, monthly closing prices, shares outstanding, and daily returns (for 3-month return volatility $\text{SIGMA}$).
  - **Compustat North America:** Quarterly accounting items (net income, total liabilities, cash, total assets, stockholders' equity, quarterly sales) and annual accounting items (debt, revenues, COGS).
  - **Robert Shiller website:** Smoothed earnings-price ratio (CAPE/P-E) to construct monthly discount rate series and discount rate shocks $\Delta \text{Discount\_rate}_t$.
  - **Mergent FISD & TRACE:** Corporate bond transaction prices and yields (1973–2018), cleaned via Collin-Dufresne, Goldstein, Martin (2001) and Dick-Nielsen (2009) procedures (used for credit spread verification).
  - **Markit:** 5-year senior unsecured CDS spreads (2001–2018).
  - **Bloomberg:** US interest rate swap rates (1988–2018) as risk-free benchmark for corporate credit spreads.
  - **Bankruptcy databases:** New Generation Research Bankruptcydata.com, UCLA LoPucki Bankruptcy Research Database, PACER, National Archives (1981–2014) for default event calibration.
- **Point-in-time constraints:** Strict two-month reporting lag on quarterly Compustat fundamentals; annual fundamentals updated end of June; monthly CRSP returns matched causally.
- **Missing-data treatment:** Delisting returns included from CRSP; insolvency delisting code 572 treated as default event. Imputation rules beyond standard CRSP/Compustat practices: `not stated in source` (`data gap`).

## Execution assumptions

### Source-reported

- **Execution timing:** Portfolios are formed at the end of month $t$ and held through month $t+1$. Exact execution day, auction vs continuous trading, intraday timing, and order routing: `underspecified`.
- **Order types:** `not stated in source` (`data gap`).
- **Transaction costs, commissions, and bid-ask spreads:** The paper is an empirical macro-finance study; **all reported returns are gross equity excess returns and gross factor alphas**. Zero transaction cost, bid-ask half-spread, or commission model is incorporated into any table.
- **Turnover:** Portfolio turnover is `not stated in source` (`data gap`).
- **Shorting & borrow fees:** Short-selling borrow fees, locate availability, rebate rates, and short-squeeze risks on high-distress Q5 industries are `not stated in source` (`data gap`). High-distress stocks frequently face severe borrow constraints and elevated loan fees in practice.
- **Market impact & capacity:** Capacity and price impact are `not stated in source` (`data gap`).
- **Margin & leverage:** 100% long / 100% short dollar-neutral portfolio implied, with no leverage or financing cost model stated.

### Research-proposed operational assumptions

- Any operational implementation must supply:
  - Fixed cost grid or dynamic effective spread model: `research-proposed` (e.g. 10–25 bps per rebalance on large/mid caps, 50–100 bps on small distressed names).
  - Short borrow fee schedule: `research-proposed` (e.g. 50 bps annualized baseline for general collateral, 200–500 bps for Q5 distressed stocks).
  - Execution model: `research-proposed` (MOC - market-on-close rebalancing on the final trading day of month $t$).
  - Maximum position limit per stock/industry: `research-proposed` (e.g. cap single industry at 10% of portfolio).

## Evidence

### Source-reported

All empirical figures below trace directly to Hui Chen, Winston Wei Dou, Hongye Guo, and Yan Ji, *NBER Working Paper 35513* (July 2026), Section 2, Section 4, Section 5, and Tables 1–12. The monthly equity sample covers 1976–2021 (42,385 industry-month observations, 1,126,119 stock-month observations, 549 monthly return observations).

#### 1. Industry-Level Distress Spread (Table 1 Panel A)
Portfolios of SIC4 industries sorted into quintiles based on $\text{Distress}_{i,t}$ (all returns annualized percentage terms; t-statistics in brackets robust to heteroskedasticity and autocorrelation):

| Metric | Q1 (Low Distress) | Q2 | Q3 | Q4 | Q5 (High Distress) | Q5 − Q1 (Spread) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Excess Return (%)** | 9.699 [5.34] | 10.487 [5.37] | 10.435 [6.19] | 9.207 [5.45] | 4.073 [1.85] | **−5.625 [−3.04]** |
| **CAPM Alpha (%)** | 1.203 [1.17] | 1.605 [1.42] | 0.836 [0.56] | −1.176 [−0.63] | −6.962 [−3.25] | **−8.165 [−3.90]** |
| **FF3 Alpha (%)** | 1.385 [1.96] | 1.676 [1.89] | 0.381 [0.34] | −1.675 [−1.24] | −8.298 [−5.23] | **−9.683 [−5.65]** |
| **Credit Spread (%)** | 0.992 [9.40] | 1.253 [7.08] | 1.430 [7.47] | 1.814 [7.72] | 3.338 [7.95] | **+2.346 [+7.33]** |
| **CDS Spread (%)** | 0.298 [6.14] | 0.409 [5.07] | 0.530 [5.14] | 0.812 [4.11] | 2.046 [5.86] | **+1.748 [+5.51]** |

*Key finding:* A long Q1 / short Q5 strategy generates **+5.625%** annualized gross excess return ($t = 3.04$), **+8.165%** CAPM alpha ($t = 3.90$), and **+9.683%** Fama-French 3-factor alpha ($t = 5.65$). Distressed industries simultaneously exhibit **+2.346%** higher corporate bond credit spreads ($t = 7.33$) and **+1.748%** higher CDS spreads ($t = 5.51$).

#### 2. Industry vs Firm Distress Decomposition (Table 1 Panels B & C, Table 2)
- **Industry-Adjusted Firm Distress (Table 1 Panel B):** Sorting individual firms on distress net of industry average ($\text{Ind\_Adj\_Distress}_{ij,t}$) yields $Q5 - Q1$ excess return of **−8.507%** ($t = -2.15$), CAPM alpha **−13.245%** ($t = -3.75$), FF3 alpha **−14.950%** ($t = -6.12$).
- **Raw Firm Distress (Table 1 Panel C):** Sorting individual firms on raw distress ($\text{Distress}_{ij,t}$) yields $Q5 - Q1$ excess return of **−11.429%** ($t = -2.77$), CAPM alpha **−18.487%** ($t = -4.21$), FF3 alpha **−21.113%** ($t = -6.10$).
- **Regression of Industry Distress Spread on Firm Distress Spread (Table 2, $N = 549$ months):**
  - Univariate: $\text{Intercept} = -3.037\%$ ($t = -2.04$), loading on $\text{Firm\_Distress\_Spread} = 0.304$ ($t = 11.45$), $R^2 = 0.296$.
  - With Mkt: $\text{Intercept} = -4.539\%$ ($t = -2.82$), firm distress loading $0.274$ ($t = 13.91$), $R^2 = 0.318$.
  - With FF3 (Mkt, HML, SMB): $\text{Intercept} = -6.247\%$ ($t = -4.68$), firm distress loading $0.230$ ($t = 3.87$), $R^2 = 0.357$.
  - With Carhart 4-factor (+ MOM): $\text{Intercept} = -4.192\%$ ($t = -3.19$), firm distress loading $0.089$ ($t = 2.15$), MOM loading $-0.429$ ($t = -8.58$), $R^2 = 0.498$.
  - *Inference:* Firm-level distress explains less than half of the industry distress spread; the industry effect remains statistically and economically distinct across all specifications.

#### 3. Placebo Synthetic Industries Test (Table 3, 2,000 Independent Simulations)
- M1 (random firm assignment to synthetic industries): Mean $Q5 - Q1$ spread = **−0.70%** (p1 = −2.56%, p50 = −0.70%, p95 = +0.60%).
- M2 (preserve firm count per industry): Mean $Q5 - Q1$ spread = **−1.28%** (p1 = −3.39%, p50 = −1.30%, p95 = +0.28%).
- M3 (preserve firm count and firm-level distress distribution): Mean $Q5 - Q1$ spread = **−1.54%** (p1 = −3.77%, p50 = −1.53%, p95 = −0.05%, p99 = +0.68%).
- *Inference:* Even at the 1st percentile of 2,000 reshuffled distributions, the synthetic spread never reaches the actual $-5.625\%$ industry spread, proving the anomaly requires real product-market industry boundaries.

#### 4. Model vs Data Moments (Table 5 Panel A)
- Equity excess return Q1 vs Q5: Data 9.70% vs 4.07% (spread **−5.63%**, 95% CI [−9.27, −1.99]); Model 9.09% vs 4.74% (spread **−4.35%**).
- Credit spread Q1 vs Q5: Data 0.99% vs 3.34% (spread **+2.35%**, 95% CI [1.72, 2.98]); Model 0.68% vs 2.49% (spread **+1.81%**).
- 5-year default rate Q1 vs Q5: Data 0.53% vs 5.66% (spread **+5.13%**, 95% CI [3.60, 6.66]); Model 0.97% vs 4.94% (spread **+3.97%**).
- Leverage ratio Q1 vs Q5: Data 22.57% vs 33.47% (spread **+10.90%**, 95% CI [9.12, 12.67]); Model 24.51% vs 40.36% (spread **+15.85%**).
- Gross profit margin Q1 vs Q5: Data 40.88% vs 29.07% (spread **−11.81%**, 95% CI [−14.81, −8.81]); Model 32.76% vs 23.77% (spread **−8.99%**).

#### 5. Tail-Risk Neutralization & Mechanism Tests (Table 7, Table 8, Table 9)
- **Table 7 Panel A (Double sort on $\nu_{i,t}$ then $\text{Distress}_{i,t}$):** $Q5 - Q1$ excess return shrinks to **−2.326%** ($t = -1.38$, insignificant); CAPM alpha to **−2.848%** ($t = -1.61$, insignificant); FF3 alpha to **−2.987%** ($t = -1.69$, insignificant).
- **Table 7 Panel B (Single sort on $\text{Distress\_adjusted}_{i,t}$ orthogonal to $\nu_{i,t}$):** $Q5 - Q1$ excess return drops to **−0.735%** ($t = -0.53$); CAPM alpha **−0.339%** ($t = -0.27$); FF3 alpha **+0.285%** ($t = 0.26$).
- **Table 8 (Beta to $\Delta \text{Discount\_rate}_t$):** Q1 equity beta = **−6.322** ($t = -2.68$); Q5 equity beta = **+4.564** ($t = 1.34$); spread $Q5 - Q1 = \mathbf{+10.886}$ ($t = 2.45$).
- **Table 9 (Pricing 21 test assets: 5 industry distress, 10 stock distress, 6 Treasury bonds):**
  - CAPM: Intercept 3.015% ($t\text{-FM} = 4.07$), Total MAPE 3.499%, $R^2 = 0.160$.
  - Two-factor (Mkt + Industry Distress Spread): Intercept 0.492% ($t\text{-FM} = 0.98$), price of risk $\lambda = \mathbf{-8.552\%}$ ($t\text{-FM} = -3.20$, $t\text{-Shanken} = -3.15$), Total MAPE 1.357%, $R^2 = \mathbf{0.821}$.

#### 6. Cross-Industry Variation by Market-Share Imbalance (Table 11 Panel B)
- Group 1 (balanced market shares): Distress spread $T3 - T1 = \mathbf{-6.685\%}$ ($t = -3.74$).
- Group 2: Distress spread $T3 - T1 = -2.195\%$ ($t = -1.03$, insignificant).
- Group 3 (imbalanced market shares): Distress spread $T3 - T1 = -2.519\%$ ($t = -1.48$, insignificant).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Entirely gross of trading costs and shorting frictions:** The source reports zero transaction costs, bid-ask spreads, or borrow fees. Shorting distressed equities (Q5) in practice encounters substantial borrowing constraints, high borrow fees (often hundreds of basis points annualized for small distressed firms), recall risk, and severe short-squeeze risk during market rebounds.
2. **Disappearance under tail-risk orthogonalization:** In Table 7, when industry distress is orthogonalized against ex-ante idiosyncratic left-tail risk ($\nu_{i,t}$), the distress spread completely collapses from $-5.625\%$ ($t = -3.04$) to $-0.735\%$ ($t = -0.53$, $p = 0.59$), with FF3 alpha becoming $+0.285\%$ ($t = 0.26$). This indicates that financial distress per se does not drive equity returns once tail-risk exposure is removed.
3. **Loss of statistical significance in imbalanced / concentrated industries:** Table 11 Panel B demonstrates that in industries where market shares are concentrated among one or two dominant firms (Group 3), the distress spread drops to $-2.519\%$ ($t = -1.48$, statistically insignificant). The anomaly is absent in dominant-firm or monopolistic structures.
4. **Disappearance in synthetic / placebo industries:** Table 3 proves that if firms are not interacting within actual SIC4 product-market boundaries, the distress spread disappears (shrinking to $-0.70\%$ to $-1.54\%$), showing that the factor cannot be implemented using arbitrary statistical or clustered groupings.
5. **Diametrical contradiction between debt and equity risk:** Distressed industries have higher default probability (5.66% vs 0.53% 5-year default rate), higher leverage (33.47% vs 22.57%), and higher credit spreads (+2.35%), yet lower equity returns (-5.63%). An unhedged investor buying distressed equity under the assumption of a "distress risk premium" suffers severe underperformance.
6. **Sensitivity to trade and market-structure shocks:** Table 12 demonstrates that exogenous competitive shocks (large import tariff cuts) significantly attenuate the competition-distress feedback ($\beta_1 = 1.57$, $t = 2.59$), showing that trade policy shifts can structurally disrupt the pricing relationship.
7. **No out-of-sample or live verification:** The empirical sample ends in December 2021. No post-2021 live or walk-forward validation is provided in the source.
8. **Preprint status:** The paper is an NBER working paper (July 2026) and has not yet completed peer-reviewed journal publication.

## Falsification plan

- **F1 (Out-of-sample forward window):** Evaluate the Long Q1 (low distress) / Short Q5 (high distress) industry strategy over the held-out post-2021 period (2022-01-01 to 2026-06-30). A **research-defined falsification threshold** is a gross annualized return spread $\le 0.0\%$ or a CAPM alpha $t$-statistic $< 1.65$.
- **F2 (Net-of-cost fee ladder):** Apply a realistic cost ladder:
  - 10 bps one-way trading cost + 50 bps annualized borrow fee on Q5;
  - 25 bps one-way trading cost + 150 bps annualized borrow fee on Q5;
  - 50 bps one-way trading cost + 300 bps annualized borrow fee on Q5.
  A **research-defined falsification threshold** is the total erosion of the annualized return spread (net return $< 0.0\%$) at or below the 25 bps / 150 bps borrow cost level.
- **F3 (Turnover & Capacity stress test):** Measure the realized monthly one-way portfolio turnover. If monthly turnover exceeds 25% one-way and available loan supply in Q5 names prevents full short allocation on $>15\%$ of target dollar weight, the strategy fails as non-implementable.
- **F4 (Microcap & Liquidity screen):** Exclude all stocks with market equity below the 20th percentile of NYSE before computing industry distress and industry returns. A **research-defined falsification threshold** is a reduction of the $Q5 - Q1$ spread by $>50\%$ relative to the full sample or an annualized spread $< 2.5\%$.
- **F5 (Alternative industry classification robustness):** Re-estimate the industry distress spread using GICS 6-digit (Sub-Industry), NAICS 4-digit, and Hoberg-Phillips TNIC (Text-based Network Industry Classifications). A **research-defined falsification threshold** is a non-significant spread ($t > -1.96$) across two or more alternative classification taxonomies.
- **F6 (Ex-ante tail risk orthogonalization):** Confirm the paper's negative result in out-of-sample data: when sorting on $\text{Distress\_adjusted}_{i,t}$ orthogonal to $\nu_{i,t}$, the spread must remain statistically indistinguishable from zero ($|t| < 1.96$).
- **F7 (Market share concentration interaction):** Test whether the spread is concentrated in balanced oligopolies (Group 1 market share imbalance) vs imbalanced (Group 3). If Group 1 does not outperform Group 3 spread by at least 3.0% annualized, the competition-distress mechanism is disconfirmed.
- **F8 (Discount-rate shock comovement):** Time-series correlation between the industry distress spread and Shiller CAPE discount-rate innovations $\Delta \text{Discount\_rate}_t$ must exceed $+0.40$ in out-of-sample data; correlation $< 0.20$ falsifies the discount-rate exposure channel.
- **F9 (Credit spread divergence check):** In any evaluated period, the credit spread difference $\text{Credit\_Spread}(Q5) - \text{Credit\_Spread}(Q1)$ must remain strictly positive ($> 1.0\%$ annualized); if credit spreads invert while equity spreads persist, the joint structural model is falsified.
- **F10 (Long-leg vs Short-leg attribution):** Decompose the spread into Long Q1 vs Market and Short Q5 vs Market. If the entire spread is generated by extreme short-leg drawdowns during liquidity panics with zero alpha on the long leg ($Q1 - \text{Mkt} \le 0$), the operational strategy should be classified as a negative-screen / short-only signal rather than a two-sided market-neutral factor.
- **F11 (Placebo reshuffle null test):** Generate 1,000 synthetic industry cross-sections by randomly reshuffling firm SIC codes. The empirical strategy spread must lie beyond the 99th percentile of the empirical synthetic distribution; otherwise the effect is indistinguishable from random firm clustering.
- **F12 (Crypto sector portability test):** Group crypto assets into sectors (e.g. DeFi, Layer 1, Layer 2, Infrastructure, Gaming) and rank sector distress by protocol treasury runway or developer commit decline. A **research-defined falsification threshold** is a failure of sector distress to predict negative forward returns, or the emergence of a positive distress spread due to retail speculative lottery preferences.

## Crypto portability

unproven

- **Reason for classification:** The primary source investigates exclusively US publicly traded equities (CRSP/Compustat) and corporate debt (Mergent FISD/TRACE) from 1976 to 2021. Zero crypto-asset data, digital tokens, or blockchain protocols are evaluated in the paper. Porting the mechanism to cryptocurrency is an unproven research interpretation.
- **Specific crypto portability challenges:**
  1. *Lack of formal corporate balance sheets and debt contracts:* Crypto tokens do not issue Leland-style long-term defaultable debt with formal bankruptcy court protection (Chapter 7/11). Protocol distress corresponds instead to treasury exhaustion, stablecoin de-pegging, liquidation cascades, or loss of developer/validator activity.
  2. *Product-market competition vs tokenomics:* Unlike oligopolistic manufacturing firms competing on profit margins and consumer price undercutting, crypto protocols compete on liquidity mining incentives, token emissions, fee burning, and developer mindshare. A distressed protocol typically increases token emissions (hyperinflation) rather than cutting consumer prices, diluting existing holders.
  3. *Retail speculative lottery preferences:* In cryptocurrency markets, highly distressed or near-insolvent tokens often experience speculative short squeezes, meme pumps, and retail lottery demand, which can invert the distress anomaly (generating positive rather than negative expected returns for distressed tokens over short horizons).
  4. *Absence of standardized sector classifications:* Crypto tokens lack standardized 4-digit SIC industrial codes; sector classifications (CoinMarketCap, CoinGecko, Artemis) are fluid, overlapping, and subject to rapid re-labeling.
  5. *Shorting constraints and perpetual funding:* Shorting distressed altcoins incurs prohibitive borrow fees (often $>50\%$ to $>100\%$ APR) or highly negative perpetual funding rates, making shorting high-distress crypto sectors cost-prohibitive.

## Limitations

- **Not independently reproduced:** Results rely entirely on source-reported econometric regressions and backtest tables.
- **Absence of transaction-cost and execution modeling:** All returns in the paper are gross of trading fees, commissions, and market impact.
- **Unaddressed short borrow fees on distressed firms:** The short leg requires borrowing high-distress, volatile stocks that often trade on special with high borrow fees, borrow recall risk, and potential buy-in risk.
- **Preprint / working paper status:** NBER working paper (July 2026), not yet published in a peer-reviewed academic journal.
- **Exclusion of financials and utilities:** The empirical findings exclude SIC 6000–6999 and 4900–4999; results cannot be generalized to banking, insurance, or regulated utility sectors.
- **Data availability lag:** Requires both CRSP returns and lagged quarterly Compustat accounting data, creating an operational lag of up to two months before fundamental failure probabilities update.
- **Sensitivity to ex-ante tail-risk adjustment:** The anomaly completely vanishes once orthogonalized against customer-base left-tail risk ($\nu_{i,t}$), indicating the raw distress spread is an indirect proxy for underlying competitive fragility rather than financial leverage per se.

## Implementation status

not-implemented

- No implementation in the research stack, PyBroker, NautilusTrader, or Qlib has been executed.
- No backtest with execution costs, slippage models, or borrow fees has been constructed.
- No production card, candidate pool entry, or trading workflow has been created.

## Adoption boundary

not-approved

- This record is research-only material.
- Presence in this repository does not mean:
  - Passed Research Intake Review;
  - Entered Hermes Wiki Brain;
  - Entered the production candidate pool;
  - Completed Qlib validation;
  - Approved for paper trading, testnet, or live deployment.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Methodological standard for preventing forward-looking leakage and overlap bias in cross-sectional asset pricing regressions.
- `[[quant/alpha-transforms-decay-neutralization-2026-08-28]]` — Industry and market neutralization techniques relevant to separating industry-level from idiosyncratic firm-level alpha.
- `[[quant/around-the-clock-macro-jump-risk-premia-fama-macbeth-2026-09-04]]` — Cross-sectional asset pricing methodology and Fama-MacBeth risk premium estimation.
- `[[quant/crypto-regime-dependent-distress-microstructure-next-quarter-2026-09-04]]` — Prior research record examining regime-dependent distress signals in digital assets.

## Sources

- Chen, H., Dou, W. W., Guo, H., & Ji, Y. (2026). *"Industry Distress Anomaly"*. National Bureau of Economic Research (NBER) Working Paper Series, Working Paper 35513, July 2026.
  - Canonical landing: `http://www.nber.org/papers/w35513`
  - DOI: `10.3386/w35513` (`https://doi.org/10.3386/w35513`)
  - Full text PDF: `http://www.nber.org/system/files/working_papers/w35513/w35513.pdf` (1,176,796 bytes, 63 pages, SHA-256 `1a57635562c79ffc7936da03345b9b965bae7a653890869c220faa65c1c3e924`).
- Campbell, J. Y., Hilscher, J., & Szilagyi, J. (2008). *"In Search of Distress Risk"*. Journal of Finance, 63(6), 2899–2939.
- Moskowitz, T. J., & Grinblatt, M. (1999). *"Do Industries Explain Momentum?"*. Journal of Finance, 54(4), 1249–1290.
- Fama, E. F., & French, K. R. (1993). *"Common Risk Factors in the Returns on Stocks and Bonds"*. Journal of Financial Economics, 33(1), 3–56.
- Leland, H. E. (1994). *"Corporate Debt Value, Bond Covenants, and Optimal Capital Structure"*. Journal of Finance, 49(4), 1213–1252.
