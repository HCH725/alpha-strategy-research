---
schema: strategy-research-record-v1
title: Path Signature Decomposition with Segmented Lévy Area and Incremental Covariation for High-Frequency Futures Pairs Trading
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rough-paths
  - path-signature
  - levy-area
  - pairs-trading
  - statistical-arbitrage
  - commodity-futures
status: research-only
confidence: medium
source_as_of: 2025-10-16
sources:
  - https://arxiv.org/abs/2505.05332
  - https://doi.org/10.1002/fut.70075
  - https://doi.org/10.48550/arXiv.2505.05332
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Path Signature Decomposition with Segmented Lévy Area and Incremental Covariation for High-Frequency Futures Pairs Trading

## Provenance

- **Primary Source:** Zihao Guo (Zhongtai Securities Institute for Financial Studies, Shandong University), Hanqing Jin (Mathematical Institute, University of Oxford & Oxford Suzhou Centre for Advanced Research), Jiaqi Kuang (Mathematical Modelling and Data Analytics Center, Oxford Suzhou Centre for Advanced Research), Zhongmin Qian (Mathematical Institute, University of Oxford & Oxford Suzhou Centre for Advanced Research), and Jinghan Wang (Zhongtai Securities Institute for Financial Studies, Shandong University), *"Signature Decomposition Method Applying to Pair Trading"*, *Journal of Futures Markets*, Vol. 46, Issue 3 (March 2026), pp. 582–603.
- **Preprint Identifier:** arXiv:2505.05332v2 `[q-fin.TR, math.PR]`, submitted May 8, 2025; revised October 16, 2025.
- **Digital Object Identifiers:**
  - Journal DOI: [10.1002/fut.70075](https://doi.org/10.1002/fut.70075)
  - arXiv DOI: [10.48550/arXiv.2505.05332](https://doi.org/10.48550/arXiv.2505.05332)
- **Traceable Canonical URLs:**
  - [https://arxiv.org/abs/2505.05332](https://arxiv.org/abs/2505.05332)
  - [https://arxiv.org/html/2505.05332](https://arxiv.org/html/2505.05332)
  - [https://doi.org/10.1002/fut.70075](https://doi.org/10.1002/fut.70075)
- **Empirical Dataset:** Minute-level futures bar data from November 1, 2024 to December 31, 2024 across Chinese futures exchanges (SHFE, DCE, CZCE) via RQData API and US commodity futures (CME) via Oxford Suzhou Centre for Advanced Research data infrastructure.
- **Asset Universe Evaluated:** 5 sector groups encompassing 21 commodity and energy futures contracts across China and the US:
  - *Group 1 (Chinese Metals):* Gold (AU), Silver (AG), Tin (SN), Aluminum (AL). (Filtered from a larger metal pool by excluding Copper (CU) and Nickel (NI) due to correlation $< 0.50$ or spread Hurst exponent $> 0.50$).
  - *Group 2 (Chinese Agricultural):* Corn (C), Soybeans (B), Cotton (CF), Soybean Meal (M).
  - *Group 3 (Chinese Oil/Chemical/Industrial):* Methanol (MA), Crude Oil (SC), Soybean Oil (Y), Rebar (RB).
  - *Group 4 (US CME Metals):* US Gold (GC), US Silver (SI), US Palladium (PA).
  - *Group 5 (US CME Agricultural):* US Corn (ZC), US Wheat (ZW), US Soybeans (ZS), US Soybean Oil (ZL).

## Economic mechanism

### Source-reported

Classical pairs trading relies on the assumption that two economically linked assets exhibit a stationary, cointegrated price spread that periodically deviates from historical equilibrium and subsequently mean-reverts. However, traditional spread modeling relies almost entirely on first-moment linear cointegration and rolling standard deviations ($Z$-scores). In high-frequency, complex market environments, linear correlation alone fails to capture non-linear, path-dependent geometric relationships between asset price streams. When an apparent spread divergence occurs, linear models cannot distinguish whether the divergence reflects a transient, mean-reverting liquidity shock or an unhedged structural regime shift in one of the legs.

The authors propose leveraging **rough path signature theory** (Lyons, 1998) to represent the non-linear interaction between two price paths. While the truncated second-order path signature $X_{s,t}^2$ contains rich geometric information, its direct use as a trading signal is hindered by abstract financial interpretability. Algebraically, the second-order signature tensor decomposes into a symmetric part $D_{s,t}^2$ (the product of increments, representing directional co-movement) and an anti-symmetric part $A_{s,t}^2$ (the classical Lévy area, representing signed enclosed area between the trajectory and its chord). 

The authors identify a critical flaw in using the raw Lévy area: positive and negative loops around the chord cancel each other out ($A^+ - A^- = 0$), falsely indicating perfect correlation when paths are actually diverging wildly. To solve this, they introduce the **segmented signature** $C_{s,t}^{(1,2)}$, defined as the sum of the absolute values of the Lévy area over each sub-interval formed by the intersection points of the trajectory and its chord. A near-zero segmented signature guarantees strict collinearity, and lower values indicate stronger, un-cancelled geometric coupling.

The resulting hybrid strategy (**SE-SIG-DIFF**) deploys two filters alongside the linear spread $Z$-score:
1. **Segmented Signature Filter ($C_{s,t}^{(1,2)} < \text{historical mean}(C^{(1,2)})$):** Confirms that the two assets currently possess unusually high geometric interactivity and tight structural coherence, eliminating false breakouts caused by decorrelation.
2. **Covariation of Increments Filter ($D_{s,t}^{(1,2)} > 0$):** Confirms that both assets are moving in the same directional sense over the formation window, ensuring that the spread deviation is a relative misalignment rather than a fundamental divergence where one asset falls while the other rallies.

### Research interpretation

The falsifiable mechanism is a **non-linear geometric adverse-selection filter** for statistical arbitrage:
1. **Adverse Selection in Spread Deviation:** Standard linear threshold models ($|Z_t| > 2.0$) generate substantial left-tail losses because large spread deviations frequently stem from idiosyncratic shocks, order flow toxicity, or fundamental news affecting only one leg. In these situations, the spread does not mean-revert; instead, it continues to drift, hitting stops or generating catastrophic drawdowns.
2. **Geometric Path Invariant as a Co-movement Verifier:** By mapping the two discrete price series into a continuous 2D path and measuring its chord-crossing segmented Lévy area, the model extracts the transverse excursion of the system. An idiosyncratic drift in one leg causes wide transverse excursions away from the chord, inflating $C_{s,t}^{(1,2)}$ above its historical mean. 
3. **Selective Trade Elimination:** The primary channel of alpha enhancement in SE-SIG-DIFF is not predicting larger reversals, but **filtering out toxic non-reverting trades**. Across all 21 evaluated pairs, the number of executions drops by 30% to 70%, which simultaneously suppresses transaction cost drag (fees and slippage) and truncates maximum drawdown, turning negative baseline Sharpe ratios into solidly positive performance.

## Signal

### Source-reported construction

The strategy operates on paired continuous futures contracts $(X^{(1)}, X^{(2)})$ using 1-minute close prices:

#### 1. Asset Screening & Pre-filtering
- **Sector Homogeneity:** Pairs are selected only within the same broad economic category.
- **Linear Correlation Filter:** Compute Pearson correlation $\rho$ across the screening window; require $\rho > 0.50$ (e.g., excluding Nickel NI which had $\rho < 0.50$ with multiple metals).
- **Mean-Reversion Hurst Exponent Filter:** Compute the Generalized Hurst Exponent $H(q=1)$ on the balanced log-spread series over rolling sub-windows:
  $$E_p(s) = \frac{\mathrm{mean}(|X(t+s) - X(t)|^p)}{\mathrm{mean}(|X(t)|^p)} \propto s^{q H(q)}$$
  Require $H(q=1) < 0.50$ across all observed sub-windows to guarantee mean-reverting properties. Assets failing this criteria (e.g., Copper CU, where spread Hurst exponents exceeded 0.50 reaching 0.6785) are permanently removed from the pair pool.

#### 2. Hedge Ratio & Normalized Spread Construction
- Log-transform price series: $\mathcal{L}_t^{(1)} = \log(X_t^{(1)})$, $\mathcal{L}_t^{(2)} = \log(X_t^{(2)})$.
- Fit ordinary least squares (OLS) regression over the initial formation window:
  $$\mathcal{L}^{(1)} = \alpha + \beta \mathcal{L}^{(2)} + \epsilon$$
  where $\beta$ is the optimal hedge ratio (number of lots of asset 2 per lot of asset 1).
- Compute balanced log price spread:
  $$S_t = \mathcal{L}_t^{(1)} - \beta \mathcal{L}_t^{(2)}$$
- In each rolling window $w$ (baseline $w = 60$ minutes; robustness tested at $w \in \{30, 60, 90\}$):
  $$\mu_t = \frac{1}{w} \sum_{i=t-w}^{t-1} S_i, \quad \sigma_t = \sqrt{\frac{1}{w-1}\sum_{i=t-w}^{t-1}(S_i - \mu_t)^2}$$
  $$Z_t = \frac{S_t - \mu_t}{\sigma_t}$$

#### 3. Path Signature & Segmented Lévy Area Decomposition
- Over the current window $[t-w, t]$, consider the 2D path $X_u = (X_u^{(1)}, X_u^{(2)})$ constructed by connecting discrete points via linear interpolation.
- Let $(X_0^{(1)}, X_0^{(2)})$ be the initial point at $t-w$ and $(X_T^{(1)}, X_T^{(2)})$ be the terminal point at $t$. The chord is the line segment connecting $(X_0^{(1)}, X_0^{(2)})$ to $(X_T^{(1)}, X_T^{(2)})$.
- Calculate all intersection (crossing) points $t_0, t_1, \dots, t_n$ ($t_0 = t-w, t_n = t$) where the continuous interpolated path crosses the chord. For each discrete step, find the intersection between the line connecting $(X_{k-1}^{(1)}, X_{k-1}^{(2)})$ to $(X_k^{(1)}, X_k^{(2)})$ and the chord equation; if the intersection $x$-coordinate falls strictly within $[X_{k-1}^{(1)}, X_k^{(1)}]$, mark it as a crossing point.
- Calculate the **Segmented Signature** $C_{t-w, t}^{(1,2)}$:
  $$C_{t-w, t}^{(1,2)} = \sum_{r=0}^{n-1} \left| A_{t_r, t_{r+1}}^{(1,2)} \right|$$
  where $A_{t_r, t_{r+1}}^{(1,2)} = \frac{1}{2}\left( X_{t_r, t_{r+1}}^{(1,2)} - X_{t_r, t_{r+1}}^{(2,1)} \right)$ is the signed Lévy area over sub-interval $[t_r, t_{r+1}]$ enclosed between the path and the chord.
- Calculate the **Covariation of Increments** $D_t^{(1,2)}$:
  $$D_t^{(1,2)} = \frac{1}{2} D_t^{(1)} \times D_t^{(2)} = \frac{1}{2} \left( X_t^{(1)} - X_{t-w}^{(1)} \right) \left( X_t^{(2)} - X_{t-w}^{(2)} \right)$$

#### 4. Execution Logic (Algorithm 2: SE-SIG-DIFF)
- **Gating Condition 1 (High Geometric Interactivity):**
  $$C_t^{(1,2)} < \text{historical mean}(C^{(1,2)})$$
  (computed recursively from start of trading up to $t-1$ to eliminate lookahead bias).
- **Gating Condition 2 (Positive Directional Covariation):**
  $$D_t^{(1)} \times D_t^{(2)} > 0$$
- **Entry Trigger:**
  - If Gating Condition 1 AND Gating Condition 2 are both satisfied:
    - If $Z_t > Z_{\text{score}}$ (baseline $Z_{\text{score}} = 2.0$; robustness tested at $1.5, 2.0, 2.5$): **Short Asset 1, Long Asset 2** (hedge ratio $\beta$).
    - If $Z_t < -Z_{\text{score}}$: **Long Asset 1, Short Asset 2** (hedge ratio $\beta$).
  - Otherwise: **Hold / No Entry**.
- **Exit Trigger:**
  - **Mean Reversion Target:** Close positions when spread normalizes to zero ($Z_t$ crosses 0).
  - **Downside Stop-Loss:** Per-trade loss is capped at a fixed threshold equal to the maximum drawdown observed during the 2-month pre-strategy calibration period.

## Required data

- **Instruments:** Liquid commodity, metal, and energy futures contracts traded on Chinese exchanges (Shanghai Futures Exchange [SHFE], Dalian Commodity Exchange [DCE], Zhengzhou Commodity Exchange [CZCE]) and the Chicago Mercantile Exchange (CME).
- **Timeframe:** 1-minute discrete bar frequency ($OHLCV$). Strategy logic primarily evaluates minute close prices.
- **Fields:** Minute close price for each asset; trading timestamp; exchange session boundaries.
- **Preprocessing:** Natural logarithm transform $\mathcal{L}_t = \log(X_t)$ applied to all price series prior to regression and signature calculation.
- **Point-in-Time Integrity:**
  - Hedge ratio $\beta$ calibrated on pre-strategy historical data.
  - Rolling mean $\mu_t$ and rolling standard deviation $\sigma_t$ strictly use $[t-w, t-1]$.
  - Segmented signature baseline threshold uses historical mean computed strictly over past realized values prior to bar $t$.

## Execution assumptions

- **Execution Timing:** Signals generated at the close of bar $t$ are executed immediately on that bar / next bar.
- **Order Types:** Market / aggressive limit orders assumed fillable at recorded minute prices.
- **Round-Trip Transaction Cost:** Deducted at $0.05\%$ of notional value per round-trip trade across all markets.
  - *Chinese Futures Market:* Standard institutional benchmark composed of exchange fees ($0.00015\%$ to $0.008\%$), brokerage markups ($0.001\%$ to $0.012\%$), and slippage ($0.01\%$ to $0.03\%$).
  - *US Futures Market:* CME standard total transaction costs typically span $0.01\%$ to $0.02\%$ for ultra-liquid contracts, but can reach $0.02\%$ to $0.04\%$ for commodities with liquidity differentials. A uniform conservative fee of $0.05\%$ is applied to both markets to ensure rigorous robustness.
- **Position Sizing & Margins:** Risk-neutral sizing according to estimated regression coefficient $\beta$. Standard futures margin accounts with symmetric long and short capabilities.
- **Stop-Loss Model:** Fixed maximum loss per trade equal to the maximum drawdown observed over the preceding 2-month historical calibration sample.

## Evidence

### Source-reported

All figures below are directly reported by Guo et al. (*Journal of Futures Markets*, 2026 / arXiv:2505.05332v2, Tables 4–15) over the empirical test sample (November 1, 2024 to December 31, 2024; baseline parameters: $w=60$ minutes, $Z_{\text{score}}=2.0$, round-trip cost = 0.05%):

#### 1. Performance on Chinese Metal Futures (Group 1, Tables 4 & 5)
- **AU & AG (Gold & Silver):**
  - NO SIG (Benchmark): Return $2.27\%$, Daily $0.041\%$, MDD $-1.95\%$, Sharpe $1.00$, Count $2398$.
  - SIG (Raw Signature Filter): Return $-0.13\%$, Daily $-0.0039\%$, MDD $-2.19\%$, Sharpe $-0.28$, Count $1647$.
  - SE-SIG (Segmented Sig Filter): Return $2.13\%$, Daily $0.039\%$, MDD $-1.61\%$, Sharpe $1.29$, Count $1633$.
  - **SE-SIG-DIFF:** Return $2.64\%$, Daily $0.048\%$, MDD $-1.29\%$, Sharpe **$1.44$**, Count $1335$.
- **AU & AL (Gold & Aluminum):**
  - NO SIG: Return $2.48\%$, MDD $-1.64\%$, Sharpe $1.57$, Count $1801$.
  - SIG: Return $0.66\%$, MDD $-2.92\%$, Sharpe $0.19$, Count $1169$.
  - SE-SIG: Return $3.79\%$, MDD $-1.74\%$, Sharpe $2.48$, Count $1195$.
  - **SE-SIG-DIFF:** Return $3.74\%$, MDD $-1.57\%$, Sharpe **$2.83$**, Count $667$.
- **AU & SN (Gold & Tin):**
  - NO SIG: Return $-3.95\%$, MDD $-7.31\%$, Sharpe $-2.14$, Count $1672$.
  - SIG: Return $0.13\%$, MDD $-4.61\%$, Sharpe $-0.14$, Count $1094$.
  - SE-SIG: Return $0.32\%$, MDD $-3.14\%$, Sharpe $-0.04$, Count $1168$.
  - **SE-SIG-DIFF:** Return $3.94\%$, MDD $-1.41\%$, Sharpe **$2.10$**, Count $778$.
- **AL & AG (Aluminum & Silver):**
  - NO SIG: Return $1.42\%$, MDD $-2.99\%$, Sharpe $0.45$, Count $1783$.
  - SIG: Return $1.31\%$, MDD $-2.40\%$, Sharpe $0.50$, Count $1266$.
  - SE-SIG: Return $3.03\%$, MDD $-2.76\%$, Sharpe $1.23$, Count $1226$.
  - **SE-SIG-DIFF:** Return $6.63\%$, MDD $-1.81\%$, Sharpe **$3.03$**, Count $550$.
- **AG & SN (Silver & Tin):**
  - NO SIG: Return $-3.92\%$, MDD $-8.60\%$, Sharpe $-1.81$, Count $1670$.
  - SIG: Return $-0.44\%$, MDD $-5.64\%$, Sharpe $-0.40$, Count $1069$.
  - SE-SIG: Return $2.54\%$, MDD $-4.13\%$, Sharpe $0.95$, Count $1140$.
  - **SE-SIG-DIFF:** Return $2.75\%$, MDD $-4.58\%$, Sharpe **$1.06$**, Count $832$.
- **AL & SN (Aluminum & Tin):**
  - NO SIG: Return $-1.62\%$, MDD $-6.05\%$, Sharpe $-0.95$, Count $1664$.
  - SIG: Return $0.30\%$, MDD $-4.32\%$, Sharpe $-0.06$, Count $958$.
  - SE-SIG: Return $2.93\%$, MDD $-4.54\%$, Sharpe **$1.21$**, Count $1096$.
  - **SE-SIG-DIFF:** Return $2.57\%$, MDD $-3.38\%$, Sharpe $1.01$, Count $742$.

#### 2. Performance on Chinese Agricultural Futures (Group 2, Tables 6 & 7)
- **C & B (Corn & Soybeans):** NO SIG Sharpe $1.89$ (return $3.40\%$, trades $5077$); SE-SIG-DIFF Sharpe **$2.42$** (return $4.42\%$, MDD $-2.35\%$, trades $1712$).
- **C & CF (Corn & Cotton):** NO SIG Sharpe $-2.48$ (return $-2.99\%$, trades $4592$); SE-SIG-DIFF Sharpe **$-0.99$** (return $-0.93\%$, MDD $-2.36\%$, trades $1349$).
- **C & M (Corn & Soybean Meal):** NO SIG Sharpe $-1.39$ (return $-1.59\%$, trades $4743$); SE-SIG-DIFF Sharpe **$-0.84$** (return $-0.89\%$, MDD $-2.44\%$, trades $1633$).
- **B & CF (Soybeans & Cotton):** NO SIG Sharpe $-4.92$ (return $-7.45\%$, trades $4736$); SE-SIG-DIFF Sharpe **$-3.07$** (return $-4.79\%$, MDD $-6.12\%$, trades $1414$).
- **B & M (Soybeans & Soybean Meal):** NO SIG Sharpe $2.80$ (return $4.78\%$, trades $4890$); SE-SIG-DIFF Sharpe **$3.66$** (return $6.64\%$, MDD $-1.80\%$, trades $2252$).
- **M & CF (Soybean Meal & Cotton):** NO SIG Sharpe $-4.96$ (return $-7.65\%$, trades $4755$); SE-SIG-DIFF Sharpe **$-3.86$** (return $-5.59\%$, MDD $-6.32\%$, trades $1542$).

#### 3. Performance on Chinese Oil / Chemical / Industrial Futures (Group 3, Tables 8 & 9)
- **MA & SC (Methanol & Crude Oil):** NO SIG Sharpe $0.19$ (return $0.57\%$, trades $2491$); SE-SIG-DIFF Sharpe **$2.30$** (return $3.54\%$, MDD $-1.95\%$, trades $866$).
- **MA & Y (Methanol & Soybean Oil):** NO SIG Sharpe $-1.85$ (return $-2.82\%$, trades $2870$); SE-SIG-DIFF Sharpe **$-1.45$** (return $-2.47\%$, MDD $-6.96\%$, trades $794$).
- **MA & RB (Methanol & Rebar):** NO SIG Sharpe $0.71$ (return $1.29\%$, trades $2686$); SE-SIG-DIFF Sharpe **$1.47$** (return $2.22\%$, MDD $-1.71\%$, trades $928$). (SE-SIG alone achieved $1.98$).
- **SC & Y (Crude Oil & Soybean Oil):** NO SIG Sharpe $2.82$ (return $5.89\%$, trades $2499$); SE-SIG-DIFF Sharpe **$5.38$** (return $10.14\%$, MDD $-1.63\%$, trades $813$).
- **SC & RB (Crude Oil & Rebar):** NO SIG Sharpe $2.72$ (return $3.54\%$, trades $4646$); SE-SIG-DIFF Sharpe **$3.95$** (return $5.40\%$, MDD $-1.08\%$, trades $1669$).
- **RB & Y (Rebar & Soybean Oil):** NO SIG Sharpe $-1.55$ (return $-2.09\%$, trades $5122$); SE-SIG-DIFF Sharpe **$0.12$** (return $0.53\%$, MDD $-4.76\%$, trades $1617$).

#### 4. Performance on US CME Metal Futures (Group 4, Tables 10 & 11)
- **GC & SI (US Gold & Silver):** NO SIG Sharpe $0.30$ (return $0.81\%$, MDD $-1.71\%$, trades $10011$); SIG Sharpe $-1.81$; SE-SIG Sharpe $2.12$; SE-SIG-DIFF Sharpe **$2.91$** (return $3.45\%$, MDD $-1.05\%$, trades $5722$).
- **GC & PA (US Gold & Palladium):** NO SIG Sharpe $-1.81$ (return $-2.49\%$, MDD $-3.88\%$, trades $4257$); SE-SIG-DIFF Sharpe **$1.21$** (return $2.61\%$, MDD $-1.15\%$, trades $1289$).
- **SI & PA (US Silver & Palladium):** NO SIG Sharpe $-3.42$ (return $-5.46\%$, MDD $-5.49\%$, trades $4318$); SE-SIG-DIFF Sharpe **$-0.84$** (return $-0.85\%$, MDD $-1.76\%$, trades $1969$).

#### 5. Performance on US CME Agricultural Futures (Group 5, Tables 12 & 13)
- **ZC & ZW (US Corn & Wheat):** NO SIG Sharpe $2.67$; SE-SIG-DIFF Sharpe **$3.25$** (return $4.88\%     o 6.16\%$, trades $4131     o 1394$).
- **ZC & ZS (US Corn & Soybeans):** NO SIG Sharpe $5.68$; SE-SIG-DIFF Sharpe **$5.92$** (return $11.21\%     o 12.31\%$, trades $4504     o 1681$).
- **ZC & ZL (US Corn & Soybean Oil):** NO SIG Sharpe $3.65$; SE-SIG-DIFF Sharpe **$3.94$** (return $4.20\%     o 5.15\%$, trades $3980     o 1417$).
- **ZW & ZS (US Wheat & Soybeans):** NO SIG Sharpe $0.75$; SE-SIG-DIFF Sharpe **$0.95$** (return $1.09\%     o 1.39\%$, trades $4580     o 1350$).
- **ZW & ZL (US Wheat & Soybean Oil):** NO SIG Sharpe $-1.99$; SE-SIG-DIFF Sharpe **$0.12$** (return $-1.70\%     o 0.59\%$, trades $4682     o 1742$).
- **ZS & ZL (US Soybeans & Soybean Oil):** NO SIG Sharpe $-1.03$; SE-SIG-DIFF Sharpe **$-0.02$** (return $-1.90\%     o 0.50\%$, trades $5132     o 2627$).

#### 6. Failure of Raw Second-Order Signature (Ablation Proof)
In numerous asset pairs, applying the raw second-order signature $A_{s,t}^{(1,2)}$ (SIG) severely degrades performance compared to having no filter at all (NO SIG):
- AU & AG: Sharpe fell from $1.00$ to $-0.28$.
- GC & SI: Sharpe fell from $0.30$ to $-1.81$.
- C & CF: Sharpe fell from $-2.48$ to $-2.94$.
- C & M: Sharpe fell from $-1.39$ to $-2.13$.
- B & CF: Sharpe fell from $-4.92$ to $-5.49$.
- MA & SC: Sharpe fell from $0.19$ to $0.15$.
This directly confirms the author's theoretical proof: the raw Lévy area fails because signed loop cancellation masks true path disassociation, whereas segmented signature decomposition isolates authentic path interactivity.

#### 7. Robustness Sensitivity & Statistical Significance (Tables 14 & 15)
- **Grid Sensitivity (Table 14):** Evaluated across 9 window and threshold combinations ($w \in \{30, 60, 90\}$ minutes; $Z_{\text{score}} \in \{1.5, 2.0, 2.5\}$). Across all five groups, the average improvement in Sharpe ratio for SE-SIG-DIFF over NO SIG was positive in all 45 group-parameter configurations (ranging from $+0.23$ to $+2.72$).
- **Jobson-Korkie-Memmel (JK-Memmel) Hypothesis Test (Table 15):** Tested the null hypothesis $H_0: \Delta \text{Sharpe} \leq 0$ against $H_1: \Delta \text{Sharpe} > 0$ at significance level $\alpha = 0.05$. Every single tested pair rejected $H_0$ with extreme significance:
  - Group 1: AUAG ($p = 0.015$), AUAL ($p = 3.18\times 10^{-9}$), AUSN ($p = 7.81\times 10^{-13}$), ALAG ($p = 3.25\times 10^{-5}$), AGSN ($p = 3.53\times 10^{-11}$), ALSN ($p = 3.38\times 10^{-12}$).
  - Group 2: CB ($p = 0.0121$), CCF ($p = 7.19\times 10^{-11}$), CM ($p = 0.0089$), BCF ($p = 2.67\times 10^{-17}$), BM ($p = 7.96\times 10^{-5}$), MCF ($p = 9.64\times 10^{-7}$).
  - Group 3: MASC ($p = 5.11\times 10^{-11}$), MAY ($p = 0.0393$), MARB ($p = 0.0101$), SCY ($p = 3.48\times 10^{-18}$), SCRB ($p = 5.46\times 10^{-7}$), RBY ($p = 3.62\times 10^{-14}$).
  - Group 4: GCSI ($p = 4.35\times 10^{-33}$), GCPA ($p = 6.32\times 10^{-21}$), SIPA ($p = 6.32\times 10^{-15}$).
  - Group 5: ZCZW ($p = 6.59\times 10^{-4}$), ZCZS ($p = 0.0116$), ZCZL ($p = 0.0211$), ZWZS ($p = 0.0129$), ZWZL ($p = 4.05\times 10^{-6}$), ZSZL ($p = 7.81\times 10^{-7}$).

### Independently reproduced

Not independently reproduced. (Scout research capture; primary data from RQData and CME not locally executed).

### Negative evidence

1. **Persistent Negative Absolute Sharpe on Structurally Divergent Pairs:** While SE-SIG-DIFF significantly truncates downside losses relative to the unconstrained benchmark, it does not magically turn every pair profitable. In Group 2, four out of six pairs (C&CF, C&M, B&CF, M&CF) remained net negative (e.g., B&CF Sharpe $-3.07$; M&CF Sharpe $-3.86$). In Group 4, SI&PA remained negative (Sharpe $-0.84$). This demonstrates that geometric filtering cannot overcome fundamental structural breakdowns where two commodities experience persistent supply/demand divergence.
2. **Short Historical Evaluation Window:** The empirical validation is conducted over a single 2-month sample (November 1 to December 31, 2024). Although high-frequency minute data provides large sample sizes ($N > 40,000$ minutes per asset), a 2-month span cannot capture multi-year macroeconomic regime transitions, commodity super-cycles, or major seasonal agricultural shifts.
3. **Turnover & Latency Sensitivity:** The strategy requires continuous high-frequency order book tracking and rapid execution. While $0.05\%$ round-trip friction was deducted, aggressive fills in fast-moving commodity markets during news releases could encounter adverse slippage exceeding $0.05\%$.

## Falsification plan

To falsify the proposed hypothesis that segmented path signatures extract genuine non-linear path coupling rather than fitting noise:

1. **Multi-Year Walk-Forward Cross-Validation:**
   - *Test:* Run the SE-SIG-DIFF pipeline across 5 continuous years of minute data (2020–2025) on CME commodity futures, evaluating across distinct macro regimes (2020 COVID crash, 2021-2022 inflationary spike, 2023-2024 rate tightening).
   - *Failure Rule:* If the average $\Delta \text{Sharpe} = \text{Sharpe}_{\text{SE-SIG-DIFF}} - \text{Sharpe}_{\text{NO SIG}} \leq 0$ over rolling 6-month out-of-sample windows, the non-linear path persistence hypothesis is falsified.
2. **Placebo / Scrambled-Chord Test:**
   - *Test:* Randomly permute the bar order within the rolling 60-minute window before calculating chord crossing points and segmented areas, destroying temporal geometry while preserving the marginal return distribution.
   - *Failure Rule:* If the scrambled-path filter achieves Sharpe ratio improvements statistically indistinguishable from the real segmented signature ($p > 0.10$), the geometric roughness explanation is falsified.
3. **Cost Tolerance & Break-Even Stress Testing:**
   - *Test:* Vary round-trip execution drag from $0.01\%$ to $0.15\%$ in steps of $0.01\%$.
   - *Failure Rule:* If SE-SIG-DIFF fails to maintain positive excess Sharpe over NO SIG at realistic institutional slippage levels ($\geq 0.04\%$), the operational viability of the strategy is disproven.
4. **Component Ablation Screen:**
   - *Test:* Isolate SE-SIG (segmented signature alone) vs DIFF (incremental covariation alone) vs SE-SIG-DIFF.
   - *Failure Rule:* If DIFF alone accounts for $\geq 95\%$ of the Sharpe improvement, the computational overhead of computing rough path segmented signatures is non-accretive.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source investigates traditional commodity and metal futures traded on regulated exchanges (SHFE, DCE, CZCE, CME). It does not test crypto assets. Any application to cryptocurrency pairs is a research adaptation.
- **Crypto-Specific Structural Factors:**
  1. **Continuous 24/7 Trading Without Session Halts:** Traditional commodity futures have discrete trading sessions, overnight gaps, and weekend closures that introduce artificial jump discontinuities into continuous path interpolation. Cryptocurrency markets trade 24/7/365, which theoretically provides a cleaner, uninterrupted continuous path for rough path signature calculations.
  2. **Perpetual Contract Funding Rates:** In crypto perpetual futures (e.g., BTC/USDT vs. ETH/USDT, SOL/USDT vs. AVAX/USDT), holding positions across 8-hour funding intervals incurs asymmetric funding carry. The pair spread $S_t$ must incorporate net funding yield differentials; otherwise, funding payments could erode the statistical arbitrage margin.
  3. **High Cointegration Instability:** Unlike physical commodities with shared industrial demand or agricultural seasonality, crypto altcoins exhibit frequent idiosyncratic decoupling due to token unlock schedules, protocol governance exploits, or localized liquidity drainage. The pre-screening phase must run rolling cointegration and dynamic Hurst exponent tests with short lookbacks ($< 7$ days) to rapidly expel degrading pairs.
  4. **Exchange Latency & Cross-Venue Fragmentation:** High-frequency statistical arbitrage in crypto often requires cross-venue execution (e.g., Binance vs. Bybit vs. OKX). Execution latency and toxic taker flow can significantly worsen slippage beyond the 5 bps assumed in traditional futures.

## Limitations

- **Empirical Sample Duration:** The source backtest spans only two calendar months (Nov–Dec 2024). Multi-year regime robustness remains unproven.
- **Fixed Hedge Ratio:** The hedge ratio $\beta$ is estimated once via OLS across historical calibration data rather than dynamically updated via Kalman filters or rolling error-correction models (VECM).
- **Computational Overhead:** Segmented signature calculation requires real-time linear interpolation and geometric line-segment intersection solving for every bar across all universe pairs, demanding optimized C++/Rust vectorization for low-latency production pipelines.
- **Absence of Independent Codebase:** The paper provides algorithmic pseudocode (Algorithms 1 & 2) but does not link a public GitHub repository.

## Implementation status

- `not-implemented`: This research capture is an upstream theoretical normalization. No implementation has been completed in NautilusTrader, PyBroker, or any execution engine.
- Neither backtest replication, paper trading, nor testnet deployment has been authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record serves solely as structured research material for the Hermes Wiki Brain knowledge repository. It does not constitute investment advice, commercial recommendation, or authorization to trade live capital.

## Related Wiki records

- `[[quant/signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02]]` — Related application of rough path signatures to optimal execution in statistical arbitrage; proves quadratic reduction theorem for execution speeds.
- `[[quant/path-portfolio-optimization-signature-defect-lift-2026-09-02]]` — Uses path signatures to capture higher-order geometric path defects for dynamic portfolio optimization.
- `[[quant/commodity-futures-network-momentum-lead-lag-graph-learning-2026-09-02]]` — Investigates lead-lag graph learning in commodity futures using signature Lévy area and dynamic time warping.
- `[[quant/crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]` — Explores multi-pair statistical arbitrage overlayed with deep reinforcement learning execution and deterministic risk shielding.
- `[[quant/attention-factors-statistical-arbitrage-residual-portfolios-2026-09-02]]` — Deep learning statistical arbitrage on residual asset returns; contrasts with the interpretable geometric signature decomposition approach.

## Sources

1. **Primary Journal Publication:** Zihao Guo, Hanqing Jin, Jiaqi Kuang, Zhongmin Qian, and Jinghan Wang, *"Signature Decomposition Method Applying to Pair Trading"*, *Journal of Futures Markets*, Vol. 46, No. 3 (March 2026), pp. 582–603. DOI: [10.1002/fut.70075](https://doi.org/10.1002/fut.70075).
2. **Preprint Full Text:** Zihao Guo, Hanqing Jin, Jiaqi Kuang, Zhongmin Qian, and Jinghan Wang, *"Signature Decomposition Method Applying to Pair Trading"*, arXiv preprint `arXiv:2505.05332v2 [q-fin.TR, math.PR]`, submitted May 8, 2025; revised October 16, 2025. DOI: [10.48550/arXiv.2505.05332](https://doi.org/10.48550/arXiv.2505.05332). Full text URL: [https://arxiv.org/abs/2505.05332](https://arxiv.org/abs/2505.05332). HTML URL: [https://arxiv.org/html/2505.05332](https://arxiv.org/html/2505.05332).
3. **Rough Path Signature Theoretical Foundations:** 
   - T. J. Lyons (1998), *"Differential equations driven by rough signals"*, *Revista Matemática Iberoamericana*, 14(2), 215–310.
   - T. Lyons and Z. Qian (2002), *System Control and Rough Paths*, Oxford University Press.
   - D. Levin, T. Lyons, and H. Ni (2013), *"Learning from the past, predicting the statistics for the future, learning an evolving system"*, arXiv:1309.0260.
