---
schema: strategy-research-record-v1
title: "Visibility Graphs Relative Strength Index (VGRSI): Multi-Timeframe Geometric Structure Momentum and Mean Reversion"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - visibility-graphs
  - complex-networks
  - technical-analysis
  - multi-timeframe
  - momentum
  - mean-reversion
  - walk-forward-optimization
status: research-only
confidence: medium
source_as_of: 2026-09-02
sources:
  - "Rafał Rak, 'Visibility graphs can make money in financial markets', arXiv:2605.01300v1 [cs.CE, physics.data-an, q-fin.TR], May 2026. DOI: 10.48550/arXiv.2605.01300. https://arxiv.org/abs/2605.01300"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Visibility Graphs Relative Strength Index (VGRSI): Multi-Timeframe Geometric Structure Momentum and Mean Reversion

## Provenance

- **Primary Source:** Rafał Rak (Institute of Physics, Faculty of Exact and Technical Sciences, University of Rzeszow, Pigonia 1, 35-310 Rzeszow, Poland), *"Visibility graphs can make money in financial markets"*, arXiv preprint `arXiv:2605.01300v1 [cs.CE, physics.data-an, q-fin.TR]`, May 2, 2026. DOI: [10.48550/arXiv.2605.01300](https://doi.org/10.48550/arXiv.2605.01300). Stable URL: [https://arxiv.org/abs/2605.01300](https://arxiv.org/abs/2605.01300). Full HTML text: [https://arxiv.org/html/2605.01300v1](https://arxiv.org/html/2605.01300v1).
- **Subject Areas:** Computational Engineering, Finance, and Science (`cs.CE`), Data Analysis, Statistics and Probability (`physics.data-an`), Trading and Market Microstructure (`q-fin.TR`).
- **Research Setting & Implementation Platform:** Calculations and simulations were executed on MetaTrader 5 (MT5) using a built-in automated Expert Advisor (EA) implemented in MQL5 and Python. The empirical evaluation utilized a broker demo account replicating historical FOREX and CFD prices, bid/ask quotations, spreads, and commissions across three assets representing distinct asset classes: the Dow Jones Industrial Average (DJI30 index), the EUR/USD currency pair, and Spot Gold in US Dollars (XAU/USD) over the two-year period from January 1, 2024 to December 31, 2025 (503 trading days).
- **Intellectual Property / Rights Restriction:** The source explicitly notes in Footnote 1: *"The VGRSI indicator is an original authorial concept introduced in this paper; the author reserves all rights to its use."* The paper is distributed under an arXiv open-access license (CC BY-NC-ND 4.0). While scientific analysis, normalization, and academic verification are permitted, any commercial deployment requires explicit licensing and intellectual property clearance.

## Economic mechanism

### Source-reported

Conventional technical analysis indicators (such as RSI, MACD, Bollinger Bands, or Moving Averages) rely on simple linear price differences, rolling moving averages, or basic counts of upward and downward steps within fixed lookback windows. Empirical reviews show that their reported profitability is frequently undermined by data-snooping, transaction cost drag, and ex-post rule selection. Furthermore, multifractal analyses show that financial price trajectories exhibit complex multiscale temporal organization, heavy-tailed return distributions, and subtle persistence effects that standard indicators cannot capture.

The Visibility Graphs Relative Strength Index (VGRSI) addresses this limitation by transforming price series into network graphs via backward visibility relations in the two-dimensional time–price plane $(t, p_t)$. Rather than aggregating all consecutive price increments uniformly, backward visibility selects only historical points that maintain an unobstructed "line of sight" to the current price observation, naturally isolating key structural swing points and filtering out intra-envelope noise. Local price changes ($\Delta p_i = p_i - p_{i-1}$) attached to these visible vertices are decomposed into amplitude dominance ($r_S$, total magnitude of positive vs negative moves) and frequency dominance ($r_N$, total count of positive vs negative moves). Two aggregation modes are introduced:
- **Variant A0 (mean aggregation):** Combines amplitude and frequency information through averaging. It acts as a trend persistence filter, confirming that directional dominance is sustained across both magnitude and frequency rather than being driven by isolated outlier candles.
- **Variant A1 (ratio aggregation):** Divides amplitude dominance by frequency dominance ($r_S / r_N$). It highlights situations where large price moves occur over very few steps, acting as a breakout or regime-change detector that captures strong institutional price impulses while remaining sensitive to unconfirmed fakeouts.

### Research interpretation

The core falsifiable thesis is that **projecting the two-dimensional geometric visibility structure of price trajectories onto a bounded [0, 100] relative strength scale across a multi-timeframe cascade (1-minute, 5-minute, and 30-minute bars) isolates structural momentum and mean-reversion turning points, delivering persistent risk-adjusted returns (Sharpe 2.55–3.60) across equity indices, foreign exchange, and precious metals under walk-forward parameter re-optimization**:

1. **Geometric Support/Resistance Filtering:** The backward visibility condition ($p_k < p_j + (p_i - p_j) \frac{j-k}{j-i}$ for all $i < k < j$) naturally extracts the upper and lower convex hulls of past price action. Points obscured by intermediate fluctuations are eliminated from the calculation. As a result, the indicator evaluates price pressure exclusively against structurally significant pivot points.
2. **Disentanglement of Drift and Frequency:**
   - $r_S(t) = S^+(t) / S^-(t)$ reflects the directional volume/magnitude asymmetry.
   - $r_N(t) = N^+(t) / N^-(t)$ reflects the tick/count persistence asymmetry.
   - Mode $A0 = \frac{1}{2}(r_S + r_N)$ acts as a trend continuation filter: it requires both size and count to align before signaling a trend.
   - Mode $A1 = r_S / r_N$ detects explosive institutional imbalance: large price moves on low trade counts push $A1$ high while leaving $A0$ modest.
3. **Multi-Timeframe Concordance Filter:** Requiring simultaneous threshold triggers across M1, M5, and M30 bars filters out transient single-timeframe noise and ensures that micro-entries align with higher-timeframe order flow structures.
4. **Symmetric Median-Range Bracket Management:** By pegging Stop Loss and Take Profit symmetrically to a multiple of the median candle height over recent bars, the strategy enforces bounded, identical reward-to-risk geometry per trade.

*Ported Hypothesis Note:* This mechanism was evaluated on traditional OTC/Forex broker demo data (DJI30, EUR/USD, XAU/USD). Applying this framework to cryptocurrency markets is an adapted, unproven research hypothesis rather than verified crypto empirical evidence.

## Signal

The signal generation pipeline operates deterministically on discrete price series $p_t$ ($t = 0, \ldots, N$):

### 1. Backward Visibility Relation
For a given timeframe $\tau \in \{\text{M1}, \text{M5}, \text{M30}\}$ and parameters:
- Window Size: $W_S \in [10, 200]$ candles
- Window Visibility: $W_V \in [10, 200]$ candles

For each observation index $j$ within the aggregation window $j \in \{t - W_S + 1, \ldots, t\}$, consider candidate historical points $i \in \{\max(0, j - W_V), \ldots, j - 1\}$.
A point $(i, p_i)$ is visible from $(j, p_j)$ if and only if for every intermediate index $k$ satisfying $i < k < j$:
$$p_k < p_j + (p_i - p_j) \frac{j - k}{j - i}$$

The set of visible indices from $j$ bounded by $W_V$ is:
$$\mathcal{V}_j = \left\{ i \in \{\max(0, j - W_V), \ldots, j - 1\} : (i, p_i) \text{ is visible from } (j, p_j) \right\}$$
In practice, at most $W_S$ visible indices are retained:
$$\mathcal{V}_j^{(W_S)} \subseteq \mathcal{V}_j, \quad |\mathcal{V}_j^{(W_S)}| \le W_S$$

### 2. Local Increments and Directional Aggregation
The local one-step price increment associated with visible vertex $i$ is:
$$\Delta p_i = p_i - p_{i-1}$$
For observation instant $t$, sum the positive and negative increments over $j \in \{t - W_S + 1, \ldots, t\}$:
$$S^+(t) = \sum_{j=t-W_S+1}^t \sum_{i \in \mathcal{V}_j^{(W_S)}, \Delta p_i > 0} \Delta p_i$$
$$S^-(t) = \sum_{j=t-W_S+1}^t \sum_{i \in \mathcal{V}_j^{(W_S)}, \Delta p_i < 0} |\Delta p_i|$$

Concurrently, count the frequency of positive and negative increments:
$$N^+(t) = \sum_{j=t-W_S+1}^t \sum_{i \in \mathcal{V}_j^{(W_S)}, \Delta p_i > 0} 1$$
$$N^-(t) = \sum_{j=t-W_S+1}^t \sum_{i \in \mathcal{V}_j^{(W_S)}, \Delta p_i < 0} 1$$

### 3. Relative Strength Coefficients and Aggregation Variants
Relative strength coefficients for amplitude and frequency are:
$$r_S(t) = \frac{S^+(t)}{S^-(t)}, \qquad r_N(t) = \frac{N^+(t)}{N^-(t)}$$

Two aggregation modes $A$ are defined:
- **Variant A0 (Mean Aggregation):**
  $$r_{A0}(t) = \frac{1}{2} \Bigl( r_S(t) + r_N(t) \Bigr)$$
- **Variant A1 (Ratio Aggregation):**
  $$r_{A1}(t) = \frac{r_S(t)}{r_N(t)}$$

### 4. Normalization
The scalar strength indicator is normalized to the range $[0, 100]$:
$$\text{VGRSI}_{r_A}(t) = 100 - \frac{100}{1 + r_A(t)}$$
where $r_A(t)$ denotes $r_{A0}(t)$ or $r_{A1}(t)$.

### 5. Multi-Timeframe Entry Logic
The trading system runs concurrently across three timeframes: M1, M5, and M30.
- **Long Entry (Buy):**
  Triggered when $\text{VGRSI}_{r_A}(t)$ crosses the long threshold $\theta_{\text{long}} \in [20, 35]$ from above simultaneously across all three time scales (M1, M5, and M30).
- **Short Entry (Sell):**
  Triggered when $\text{VGRSI}_{r_A}(t)$ crosses the short threshold $\theta_{\text{short}} \in [70, 95]$ from above simultaneously across all three time scales (M1, M5, and M30).
- **Execution Constraints:**
  - Maximum concurrent open positions per instrument: 2 positions.
  - Minimum refractory period between consecutive trade entries: 30 minutes.

### 6. Dynamic Symmetrical Bracket Exit Logic
At the instant a trade is opened, Stop Loss (SL) and Take Profit (TP) are placed symmetrically:
- Analyze the most recent $N$ candles (both bullish and bearish).
- Compute the median candle height $h_{\text{med}} = \text{median}(\{h_k\}_{k=t-N+1}^t)$ measured in points ($h_k = \text{High}_k - \text{Low}_k$).
- Calculate the bracket distance: $\Delta P_{\text{bracket}} = Z \cdot h_{\text{med}}$, where $Z$ is a scalar multiplier.
- For Long positions: $\text{TP} = P_{\text{entry}} + \Delta P_{\text{bracket}}$, $\text{SL} = P_{\text{entry}} - \Delta P_{\text{bracket}}$.
- For Short positions: $\text{TP} = P_{\text{entry}} - \Delta P_{\text{bracket}}$, $\text{SL} = P_{\text{entry}} + \Delta P_{\text{bracket}}$.
- Positions close strictly upon hitting either the TP or SL limit.

### 7. Walk-Forward Parameter Optimization
- Rolling 30-day training window: the EA tests parameter sets ($W_S, W_V$ per timeframe in $[10, 200]$, variant $A0$ vs $A1$, thresholds $\theta_{\text{long}} \in [20, 35], \theta_{\text{short}} \in [70, 95]$, and candle height parameters $N, Z$) to identify the profit-maximizing configuration.
- Out-of-sample trading window: the selected parameter set is frozen and traded for the following 7 days.
- Rolling shift: the 30-day training window is shifted forward by 7 days, repeating across the entire 503-day sample (2024–2025).

## Required data

- **Instruments:**
  - DJI30 (Dow Jones Industrial Average index CFD).
  - EUR/USD (Euro / US Dollar spot currency pair).
  - XAU/USD (Spot Gold in US Dollars).
- **Timeframes:** 1-minute (M1), 5-minute (M5), and 30-minute (M30) aggregated candlestick bars.
- **Fields:** OHLCV (Open, High, Low, Close, Volume) and tick-level bid/ask price feeds for spread and execution accounting.
- **History & Lookback:** Minimum $W_V + W_S \le 400$ historical bars per timeframe for indicator warm-up, plus $N$ bars for median candle height calculation.
- **Point-in-Time & Availability:** Candle close must be fully confirmed before evaluating visibility relations; no future bar data is accessible.
- **Transaction Costs:** Full bid-ask spread and broker commissions included as provided by the MetaTrader 5 broker feed.

## Execution assumptions

- **Platform:** MetaTrader 5 Expert Advisor automated execution.
- **Order Types:** Market orders for entry upon multi-timeframe threshold trigger; GTC limit/stop bracket orders for Take Profit and Stop Loss.
- **Account Capitalization:** Initial portfolio capital base of USD 10,000 per instrument.
- **Position Sizing:** Fixed investment allocation of approximately USD 1,000 margin per opened trade (corresponding to ~1 lot for EUR/USD).
- **Leverage:** 1:100 leverage assumed in all simulations.
- **Fill Model:** Broker demo account execution model replicating live FOREX market bid/ask quotes, spreads, and commissions.
- **Execution Caveat:** Demo account fills assume instantaneous liquidity at top of book with zero adverse queue latency or market impact. In live institutional execution, 1:100 leverage and 1-lot market orders on M1 triggers would incur non-negligible slippage during volatile macroeconomic data releases.

## Evidence

### Source-reported

All figures trace directly to Table 1 and Section "Results" of Rafał Rak (2026), evaluated over 503 trading days (January 1, 2024 – December 31, 2025) using a rolling 30-day train $\to$ 7-day test walk-forward framework:

| Asset | All Trades (min / max / mean per 7d) | Long Trades (min / max / mean per 7d) | Short Trades (min / max / mean per 7d) | Sharpe Ratio (mean) | Max Drawdown % (mean, on $10k) | Total Trades | Trades / Day | Total Profit (USD) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DJI30** | 0 / 37 / 18 | 0 / 32 / 10 | 0 / 29 / 8 | **3.60** | **18%** | 1,842 | 3.5 | **$146,000** |
| **EUR/USD** | 0 / 45 / 16 | 0 / 40 / 7 | 0 / 39 / 9 | **2.55** | **12%** | 1,677 | 3.3 | **$69,000** |
| **XAU/USD** | 0 / 62 / 24 | 0 / 55 / 18 | 0 / 45 / 6 | **3.20** | **10%** | 2,418 | 4.8 | **$125,000** |
| **Aggregate** | — | — | — | — | **10–18%** | **5,937** | **~3.9** | **$340,000** |

- **Daily Expectancy:** Average profit of USD ~676 per trading day across the 503 trading days with USD 1,000 margin per trade.
- **Directional Balance:**
  - EUR/USD: 7 long vs. 9 short trades/week average, maintaining rising cumulative profit during extended multi-month EUR/USD downtrends.
  - DJI30: 10 long vs. 8 short trades/week average, profiting during both bull runs and correction regimes.
  - XAU/USD: 18 long vs. 6 short trades/week average, strongly capturing the persistent gold upward trend.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **High Leverage Dependency:** The reported returns ($340,000 profit on a $10,000 base) rely heavily on 1:100 leverage with USD 1,000 margin commitment per trade (~$100,000 notional exposure). On an unleveraged basis (1:1 leverage), returns would be 100-fold lower, and drawdowns on adverse gaps would be magnified relative to uncollateralized equity.
- **High-Dimensional Walk-Forward Overfitting Risk:** The optimization window tests multiple parameters ($W_S, W_V$ across three timeframes, variant $A0$ vs $A1$, thresholds, and $N, Z$ bracket parameters) over only 30 days of data. Selecting the ex-post best-performing parameter set for a 7-day out-of-sample window creates substantial risk of parameter instability and selection bias.
- **Broker Demo Environment Fill Quality:** Demo accounts execute orders without slippage, queue priority degradation, or rejection during high-volatility news spikes (e.g. FOMC, Non-Farm Payrolls), whereas real FOREX/CFD market execution frequently suffers wide spreads and slippage on market orders.
- **Intellectual Property Reservation:** The author explicitly reserves all proprietary rights to the VGRSI indicator, imposing a commercial legal barrier.

## Falsification plan

To falsify or confirm the genuine edge of the VGRSI multi-timeframe strategy:

1. **Pre-2024 Historical Out-of-Sample Test:**
   - Run the exact 30-day train / 7-day test walk-forward framework across 2018–2023 on DJI30, EUR/USD, and XAU/USD without changing the parameter grid.
   - *Failure Rule:* If the mean Sharpe ratio falls below 0.75 or cumulative profit turns negative over any rolling 6-month period, the thesis of structural geometric predictability is falsified.
2. **Transaction Cost and Spread Stress Testing:**
   - Apply realistic spread multipliers (1.5x, 2.0x, and 3.0x base spreads) and inject 10–50 ms execution latency with realistic top-of-book slippage.
   - *Failure Rule:* If doubling transaction costs erodes more than 60% of total profits, the strategy is an artifact of tight demo account execution rather than genuine structural alpha.
3. **Multi-Timeframe Concordance Ablation:**
   - Test single-timeframe execution (M1 only, M5 only, M30 only) against the full three-timeframe concordance rule.
   - *Failure Rule:* If multi-timeframe concordance does not demonstrate statistically superior risk-adjusted returns ($p < 0.05$ via block bootstrap) compared to single-timeframe baselines, the multi-scale hypothesis is rejected.
4. **Visibility Graph Randomization (Placebo Test):**
   - Shuffle intermediate price increments or replace the visibility graph selection with a random vertex sampling of equal cardinality.
   - *Failure Rule:* If the randomized visibility control produces comparable returns to the true visibility graph, the geometric visibility mechanism is proven spurious.

## Crypto portability

**Classification: Adapted / Unproven.**

The strategy was evaluated exclusively on traditional Forex, equity index, and commodity CFDs. Porting to cryptocurrency spot or perpetual markets involves significant structural discrepancies:

- **24/7 Continuous Trading:** Unlike traditional Forex with weekend market closures and distinct London/New York sessions, crypto trades continuously 24/7. Visibility horizons ($W_V$) on M1/M5/M30 will encompass different liquidity regimes during Asian, European, and US hours.
- **Perpetual Funding Rate Drag:** In crypto perpetual futures, holding positions across 8-hour funding settlements incurs funding drag. If VGRSI signals align with crowded positioning (e.g. going long when funding is highly positive), funding costs may exceed the expected price gain.
- **Exchange Fee Structure:** Crypto CEX taker fees (typically 2 to 5 bps) are significantly higher than wholesale Forex spreads (0.2–0.5 pips). Given the high trade frequency (3.3–4.8 trades/day), taker fee drag could eliminate the edge unless orders are executed strictly as passive maker limit orders.
- **Flash Wicks and Liquidation Cascades:** Crypto markets exhibit sharp, high-frequency liquidation spikes. Symmetrical SL/TP brackets pegged to median candle heights ($h_{\text{med}}$) are prone to premature stop-outs during localized order-book sweeps.

## Limitations

- **Arbitrary Walk-Forward Windows:** The 30-day training and 7-day test windows were chosen heuristically by the author without systematic sensitivity analysis.
- **Underspecified Parameter Grid:** The paper specifies search ranges for $W_S, W_V \in [10, 200]$, thresholds $[20, 35]$ and $[70, 95]$, but omits the exact grid step sizes and tie-breaking criteria for parameter selection.
- **Capacity Unmodeled:** Sizing was fixed at USD 1,000 margin per trade; market impact, book depth consumption, and liquidity scaling limits were not addressed.
- **Demo Account Execution:** All results are derived from a broker demo account rather than live production accounts with real liquidity matching.

## Implementation status

- `not-implemented`: This strategy record is a normalized research capture only.
- No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been executed.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- Inclusion in this repository does not constitute authorization to trade, backtest on shared infrastructure, or implement in production. Any future consideration requires independent replication on clean historical data with realistic transaction costs and resolution of author IP rights.

## Related Wiki records

- `[[bollinger-bands_ohlcv-2026-08-31]]`
- `[[rsi-mean-reversion_ohlcv-2026-08-31]]`
- `[[crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]`
- `[[strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]`
- `[[forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02]]`

## Sources

- Rafał Rak, *"Visibility graphs can make money in financial markets"*, arXiv preprint `arXiv:2605.01300v1 [cs.CE, physics.data-an, q-fin.TR]`, May 2, 2026. DOI: [10.48550/arXiv.2605.01300](https://doi.org/10.48550/arXiv.2605.01300). Stable URL: [https://arxiv.org/abs/2605.01300](https://arxiv.org/abs/2605.01300). Full HTML text: [https://arxiv.org/html/2605.01300v1](https://arxiv.org/html/2605.01300v1).
