---
schema: strategy-research-record-v1
title: "LSTM with Learnable Sector Embeddings for Cross-Sectional Equity Statistical Arbitrage: Endogenous Industry Momentum and Short-Term Reversal Decomposition"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning
  - deep-learning
  - lstm
  - sector-embeddings
  - statistical-arbitrage
  - cross-sectional-equity
  - short-term-reversal
  - industry-momentum
  - explainable-ai
status: research-only
confidence: high
source_as_of: 2026-08-06
sources:
  - "Julius Döbelt, 'Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series', arXiv:2608.05755v2 [q-fin.ST], August 2026. DOI: 10.48550/arXiv.2608.05755. https://arxiv.org/abs/2608.05755"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LSTM with Learnable Sector Embeddings for Cross-Sectional Equity Statistical Arbitrage: Endogenous Industry Momentum and Short-Term Reversal Decomposition

## Provenance

- **Author:** Julius Döbelt (Technical University of Darmstadt, `julius.doebelt@tu-darmstadt.de`)
- **Title:** "Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series"
- **Identifier:** arXiv:2608.05755v2 [q-fin.ST]
- **Submission Date:** August 6, 2026 (v1: 2026-08-06, v2: 2026-08-11)
- **DOI:** [10.48550/arXiv.2608.05755](https://doi.org/10.48550/arXiv.2608.05755)
- **Stable URL:** https://arxiv.org/abs/2608.05755
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Target Universe:** S&P 500 historical constituents, survivorship-bias-free reconstructed from Refinitiv monthly constituent lists over 30 years (January 1995 to December 2024), evaluated across 27 walk-forward 4-year rolling periods (3-year training, 1-year test; $N = 6,793$ daily out-of-sample trading days).

## Economic mechanism

### Source-reported

Standard sequence models (e.g., canonical LSTMs following Fischer and Krauss, 2018) pool cross-sectional stock returns and apply shared weights across all securities, implicitly assuming all stocks follow an identical return-generating process. This ignores well-documented cross-sectional heterogeneity across industrial sectors (Moskowitz and Grinblatt, 1999; Hou, 2007).

The author incorporates continuous, learnable sector embeddings ($D=2$ dimensions for $C=11$ TRBC sectors) into a recurrent architecture alongside regularization (label smoothing, gradient clipping, weight decay, dropout, early stopping). The model is trained on a binary classification task: predicting whether each stock will underperform or outperform the cross-sectional median return of the S&P 500 on the following day.

Through mathematical decomposition of the linear output layer connecting hidden states and sector embeddings to the classification logits, the author shows that the predictive signal endogenously decomposes into two established asset pricing anomalies:
1. **Industry Momentum:** The learned sector embedding offset $\Delta_c = (e_{1,c}w_{12} + e_{2,c}w_{22}) - (e_{1,c}w_{11} + e_{2,c}w_{21})$ operates as a static cross-sectional intercept that reflects sector return persistence over the 3-year training window. Sectors with strong past performance receive positive $\Delta_c$, lowering the temporal threshold required for a stock in that sector to enter the long portfolio (mirroring Jegadeesh and Titman, 1993; Moskowitz and Grinblatt, 1999).
2. **Short-Term Reversal:** The temporal component extracted by the LSTM from the 60-day lag sequence of standardized returns recovers short-horizon mean reversion. Candidates selected for the long portfolio exhibit sustained negative returns over the prior 5 days, while short candidates exhibit sharp positive run-ups over the prior 5 days (mirroring Lehmann, 1990; Jegadeesh, 1990).

### Research interpretation

The strategy is a hybrid statistical arbitrage architecture combining cross-sectional categorical conditioning with temporal sequence modeling:
- **Structural Component (Macro / Cross-Sectional):** The 2-dimensional sector embedding $e_c$ acts as an empirical sector risk premium / momentum filter. It shifts the baseline log-odds of outperforming the cross-sectional median based on medium-horizon sector performance learned during the preceding 3-year rolling window.
- **Dynamic Component (Micro / Idiosyncratic):** The recurrent LSTM cell acts as an idiosyncratic short-term reversal extractor, identifying stocks within or across sectors that have experienced temporary liquidity shocks or price overshoots over the past 5 to 60 trading days.
- **Mechanism of Alpha Failure (Momentum Crashes):** Because the sector embedding is fixed during the 1-year out-of-sample test period based on the prior 3-year training data, the model is inherently exposed to "momentum crashes" (Daniel and Moskowitz, 2016). When a bear market turns into a sharp recovery (such as 2003 post-dot-com bust), prior beaten-down sectors (e.g., Technology) rebound violently while defensive sectors (e.g., Utilities) lag. The fixed sector embedding tilts heavily short into the highest-rebounding sectors and long into lagging defensive sectors, generating severe drawdowns on the short leg.

## Signal

### Formation timestamp
- Calculated at daily close ($t$) after all S&P 500 constituent closing prices are recorded.
- Trade executed at the open of trading day $t+1$ (or close-to-close with 1-bar execution delay).
- Market timezone: US Eastern Time (ET).

### Lookback
- **Input sequence window:** 60 trading days of lagged daily returns ($\tilde{R}_{t-59}^s, \dots, \tilde{R}_t^s$).
- **Rolling calibration window:** 4 years per study period, partitioned into exactly 3 years (approx. 756 trading days, $\sim 340,000$ stock-day observations) for training/validation, and 1 year (approx. 252 trading days, $\sim 125,000$ stock-day observations) for out-of-sample testing.
- **Roll frequency:** The 4-year block rolls forward annually by 1 year, creating 27 distinct non-overlapping out-of-sample test years (1998 to 2024).

### Data preprocessing & normalization
- Daily simple returns: $R_t^s = \frac{P_t^s - P_{t-1}^s}{P_{t-1}^s}$.
- Standardization: $\tilde{R}_t^s = \frac{R_t^s - \mu_{\text{train}}}{\sigma_{\text{train}}}$, where $\mu_{\text{train}}$ and $\sigma_{\text{train}}$ are calculated strictly over the 3-year training set to prevent look-ahead bias and data leakage.
- Target label: Binary classification relative to the daily cross-sectional median return across all active S&P 500 constituents at day $t+1$:
  $$y_{t+1}^s = \begin{cases} 1 & \text{if } R_{t+1}^s > \text{median}_{i}(R_{t+1}^i) \\ 0 & \text{if } R_{t+1}^s \le \text{median}_{i}(R_{t+1}^i) \end{cases}$$

### Network architecture
- **Recurrent layer:** 3-layer many-to-one LSTM with $H = 25$ hidden units per layer.
- **Final hidden state:** $\mathbf{h}_T^s \in \mathbb{R}^{25}$ extracted after processing the 60-day return sequence.
- **Sector embedding layer:** Differentiable lookup table $W_{\text{emb}} \in \mathbb{R}^{11 \times 2}$ for the 11 TRBC sectors. Each stock $s$ belonging to sector $c \in \{1, \dots, 11\}$ retrieves a 2-dimensional continuous embedding $\mathbf{e}_c \in \mathbb{R}^2$.
- **Classification layer:** Concatenation of $\mathbf{h}_T^s$ and $\mathbf{e}_c$ into a fully connected layer with $H + D = 25 + 2 = 27$ inputs, producing 2-class logits $\mathbf{z}_s = (z_0, z_1) \in \mathbb{R}^2$:
  $$\mathbf{z}_s = \mathbf{W}_h \mathbf{h}_T^s + \mathbf{W}_e \mathbf{e}_{c(s)} + \mathbf{b}$$
  where $\mathbf{W}_h \in \mathbb{R}^{2 \times 25}$, $\mathbf{W}_e \in \mathbb{R}^{2 \times 2}$, and $\mathbf{b} \in \mathbb{R}^2$.
- **Probabilities:** Passed through Softmax $\hat{P}(y_{t+1}^s = 1) = \frac{e^{z_1}}{e^{z_0} + e^{z_1}}$.

### Regularization parameters
- **Label smoothing:** $\alpha = 0.1$, re-scaling binary labels to target values $0.05$ (for Class 0) and $0.95$ (for Class 1).
- **Gradient clipping:** Global gradient norm clipped at $2.0$.
- **Weight decay:** $\lambda = 10^{-4}$ in the Adam optimizer.
- **Early stopping:** Monitored on validation loss with a patience of 20 epochs.
- **Dropout:** Input dropout applied to input features; recurrent dropout applied to hidden state transitions.

### Portfolio construction & entry/exit
- **Portfolio parameter:** $k = 10$ (robustness evaluated across $k \in \{5, 10, 15, 20, 25, 30, 35, 40, 45, 50\}$).
- **Long leg:** Long the $k = 10$ stocks with the highest predicted probability $\hat{P}(y_{t+1}^s = 1)$ of outperforming the cross-sectional median.
- **Short leg:** Short the $k = 10$ stocks with the highest predicted probability of underperforming (lowest probability of outperforming, $\hat{P}(y_{t+1}^s = 0)$).
- **Total positions:** $2k = 20$ stocks equally weighted ($w_i = +1/(2k)$ for longs, $w_i = -1/(2k)$ for shorts).
- **Rebalance cadence:** Daily.
- **Position roll rule:** If a stock selected at day $t$ remains in the same leg at day $t+1$, the position is held without incurring rebalancing turnover.

## Required data

- **Instrument universe:** Constituents of the S&P 500 index.
- **Survivorship-bias-free composition:** Monthly index constituent lists (sourced from Refinitiv / Thomson Reuters) mapped into an active inclusion matrix; stocks delisted during a test year are held as long as trading data is available.
- **Timeframe:** Daily closing prices, total return indices adjusted for dividends, splits, and corporate actions.
- **Sample period:** January 1, 1995 to December 31, 2024 (30 calendar years).
- **Sector taxonomy:** The Refinitiv Business Classification (TRBC), comprising 11 economic sectors: Basic Materials, Consumer Cyclicals, Consumer Non-Cyclicals, Energy, Financials, Healthcare, Industrials, Technology, Telecommunications Services, Utilities, Real Estate.
- **Macro-financial covariates (evaluated as an ablation/negative test):**
  - WTI crude oil futures returns (linear interpolation applied to the negative pricing anomaly on April 20, 2020, setting value to 14.14).
  - CBOE Volatility Index (VIX) daily values (linear interpolation on 6 missing random prints between 1997 and 2021).
  - Gold futures daily returns.
  - 10-year US Treasury constant maturity yield.
  - Term spread: 10-year Treasury yield minus 3-month Treasury yield.

## Execution assumptions

- **Execution price:** Daily close or next-day open for constituent stocks.
- **Order types:** Market-on-open (MOO) or market-on-close (MOC) assumed.
- **Transaction costs:** 2 basis points (0.02%) per half-turn (4 bps round-trip) applied to large-cap liquid S&P 500 constituents, based on institutional trading cost metrics from Frazzini, Israel, and Moskowitz (2012) and Jha (2016).
- **Cost application rule:** Costs applied only upon position entry and position exit. If a stock remains in the long or short leg across consecutive days, no transaction cost is charged on intervening days.
- **Borrowing / Shorting:** Unconstrained short availability assumed for S&P 500 large-cap constituents; borrow cost omitted under institutional prime brokerage assumption for major index names.
- **Market impact:** Assumed negligible for small institutional allocations taking $\le 0.01\% - 0.03\%$ of daily stock volume (Frazzini et al., 2012).

## Evidence

### Source-reported

All figures below are reported directly by Julius Döbelt (arXiv:2608.05755v2) over the full 27-year out-of-sample evaluation period ($N = 6,793$ daily test returns, 1998–2024) with 2 bps transaction costs per half-turn:

1. **Risk-Adjusted Performance (Primary Comparison, $k=10$):**
   - **Sector LSTM:** Annualized Sharpe Ratio = **0.69** (post-cost).
   - **Base LSTM (canonical return-only):** Annualized Sharpe Ratio = **0.39** (post-cost).
   - **Random Forest Benchmark:** Annualized Sharpe Ratio = **0.53** (post-cost).
   - **Covariate LSTM (macro-financial features):** Annualized Sharpe Ratio = **0.27** (post-cost).
   - **Buy-and-Hold Market Benchmark:** Annualized Sharpe Ratio = 0.50 (pre-cost market return, exposed to market $\beta$).

2. **Statistical Significance Testing:**
   - **Ledoit-Wolf Circular Block Bootstrap Test (Sharpe differences):**
     - Sector LSTM vs. Base LSTM: $p = 0.045$ (statistically significant higher Sharpe at 5% level; block length 19 days, 1,000 bootstrap iterations).
     - Sector LSTM vs. Covariate LSTM: $p = 0.009$ (statistically significant higher Sharpe at 1% level).
     - Sector LSTM vs. Random Forest: $p = 0.204$ (not statistically distinguishable at conventional levels).
     - Covariate LSTM vs. Base LSTM: $p = 0.083$ (Covariate LSTM significantly dominated).
   - **Diebold-Mariano Test (Directional Accuracy):**
     - Sector LSTM vs. Random Forest: $p = 0.0095$ (statistically superior accuracy at 1% level).
     - Sector LSTM vs. Base LSTM: $p = 0.092$ (marginally significant at 10% level).
     - Base LSTM vs. Random Forest: $p = 0.115$ (not statistically distinguishable).

3. **Predictive Accuracy and Parameter Stability:**
   - Traded portfolio directional accuracy ($Acc_{k=10}$) remained strictly within **0.514 to 0.525** across all tested network depths (1 to 5 layers).
   - Cross-sectional classification accuracy across the entire S&P 500 ($Acc_{\text{all}}$) remained within **0.502 to 0.506**.
   - Sector embeddings add only 26 trainable parameters ($11 \times 2$ embedding matrix plus $2 \times 2$ projection weights) to the network.

4. **Decomposition & Interpretability Validation:**
   - Across the 27 out-of-sample periods, the alignment between learned sector bias $\Delta_c$ and realized test-year sector returns had a Pearson correlation of **$r = 0.38$ ($p = 0.025$)** with accuracy outperformance over the base LSTM, and **$r = 0.40$ ($p = 0.019$)** with Sharpe ratio outperformance (Holm-adjusted $p$-value = **0.038** via 20,000 permutations).
   - In 2007 (favorable regime), cross-sectional correlation between $\Delta_c$ and realized sector mean daily return reached **$+0.74$**, generating heavy long exposure in Energy (+87.6 pp) and short exposure in Consumer Cyclicals (-34.8 pp) and Technology (-32.1 pp).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Severe Post-2008 Alpha Decay:**
   - Strategy returns and Sharpe ratios deteriorated markedly after 2008. Prior to 2008, all models exhibited annualized Sharpe ratios averaging above 2.0 (and $>4.0$ in late 1990s).
   - From 2009 through 2024, average daily returns of all models remained consistently below **0.1%**, with multiple years exhibiting negative Sharpe ratios.
   - The single post-2008 exception was 2020 during the COVID-19 crash, confirming findings in Clegg and Krauss (2018) that statistical arbitrage opportunities spike during systemic crises but remain depressed during normal regimes.

2. **Vulnerability to Momentum Crashes (2003 Case Study):**
   - In 2003, during the market rebound following the dot-com crash, the weighted correlation between learned $\Delta_c$ and realized test returns collapsed to **$-0.91$**.
   - The model was long defensive sectors (Utilities $+15.09\%$, Healthcare $+27.04\%$) and short crushed cyclicals (Technology $+53.73\%$), causing massive losses on the short leg.
   - Over the full 27-year sample, the average weighted correlation between $\Delta_c$ and realized return was only **7.6%**, proving that the static 1-year sector bias is fragile during regime shifts.

3. **Complete Failure of Macro-Financial Covariates:**
   - Incorporating macro covariates (oil, VIX, gold, yield spread, 10Y yield) into the LSTM reduced the Sharpe ratio from 0.69 to **0.27** ($p = 0.009$).
   - Without strong input dropout, the covariate LSTM suffered severe overfitting with rapidly diverging validation loss. Even with regularized dropout, the macro covariates added noise rather than predictive signal.

## Falsification plan

1. **Ablation of Sector Embedding:** Remove the sector embedding lookup table $W_{\text{emb}}$ and evaluate the return-only base LSTM. If the Sharpe ratio does not show a statistically significant degradation ($p < 0.05$ via Ledoit-Wolf bootstrap), the thesis that cross-sectional categorical heterogeneity drives the edge is falsified.
2. **Shuffled Sector Permutation (Placebo Test):** Randomly permute the TRBC sector IDs across stocks at the beginning of each 3-year training window. If the randomized-sector model matches or exceeds the real-sector model's Sharpe ratio (0.69), the economic industry momentum thesis is falsified.
3. **Turnover & Execution Friction Stress Test:** Increase transaction costs from 2 bps per half-turn to 5, 10, and 15 bps. Since the strategy rebalances daily across 20 names, identify the breakeven cost threshold where the Sharpe ratio falls to zero.
4. **Sub-period Post-2015 Validation:** Restrict out-of-sample evaluation strictly to 2016–2024. If the post-2015 Sharpe ratio is non-positive or statistically indistinguishable from zero, the strategy is confirmed dead in modern equity markets due to quantitative crowding.
5. **Alternative Cross-Sectional Groupings:** Substitute GICS (Global Industry Classification Standard) or statistical correlation clustering for TRBC. If the performance disappears under alternative standard classifications, the result is an artifact of Refinitiv TRBC boundaries.

## Crypto portability

**Adapted / Unproven**

The core architectural hypothesis—combining an explicit, low-dimensional learnable categorical embedding for cross-sectional market segments with a recurrent sequence model for short-term temporal reversal—can be ported conceptually to crypto, but involves fundamental friction adaptations:

1. **Sector Taxonomy Void:** Equities have standardized, audited classifications (TRBC, GICS, SIC). Cryptocurrency "sectors" (e.g., Layer 1, DeFi, AI/Compute, Memes, DePIN, Gaming, Oracle/Interoperability) are unofficial, fluid, and subjective (e.g., CoinMarketCap/CoinGecko tags). Protocols frequently pivot narrative categories.
2. **High Beta / Cross-Sectional Co-Movement:** Crypto assets display significantly higher pairwise cross-correlation and Bitcoin-beta exposure ($>0.70$ during drawdowns) than S&P 500 equities. True idiosyncratic cross-sectional dispersion is substantially lower, reducing the diversification benefit of a dollar-neutral long-short basket.
3. **Hyper-Compressed Sector Rotation Cycles:** Equity industry momentum operates over 3 to 12 months. Crypto narrative rotation cycles operate over days or weeks. A 3-year rolling calibration window would hopelessly lag crypto market shifts; a crypto adaptation would require rolling windows of 30 to 90 days, increasing sample noise.
4. **Severe Fee & Slippage Drag:** The equity model assumes 2 bps per half-turn in ultra-liquid S&P 500 names. On crypto exchanges (e.g., Binance, Bybit), taker fees for mid-cap altcoins range from 4 to 10 bps, plus 5 to 20 bps effective bid-ask spread and market impact. A daily rebalancing long-short strategy would suffer severe fee drag that would rapidly erase a 0.69 Sharpe ratio.
5. **Short Borrow Constraints & Funding Costs:** In equity, large-cap borrow is generally stable and low-cost. In crypto perpetual futures, shorting requires paying funding rates during negative funding regimes, or maintaining margin across fragmented collateral pools, exposing the portfolio to liquidation cascade risks.

## Limitations

- **Underspecified Code Repository:** While the author notes that models and weights are available on GitHub, an immutable commit SHA and specific repository path were not provided in the preprint text.
- **Severe Post-2008 Return Degradation:** The strategy's long-term profitability is largely concentrated in pre-2008 data; post-2008 performance shows minimal economic alpha, indicating that statistical arbitrage on S&P 500 daily returns has experienced severe structural decay.
- **Momentum Crash Sensitivity:** The 1-year fixed sector bias causes catastrophic drawdowns when market regimes abruptly rotate from crisis to recovery (e.g., 2003).
- **Execution Cost Sensitivity:** Daily rebalancing of 20 stocks generates substantial turnover; realistic execution slippage and non-zero borrow fees would materially reduce net performance.
- **No Independent Reproduction:** Findings are source-reported by a single author and have not been validated in an independent trading engine.

## Implementation status

Not implemented. No prototype or backtest of this architecture has been constructed in PyBroker, NautilusTrader, or any internal research framework.

## Adoption boundary

Research-only. This record is an analytical capture of academic research into recurrent neural networks with learnable categorical embeddings. It does not constitute:
- Validated or live-ready alpha;
- Implementation approval for PyBroker or NautilusTrader;
- Authorization for paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- [[cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02]] — Mixture-of-experts architecture for cross-sectional volatility prediction; shares the approach of conditioning neural predictions on structural regime/categorical variables.
- [[equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]] — Tabular deep learning and cross-regime optimization for equity statistical arbitrage.
- [[equity-analyst-coverage-network-graph-attention-momentum-spillover-2026-09-02]] — Cross-sectional information diffusion and momentum spillovers across equities via network attention.
- [[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]] — Cross-sectional momentum baseline and quintile sorting mechanics.
- [[crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]] — Daily short-term reversal dynamics in cross-sectional asset universes.

## Sources

1. Julius Döbelt, "Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series", arXiv:2608.05755v2 [q-fin.ST], August 2026. DOI: [10.48550/arXiv.2608.05755](https://doi.org/10.48550/arXiv.2608.05755). URL: https://arxiv.org/abs/2608.05755.
