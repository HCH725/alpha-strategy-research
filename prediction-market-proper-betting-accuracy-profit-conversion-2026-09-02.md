---
schema: strategy-research-record-v1
title: "Proper Betting: Converting Forecasting Accuracy into Profit in CLOB Prediction Markets"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - scoring-rules
  - bregman-divergence
  - clob
  - kalshi
  - polymarket
  - accuracy-to-profit
status: research-only
confidence: high
source_as_of: 2026-07-11
sources:
  - "Anri Gu, Nicole Kagan, Alec Sun, Jibang Wu, and Haifeng Xu, 'When do prophets profit in prediction markets?', arXiv:2607.06166v2 [cs.AI], July 11, 2026. https://arxiv.org/abs/2607.06166"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Proper Betting: Converting Forecasting Accuracy into Profit in CLOB Prediction Markets

## Provenance

- **Source**: arXiv:2607.06166v2, submitted July 7, 2026 (v1); revised July 11, 2026 (v2).
- **Authors**: Anri Gu (University of Chicago), Nicole Kagan (Kalshi Research), Alec Sun (University of Chicago), Jibang Wu (New York University, Shanghai), Haifeng Xu (University of Chicago).
- **Type**: Peer-reviewed preprint; accepted at no known venue at time of capture.
- **As-of date**: July 11, 2026 (v2). Live deployment results reported for a one-month period on Kalshi.

## Economic mechanism

### Source-reported

The authors establish that in central limit order book (CLOB) prediction markets, the classical equivalence between forecasting accuracy and trading profit (which holds under AMM market scoring rules) breaks down. Informed forecasters routinely lose money on CLOBs despite having superior predictions, while uninformed strategies can profit on simple heuristics.

The paper proves that for any strictly proper scoring rule S, there exists a "proper betting" strategy that converts an accuracy edge over the market into positive expected profit, provided the market has sufficient liquidity. The expected profit decomposes into three explicit terms: (1) score gap (the accuracy advantage), (2) Bregman divergence (which can generate profit even without accuracy advantage), and (3) liquidity loss (the cost of price impact). The authors further prove that proper betting is essentially the only strategy that robustly guarantees profitability on any sufficiently liquid market.

### Research interpretation

The core mechanism is a scoring-rule-indexed betting strategy: given a forecaster's probability vector p and the market price vector q, the strategy places bets whose size is determined by the gradient of the convex conjugate of the scoring rule's generating function evaluated at the gap between p and q. This generalizes the AMM guarantee (where moving the price exactly to p yields profit equal to the score gap) to arbitrary CLOB price-impact functions.

The Bregman divergence term is the most theoretically novel component: it implies that a forecaster can profit even when p = q (no accuracy edge), simply by exploiting the convex geometry of the scoring rule relative to the market's price-impact function. This is a structural alpha source distinct from information advantage.

## Signal

- **Formation timestamp**: The signal is formed whenever a forecaster has a probability estimate p and a market price q for the same event. On Kalshi, this is continuously available during trading hours (24/7 for most contracts).
- **Lookback**: No historical lookback required for the core strategy; the strategy depends only on the current (p, q) pair and the chosen scoring rule.
- **Entry**: For a K-outcome event with forecaster belief p and market price q, the position vector s is computed as: s = ∇G*(p) - ∇G*(q), where G* is the convex conjugate of the scoring rule's generating function G. For the Brier score (quadratic), this simplifies to s_k ∝ (p_k - q_k). For the logarithmic score, s_k ∝ log(p_k / q_k). The direction is: buy outcome k when p_k > q_k, sell when p_k < q_k.
- **Exit**: Positions are held until contract resolution (binary settlement). The paper also discusses a long-horizon extension where the forecaster can trade at multiple time points as both p and q evolve.
- **Holding period**: Until contract resolution. In the long-horizon extension, positions can be updated as forecasts and market prices evolve.
- **Parameters**: The choice of scoring rule S (Brier, logarithmic, spherical, etc.) determines the exact betting formula. The paper identifies "forecasting personas" — systematic patterns in how different AI models deviate from the market — and shows the optimal scoring rule varies across personas. **Research-proposed**: The Brier-score variant is the simplest starting point; the logarithmic-score variant may be more appropriate for events with extreme probabilities.
- **Position sizing**: The strategy is fully specified by the scoring rule and the (p, q) pair. No additional sizing parameter is needed beyond the scoring rule choice. The paper proves that any robustly profitable strategy is essentially equivalent to proper betting up to proportionally rescaling bets and constant shifting.

## Required data

- **Instrument**: Binary prediction market contracts (e.g., Kalshi, Polymarket).
- **Venue**: Kalshi (primary empirical venue); Polymarket (CLOB-based, structurally compatible).
- **Market type**: Binary event contracts with CLOB price formation.
- **Timeframe**: Continuous; the strategy can be evaluated at any point during the contract's trading life.
- **Fields**: Market price q (bid/ask midpoint or last trade); forecaster probability estimate p; contract expiration; contract outcome (for evaluation).
- **Point-in-time**: The forecaster's probability p must be computed before or simultaneously with the bet; no look-ahead. The market price q is observed in real time.
- **Timestamp**: Not critical for the core strategy, but important for the long-horizon extension.
- **Missing-data**: The forecaster must produce a calibrated probability for each outcome. If the forecaster cannot produce p, the strategy cannot be deployed.
- **Funding/fee/spread needs**: The paper's theoretical results hold for any sufficiently liquid market. In practice, bid-ask spreads and platform fees reduce the effective score gap. Kalshi charges fees that vary by contract. The paper's live deployment results are net of fees.

## Execution assumptions

- **Signal-to-order timing**: The bet is placed immediately after computing the position vector s from (p, q).
- **Order type**: Market orders (to ensure execution) or limit orders at the scoring-rule-determined price. The paper does not specify order type in detail.
- **Fill model**: Assumed sufficient liquidity at the observed price. The paper's liquidity condition requires that the market can absorb the bet without moving the price beyond the forecaster's belief.
- **Fees**: Kalshi fees are included in the live deployment results. The theoretical framework accounts for fees as part of the liquidity loss term.
- **Slippage**: The Bregman divergence term in the profit decomposition accounts for price impact. The paper proves profitability holds under any price-impact function satisfying mild conditions.
- **Leverage**: Not specified; the live deployment used real capital without reported leverage.
- **Partial fills / failures**: Not discussed in detail; the paper assumes sufficient liquidity.

## Evidence

### Source-reported

- The paper reports a month-long live deployment on Kalshi achieving +80.33% ROI with a Sharpe ratio of 3.35. This used real capital with an AI forecasting agent.
- Across thousands of AI-generated forecasts, proper betting is the only strategy that reliably converts accuracy into profit. Standard heuristics (Kelly criterion, max-margin betting) fail even with good forecasts.
- The paper identifies systematic "forecasting personas" across AI models, with different personas favoring different proper betting strategies.
- Example case: A Dallas precipitation contract where the model identified an internal inconsistency in the order book (P(>3) > P(>2), violating monotonicity) and profited by buying NO at $0.05, staking $0.038 and paying out $0.76 (+1900% return on that contract).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that the live deployment was one month on a single platform (Kalshi). The results may not generalize to other platforms, market conditions, or time periods.
- The paper notes that even proper betting can fail when the market has insufficient liquidity (the liquidity loss term dominates).
- The forecasting persona analysis shows that not all AI models produce forecasts that can be profitably converted; the strategy requires the forecaster to have a genuine accuracy edge.

## Falsification plan

1. **Out-of-sample testing**: Deploy proper betting on Kalshi or Polymarket across diverse event categories (politics, weather, economics, sports) over a 3+ month period. **Failure threshold**: ROI < 0% after fees over the full sample, or Sharpe < 1.0.
2. **Baseline comparison**: Compare proper betting against (a) uniform random betting, (b) Kelly criterion with estimated probabilities, (c) max-margin betting, (d) simple heuristic strategies. **Failure condition**: Proper betting does not statistically outperform at least one baseline (one-sided permutation test, p < 0.05).
3. **Forecaster ablation**: Deploy proper betting with forecasts from models of varying quality. **Failure condition**: Profitability does not correlate with forecast accuracy (Spearman ρ between model accuracy and strategy ROI is not significantly positive).
4. **Fee sensitivity**: Re-run analysis with varying fee assumptions (0%, 5%, 10%, 20% of notional). **Failure condition**: Strategy becomes unprofitable at fees ≤ 5% of notional.
5. **Liquidity stress**: Test strategy performance during low-liquidity periods (early contract life, niche events). **Failure condition**: Strategy is unprofitable specifically in low-liquidity regimes.
6. **Parameter perturbation**: Vary the scoring rule (Brier vs. logarithmic vs. spherical) and measure sensitivity. **Failure condition**: Performance is highly sensitive to scoring rule choice (coefficient of variation > 50%).

## Crypto portability

- **Direct**: The strategy is designed for CLOB prediction markets. Polymarket is a CLOB-based prediction market on Polygon (crypto-native), making it directly portable. Kalshi is a regulated US exchange (not crypto-native) but uses similar CLOB mechanics.
- **Adaptation notes**: Polymarket uses USDC for settlement, adding stablecoin-related considerations (deposit/withdrawal, gas fees). The 24/7 nature of Polymarket aligns with the continuous trading assumption. Market depth and liquidity on Polymarket may differ from Kalshi.
- **Crypto-specific risks**: Polymarket's liquidity is thinner for many contracts; bid-ask spreads may be wider. Smart contract risk exists on Polymarket (Polygon). Oracle resolution risk differs from Kalshi's centralized resolution.
- **Not applicable to**: AMM-based prediction markets (e.g., Azuro, Overtime) where the classical AMM guarantee already holds; the proper betting framework is specifically designed for CLOB markets.

## Limitations

- **Single-month live result**: The +80.33% ROI / 3.35 Sharpe is from a single month on Kalshi. This is a small sample and may reflect favorable conditions rather than persistent edge.
- **Not independently reproduced**: No third-party replication of the live deployment results.
- **Forecaster dependency**: The strategy's profitability depends entirely on the forecaster's accuracy edge. Without a superior forecaster, the strategy has no edge. The paper does not provide a standalone alpha signal.
- **Kalshi-specific fees**: The live results include Kalshi's fee structure, which may differ from other platforms.
- **Binary settlement only**: The framework is developed for binary (K-outcome) prediction markets. Extension to continuous-outcome or multi-period derivatives is not covered.
- **Liquidity assumption**: The theoretical results require "sufficient liquidity." In practice, many prediction market contracts are thinly traded.
- **Data gap**: The paper does not release the full dataset of AI forecasts or the exact deployment parameters.

## Implementation status

No implementation in our research stack. The strategy requires (1) a forecasting model that produces calibrated probability estimates p for prediction market events, and (2) access to a CLOB prediction market (Kalshi or Polymarket).

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- [[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]] (complementary: market-making side vs. this record's taker/forecaster side)
- [[quant/prediction-market-structural-volatility-wright-fisher-glosten-milgrom-2026-09-02]] (complementary: volatility forecasting for prediction markets)
- [[quant/crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01]] (related: informed trading detection in prediction markets)
- [[quant/crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01]] (related: different alpha source in same venue type)

## Sources

- Anri Gu, Nicole Kagan, Alec Sun, Jibang Wu, and Haifeng Xu. "When do prophets profit in prediction markets?" arXiv:2607.06166v2 [cs.AI], July 11, 2026. https://arxiv.org/abs/2607.06166
