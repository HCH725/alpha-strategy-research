---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Locked Supply and Staking Conviction Premium
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - on-chain
  - staking
  - locked-supply
  - conviction
status: research-only
confidence: medium
source_as_of: 2026
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7314420
  - https://doi.org/10.2139/ssrn.7314420
  - https://www.researchgate.net/publication/393437583_Skin_in_the_Chain_Locked_Supply_and_the_Cross-section_of_Cryptocurrency_Returns
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Locked Supply and Staking Conviction Premium

## Provenance

Primary source: Ainsley To, "Skin in the Chain: Locked Supply and the Cross-section of Cryptocurrency Returns," SSRN working paper, posted 2023 / updated 2026. SSRN Abstract ID: 7314420, DOI: https://doi.org/10.2139/ssrn.7314420. ResearchGate persistent URL: https://www.researchgate.net/publication/393437583_Skin_in_the_Chain_Locked_Supply_and_the_Cross-section_of_Cryptocurrency_Returns.

The paper introduces a directly observable on-chain metric of holder conviction, $\lambda$, defined as the fraction of circulating token supply voluntarily locked through staking, governance commitments, or dormancy. It analyzes the cross-sectional asset pricing implications of $\lambda$ within a quantity-theoretic framework, separating transactional medium-of-exchange value from store-of-value/governance conviction.

Exact sample period dates, point-in-time coin/token categorization taxonomy rules, and precise portfolio weighting conventions not fully detailed in the reviewed public abstract remain **underspecified**.

## Economic mechanism

### Source-reported

In digital asset valuation, models often lack a measurable counterpart to the unobservable subjective beliefs or platform confidence that they capitalize. The author introduces $\lambda$ as a direct on-chain proxy for holder conviction: the share of circulating supply voluntarily committed to long-term lockups (staking protocols, governance timelocks, or prolonged dormancy).

Embedded in a quantity-theoretic framework:
- For transactional Layer-1 "coins", $\lambda$ separates the store-of-value premium from the medium-of-exchange utility. Theory predicts conditional pricing: conviction forecasts forward returns only where valuation has not already absorbed it. Among "cheap" coins, high staking share signals authentic undervaluation; among "expensive" coins, high staking share reflects overextended speculative lock-in.
- For governance "tokens" (which lack transactional medium-of-exchange velocity), $\lambda$ directly reflects platform belief. Conviction is priced unconditionally through the extremes of its distribution, generating significant factor-adjusted abnormal returns unspanned by traditional factor models.

### Research interpretation

The falsifiable hypothesis is that **voluntary on-chain supply lockup ($\lambda$) is an informative cross-sectional state variable whose pricing dynamics differ fundamentally between transactional coins and governance tokens**:

1. **Coins (Conditional Double Sort)**: 
   For native Layer-1 network assets whose valuation reflects both transactional velocity and monetary premium, $\lambda$ must be conditioned on valuation multiples (e.g. MVRV, Market Cap to On-Chain Volume). When valuation is low (cheap), high $\lambda$ indicates committed long-term holders accumulating supply off the market, predicting positive excess returns. When valuation is high (expensive), high $\lambda$ indicates overextended crowding that precedes steep drawdowns.
2. **Tokens (Unconditional Single Sort)**: 
   For non-transactional DeFi/governance tokens, $\lambda$ acts as an unconditional quality/conviction factor. Tokens with extreme high staking/governance participation exhibit persistent outperformance over tokens with low holder commitment.

## Signal

Normalized source-faithful signal framework:

1. **Asset Classification**: At each monthly formation date $t$, partition the active cryptocurrency universe into:
   - Category A: Transactional Layer-1 / Layer-0 native coins (e.g. BTC, ETH, SOL, ADA).
   - Category B: Governance, DeFi, and application tokens (e.g. UNI, AAVE, MKR, LDO).
2. **Compute Conviction Metric ($\lambda$)**:
   $$\lambda_{i,t} = \frac{\text{Voluntarily Locked Supply}_{i,t} + \text{Staked Supply}_{i,t}}{\text{Circulating Supply}_{i,t}}$$
3. **Coin Portfolio (Conditional Strategy)**:
   - Measure valuation status $V_{i,t}$ (e.g., market cap relative to on-chain fundamental baseline or realized value).
   - Split coins into Valuation groups (e.g. "Cheap" vs "Expensive").
   - Within "Cheap" coins, go long high-$\lambda$ assets.
   - Within "Expensive" coins, go short high-$\lambda$ assets (or long low-$\lambda$ assets).
4. **Token Portfolio (Unconditional Strategy)**:
   - Rank tokens directly by $\lambda_{i,t}$.
   - Long the top extreme quantile (highest locked supply share) and short the bottom extreme quantile (lowest locked supply share).
5. **Holding & Rebalancing**: Monthly rebalancing frequency.

Exact valuation metric thresholds, precise coin-versus-token automated classification rules, and exact quantile cutoffs (quintiles vs deciles) are **underspecified** in public summaries and must not be invented.

## Required data

- On-chain circulating supply, total supply, staked supply (PoS validator stakes, smart contract staking deposits), and governance-locked supply.
- Point-in-time cryptocurrency asset master and taxonomy (Layer-1 coin vs smart contract token).
- Historical daily/monthly prices, volumes, and market capitalizations.
- On-chain transaction volume and realized capitalization for valuation conditioning.
- Unbonding period rules and staking contract metadata per protocol.

## Execution assumptions

- Monthly rebalance frequency executed at transparent timestamp boundaries.
- Long legs executed in spot or perpetual futures.
- Short legs executed via perpetual futures contracts or spot margin borrow where available.
- Explicit modeling of:
  - Staking unbonding periods (unstaking delays ranging from days to weeks if physical staking is involved).
  - Protocol inflation/emission rates (token dilution via staking yield).
  - Borrow availability and borrow fee rates for shorting smaller tokens.
  - Bid-ask spread and turnover drag on monthly rebalancing.

## Evidence

### Source-reported

- **Coins (Conditional Pricing)**: A one-standard-deviation increase in staking share ($\lambda$) earns:
  - **+0.7% per month** among "cheap" coins.
  - **-3.0% per month** among "expensive" coins.
  - The conviction-valuation interaction survives a joint horse race against every measurable valuation model and technical signal tested in the paper, none of which predicted coin returns on its own.
- **Tokens (Unconditional Pricing)**:
  - Conviction is priced unconditionally across distribution extremes.
  - Generates a **1.7% monthly factor-adjusted alpha** unspanned by competitor factor portfolios.

All numerical figures above are **source-reported** by Ainsley To (SSRN 7314420) and have not been independently verified.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed primary source.

Absence of reported negative evidence is not evidence of absence. Potential real-world failure modes include:
- Staking lockups can create severe unbonding liquidity traps during broad market crashes.
- High reported staking ratios in inflationary tokens can be artificial artifacts of high staking yield emissions rather than genuine organic holder conviction.
- Shorting high-$\lambda$ expensive coins or low-$\lambda$ tokens in spot markets may suffer from prohibitive borrow costs or lack of borrow availability.

## Falsification plan

The hypothesis should be weakened or rejected if an independent point-in-time backtest demonstrates:

1. The interaction between $\lambda$ and valuation for Layer-1 coins fails to generate statistically significant return spread ($t < 2.0$) out-of-sample (e.g. post-2023).
2. The 1.7% monthly factor-adjusted alpha in governance tokens is entirely explained by market beta, size, or momentum factors.
3. Controlling for token emission/inflation rates eliminates the predictive power of $\lambda$.
4. Execution costs, token borrow fees, and unbonding illiquidity eliminate net profitability.
5. The result is unstable to reasonable alternative definitions of locked supply or valuation metrics.

## Crypto portability

**Direct**, as the mechanism is built natively on crypto on-chain staking, governance lockups, and tokenomic structures.

Key operational considerations:
- Staking mechanisms differ structurally across chains (e.g. delegated proof-of-stake vs liquid staking vs lock-drop contracts).
- Liquid staking tokens (e.g. stETH, mSOL) alter the effective economic lockup of staked supply.
- Token unlock cliffs and vesting schedules must be distinguished from voluntary holder lockups.

## Limitations

- **Not independently reproduced.**
- **Working-paper status:** SSRN working paper (SSRN 7314420).
- **underspecified:** Exact quantitative valuation multiple formula, coin/token classification boundaries, and portfolio weighting schemes are not fully specified in the public abstract.
- **implementation gap:** Staking lockup constraints may prevent agile portfolio rebalancing if physical staking yields are harvested.
- **borrow risk:** Shorting low-conviction tokens is constrained by borrow availability on centralized and decentralized lending markets.

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was queried, created, or modified in this Scout cycle.

Related Alpha Strategy Pool artifacts:
- `bitcoin-onchain-reserve-risk-hodl-conviction-2026-08-31.md` — Bitcoin on-chain HODL conviction and reserve risk.
- `bitcoin-onchain-entity-adjusted-dormancy-flow-macro-bottom-2026-09-01.md` — on-chain dormancy flow and spending patterns.
- `crypto-cross-sectional-onchain-user-activity-growth-2026-08-31.md` — cross-sectional on-chain activity growth.

## Sources

1. Ainsley To, “Skin in the Chain: Locked Supply and the Cross-section of Cryptocurrency Returns,” SSRN working paper, 2023 / 2026. SSRN Abstract: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7314420
2. DOI / SSRN persistent identifier: https://doi.org/10.2139/ssrn.7314420
3. ResearchGate publication entry: https://www.researchgate.net/publication/393437583_Skin_in_the_Chain_Locked_Supply_and_the_Cross-section_of_Cryptocurrency_Returns
