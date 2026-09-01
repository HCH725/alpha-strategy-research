---
schema: strategy-research-record-v1
title: Crypto Realized Volatility Forecasting from Kalshi Macro Prediction Market Repricing (Monetary Policy and Inflation Channels)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - prediction-markets
  - kalshi
  - realized-volatility
  - macro-uncertainty
  - monetary-policy
  - inflation
  - har-model
  - options-pricing
status: research-only
confidence: high
source_as_of: 2026-04-01
sources:
  - https://arxiv.org/abs/2604.01431
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Realized Volatility Forecasting from Kalshi Macro Prediction Market Repricing (Monetary Policy and Inflation Channels)

## Provenance

- **Primary Source:** Hardhik Mohanty and Bhaskar Krishnamachari (University of Southern California / Viterbi School of Engineering), "Do Prediction Markets Forecast Cryptocurrency Volatility? Evidence from Kalshi Macro Contracts", *arXiv preprint arXiv:2604.01431v1* [q-fin.ST / q-fin.RM], submitted 1 April 2026.
- **arXiv URL:** https://arxiv.org/abs/2604.01431
- **DOI:** https://doi.org/10.48550/arXiv.2604.01431
- **Evaluation Sample:** January 2023 through March 2026 ($N = 1,183$ calendar days).
- **Venue & Contract Coverage:** Public API data from Kalshi, the first CFTC-regulated event contract exchange in the United States. Evaluates 10 macro event contract series, focusing on `KXFED` (Federal Reserve interest rate decisions), `KXCPI` (Consumer Price Index releases), `KXRECSSNBER` (NBER recession determinations, 569 usable trading days), and `KXPCECORE` (core PCE, 294 usable trading days). Excludes `KXRATECUT` (28 usable days) and `KXUSNFP` (0 overlapping days) due to insufficient coverage.
- **Crypto Universe:** Daily spot close data from CoinGecko for Bitcoin (BTC), Ethereum (ETH), Solana (SOL), Cardano (ADA), Avalanche (AVAX), and Chainlink (LINK).
- **Macro & Asset Benchmarks:** CBOE VIX, US Dollar Index (DXY), S&P 500, 30-day Fed Funds futures daily implied rate changes, 10-year US Treasury benchmark daily returns, and the Deribit Bitcoin and Ethereum Volatility Indices (DVOL).

## Economic mechanism

### Source-reported

Conventional macroeconomic surprise metrics (e.g., Bernanke & Kuttner 2005; Gürkaynak et al. 2005) are observed only on scheduled event release dates (FOMC press conferences, BLS CPI releases). Between scheduled dates, financial and digital asset markets lack a continuous metric for how macroeconomic expectations are shifting. CFTC-regulated prediction markets like Kalshi trade binary options on macro events continuously, aggregating dispersed information into risk-neutral outcome probabilities. Because constant risk premia difference out in daily first differences, daily volume-weighted probability changes act as continuous gauges of macro uncertainty repricing.

The authors identify two asset-specific transmission channels:
1. **Monetary Policy Channel (`KXFED` $\to$ Bitcoin):** Dovish monetary policy repricing ($-\Delta^{vw}_{\text{KXFED},t}$, indicating increasing expectations of rate cuts) positively predicts 5-day forward realized volatility for Bitcoin ($t = 3.63, p < 0.001$). Dovish shifts typically accompany deteriorating economic data, signaling macroeconomic vulnerability and driving institutional rebalancing that elevates Bitcoin market volatility.
2. **Inflation Uncertainty Resolution Channel (`KXCPI` $\to$ Altcoins):** Larger absolute probability shifts in CPI contracts ($|\Delta^{vw}_{\text{KXCPI},t}|$) negatively predict 5-day forward realized volatility across altcoins (ETH, SOL, ADA, LINK) with $t$-statistics from $-2.1$ to $-3.4$. Because probability moves concentrate around scheduled BLS releases, the arrival and pricing of the inflation print resolves acute ambiguity, leading to a post-event volatility collapse.
3. **Recession Risk Channel (`KXRECSSNBER` $\to$ Bitcoin):** Recession-risk contracts trade as continuous-tenor hedging instruments with high, stable open interest (sample median $\$456,648$). Daily repricing on `KXRECSSNBER` negatively predicts Bitcoin volatility ($t = -2.76, p = 0.006$) and provides the most stable out-of-sample forecast gains.

### Research interpretation

The empirical evidence supports a structural divergence between institutional and retail crypto participants:
- **Institutional liquidity vs. retail inflation exposure:** Bitcoin functions as a macro-sensitive liquidity asset whose volatility is primarily driven by institutional adjustments to the Federal Reserve's policy path and dollar liquidity. Altcoins, having higher retail ownership and smaller market capitalizations, are more sensitive to real-economy inflation ambiguity.
- **Uncertainty resolution as an exploitable volatility harvest:** The negative coefficient for altcoins confirms an event-resolution volatility crush. Options markets (e.g., Deribit ETH options) that fail to condition on Kalshi's continuous probability absorption systematically overprice 1-week straddle premiums following large CPI repricing events.
- **Regime dependency:** The monetary policy channel is highly regime-dependent. It accumulated forecast gains during the active 2024–2025 Fed rate-cutting cycle but decayed outside that cycle, indicating it is an episodic macro-catalyst factor rather than a stationary steady-state alpha.

## Signal

### Primary Signal Construction

For each Kalshi event series $s$ on calendar date $t$:
1. Identify all active strike/threshold contracts $\mathcal{J}_{s,t}$.
2. Compute the volume-weighted closing-to-closing probability change:
   $$\Delta^{vw}_{s,t} = \sum_{j \in \mathcal{J}_{s,t}} \frac{V_{j,t}}{\sum_{k \in \mathcal{J}_{s,t}} V_{k,t}} \cdot (p_{j,t} - p_{j,t-1})$$
   where $V_{j,t}$ is daily contract dollar volume and $p_{j,t} \in [0, 1]$ is the closing transaction price.
3. **Magnitude Signal (Inflation & Recession):**
   $$\text{Kalshi}_{s,t} = |\Delta^{vw}_{s,t}|$$
4. **Directional Fed-Dovish Signal (Monetary Policy):**
   $$\text{Kalshi}_{\text{Fed-Dovish},t} = -\Delta^{vw}_{\text{KXFED},t}$$
   (positive when the probability of rate cuts increases / rate expectations decline).

### Dependent Variable & Forecasting Model

The target is 5-day forward annualized realized volatility:
$$\text{RVol}_{a,t}^{h=5} = \sqrt{252} \cdot \sqrt{\frac{1}{4} \sum_{i=1}^{5} \left(r_{a,t+i} - \bar{r}_{a,t,5}\right)^2}$$
where $r_{a,t} = \ln(P_{a,t} / P_{a,t-1})$.

The augmented predictive model (M3) expands Corsi's (2009) HAR benchmark:
$$\text{RVol}_{a,t+1:t+5} = \beta_0 + \beta_d |r|_{a,t}^{(1)} + \beta_w \overline{|r|}_{a,t}^{(5)} + \beta_m \overline{|r|}_{a,t}^{(22)} + \gamma_1 \text{VIX}_t + \gamma_2 r_{\text{DXY},t} + \gamma_3 r_{\text{SP500},t} + \delta \cdot \text{Kalshi}_{s,t} + \varepsilon_{a,t+5}$$
where all predictors are lagged to time $t$. Because Kalshi closes at 4:00 PM ET and crypto prices close at midnight UTC (7:00 PM ET), a strict 21-hour minimum buffer separates the signal timestamp from the $t+1$ forecast window start.

### Trading Strategy Formulations

1. **Volatility-Managed Portfolio Rebalancing (Moreira & Muir 2017 framework):**
   - Scale portfolio exposure inversely to model M3 predicted 5-day realized volatility:
     $$w_{a,t} = \frac{\bar{\sigma}_a}{\hat{\sigma}_{a,t+1:t+5}}$$
   - When the `KXFED` Fed-dovish signal reaches its 90th percentile, predicted 5-day Bitcoin volatility rises from $0.324$ to $0.348$ annualized, generating an automated $\approx 7\%$ position trim to protect against impending volatility expansion.
2. **Options Straddle / Short-Volatility Harvesting:**
   - Following days with 90th percentile absolute `KXCPI` probability moves ($\approx 0.070$), predicted Ethereum 5-day realized volatility drops by $0.084$ annualized units ($\approx 16\%$ below the HAR benchmark prediction of $0.52$).
   - Sell 7-day ATM ETH straddles on Deribit (or delta-hedge an option short) to harvest the volatility crush before vanilla crypto options markets fully reflect the resolved macro uncertainty.

## Required data

- **Prediction Market Data:** Daily closing prices, dollar trading volumes, and open interest for Kalshi contracts (`KXFED`, `KXCPI`, `KXRECSSNBER`).
- **Cryptocurrency Price Data:** Daily closing prices (00:00 UTC) for BTC, ETH, SOL, ADA, AVAX, LINK.
- **TradFi Controls:** Daily closing values for CBOE VIX, US Dollar Index (DXY), and S&P 500 (4:00 PM ET).
- **Options / Benchmark Series:** Deribit DVOL index levels; 30-day Fed Funds futures prices; 10-year US Treasury benchmark yields.
- **Timestamp Alignment:** Regressors observed as of 4:00 PM ET on day $t$; forecast horizon begins at day $t+1$ 00:00 UTC (no look-ahead bias). Weekends and US holidays are omitted in the primary paper due to Kalshi market session boundaries.

## Execution assumptions

- **Execution Timing:** Daily execution at or immediately following 00:00 UTC, using Kalshi signals established at the preceding 4:00 PM ET close.
- **Order Types & Execution Costs:**
  - Spot/Perp rebalancing: Limit orders (maker) or VWAP market orders over the daily bar. Taker fee assumed at 0.02%–0.05%.
  - Deribit options: Mid-quote execution with bid-ask spread friction. The paper explicitly warns that altcoin option bid-ask spreads (often 1.5%–3.0% in implied volatility terms) absorb a meaningful share of expected short-straddle returns.
- **Leverage & Financing:** Unleveraged spot or $\le 2\times$ perpetual futures for the volatility-managed portfolio; full delta-hedging required for options straddles.
- **Capacity:** Kalshi `KXFED` median daily volume is $\$9,326$ (peaks $>\$651,000$), and median open interest is $\$278,805$. `KXRECSSNBER` median open interest is $\$456,648$. Signal generation is non-capacity-constrained because the strategy trades liquid crypto spot/perpetuals/options rather than executing in size on Kalshi itself.

## Evidence

### Source-reported

- **Bitcoin & Monetary Policy Channel (`KXFED` $\to$ BTC):**
  - HAR baseline (M1) adjusted $R^2 = 9.3\%$.
  - HAR + Market Controls (M2) adjusted $R^2 = 14.1\%$.
  - Full Model with Fed-Dovish Signal (M3) adjusted $R^2 = 15.5\%$.
  - Fed-dovish coefficient $\hat{\delta} = 0.639$, Newey-West HAC $t = 3.63$, $p < 0.001$.
  - Interquartile range of Fed-dovish signal is $\approx 0.023$; moving from the 25th to 75th percentile increases predicted 5-day realized volatility by $0.015$ annualized units ($\approx 2.4\%$ of mean BTC realized volatility of $0.634$).
  - Survives Benjamini-Hochberg multiple testing correction across all 60 specifications at $q = 0.05$ (adjusted $p = 0.020$).
  - Moving-block bootstrap (block length 5, 2,000 resamples) yields bootstrap $p = 0.035$.
  - Orthogonalization against Fed Funds implied rate change, VIX, DXY, and S&P 500 yields first-stage $R^2 = 2.3\%$; the orthogonalized residual predicts BTC volatility with $t = 3.62$ ($p < 0.001$).
  - Benchmarking against Fed Funds futures alone gives $t = -0.83$ (insignificant); 10Y Treasury returns give $t = +0.01$ (insignificant). In a joint regression with both, Kalshi Fed-dovish retains $t = +3.45$ ($p < 0.001$).
  - Crypto options benchmark: Joint regression with Deribit DVOL retains Kalshi Fed-dovish $t = +3.46$ ($p = 0.001$) while DVOL is statistically insignificant ($t = +1.58, p = 0.12$).
  - Horizon profile peaks at $h = 3$ to $h = 5$ days; fades at $h = 21$ ($t = +0.93, p = 0.35$).
  - Out-of-sample: Full-sample MSFE ratio $= 1.009$ (fails OOS due to regime concentration in the 2024–2025 rate-cutting cycle).
  - Recession risk (`KXRECSSNBER`): In-sample coefficient $t = -2.76$ ($p = 0.006$); out-of-sample expanding-window evaluation yields MSFE ratio $= 0.979$, Clark-West $p = 0.020$ (stable across full evaluation window).
- **Altcoins & Inflation Channel (`KXCPI` $\to$ Altcoins):**
  - Negative coefficients across ETH, SOL, ADA, LINK with HAC $t$-statistics from $-2.1$ to $-3.4$.
  - Chainlink survives Benjamini-Hochberg FDR correction at $q = 0.05$ (adjusted $p = 0.042$).
  - Out-of-sample expanding-window evaluation: Ethereum MSFE ratio $= 0.959$ ($p = 0.010$), Solana MSFE ratio $= 0.983$ ($p = 0.048$).
  - Release-window control: Adding a 3-day BLS release-window indicator preserves significance: Chainlink ($t = -3.21, p = 0.001$), Solana ($t = -2.63, p = 0.009$), Ethereum ($t = -2.07, p = 0.039$). Restricting to non-release days only preserves significance for Solana ($t = -2.80$) and Chainlink ($t = -3.07$).
  - Orthogonalization against 10-year Treasury returns (first-stage $R^2 = 7.5\%$): Residuals retain $t = -2.29$ for ETH ($p = 0.022$), $t = -2.79$ for SOL ($p = 0.005$), $t = -2.60$ for ADA ($p = 0.009$), and $t = -3.73$ for LINK ($p < 0.001$).
  - Crypto options benchmark: Joint regression with ETH DVOL yields Kalshi CPI $t = -2.08$ ($p = 0.037$), while ETH DVOL is insignificant ($t = -1.52, p = 0.13$).
  - Avalanche exception: Insignificant ($t = -1.31$, adjusted $R^2 = 0.017$), overwhelmed by token-specific idiosyncratic variance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Regime Failure Out-of-Sample for Fed-Dovish:** Over the full evaluation window, the Fed-dovish signal failed out-of-sample forecasting (MSFE ratio $= 1.009$). Forecast gains accumulated during the active September 2024–mid 2025 rate-cutting cycle and reversed when the easing cycle ended.
- **Power Loss Under Non-Overlapping Windows:** When non-overlapping 5-day windows are evaluated to eliminate moving-average serial correlation, the sample size drops by $80\%$ ($N = 64$ for BTC, $N = 54$ for LINK). The BTC Fed-dovish coefficient attenuates to $t = 1.17$ ($p = 0.24$) and Chainlink CPI attenuates to $t = -0.71$.
- **GARCH(1,1) Ineffectiveness:** GARCH conditional variance fails to detect the CPI signal for ETH ($t = -0.69$), demonstrating that backward-looking autoregressive volatility filters fail to incorporate forward-looking discrete uncertainty resolution.
- **Lead-Lag Overlap for CPI:** Lead signals ($t+1$) for KXCPI are also statistically significant for ETH ($t = -2.53$) and SOL ($t = -3.76$), indicating multi-day persistence in probability repricing around announcement dates rather than single-day causal impulses.

## Falsification plan

1. **Rate-Pause Regime Test:** Test the Fed-dovish signal on out-of-sample data during prolonged monetary pauses or rate-hiking cycles. If the out-of-sample MSFE ratio remains $> 1.0$, falsify the thesis that Fed repricing is a permanent unconditional volatility predictor.
2. **Net Options PnL Hurdle:** Backtest short 7-day ETH/BTC straddles on Deribit conditioned on Kalshi KXCPI spikes, incorporating historical Deribit bid-ask spreads, delta-rehedging slippage, and taker fees. If net annualized Sharpe is $< 0.50$ or maximum drawdown exceeds $20\%$, reject the actionable options alpha claim.
3. **Synthetic Placebo Test:** Run the M3 specification substituting volume-weighted probability changes from non-macro Kalshi event categories (e.g., weather, politics, entertainment). If non-macro series exhibit comparable predictive significance, reject macro transmission as the causal mechanism.
4. **Failure Thresholds:** Out-of-sample Clark-West $p > 0.10$ across a rolling 180-day window, or failure to beat the baseline HAR+Controls model in Root Mean Squared Forecasting Error (RMSFE).

## Crypto portability

direct

The study was performed directly on spot cryptocurrency returns (BTC, ETH, SOL, ADA, AVAX, LINK) and Deribit volatility indices (DVOL).

Portability and operational considerations:
- **Trading Session Mismatch:** Kalshi event contracts trade during US market hours (closing at 4:00 PM ET), whereas cryptocurrency exchanges trade 24/7/365. The 21-hour buffer to midnight UTC prevents look-ahead bias but leaves a multi-hour window where crypto price action may partially incorporate macro news before daily rebalancing.
- **Exchange Fragmentation:** CoinGecko daily closing prices aggregate global centralized exchanges. Execution on a specific venue (e.g., Binance or Bybit perps) will face venue-specific basis, funding, and spread nuances.
- **CFTC Regulation and Access:** Kalshi is a regulated US exchange; direct API access requires US compliance. However, because the strategy trades crypto assets rather than holding Kalshi positions to settlement, traders can use public Kalshi price feeds as pure informational signals without capital deployment on the prediction exchange.

## Limitations

- **Regression-based Forecast, Not Execution Backtest:** The source provides econometric realized volatility forecasting models (HAR / OLS / Newey-West) rather than an order-level backtest with fees, slippage, and margin accounting.
- **Execution Cost Omission for Options:** The paper demonstrates theoretical overpricing of ETH straddles but does not simulate execution against historical Deribit order book depth.
- **Data Gap in Kalshi Microstructure:** The public Kalshi API does not provide individual contract tick-level bid-ask spreads; execution costs on the prediction market itself are estimated from aggregate order book observations ($\approx \$0.02$ to $\$0.05$ spread).
- **Calendar Truncation:** Omitting weekends and US holidays drops $\approx 30\%$ of crypto trading days, creating gaps in an otherwise continuous 24/7 market.
- **Not independently reproduced.**

## Implementation status

Not implemented. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been completed.

## Adoption boundary

This record represents normalized research material only. A record being present in this repository does not mean:
- The strategy is profitable after execution frictions.
- The alpha has been validated in a backtest or live environment.
- The strategy is approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]]
- [[crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]]
- [[crypto-cross-sectional-volatility-managed-momentum-2026-08-31]]
- [[crypto-options-volatility-risk-premium-zscore-2026-08-31]]
- [[crypto-cross-sectional-financial-uncertainty-beta-premium-2026-09-01]]

## Sources

1. Hardhik Mohanty and Bhaskar Krishnamachari, "Do Prediction Markets Forecast Cryptocurrency Volatility? Evidence from Kalshi Macro Contracts", *arXiv preprint arXiv:2604.01431v1* [q-fin.ST / q-fin.RM], April 2026. DOI: https://doi.org/10.48550/arXiv.2604.01431. URL: https://arxiv.org/abs/2604.01431.
2. Francesco Corsi, "A Simple Approximate Long-Memory Model of Realized Volatility", *Journal of Financial Econometrics*, 7(2), 174–196 (2009). DOI: https://doi.org/10.1093/jjfinec/nbp001.
3. Todd E. Clark and Kenneth D. West, "Approximately normal tests for equal predictive accuracy in nested models", *Journal of Econometrics*, 138(1), 291–311 (2007). DOI: https://doi.org/10.1016/j.jeconom.2006.05.023.
4. Yoav Benjamini and Yosef Hochberg, "Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing", *Journal of the Royal Statistical Society: Series B*, 57(1), 289–300 (1995). DOI: https://doi.org/10.1111/j.2517-6161.1995.tb02031.x.
5. Alan Moreira and Tyler Muir, "Volatility-Managed Portfolios", *The Journal of Finance*, 72(4), 1611–1644 (2017). DOI: https://doi.org/10.1111/jofi.12513.
6. Justin Wolfers and Eric Zitzewitz, "Prediction Markets in Theory and Practice", NBER Working Paper No. 12083 (2006). DOI: https://doi.org/10.3386/w12083.
