---
schema: strategy-research-record-v1
title: "Policy-Selected Transaction Tapes in Automated Market Makers: Ranking Certification under Hidden Opportunities"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - lvr
  - partial-identification
  - selection-bias
  - transaction-tapes
  - market-microstructure
  - empirical-falsification
status: research-only
confidence: high
source_as_of: 2026-09-17
sources:
  - "Wen-Ting Wang, 'Policy-Selected Transaction Tapes in Automated Market Makers: Ranking Certification under Hidden Opportunities', arXiv:2609.19013v1 [q-fin.ST, stat.ME], September 17, 2026. https://arxiv.org/abs/2609.19013"
  - "Wen-Ting Wang, 'amm-lab', GitHub repository commit f37ee93b80ac6e19088180f3ce3393e3fb68ecbd, September 2026. https://github.com/egpivo/amm-lab"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Policy-Selected Transaction Tapes in Automated Market Makers: Ranking Certification under Hidden Opportunities

## Provenance

- **Primary Source:** Wen-Ting Wang (Institute of Statistics, National Chung Hsing University, Taiwan, `egpivo@gmail.com`), *"Policy-Selected Transaction Tapes in Automated Market Makers: Ranking Certification under Hidden Opportunities"*, arXiv preprint `arXiv:2609.19013v1 [q-fin.ST, stat.ME]`, submitted September 17, 2026.
- **Canonical Identifier / Stable URL:** https://arxiv.org/abs/2609.19013
- **Canonical DOI:** [10.48550/arXiv.2609.19013](https://doi.org/10.48550/arXiv.2609.19013)
- **Full-Text HTML Source:** https://arxiv.org/html/2609.19013v1
- **Full-Text PDF Source:** https://arxiv.org/pdf/2609.19013v1
- **Reference Implementation / Codebase:** Public open-source Rust & Python system `egpivo/amm-lab` at immutable commit SHA `f37ee93b80ac6e19088180f3ce3393e3fb68ecbd` (MIT License). Track 4 ("Paper — LVR / Policy-Selected Tapes") code modules audited:
  - `src/pstt/` (`application.rs`, `asof.rs`, `block_time.rs`, `bootstrap.rs`, `cex.rs`, `classification.rs`, `diagnostics.rs`, `error.rs`, `manifest.rs`, `marks.rs`, `mod.rs`, `orientation.rs`, `panel.rs`, `parity.rs`, `projection.rs`, `schema.rs`, `sensitivity.rs`, `weekly.rs`).
  - `tests/` (`pstt_parity_gate.rs`, `pstt_prepare_gate.rs`, `pstt_projection_gate.rs`, `pstt_staleness_gate.rs`, `pstt_standalone_gate.rs`).
  - `scripts/lvr/` (paired decomposition, grid decomposition, joint support, and projection analysis scripts).
- **Source Verification:** The primary preprint full-text HTML, formal mathematical proofs (Propositions 2.1, 2.2, Corollary 2.3, Theorem 3.1, Corollary 3.2, Propositions A.1, Theorem A.2, Theorem C.2), Table 1, Figures 1–2, and reference Rust test fixtures were directly inspected. All numerical point estimates, bootstrap parameters, confidence intervals, effective sample sizes, and empirical findings cited in this record trace directly to Sections 1–6 and Appendices A–C of `arXiv:2609.19013v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.19013`, Wen-Ting Wang, `amm-lab`, or policy-selected transaction tape ranking certification. Adjacent AMM/LVR records in the repository (`crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31.md`, `amm-lvr-jump-floor-optimal-block-time-2026-09-08.md`, `defi-concentrated-liquidity-amm-dynamic-fee-staleness-proxy-lvr-compensation-2026-09-02.md`, `optimal-dynamic-fee-amm-pro-cyclical-lvr-volatility-feedback-2026-09-09.md`) investigate theoretical continuous-time LVR formulas under stylized geometric Brownian motion or jump-diffusion price paths; none address the econometric non-identification of empirical transaction tapes, selection bias from matching mechanisms, synchronized calendar moving-block bootstrap inference, or the empirical falsification of cross-pool loss-per-service rankings.

## Economic mechanism

### Source-reported

In decentralized finance (DeFi), market participants, liquidity providers (LPs), and protocol designers frequently compare and rank automated market maker (AMM) pools (such as different fee tiers or dynamic fee hooks) by computing empirical loss metrics from public on-chain transaction tapes (e.g. calculating loss-versus-rebalancing, LVR, or loss-per-unit-service referenced against centralized exchange trade prices).

Wang (`arXiv:2609.19013v1`) establishes that this standard empirical ranking practice is fundamentally flawed due to two distinct phenomena: **selection bias from programmable matching mechanisms** and **finite-tape sampling variation with temporal dependence**:
1. **Programmable Matching as a Selection Filter:**
   - A dynamic-fee AMM, routing rule, batch auction, or fee-tier pool does not merely quote a price; it selects which latent trading opportunities execute.
   - The public transaction tape records a selected subset of latent opportunities, recording prices, sizes, and execution marks only for executed swaps. Opportunities that an incumbent pool rejected, priced out, or routed away are absent.
   - Formally, the observed tape is a marked counting process $N_{\text{exec}}(dt, dm)$ adapted to filtration $\{\mathcal{F}_t\}$. Under the multiplicative-intensity framework of Aalen (1978) and Andersen et al. (1993), its compensator has the product form:
     $$\Lambda_{\text{exec}}(dt, dm) = e^{\pi_0(t, S_t, Z_{t-}, m)} \nu^\circ(dt, dm)$$
     where $\nu^\circ$ is the latent-opportunity compensator and $e^{\pi_0}$ is the incumbent mechanism's execution propensity.
   - The selected compensator reveals only the product $e^{\pi_0} \nu^\circ$, never the separate factors. Consequently, a pool may appear to have lower loss per unit service either because it executes with genuinely lower adverse selection, or simply because its fee/quote policy selectively filtered out toxic flow that a competing pool absorbed.
2. **Empirical Loss Marks vs. Canonical LVR:**
   - Canonical continuous-time LVR (Milionis et al. 2022) is the non-negative compensator of a committed quote schedule under a fixed execution rule.
   - The empirical mark on a public transaction tape is a *signed, trade-price-referenced execution loss*: $\ell = A - B$ with $A, B \ge 0$, where $A$ represents adverse execution (slippage against LP) and $B$ represents favorable fills. The empirical mark coincides with canonical LVR only in the passive, one-sided adverse-execution corner ($B \equiv 0$).
3. **Native Two-Tape Non-Identification (Proposition 2.1):**
   - Even at the population compensator level (infinite data, zero sampling noise), two structural models can generate identical executed-event laws, quantities, signed marks, and reference prices for two pools, yet imply opposite full-opportunity rankings ($\Delta_{12}^\star < 0$ in Model A vs $\Delta_{12}^\star > 0$ in Model B) due to unexecuted opportunities off selected support where $e_j = 0$.
4. **Sharp Signed Hidden-Mass Ranking Regions (Proposition 2.2):**
   - To bound unobserved opportunities, Wang defines a hidden-mass budget $r \in [0, \bar{r}]$ per unit observed mass, with severity envelope $\ell_H \in [\ell_{lo}, \ell_{hi}]$ and service envelope $s_H \in [s_{lo}, s_{hi}]$.
   - The sensitivity value is a linear-fractional map of observed and hidden components. For signed marks, the sharp identified set for the ranking contrast is a compact interval whose endpoints are attained at the finite corners of the parameter rectangle. A ranking is certified only when the entire projected confidence interval lies strictly on one side of zero.
5. **Inference via Synchronized Calendar Moving-Block Bootstrap (Theorem 3.1 & Corollary 3.2):**
   - Finite realized transaction sums fluctuate around the selected compensator as a square-integrable martingale. Because weekly loss increments are spike-dominated and temporally correlated, Wang introduces a synchronized calendar moving-block bootstrap (drawing identical week blocks across all pools and references).
   - Projecting the 6-dimensional studentized primitive confidence ellipsoid through the linear-fractional ratio bounds via Fieller's quadratic delivers simultaneous coverage without relying on invalid smooth delta methods at min/max kinks.

### Research interpretation

The proposed research thesis is an **empirical falsification of naive AMM pool performance rankings**:
- In quantitative crypto trading and liquidity provision, alpha is often sought by dynamically allocating capital across AMM fee tiers (e.g., migrating LP capital between 5bp and 30bp pools depending on volatility) or designing Uniswap v4 dynamic fee hooks to minimize LVR.
- These strategies rely on the premise that observed transaction tapes provide an identifiable signal of execution quality.
- Wang's theoretical and empirical results demonstrate that **empirical LVR rankings between Uniswap v3 fee tiers are statistically uncertifiable**:
  - In a 2-year empirical study of Uniswap v3 WETH-USDC (104 calendar weeks), the 5bp pool exhibits a lower point estimate of loss per service than the 30bp pool ($0.112$ vs $0.455$ on last-trade reference).
  - However, when evaluated under synchronized calendar moving-block bootstrap inference, the simultaneous 95% confidence interval for the ranking contrast spans $[-1.18, +0.65]$ at $r = 0$ (zero hidden mass).
  - Because zero is included in the 95% confidence set, the claim that the 5bp pool achieves superior loss-per-service execution is **statistically uncertifiable** even before admitting hidden unexecuted opportunities.
  - When hidden-mass sensitivity envelopes are admitted ($r > 0$), the confidence bounds expand further, confirming that public transaction tapes do not support causal fee-tier or mechanism rankings.
  - Furthermore, static replay of alternative fee policies on incumbent tapes suffers from substantial bias (Proposition A.1 proves a $-9.6\%$ bias on a 2-period CPMM), proving that dynamic counterfactuals require full closed-loop simulation rather than tape replay.

## Signal

The methodology defines an econometric certification protocol and decision rule for AMM pool ranking (Algorithm / Estimand):

### 1. State Variables & Observed Primitives (`source-reported`)
- **Observed Tape Primitives:** For pool $j \in \{1, 2\}$, let $N_{\text{exec}, j}$ be the counting process of executed swaps over horizon $[0, T]$. Observed additive primitives are collapsed to synchronized calendar-week increments $w \in \{1, \dots, W\}$:
  - Additive loss component: $\Theta_{L,j}^O = \sum_{w=1}^W \theta_{L,j,w}$, where $\theta_{L,j,w} = \sum_{i \in \text{swaps}_{j,w}} \ell_{j,i}$.
  - Additive service component: $\Theta_{S,j}^O = \sum_{w=1}^W \theta_{S,j,w}$, where $\theta_{S,j,w} = \sum_{i \in \text{swaps}_{j,w}} s_{j,i}$.
- **Signed Execution Loss Mark ($\ell_{j,i}$):**
  $$\ell_{j,i} = \delta_{j,i} \cdot (P_i - p_{\text{exec},j,i})$$
  where $\delta_{j,i}$ is swap direction ($+1$ for buyer of risky asset, $-1$ for seller), $P_i$ is the external CEX reference price at block arrival, and $p_{\text{exec},j,i}$ is the effective swap execution price. Decomposed into Jordan components $\ell = A - B$ ($A = \max(\ell, 0)$, $B = \max(-\ell, 0)$).
- **Service Mark ($s_{j,i}$):** Swap volume / size in numéraire units ($s_{j,i} = \delta_{j,i} \cdot p_{\text{exec},j,i}$ or base units).
- **Service Effective Sample Size:** $n_{\text{eff}, S} = (\sum q)^2 / \sum q^2$ (`source-reported`), serving as a weight-concentration diagnostic.

### 2. Ranking Estimand & Identified Set (`source-reported`)
- **Observed-Support Ratio:** $\bar{M}_j^O = \bar{\Theta}_{L,j}^O / \bar{\Theta}_{S,j}^O$.
- **Native Ranking Contrast:** $\Delta_{12}^\circ = \bar{M}_1^O - \bar{M}_2^O$.
- **Hidden-Opportunity Envelopes:**
  - Hidden mass ratio: $r \in [0, \bar{r}]$, evaluating grid $\bar{r} \in \{0.0, 0.1, 0.25, 0.5, 1.0\}$.
  - Hidden severity interval: $\ell_H \in [\ell_{lo}, \ell_{hi}]$.
  - Hidden service interval: $s_H \in [s_{lo}, s_{hi}]$.
- **Sharp Ranking Set ($I_\Delta(\bar{r})$):**
  $$I_\Delta(\bar{r}) = [\underline{M}_1 - \bar{M}_2, \, \bar{M}_1 - \underline{M}_2]$$
  where $\underline{M}_j, \bar{M}_j$ solve the corner extrema of linear-fractional map $M_j(r, \ell, s) = (\bar{L}_{j}^O + r \ell) / (\bar{S}_{j}^O + r s)$ over the 8 parameter corners.

### 3. Inference & Decision Logic (Algorithm 1) (`source-reported`)
1. **Synchronized Moving-Block Resampling:**
   - Partition $W = 104$ calendar weeks into overlapping blocks of length $b = \lceil \sqrt{W} \rceil = 11$ weeks (`source-reported`).
   - Draw $B = 999$ bootstrap replicates applying identical block indices to both pools and external references (`source-reported`).
2. **Primitive Ellipsoid Construction (Theorem 3.1):**
   - Form studentized primitive confidence region:
     $$R_T = \left\{ \theta \in \mathbb{R}^6 : (\hat{\theta} - \theta)' \hat{V}_T^{-1} (\hat{\theta} - \theta) \le c_{\alpha,T}^* \right\}$$
     at confidence level $1 - \alpha = 0.95$ (`source-reported`).
3. **Region-Wise Denominator Positivity Screen (Condition 1):**
   - Compute $\inf_{\theta \in R_T, r \in [0, \bar{r}], s \in [s_{lo}, s_{hi}]} \{ \bar{S}_O(\theta) + r s \}$.
   - If $\le 0$, emit `abstain: positivity-limited` (`source-reported`).
4. **Fieller Projection for Ranking Set (Corollary 3.2):**
   - Solve Fieller quadratic roots for ratio extrema over ellipsoid $R_T$.
   - Obtain projected simultaneous ranking interval $[\underline{\Delta}_{12}, \bar{\Delta}_{12}]$.
5. **Decision Output (`source-reported`):**
   - If $\bar{\Delta}_{12} < 0 \implies$ **Sign-certified negative** (Pool 1 has strictly lower loss per service).
   - If $\underline{\Delta}_{12} > 0 \implies$ **Sign-certified positive** (Pool 1 has strictly higher loss per service).
   - If $0 \in [\underline{\Delta}_{12}, \bar{\Delta}_{12}] \implies$ **Not sign-certified** (Contrast straddles zero; ranking is unprovable).

### 4. Operational Parameters
- Evaluation horizon: 2024-01-01 to 2025-12-27 (104 calendar weeks) (`source-reported`).
- Confidence level: $1 - \alpha = 0.95$ (`source-reported`).
- Moving-block length: $b = 11$ weeks (`source-reported`).
- Bootstrap iterations: $B = 999$ (`source-reported`).
- Minimum TVL inclusion filter for candidate pools: $10,000,000 USD (`research-proposed`).
- Maximum portfolio capital allocation per AMM pool: 25% of total liquidity budget (`research-proposed`).
- Minimum weekly trading volume threshold: $50,000,000 USD (`research-proposed`).

## Required data

- **Instruments / Pools (`source-reported`):**
  - Uniswap v3 WETH-USDC 5bp (0.05% fee tier, pool contract `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640`).
  - Uniswap v3 WETH-USDC 30bp (0.30% fee tier, pool contract `0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8`).
  - Blockchain: Ethereum Mainnet.
- **On-Chain Transaction Data (`source-reported`):**
  - Event log: Uniswap v3 `Swap(address sender, address recipient, int256 amount0, int256 amount1, uint160 sqrtPriceX96, uint128 liquidity, int24 tick)`.
  - Block header data: exact Ethereum block numbers and block timestamps (nanosecond hardware/RPC precision).
- **External CEX Reference Data (`source-reported`):**
  - Primary reference: Binance Spot ETHUSDC `aggTrades` tick stream (`trade_id`, `price`, `quantity`, `trade_time`).
  - Last-trade rule: strictly pre-block trade (last trade prior to Ethereum block timestamp).
  - Secondary reference: strictly pre-block 1-second VWAP over Binance aggTrades stream.
- **Point-in-Time Availability (`source-reported`):**
  - Block-level matching convention: all swaps within Ethereum block $b$ are referenced strictly to CEX trades timestamped $t < t_{\text{block}, b}$, eliminating look-ahead bias.
- **Missing Data & Staleness Handling (`source-reported`):**
  - Reference staleness $q_{99} \approx 44$ seconds over the full 2-year sample (driven by thin liquidity in early 2024).
  - Any RPC desynchronization, reorg, or missing trade data window requires invalidating the affected calendar week (`research-proposed`).

## Execution assumptions

- **Order Types (`source-reported`):** Realized on-chain AMM swaps executed by market participants (aggregators, retail traders, MEV searchers).
- **Execution Mechanism (`source-reported`):** Deterministic execution along the constant-product virtual reserve curve within Uniswap v3 tick ranges.
- **Latency & Matching Model (`source-reported`):** Pre-block reference convention. Trades within a block execute at discrete transaction index order within Ethereum execution blocks.
- **Transaction Fees & Gas (`source-reported`):**
  - Pool fees (5bp vs 30bp) deducted proportionally from input token.
  - Gas fees (EIP-1559 base fee + priority tip) paid by swap initiator; excluded from LP loss mark calculation.
- **Slippage & Impact Model (`source-reported`):** Endogenous price impact governed by pool concentrated liquidity depth profile $L(t, i)$.
- **Margin & Shorting (`research-proposed`):** Unleveraged liquidity provision in native tokens (WETH, USDC); zero borrowing or debt liquidation risk on-chain.

## Evidence

### Source-reported

All empirical figures below trace directly to Wen-Ting Wang (`arXiv:2609.19013v1`, Section 4, Table 1, Section 5, and Figures 1–2):

1. **Two-Year Uniswap v3 WETH–USDC Empirical Evaluation (Section 5.1):**
   - **Sample Window:** 2024-01-01 to 2025-12-27 (104 calendar weeks).
   - **Pool Statistics:**
     - 5bp pool: Observed loss-per-service $M^\circ = 0.112$ (last-trade reference) and $0.463$ (1s-VWAP reference); service effective sample size $n_{\text{eff}, S} = 3.2 \times 10^5$.
     - 30bp pool: Observed loss-per-service $M^\circ = 0.455$ (last-trade reference) and $0.878$ (1s-VWAP reference); service effective sample size $n_{\text{eff}, S} = 4.7 \times 10^4$.
   - **Naive Point Estimate Contrast:**
     - $\Delta_{12}^\circ = M^\circ(5\text{bp}) - M^\circ(30\text{bp}) = 0.112 - 0.455 = -0.343$ (last-trade reference).
     - $\Delta_{12}^\circ = 0.463 - 0.878 = -0.415$ (1s-VWAP reference).
     - Under naive point comparison, the 5bp pool appears to deliver substantially lower loss per service than the 30bp pool.
   - **Statistical Certification Test Results:**
     - At $r = 0$ (zero hidden mass admitted), the synchronized calendar moving-block simultaneous 95% confidence region for $\Delta_{12}^\circ$ is:
       $$\Delta_{12}^\circ \in [-1.18, \, +0.65]$$
     - **Empirical Falsification Finding:** The 95% confidence interval contains zero (upper bound $+0.65 > 0$). The point ordering is **not sign-certified**.
     - As hidden-mass budget $r$ increases ($r \in \{0.1, 0.25, 0.5, 1.0\}$), the confidence region expands monotonically and continues to straddle zero under both external trade references.
     - Positivity screen: $\inf \{ \bar{S}_O + r s \} > 0$ holds across all tested envelopes; the failure to certify is driven by weekly sampling variance, not denominator degeneracy.

2. **Numerical Simulation Benchmark Results (Section 4.2, Table 1 & Figure 1):**
   - Evaluated on calibrated marked Cox point process over 1,000 Monte Carlo replications and 999 bootstrap draws:
     - Finite-output coverage of full method: **0.993 to 0.998** across regular primary cells (exceeding nominal 0.95).
     - False-sign rate in zero-straddling and branch-switching cells: **0.000**.
     - Plug-in endpoint bootstrap competitor undercovers severely: empirical coverage drops to **0.862–0.899** in hidden-breakdown and common-tail cells.
     - Hidden-breakdown cell: True frontier at $r^\star = 0.33036$. Full method correctly certifies negative ranking at $r = 0$ and $r = 0.25$, and correctly withdraws certification (abstains) at $r = 0.5$ and $r = 1.0$.
     - Denominator-crossing cell: Full method returns positivity-limited abstention with probability **0.990**.

3. **Dynamic Boundary Bias (Proposition A.1):**
   - On a two-period CPMM environment with full opportunity logging, static replay of alternative policy $\pi_1$ on the incumbent path yields frozen-state benchmark $M_{\text{FS}}^{0 \to 1} = 432729 / 190076 \approx 2.2766$, whereas the true dynamic oracle is $M^\circ(\pi_1) = 27 / 13 \approx 2.0769$.
   - Static tape replay induces an exact **$-9.6\%$ error**, proving that transaction tapes cannot evaluate counterfactual dynamic mechanisms without closed-loop trajectory simulation.

### Independently reproduced

`Not independently reproduced.` All empirical metrics, confidence bounds, effective sample sizes, and simulation results cited above reflect third-party findings reported by Wen-Ting Wang (`arXiv:2609.19013v1`) and verified against public repository `egpivo/amm-lab` at commit `f37ee93b80ac6e19088180f3ce3393e3fb68ecbd`. No independent replication on raw Ethereum RPC archive nodes or Binance tick databases has been completed in this research stack.

### Negative evidence

- **Empirical LVR Comparisons Fail Significance:** The widespread industry assumption that AMM fee tiers or hook policies can be reliably ranked in adverse selection cost using public transaction tapes is refuted: the simultaneous 95% confidence region for WETH-USDC 5bp vs 30bp spans $[-1.18, +0.65]$, proving zero statistical certainty.
- **Reference Staleness:** Binance Spot ETHUSDC last-trade $q_{99}$ staleness reached 44 seconds during early 2024, introducing substantial measurement noise into public-trade loss marks.
- **Dynamic Policy Counterfactual Failure:** Static tape replay is formally invalid for evaluating alternative fee or hook policies, exhibiting a $-9.6\%$ structural bias even in idealized two-period CPMM settings.

## Falsification plan

To falsify the conclusion of non-certification (i.e. to prove that an AMM pool ranking *can* be certified), the following empirical tests are specified:

1. **Sub-Second CEX Order-Book Midpoint Test (`research-proposed`):**
   - *Data:* Replace Binance Spot aggTrades with L2/L3 order-book midpoints sampled at 100ms intervals from multiple venues (Binance, Coinbase, OKX).
   - *Sample:* Rolling 52-week window on WETH-USDC and WBTC-USDC.
   - *Falsification Criterion (`research-defined falsification threshold`):* If the synchronized moving-block 95% confidence interval for $\Delta_{12}^\circ$ strictly excludes zero with an upper bound $\le -0.05$ under $r = 0$, the thesis that public-tape ranking variance prevents certification is falsified.
2. **Mempool Opportunity Census Audit (`research-proposed`):**
   - *Data:* Full Ethereum P2P mempool transaction feed capturing all unexecuted / dropped / replaced swap intents.
   - *Falsification Criterion (`research-defined falsification threshold`):* If the empirical hidden-mass ratio $r$ can be bounded below $0.01$ and the projected identified set strictly excludes zero, the non-identification barrier is overcome.
3. **Cross-Pair Consistency Test (`research-proposed`):**
   - *Universe:* Top 10 Uniswap v3 pairs by volume (WETH-USDT, WBTC-USDC, ARB-USDC, etc.).
   - *Action on Failure (`research-defined falsification threshold`):* If $> 80\%$ of liquid pairs exhibit ranking intervals containing zero, retain the null hypothesis that empirical tape rankings cannot guide capital allocation across fee tiers.

## Crypto portability

- **Direct.** The empirical investigation, mathematical derivations, and reference implementation are natively designed for cryptocurrency Automated Market Makers (Uniswap v3 on Ethereum Mainnet) and CEX-DEX arbitrage dynamics.
- **Protocol Portability:**
  - Directly applicable to Uniswap v3, Uniswap v4 (hooks), Curve, Balancer, and PancakeSwap pools.
  - Applicable to Solana CLMMs (Raydium, Orca Whirlpools) with slot-time adjustments.
- **Crypto-Specific Structural Factors:**
  - Block-time quantization: Ethereum 12-second block slots create discrete temporal aggregation where all intra-block swaps share identical pre-block CEX references.
  - MEV and Priority Gas Auctions: Searcher bundles dominate toxic swap flow; unexecuted bundles dropped by builders constitute significant hidden opportunity mass.

## Limitations

- **Observability Gap for Hidden Flow:** Transaction tapes identify only $e^{\pi_0} \nu^\circ$; without full mempool capture or structural demand modeling, the true latent opportunity intensity $\nu^\circ$ remains partially identified.
- **Reference Price Proxy Quality:** External CEX trades represent discrete transactions rather than the continuous true marginal price, contributing to estimation variance.
- **Weekly Block Sample Size:** 104 calendar weeks provide only $W = 104$ effective temporal observations; expanding sample size requires multi-year historical data across evolving fee regimes.
- **No Direct Directional Alpha:** This research provides an econometric falsification framework rather than an active trading alpha signal; it prevents misallocation of capital to spurious AMM fee-tier arbitrage.

## Implementation status

- `not-implemented`. Prototype-only implementation exists in the author's public repository `egpivo/amm-lab` (Rust 2024 / Python), but no components have been integrated into our research stack.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures external quantitative research for knowledge base ingestion. It does not authorize capital deployment, paper trading, testnet, or live trading execution.

## Related Wiki records

- `[[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]` — Milionis et al. (2022): Canonical theoretical continuous-time LVR formulation.
- `[[quant/amm-lvr-jump-floor-optimal-block-time-2026-09-08]]` — Optimal block time and LVR jump floor under discrete latency.
- `[[quant/optimal-dynamic-fee-amm-pro-cyclical-lvr-volatility-feedback-2026-09-09]]` — Dynamic fee formulas for AMM adverse selection mitigation.
- `[[quant/defi-concentrated-liquidity-amm-dynamic-fee-staleness-proxy-lvr-compensation-2026-09-02]]` — Concentrated liquidity dynamic fee staleness proxies.
- `[[quant/polymarket-protocol-finality-redemption-latency-carry-arbitrage-falsification-2026-09-16]]` — Nechepurenko (2026): Empirical settlement latency and carry falsification.

## Sources

1. **Wen-Ting Wang**, *"Policy-Selected Transaction Tapes in Automated Market Makers: Ranking Certification under Hidden Opportunities"*, arXiv preprint `arXiv:2609.19013v1 [q-fin.ST, stat.ME]`, submitted September 17, 2026.
   - Stable URL: https://arxiv.org/abs/2609.19013
   - Full-Text HTML: https://arxiv.org/html/2609.19013v1
   - Full-Text PDF: https://arxiv.org/pdf/2609.19013v1
   - DOI: [10.48550/arXiv.2609.19013](https://doi.org/10.48550/arXiv.2609.19013)
2. **Wen-Ting Wang**, *"amm-lab"*, GitHub repository commit `f37ee93b80ac6e19088180f3ce3393e3fb68ecbd`, September 2026.
   - Repository URL: https://github.com/egpivo/amm-lab
   - Relevant paths: `src/pstt/` (`application.rs`, `bootstrap.rs`, `projection.rs`, `marks.rs`, `sensitivity.rs`), `tests/pstt_*.rs`, `scripts/lvr/`.
