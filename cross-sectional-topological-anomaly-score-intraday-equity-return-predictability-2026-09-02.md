---
schema: strategy-research-record-v1
title: "Cross-Sectional Topological Anomaly Scores and Intraday Return Predictability: BallMapper, Decoder-Conditional VAE, and Function-on-Function Regression"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - topological-data-analysis
  - anomaly-detection
  - intraday
  - equity
  - sp500
  - variational-autoencoder
  - ballmapper
  - function-on-function-regression
status: research-only
confidence: medium
source_as_of: 2026-06-07
sources:
  - "Krzysztof Ozimek, 'Cross-sectional topological anomaly scores and intraday return predictability in the S&P 500: A BallMapper, decoder-conditional VAE, and Function-on-Function regression approach', arXiv preprint arXiv:2606.08586v1 [q-fin.ST], submitted June 7, 2026. DOI: 10.48550/arXiv.2606.08586. Stable URL: https://arxiv.org/abs/2606.08586"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Topological Anomaly Scores and Intraday Return Predictability: BallMapper, Decoder-Conditional VAE, and Function-on-Function Regression

## Provenance

- **Source**: arXiv:2606.08586v1, submitted June 7, 2026.
- **Author**: Krzysztof Ozimek (sole author). Contact: contact@drkrzysztofozimek.com.
- **Subject**: Statistical Finance (q-fin.ST). MSC classes: 91G15, 91G70.
- **Sample period**: April 2025 – March 2026 (12 calendar months).
- **Universe**: 10 most liquid S&P 500 constituents selected by Amihud (2002) illiquidity ratio from daily price/volume data (Yahoo Finance). Constituents: NVDA, AAPL, TSLA, AMZN, META, MSFT, GOOG, GOOGL, AVGO, PLTR. GOOG and GOOGL are included as separate instruments because their intraday price formation is share-class-specific.
- **Data**: Intraday OHLCV from EODHD (eodhd.com) at four bar granularities: 5 min, 15 min, 30 min, 60 min.
- **Sample window characteristics**: Encompasses broad U.S. tariff announcement (April 2, 2025), trade-policy escalation, Russia-Ukraine conflict continuation, military strikes on Iranian nuclear infrastructure (June 2025), and renewed U.S.-Iran-Israel tensions (Q1 2026). These events generated repeated episodes of volatility clustering, sectoral repricing, and liquidity shifts.
- **License**: CC-BY 4.0.

## Economic mechanism

### Source-reported

The author proposes that standard anomaly detection methods score statistically unusual observations in observable data but miss topologically misexpected persistent deviations in the latent structure of cross-sectional co-movement. An anomaly, as defined in this paper, is any mismatch between the intraday return pattern expected for a stock — given the market's current return structure as seen topologically and the stock's peer group — and what is actually observed, regardless of the magnitude or direction of the departure. The history of such mismatches serves as the predictor of subsequent cumulative returns.

Three hypotheses are tested:
- **H1**: The cumulative return impact of an anomaly episode accumulates gradually and persistently across the forecast horizon (consistent with limits-to-arbitrage, Shleifer & Vishny 1997).
- **H2**: Predictive content is distributed broadly across the full history window, with a statistically significant lean toward more recent observations (consistent with information-decay principle, Engle 1982).
- **H3**: The cumulative return impact of an anomaly episode typically reverses direction before the end of the forecast horizon (consistent with overreaction-and-correction regularity, De Bondt & Thaler 1985, and liquidity-provision mechanism, Grossman & Miller 1988).

### Research interpretation

The proposed mechanism is that structural co-movement anomalies — topologically mispositioned assets within a cross-sectional co-movement graph — persist due to limits-to-arbitrage and inventory-driven price correction dynamics. Assets that are geometrically isolated from their peer group in the BallMapper graph exhibit systematically different subsequent return profiles. The VAE scores capture the degree of structural isolation or mispositioning relative to peers, and the history of these scores contains forward-looking information about return curves.

This is a cross-sectional structural anomaly hypothesis, not a momentum, mean-reversion, or factor-exposure hypothesis. The hypothesized alpha channel is: structural co-movement anomalies → limits-to-arbitrage → gradual return correction → predictable return curve shape.

## Signal

### Formation timestamp

- The topological pipeline operates on intraday return snapshots at the end of each bar period (5/15/30/60 min).
- The Takens delay embedding creates a 3-dimensional embedding vector for each stock at each snapshot.
- BallMapper graphs the cross-sectional co-movement structure from these embeddings.
- The decoder-conditional VAE scores each stock at each snapshot.
- The signal is the time series of anomaly scores for each stock.

### Lookback

- **Predictor window (W)**: ⌈5b⌉ bars, where b = bars per day. Economic time: approximately 5 trading days across all bar frequencies (W ≈ 2.5 × b).
- **Warm-up period**: Not explicitly stated in the paper; the Takens delay embedding requires an initial embedding window (the embedding dimension is 3).
- **Endpoints**: Inclusive (the anchor snapshot is included in the predictor window).

### Entry

- **Research-proposed (not specified by source)**: The paper establishes predictive content but does not propose specific entry rules. A research-proposed long/short entry rule would be: go long assets with the most negative recent anomaly score trajectory (potential undervaluation from structural mispositioning) and short assets with the most positive trajectory, but this is not validated by the source.
- The signal is a scoring mechanism, not a directional trade signal on its own.

### Exit

- **Research-proposed**: Forecast horizon (H) = ⌈2b⌉ bars (approximately 2 trading days). The source establishes that predictive content exists within this horizon but does not specify exit rules.

### Holding period

- Maximum holding period (research-proposed): 2 trading days (matching the forecast horizon H).

### Parameters

- **Takens delay embedding**: Dimension d = 3 (source-specified).
- **BallMapper algorithm**: Uses BallMapper to graph the cross-sectional co-movement structure (Dłotko 2019).
- **VAE variants**: Three decoder-conditional variants (VAE-I, VAE-II, VAE-III) with different peer-context encodings (raw, aggregate, attention-weighted).
- **Bar frequencies**: 5 min, 15 min, 30 min, 60 min (source-specified).
- **W/H ratio**: 5×b / 2×b ≈ 2.5 (source-specified).
- All parameters are source-specified or derived from the source's stated methodology.

## Required data

- **Instrument**: 10 most liquid S&P 500 constituents (NVDA, AAPL, TSLA, AMZN, META, MSFT, GOOG, GOOGL, AVGO, PLTR).
- **Universe**: S&P 500 constituents ranked by Amihud (2002) illiquidity ratio; top 10 by liquidity retained.
- **Venue**: Not venue-specific; data sourced from EODHD and Yahoo Finance.
- **Timeframe**: Intraday OHLCV at 5 min, 15 min, 30 min, 60 min bars.
- **Fields**: Open, High, Low, Close, Volume.
- **Point-in-time**: EODHD data; publication/availability lag not stated.
- **Timestamp**: Timezone not explicitly stated; intraday data for U.S. equities implies U.S. market hours (ET).
- **Missing-data**: Not discussed by source.

## Execution assumptions

- **Signal-to-order timing**: Not specified by source.
- **Execution model**: Not specified by source.
- **Fees, spread, slippage, impact**: Not modeled by source. The paper is a predictive-content study, not a backtested strategy.
- **Fill model**: Not specified.
- **Leverage/margin**: Not specified.
- **Latency**: Not specified.
- **Source assumption gap**: The paper establishes statistical predictive content but provides no trading simulation or cost-adjusted returns.

## Evidence

### Source-reported

- Predictive content confirmed across all 10 assets, all four intraday bar frequencies (5min, 15min, 30min, 60min), and all three VAE scoring variants via penalised function-on-function regression.
- Consistent temporal fingerprint: gradual accumulation of return impact, frequent early reversal of direction, broadly distributed predictive content weighted toward recent anomaly history.
- When reversal occurs depends on market regime; how evenly anomaly history contributes to prediction depends on bar frequency.
- Reversal observed in 66.7% of observations (320 of 480 across the factorial design).
- Five scalar measures quantify the return-impact profile: front-load ratio (δ(H/4)), median effect horizon (h0.50), predictor centre of mass (w̄), uniformity ratio (U), zero-crossing horizon (h*).
- Mixed-effects models (LMM and binomial GLMM) with random asset intercepts, Type III Satterthwaite F-tests. Overall LRT p-values < 0.001 for most measures, confirming that the full fixed-effects model outperforms random-intercept-only null.
- Quarter and timeframe effects are statistically significant for several measures, indicating regime and frequency dependence.
- Source reports no transaction costs, no portfolio construction, and no risk-adjusted performance metrics.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges three principal limitations: (1) small sample of 10 stocks from a single index, (2) limited sample period of 12 months, (3) the paper is a predictive-content study, not a backtested strategy.
- The paper does not report false-positive rates, multiple-testing corrections across assets/bars/methods, or economic significance of the predictive relationship after costs.
- Source-reported: quarter effects and timeframe effects are significant, suggesting the relationship is not uniform across regimes or frequencies. This could indicate fragility if the relationship is regime-dependent.

## Falsification plan

- **Out-of-sample**: Test the topological anomaly score on a different universe (e.g., Russell 1000, mid-caps, non-U.S. equities) and different time period.
- **Multiple-testing correction**: Apply Bonferroni, Benjamini-Hochberg, or permutation-based corrections across the 10 assets × 4 timeframes × 3 methods factorial design.
- **Economic significance**: Construct a simple long/short portfolio based on the anomaly score and measure Sharpe ratio, turnover, and capacity after realistic transaction costs.
- **Parameter perturbation**: Vary embedding dimension d (source uses d=3), predictor window W, and forecast horizon H.
- **Placebo test**: Shuffle the cross-sectional labels of stocks at each snapshot and re-run the full pipeline. The BallMapper graph structure should disappear, and predictive content should vanish.
- **Alternative universe**: Test on crypto cross-sectional data (e.g., top 10 crypto by market cap) to assess portability.
- **Regime breakdown**: Split the sample by volatility regime (VIX high vs. low) and test whether predictive content persists.
- **Failure metric**: If the function-on-function regression R² drops below 0.01 or the five scalar measures lose statistical significance after multiple-testing correction, the hypothesis is weakened.
- **Action on failure**: Discard the signal or restrict it to the specific regime/frequency where significance survives.

## Crypto portability

**Unproven**.

- The paper studies U.S. equities on regulated exchanges with centralized limit order books and fixed trading sessions.
- Crypto markets have 24/7 sessions, fragmented venues, different microstructure (perpetuals, funding, mark/index prices), and generally higher noise-to-signal ratios.
- The Takens delay embedding and BallMapper approach are theoretically applicable to any cross-sectional time series, including crypto returns, but the specific statistical relationships (limits-to-arbitrage, liquidity-provision mean reversion) may not transfer.
- Crypto-specific risks: (1) venue fragmentation means cross-sectional co-movement may be distorted by venue-specific liquidity patterns; (2) 24/7 sessions mean the embedding dynamics differ; (3) no pre-market/after-hours distinction; (4) the top 10 crypto by market cap have very different liquidity profiles than the top 10 S&P 500 stocks.
- Portability to crypto would require re-validation on crypto intraday data.

## Limitations

- **Small sample**: Only 10 stocks from a single index; results may not generalize.
- **Short sample period**: 12 months (April 2025 – March 2026); regime-specific effects may not hold in other periods.
- **No trading simulation**: The paper establishes predictive content but does not test whether this translates into profitable trading after costs.
- **No multiple-testing correction reported**: The factorial design (10 assets × 4 timeframes × 3 methods = 120 cells for each measure) raises multiple-testing concerns.
- **No economic significance**: No Sharpe ratio, drawdown, or risk-adjusted return metrics reported.
- **Source quality**: Single-author preprint, not peer-reviewed at time of submission. No independent replication.
- **Data gap**: EODHD intraday data quality, availability lag, and revision history not discussed.
- **Underspecified**: The Takens delay embedding parameter (time delay τ) is not explicitly stated in the available text.
- **Omitted variable risk**: The predictive relationship may be driven by unmodeled factors (e.g., sector rotation, news events) rather than topological structure per se.

## Implementation status

Not implemented. No implementation in our research stack has been completed. The paper is a statistical predictive-content study, not a backtested strategy.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- [[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]] — related TDA method but different mechanism (persistent homology filtering + sentiment vs. BallMapper + VAE anomaly scoring).
- [[quant/equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02]] — related cross-sectional TDA but different mechanism (HNN-MFCF dependence architecture vs. BallMapper + VAE).

## Sources

- Krzysztof Ozimek, 'Cross-sectional topological anomaly scores and intraday return predictability in the S&P 500: A BallMapper, decoder-conditional VAE, and Function-on-Function regression approach', arXiv:2606.08586v1 [q-fin.ST], submitted June 7, 2026. DOI: 10.48550/arXiv.2606.08586. Stable URL: https://arxiv.org/abs/2606.08586. License: CC-BY 4.0.
