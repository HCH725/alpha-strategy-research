---
schema: strategy-research-record-v1
title: "Hybrid AI-Driven Trading Architecture with XGBoost Return Direction Classifier, FinBERT Sentiment Risk Gating, and Volatility-Regime Adaptation"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - hybrid-strategy
  - xgboost
  - finbert
  - sentiment-analysis
  - regime-switching
  - equity-long-only
  - volatility-targeting
status: research-only
confidence: medium
source_as_of: 2026-01-24
sources:
  - "https://arxiv.org/abs/2601.19504"
  - "https://doi.org/10.48550/arXiv.2601.19504"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hybrid AI-Driven Trading Architecture with XGBoost Return Direction Classifier, FinBERT Sentiment Risk Gating, and Volatility-Regime Adaptation

## Provenance

- **Primary Source:** Varun Narayan Kannan Pillai, Akshay Ajith, and Sumesh K. J. (Department of Computer Science and Engineering, Amrita School of Computing, Amrita Vishwa Vidyapeetham, Amritapuri, India), *"Generating Alpha: A Hybrid AI-Driven Trading System Integrating Technical Analysis, Machine Learning and Financial Sentiment for Regime-Adaptive Equity Strategies"*, arXiv preprint `arXiv:2601.19504v1 [q-fin.CP]`, submitted January 24, 2026. Accepted for publication at the *International Conference on Computing Systems and Intelligent Applications (ComSIA 2026)*.
- **Canonical Stable Abstract URL:** [https://arxiv.org/abs/2601.19504](https://arxiv.org/abs/2601.19504)
- **Full Text HTML URL:** [https://arxiv.org/html/2601.19504v1](https://arxiv.org/html/2601.19504v1)
- **Full Text PDF URL:** [https://arxiv.org/pdf/2601.19504](https://arxiv.org/pdf/2601.19504)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2601.19504](https://doi.org/10.48550/arXiv.2601.19504)
- **Target Instrument / Universe:** Cross-section of 100 large-cap equities from the S&P 500 Index spanning major sectors (e.g., technology: AAPL, MSFT, NVDA; financials: JPM, BAC; energy; healthcare; consumer discretionary).
- **Historical Sample Period:** January 1, 2019 to January 1, 2025 (6 years).
- **Partitioning:** Chronological split:
  - In-sample training partition: 70% of chronological data (January 1, 2019 to December 31, 2022, 4 years).
  - Out-of-sample backtest/evaluation partition: 30% of chronological data (January 1, 2023 to January 1, 2025, 2 years / 24 months).
- **Initial Account Equity:** $100,000 cash.
- **Direct Primary-Source Inspection:** This record was produced through direct examination of the full academic preprint text (`arXiv:2601.19504v1`), including Section III methodology, Algorithm 1 pseudo-code, mathematical specifications for sentiment, regime, and position sizing, and Section IV empirical evaluation tables. No search snippets, secondary aggregators, or model-hallucinated figures were used.

## Economic mechanism

### Source-reported

Financial asset prices are driven by an evolving interplay of fundamental variables, structural technical momentum, and behavioral market psychology:
1. **Failure of Isolated Single-Signal Strategies:** Unconditional trend-following models (e.g., EMA or MACD crossovers) experience chronic whipsaw losses and false breakouts in mean-reverting or sideways environments. Conversely, standalone mean-reversion models (e.g., RSI or Bollinger Bands) suffer catastrophic drawdowns when attempting to fade persistent trending regimes.
2. **Behavioral News Shocks and Information Lag:** Technical indicators are strictly backward-looking transformations of past price/volume and remain blind to real-time structural news shocks (e.g., regulatory investigations, unexpected earnings revisions, management departures). Integrating NLP sentiment analysis through FinBERT acts as a behavioral "risk shield" that detects adverse corporate disclosures before market close, preventing capital commitment during negative news cycles.
3. **Regime-Conditioned Execution:** Market return distributions vary across macroeconomic environments (inflationary rate hikes, recovery rallies, bear drawdowns). Imposing an overarching rolling return trend filter halts long entries during unfavorable macro regimes, preserving capital for positive-drift regimes.
4. **Volatility-Adjusted Capital Allocation:** Fixed-lot or static percentage position sizing exposes portfolios to disproportionate risk during high-volatility regimes. Sizing inversely to the Average True Range (ATR) harmonizes risk contribution across diverse volatility conditions.

### Research interpretation

The hypothesized mechanism is a **multi-layer gated hybrid architecture**:
1. **Separation of Alpha Generation from Risk Defense:** The machine learning classifier (XGBoost) and classical technical indicators (EMA, MACD, RSI) act as predictive alpha filters, identifying directional setups. In contrast, FinBERT headline sentiment and rolling 20-day return regimes do not generate directional trades; they function strictly as asymmetric kill switches (negative sentiment filter and trend gating).
2. **Non-Linear Feature Interaction:** Classical technical indicators assume static linear thresholds. Training a tree-based ensemble (XGBoost) on standardized cross-sectional feature combinations (such as the ratio of short-to-long moving averages and MACD momentum differentials) captures non-linear conditional interactions between trend persistence and oscillator exhaustion.
3. **Volatility Parity in Long-Only Equities:** Bounding maximum risk to 1% of cash divided by ATR, subject to a 10% total capital cap per asset, avoids position-concentration blowups in volatile small/mid-cap growth components while ensuring adequate capital deployment in steady mega-caps.

## Signal

### Mathematical Formulation (Source-reported)

The trading system operates as a daily long-only equity model executed via Algorithm 1:

1. **Sentiment Score Formulation:**
   For ticker $j$ on trading day $t$, all news headlines and summaries published prior to 9:30 AM EST ($N$ articles) are evaluated using FinBERT to obtain class probabilities for positive ($P_{\text{positive}}^{(i)}$) and negative ($P_{\text{negative}}^{(i)}$) sentiment:
   $$S_{j, t} = \frac{1}{N} \sum_{i=1}^{N} \left( P_{\text{positive}}^{(i)} - P_{\text{negative}}^{(i)} \right), \quad S_{j, t} \in [-1, 1]$$
   - `source-reported rule`: $S_{j, t}$ is used strictly as a risk filter/gate. If $S_{j, t} < -0.70$, new long positions are prohibited and any open long position is immediately exited.

2. **Market Regime Detection Formulation:**
   Asset-specific regime $R_{j, t}$ is determined from the 20-day simple moving average of daily returns:
   $$R_{j, t} = \text{SMA}_{20}(\text{pct\_change}(P_{j, t}))$$
   $$\text{Regime}_{j, t} = \begin{cases} \text{Bullish } (+1), & R_{j, t} > 0 \\ \text{Bearish } (-1), & R_{j, t} \le 0 \end{cases}$$
   - `source-reported rule`: Trades are enabled only when $\text{Regime}_{j, t}$ is Bullish.

3. **Machine Learning Return Classifier:**
   - **Target Variable:** Binary next-day price direction:
     $$y_{j, t} = \begin{cases} 1, & \frac{P_{j, t+1}}{P_{j, t}} - 1 > 0 \\ 0, & \frac{P_{j, t+1}}{P_{j, t}} - 1 \le 0 \end{cases}$$
   - **Model:** XGBoost Classifier with hyperparameters: `n_estimators=200`, `max_depth=6`, `learning_rate=0.05`.
   - **Feature Preprocessing:** All features are standardized via `StandardScaler` fitted on the training split.
   - **Prediction:** Binary classification output $\hat{y}_{j, t} \in \{0, 1\}$.
   - **Feature Inputs (10 features):**
     1. $\text{EMA}_{50}$ (50-day exponential moving average)
     2. $\text{EMA}_{200}$ (200-day exponential moving average)
     3. $\text{Ratio}_{\text{EMA}} = \text{EMA}_{50} / \text{EMA}_{200}$
     4. $\text{MACD}$ line
     5. $\text{MACD Signal}$ line
     6. $\text{MACD Histogram} = \text{MACD} - \text{Signal}$
     7. $\text{RSI}_{14}$ (14-day Relative Strength Index)
     8. Bollinger Band Width
     9. $\text{ATR}_{14}$ (14-day Average True Range)
     10. Rolling return standard deviation (volatility)

4. **Composite Hybrid Score Computation:**
   For candidate stock $j$ at date $t$, the composite integer score is initialized to the ML prediction and incremented by technical momentum/mean-reversion conditions:
   $$\text{score}_{j, t} = \hat{y}_{j, t}$$
   $$\text{if } P_{j, t} > \text{EMA}_{50, j, t} \text{ and } \text{MACD}_{j, t} > \text{Signal}_{j, t}, \quad \text{score}_{j, t} \leftarrow \text{score}_{j, t} + 1$$
   $$\text{if } \text{RSI}_{14, j, t} < 30, \quad \text{score}_{j, t} \leftarrow \text{score}_{j, t} + 1$$
   The theoretical integer range is $\text{score}_{j, t} \in \{0, 1, 2, 3\}$.

5. **Entry Trigger (Source-reported):**
   A long position is initiated if and only if all of the following conditions hold simultaneously:
   - $\text{Regime}_{j, t} \text{ is Bullish } (R_{j, t} > 0)$
   - $P_{j, t} > \text{EMA}_{200, j, t}$
   - $\text{score}_{j, t} \ge 2$
   - No existing position open in stock $j$
   - $S_{j, t} \ge -0.70$ (news sentiment risk gate)

6. **Position Sizing Logic (Source-reported):**
   Cash allocation uses a volatility-parity rule with a hard capital cap:
   $$\text{Risk}_{\text{trade}} = 0.01 \times \text{Cash}$$
   $$\text{shares}_{\text{ATR}} = \left\lfloor \frac{\text{Risk}_{\text{trade}}}{\text{ATR}_{14, j, t}} \right\rfloor$$
   $$\text{shares}_{\text{cap}} = \left\lfloor \frac{0.10 \times \text{Cash}}{P_{j, t}} \right\rfloor$$
   $$\text{Shares}_{j, t} = \min(\text{shares}_{\text{ATR}}, \text{shares}_{\text{cap}})$$
   If $\text{Shares}_{j, t} > 0$, order is dispatched; otherwise, hold.

7. **Exit Trigger (Source-reported):**
   An existing long position is fully liquidated upon the occurrence of ANY of the following four exit conditions:
   - $\hat{y}_{j, t} = 0$ (XGBoost predicts flat or negative next-day return)
   - $R_{j, t} \le 0$ (Regime flips to Bearish)
   - $\text{RSI}_{14, j, t} > 70$ (Mean-reversion overbought extreme)
   - $S_{j, t} < -0.70$ (FinBERT sentiment breaches severe bearish threshold)

8. **Holding Period:**
   - `source-reported`: Average holding period observed empirically is 5.8 days in the hybrid strategy (versus 11.4 days in the baseline strategy).

## Required data

- **Asset Universe:** 100 large-cap US equities selected from the S&P 500 Index across technology, financial, healthcare, energy, and consumer discretionary sectors.
- **Price/Volume Data:** Daily Open, High, Low, Close, and Volume (OHLCV) retrieved via `yfinance`.
- **Textual News Data:** Daily financial news headlines and article summaries retrieved via Alpha Vantage News Sentiment API.
- **Timestamp / Availability Boundary:**
  - `source-reported`: Only news articles timestamped before 9:30 AM EST on trading day $t$ are considered.
  - Prior-day OHLCV closing values $P_{t-1}$ are finalized at 4:00 PM EST market close.
- **Derived Indicators:** $\text{EMA}_{50}$, $\text{EMA}_{200}$, $\text{MACD}(12, 26, 9)$, $\text{RSI}_{14}$, Bollinger Bands $(20, 2)$, $\text{ATR}_{14}$, and 20-day rolling return standard deviation.
- **Missing Data & Filtering:**
  - `source-reported`: StandardScaler applied strictly to the training split (70% time-based partition) and applied out-of-sample without forward leakage.
  - `research-proposed universe filter`: Point-in-time constituent membership filter to eliminate survivorship bias; minimum 30-day median daily dollar volume $\ge \$25\text{M}$ to prevent illiquidity artifacts.

## Execution assumptions

- **Execution Engine:** Backtrader event-driven simulation framework.
- **Trade Formation & Fill Timing:**
  - `source-reported`: Daily execution cycle triggered via cron job prior to market open on an AWS EC2 `t2.medium` instance. Trades routed via market orders.
  - `research-proposed execution timing`: Market-on-Open (MOO) execution at 9:30 AM EST on date $t$, combining pre-market news sentiment up to 9:25 AM EST with date $t-1$ technical indicator state.
- **Order Type & Execution Pricing:**
  - `source-reported`: Market orders executed at daily prices in Backtrader.
  - `source-reported friction`: Frictionless execution assumed; no commissions, spreads, or slippage models are reported in the primary paper.
  - `research-proposed transaction costs`: 0.5 bps brokerage commission + 1.0 bps half-spread slippage (total 3.0 bps round-trip transaction cost per trade).
- **Leverage and Shorting:**
  - `source-reported`: Long-only strategy without short-selling or leverage; cash allocation per trade bounded to a maximum of 10% of total portfolio cash.
  - Maximum simultaneous positions: 10 stocks (implied by 10% position cap).

## Evidence

### Source-reported

All performance figures below are directly reported by Pillai, Ajith, and Sumesh (arXiv:2601.19504v1, Section IV, Tables I & II) across the 24-month out-of-sample backtesting period spanning January 1, 2023 to January 1, 2025, starting from an initial capital of $100,000:

#### Table I: Comparison of Hybrid vs. Baseline Rule-Based Strategy (Source-reported)

| Metric | Hybrid Strategy (XGBoost + FinBERT + Regime) | Baseline Strategy (SMA-50/200 + RSI-14) | Performance Differential |
| :--- | :--- | :--- | :--- |
| **Final Portfolio Value** | **$235,492.83** | $108,643.27 | +$126,849.56 (+116.8%) |
| **Market Value of Positions** | **$166,042.01** | $29,184.72 | +$136,857.29 |
| **Cash Balance** | **$69,450.82** | $79,458.55 | -$10,007.73 |
| **Total Return (%)** | **135.49%** | 8.64% | +126.85% percentage points |
| **CAGR (%)** | **53.46%** | 4.23% | +49.23% percentage points |
| **Max Drawdown (%)** | **-15.60%** | -19.84% | +4.24% percentage points improvement |
| **Sharpe Ratio** | **1.68** | 0.48 | +1.20 (+250.0% relative increase) |
| **Win Ratio (%)** | **61.50%** | 53.40% | +8.10% percentage points |
| **Average Holding Period** | **5.8 days** | 11.4 days | -5.6 days (more active rotation) |

#### Table II: Benchmark Comparison against Major US Market Indexes (Source-reported)

All benchmarks normalized to $100,000 starting capital over the exact same period (January 1, 2023 to January 1, 2025):

| Strategy / Index | Final Portfolio Value ($) | Total Return (%) | Compound Annual Growth Rate (CAGR %) |
| :--- | :--- | :--- | :--- |
| **Hybrid AI Strategy** | **$235,492.83** | **135.49%** | **53.46%** |
| NASDAQ-100 (NDX) | $192,071.58 | 92.07% | 36.78% |
| S&P 500 Index (SPX) | $153,187.39 | 53.18% | 23.56% |
| Dow Jones Industrial Average (DJI) | $128,349.17 | 28.35% | 13.27% |

- **XGBoost Standalone Predictive Metric (Source-reported):** Out-of-sample directional classification accuracy is reported as **63.0%** on the 30% test split.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Omission of Execution Frictions (Provenance Gap):** The primary paper assumes frictionless execution in Backtrader with 0 bps fees and 0 bps slippage. Given an average holding period of 5.8 days (translating to ~40–50 round-trip portfolio turnovers per year across 10 active slots), introducing realistic retail friction (3.0 bps round-trip) would deduct approximately 1.2%–1.5% annually, moderately eroding net CAGR.
2. **Survivorship Bias in Equity Pool:** The 100 S&P 500 equities were selected as large-cap companies as of the study period (e.g., AAPL, MSFT, NVDA). Running historical simulations on surviving winners from 2019 to 2025 introduces non-trivial survivorship bias, inflating reported returns.
3. **Lack of Isolated Component Ablations:** The paper contrasts the complete hybrid system against an unassisted SMA/RSI baseline, but omits ablation tables isolating the marginal contribution of FinBERT sentiment gating alone versus XGBoost prediction alone versus the 20-day return regime filter alone.
4. **Bull Market Out-of-Sample Window:** The test period (January 2023 to January 2025) was an exceptional mega-cap bull market driven by the AI theme (NDX gained 92.07%). A long-only strategy holding high-beta tech components naturally exhibits inflated returns during this window.

## Falsification plan

To test whether the reported hybrid alpha represents genuine multi-modal predictive edge rather than market-beta riding and frictionless backtest artifacts:

1. **Transaction Cost & Slippage Stress Test:**
   - Inject realistic round-trip costs of 3 bps, 5 bps, and 10 bps into the Backtrader simulation over 2023–2025.
   - `research-defined falsification threshold`: The strategy is falsified if net Sharpe ratio drops below 1.00 or net CAGR drops below 25.0% under a conservative 5.0 bps round-trip friction assumption.
2. **FinBERT Sentiment Gate Ablation Test:**
   - Run the full system with the sentiment gating condition ($S_t < -0.70$) completely disabled.
   - `research-defined falsification threshold`: The hypothesis that FinBERT provides an active downside "risk shield" is falsified if maximum drawdown does not worsen by at least 2.5 percentage points (i.e., if max drawdown remains less severe than -18.1%).
3. **Machine Learning Model Permutation Test:**
   - Replace the XGBoost classifier predictions with a random binary coin flip ($\hat{y}_t \sim \text{Bernoulli}(0.5)$) across 1,000 Monte Carlo paths while retaining the technical and regime rules.
   - `research-defined falsification threshold`: The predictive contribution of XGBoost is falsified if the real strategy's Sharpe ratio (1.68) fails to exceed the 95th percentile of the randomized null distribution ($p \ge 0.05$).
4. **Bear Market Regime Stress (2022 Walk-Forward):**
   - Evaluate the strategy during the 2022 calendar year (inflationary bear market where S&P 500 declined ~18% and NDX dropped ~33%).
   - `research-defined falsification threshold`: The regime-adaptive hypothesis is falsified if the strategy suffers a drawdown exceeding -22.0% or fails to outperform the S&P 500 index during the 2022 downturn.

## Crypto portability

- **Portability Classification:** `adapted / unproven` (Research interpretation).
- **Core Structural Divergences in Cryptocurrency Markets:**
  - **Asset Class Focus:** The primary paper evaluates exclusively US equities (S&P 500 constituents). Applying this framework to digital assets (BTC, ETH, SOL, altcoins) is unproven and constitutes research adaptation.
  - **News Channel and NLP Domain Gap:** Equity news via Alpha Vantage focuses on SEC filings, earnings guidance, and traditional press. In crypto, market-moving sentiment is concentrated on X (formerly Twitter), Telegram, Discord, and specialized aggregators (CoinDesk, Cointelegraph). FinBERT's financial vocabulary does not account for crypto-native jargon ("rug pull", "airdrop", "liquidations", "exploit", "hard fork").
  - `research-proposed adaptation (Sentiment)`: FinBERT must be replaced or fine-tuned with a crypto-specific language model (e.g., CryptoBERT) or calibrated prompt-engineered LLMs, and sentiment threshold relaxed from $-0.70$ to $-0.50$ due to elevated crypto polarity volatility.
  - **24/7 Continuous Trading:** Unlike US equity markets with distinct 9:30 AM EST market opens and overnight gaps, crypto trades continuously. Daily rebalancing must be anchored to a standardized UTC cutoff (e.g., 00:00 UTC candle close).
  - **Volatility Sizing:** Digital asset volatility is 3–5x higher than large-cap US equities. The ATR sizing rule ($\text{Cash} \times 0.01 / \text{ATR}$) would allocate tiny capital fractions unless volatility scaling is recalibrated: `research-proposed adaptation`: base risk allocation reduced to $0.5\%$ of cash, with position cap reduced to $5\%$ of total portfolio equity.
  - **Perpetual Funding Rate Drag:** In crypto perpetual futures, long positions in strong bull regimes incur funding costs that frequently reach 15%–40% annualized, creating a substantial negative carry drag that does not exist in cash equities.

## Limitations

1. **Underspecified Feature Construction Details:** While the broad technical indicator families are named, exact mathematical formulas for the 10 specific input columns to XGBoost (e.g., precise normalization of price relative to Bollinger bands and exact lag structure) are partially underspecified in the primary paper text.
2. **Point-in-Time News Feed Timestamping:** In live execution, news arriving between 9:00 AM and 9:30 AM EST requires low-latency parsing and FinBERT inference. The paper executed inference on a single AWS EC2 `t2.medium` CPU instance; latency spikes under heavy news volume could cause delayed market-open orders.
3. **Short Test Horizon:** A 2-year backtest (2023–2025) coincides almost entirely with a strong market recovery driven by tech mega-caps, providing inadequate exposure to multi-year stagnation or structural stagflation regimes.
4. **Execution Cost Blindness:** Completely ignoring commissions and exchange execution slippage in an actively rebalancing portfolio (5.8 days average holding period) creates optimistic return biases.

## Implementation status

`not-implemented`. This strategy has not been coded, backtested, or verified in NautilusTrader, PyBroker, paper trading, testnet, or live trading.

## Adoption boundary

`research-only`. This record is captured for intake review, deduplication, and subsequent hypothesis synthesis within Hermes Wiki Brain. It is `not-approved` for trading, implementation, paper deployment, testnet, or live capital allocation.

## Related Wiki records

- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Market-aligned reinforcement learning for financial sentiment trading.
- `[[quant/raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04]]` — Regime-aware multimodal transformer fusion of news sentiment and price dynamics.
- `[[quant/llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04]]` — LLM-extracted event sentiment factor and contrarian market reaction dynamics.
- `[[quant/qqq-options-microstructure-ensemble-volatility-targeted-2026-09-04]]` — Volatility-targeted ensemble models with multi-tier volatility regime switching.
- `[[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]` — FinBERT news sentiment embeddings combined with topological data analysis for portfolio allocation.

## Sources

1. Varun Narayan Kannan Pillai, Akshay Ajith, and Sumesh K. J. (2026). *"Generating Alpha: A Hybrid AI-Driven Trading System Integrating Technical Analysis, Machine Learning and Financial Sentiment for Regime-Adaptive Equity Strategies"*. arXiv preprint `arXiv:2601.19504v1 [q-fin.CP]`, submitted January 24, 2026. DOI: [10.48550/arXiv.2601.19504](https://doi.org/10.48550/arXiv.2601.19504).
   - Canonical stable abstract URL: [https://arxiv.org/abs/2601.19504](https://arxiv.org/abs/2601.19504)
   - Full text HTML URL: [https://arxiv.org/html/2601.19504v1](https://arxiv.org/html/2601.19504v1)
   - PDF URL: [https://arxiv.org/pdf/2601.19504](https://arxiv.org/pdf/2601.19504)
2. Primary source text citations:
   - Section III-C: Feature Engineering & Preprocessing (Indicators, normalization, derived features).
   - Section III-D: Sentiment Analysis (FinBERT class probabilities, daily sentiment aggregation equation $S_t$, threshold $-0.70$).
   - Section III-E: Machine Learning (XGBoost classifier, `n_estimators=200`, `max_depth=6`, `learning_rate=0.05`, 63% test accuracy).
   - Section III-F: Market Regime Detection ($R_t = \text{SMA}_{20}(\text{pct\_change}(P_t))$, Bullish/Bearish switch).
   - Section III-G: Strategy Execution Logic (Algorithm 1, volatility-based ATR position sizing equation, entry/exit triggers).
   - Section IV-A: Experimental Setup (100 large-cap S&P 500 stocks, 2019–2025 data, Backtrader engine, $100k starting capital).
   - Section IV-B: Table I (Comparison of Hybrid and Baseline Trading Strategies: final values, returns, CAGR, Sharpe, drawdown, holding period).
   - Section IV-C: Table II (Performance Comparison of Hybrid Strategy vs Major Indices: SPX, NDX, DJI).
3. Academic works cited in primary paper:
   - Lo, A. W., Mamaysky, H., & Wang, J. (2000). "Foundations of technical analysis: Computational algorithms, statistical inference, and empirical implementation." *The Journal of Finance*, 55(4), 1705–1765.
   - Araci, D. (2019). "FinBERT: Financial sentiment analysis with pre-trained language models." *arXiv preprint arXiv:1908.10063*.
   - Atkins, A., Niranjan, M., & Gerding, E. (2018). "Financial news predicts stock market volatility better than close price." *The Journal of Finance and Data Science*, 4(2), 120–137.
   - Jiang, Z., Xu, D., & Liang, J. (2017). "A deep reinforcement learning framework for the financial portfolio management problem." *arXiv preprint arXiv:1706.10059*.
