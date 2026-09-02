---
schema: strategy-research-record-v1
title: "AlphaZeroBeta: Deep Reinforcement Learning with Multi-Objective Reward Shaping and Dollar-Neutral Projection for Market-Neutral Portfolios"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - market-neutral
  - ppo
  - equity-long-short
  - cnn-gru
  - transaction-costs
  - factor-attribution
status: research-only
confidence: high
source_as_of: 2026-07-20
sources:
  - "Boris Belyakov, 'AlphaZeroBeta: Deep Reinforcement Learning for Market-Neutral Portfolios', arXiv:2607.18001v1 [q-fin.PM], July 2026. DOI: 10.48550/arXiv.2607.18001. Stable URL: https://arxiv.org/abs/2607.18001. Accepted for publication in Financial Innovation (Springer)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaZeroBeta: Deep Reinforcement Learning with Multi-Objective Reward Shaping and Dollar-Neutral Projection for Market-Neutral Portfolios

## Provenance

- **Primary Source:** Boris Belyakov, *"AlphaZeroBeta: Deep Reinforcement Learning for Market-Neutral Portfolios"*, arXiv preprint `arXiv:2607.18001v1 [q-fin.PM]`, submitted July 20, 2026.
- **Canonical DOI:** [10.48550/arXiv.2607.18001](https://doi.org/10.48550/arXiv.2607.18001)
- **Traceable Source URL:** `https://arxiv.org/abs/2607.18001` (HTML full text: `https://arxiv.org/html/2607.18001v1`)
- **Publication Status:** Accepted for publication in the peer-reviewed journal *Financial Innovation* (Springer).
- **Author Affiliation & Contact:** Independent quantitative research (`work.belyakov@gmail.com`).
- **Data Vendors & Sources:** Bloomberg Terminal and Financial Modeling Prep (2004–2024 panel).

## Economic mechanism

### Source-reported

Conventional implementations of equity market-neutral (EMN) investing rely on static factor structures (e.g., Fama–French multifactor models or commercial risk models such as MSCI Barra), where asset factor loadings are assumed stationary over estimation windows. However, factor risk models face acute structural breakdowns during regime shifts, such as volatility clustering or the August 2007 quant deleveraging event, where factor-hedged portfolios suffered severe co-movement shocks. In parallel, classical two-step "predict-then-optimize" mean-variance frameworks suffer from estimation error magnification when inverting empirical covariance matrices $\Sigma^{-1}$, yielding extreme, unstable portfolio weights out of sample.

Deep reinforcement learning (DRL) addresses these limitations by casting portfolio construction as a Markov Decision Process (MDP) that maps market states directly to allocation actions. AlphaZeroBeta introduces a framework specifically tailored for market neutrality:
1. It combines a hard dollar-neutral projection ($\sum w_i = 0$, $\|w\|_1 \le 1$) at each rebalance with a soft multi-objective reward function that explicitly penalizes rolling correlation with the benchmark index and portfolio turnover.
2. Rather than relying on factor cancellation alone, the agent learns an intertemporal, state-contingent policy that generates benchmark-relative alpha while continuously driving residual beta toward zero across changing market regimes.

### Research interpretation

The proposed alpha thesis operates as a dynamic cross-sectional equity relative-value strategy regularized against systematic market risk and transaction cost erosion:

1. **Orthogonal Alpha Extraction via Hard Projection:** By centering the raw action vector before $\ell_1$ projection, the portfolio is strictly dollar-neutral by construction ($\sum_{i=1}^N w_i = 0$ and $\sum_{i=1}^N |w_i| \le 1$). However, dollar neutrality alone does not guarantee market-beta neutrality: a book long high-beta growth stocks and short low-beta defensive stocks possesses a substantial positive market beta.
2. **Soft Correlation Regularization as Beta Suppression:** The inclusion of a rolling correlation penalty $-\lambda_1 \operatorname{Corr}(r_p, r_m)$ directly aligns policy optimization with beta minimization. If an allocation tilts into net market beta, the correlation term degrades the reward, training the policy network to identify relative-value pairs whose factor exposures symmetrically offset.
3. **Turnover Regularization as Noise Attenuation:** High-capacity neural policies are prone to overfitting high-frequency microstructure noise, resulting in excessive rebalancing. Internalizing proportional turnover costs via $-\lambda_2 \sum |\Delta w_i|$ forces the agent to filter out transient fluctuations and trade only on persistent cross-sectional momentum and quality divergence signals.
4. **Multi-Horizon Hierarchical Feature Compression:** Multi-scale 1D CNNs extract patterns across daily, weekly, and monthly resampled tensors, feeding into a GRU recurrent core that maintains a low-dimensional state memory across multi-year walk-forward cycles.

## Signal

The trading signal and allocation policy operate as an end-to-end continuous actor-critic control loop:

- **State Representation ($s_t \in \mathcal{S}$):**
  - Multivariate input tensor concatenating daily, weekly, and monthly feature streams with the previous portfolio weight vector $w_t$.
  - Weekly and monthly streams are resampled using end-of-period values and synchronously aligned to the daily close. To prevent look-ahead bias, closed periods are indexed via $(t // k) - 1$.
  - Per-asset feature catalog includes: 5/20/60-day rolling return means and standard deviations; 5/20/60-day volume means and standard deviations; technical indicators (EMA-12, EMA-26, MACD diff, RSI-14, Bollinger Bands-20); one-hot encoded GICS sector vectors; 60-day lagged fundamental balance sheet/income statement ratios; point-in-time earnings surprise revisions; macroeconomic releases (interest rates, CPI, GDP growth); and investor sentiment indicators.
  - All continuous features are standardized to zero mean and unit variance within each rolling training batch, with winsorization thresholds (1st and 99th percentiles) pre-fitted on an initial 2004–2010 warm-up segment.
- **Encoder Architecture:**
  - Hierarchical 1D-CNN: Three 1D convolutional layers across temporal channels with kernel sizes $(8, 4, 3)$, strides $(4, 2, 1)$, and filter depths $(32, 64, 64)$ with ReLU activations, mixing multi-scale horizons.
  - Recurrent Backbone: Gated Recurrent Unit (GRU) with 512 hidden units, tracking non-stationary sequential dependencies.
- **Actor (Policy) and Critic (Value) Heads:**
  - Policy Head: Fully connected layer `Linear(512, 512)` $\to$ ReLU $\to$ `Linear(512, N)` $\to$ `Tanh`, outputting raw continuous actions $a_t \in [-1, 1]^N$.
  - Value Head: Fully connected layer `Linear(512, 512)` $\to$ ReLU $\to$ `Linear(512, 1)`, estimating expected discounted return-to-go $V_\phi(s_t)$.
- **Dollar-Neutral & Exposure Projection:**
  - Center raw action: $w'_{i,t+1} = a_{i,t} - \frac{1}{N}\sum_{j=1}^N a_{j,t}$.
  - Project onto $\ell_1$ unit ball:
    $$w_{t+1} = \frac{w'_{t+1}}{\max\left(1.0, \|w'_{t+1}\|_1\right)}$$
  - Enforces $\sum_{i=1}^N w_{i,t+1} = 0$ (dollar neutrality) and $\sum_{i=1}^N |w_{i,t+1}| \le 1$ (gross leverage $\le 1.0$) at every rebalance.
- **Reward Function ($r_t = \mathcal{R}(s_t, a_t)$):**
  $$r_t = \frac{r_p(t) - r_m(t)}{\max(\sigma_p(t), 10^{-8})} - \lambda_1 \operatorname{Corr}\bigl(r_p(t), r_m(t)\bigr) - \lambda_2 \sum_{i=1}^N |w_i(t) - w_i(t-1)|$$
  - $r_p(t) = \sum_{i=1}^N w_i(t-1) R_{i,t}$: realized portfolio return from $t-1$ to $t$.
  - $r_m(t)$: realized benchmark index return.
  - $\sigma_p(t)$: rolling standard deviation of daily portfolio returns over a trailing $W = 60$ business-day window, computed strictly over historical weights held on $[t-W, t)$.
  - $\operatorname{Corr}(r_p(t), r_m(t))$: Pearson correlation between portfolio and benchmark returns over trailing $W = 60$ days.
  - Regularization hyperparameters: Neutrality penalty $\lambda_1 = 0.5$; turnover penalty $\lambda_2 = 0.001$.
- **Policy Gradient Update (Recurrent PPO):**
  - Generalized Advantage Estimation (GAE): Discount factor $\gamma = 0.99$, trace decay $\lambda_{\text{GAE}} = 0.95$.
  - PPO clipping threshold $\epsilon = 0.20$; value function loss coefficient $c_1 = 0.5$; Adam optimizer learning rate $\eta = 3 \times 10^{-4}$; gradient clipping norm $0.5$; 10 PPO epochs per rollout.
- **Cadence & Execution Timing:** Daily close-to-close convention. Decisions formed at close $t$, orders executed at close $t+1$.

## Required data

- **Universe & Instruments:** Evaluated across 7 major equity indices spanning developed and emerging markets:
  1. S&P 500 (`^GSPC`): 500 large-cap US equities (cap-weighted).
  2. NASDAQ-100 (`^NDX`): 100 tech-heavy US equities (modified cap-weighted).
  3. Dow Jones Industrial Average (`^DJI`): 30 large-cap US blue chips (price-weighted).
  4. FTSE 100 (`^FTSE`): 100 UK blue-chip equities (cap-weighted).
  5. DAX 40 (`^GDAXI`): 40 German industrial and exporter equities (cap-weighted).
  6. Hang Seng Index (`^HSI`): Concentrated Hong Kong / Chinese equities (cap-weighted).
  7. SSE Composite (`000001.SS`): ~2,200 Chinese A-share equities (all listed names, large cross-section).
- **Timeframe & Resolution:** Daily close prices, adjusted for stock splits and dividend distributions, spanning calendar years 2004 to 2024 (20 years).
- **Data Providers:** Bloomberg Terminal and Financial Modeling Prep.
- **Fields Ingested:**
  - Price/Volume: Daily open, high, low, close, volume, free-float shares, average daily dollar volume ($\text{ADV}_{60}$).
  - Fundamentals: Quarterly balance sheets, income statements, cash flows.
  - Sentiment & News: Analyst consensus EPS, earnings surprise revisions, insider transactions, options implied volatility surfaces, structured news sentiment.
  - Macro: Federal funds rate, local sovereign bond yields, CPI, GDP growth, industrial production, unemployment rates, commodity prices (WTI crude, gold), FX rates.
- **Point-in-Time Integrity:**
  - Fundamental data conservatively lagged by 60 calendar days after fiscal period close to prevent reporting look-ahead.
  - Earnings surprise events incorporated on the recorded announcement date; after-close announcements take effect on $t+1$.
  - Macro releases lagged by one full publication cycle where real-time vintages were absent.
  - Winsorization cutoffs (1%, 99%) frozen from the 2004–2010 warm-up segment before out-of-sample deployment.
  - Exchange-specific local trading calendars enforced (no cross-market forward-filling on national holidays).
  - Survivorship handling: Time-varying historical index membership used for `^GSPC`, `^NDX`, `^FTSE`, `^GDAXI`, `^HSI`, and `^DJI`. For `000001.SS`, historical constituent changes were incomplete, so a fixed constituent snapshot as of 2025-02-01 was used (survivorship bias caveat acknowledged).

## Execution assumptions

- **Execution Timing:** Close-to-close rule. Information available up to day $t$ close determines target weights $w_{t+1}$, executed at (or near) the close of $t+1$.
- **Transaction Costs Schedule (Deterministic, Per-Side):**
  - US top-decile $\text{ADV}_{60}$ names (`^GSPC`, `^NDX`, `^DJI`): 5 bps.
  - UK, Germany, and HK top-decile names (`^FTSE`, `^GDAXI`, `^HSI`): 10 bps.
  - Remaining US, UK, and German names: 15 bps.
  - Remaining Hang Seng names: 20 bps.
  - SSE Composite constituents (`000001.SS`): 30 bps.
  - Top-decile thresholds defined by trailing 60-day average dollar volume ($\text{ADV}_{60}$), refreshed monthly.
- **Borrow Fees (Short Leg, Annualized Accrued Daily):**
  - US equities: 30 bps/year.
  - UK / Germany equities: 45 bps/year.
  - Hong Kong equities: 75 bps/year.
  - China A-shares: 120 bps/year.
- **Turnover & Implementation Burden:**
  - Mean realized daily turnover $\sum |\Delta w_i| = 0.56 \pm 0.11$ across markets (95th percentile 0.92).
  - Translates into an estimated daily drag of 8 to 12 bps in active regimes.
  - All reported performance figures are net of transaction costs and borrow fees.

## Evidence

### Source-reported

Empirical results are reported across $K = 22$ non-overlapping 6-month walk-forward out-of-sample test splits from January 2014 through December 2024 (11 years). Each split uses a 36-month training window, 6-month validation window (early stopping), and 6-month test window, advancing in 6-month sliding steps. Models are retrained from scratch at each fold across 9 independent random seeds (198 evaluations per market).

**Table 1: Out-of-Sample Performance Comparison (2014–2024, Net of Costs & Borrow Fees):**

| Universe / Index | Strategy | Annualized Sharpe | Max Drawdown | Benchmark Correlation ($\rho$) |
| :--- | :--- | :--- | :--- | :--- |
| **Cross-Market Mean** | **AlphaZeroBeta** | **1.25 ± 0.30** | Competitive | **Within ±0.15** |
| | Best Convex Baseline | 0.70 ± 0.19 | Mixed | High / Net-Long |
| **S&P 500 (`^GSPC`)** | **AlphaZeroBeta** | **1.61** | Shallow in crashes | **Near Zero** |
| | Index Buy & Hold | ~0.75 | -33.9% (2020) | 1.00 |
| **NASDAQ-100 (`^NDX`)** | **AlphaZeroBeta** | **1.48 ± 0.41** | -32% ± 10% | **0.07 ± 0.06** |
| | Index Buy & Hold | ~0.85 | Deepest in panel | 1.00 |
| **SSE Composite (`000001.SS`)** | **AlphaZeroBeta** | **1.63 ± 0.38** | -34% ± 11% | **-0.02 ± 0.05** |
| | Decorr Baseline | Negative | -31% | ~0.05 |
| **Dow Jones (`^DJI`)** | **AlphaZeroBeta** | **1.20 ± 0.28** | -27% ± 14% | **0.03 ± 0.07** |
| | Index Buy & Hold | ~0.65 | -37% | 1.00 |
| **Hang Seng (`^HSI`)** | **AlphaZeroBeta** | **1.04 ± 0.33** | -21% ± 22% | **0.01 ± 0.04** |
| | Index Buy & Hold | Flat (~0.00) | Prolonged selloff | 1.00 |
| **FTSE 100 (`^FTSE`)** | **AlphaZeroBeta** | **0.94 ± 0.19** | -28% ± 9% | **-0.02 ± 0.08** |
| | Index Buy & Hold | ~0.40 | -34% | 1.00 |
| **DAX 40 (`^GDAXI`)** | **AlphaZeroBeta** | **0.86 ± 0.23** | **-16% ± 11%** (Best DD) | **0.05 ± 0.04** |
| | MxSharpe Baseline | 0.11 | -38% | Net-long |

**Factor Attribution & Risk Decomposition (Table 5 in source):**
- Excess returns regressed on MKT, SMB, HML, RMW, MOM, REV, and QUAL across 6 markets:
  - Market Beta ($\beta_{\text{MKT}}$): Statistically indistinguishable from zero across all regions ($p > 0.10$), confirming empirical dollar- and beta-neutrality.
  - Momentum ($\beta_{\text{MOM}}$): Positive and statistically significant ($p < 0.01$) across all 6 markets, indicating consistent exploitation of medium-term cross-sectional trend.
  - Short-Term Reversal ($\beta_{\text{REV}}$): Negative and statistically significant ($p < 0.01$), confirming avoidance of fast, high-friction mean reversion.
  - Intercepts ($\alpha$): Statistically positive at $p < 0.01$ across all markets, representing benchmark-relative abnormal return.
- Permutation Feature Importance: Shuffling feature blocks within test windows reduced Sharpe by 37% (price/momentum), 18% (volatility/regime), 12% (macro/cross-asset), and 9% (sentiment/flows).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Binary Ablation on Neutrality Penalty ($\lambda_1 = 0$):** Removing the benchmark correlation penalty while keeping turnover penalty active caused benchmark correlation to surge into the $0.40 \text{--} 0.60$ range. Maximum drawdowns deepened by 7 to 20 percentage points across indices, and annualized Sharpe dropped in every single market. This confirms that unconstrained DRL does not naturally achieve market neutrality; explicit reward shaping is indispensable.
- **Drawdown Underperformance Relative to Long-Biased Baselines:** While AlphaZeroBeta achieved superior risk-adjusted return and shallower drawdowns than Buy & Hold, the convex optimization baselines (MxSharpe and Decorr) achieved shallower maximum drawdowns in 6 of the 7 markets. AlphaZeroBeta achieved the lowest drawdown only on the DAX (-16%).
- **Turnover Sensitivity:** The policy generates substantial daily turnover ($0.56$ fraction of capital per day). If applied to small-cap, illiquid, or high-spread equities where transaction costs exceed 30 bps, the 8–12 bps daily drag would eliminate net excess return.
- **Survivorship Bias in Chinese A-Shares:** Historical constituent history was unavailable for the SSE Composite; using a fixed February 2025 constituent snapshot introduces survivorship bias into the reported $1.63$ Sharpe for `000001.SS`.
- **Proprietary Code & Data Dependency:** Data collection relies on proprietary Bloomberg Terminal and Financial Modeling Prep APIs, precluding open-source turn-key verification.

## Falsification plan

1. **Transaction Cost Haircut Stress Test:** Double the deterministic transaction cost schedule (e.g., 10 bps for US top-decile, 30 bps for general US/UK, 60 bps for SSE). If net annualized Sharpe ratio drops below $0.50$ across the 7 indices, the economic viability of the learned policy after institutional execution frictions is falsified.
2. **Dynamic Beta Crash Test:** Evaluate realized 20-day rolling market beta during acute historical shock windows (August 2015 China devaluation, March 2020 COVID crash, 2022 rate hikes). If rolling $|\beta_{\text{MKT}}| > 0.25$ or correlation with benchmark breaches $|\rho| > 0.35$ for more than 5 consecutive days, the hypothesis that AlphaZeroBeta sustains market neutrality across structural breaks is rejected.
3. **Linear Model Ablation:** Train a regularized linear Ridge/ElasticNet policy directly optimizing the dollar-neutral Sharpe ratio on the identical feature catalog. If the linear benchmark achieves within 0.15 Sharpe of the deep CNN-GRU network out of sample, the necessity of deep recurrent reinforcement learning is falsified.
4. **Permuted Cross-Sectional Label Test:** Randomly shuffle asset identifier tags across the cross-section prior to CNN-GRU feature extraction while preserving time series order. If the policy achieves an out-of-sample Sharpe $> 0.30$, the signal is driven by structural look-ahead or reward leakage rather than genuine firm-specific alpha.
5. **Failure Action:** If net Sharpe ratio over a 3-year out-of-sample rolling period is $< 0.40$ or rolling benchmark correlation exceeds $0.20$, the model is rejected from strategy development pipelines.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Rationale:** The core mechanics—extracting multi-horizon technical and sentiment features, applying dollar-neutral action projections ($\sum w_i = 0$), and penalizing correlation against the market benchmark—can be ported to cryptocurrency perpetual futures (e.g., top 50–100 altcoins on Binance or Bybit against BTC/ETH).
- **Crypto-Specific Impediments & Hazards:**
  1. **Extreme Market Beta Dominance:** In equities, the market factor accounts for 30–50% of cross-sectional variance. In crypto, Bitcoin beta accounts for 75–85% of altcoin variance. Stripping BTC beta leaves narrow idiosyncratic variance, increasing sensitivity to factor estimation noise.
  2. **Funding Rate Carry Asymmetry:** Crypto perpetual futures charge funding fees every 8 hours. Altcoins with strong positive momentum often trade at massive funding premiums (20–100% APR). A dollar-neutral book holding long momentum and short reversal/low-beta could experience severe funding bleed that overwhelms relative-value alpha.
  3. **24/7 Liquidation Cascades:** Equity markets operate on discrete session closes. Crypto trades continuously, and severe deleveraging cascades break statistical correlations as margin engines liquidate altcoins simultaneously, driving cross-asset correlation toward 1.0.
  4. **Survivorship and Rapid Listing Turnover:** Rapid delistings, token migrations, and liquidity fragmentation violate stationary universe assumptions.

## Limitations

- **Not Independently Reproduced:** All performance figures and regression statistics are third-party empirical findings from Boris Belyakov (arXiv:2607.18001v1).
- **Survivorship Bias in SSE Composite:** Data limitations required a static February 2025 constituent snapshot for China A-shares.
- **Simplified Slippage Model:** Backtests employ a fixed basis-point cost schedule; real-world market impact on large sizes is unmodeled.
- **Compute Requirements:** Full training requires server-class GPU infrastructure (approx. 12 days on 8x A100 for 22 walk-forward folds across 9 seeds).

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, or production live execution environments has been completed.

## Adoption boundary

`research-only`. This document constitutes normalized research material. It does not authorize capital deployment, implementation into execution engines, paper trading, testnet verification, or live trading.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]`
- `[[quant/phase8-temporal-validation-calibration-uncertainty-2026-08-28]]`
- `[[quant/phase9-multifactor-portfolio-attribution-cost-handoff-2026-08-28]]`
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]`

## Sources

- Boris Belyakov, *"AlphaZeroBeta: Deep Reinforcement Learning for Market-Neutral Portfolios"*, arXiv preprint `arXiv:2607.18001v1 [q-fin.PM]`, submitted July 20, 2026. DOI: [10.48550/arXiv.2607.18001](https://doi.org/10.48550/arXiv.2607.18001). Stable URL: `https://arxiv.org/abs/2607.18001`. Accepted for publication in *Financial Innovation* (Springer).
