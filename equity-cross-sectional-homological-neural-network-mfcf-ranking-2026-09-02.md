---
schema: strategy-research-record-v1
title: "Cross-Sectional Equity Excess Return Forecasting via Homological Neural Networks (HNN) with Maximally Filtered Clique Forest (MFCF) Dependence Architectures"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - homological-neural-network
  - maximally-filtered-clique-forest
  - factor-investing
  - machine-learning
  - sparse-architecture
  - u-s-equities
status: research-only
confidence: medium
source_as_of: 2026-08-14
sources:
  - "Hongyu Lin, Yulin Chen, Yuanrong Wang, Antonio Briola, and Tomaso Aste, 'Dependence-Informed Sparse Neural Architecture for Stock Return Prediction', arXiv preprint arXiv:2608.14323v1 [q-fin.ST, cs.LG], submitted August 14, 2026. Stable URL: https://arxiv.org/abs/2608.14323. Full text HTML: https://arxiv.org/html/2608.14323v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Equity Excess Return Forecasting via Homological Neural Networks (HNN) with Maximally Filtered Clique Forest (MFCF) Dependence Architectures

## Provenance

- **Primary Source:** Hongyu Lin, Yulin Chen, Yuanrong Wang, Antonio Briola, and Tomaso Aste (Department of Computer Science, University College London), *"Dependence-Informed Sparse Neural Architecture for Stock Return Prediction"*, arXiv preprint `arXiv:2608.14323v1 [q-fin.ST, cs.LG]`, submitted August 14, 2026. Stable URL: [https://arxiv.org/abs/2608.14323](https://arxiv.org/abs/2608.14323). Full text HTML: [https://arxiv.org/html/2608.14323v1](https://arxiv.org/html/2608.14323v1).
- **Underlying Empirical Datasets:**
  - **U.S. Common Equities Panel:** Monthly stock returns and accounting data from CRSP and Compustat following the Gu, Kelly, and Xiu (GKX, 2020) sample protocol.
  - **Feature Universe:** 94 firm characteristics covering valuation, momentum/reversal, liquidity, profitability, and investment variables.
  - **Risk-Free Rate:** 1-month Treasury bill rate sourced from Kenneth French's data library.
  - **Sample Horizon:** January 1957 to December 2016. Out-of-sample test window covers 30 annual walk-forward cycles from January 1987 to December 2016 (359 monthly rebalancing periods).
- **Foundational Literature:**
  - Gu, S., Kelly, B., and Xiu, D. (2020), "Empirical asset pricing via machine learning", *The Review of Financial Studies* 33(5), 2223–2273 — standard machine learning benchmark in cross-sectional equity asset pricing (NN3 architecture).
  - Massara, G. P. and Aste, T. (2019), "Learning clique forests", arXiv preprint `arXiv:1905.02266` — Maximally Filtered Clique Forest (MFCF) graph filtering algorithm.
  - Wang, Y., Lin, H., and Aste, T. (2023), "Homological neural networks: a new architecture for data with higher-order relations", *Machine Learning: Science and Technology* 4(4), 045055.
  - Lin, H., Briola, A., Wang, Y., and Aste, T. (2026), "Compositional sparsity in homological neural networks", *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
  - Tumminello, M., Aste, T., Di Matteo, T., and Mantegna, R. N. (2005), "A tool for filtering information in complex systems", *PNAS* 102(30), 10421–10426.
  - Holm, S. (1979), "A simple sequentially rejective multiple test procedure", *Scandinavian Journal of Statistics* 6(2), 65–70 — multiple-testing adjustment.

## Economic mechanism

### Source-reported

1. **Interpretability Void in Machine Learning Asset Pricing:** While multilayer perceptrons (MLPs) improve cross-sectional return forecasts by capturing non-linear interactions among firm characteristics (Gu et al., 2020), their depth and layer widths are chosen via arbitrary grid search or heuristic tuning with no economic or financial rationale.
2. **Dense Overparameterization vs. Characteristic Sparsity:** Characteristics related to valuation, liquidity, momentum, and investment exhibit strong empirical co-dependencies. Standard fully connected MLPs ignore this structure, attempting to estimate every possible pairwise and higher-order connection, resulting in severe overparameterization and susceptibility to noise.
3. **Graph-Filtered Higher-Order Interactions via MFCF:** The Maximally Filtered Clique Forest (MFCF) filters a dense empirical correlation matrix of firm characteristics into a sparse chordal graph (a collection of overlapping cliques) under topological constraints. The maximum clique size $K$ directly bounds the highest interaction order the network can represent, giving network depth and layer widths a direct financial and graphical interpretation prior to training.
4. **Homological Neural Networks (HNN):** HNN maps the MFCF clique complex directly into neural network layers via simplicial set inclusion: individual characteristics form the input layer, 2-cliques (edges) form the second layer, and higher-order cliques form subsequent layers. Connections exist only between a lower-order clique and a higher-order clique containing it ($C' \subset C$). This guarantees architectural sparsity by construction without requiring post-hoc $L_1$ weight pruning.

### Research interpretation

The alpha thesis operates as an **interpretable, dependence-regularized cross-sectional equity ranking model**:
1. **Interaction-Order Regularization:** In cross-sectional equity data, signals have very low signal-to-noise ratios ($R^2 < 1\%$). By constraining connections to only empirically observed characteristic cliques of bounded size $K \le 5$, the model eliminates 98.7% of the parameters present in a standard dense MLP ($\approx 21.0\text{k}$ parameters vs. $1,680.7\text{k}$ for MLP-HNN), preventing the neural network from memorizing spurious higher-order factor noise.
2. **Decile Spread Generation:** The model improves cross-sectional ranking accuracy (Pearson Information Coefficient of 0.0642 vs. 0.0586 for NN3), producing a wider equal-weighted long-short decile spread (3.95% gross, 3.34% net of 25 bps transaction costs, with an annualized Sharpe ratio of 2.28).

## Signal

### Signal Definition and Model Architecture

1. **Input Normalization:**
   At each month $t$, for each stock $i \in \{1, \ldots, N_t\}$, collect $p = 94$ firm characteristics $x_{i, t} \in \mathbb{R}^p$. Characteristics are cross-sectionally rank-transformed to the interval $[-1, 1]$:
   $$\widetilde{x}_{i, t}^{(j)} = \frac{2 \cdot \operatorname{rank}(x_{i, t}^{(j)})}{N_t + 1} - 1, \quad j = 1, \ldots, 94$$
2. **Dependence Graph Estimation (MFCF):**
   Compute the empirical absolute Pearson correlation matrix $D \in \mathbb{R}^{p \times p}$ of ranked characteristics across the training panel:
   $$D_{a, b} = |\operatorname{Corr}(X_a, X_b)|$$
   The MFCF greedily builds a clique forest $\mathcal{C}$ by adding characteristics that maximize clique-separator correlation gains while preserving chordality and bounding the maximum clique size by $K \in \{2, 3, 4, 5\}$.
3. **Homological Neural Network Layer Construction:**
   - Layer 1 (Input): $p = 94$ nodes representing single characteristics (1-cliques).
   - Layer 2: Nodes corresponding to all retained 2-cliques (edges) in $\mathcal{C}$.
   - Layer $k$ ($k \le K$): Nodes corresponding to all retained $k$-cliques in $\mathcal{C}$.
   - Directed Connectivity: Node $u$ in Layer $k-1$ connects to Node $v$ in Layer $k$ if and only if the clique represented by $u$ is a strict subset of the clique represented by $v$ ($C_u \subset C_v$).
   - Output Layer: A linear layer aggregating the final layer representations to produce predicted excess return $\widehat{R}_{i, t+1}$.
4. **Variants:**
   - **HNN (marginal):** Architecture constructed strictly from characteristic correlation matrix $D$.
   - **HNN (m-s):** Architecture augmented with separate sign-conditioned subgraphs based on above-median vs. below-median returns.
5. **Portfolio Formation & Execution Rule:**
   - At each month-end $t$, rank all stocks in the cross-section by predicted 1-month-ahead excess return $\widehat{R}_{i, t+1}$.
   - Form 10 decile portfolios.
   - Long Top Decile (Decile 10, highest predicted returns) and Short Bottom Decile (Decile 1, lowest predicted returns).
   - Holdings are held for 1 month and rebalanced monthly.

## Required data

- **Universe:** All U.S. common stocks listed on NYSE, AMEX, and NASDAQ from January 1957 to December 2016.
- **Predictor Features:** 94 firm-level accounting and price characteristics following Gu, Kelly, and Xiu (2020), including:
  - Momentum: 1-month reversal (`mom1m`), 12-month momentum (`mom12m`), 36-month momentum (`mom36m`), intermediate momentum (`mom6m`);
  - Valuation: Book-to-market (`bm`), earnings-to-price (`ep`), cash-flow-to-price (`cfp`), sales-to-price (`sp`);
  - Volatility & Risk: Idiosyncratic volatility (`idiovol`), market beta (`beta`), return variance (`retvol`);
  - Liquidity: Amihud illiquidity (`ill`), turnover (`turn`), bid-ask spread (`baspread`);
  - Investment & Profitability: Asset growth (`agr`), capital expenditures (`invest`), return on equity (`roe`), return on assets (`roa`).
- **Target Variable:** One-month-ahead monthly stock return in excess of the 1-month Treasury bill rate ($R_{i, t+1} - R_{t+1}^f$).
- **Preprocessing:** Cross-sectional ranking to $[-1, 1]$ per characteristic each month; missing characteristics imputed to median (zero in ranked scale).

## Execution assumptions

- **Rebalancing Cadence:** Monthly at the end of each calendar month.
- **Holding Period:** Exactly 1 calendar month (359 out-of-sample monthly rebalances from 1987 to 2016).
- **Weighting Schemes:**
  - Equal-Weighted (EW): Each stock within Decile 1 and Decile 10 receives equal weight $1 / N_{\text{decile}}$.
  - Asset-Weighted (AW): Each stock is weighted by its lagged market equity ($ME_{i, t}$).
- **Turnover:** Mean total one-way turnover across two unit-notional legs is 1.25 for HNN (marginal) EW (1.36 for AW).
- **Transaction Costs:** Modeled at 25 basis points ($0.0025$) per dollar traded on both long and short legs.
- **Shorting Assumptions:** Unconstrained shorting permitted in the bottom decile with zero borrow fee modeled (provenance gap: hard-to-borrow fees in small-cap stocks omitted).

## Evidence

### Source-reported

All figures, test statistics, and parameter counts trace directly to Lin, Chen, Wang, Briola, and Aste (arXiv:2608.14323v1, Section 5, Tables 2–3, Figures 2–4):

1. **Out-of-Sample Performance Comparison (1987–2016, 359 months, Table 2):**
   - **HNN (marginal):**
     - Out-of-sample $R^2_{\mathrm{oos}}$: **0.509%**
     - MAE: 0.1059
     - Pearson IC: **0.0642** (statistically significantly higher than NN3 by $+0.0056$, unadjusted $p=0.002$, Holm multiple-comparison adjusted $p=0.034$)
     - Spearman IC: **0.0517** ($p=0.178$ vs NN3)
     - Equal-Weighted (EW) Gross Spread: **3.95%** per month
     - Asset-Weighted (AW) Gross Spread: 1.99% per month
     - Trainable Parameters: **21.0k** (median per ensemble member across annual refits)
   - **HNN (m-s):**
     - $R^2_{\mathrm{oos}}$: **0.511%** (highest pooled $R^2$)
     - MAE: 0.1058
     - Pearson IC: 0.0610
     - Spearman IC: 0.0491
     - EW Gross Spread: 3.85% per month, AW Gross Spread: 2.00% per month
     - Trainable Parameters: **5.2k**
   - **NN3 (Gu, Kelly, Xiu 2020 Benchmark):**
     - $R^2_{\mathrm{oos}}$: 0.475%
     - MAE: 0.1057
     - Pearson IC: 0.0586
     - Spearman IC: 0.0474
     - EW Gross Spread: 3.75% per month, AW Gross Spread: 2.44% per month
     - Trainable Parameters: 3.8k
   - **HNN (input-shuffled ablation):**
     - $R^2_{\mathrm{oos}}$: 0.496%, Pearson IC: 0.0597, Spearman IC: 0.0490, EW Spread: 3.73%, AW Spread: 1.91%, Parameters: 21.0k
   - **MLP-HNN (fully connected network with identical induced layer widths):**
     - $R^2_{\mathrm{oos}}$: 0.429%, Pearson IC: 0.0524, Spearman IC: 0.0436, EW Spread: 3.47%, AW Spread: 2.48%, Parameters: **1,680.7k** (1.68 million parameters)
   - **Linear Baselines:**
     - Huber-3: $R^2_{\mathrm{oos}} = -0.137\%$, Pearson IC = 0.0227, EW Spread = 0.51%, Parameters = 4
     - PCR (Principal Component Regression): $R^2_{\mathrm{oos}} = 0.336\%$, Pearson IC = 0.0437, EW Spread = 2.87%, Parameters = 81

2. **Parameter Economy:**
   HNN (marginal) matches or exceeds the predictive ranking of dense architectures while utilizing **80 times fewer parameters** than MLP-HNN ($21.0\text{k}$ vs. $1,680.7\text{k}$).

3. **Transaction Cost Sensitivity & Turnover (Table 3):**
   - **Equal-Weighted Portfolios (EW, 25 bps/dollar traded cost):**
     - HNN (marginal): Turnover = 1.25, Net Monthly Spread = **3.34%**, Annualized Sharpe Ratio = **2.28**, Break-even Cost = **159 bps**
     - HNN (m-s): Turnover = 1.24, Net Monthly Spread = 3.24%, Annualized Sharpe Ratio = 2.24, Break-even Cost = 156 bps
     - NN3: Turnover = 1.23, Net Monthly Spread = 3.13%, Annualized Sharpe Ratio = 2.17, Break-even Cost = 153 bps
     - HNN (input-shuffled): Turnover = 1.26, Net Monthly Spread = 3.12%, Annualized Sharpe Ratio = 2.11, Break-even Cost = 149 bps
     - MLP-HNN: Turnover = 1.15, Net Monthly Spread = 2.91%, Annualized Sharpe Ratio = 1.93, Break-even Cost = 151 bps
   - **Asset-Weighted Portfolios (AW, 25 bps/dollar traded cost):**
     - HNN (marginal): Turnover = 1.36, Net Monthly Spread = 1.31%, Annualized Sharpe Ratio = 0.73, Break-even Cost = 73 bps
     - NN3: Turnover = 1.35, Net Monthly Spread = **1.78%**, Annualized Sharpe Ratio = **0.95**, Break-even Cost = 91 bps

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- **Pronounced Degradation under Asset Weighting:** While HNN (marginal) achieves a strong EW Sharpe ratio of 2.28 (net spread 3.34%/mo), its Asset-Weighted performance drops drastically to Sharpe 0.73 (net spread 1.31%/mo). Under AW, the dense NN3 benchmark outperforms HNN (marginal) with a Sharpe of 0.95 and net spread of 1.78%. This confirms that HNN's cross-sectional ranking alpha is heavily concentrated in smaller-cap stocks where liquidity is lower and real-world trading frictions are highest.
- **Statistical Indistinguishability on $R^2$ and Spearman IC:** Although HNN achieves higher pooled $R^2$ ($0.509\%$ vs. $0.475\%$) and Spearman IC ($0.0517$ vs. $0.0474$) than NN3, these differences are not statistically significant ($p = 0.796$ and $p = 0.178$, respectively). Only Pearson IC survives Holm multiple-comparison adjustment.
- **Omission of Borrow Fees:** The backtest assumes equal shorting capability across all stocks, including small caps. In practice, borrow fees and locate constraints on bottom-decile microcap equities would erode a portion of the short leg's returns.

## Falsification plan

1. **Large-Cap / Liquid-Cap Sub-Universe Test:** Re-run the HNN (marginal) ranking model on the S&P 500 or Russell 1000 universe. If the resulting net spread drops below 0.50% per month or the net Sharpe ratio falls below 0.50, reject the hypothesis that the HNN alpha generalizes to institutional-capacity portfolios.
2. **Alternative Graph Filtering Comparison:** Replace the MFCF filter with Graphical Lasso (GLASSO) and Planar Maximally Filtered Graph (PMFG). If HNN based on MFCF does not produce a statistically significant ranking improvement over GLASSO-derived sparse networks ($p > 0.10$), reject the claim of MFCF's specific architectural advantage.
3. **Characteristic Permutation Placebo Test:** Randomly shuffle the order of characteristics before MFCF graph generation. If the shuffled model achieves Pearson IC within 5% of the genuine HNN ($> 0.0610$), falsify the claim that structural characteristic groupings drive the empirical ranking advantage.
4. **Post-2016 Out-of-Sample Evaluation:** Evaluate model predictions from 2017 to 2026 without refitting the 1987–2016 hyperparameters. If $R^2_{\mathrm{oos}} \le 0$, reject the long-term temporal persistence of the factor dependence structure.

## Crypto portability

- **Portability:** `adapted` / `unproven` (demonstrated exclusively on U.S. common equities from 1957 to 2016; ported to cryptocurrency as a research interpretation).
- **Crypto-Specific Adaptation Requirements:**
  - **Feature Universe Redefinition:** The 94 accounting-based characteristics (e.g. book-to-market, R&D, capital expenditures) do not exist for most crypto assets. A crypto HNN requires reconstructing a native cross-sectional feature set based on:
    - On-chain metrics: Active addresses, NVT, SOPR, token velocity, holder concentration;
    - Market microstructure: Funding rate momentum, perpetual basis, open interest velocity, DEX liquidity depth, 30-day realized volatility;
    - Momentum/Reversal: 1-day, 7-day, and 30-day returns.
  - **Universe Size & Survivorship:** The U.S. equity universe contains thousands of stocks, whereas the liquid crypto perpetual universe consists of 100–300 tokens. The MFCF graph filter must be verified on smaller cross-sections ($p \approx 30\text{–}50$ features).
  - **24/7 Session Boundaries:** Crypto markets trade continuously; monthly or weekly rebalancing requires establishing fixed UTC timestamp conventions.

## Limitations

- `not independently reproduced`;
- **Small-Cap Concentration:** The alpha is substantially stronger in equal-weighted portfolios (Sharpe 2.28) than in market-cap weighted portfolios (Sharpe 0.73), indicating capacity limits for large institutional capital;
- **Stationarity Assumption of Characteristic Graph:** While graphs and weights are re-estimated annually, the MFCF structural hyperparameter $K$ is held constant within 5-year blocks;
- **Preprint Source:** Sourced from an academic preprint (arXiv:2608.14323v1) submitted August 2026, subject to ongoing peer review;
- **Long-Short Borrow Cost Gap:** Real-world borrow fees and short locate availability on bottom-decile stocks are not modeled.

## Implementation status

- `not-implemented`. Research capture only; no NautilusTrader, PyBroker, paper, testnet, or live trading modules have been constructed or authorized.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures academic research on graph-filtered neural network architectures for cross-sectional factor ranking. It does not authorize deployment to paper, testnet, or live trading systems.

## Related Wiki records

- `[[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]` — Cross-sectional deep learning equity reversal.
- `[[quant/mingle-exposure-locality-factor-graph-portfolio-diversification-2026-09-02]]` — Factor graph frameworks for portfolio diversification.
- `[[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]]` — Factor compression in cross-sectional asset pricing.

## Sources

1. Hongyu Lin, Yulin Chen, Yuanrong Wang, Antonio Briola, and Tomaso Aste, *"Dependence-Informed Sparse Neural Architecture for Stock Return Prediction"*, arXiv preprint `arXiv:2608.14323v1 [q-fin.ST, cs.LG]`, submitted August 14, 2026. Stable URL: [https://arxiv.org/abs/2608.14323](https://arxiv.org/abs/2608.14323). Full text HTML: [https://arxiv.org/html/2608.14323v1](https://arxiv.org/html/2608.14323v1).
2. Gu, S., Kelly, B., and Xiu, D. (2020), "Empirical asset pricing via machine learning", *The Review of Financial Studies* 33(5), 2223–2273. DOI: [10.1093/rfs/hhaa009](https://doi.org/10.1093/rfs/hhaa009).
3. Massara, G. P. and Aste, T. (2019), "Learning clique forests", arXiv preprint `arXiv:1905.02266` [cs.SI]. Stable URL: [https://arxiv.org/abs/1905.02266](https://arxiv.org/abs/1905.02266).
4. Wang, Y., Lin, H., and Aste, T. (2023), "Homological neural networks: a new architecture for data with higher-order relations", *Machine Learning: Science and Technology* 4(4), 045055. DOI: [10.1088/2632-2153/ad0de3](https://doi.org/10.1088/2632-2153/ad0de3).
5. Lin, H., Briola, A., Wang, Y., and Aste, T. (2026), "Compositional sparsity in homological neural networks", *IEEE Transactions on Pattern Analysis and Machine Intelligence*. DOI: [10.1109/TPAMI.2026.3530011](https://doi.org/10.1109/TPAMI.2026.3530011).
6. Tumminello, M., Aste, T., Di Matteo, T., and Mantegna, R. N. (2005), "A tool for filtering information in complex systems", *Proceedings of the National Academy of Sciences* 102(30), 10421–10426. DOI: [10.1073/pnas.0500298102](https://doi.org/10.1073/pnas.0500298102).
7. Holm, S. (1979), "A simple sequentially rejective multiple test procedure", *Scandinavian Journal of Statistics* 6(2), 65–70. Stable URL: [https://www.jstor.org/stable/4615733](https://www.jstor.org/stable/4615733).
