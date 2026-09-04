---
schema: strategy-research-record-v1
title: "Crypto Walk-Forward Window Optimization and Double Out-of-Sample Momentum: Parameterization, Cost Attrition, and Active-Passive Diversification"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - walk-forward-optimization
  - double-out-of-sample
  - momentum
  - moving-average-crossover
  - transaction-costs
  - active-passive-diversification
status: research-only
confidence: high
source_as_of: 2026-02-11
sources:
  - "arXiv:2602.10785v1 [q-fin.TR, q-fin.MF, q-fin.PM], February 11 2026. https://arxiv.org/abs/2602.10785"
  - "https://github.com/tmr-crypto/wf_optim_crypto_analysis/tree/a9b4d8d09da162c970253c0b8cb5e5b3f2400444"
  - "https://github.com/tmr-crypto/wf_optim_crypto/tree/8be3ecf0019e991962f6f59bf9938cfa56411350"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Walk-Forward Window Optimization and Double Out-of-Sample Momentum: Parameterization, Cost Attrition, and Active-Passive Diversification

## Provenance

- **Primary Source:** Tomasz Mroziewicz and Robert Ślepaczuk (Quantitative Finance Research Group, Faculty of Economic Sciences, University of Warsaw), *"A novel approach to trading strategy parameter optimization, using double out-of-sample data and walk-forward techniques"*, arXiv preprint `arXiv:2602.10785v1 [q-fin.TR, q-fin.MF, q-fin.PM]`, submitted February 11, 2026.
- **Canonical DOI:** [10.48550/arXiv.2602.10785](https://doi.org/10.48550/arXiv.2602.10785)
- **Stable Abstract URL:** [https://arxiv.org/abs/2602.10785](https://arxiv.org/abs/2602.10785)
- **Full Text HTML:** [https://arxiv.org/html/2602.10785v1](https://arxiv.org/html/2602.10785v1)
- **Companion Repositories (Public, Open Source):**
  - Analysis & Reporting: `https://github.com/tmr-crypto/wf_optim_crypto_analysis` (immutable commit `a9b4d8d09da162c970253c0b8cb5e5b3f2400444`)
  - Data Pipeline & Backtesting Engine: `https://github.com/tmr-crypto/wf_optim_crypto` (immutable commit `8be3ecf0019e991962f6f59bf9938cfa56411350`)
- **Data Examined:**
  - Kaggle G-Forecast cryptocurrency competition dataset: 1-minute intraday prices for Bitcoin (BTC), Ethereum (ETH), and Binance Coin (BNB).
  - Global Training Data Period: February 8, 2018 to September 1, 2019 (19 months).
  - Unseen Data Period (Strict Single-Time Evaluation): November 7, 2019 to August 22, 2021 (21.5 months).

## Economic mechanism

### Source-reported

The paper investigates whether technical momentum strategies (specifically Exponential Moving Average [EMA] crossovers) combined with an optimized walk-forward framework can extract persistent, statistically significant risk-adjusted returns net of transaction fees on intraday cryptocurrency markets.

The authors evaluate three foundational research questions:
1. **Walk-forward window parameterization:** Whether the lengths of training ($T_{train}$) and testing ($T_{test}$) windows in walk-forward optimization materially determine investor outcomes, directly challenging the Efficient Market Hypothesis (Fama 1965) which predicts window length variations should yield no systematic edge.
2. **Frequency dependency and transaction cost attrition:** How sampling frequency (1 to 60 minutes) interacts with realistic exchange transaction fees (0.10% per transaction, 0.20% per round-trip turnaround), identifying the exact break-even cost and the minimum viable candle resolution.
3. **Active-passive diversification:** Whether combining an active trend-following momentum strategy with a passive Buy-and-Hold portfolio produces structural diversification benefits, dampening drawdowns while preserving capital growth across market cycles.

### Research interpretation

The empirical results document four structural market phenomena:
1. **Microstructure friction threshold in crypto momentum:** At high intraday sampling frequencies ($\le 30$ minutes), bid-ask crossing and exchange taker fees rapidly overwhelm trend signals. The strategy's mean Sharpe ratio is catastrophic at 1-minute ($-12.71$) and 5-minute ($-2.84$) resolutions, turning consistently positive only at the 60-minute interval (mean Sharpe $+0.79$).
2. **Payoff asymmetry and crash protection:** Active EMA momentum acts as an asymmetric hedge. It delivers positive returns during severe market declines and volatility spikes (e.g., the March 2020 liquidity shock), but suffers steady attrition and underperformance during strong, prolonged bull runs (e.g., 2021) and low-volatility consolidation regimes.
3. **Double out-of-sample parameter decay and boundary instability:** The top in-sample parameter set (WF 7/28, residing on the search grid boundary) degraded substantially out-of-sample ($-30\%$ Sharpe drop on unseen BTC data), whereas the centrally located interior set (WF 14/10) demonstrated superior generalization across BTC, ETH, and BNB, outperforming Buy-and-Hold in Information Ratio and downside risk.
4. **Active-passive convexity lift:** Blending equal weights of passive Buy-and-Hold and active walk-forward momentum across assets reduced maximum portfolio drawdown from $68.3\%$ to $43.8\%$ and lifted the portfolio Sharpe ratio to $1.921$ (vs. $1.542$ for pure Buy-and-Hold), confirming that trend-following provides valuable downside non-correlation during cryptocurrency market crashes.

## Signal

The trading logic is fully specified in the primary manuscript and open-source codebase (`master/rcode/logic/strategy.r`):

### Indicator Construction
- Primary Indicator: Two Exponential Moving Averages (EMA), fast and slow.
- Recursive formulation (`source-reported`):
  $$EMA_t(N) = \alpha \cdot P_t + (1 - \alpha) \cdot EMA_{t-1}(N), \quad \alpha = \frac{2}{N + 1}$$
- Parameter Search Universe (`source-reported`):
  - Candidate periods: $N \in \{5, 7, 10, 15, 20, 30, 40, 50, 100, 150, 200\}$.
  - Fast EMAs: $N_{fast} \le 35 \implies \{5, 7, 10, 15, 20, 30\}$ (6 candidates).
  - Slow EMAs: $N_{slow} > 35 \implies \{40, 50, 100, 150, 200\}$ (5 candidates).
  - Total fast/slow combinations evaluated per training slice: $6 \times 5 = 30$ candidate pairs.

### Causal Execution & Position Formulation
- Signal Formation Timestamp (`source-reported`): End of each 60-minute candle bar.
- Causal Lag Rule (`source-reported`): Evaluated using 1-bar lagged EMA values to eliminate lookahead bias:
  $$Pos_t = \begin{cases} +1.0 & \text{if } EMA_{fast, t-1} > EMA_{slow, t-1} \quad (\text{Long}) \\ -1.0 & \text{if } EMA_{fast, t-1} \le EMA_{slow, t-1} \quad (\text{Short}) \end{cases}$$
- Reversal Execution (`source-reported`): Continuous market exposure (never neutral in standalone strategy). A change from $+1$ to $-1$ triggers closing the long position and immediately opening the short position, incurring 2 transaction fee charges.
- Position Sizing (`source-reported`): Fixed 1.0 unit exposure (100% equity allocated without leverage).

### Walk-Forward Optimization & 2D Smoothing
- Window Candidates (`source-reported`): Both training ($T_{train}$) and testing ($T_{test}$) lengths are chosen from $\{1, 2, 3, 5, 7, 10, 14, 21, 28\}$ days ($9 \times 9 = 81$ grid combinations).
- Step Execution (`source-reported`):
  1. For each window pair $(T_{train}, T_{test})$, historical data is partitioned into rolling steps of length $T_{train} + T_{test}$.
  2. Inside each step's training segment, the 30 EMA pairs are evaluated; the pair $(N_{fast}^*, N_{slow}^*)$ maximizing Sharpe is selected.
  3. The chosen pair is executed on the out-of-sample testing segment of length $T_{test}$.
  4. Testing segment returns are concatenated across the entire global training period to calculate the unpenalized walk-forward Sharpe ratio.
- 2D Robust Sharpe Filter (`source-reported`):
  $$\text{Robust Sharpe}_{i,j} = \frac{1}{2} \cdot \text{Sharpe}_{i,j} + \frac{1}{2} \cdot \left(\frac{1}{k} \sum_{m \in \mathcal{N}(i,j)} \text{Sharpe}_m\right)$$
  where $\mathcal{N}(i,j)$ represents the set of $k$ adjacent neighboring grid cells ($k \in [3, 8]$ depending on interior vs. boundary location).
- Selected Training Parameter Sets (`source-reported`):
  1. **WF 7/28:** $T_{train} = 7\text{ days}$, $T_{test} = 28\text{ days}$ (grid peak on upper boundary).
  2. **WF 14/10:** $T_{train} = 14\text{ days}$, $T_{test} = 10\text{ days}$ (interior robust peak).

## Required data

- **Instruments (`source-reported`):** Bitcoin (BTC), Ethereum (ETH), Binance Coin (BNB).
- **Market Type (`source-reported`):** Cryptocurrency spot cash markets (derived from the public Kaggle G-Forecast dataset).
- **Timeframe & Sampling (`source-reported`):** 60-minute OHLCV candles, resampled from raw 1-minute timestamps.
- **Fields Used (`source-reported`):** Close price ($P_t$), log returns $R_t = \ln(P_t / P_{t-1})$.
- **Point-in-Time Availability (`source-reported`):** Strictly causal via 1-period lagged EMA indicators (`lag.xts()`) evaluated at bar completion.
- **Missing Data Handling (`source-reported`):** Missing price ticks imputed via forward-fill (`na.locf`); EMA warm-up window requires $N_{max} = 200$ bars before signal generation commences.

## Execution assumptions

- **Execution Timing (`source-reported`):** Trade initiated at the close/open boundary following the completion of the 60-minute bar.
- **Fill Model (`source-reported`):** Immediate fill at recorded candle price without modeled queue delay.
- **Transaction Costs (`source-reported`):**
  - Baseline: $0.10\%$ ($10\text{ bps}$) per transaction.
  - Position reversal ($+1 \to -1$ or $-1 \to +1$): Incurs $2 \times 0.10\% = 0.20\%$ ($20\text{ bps}$).
  - Slippage and bid-ask spread: Explicitly subsumed within the $0.10\%$ conservative fee buffer.
- **Shorting Mechanism:**
  - Assumed costless continuous short execution in the primary simulation (`source-reported`).
  - In actual spot cryptocurrency markets, continuous short exposure requires borrow availability and margin interest; for perpetual futures, shorting is native but subject to 8-hour funding rates (`research-proposed`).
- **Leverage (`source-reported`):** 1.0x (unlevered).

## Evidence

### Source-reported

All figures below are directly reported by Tomasz Mroziewicz and Robert Ślepaczuk (`arXiv:2602.10785v1`, February 2026) and verified from the author's primary LaTeX source (`publikacja_20260211.tex`):

#### 1. Sampling Frequency vs. Sharpe Ratio (Table 3, Global Train Period, Feb 2018 – Sep 2019, 81 WF Combinations per Freq, 0.1% Fee)
| Frequency | Mean Sharpe | Max Sharpe | Min Sharpe | Std Sharpe | Q25% Sharpe | Q50% Sharpe | Q75% Sharpe |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1-Minute** | -12.7144 | -11.4142 | -16.6509 | 1.0943 | -12.7549 | -12.5585 | -12.1700 |
| **5-Minute** | -2.8416 | -1.6011 | -5.0528 | 0.8268 | -3.0947 | -2.6447 | -2.3863 |
| **10-Minute** | -1.4896 | -0.4917 | -2.9345 | 0.6626 | -1.9249 | -1.4718 | -1.0263 |
| **15-Minute** | -0.9783 | +0.1951 | -2.7203 | 0.7177 | -1.1952 | -0.7957 | -0.5273 |
| **30-Minute** | -0.4954 | +0.7372 | -2.1529 | 0.6440 | -0.9490 | -0.4528 | -0.1158 |
| **60-Minute** | **+0.7908** | **+1.2524** | **+0.1863** | 0.2256 | +0.6479 | +0.8124 | +0.9540 |

#### 2. Top Walk-Forward Strategies on Bitcoin Global Training Data (Table 4, 60-Minute Freq, 0.1% Fee)
| Strategy Description | Ann Mean Return | Ann Volatility | Sharpe Ratio | Information Ratio** | Max Drawdown | Sortino Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **BTC Train 7 Test 28** | 0.9483 | 0.7572 | **1.252** | **4.622** | **0.3516** | **1.799** |
| **BTC Train 14 Test 10** | 0.8918 | 0.7571 | 1.178 | 2.902 | 0.4513 | 1.678 |

*Note: $\text{Information Ratio}^{**} = \frac{\text{sign}(\text{Mean}) \cdot (\text{Mean})^2}{\text{Vol} \cdot \text{MaxDD}}$ following Ryś & Ślepaczuk (2019).*

#### 3. Statistical Significance Testing via Bootstrapping (1,000 Iterations, Tables 5, 6, 7, 8)
- **Subsampled EMA Parameter Bootstrap (Tables 5 & 6):**
  - Train 7 Test 28: Original Sharpe $1.252$, Bootstrap Mean $0.7847$, Bootstrap SD $0.3259$, Max $1.777$; 80 iterations higher ($p = 0.080$, not significant at 5%).
  - Train 14 Test 10: Original Sharpe $1.178$, Bootstrap Mean $0.7901$, Bootstrap SD $0.3448$, Max $1.716$; 137 iterations higher ($p = 0.137$, not significant at 5%).
  - Finding: Original Sharpe falls within 1 standard deviation of random EMA selection, indicating in-sample EMA parameter selection does not beat random selection within the candidate set.
- **Shuffled Transaction Blocks Bootstrap (Tables 7 & 8):**
  - Train 7 Test 28: Original Sharpe $1.252$, Bootstrap Mean $-0.2373$, Bootstrap SD $0.8083$, Min $-2.789$, Max $2.273$; 35 iterations higher (**$p = 0.035$, significant at 5%**).
  - Train 14 Test 10: Original Sharpe $1.178$, Bootstrap Mean $-0.1737$, Bootstrap SD $0.8012$, Min $-3.098$, Max $2.721$; 44 iterations higher (**$p = 0.044$, significant at 5%**).
  - Finding: The strategy's execution timing significantly rejects the null hypothesis of zero timing skill against random trade ordering ($p < 0.05$).

#### 4. Cost Sensitivity on BTC Global Training Data (Table 9, WF 7/28)
| Cost Level / Trade | Ann Mean Return | Ann Volatility | Sharpe Ratio | Information Ratio** | Max Drawdown | Sortino Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.05%** | 1.1068 | 0.7569 | 1.4623 | 6.6457 | 0.3408 | 2.1035 |
| **0.07%** | 1.0419 | 0.7570 | 1.3763 | 5.7491 | 0.3442 | 1.9788 |
| **0.10% (Base)** | 0.9483 | 0.7572 | 1.2524 | 4.6218 | 0.3516 | 1.7990 |
| **0.20%** | 0.6197 | 0.7584 | 0.8171 | 1.5867 | 0.4240 | 1.1699 |
| **0.30%** | 0.2950 | 0.7604 | 0.3879 | 0.2902 | 0.4979 | 0.5531 |
| **0.40%** | -0.0297 | 0.7633 | -0.0390 | -0.0024 | 0.6448 | -0.0553 |
| **0.50%** | -0.3545 | 0.7670 | -0.4622 | -0.2193 | 0.7788 | -0.6519 |

*Finding: Estimated break-even cost is $0.36\%$ per transaction ($0.72\%$ round-trip turnaround).*

#### 5. Performance on Strictly Unseen Data Period (Table 10, Nov 7, 2019 – Aug 22, 2021, 0.1% Fee)
| Asset | Strategy | Ann Mean Return | Ann Volatility | Sharpe Ratio | Information Ratio** | Max Drawdown | Sortino Ratio |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **BTC** | Buy & Hold | **0.9267** | **0.8214** | **1.1281** | 2.0485 | 0.6228 | 1.5540 |
| **BTC** | Train 7 Test 28 | 0.6828 | 0.8219 | 0.8307 | 1.3191 | 0.5849 | 1.2198 |
| **BTC** | Train 14 Test 10 | 0.9091 | 0.8216 | 1.1064 | **2.6275** | **0.5243** | **1.6249** |
| **ETH** | Buy & Hold | **1.5771** | **1.0264** | **1.5365** | 4.0574 | 0.6937 | **2.1089** |
| **ETH** | Train 7 Test 28 | 1.2408 | 1.0268 | 1.2085 | 2.0651 | 0.7696 | 1.7669 |
| **ETH** | Train 14 Test 10 | 1.3727 | 1.0266 | 1.3371 | **4.2635** | **0.6177** | 1.9519 |
| **BNB** | Buy & Hold | **1.7142** | **1.1705** | **1.4644** | **3.5801** | 0.7483 | **2.0211** |
| **BNB** | Train 7 Test 28 | 1.2879 | 1.1712 | 1.0997 | 1.8793 | 0.7798 | 1.6298 |
| **BNB** | Train 14 Test 10 | 1.4030 | 1.1710 | 1.1982 | 2.6565 | **0.7275** | 1.7850 |

#### 6. Multi-Asset Portfolio Performance on Unseen Data Period (Table 11, Equal Weighted at Inception, No Rebalancing)
| Portfolio Description | Ann Mean Return | Ann Volatility | Sharpe Ratio | Information Ratio** | Max Drawdown | Sortino Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Portfolio WF 7/28 (BTC+ETH+BNB)** | 1.129 | 0.889 | 1.270 | 3.047 | 0.619 | 1.874 |
| **Portfolio WF 14/10 (BTC+ETH+BNB)** | 1.269 | 0.907 | 1.400 | 4.274 | 0.569 | 2.067 |
| **Portfolio Buy & Hold (BTC+ETH+BNB)** | **1.495** | 0.970 | 1.542 | 3.870 | 0.683 | 2.075 |
| **All Portfolios Combined (Active + Passive)** | 1.318 | **0.686** | **1.921** | **9.369** | **0.438** | **2.757** |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Catastrophic High-Frequency Cost Decay (`source-reported`):** At 1-minute to 15-minute sampling frequencies, all 81 walk-forward window configurations produce deeply negative risk-adjusted returns (mean Sharpe of $-12.71$ at 1m and $-2.84$ at 5m), demonstrating that high-frequency EMA momentum is unviable under normal spot exchange fee structures.
2. **Out-of-Sample Window Decay on Grid Boundaries (`source-reported`):** The top training parameter set (WF 7/28) was situated on the upper search boundary and suffered a $30\%$ drop in Sharpe ratio during unseen testing, underperforming both Buy-and-Hold and the interior WF 14/10 configuration across all three assets.
3. **Severe Bull Market Lag (`source-reported`):** During strong market uptrends (such as the second half of the unseen period in 2021), the active momentum strategies lagged Buy-and-Hold substantially due to unhedged short positions during pullbacks and transaction fee churn.
4. **Failure of In-Sample Parameter Optimization to Beat Random EMA (`source-reported`):** In the subsampled EMA bootstrap, the optimized EMA strategy failed to outperform random EMA selection at the $5\%$ significance level ($p = 0.080$ for 7/28, $p = 0.137$ for 14/10), revealing that exact EMA parameter tuning provides negligible incremental edge over the broad trend regime.
5. **Cost Failure Point (`source-reported`):** At fees $\ge 0.40\%$ per trade ($0.80\%$ round-trip), the strategy generates negative annual returns ($-2.97\%$ at 0.40%, $-35.45\%$ at 0.50%) and drawdowns exceed $64\%$.

## Falsification plan

To falsify the positive empirical findings (that 60-minute walk-forward EMA momentum combined with Buy-and-Hold generates robust diversification alpha and lower drawdowns), any future evaluation must subject the strategy to the following pre-declared operational battery:

1. **Interior Grid Stability Gate (`research-proposed`):**
   - Protocol: Perform the 2D smoothed Sharpe optimization across walk-forward training/testing lengths on a rolling basis.
   - Failure metric (`research-defined falsification threshold`): If the selected window pair resides on the boundary of the search space, or if the out-of-sample Sharpe ratio degrades by $> 35\%$ relative to the in-sample smoothed Sharpe over an out-of-sample window of $\ge 12$ months, reject the window optimization as overfitted.

2. **Transaction Cost and Slippage Margin Test (`research-proposed`):**
   - Protocol: Re-evaluate the 60-minute strategy on out-of-sample crypto perpetual futures under an all-in cost model of 5 bps taker fee + 3 bps adverse selection slippage ($8\text{ bps}$ per trade, $16\text{ bps}$ round-trip).
   - Failure metric (`research-defined falsification threshold`): If net annualized Sharpe ratio drops below $0.40$ or net annual return falls below $0.0\%$, the momentum alpha hypothesis is falsified.

3. **Active-Passive Diversification Deficit Gate (`research-proposed`):**
   - Protocol: Construct an equally weighted portfolio of Buy-and-Hold and active WF 14/10 momentum on post-2022 out-of-sample crypto data spanning at least one bear market and one bull market.
   - Failure metric (`research-defined falsification threshold`): If the blended active-passive portfolio fails to reduce maximum drawdown by at least $15\%$ (absolute) relative to pure Buy-and-Hold, or fails to achieve a higher Information Ratio, reject the active-passive diversification hypothesis.

4. **Shuffled-Block Significance Re-Verification (`research-proposed`):**
   - Protocol: Apply the Politis-Romano block bootstrap (1,000 iterations) on out-of-sample realized positions.
   - Failure metric (`research-defined falsification threshold`): If the empirical p-value exceeds $\alpha = 0.05$ (meaning random trade sequences match or exceed strategy return), reject timing skill as spurious.

5. **Regime-Conditioned Long-Only Switch Test (`research-proposed`):**
   - Protocol: Compare the unconstrained long/short momentum policy against a long/cash policy during bull market regimes (defined by BTC price above its 200-day simple moving average).
   - Failure metric (`research-defined falsification threshold`): If the continuous short rule underperforms a long/cash policy by $> 20\%$ annualized during bull regimes, the mandatory unhedged short rule is rejected in favor of an asymmetric cash filter.

## Crypto portability

- **Portability Status (`source-reported`):** Direct for spot cryptocurrency exchanges; adapted for perpetual futures (`research-proposed`).
- **Spot Market Borrow Friction (`research-proposed`):**
  - The study assumes continuous symmetric short exposure on spot markets without accounting for borrow availability, borrow interest rates, or margin maintenance rules.
  - In physical spot markets, a short position requires margin borrowing which incurs hourly interest rates ($5\%\text{--}25\%\text{ APR}$) and carries liquidation risk (`research-proposed`).
- **Perpetual Futures Adaptation (`research-proposed`):**
  - In crypto perpetual futures, shorting is native and capital-efficient.
  - However, perpetual contracts introduce 8-hour funding rate payments. In extended bull markets, short positions receive positive funding, whereas in bear markets, short positions pay funding to longs, altering the net holding cost (`research-proposed`).
- **24/7 Continuity (`source-reported`):**
  - Crypto markets trade continuously without weekend breaks or market-on-close auctions. The 60-minute candle boundary is uninterrupted, avoiding overnight gap risks found in traditional equity markets.

## Limitations

- **Historical Sample Range (`source-reported`):** The data covers February 2018 through August 2021 (Kaggle G-Forecast dataset). It does not reflect post-2022 market structure developments such as spot Bitcoin/Ethereum ETFs, dominant perpetual volume on centralized exchanges, or decentralized order books (`source-reported`).
- **Frozen Walk-Forward Windows in Unseen Testing (`source-reported`):** The strategy parameters were optimized on the 2018–2019 global training period and executed for 21.5 months without retraining or recalibrating window lengths, leading to performance stagnation during the 2021 bull run (`source-reported`).
- **Microstructure Omission (`source-reported`):** The evaluation uses candle closes without modeling intraday order book depth, queue priority, latency slippage, or spread widening during market crashes (`source-reported`).
- **Symmetric Short Assumption (`source-reported`):** Short positions are treated symmetrically with longs, ignoring margin borrow costs, borrow availability constraints, and short squeeze dynamics (`source-reported`).

## Implementation status

- `not-implemented`. This record captures external published research from arXiv:2602.10785v1.
- No strategy, trading engine, or operational component has been implemented or modified in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- All decisions across all audited families remain strictly `NO_TRADE`.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves as methodological and empirical reference regarding walk-forward window parameterization, high-frequency fee attrition, and active-passive portfolio diversification.
- It does not authorize paper trading, testnet execution, or live capital allocation.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/backtest-overfitting-pbo-cscv-2026-08-27]]`
- `[[quant/binance-spot-candle-ml-extrema-timing-falsification-2026-09-04]]`
- `[[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]`

## Sources

1. Tomasz Mroziewicz and Robert Ślepaczuk, *"A novel approach to trading strategy parameter optimization, using double out-of-sample data and walk-forward techniques"*, arXiv preprint `arXiv:2602.10785v1 [q-fin.TR, q-fin.MF, q-fin.PM]`, submitted February 11, 2026. DOI: [10.48550/arXiv.2602.10785](https://doi.org/10.48550/arXiv.2602.10785). Stable URL: [https://arxiv.org/abs/2602.10785](https://arxiv.org/abs/2602.10785). Full text HTML: [https://arxiv.org/html/2602.10785v1](https://arxiv.org/html/2602.10785v1).
2. Tomasz Mroziewicz and Robert Ślepaczuk, *Reproducible Backtesting and Data Pipeline Orchestration: Analysis & Reporting Repository*, GitHub repository: [https://github.com/tmr-crypto/wf_optim_crypto_analysis](https://github.com/tmr-crypto/wf_optim_crypto_analysis) (commit `a9b4d8d09da162c970253c0b8cb5e5b3f2400444`).
3. Tomasz Mroziewicz and Robert Ślepaczuk, *Walk-Forward Crypto Optimization Pipeline Repository*, GitHub repository: [https://github.com/tmr-crypto/wf_optim_crypto](https://github.com/tmr-crypto/wf_optim_crypto) (commit `8be3ecf0019e991962f6f59bf9938cfa56411350`).
4. J. Gómez and R. Ślepaczuk, *"Robust Sharpe Ratio: A New Measure of Investment Performance"*, Working Paper, University of Warsaw, 2021.
5. P. Ryś and R. Ślepaczuk, *"The optimization of algorithmic investment strategies based on technical analysis indicators"*, Central European Economic Journal, Vol. 6, No. 53, pp. 206–229, 2019. DOI: [10.2478/ceej-2019-0014](https://doi.org/10.2478/ceej-2019-0014).
6. D. N. Politis and J. P. Romano, *"The stationary bootstrap"*, Journal of the American Statistical Association, Vol. 89, No. 428, pp. 1303–1313, 1994. DOI: [10.1080/01621459.1994.10476870](https://doi.org/10.1080/01621459.1994.10476870).
7. E. F. Fama, *"The behavior of stock-market prices"*, The Journal of Business, Vol. 38, No. 1, pp. 34–105, 1965.
