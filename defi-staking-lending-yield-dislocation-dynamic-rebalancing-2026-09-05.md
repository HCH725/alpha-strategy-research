---
schema: strategy-research-record-v1
title: "DeFi Staking-Lending Yield Dislocation: Dynamic Yield-Spread Rebalancing and Frictional Mispricing Arbitrage in Ethereum Cryptoasset Markets"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - ethereum
  - defi
  - staking
  - liquid-staking
  - aave
  - lido
  - yield-arbitrage
  - market-inefficiency
status: research-only
confidence: medium
source_as_of: 2026-03-12
sources:
  - "Joel Hasbrouck, Julian Ma, Fahad Saleh, and Caspar Schwarz-Schilling, 'Market Inefficiency in Cryptoasset Markets', arXiv:2602.20771v2 [q-fin.TR], March 12, 2026. DOI: 10.48550/arXiv.2602.20771. https://arxiv.org/abs/2602.20771"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeFi Staking-Lending Yield Dislocation: Dynamic Yield-Spread Rebalancing and Frictional Mispricing Arbitrage in Ethereum Cryptoasset Markets

## Provenance

- **Primary Academic Source:** Joel Hasbrouck (New York University, Stern School of Business), Julian Ma (Independent Researcher), Fahad Saleh (Wake Forest University, School of Business), and Caspar Schwarz-Schilling (Independent Researcher), *"Market Inefficiency in Cryptoasset Markets"*, arXiv preprint `arXiv:2602.20771v2 [q-fin.TR]`, submitted February 24, 2026, revised March 12, 2026.
- **Canonical Digital Object Identifier (DOI):** [10.48550/arXiv.2602.20771](https://doi.org/10.48550/arXiv.2602.20771).
- **Traceable Full-Text URLs:**
  - Abstract & Metadata: [https://arxiv.org/abs/2602.20771](https://arxiv.org/abs/2602.20771)
  - Full-Text HTML: [https://arxiv.org/html/2602.20771v2](https://arxiv.org/html/2602.20771v2)
  - Full-Text PDF: [https://arxiv.org/pdf/2602.20771](https://arxiv.org/pdf/2602.20771)
  - Primary TeX Source Archive: [https://arxiv.org/e-print/2602.20771](https://arxiv.org/e-print/2602.20771) (contains unabridged LaTeX source `main.tex`, bibliography `references.bib`, and style file `jfe.bst`).
- **Primary Smart Contract Reference Points:**
  - Lido stETH Token & Deposit Contract: `0xae7ab96520de3a18e5e111b5eaab095312d7fe84` [source-reported].
  - Lido Withdrawal Queue Contract: `0x889edc2edab5f40e902b864ad4d7ade8e412f9b1` [source-reported].
  - Aave V3 Pool Contract (Ethereum Mainnet): `0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2` [source-reported].
- **Pre-Write Deduplication & Independence Audit:**
  - A comprehensive repository-wide search on 2026-09-05 confirmed zero existing records citing `arXiv:2602.20771`, `Market Inefficiency in Cryptoasset Markets`, `Julian Ma`, `Fahad Saleh`, or `Caspar Schwarz-Schilling`.
  - While existing records in the repository examine LST secondary discount basis arbitrage on Curve pre-Shanghai (`liquid-staking-basis-mean-reversion-discount-arbitrage-2026-09-01.md`), perpetual funding spread arbitrage (`perpetual-inverse-linear-margin-currency-funding-spread-2026-09-01.md`), and high-frequency spot-perpetual price discovery (`crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01.md`), this record is structurally, mechanically, and empirically distinct: it evaluates post-Shanghai (2023–2025) equilibrium yield linkages across native Ethereum Proof-of-Stake consensus, Aave V3 decentralized lending pools, and Lido liquid staking, documenting an econometric rejection of no-arbitrage restrictions under arbitrary risk pricing.

## Economic mechanism

### Source-reported

1. **Common Dominant Risk Factor with Segmented Return Structures:** Investors holding ether (ETH) on the Ethereum blockchain face three distinct capital deployment alternatives [source-reported]:
   - *Direct Staking:* Locking ETH in the consensus protocol to become an active validator, earning the protocol staking yield $\gamma_t^{ETH}$ (seigniorage rewards plus EIP-1559 priority fees and Maximal Extractable Value [MEV]) net of operational and hardware staking costs $\kappa$ [source-reported].
   - *ETH Lending:* Supplying ETH to a Decentralized Lending Protocol (DLP, specifically Aave V3) to earn the algorithmic supply interest rate $\psi_t^{ETH}$, which fluctuates dynamically with pool utilization [source-reported].
   - *Liquid Staking Token (LST) Lending:* Depositing ETH with a Staking Service Provider (SSP, specifically Lido) to mint staked ether (stETH) one-for-one, which accrues the net staking yield $\gamma_t^{stETH} = 0.90 \times \gamma_t^{ETH}$ (after Lido's 10% protocol fee), and simultaneously supplying that stETH to Aave V3 to earn an additional lending interest yield $\psi_t^{stETH}$ [source-reported].
2. **Dominant vs. Secondary Risk Decomposition:** All three strategies share the dominant risk factor: the price return of ETH ($r_{t, t+1}^{ETH}$). Liquid staking introduces a secondary risk factor: the stETH-ETH exchange rate can deviate from unity ($\chi_t = \log(P_t^{stETH}/P_t^{ETH}) < 0$, de-peg discount risk). Because stETH is redeemable for ETH via Lido's withdrawal queue, it trades near parity (mean ratio 0.999), and de-peg deviations are minor under normal conditions [source-reported].
3. **No-Arbitrage Equilibrium Restrictions under Arbitrary Risk Pricing:** The authors formulate an asset pricing framework with an unconstrained stochastic discount factor / pricing kernel $\Lambda_{t, t+1}$ that prices ETH return innovations ($\lambda_{ETH}$) and 2-state Markov de-peg innovations ($\lambda_\chi$) without restricting how investors price either risk [source-reported]. By applying the fundamental Euler equation $\mathbb{E}[\Lambda_{t, t+1} R_{t, t+1}^i \mid \mathcal{F}_t] = 1$ to each strategy, the model yields tight, necessary equilibrium restrictions relating observable yields [source-reported]:
   - *Proposition 4 (stETH Lending vs. ETH Staking):* $\psi_t^{stETH} = \gamma_t^{ETH} - \gamma_t^{stETH} + \tilde{\eta}_t - \kappa$ [source-reported].
   - *Proposition 5 (stETH Lending vs. ETH Lending):* $\psi_t^{stETH} = \psi_t^{ETH} - \gamma_t^{stETH} + \tilde{\eta}_t$ [source-reported].
   In an efficient market where capital reallocates freely, changes in the yield differentials must be matched one-for-one by changes in the stETH lending yield ($\beta = 1$) [source-reported].
4. **Empirical Rejection of Equilibrium & Frictional Capital Impediment:** Using 966 daily observations from January 30, 2023 to September 21, 2025, regression tests resoundingly reject $\beta = 1$ ($p < 0.001$ for both tests) [source-reported]. Rather than adjusting one-for-one, $\psi_t^{stETH}$ shows almost zero sensitivity to the ETH lending-staking spread ($\hat{\beta} = 0.017$) and a statistically significant negative response to the protocol fee wedge ($\hat{\beta} = -0.228$) [source-reported]. Because the test holds for any price of de-peg risk, the failure cannot be explained by risk mispricing; instead, it demonstrates that market frictions impede capital reallocation across cryptoasset yield venues [source-reported].

### Research interpretation

The econometric finding indicates persistent structural market segmentation between Ethereum's consensus layer, decentralized lending markets, and liquid staking tokens:
1. **Source of Frictional Inertia:** The failure of yields to co-move stems from institutional and architectural frictions:
   - *Redemption Latency & Unstaking Queue:* Direct staking and Lido redemption pass through the Ethereum consensus exit queue, requiring days to weeks. Investors cannot rapidly recall staked capital when lending rates spike.
   - *Kinked Borrow Curves & Recursive Loops:* Aave V3 lending rates spike non-linearly when borrowing utilization exceeds the optimal kink (typically 80%–90%). Surges in leverage demand (e.g. traders borrowing ETH to short or loop into yield farms) drive $\psi_t^{ETH}$ as high as 17.80%, yet capital parked in stETH cannot arbitrage this spike instantaneously due to gas costs, liquidation risk, and withdrawal friction.
   - *Sticky Supply Rate on LSTs:* Demand to borrow stETH is structurally low (mean $\psi^{stETH} = 0.05\%$), keeping its lending yield pinned near zero regardless of general ETH yield conditions.
2. **Systematic Alpha Opportunity:** This structural mispricing creates an exploitable, market-neutral carry & dynamic rebalancing strategy on ETH-denominated principal:
   - During normal regimes ($\psi_t^{ETH} < \gamma_t^{stETH}$), holding stETH and supplying it on Aave captures a ~100–110 bps yield premium over lending vanilla ETH with negligible de-peg risk.
   - During high-utilization borrowing surges ($\psi_t^{ETH} > \gamma_t^{stETH} + \psi_t^{stETH}$), migrating capital to Aave ETH supply captures transient borrowing spikes (up to 17.80% annualized), harvesting excess carry.
   - A systematic rule switching between these two states conditional on the observable yield spread $\Delta_t = \psi_t^{ETH} - (\gamma_t^{stETH} + \psi_t^{stETH})$, filtered by a peg-stability threshold and gas-cost hurdle, extracts excess yield while maintaining zero net price exposure to ETH/USD fluctuations.

## Signal

### Mathematical Formulation & Target Definition

Let $t$ index daily observation intervals. The strategy operates on five primary observable daily variables [source-reported]:
- $\psi_t^{ETH}$: Annualized log lending yield (supply APR) for ETH on Aave V3 [source-reported].
- $\psi_t^{stETH}$: Annualized log lending yield (supply APR) for stETH on Aave V3 [source-reported].
- $\gamma_t^{ETH}$: Annualized log Ethereum protocol staking yield [source-reported].
- $\gamma_t^{stETH}$: Annualized log staking yield passed to Lido stETH holders ($\gamma_t^{stETH} = 0.90 \times \gamma_t^{ETH}$) [source-reported].
- $\chi_t := \log(P_t^{stETH} / P_t^{ETH})$: Log stETH-ETH price ratio (peg discount measure) [source-reported].

The primary state variable is the **Lending-Staking Carry Spread** $\Delta_t$ `[research-proposed]`:
$$\Delta_t := \psi_t^{ETH} - \left( \gamma_t^{stETH} + \psi_t^{stETH} \right)$$

where:
- $\Delta_t > 0$ indicates that lending ETH on Aave yields a higher rate than holding stETH and supplying it on Aave.
- $\Delta_t < 0$ indicates that the combined liquid staking + LST lending strategy dominates direct ETH lending.

### Input Specification & Data Fields

1. **Aave V3 Reserve State:** Trailing 24-hour time-weighted average supply rate for WETH and stETH reserves on Ethereum mainnet [source-reported].
2. **Consensus Staking Yield:** Trailing 7-day moving average of Ethereum network staking APR (Dune query 570874/1464690 or execution/consensus beacon client telemetry) [source-reported].
3. **Peg Discount Metric:** Daily average price ratio $P_t^{stETH} / P_t^{ETH}$ derived from CoinGecko / major DEX liquidity pools (Curve stETH/ETH pool `0xDC243607692288994371BC8588078875375E4776`) [source-reported].
4. **Gas Base Fee:** EIP-1559 base fee $\text{BaseFee}_t$ in gwei, used to evaluate the economic viability of a contract rebalance `[research-proposed]`.

### Model Decision Rule & Operational Thresholds

The capital allocation state $S_t \in \{\text{LEND\_ETH}, \text{STAKE\_LEND\_STETH}\}$ is updated at daily close $t$ `[research-proposed]`:

1. **Regime A: High Lending Demand / ETH Lending Overweight**
   - Condition: $\Delta_t > \tau_{\text{enter}}$ AND $|\chi_t| < \chi_{\text{safe}}$ `[research-proposed]`
   - Parameter values: $\tau_{\text{enter}} = +0.75\%$ annualized (+75 bps), $\chi_{\text{safe}} = 0.005$ (0.5% peg deviation) `[research-proposed]`.
   - Action: Allocate 100% of capital to Aave V3 WETH lending pool (`0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2`) `[research-proposed]`.
2. **Regime B: Baseline Regime / Liquid Staking Overweight**
   - Condition: $\Delta_t \le \tau_{\text{exit}}$ AND $\chi_t \ge -\chi_{\text{safe}}$ `[research-proposed]`
   - Parameter values: $\tau_{\text{exit}} = +0.15\%$ annualized (+15 bps) `[research-proposed]`.
   - Action: Allocate 100% of capital to holding stETH and supplying it to Aave V3 stETH reserve `[research-proposed]`.
3. **Hysteresis Band:** The gap between $\tau_{\text{enter}} = 0.75\%$ and $\tau_{\text{exit}} = 0.15\%$ creates a 60 bps deadband to prevent portfolio churn and transaction-cost erosion `[research-proposed]`.
4. **Peg Risk Circuit Breaker:**
   - If $\chi_t < -0.010$ (stETH trades at $>1.0\%$ discount to ETH), freeze rebalancing into stETH immediately `[research-proposed]`.
   - If already in stETH during a severe discount shock ($\chi_t < -0.015$), do not sell stETH into secondary automated market makers (Curve/Uniswap); instead, submit a withdrawal request to Lido's canonical Withdrawal Queue contract (`0x889edc2edab5f40e902b864ad4d7ade8e412f9b1`) to ensure redemption at full 1:1 parity within the protocol `[research-proposed]`.
5. **Gas Amortization Filter:**
   - A rebalance transaction is executed only if the projected net carry improvement over the minimum expected holding horizon $H_{\min} = 14\text{ days}$ exceeds $3 \times$ estimated Ethereum L1 transaction gas fees `[research-proposed]`:
     $$\text{Capital} \times \left|\Delta_t\right| \times \frac{H_{\min}}{365} > 3 \times \text{GasCost}_{\text{rebalance}}$$

## Required data

- **Asset Universe:** Ether (ETH / WETH), Lido Staked Ether (stETH), Aave Ethereum WETH aToken (aWETH), Aave Ethereum stETH aToken (astETH) [source-reported].
- **Venues & Smart Contracts:**
  - Ethereum Mainnet consensus and execution clients [source-reported].
  - Lido stETH Core Contract: `0xae7ab96520de3a18e5e111b5eaab095312d7fe84` [source-reported].
  - Lido Withdrawal Queue Contract: `0x889edc2edab5f40e902b864ad4d7ade8e412f9b1` [source-reported].
  - Aave V3 Pool Contract: `0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2` [source-reported].
- **Market Data Feeds:**
  - Aave V3 daily supply yields ($\psi_t^{ETH}, \psi_t^{stETH}$) obtained via Aavescan / Aave API / on-chain contract events [source-reported].
  - Ethereum protocol staking yield $\gamma_t^{ETH}$ and Lido passed-through yield $\gamma_t^{stETH}$ from Dune Analytics (query 570874/1464690) [source-reported].
  - Daily stETH/ETH exchange rate $P_t^{stETH}/P_t^{ETH}$ from CoinGecko daily closing series and secondary DEX pools (Curve stETH/ETH) [source-reported].
  - Ethereum network base fee from execution client block headers (`eth_gasPrice` / EIP-1559 base fee) `[research-proposed]`.
- **Sampling & Timezone Conventions:** Daily observation frequency sampled at 00:00:00 UTC [source-reported].
- **Point-in-Time Integrity:** All rate, yield, and exchange rate variables are strictly lagged to date $t$ close to prevent look-ahead bias in date $t+1$ rebalance scheduling [source-reported].
- **Missing-Data & Stale Print Handling:** Missing daily rate points are forward-filled for at most 1 day; if feed staleness exceeds 24 hours, capital defaults to static stETH holding until fresh telemetry is verified `[research-proposed]`.

## Execution assumptions

- **Execution Mechanism:** On-chain programmatic smart contract calls executing via decentralized protocol interfaces [source-reported]:
  - Minting stETH: Calling `submit(address(0))` on Lido deposit contract with ETH value [source-reported].
  - Lending ETH on Aave: Calling `supply(address WETH, uint256 amount, address onBehalfOf, uint16 referralCode)` on Aave V3 Pool contract [source-reported].
  - Lending stETH on Aave: Calling `supply(address stETH, uint256 amount, address onBehalfOf, uint16 referralCode)` on Aave V3 Pool contract [source-reported].
  - Redemptions: Calling `requestWithdrawals(uint256[] amounts, address owner)` on Lido Withdrawal Queue contract [source-reported].
- **Execution Timing & Latency:** Decisions computed at 00:00 UTC; transactions dispatched during low-gas windows (typically European/early Asian morning hours, 02:00–06:00 UTC) `[research-proposed]`.
- **Transaction Costs & Gas Modeling:**
  - Estimated gas consumption per state switch: ~350,000 gas units (withdraw aToken + deposit to new reserve / wrap / submit) `[research-proposed]`.
  - At an assumed average base fee of 25 gwei and ETH price of \$3,000, round-trip rebalancing gas cost is $\approx 0.00875\text{ ETH} \approx \$26.25$ `[research-proposed]`.
- **Slippage & Secondary Market Impact:** Zero market price impact when depositing/withdrawing directly through canonical protocol contracts (Lido minting is exact 1:1; Aave supply/withdraw has zero price impact on pool reserves) [source-reported]. If an emergency exit requires secondary market swapping on Curve, slippage is bounded at $<0.15\%$ for sizes up to 1,000 ETH `[research-proposed]`.
- **Leverage & Collateralization:** Unleveraged spot strategy (1.0x gross exposure to ETH principal); no recursive borrowing, no debt positions, eliminating protocol liquidation risk `[research-proposed]`.
- **Capacity Constraint:** Aave V3 ETH reserve liquidity exceeds \$2B, and Lido manages over 9.5M ETH [source-reported]. Strategy capacity is institutional-grade ($\ge \$50\text{M}$ principal) before encountering significant interest rate dilution on Aave supply curves `[research-proposed]`.

## Evidence

### Source-reported

1. **Empirical Dataset & Summary Statistics (Table 1, arXiv:2602.20771v2):**
   - Sample period: January 30, 2023 to September 21, 2025 (966 daily observations) [source-reported].
   - $\psi^{ETH}$ (Aave ETH lending yield):
     - Mean: $1.92\%$ [source-reported]
     - Std. Dev.: $0.65\%$ [source-reported]
     - Min: $0.95\%$ [source-reported]
     - Max: $17.80\%$ [source-reported]
   - $\psi^{stETH}$ (Aave stETH lending yield):
     - Mean: $0.05\%$ [source-reported]
     - Std. Dev.: $0.07\%$ [source-reported]
     - Min: $0.00\%$ [source-reported]
     - Max: $0.67\%$ [source-reported]
   - $\gamma^{ETH}$ (Ethereum protocol staking yield):
     - Mean: $3.29\%$ [source-reported]
     - Std. Dev.: $0.64\%$ [source-reported]
     - Min: $2.18\%$ [source-reported]
     - Max: $12.27\%$ [source-reported]
   - $\gamma^{stETH}$ (Lido staking yield, net of 10% fee):
     - Mean: $2.96\%$ [source-reported]
     - Std. Dev.: $0.58\%$ [source-reported]
     - Min: $1.97\%$ [source-reported]
     - Max: $11.05\%$ [source-reported]
   - stETH/ETH Exchange Ratio:
     - Mean: $0.999$ [source-reported]
     - Std. Dev.: $0.001$ [source-reported]
     - Min: $0.990$ [source-reported]
     - Max: $1.015$ [source-reported]

2. **Tests of Market Efficiency & No-Arbitrage Restrictions (Table 2, arXiv:2602.20771v2):**
   - Both models estimated using ordinary least squares with Newey-West Heteroskedasticity and Autocorrelation Consistent (HAC) standard errors (10 lags) [source-reported]:
   - **Model 1: Test of Proposition 4 (stETH Lending vs. ETH Staking)**
     $$\psi_t^{stETH} = \alpha + \beta \left(\gamma_t^{ETH} - \gamma_t^{stETH}\right) + \epsilon_t$$
     - Estimated slope $\hat{\beta}$: $-0.228$ (HAC standard error: $0.043$) [source-reported].
     - Estimated intercept $\hat{\alpha}$: $0.12\%$ annualized (HAC standard error: $0.02\%$) [source-reported].
     - $t$-statistic for null hypothesis $H_0: \beta = 1$: $-28.33$ [source-reported].
     - $p$-value: $< 0.001$ (rejects market efficiency at the 1% level) [source-reported].
     - Coefficient of determination $R^2$: $0.143$ [source-reported].
     - *Economic finding:* When the protocol staking yield differential $\gamma^{ETH} - \gamma^{stETH}$ increases, the stETH lending yield actually decreases ($\hat{\beta} < 0$), contradicting the theoretical prediction of co-movement [source-reported].
   - **Model 2: Test of Proposition 5 (stETH Lending vs. ETH Lending)**
     $$\psi_t^{stETH} = \alpha + \beta \left(\psi_t^{ETH} - \gamma_t^{stETH}\right) + \epsilon_t$$
     - Estimated slope $\hat{\beta}$: $0.017$ (HAC standard error: $0.005$) [source-reported].
     - Estimated intercept $\hat{\alpha}$: $0.06\%$ annualized (HAC standard error: $0.01\%$) [source-reported].
     - $t$-statistic for null hypothesis $H_0: \beta = 1$: $-179.22$ [source-reported].
     - $p$-value: $< 0.001$ (rejects market efficiency at the 1% level) [source-reported].
     - Coefficient of determination $R^2$: $0.120$ [source-reported].
     - *Economic finding:* A 1.0 percentage point increase in $\psi^{ETH} - \gamma^{stETH}$ generates only a $0.017$ percentage point response in $\psi^{stETH}$, demonstrating extreme stickiness and market segmentation [source-reported].

### Independently reproduced

Not independently reproduced. All econometric coefficients, $t$-statistics, summary statistics, and empirical distributions are third-party results reported by Hasbrouck, Ma, Saleh, and Schwarz-Schilling (arXiv:2602.20771v2). No internal smart contract replay or historical simulator execution in PyBroker or NautilusTrader has been performed.

### Negative evidence

1. **Capital Reallocation Frictions as Limits to Arbitrage:** The authors explicitly conclude that the rejection of equilibrium reflects real-world frictions that impede capital movement. The primary friction is redemption queue duration: while entering liquid staking or lending is instantaneous, unstaking from Lido or Ethereum consensus requires queuing through the consensus exit mechanism, which introduces temporal illiquidity risk during market dislocations [source-reported].
2. **Asymmetric Risk in Rate Spike Capture:** When ETH lending rates spike (e.g. to 17.80%), an investor whose capital is currently held in stETH cannot unstake quickly enough to capture short-lived spikes (which often normalize within 48–72 hours) unless they accept secondary market slippage on DEX pools `[research-proposed]`.
3. **Smart Contract & Protocol Upgrade Risks:** Supplying assets to Aave V3 or Lido exposes capital to smart contract bugs, governance parameter changes (e.g. reserve factor adjustments, borrow caps), and oracle latency during extreme volatility `[research-proposed]`.
4. **Negative Response Anomaly:** The negative $\hat{\beta} = -0.228$ in Model 1 indicates that periods of high network fee generation (which elevate protocol staking yield $\gamma^{ETH}$) frequently coincide with broader market congestion and demand shifts that fail to translate into LST lending demand on Aave [source-reported].

## Falsification plan

The following operational empirical tests are designed to disprove or materially invalidate the alpha hypothesis:

1. **Out-of-Sample Equilibrium Convergence Test:**
   - *Data:* Daily yield series from September 22, 2025 through December 31, 2026 across Aave V3, Lido, and Ethereum consensus `[research-proposed]`.
   - *Methodology:* Re-estimate Model 2 ($\psi_t^{stETH}$ on $\psi_t^{ETH} - \gamma_t^{stETH}$) with Newey-West HAC standard errors (10 lags).
   - *Falsification Threshold:* If $\hat{\beta}_{\text{OOS}} \ge 0.80$ and the null hypothesis $H_0: \beta = 1$ cannot be rejected at the 5% significance level ($p \ge 0.05$), market efficiency has been restored through automated cross-protocol arbitrage vaults (e.g. morpho/euler rebalancers); the structural dislocation hypothesis is falsified `[research-defined falsification threshold]`.
   - *Action on Failure:* Retire the dynamic yield dislocation hypothesis.
2. **Net-of-Gas Realized Yield Hurdle Test:**
   - *Data:* Historical simulation over the 2023–2025 sample incorporating actual block-by-block Ethereum base fees and priority fees `[research-proposed]`.
   - *Evaluation Metric:* Annualized net return of the dynamic switching strategy minus the static buy-and-stake Lido benchmark return for a \$500,000 capital base `[research-proposed]`.
   - *Falsification Threshold:* If the annualized net yield improvement over static staking is $< 0.20\%$ (+20 bps net of gas costs), the observed yield dislocation is an unexecutable friction illusion driven by transaction costs `[research-defined falsification threshold]`.
   - *Action on Failure:* Reclassify the phenomenon as an unexecutable friction boundary and reject implementation.
3. **De-Peg Shock Drawdown Test:**
   - *Data:* Full historical tick data during stETH de-peg stress events (e.g. June 2022 Celsius/stETH event, November 2022 FTX collapse, March 2023 SVB de-peg) `[research-proposed]`.
   - *Evaluation Metric:* Maximum drawdown of ETH principal during the event window `[research-proposed]`.
   - *Falsification Threshold:* If maximum drawdown of ETH-denominated capital exceeds $-1.50\%$ at any point during a de-peg episode, the tail risk of holding stETH overwhelms the incremental carry `[research-defined falsification threshold]`.
   - *Action on Failure:* Reject the strategy for institutional capital deployment.
4. **Cross-Protocol Inefficiency Robustness Test:**
   - *Data:* Parallel daily supply yields across alternative decentralized lending venues: Spark Protocol, Morpho Blue (WETH and wstETH vaults), and Compound V3 over the 2023–2025 period `[research-proposed]`.
   - *Evaluation Metric:* Slope coefficient $\beta_{\text{alt}}$ of stETH lending yield on the lending-staking spread across non-Aave venues `[research-proposed]`.
   - *Falsification Threshold:* If $\hat{\beta}_{\text{alt}} \approx 1.0$ on alternative venues, the documented inefficiency is an artifact of Aave V3's specific interest rate kink parameters rather than a market-wide phenomenon `[research-defined falsification threshold]`.
   - *Action on Failure:* Restrict scope exclusively to Aave V3 parameter optimization or discard as venue-specific anomaly.

## Crypto portability

- **Portability Status:** `direct` [source-reported].
- **Rationale:** The underlying theory, empirical dataset, and institutional mechanisms originate directly within the native Ethereum blockchain ecosystem (Proof-of-Stake consensus, Lido smart contracts, Aave V3 lending pools). No traditional asset porting or proxy mapping is required.
- **Crypto-Specific Frictions & Structural Characteristics:**
  - *Consensus Queue Mechanics:* Ethereum consensus enforces churn limits on validator activation and exits. During periods of heavy validator exits, the withdrawal queue can stretch from days to weeks, creating redemption delays that do not exist in traditional money markets.
  - *Smart Contract Interoperability:* While minting stETH and supplying to Aave is executed atomically in single Ethereum transactions, unravelling positions requires multi-step approvals and contract calls subject to block confirmation latency.
  - *Oracle Dependency:* Lending pool interest rate calculations depend on internal reserve indices updated upon every pool interaction, ensuring that rate calculations reflect real-time on-chain utilization without external oracle delay.
  - *Gas Dynamics:* EIP-1559 base fee spikes during high-volatility events can increase rebalancing costs by an order of magnitude (from 15 gwei to $>150$ gwei), demanding explicit gas-cost gating for smaller account sizes.

## Limitations

- **Asymmetric Liquidity & Unstaking Latency:** The primary source establishes that capital reallocation frictions exist, but does not provide an algorithmic protocol for navigating withdrawal queue delays. In practical trading, switching from stETH back to vanilla ETH via canonical withdrawal requires waiting for protocol processing, whereas switching via decentralized exchanges (Curve/Uniswap) incurs price discount and liquidity slippage [source-reported].
- **Rate Kink Discontinuity:** Aave V3 uses a two-slope piece-wise linear interest rate curve with a steep slope above optimal utilization (typically 80% or 90%). ETH lending rates exhibit extreme right-skewness (max 17.80% vs mean 1.92%), meaning that the majority of the spread alpha is concentrated in brief, high-volatility borrowing episodes rather than a constant steady-state drift [source-reported].
- **Unmodeled Smart Contract Risk:** Neither the theoretical model nor the empirical regressions explicitly quantify smart contract audit risk, economic exploit risk, or governance risk across Lido and Aave. A small yield pickup (e.g. 50–100 bps) may represent a fair risk premium for bearing smart contract composability exposure.
- **Data Gap:** The empirical study relies on daily aggregated snapshots (966 observations). High-frequency block-by-block rate oscillations and intra-day utilization spikes are smoothed out in the published dataset [source-reported].

## Implementation status

`not-implemented`.

This research capture documents external academic findings from Hasbrouck, Ma, Saleh, and Schwarz-Schilling (arXiv:2602.20771v2). No smart contract integration, automated rebalancing script, backtest harness, or strategy module has been implemented in PyBroker, NautilusTrader, paper trading, testnet, or live trading infrastructure.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record serves exclusively as normalized research material for the quantitative strategy staging pipeline. Presence in this repository does not constitute:
- Validation of persistent alpha in live execution;
- Approval for portfolio deployment or capital allocation;
- Authorization for paper, testnet, or live trading.

Any progression toward prototyping or backtesting requires explicit, independent review and approval outside the Research Scout workflow.

## Related Wiki records

- `[[liquid-staking-basis-mean-reversion-discount-arbitrage-2026-09-01]]` — Evaluates Curve pool LST discount basis mean reversion prior to the Shanghai upgrade.
- `[[perpetual-inverse-linear-margin-currency-funding-spread-2026-09-01]]` — Examines cross-instrument yield and funding rate mispricings across crypto margin types.
- `[[crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01]]` — Analyzes cross-venue price discovery and information share dynamics between spot and derivative crypto venues.

## Sources

1. **Primary Academic Source:**
   - Joel Hasbrouck, Julian Ma, Fahad Saleh, and Caspar Schwarz-Schilling. *"Market Inefficiency in Cryptoasset Markets"*. arXiv preprint `arXiv:2602.20771v2 [q-fin.TR]`, submitted February 24, 2026, revised March 12, 2026.
   - DOI: [https://doi.org/10.48550/arXiv.2602.20771](https://doi.org/10.48550/arXiv.2602.20771)
   - Abstract: [https://arxiv.org/abs/2602.20771](https://arxiv.org/abs/2602.20771)
   - Full-text HTML: [https://arxiv.org/html/2602.20771v2](https://arxiv.org/html/2602.20771v2)
   - PDF: [https://arxiv.org/pdf/2602.20771](https://arxiv.org/pdf/2602.20771)
   - Complete TeX bundle: [https://arxiv.org/e-print/2602.20771](https://arxiv.org/e-print/2602.20771) (LaTeX source file `main.tex`, bibliography file `references.bib`, style file `jfe.bst`).
2. **Empirical Data & Smart Contract References Cited by Primary Source:**
   - Aavescan Lending Yield Telemetry: [https://aavescan.com/](https://aavescan.com/) (accessed September 2025).
   - Dune Analytics Ethereum Staking Query: [https://dune.com/queries/570874/1464690](https://dune.com/queries/570874/1464690) (accessed September 2025).
   - CoinGecko Historical Price Series (ETH & stETH): [https://www.coingecko.com/en/coins/lido-staked-ether](https://www.coingecko.com/en/coins/lido-staked-ether) and [https://www.coingecko.com/en/coins/ethereum](https://www.coingecko.com/en/coins/ethereum) (accessed September 2025).
   - Lido Core stETH Contract: `0xae7ab96520de3a18e5e111b5eaab095312d7fe84`
   - Lido Withdrawal Queue Contract: `0x889edc2edab5f40e902b864ad4d7ade8e412f9b1`
   - Aave V3 Pool Contract: `0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2`
