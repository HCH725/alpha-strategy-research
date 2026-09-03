---
schema: strategy-research-record-v1
title: "China A-Share Equity Return Predictability via XGBoost and TreeSHAP Behavioral Factor Decomposition"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-equity
  - machine-learning
  - xgboost
  - treeshap
  - factor-decomposition
  - behavioral-finance
  - china-a-shares
  - retail-sentiment
  - turnover
  - ablation-study
status: research-only
confidence: medium
source_as_of: 2026-06-17
sources:
  - https://arxiv.org/abs/2606.12843
  - https://arxiv.org/html/2606.12843v1
  - https://doi.org/10.48550/arXiv.2606.12843
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# China A-Share Equity Return Predictability via XGBoost and TreeSHAP Behavioral Factor Decomposition

## Provenance

- **Primary Source:** Xiao Han (Department of Mathematics, Emory University), Yao Xiao (H. Milton Stewart School of Industrial and Systems Engineering, Georgia Institute of Technology), Zhen Zhang (Department of Electrical and Systems Engineering, University of Pennsylvania), and Moxuan Zheng (Courant Institute of Mathematical Sciences, New York University), *"Interpretable Factor Decomposition for Decision Intelligence in Large-Scale Financial Markets: Evidence from China's A-Share Market"*, arXiv preprint `arXiv:2606.12843v1 [q-fin.ST, cs.LG, q-fin.PM]`, submitted June 17, 2026. DOI: `10.48550/arXiv.2606.12843`. Stable URL: `https://arxiv.org/abs/2606.12843`. Full-text HTML: `https://arxiv.org/html/2606.12843v1`. License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Target Universe & Data Sample:** Chinese A-shares listed on the Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE) within the CSI All-Share Index, retrieved via the `baostock` API from 2009-01-01 through 2019-12-31 (10 calendar years). The initial 3,632-security universe was screened by removing Special Treatment (ST / *ST) flagged stocks and excluding stock-months with fewer than 10 trading days, yielding a clean monthly panel of 254,854 stock-month observations across 3,199 distinct firms and 116 months.
- **Evaluation & Walk-Forward Protocol:** Rolling walk-forward evaluation using a fixed 60-month training window and 1-month out-of-sample testing window, resulting in 55 out-of-sample evaluation months. Hyperparameters are fixed across all rolling windows following the empirical asset pricing benchmark of Gu, Kelly, and Xiu (2020) to eliminate parameter snooping and look-ahead bias.
- **Repository Deduplication:** Repository-wide inspection on 2026-09-04 confirms that `arXiv:2606.12843` and authors Xiao Han, Yao Xiao, and Zhen Zhang do not appear in any existing strategy record. While co-author Moxuan Zheng appears in `volume-price-adjusted-macd-sensitivity-calibration-2026-09-02.md`, that earlier record captures a single-instrument technical timing model on U.S. ETFs (SPY/QQQ/DIA) via volume-price adjusted MACD (`arXiv:2604.26063`). Existing machine-learning cross-sectional equity records in this repository (`cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03.md`, `cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md`, `equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02.md`, `equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02.md`) explore Ridge percentile ranking, double-selection Lasso, TabNet/XGBoost regime switches, or homological graph filtration on U.S. or multi-market equities. This record uniquely captures an interpretable tree-ensemble framework integrating exact game-theoretic TreeSHAP attribution and systematic group ablation on China's retail-dominated equity market, demonstrating the empirical dominance of behavioral factors over classical valuation metrics and mapping the feature substitutability structure between load-bearing scale proxies and behavioral timing features.

## Economic mechanism

### Source-reported

The authors address the fundamental question of which financial indicators drive equity returns and how predictive they are in a retail-dominated market setting:
1. **Retail Participant Dominance:** The Chinese A-share market is characterized by approximately 80% retail trading participation (citing Ng and Wu 2007). In such an environment, speculative trading, attention shifts, and sentiment overreaction generate pronounced cross-sectional return anomalies that differ fundamentally from institutional-dominated markets.
2. **Behavioral over Valuation Hierarchy:** While classical value investing literature (Fama and French 1993, 2015) posits that valuation multiples (low P/E, P/B, P/CF) serve as primary risk-premia drivers, TreeSHAP attribution reveals that behavioral characteristics (turnover, momentum, volatility) account for an average of 58.2% of predictive attribution across 55 industry sectors, compared to only 10.7% for valuation ratios.
3. **Turnover, Attention, and Liquidity:** Average turnover rate acts as the highest-utilized individual feature in tree splits, aligning with behavioral finance theories where turnover proxies for retail attention, divergence of investor opinion, and liquidity premia (Datar et al. 1998, Amihud 2002, Brennan et al. 1998, Lee and Swaminathan 2000). High turnover in Chinese equities indicates speculative retail fever that subsequently reverts.
4. **Feature Substitutability vs. Hard Dependency:** By contrasting TreeSHAP additive attribution with systematic group ablation, the authors identify an operational substitutability structure:
   - **Load-bearing (Hard-dependent) Features:** Firm size (log market cap) ranks #2 on SHAP attribution (16.4%) but ranks #1 in ablation penalty, causing the largest out-of-sample AUC drop ($-0.009$) when omitted. Size is required for model structural routing.
   - **Substitutable Features:** Turnover ranks #1 on SHAP attribution but only #3 in ablation penalty. Because turnover is correlated with intra-month volatility and short-term momentum, tree algorithms heavily leverage it when present, but substitute adjacent behavioral signals when turnover is removed.
   - **Noise-Inducing Features:** Valuation metrics, when completely removed in ablation, slightly improve out-of-sample AUC by $+0.001$, indicating that valuation ratios introduce noise and parameter variance due to low coverage and sparse reporting.

### Research interpretation

The overarching mechanism is **state-contingent behavioral mispricing routed through capitalization regimes**:
1. **Capitalization Tier Routing:** Decision trees in gradient boosting prioritize firm size ($\ln(\text{Mkt Cap})$) at root-level splits because small-cap and large-cap equities in China operate under distinct price-formation regimes. Small-cap stocks are primarily traded by noise-trader retail participants prone to attention-driven cascades, whereas large-cap SOE stocks are anchored by institutional mutual funds and sovereign stabilization entities.
2. **Limits to Arbitrage and Downside Correction:** Due to mainland Chinese market frictions—specifically strict short-selling constraints (sparse securities lending availability and high borrow fees) and T+1 settlement rules—optimistic retail traders bid up high-turnover speculative stocks. Rational arbitrageurs cannot easily short the overpriced securities, causing mispricing to persist until it gradually deflates over 1-to-3-month horizons, creating a predictable cross-sectional return reversal exploited by sorting on model-predicted probabilities.
3. **Information Inefficiency of Accounting Valuation:** Accounting multiples in emerging markets with state ownership divergence, varied subsidies, and irregular reporting cycles exhibit lower signal-to-noise ratios than direct high-frequency price and volume behavioral data.

## Signal

The trading logic is fully normalized as a monthly cross-sectional quintile long-short strategy:

### Signal Formation Timestamp
- **Observation Time:** End of month $t$, evaluated at the market close of the final trading day of calendar month $t$.
- **Trading Time:** Execution occurs at the open of the first trading day of calendar month $t+1$.
- **Timezone & Calendar:** China Standard Time (UTC+8); Shanghai and Shenzhen Stock Exchange trading calendar.

### Predictive Feature Set (12 Characteristics across 4 Groups)
1. **Valuation Group (4 features):**
   - Mean Price-to-Earnings ratio ($P/E$) over month $t$.
   - Mean Price-to-Book ratio ($P/B$) over month $t$.
   - Mean Price-to-Sales ratio ($P/S$) over month $t$.
   - Mean Price-to-Cash-Flow ratio ($P/CF$) over month $t$.
2. **Behavioral Group (4 features):**
   - Monthly Return: Close-to-close percentage price return over month $t$.
   - Mean Turnover: Average daily share turnover rate ($\text{Volume} / \text{Floating Shares}$) over month $t$.
   - Intra-month Volatility: Sample standard deviation of daily returns within month $t$.
   - Multi-horizon Momentum: Compounded returns over the preceding 3-month, 6-month, and 12-month windows prior to month $t$.
3. **Fundamental Group (2 features):**
   - Return on Equity ($ROE$): Net income divided by total shareholders' equity from the most recently reported quarterly financial statements, forward-filled (88.4% panel coverage).
   - Net Profit Margin ($NP\text{ margin}$): Net profit divided by total revenue from the most recently reported quarterly financial statements, forward-filled.
4. **Size Group (1 feature):**
   - Log Market Capitalization: $\ln(\text{Total Market Capitalization})$ as of the final trading day of month $t$.

### Preprocessing & Data Cleaning
- **Winsorization:** All 12 feature variables are winsorized cross-sectionally at the 1st and 99th percentiles in each monthly cross-section to prevent extreme outliers from distorting tree split criteria.
- **Screening:** Exclude Special Treatment (ST, *ST) flagged securities and firm-months with fewer than 10 active trading days.

### Model Specification & Training Protocol
- **Target Variable:** Binary indicator of next-month relative outperformance:
  $$y_{i, t+1} = \mathbb{I}\left(R_{i, t+1} > \text{Median}\left(\{R_{j, t+1}\}_{j=1}^{N_{t+1}}\right)\right)$$
  where $R_{i, t+1}$ is the percentage total return of stock $i$ over month $t+1$, and $\text{Median}(\cdot)$ is the cross-sectional median return across all active universe stocks in month $t+1$.
- **Model Architecture:** Extreme Gradient Boosting (`XGBoost`) binary classification tree ensemble.
- **Fixed Hyperparameters (Gu, Kelly, Xiu 2020 protocol):**
  - `n_estimators`: 200 trees.
  - `max_depth`: 4.
  - `learning_rate` ($\eta$): 0.05.
  - `subsample` (row subsampling): 0.80 (80%).
  - `colsample_bytree` (column subsampling): 0.80 (80%).
  - Objective: Binary logistic (`binary:logistic`).
- **Estimation Window:** Rolling 60-month training window $[t-59, t]$.
- **Out-of-Sample Validation:** 1-month ahead out-of-sample evaluation on month $t+1$, rolled forward across 55 monthly evaluation periods.

### Portfolio Construction & Execution Rules
- **Predicted Probability:** For each stock $i$ in month $t$, evaluate $\hat{p}_{i, t+1} = P(y_{i, t+1} = 1 \mid X_{i, t})$.
- **Sorting & Grouping:** Sort active stocks into quintiles based on $\hat{p}_{i, t+1}$:
  - Quintile 5 (Q5): Top 20% highest predicted probability (predicted outperforming stocks).
  - Quintile 1 (Q1): Bottom 20% lowest predicted probability (predicted underperforming stocks).
- **Position Allocation:**
  - **Long:** Long positions in all Quintile 5 constituents.
  - **Short:** Short positions in all Quintile 1 constituents (assumed benchmark-relative in practice).
  - **Weighting Schemes Evaluated:**
    1. Equal-Weighted (EW): Uniform weight $w_i = 1 / N_Q$ across quintile constituents.
    2. Float-Cap-Weighted (CW): Weight proportional to floating market cap.
    3. Industry-Neutral (IN): Ranking conducted within each of the 55 China Securities Regulatory Commission (CSRC) industry sectors.
- **Holding Period:** 1 calendar month.
- **Rebalance & Exit:** Complete monthly rebalance at the close of month $t+1$ / open of month $t+2$. Existing positions are liquidated or adjusted to reflect newly sorted quintile assignments.

### Underspecified Rules
- Execution execution price: The study assumes execution at monthly boundary closing/opening prices without modeling intraday limit order books or market-on-open auctions.
- Limit-up / limit-down handling: Mainland Chinese exchanges enforce a $\pm 10\%$ daily price movement limit ($\pm 20\%$ for ChiNext/STAR Market); execution handling when a Q5 buy hits limit-up or a Q1 sell hits limit-down on the rebalancing day is omitted in the source paper.
- Specific stock borrow availability: Cost and availability of borrowing specific small-cap Q1 constituents for physical shorting are omitted from the backtest engine.

## Required data

- **Instrument:** Chinese A-share common stocks listed on the Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE).
- **Universe:** CSI All-Share Index constituents, excluding Special Treatment (ST / *ST) securities and firm-months with fewer than 10 trading days.
- **Venue:** Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE).
- **Timeframe:** Daily OHLCV aggregated to monthly cross-sections, matched with quarterly corporate financial statements.
- **Fields:**
  - Daily Price/Volume: Open, High, Low, Close, Trading Volume, Share Turnover Rate.
  - Market Value: Floating Market Capitalization, Total Market Capitalization.
  - Valuation: Price-to-Earnings ($P/E$), Price-to-Book ($P/B$), Price-to-Sales ($P/S$), Price-to-Cash-Flow ($P/CF$).
  - Financials: Quarterly Net Income, Shareholders' Equity, Total Revenue, Net Profit.
  - Sector Metadata: CSRC industry classification codes (55 industry sectors).
- **Point-in-Time Integrity & Availability:**
  - Price and volume data: Available at market close (15:00 CST) on the last trading day of month $t$.
  - Fundamental data limitation: The authors explicitly note that quarterly fundamental metrics were merged without enforcing publication reporting lags (forward-filled from quarter-end), introducing an in-sample look-ahead risk bounded by the 14.7% fundamental SHAP attribution.
  - Survivorship: Data panel was constructed from securities active over 2009–2019; delisted or failed companies during this period are excluded, introducing survivorship bias.
- **Missing-Data Handling:** Quarterly fundamental metrics forward-filled (88.4% panel coverage); firm-months with $< 10$ trading days excluded; extreme values winsorized at 1st/99th percentiles.

## Execution assumptions

- **Signal-to-Order Latency:** Rebalancing calculated at month-end close and executed at next-month start.
- **Order Type:** Theoretical execution at cross-sectional prices (market order assumption).
- **Slippage & Spread:** Not modeled at the microstructure bar level; modeled via round-trip transaction cost parameterization.
- **Transaction Cost Tiers Evaluated:**
  - 0.0% round-trip (gross baseline).
  - 0.2% round-trip (low-friction institutional rate).
  - 0.6% round-trip (typical retail/institutional realistic cost including commissions, exchange fees, and mainland stamp tax).
  - 1.0% round-trip (stressed high-friction environment).
- **Shorting Constraints:** Frictionless shorting of Q1 stocks is assumed in the reported long-short spread (+2.38%/month). In practice, mainland Chinese securities lending (融券) is heavily constrained, illiquid, and subject to high borrow rates and regulatory suspensions. Practical adoption requires a long-only benchmark-relative implementation.
- **Capital Allocation:** Fully invested across quintile constituents; no leverage or margin borrowing modeled.

## Evidence

### Source-reported

All figures below are directly extracted from the primary text and tables of Han, Xiao, Zhang, and Zheng (2026), `arXiv:2606.12843v1`:
- **Out-of-Sample Window:** 55 monthly out-of-sample periods from rolling 60-month walk-forward windows over 3,632 Chinese A-shares (254,854 stock-month observations from 2009 to 2019).
- **Predictive Performance:** XGBoost achieves a mean out-of-sample Area Under the ROC Curve (AUC) of 0.547, outperforming Logistic Regression (mean AUC of 0.542, representing a +0.46% AUC increase).
- **Long-Short Spread & Sharpe Ratio:**
  - The top-quintile minus bottom-quintile (Q5 - Q1) long-short spread generates +2.38% per month ($t = 5.94$ using Newey-West standard errors).
  - Annualized Sharpe ratio of the long-short portfolio is 2.23.
- **Factor-Model Risk Adjustment:**
  - CAPM regression: Market beta $\beta_{\text{MKT}} \approx 0.0$ ($\pm 0.03$, $t = -0.27$), confirming empirical market neutrality.
  - Carhart four-factor regression: Generates an alpha $\alpha = +2.31\%$ per month ($t = 7.48$).
- **Year-by-Year Robustness:** Positive out-of-sample AUC and positive long-short return across all calendar years in the test period (2015 was the weakest year; 2018 was the strongest year despite the Sino-U.S. trade war).
- **Transaction Cost Sensitivity:**
  - Net of 0.6% round-trip costs, annualized Sharpe ratio remains 1.67.
  - The strategy remains profitable up to 1.0% round-trip transaction costs.
- **Industry Neutrality & Transferability:**
  - Industry-neutral sorting improves Logistic Regression Sharpe by +0.64 compared to equal-weighted LR.
  - The framework produces positive long-short return spreads in 48 out of 50 evaluated industry sectors (binomial test $p < 10^{-12}$).
- **TreeSHAP Feature Attribution:**
  - Behavioral features account for 58.2% of global predictive attribution.
  - Size features account for 16.4% of attribution.
  - Fundamental features account for 14.7% of attribution.
  - Valuation ratios account for only 10.7% of attribution.
  - Across all 55 CSRC industry sectors, behavioral attribution exceeds 50%, while valuation is universally the weakest factor category (ranging from 8.5% to 14.9%).
- **Systematic Ablation Findings:**
  - Omission of Size ($\ln(\text{Mkt Cap})$) leads to the largest drop in AUC ($-0.009$), confirming size as the primary structural backbone for decision splits.
  - Omission of Valuation features slightly improves AUC by $+0.001$, indicating that valuation multiples add noise in short-horizon cross-sectional ranking.
  - Turnover ranks #1 on SHAP usage but #3 in ablation penalty, demonstrating that while heavily split upon, its predictive information can be partially substituted by correlated momentum and volatility features.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Short-Sale Infeasibility in China A-Shares:** The reported +2.38%/month long-short spread derives substantial return from shorting the bottom quintile (Q1). In mainland China, physical securities lending is illiquid, expensive (often 6–10% annualized borrow fees), heavily skewed toward large-cap index components, and subject to direct regulatory shorting bans during market downturns. Shorting small-cap Q1 constituents is practically impossible for most market participants.
- **Fundamental Look-Ahead Contamination:** The authors explicitly acknowledge that quarterly financial variables were forward-filled from the fiscal quarter-end rather than the actual disclosure filing date. This introduces forward-looking data leakage, though bounded by the 14.7% fundamental SHAP attribution.
- **Survivorship Bias:** Delisted and bankrupt securities over 2009–2019 were excluded from the panel, potentially inflating the performance of Q5 or understating the survivorship drag in Q1.
- **Turnover and Execution Frictions:** Full monthly rebalancing across hundreds of small-to-mid-cap equities incurs substantial market impact and turnover drag that may exceed the 0.6% modeled transaction cost in stressed liquidity conditions.

## Falsification plan

To empirically validate or falsify the reported alpha mechanism, the following independent tests must be executed:

1. **Strict Point-in-Time Fundamental Audit:**
   - *Protocol:* Re-run the walk-forward panel replacing forward-filled quarterly financials with strict point-in-time publication timestamps (enforcing an explicit minimum 60-calendar-day reporting lag or matching against CSMAR/Wind official disclosure filing dates).
   - *Falsification Rule:* If the Carhart four-factor alpha drops below +1.0% per month or $t < 2.0$, falsify the reported alpha as primarily artifactual due to fundamental look-ahead leakage.
2. **Survivorship & Delisting Stress Test:**
   - *Protocol:* Reconstruct the CSI All-Share historical constituent panel including all suspended, merged, and delisted securities over 2009–2019, applying a conservative delisting return assumption ($-30\%$ to $-50\%$ on final exit).
   - *Falsification Rule:* If the out-of-sample Q5 - Q1 long-short spread compresses by $> 40\%$ (spread $< +1.4\%$ per month), falsify the strategy as driven by survivorship selection bias.
3. **Executable Long-Only Benchmark-Relative Test:**
   - *Protocol:* Constrain the portfolio to a long-only implementation (investing 100% of capital into Quintile 5, equal-weighted and industry-neutral) and evaluate excess return over the CSI All-Share Index net of 0.3% one-way turnover costs (0.1% broker commission + 0.1% stamp tax on sells + 0.1% market impact).
   - *Falsification Rule:* If the 3-year rolling Information Ratio against the benchmark drops below 0.40, falsify the active economic viability of the strategy for long-only asset managers.
4. **Behavioral Feature Ablation Test:**
   - *Protocol:* Concurrently omit both turnover and momentum from the feature set, retraining the XGBoost model exclusively on size, fundamentals, and valuation ratios.
   - *Falsification Rule:* If the out-of-sample AUC collapses to $\le 0.510$ and Carhart alpha drops to zero ($p > 0.10$), verify the authors' thesis that behavioral signals provide the entire actionable edge in this market.
5. **Modern Out-of-Sample Regime Validation (2020–2026):**
   - *Protocol:* Freeze the model hyperparameters and evaluate the rolling walk-forward pipeline on out-of-sample data from 2020-01-01 through 2026-06-30 (covering the post-COVID regime, property sector debt contraction, and increased institutional algorithmic participation).
   - *Falsification Rule:* If the annualized Sharpe ratio over 2020–2026 falls below 0.50 or Carhart alpha fails significance ($t < 1.96$), falsify the temporal stationarity of the behavioral pricing anomaly.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Portability Rationale:** The core economic hypothesis—that in retail-dominated speculative asset classes, behavioral characteristics (trading turnover, momentum, and volatility) overwhelmingly dominate fundamental valuation ratios—transfers directly to cryptocurrency spot and perpetual markets. Crypto markets have near-zero reliable accounting valuation metrics, making behavioral and liquidity proxies the primary drivers of cross-sectional return variation.
- **Factor Adaptation Mapping:**
  - *Firm Size:* Replace log market cap with the natural logarithm of 30-day circulating market capitalization or open interest.
  - *Turnover:* Replace equity share turnover with 24-hour spot volume divided by circulating market cap, or perpetual taker volume divided by aggregate open interest.
  - *Momentum:* Retain multi-horizon return momentum across 7-day, 14-day, 30-day, and 90-day lookbacks.
  - *Volatility:* Retain intra-month realized daily return standard deviation or high-frequency Parkinson/Garman-Klass volatility estimators.
  - *Valuation:* Map to protocol-specific on-chain metrics (e.g., NVT ratio, MVRV ratio, Fully Diluted Valuation / Total Value Locked (FDV/TVL), or fee-to-market-cap ratios).
- **Execution & Microstructure Differences:**
  - *Shorting Advantage:* Unlike Chinese A-shares, crypto perpetual futures provide deep, unconstrained two-way liquidity, allowing seamless execution of the short leg (Q1) without securities lending bottlenecks.
  - *Session Structure:* Crypto trades 24/7/365 without daily closing auctions. Monthly signals must be anchored to fixed UTC timestamps (e.g., 00:00 UTC on the 1st of each month).
  - *Sector Taxonomy:* The absence of standardized industry classifications (such as CSRC codes) requires utilizing on-chain clustering or category tags (DeFi, Layer-1, AI, Meme) for industry-neutral sorting.

## Limitations

- **Underspecified Real-World Execution:** The model assumes execution at monthly cross-sectional prices without simulating intraday liquidity, order-book depth, or price impact on small-cap securities.
- **Short-Leg Execution Barrier:** The primary market's structural prohibition on unconstrained short selling means the reported long-short Sharpe of 2.23 cannot be directly harvested in mainland China without synthetic derivatives or index futures shorting.
- **Fundamental Look-Ahead Risk:** Quarterly accounting data was forward-filled from fiscal quarter-end dates rather than verified public filing dates, creating a data leakage risk bounded by the 14.7% fundamental SHAP attribution.
- **Survivorship Panel Selection:** Exclusion of delisted companies over 2009–2019 creates potential survivorship bias.
- **In-Sample SHAP Attribution:** SHAP calculations were computed in-sample across the 254,854 stock-month panel without out-of-sample temporal cross-validation or multiple-testing corrections across the 55 sector regressions.
- **Not Independently Reproduced:** All performance metrics and attribution percentages are third-party source-reported claims.

## Implementation status

- `not-implemented`.
- No prototype, backtest script, or pipeline integration exists in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- The strategy has not been tested in paper trading, testnet, or live trading environments.

## Adoption boundary

- `research-only`.
- Adoption status: `not-approved`.
- Approval scope: `research-only`.
- Inclusion in this repository indicates that the research paper has been normalized into canonical format for ChatGPT Research Intake Review. It does not constitute approval for strategy implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]`
- `[[quant/phase8-feature-model-diagnostics-executable-edge-2026-08-28]]`
- `[[quant/phase8-regularized-nonlinear-ml-toolbox-2026-08-28]]`
- `[[quant/phase9-factor-taxonomy-and-cross-sectional-sorts-2026-08-28]]`
- `[[quant/phase9-cross-sectional-regression-and-factor-premia-2026-08-28]]`
- `[[quant/sharpe-deflated-multiple-testing-2026-08-27]]`
- `[[quant/volume-price-adjusted-macd-sensitivity-calibration-2026-09-02]]`

## Sources

- Xiao Han, Yao Xiao, Zhen Zhang, and Moxuan Zheng, *"Interpretable Factor Decomposition for Decision Intelligence in Large-Scale Financial Markets: Evidence from China's A-Share Market"*, arXiv preprint `arXiv:2606.12843v1 [q-fin.ST, cs.LG, q-fin.PM]`, submitted June 17, 2026. DOI: `10.48550/arXiv.2606.12843`. Stable URL: `https://arxiv.org/abs/2606.12843`. Full-text HTML: `https://arxiv.org/html/2606.12843v1`.
