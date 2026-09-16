---
schema: strategy-research-record-v1
title: "DEX Algorithmic Filter Precision, Reject Inference, and Early-Death Heuristic Disproof (Kamat 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - dex-trading
  - solana
  - reject-inference
  - filter-precision
  - counterfactual-sampling
  - prfs
  - red-2400
  - falsification
status: research-only
confidence: high
source_as_of: 2026-05-30
sources:
  - "Arati Uday Kamat, 'Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading: Evidence from 2,400 Rejection Events', arXiv:2607.02830v1 [q-fin.TR, q-fin.CP, q-fin.ST], Version 2.0 (2026-05-30). https://arxiv.org/abs/2607.02830"
  - "Arati Uday Kamat, 'Kamat_FilterPrecision_2026 Companion Dataset and Audit Code', Zenodo, DOI: 10.5281/zenodo.19987695, May 2026. https://doi.org/10.5281/zenodo.19987695"
  - "Arati Uday Kamat, 'RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels', Zenodo, DOI: 10.5281/zenodo.19989075, SSRN abstract ID 6702198, May 2026. https://doi.org/10.5281/zenodo.19989075"
  - "Arati Uday Kamat, 'Post-Rejection Follow-up Sampling: A Methodology for Counterfactual Outcome Measurement in Algorithmic DEX Trading', Zenodo, DOI: 10.5281/zenodo.20043516, SSRN abstract ID 6607301, May 2026. https://doi.org/10.5281/zenodo.20043516"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DEX Algorithmic Filter Precision, Reject Inference, and Early-Death Heuristic Disproof (Kamat 2026)

## Provenance

- **Primary Source:** Arati Uday Kamat (Independent Researcher, ORCID: `0009-0000-4781-312X`), *"Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading: Evidence from 2,400 Rejection Events"*, arXiv preprint `arXiv:2607.02830v1 [q-fin.TR, q-fin.CP, q-fin.ST]`, Version 2.0 submitted May 30, 2026 (`source-reported`).
  - Stable arXiv URL: https://arxiv.org/abs/2607.02830
  - PDF: https://arxiv.org/pdf/2607.02830
  - Canonical DOI: [10.48550/arXiv.2607.02830](https://doi.org/10.48550/arXiv.2607.02830) (`source-reported`).
  - SSRN Abstract ID: `6638259` (`source-reported`).
  - Companion Dataset & Code: Zenodo DOI `10.5281/zenodo.19987695` (`source-reported`).
- **External Validation Benchmark Source:** Arati Uday Kamat, *"RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels"*, Zenodo DOI `10.5281/zenodo.19989075`, SSRN abstract ID `6702198` (`source-reported`).
- **Methodological Substrate Source:** Arati Uday Kamat, *"Post-Rejection Follow-up Sampling: A Methodology for Counterfactual Outcome Measurement in Algorithmic DEX Trading"*, Zenodo DOI `10.5281/zenodo.20043516`, SSRN abstract ID `6607301` (`source-reported`).
- **Observation Window & Data Scope:** 12.7 elapsed days (approximately 13 calendar days) from 2026-04-10T21:54Z through 2026-04-23T15:22Z UTC on Solana DEX trading, comprising 99,510 forward samples across 2,402 unique rejection events spanning eight active filter rules (`source-reported`).
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2607.02830`, SSRN `6638259`, Zenodo `10.5281/zenodo.19987695`, PRFS, or RED-2400. Existing Kamat records (`solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md`, arXiv:2607.02795; `solana-memecoin-hour-aware-deployment-fragility-2026-09-14.md`, arXiv:2606.08232) investigate first-hour sniper cohort wallet rings and hourly volatility regimes respectively; neither addresses reject inference, counterfactual forward-outcome sampling, precision auditing of active risk filters, or the empirical disproof of the early-death heuristic.

## Economic mechanism

### Source-reported

1. **The Reject Inference Dilemma in Filter-Gated Trading:**
   - Filter-gated algorithmic trading systems deployed on decentralized exchanges (DEXs) evaluate hundreds or thousands of newly minted token pairs and reject the vast majority (`source-reported`).
   - Designers assume that rejection criteria save capital more often than they forgo profit: i.e., filters selectively eliminate tokens destined for catastrophic drawdowns or rug-pulls while admitting tokens with positive expected returns (`source-reported`).
   - However, in production, rejected tokens are unexecuted. Standard backtests and trading logs suffer from selection bias because counterfactual forward trajectories of rejected tokens are never recorded (`source-reported`).
   - Without empirical tracking of rejected tokens, quantitative traders cannot determine whether a low win rate or low throughput is caused by defective entry signals or by overly aggressive filters that inadvertently discard profitable opportunities (false positives / missed winners) (`source-reported`).

2. **Post-Rejection Follow-up Sampling (PRFS) & Counterfactual Tracking:**
   - Kamat introduces PRFS: an asynchronous tracking subsystem that monitors rejected tokens in real time at configurable intervals (every 15–30 minutes during the first hour, thinning thereafter) for up to 24 hours post-rejection (`source-reported`).
   - Tracking terminates upon 24-hour horizon expiry, token disappearance from the on-chain price oracle, or retry budget exhaustion (`source-reported`).

3. **Five-Tier Outcome Classification & The Early-Death Fallacy:**
   - Rejection events are categorized into five outcome tiers based on observed 24-hour forward trajectories:
     1. *Saved (windowed):* Minimum price drops $\le 50\%$ of reference price ($P_{\mathrm{ref}}$, earliest forward sample). Had the system entered, it would have suffered a $\ge 50\%$ measured drawdown (`source-reported`).
     2. *Missed (moon):* Maximum price reaches $\ge 200\%$ of reference price. Had the system entered, it would have captured a $\ge 100\%$ run-up (`source-reported`).
     3. *Saved (early-death):* Exactly one forward sample collected within $\le 60$ minutes of rejection, after which the token vanishes from the price oracle (`source-reported`).
     4. *Flat:* Token exhibits bounded movement without reaching either the $\le 50\%$ or $\ge 200\%$ thresholds (`source-reported`).
     5. *Unclassifiable:* Invalid reference price ($NaN$ or $\le 0$) or single sample collected at $> 60$ minutes (`source-reported`).
   - Under a naive heuristic widely held by algorithmic DEX operators, single-sample disappearance within 60 minutes is treated as an immediate "rug-pull save" (producing an optimistic 14.8 : 1 save-to-miss ratio) (`source-reported`).
   - Kamat joins the 399 early-death mints against ground-truth graveyard lifecycle data from the RED-2400 benchmark (`graveyard_lifecycle.csv`). The matched comparison proves that early-death mints die (`gone` state) at a *lower* rate (48.9%) than non-early-death rejected mints (57.6%) (`source-reported`).
   - Therefore, the early-death classification fails to identify elevated rug-pull risk over rejection alone; the 14.8 : 1 ratio is falsified, leaving the conservative 3.7 : 1 measured-drawdown ratio as the only evidence-supported figure (`source-reported`).

### Research interpretation

1. **Information Value of Reject Auditing for Alpha System Design:**
   - In quantitative trading, risk management and filtering rules are frequently treated as "pure protection." This paper formalizes the econometric reality that every filter rule is an implicit short position on the candidate token: rejecting a token is an assertion that its forward risk-adjusted drift is negative.
   - Auditing the reject stream provides the critical missing denominator for Bayesian signal optimization:
     $$\mathrm{Precision}(\mathrm{Filter}_k) = \frac{\mathbb{P}(\mathrm{Loss} \ge 50\% \mid \mathrm{Rejected}_k)}{\mathbb{P}(\mathrm{Gain} \ge 100\% \mid \mathrm{Rejected}_k)}$$
   - When a filter displays a save-to-miss ratio $< 1.0$, it is actively destroying portfolio alpha by filtering out more winners than losers.

2. **Heuristic Bias and Survivorship Illusion in Algorithmic Infrastructure:**
   - The paper's core epistemological warning is that infrastructure failures (oracle dropped connection, RPC rate-limit, pool liquidity exhaustion) mimic token "death." Naively crediting tracking dropouts as "successful saves" inflates perceived filter precision by $4\times$ (from 3.7:1 to 14.8:1).
   - In crypto microstructure, rigorous counterfactual validation requires distinguishing observable price drawdowns from measurement dropouts.

## Signal

### 1. Underlying Production Filter Rules (`source-reported`)

The audit evaluates eight active filter rules deployed in production on Solana DEXs, anonymized as `filter_1` through `filter_8` in descending order of event count (`source-reported`):
- `filter_1` (N = 935): Highest-frequency primary gating filter (`source-reported`).
- `filter_2` (N = 572): Second most frequent gating filter (`source-reported`).
- `filter_3` (N = 361): Liquidity / market-depth gate (`source-reported`).
- `filter_4` (N = 215): Structural / creator risk gate (`source-reported`).
- `filter_5` (N = 210): Flow / momentum gating filter (`source-reported`).
- `filter_6` (N = 80): High-drawdown prevention filter (`source-reported`).
- `filter_7` (N = 25): Secondary risk filter (`source-reported`).
- `filter_8` (N = 4): Rare-event exception filter (`source-reported`).

### 2. Five-Tier Classification Algorithm (`source-reported`)

For each unique rejection event $e_i$ of token mint $m$ at timestamp $t_{\mathrm{reject}}$:
1. **Reference Price Formation:** Identify the earliest available forward sample $s_0$ where $\mathrm{ageMin}(s_0) = \min_j \mathrm{ageMin}(s_j)$. Set $P_{\mathrm{ref}} = \mathrm{priceUsd}(s_0)$ (`source-reported`).
   - If $P_{\mathrm{ref}} \le 0$ or is $NaN$, classify as `unclassifiable` (`source-reported`).
2. **Trajectory Extremes:** Over the 24-hour follow-up window $[t_{\mathrm{reject}}, t_{\mathrm{reject}} + 24\mathrm{h}]$:
   $$P_{\mathrm{min}} = \min_{j} \mathrm{priceUsd}(s_j), \quad P_{\mathrm{max}} = \max_{j} \mathrm{priceUsd}(s_j)$$
3. **Classification Rules & Precedence:**
   - If total valid samples $N_{\mathrm{samples}} \ge 2$:
     - **Tie-Break Precedence (Missed-over-Saved):** If *both* $P_{\mathrm{max}} \ge 2.0 \cdot P_{\mathrm{ref}}$ AND $P_{\mathrm{min}} \le 0.5 \cdot P_{\mathrm{ref}}$ occur within the 24-hour window, the event is strictly classified as **`missed`** (`source-reported`).
     - Else if $P_{\mathrm{max}} \ge 2.0 \cdot P_{\mathrm{ref}}$, classify as **`missed`** (`source-reported`).
     - Else if $P_{\mathrm{min}} \le 0.5 \cdot P_{\mathrm{ref}}$, classify as **`saved_windowed`** (`source-reported`).
     - Else classify as **`flat`** (`source-reported`).
   - If $N_{\mathrm{samples}} == 1$:
     - If $\mathrm{ageMin}(s_0) \le 60$ minutes, classify as **`saved_early_death`** (`source-reported`).
     - If $\mathrm{ageMin}(s_0) > 60$ minutes, classify as **`unclassifiable`** (`source-reported`).

### 3. Normalized Reject-Inference Alpha Overlay (`research-proposed`)

To translate Kamat's audit methodology into a systematic alpha enhancement rule for DEX trading systems:
- **Filter Retirement Rule (`research-proposed`):** Any candidate filter rule $k$ evaluated across a minimum sample of $N_k \ge 50$ rejection events that exhibits a conservative save-to-miss ratio:
  $$\mathcal{R}_{\mathrm{cons}}(k) = \frac{N_{\mathrm{saved\_windowed}}(k)}{N_{\mathrm{missed}}(k)} < 1.5$$
  is automatically flagged for immediate retirement or parameter loosening (`research-proposed`).
- **Dynamic Filter Weighting (`research-proposed`):** In a soft-voting or multi-factor entry architecture, filter penalty weights are scaled proportionally to $\ln(\mathcal{R}_{\mathrm{cons}}(k))$, prioritizing filters like `filter_1` (5.0 : 1) and `filter_3` (4.2 : 1) over low-conviction filters (`research-proposed`).
- **Lookahead & Leakage Protection:** The classification rule operates strictly on forward samples collected after $t_{\mathrm{reject}}$; no contemporaneous post-rejection price data is fed back into the live evaluation engine during the active 24-hour window (`research-proposed`).

## Required data

- **Forward Follow-Up Sampling Schema (11 Fields) (`source-reported`):**
  - `sampleTs`: ISO-8601 UTC timestamp of the forward observation (`source-reported`).
  - `mint`: On-chain base mint address on Solana (`source-reported`).
  - `symbol`: Ticker symbol string (`source-reported`).
  - `rejectReason`: Active filter label string (`filter_1` through `filter_8`) (`source-reported`).
  - `rejectTs`: ISO-8601 UTC timestamp of the original rejection decision (`source-reported`).
  - `ageMin`: Elapsed time in minutes between rejection and forward observation ($\ge 0$) (`source-reported`).
  - `priceUsd`: USD token price obtained from on-chain DEX pool or price oracle (`source-reported`).
  - `liquidity`: Pool liquidity in USD, $\log_2$-binned for privacy/compression (`source-reported`).
  - `volume24h`: 24-hour rolling volume in USD, $\log_2$-binned (`source-reported`).
  - `dexId`: Decentralized exchange identifier (e.g. Raydium, Orca, Meteora) (`source-reported`).
  - `pairAddress`: Liquidity pool account public key on Solana (`source-reported`).
- **External Validation Join Data (`source-reported`):**
  - RED-2400 `graveyard_lifecycle.csv`: Long-term tracking records with discrete state labels (`alive_active`, `alive_dormant`, `gone`) (`source-reported`).
- **Point-in-Time Discipline:**
  - Forward samples must be timestamped with confirmed block time or atomic UTC clock timestamps (`source-reported`).
  - Rejection events must precede the first forward sample: $\mathrm{ageMin} > 0$ (`source-reported`).

## Execution assumptions

- **Evaluation Perspective:** Counterfactual execution modeling (`source-reported`).
  - Entry assumption: Simulated entry at $P_{\mathrm{ref}}$ (earliest available sample price within minutes of rejection) with zero slippage assumed for classification benchmarking (`source-reported`).
  - Target exit levels: Drawdown exit at $-50\%$ ($P \le 0.5 \cdot P_{\mathrm{ref}}$); run-up profit exit at $+100\%$ ($P \ge 2.0 \cdot P_{\mathrm{ref}}$) (`source-reported`).
  - Horizon: Fixed 24 hours post-rejection (`source-reported`).
- **Operational Reality on Solana DEXs (`research-proposed`):**
  - Base priority fee: 5,000–50,000 microlamports per compute unit (`research-proposed`).
  - Pool slippage: For illiquid micro-cap memecoins, market orders of $> 1$ SOL suffer 2–5% slippage and sandwich risk (`research-proposed`).
  - Taker fee: 25–30 bps on standard Raydium AMM / CPMM pools (`research-proposed`).
  - These frictions imply that in live execution, the real-world threshold for a "missed winner" requires $> +115\%$ gross move to capture $+100\%$ net, making the paper's $2.0\times$ threshold conservative (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below are extracted directly from Kamat (2026, arXiv:2607.02830v1, Section IV, V, and Figures 1–2):

1. **Cohort-Level Outcome Distribution (Section V.A, Table 1):**
   - Total rejection events: **2,402 events** across 13 calendar days (`source-reported`).
   - Total follow-up samples: **99,510 observations** (`source-reported`).
   - **Saved (windowed):** **418 events** (**17.4%**) (`source-reported`).
   - **Saved (early-death):** **1,236 events** (**51.5%**) (`source-reported`).
   - **Flat:** **636 events** (**26.6%**) (`source-reported`).
   - **Missed (moon):** **112 events** (**4.7%**) (`source-reported`).
   - **Unclassifiable:** **0 events** (**0.0%**) (`source-reported`).

2. **Per-Filter Breakdown (Section V.A, Table 1):**
   - `filter_1` (N = 935): Saved-W = 17.9%, Saved-ED = 44.8%, Flat = 33.7%, Missed = 3.6%, Unclass = 0.0%. (Conservative ratio = **5.0 : 1**).
   - `filter_2` (N = 572): Saved-W = 16.6%, Saved-ED = 58.9%, Flat = 18.9%, Missed = 5.6%, Unclass = 0.0%. (Conservative ratio = **3.0 : 1**).
   - `filter_3` (N = 361): Saved-W = 15.2%, Saved-ED = 50.1%, Flat = 31.0%, Missed = 3.6%, Unclass = 0.0%. (Conservative ratio = **4.2 : 1**).
   - `filter_4` (N = 215): Saved-W = 20.0%, Saved-ED = 58.6%, Flat = 15.8%, Missed = 5.6%, Unclass = 0.0%. (Conservative ratio = **3.6 : 1**).
   - `filter_5` (N = 210): Saved-W = 14.8%, Saved-ED = 65.7%, Flat = 15.7%, Missed = 3.8%, Unclass = 0.0%. (Conservative ratio = **3.9 : 1**).
   - `filter_6` (N = 80): Saved-W = 30.0%, Saved-ED = 37.5%, Flat = 20.0%, Missed = 12.5%, Unclass = 0.0%. (Conservative ratio = **2.4 : 1**).
   - `filter_7` (N = 25): Saved-W = 12.0%, Saved-ED = 16.0%, Flat = 60.0%, Missed = 12.0%, Unclass = 0.0%. (Conservative ratio = **1.0 : 1**).
   - `filter_8` (N = 4): Saved-W = 0.0%, Saved-ED = 25.0%, Flat = 75.0%, Missed = 0.0%, Unclass = 0.0%. (Sample size too small for inference).

3. **Aggregate Performance Ratios (Section V.B):**
   - **Headline Conservative Save-to-Miss Ratio:** $\frac{418}{112} = \mathbf{3.7 : 1}$ (`source-reported`).
   - Every individual active filter with adequate sample size (`filter_1` through `filter_7`) has $\mathrm{Saved\_W} \% > \mathrm{Missed} \%$ (net-positive) (`source-reported`).
   - Combined (windowed + early-death) ratio: $\frac{418 + 1236}{112} = \frac{1654}{112} = \mathbf{14.8 : 1}$ (`source-reported`).

4. **Matched External Validation Disproof of Early-Death Heuristic (Section V.C):**
   - Joining 399 distinct `saved_early_death` mints to RED-2400 `graveyard_lifecycle.csv`:
     - Early-death mints reaching terminal `gone` state: **195 / 399** = **48.9%** (`source-reported`).
     - Early-death mints observed alive (`alive_active` or `alive_dormant`): **204 / 399** = **51.1%** (`source-reported`).
   - Matched comparison group (non-early-death rejected mints):
     - Total rejected mints with graveyard observation: 656 mints, 343 reach `gone` (52.3% base rate) (`source-reported`).
     - Non-early-death rejected mints: 257 mints, **148 reach `gone`** = **57.6%** (`source-reported`).
   - **Disproof Finding:** Early-death classified mints actually reach `gone` at a *lower* rate (48.9%) than non-early-death rejected mints (57.6%) (`source-reported`).
   - The early-death flag carries *zero incremental rug-pull predictive signal* over rejection alone; the wider 14.8 : 1 ratio is an artifact of selection bias and unvalidated proxy assumptions (`source-reported`).

5. **Sample Dynamics & Tracking Characteristics (Section VIII, Figures 1 & 2):**
   - Single-sample event age distribution: 1,083 events in 0–5 min bucket; 153 events in 5–60 min bucket; 0 events in 1–6 hr and 6–24 hr buckets (`source-reported`).
   - Median follow-up sample counts: Saved (early-death) = 1; Saved (windowed) = 144; Flat = 5; Missed = 144 (`source-reported`).

### Independently reproduced

`Not independently reproduced.` All cohort numbers, per-filter outcome shares, save-to-miss ratios, and matched graveyard lifecycle rates represent third-party empirical findings directly reported by Arati Uday Kamat in arXiv:2607.02830v1 and verified against the deposited dataset schema (`Zenodo 10.5281/zenodo.19987695`). No independent raw Solana RPC node replication has been conducted in this research stack.

### Negative evidence

- **Falsification of Early-Disappearance Heuristic:** The paper directly disproves the common algorithmic trading belief that tokens disappearing from price oracles within 60 minutes represent successful rug-pull avoidance. In matched tests, these tokens survived at higher rates (51.1% alive) than tokens with persistent tracking (`source-reported`).
- **Substantial Missed Profit (Opportunity Cost):** 112 rejected tokens (4.7% of the rejected universe) doubled in price ($+100\%$) within 24 hours. In volatile regimes, `filter_6` and `filter_7` suffered a 12.0–12.5% missed rate, imposing severe drag on gross alpha (`source-reported`).
- **Single-Regime Limitation:** The 13-day observation window (April 10–23, 2026) captures a single market regime on Solana DEXs; stability of filter precision across bear-market liquidity droughts or extreme meme mania remains unproven (`source-reported`).

## Falsification plan

To empirically validate or falsify the effectiveness of reject-inference auditing and filter-pruning rules in our own execution stack:

1. **Out-of-Sample PRFS Audit on Alternative Chains / Regimes:**
   - **Sample:** Continuous 30-day PRFS tracking of rejected micro-cap token entries on Base DEXs (Uniswap v3 / Aerodrome) and Solana DEXs across Q4 2026 (`research-proposed`).
   - **Methodology:** Run Kamat's five-tier classification algorithm with strict missed-over-saved precedence on all rejected candidates (`research-proposed`).
   - **Decision Rule (`research-defined falsification threshold`):** If the aggregate conservative save-to-miss ratio drops below $1.5 : 1$, or if more than $40\%$ of active filters exhibit $\mathrm{Saved\_W} < \mathrm{Missed}$, the hypothesis that the production filter stack preserves capital is falsified.

2. **Ablation Test on Pruned vs. Unpruned Filter Stacks:**
   - **Sample:** Dual parallel paper-trading agents running identical core entry signals over 1,000 candidate token launches (`research-proposed`).
     - Agent A: Full 8-filter production stack.
     - Agent B: Pruned stack removing filters with $\mathcal{R}_{\mathrm{cons}} < 2.0$ (e.g. removing `filter_7`).
   - **Decision Rule (`research-defined falsification threshold`):** If Agent A achieves a higher net Sharpe ratio and higher net PnL (after transaction costs and fees) than Agent B, the hypothesis that PRFS-guided filter pruning improves net portfolio returns is falsified.

3. **Graveyard Join Robustness Test:**
   - **Sample:** Join 500 newly collected single-sample disappearance tokens against Birdeye / DexScreener liquidity archives at $T = 7$ days (`research-proposed`).
   - **Decision Rule (`research-defined falsification threshold`):** If the 7-day terminal death rate of single-sample dropouts exceeds $80\%$ (statistically exceeding the matched rejected base rate at $p < 0.01$), Kamat's disproof of the early-death tier is falsified for modern multi-RPC collector architectures.

## Crypto portability

`direct`

The empirical audit, underlying mechanisms, and datasets are 100% native to cryptocurrency decentralized exchanges (specifically Solana DEX markets including Raydium, Orca, and Meteora).

Crypto-specific structural factors documented in the research:
- **DEX Liquidity Dynamics:** Tokens can experience abrupt liquidity removal (rug-pulls) or extreme explosive growth ($> 100\%$ within hours) uncommon in traditional equity markets (`source-reported`).
- **Oracle & Indexer Dropout:** On decentralized infrastructure, price APIs and RPC nodes experience indexing drops, rate-limits, or routing failures when tokens launch rapidly, generating spurious disappearance events (`source-reported`).
- **Token Mint Lifecycle:** Solana SPL token mints provide unambiguous, immutable identifiers, allowing exact cross-dataset joins between production reject logs and long-term graveyard trackers (`source-reported`).
- **Gas & Priority Fees:** High congestion on Solana during memecoin waves induces trade dropouts that interact with filter execution (`research-proposed`).

## Limitations

- **Not Independently Reproduced:** All reported percentages, distributions, and join statistics represent third-party empirical findings from Kamat (2026).
- **Single 13-Day Snapshot:** The dataset reflects market conditions between April 10 and April 23, 2026. Generalization to prolonged bear markets or differing liquidity environments is unproven (`source-reported`).
- **Anonymized Filter Rules:** The public dataset deterministically anonymizes the eight filter rules (`filter_1` through `filter_8`), meaning specific indicator parameters (e.g. exact liquidity threshold or holder dispersion cutoff) must be independently calibrated (`source-reported`).
- **Single-Chain Deployment:** Findings reflect Solana DEX microstructure; portability to EVM rollups (Base, Arbitrum) where block times, gas auctions, and MEV dynamics differ has not been tested (`source-reported`).

## Implementation status

`not-implemented`

No automated PRFS tracking pipeline or filter-pruning engine has been implemented in our research stack (`nautilus-quant-system` or PyBroker). This record captures external empirical methodology, classification algorithms, and negative findings regarding reject inference.

## Adoption boundary

Research material only. This record documents empirical filter audit methodology and the falsification of a common heuristic in algorithmic trading. It does not constitute an approved alpha strategy, a production filter stack, or authorization for live capital allocation, testnet deployment, or paper trading.

## Related Wiki records

- `[[solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02]]` — Kamat (2026, arXiv:2607.02795): Coordinated sniper cohort detection on pump.fun.
- `[[solana-memecoin-hour-aware-deployment-fragility-2026-09-14]]` — Kamat (2026, arXiv:2606.08232): Hour-aware risk management and diurnal volatility fragility on Solana DEXs.
- `[[pump-fun-manipulation-signal-fade-wash-copycat-coordinated-sell-2026-09-15]]` — Tsuchiya et al. (2026, arXiv:2609.10246): Memecoin factory manipulation classification and volume fade.
- `[[fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16]]` — Danait et al. (2026, arXiv:2609.13597): Partial identification and execution sensitivity in backtesting.
- `[[polymarket-protocol-finality-redemption-latency-carry-arbitrage-falsification-2026-09-16]]` — Nechepurenko (2026, arXiv:2609.15373): Empirical protocol finality latency and carry arbitrage falsification.

## Sources

1. **Arati Uday Kamat**, *"Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading: Evidence from 2,400 Rejection Events"*, arXiv preprint `arXiv:2607.02830v1 [q-fin.TR, q-fin.CP, q-fin.ST]`, Version 2.0, submitted May 30, 2026.
   - Stable arXiv URL: https://arxiv.org/abs/2607.02830
   - Full-text PDF: https://arxiv.org/pdf/2607.02830
   - Canonical DOI: https://doi.org/10.48550/arXiv.2607.02830
   - SSRN Working Paper: https://ssrn.com/abstract=6638259
2. **Arati Uday Kamat**, *"Kamat_FilterPrecision_2026 Companion Dataset and Audit Code"*, Zenodo Open Access Repository, May 30, 2026.
   - Zenodo DOI: https://doi.org/10.5281/zenodo.19987695
   - Includes: `Kamat_FilterPrecision_2026_outcomes.jsonl`, `Kamat_FilterPrecision_2026_audit.js`, `Kamat_FilterPrecision_2026_figures.py`, `PROVENANCE.md`, `README.md`.
3. **Arati Uday Kamat**, *"RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels"*, Zenodo Open Access Repository, May 30, 2026.
   - Zenodo DOI: https://doi.org/10.5281/zenodo.19989075
   - SSRN Working Paper: https://ssrn.com/abstract=6702198
4. **Arati Uday Kamat**, *"Post-Rejection Follow-up Sampling: A Methodology for Counterfactual Outcome Measurement in Algorithmic DEX Trading"*, Zenodo Open Access Repository, May 30, 2026.
   - Zenodo DOI: https://doi.org/10.5281/zenodo.20043516
   - SSRN Working Paper: https://ssrn.com/abstract=6607301
