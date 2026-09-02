---
schema: strategy-research-record-v1
title: "Volume-Price-Adjusted MACD with Sensitivity Calibration (VP-MACD)"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-indices
  - momentum
  - technical-analysis
  - volume-weighted
  - volatility-adjustment
  - candlestick-structure
  - macd
  - sensitivity-parameter
status: research-only
confidence: medium
source_as_of: 2026-04-28
sources:
  - "Luyun Lin, Lixing Lin, Zhen Zhang, Moxuan Zheng, and Yiqing Wang, 'A Volume-Price-Adjusted MACD Trading Strategy with Sensitivity Calibration for U.S. Equity Indices', arXiv preprint arXiv:2604.26063v1 [q-fin.TR], April 28, 2026. DOI: 10.48550/arXiv.2604.26063. https://arxiv.org/abs/2604.26063"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume-Price-Adjusted MACD with Sensitivity Calibration (VP-MACD)

## Provenance

- **Authors:** Luyun Lin (Independent Researcher, Dallas, TX, USA), Lixing Lin (Yale University, New Haven, CT, USA), Zhen Zhang (Independent Researcher, Jersey City, NJ, USA), Moxuan Zheng (Independent Researcher, Jersey City, NJ, USA), Yiqing Wang (Independent Researcher, Dallas, TX, USA; corresponding author: `woshilucy712@gmail.com`).
- **Title:** "A Volume-Price-Adjusted MACD Trading Strategy with Sensitivity Calibration for U.S. Equity Indices"
- **Identifier:** arXiv preprint `arXiv:2604.26063v1 [q-fin.TR]`, submitted April 28, 2026.
- **DOI:** [10.48550/arXiv.2604.26063](https://doi.org/10.48550/arXiv.2604.26063)
- **Stable URL:** https://arxiv.org/abs/2604.26063
- **Full Text HTML:** https://arxiv.org/html/2604.26063v1
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Sample/Data Period:** Daily data from 2018 to February 2026.
  - Training / In-sample calibration: 2018 to 2022 (1,259 trading-day observations per instrument).
  - Testing / Out-of-sample evaluation: January 1, 2023 to February 28, 2026 (791 trading-day observations per instrument).
- **Target Universe:** Major U.S. equity index exchange-traded funds (ETFs): S&P 500 (SPY), NASDAQ-100 (QQQ), and Dow Jones Industrial Average (DIA).
- **Data Source:** Daily OHLCV data obtained from Yahoo Finance.

## Economic mechanism

### Source-reported

Conventional Moving Average Convergence Divergence (MACD) trading rules rely entirely on exponential moving averages of closing prices, leading to two well-documented structural vulnerabilities:
1. **Signal lag:** Because closing prices are sequentially smoothed, crossover signals are inherently delayed relative to underlying trend turns, causing late entries and exits.
2. **Omission of volume and intraday price structure:** Conventional MACD treats all equal price changes alike, regardless of whether a move was backed by heavy trading volume or occurred on thin participation, and regardless of whether the intraday candlestick reflects one-sided conviction (large real body) or indecision (long wicks, small body). Consequently, choppy or consolidating markets generate frequent false crossover whipsaws.

To address these flaws without fragmenting the system into arbitrary multi-indicator combinations, the authors formulate a unified structural enhancement:
- Construct an adjusted price series $P_t^*$ that jointly weights historical price points by trading volume ($\mathrm{Volume}_i$), normalized high-low range volatility ($\sigma_i$), and candlestick body-to-range directional ratio ($r_i$).
- Introduce a sensitivity parameter $\lambda \in [0.8, 1.0]$ into the crossover condition ($\mathrm{VP\text{-}MACD}_t > \lambda \cdot \mathrm{Signal}_t$), which lowers the crossover hurdle and permits earlier entry into nascent trends before standard moving-average crossing is completed.

### Research interpretation

The proposed framework represents a **volume- and intraday-conviction-weighted momentum filter with threshold relaxation**:
1. **Volume weighting as a proxy for institutional order flow:** Price advances accompanied by high volume receive higher weight in $P_t^*$, accelerating the short-term moving average when institutional participation confirms directional flow, while low-volume drift receives suppressed weight.
2. **Range-normalized volatility ($\sigma_i$) as an activity scale:** Price points occurring during elevated trading ranges expand the dynamic weight, scaling the input by the magnitude of intraday price discovery.
3. **Candlestick directional conviction ($r_i$):** By scaling by $r_i = |P_i^{\mathrm{Close}} - P_i^{\mathrm{Open}}| / (P_i^{\mathrm{High}} - P_i^{\mathrm{Low}})$, the indicator explicitly rewards unidirectional candles (marubozu-style conviction) and penalizes long-legged dojis or spinning tops that have high high-low range but negligible net progress.
4. **Sensitivity threshold $\lambda$:** Moving-average crossover systems have a deterministic phase delay of approximately $(n-1)/2$ bars. Scaling the signal line by $\lambda \in [0.8, 1.0]$ shifts the trigger boundary backward in time, trading off a slight increase in false-breakout exposure against earlier trend participation.

**Component roles:**
- **Regime/State input:** Volume-volatility-candlestick adjusted price $P_t^*$.
- **Primary momentum oscillator:** $\mathrm{VP\text{-}MACD}_t = \mathrm{EMA}_{12}(P_t^*) - \mathrm{EMA}_{26}(P_t^*)$.
- **Signal smoothing:** $\mathrm{Signal}_t = \mathrm{EMA}_9(\mathrm{VP\text{-}MACD}_t)$.
- **Entry trigger:** Sensitivity-relaxed crossover ($\mathrm{VP\text{-}MACD}_t > \lambda \cdot \mathrm{Signal}_t$).
- **Exit trigger:** Standard unscaled crossover ($\mathrm{VP\text{-}MACD}_t < \mathrm{Signal}_t$).

## Signal

### Formation timestamp

The indicator is evaluated at daily market close ($t$). Calculations utilize daily Open, High, Low, Close, and Volume available at close.

### Lookback and Construction

1. **Relative Volatility ($\sigma_i$):**
   $$\sigma_i = \frac{\mathrm{STD}(P_i^{\mathrm{High}} - P_i^{\mathrm{Low}})}{P_i^{\mathrm{Close}}}$$
   where $P_i^{\mathrm{High}}$, $P_i^{\mathrm{Low}}$, and $P_i^{\mathrm{Close}}$ denote high, low, and closing prices on day $i$.
   - *Provenance gap / Underspecification:* The paper states that the numerator measures variation in the daily high-low price range normalized by close, but does not explicitly specify the lookback window over which the rolling standard deviation $\mathrm{STD}(\cdot)$ is calculated.

2. **Candlestick Directional Conviction Ratio ($r_i$):**
   $$r_i = \frac{\left|P_i^{\mathrm{Close}} - P_i^{\mathrm{Open}}\right|}{P_i^{\mathrm{High}} - P_i^{\mathrm{Low}}}$$
   where $r_i \in [0, 1]$ represents the ratio of the candlestick real body to the total high-low span.

3. **Adjusted Price ($P_t^*$):**
   $$P_t^* = \frac{\sum_{i=t-N}^{t-1} P_i \cdot \mathrm{Volume}_i \cdot \sigma_i \cdot r_i}{\sum_{i=t-N}^{t-1} \mathrm{Volume}_i}$$
   where $N$ represents the number of past trading days in the rolling calculation.
   - *Provenance gap / Underspecification:* The text omits the numerical value of $N$ used in the empirical section (e.g., whether $N$ is 5, 10, 20, or 26 days).

4. **VP-MACD and Signal Line:**
   $$\mathrm{VP\text{-}MACD}_t = \mathrm{EMA}_{12}(P_t^*) - \mathrm{EMA}_{26}(P_t^*)$$
   $$\mathrm{Signal}_t = \mathrm{EMA}_9(\mathrm{VP\text{-}MACD}_t)$$
   using standard smoothing parameters $\alpha = 2 / (n + 1)$ with $n_{\mathrm{fast}} = 12$, $n_{\mathrm{slow}} = 26$, and $n_{\mathrm{signal}} = 9$.

### Entry and Exit Rules

- **Long Entry (Buy):**
   $$\mathrm{VP\text{-}MACD}_{t-1} \le \lambda \cdot \mathrm{Signal}_{t-1} \quad \text{and} \quad \mathrm{VP\text{-}MACD}_t > \lambda \cdot \mathrm{Signal}_t$$
   where $\lambda \in [0.8, 1.0]$.
   - Calibrated optimal $\lambda$ values (from in-sample 2018–2022 grid search, step 0.02, Table 1):
     - SPY: $\lambda = 0.88$ (selected by Sharpe ratio)
     - QQQ: $\lambda = 0.98$ (selected by Sharpe ratio)
     - DIA: $\lambda = 0.86$ (selected by Sharpe ratio + Expected value)
     - (For Strategy B MACD+$\lambda$, calibrated values were: SPY 0.90, QQQ 0.84, DIA 0.92).

- **Long Exit (Sell):**
   $$\mathrm{VP\text{-}MACD}_{t-1} \ge \mathrm{Signal}_{t-1} \quad \text{and} \quad \mathrm{VP\text{-}MACD}_t < \mathrm{Signal}_t$$
   Exits use the standard unscaled signal line ($\lambda = 1.0$).

- **Execution Timing:**
   To strictly prevent look-ahead bias, trades generated by signals formed at day $t$ close are executed at the **Open price of day $t+1$** ($P_{t+1}^{\mathrm{Open}}$).

- **Position Sizing and Direction:**
   - Long-only strategy.
   - Fully invested upon buy signal (initial capital $100,000, 0% leverage, minimum 1 share).
   - Cash held while flat until the next valid buy signal.

## Required data

- **Instruments:** U.S. broad equity index ETFs: SPY (SPDR S&P 500 ETF Trust), QQQ (Invesco QQQ Trust, Series 1), DIA (SPDR Dow Jones Industrial Average ETF Trust).
- **Timeframe:** Daily bars (1D).
- **Fields:** Open, High, Low, Close, Trading Volume.
- **Venue / Vendor:** Yahoo Finance daily historical price feeds.
- **Point-in-Time:** Requires official closing price and total daily volume at market close (16:00 ET). Order execution occurs at the official market open (09:30 ET) on day $t+1$.
- **Calendar:** U.S. equity market sessions (NYSE/Nasdaq); weekends and non-trading holidays excluded.
- **Corporate Actions:** Prices must be split- and dividend-adjusted.

## Execution assumptions

- **Order Type:** Market open order at $t+1$ ($P_{t+1}^{\mathrm{Open}}$).
- **Execution Latency:** Overnight buffer (signal computed after 16:00 ET close, executed at 09:30 ET next morning).
- **Transaction Costs:**
  - One-way cost: 4 bps per trade (3 bps broker/exchange commission + 1 bp slippage).
  - Round-trip cost: 8 bps per completed buy-sell pair.
- **Shorting / Borrow:** None (long-only).
- **Margin / Leverage:** 1.0x (unleveraged, cash-settled accounting).
- **Capacity / Impact:** Highly liquid large-cap ETFs (SPY, QQQ, DIA) with daily turnover exceeding billions; market impact for institutional sizes under $10M is assumed negligible at the opening auction.

## Evidence

### Source-reported

The study evaluates three distinct strategies out-of-sample over January 1, 2023 to February 28, 2026 (791 trading days), incorporating 8 bps round-trip transaction costs:
- **Strategy A:** Baseline MACD crossover rule.
- **Strategy B:** Traditional MACD with calibrated $\lambda$ threshold.
- **Strategy C:** Proposed Volume-Price-Adjusted MACD (VP-MACD) with calibrated $\lambda$.

#### Out-of-Sample Performance by Index (Tables 2, 3, 4)

1. **SPY (Table 2, out-of-sample 2023–2026):**
   - *Baseline MACD (Strategy A):* 40 trades, Win Rate 50.00%, Total PnL $13,612.34, PnL Ratio 1.39, Sharpe 0.47, Max Drawdown -13.78%, Expectancy $19.39.
   - *MACD+$\lambda$ ($\lambda=0.90$, Strategy B):* 36 trades, Win Rate 55.56%, Total PnL $52,688.94, PnL Ratio 2.98, Sharpe 1.35, Max Drawdown -8.17%, Expectancy $121.04.
   - *VP-MACD ($\lambda=0.88$, Strategy C):* 6 trades, Win Rate 50.00%, Total PnL $27,543.78, PnL Ratio 8.61, Sharpe 0.96, Max Drawdown -6.33%, Expectancy $365.72.

2. **QQQ (Table 3, out-of-sample 2023–2026):**
   - *Baseline MACD (Strategy A):* 35 trades, Win Rate 45.71%, Total PnL $16,823.12, PnL Ratio 1.56, Sharpe 0.45, Max Drawdown -22.84%, Expectancy $17.14.
   - *MACD+$\lambda$ ($\lambda=0.84$, Strategy B):* 31 trades, Win Rate 61.29%, Total PnL $63,321.06, PnL Ratio 1.89, Sharpe 1.13, Max Drawdown -11.94%, Expectancy $76.83.
   - *VP-MACD ($\lambda=0.98$, Strategy C):* 21 trades, Win Rate 80.95%, Total PnL $88,324.48, PnL Ratio 1.72, Sharpe 1.51, Max Drawdown -7.41%, Expectancy $120.26.

3. **DIA (Table 4, out-of-sample 2023–2026):**
   - *Baseline MACD (Strategy A):* 40 trades, Win Rate 40.00%, Total PnL $1,236.96, PnL Ratio 1.55, Sharpe 0.09, Max Drawdown -13.95%, Expectancy $2.09.
   - *MACD+$\lambda$ ($\lambda=0.92$, Strategy B):* 34 trades, Win Rate 50.00%, Total PnL -$6,862.00, PnL Ratio 0.75, Sharpe -0.20, Max Drawdown -14.19%, Expectancy -$12.55.
   - *VP-MACD ($\lambda=0.86$, Strategy C):* 13 trades, Win Rate 69.23%, Total PnL $29,592.17, PnL Ratio 3.72, Sharpe 1.08, Max Drawdown -6.20%, Expectancy $226.87.

#### Statistical Significance of Incremental Returns

The authors conduct one-sided tests on daily return differentials over the testing period:
- **Standard $t$-tests (Table 5):**
  - SPY: Pair 1 (B vs A) $t = 1.7171, p = 0.0432^*$; Pair 2 (C vs A) $t = 0.4971, p = 0.3096$; Pair 3 (C vs B) $t = -0.8857, p = 0.8120$.
  - QQQ: Pair 1 (B vs A) $t = 1.6653, p = 0.0481^*$; Pair 2 (C vs A) $t = 1.6586, p = 0.0488^*$; Pair 3 (C vs B) $t = 0.3107, p = 0.3781$.
  - DIA: Pair 1 (B vs A) $t = -0.6313, p = 0.0736$; Pair 2 (C vs A) $t = 1.2804, p = 0.1004$; Pair 3 (C vs B) $t = 1.7065, p = 0.0442^*$.
- **Newey–West HAC-Adjusted $t$-tests (Table 6):**
  - SPY: Pair 1 $t = 1.8983, p = 0.0288^*$; Pair 2 $t = 0.5307, p = 0.2978$; Pair 3 $t = -0.9922, p = 0.8394$.
  - QQQ: Pair 1 $t = 1.6931, p = 0.0452^*$; Pair 2 $t = 1.7229, p = 0.0425^*$; Pair 3 $t = 0.3487, p = 0.3637$.
  - DIA: Pair 1 $t = -0.6593, p = 0.7452$; Pair 2 $t = 1.2964, p = 0.0974$; Pair 3 $t = 1.7894, p = 0.0368^*$.
- **Circular Block Bootstrap (1,000 resamples, block length 5 days):**
  - Confirms significance for SPY Pair 1 ($p = 0.024^*$), QQQ Pair 2 ($p = 0.039^*$), and DIA Pair 3 ($p = 0.028^*$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Severe trade count reduction and mixed outcome in SPY:**
   In SPY, VP-MACD executed only 6 trades across 38 months (791 trading days). While the PnL ratio rose to 8.61 and drawdown was halved (-6.33% vs -13.78%), the total PnL of VP-MACD ($27,543.78) was substantially lower than Strategy B ($52,688.94). Pair 2 (VP-MACD vs Baseline MACD) failed to achieve statistical significance on SPY ($p = 0.3096$).
2. **Strategy B failure on DIA:**
   In DIA, the $\lambda$ adjustment alone (Strategy B) yielded negative total PnL (-$6,862.00) and negative Sharpe (-0.20), showing that sensitivity relaxation on unadjusted closing prices can severely backfire in lower-volatility, non-tech equity indices.
3. **Index-specific optimal $\lambda$ divergence:**
   Optimal $\lambda$ did not generalize to a universal parameter: for QQQ, VP-MACD required $\lambda = 0.98$ (almost an unadjusted crossover) to avoid overreacting to volatile tech noise, whereas DIA required $\lambda = 0.86$ and SPY required $\lambda = 0.88$.
4. **Sample size vulnerability:**
   A sample of only 6 trades for SPY over 3 years creates high estimation error and renders any single-trade outcome capable of skewing reported metrics.

## Falsification plan

To falsify the empirical claims of the VP-MACD framework:
1. **Component Ablation Test:**
   Construct four separate variant baselines:
   - Variant 1: MACD computed on Volume-weighted price only ($P_i \cdot \mathrm{Volume}_i$).
   - Variant 2: MACD computed on Volatility-weighted price only ($P_i \cdot \sigma_i$).
   - Variant 3: MACD computed on Candlestick-body-weighted price only ($P_i \cdot r_i$).
   - Variant 4: Standard MACD + $\lambda$ alone.
   *Falsification rule:* If Variant 4 or Variant 1 matches or exceeds the full VP-MACD Sharpe ratio, the hypothesized synergy between volume, volatility, and candlestick structure is falsified.
2. **Lookback Parameter Perturbation ($N$ and $\sigma$ window):**
   Evaluate sensitivity over $N \in [5, 10, 15, 20, 30]$ trading days and $\sigma$ window $\in [5, 10, 20]$ days.
   *Falsification rule:* If out-of-sample Sharpe drops by $>50\%$ across adjacent parameter choices, the framework is rejected as an artifact of parameter overfitting.
3. **Out-of-Sample Asset Universe Extension:**
   Backtest the fixed calibrated parameters on individual large-cap equities (e.g., AAPL, MSFT, JNJ, XOM) and commodity/rates futures (CL, GC, ZN).
   *Falsification rule:* If mean out-of-sample Sharpe across the broader universe is $\le 0.0$, the strategy represents an ETF-specific statistical artifact rather than a generalized market principle.
4. **Friction and Execution Lag Stress:**
   Increase round-trip costs to 15 bps and 25 bps, and test delayed execution at $t+1$ close instead of $t+1$ open.
   *Falsification rule:* If the edge vanishes under 15 bps round-trip cost, the strategy is deemed non-tradable in institutional practice.

## Crypto portability

- **Portability status:** `adapted` / `unproven`.
- The strategy originates entirely from traditional U.S. equity ETF index research and is **not demonstrated in cryptocurrency markets by the cited source**. Porting to crypto represents a research hypothesis, not empirical evidence.
- **Crypto-specific friction and structural risks:**
  1. *Continuous 24/7 session structure:* Equity daily bars have well-defined 09:30 ET opening and 16:00 ET closing auction prices that reflect distinct institutional order aggregation. In crypto, "Open" and "Close" are arbitrary UTC boundary timestamps (e.g., 00:00 UTC). The candlestick body ratio $r_i = |Close - Open| / (High - Low)$ will vary drastically depending on arbitrary session cutoffs.
  2. *Volume distortions and venue fragmentation:* Unlike consolidated tape equity ETF volume, crypto volume is fragmented across dozens of centralized and decentralized exchanges, with significant wash trading and fee-tier distortions on zero-fee pairs. Using reported volume without strict filtering will corrupt the weighting in $P_t^*$.
  3. *Perpetual swap funding drag:* The original paper assumes zero carry cost while holding long positions. Holding perpetual swaps during bull regimes frequently incurs significant positive funding rates (often 10% to 30% annualized), which could completely erode the modest multi-month holding returns of the 6–21 trades generated.
  4. *Volatility regime divergence:* Crypto volatility is 2x to 5x higher than equity indices; the equity-calibrated $\lambda$ grid ($[0.80, 1.00]$) may produce extreme whipsaws in crypto without widening the threshold bounds or scaling $\lambda$ dynamically by realized volatility.

## Limitations

- `underspecified`: The paper does not state the exact integer value of the lookback parameter $N$ in Equation (8), nor the window length for the rolling standard deviation $\mathrm{STD}(\cdot)$ in Equation (9).
- `small sample size`: In SPY, the strategy generated only 6 completed trades over a 38-month evaluation window, rendering trade-level statistics statistically fragile.
- `not independently reproduced`: All performance figures, $t$-statistics, and win rates are source-reported from Lin et al. (2026) and have not been replicated in our proprietary research stack.
- `unproven in crypto`: TradFi index results cannot be assumed to hold in decentralized or continuous crypto asset classes.
- `parameter calibration risk`: Optimal $\lambda$ varied from 0.86 to 0.98 across the three indices, indicating that the threshold is sensitive to underlying asset volatility and not constant across markets.

## Implementation status

`not-implemented`. This strategy has not been implemented or tested in PyBroker, NautilusTrader, or any paper or live execution system.

## Adoption boundary

Research material only. A record being present in this repository does not constitute evidence of profitability, approval for implementation, or authorization for paper, testnet, or live trading.

## Related Wiki records

- `[[quant/macd-trend_ohlcv-2026-08-31]]`
- `[[quant/futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`

## Sources

- Luyun Lin, Lixing Lin, Zhen Zhang, Moxuan Zheng, and Yiqing Wang, "A Volume-Price-Adjusted MACD Trading Strategy with Sensitivity Calibration for U.S. Equity Indices", arXiv preprint `arXiv:2604.26063v1 [q-fin.TR]`, submitted April 28, 2026. DOI: [10.48550/arXiv.2604.26063](https://doi.org/10.48550/arXiv.2604.26063). Stable URL: https://arxiv.org/abs/2604.26063. PDF URL: https://arxiv.org/pdf/2604.26063. HTML URL: https://arxiv.org/html/2604.26063v1.
