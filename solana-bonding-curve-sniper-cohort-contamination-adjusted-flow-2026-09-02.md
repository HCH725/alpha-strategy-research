---
schema: strategy-research-record-v1
title: "Coordinated Sniper Cohort Detection and Contamination-Adjusted Buyer-Flow Alpha on Solana Bonding Curves"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - on-chain
  - solana
  - bonding-curves
  - pump-fun
  - wallet-clustering
  - sniper-detection
  - order-flow
  - adverse-selection
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-07-02
sources:
  - "Arati Uday Kamat, 'Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and a Contamination-Adjusted Estimate of Coordination-Specific First-Hour Buyer-Flow Lift', arXiv:2607.02795v1 [q-fin.TR], July 2026. https://arxiv.org/abs/2607.02795"
  - "Arati Uday Kamat, 'RED-COHORT-2026-v1 Dataset and Reproduction Scripts', Zenodo, DOI: 10.5281/zenodo.20978741, July 2026."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coordinated Sniper Cohort Detection and Contamination-Adjusted Buyer-Flow Alpha on Solana Bonding Curves

## Provenance

- **Primary Source:** Arati Uday Kamat, *"Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and a Contamination-Adjusted Estimate of Coordination-Specific First-Hour Buyer-Flow Lift"*, arXiv preprint `arXiv:2607.02795v1 [q-fin.TR]`, published July 2026. URL: https://arxiv.org/abs/2607.02795.
- **Data Repository:** Zenodo dataset `RED-COHORT-2026-v1`, DOI: `10.5281/zenodo.20978741`.
- **Primary Category:** Trading and Market Microstructure (`q-fin.TR`).
- **Empirical Dataset:** 1,578,333 buyer observations from 166,098 token launches over 13.4 days (2026-06-11 to 2026-06-25) on the Solana `pump.fun` constant-product bonding-curve marketplace.

## Economic mechanism

### Source-reported

In decentralized on-chain token launchpads (e.g., Pump.fun on Solana), newly deployed tokens follow a deterministic bonding curve where early purchases systematically increase token spot price. 

Retail market participants and automated on-chain bots frequently employ "sniper copy-trading" or "smart-money tracking" strategies, operating under the hypothesis that when coordinated groups of sophisticated early buyers ("sniper rings" or "syndicates") enter a new launch simultaneously, their presence causes or signals substantial follow-on retail buyer momentum and capital inflow.

The author designs a two-stage detection pipeline:
1. **Intra-Launch First-Buyer Window Extraction:** Identifies all wallet addresses participating in the earliest transaction block / initial buyer window of each launch.
2. **Cross-Launch Persistent Cohort Surfacing:** Constructs a co-occurrence graph across 166,098 launches and applies union-find connected-component clustering to extract persistent wallet cohorts that repeatedly co-fire across multiple independent token launches.

The pipeline isolates **1,012 persistent wallet cohorts** (spanning 2 to 12 wallets each, encompassing 2,965 distinct addresses).

### Research interpretation

This research provides crucial negative and adversarial econometric evidence against naive on-chain wallet-following alpha:

1. **Severe Arithmetic Contamination:** A naive pooled comparison suggests that cohort-touched launches experience a massive **+130.9%** higher first-hour buyer count. However, roughly half of this apparent effect is pure arithmetic contamination caused by counting the cohort wallets' own buy transactions in the outcome variable. When contamination is removed (measuring strictly non-cohort external buyers), the lift drops to **+63.9%**.
2. **Confounding by Launch Quality (Selection Bias):** Applying 1:1 nearest-neighbour Propensity Score Matching (PSM, 0.2-SD caliper on 10 launch-quality covariates across 5,419 matched pairs) reveals that most remaining lift is explained by launch-level observable features (creator history, initial liquidity, metadata, social links). The genuine causal non-cohort buyer count lift drops to **+16.1% (95% CI [+13.0%, +19.4%])**.
3. **Statistically Zero Capital Inflow Lift:** The estimated net external SOL capital inflow lift under PSM drops to **+6.3% (95% CI [-0.5%, +15.1%])**, which is **statistically indistinguishable from zero ($p > 0.05$)**.
4. **Liquidity Trap / Honeypot Risk:** Out of 5,419 treated launches, **382 launches (7.0%) attracted exactly zero non-cohort buyers** in the first 30 minutes. Automated copy-traders following these sniper rings become trapped with zero exit liquidity.
5. **Placebo Bias Diagnostic:** An activity-matched placebo across 100 seeds generated a median estimated lift of **+189.6%** (exceeding the real estimate in 100 out of 100 seeds), proving that naive activity-based wallet tracking suffers from severe intrinsic selection bias.

## Signal

### 1. Two-Stage Cohort Detection Pipeline

- **Stage 1 (First-Window Extraction):** For each launch $k \in \{1, \dots, K\}$, record the set of early buyer wallet addresses $W_k = \{w_{k, 1}, \dots, w_{k, m}\}$ appearing within the initial $N_{\text{first}} = 10$ buyer transactions.
- **Stage 2 (Union-Find Co-occurrence Graph):**
  - Compute edge weights $E(w_i, w_j) = \sum_{k=1}^K \mathbb{I}(w_i \in W_k \land w_j \in W_k)$.
  - Filter edges satisfying minimum co-occurrence threshold $E(w_i, w_j) \ge E_{\text{thresh}} = 5$.
  - Run Disjoint Set Union (Union-Find) to partition addresses into persistent cohort clusters $\mathcal{C}_1, \mathcal{C}_2, \dots, \mathcal{C}_R$.

### 2. Launch Identification & Adverse-Selection Filter

When a new token launch $L_{\text{new}}$ is initiated:
- Extract early buyer set $W_{\text{new}}$.
- Identify active cohort:
  $$\text{CohortHit}(L_{\text{new}}) = \mathbb{I}\left(\exists r \text{ s.t. } |W_{\text{new}} \cap \mathcal{C}_r| \ge 2\right)$$
- **Adversarial Risk Conditioning (Anti-Copy Rule):**
  - If $\text{CohortHit}(L_{\text{new}}) = 1$ AND external non-cohort transaction count in the first $\Delta t_{\text{verify}} = 15\text{ seconds}$ is zero ($N_{\text{ext}} = 0$):
    - **Do NOT execute copy-trade** (7.0% base-rate liquidity trap filter).
  - If $\text{CohortHit}(L_{\text{new}}) = 1$ AND $N_{\text{ext}} \ge 3$ within $15\text{s}$ AND launch quality propensity score $e(X) \ge 0.70$:
    - Permit micro-momentum scalp with mandatory hard stop at $t_{\text{hold}} \le 45\text{ seconds}$ or $-10\%$ price drawdown.

## Required data

- **Instrument Universe:** Solana SPL tokens launched on Pump.fun bonding curves.
- **Venues:** Solana mainnet via low-latency RPC / Geyser WebSocket streaming (e.g., Jito, Helius, Triton).
- **Timeframe:** Microsecond-stamped on-chain transaction instruction traces and block events.
- **Fields:**
  - Token mint address and launch transaction signature.
  - Buyer wallet public keys (`pubkey`).
  - Transaction block slot, index, and microsecond timestamp.
  - SOL amount transferred and tokens minted.
  - Launch metadata covariates (creator address past launch history, token name/symbol entropy, presence of Twitter/Telegram URLs).

## Execution assumptions

- **Execution Route:** Solana priority fees + Jito MEV bundle submission to ensure sub-400ms transaction inclusion.
- **Slippage & Impact:** Constant-product bonding curve $x \cdot y = k$; slippage must be bounded at $\le 1.0\%$.
- **Transaction Costs:** Solana base network fee ($0.000005\text{ SOL}$) + Jito validator tip ($0.001 - 0.01\text{ SOL}$).
- **Holding Period:** Ultra-short scalping horizon ($< 60\text{ seconds}$) due to rapid sniper dumping.

## Evidence

### Source-reported

- **Empirical Scope:** 1,578,333 buyer events across 166,098 launches over 13.4 days analyzed via Zenodo dataset `RED-COHORT-2026-v1`.
- **Cohort Identification:** 1,012 persistent wallet cohorts detected (2 to 12 wallets each, 2,965 unique addresses).
- **Contamination Decomposition:**
  - Naive pooled buyer count lift: **+130.9%**.
  - Contamination-adjusted (excluding cohort wallets): **+63.9%**.
  - 1:1 PSM on 10 covariates (5,419 matched pairs): **+16.1% (95% CI [+13.0%, +19.4%])**.
- **Inflow Significance Failure:** Contamination-adjusted PSM net SOL inflow lift: **+6.3% (95% CI [-0.5%, +15.1%])**, failing two-sided null hypothesis test at $\alpha = 0.05$.
- **Ghost Launches:** 382 out of 5,419 treated launches (7.0%) had exactly 0 non-cohort buyers in the first 30 minutes.
- **Placebo Test Bias:** Activity-matched placebo across 100 seeds produced median lift of +189.6%, higher than empirical lift in 100/100 seeds, diagnosing severe inherent selection bias.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Econometric Breakdown of Sniper Copy-Trading:** The empirical finding that capital inflow is statistically indistinguishable from zero ($[-0.5\%, +15.1\%]$) directly refutes the common retail alpha claim that following sniper rings yields robust positive dollar momentum.
- **Extreme Adverse Selection & Exit Infeasibility:** In 7.0% of cohort launches, zero external liquidity ever enters, resulting in 100% principal loss for naive copy-bots. In the remaining 93%, cohort wallets systematically dump their inventory within the first 1 to 5 minutes, front-running late-arriving retail and copy-trade flow.

## Falsification plan

1. **Contamination Adjustment Check:** In any proposed on-chain wallet tracking strategy, compute performance metrics with and without target wallet transactions in the outcome variable. Falsified if $> 50\%$ of strategy alpha vanishes upon removing target wallet self-volume.
2. **Propensity Score Matching Control Test:** Match treated launches against non-treated launches using pre-launch observable features (creator reputation, metadata completeness, launch time-of-day). Falsified if net P&L on matched pairs drops to statistical insignificance ($t < 1.96$).
3. **Out-of-Sample Cohort Persistence Test:** Track detected cohorts $\mathcal{C}_r$ across the subsequent 14-day rolling window. If cohort co-firing rate decays by $> 75\%$ or wallet addresses rotate to fresh burner accounts, static cohort tracking is falsified.
4. **Execution Cost & MEV Sandwich Audit:** Simulate net strategy returns under realistic Solana Jito tip auctions and bonding curve price impact. Falsified if transaction fees and tip bidding consume $100\%$ of the residual $+16.1\%$ buyer lift.

## Crypto portability

- **Classification:** `direct`.
- **Portability Analysis:**
  - **Native Crypto Architecture:** The mechanism and empirical data are native to Solana bonding curves (Pump.fun, Moonshot) and EVM bonding curve launchpads (e.g., Uniswap v4 hook launchpads, Base token deployers).
  - **Mendelian Address Mutation (Burner Wallets):** On Solana, generating fresh keypairs is zero-cost, allowing sophisticated cohort operators to continuously discard old addresses and establish new rings, limiting the lifespan of static address clusters.
  - **MEV & Bundling Dependency:** The entire microstructure of early bonding-curve entry depends on Solana slot leader scheduling and Jito block bundling.

## Limitations

- **Short Observational Window:** The study spans 13.4 days of high-volume meme-token activity; cohort behavior and retail participation may differ across macro market regimes.
- **Address Clustering Ceiling:** Union-find clustering on co-occurrence captures static or slowly evolving cohorts, but misses dynamically generated single-use sybil wallets funded via common mixer/CEX deposits.
- **Unmodeled Gas Auction Competition:** Does not fully simulate competitive Jito tip escalation between competing sniper syndicates.

## Implementation status

Not implemented. No automated Solana on-chain sniper bot, PyBroker backtest, or live Geyser streaming engine has been constructed for this research record.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record constitutes a research capture of public empirical research on decentralized market microstructure and causal order-flow analysis. It does not authorize execution in paper, testnet, or live trading environments.

## Related Wiki records

- [[quant/crypto-public-wallet-identity-trader-informativeness-adverse-selection-2026-09-02]]
- [[quant/crypto-priority-gas-auctions-pga-dex-latency-arbitrage-2026-09-01]]
- [[quant/hyperliquid-sunshine-trading-adverse-selection-liquidity-extraction-2026-09-01]]
- [[quant/crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]]

## Sources

- Arati Uday Kamat, *"Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and a Contamination-Adjusted Estimate of Coordination-Specific First-Hour Buyer-Flow Lift"*, arXiv preprint `arXiv:2607.02795v1 [q-fin.TR]`, July 2026. Available at: https://arxiv.org/abs/2607.02795.
- Arati Uday Kamat, *"RED-COHORT-2026-v1 Dataset and Reproduction Scripts"*, Zenodo, DOI: `10.5281/zenodo.20978741`, July 2026. Available at: https://doi.org/10.5281/zenodo.20978741.
