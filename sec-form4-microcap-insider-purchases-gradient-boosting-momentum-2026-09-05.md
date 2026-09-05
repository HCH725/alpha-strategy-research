---
schema: strategy-research-record-v1
title: "SEC Form 4 Insider Purchases in Microcap Equities: Gradient Boosting Abnormal Return Detection and Disclosure Price-Momentum Confirmation"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - microcaps
  - insider-trading
  - sec-form-4
  - gradient-boosting
  - xgboost
  - momentum
  - information-diffusion
status: research-only
confidence: medium
source_as_of: 2026-02-06
sources:
  - "Hangyi Zhao, 'Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns', arXiv:2602.06198v1 [q-fin.ST], February 6, 2026. DOI: 10.48550/arXiv.2602.06198. https://arxiv.org/abs/2602.06198"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SEC Form 4 Insider Purchases in Microcap Equities: Gradient Boosting Abnormal Return Detection and Disclosure Price-Momentum Confirmation

## Provenance

- **Primary Source:** Hangyi Zhao, *"Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns"*, arXiv preprint `arXiv:2602.06198v1 [q-fin.ST]`, published February 6, 2026.
- **Author Affiliation:** Hangyi Zhao (`hyz0815@stanford.edu`), Stanford University.
- **Canonical DOI:** [10.48550/arXiv.2602.06198](https://doi.org/10.48550/arXiv.2602.06198).
- **Traceable URLs:**
  - Abstract: [https://arxiv.org/abs/2602.06198](https://arxiv.org/abs/2602.06198)
  - Full Text HTML: [https://arxiv.org/html/2602.06198v1](https://arxiv.org/html/2602.06198v1)
  - PDF: [https://arxiv.org/pdf/2602.06198](https://arxiv.org/pdf/2602.06198)
  - Source Archive: [https://arxiv.org/e-print/2602.06198](https://arxiv.org/e-print/2602.06198) (contains primary LaTeX document `refine_3.tex`, macro definition file `outputs/metrics.tex`, and regression/classification tables `outputs/table1.tex` through `outputs/table4.tex`).
- **Pre-Write Deduplication Audit:**
  - A repository-wide inspection on 2026-09-05 confirmed zero existing records referencing `2602.06198`, `Zhao`, `Form 4`, or `SEC Form 4`.
  - Existing records in the repository examining informed trading or order flow (`crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01.md`, `crypto-noise-perturbed-order-flow-privacy-subsidy-kyle-market-making-2026-09-01.md`, `news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02.md`, `equity-order-flow-kyle-lambda-cross-sectional-liquidity-premium-2026-09-03.md`) focus on continuous Kyle's lambda, high-frequency LOB microstructure, prediction markets, or rumor drift.
  - This record is structurally, mechanically, and empirically distinct: it models regulatory filing events (SEC Form 4 open-market purchases) in illiquid U.S. microcaps using gradient-boosted decision trees (XGBoost) and documents a counter-intuitive positive price-momentum confirmation effect across disclosure windows.

## Economic mechanism

### Source-reported

1. **Information Asymmetry in Neglected Equities:** While large-cap and mid-cap equities feature dense sell-side analyst coverage, institutional sponsorship, and rapid algorithmic price discovery, microcaps ($30M to $500M market capitalization) suffer from sparse coverage and low institutional float. Corporate executives and directors possess superior private information regarding operational inflection points, commercial pipeline developments, and true intrinsic value. Because open-market purchases (SEC transaction code "P") require deployment of personal capital and carry legal exposure under SEC Rule 10b-5 and insider trading statutes, they constitute a costly, credible signal of positive firm prospects [source-reported].
2. **Slow Information Incorporation vs. Limits to Arbitrage:** In microcap equities, wider effective bid-ask spreads, thin order books, and borrowing constraints limit arbitrage activity by institutional quantitative traders. Consequently, even after mandatory disclosure on SEC Form 4 (required within two business days under Sarbanes-Oxley Section 16(a)), public market prices adjust gradually rather than instantaneously [source-reported].
3. **Momentum Confirmation vs. Mean Reversion:** Conventional market heuristics advise against entering insider purchase signals after substantial price appreciation between the transaction date and disclosure date, anticipating mean-reversion or exhausted upside. The author's empirical evidence contradicts this heuristic: insider purchases disclosed into strong price appreciation ($>10\%$ run-up) generate the highest mean cumulative abnormal returns ($6.3\%$) and highest probability of outperformance ($36.7\%$). In informationally sparse markets, immediate price strength validates the conviction of the insider signal and reflects the initial phase of prolonged information diffusion rather than an overextended anomaly [source-reported].
4. **Dominance of Valuation Reference Points:** Distance from the 52-week high dominates all feature categories (accounting for $36\%$ of XGBoost predictive gain). This is consistent with behavioral valuation anchoring (insiders preferentially deploying personal capital when shares trade at severe discounts to historical reference levels) or mechanical recovery headroom over a 30-day window [source-reported].

### Research interpretation

The strategy functions as an event-driven, quality-gated momentum continuation model:
1. **Primary Event Catalyst:** Public dissemination of an SEC Form 4 open-market purchase in an investable microcap stock ($30\text{M} \le \text{Market Cap} \le 500\text{M}$, 30-day $\text{ADDV} \ge \$200,000$).
2. **Contextual Classification Gating:** Rather than indiscriminately buying all insider filings, a calibrated non-linear classifier (XGBoost) conditions on 12 features spanning firm valuation (`pct_from_52w_high`), interim price momentum (`price_deviation`), trailing volatility, and liquidity. A classification threshold ($p \ge 0.20$) filters for asymmetrical positive tail outcomes ($CAR_{[1, 30]} > 10\%$).
3. **Friction-Adjusted Tradability:** Gross returns in the top momentum bucket ($6.3\%$ mean CAR) are substantially curtailed by microcap market frictions (effective bid-ask spread $\approx 2.0\%$, market impact $\approx 1.0\%$), leaving a net CAR of $\approx 3.3\%$ [source-reported]. The capacity per trade is naturally constrained ($50,000 position limit), making it an institutional niche alpha or an asset-gathering vehicle for specialized execution systems.

## Signal

### Mathematical Formulation & Target Definition

- **Information Set & Point-in-Time Constraint:** For an SEC Form 4 filing publicly disclosed on trading date $t$, the information set $\mathcal{I}_t$ incorporates only market and regulatory data available at or before the market close of date $t$ [source-reported].
- **Event Target Variable:** The binary target variable $y$ indicates whether the post-disclosure 30-day cumulative abnormal return exceeds $10\%$ [source-reported]:
  $$y = \mathbf{1}\{CAR_{[1, 30]} > 10\%\}$$
  where $CAR_{[1, 30]}$ is evaluated over the event window from trading day $t+1$ (the session immediately following disclosure) through trading day $t+30$ [source-reported].
- **Risk-Adjustment Benchmark:** Abnormal returns $AR_\tau$ are computed relative to the Fama-French three-factor model [source-reported]:
  $$AR_\tau = R_\tau - \hat{\alpha} - \hat{\beta}_{\text{MKT}}(R_{\text{MKT}, \tau} - R_{f, \tau}) - \hat{\beta}_{\text{SMB}} \cdot SMB_\tau - \hat{\beta}_{\text{HML}} \cdot HML_\tau$$
  where factor loadings $(\hat{\alpha}, \hat{\beta}_{\text{MKT}}, \hat{\beta}_{\text{SMB}}, \hat{\beta}_{\text{HML}})$ are estimated over the 252 trading days preceding the event window ($[t-252, t-1]$) [source-reported]. The $10\%$ cutoff corresponds approximately to the top decile of the empirical $CAR_{[1, 30]}$ distribution [source-reported].

### Input Feature Specification (12 Features)

The XGBoost model processes 12 features partitioned into four distinct categories [source-reported]:

1. **Market Conditions at Disclosure:**
   - `pct_from_52w_high`: Percentage distance of closing price on filing date $t$ from the trailing 52-week high: $(P_t - \text{High}_{52\text{w}, t}) / \text{High}_{52\text{w}, t}$ [source-reported; importance = 0.360].
   - `return_mtd`: Month-to-date return of the equity through date $t$ [source-reported; importance = 0.081].
   - `volatility_30d`: 30-day annualized realized volatility calculated using closing prices through date $t$ [source-reported; importance = 0.072].
   - `market_cap_at_filing`: Total market capitalization as of date $t$ [source-reported; importance = 0.066].
   - `pct_from_52w_low`: Percentage distance from trailing 52-week low: $(P_t - \text{Low}_{52\text{w}, t}) / \text{Low}_{52\text{w}, t}$ [source-reported; importance = 0.065].
   - `avg_daily_vol_at_filing`: Trailing 30-day average daily dollar volume (ADDV) as of date $t$ [source-reported; importance = 0.061].
   - `price_deviation`: Percentage price change between the insider transaction execution price ($P_{\text{trans}}$) and the public filing date closing price ($P_t$): $(P_t - P_{\text{trans}}) / P_{\text{trans}}$ [source-reported; importance = 0.059].
2. **Insider Characteristics:**
   - `insider_title_score`: Ordinal score reflecting corporate seniority: CEO = 5, CFO = 4, COO = 3, Director = 2, Other / 10% Owner = 1 [source-reported; importance = 0.029].
   - `transaction_value`: Total dollar purchase value ($P_{\text{trans}} \times \text{Shares}$) [source-reported; importance = 0.056].
3. **Trading History:**
   - `is_first_purchase_12m`: Binary flag set to 1 if the insider executed zero open-market purchases in the preceding 12 months, 0 otherwise [source-reported; importance = 0.049].
   - `value_vs_avg_ratio`: Ratio of current transaction value to the insider's historical average purchase value across prior filings [source-reported; importance = 0.043].
4. **Sector Indicator:**
   - `is_biotech`: Binary flag set to 1 for biotechnology and pharmaceutical issuers, 0 otherwise [source-reported; importance = 0.060].

### Model Decision Rule & Operational Thresholds

- **Model Family:** XGBoost classifier with tree boosting, trained using time-series cross-validation on 2018–2022 data [source-reported].
- **Posterior Probability Output:** $\hat{p}_t = P(y = 1 \mid \mathcal{I}_t) \in [0, 1]$.
- **Optimized Action Threshold:** $\hat{p}_t \ge 0.20$ (optimized on 2023 validation set to maximize F1 score; default 0.50 yields poor recall of 0.17) [source-reported].
- **High-Conviction Price-Deviation Overlay:** Price deviation $(P_t - P_{\text{trans}}) / P_{\text{trans}} > 10\%$ identifies transactions with highest empirical outperformance probability ($36.7\%$) and mean CAR ($6.3\%$) [source-reported].

### Research-Proposed Execution Rules

- **Execution Timing:** Enter Long at market open on trading day $t+1$ (the session immediately following filing date $t$) using a TWAP order over the opening 30 minutes `[research-proposed]`.
- **Holding Period:** Fixed holding duration of 30 trading days ($t+30$ market close) matching the target labeling horizon `[research-proposed]`.
- **Protective Stop-Loss:** Catastrophic stop-loss at $-15.0\%$ cumulative drawdown from fill price, or early exit if an SEC Form 4 insider sale (Code "S") is disclosed for the same issuer `[research-proposed]`.
- **Position Sizing:** Equal dollar weighting capped at $\$50,000$ per name or $\le 5\%$ of trailing 30-day ADDV to restrict market impact `[research-proposed]`.
- **Portfolio Concurrency:** Maximum portfolio capacity of 20 concurrent active positions; residual capital parked in cash equivalents `[research-proposed]`.

## Required data

- **Universe Definition:** U.S. common equities listed on major national exchanges (NASDAQ / NYSE / AMEX) with market capitalization between $\$30\text{M}$ and $\$500\text{M}$ as of the filing date [source-reported].
- **Liquidity Inclusion Filter:** Trailing 30-day Average Daily Dollar Volume (ADDV) $\ge \$200,000$ [source-reported].
- **Regulatory Filing Feed:** Point-in-time SEC EDGAR Form 4 filings [source-reported].
  - Filter: Transaction code "P" (open-market purchase) only [source-reported].
  - Filter: Reporting lag between transaction date and filing date $\le 90$ days (excludes backdating anomalies and clerical filing errors) [source-reported].
  - Filter: Transaction value $\ge \$5,000$ (filters out de minimis / nominal purchases) [source-reported].
  - Entity Resolution: Mapping parsed Form 4 CUSIPs to permanent security identifiers (PERMNO / FIGI) to handle mergers, ticker changes, and corporate reorganizations [source-reported].
- **Market Data Fields:**
  - Daily OHLCV price series and split/dividend corporate adjustment factors [source-reported].
  - Trailing 52-week rolling high and low prices [source-reported].
  - Trailing 30-day daily return series for historical realized volatility [source-reported].
  - Fama-French 3-Factor daily returns ($R_{\text{MKT}} - R_f$, $SMB$, $HML$, and $R_f$) for 252-day pre-event factor regressions [source-reported].
  - Standard Industrial Classification (SIC) / NAICS codes for biotechnology and pharmaceutical identification [source-reported].
- **Point-in-Time Integrity:** All market cap, volume, and technical features must be indexed strictly to market close on date $t$; the target window starts strictly at $t+1$ to ensure zero look-ahead bias [source-reported].

## Execution assumptions

- **Signal-to-Order Latency:** Filing disclosed on date $t$; order routed for execution at market open on $t+1$ [source-reported].
- **Order Mechanism:** Market open or passive limit orders pegged to the opening auction [source-reported].
- **Execution Frictions & Bid-Ask Spread:**
  - Effective spread in microcap universe: modeled at $2.0\%$ round-trip [source-reported].
  - Price impact: modeled at $1.0\%$ for position sizes of $\approx \$50,000$ [source-reported].
  - Combined round-trip transaction friction: $\approx 3.0\%$ [source-reported].
  - Net return impact: reduces mean CAR in the $>10\%$ momentum bucket from $6.3\%$ to $\approx 3.3\%$ net [source-reported].
- **Borrow & Shorting:** Long-only execution; no short borrowing fees or locates required [source-reported].
- **Capacity Constraint:** Constrained by the $\$200,000$ ADDV lower threshold; single-trade allocation is practically bounded at $\$50,000$ to prevent adverse market impact `[research-proposed]`.

## Evidence

### Source-reported

1. **Empirical Dataset Composition (Table 1 & `outputs/metrics.tex`):**
   - Total analyzed insider purchase transactions: 17,237 [source-reported].
   - Unique issuers: 1,343 [source-reported].
   - Unique corporate insiders: 5,421 [source-reported].
   - Base positive class rate ($CAR_{[1, 30]} > 10\%$): $27.0\%$ [source-reported].
   - Median transaction dollar value: $\$27,000$ [source-reported].
   - Temporal Partitioning:
     - Training set (2018–2022): 11,609 observations [source-reported].
     - Validation set (2023): 2,982 observations [source-reported].
     - Test set (2024): 2,646 observations (709 positive cases, $26.8\%$ base rate) [source-reported].
2. **Out-of-Sample Test Set Classification Performance (2024 Test Set, Table 2):**
   - Logistic Regression (threshold 0.50): AUC = 0.67, Precision = 0.44, Recall = 0.21, F1 = 0.28 [source-reported].
   - Random Forest (threshold 0.50): AUC = 0.69, Precision = 0.52, Recall = 0.21, F1 = 0.30 [source-reported].
   - XGBoost Default (threshold 0.50): AUC = 0.70, Precision = 0.50, Recall = 0.17, F1 = 0.26 [source-reported].
   - XGBoost Optimized (threshold 0.20): AUC = 0.70, Precision = 0.38, Recall = 0.69, F1 = 0.49 [source-reported].
   - Validation set AUC: 0.74, indicating modest temporal decay to 0.70 in out-of-sample 2024 data [source-reported].
3. **Confusion Matrix at Optimized Threshold ($\hat{p} \ge 0.20$):**
   - True Positives (TP): 490 [source-reported].
   - False Positives (FP): 808 [source-reported].
   - False Negatives (FN): 219 [source-reported].
   - True Negatives (TN): 1,129 [source-reported].
   - Model Specificity: $58\%$ ($1,129 / 1,937$) [source-reported].
   - Model Recall: $69\%$ ($490 / 709$) [source-reported].
4. **Feature Importance Decomposition (Table 3, Measured by Average Gain):**
   - 1. `pct_from_52w_high`: 0.360 ($36\%$ of total predictive contribution) [source-reported].
   - 2. `return_mtd`: 0.081 [source-reported].
   - 3. `volatility_30d`: 0.072 [source-reported].
   - 4. `market_cap_at_filing`: 0.066 [source-reported].
   - 5. `pct_from_52w_low`: 0.065 [source-reported].
   - 6. `avg_daily_vol_at_filing`: 0.061 [source-reported].
   - 7. `is_biotech`: 0.060 [source-reported].
   - 8. `price_deviation`: 0.059 [source-reported].
   - 9. `transaction_value`: 0.056 [source-reported].
   - 10. `is_first_purchase_12m`: 0.049 [source-reported].
   - `value_vs_avg_ratio`: 0.043 [source-reported].
   - `insider_title_score`: 0.029 [source-reported].
5. **Abnormal Returns Stratified by Price Deviation at Disclosure (Table 4):**
   - $\le 0\%$ Price Deviation: $N = 10,787$ (1,018 tickers), Mean CAR = $2.3\% \pm 0.6\%$, $\Pr(CAR > 10\%) = 22.6\%$ [source-reported].
   - $0\% - 3\%$ Price Deviation: $N = 1,820$ (488 tickers), Mean CAR = $4.7\% \pm 1.2\%$, $\Pr(CAR > 10\%) = 31.2\%$ [source-reported].
   - $3\% - 5\%$ Price Deviation: $N = 662$ (307 tickers), Mean CAR = $4.4\% \pm 2.5\%$, $\Pr(CAR > 10\%) = 34.9\%$ [source-reported].
   - $5\% - 10\%$ Price Deviation: $N = 793$ (364 tickers), Mean CAR = $4.8\% \pm 2.0\%$, $\Pr(CAR > 10\%) = 36.1\%$ [source-reported].
   - $> 10\%$ Price Deviation: $N = 2,998$ (597 tickers), Mean CAR = $6.3\% \pm 1.4\%$, $\Pr(CAR > 10\%) = 36.7\%$ [source-reported].
   - Difference Test: $t = -5.13$, $p < 0.001$ comparing the lowest ($\le 0\%$) and highest ($> 10\%$) buckets [source-reported].
   - Highest Bucket Distribution: Median CAR = $1.93\%$, Winsorized Mean CAR = $5.44\%$ (confirming the result is not driven by single outliers) [source-reported].
6. **Subsample & Macro Regime Robustness:**
   - Regime Sensitivity: Model predictive power is elevated during low market volatility regimes ($\text{VIX} < 20$) [source-reported].
   - Horizon Sensitivity: Alternative return windows (20-day, 60-day) demonstrate qualitatively consistent patterns, with predictive signal degrading at longer horizons [source-reported].
   - Sector Effects: The biotechnology binary flag ranks 7th in importance (0.060), indicating the effect is broadly distributed across microcap industries rather than concentrated in binary drug trials [source-reported].

### Independently reproduced

Not independently reproduced. The empirical statistics, classification metrics, feature importances, and distribution parameters are captured verbatim from the author's primary manuscript and underlying LaTeX source macros.

### Negative evidence

- **Severe Transaction Cost Attrition:** With microcap effective spreads averaging $\approx 2.0\%$ and market impact averaging $\approx 1.0\%$, approximately $48\%$ of the gross $6.3\%$ CAR in the highest momentum bucket is consumed by frictions, compressing net edge to $\approx 3.3\%$ [source-reported].
- **Sub-50% Classification Precision:** At the F1-optimized threshold ($0.20$), model precision is only $0.38$ ($38\%$). Therefore, $62\%$ of trades triggering an entry fail to generate $>10\%$ cumulative abnormal returns [source-reported].
- **Temporal Degradation:** The ROC AUC decays from $0.74$ on 2023 validation data to $0.70$ on 2024 test data, reflecting non-stationary market regimes [source-reported].
- **Macro Volatility Vulnerability:** Performance degrades substantially during periods of elevated equity market volatility ($\text{VIX} \ge 20$) [source-reported].
- **Pre-Disclosure Information Leakage:** A portion of the $>10\%$ price run-up occurs between the transaction date and public disclosure date (spanning up to 2 business days), indicating that informal leakage or aggressive dealer inventory positioning precedes SEC EDGAR filings [source-reported].

## Falsification plan

To falsify the hypothesis that SEC Form 4 microcap purchases combined with price momentum generate actionable net alpha, execute the following pre-declared empirical tests:

1. **Net Transaction Cost Breakeven Test:** Reconstruct historical order fills across the 2018–2024 event universe using actual NBBO quote spreads and a square-root market impact function calibrated to trade size relative to 30-day ADDV. If the net annualized Sharpe ratio falls below $0.50$ or net CAR is statistically indistinguishable from zero ($t < 1.96$), reject the strategy as an untradable friction artifact `[research-defined falsification threshold]`.
2. **Placebo Disclosure Date Test:** Randomly shuffle disclosure dates within a uniform window of $\pm 45$ trading days for each issuer while preserving market prices and volume series. If the XGBoost classifier achieves an out-of-sample AUC $\ge 0.65$ on shuffled disclosure dates, conclude that the model is fitting unconditional microcap drift rather than an insider information event `[research-defined falsification threshold]`.
3. **Price Deviation Directional Reversal Test:** Construct a long portfolio from transactions in the negative price deviation bucket ($\le 0\%$) and a short portfolio from the top momentum bucket ($> 10\%$). If the net CAR of the negative bucket exceeds that of the positive bucket over a 30-day holding horizon, reject the "slow information incorporation momentum hypothesis" in favor of classical mean reversion `[research-defined falsification threshold]`.
4. **Liquidity Bucket Disappearance Test:** Partition the test sample into three ADDV terciles: $[\$200\text{k}, \$500\text{k}]$, $[\$500\text{k}, \$1.5\text{M}]$, and $>\$1.5\text{M}$. If abnormal returns in the $>\$1.5\text{M}$ bucket exhibit an outperformance probability $\le 27\%$ (the unconditional base rate), confirm that the alpha is an illiquidity-locked phenomenon with zero capacity for institutional scaling `[research-defined falsification threshold]`.
5. **Walk-Forward Out-of-Sample Decay Test:** Apply the frozen 2018–2023 trained model to 2025–2026 filings. If out-of-sample AUC drops below $0.58$ or test precision drops below $0.30$, conclude that the signal has decayed and decommission the candidate `[research-defined falsification threshold]`.

## Crypto portability

- **Portability Classification:** `unproven` / `adapted` (traditional-asset research ported to cryptocurrency).
- **Absence of Regulatory Disclosures:** Cryptocurrencies operate outside the U.S. Securities Exchange Act of 1934 Section 16(a). Foundation officers, protocol developers, and venture investors are not legally required to file standardized 2-day disclosure forms (SEC Form 4) for secondary-market open-market purchases.
- **On-Chain Proxy Adaptation:** A conceptual adaptation involves monitoring verified on-chain treasury multi-sigs, core team vesting smart contracts, and designated venture wallet clusters (tagged via Arkham Intelligence or Nansen). When a known core developer or foundation wallet executes open-market spot accumulation on decentralized exchanges (Uniswap, Curve) or withdraws large token balances from centralized exchanges, an analogous informational signal is triggered [research interpretation].
- **Momentum Confirmation Analogue in Crypto:** The paper's primary conceptual finding—that insider purchases accompanied by price appreciation ($>10\%$ run-up) outperform purchases into flat or falling prices—challenges standard crypto trader instincts to "fade the pump." In illiquid altcoins, early price appreciation following on-chain whale accumulation may reflect prolonged retail diffusion rather than an immediate exit pump [research interpretation].
- **Portability Verdict:** Direct implementation in crypto is impossible due to the lack of regulatory reporting mandates. The on-chain adaptation remains purely theoretical and unproven.

## Limitations

- **Proprietary Hyperparameter Gaps:** While feature sets, validation splits, and evaluation metrics are fully documented, the exact tuned XGBoost hyperparameter dictionary (e.g., maximum depth, subsample ratio, learning rate) and parsing codebase are retained by the author and not published in an open-source repository [data gap].
- **Survivorship & Bankruptcy Delisting Risk:** Microcap equities experience significant rates of OTC delisting, Chapter 11 filings, and reverse stock splits. The source does not explicitly specify how terminal delisting returns were modeled [source limitation].
- **Strict Capacity Ceiling:** Bounded by the $\$200,000$ ADDV lower limit. The aggregate strategy capacity across the entire microcap segment is estimated to be below $\$10\text{M} - \$20\text{M}$ AUM before market impact erodes all net alpha [capacity limitation].
- **Execution Latency Model:** The study assumes next-day execution ($t+1$), ignoring high-frequency automated scraping where algorithmic traders parse SEC EDGAR RSS feeds in milliseconds, potentially exhausting opening-auction liquidity [execution gap].

## Implementation status

- `not-implemented`.
- No prototype or historical execution code has been integrated into PyBroker, NautilusTrader, paper trading, testnet, or live trading systems.
- This record represents a research capture for ChatGPT Intake Review and Hermes Wiki Brain staging.

## Adoption boundary

- `not-approved`.
- `approval_scope: research-only`.
- `status: research-only`.
- This record is an analytical synthesis of external academic research. It does not constitute investment advice, commercial authorization, or approval for live capital allocation.

## Related Wiki records

- `[[quant/microcap-illiquidity-premium-amihud-frictional-decay]]`
- `[[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]]`
- `[[quant/equity-order-flow-kyle-lambda-cross-sectional-liquidity-premium-2026-09-03]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`

## Sources

- **Primary Source:** Hangyi Zhao, *"Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns"*, arXiv preprint `arXiv:2602.06198v1 [q-fin.ST]`, published February 6, 2026. DOI: [10.48550/arXiv.2602.06198](https://doi.org/10.48550/arXiv.2602.06198). URL: [https://arxiv.org/abs/2602.06198](https://arxiv.org/abs/2602.06198).
- **Full Text HTML:** [https://arxiv.org/html/2602.06198v1](https://arxiv.org/html/2602.06198v1).
- **Source Code & Data Package:** arXiv e-print source archive `2602.06198`, containing `refine_3.tex`, `outputs/metrics.tex`, and tables `table1.tex` through `table4.tex`.
- **Foundational Literature Cited in Primary Source:**
  - Amihud, Y. (2002). "Illiquidity and stock returns: cross-section and time-series effects." *Journal of Financial Markets*, 5(1), 31-56.
  - Chen, T., & Guestrin, C. (2016). "XGBoost: A scalable tree boosting system." *Proceedings of the 22nd ACM SIGKDD*, 785-794.
  - Cohen, L., Malloy, C., & Pomorski, L. (2012). "Decoding inside information." *The Journal of Finance*, 67(3), 1009-1043.
  - Fama, E. F., & French, K. R. (1992). "The cross-section of expected stock returns." *The Journal of Finance*, 47(2), 427-465.
  - Fama, E. F., & French, K. R. (1993). "Common risk factors in the returns on stocks and bonds." *Journal of Financial Economics*, 33(1), 3-56.
  - Gu, S., Kelly, B., & Xiu, D. (2020). "Empirical asset pricing via machine learning." *The Review of Financial Studies*, 33(5), 2223-2273.
  - Jaffe, J. F. (1974). "Special information and insider trading." *The Journal of Business*, 47(3), 410-428.
  - Jeng, L. A., Metrick, A., & Zeckhauser, R. (2003). "Estimating the returns to insider trading: A performance-evaluation perspective." *Review of Economics and Statistics*, 85(2), 453-471.
  - Lakonishok, J., & Lee, I. (2001). "Are insider trades informative?" *The Review of Financial Studies*, 14(1), 79-111.
  - Securities and Exchange Commission (SEC). (2002). "Final Rule: Ownership Reports and Trading by Officers, Directors, and Principal Security Holders." Release No. 34-46421.
  - Seyhun, H. N. (1986). "Insiders’ profits, costs of trading, and market efficiency." *Journal of Financial Economics*, 16(2), 189-212.
