---
schema: strategy-research-record-v1
title: "Asymmetric Long-Memory GARCH: Sign-Dependent Kernel Injection and Dual-Channel Volatility Decomposition"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volatility-forecasting
  - long-memory
  - garch
  - asymmetric-volatility
  - markov-chain
  - bitcoin
status: research-only
confidence: medium
source_as_of: 2026-09-10
sources:
  - "https://arxiv.org/abs/2609.06422"
  - "https://arxiv.org/html/2609.06422v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Asymmetric Long-Memory GARCH: Sign-Dependent Kernel Injection and Dual-Channel Volatility Decomposition

## Provenance

- **Primary Source:** Kennedy Titus Kayaki and Kyungsub Lee (Department of Statistics, Yeungnam University, Gyeongsan, Republic of Korea).
- **Article Title:** *Asymmetric Long-Memory GARCH: Sign-Dependent Kernel Injection in a Two-Dimensional Markov Chain*.
- **Canonical Identifier / URL:** arXiv:2609.06422v1 [q-fin.ST] (submitted 10 September 2026), full HTML text verified at `https://arxiv.org/html/2609.06422v1`.
- **Predecessor Base Model:** Lee and Kayaki (2026), *Long-memory GARCH via a two-dimensional Markov chain*, arXiv:2607.25189 [q-fin.ST].
- **Sample Period (Source-Reported):**
  - **Equity Indices:** January 2000 – June 27, 2018 (Oxford-Man Institute Realized Library; S&P 500 $N=4,641$, FTSE 100 $N=4,660$, DAX $N=4,692$, Nikkei 225 $N=4,501$, KOSPI $N=4,550$). Daily open-to-close returns and 5-minute realized variance.
  - **Cryptocurrency (Bitcoin):** January 2, 2012 – January 6, 2025 ($N=4,754$ daily observations, Bitstamp 1-minute prices aggregated to UTC close-to-close returns and daily sum of 1,439 squared 1-minute log returns for realized variance target).
- **Evaluation Paradigm:** Gaussian quasi-maximum likelihood estimation; likelihood-ratio tests calibrated with finite-sample parametric and symmetrized-residual bootstraps ($B=999$, $B=3,999$ for DAX memory); out-of-sample QLIKE forecast comparison on final 30% sample holdout with expanding-window re-estimation every 250 days.

## Economic mechanism

### Source-reported

1. **Dual Empirical Volatility Regularities:** Financial asset returns exhibit two distinct, persistent stylized facts:
   - *Long-memory persistence:* Return volatility autocorrelations decay hyperbolically rather than exponentially.
   - *Sign-dependent asymmetry (leverage effect):* Negative returns elevate subsequent volatility by more than positive returns of identical magnitude.
2. **Structural Decomposition of Asymmetry:** Conventional long-memory models (e.g., FIGARCH, FIEGARCH, FIAPARCH) require infinite-order lag truncations ($\text{ARCH}(\infty)$) or assume fractional differentiation orders common across return signs. ALM-GARCH instead constructs a finite-dimensional, two-state Markov chain $(X_n, c_n)$ where $X_n$ represents the accumulated variance level and $c_n$ represents an effective kernel age (memory carrier). Upon receiving a shock $\eta_n = \sigma_n \varepsilon_n$ with sign $s = \operatorname{sgn}(\eta_n) \in \{+, -\}$, the model injects a power-law kernel with sign-specific properties:
   - **Level Channel (Injection Amplitude):** Positive shocks inject amplitude $\xi_+$, while negative shocks inject $\xi_- = \xi_+(1 + \delta)$ with $\delta > 0$. This captures the immediate variance impact disparity (the standard leverage effect).
   - **Memory Channel (Kernel Offset / Reset Age):** Shocks reset the memory carrier toward sign-specific offset $\gamma_s$. Because one-step persistence is $\rho_s = (\gamma_s / (\gamma_s + \tau))^p$, differing offsets create asymmetric finite-horizon decay profiles without altering the asymptotic power-law decay exponent $p$.
3. **Ergodic Stability Frontier:** Under a Foster-Lyapunov drift condition on test function $V(x, c) = \log(1 + x) + \lambda c$, the two-dimensional chain $(X_n, c_n)$ is positive Harris recurrent with a unique invariant probability measure. Theoretically, positive level asymmetry ($\delta > 0$) moves the diagnostic stability boundary inward (locally destabilizing), while a harder negative-shock reset ($\gamma_- < \gamma_+$) moves it outward (stabilizing).

### Research interpretation

- The structural insight of ALM-GARCH is separating *how hard* a shock hits future volatility ($\xi_s$, level channel) from *how long* its impact persists across finite trading horizons ($\gamma_s / \rho_s$, memory channel).
- In crypto markets (specifically Bitcoin), the empirical estimates reveal a striking structural inversion: while negative shocks inject 2.2 times more initial variance than positive shocks ($\hat{\xi}_- = 0.2589$ vs $\hat{\xi}_+ = 0.1173$), positive shocks exhibit significantly longer finite-horizon persistence ($\hat{\rho}_+ = 0.875$ vs $\hat{\rho}_- = 0.528$). Bad news produces violent, short-lived volatility spikes that mean-revert rapidly, whereas upside crypto runs generate persistent, multi-week volatility elevation.
- For systematic quantitative strategies, ALM-GARCH provides an explicit, recursive filter for dynamic volatility targeting, variance-swap pricing, and regime gating without requiring infinite-history storage or latent regime switches.

## Signal

### Mathematical Specification (Source-Reported)

1. **Conditional Variance Formulation:**
   The conditional return process is specified as:
   $$r_n = \sigma_n \varepsilon_n, \quad \sigma_n^2 = \mu + X_{n-1}$$
   where $\mu > 0$ is the baseline variance intercept, $\sigma_n^2$ is $\mathcal{F}_{n-1}$-measurable (predictable), and $\varepsilon_n \sim \text{i.i.d.}(0, 1)$ with symmetric density around zero.

2. **Two-Dimensional Markov State Recursion:**
   Given return shock $\eta_n = r_n = \sigma_n \varepsilon_n$ and its sign $s_n = \operatorname{sgn}(\eta_n) \in \{+, -\}$:
   $$X_n = \rho(c_{n-1}) X_{n-1} + \xi_{s_n} \eta_n^2$$
   $$c_n = \frac{\rho(c_{n-1}) X_{n-1} + \xi_{s_n} \eta_n^2}{\frac{\rho(c_{n-1})}{r(c_{n-1})} \frac{X_{n-1}}{c_{n-1}} + \frac{\xi_{s_n}}{\gamma_{s_n}} \eta_n^2}$$
   where:
   - Time increment: $\tau = 1.0$ (source-reported for daily sampling).
   - Aging ratio: $r(c) = (1 + \tau / c)^{-1}$.
   - One-step persistence function: $\rho(c) = r(c)^p = (c / (c + \tau))^p$.
   - Memory exponent: $p = 1.2$ fixed by identification normalization (source-reported; verified robust against $p = 2.0$).
   - Injected amplitude: $\xi_+ > 0$ if $\eta_n \ge 0$, and $\xi_- = \xi_+(1 + \delta) > 0$ if $\eta_n < 0$.
   - Injected offset: $\gamma_+ > 0$ if $\eta_n \ge 0$, and $\gamma_- > 0$ if $\eta_n < 0$.
   - Persistence summary: $\rho_+ = (\gamma_+ / (\gamma_+ + \tau))^p$ and $\rho_- = (\gamma_- / (\gamma_- + \tau))^p$.

### Operational Trading Overlay Construction (`research-proposed`)

Because the primary source derives an econometric conditional variance filter rather than an automated order-generation system, any execution strategy deploying ALM-GARCH requires research-proposed rules:

- **Signal Formation Timestamp (`research-proposed`):** Evaluated daily at UTC 00:00:00 upon closure of bar $n-1$, updating $(X_{n-1}, c_{n-1})$ and generating conditional variance forecast $\hat{\sigma}_n^2 = \mu + X_{n-1}$ for the upcoming day $n$.
- **Volatility-Targeted Sizing Signal (`research-proposed`):**
  For an underlying long-only or trend-following portfolio targeting annual volatility $\sigma_{\text{target}} = 0.40$ (40% annualized):
  $$w_n = \operatorname{clip}\left(\frac{\sigma_{\text{target}}}{\hat{\sigma}_n \sqrt{365}}, \, w_{\min}, \, w_{\max}\right)$$
  with allocation bounds $w_{\min} = 0.10$ and $w_{\max} = 1.50$.
- **Asymmetric Volatility Regime Gating (`research-proposed`):**
  - *Calm Expansion Regime ($s_n = +$, $c_{n-1} \gg \gamma_-$):* Low immediate injection with high persistence $\rho_+$; maintain standard trend exposure.
  - *Panic Flush Regime ($s_n = -$, large $\eta_n^2$):* High immediate variance shock $\xi_- \eta_n^2$; scale down gross leverage immediately by factor $\hat{\sigma}_{n-1} / \hat{\sigma}_n$.
  - *Rapid Mean-Reversion Recovery:* Because $\hat{\rho}_- \approx 0.528$, variance decay from negative shocks is swift (half-life $\approx \ln(0.5) / \ln(0.528) \approx 1.09$ days), allowing re-leveraging within 2–3 trading sessions compared to standard symmetric models which stay defensive for weeks.

### Key Parameters

| Parameter | Type | Source-Reported Value (Bitcoin Fit) | Notes / Provenance |
|---|---|---|---|
| $p$ (Memory Exponent) | Source-Reported (Fixed) | $1.2$ | Normalization for identification; $p=2.0$ tested in Section 4.7 |
| $\tau$ (Time Step) | Source-Reported | $1.0$ | Daily calendar bar increment |
| $\hat{\mu}$ (Base Variance) | Source-Reported | $3.33 \times 10^{-4}$ | Maximized Gaussian quasi-likelihood estimate |
| $\hat{\xi}_+$ (Positive Amplitude) | Source-Reported | $0.1173 \pm 0.027$ | Sandwich-robust standard error in parentheses |
| $\hat{\xi}_-$ (Negative Amplitude) | Source-Reported | $0.2589 \pm 0.062$ | Amplitude leverage ratio $\hat{\xi}_- / \hat{\xi}_+ \approx 2.21$ |
| $\hat{\rho}_+$ (Positive Persistence) | Source-Reported | $0.875 \pm 0.077$ | One-step persistence ratio for positive returns |
| $\hat{\rho}_-$ (Negative Persistence) | Source-Reported | $0.528 \pm 0.060$ | One-step persistence ratio for negative returns |
| $\hat{\gamma}_+$ (Positive Offset) | Source-Reported | $8.5$ | Derived offset parameter |
| $\sigma_{\text{target}}$ | Research-Proposed | $0.40$ (40% ann.) | Proposed portfolio risk-targeting parameter |
| $w_{\min}, w_{\max}$ | Research-Proposed | $0.10, 1.50$ | Leverage constraint clamp |

## Required data

- **Instruments:** Bitcoin spot or perpetual contract (BTC/USD or BTC/USDT), alongside major equity indices (S&P 500, FTSE 100, DAX, Nikkei 225, KOSPI) for cross-market calibration.
- **Venues:** Bitstamp (primary source for BTC), Oxford-Man Institute Realized Library (equities).
- **Timeframe / Sampling:** Daily frequency ($\tau = 1.0$). Daily close-to-close returns for returns estimation; 1-minute intraday prices for realized variance benchmarking ($1,439$ intraday squared returns per UTC day).
- **Fields Required:** Daily close prices ($P_n$), logarithmic returns $r_n = \ln(P_n / P_{n-1})$, and optionally intraday 1-minute high-frequency bars for realized variance calculation.
- **Point-in-Time Availability:** Daily return $r_n$ is computed at UTC midnight; $\sigma_{n+1}^2$ is predictable using state $(X_n, c_n)$ formed strictly on information available up to bar $n$. No look-ahead bias in recursive updates.
- **Missing Data Handling (Source-Reported):** For Bitcoin on the 1-minute grid, missing minutes carry forward previous close, contributing zero one-minute return.

## Execution assumptions

### Source-Reported Framework

- The primary source is an econometric model and volatility forecasting study; it does **not** simulate automated order executions or portfolio PnL curves. Execution costs, maker/taker fees, and slippage were not modeled by the source.

### Operational Trading Layer Assumptions (`research-proposed`)

- **Execution Timing (`research-proposed`):** Daily rebalance executed at UTC 00:01:00 via TWAP or VWAP over 5 minutes following daily bar closure.
- **Order Types (`research-proposed`):** Passive limit orders (maker) where feasible; IOC market orders for risk-reduction deleveraging during sudden volatility expansions.
- **Fee Model (`research-proposed`):** Tier-1 perpetual exchange fee structure: 2.0 bps maker, 5.0 bps taker.
- **Slippage & Impact Model (`research-proposed`):** Modeled as 3.0 bps for trade sizes under 1.0% of 5-minute pool turnover; liquidity-capped participation rate $\le 2.5\%$ of daily volume.
- **Funding Cost Treatment (`research-proposed`):** Perpetual funding rate accounted as continuous carry cost on net delta positions.

## Evidence

### Source-reported

All quantitative figures below trace directly to Tables 1–7 and Tables S1–S14 in arXiv:2609.06422v1:

1. **Hypothesis Testing on Asymmetry Channels (Table 2 & Table 3):**
   - **Joint Symmetry Test ($LR_{\mathrm{sym}}$):** The joint null $H_0: \xi_+ = \xi_- \text{ and } \gamma_+ = \gamma_-$ is rejected across all 6 markets ($p < 0.001$; bootstrap $p_{\mathrm{boot}} = 0.001$ for all assets; residual bootstrap $p_{\mathrm{boot}}^{\mathrm{res}} \le 0.035$).
     - Bitcoin observed $LR_{\mathrm{sym}} = 25.83$ ($p_{\mathrm{boot}} = 0.001$, $p_{\mathrm{boot}}^{\mathrm{res}} = 0.027$).
     - S&P 500 $LR_{\mathrm{sym}} = 187.09$, FTSE 100 $LR_{\mathrm{sym}} = 210.87$, DAX $LR_{\mathrm{sym}} = 157.66$, Nikkei 225 $LR_{\mathrm{sym}} = 38.38$, KOSPI $LR_{\mathrm{sym}} = 49.86$.
   - **Level Channel Test ($LR_{\mathrm{lev}}$):** The restriction $\xi_+ = \xi_-$ is rejected in all 6 markets ($p < 0.001$ throughout).
     - Bitcoin observed $LR_{\mathrm{lev}} = 16.62$ ($p_{\mathrm{boot}} = 0.001$, $p_{\mathrm{boot}}^{\mathrm{res}} = 0.035$).
   - **Memory Channel Test ($LR_{\mathrm{mem}}$):** The restriction $\gamma_+ = \gamma_-$ is rejected in Nikkei 225 ($LR = 15.01, p_{\mathrm{boot}} = 0.001$), KOSPI ($LR = 26.08, p_{\mathrm{boot}} = 0.001$), and Bitcoin ($LR = 24.82, p_{\mathrm{boot}} = 0.001, p_{\mathrm{boot}}^{\mathrm{res}} = 0.011$).
     - Crucially, the memory restriction is **not** rejected for DAX at the 5% level ($LR = 7.23, p_{\mathrm{boot}} = 0.066, p_{\mathrm{boot}}^{\mathrm{res}} = 0.141$).
     - For S&P 500 ($LR = 0.15, p_{\mathrm{boot}} = 0.853$) and FTSE 100 ($LR = 0.95, p_{\mathrm{boot}} = 0.573$), positive branch amplitude is nearly zero ($\hat{\xi}_+ \approx 0$), making the positive memory offset weakly identified rather than structurally equal.

2. **In-Sample Fit and Comparison (Tables 4 & 5):**
   - Gaussian quasi-log-likelihood for Bitcoin: ALM-GARCH ($13,657.4$) improves over symmetric LM-GARCH ($13,644.5$), standard GARCH(1,1) ($13,641.0$), and GJR-GARCH ($13,641.2$), but trails component GARCH ($13,661.8$) and FIAPARCH(1,d,1) ($13,682.0$).
   - BIC for Bitcoin: FIAPARCH has the best BIC ($-27,313.3$), followed by component GARCH ($-27,281.2$), ALM-GARCH ($-27,272.6$), LM-GARCH ($-27,263.7$), GARCH(1,1) ($-27,256.6$), and GJR-GARCH ($-27,248.6$).
   - Across all 6 markets, FIAPARCH achieves superior BIC and log-likelihood over ALM-GARCH (BIC difference favoring FIAPARCH: S&P 500 $-104.0$, FTSE 100 $-25.5$, DAX $-33.4$, Nikkei $-68.6$, KOSPI $-66.8$, Bitcoin $-40.7$).

3. **Out-of-Sample Forecasting Performance (Table 7 & Table S14):**
   - Evaluated by QLIKE loss against realized variance target (1-minute RV for Bitcoin):
     - Bitcoin QLIKE: HAR-RV ($0.280$), FIGARCH ($0.312$), EGARCH ($0.327$), LM-GARCH ($0.336$), GARCH(1,1) ($0.336$), GJR-GARCH ($0.340$), ALM-GARCH ($0.342$).
     - Diebold-Mariano test on Bitcoin shows ALM-GARCH is significantly outperformed by HAR-RV ($DM = 2.58, p < 0.01$) and FIGARCH ($DM = 4.81, p < 0.01$), while showing no statistically significant difference versus standard GARCH ($DM = 1.01$), GJR ($DM = 0.44$), or EGARCH ($DM = 1.58$).
   - ALM-GARCH is significantly more accurate than GARCH(1,1) and GJR on DAX ($DM = -2.11$ and $-3.60$) and KOSPI ($DM = -4.98$), but does not dominate overall.

4. **Joint-Stability Certificate (Table 1 & Table 6):**
   - The Foster-Lyapunov stability diagnostic $M^* = \inf_{\lambda > 0} \sup_c \{\Lambda_\delta(c) + \lambda S_\delta(c)\}$ is verified negative for Bitcoin ($M^* = -0.016615, \lambda^* = 0.0924, c_{\arg\sup} = 5.72$), DAX ($M^* = -0.010012$), and KOSPI ($M^* = -0.000088$, borderline). Nikkei 225 is unconstrained positive ($M^* = +0.003054$, not covered by sufficient certificate, but imposing margin costs only $0.61$ log-likelihood points).

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Lack of Forecast Dominance:** ALM-GARCH does **not** outperform established fractional or realized-volatility models out of sample. For Bitcoin, FIGARCH (QLIKE $0.312$) and HAR-RV (QLIKE $0.280$) clearly beat ALM-GARCH ($0.342$).
- **In-Sample Penalized Fit Inferiority:** FIAPARCH outperforms ALM-GARCH on BIC across every single market tested (by $-40.7$ points in Bitcoin).
- **Weak Identification of Memory Exponent $p$:** Profile likelihood across $p \in [1.05, 3.0]$ is flat (log-likelihood varies by $\le 1.2$ points in Bitcoin); $p$ cannot be freely estimated and must be pinned by normalization ($p = 1.2$).
- **Score Collinearity Near Null:** The score correlation between the level parameter $\delta$ and memory offset $\gamma$ is approximately $0.95$ near symmetry, severely limiting channel-specific test power unless the market exhibits pronounced asymmetry.
- **Boundary Degeneracy in Mature Equities:** In S&P 500 and FTSE 100, the positive shock injection amplitude is near zero ($\hat{\xi}_+ < 10^{-4}$), causing the memory channel to collapse into boundary indeterminacy.

## Falsification plan

1. **Crypto Memory Inversion Falsification Test (`research-proposed`):**
   - *Hypothesis:* In Bitcoin, positive returns generate higher finite-horizon persistence than negative returns ($\rho_+ > \rho_-$).
   - *Test Procedure:* Fit ALM-GARCH on walk-forward 3-year rolling windows of Bitcoin daily returns from 2021 to 2026.
   - *Research-Defined Falsification Threshold:* If in more than 30% of rolling windows $\hat{\rho}_+ \le \hat{\rho}_-$, or if the bootstrap likelihood-ratio test fails to reject $\gamma_+ = \gamma_-$ at the 5% significance level, the crypto memory asymmetry hypothesis is falsified.

2. **Volatility Targeting Cost-Adjusted Efficiency Falsification (`research-proposed`):**
   - *Hypothesis:* Sizing a Bitcoin trend strategy using ALM-GARCH conditional variance yields higher Sharpe ratio net of fees than standard GARCH(1,1) or fixed-window realized volatility.
   - *Test Procedure:* Backtest dynamic volatility-targeted Bitcoin exposure (target $\sigma = 40\%$) with 5 bps round-trip transaction costs over 2018–2026.
   - *Research-Defined Falsification Threshold:* If the ALM-GARCH volatility-targeted portfolio achieves an annualized net Sharpe ratio $\le$ standard GARCH(1,1) volatility targeting, the operational value of ALM-GARCH is falsified.

3. **Multi-Asset Crypto Cross-Section Portability Test (`research-proposed`):**
   - *Hypothesis:* High-beta altcoins (ETH, SOL) replicate the Bitcoin asymmetry pattern ($\xi_- > \xi_+$ and $\rho_+ > \rho_-$).
   - *Test Procedure:* Estimate ALM-GARCH on daily ETH and SOL returns (2020–2026) using quasi-maximum likelihood with fixed $p = 1.2$.
   - *Research-Defined Falsification Threshold:* If the joint symmetry test $LR_{\mathrm{sym}}$ fails to reject at $p < 0.01$, or if altcoin conditional variance exhibits explosive drift ($M^* > 0$ under stability optimization), reject direct model portability across crypto assets.

4. **Ablation Against Simpler Single-Channel Models (`research-proposed`):**
   - *Hypothesis:* The dual-channel model ($LR_{\mathrm{sym}}$) provides incremental forecasting power over a level-only asymmetric model ($\gamma_+ = \gamma_-$).
   - *Research-Defined Falsification Threshold:* If Diebold-Mariano test of ALM-GARCH against level-restricted ALM-GARCH on 1-step-ahead daily QLIKE yields $DM \ge 0$ (no significant improvement), the memory channel is redundant for forecasting.

## Crypto portability

**Adapted / Unproven** (Econometrically demonstrated on Bitcoin daily data in the primary paper, but operational trading overlays and multi-altcoin implementations remain unproven).

### Crypto-Specific Microstructure & Risk Considerations

1. **24/7 Continuous Trading & Session Boundaries:** The primary source constructed daily Bitcoin observations using UTC midnight boundaries ($00:00:00\text{ UTC}$). In crypto, volatility clustering is sensitive to session definitions (e.g., US market open vs Asian market hours). Shifting candle boundary timestamps may alter parameter estimates.
2. **Asymmetric Leverage Mechanics:** In traditional equities, the leverage effect is attributed to financial leverage (debt-to-equity ratios increasing on stock price drops). In crypto, where tokens do not have corporate balance sheets, the source's empirical confirmation that $\hat{\xi}_- \approx 2.21 \times \hat{\xi}_+$ reflects structural crypto derivatives liquidations: cascade liquidations of leveraged long perpetual positions inject immediate, concentrated market orders into thin order books.
3. **Upside Volatility Drift:** The unique finding that Bitcoin positive shocks exhibit high persistence ($\hat{\rho}_+ = 0.875$ vs $\hat{\rho}_- = 0.528$) matches the retail FOMO and bull-market momentum dynamics of crypto, where upward trends create extended periods of elevated volatility, unlike equities where bull markets are typically low-volatility regimes.
4. **Funding Rate & Basis Friction:** Deploying ALM-GARCH for delta-neutral volatility harvesting (e.g., trading variance swaps or options straddles on Deribit) requires explicit accounting of perpetual funding rates and basis drift, which the primary source does not model.

## Limitations

1. **Econometric Model, Not a Trading System (`underspecified` execution):** The primary paper is an academic statistical econometric study. It does not provide trade execution logic, entry/exit thresholds, or transaction-cost backtests.
2. **Forecast Accuracy Parity (`not independently reproduced`):** Out-of-sample forecasting tests against 1-minute realized variance show ALM-GARCH is comparable to standard GARCH/GJR models and is outperformed by HAR-RV and FIGARCH.
3. **Weak Parameter Identification:** The power-law exponent $p$ cannot be identified freely from data and must be pegged ($p=1.2$).
4. **Sample Boundary Effects:** In low-volatility regimes or markets with weak positive-shock variance response (S&P 500), the positive branch collapses to the parameter floor ($\hat{\xi}_+ < 10^{-4}$), invalidating standard Wald and asymptotic LR inferences.
5. **Absence of High-Frequency Microstructure:** The model operates on daily return aggregations; it does not model intraday order-book depth, trade arrival intensity, or bid-ask bounce.

## Implementation status

- **`not-implemented`** in `nautilus-quant-system` or PyBroker.
- No algorithmic execution logic, order generation, or backtesting script has been developed or verified.
- Status remains purely theoretical research capture and econometric baseline.

## Adoption boundary

- **`status: research-only`**
- **`adoption: not-approved`**
- **`approval_scope: research-only`**
- This record serves as a formal research capture of the ALM-GARCH volatility decomposition framework. It does **not** authorize live deployment, paper trading, testnet execution, or capital allocation.

## Related Wiki records

- `[[crypto-cross-sectional-realized-signed-jump-good-bad-volatility-2026-09-01]]` — Decomposes realized volatility into positive and negative semi-variances and signed jumps.
- `[[taiwan-semiconductor-etf-asymmetric-volatility-cvar-rachev-ratio-2026-09-02]]` — Asymmetric volatility modeling and tail risk in equity derivatives.
- `[[duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11]]` — Microstructure regime detection and point processes by Kyungsub Lee et al.
- `[[crypto-options-volatility-risk-premium-zscore-2026-08-31]]` — Crypto options volatility risk premium estimation.

## Sources

1. **Primary Paper (arXiv canonical):** Kayaki, K. T., & Lee, K. (2026). *Asymmetric Long-Memory GARCH: Sign-Dependent Kernel Injection in a Two-Dimensional Markov Chain*. arXiv preprint arXiv:2609.06422v1 [q-fin.ST]. https://arxiv.org/abs/2609.06422
2. **Full-Text Primary Source:** https://arxiv.org/html/2609.06422v1 (verified in full; all tables, equations, parameters, and proofs extracted 2026-09-17).
3. **Predecessor Formulation:** Lee, K., & Kayaki, K. T. (2026). *Long-memory GARCH via a two-dimensional Markov chain*. arXiv:2607.25189 [q-fin.ST]. https://arxiv.org/abs/2607.25189
4. **Realized Variance Data Reference:** Heber, G., Lunde, A., Shephard, N., & Sheppard, K. (2009). *Oxford-Man Institute's Realized Library*. Oxford-Man Institute, University of Oxford.
