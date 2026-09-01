---
schema: strategy-research-record-v1
title: "Geometric Mean Automated Market Makers as Verifiable Portfolio Mandates: Multi-Asset Fee Invariant Rebalancing and Arbitrage-Bounded Tracking Error"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi-amm
  - g3m
  - balancer
  - portfolio-management
  - verifiable-finance
  - arbitrage-rebalancing
  - tracking-error
status: research-only
confidence: high
source_as_of: 2026-08
sources:
  - "Zachary Feinstein, Ionut Florescu, and Sean O'Leary, 'Mandate without Managers: Automated Market Makers as Verifiable Portfolio Products', arXiv:2608.02917v1 [q-fin.PM, q-fin.TR], August 2026. DOI: 10.48550/arXiv.2608.02917. https://arxiv.org/abs/2608.02917"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Geometric Mean Automated Market Makers as Verifiable Portfolio Mandates: Multi-Asset Fee Invariant Rebalancing and Arbitrage-Bounded Tracking Error

## Provenance

- **Primary Source:** Zachary Feinstein, Ionut Florescu, and Sean O'Leary (School of Business, Stevens Institute of Technology), *"Mandate without Managers: Automated Market Makers as Verifiable Portfolio Products"*, arXiv preprint `arXiv:2608.02917v1 [q-fin.PM, q-fin.TR]`, August 2026. DOI: [10.48550/arXiv.2608.02917](https://doi.org/10.48550/arXiv.2608.02917). Full text: [https://arxiv.org/abs/2608.02917](https://arxiv.org/abs/2608.02917).
- **Primary Categories:** Portfolio Management (`q-fin.PM`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** Traditional asset management relies on centralized portfolio managers, custodians, and fund administrators to execute periodic discretionary or rule-based rebalancing, incurring management fees, execution drag, and agency risks. Feinstein, Florescu, and O'Leary reconceptualize Constant Function Market Makers—specifically the Geometric Mean Market Maker (G3M) invariant popularized by Balancer—as decentralized, verifiable portfolio technologies. By introducing a rigorous multi-asset fee structure, they prove that external competitive arbitrageurs endogenously enforce target-weighted portfolio mandates within analytical tracking error bounds while paying trading fees directly into the pool.

## Economic mechanism

### Source-reported

1. **AMMs as Self-Rebalancing Portfolios:** In a multi-asset Geometric Mean Market Maker (G3M), pool reserves $(R_1, R_2, \dots, R_n)$ satisfy the invariant $\prod_{i=1}^n R_i^{w_i} = k$, where $w_i > 0$ with $\sum_{i=1}^n w_i = 1$ are fixed target portfolio weights.
2. **Endogenous Arbitrage Rebalancing:** When external market prices $P = (P_1, \dots, P_n)$ fluctuate, the pool's marginal exchange rates deviate from external reference prices. Rational external arbitrageurs trade against the pool until marginal pool prices align with market prices, thereby restoring asset value ratios without requiring any active fund manager intervention.
3. **Multi-Asset Fee Band Structure:** In the presence of a proportional trading fee vector $\tau = (\tau_1, \dots, \tau_n) \in [0, 1)^n$, arbitrage is triggered only when relative price ratios exceed fee friction bounds:
   $$\frac{P_i}{P_j} \notin \left[ (1 - \tau_i)(1 - \tau_j) \frac{w_i R_j}{w_j R_i}, \frac{1}{(1 - \tau_i)(1 - \tau_j)} \frac{w_i R_j}{w_j R_i} \right]$$
   This fee wedge establishes an *ex-ante* bounded "band-rebalancing corridor," ensuring asset weights never drift beyond mathematically provable tolerance intervals.
4. **Verifiable Mandate Compliance:** A pool's compliance with its target mandate $(w_1, \dots, w_n)$ can be verified on-chain at any block directly from observable token balances $R_i$ and external oracle prices $P_i$, eliminating reporting lags and manager opacity.
5. **Fee Revenue Offsetting Loss-Versus-Rebalancing (LVR):** Unlike passive buy-and-hold portfolios that suffer rebalancing costs, the G3M collects swap fees from arbitrageurs on every rebalancing flow, creating an internal cash-flow engine that can offset adverse selection and tracking error.

### Research interpretation

The falsifiable thesis is that **a G3M pool parameterized with optimal multi-asset fee bands achieves superior net annualized return and lower empirical tracking error than traditional discretionary or periodic calendar-rebalanced target-weight funds (e.g., 60/40 balanced funds, equal-sector ETFs, equal-weighted equity indices)**:
- Continuous arbitrage-driven band rebalancing dampens extreme weight drift during trending market legs while avoiding excessive turnover costs during range-bound chop.
- The AMM fee structure monetizes volatility through external arbitrageur flows rather than paying bid-ask spread costs to external liquidity providers.

## Signal

### 1. Multi-Asset G3M Portfolio State & Quoting Rules

For a portfolio of $n$ assets with target weights $w = (w_1, \dots, w_n) \in \Delta^{n-1}$ and fee rates $\tau = (\tau_1, \dots, \tau_n)$:
- **Pool Value:** $V_{\mathrm{pool}}(t) = \sum_{i=1}^n P_i(t) R_i(t)$.
- **Effective Pool Weight:** $\hat{w}_i(t) = \frac{P_i(t) R_i(t)}{V_{\mathrm{pool}}(t)}$.
- **G3M Marginal Rate:** Marginal exchange rate between asset $i$ and asset $j$ inside the pool:
  $$p_{i/j}^{\mathrm{pool}}(t) = \frac{w_i R_j(t)}{w_j R_i(t)}$$

### 2. Arbitrage-Triggered Rebalancing Condition

An external arbitrage trade swapping $\Delta R_i$ of asset $i$ for $\Delta R_j$ of asset $j$ is executed by competitive searchers if and only if:
$$\frac{P_i(t)}{P_j(t)} > \frac{1}{(1 - \tau_i)(1 - \tau_j)} \frac{w_i R_j(t)}{w_j R_i(t)} \quad \text{or} \quad \frac{P_i(t)}{P_j(t)} < (1 - \tau_i)(1 - \tau_j) \frac{w_i R_j(t)}{w_j R_i(t)}$$

### 3. Ex-Ante Weight Deviation Bound

Under proportional fee parameter $\bar{\tau} = \max_{i,j} (1 - (1-\tau_i)(1-\tau_j))$, the maximum instantaneous weight misallocation $|\hat{w}_i(t) - w_i|$ is strictly bounded:
$$\sup_{t} |\hat{w}_i(t) - w_i| \le w_i (1 - w_i) \frac{\bar{\tau}}{1 - \bar{\tau}} + \mathcal{O}(\bar{\tau}^2)$$

### 4. Target Mandate Tracking Error Metric

Portfolio tracking error (TE) relative to the continuous benchmark mandate $B(t) = \sum_{i=1}^n w_i \frac{P_i(t)}{P_i(0)}$ is computed as:
$$\mathrm{TE}_{\mathrm{mandate}} = \sqrt{\frac{1}{T} \sum_{k=1}^K \left( \frac{V_{\mathrm{pool}}(t_k)}{V_{\mathrm{pool}}(t_{k-1})} - \frac{B(t_k)}{B(t_{k-1})} \right)^2}$$

## Required data

- **Asset Universe:** Multi-asset baskets corresponding to target-weight mandates:
  1. Balanced 60/40 Portfolio: Equity Index (e.g., S&P 500 / VOO) + Aggregate Bond Index (e.g., BND).
  2. Equal Sector Basket: 11 SPDR Sector ETFs (XLK, XLF, XLV, XLE, XLI, XLY, XLP, XLU, XLB, XLRE, XLC).
  3. Equal Weighted Dow 30: 30 constituent equities of the Dow Jones Industrial Average.
- **Reference Market Prices:** High-frequency ($1\text{s}$ to $1\text{min}$) external trade tape and NBBO mid-prices $P_i(t)$ across constituent assets.
- **On-Chain Pool Balances:** Exact token reserves $R_i(t)$ recorded at every transaction/block.
- **Gas / Execution Cost Data:** Transaction gas costs $g(t)$ to verify external searcher economic viability.

## Execution assumptions

- **Arbitrageur Competition:** Zero-profit competitive searcher limit; external arbitrageurs execute swaps whenever net profit exceeds gas transaction costs:
  $$\Pi_{\mathrm{arb}} = P_j \Delta R_j - P_i \Delta R_i - \mathrm{GasCost} > 0$$
- **Rebalancing Order Flow:** Passive maker liquidity provision; the pool does not submit active market orders.
- **Fee Accrual:** Swap fees $(1 - \tau)$ are retained entirely within pool reserves, compounding pool invariant $k_t$.
- **Settlement:** Atomic on-chain execution with zero counterparty settlement risk.

## Evidence

### Source-reported

- **Simulation Universe & Benchmarks:** Evaluated across three prominent incumbent fund structures:
  1. **VBIAX** (Vanguard Balanced Index Fund, 60% equity / 40% fixed income mandate).
  2. **EQL** (ALPS Equal Sector Weight ETF, 11 equal sector components).
  3. **EDOW** (First Trust Dow 30 Equal Weight ETF, 30 equal Dow components).
- **Comparative Metrics:** Annualized net return and tracking error relative to stated mandates evaluated across varying fee schedules $\tau \in [1\text{ bps}, 100\text{ bps}]$.
- **Performance Findings:**
  - In historical simulations, the G3M portfolio **outperformed incumbent funds** (VBIAX, EQL, EDOW) in both annualized net return and tracking error within moderate fee corridors ($\tau \in [5\text{ bps}, 30\text{ bps}]$).
  - The higher tracking error observed in incumbent ETFs relative to mutual funds was partially attributable to intraday market microstructure noise not captured by daily NAV reporting, whereas G3M balances track continuous theoretical targets.
  - Arbitrage-generated swap fees provided positive carry that fully compensated for LVR (Loss-Versus-Rebalancing) during non-trending and moderate volatility regimes.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Under extreme unilateral trend regimes (e.g., severe market crashes where one asset collapses to zero), AMM pool value experiences significant impermanent loss/LVR relative to a pure stop-loss protected portfolio.

## Falsification plan

1. **LVR vs. Fee Yield Breakeven Test:** Under simulated geometric Brownian motion price paths with asset drift $\mu_i$ and volatility $\sigma_i$, compute the empirical ratio $\mathcal{R} = \frac{\text{Cumulative Swap Fees}}{\text{LVR}}$. If $\mathcal{R} < 1.0$ across a representative historical cycle (e.g., 2020–2024), the thesis that AMM fee capture compensates for arbitrageur extraction is falsified.
2. **Fee-Band Tracking Error Stress Test:** Perturb the fee rate $\tau$ from 0 bps to 200 bps. If tracking error increases faster than $\mathcal{O}(\tau)$ or fails the analytical ex-ante upper bound, the mathematical rebalancing model is invalid.
3. **Searcher Latency & Gas Congestion Simulation:** Introduce high gas spike regimes where arbitrageurs delay rebalancing until price divergence reaches $> 5\%$. Measure tracking error degradation; if TE exceeds incumbent fund TE by $> 50\%$, the decentralized execution model fails under adverse network conditions.

## Crypto portability

- **Portability Classification:** `direct`.
- **Crypto Native Implementation:**
  - The mechanism is directly native to decentralized finance and smart contract blockchains (specifically implemented via Balancer v2 / v3 multi-token weighted pools).
  - Can be deployed immediately on EVM Layer-2s (Arbitrum, Base, Optimism) or Solana using native AMM protocols for index products (e.g., DeFi blue-chip indices, Layer-1 basket tokens, liquid staking derivative baskets).
- **Crypto Risks:**
  - Smart contract vulnerability risk, oracle manipulation (for dynamic fee hooks), toxic MEV sandwich attacks on rebalancing arbitrageurs, and pool liquidity fragmentation across competing DEXs.

## Limitations

- **Arbitrage Dependency:** The mechanism relies entirely on external economic actors to trigger rebalancing trades; in illiquid token markets where gas fees exceed potential arbitrage profits, asset weights can remain displaced outside target bands.
- **Cash Flow Imbalances:** Unlike traditional funds that can meet investor redemptions via proportional liquidations in primary markets, AMM LP token burns alter reserve ratios unless executed symmetrically.
- **Unilateral Trend Decay:** In persistent one-directional trend regimes without mean reversion, impermanent divergence loss accumulates monotonically.

## Implementation status

- Not implemented in our research stack.
- No PyBroker, NautilusTrader, paper, testnet, or live trading validation has been performed.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record represents theoretical and empirical research capture for quantitative intake review. It does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `[[quant/defi-amm-loss-versus-rebalancing-lvr-mechanics]]`
- `[[quant/balancer-weighted-pool-invariant-dynamics]]`
- `[[quant/arbitrage-driven-portfolio-rebalancing-corridors]]`

## Sources

- Zachary Feinstein, Ionut Florescu, and Sean O'Leary, "Mandate without Managers: Automated Market Makers as Verifiable Portfolio Products", arXiv preprint `arXiv:2608.02917v1 [q-fin.PM, q-fin.TR]`, August 2026. DOI: [10.48550/arXiv.2608.02917](https://doi.org/10.48550/arXiv.2608.02917). Full text: [https://arxiv.org/abs/2608.02917](https://arxiv.org/abs/2608.02917).
