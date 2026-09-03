---
schema: strategy-research-record-v1
title: "Liquidity Premium and Investment Horizons: Cross-Sectional Return Predictability from Daily Signed Order Flow and Kyle's Price Impact Lambda"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - kyles-lambda
  - order-flow
  - liquidity-premium
  - price-impact
  - amihud-illiquidity
  - cross-sectional-equity
  - fama-macbeth
status: research-only
confidence: medium
source_as_of: 2026-07-02
sources:
  - "https://arxiv.org/abs/2607.01377"
  - "https://doi.org/10.48550/arXiv.2607.01377"
  - "https://arxiv.org/html/2607.01377v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Liquidity Premium and Investment Horizons: Cross-Sectional Return Predictability from Daily Signed Order Flow and Kyle's Price Impact Lambda

## Provenance

- **Primary paper:** Irene Aldridge, *Liquidity Premium and Investment Horizons*, arXiv preprint `arXiv:2607.01377v1 [econ.EM, q-fin.PR, q-fin.ST, q-fin.TR]`, submitted July 2, 2026. DOI: `10.48550/arXiv.2607.01377`.
- **Author:** Irene Aldridge, Cornell University / AbleMarkets (`irene.aldridge@gmail.com`).
- **Primary source text:** Full-text LaTeX source files (`main.tex`, `EquitiesPricing_Kyle.bib`, `FixedIncome.bib`) and HTML5 article directly retrieved and verified from arXiv (`https://arxiv.org/src/2607.01377` and `https://arxiv.org/html/2607.01377v1`, July 2026 release).
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Source/data as-of:** 2026-07-02.
- **Source-identity deduplication:** Repository-wide inspection confirmed zero existing records citing `2607.01377` or `Irene Aldridge`. While an earlier record (`crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31.md`) references the foundational Kyle (1985) paper in a subsecond-to-minute crypto perpetual order book context, Aldridge (2026) provides an independent cross-sectional asset pricing framework evaluated across the full CRSP US equity panel (9,893 unique point-in-time firms, 448,393 firm-months from 2020 to 2025) demonstrating that Kyle's $\lambda$ and signed order flow resolve Constantinides' (1986) liquidity premium puzzle via adverse selection dynamics and temporary mispricing over 1-month holding horizons.

## Economic mechanism

### Source-reported

In classical asset pricing, illiquid assets are observed to command higher average returns (Amihud and Mendelson, 1986). Merton (1973) hypothesized that investors require compensation for trading frictions. However, Constantinides (1986) established the "liquidity premium puzzle": in general equilibrium, an investor with an infinite horizon rebalances infrequently, making their required premium for transaction costs negligibly small, far below empirical estimates.

Aldridge (2026) resolves this paradox by demonstrating that the illiquidity premium is **realized, not required**:
1. **Adverse selection discount (Stage 1, $t = 0$):** When signed order flow falls, the ratio of informed trading to noise trading deteriorates. Under Kyle's (1985) equilibrium, the price-impact coefficient is:
   $$\lambda = \frac{1}{2} \frac{\sqrt{\Sigma_0}}{\sigma_u}$$
   where $\Sigma_0$ is fundamental uncertainty and $\sigma_u^2$ is noise-trading variance. When noise-trading variance is low relative to fundamental uncertainty, $\lambda$ widens. A wider $\lambda$ increases price impact per share, discouraging participation by both informed and noise traders. Competitive, risk-neutral market makers earn zero expected profit and do not voluntarily lower prices; instead, prices fall because reduced participation and elevated adverse-selection risk depress buyers' willingness to pay. The stock trades at a discount relative to its fundamental value.
2. **Order flow normalization and price recovery (Stage 2, $t = 1$):** As the information environment normalizes (noise traders return, raising $\sigma_u$, or fundamental information resolves $\Sigma_0$), $\lambda$ narrows. Subsequent positive signed order flow moves prices upward toward fundamental value. Investors who purchased at the Stage 1 discount realize a positive return differential:
   $$\text{Return} = \frac{P_{\text{fair}} - P_{\text{depressed}}}{P_{\text{depressed}}}$$
   without any counterparty knowingly paying a risk premium to compensate for illiquidity.
3. **Four core propositions:**
   - *Proposition 1 (Kyle's Lambda):* Unique linear equilibrium pricing rule $p(y) = p_0 + \lambda y$ with $\beta = 1/(2\lambda)$ and $\lambda = \frac{1}{2}\sqrt{\Sigma_0}/\sigma_u$. Volume volatility $\operatorname{std}(V_t)$ proxies for noise-trading variance $\sigma_u^2$; higher noise variance narrows $\lambda$ and degrades price discovery precision.
   - *Proposition 2 (Propagation of Informed Trading):* An increase in informed trading intensity at round $n$ sustains elevated expected order flow in subsequent rounds because residual uncertainty $\Sigma_n$ takes longer to resolve.
   - *Proposition 3 (Price Impact of Order Flow Innovations):* In any round $n$, $\mathbb{E}[\Delta p_n \mid \Delta y_n > 0] > 0$ whenever $\lambda_n > 0$.
   - *Proposition 4 (Horizon-Dependent Price Impact):* In the continuous-time limit (Kyle, 1985; Back, 1992), $\lambda(t) = \frac{\sqrt{\Sigma_0}}{2\sigma_u \sqrt{T-t}}$, so price impact accelerates as the public information revelation date $T$ approaches.

### Research interpretation

From a systematic alpha perspective, Aldridge's framework formalizes a **cross-sectional microstructure liquidity-reversion alpha**:
- **Signed volume vs. unsigned volume:** Standard quantitative factors often use raw turnover or dollar volume as liquidity controls. Aldridge demonstrates that unsigned volume is confounded; directional signed order flow ($\text{OF} = \text{VOL} \times \operatorname{sign}(\Delta P)$) carries the true structural signal of informed demand.
- **Exploiting adverse selection overshoot:** Rather than treating wide bid-ask spreads or high Kyle's $\lambda$ as uninvestable frictions to be avoided, a systematic contrarian liquidity-provision strategy identifies securities where $\lambda$ has widened due to transient noise-trader withdrawal, purchases the asset at the adverse-selection discount, and captures the mechanical price recovery as order flow normalizes.

## Signal

### 1. Daily Variable Construction

For each stock $i$ on trading day $\tau$:
- **Split-adjusted daily price change:** $\Delta \text{PRC}_{i\tau} = \text{PRC}_{i\tau} - \text{PRC}_{i,\tau-1}$ (adjusted via CRSP `DisFacPr`).
- **Daily dollar volume:** $\text{DVOL}_{i\tau} = \text{PRC}_{i\tau} \times \text{VOL}_{i\tau}$.
- **Daily signed order flow (Kyle proxy):**
  $$\text{OF}_{i\tau} = \text{VOL}_{i\tau} \times \operatorname{sign}(\Delta \text{PRC}_{i\tau})$$
- **Daily price impact (Amihud ratio):**
  $$\text{Amihud}_{i\tau} = \frac{|\text{RET}_{i\tau}|}{\text{DVOL}_{i\tau}}$$

### 2. Monthly Aggregated Features

For firm $i$ in calendar month $t$ over $n$ trading days ($\tau \in t$):
- **Total volume:**
  $$\text{sumvolume}_{it} = \sum_{\tau \in t} \text{VOL}_{i\tau}$$
- **Volume volatility (proxy for noise-trading variance $\sigma_u^2$):**
  $$\text{stdvolume}_{it} = \sqrt{\frac{1}{n-1} \sum_{\tau \in t} \big(\text{VOL}_{i\tau} - \overline{\text{VOL}}_i\big)^2}$$
- **Net signed order flow:**
  $$\text{signedflow}_{it} = \sum_{\tau \in t} \text{OF}_{i\tau}$$
- **Kyle's $\lambda$ regression estimator (Method B, signed regression):**
  $$\Delta \text{PRC}_{i\tau} = \hat{\lambda}_{it}^{\text{regression}} \cdot \text{OF}_{i\tau} + \eta_{i\tau}, \quad \tau \in t$$
  estimated via within-month OLS without intercept.
- **Kyle's $\lambda$ Amihud-style estimator (Method A, level):**
  $$\hat{\lambda}_{it}^{\text{Amihud}} = \frac{1}{n} \sum_{\tau \in t} \text{Amihud}_{i\tau}$$

### 3. Out-of-Sample Return Prediction & Portfolio Sort Signal

1. **Expanding-window training:** Initialized on the first 30% of chronological observations per firm.
2. **Rolling regression estimation:**
   $$\text{ActualReturn}_{it} = a_i + b_{1,i} r_{f,t} + b_{2,i} \hat{\lambda}_{it} + \epsilon_{it}$$
3. **One-month-ahead expected return forecast:**
   $$\hat{r}^{\text{pred}}_{i,t+1} = \hat{a}_i + \hat{b}_{1,i} r_{f,t} + \hat{b}_{2,i} \hat{\lambda}_{it}$$
4. **Portfolio sorting rule:** Rank all eligible firms cross-sectionally each month by $\hat{r}^{\text{pred}}_{i,t+1}$ (or directly by $-\hat{\lambda}_{it}$ / $\text{signedflow}_{it}$); enter long positions in the top decile (D10) and short positions in the bottom decile (D1).

## Required data

- **Universe:** US common equities listed on NYSE, AMEX, and NASDAQ (CRSP exchange codes 1, 2, 3).
- **Timeframe:** Daily trading data aggregated to monthly rebalancing frequency.
- **Sample period:** 2020-01-01 through 2025-12-01 (6 years, 72 calendar months, 58 out-of-sample monthly forecast evaluation periods).
- **CRSP daily fields:** Closing price (`DlyPrc`), daily trading volume (`DlyVol`), daily return (`DlyRet`), shares outstanding (`ShrOut`), price adjustment factor (`DisFacPr`), share adjustment factor (`DisFacShr`), bid (`DlyBid`), ask (`DlyAsk`).
- **External macroeconomic & factor data:** Monthly 13-week Treasury bill yield from Federal Reserve H.15 Statistical Release ($r_{f,t}$); Fama-French 3-factor and Carhart momentum returns (MKT, SMB, HML, MOM) for factor spanning tests.
- **Filters:**
  - Month-end price filter: $\text{PRC} \ge \$1.00$ to eliminate penny-stock microstructure noise.
  - Trading activity filter: At least 15 active trading days with non-zero volume within the month.
- **Outlier handling:** 1% and 99% two-tailed winsorization across all firm-month variables.

## Execution assumptions

- **Rebalancing frequency:** Monthly, at month-end closing prices.
- **Execution timing:** Signal computed using data up to the final trading day of month $t$; orders executed at the closing cross of month $t$, held through the close of month $t+1$.
- **Order types:** Market-on-close (MOC) or closing auction limit orders.
- **Transaction costs & frictions:** The primary research reports gross empirical returns without explicit deduction of bid-ask spreads, exchange fees, or short-borrow fees. The author notes that because $\hat{\lambda}_{it}$ directly captures price impact, execution algorithms must constrain turnover or trade passively to preserve alpha.
- **Borrow / shorting:** Unconstrained shorting assumed in long-short decile evaluations; real-world implementation would require hard-to-borrow screens for high-illiquidity securities.

## Evidence

### Source-reported

All empirical figures below are directly cited from Aldridge (2026), evaluated on the filtered CRSP universe (2020–2025):

#### 1. Sample Coverage & Summary Statistics (Tables 1–4)
- **Unique firms:** 9,893 point-in-time equities.
- **Total firm-month observations:** 448,393 post-filter observations (438,500 in clean baseline regressions; 329,252 to 337,722 in regressions with full controls).
- **Monthly equity returns:** Mean = $0.0204$ (2.04%/month), Std Dev = $0.3945$, Median = $0.0009$, Kurtosis = $4337.50$, Min = $-0.9806$, Max = $74.1961$.
- **Volume features:**
  - Sum volume: Mean = $25,104,816.66$, Std Dev = $58,617,786.50$, Median = $5,399,945.00$.
  - Volume standard deviation: Mean = $698,023.91$, Std Dev = $1,784,336.29$, Median = $140,154.56$.
  - Signed order flow: Mean = $927,410.24$, Std Dev = $11,956,241.76$, Median = $10,606.00$.
- **Kyle-Lambda estimators:**
  - $\hat{\lambda}^{\text{regression}}$: Mean = $9.631 \times 10^{-6}$, Median = $9.738 \times 10^{-7}$, Std Dev = $3.516 \times 10^{-5}$, Max = $0.0002816$.
  - $\hat{\lambda}^{\text{Amihud}}$: Mean = $6.775 \times 10^{-7}$, Median = $5.436 \times 10^{-9}$, Std Dev = $3.287 \times 10^{-6}$, Max = $2.66 \times 10^{-5}$.

#### 2. Model 1: Order Flow and Stock Return Regressions (Table 5)
- **Contemporaneous regression (without controls, $N = 438,500$):**
  - Sum Volume ($\beta_1$): $-6.319 \times 10^{-10}$ ($t = -33.92$, $p < 0.001$)
  - Std Dev Volume ($\beta_2$): $+2.594 \times 10^{-8}$ ($t = 40.70$, $p < 0.001$)
  - Signed Flow ($\beta_3$): $+6.33 \times 10^{-9}$ ($t = 121.70$, $p < 0.001$)
  - Intercept: $0.01229$ ($t = 19.40$), $R^2 = 0.0484$
- **One-month-ahead predictive regression (without controls, $N = 438,500$):**
  - Sum Volume ($\beta_1$): $-9.461 \times 10^{-11}$ ($t = -4.94$, $p < 0.001$)
  - Std Dev Volume ($\beta_2$): $+8.688 \times 10^{-9}$ ($t = 13.24$, $p < 0.001$)
  - Signed Flow ($\beta_3$): $-5.537 \times 10^{-10}$ ($t = -10.34$, $p < 0.001$)
  - Intercept: $0.01723$ ($t = 26.56$), $R^2 = 0.0007$
- **One-month-ahead predictive regression (with full controls, $N = 329,252$):**
  - Sum Volume ($\beta_1$): $-1.364 \times 10^{-10}$ ($t = -6.31$, $p < 0.001$)
  - Std Dev Volume ($\beta_2$): $+8.334 \times 10^{-9}$ ($t = 11.00$, $p < 0.001$)
  - Signed Flow ($\beta_3$): $-6.240 \times 10^{-10}$ ($t = -10.65$, $p < 0.001$)
  - Intercept: $0.01530$ ($t = 20.99$), $R^2 = 0.0031$

#### 3. Model 2: Kyle-Lambda Return Predictive Regressions (Tables 6 & 8)
- **With intercept ($N = 438,465$):**
  - $\hat{\lambda}^{\text{regression}}$ slope: $-101.2$ ($t = -6.46$, $p < 0.001$), Intercept = $0.02134$ ($t = 3.20$), $R^2 = 0.0001$.
  - $\hat{\lambda}^{\text{Amihud}}$ slope: $+136.1$ ($t = 0.48$, not significant), Intercept = $0.02027$ ($t = 3.03$), $R^2 = 0.0000$.
- **Uncentered ($N = 438,471$):**
  - $\hat{\lambda}^{\text{regression}}$ slope: $+53.69$ ($t = 1.30$, not significant), $R^2 = 0.0000$.
  - $\hat{\lambda}^{\text{Amihud}}$ slope: $+1355.0$ ($t = 4.08$, $p < 0.001$), $R^2 = 0.0001$.

#### 4. Out-of-Sample Fama-MacBeth Cross-Sectional Regressions (Table 10)
Over $T = 58$ monthly out-of-sample cross-sections:
- **$\hat{\lambda}^{\text{Amihud}}$ model:**
  - Average slope $\bar{\beta}$: $-0.0122$ ($t = -2.27$, Newey-West adjusted, $p < 0.05$)
  - Average intercept $\bar{\alpha}$: $+0.0130$ ($t = 1.65$, Newey-West adjusted, $p < 0.10$)
- **$\hat{\lambda}^{\text{regression}}$ model:**
  - Average slope $\bar{\beta}$: $-0.0050$ ($t = -2.25$, Newey-West adjusted, $p < 0.05$)
  - Average intercept $\bar{\alpha}$: $+0.0132$ ($t = 1.68$, Newey-West adjusted, $p < 0.10$)

#### 5. Simple Strategy Returns (Table 7)
- Mean monthly return across both Method A and Method B: $0.0209$ (2.09% per month), Std Dev = $0.3888$, Kurtosis = $4554.60$, Q1 = $-0.0609$, Median = $0.0000$, Q3 = $0.0598$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Specification fragility and sign instability:** The return predictability of $\hat{\lambda}_{it}$ flips sign between centered and uncentered models. When an intercept is included, $\hat{\lambda}^{\text{regression}}$ is strongly negative ($-101.2$, $t = -6.46$) while $\hat{\lambda}^{\text{Amihud}}$ is insignificant ($+136.1$, $t = 0.48$). Conversely, without an intercept, $\hat{\lambda}^{\text{Amihud}}$ becomes strongly positive ($+1355$, $t = 4.08$) while $\hat{\lambda}^{\text{regression}}$ loses significance ($+53.69$, $t = 1.30$). The author explicitly highlights this instability as an unresolved empirical puzzle.
- **Low predictive $R^2$:** Out-of-sample $R^2$ values for 1-month-ahead return predictions range from $0.0001$ to $0.0031$, showing that idiosyncratic monthly equity variance dominates predictive variance.
- **Gross-of-cost reporting:** Performance metrics do not incorporate transaction costs, bid-ask spreads, or short-borrowing fees. In highly illiquid small-cap equities where Kyle's $\lambda$ is largest, round-trip execution drag could significantly impair the gross return.

## Falsification plan

To test and potentially falsify the Aldridge order-flow and Kyle-lambda alpha hypothesis:

1. **Subperiod and Out-of-Sample Regime Stability Test:**
   - *Protocol:* Split the 2020–2025 panel into early pandemic/stimulus regime (2020–2022) and quantitative tightening/high-rate regime (2023–2025). Run Fama-MacBeth regressions independently across both halves.
   - *Falsification threshold:* If the Newey-West $t$-statistic of the cross-sectional slope $\bar{\beta}$ drops below $|t| < 1.96$ or flips sign in either subperiod, the reported cross-sectional predictability is an artifact of sample pooling rather than a structural asset pricing mechanism.
2. **Intraday Tick-Level Order Flow vs. Daily Proxy Ablation:**
   - *Protocol:* Replace the daily sign proxy $\text{OF}_{i\tau} = \text{VOL}_{i\tau} \times \operatorname{sign}(\Delta \text{PRC}_{i\tau})$ with true tick-level aggressor order flow from NYSE TAQ (Lee-Ready algorithm signed volume).
   - *Falsification threshold:* If the TAQ-derived true signed order flow produces a lower Information Coefficient (IC) or insignificant Fama-MacBeth slope compared to the crude daily price-change heuristic, the empirical effect is driven by daily price momentum/reversal artifacts rather than genuine order flow price impact.
3. **Transaction Cost and Capacity Stress Test:**
   - *Protocol:* Simulate the decile long-short strategy applying realistic size-dependent transaction costs: 5 bps for large caps, 15 bps for mid caps, 35 bps for small caps, plus borrow fees for hard-to-borrow short legs.
   - *Falsification threshold:* If net Sharpe ratio drops below zero after deducting realistic trading costs and borrow fees, the strategy fails the tradability criterion.
4. **Factor Spanning and Characteristic Residualization:**
   - *Protocol:* Regress long-short decile returns on the Fama-French 5-factor model plus Carhart momentum and short-term reversal factors.
   - *Falsification threshold:* If the multi-factor alpha $\alpha_{\text{FF5+MOM+REV}}$ is statistically indistinguishable from zero ($p > 0.05$), the Kyle-lambda signal provides no incremental alpha beyond existing size, illiquidity, and reversal anomalies.

## Crypto portability

**Portability Classification: Adapted / Unproven.**

The empirical results in Aldridge (2026) were established exclusively on US equities (CRSP, 2020–2025). Porting this mechanism to cryptocurrency markets involves several important adaptations:

1. **Native Trade Aggressor Data (No Sign Proxy Needed):** Unlike equities where order direction must be inferred (e.g. Lee-Ready or daily price-change sign), cryptocurrency centralized exchanges (Binance, Bybit, OKX) stream real-time trade feeds with explicit taker side flags (`is_buyer_maker`). This allows direct, exact measurement of Kyle's order flow $y_\tau$ at sub-minute resolutions without relying on the heuristic $\operatorname{sign}(\Delta P)$.
2. **Perpetual Funding Rate Confounding:** In crypto perpetual futures, price deviations from the spot index generate funding rate cash flows every 1 to 8 hours. An apparent adverse selection price discount (wide $\lambda$) may be caused by negative funding rate arbitrage rather than fundamental information asymmetry. Effective drift must subtract funding payments.
3. **Continuous 24/7 Trading and Absence of Closing Auctions:** Equity rebalancing relies heavily on closing auctions (MOC orders). Crypto operates continuously without session boundaries, eliminating opening/closing auction effects but increasing exposure to weekend liquidity dry-ups.
4. **Extreme Volatility and Tail Jumps:** Crypto assets violate Kyle's (1985) normality assumptions on terminal liquidation values $v \sim N(p_0, \Sigma_0)$ and noise trading $u \sim N(0, \sigma_u^2)$, exhibiting heavy power-law tails and jump cascades that require robust non-Gaussian filtering.

## Limitations

- **Daily Sign Heuristic:** The paper's primary empirical measure approximates Kyle's latent order flow using daily volume multiplied by the sign of daily price change ($\text{VOL} \times \operatorname{sign}(\Delta P)$), which collapses intraday order flow dynamics.
- **Specification Sensitivity:** The drastic sign and significance change of Kyle's $\lambda$ between centered and uncentered models indicates substantial multicollinearity with the intercept.
- **Frictionless Backtesting:** Empirical strategy returns are reported gross of transaction costs, slippage, and short-borrow fees.
- **CRSP Equity Specificity:** The empirical evidence is confined to US equities; performance in alternative asset classes (FX, commodities, crypto) remains unproven.

## Implementation status

- `implementation_status: not-implemented`
- This record captures upstream academic research only.
- No implementation has been created in PyBroker, NautilusTrader, paper trading, testnet, or live trading workflows.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize strategy implementation, backtesting promotion, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]` — High-frequency intra-second Kyle's lambda price impact and order book resilience in crypto perpetuals.
- `[[quant/crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]` — Cross-sectional Amihud illiquidity factor in crypto markets.
- `[[quant/order-flow-matched-filter-normalization-investor-segmentation-2026-09-02]]` — Matched-filter order flow normalization for institutional vs retail flow segmentation.
- `[[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]]` — Passive market impact and multi-level order flow imbalance modeling.
- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]` — Intraday multi-level order flow imbalance forecasting.

## Sources

- **Primary paper:** Irene Aldridge, *Liquidity Premium and Investment Horizons*, arXiv preprint `arXiv:2607.01377v1 [econ.EM, q-fin.PR, q-fin.ST, q-fin.TR]`, submitted July 2, 2026. DOI: `10.48550/arXiv.2607.01377`.
  - Abstract & metadata: https://arxiv.org/abs/2607.01377
  - Full-text HTML5: https://arxiv.org/html/2607.01377v1
  - PDF version: https://arxiv.org/pdf/2607.01377
  - Primary TeX source bundle: https://arxiv.org/src/2607.01377
- **Foundational literature cited within primary source:**
  - A. S. Kyle (1985), *Continuous auctions and insider trading*, Econometrica 53(6), 1315–1335. DOI: `10.2307/1913210`.
  - G. M. Constantinides (1986), *Capital market equilibrium with transaction costs*, Journal of Political Economy 94(4), 842–862.
  - Y. Amihud and H. Mendelson (1986), *Asset pricing and the bid-ask spread*, Journal of Financial Economics 17(2), 223–249. DOI: `10.1016/0304-405X(86)90065-6`.
  - Y. Amihud (2002), *Illiquidity and stock returns: cross-section and time-series effects*, Journal of Financial Markets 5(1), 31–56. DOI: `10.1016/S1386-4181(01)00024-6`.
  - D. Easley, N. M. Kiefer, M. O'Hara, and J. B. Paperman (1996), *Liquidity, information, and infrequently traded stocks*, The Journal of Finance 51(4), 1405–1436.
  - L. R. Glosten and P. R. Milgrom (1985), *Bid, ask and transaction prices in a specialist market with heterogeneously informed traders*, Journal of Financial Economics 14(1), 71–100. DOI: `10.1016/0304-405X(85)90044-3`.
  - K. Back (1992), *Insider trading in continuous time*, The Review of Financial Studies 5(3), 387–409. DOI: `10.1093/rfs/5.3.387`.
  - K. Back and S. Baruch (2004), *Information in securities markets: Kyle meets Glosten and Milgrom*, Econometrica 72(2), 433–465. DOI: `10.1111/j.1468-0262.2004.00497.x`.
  - E. F. Fama and K. R. French (1988), *Permanent and temporary components of stock prices*, Journal of Political Economy 96(2), 246–273.
  - L. Pastor and R. F. Stambaugh (2003), *Liquidity risk and expected stock returns*, Journal of Political Economy 111(3), 642–685. DOI: `10.1086/374184`.
  - V. V. Acharya and L. H. Pedersen (2005), *Asset pricing with liquidity risk*, Journal of Financial Economics 77(2), 375–410. DOI: `10.1016/j.jfineco.2004.06.007`.
  - A. W. Lo and J. Wang (2015), *Trading volume: definitions, data analysis, and implications of portfolio theory*, The Review of Financial Studies 13(2), 257–300. DOI: `10.1093/rfs/13.2.257`.
