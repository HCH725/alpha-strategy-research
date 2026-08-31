---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Cumulative Prospect Theory Value Factor
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - behavioral
  - prospect-theory
  - lottery-preference
  - anomaly
status: research-only
confidence: medium
source_as_of: 2024-01-23
sources:
  - "https://ssrn.com/abstract=3753530"
  - "https://doi.org/10.2139/ssrn.3753530"
  - "https://doi.org/10.1108/RBF-07-2023-0172"
  - "https://doi.org/10.1016/j.jfineco.2016.01.001"
  - "https://doi.org/10.1007/BF00122574"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Cumulative Prospect Theory Value Factor

## Provenance

This record uses two **distinct** empirical crypto sources that must not be conflated:

1. **Alexander Thoma**, *A Prospect Theory Model for Predicting Cryptocurrency Returns*, SSRN Working Paper 3753530 (2020/2021), https://ssrn.com/abstract=3753530 / https://doi.org/10.2139/ssrn.3753530. Thoma studies a large body of cryptocurrencies from 2014 to 2020 and reports that high (low) prospect theory value predicts low (high) subsequent returns, with significant factor-model alpha and probability weighting as an important driver.
2. **Manisha Yadav**, *Behavioral biases of cryptocurrency investors: a prospect theory model to explain cryptocurrency returns*, *Review of Behavioral Finance* 16(4), 643–667 (2024), https://doi.org/10.1108/RBF-07-2023-0172. Yadav analyzes 1,629 cryptocurrencies representing more than 95% of the cryptocurrency market and uses univariate/bivariate portfolio sorts, OLS, panel methods, and quantile regression; the paper reports an inverse PTV-return relation with stronger effects among smaller, high-volatility, illiquid cryptocurrencies and a dominant probability-weighting component.

The theoretical foundation builds directly on the Cumulative Prospect Theory (CPT) asset pricing framework of Nicholas Barberis, Abhiroop Mukherjee, and Baolian Wang, *Prospect Theory and Stock Returns: An Empirical Test*, *Journal of Financial Economics* 119(3), 2016, pp. 637-668 (DOI: https://doi.org/10.1016/j.jfineco.2016.01.001) and Daniel Kahneman and Amos Tversky, *Advances in Prospect Theory: Cumulative Representation of Uncertainty*, *Journal of Risk and Uncertainty* 5(4), 1992, pp. 297-323 (DOI: https://doi.org/10.1007/BF00122574).

Exact point-in-time constituent rules, missing-price handling, delisting conventions, and implementable exchange-level universe filters remain **underspecified** for this research record and must be independently reconstructed before backtesting.

## Economic mechanism

### Source-reported

Thoma (2020/2021) applies Prospect Theory Value to cryptocurrency returns and reports that high-PTV cryptocurrencies subsequently earn lower returns while low-PTV cryptocurrencies subsequently earn higher returns. Thoma also reports that high-PTV cryptocurrencies tend to be highly positively skewed and that mechanical tests identify probability weighting as an important driver of the signal.

Yadav (2024) independently studies the PTV-return relationship in a much larger explicitly reported cross-section of 1,629 cryptocurrencies. Yadav reports the same average inverse relation, asymmetry across return-distribution quantiles, stronger predictability among smaller/high-volatility/illiquid cryptocurrencies, and a dominant role for the probability-weighting component.

The lottery-demand / speculative-overpricing mechanism is therefore a **research interpretation consistent with both sources**, not a claim that either paper directly observes investor motives or a specific causal flow from retail buying to fundamental-value correction.

### Research interpretation

The falsifiable hypothesis is that **retail cognitive biases modeled by Cumulative Prospect Theory create systematic cross-sectional mispricing across crypto assets**:

1. **Lottery Overpricing via Probability Weighting ($w^+$)**: Because investors overweight low-probability extreme gains, assets with historical return distributions featuring extreme positive jumps receive elevated subjective valuations ($PTV$) relative to their objective expected payoff. This generates negative forward excess returns as speculative exuberance unwinds.
2. **Underpricing of Unattractive/Low-PTV Distributions**: Cryptocurrencies with low subjective prospect value (e.g. steady return profiles or uncompensated downside dispersion) are neglected by retail speculators, creating a persistent positive forward drift when sorted into long-only or long/short factor portfolios.
3. **Firm-Size and Liquidity Conditioning**: The mispricing is hypothesized to be most pronounced among small, volatile, and illiquid tokens where retail participation is highest and institutional arbitrage capital is absent.

## Signal

The signal computation follows the Barberis-Mukherjee-Wang (2016) CPT formulation as applied to cryptocurrency returns in the Thoma and Yadav research family. The exact production implementation below remains a **research reconstruction**, not an independently reproduced replication.

1. **Universe & Lookback Window:** For each cryptocurrency $i$ on day $t-1$, collect the past $K = 30$ daily returns:
   $$\{r_{i,t-30}, r_{i,t-29}, \dots, r_{i,t-1}\}$$
   Here $K=30$ is retained as a **proposed research parameter** from the prior capture. It must be checked against the primary full-text methodology and independently reproduced before being treated as a source-prescribed constant.

2. **Order Statistics:** Sort the historical returns in ascending order:
   $$r_{(1)} \le r_{(2)} \le \dots \le r_{(m)} < 0 \le r_{(m+1)} \le \dots \le r_{(K)}$$
   where $m$ is the count of strictly negative daily returns, and $K - m$ is the count of non-negative returns. Each historical return is treated as having equal historical probability $p_k = 1/K$.

3. **Piecewise Value Function:** Apply the Tversky-Kahneman (1992) value function centered at a zero-return reference point ($r_0 = 0$):
   $$v(r) = \begin{cases} r^\alpha & \text{if } r \ge 0 \\ -\lambda (-r)^\beta & \text{if } r < 0 \end{cases}$$
   where canonical parameter values are $\alpha = \beta = 0.88$, and loss-aversion coefficient $\lambda = 2.25$.

4. **Cumulative Probability Weighting:** Apply the Tversky-Kahneman probability weighting functions:
   - For gains ($r \ge 0$):
     $$w^+(p) = \frac{p^\gamma}{\left(p^\gamma + (1-p)^\gamma\right)^{1/\gamma}} \quad (\gamma = 0.61)$$
   - For losses ($r < 0$):
     $$w^-(p) = \frac{p^\delta}{\left(p^\delta + (1-p)^\delta\right)^{1/\delta}} \quad (\delta = 0.69)$$

5. **Decision Weights ($\pi$):** Compute rank-dependent decision weights:
   - For gains ($k = m+1, \dots, K$):
     $$\pi^+_k = w^+\left(\frac{K - k + 1}{K}\right) - w^+\left(\frac{K - k}{K}\right)$$
   - For losses ($k = 1, \dots, m$):
     $$\pi^-_k = w^-\left(\frac{k}{K}\right) - w^-\left(\frac{k - 1}{K}\right)$$

6. **Prospect Theory Value Score:**
   $$PTV_{i,t-1} = \sum_{k=1}^m v(r_{(k)}) \pi^-_k + \sum_{k=m+1}^K v(r_{(k)}) \pi^+_k$$

7. **Portfolio Formation & Rebalancing:**
   - At each daily boundary $t-1$, sort all eligible universe constituents into deciles based on $PTV_{i,t-1}$.
   - **Long:** Decile 1 (Lowest PTV / Underbought).
   - **Short:** Decile 10 (Highest PTV / Overbought Lottery Assets).
   - Equal-weighted or market-cap-weighted portfolio construction; rebalanced daily for the $t$ to $t+1$ holding interval.

## Required data

- Point-in-time cryptocurrency universe membership and daily close prices (UTC 00:00 boundary recommended).
- Minimum history of 30 consecutive daily return observations per candidate asset prior to signal formation date $t-1$.
- Point-in-time daily market capitalization and 24-hour volume for liquidity screening and value-weighting.
- Survivorship-bias-free database including delisted, defunct, and bankrupt tokens across the 2014–2026 period.
- Standard benchmark market returns and multi-factor series (e.g. Size, Momentum, Value) for cross-sectional factor alpha regressions.

## Execution assumptions

The empirical sources evaluate statistical predictability and portfolio relationships without specifying a complete institutional execution architecture for this repository.

Material assumptions that remain **underspecified** in the source include:

- **Short-Sale Feasibility:** The strategy assumes short positions in Decile 10 (highest PTV). In practice, high-PTV assets are frequently micro-cap or illiquid altcoins with no borrow market, no perpetual futures listing, or prohibitive borrow fees.
- **Execution Timing:** Signals formed using data through day $t-1$; execution assumed at day $t$ open or close. Intraday execution slippage and latency are not modeled.
- **Transaction Costs & Turnover:** Daily decile rebalancing generates substantial turnover. The source does not incorporate bid-ask spreads, exchange maker/taker fees, or market impact.
- **Capacity Constraints:** High-PTV and low-PTV decile constituents in the broad universe include low-liquidity coins with minimal trading capacity.

## Evidence

### Source-reported

**Thoma (2020/2021):**
- Uses a large body of cryptocurrencies covering 2014–2020.
- Reports that high (low) PTV cryptocurrencies earn low (high) subsequent returns.
- Reports strong strategy outperformance even after controlling for known predictors and significant alpha in cryptocurrency three-factor regressions.
- Reports that high-PTV cryptocurrencies tend to be highly positively skewed and that probability weighting is an important driver in mechanical tests of the model.

**Yadav (2024):**
- Analyzes 1,629 cryptocurrencies representing more than 95% of the cryptocurrency market.
- Uses univariate and bivariate portfolio sorts with equal-weighted and value-weighted portfolios, plus OLS, panel-data methods, and quantile regression.
- Reports an average inverse relationship between PTV and subsequent cryptocurrency returns, with asymmetric effects across quantiles.
- Reports more robust PTV predictability among smaller cryptocurrencies characterized by high volatility and illiquidity, and identifies probability weighting as the dominant PT component.

These claims are deliberately separated by source; they must not be recombined into a synthetic sample, methodology, or result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Transaction costs and bid-ask spreads in small-cap crypto markets can be large enough to erase daily rebalancing alpha; the magnitude must be measured from the actual point-in-time execution universe rather than assumed.
- Shorting the top PTV decile is severely constrained in real-world trading, potentially reducing the strategy to a long-only low-PTV screen or requiring perpetual futures restriction.
- Factor redundancy remains an open risk: PTV may overlap materially with MAX, idiosyncratic skewness, or other lottery-demand proxies. This record does not claim external evidence of decay or spanning unless a specific source is added and attributed.

## Falsification plan

1. **Out-of-Sample Validation:** Test the $PTV$ ranking model on an untouched sample from 2021 to 2026 across Binance, Bybit, and OKX spot/perpetual universes.
2. **Ablation & Factor Spanning Tests:**
   - Run Fama-MacBeth regressions including MAX (maximum daily return over 30 days), idiosyncratic skewness (ISKEW), idiosyncratic volatility (IVOL), size (SMB), and momentum.
   - Test whether $PTV$ retains orthogonal predictive alpha after controlling for MAX and Salience Theory Value (STV). If $t(\alpha) < 2.0$, reject $PTV$ as an independent factor.
3. **Long-Only Decile 1 Viability:** Evaluate whether the long-only Decile 1 portfolio produces positive risk-adjusted alpha against a Bitcoin / equal-weight crypto benchmark without relying on shorting Decile 10.
4. **Frictions & Cost Stress-Test:** Apply realistic taker fee schedules (5 bps maker / 10 bps taker) and empirical bid-ask spread models. If the net Sharpe ratio drops below zero, reject executable implementation.
5. **Universe Robustness:** Test whether $PTV$ alpha survives when restricted to the top 100 liquid coins versus the unconstrained micro-cap universe.

## Crypto portability

**direct** for the underlying research mechanism, as the primary source specifically investigates the cryptocurrency market cross-section.

Implementation portability to production environments requires adaptations:
- **Perpetual Universe Restriction:** To enable true long/short execution, the universe must be filtered to assets with active perpetual futures contracts and verified borrow/funding availability.
- **Rebalancing Frequency Smoothing:** Daily rebalancing may need replacement with 3-day or 7-day rolling horizons or threshold rebalancing to manage turnover costs.
- **Parameter Calibration:** The classical Tversky-Kahneman (1992) equity parameters ($\alpha=0.88, \lambda=2.25, \gamma=0.61, \delta=0.69$) were calibrated on human lab experiments; crypto-specific structural parameters remain **unproven**.

## Limitations

- **not independently reproduced**.
- **execution frictions:** Shorting high-PTV coins in the broader universe is practically infeasible for most altcoins.
- **turnover sensitivity:** Daily decile sorting incurs heavy turnover that may eliminate gross alpha net of fees and slippage.
- **underspecified:** Exact point-in-time liquidity filters and delisting return accounting in the primary paper are not fully detailed.
- **factor redundancy risk:** $PTV$ may partially overlap with MAX (lottery momentum) or idiosyncratic skewness.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, strategy registry, Paper, Testnet, or Live has been performed in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this Scout cycle. Do not fabricate one.

Related strategy families in this repository include:
- `crypto-cross-sectional-salience-theory-value-factor-2026-09-01.md` (Salience Theory)
- `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31.md` (MAX Lottery Momentum)
- `crypto-cross-sectional-idiosyncratic-skewness-2026-08-31.md` (Idiosyncratic Skewness)

## Sources

1. Alexander Thoma, *A Prospect Theory Model for Predicting Cryptocurrency Returns*, SSRN Working Paper 3753530 (2020/2021): https://ssrn.com/abstract=3753530 ; DOI: https://doi.org/10.2139/ssrn.3753530
2. Manisha Yadav, *Behavioral biases of cryptocurrency investors: a prospect theory model to explain cryptocurrency returns*, *Review of Behavioral Finance* 16(4), pp. 643–667 (2024): https://doi.org/10.1108/RBF-07-2023-0172
3. Nicholas Barberis, Abhiroop Mukherjee, and Baolian Wang, *Prospect Theory and Stock Returns: An Empirical Test*, *Journal of Financial Economics* 119(3), pp. 637-668 (2016): https://doi.org/10.1016/j.jfineco.2016.01.001
4. Daniel Kahneman and Amos Tversky, *Advances in Prospect Theory: Cumulative Representation of Uncertainty*, *Journal of Risk and Uncertainty* 5(4), pp. 297-323 (1992): https://doi.org/10.1007/BF00122574
