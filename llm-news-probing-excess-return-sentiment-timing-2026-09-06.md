---
schema: strategy-research-record-v1
title: "LLM News Sentiment Probing for Return Direction: Market-Adjusted Excess Return Supervision, Intraday Release Synchronization, and Large-Scale Transformer Quintile Portfolios (Kirtac & Germano 2024)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - large-language-models
  - financial-news-sentiment
  - opt-2.7b
  - bert
  - finbert
  - excess-return-probing
  - intraday-execution-timing
  - value-weighted-portfolios
  - long-short-equity
status: research-only
confidence: medium
source_as_of: 2024-04-01
sources:
  - "Kemal Kirtac and Guido Germano. 'Sentiment trading with large language models'. Finance Research Letters, Volume 62, April 2024, Article 105227. DOI: 10.1016/j.frl.2024.105227. arXiv preprint: arXiv:2412.19245v1 [q-fin.PM, q-fin.ST], submitted December 26, 2024. URL: https://arxiv.org/abs/2412.19245."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM News Sentiment Probing for Return Direction: Market-Adjusted Excess Return Supervision, Intraday Release Synchronization, and Large-Scale Transformer Quintile Portfolios

## Provenance

- **Primary Source Authors:** Kemal Kirtac and Guido Germano (Financial Computing and Analytics Group, Department of Computer Science, University College London, London, UK).
- **Paper Title:** *"Sentiment trading with large language models"*
- **Journal Publication:** *Finance Research Letters*, Volume 62, April 2024, Article 105227.
- **Canonical DOI:** [10.1016/j.frl.2024.105227](https://doi.org/10.1016/j.frl.2024.105227)
- **arXiv Preprint:** arXiv preprint `arXiv:2412.19245v1 [q-fin.PM, q-fin.ST]`, submitted December 26, 2024.
- **Stable URL:** [https://arxiv.org/abs/2412.19245](https://arxiv.org/abs/2412.19245)
- **Primary Source Inspection:** The complete text of `arXiv:2412.19245v1` was directly retrieved and audited via `pypdf` extraction, verifying all mathematical equations (Eq. 1), sample filtering statistics (Table 1), return and score distributions (Table 2), sentiment classification metrics (Table 3), panel regression specifications (Table 4), portfolio backtest performance metrics (Table 5), and cumulative return curves (Figure 1).
- **Repository Deduplication Audit:** A full-text search across `alpha-strategy-research` confirmed zero pre-existing records referencing `arXiv:2412.19245`, DOI `10.1016/j.frl.2024.105227`, or authors Kemal Kirtac and Guido Germano. Adjacent records in the repository evaluate zero-shot LLM prompts for cross-sectional momentum tilting (`llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md`), event-aware contrarian sentiment (`llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md`), semantic networks for cross-stock reversal (`llm-augmented-semantic-network-cross-stock-reversal-2026-09-04.md`), or VADER-based sentiment for crypto mean-variance allocation (`sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04.md`). None investigate supervised probing of causal open pre-trained transformers (OPT-2.7B) vs. bidirectional encoders (BERT-345M, FinBERT) trained directly on 3-day market-adjusted excess return direction with session-aligned intraday execution timestamps.

## Economic mechanism

### Source-reported

Conventional textual analysis in quantitative finance relies heavily on static domain-specific lexicons (such as the Loughran-McDonald master dictionary) or simple bag-of-words term frequencies. These traditional methods oversimplify text by ignoring word order, syntactic context, negation, and complex financial nuance, leading to severe information loss and statistical inefficiencies. Furthermore, existing sentiment indicators often operate at the aggregate macroeconomic or market level, failing to capture firm-specific news sentiment dynamics at the individual stock level.

Kirtac and Germano argue that modern Large Language Models (LLMs)—specifically autoregressive causal transformers such as Meta's Open Pre-trained Transformers (OPT-2.7B) and bidirectional transformers like Google's BERT (345M parameters)—possess expansive parameter spaces and deep contextual linguistic representations that can extract subtle economic signals from unstructured corporate news.

Instead of relying on human sentiment annotations (which can be subjective or disconnected from market pricing), the authors implement a probing feature-extraction methodology adapted from Alain & Bengio (2016) and Ke, Kelly, & Xiu (2020). The LLMs are fine-tuned to classify whether a news article is followed by positive or non-positive 3-day market-adjusted cumulative excess returns. The resulting continuous model scores reflect the likelihood of immediate post-announcement price outperformance. The authors hypothesize that large-scale autoregressive models (OPT-2.7B) outperform smaller bidirectional models (BERT-345M) and specialized domain models (FinBERT) because their broader training corpora and higher capacity prevent overfitting to narrow vocabulary, enabling superior generalization to firm-level price reactions.

### Research interpretation

The economic edge reported in this study can be analyzed through three complementary mechanisms:
1. **Gradual Information Diffusion and Post-Earnings/News Drift:** Markets do not instantaneously incorporate the full qualitative implications of corporate news. Complex announcements (earnings releases, product launches, litigation, regulatory investigations) require cognitive processing. A high-capacity language model acts as an automated analyst, identifying subtle tone, guidance nuances, or risk disclosures faster than retail market participants, capturing the multi-day drift as prices adjust toward fundamental value.
2. **Supervised Return-Direction Alignment vs. Lexical Scoring:** Lexicon models count predefined words (e.g., 'loss', 'uncertainty') that may carry entirely different meanings depending on whether they appear in boilerplate legal disclaimers or operational forecasts. Probing an LLM directly on post-news cumulative excess return aligns the representation with actual price formation rather than human grammatical convention.
3. **Capacity-Overfitting Duality in Financial Text:** The study observes that OPT-2.7B outperforms FinBERT (a model pre-trained exclusively on financial domain text). Our research interpretation is that specialized small models (FinBERT with 110M parameters) overfit the stylized syntax of financial phrasebooks (such as Financial PhraseBank), whereas large generative foundation models (OPT-2.7B) possess broader world knowledge, cross-entity contextual awareness, and nuanced semantic disambiguation that generalize better across diverse corporate news topics.
4. **Critical Methodological Vulnerability (Temporal Leakage):** Crucially, the authors' fine-tuning protocol randomly allocated 20% of articles for testing and 20% for validation across the entire 2010–2023 sample (`source-reported`). Because articles were partitioned randomly rather than strictly chronologically (expanding-window walk-forward), the model may have learned from news published in future periods to predict test articles from earlier or concurrent dates. This design creates a substantial risk of lookahead bias and temporal leakage that must be subjected to strict out-of-sample falsification.

## Signal

### 1. Mathematical Formulation & News Filtering (`source-reported`)

Let $\mathcal{D}_{\text{raw}}$ be the universe of U.S. financial news headlines and articles from Refinitiv.
The raw dataset contains $N_{\text{all}} = 2,732,845$ news items across $N_{\text{firm}} = 6,214$ unique companies (`source-reported`).
Two filtering stages are applied:
1. **Single-Stock Association Filter:** Exclude multi-stock or macro articles; retain only articles exclusively associated with an individual U.S. common stock ($N_{\text{single}} = 1,865,372$) (`source-reported`).
2. **Novelty / Deduplication Filter:** Exclude articles that have a cosine similarity score $S_{\text{cos}} \ge 0.80$ with any older article published within the prior 5 business days (`source-reported`, Table 1; note text states 20 days, see Provenance Gap). The remaining filtered universe contains $N_{\text{unique}} = 965,375$ unique articles (`source-reported`).

### 2. Excess Return Labeling & Probing Architecture (`source-reported`)

For each unique article published for firm $i$ on date $t$, the 3-day market-adjusted cumulative excess return is calculated:
$$r^{\text{excess}}_{i, [t, t+2]} = \sum_{k=0}^{2} \left( r_{i, t+k} - r_{m, t+k} \right)$$
where:
- $r_{i, t+k}$ is the daily return of stock $i$ from CRSP on trading day $t+k$ (`source-reported`).
- $r_{m, t+k}$ is the overall U.S. market return (CRSP value-weighted index) on day $t+k$ (`source-reported`).
- The binary sentiment label $y_{i, t} \in \{0, 1\}$ is defined by:
  $$y_{i, t} = \begin{cases} 1 & \text{if } r^{\text{excess}}_{i, [t, t+2]} > 0 \\ 0 & \text{if } r^{\text{excess}}_{i, [t, t+2]} \le 0 \end{cases}$$
  (`source-reported`).

The probing network maps the text sequence $\mathbf{w}_{i, t}$ into a continuous prediction score $x_{i, t} \in [0, 1]$ representing the predicted probability of positive 3-day excess return:
$$x_{i, t} = \sigma\left( \mathbf{W}_{\text{probe}}^\top \mathbf{h}_{\text{LLM}}(\mathbf{w}_{i, t}) + b_{\text{probe}} \right)$$
where $\mathbf{h}_{\text{LLM}}$ is the contextual embedding extracted from the pre-trained transformer model (OPT-2.7B or BERT-345M), $\mathbf{W}_{\text{probe}}$ and $b_{\text{probe}}$ are the linear probing parameters fine-tuned under cross-entropy loss, and $\sigma$ is the sigmoid activation function (`source-reported`).

### 3. Panel Return Forecasting Regression (`source-reported`)

To evaluate predictive validity on daily stock returns on the subsequent day $n+1$, the authors estimate a two-way fixed effects panel regression:
$$r_{i, n+1} = a_i + b_n + \beta x_{i, n} + \epsilon_{i, n+1}$$
where:
- $r_{i, n+1}$ is the percentage return of stock $i$ on trading day $n+1$ (`source-reported`).
- $x_{i, n}$ is the vector of LLM prediction scores for firm $i$ on day $n$ (`source-reported`).
- $a_i$ denotes firm fixed effects (`source-reported`).
- $b_n$ denotes date fixed effects (`source-reported`).
- Standard errors are two-way clustered by firm and date (`source-reported`).

### 4. Portfolio Formation and Trading Triggers (`source-reported`)

Portfolios are updated daily based on the cross-sectional distribution of sentiment scores:
- **Long Portfolio ($Q_5$):** Stocks in the top 20th percentile (highest quintile) of positive sentiment scores on day $n$ (`source-reported`).
- **Short Portfolio ($Q_1$):** Stocks in the bottom 20th percentile (lowest quintile) of sentiment scores on day $n$ (`source-reported`).
- **Long-Short (L-S) Portfolio:** A self-financing zero-net-investment portfolio that simultaneously takes long positions in $Q_5$ and short positions in $Q_1$ (`source-reported`).
- **Weighting Scheme:** Value-weighted based on market capitalization of each constituent stock (`source-reported`). An equal-weighted portfolio is provided as an alternative baseline (`source-reported`).

### 5. Intraday Execution Synchronization Rules (`source-reported`)

Trading execution is strictly synchronized with the news publication timestamp:
1. **Pre-Market Releases ($\text{Timestamp} < \text{06:00 AM EST}$):**
   - *Entry Trigger:* Market open on trade date $t$ (`source-reported`).
   - *Exit Trigger:* Market close on the same trade date $t$ (`source-reported`).
   - *Holding Period:* Intraday (1 trading session) (`source-reported`).
2. **Regular Trading Hours Releases ($\text{06:00 AM EST} \le \text{Timestamp} \le \text{04:00 PM EST}$):**
   - *Entry Trigger:* Market close on trade date $t$ (`source-reported`).
   - *Exit Trigger:* Market close on the subsequent trading date $t+1$ (`source-reported`).
   - *Holding Period:* Overnight + 1 full trading session (`source-reported`).
3. **After-Hours Releases ($\text{Timestamp} > \text{04:00 PM EST}$):**
   - *Entry Trigger:* Market open on the subsequent trading date $t+1$ (`source-reported`).
   - *Exit Trigger:* Market close on trading date $t+1$ (`source-reported`).
   - *Holding Period:* Intraday on day $t+1$ (`source-reported`).

## Required data

- **Universe:** All U.S. common stocks listed on the American Stock Exchange (AMEX), NASDAQ, and New York Stock Exchange (NYSE) with at least one news article in Refinitiv ($N = 6,214$ companies) (`source-reported`).
- **Equity Price & Volume Data:** CRSP daily stock returns, closing prices, opening prices, trading volume, and market capitalization (`source-reported`).
- **News Text Data:** Refinitiv Global News database, covering both full-text articles and quick news alerts (`source-reported`).
- **Sample Period:** January 1, 2010 to June 30, 2023 (13.5 years; $N = 965,375$ unique observations) (`source-reported`).
- **Market Benchmark:** CRSP value-weighted market return index (`source-reported`).
- **Model Checkpoints:** Hugging Face model hub pre-trained checkpoints for OPT-2.7B (`facebook/opt-2.7b`), BERT-Large (`bert-large-uncased`, 345M parameters), FinBERT (`ProsusAI/finbert`), and the Loughran-McDonald master dictionary (`source-reported`).
- **Timestamp Precision:** High-resolution news publication timestamps (hour, minute, second in Eastern Time) to bin articles into pre-market ($<06:00$), regular hours ($06:00\text{--}16:00$), and post-market ($>16:00$) execution buckets (`source-reported`).

## Execution assumptions

- **Transaction Costs:** 10 basis points (0.10% or $c = 0.0010$) per trade imposed on every transaction (`source-reported`).
- **Execution Fill Prices:**
  - Market open trades are filled at CRSP opening prices (`source-reported`).
  - Market close trades are filled at CRSP closing prices (`source-reported`).
- **Slippage & Market Impact:** No additional market impact model beyond the fixed 10 bps transaction cost fee (`source-reported`). The authors justify value-weighting towards larger-cap equities as a practical mechanism to mitigate market impact (`source-reported`).
- **Short Selling:** Assumes unrestricted shorting liquidity and zero borrow cost on the bottom quintile ($Q_1$) constituents (`source-reported`).
- **Leverage & Financing:** The L-S portfolio is structured as a self-financing long-short strategy with gross exposure 200% (100% long, 100% short) and net exposure 0% (`research interpretation`). Risk-free financing rate on cash collateral is omitted (`provenance gap`).

## Evidence

### Source-reported

#### 1. Descriptive Statistics of Daily Returns and Sentiment Scores (Table 2)
Over the 965,375 news events:
- **Daily Stock Return (%):** Mean = 0.37%, StdDev = 0.18%, Min = -64.97%, Median = -0.02%, Max = 237.11% (`source-reported`).
- **OPT Score:** Mean = 0.53, StdDev = 0.24, Min = 0.00, Median = 0.50, Max = 1.00 (`source-reported`).
- **BERT Score:** Mean = 0.48, StdDev = 0.25, Min = 0.00, Median = 0.50, Max = 1.00 (`source-reported`).
- **FinBERT Score:** Mean = 0.51, StdDev = 0.24, Min = 0.00, Median = 0.50, Max = 1.00 (`source-reported`).
- **Loughran-McDonald (LM) Score:** Mean = 0.68, StdDev = 0.32, Min = 0.00, Median = 0.50, Max = 1.00 (`source-reported`).

#### 2. Sentiment Classification Accuracy on Out-of-Sample Test Set (Table 3)
Evaluated on a 20% test partition (approx. 193,075 articles) for predicting 3-day market-adjusted excess return direction:
| Metric | OPT (2.7B) | BERT (345M) | FinBERT (110M) | Loughran-McDonald |
| :--- | :---: | :---: | :---: | :---: |
| **Accuracy** | **0.744** | 0.725 | 0.722 | 0.501 |
| **Precision** | **0.732** | 0.711 | 0.708 | 0.505 |
| **Recall** | **0.781** | 0.761 | 0.755 | 0.513 |
| **Specificity** | **0.711** | 0.693 | 0.685 | 0.522 |
| **F1 Score** | **0.754** | 0.734 | 0.731 | 0.508 |

The Loughran-McDonald dictionary achieves an accuracy of only 50.1%, barely distinguishable from a random coin toss.

#### 3. Panel Regression of Next-Day Stock Returns on Sentiment Scores (Table 4)
Model: $r_{i, n+1} = a_i + b_n + \beta x_{i, n} + \epsilon_{i, n+1}$ with firm and date fixed effects, $N = 965,375$ observations:
| Variable | Reg 1 (Joint) | Reg 2 (Joint) | Reg 3 (OPT) | Reg 4 (BERT) | Reg 5 (FinBERT) | Reg 6 (LM) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **OPT Score** | **0.274\*\*\*** (5.367) | — | **0.254\*\*\*** (4.871) | — | — | — |
| **BERT Score** | **0.142\*\*** (2.632) | 0.091\* (1.971) | — | **0.129\*** (2.334) | — | — |
| **FinBERT Score** | — | **0.257\*\*\*** (5.121) | — | — | **0.181\*\*\*** (4.674) | — |
| **LM Dictionary** | — | — | — | — | — | 0.083 (1.871) |
| **$R^2$** | 0.221 | 0.217 | 0.195 | 0.145 | 0.174 | 0.087 |
| **$R^2_{\text{adj}}$** | 0.183 | 0.184 | 0.195 | 0.145 | 0.174 | 0.087 |
| **$R^2_{\text{within}}$** | 0.021 | 0.022 | 0.017 | 0.009 | 0.016 | 0.002 |
| **AIC** | 64,378 | 77,884 | 62,345 | 97,473 | 67,345 | 135,783 |
| **BIC** | 117,231 | 132,212 | 115,655 | 114,746 | 109,272 | 123,382 |
| **RMSE** | 5.32 | 11.12 | 4.21 | 14.12 | 9.75 | 23.54 |

OPT exhibits the largest predictive coefficient ($\beta = 0.254$, $t = 4.871$), whereas the Loughran-McDonald score is statistically insignificant at the 5% level ($t = 1.871$).

#### 4. Portfolio Performance Statistics Across Models (Table 5)
Value-weighted portfolios rebalanced daily:
| Model / Strategy | Portfolio Type | Sharpe Ratio | Mean Daily Return (MDR) | Daily StdDev | Max Daily Drawdown (MDD) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **OPT** | Long ($Q_5$) | 1.81 | 0.32% | 2.18% | -14.76% |
| | Short ($Q_1$) | 1.42 | 0.25% | 2.91% | -24.69% |
| | **Long-Short (L-S)** | **3.05** | **0.55%** | **2.49%** | **-18.57%** |
| **BERT** | Long ($Q_5$) | 1.59 | 0.25% | 2.49% | -17.89% |
| | Short ($Q_1$) | 1.28 | 0.21% | 3.19% | -27.95% |
| | **Long-Short (L-S)** | **2.11** | **0.45%** | **2.68%** | **-21.95%** |
| **FinBERT** | Long ($Q_5$) | 1.51 | 0.22% | 2.59% | -19.71% |
| | Short ($Q_1$) | 1.19 | 0.18% | 3.31% | -29.94% |
| | **Long-Short (L-S)** | **2.07** | **0.39%** | **2.81%** | **-23.82%** |
| **LM Dictionary** | Long ($Q_5$) | 0.87 | 0.12% | 3.54% | -35.47% |
| | Short ($Q_1$) | 0.66 | 0.13% | 4.13% | -45.39% |
| | **Long-Short (L-S)** | **1.23** | **0.22%** | **3.74%** | **-38.29%** |
| **Equal-Weighted (EW)** | Long ($Q_5$) | 1.25 | 0.18% | 2.90% | -31.13% |
| | Short ($Q_1$) | 1.05 | 0.15% | 3.70% | -42.21% |
| | **Long-Short (L-S)** | **1.40** | **0.33%** | **3.20%** | **-32.87%** |
| **Value-Weighted (VW)** | Long ($Q_5$) | 1.28 | 0.19% | 2.95% | -28.76% |
| | Short ($Q_1$) | 1.08 | 0.16% | 3.75% | -38.95% |
| | **Long-Short (L-S)** | **1.45** | **0.35%** | **3.25%** | **-31.87%** |

#### 5. Cumulative Backtest Outperformance with 10 bps Costs (Figure 1)
In an out-of-sample backtest spanning August 2021 to July 2023 incorporating 10 bps transaction costs per trade:
- **OPT L-S:** Cumulative return = **+355%** (`source-reported`).
- **BERT L-S:** Cumulative return = **+235%** (`source-reported`).
- **FinBERT L-S:** Cumulative return = **+165%** (`source-reported`).
- **Value-Weighted Market Portfolio:** Cumulative return = **~1%** (`source-reported`).
- **Loughran-McDonald Dictionary L-S:** Cumulative return = **+0.91%** (`source-reported`).

### Independently reproduced

`Not independently reproduced.` Findings are transcribed directly from Kirtac & Germano (*Finance Research Letters* 62, 105227, 2024 / arXiv:2412.19245v1).

### Negative evidence

1. **Failure of Traditional Lexical Methods:** The widely cited Loughran-McDonald financial sentiment dictionary delivers an accuracy of only 50.1% on the test set (statistically equivalent to random guessing), has an insignificant regression t-statistic ($t = 1.871, p > 0.05$), and produces a cumulative return of only 0.91% after transaction costs over August 2021–July 2023, failing to beat the passive benchmark.
2. **Domain-Specific Overfitting in FinBERT:** Despite being explicitly pre-trained on financial texts (Financial PhraseBank), FinBERT underperforms both OPT-2.7B (Sharpe 2.07 vs 3.05) and general-domain BERT (Sharpe 2.07 vs 2.11), suggesting that narrow domain pre-training on small financial corpora induces representation rigidity that harms generalized market return forecasting.
3. **Execution Drag on Short Leg:** Across all models, the short quintile portfolio ($Q_1$) displays significantly worse risk-adjusted metrics than the long quintile ($Q_5$) (e.g., OPT Short Sharpe 1.42 vs Long 1.81; MDD -24.69% vs -14.76%), demonstrating substantial asymmetric downside risk during market rallies.
4. **Lack of Walk-Forward Purging:** The primary source does not implement combinatorial purged cross-validation (CPCV) or strict chronological expanding-window splits during probing fine-tuning. A non-temporal random split across a 13.5-year panel inherently leaks macroeconomic regime and future entity information into model weights.

## Falsification plan

To falsify the claim that OPT-2.7B sentiment probing generates genuine, actionable alpha:

1. **Strict Expanding-Window Chronological Walk-Forward Audit (`research-proposed`):**
   - *Protocol:* Replace the author's random 60/20/20 train/val/test split with an expanding-window walk-forward schedule: train on years $2010\text{--}t-1$, calibrate validation threshold on year $t$, and execute strictly out-of-sample on year $t+1$ (rolling from 2015 through 2023).
   - *Decision Rule (`research-defined falsification threshold`):* If the annualized out-of-sample Sharpe ratio drops below 1.0 or decays by more than 50% relative to Table 5's reported 3.05, the reported alpha is falsified as an artifact of temporal lookahead leakage during probing.
2. **Publication-to-Execution Delay Stress Test (`research-proposed`):**
   - *Protocol:* Introduce an execution lag of $\Delta t \in \{5, 15, 30, 60\}$ minutes following news release timestamps, simulating latency in web-scraping, tokenization, model inference, and order routing.
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized alpha becomes negative at a 15-minute execution delay, the edge is purely high-frequency latency arbitrage rather than durable multi-day sentiment drift.
3. **Borrow Fee and Shorting Availability Gauntlet (`research-proposed`):**
   - *Protocol:* Apply realistic institutional stock borrow fees (using Markit/S3 borrow cost distributions) and hard-to-borrow constraints on small/mid-cap constituents in the bottom quintile ($Q_1$).
   - *Decision Rule (`research-defined falsification threshold`):* If deducting actual borrow rates reduces the L-S Sharpe ratio below the long-only $Q_5$ Sharpe ratio (1.81), the short leg is non-viable in production.
4. **Transaction Cost and Bid-Ask Spread Sensitivity (`research-proposed`):**
   - *Protocol:* Sweep one-way transaction costs from 10 bps to 25 bps, accounting for widening spreads around breaking news announcements.
   - *Decision Rule (`research-defined falsification threshold`):* If the net Sharpe ratio falls below 0.50 at 20 bps round-trip cost, the strategy lacks sufficient margin of safety for automated deployment.

## Crypto portability

- **Portability Classification:** `adapted` and `unproven`.
- **Primary Source Demonstration:** The primary source investigates only U.S. common stocks listed on AMEX, NASDAQ, and NYSE from CRSP and Refinitiv. The mechanism has not been demonstrated in crypto markets (`research interpretation`).
- **Cryptocurrency Structural Dynamics:**
  - *Continuous 24/7 Market Structure:* U.S. equity markets feature distinct opening (09:30 EST) and closing (16:00 EST) auctions with overnight trading pauses that form the basis of the author's pre-6am / 6am-4pm / post-4pm execution schedule. In 24/7 crypto markets, there are no market opens or closes; execution rules must be adapted to continuous rolling rebalancing (e.g., immediate execution upon news publication with a fixed 24-hour or 48-hour holding window) (`research-proposed`).
  - *News Source Divergence:* Corporate equity news is concentrated in formal news wires (Refinitiv, Bloomberg, PR Newswire, SEC filings). Crypto price-sensitive information is highly fragmented across decentralized channels: X (formerly Twitter), Telegram, Discord, governance forums, on-chain transaction alerts, and specialized aggregators (CoinDesk, Cointelegraph). Fine-tuning OPT on Refinitiv articles cannot transfer directly to noisy, short-form crypto social media.
  - *Perpetual Futures Funding Rate Asymmetry:* Taking short positions on momentum-driven altcoins in crypto perpetuals exposes the strategy to aggressive funding rate shocks. If positive news triggers a massive short squeeze, holding short positions will incur catastrophic funding payments (often exceeding 50–100% annualized), magnifying drawdown risk beyond equity shorting.
  - *Liquidity Fragmentation and Spread Widening:* While the paper relies on value-weighting to ensure liquidity among U.S. equities, crypto altcoins exhibit severe cross-exchange liquidity fragmentation. Breaking news frequently causes immediate order book evaporation, resulting in effective round-trip slippage of 30–80 bps on decentralized and centralized venues, which would completely consume the reported 10 bps margin.

## Limitations

- **Random Split Lookahead Leakage (`methodology gap`):** The primary source used a random 60/20/20 train/validation/test split across 2010–2023. Training the LLM probe on news from 2022 to predict 2015 news (or vice versa) allows the model to learn forward-looking macroeconomic and firm-specific price regimes, artificially inflating classification accuracy and Sharpe ratios.
- **Discrepancy in Filtering Window (`provenance gap`):** In Section 2.1 (p. 3), the text states that redundant news articles were filtered if cosine similarity exceeded 0.80 within the 'past 20 days'. However, in Table 1's caption (p. 3), the authors state that articles were excluded if similarity exceeded 0.80 within the 'prior five business days'. This internal conflict in lookback window is an unaddressed inconsistency in the primary source.
- **Arithmetic Training Sample Discrepancy (`provenance gap`):** Section 2.2 states: *"We allocated 20% of the data randomly for testing and, from the remaining data pool, allocated another 20% randomly for validation purposes, resulting in a training set of 193,070 articles."* However, 20% of 965,375 is 193,075, which leaves 60% (579,225 articles) for training, not 193,070. The authors appear to have swapped the training and validation/test partition sizes without clarifying the allocation.
- **Zero Borrow Cost Assumption (`execution gap`):** The self-financing L-S strategy assumes shorting the bottom 20% of sentiment stocks incurs zero borrow fees, which is unrealistic for distressed firms experiencing severe negative news coverage.
- **Fixed Transaction Cost Assumption (`execution gap`):** Applying a static 10 bps fee does not capture the severe bid-ask spread widening that occurs immediately after breaking news announcements.
- **Hardware and Inference Latency (`operational limitation`):** Deploying a 2.7-billion parameter LLM for real-time inference on streaming news feeds requires dedicated GPU infrastructure (e.g., NVIDIA A100/H100 clusters) to maintain sub-second response times.

## Implementation status

- **Frontmatter Status:** `not-implemented`.
- **Repository Implementation:** No code has been implemented in PyBroker, NautilusTrader, or any internal execution pipeline.
- **Research Scope:** This document is an upstream academic research capture and methodological critique. It does not modify NautilusTrader, create a production trading strategy, or authorize Paper, Testnet, or Live execution.

## Adoption boundary

- **Adoption Status:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Conditions:**
  - Presence in this repository indicates that the research record has been normalized to the canonical Wiki Brain specification; it does not indicate profitable alpha, validated execution edge, or trading readiness.
  - The high reported Sharpe ratio (3.05) is subject to significant suspicion due to the random train/test split methodology. Any progression to PyBroker exploratory backtesting requires a complete purge of temporal leakage via strict expanding-window walk-forward validation and realistic short borrow fee modeling.

## Related Wiki records

- `[[llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06]]` — Examines zero-shot prompt engineering on GPT-4 / ChatGPT for sentiment tilting of cross-sectional equity momentum.
- `[[llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md]]` — Investigates event-driven LLM sentiment factor discovery with contrarian alpha signals.
- `[[llm-augmented-semantic-network-cross-stock-reversal-2026-09-04]]` — Analyzes semantic knowledge graphs and language models for cross-stock return reversal.
- `[[sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04]]` — Explores rule-based lexicon sentiment combined with technical indicators for cryptocurrency mean-variance portfolios.
- `[[spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06]]` — Analyzes multi-task tensor learning and turnover regularization for cross-asset momentum spillovers.

## Sources

1. **Primary Academic Source:**
   - Kemal Kirtac and Guido Germano. *"Sentiment trading with large language models"*. *Finance Research Letters*, Volume 62, April 2024, Article 105227. ISSN: 1544-6123. DOI: [10.1016/j.frl.2024.105227](https://doi.org/10.1016/j.frl.2024.105227). arXiv preprint: `arXiv:2412.19245v1 [q-fin.PM, q-fin.ST]`, submitted December 26, 2024. Stable URL: [https://arxiv.org/abs/2412.19245](https://arxiv.org/abs/2412.19245). Direct HTML: [https://arxiv.org/html/2412.19245v1](https://arxiv.org/html/2412.19245v1).
2. **Methodological Foundations:**
   - Alain, G., and Bengio, Y. (2016). *"Understanding intermediate layers using linear classifier probes"*. arXiv preprint arXiv:1610.01644.
   - Ke, Z. T., Kelly, B. T., and Xiu, D. (2020). *"Predicting returns with text data"*. NBER Working Paper No. w26186. DOI: 10.3386/w26186.
   - Zhang, S., Roller, S., Goyal, N., Artetxe, M., Moya, C., Chen, S., ... and Zettlemoyer, L. (2022). *"OPT: Open pre-trained transformer language models"*. arXiv preprint arXiv:2205.01068.
   - Devlin, J., Chang, M. W., Lee, K., and Toutanova, K. (2018). *"BERT: Pre-training of deep bidirectional transformers for language understanding"*. arXiv preprint arXiv:1810.04805.
   - Huang, A. H., Wang, H., and Yang, Y. (2023). *"FinBERT: A large language model for extracting information from financial text"*. *Contemporary Accounting Research*, 40(2):806–841.
   - Loughran, T., and McDonald, B. (2011). *"When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks"*. *The Journal of Finance*, 66(1):35–65.
   - Loughran, T., and McDonald, B. (2022). *"Loughran and McDonald master dictionary"*. Available at: https://sraf.nd.edu/textual-analysis/resources/.
