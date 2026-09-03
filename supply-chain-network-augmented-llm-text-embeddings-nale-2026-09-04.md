---
schema: strategy-research-record-v1
title: Supply Chain Knowledge Graph Propagation of LLM Textual Embeddings for Cross-Sectional Equity Alpha (NALE)
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - llm-embeddings
  - supply-chain
  - knowledge-graph
  - finbert
  - equity
  - factor-investing
status: research-only
confidence: medium
source_as_of: 2025-12
sources:
  - https://arxiv.org/abs/2606.29290
  - https://doi.org/10.48550/arXiv.2606.29290
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Supply Chain Knowledge Graph Propagation of LLM Textual Embeddings for Cross-Sectional Equity Alpha (NALE)

## Provenance

- **Primary Source:** Asef Yılkı (Institute of Banking and Insurance, Department of Banking, Marmara University, Istanbul, Turkey; ORCID: 0000-0003-0683-7218), *"Supply Chain Propagation of Textual Signals: LLM Embeddings and Cross-Sectional Return Predictability"*, arXiv preprint `arXiv:2606.29290v1 [q-fin.PR, q-fin.ST]`, submitted June 2026.
- **Canonical DOI:** [10.48550/arXiv.2606.29290](https://doi.org/10.48550/arXiv.2606.29290).
- **Traceable Source URL:** [https://arxiv.org/abs/2606.29290](https://arxiv.org/abs/2606.29290). Full text PDF: [https://arxiv.org/pdf/2606.29290](https://arxiv.org/pdf/2606.29290).
- **Empirical Sample / Data As-Of:** January 2011 through December 2025 (174 calendar months, 155 usable monthly cross-sections meeting the minimum 20-firm estimation threshold); 2,365 annual 10-K filings across 261 unique firms; 24,723 firm-month observations across 255 S&P 500 constituents.
- **Direct Source Verification:** The complete 30-page primary research paper was directly downloaded from arXiv (`arXiv:2606.29290`) and audited in full. All mathematical formulations, FinBERT layer parameters, PCA variance contributions, propagation formulas, Fama–MacBeth regression estimates (Table 2), long-short quintile portfolio metrics (Table 3), decile return spreads (Table 4), information coefficients (Table 5), and robustness statistics trace directly to the primary paper.
- **Deduplication Check:** A repository-wide audit confirmed zero matching records for `2606.29290`, author `Asef Yılkı` (or `Yilki`), `NALE`, or `net_pc_5`. While existing repository records cover LLM alpha discovery (e.g. `[[quant/alphacrafter-harness-driven-multi-agent-llm-alpha-discovery-2026-09-03]]`, `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]`, and `[[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]]`), this record provides a materially distinct economic thesis: augmenting annual corporate disclosure embeddings via production network propagation across inter-firm supply chain knowledge graphs.

## Economic mechanism

### Source-reported

The author posits that the cross-section of expected stock returns is shaped not only by isolated firm-level disclosures but by the production network of customer-supplier relationships in which firms operate.

1. **Informational Content of Annual Disclosures:** Textual disclosures in the Management's Discussion and Analysis (MD&A, Item 7) section of annual 10-K filings contain management's forward-looking assessments of operating performance, liquidity, and capital resources. Prior literature demonstrates that changes in MD&A language predict future returns and corporate operations (Cohen, Malloy, & Nguyen, 2020), and that LLM embeddings of financial text capture return-predictive information beyond conventional technical and fundamental signals (Chen, Kelly, & Xiu, 2025).
2. **Economic Transmission Across Supply Chains:** Modern firms are interconnected through customer-supplier linkages. Shocks originating at upstream suppliers (input shortages, cost spikes, margin compression) propagate downstream to customer firms (Barrot & Sauvagnat, 2016).
3. **Investor Inattention and Delayed Price Discovery:** Under bounded investor rationality and attention constraints (Cohen & Frazzini, 2008; Hirshleifer & Teoh, 2003), investors focus primarily on direct corporate disclosures and fail to immediately trace how textual risk signals propagate across economic links. When a supplier's MD&A reports deteriorating conditions, investors in downstream customer firms underreact, creating delayed, predictable return co-movements across linked firms.
4. **Network-Augmented LLM Embeddings (NALE):** Propagating firm-level FinBERT embeddings through a supply chain knowledge graph prior to factor extraction captures these information spillovers before they are fully priced into downstream equity shares.

### Research interpretation

The falsifiable research hypothesis is an **inter-firm information transmission and bounded-attention hypothesis**:

1. **Subsumption of Direct LLM Embeddings:** If the primary source of cross-sectional predictability in corporate textual disclosures is network transmission rather than standalone firm sentiment, network-augmented embeddings (`net_pc_5`) will subsume direct LLM embeddings (`pc_5`) in multi-factor specifications.
2. **Orthogonality to Systematic Risk Premia:** The return predictability generated by supply chain propagation reflects information transmission frictions rather than compensation for systematic risk, implying that the resulting alpha will survive controls for momentum, short-term reversal, volatility, firm size, and the Fama–French five-factor model (Mkt-RF, SMB, HML, RMW, CMA).
3. **Network Content vs. Topology:** The incremental predictive power must stem from genuine economic relationships rather than artifactual graph properties (rejectable via random graph edge reshuffling).
4. **Asymmetry Under Short-Sale Constraints:** If mispricing driven by investor inattention is exacerbated by limits to arbitrage, return predictability will concentrate in the short leg (overpriced firms with supplier distress).

## Signal

### Preprocessing and Document Representation

1. **Text Extraction:** Extract the MD&A section (Item 7) from annual 10-K filings via the SEC EDGAR API (`data.sec.gov/submissions`), delimited between the strings `"Item 7. Management's Discussion and Analysis"` and `"Item 7A. Quantitative and Qualitative Disclosures About Market Risk"`.
2. **Truncation Rule:** Retain the first 8,000 characters of the extracted Item 7 text (the average MD&A document in the sample contains ~6,800 characters; this boundary captures early sections on operating performance, liquidity, and capital resources while ensuring uniform computational bounds).
3. **FinBERT Encoding:** Encode each truncated MD&A document using `ProsusAI/FinBERT` (Araci, 2019; 12 transformer layers, 768 hidden dimensions, pre-trained on Reuters TRC2 financial news from 2008–2010). Compute the document embedding via mean pooling across all final-layer tokens:
   $$\mathbf{e}_{i,t}^{\text{raw}} = \text{MeanPool}(\text{FinBERT}(d_{i,t})) \in \mathbb{R}^{768}$$
4. **Unit Normalization:** Apply $\ell_2$-normalization to enable cosine-distance and bounded weighted averaging:
   $$\mathbf{e}_{i,t} = \frac{\mathbf{e}_{i,t}^{\text{raw}}}{\|\mathbf{e}_{i,t}^{\text{raw}}\|_2} \in \mathbb{R}^{768}$$

### Supply Chain Knowledge Graph Propagation

1. **Graph Specification:** Represent the supply chain as a directed weighted graph $G = (V, E, W)$, where $V$ is the set of firm nodes, $E \subseteq V \times V$ represents documented supplier-customer relationships, and $W: E \rightarrow [0, 1]$ assigns edge weights $w_{ji}$ reflecting input specificity and revenue dependence following Barrot & Sauvagnat (2016).
2. **Predecessor Mapping:** For each firm $i \in V$, define the set of upstream suppliers:
   $$\mathcal{P}(i) = \{j : (j, i) \in E\}$$
3. **Propagation Operator:** Augment firm $i$'s embedding by convexly combining its direct embedding with the weighted average of its upstream suppliers' embeddings:
   $$\tilde{\mathbf{e}}_i = \begin{cases} (1 - \alpha)\,\mathbf{e}_i + \alpha \cdot \frac{\sum_{j \in \mathcal{P}(i)} w_{ji}\,\mathbf{e}_j}{\sum_{j \in \mathcal{P}(i)} w_{ji}}, & \text{if } \mathcal{P}(i) \neq \emptyset \\ \mathbf{e}_i, & \text{otherwise} \end{cases}$$
   where $\alpha \in [0, 1]$ is the network propagation weight. Baseline parameter: $\alpha = 0.4$.

### Dimensionality Reduction (PCA)

1. **Feature Standardization:** Standardize each of the 768 embedding dimensions across all firm-year observations to have zero mean and unit variance.
2. **Unsupervised PCA:** Extract the leading $K = 10$ principal components from the standardized embedding space. The top 10 components account for 66.2% of total embedding variance.
3. **Projection:** Let $\mathbf{P} \in \mathbb{R}^{768 \times 10}$ denote the loading matrix. Compute factor scores for direct and network-augmented embeddings using the identical transformation matrix $\mathbf{P}$:
   $$\mathbf{f}_{i,t}^{\text{direct}} = \mathbf{P}^\top \mathbf{e}_{i,t} \in \mathbb{R}^{10}, \quad \mathbf{f}_{i,t}^{\text{network}} = \mathbf{P}^\top \tilde{\mathbf{e}}_{i,t} \in \mathbb{R}^{10}$$
4. **Primary Signal Extraction:** Extract the fifth principal component ($k = 5$):
   - Direct factor: $\text{pc\_5}_{i,t} = f_{i,t,5}^{\text{direct}}$
   - Network-augmented factor: $\text{net\_pc\_5}_{i,t} = f_{i,t,5}^{\text{network}}$

### Trading Rule & Portfolio Construction

1. **Temporal Alignment (Zero Look-Ahead):** Each annual 10-K filing is linked to forward monthly stock returns beginning the month after the SEC acceptance date. The factor score remains constant for each firm across the 12-month window until the next annual filing.
2. **Ranking & Slicing:** At the end of each month $t$, rank all available universe firms by their latest observable $\text{net\_pc\_5}_{i,t}$ factor score.
3. **Long-Short Allocation:** Due to negative empirical Fama–MacBeth slope ($\gamma < 0$), low factor scores predict higher subsequent returns:
   - **Long Leg ($Q_1$):** Equal-weight the bottom quintile (lowest 20% of $\text{net\_pc\_5}$ scores).
   - **Short Leg ($Q_5$):** Equal-weight the top quintile (highest 20% of $\text{net\_pc\_5}$ scores).
   - **Spread Return:** $R_{t+1}^{LS} = \frac{1}{|Q_1|} \sum_{i \in Q_1} r_{i,t+1} - \frac{1}{|Q_5|} \sum_{i \in Q_5} r_{i,t+1}$.
4. **Holding Period:** Rebalanced monthly at month-end closing prices.

## Required data

- **Universe:** Constituent firms of the S&P 500 index with at least 24 consecutive months of return data and at least one 10-K filing within the sample window (unbalanced panel of 255 firms).
- **Timeframe / Sample Period:** January 2011 to December 2025 (174 calendar months; 155 usable monthly cross-sections meeting the minimum 20-firm estimation threshold).
- **Pricing Data:** Monthly split- and dividend-adjusted closing prices from Yahoo Finance.
- **Textual Data:** Full-text annual 10-K filings from SEC EDGAR API (`data.sec.gov/submissions`), indexed by CIK, with SEC acceptance timestamps.
- **Network Data:** Supply chain knowledge graph comprising 48 firm nodes and 51 directed edges constructed from regulatory filings, corporate disclosures, and industry reports, weighted by input specificity and revenue dependence (Barrot & Sauvagnat, 2016).
- **Characteristic Controls:**
  - *Momentum:* Cumulative return from month $t-12$ to month $t-2$ (1-month skip to avoid reversal).
  - *Short-Term Reversal:* Return in month $t-1$.
  - *Volatility:* Annualized standard deviation of monthly returns over months $t-12$ to $t-1$.
  - *Log Price:* $\ln(\text{Price}_{t})$, serving as a parsimonious market-cap/size proxy.
  - All characteristics cross-sectionally standardized each month to zero mean, unit variance.

## Execution assumptions

- **Execution Cadence:** Monthly rebalancing at month-end closing prices.
- **Signal-to-Execution Timing:** The signal uses the SEC acceptance timestamp and applies to returns starting the subsequent month, ensuring that the 10-K filing is public before execution.
- **Transaction Costs:** Evaluated at 0 bps (gross) and 20 bps round-trip per month (net), with sensitivity tested over 10 to 30 bps round-trip.
- **Shorting / Borrow Assumptions:** Assumes unconstrained short selling for S&P 500 large-cap constituents; actual institutional borrow fees, locate availability, and dividend liability on short positions are omitted from the source's empirical model.
- **Slippage & Market Impact:** Omitted from explicit modeling; liquidity is assumed sufficient given the large-cap S&P 500 setting and monthly rebalancing frequency.

## Evidence

### Source-reported

All quantitative figures below trace directly to Yılkı (arXiv:2606.29290v1, June 2026):

#### 1. Fama–MacBeth Cross-Sectional Regressions (Table 2)
Estimates from 155 monthly cross-sections (255 firms), Newey–West standard errors with 6 lags:

| Variable | Model 1 (Direct LLM) | Model 2 (Network KG) | Model 3 (LLM + KG + Controls) |
| :--- | :--- | :--- | :--- |
| **Intercept** | $+0.0135^{***}$ ($t = 3.67$) | $+0.0137^{***}$ ($t = 3.76$) | $+0.0135^{***}$ ($t = 4.98$) |
| **pc_5** | $-0.0003^{**}$ ($t = -2.12$) | — | $+0.0000$ ($t = 0.31$) |
| **net_pc_5** | — | $-0.0005^{***}$ ($t = -2.60$) | $-0.0004^{***}$ ($t = -2.64$) |
| **Momentum** | — | — | $+0.0008$ ($t = 0.57$) |
| **Reversal** | — | — | $-0.0007$ ($t = -0.56$) |
| **Volatility** | — | — | $+0.0063^{**}$ ($t = 2.53$) |
| **Log Price** | — | — | $+0.0043^{***}$ ($t = 4.46$) |

*Key finding:* In Model 3, `net_pc_5` retains its statistical significance ($t = -2.64$), whereas the direct LLM factor `pc_5` drops to $t = 0.31$, demonstrating complete subsumption of direct text embeddings by network-augmented embeddings.

#### 2. Long–Short Quintile Portfolio Performance (Table 3)
Equal-weighted quintile portfolios sorted monthly (Sample: 2011–2025):

| Performance Metric | Model 1 (pc_5) | Model 2 (net_pc_5) | S&P 500 Benchmark |
| :--- | :--- | :--- | :--- |
| **Annualized Return** | $6.1\%$ | $10.9\%$ | $14.6\%$ |
| **Annualized Volatility** | $10.8\%$ | $12.6\%$ | $14.2\%$ |
| **Sharpe Ratio (Gross)** | $0.56$ | $0.86$ | $1.03$ |
| **Sharpe Ratio (Net, 20 bps)** | $0.34$ | $0.67$ | — |
| **Maximum Drawdown** | $-13.8\%$ | $-16.9\%$ | $-23.9\%$ |
| **Fama–French 5-Factor Alpha** | $2.14\%$ ($t = 0.92$) | $7.27\%$ ($t = 2.30^{**}$) | — |
| **FF5 Factor Spanning $R^2$** | $0.119$ | $0.185$ | — |

*Key finding:* The low factor-spanning $R^2$ of 0.185 confirms that `net_pc_5` alpha is largely orthogonal to conventional market, size, value, profitability, and investment risk factors. Rolling 24-month Sharpe ratio for Model 2 peaked at 2.51 during 2020–2021.

#### 3. Decile Portfolio Distribution (Table 4)
Equal-weighted deciles sorted monthly on `net_pc_5` (2011–2025):

| Decile | Annual Return | Annualized Sharpe | $t$-statistic | Leg Allocation |
| :--- | :--- | :--- | :--- | :--- |
| **D1** | $20.3\%$ | $1.18$ | $4.07$ | Core of Short Leg |
| **D2** | $21.1\%$ | $1.16$ | $3.99$ | Core of Short Leg |
| **D3** | $14.9\%$ | $0.98$ | $3.38$ | Neutral |
| **D4** | $13.7\%$ | $0.76$ | $2.62$ | Neutral |
| **D5** | $13.9\%$ | $0.70$ | $2.43$ | Neutral |
| **D6** | $15.0\%$ | $0.86$ | $2.97$ | Neutral |
| **D7** | $15.1\%$ | $0.89$ | $3.07$ | Neutral |
| **D8** | $12.7\%$ | $0.65$ | $2.26$ | Neutral |
| **D9** | $11.6\%$ | $0.65$ | $2.26$ | Neutral |
| **D10** | $11.7\%$ | $0.66$ | $2.29$ | Core of Long Leg |
| **Spread (D1 $-$ D10)** | $-8.6\%$ | — | — | Short-minus-Long Spread |

*Key finding:* Returns decrease across deciles, with the steepest gradient in D1–D2, consistent with short-sale constraints and arbitrage asymmetry (Stambaugh, Yu, & Yuan, 2015).

#### 4. Information Coefficient Dynamics (Table 5)
Monthly Spearman rank correlation between factor scores and forward 1-month returns (155 months):

| Metric | Model 1 (pc_5) | Model 2 (net_pc_5) |
| :--- | :--- | :--- |
| **Mean IC (Spearman)** | $-0.022$ | $+0.029$ |
| **IC $t$-statistic** | $-2.11^{**}$ | $+2.30^{**}$ |
| **IC Standard Deviation** | $0.130$ | $0.157$ |
| **Information Ratio (IC / SD)** | $-0.170$ | $+0.185$ |
| **Hit Rate ($\% \text{ months } > 0$)** | $45.2\%$ | $54.2\%$ |

#### 5. Robustness and Sensitivity Results
- **Temporal Out-of-Sample Holdouts:** Splitting the sample at 2018 yields OOS $t = -2.54^{**}$; splitting at 2020 yields OOS $t = -1.96^{**}$. Both OOS statistics exceed in-sample estimates, arguing against data snooping.
- **Placebo Knowledge Graph Experiment:** Randomly reshuffling graph edges 100 times while preserving node identities yields an empirical $p$-value of $0.000$, confirming that the economic content of supply chain links drives the signal.
- **Subsample Eras:** Strongest in the low interest rate era (2017–2021, $t = -2.49^{**}$) and post-COVID era (2020–2025, $t = -1.96^{**}$).
- **Firm Size Heterogeneity:** Predictability concentrates in mid-cap S&P 500 quintiles Q2–Q3 ($t = -2.29^{**}$ and $-2.17^{**}$), where investor inattention is more pronounced than in mega-caps.
- **Sector Neutrality:** Survives within-GICS sector quintile sorting.
- **Propagation Weight Sensitivity:** Factor predictability increases monotonically in propagation weight $\alpha$ over the range $[0.4, 1.0]$.
- **Cost Resilience:** Net Sharpe ratio remains positive across transaction costs from 10 to 30 bps round-trip.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Complete Subsumption of Direct Text Embeddings:** Standalone FinBERT embeddings (`pc_5`) exhibit zero independent alpha ($t = 0.31$) once controls are included in Model 3. An investor relying solely on direct LLM text embeddings without graph propagation captures no statistically distinguishable premium.
2. **Short-Side Asymmetry:** The strategy's excess returns are concentrated in the short leg (shorting overpriced stocks in D1/D2 returning 20–21%). When borrow fees, rebate rates, short locates, or institutional recall risks are accounted for, net profitability will be lower than the frictionless estimate.
3. **Passive Benchmark Underperformance:** The long-short quintile strategy delivered an annualized return of 10.9% (Sharpe 0.86) compared to the long-only S&P 500 benchmark of 14.6% (Sharpe 1.03) over the same 2011–2025 period.
4. **Restricted Knowledge Graph Scope:** The baseline KG contains only 48 nodes and 51 directed edges, leaving the majority of the 255 S&P 500 firms with $\mathcal{P}(i) = \emptyset$ (i.e. unpropagated).
5. **Absence of Fundamental Accounting Controls:** The empirical tests control only for price-derived characteristics (momentum, reversal, volatility, log price), omitting book-to-market, operating profitability, and investment factors in the cross-sectional regressions.
6. **Negative Evidence in Literature:** None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-Universe Transfer Test:** Apply the NALE pipeline to non-S&P 500 universes (e.g. Russell 2000 small-caps or STOXX Europe 600) using independently mapped supply chain data. If the Fama–MacBeth Newey–West $t$-statistic on `net_pc_5` fails to achieve $|t| \ge 1.96$, reject universe universality.
2. **Dynamic / Time-Varying KG Test:** Replace the static 48-node KG with a point-in-time dynamic supply chain feed (e.g. FactSet Supply Chain or Bloomberg SPLC) that updates supplier-customer relationships annually. If dynamic edge updating degrades factor predictability below $|t| < 1.96$, the static graph may have suffered from survivorship or look-ahead selection.
3. **Full Fundamental Factor Spanning Test:** Re-estimate Fama–MacBeth Model 3 including Compustat balance sheet controls: book-to-market ($B/M$), operating profitability ($OP$), and investment ($Inv$). If $\text{net\_pc\_5}$ loses significance ($|t| < 1.96$), reject orthogonality to fundamental risk factors.
4. **Institutional Borrow & Implementation Cost Stress:** Evaluate the strategy under realistic, borrow-rate-adjusted short execution costs (e.g. 50–150 bps annualized borrow fee for hard-to-borrow names in D1/D2). If the net Sharpe ratio falls below 0.20, reject investable viability.
5. **Placebo Text Test:** Replace FinBERT 10-K embeddings with random Gaussian vectors propagated through the same KG. If random vectors achieve comparable $t$-statistics under PCA, reject the textual information hypothesis.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source investigates US equity spot shares traded on regulated exchanges using SEC EDGAR 10-K annual filings and corporate supply chain links. It provides zero empirical testing on cryptocurrency assets. Any application to digital assets is a research adaptation rather than demonstrated empirical evidence.
- **Structural Portability Obstacles:**
  1. *Absence of Statutory Disclosures:* Cryptocurrencies lack mandatory, standardized annual 10-K MD&A filings subject to regulatory liability. Potential textual proxies include governance proposals (Snapshot, Discourse forums), GitHub developer commit messages, security audit reports, or protocol whitepapers, but these sources lack standardized reporting schedules and audited accountability.
  2. *Alternative Network Topology:* In crypto, "supply chains" correspond to smart contract composability, shared oracle dependencies (e.g. Chainlink feeds), liquid restaking token (LRT) backing hierarchies, cross-chain bridge dependencies, or collateral-debt relationships in DeFi protocols (e.g. MakerDAO/Sky, Aave).
  3. *Temporal Mismatch & Latency:* 10-K disclosures occur annually and are evaluated monthly. Crypto market dislocations propagate across DeFi dependencies in seconds to minutes, rendering monthly rebalancing ineffective.
  4. *Perpetual Funding Rate Drag:* In crypto perpetual futures, short positions in altcoins often pay significant positive funding rates during bull markets, which could erode the 7.27% annual alpha.
  5. *Tokenomics & Dilution:* Token inflation, scheduled vesting unlocks, and emissions differ fundamentally from corporate equity shares, confounding text-based factor signals.

## Limitations

- **Underspecified Dynamic Graph:** The knowledge graph is static (constructed over 48 firms and 51 edges) and does not reflect time-varying restructuring of supply chains.
- **Unpropagated Majority:** For firms without predecessors in the 48-node KG, $\tilde{\mathbf{e}}_i = \mathbf{e}_i$, reducing the effective sample of augmented firms.
- **Look-Ahead Bias in Graph Selection:** Public curation of the 48-node KG over the full sample period could introduce mild retrospective selection bias in edge definitions.
- **Short-Side Dependency:** The decile spread is driven by shorting the bottom two deciles, making net profitability sensitive to shorting constraints.
- **Pre-Training Boundary Assumptions:** While FinBERT was pre-trained on 2008–2010 news, later model updates or tokenizer nuances could introduce subtle temporal leakage.
- **Not Independently Reproduced:** All performance and statistical figures reflect source-reported metrics and have not been validated on internal backtesting engines.

## Implementation status

- `not-implemented`.
- No prototype or production implementation exists in our PyBroker or NautilusTrader infrastructure.
- No historical backtest has been performed on internal market data.
- Not authorized for paper trading, testnet, or live deployment.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This research record is captured solely as normalized research intelligence. Presence in this repository does **not** constitute approval for implementation, capital allocation, or trading on paper, testnet, or live venues. Any future adoption must undergo independent code reproduction, full out-of-sample testing with borrow costs, and separate formal review.

## Related Wiki records

- `[[quant/alphacrafter-harness-driven-multi-agent-llm-alpha-discovery-2026-09-03]]` — Multi-agent LLM framework for cross-sectional factor generation.
- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Market-aligned reinforcement learning for equity sentiment alpha.
- `[[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]]` — LLM-agentic factor discovery with multi-gate validation.
- `[[quant/equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02]]` — Cross-sectional factor ranking via topological persistent homology.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Standards for leakage prevention, purging, and cross-validation integrity.

## Sources

1. **Primary Research Paper:**
   Asef Yılkı. *"Supply Chain Propagation of Textual Signals: LLM Embeddings and Cross-Sectional Return Predictability."* arXiv preprint `arXiv:2606.29290v1 [q-fin.PR, q-fin.ST]`, submitted June 2026.
   - DOI: [10.48550/arXiv.2606.29290](https://doi.org/10.48550/arXiv.2606.29290)
   - Abstract URL: [https://arxiv.org/abs/2606.29290](https://arxiv.org/abs/2606.29290)
   - PDF URL: [https://arxiv.org/pdf/2606.29290](https://arxiv.org/pdf/2606.29290)
2. **Foundational Economic & Textual References Cited:**
   - Araci, D. (2019). "FinBERT: Financial sentiment analysis with pre-trained language models." *arXiv preprint arXiv:1908.10063*.
   - Barrot, J.-N., & Sauvagnat, J. (2016). "Input specificity and the propagation of idiosyncratic shocks in production networks." *Quarterly Journal of Economics*, 131(3), 1543–1592.
   - Chen, Y., Kelly, B. T., & Xiu, D. (2025). "Expected returns and large language models." *Review of Financial Studies*, 38, 3542–3579.
   - Cohen, L., & Frazzini, A. (2008). "Economic links and predictable returns." *Journal of Finance*, 63(4), 1977–2011.
   - Cohen, L., Malloy, C., & Nguyen, Q. (2020). "Lazy prices." *Journal of Finance*, 75(3), 1371–1408.
   - Fama, E. F., & French, K. R. (2015). "A five-factor asset pricing model." *Journal of Financial Economics*, 116(1), 1–22.
   - Fama, E. F., & MacBeth, J. D. (1973). "Risk, return, and equilibrium: Empirical tests." *Journal of Political Economy*, 81(3), 607–636.
   - Stambaugh, R. F., Yu, J., & Yuan, Y. (2015). "Arbitrage asymmetry and the idiosyncratic volatility puzzle." *Journal of Finance*, 70(5), 1903–1948.
