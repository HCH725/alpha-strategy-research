---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Investor Disagreement and Short-Sale Constraints (Abnormal Volume Premium)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - volume
  - turnover
  - investor-disagreement
  - short-sale-constraints
  - behavioral-finance
status: research-only
confidence: high
source_as_of: 2025-09
sources:
  - "Jon A. Garfinkel, Lawrence Hsiao, and Danqi Hu, 'Disagreement and returns: The case of cryptocurrencies', Financial Management 54(3), 633-672 (2025). DOI: 10.1111/fima.12491"
  - "Edward M. Miller, 'Risk, Uncertainty, and Divergence of Opinion', The Journal of Finance 32(4), 1151-1168 (1977). DOI: 10.1111/j.1540-6261.1977.tb03317.x"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Investor Disagreement and Short-Sale Constraints (Abnormal Volume Premium)

## Provenance

- **Primary Source:** Jon A. Garfinkel, Lawrence Hsiao, and Danqi Hu, "Disagreement and returns: The case of cryptocurrencies", *Financial Management*, Volume 54, Issue 3, Pages 633–672 (Fall 2025). DOI: [10.1111/fima.12491](https://doi.org/10.1111/fima.12491).
- **Theoretical Foundation:** Edward M. Miller, "Risk, Uncertainty, and Divergence of Opinion", *The Journal of Finance*, Volume 32, Issue 4, Pages 1151–1168 (September 1977). DOI: [10.1111/j.1540-6261.1977.tb03317.x](https://doi.org/10.1111/j.1540-6261.1977.tb03317.x).
- **Empirical Dataset:** Multi-year daily cross-section of cryptocurrencies across major spot exchanges, analyzing trading volume turnover, order flow imbalance, and the introduction of margin/shorting trading mechanisms.

## Economic mechanism

### Source-reported
Miller (1977) posits that in the presence of short-sale constraints and heterogeneous beliefs, an asset's market price reflects only the valuation of optimistic investors because pessimistic investors are precluded from expressing their views through short positions. Consequently, when investor disagreement is high, the market price is biased upward relative to the fundamental consensus valuation. As information is revealed over time and disagreement subsides, prices predictably revert downward.

Garfinkel, Hsiao, and Hu (2025) provide empirical evidence confirming Miller's model in cryptocurrency markets. Using abnormal trading volume (abnormal turnover) as a direct proxy for trading-based investor disagreement, they find that tokens experiencing high disagreement generate significantly lower future cross-sectional returns. Crucially, this negative return predictability is concentrated in tokens where short-sale constraints are binding (spot-only trading) and largely disappears once margin trading or perpetual shorting is activated for a given cryptocurrency.

### Research interpretation
The economic thesis is **behavioral overpricing under market friction and short-sale limits**:
1. **Disagreement as Volume Shocks:** When retail and speculative participants diverge sharply on a token's valuation (due to announcements, social media sentiment, or protocol events), trading volume surges abnormally as optimistic buyers trade against neutral or selling holders.
2. **Asymmetric Price Discovery:** In spot cryptocurrency markets lacking liquid borrow or shorting facilities, pessimistic participants can at most sell their existing holdings (reducing position to zero) but cannot establish short exposure. The marginal clearing price is thus set by the most optimistic cohort, causing short-term overvaluation.
3. **Subsequent Order Flow Exhaustion:** Following high-disagreement epochs, buying activity diminishes substantially faster than selling activity, leading to negative net order imbalance and predictable price mean-reversion over 1-to-5-day horizons.
4. **Friction-Conditioned Edge:** The alpha is strongest when conditioning on assets with high shorting frictions, making it an asymmetric anomaly that differentiates spot-only tokens from margin/derivative-enabled tokens.

## Signal

- **Eligible Universe:**
  - Cross-section of top 200 liquid cryptocurrencies with at least 60 days of continuous daily trading history and 30-day average daily dollar volume ($ADV_{30d} > \$1\text{M}$).
- **Daily Turnover Calculation:**
  $$Turnover_{i,t} = \frac{VolumeUSD_{i,t}}{MarketCap_{i,t}}$$
  *(Alternatively, for tokens without reliable circulating cap, use log dollar volume normalized by rolling volume).*
- **Baseline Expected Turnover ($TTMM_{i,t}$):**
  - 50-day rolling arithmetic mean of turnover:
    $$TTMM_{i,t} = \frac{1}{50} \sum_{k=1}^{50} Turnover_{i, t-k}$$
- **Abnormal Turnover / Investor Disagreement Proxy ($\Delta TTMM_{i,t}$):**
  $$\Delta TTMM_{i,t} = Turnover_{i,t} - TTMM_{i,t}$$
- **Short-Sale Constraint Indicator ($SSC_{i,t}$):**
  $$SSC_{i,t} = \begin{cases} 1 & \text{if token } i \text{ has NO active margin trading / perpetual futures on major venues} \\ 0 & \text{if token } i \text{ has active margin trading / perpetual futures shorting} \end{cases}$$
- **Composite Disagreement Signal:**
  $$Signal_{i,t} = -\Delta TTMM_{i,t} \times (1 + \gamma \cdot SSC_{i,t})$$
  where $\gamma \ge 0$ scales the penalty for tokens with binding short-sale constraints.
- **Portfolio Construction:**
  - Sort eligible universe cross-sectionally into deciles (or quintiles) by $\Delta TTMM_{i,t}$ at daily rebalancing timestamp $t = 00:00\text{ UTC}$.
  - **Long Leg ($D1$ / $Q1$):** Lowest abnormal turnover (lowest investor disagreement / quiet accumulation).
  - **Short Leg ($D10$ / $Q5$):** Highest abnormal turnover (highest investor disagreement / speculative overpricing).
  - For long-only implementations: Overweight Decile 1 and completely exclude or underweight Decile 10.
  - Rebalance: Daily at 00:00 UTC.

## Required data

- **Universe:** Cross-sectional crypto spot and perpetual markets.
- **Timeframe:** Daily OHLCV bars (00:00 UTC boundary).
- **Fields:** Open, High, Low, Close, Volume in base and USD quote currency, circulating market capitalization, margin/futures availability status.
- **Lookback:** Minimum 60 daily bars to establish 50-day baseline turnover $TTMM$.

## Execution assumptions

- **Execution Timing:** Daily rebalance at 00:00 UTC executed via 15-minute TWAP.
- **Order Types:** Limit orders placed near the bid/ask or TWAP market orders.
- **Transaction Costs:** 5–8 bps taker fee; 2–5 bps slippage.
- **Shorting Mechanism:** For tokens in $D10$ with available perpetual futures contracts, execute short via perpetuals; for spot-only tokens, apply long-only exclusion.

## Evidence

### Source-reported
- Garfinkel, Hsiao, and Hu (2025) report that abnormal turnover ($\Delta TTMM$) exhibits a statistically significant negative relationship with subsequent daily crypto returns ($t\text{-stat} < -2.50$) across comprehensive cross-sectional regressions.
- The return spread between low-disagreement and high-disagreement portfolios is economically large and statistically robust in assets subject to binding short-sale constraints.
- Following the launch of margin trading for specific cryptocurrencies, the negative return predictability of $\Delta TTMM$ weakens substantially, directly corroborating Miller's theoretical predictions.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- **Parabolic Momentum Overrun:** During intense market-wide speculative mania or sector-specific meme rotations, high abnormal volume can accompany multi-day parabolic trend continuation before mean-reverting, generating severe short-term drawdowns for short positions.
- **Turnover Drag:** Daily portfolio rebalancing across lower-cap altcoins can incur significant transaction costs if executed aggressively without cost-aware buffering.

## Falsification plan

1. **Fama-MacBeth Characteristic Orthogonality:** Regress forward 1-day and 7-day returns on $\Delta TTMM$ alongside 1-day reversal, 30-day momentum, Amihud illiquidity, and idiosyncratic volatility. If the coefficient on $\Delta TTMM$ loses significance ($|t| < 1.96$), reject the disagreement thesis as a redundant proxy for short-term reversal or illiquidity.
2. **Margin Activation Interaction Test:** Partition the cross-section into margin-enabled vs spot-only tokens. If the long-short spread on spot-only tokens is not significantly higher than on margin-enabled tokens ($p > 0.05$), reject the short-sale constraint mechanism.
3. **Net-of-Fee Simulation:** Test with 10 bps round-trip transaction costs. If net annualized Sharpe ratio drops below $0.50$, reject practical tradability.

## Crypto portability

**Direct**: The underlying empirical study was conducted natively on daily cryptocurrency exchange cross-sections, incorporating crypto-specific market microstructure, spot volume, and margin-trading rollout timelines.

## Limitations

- **not independently reproduced**: Internal reproduction in PyBroker and NautilusTrader pipelines is pending.
- **high portfolio turnover**: Daily decile rebalancing requires passive execution or trade-buffering overlays to prevent fee erosion.
- **asymmetric shorting availability**: Tokens with the strongest predicted overpricing (spot-only altcoins) cannot be directly shorted, restricting full long-short capture.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live trading infrastructure has been completed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]`
- `[[crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31]]`
- `[[crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]`

## Sources

1. Jon A. Garfinkel, Lawrence Hsiao, and Danqi Hu, "Disagreement and returns: The case of cryptocurrencies", *Financial Management*, Volume 54, Issue 3, Pages 633–672 (Fall 2025). DOI: [10.1111/fima.12491](https://doi.org/10.1111/fima.12491)
2. Edward M. Miller, "Risk, Uncertainty, and Divergence of Opinion", *The Journal of Finance*, Volume 32, Issue 4, Pages 1151–1168 (September 1977). DOI: [10.1111/j.1540-6261.1977.tb03317.x](https://doi.org/10.1111/j.1540-6261.1977.tb03317.x)
