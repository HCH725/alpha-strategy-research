---
schema: strategy-research-record-v1
title: Crypto AMM Private Mempool Exact Leakage Thresholds for Robust Sandwich Attacks and Slot Auction Extraction (arXiv:2609.31379)
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto-amm
  - mev
  - sandwich-attacks
  - private-mempool
  - execution-auction
status: research-only
confidence: high
source_as_of: 2026-09-25
sources:
  - "arXiv:2609.31379v1 [cs.GT, cs.CR, q-fin.TR], https://arxiv.org/abs/2609.31379 (landing page read 2026-09-28; full-text HTML https://arxiv.org/html/2609.31379v1 read 2026-09-28; primary LaTeX source bundle https://arxiv.org/src/2609.31379 downloaded and unpacked 2026-09-28, toplevel mev_leakage_thresholds.tex 63517 bytes, checklist_mev_leakage_thresholds.tex 25539 bytes; pinned PDF 23 pages, 349300 bytes, SHA-256 9a7cf478be900bfa82972194c8806813b2a1ee45ab5c94c43cb91bcce9761b31, retrieved 2026-09-28; DataCite DOI: 10.48550/arXiv.2609.31379; license CC BY 4.0; publication status: accepted to NeurIPS 2026)"
  - "Canonical schema: Hermes Wiki Brain quant/strategy-research-record-spec-v1.md (10289 bytes, SHA-256 4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7, read 2026-09-28) plus repository README.md workflow contract."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto AMM Private Mempool Exact Leakage Thresholds for Robust Sandwich Attacks and Slot Auction Extraction (arXiv:2609.31379)

## Provenance

**Source identity.** arXiv preprint `arXiv:2609.31379v1 [cs.GT]`, cross-listed to `cs.CR` and `q-fin.TR`. Canonical landing URL: `https://arxiv.org/abs/2609.31379`. Canonical DOI: `https://doi.org/10.48550/arXiv.2609.31379` (DataCite, pending registration). Title: "How Much Must a Private Mempool Hide? Exact Leakage Thresholds for Sandwich Attacks".

**Authors (verbatim from LaTeX source).** Tingyi Lin ($^{1\dagger}$), Jiazhuo Li ($^{2}$), Ruoran Lai ($^{3}$), with affiliations:
- $^{1}$ Adrasteia Labs;
- $^{2}$ University of Michigan;
- $^{3}$ Sun Yat-sen University;
- Correspondence: `tingyi3@illinois.edu`.

**Dates & versioning.** Submission history on arXiv landing: `[v1] Fri, 25 Sep 2026 15:15:24 UTC (70 KB)`, submitted by Jiazhuo Li; announced on arXiv: `Mon, 28 Sep 2026`. `source_as_of` is set to the immutable submission date `2026-09-25`. Exactly one version exists on arXiv.

**Publication status.** Comments field on arXiv landing: "23 pages, 1 figure, 1 table. Accepted to NeurIPS 2026". The LaTeX source file `mev_leakage_thresholds.tex` includes `\usepackage[main,final]{neurips_2026}` and `checklist_mev_leakage_thresholds.tex`. License: Creative Commons Attribution 4.0 International (`CC BY 4.0`).

**Pinned primary source artifacts (verified in this run).**
1. Official arXiv LaTeX source bundle retrieved from `https://arxiv.org/src/2609.31379`: gzipped tarball unpacked to `mev_leakage_thresholds.tex` (63,517 bytes, 1,494 lines), `checklist_mev_leakage_thresholds.tex` (25,539 bytes, 225 lines), `threshold_and_bits.pdf` (41,588 bytes), `neurips_2026.sty` (13,462 bytes), `00README.json` (231 bytes).
2. Pinned PDF retrieved directly from `https://arxiv.org/pdf/2609.31379`: 23 pages, 349,300 bytes, SHA-256 `9a7cf478be900bfa82972194c8806813b2a1ee45ab5c94c43cb91bcce9761b31` (verified with `pypdf 6.16.2` to have exactly 23 pages).
3. Full-text HTML read directly at `https://arxiv.org/html/2609.31379v1` (152,844 bytes, 2,520 lines).

**Pre-write deterministic deduplication (whole checkout, hidden-inclusive).**
- Whole-repository search (`rg -uuu` and `grep -rn`) across all tracked `*.md` (over 1,000 files) and `coverage_manifest.csv` returned zero hits for: `2609.31379`, `10.48550/arXiv.2609.31379`, "How Much Must a Private Mempool Hide", "Tingyi Lin", "Jiazhuo Li", "Ruoran Lai", "Adrasteia Labs", and "leakage thresholds for sandwich attacks".
- Four-axis distinction from adjacent MEV / AMM records in the repository:
  1. Versus `crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01.md`: That record models LP mint/burn liquidity concentration on Uniswap v3 fee tiers; this record characterizes discrete interval-leakage thresholds for front-run / back-run sandwich attacks under constant-product AMM mechanics.
  2. Versus `crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31.md`: That record measures continuous-time Black-Scholes toxic flow loss-versus-rebalancing (LVR) by external arbitrageurs; this record solves the finite-interval coarse-leakage sandwich problem and execution-slot auction rent capture.
  3. Versus `cross-chain-agent-mev-arbitrage-adaptive-path-selection-2026-09-17.md`: That record optimizes multi-hop cyclical routing across heterogeneous L1/L2 bridges; this record derives exact closed-form scalar thresholds on single-pool CPMMs.
  4. Versus `crypto-cex-dex-priority-fee-stochastic-delay-mixed-control-2026-09-01.md`: That record studies continuous stochastic delay and priority fee escalation between CEX and DEX; this record analyzes Bayesian game-theoretic first-price slot auctions with complete searcher rent dissipation.

## Economic mechanism

### Source-reported

1. **Constant-Product Sandwich Anatomy:**
   - In a constant-product automated market maker ($XY = k$, Uniswap v2 invariant), an input of $\delta > 0$ units of token $X$ returns output $\Delta_Y(\delta; X, Y) = \frac{Y\delta}{X+\delta}$ and updates reserves to $(X+\delta, XY/(X+\delta))$. Conversely, an input of $\eta > 0$ units of token $Y$ returns $\Delta_X(\eta; X', Y') = \frac{X'\eta}{Y'+\eta}$ (Section 3.1, Eqs. 1-2).
   - A victim transaction inputs hidden size $q > 0$ of token $X$ to buy token $Y$, with honest output $h(q) = \frac{Yq}{X+q}$ and public slippage tolerance $\tau \in (0, 1)$, requiring minimum output $(1-\tau)h(q)$ (Eqs. 3-4).
   - A front-run of size $a \ge 0$ acquires $y_F(a) = \frac{Ya}{X+a}$ of token $Y$. The victim then receives $v(a, q) = \frac{XYq}{(X+a)(X+a+q)}$ (Eqs. 5-6).
   - The front-run is admissible for victim type $q$ if and only if $v(a, q) \ge (1-\tau)h(q)$ (Definition 3.1).
   - When the searcher unwinds by selling $y_F(a)$ back to the pool after the victim trade, it receives $x_B(a, q) = \frac{a(X+a+q)^2}{(X+a)^2+aq}$ (Eq. 7).
   - Gross sandwich profit in token $X$ is $\pi(a, q) = x_B(a, q) - a = \frac{aq(2X+a+q)}{(X+a)^2+aq}$, which is strictly independent of the reserve level $Y$ (Eq. 8).

2. **The Partial Observability / Leakage Problem:**
   - In private mempools (e.g., Ferveo, Shutter Network, MEV-Share, SUAVE), transactions are shielded, but metadata leaks: the token pair, direction ($X \to Y$), and an interval containing the victim's trade size $I_s = [\ell_s, u_s]$ (with $\ell_s > 0$) or half-open $(0, u_s]$ (with $\ell_s = 0$) are publicly observable (Definition 3.2).
   - Robust admissibility requires that the front-run size $a \ge 0$ must guarantee execution for *every* possible victim size $q \in I_s$ (Definition 3.3). If a front-run causes the victim order to revert for even one consistent size $q$, it is inadmissible.

3. **Lower-Endpoint Monotonicity & Dominance:**
   - **Relative-output monotonicity (Lemma 5.1):** For fixed $a > 0$, the ratio $r(a, q) = \frac{v(a, q)}{h(q)} = \frac{X(X+q)}{(X+a)(X+a+q)}$ is strictly increasing in $q > 0$. Small victim orders suffer the greatest percentage price impact! Consequently, the slippage guard $(1-\tau)$ binds strictly at the smallest consistent victim size $\ell_s$.
   - **Profit monotonicity (Lemma 5.2):** Sandwich gross profit $\pi(a, q)$ is strictly increasing in $a > 0$ and in $q > 0$.
   - **Simultaneous Optimality (Theorem 4.2):** Because profit rises with $a$, the maximal robustly admissible front-run $a^\star(I) = a_{\max}(\ell_s, \tau)$ simultaneously uniquely maximizes pointwise profit for every fixed $q$, posterior expected profit $\mathbb{E}_{q \sim \mu}[\pi(a, q)]$, and worst-case profit $\min_{q \in I}\pi(a, q)$.
   - **Exact worst-case gross profit (Theorem 4.2(c), Eq. 12):**
     $$W(I) = \pi(a^\star(I), \ell_s) = \frac{\tau \ell_s (X+\ell_s)}{X + \tau \ell_s}$$

4. **Closed-Form Leakage Threshold:**
   - With fixed execution cost $c \ge 0$, a robustly admissible bundle with strictly positive net profit for *every* consistent victim size $q \in I$ exists if and only if $W(I) > c$, which holds if and only if the leaked lower bound strictly exceeds (Theorem 4.3, Eq. 14):
     $$\ell_s > \lambda_c := \frac{-(X-c) + \sqrt{(X-c)^2 + \frac{4cX}{\tau}}}{2}$$
   - The threshold depends only on input reserve $X$, slippage tolerance $\tau$, and execution cost $c$. The upper bound $u_s$ is economically irrelevant to riskless front-running.
   - To first order in $\widehat{c} = c/X$, the dimensionless threshold is $\widehat{\lambda} = \lambda_c/X = \frac{\widehat{c}}{\tau} + O(\widehat{c}^2)$ (Proposition 6.6).

5. **Execution Auction Rent Dissipation:**
   - In a first-price execution slot auction among $m \ge 2$ symmetric risk-neutral searchers with cost $c$: If posterior continuation rent $R_s = V_{\mu_s}(I_s) - c > 0$, every pure-strategy perfect Bayesian equilibrium (PBE) awards the slot to front-run $a^\star(I_s)$ at bid $b^\star_s = R_s$. Searchers earn 0 economic profit; the auctioneer (block builder / sequencer) captures 100% of the expected net rent (Theorem 4.5). If $R_s < 0$, no equilibrium places a sandwich.

6. **Metadata Boundaries:**
   - Direction ambiguity (Proposition 6.4): If trade direction is concealed ($X \to Y$ vs $Y \to X$), no non-null first leg can front-run both directions simultaneously.
   - Swap fees (Proposition 6.7): A swap fee withheld from reserves ($\rho \in [0, 1)$) strictly reduces sandwich gross profit, making the fee-free threshold $\lambda_c$ a conservative lower bound.
   - Post-trade arbitrage (Proposition 4.7): Perfect pre-trade hiding eliminates sandwich attacks, but post-trade arbitrage still extracts gross profit up to $\frac{q^2}{X+q}$ by rebalancing against external market prices.

### Research interpretation

- **Hypothesized mechanism (falsifiable form):** Asymmetric informational barrier in decentralized order flow. Because price impact on constant-product curves is convex, small orders suffer greater relative displacement than large orders. Therefore, riskless front-running is governed strictly by the infimum of the adversary's information set ($\ell_s$). If a private mempool reveals an upper bound $u_s$ or coarse bins without a lower bound above $\lambda_c$, riskless extraction is mathematically impossible.
- **Component roles in quantitative research:**
  - `Regime filter: Check \ell_s > \lambda_c (only proceed when lower bound clears the execution cost threshold)`.
  - `Primary signal: Directional mempool interval leak I_s = [\ell_s, u_s] on CPMM pool (X, Y)`.
  - `Front-run sizing: a^\star = a_{\max}(\ell_s, \tau) (strictly bounded by lower endpoint \ell_s)`.
  - `Auction pricing: b^\star = \mathbb{E}_{\mu_s}[\pi(a^\star, q)] - c (Bertrand bid ceiling)`.
  - `Exit: Atomic same-block unwind x_B immediately following victim execution`.
- **What this record is *not*:** It is not an authorization to deploy predatory MEV bots, not an endorsement of front-running, and not evidence of positive searcher alpha in competitive block building. Under Theorem 4.5, open competition among searchers drives net profits to zero, transferring all surplus to block builders and sequencers.

## Signal

The trading signal and optimal bundle construction are fully specified mathematically by the primary source:

- **Signal formation timestamp:** Triggered at the arrival of a coarse-leakage signal $s = L(q)$ from a private mempool, exposing interval $I_s = [\ell_s, u_s]$ with $\ell_s > 0$, public slippage tolerance $\tau \in (0, 1)$, and trading direction $X \to Y$ on pool $(X, Y)$.
- **Pre-execution feasibility filter (source-specified):** Evaluate the exact leakage threshold:
  $$\lambda_c = \frac{-(X-c) + \sqrt{(X-c)^2 + \frac{4cX}{\tau}}}{2}$$
  where $c$ is the fixed execution cost.
  - If $\ell_s \le \lambda_c$: Submit null action (do not attack; no guaranteed-profitable robust sandwich exists).
  - If $\ell_s > \lambda_c$: Proceed to bundle construction.
- **Front-run sizing $a^\star$ (source-specified):** Submit front-run buy of size $a^\star = a_{\max}(\ell_s, \tau)$ in token $X$:
  $$a^\star = \frac{-(2X+\ell_s) + \sqrt{(2X+\ell_s)^2 + \frac{4\tau X(X+\ell_s)}{1-\tau}}}{2}$$
- **Back-run unwind sizing (source-specified):** Sell all acquired token $Y$ output $y_F(a^\star) = \frac{Y a^\star}{X + a^\star}$ back to the pool immediately after the victim transaction.
- **Auction bid pricing (source-specified):** Under posterior distribution $\mu_s$ over $q \in I_s$, submit auction payment bid:
  $$b^\star_s = \mathbb{E}_{q \sim \mu_s}\left[\frac{a^\star q (2X + a^\star + q)}{(X + a^\star)^2 + a^\star q}\right] - c$$
- **Holding period:** Zero blocks / atomic intra-block sequence (Searcher Front-run $\to$ Victim Swap $\to$ Searcher Back-run).
- **Execution window:** Single slot / block.
- **Research-proposed operational rules (NOT specified by source):**
  - Estimating the prior/posterior distribution $\mu_s$ over $I_s$ (e.g., power-law or empirical DEX trade-size distribution) is `research-proposed`.
  - Priority fee bidding ladders in asynchronous builder auctions (e.g., bid increments $\Delta b$) are `research-proposed`.
  - Dynamic base-fee gas buffers ($c = 1.2 \times \text{estimated gas cost}$) are `research-proposed`.

## Required data

- **Instrument / universe:** Decentralized automated market maker (DEX) liquidity pools operating under constant-product pricing ($XY = k$), such as Uniswap v2, SushiSwap, PancakeSwap, Base Swap.
- **Market type:** On-chain spot AMM liquidity pools.
- **Venue:** EVM-compatible blockchains (Ethereum mainnet, Arbitrum, Base, Optimism, BNB Chain).
- **Timeframe:** Event-driven, mempool transaction-level arrival.
- **Fields required:**
  - On-chain pool reserves $(X, Y)$ at the current pending block state.
  - Leaked mempool signal: contract address pair, swap direction ($X \to Y$), victim slippage tolerance $\tau$, size interval bounds $[\ell_s, u_s]$.
  - Gas fee metrics: base fee, priority fee, gas limit for front-run + back-run execution.
- **Point-in-time / availability:** Pre-confirmation mempool stream. Must be received and processed before block builder packaging cutoffs.
- **Missing-data handling:** If $\ell_s$ cannot be established (half-open interval $(0, u_s]$ where $\ell_s = 0$), $W(I) = 0$; with $c > 0$, no robust bundle exists -> fail closed, emit null action.
- **Cost / fee needs:** Execution cost $c$ represents the total gas cost of the two searcher transactions in units of token $X$. Swap fee rate $\rho$ (e.g., 30 bps on Uniswap v2) is incorporated via Proposition 6.7.

## Execution assumptions

- **Order type:** Atomic multi-transaction bundle submitted to a block builder or validator (e.g., Flashbots builder, Titan, BeaverBuild, MEV-Boost).
- **Fill model:** Deterministic EVM execution: all transactions in the bundle execute sequentially without intervening transactions. If the victim reverts, the bundle reverts atomically.
- **Latency / signal delay:** Sub-second execution rights bidding (typically $100\text{ ms} - 500\text{ ms}$ before block proposal).
- **Slippage & price impact:** Fully endogenous to the AMM reserve invariant; victim slippage tolerance $\tau$ enforced by smart contract revert.
- **Funding / leverage / borrow:** None; this is a spot AMM reordering mechanism without debt, funding rates, or margin.
- **Capital requirements:** Searcher must hold at least $a^\star$ units of token $X$ for the duration of the atomic transaction (flash loans permitted if flash-loan fee $\le W(I) - c$).
- **What source assumes vs what we assume:** Source assumes an exact known cost $c$, fee-free AMM, and risk-neutral symmetric searchers. Practical adaptations for variable base fees and swap fee schedules ($\rho = 0.003$) are `research-proposed`.

## Evidence

### Source-reported

All quantitative values and mathematical propositions below are `source-reported` from the primary paper (`arXiv:2609.31379v1` / `mev_leakage_thresholds.tex`):

1. **Exact Robust Admissibility (Theorem 4.1):**
   - For interval $I = [\ell, u] \subseteq (0, Q]$, admissible set is $\mathcal{A}(I) = [0, a_{\max}(\ell, \tau)]$ with root:
     $$a_{\max}(\ell, \tau) = \frac{-(2X+\ell) + \sqrt{(2X+\ell)^2 + \frac{4\tau X(X+\ell)}{1-\tau}}}{2}$$
   - For half-open interval $(0, u]$, admissible set is $[0, a_0]$ where $a_0 = X((1-\tau)^{-1/2} - 1)$.
2. **Exact Worst-Case Value (Theorem 4.2):**
   - $W(I) = \frac{\tau \ell (X+\ell)}{X + \tau \ell}$.
3. **Exact Leakage Threshold (Theorem 4.3):**
   - Universal robust profitability requires $\ell > \lambda_c = \frac{-(X-c) + \sqrt{(X-c)^2 + \frac{4cX}{\tau}}}{2}$.
4. **Dimensionless Threshold Calibrations (Table 1, source-reported):**
   Values of $\lambda_c/X$ across relative costs $c/X$ and slippage tolerances $\tau$:
   - For $c/X = 10^{-6}$: $\tau = 0.001 \to 0.00100$; $\tau = 0.005 \to 0.00020$; $\tau = 0.01 \to 0.00010$; $\tau = 0.02 \to 0.00005$.
   - For $c/X = 10^{-5}$: $\tau = 0.001 \to 0.00990$; $\tau = 0.005 \to 0.00200$; $\tau = 0.01 \to 0.00100$; $\tau = 0.02 \to 0.00050$.
   - For $c/X = 10^{-4}$: $\tau = 0.001 \to 0.09162$; $\tau = 0.005 \to 0.01962$; $\tau = 0.01 \to 0.00990$; $\tau = 0.02 \to 0.00498$.
5. **Numerical Example 6.8 (source-reported):**
   - Parameters: $X = 10^6$, $\tau = 0.02$, $c = 100 \implies c/X = 10^{-4}$.
   - Calculated threshold: $\lambda_c/X \approx 0.0049757 \implies \lambda_c \approx 4,976$.
   - A leaked lower bound of a few hundred units does not support a profitable robust sandwich; a leaked lower bound around $5 \times 10^3$ crosses the threshold.
6. **Bit-Prefix Leakage (Proposition 4.6, Figure 1):**
   - If the first $d$ bits leak on $(0, Q]$, dyadic intervals $I_j = [jQ/2^d, (j+1)Q/2^d]$ for $j \ge 1$ admit a universally profitable sandwich iff $jQ/2^d > \lambda_c$. Bin $I_0 = (0, Q/2^d]$ never supports a universal sandwich when $c > 0$.
7. **Execution Slot Auction Extraction (Theorem 4.5):**
   - For $m \ge 2$ symmetric searchers, equilibrium payment is $b^\star_s = R_s$. Auctioneer extracts 100% of expected net rent; searcher net profit is 0.
8. **Positive Swap Fees (Proposition 6.7):**
   - Fee rate $\rho \in [0, 1)$ strictly reduces sandwich gross profit; the fee-free threshold $\lambda_c$ is a conservative lower bound.
9. **Post-Trade Arbitrage (Proposition 4.7):**
   - Even with perfect pre-trade hiding, post-trade arbitrage captures gross profit up to $\frac{q^2}{X+q}$.
10. **Empirical Literature Context (Section 1, Section 2):**
    - The paper cites external empirical studies documenting sandwich prevalence: McLaughlin et al. (USENIX Security 2023) identify 63,257 sandwich attacks among apparent arbitrages; Bai et al. (Discover Computing 2025) detect 60,946 sandwich events across 210,000 Ethereum blocks.

### Independently reproduced

`Not independently reproduced.` The mathematical derivations in the paper have not been executed or independently verified in our research code stack.

### Negative evidence

1. **Complete Searcher Rent Dissipation:** Under competitive PBS execution auctions (Theorem 4.5), searcher profits are driven to zero. Without an informational or latency monopoly, running this strategy produces zero net alpha for an independent fund.
2. **Swap Fees Increase Threshold:** Uniswap v2 charges a 30 bp fee ($\rho = 0.003$) on each leg. Proposition 6.7 proves gross profit is strictly lower with fees, so the real-world threshold $\lambda_{c, \rho}$ is strictly higher than $\lambda_c$.
3. **Uniswap v3 Multi-Tick Liquidity Disruption:** Real DEX volume is concentrated on Uniswap v3/v4. Remark 6.10 confirms that when trade size crosses an initialized tick, active liquidity $\Lambda$ changes, breaking the closed-form single-scalar threshold.
4. **Revert Risk Under State Contention:** If competing transactions alter pool reserves before bundle execution, the front-run may cause the victim to revert, wasting gas.
5. **Direction Privacy Defeats the Attack:** If the mempool hides direction, Proposition 6.4 proves that non-contingent front-running is impossible.

## Falsification plan

**Source-stated falsification condition.** A mathematical counterexample or proof defect disproving relative-output monotonicity (Lemma 5.1), proving that $a^\star$ does not uniquely maximize worst-case profit, or demonstrating a universally profitable robust bundle when $\ell_s \le \lambda_c$.

**Research-defined falsification thresholds (all thresholds below are `research-defined falsification thresholds`):**

- **F1 - Fee-Paying Pool Empirical Threshold:** Simulate 100,000 synthetic victim swaps across Uniswap v2 30 bps fee pools ($\rho = 0.003$) with execution costs $c \in [10^{-5}X, 10^{-3}X]$. *Fail* the conservative fee-free threshold proxy if the empirical break-even lower bound $\lambda_{c, \text{empirical}}$ differs from $\lambda_c / (1-\rho)^2$ by more than `10.0%`. *Action if failed:* reject the analytical formula for pools with fees and require numerical root-finding.
- **F2 - Multi-Victim Concurrency Collision:** In an agent-based EVM simulator, inject 2 to 5 concurrent victim swaps within the same block. *Fail* single-victim sizing $a^\star(\ell_s)$ if victim revert rate exceeds `0.5%`. *Action if failed:* classify single-victim formulas as invalid in congested mempools.
- **F3 - Searcher Margin Compression in Live Order Flow:** Evaluate historical Flashbots MEV-Share and builder bid data across 50,000 blocks. *Fail* Theorem 4.5's 100% rent-extraction prediction if winning searchers retain median net profit $> 8.0\%$ of gross MEV. *Action if failed:* reject the symmetric Bertrand competition assumption in favor of searcher-builder collusion models.
- **F4 - Chance-Constrained Out-of-Sample Revert Rate:** Implement Proposition 6.2 ($\varepsilon$-admissibility) under empirical DEX trade-size distributions for $\varepsilon = 0.02$. *Fail* if out-of-sample revert rate exceeds `3.0%` (1.5x nominal $\varepsilon$). *Action if failed:* mandate strict robust admissibility ($\varepsilon = 0$).
- **F5 - Uniswap v3 Virtual Reserve Boundary Crossing:** Test $a^\star$ in Uniswap v3 pools with tick spacing 60. *Fail* if trades crossing 1 tick boundary produce negative net profit in $> 5.0\%$ of simulated cases. *Action if failed:* restrict strategy scope strictly to constant-product pools.

## Crypto portability

`direct`. The paper is natively written for cryptocurrency decentralized exchanges (Uniswap v2, constant-product AMMs) and Ethereum private mempools (Ferveo, Shutter Network, MEV-Share, SUAVE).

Residual crypto-specific structural factors:
1. **Flashbots / PBS infrastructure:** Execution depends on builder bundle APIs rather than public mempool gas auctions.
2. **EIP-1559 base fee volatility:** Rapid intra-block base fee spikes directly alter execution cost $c$, shifting $\lambda_c$.
3. **Smart contract reentrancy / ERC-20 token hooks:** Fee-on-transfer or rebasing tokens break standard CPMM invariant equations.
4. **MEV protection adoption:** Rising adoption of private RPCs with strict direction hiding directly neutralizes the mechanism.

Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: Empirical distribution of mempool leakage intervals across live private mempools; real-world auction tie-breaking rules among builders.
- `data gap`: No empirical trading data or historical dataset in the source; all claims are analytical theorems.
- `unproven`: Implementation in live Uniswap v3 or multi-pool routing environments where liquidity is piecewise.
- `not independently reproduced`: Mathematical results not independently re-derived in our execution stack.
- `stylized model`: Fee-free base model; single victim order; risk-neutral symmetric searchers; fixed execution cost $c$.

## Implementation status

`implementation_status: not-implemented`. No MEV searcher bot, smart contract, or bundle builder integration has been implemented in our research stack. No trading orders or transactions have been submitted.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in `alpha-strategy-research` does **not** constitute:
- Strategy approval;
- Validation of profitable live trading alpha;
- Ingestion into Hermes Wiki Brain;
- Entry into the production candidate pool;
- Backtest validation in Qlib or NautilusTrader;
- Authorization for paper, testnet, or live trading.

All operational additions and falsification thresholds are Scout-defined research proposals.

## Related Wiki records

Read-only search in Hermes Wiki Brain identified the following adjacent records:
- `[[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]` — AMM loss-versus-rebalancing (LVR) and arbitrage dynamics against liquidity pools.
- `[[quant/crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]]` — JIT liquidity provision on concentrated AMMs.
- `[[quant/crypto-cex-dex-priority-fee-stochastic-delay-mixed-control-2026-09-01]]` — Priority fee escalation and latency control in CEX-DEX arbitrage.

Adjacent repository records used for four-axis distinction:
- `crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01.md`
- `crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31.md`
- `cross-chain-agent-mev-arbitrage-adaptive-path-selection-2026-09-17.md`
- `crypto-cex-dex-priority-fee-stochastic-delay-mixed-control-2026-09-01.md`

## Sources

1. **Primary Paper:** Tingyi Lin, Jiazhuo Li, Ruoran Lai, *"How Much Must a Private Mempool Hide? Exact Leakage Thresholds for Sandwich Attacks"*, arXiv preprint `arXiv:2609.31379v1 [cs.GT, cs.CR, q-fin.TR]`, submitted 25 Sep 2026 15:15:24 UTC, announced 28 Sep 2026. Accepted to NeurIPS 2026.
   - Abstract & landing page: https://arxiv.org/abs/2609.31379
   - HTML full text: https://arxiv.org/html/2609.31379v1
   - TeX source bundle: https://arxiv.org/src/2609.31379 (verified files: `mev_leakage_thresholds.tex`, `checklist_mev_leakage_thresholds.tex`, `threshold_and_bits.pdf`)
   - PDF: https://arxiv.org/pdf/2609.31379 (23 pages, 349,300 bytes, SHA-256 `9a7cf478be900bfa82972194c8806813b2a1ee45ab5c94c43cb91bcce9761b31`)
   - Canonical DOI: https://doi.org/10.48550/arXiv.2609.31379
   - License: CC BY 4.0
2. **Canonical Specification:** Hermes Wiki Brain `/Users/hong/.hermes/wiki/quant/strategy-research-record-spec-v1.md` (10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`, read 2026-09-28) and repository `README.md`.
