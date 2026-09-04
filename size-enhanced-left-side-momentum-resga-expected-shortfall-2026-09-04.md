---
schema: strategy-research-record-v1
title: "Size-Enhanced Left-Side Momentum: Cross-Sectional Expected Shortfall and Firm Size Interaction Alpha (ReSGA)"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tail-risk
  - expected-shortfall
  - value-at-risk
  - cross-sectional-momentum
  - left-side-momentum
  - too-big-to-fail
  - autoencoder
  - retrieval-augmented
status: research-only
confidence: medium
source_as_of: 2026-06-05
sources:
  - https://arxiv.org/abs/2606.04576
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Size-Enhanced Left-Side Momentum: Cross-Sectional Expected Shortfall and Firm Size Interaction Alpha (ReSGA)

## Provenance

- **Primary Source**: arXiv:2606.04576v1 [stat.ML], submitted June 5, 2026.
- **Authors**: Yichi Zhang (Department of Statistics & Actuarial Science, The University of Hong Kong), Ke Zhu (Department of Statistics & Actuarial Science, The University of Hong Kong), Zhoufan Zhu (Wang Yanan Institute for Studies in Economics [WISE] and School of Economics, Xiamen University; corresponding author).
- **Title**: "ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall"
- **Primary DOI / Canonical URL**: https://doi.org/10.48550/arXiv.2606.04576 / https://arxiv.org/abs/2606.04576
- **Companion Website / Source Code / Forecast Archive**: https://tailrisk-resga.github.io / https://github.com/tailrisk-resga/tailrisk-resga.github.io
- **Data As-Of**: Monthly US equities from January 1926 through December 2023 (>40,000 stocks, 153 firm characteristics compiled by Jensen, Kelly, and Pedersen [2023]). Out-of-sample test window: January 2014 to December 2023 (10 years, 120 monthly rebalances).

## Economic mechanism

### Source-reported

In standard asset pricing theory, downside tail risk—specifically Value-at-Risk (VaR) and Expected Shortfall (ES)—represents an uncompensated risk or persistent underreaction phenomenon in the cross-section of equities (Atilgan et al., 2020). Previous studies document "left-side momentum": stocks with severe downside tail risk continue to suffer negative abnormal returns due to investor underreaction to bad news and persistent idiosyncratic risk.

Zhang, Zhu, and Zhu (2026) introduce a new economic hypothesis: the pricing and future return implications of tail risk are fundamentally asymmetric across firm size, motivated by the "too big to fail" phenomenon in equity markets:
1. **Large-cap firms with severe downside risk**: When a large, systemic firm suffers elevated predicted tail risk (severe negative ES), downside risk attracts heightened market attention, institutional liquidity provision, lender renegotiation, or government/central bank policy backstops. This intervention truncates catastrophic bankruptcy risk, limiting extreme losses and enabling long-term valuation recovery. Consequently, high-tail-risk large-cap equities yield strong positive subsequent returns.
2. **Small-cap firms with severe downside risk**: In contrast, when small-cap firms experience severe predicted tail risk, extreme downside potential reflects genuine idiosyncratic fragility, distress, financing exhaustion, and elevated default/delisting probability rather than priced systematic risk. Small firms lack policy backstops and institutional liquidity support, leading to continued underperformance and negative returns.

### Research interpretation

The proposed strategy exploits an interaction between machine-learning-forecasted downside tail risk (5% Expected Shortfall) and cross-sectional firm capitalization:
- **Primary Signal**: The non-linear product of firm size deviation $(\mathrm{Cap}_{i,t-1} - \overline{\mathrm{Cap}}_{t-1})$ and normalized tail-loss severity $[1 - \exp(\widehat{\mathrm{ES}}_{i,t})]$.
- **Long Leg (P1 Decile)**: Mega- and large-cap stocks facing severe predicted tail losses (acting as high-probability rebound candidates supported by institutional demand and systemic importance).
- **Short Leg (P10 Decile)**: Small- and micro-cap stocks facing severe predicted tail losses (distressed, fragile firms facing structural dilution, illiquidity, or default).
- **Forecast Engine (ReSGA)**: A Retrieval-Enhanced Self-Grouping Autoencoder trained under the degree-0 Fissler-Ziegel (FZ0) joint scoring rule. ReSGA extracts latent cross-sectional clusters among assets via self-grouping and augments asset-level temporal memory via historical retrieval across peer assets, outperforming 12 benchmark models in statistical tail loss minimization.

## Signal

### Mathematical Specification

1. **Loss Elicitation Function (Source-reported)**:
   The model jointly predicts $\mathrm{VaR}_{i,t}$ and $\mathrm{ES}_{i,t}$ at quantile $\tau = 0.05$ under the degree-0 Fissler-Ziegel scoring rule $\ell_{\mathrm{FZ0}}$ (Fissler & Ziegel, 2016):
   $$\ell_{\mathrm{FZ0}}(Y, (v, e)) = -\frac{1}{\tau e}\,\mathbf{1}\{Y \le v\}(v - Y) + \frac{v}{e} + \log(-e) - 1$$
   where $Y = r_{i,t}$ is the excess monthly return, $v = \mathrm{VaR}_{i,t}$, and $e = \mathrm{ES}_{i,t}$, defined on the admissible cone $\Gamma = \{(v, e) : e < v < 0\}$.

2. **Admissibility Mapping (Source-reported)**:
   The network outputs two unconstrained latent scores $\mathbf{y}_{i,t} = (y_{i,t,1}, y_{i,t,2})' \in \mathbb{R}^2$, mapped to valid $(\mathrm{VaR}, \mathrm{ES})$ through Softplus activation:
   $$\widehat{\mathrm{VaR}}_{i,t} = -\mathrm{Softplus}(y_{i,t,1})$$
   $$\widehat{\mathrm{ES}}_{i,t} = -\big[\mathrm{Softplus}(y_{i,t,1}) + \mathrm{Softplus}(y_{i,t,2})\big]$$
   where $\mathrm{Softplus}(x) = \log(1 + e^x) > 0$. This strictly enforces $\widehat{\mathrm{ES}}_{i,t} < \widehat{\mathrm{VaR}}_{i,t} < 0$.

3. **Size-Enhanced Left-Side Momentum Signal $\alpha_{i,t}$ (Source-reported)**:
   $$\alpha_{i,t} = \big(\mathrm{Cap}_{i,t-1} - \overline{\mathrm{Cap}}_{t-1}\big) \times \big[1 - \exp(\widehat{\mathrm{ES}}_{i,t})\big]$$
   where:
   - $\mathrm{Cap}_{i,t-1} = \log(\text{MarketCap}_{i,t-1})$ is the log market capitalization of stock $i$ at month-end $t-1$.
   - $\overline{\mathrm{Cap}}_{t-1} = \frac{1}{N_{t-1}}\sum_{i=1}^{N_{t-1}} \mathrm{Cap}_{i,t-1}$ is the contemporaneous cross-sectional mean log market cap.
   - $[1 - \exp(\widehat{\mathrm{ES}}_{i,t})] \in (0, 1)$ acts as a monotonic tail-loss severity weight (approaching 1 when $\widehat{\mathrm{ES}} \ll 0$, and approaching 0 when $\widehat{\mathrm{ES}} \to 0^-$).
   - $(\mathrm{Cap}_{i,t-1} - \overline{\mathrm{Cap}}_{t-1})$ acts as a size classifier (positive for large caps, negative for small caps).

4. **Signal Formation & Execution Cadence**:
   - **Formation Timestamp**: Monthly, at the final calendar close of month $t-1$ (source-reported).
   - **Execution Timestamp**: First trading bar of month $t$ (`research-proposed`; source assumes generic monthly holding period).
   - **Lookback Window**: Trailing $S = 12$ monthly lags of 153 firm characteristics tensor $\mathcal{X}_{t-1} \in \mathbb{R}^{N_t \times S \times P}$ (source-reported). Expanding window training from 1926.
   - **Long Entry**: Stocks sorted into top decile P1 (highest $\alpha_{i,t}$) at month-end $t-1$ (source-reported).
   - **Short Entry**: Stocks sorted into bottom decile P10 (lowest $\alpha_{i,t}$) at month-end $t-1$ (source-reported).
   - **Exit Rule**: Positions held for exactly one month; re-sorted and rebalanced monthly (`source-reported`).
   - **Position Sizing**: Value-weighted by market capitalization within each decile portfolio (source-reported). Dollar-neutral 100% Long P1 / 100% Short P10 (`research-proposed` portfolio leverage implementation).

## Required data

- **Instruments**: US-listed common equities (NYSE, AMEX, NASDAQ).
- **Universe**: >40,000 unique common stocks over 1926–2023 compiled by Jensen, Kelly, and Pedersen (2023).
- **Timeframe**: Monthly excess returns and characteristic panels.
- **Fields**:
  - Monthly stock excess returns $r_{i,t}$ (relative to risk-free rate).
  - Market capitalization $\text{MarketCap}_{i,t-1}$.
  - 153 firm characteristics covering 13 themes: Low Risk, Value, Quality, Low Leverage, Momentum, Size, Profit Growth, Short-Term Reversal, Seasonality, Investment, Profitability, Debt Issuance, Accruals.
- **Preprocessing & Normalization (Source-reported)**:
  - All 153 characteristics cross-sectionally rank-normalized into $[-0.5, 0.5]$ contemporaneous to each month $t-1$ (following Gu, Kelly, Xiu, 2020).
  - Missing characteristic values imputed with contemporaneous cross-sectional median (source-reported).
- **Point-in-Time Availability**: Accounting characteristics lagged by standard publication delays (e.g. 6-month lag for annual accounting data as per standard JKP factor construction) to ensure strictly causal point-in-time validity.

## Execution assumptions

- **Signal-to-Order Timing**: Month-end signal evaluation $\to$ execution at next-period open (`research-proposed`; source specifies monthly return intervals).
- **Fill Model**: Monthly value-weighted rebalance assuming instantaneous execution at recorded month-end prices (`source-reported` implicit assumption).
- **Fees & Slippage**:
  - Primary source reports gross returns with **0 bps** transaction fees, **0 bps** slippage, and **0 bps** short borrow cost (`source-reported` gap).
  - `Research-proposed` operational friction hurdle: 10 bps round-trip transaction costs for liquid long deciles; 35 bps round-trip transaction costs plus 120 bps annualized short-borrow rebate/fee for small-cap P10 short decile.
- **Borrow & Shorting Constraints**: Primary source assumes unconstrained shorting of decile P10. In reality, P10 contains small/micro-cap equities with extreme predicted tail loss, which are frequently hard-to-borrow (HTB) with elevated borrow fees or locate restrictions (`research-proposed` operational limitation).
- **Capacity & Turnover**: High capacity on Long leg (P1 contains large/mega caps), but constrained capacity on Short leg (P10 contains illiquid small caps).

## Evidence

### Source-reported

All figures below are directly extracted from Section 3.2, Section 3.3 (Tables 5 & 6), and Section 4 (Table 8) of Zhang, Zhu, and Zhu (2026), evaluated over the 10-year out-of-sample period (January 2014 to December 2023, 120 monthly periods):

#### 1. Statistical Tail Risk Forecasting Performance (Table 3 & Table 4)
- **Diebold-Mariano (DM) Test**: ReSGA achieves statistically significantly lower out-of-sample FZ0 loss than all competing models except SGA at 1% significance level.
- **Model Confidence Set (MCS)**: At 90% confidence level, only ReSGA and SGA are retained in the superior model set across all 13 evaluated architectures.
- **Expected Shortfall Validity (AESR Test Pass Rate at $\alpha = 0.05$)**: ReSGA achieves 70.55% stock pass rate in US data (highest among all models; SGA is 67.39%).

#### 2. Baseline Left-Side Momentum (Sorting on ES alone, Table 5)
- Rebalanced monthly, value-weighted:
  - **P1 (Lowest Tail Risk)**: Avg return +0.900%/mo, MDD 20.7%, Annualized Sharpe Ratio 0.826.
  - **P8**: Avg return +1.196%/mo, MDD 51.5%, Annualized Sharpe Ratio 0.487.
  - **P9**: Avg return +0.512%/mo, MDD 71.0%, Annualized Sharpe Ratio 0.185.
  - **P10 (Highest Tail Risk)**: Avg return -0.024%/mo, MDD 81.0%, Annualized Sharpe Ratio -0.007.
  - **H-L (Buy P1, Sell P10)**: Avg return +0.924%/mo, MDD 76.9%, Annualized Sharpe Ratio 0.298.

#### 3. Size-Enhanced Left-Side Momentum (Sorting on $\alpha_{i,t}$, Table 6)
- Value-weighted deciles sorted on $\alpha_{i,t} = (\mathrm{Cap}_{i,t-1} - \overline{\mathrm{Cap}}_{t-1}) \times [1 - \exp(\widehat{\mathrm{ES}}_{i,t})]$:
  - **P1 (High $\alpha$, Large-Cap High-ES)**: Avg return **+0.905%/mo**, Annualized Sharpe Ratio **0.710**.
  - **P2**: Avg return +0.806%/mo, Sharpe 0.613.
  - **P3**: Avg return +0.868%/mo, Sharpe 0.585.
  - **P4**: Avg return +0.819%/mo, Sharpe 0.510.
  - **P5**: Avg return +0.697%/mo, Sharpe 0.401.
  - **P6**: Avg return +0.702%/mo, Sharpe 0.391.
  - **P7**: Avg return +0.552%/mo, Sharpe 0.291.
  - **P8**: Avg return +0.336%/mo, Sharpe 0.153.
  - **P9**: Avg return -0.069%/mo, Sharpe -0.026.
  - **P10 (Low $\alpha$, Small-Cap High-ES)**: Avg return **-1.308%/mo**, Annualized Sharpe Ratio **-0.392**.
  - **H-L (Long P1 / Short P10)**:
    - Monthly Average Return: **+2.213%** (annualized ~26.56%).
    - Annualized Sharpe Ratio: **0.787**.
    - Fama-French 5-Factor Alpha: **+1.842% per month** (~22.10% annualized), $t$-statistic $p$-value = **0.013** (statistically significant at 5% level).

#### 4. Benchmark Model Comparison on H-L Strategy (Table 6)
- **Linear**: Avg +1.818%/mo, SR 0.673, FF5 Alpha +1.477% ($p = 0.030$)
- **Feedforward NN**: Avg +1.827%/mo, SR 0.659, FF5 Alpha +1.510% ($p = 0.035$)
- **LANN**: Avg +1.973%/mo, SR 0.723, FF5 Alpha +1.625% ($p = 0.019$)
- **DLinear**: Avg +1.876%/mo, SR 0.691, FF5 Alpha +1.516% ($p = 0.032$)
- **LSTM**: Avg +2.034%/mo, SR 0.744, FF5 Alpha +1.720% ($p = 0.010$)
- **GRU**: Avg +1.860%/mo, SR 0.671, FF5 Alpha +1.536% ($p = 0.030$)
- **Informer**: Avg +2.002%/mo, SR 0.719, FF5 Alpha +1.680% ($p = 0.013$)
- **EInformer**: Avg +1.850%/mo, SR 0.678, FF5 Alpha +1.501% ($p = 0.029$)
- **DInformer**: Avg +1.862%/mo, SR 0.689, FF5 Alpha +1.519% ($p = 0.023$)
- **SGA (Self-Grouping Autoencoder without retrieval)**: Avg +2.169%/mo, SR 0.780, FF5 Alpha +1.812% ($p = 0.013$)
- **ReSGA**: Avg **+2.213%/mo**, SR **0.787**, FF5 Alpha **+1.842%** ($p = 0.013$) — **Dominates all competing models across all metrics**.
- **GAS (Econometric)**: Avg +1.621%/mo, SR 0.672, FF5 Alpha +1.217% ($p = 0.051$)
- **GARCH (Econometric)**: Avg +1.395%/mo, SR 0.562, FF5 Alpha +1.012% ($p = 0.128$, insignificant)

### Independently reproduced

Not independently reproduced.

### Negative evidence

The authors report explicit negative transfer results and structural limitations in the published paper:

1. **Cross-Market Transfer Inversion (Table 8 - Source-reported)**:
   When ReSGA trained on US equities is applied zero-shot (without re-estimation) to non-US equity markets, the size-enhanced left-side momentum strategy completely fails or reverses:
   - **China**: H-L return is **-1.417%/mo**, Sharpe **-0.619** (monotonically reversed: P1 = +0.431%, P10 = +1.848%).
   - **Japan**: H-L return is **-0.696%/mo**, Sharpe **-0.543** (reversed: P1 = +0.451%, P10 = +1.146%).
   - **UK**: H-L return is **-6.781%/mo**, Sharpe **-0.586** (P10 yields an anomalous +7.021%/mo due to low-priced small-cap spikes).
   - **Australia**: H-L return is **-4.778%/mo**, Sharpe **-1.553** (P10 yields +5.324%/mo).
   - **Canada**: H-L return is **-3.248%/mo**, Sharpe **-1.191** (P10 yields +3.795%/mo).
   *Author finding*: Tail-risk pricing mechanisms are market-dependent. In retail-dominated or resource-heavy markets, distressed small caps exhibit lottery-like retail buying behavior that destroys the short leg.

2. **Absence of Transaction and Short-Borrow Costs (Provenance gap)**:
   The paper does not account for the substantial cost of shorting P10 small-cap stocks. Because P10 accounts for the bulk of the strategy spread (P10 return is -1.308%/mo while P1 is +0.905%/mo), hard-to-borrow fees, borrow recall risk, and bid-ask bounce in distressed micro-cap equities could significantly erode net alpha.

3. **Absence of Monotonic Model Parameter Scaling (Table 7 - Source-reported)**:
   Scaling model parameters from $10^3$ to $10^7$ does not monotonically improve out-of-sample risk forecasting loss or Sharpe ratios. Only input data complexity (temporal history and cross-sectional pooling) consistently improves risk forecasts.

## Falsification plan

1. **Transaction Cost and Borrow Friction Hurdle**:
   Re-evaluate the monthly H-L decile portfolio after deducting:
   - 10 bps per trade on long P1 stocks;
   - 35 bps per trade on short P10 stocks;
   - An annual borrow fee of 200 bps on short P10 positions.
   *Decision Rule*: If net H-L annualized Sharpe ratio falls below 0.35 or net Fama-French 5-factor alpha becomes statistically insignificant ($p > 0.05$), the strategy is falsified as an un-tradable gross-return artifact (`research-defined falsification threshold`).

2. **Small-Cap Ex-Micro Cap Truncation Audit**:
   Re-run the cross-sectional sort while restricting the universe to stocks with market capitalization above the 20th percentile of NYSE market cap (eliminating micro/nano caps).
   *Decision Rule*: If the H-L monthly average return drops by more than 50% (from 2.213% to below 1.10%/mo) or the short leg P10 fails to generate negative excess returns, the "size-enhanced" mechanism is rejected as an artifact of micro-cap short illiquidity rather than systematic tail risk pricing (`research-defined falsification threshold`).

3. **Size Interaction Ablation Test**:
   Compare the Size-Enhanced Left-Side Momentum signal $\alpha_{i,t}$ directly against:
   - Baseline Left-Side Momentum ($-\widehat{\mathrm{ES}}_{i,t}$ sort);
   - Pure Size sort ($\mathrm{Cap}_{i,t-1}$ sort);
   - Linear combination of size and tail risk without multiplicative interaction.
   *Decision Rule*: If the multiplicative interaction term $\alpha_{i,t}$ fails to deliver a statistically significant incremental alpha ($t$-stat $> 2.0$) over the additive benchmark, the "too-big-to-fail" non-linear interaction hypothesis is rejected (`research-defined falsification threshold`).

4. **Quantile $\tau$ Sensitivity Audit**:
   Re-estimate ReSGA and the signal under alternative quantile levels $\tau \in \{0.01, 0.10, 0.20\}$.
   *Decision Rule*: The H-L portfolio annualized Sharpe ratio must remain $> 0.45$ across $\tau \in [0.01, 0.10]$. If alpha is only present at exactly $\tau = 0.05$, the result is rejected as quantile-overfitted (`research-defined falsification threshold`).

5. **Sub-period Stability & Crisis Breakdown**:
   Examine performance across distinct market regimes within the 2014–2023 evaluation period:
   - Low-volatility expansion (2014–2019);
   - COVID-19 crash and rapid recovery (2020);
   - High inflation / aggressive rate hikes (2022);
   - Mega-cap tech rally (2023).
   *Decision Rule*: If the strategy experiences maximum drawdown $> 30\%$ during the 2020 crash/rebound or delivers negative annual return in more than 3 out of 10 years, the regime-robustness hypothesis is falsified (`research-defined falsification threshold`).

## Crypto portability

**unproven**

The size-enhanced left-side momentum strategy is developed and tested exclusively on monthly US equities. Porting this mechanism to cryptocurrency markets involves substantial structural barriers and is strictly an adapted/unproven research hypothesis:

- **Absence of Sovereign Backstops / Institutional "Too-Big-to-Fail"**: The foundational premise—that mega-cap firms with severe downside risk receive government bailouts, lender restructuring, or systemic safety nets—does not hold in crypto. Even major layer-1 assets, centralized lenders, or top tokens (e.g. LUNA, FTX/FTT) can experience total collapse without sovereign intervention.
- **Perpetual Funding Rate Drag**: In crypto perpetual markets, holding short positions on high-volatility, low-cap tokens (analogous to P10) often incurs severe negative funding costs (shorts pay longs) when speculative short demand crowds into distressed tokens.
- **Extreme Asymmetric Short Tail Risk**: Distressed low-cap crypto tokens frequently experience violent short squeezes (+100% to +500% in days) driven by low float, meme momentum, or aggressive pump-and-dump behavior, which would cause catastrophic drawdowns on the short P10 leg.
- **24/7 Continuous Trading vs. Monthly Rebalancing**: Monthly rebalancing is far too slow for crypto tail events, where insolvency, liquidation cascades, and regime shifts unfold over minutes or hours. An adapted crypto implementation would require daily or 8-hour horizon tail risk forecasting.
- **Data Availability Gaps**: ReSGA relies on 153 fundamental and technical characteristics over long histories (70+ years). Crypto tokens lack standardized multi-decade balance sheets; only on-chain, order book, and price/derivatives features could be utilized.

## Limitations

- **Gross Returns Only**: All reported portfolio figures in the primary source omit transaction costs, exchange fees, market impact, and short borrow rates (`source-reported` gap).
- **Asymmetric Short Leg Dependency**: In Table 6, the short leg (P10) contributes -1.308%/mo, while the long leg (P1) contributes +0.905%/mo. A substantial portion of the strategy's 2.213%/mo return comes from shorting distressed small caps, which is the most friction-heavy segment of the market.
- **Severe Cross-Border Generalizability Failure**: The strategy fails completely when transferred zero-shot to China, Japan, UK, Australia, and Canada (Table 8), proving that the mechanism is heavily dependent on specific US equity market institutions, bankruptcy laws, and investor demographics.
- **Model Training Complexity**: ReSGA requires training a deep autoencoder with dynamic grouping and cross-asset retrieval across 40,000+ stocks and 153 characteristics across century-long rolling panels, incurring heavy GPU compute overhead.
- **Contemporaneous Median Imputation**: Missing characteristics are imputed using contemporaneous cross-sectional medians, which introduces mild cross-sectional look-ahead bias if not implemented with strict point-in-time partitioning.
- **Unverified Crypto Tradability**: Portability to crypto is unproven and subject to severe structural risks (lack of bailouts, violent short squeezes).

## Implementation status

Not implemented.

This is an external strategy research capture from arXiv:2606.04576v1. No implementation has been created in the `alpha-strategy-research` repository, PyBroker, NautilusTrader, or any paper/testnet/live execution environment.

## Adoption boundary

This document is for research purposes only. The inclusion of this strategy record does not constitute:
- Verification of live profitability;
- Approval for quantitative implementation;
- Authorization for paper trading, testnet execution, or live capital allocation.

Any future progression toward implementation would require explicit research review, rigorous transaction cost and short-borrow modeling, independent replication on out-of-sample data (2024–2026), and strict survivorship/micro-cap filtering.

## Related Wiki records

- `taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02.md` — Asymmetric downside tail risk and CVaR measures in equity portfolios.
- `cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md` — Cross-sectional return predictability from graph and topological structure.
- `prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04.md` — Deep learning latent factor discovery for cross-sectional stock ranking.
- `stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04.md` — Graph neural network ranking mechanisms across cross-sectional equity assets.
- `latent-drift-kalman-bucy-macd-optimal-portfolio-2026-09-03.md` — Latent drift estimation and portfolio allocation under non-stationary market regimes.

## Sources

1. **Yichi Zhang, Ke Zhu, and Zhoufan Zhu**. "ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall." *arXiv preprint arXiv:2606.04576v1 [stat.ML]*, June 5, 2026. Available at: https://arxiv.org/abs/2606.04576.
2. **ReSGA Companion Research Site**. "ReSGA Tail Risk Forecasts: Stock-level Value-at-Risk and Expected Shortfall Forecasts." Available at: https://tailrisk-resga.github.io.
3. **ReSGA Open-Source Repository**. "tailrisk-resga.github.io: Model documentation, forecasting scripts, and research materials." Available at: https://github.com/tailrisk-resga/tailrisk-resga.github.io.
4. **Turan G. Atilgan, Turan Bali, K. Ozgur Demirtas, and A. Doruk Gunaydin**. "Left-tail momentum: Underreaction to bad news, costly arbitrage, and equity returns." *Journal of Financial Economics*, 135(3):725–745, 2020. (Foundational reference for left-side momentum baseline).
5. **Tobias Fissler and Johanna F. Ziegel**. "Higher order elicitability and Becker's conjecture." *The Annals of Statistics*, 44(5):2180–2210, 2016. (Foundational reference for joint VaR-ES degree-0 FZ scoring rule).
6. **Theis Ingerslev Jensen, Bryan Kelly, and Lasse Heje Pedersen**. "Is there a replication crisis in finance?" *The Journal of Finance*, 78(5):2465–2518, 2023. (Primary source dataset: JKP 153 firm characteristics panel).
