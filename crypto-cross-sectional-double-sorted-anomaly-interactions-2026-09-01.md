---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Double-Sorted Anomaly Interactions
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - anomaly-interactions
  - double-sorted-portfolios
  - liquidity-frictions
  - risk-premia
status: research-only
confidence: high
source_as_of: 2025-01
sources:
  - https://doi.org/10.1016/j.irfa.2024.103756
  - https://ideas.repec.org/a/eee/finana/v97y2025ics1057521924004944.html
  - https://aleksandermercik.pl
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Double-Sorted Anomaly Interactions

## Provenance

- **Primary Academic Source:** Aleksander Mercik, Barbara Będowska-Sójka, Sitara Karim, and Adam Zaremba, “Cross-sectional interactions in cryptocurrency returns,” *International Review of Financial Analysis*, Volume 97, January 2025, article 103756. DOI: [10.1016/j.irfa.2024.103756](https://doi.org/10.1016/j.irfa.2024.103756).
- **Bibliographic Reference:** RePEc/IDEAS stable record: https://ideas.repec.org/a/eee/finana/v97y2025ics1057521924004944.html.
- **Empirical Dataset:** Comprehensive panel of over 500 major cryptocurrencies and tokens spanning 2017 through 2023, evaluating pairwise interactions across 40 distinct cross-sectional characteristics.

## Economic mechanism

### Source-reported

In empirical asset pricing, market anomalies are frequently evaluated in isolation using univariate portfolio sorts. Mercik, Będowska-Sójka, Karim, and Zaremba (2025) investigate whether cross-sectional characteristics in the cryptocurrency market interact in non-linear ways.

The authors document that:
1. Significant interaction effects exist across cryptocurrency characteristics, with individual signals reinforcing each other to generate return spreads substantially larger than univariate baselines.
2. The most powerful interactions occur at the intersection of **liquidity, risk, and past return (momentum/reversal)** measures.
3. Network graph analysis indicates that liquidity serves as a central hub: low liquidity increases trading frictions and prevents arbitrage capital from eliminating mispricing, thereby amplifying and preserving anomalies in risk and momentum dimensions.

### Research interpretation

The strategy is a **frictional multi-factor confluence / limits-to-arbitrage alpha**:
1. **Conditional Mispricing Amplification:** In highly liquid mega-cap cryptocurrencies, market makers and institutional quantitative funds rapidly arbitrage away simple single-factor anomalies. In less liquid segments, high bid-ask spreads, shallow book depth, and shorting constraints prevent arbitrageurs from closing valuation gaps.
2. **Signal Confluence & Noise Reduction:** Univariate factor sorts suffer from false positives due to token-specific structural quirks. Double-sorting (e.g., conditioning momentum or idiosyncratic volatility on illiquidity terciles) isolates tokens where behavioral biases (retail trend chasing, lottery preferences) meet structural arbitrage constraints.
3. **Adaptive Interaction Allocation:** Constructing an out-of-sample meta-strategy that selects top-performing bivariate interaction pairs captures shifting market regimes more effectively than static single-factor portfolios.

## Signal

The quantitative portfolio construction follows a standardized bivariate sorting framework:

1. **Characteristic Universe (40 Metrics):**
   Compute 40 normalized characteristics across five thematic clusters for each eligible token $i$ at formation date $t$:
   - **Liquidity & Trading Activity:** Amihud illiquidity ratio, turnover rate, volume volatility, dollar volume, bid-ask spread proxies.
   - **Risk & Tail Risk:** Total volatility, idiosyncratic volatility ($\text{IVOL}$), downside beta ($\beta^-$), value-at-risk ($\text{VaR}$), coskewness, realized kurtosis.
   - **Past Returns & Momentum:** 1-day reversal, 1-week reversal, 1-month momentum, 3-month momentum, distance to 52-week high.
   - **Blockchain & Network Activity:** Active address growth, transaction count, NVT ratio, on-chain velocity.
   - **Investor Attention:** Abnormal trading volume, search volume index.

2. **Bivariate Double-Sorting:**
   - At weekly/monthly formation date $t$, sort the cross-section into $3 \times 3$ or $5 \times 5$ portfolios based on pairs of characteristics $(X_1, X_2)$ (using independent or conditional sequential sorts).
   - Evaluate the return spread of the long-short interaction portfolio:
     $$\Delta R_{(X_1, X_2), t} = R_{(X_{1,\text{high}}, X_{2,\text{high}}), t} - R_{(X_{1,\text{low}}, X_{2,\text{low}}), t}$$

3. **Out-of-Sample Interaction Strategy:**
   - Select the top-performing bivariate interaction pairs identified during the expanding historical estimation window (dominated by **high momentum $\times$ low liquidity** and **low downside risk $\times$ high volume disagreement**).
   - Go long the top-ranked interaction corner portfolio (equal-weighted or market-cap-weighted).
   - Go short (or underweight) the bottom-ranked interaction corner portfolio.
   - Rebalance at weekly or monthly frequency ($K = 1\text{w}$ or $1\text{m}$).

## Required data

- **Universe:** 500+ cryptocurrencies with active spot or perpetual trading history.
- **Granularity:** Daily OHLCV, circulating market capitalization, and volume.
- **Derived Metrics:** Point-in-time rolling calculations of all 40 characteristic values for all universe constituents.
- **Data Integrity:** Strict survivorship-bias-free historical universe including delisted coins, coin migration records, and synchronized UTC close boundaries.

## Execution assumptions

- **Rebalancing Frequency:** Weekly or monthly ($K = 1\text{w}$ / $K = 1\text{m}$).
- **Execution Timing:** Next-period open prices following close-of-bar characteristic calculations.
- **Trading Frictions:** The source study reports gross out-of-sample performance. Live execution assumptions must incorporate:
  - Taker exchange fees: 5 to 10 bps per trade across constituent tokens.
  - Bid-ask spread and market impact: 10 to 50 bps in the lower-liquidity terciles.
- **Shorting Feasibility:** Short legs of double-sorted portfolios often require borrowing small/mid-cap altcoins or trading perpetual contracts. Where borrow/perpetuals are unavailable, a long-only tilt benchmark must be evaluated.

## Evidence

### Source-reported

- **Out-of-Sample Risk-Adjusted Return:** The out-of-sample long-short trading strategy selecting top and bottom interaction portfolios achieves an annualized **Sharpe ratio exceeding 1.0** over the 2017–2023 sample period.
- **Dominant Interaction Clusters:** The strongest, most robust interaction effects are concentrated in the interplay of **liquidity, risk, and past return measures**.
- **Arbitrage Friction Hub:** Network graph centrality analysis confirms that liquidity measures form the central node mediating interaction strength across the entire cryptocurrency characteristic network.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Friction-Premium Paradox:** The very source of the anomaly spread (illiquidity and high trading costs preventing arbitrage) imposes severe execution costs on live implementation. In the lowest-liquidity corner portfolios, round-trip trading frictions and price impact can consume 40–70% of gross return spreads.
- **Turnover Drag:** High rebalancing turnover across double-sorted micro-cap portfolios necessitates aggressive turnover reduction filters (e.g., buffering breakpoints or rebalancing frequency optimization).
- **Perpetual Universe Constraint:** Restricting the universe strictly to tokens with liquid perpetual futures contracts reduces the universe from 500+ tokens to ~150 tokens, dampening the dispersion of illiquidity-based interaction spreads.

## Falsification plan

The hypothesis should be considered rejected or materially weakened if:
1. Applying realistic fee and slippage models (10 bps fee + 20 bps slippage on illiquid legs) reduces the out-of-sample net annualized Sharpe ratio below $0.5$.
2. Restricting the underlying universe to top-100 perpetual futures contracts reduces the double-sorted interaction spread to statistical insignificance ($t < 1.96$).
3. Multi-factor spanning regressions against standard crypto factor models (Market + Size + Momentum + Liquidity) fully absorb the interaction portfolio alpha, demonstrating that interaction effects are redundant.
4. Out-of-sample testing on 2024–2026 data shows structural decay in the liquidity-momentum interaction spread.

## Crypto portability

- **Direct:** The empirical methodology and evidence are natively established on a large cryptocurrency cross-section (500+ coins, 2017–2023).
- **Spot vs. Perpetual Nuance:** Direct spot long portfolios are fully portable; short-leg execution is unproven on unlisted micro-caps and requires perpetual futures adaptation for executable market neutrality.

## Limitations

- **Not independently reproduced.**
- **High Friction Sensitivity:** Gross Sharpe > 1.0 requires sophisticated execution and turnover management to survive in production.
- **Combinatorial Multiple Testing Risk:** Evaluating pairwise interactions across 40 characteristics creates a large hypothesis space; while the paper mitigates this via out-of-sample selection, live researchers must guard against overfitting.
- **Data Gap:** Empirical dataset terminates in 2023; post-2023 institutional ETF regime requires fresh validation.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute approval for live capital allocation, paper trading, or testnet deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md` — single-factor daily reversal conditioned on liquidity.
- `crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31.md` — univariate Amihud illiquidity pricing.
- `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md` — meta-factor momentum across anomaly portfolios.
- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` — cross-sectional price momentum.

## Sources

1. Aleksander Mercik, Barbara Będowska-Sójka, Sitara Karim, and Adam Zaremba, “Cross-sectional interactions in cryptocurrency returns,” *International Review of Financial Analysis*, Volume 97, January 2025, article 103756. DOI: [10.1016/j.irfa.2024.103756](https://doi.org/10.1016/j.irfa.2024.103756).
2. RePEc / IDEAS bibliographic archive: https://ideas.repec.org/a/eee/finana/v97y2025ics1057521924004944.html.
3. Author working paper and research repository: https://aleksandermercik.pl.
