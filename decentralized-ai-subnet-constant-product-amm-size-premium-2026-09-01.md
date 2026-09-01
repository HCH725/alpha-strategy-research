---
schema: strategy-research-record-v1
title: Decentralized AI Subnet Constant-Product AMM Size Premium (Bittensor dTAO)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - amm
  - bittensor
  - size-factor
  - factor-pricing
  - capacity-constrained
status: research-only
confidence: high
source_as_of: 2026-03-31
sources:
  - "Philip Z. Maymin, 'Common Risk Factors in Decentralized AI Subnets', arXiv:2603.29751 [q-fin.PM], March 31, 2026. DOI: https://doi.org/10.48550/arXiv.2603.29751"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Decentralized AI Subnet Constant-Product AMM Size Premium (Bittensor dTAO)

## Provenance

- **Paper:** Philip Z. Maymin, "Common Risk Factors in Decentralized AI Subnets." arXiv:2603.29751v1 [q-fin.PM / q-fin.PR], March 31, 2026.
- **DOI:** https://doi.org/10.48550/arXiv.2603.29751
- **Author:** Philip Z. Maymin, Dolan School of Business, Fairfield University (pmaymin@fairfield.edu).
- **Author disclosure:** Co-owner of Djinn, a project operating on the Bittensor network.
- **Sample:** 406 daily observations from February 14, 2025, through March 26, 2026, covering 128 unique decentralized AI subnets.
- **Data source:** Blockchain pool state and metadata recorded daily from the Taostats API (https://api.taostats.io), supplemented with TAO/USD exchange aggregated prices.
- **Source URL:** https://arxiv.org/abs/2603.29751 (HTML version: https://arxiv.org/html/2603.29751v1)

## Economic mechanism

### Source-reported

Under the Dynamic TAO (dTAO) protocol deployed on February 13, 2025, each of Bittensor's 128 specialized AI subnetworks issues an "alpha token" ($\alpha_i$) priced against the base cryptocurrency TAO ($\tau_i$) via an on-chain constant-product automated market maker ($p_i = \tau_i / \alpha_i$ with invariant $\tau_i \cdot \alpha_i = k$). The protocol continuously injects seigniorage token emissions ($\Delta \tau_i$) into active subnets.

The paper derives a fundamental mathematical relationship (Proposition 1):
In a constant-product AMM, the percentage price change induced by an emission inflow $\Delta \tau_i$ is analytically inversely proportional to pool reserves ($\tau_i$):
$$\frac{\Delta p_i}{p_i} \approx \frac{\Delta \tau_i}{\tau_i}$$

Because small-capitalization subnets mechanically have small TAO reserves $\tau_i$, fixed or price-proportional token emissions generate systematically higher percentage price impacts on small subnets than on large subnets. Consequently, the cross-sectional size premium (Small-Minus-Big) in decentralized AI subnets is not merely an empirical statistical regular pattern, but a structural mathematical property of constant-product AMM mechanics.

### Research interpretation

The alpha hypothesis is a **mechanically generated cross-sectional size factor in protocol-native AMM pools**:
1. **AMM Price Impact Amplification:** Constant-product AMM curvature dictates that price impact is convex in trade size relative to pool depth. When protocol emissions or reinvested validator/miner staking rewards flow across subnets, the percentage price increase is inversely proportional to pool capitalization.
2. **Structural Emission Halving Sensitivity:** Because the size premium is mechanically driven by emission intensity, an exogenous reduction in block rewards (such as the December 14, 2025 halving from 1 TAO to 0.5 TAO per block) should reduce the equilibrium size premium proportionally.
3. **Liquidity Niche & Capacity Barrier:** The constant-product AMM imposes exact deterministic slippage $\text{Slippage} = \Delta \tau / \tau$ (Proposition 2). The median reserve of small-tercile subnets is only 540 TAO (~$186K USD at $345/TAO). Institutional or systematic arbitrage capital cannot eliminate the size premium because transaction slippage scales linearly with capital and overwhelms gross returns for assets under management (AUM) exceeding $10K USD.
4. **Positive Risk-Return Inversion:** Unlike traditional equities where the low-volatility anomaly and betting-against-beta puzzle prevail, decentralized AI subnets exhibit a strongly positive risk-return relation (high volatility and high beta outperform low volatility and low beta) because size and volatility are mechanically coupled by AMM depth.

## Signal

Normalized cross-sectional factor sorting rule:

1. **Universe:** All active Bittensor subnets excluding Subnet 0 (root network with fixed price 1 TAO) and subnets in bootstrapping startup mode (AMM inactive). Requires a minimum 7-day post-launch history to prevent initial liquidity pool bootstrapping distortion. Daily eligible cross-section expands from 63 to 124 subnets over the sample.
2. **Formation Timestamp:** Daily close at 00:00 UTC using lagged characteristics at day $t-1$.
3. **Primary Factor (Size - SMB):**
   - Compute lagged market capitalization in TAO terms: $\text{MCAP}_{i,t-1} = p_{i,t-1} \cdot A_{i,t-1}^{\text{total}}$, where $A_i^{\text{total}}$ is total circulating alpha tokens (pooled plus staked).
   - Sort eligible subnets into daily terciles: Small (bottom tercile), Medium (middle tercile), Large (top tercile). Average tercile size is ~36 subnets (minimum 21).
   - Long Small tercile (equal-weighted), Short Large tercile (equal-weighted).
4. **Secondary Factors:**
   - **Momentum (WML30 & WML7):** Sort on 30-day past return $\text{MOM30}_{i,t-1} = p_{i,t-1}/p_{i,t-31}-1$ or 7-day past return $\text{MOM7}_{i,t-1} = p_{i,t-1}/p_{i,t-8}-1$. Long top tercile (Winners), Short bottom tercile (Losers). Spanning gaps during subnet recycling/deregistration must be explicitly masked.
   - **Emission Yield ($\text{HML}_{\text{EMIS}}$):** Sort on daily emission yield $\text{EY}_{i,t-1} = E_{i,t-1} / \text{MCAP}_{i,t-1}$. Long high emission yield, Short low emission yield.
   - **1-Day Reversal (REV):** Sort on 1-day past return $\text{REV}_{i,t-1} = p_{i,t-1}/p_{i,t-2}-1$. Long past losers, Short past winners.
   - **Liquidity (LIQ):** Sort on AMM pool TAO reserves $\tau_{i,t-1}$. Long illiquid (low reserves), Short liquid (high reserves). Correlation with SMB is 0.93.
5. **Rebalancing Frequency:** Daily rebalancing.

## Required data

- **Universe:** 128 Bittensor subnet alpha tokens ($S_1, S_2, \dots, S_{128}$).
- **Data Source:** Taostats on-chain blockchain API (`api.taostats.io`).
- **Fields Required:**
  - Alpha token price in TAO ($p_{i,t} = \tau_{i,t}/\alpha_{i,t}$)
  - Pool TAO reserves ($\tau_{i,t}$) and alpha reserves ($\alpha_{i,t}$)
  - Total circulating alpha token supply ($A_{i,t}^{\text{total}}$) and staked alpha tokens ($\text{STAKE}_{i,t}$)
  - Daily subnet emission allocation ($E_{i,t}$ in rao, where $10^9\text{ rao} = 1\text{ TAO}$)
  - Active miner/validator count and registration/startup status flags
  - Spot TAO/USD exchange aggregated reference price
- **Timestamp:** Point-in-time daily snapshots at 00:00 UTC.
- **Missing Data / Lifecycle Rule:** Subnet recycling (deregistered slot re-assigned to a new project) must be identified via startup mode status; returns across recycled project lifecycles must be set to NaN, and momentum lookback windows spanning deregistration gaps must be masked.

## Execution assumptions

- **Execution Venue:** On-chain Bittensor Subtensor blockchain AMM extrinsics (`swap`, `stake`, `unstake`).
- **Denomination:** Base returns are denominated in TAO; USD returns require compounding with TAO/USD spot return: $r_{i,t}^{\text{USD}} = (1 + r_{i,t}^{\text{TAO}})(1 + r_t^{\text{TAO/USD}}) - 1$.
- **Slippage Model (Deterministic):** For trade size $\Delta \tau$, exact one-way AMM price impact is:
  $$\text{Slippage} = \frac{\Delta \tau}{\tau}$$
- **Capital Capacity Ceiling:**
  - $10K USD total AUM: One-way slippage ~0.64% per trade; net SMB return is 0.36%/day (annualized Sharpe 1.36).
  - $100K USD total AUM: One-way slippage ~6.4% per trade; slippage exceeds 100% of gross return, making the strategy unprofitable.
  - $1M USD total AUM: One-way slippage ~64%, resulting in severe capital loss.
- **Shorting Constraint:** On-chain shorting of subnet alpha tokens requires borrowing or synthetic derivatives; in the absence of a native decentralized lending market for alpha tokens, the long-short factor is primarily investable as a long-only small-tercile allocation relative to the market benchmark or pair trades against liquid wrapped representations.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Philip Z. Maymin (arXiv:2603.29751v1, Table I–XI, 2026):

1. **Factor Portfolio Performance (Full Sample, N=405 trading days):**
   - **MKT (Market Benchmark):** Mean return 0.29%/day, daily std 4.11%, annualized Sharpe 1.35, OLS $t=1.42$, Newey-West $t$ (5 lags) = 1.28, skewness 2.02, kurtosis 37.62.
   - **SMB (Small Minus Big Size):** Mean return 1.01%/day, daily std 5.01%, annualized return 367.1%, annualized std 95.7%, annualized Sharpe 3.84, OLS $t=4.04$, Newey-West $t$ (5 lags) = 3.28, skewness 1.74, kurtosis 11.68.
   - **Small Tercile (Bottom):** Mean return 0.87%/day, annualized return 317.4%, annualized std 111.7%, Sharpe 2.84.
   - **Large Tercile (Top):** Mean return -0.14%/day, annualized return -49.7%, annualized std 80.6%, Sharpe -0.62.
   - **$\text{WML}_7$ (7-Day Momentum):** Mean return 0.75%/day, daily std 3.92%, annualized Sharpe 3.65, Newey-West $t=3.05$, N=398.
   - **$\text{WML}_{30}$ (30-Day Momentum):** Mean return 0.68%/day, daily std 3.02%, annualized Sharpe 4.32, Newey-West $t=3.69$, N=375.
   - **REV (1-Day Reversal):** Mean return -0.86%/day, daily std 3.75%, annualized Sharpe -4.35, Newey-West $t=-3.62$, N=404.
   - **LIQ (Illiquid Minus Liquid):** Mean return 0.91%/day, daily std 4.61%, annualized Sharpe 3.77, Newey-West $t=3.06$, N=405. Correlation with SMB is $\rho = 0.93$.
   - **$\text{HML}_{\text{EMIS}}$ (Emission Yield):** Mean return 0.30%/day, daily std 4.33%, annualized Sharpe 1.33, Newey-West $t=1.04$ (spanned alpha $t=2.11$ in multi-factor regression).

2. **Cross-Sectional Asset Pricing Tests:**
   - **Fama-MacBeth Regression:** Size characteristic carries a statistically significant cross-sectional risk premium of 0.80%/day ($t=3.23$). Momentum is not significant in cross-sectional Fama-MacBeth tests (consistent with time-series rather than cross-sectional pricing).
   - **GRS Test (Gibbons-Ross-Shanken):** Three-factor model (MKT, SMB, WML30) tested on 12 sorted portfolios yields $F=1.31$, $p=0.21$, failing to reject the asset pricing specification at the 5% level.

3. **Natural Experiment (December 14, 2025 Halving):**
   - Network block emission fell discontinuously from 1.0 to 0.5 TAO per block.
   - Theoretical prediction from Proposition 1: Post/Pre SMB return ratio = 0.50.
   - Realized full post-halving period (103 days): Mean daily SMB fell from 1.17% to 0.51% (realized ratio = 0.44).
   - Regression discontinuity (60-day symmetric window): Post-halving dummy coefficient $\beta = -0.60$ percentage points/day ($t=-2.01$, Newey-West $p=0.044$). 45-day window: $\beta = -0.74$/day ($t=-2.29$, $p=0.022$).
   - Placebo tests at $\pm 30, \pm 60, \pm 90$ days yielded no statistically significant coefficients.

4. **Risk Asymmetry & Positive Volatility Relation:**
   - High 30-day realized volatility subnets outperform low volatility by 0.70%/day ($t=4.62$).
   - High downside semi-deviation subnets outperform low by 0.50%/day ($t=3.52$).
   - High market beta subnets outperform low beta by 0.63%/day ($t=4.28$).
   - SMB downside semi-deviation is 3.92%/day versus upside semi-deviation 5.79%/day (downside/upside ratio 0.68, Sortino ratio 4.90 vs Sharpe ratio 3.84).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Extreme Capacity Friction:** The strategy is strictly capacity-constrained. Above $100K USD AUM, AMM slippage completely consumes gross factor returns.
- **Short Sample Period:** 406 trading days (13 months) during the initial rollout of dTAO and high crypto market interest.
- **Survivorship & IPO Confounding:** The daily eligible universe grew from 63 to 124 subnets. New subnets enter the bottom size tercile by construction, and early "IPO-like" token price discovery could inflate historical small-tercile returns.
- **Unhedged Base-Currency Volatility:** Returns evaluated in TAO terms are exposed to substantial TAO/USD exchange rate volatility.

## Falsification plan

1. **Out-of-Sample Pool Deepening Test:** Track daily SMB return across 2026–2027 as aggregate AMM pool reserves increase. The AMM size premium hypothesis is falsified if SMB mean daily return falls below 0.10%/day ($t < 1.96$) in pools with median TAO reserves $> 5,000$ TAO.
2. **Emission Allocation Sensitivity Test:** Compare returns under price-based emission weighting versus Taoflow (flow-based moving average). If decoupling emission allocation from pool size eliminates the small-tercile excess return, the premium was driven by emission subsidy feedback rather than pure size risk.
3. **Execution Slippage Stress Test:** Execute micro-trades on testnet or with live low-notional extrinsics ($100–$1,000 USD). If realized slippage exceeds theoretical constant-product slippage $\Delta \tau / \tau$ by $> 25\%$ due to MEV frontrunning or validator priority fees, reject the micro-capacity feasibility.
4. **Subnet Deregistration Hazard Test:** Evaluate portfolio return when accounting for total loss on deregistered/recycled subnets. If liquidation losses on failed subnets eliminate net SMB carry, classify the size premium as unhedged credit/insolvency risk.

## Crypto portability

direct

The mechanism is native to decentralized cryptocurrency protocols and constant-product AMMs on the Bittensor (TAO) network. It directly exploits the structural interaction between on-chain automated market maker pool reserves and protocol emission tokenomics.

## Limitations

- **Not independently reproduced.**
- **Micro-Capacity Limit:** Bounded to $<$10K USD AUM; unscalable for institutional or medium-scale quant funds.
- **Execution Barrier on Short Leg:** Shorting unlisted alpha tokens on-chain requires overcollateralized lending markets that currently have limited depth for small subnets.
- **Regime Shift Risk:** Future Bittensor protocol governance adjustments (e.g., dynamic AMM fee tiers, concentrated liquidity curves, or Taoflow parameter changes) could alter the linear price impact relationship.
- **Base Token Volatility:** Exposure to native TAO price fluctuations when trading unhedged alpha tokens.

## Implementation status

not-implemented

No implementation in PyBroker, Nautilus, paper, testnet, or live trading has been performed.

## Adoption boundary

research-only

This record is research material only. Its presence in this repository does NOT constitute:
- validated trading alpha;
- authorization for automated implementation;
- approval for live trading, testnet execution, or capital deployment.

## Related Wiki records

- `[[crypto-cross-sectional-size-factor-smb-2026-08-31]]`
- `[[crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]`
- `[[crypto-cross-sectional-low-volatility-premium-post-2017-2026-09-01]]`
- `[[dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]`

## Sources

1. Maymin, Philip Z. (2026). "Common Risk Factors in Decentralized AI Subnets." arXiv:2603.29751v1 [q-fin.PM]. Published March 31, 2026.
   - URL: https://arxiv.org/abs/2603.29751
   - Key Sections & Tables: Section I (dTAO mechanism & AMM pricing), Section II (data & sample from Taostats API), Section III & Table I (factor summary statistics: SMB 1.01%/day, Sharpe 3.84, NW $t=3.28$), Table II (size terciles), Table III (momentum terciles), Table IV (factor correlation matrix), Section IV & Table V–VII (Fama-MacBeth regressions, GRS test $F=1.31, p=0.21$), Section V.C & Table VIII (Dec 14, 2025 halving natural experiment, $\beta = -0.60$/day, $p=0.044$), Section V.D & Table IX (Proposition 2 AMM slippage & capacity bounds), Section V.E & Table X–XI (volatility and downside risk asymmetry).
2. Taostats Blockchain Data API: https://api.taostats.io (on-chain pool reserve and emission dataset).
3. Bittensor Dynamic TAO Specification & Whitepaper: https://bittensor.com/dtao-whitepaper.
