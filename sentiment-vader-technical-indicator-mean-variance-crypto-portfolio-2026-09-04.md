---
schema: strategy-research-record-v1
title: "Sentiment-Aware Mean-Variance Portfolio Optimization for Cryptocurrencies"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - portfolio-optimization
  - sentiment-analysis
  - mean-variance
  - technical-indicators
  - VADER
  - LLM
status: research-only
confidence: medium
source_as_of: "2026-03-03"
sources:
  - "Qizhao Chen, 'Sentiment-Aware Mean-Variance Portfolio Optimization for Cryptocurrencies', arXiv:2508.16378v2 [cs.CE, q-fin.ST], submitted August 22, 2025 (revised March 3, 2026). Accepted by Digital Finance journal. https://arxiv.org/abs/2508.16378"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Sentiment-Aware Mean-Variance Portfolio Optimization for Cryptocurrencies

## Provenance

- **Primary Source:** Qizhao Chen, "Sentiment-Aware Mean-Variance Portfolio Optimization for Cryptocurrencies," arXiv:2508.16378v2 [cs.CE, q-fin.ST], submitted August 22, 2025; revised March 3, 2026. Accepted by *Digital Finance* journal.
- **Canonical arXiv URL:** https://arxiv.org/abs/2508.16378
- **Canonical HTML URL:** https://arxiv.org/html/2508.16378v2
- **Source Data As-Of:** Sample spans February 14, 2020 – August 6, 2025 (2,001 daily observations). Data sourced from Crypto Compare API (price and news).
- **Pre-Write Deduplication Audit:** A repository-wide search for `arXiv:2508.16378`, `Qizhao Chen`, `Crypto Compare.*News API`, and `VADER.*Gemini.*crypto` found zero existing records. Related repository records examine sentiment-driven Bitcoin prediction (`raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04.md`) and RL-based sentiment alpha for equities (`finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02.md`), but neither uses VADER + technical indicators → Ridge regression → constrained mean-variance portfolio optimization for crypto.

## Economic mechanism

### Source-reported

Cryptocurrency markets are highly volatile and driven by both price trends and public sentiment. News events, social media, and regulatory developments significantly influence investor behavior and short-term price dynamics. Traditional mean-variance optimization (MVO) alone fails to capture the forward-looking information embedded in news sentiment and technical momentum. By incorporating sentiment scores alongside technical indicators into the expected-return estimation step of MVO, the strategy aims to produce more adaptive allocation decisions that respond to shifts in market mood and momentum state.

### Research interpretation

The hypothesized alpha mechanism is a **sentiment-augmented return signal** layered onto classical Markowitz portfolio construction:

- **Component 1 (Trend):** 14-day SMA crossover binary indicator captures whether current price is above or below its 14-day moving average, providing a directional momentum filter.
- **Component 2 (Momentum):** 14-day RSI captures overbought/oversold conditions; however, source-reported results show the RSI coefficient is near-zero for most of the sample, suggesting limited independent predictive power at the daily horizon.
- **Component 3 (Sentiment):** Daily VADER compound score aggregated from Crypto News API articles provides a noise-trader-sentiment signal.
- **Fusion mechanism:** A rolling-window Ridge regression (180-day window, daily re-estimation) combines RSI, SMA binary, and VADER sentiment into a single return-prediction adjustment term ε̂_t. This adjusts the empirical mean return μ_close to produce μ_adj = μ_close + ε̂_t, which feeds into constrained MVO.
- **Portfolio construction:** Constrained long-only MVO with risk aversion λ=2, per-asset weight cap w_max=0.4, and daily turnover cap τ_max=0.80, solved via quadratic programming.
- **LLM verification (exploratory):** Google Gemini 1.5 Flash is used as a secondary verifier on VADER scores, providing contextual cross-checks on sentiment classification. This is not part of the trading signal — it is a qualitative analysis layer.

The core hypothesis is that news sentiment provides incremental return-predictive information beyond price-based technicals, and that a Ridge regression fusion avoids overfitting while maintaining interpretability.

## Signal

### Formation timestamp
- **Observation time:** End of each trading day (daily close, UTC).
- **Signal formation:** Ridge regression re-estimated daily using the trailing 180-day window. The latest feature vector X_t = [RSI_t, 1(P_t > SMA_t), s_t] is evaluated using the fitted coefficients to produce ε̂_t.
- **Tradability:** Portfolio weights are computed and rebalanced daily based on closing prices. Execution is assumed next-day open (source does not explicitly specify same-bar vs next-bar; the daily frequency implies close-to-open).

### Lookback
- **RSI:** 14-day lookback.
- **SMA:** 14-day lookback.
- **Sentiment:** Daily VADER compound score (no lookback — contemporaneous with news publication).
- **Ridge regression window:** 180-day rolling window, estimated daily.
- **Covariance matrix:** 180-day rolling sample covariance, no shrinkage or robust adjustment.

### Entry / Exit
- **Long-only:** All positions are long. No short positions.
- **Weight determination:** Constrained MVO produces optimal weights w_t. Assets with higher adjusted expected return and lower covariance receive larger allocations.
- **Weight cap:** No single asset may exceed 40% of portfolio weight.
- **Turnover constraint:** Daily |w_t − w_{t-1}||₁ ≤ 0.80.
- **Rebalancing:** Daily, solving the constrained quadratic program.

### Parameters
| Parameter | Value | Source |
|-----------|-------|--------|
| RSI period | 14 | Source-specified |
| SMA period | 14 | Source-specified |
| Ridge regression window | 180 days | Source-specified |
| Ridge regularization α | Tuned via cross-validation within each rolling window | Source-specified |
| Risk aversion λ | 2 | Source-specified |
| Weight cap w_max | 0.4 | Source-specified |
| Turnover cap τ_max | 0.80 | Source-specified |
| Transaction cost c | 0.1% one-way | Source-specified |

All parameters above are source-specified. No post-hoc tuning or Scout-generated operationalization.

### Position sizing
- Fully invested (sum of weights = 1).
- Equal opportunity for all five assets up to the 40% cap.
- No leverage, no shorting.

## Required data

- **Universe:** BTC, ETH, ADA, BNB, XRP (fixed over sample period, top 5 by market cap at inception).
- **Venue:** Not specified; data sourced from Crypto Compare API.
- **Market type:** Spot (closing prices used).
- **Timeframe:** Daily.
- **Fields:** Closing price, volume (not directly used in signal), VADER sentiment compound score.
- **Sentiment data source:** Crypto Compare News API — daily aggregation of article VADER compound scores per asset.
- **Point-in-time:** Source states all data converted to UTC; portfolio built using only past data up to end of training period, returns calculated on following day. However, the VADER sentiment score for day t is contemporaneous with day t's news, which may arrive during the trading day — exact availability lag is not specified.
- **Missing data:** Not explicitly addressed by the source.
- **Risk-free rate:** U.S. Treasury 3-month bill yield (for Sharpe ratio calculation).

## Execution assumptions

- **Signal-to-order timing:** Daily rebalancing at close; execution assumed at next open (inferred from daily frequency; source does not explicitly state).
- **Order type:** Not specified; assumed market orders for daily rebalancing.
- **Fill model:** Not specified; assumed perfect fill at close/open.
- **Fees:** One-way transaction cost of 0.1% applied to all traded notional (source-specified). Maker/taker split not distinguished.
- **Slippage:** Not explicitly modeled beyond the 0.1% transaction cost.
- **Spread:** Not modeled.
- **Funding:** Not applicable (spot, no perpetual/futures).
- **Leverage:** None; fully invested long-only.
- **Capacity:** Not analyzed. Universe of 5 large-cap assets limits the practical capacity question.
- **Impact:** Not modeled.
- **Partial fills / failures:** Not addressed.

## Evidence

### Source-reported

All figures below are directly reported by Chen (arXiv:2508.16378v2, Table 2 of Section 4.2). Sample: Feb 2020 – Aug 2025, daily, 5 crypto assets, 180-day rolling window, 0.1% one-way cost.

| Strategy | Annualized Sharpe | Max Drawdown (%) | Cumulative Return |
|----------|------------------|-------------------|-------------------|
| Proposed (Sentiment + Technical) | 0.7102 | 81.95 | 6.0555 |
| Sentiment Only | 0.5976 | 88.99 | 2.6861 |
| Technical Only | 0.7026 | 83.07 | 4.8510 |
| Momentum (TSMOM) | 0.6967 | 85.92 | 4.7143 |
| Equal-Weighted | 0.5823 | 75.06 | 2.3911 |
| Bitcoin Long-Short | 0.5454 | 79.63 | 1.9085 |

- The proposed strategy achieves the highest Sharpe ratio (0.71) and cumulative return (6.06x over ~5.5 years).
- All strategies exhibit drawdowns exceeding 75%, with the proposed strategy at 81.95%.
- The technical-only variant (Sharpe 0.70) performs nearly as well as the full strategy, suggesting sentiment adds marginal incremental value.
- The sentiment-only variant (Sharpe 0.60) underperforms technical-only, indicating sentiment alone is a weaker standalone signal.
- Source notes that the RSI coefficient remains near-zero throughout most of the sample, implying RSI contributes little to the Ridge regression.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Extreme drawdowns:** All strategies, including the proposed one, experience drawdowns exceeding 75%. The source acknowledges: "the current signals cannot fully shield the portfolio during periods of rapid market stress." The 2022 crypto downturn (Terra/LUNA, FTX, credit platform failures) caused correlations to spike across all assets, erasing diversification benefits.
- **Weak incremental value of sentiment:** The marginal improvement from adding sentiment to technical-only is small (Sharpe 0.71 vs 0.70), and the sentiment-only variant underperforms technical-only. The paper's own coefficient analysis shows the RSI coefficient is near-zero, and the sentiment coefficient is the most volatile of the three features.
- **No regime awareness:** The 180-day rolling covariance without shrinkage or regime detection is acknowledged as "sensitive to noise and large price swings" and "does not account for heavy-tailed return behavior."
- **Static universe:** The five-asset universe is fixed over the entire sample period. No new asset inclusion, no survivorship handling discussed.

## Falsification plan

1. **Out-of-sample extension:** Extend the sample beyond August 2025 to assess whether the Sharpe 0.71 persists in subsequent market conditions. The source's own limitation section acknowledges the need for stronger model robustness.
2. **Cost sensitivity:** Test performance at higher transaction cost levels (5, 10, 15, 20 bps) to determine the cost threshold at which alpha is eroded. The source uses 0.1% (10 bps) one-way, which is relatively low for retail crypto trading.
3. **Universe expansion:** Re-run with a larger, dynamic universe including mid- and small-cap cryptos to test whether the mechanism generalizes beyond the top 5 assets.
4. **Regime-conditional decomposition:** Decompose performance by bull/bear/sideways regimes to identify whether the strategy's alpha is concentrated in specific market conditions. The source notes the 2022 crash period was catastrophic for all strategies.
5. **Covariance model robustness:** Replace the 180-day rolling sample covariance with shrinkage (Ledoit-Wolf) or exponential weighting to test sensitivity to the risk model.
6. **Ablation of individual features:** Remove SMA and RSI individually to isolate whether sentiment adds value conditional on each technical indicator. The source provides sentiment-only and technical-only variants but does not test SMA-only or RSI-only.
7. **LLM integration test:** Incorporate Gemini-validated sentiment scores (rather than VADER alone) into the Ridge regression to test whether LLM-filtered sentiment improves the signal.

## Crypto portability

**Direct** — the strategy is natively designed for crypto spot markets.

- The universe consists of top-5 market-cap cryptocurrencies.
- Spot prices are used (no perpetual/futures/funding considerations).
- The 24/7 trading nature of crypto is not explicitly addressed for signal timing (daily close assumed).
- No funding rate, borrow cost, or leverage assumptions.
- The strategy's high drawdowns (82%) are particularly concerning for crypto, where volatility regimes can persist for months.

## Limitations

- **Extreme drawdowns:** The most critical limitation. An 82% max drawdown over the sample period means the strategy would have experienced catastrophic losses during the 2022 bear market. This makes the strategy practically unusable without additional risk management (e.g., regime detection, stop-loss, volatility scaling).
- **Small universe:** Only 5 fixed assets over a 5.5-year period. No dynamic reconstitution, no mid/small-cap exposure.
- **Risk model fragility:** 180-day rolling sample covariance without shrinkage, robust estimation, or regime adjustment. Source explicitly acknowledges this limitation.
- **Marginal sentiment contribution:** The full strategy (Sharpe 0.71) barely outperforms technical-only (Sharpe 0.70). The incremental value of sentiment in the Ridge regression is minimal.
- **No independent reproduction:** Results have not been independently verified.
- **Transaction cost modeling:** Flat 0.1% one-way cost; no spread, slippage, or impact modeling. For retail-sized portfolios on major exchange pairs, 10 bps is plausible, but for larger sizes or less liquid pairs, costs would be materially higher.
- **Publication status:** Accepted by *Digital Finance* journal but not yet published at time of record creation. The arXiv preprint (v2) was submitted March 2026.
- **LLM verification is qualitative:** The Gemini cross-check on VADER scores is not incorporated into the trading signal; it is a post-hoc analysis layer.
- **data gap:** Exact availability timing of VADER sentiment scores relative to market close is not specified. If news sentiment is only available after market close, same-day portfolio construction using that sentiment would involve look-ahead bias.

## Implementation status

No implementation in our research stack has been completed. The strategy is research-only.

## Adoption boundary

This record is research material only. Presence in this repository does not imply:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The high drawdown (82%) and marginal incremental value of sentiment over technical-only make this a low-priority candidate for further validation.

## Related Wiki records

- [[raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04]] — Different mechanism: regime-gated FinBERT + OHLCV fusion for 3h/6h Bitcoin direction classification, not portfolio optimization.
- [[finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]] — Different mechanism: GRPO reinforcement learning for cross-sectional equity sentiment alpha, not crypto MVO.
- [[crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03]] — Different mechanism: Fear & Greed EMA contrarian signals, not sentiment + technicals → MVO.

## Sources

- Chen, Q. (2025/2026). "Sentiment-Aware Mean-Variance Portfolio Optimization for Cryptocurrencies." arXiv:2508.16378v2 [cs.CE, q-fin.ST]. Submitted August 22, 2025; revised March 3, 2026. Accepted by *Digital Finance*. https://arxiv.org/abs/2508.16378
