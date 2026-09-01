---
schema: strategy-research-record-v1
title: Option-Implied Volatility Surface Signals, Skewness, and Regime-Dependent Crash Predictability
created: 2026-09-02T07:30:00Z
updated: 2026-09-02T07:30:00Z
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - implied-volatility
  - volatility-surface
  - crash-risk
  - cross-sectional-equity
status: research-only
confidence: medium
source_as_of: 2026-08-28T00:00:00Z
sources:
  - "Li, B., & Wang, M. (2026). Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015–2026. arXiv:2608.26115 [q-fin.ST, q-fin.PR]. https://arxiv.org/abs/2608.26115"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Option-Implied Volatility Surface Signals, Skewness, and Regime-Dependent Crash Predictability

## Provenance

- Canonical source identity: arXiv:2608.26115 (`https://arxiv.org/abs/2608.26115`, `https://arxiv.org/html/2608.26115v1`).
- Authors: Baichuan Li and Mengxiao Wang.
- Primary paper title: *Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015–2026*.
- License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Data sample span: 2015–2026 panel comprising 12.36 million firm-day observations across 10,026 underlyings.
- Regime segmentation:
  1. Late-post-crisis low-volatility baseline: 2015–2019
  2. High-volatility transition (COVID & rate shocks): 2020–2022
  3. AI / mega-cap concentration regime: 2023–2026

## Economic mechanism

### Source-reported
Option markets reflect informed trading demand, hedging pressure, and non-linear payoff expectations prior to their full impoundment into underlying cash equities. However, the transmission mechanism has undergone structural shifts due to massive growth in retail option trading (0DTE options, meme stocks) and mega-cap concentration:
1. **Smirk Decay**: The canonical Xing, Zhang, and Zhao (2010) volatility smirk signal ($\text{IV}_{\text{OTMP}} - \text{IV}_{\text{ATM}}$)—hypothesized to reflect informed traders buying out-of-the-money puts ahead of bad news—has decayed and inverted. Demand pressure from structural retail tail-hedging and systematic volatility selling has diluted the information content of put smirks.
2. **Cremers–Weinbaum IV Spread & Risk-Neutral Skewness Persistence**: The Cremers and Weinbaum (2010) call-minus-put IV spread ($\text{IV}_{\text{call}} - \text{IV}_{\text{put}}$) and the Bakshi, Kapadia, and Madan (2003) model-free risk-neutral skewness proxy isolate directional informed order flow and higher-moment risk premia that remain robustly predictive across regimes.
3. **Non-Linear Regime-Dependent ML Alpha**: In the post-2023 AI/mega-cap regime, non-linear interactions between OTM call implied volatility, open-interest-weighted gamma/vega, and liquidity dynamics create distinct return predictability ($R^2_{\text{OOS}} = +1.29\%$) that linear models fail to capture.

### Research interpretation
The strategy captures cross-sectional equity return predictability and crash risk premia by constructing a multi-feature option-implied ranking signal:
- **Directional Alpha**: Long stocks with high call-vs-put IV spreads (informed bullish flow) and high risk-neutral skewness; short stocks with low IV spreads and extreme negative skewness.
- **Tail Risk Filter**: Machine-learning crash classifier predicting 5-day large downside moves ($>3\sigma$ return drop) conditioned on market volatility regimes, hedging out names with elevated crash probability during calm regimes where crash predictability is highest (AUC $0.706$).

## Signal

1. **Feature Extraction from Daily Implied Volatility Surface**:
   - **IV Spread ($\text{IVS}_{i,t}$)**: Difference between at-the-money call IV and put IV matched by strike and maturity:
     $$\text{IVS}_{i,t} = \text{IV}_{i,t}^{\text{ATM, Call}} - \text{IV}_{i,t}^{\text{ATM, Put}}$$
   - **Risk-Neutral Skewness ($\text{SKEW}_{i,t}^{\mathbb{Q}}$)**: Model-free risk-neutral skewness computed from the integration of the full out-of-the-money call and put strike curve (Bakshi et al., 2003).
   - **Smirk ($\text{SMIRK}_{i,t}$)**: $\text{IV}_{i,t}^{\text{OTMP}} - \text{IV}_{i,t}^{\text{ATM}}$ (retained for regime diagnostic, but excluded from primary directional weights due to demonstrated post-2020 decay).
   - **Open-Interest Greeks**: OI-weighted Delta, Gamma, Vega, Charm, and Vanna across all active options chains for underlying $i$.
   - **Trading Activity Signals**: Total contract volume, Put-Call volume ratio, Put-Call open interest ratio.

2. **Cross-Sectional Factor Model & XGBoost Ranker**:
   - Predict next-month forward stock return $R_{i,t+1:t+21}$ and 5-day crash indicator $C_{i,t:t+5} = \mathbb{I}_{\{R_{i,t:t+5} \le -10\%\}}$ using an XGBoost model trained on rolling 36-month windows.
   - Target prediction score: $\hat{s}_{i,t} = \hat{R}_{i,t}^{\text{XGB}} - \lambda_{\text{crash}} \cdot \hat{P}_{i,t}^{\text{Crash}}$.

3. **Portfolio Construction**:
   - **Long Quintile**: Top 20% of $\hat{s}_{i,t}$ with crash probability $\hat{P}_{i,t}^{\text{Crash}} \le \theta_{\text{crash}}$.
   - **Short Quintile**: Bottom 20% of $\hat{s}_{i,t}$.
   - Dollar-neutral market weighting, rebalanced monthly (21-day holding horizon) with weekly overlap smoothing.

## Required data

- **Universe**: US equity options panel (~10,000 underlyings from OptionMetrics IvyDB / CBOE).
- **Option Metrics**: Standardized 30-day, 60-day, 91-day implied volatility surface (interpolated by delta: 10d, 20d, 50d call/put), open interest, trading volume, implied Greeks.
- **Equity Cash Data**: Daily CRSP/Compustat equity prices, volume, market capitalization, shares outstanding.
- **Liquidity Filters**: Underlying stock price $\ge \$5$; daily option trading volume $\ge 50$ contracts; open interest $\ge 100$; valid bid-ask quotes with non-zero bid.
- **Point-in-Time Alignment**: Option surface measured at market close ($t$); forward returns measured from $t+1$ close.

## Execution assumptions

- **Rebalance Frequency**: Monthly (21 trading days) holding period.
- **Execution Timing**: Positions established at $t+1$ market close.
- **Transaction Costs & Spread Drag**: Assumes standard equity execution costs (5 bps one-way for large-caps, 15 bps for small/mid-caps). Note that trading the underlying stock cash leg avoids crossing the wider option bid-ask spreads.
- **Short Selling**: Requires active equity borrow; hard-to-borrow names with extreme short interest/put skew filtered out.

## Evidence

### Source-reported
- **Dataset**: 12.36 million firm-day observations across 10,026 US equities over 2015–2026.
- **Canonical Smirk Empirical Breakdown**:
  - Univariate next-month return coefficient for Xing et al. smirk fell from $-0.023$ ($t = -5.5$) in 2015–2019 to an insignificant $-0.006$ ($t = -1.5$) in 2023–2026.
  - At 3-month horizon, smirk coefficient reversed sign to $+0.016$ ($t = +2.1$) in the 2023–2026 regime.
  - In multivariate panel regressions controlling for all canonical option signals, smirk is statistically insignificant across all regimes.
- **Persistent Canonical Signals**:
  - **Cremers–Weinbaum IV spread**: Consistently positive and statistically significant ($p < 0.01$) across all three regimes (2015–2019, 2020–2022, 2023–2026).
  - **Bakshi et al. Risk-Neutral Skewness**: Robustly predictive of cross-sectional returns across regimes.
- **Machine Learning (XGBoost) Out-of-Sample Performance**:
  - Return prediction: $R^2_{\text{OOS}} = +1.29\%$ in the AI/mega-cap regime (2023–2026) vs. $+0.07\%$ for linear panel models.
  - In high-volatility transition regime (2020–2022), XGBoost $R^2_{\text{OOS}}$ degraded, reflecting severe macro distribution shifts.
  - Permutation feature importance: Leading predictors shift completely by regime. No canonical hand-engineered signal ranks in the top 5 during the 2023–2026 regime; OTM call IV and OI-weighted Greeks dominate.
- **Crash-Risk Classification**:
  - Calm/low-volatility regime (2015–2019): XGBoost achieves **AUC of 0.706** for 5-day firm crash classification.
  - Crisis/high-volatility regime (2020–2022): Crash prediction AUC drops to **0.561** (near random), demonstrating that idiosyncratic tail risk forecasting collapses during systemic market shocks.

### Independently reproduced
- Not independently reproduced.

### Negative evidence
- The canonical volatility smirk (Xing et al., 2010) is economically and statistically broken in the modern (post-2020) market environment. Strategies relying on plain put smirk signals without IV spread confirmation suffer negative/inverted performance.
- Crash prediction models provide zero predictive utility during macro crisis periods (AUC drops to 0.561), failing precisely when tail hedging is most demanded at the aggregate market level.
- Linear multi-factor models fail completely in the mega-cap/AI concentration regime ($R^2_{\text{OOS}} \approx 0.07\%$).

## Falsification plan

1. **Smirk Sign Inversion Audit**: Backtest isolated 1-month and 3-month long/short smirk quintile portfolios from 2020 to 2026 to verify whether standalone smirk generates negative alpha.
2. **IV Spread Cost-Netting Test**: Deduct actual stock borrow fees on the short quintile to determine if Cremers–Weinbaum IV spread alpha survives short-sale frictions in high-borrow-fee equities.
3. **Regime-Conditional Crash Gate Test**: Evaluate whether disabling the crash prediction filter during VIX $>25$ regimes improves total portfolio Sharpe ratio by avoiding false-positive liquidation of high-rebound candidates.
4. **0DTE Volume Contamination Test**: Exclude options contracts with expiration $< 5$ days to verify whether implied volatility surface signals are distorted by ultra-short-dated retail option trading volume.

## Crypto portability

- **Portability status**: Adapted / unproven.
- **Portability rationale**:
  - Deribit and Binance provide full implied volatility surfaces for BTC, ETH, and major altcoin options.
  - Crypto option markets exhibit pronounced volatility smiles and extreme skew (call skew during bull runs, heavy put skew during liquidation events).
  - Adapting Cremers–Weinbaum IV spread and Bakshi risk-neutral skewness to crypto:
    - Cross-sectional universe is limited (only BTC, ETH, SOL, XRP, and a few high-cap tokens have liquid options).
    - Time-series application: Computing 30-day BTC/ETH risk-neutral skewness and call-put IV spreads to forecast directional spot moves and funding rate dynamics.
    - Inverse contract quoting (options settled in BTC/ETH rather than USD/USDT) introduces non-linear margin currency effects and skew deformation that require smile adjustment.

## Limitations

- **Coverage Limitation**: Option-implied signals are only computable for equities with actively traded option chains (~3,000 of ~10,000 public firms).
- **Regime Fragility**: Machine learning models and crash risk classifiers exhibit severe degradation during macroeconomic regime transitions (e.g., 2020 COVID shock).
- **Decayed Canonical Signals**: Standard textbook signals (Xing et al. smirk) cannot be deployed in naive unadjusted forms.
- **Option Surface Noise**: Illiquidity in deep OTM strikes can distort numerical integration of risk-neutral skewness moments.

## Implementation status

- Not implemented in local research stack (`not-implemented`).
- No NautilusTrader or PyBroker execution actors configured.

## Adoption boundary

- Research-only capture.
- Not approved for paper, testnet, or live trading execution.

## Related Wiki records

- `[[quant/bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]`
- `[[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[quant/options-physical-crash-frontier-socp-finite-quotes-2026-09-02]]`
- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`

## Sources

- Li, B., & Wang, M. (2026). *Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015–2026*. arXiv preprint arXiv:2608.26115 [q-fin.ST, q-fin.PR]. https://arxiv.org/abs/2608.26115
- Bakshi, G., Kapadia, N., & Madan, D. (2003). Stock return characteristics: What does the option market tell us?. *The Review of Financial Studies*, 16(1), 101–143.
- Cremers, M., & Weinbaum, D. (2010). Deviations from put-call parity and stock return predictability. *Journal of Financial and Quantitative Analysis*, 45(2), 335–367.
- Xing, Y., Zhang, X. F., & Zhao, R. (2010). What does the individual option volatility smirk tell us about future equity returns?. *Journal of Financial and Quantitative Analysis*, 45(3), 641–662.
