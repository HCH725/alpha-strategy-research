---
schema: strategy-research-record-v1
title: Crypto Macro-Sentiment Contrarian Timing via Fear & Greed Index EMA
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - macro-sentiment
  - contrarian
  - fear-and-greed
  - timing
  - behavioral-finance
status: research-only
confidence: medium
source_as_of: 2025-11-19
sources:
  - https://arxiv.org/abs/2512.02029
  - https://arxiv.org/pdf/2512.02029
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Macro-Sentiment Contrarian Timing via Fear & Greed Index EMA

## Provenance

- **Source:** Zhang, Weikang and Watts, Alison (2025). "HODL Strategy or Fantasy? 480 Million Crypto Market Simulations and the Macro-Sentiment Effect."
- **arXiv:** 2512.02029v1
- **Submitted:** November 19, 2025
- **Subject:** q-fin.ST (Statistical Finance)
- **Full text:** https://arxiv.org/pdf/2512.02029
- **Data source for FGI:** Alternative.me Crypto Fear & Greed Index (https://alternative.me/crypto/fear-and-greed-index/)
- **Universe:** 378 non-stablecoin crypto assets from CoinMarketCap top 800, with 8 analysis baskets (BTC, ETH, ADA, BNB, DOGE, LINK, XRP, and ALL market-wide basket)
- **Sample period (Monte Carlo):** Daily OHLCV from Yahoo Finance, earliest available through approximately April 2025; assets with first date on or after 2024-01-01 removed
- **Sample period (Bayesian projection):** Weekly frequency, approximately 2019–2025 (exact start dependent on FGI availability and stationarity transforms)

## Economic mechanism

### Source-reported

The authors argue that realized risk-return distributions (endogenous predictors) offer limited generalizable guidance for future crypto outcomes, while macro-finance sentiment indicators—particularly the smoothed Fear & Greed Index—demonstrate persistent long-horizon predictive power. They attribute this to sentiment-driven market dynamics: elevated aggregate sentiment (high FGI EMA24) precedes periods of lower forward returns, consistent with behavioral overreaction and herding in crypto markets. DOGE exhibits ~3x greater sentiment sensitivity than established tokens, consistent with its meme-coin status and higher retail speculative participation.

### Research interpretation

**Hypothesis (research-proposed):** The 24-week exponential moving average of the Crypto Fear & Greed Index (FGI EMA24w) serves as a contrarian timing signal for crypto allocations.

- **Mechanism:** Behavioral overreaction and retail herding inflate sentiment-driven price dislocations; the smoothed FGI captures the slow-moving component of aggregate market sentiment, acting as a mean-reversion anchor. High sentiment (elevated FGI EMA24w) predicts lower subsequent risk-adjusted returns; low sentiment predicts higher subsequent returns.
- **Signal construction (research-proposed):** Reduce crypto allocation when FGI EMA24w is elevated (above its long-run mean); increase allocation when FGI EMA24w is depressed. The paper does not specify entry/exit thresholds or allocation sizing—these are research-proposed.
- **Horizon:** The effect is strongest at 181–1095 day horizons, suggesting this is a long-frequency timing signal rather than a short-term trading rule.
- **Cross-asset universality:** The signal is most stable across 6 of 8 baskets (XRP and ALL are excluded because stability selection did not retain FGI EMA24w for those baskets). DOGE shows disproportionate sensitivity (~3x other tokens).

## Signal

### Formation timestamp

- FGI daily values are aggregated to weekly mean (Monday–Sunday) from Alternative.me API.
- EMA24w is computed on the fractionally differenced FGI series: first, the raw FGI series is assessed for unit-root status; if classified as random walk, fractional differencing with d=0.5 and K=200 lags is applied; then EMA with w=24 weeks is computed on the transformed series.
- The signal becomes tradable at the start of the week following the EMA computation.

### Lookback

- EMA window: 24 weeks (approximately 6 months).
- Fractional differencing: d=0.5, truncation K=200 lags (strictly causal).
- The paper uses expanding-window z-score standardization for the predictor.

### Entry (research-proposed)

- **Long signal:** When FGI EMA24w z-score is below its long-run mean (i.e., sentiment is depressed), increase crypto allocation.
- **Short/underweight signal:** When FGI EMA24w z-score is above its long-run mean (i.e., sentiment is elevated), reduce crypto allocation or tilt toward defensive positioning.
- The paper does NOT specify entry thresholds, binary triggers, or exact allocation rules. The contrarian timing framework is research-proposed.

### Exit (research-proposed)

- Not specified by the source. Research-proposed: exit when FGI EMA24w reverts toward its long-run mean, or at a fixed rebalance cadence (e.g., monthly).

### Holding period

- The paper's impulse responses span 30–1095 days. The strongest effects appear at 181–1095 day horizons, suggesting a multi-month to multi-year holding period.

### Parameters

- **FGI EMA24w:** 24-week EMA of the Fear & Greed Index (parameter source: the paper's stability selection procedure retained this as the most stable long-run predictor across baskets).
- **Fractional differencing d=0.5:** Applied to series classified as random walk by unit-root tests.
- **Thresholds, allocation sizing, rebalance cadence:** Not specified by the source. Research-proposed.

### Key quantitative findings (source-reported)

- One-standard-deviation increase in FGI EMA24w reduces forward mean excess return (top 25%) by **15–22 percentage points** over 1–3 year horizons.
- One-standard-deviation increase reduces forward median excess return by **6–10 percentage points** over 1–3 year horizons.
- DOGE shows ~3x greater sensitivity: a one-std-dev FGI shock reduces DOGE's forward top-quartile mean by ~48pp at the 365-day horizon vs ~10–11pp for BNB/ADA.
- The signal is significant at 95% credible interval in 5 of 8 baskets for top-quartile returns at 181–365 day horizons.

## Required data

- **Instrument:** Broad crypto universe (378 non-stablecoin assets), with focus on major tokens (BTC, ETH, ADA, BNB, DOGE, LINK, XRP).
- **Venue:** CoinMarketCap (universe selection), Yahoo Finance (OHLCV), Alternative.me (Fear & Greed Index).
- **Market type:** Spot crypto (data sourced as USD pairs; perpetual/futures not explicitly analyzed for this signal).
- **Timeframe:** Weekly aggregation (Monday–Sunday mean of daily FGI; weekly EMA).
- **Fields:** Fear & Greed Index (0–100 scale); crypto OHLCV for universe construction and Monte Carlo simulation.
- **Point-in-time:** FGI is published daily with no stated lag; the paper aggregates to weekly mean. The expanding-window z-score avoids look-ahead bias.
- **Timestamp:** Weekly index aligned to Monday of each week.
- **Missing-data:** Tokens with insufficient history, stablecoins, and low-volume tokens are excluded per the paper's cleaning protocol. FGI data availability assumed continuous.

## Execution assumptions

The paper does NOT propose a specific trading strategy with entry/exit/position-sizing rules. The macro-sentiment finding is an impulse-response result from a Bayesian local projection model, not a backtested trading strategy. Execution assumptions are therefore research-proposed:

- **Signal-to-order timing:** Monthly or quarterly rebalance at start of month (research-proposed).
- **Order type:** Market order assumed (research-proposed).
- **Fill model:** Assumed instantaneous at weekly close (research-proposed); paper uses weekly aggregated data.
- **Fees:** The Monte Carlo portion of the paper uses 14 bps one-way fee (matching major exchange taker fees at 0.10%). The macro-sentiment finding itself does not incorporate trading costs.
- **Slippage:** Not modeled in the macro-sentiment projection analysis.
- **Funding:** Not applicable for spot; not modeled for perpetuals.
- **Leverage:** Not specified.
- **Capacity:** Not assessed; the signal targets a broad crypto universe with varying liquidity.

## Evidence

### Source-reported

- **Method:** Bayesian multi-horizon local projection with stability-selected macro-finance predictors, estimated via No-U-Turn Sampler (NUTS) with 4 chains, target_accept=0.95, max_treedepth=12. All baskets achieve convergence (R-hat = 1.00, ESS > 900, divergences < 0.05%).
- **Robustness:** Classical local projection (LP) with stationary bootstrap and simultaneous bands confirms the BLP results: 95% intervals overlap in 98.7% of cases; when both models flag significance, sign match is 100%.
- **Key result:** FGI EMA24w is the most stable long-run predictor across baskets for forward top-quartile and median excess returns at 181–1095 day horizons. Effect sizes: 15–22pp reduction in top-quartile mean and 6–10pp reduction in median per one-std-dev shock.
- **Cross-basket:** Significant in 5 of 8 baskets at 181–365 day horizon for top-quartile returns. DOGE shows 3x greater sensitivity. XRP and ALL excluded from FGI EMA24w analysis (stability selection did not retain this predictor for those baskets).
- **Monte Carlo context:** The paper's primary contribution is demonstrating HODL risk (median excess return -28.4% at 731–1095 days for ALL basket; CVaR1% approaching 1.0). The macro-sentiment finding is a secondary analysis.
- **This result has not been independently reproduced.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No single macro-finance predictor achieves 95% credible-interval significance across all 8 baskets simultaneously—cross-basket heterogeneity is substantial.
- The signal is not significant for XRP or the ALL basket at the stability selection stage.
- Endogenous predictors show some predictive power at shorter horizons (1–180 days), suggesting the macro-sentiment signal is complemented by other factors at higher frequencies.
- The paper's finding is an impulse-response analysis, not a strategy backtest; transaction costs, slippage, and implementation frictions are not incorporated into the macro-sentiment projection.

## Falsification plan

1. **Out-of-sample test:** Walk-forward replication on data after April 2025 (the paper's data cutoff). If FGI EMA24w loses significance at 181+ day horizons in the post-April 2025 period, the signal is weakened.
2. **Parameter perturbation:** Test EMA windows of 12, 18, and 30 weeks instead of 24. If the result is fragile to window choice, it suggests overfitting.
3. **Alternative sentiment sources:** Replicate using alternative sentiment indices (e.g., social media sentiment aggregates, funding rate proxies) to test whether the signal is specific to Alternative.me's FGI construction or generalizes.
4. **Transaction cost stress:** If implementing as a monthly/quarterly rebalance signal, test whether the 15–22pp effect survives realistic trading costs (10–15 bps per side, slippage on mid-cap tokens).
5. **Regime breakdown:** Test in isolation during 2022 (bear), 2023 (recovery), and 2024 (bull) separately to check for regime-dependence.
6. **Meme-coin ablation:** Test whether the DOGE-specific sensitivity is replicable across other meme coins or is idiosyncratic.
7. **Baseline comparison:** Compare against a simple buy-and-hold of BTC and a time-series momentum strategy over the same sample.

## Crypto portability

**Direct** — the paper is inherently a crypto study. The signal is derived from crypto-native data (Crypto Fear & Greed Index) applied to crypto assets.

**Crypto-specific considerations:**
- **Spot vs perpetual:** The paper uses spot OHLCV data. For perpetual futures, funding rates could amplify or dampen the sentiment effect—high funding during sentiment peaks could accelerate mean reversion.
- **24/7 session:** Weekly aggregation smooths across sessions; intraday timing is not addressed.
- **Venue fragmentation:** FGI is a cross-exchange aggregate; individual venue sentiment may differ.
- **Liquidity:** The 378-asset universe includes many illiquid tokens; a practical implementation would need a liquidity filter.
- **Survivorship:** The paper excludes tokens listed after 2024-01-01, introducing mild survivorship bias.

## Limitations

- **Not a strategy backtest:** The macro-sentiment finding is an impulse-response analysis, not a backtested trading strategy. No entry/exit rules, position sizing, or transaction cost accounting are provided for the timing signal.
- **Survivorship bias:** The universe excludes tokens listed after 2024-01-01 and removes assets with insufficient history, which may overstate forward returns for surviving tokens.
- **FGI construction opacity:** The Alternative.me Fear & Greed Index methodology is not fully transparent; the paper treats it as given.
- **Cross-basket heterogeneity:** The signal is not significant in all 8 baskets; XRP and ALL are excluded from the main analysis.
- **Sample period:** The Bayesian projection covers approximately 2019–2025, a period dominated by crypto bull markets and one major bear market (2022). Generalizability to prolonged sideways or bear regimes is uncertain.
- **DOGE concentration:** The strongest effect is concentrated in a single meme coin; whether this generalizes to other meme coins is untested.
- **Fractional differencing sensitivity:** The d=0.5 parameter is applied to series classified as random walk; sensitivity to this choice is not reported.
- **Inference framework:** Bayesian local projections with horseshoe priors involve researcher degrees of freedom in prior specification; the paper does not report sensitivity to prior hyperparameters.
- **Not independently reproduced.**

## Implementation status

**not-implemented.** No implementation in PyBroker, Nautilus, or any backtest framework has been completed. The signal is a research finding from an impulse-response analysis, not a deployable trading strategy.

## Adoption boundary

This record is **research-only**. It is not validated alpha, not approved for implementation, paper trading, testnet, or live trading. The macro-sentiment contrarian timing hypothesis requires substantial operationalization (threshold selection, sizing, rebalance rules, transaction cost modeling) before it could enter the validation pipeline.

## Related Wiki records

- [[crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01]] — uses Fear & Greed Index for cross-sectional risk beta pricing, a different mechanism (cross-sectional mispricing vs time-series contrarian timing).
- [[crypto-sentiment-extremity-bid-ask-spread-adverse-selection-2026-09-01]] — uses sentiment extremity for microstructure adverse selection, a different mechanism.

## Sources

- Zhang, W. and Watts, A. (2025). "HODL Strategy or Fantasy? 480 Million Crypto Market Simulations and the Macro-Sentiment Effect." arXiv:2512.02029v1. Submitted November 19, 2025.
- Alternative.me Crypto Fear & Greed Index: https://alternative.me/crypto/fear-and-greed-index/
