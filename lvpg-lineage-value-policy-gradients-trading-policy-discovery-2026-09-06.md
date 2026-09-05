---
schema: strategy-research-record-v1
title: "LVPG: Lineage-Value Policy Gradients and the Time Value of Evolution for Automated Trading Policy Discovery"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - evolutionary-algorithms
  - policy-discovery
  - actor-critic
  - credit-assignment
  - futures
status: research-only
confidence: medium
source_as_of: 2026-08-14
sources:
  - "https://arxiv.org/abs/2608.13297"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LVPG: Lineage-Value Policy Gradients and the Time Value of Evolution for Automated Trading Policy Discovery

## Provenance

- **Primary Academic Source:** Matthew Siper, Ahmed Khalifa, and Julian Togelius (New York University), *"The Time Value of Evolution"*, arXiv preprint `arXiv:2608.13297v1 [cs.LG]`, submitted August 14, 2026.
- **Canonical DOI:** [10.48550/arXiv.2608.13297](https://doi.org/10.48550/arXiv.2608.13297).
- **Traceable Paper URLs:**
  - Stable Abstract: [https://arxiv.org/abs/2608.13297](https://arxiv.org/abs/2608.13297)
  - Full Text HTML: [https://arxiv.org/html/2608.13297v1](https://arxiv.org/html/2608.13297v1)
  - Full Text PDF: [https://arxiv.org/pdf/2608.13297v1](https://arxiv.org/pdf/2608.13297v1)
- **Sample Universe & History:** Hourly continuous futures data for S&P 500 E-mini (23,915 bars), Silver (24,020 bars), and 30-Year US Treasury (23,947 bars), ending on October 20, 2025.
- **Experimental Evaluation Protocol:** Ten end-anchored rolling-origin folds per market. Each fold consists of 4 months training, 1 month validation, a 3-day embargo, and 1 month sealed out-of-sample test data. Across 3 assets, 10 non-overlapping test folds, and 3 random seeds ({4, 5, 7}), each experimental condition is evaluated over 90 paired runs (720 total runs across 7 conditions and 3 mechanism ablations).
- **Pre-Write Deduplication Audit:**
  - Full repository search confirmed zero existing occurrences of `2608.13297`, `LVPG`, `Lineage-Value`, `Siper`, `Khalifa`, or `Togelius`.
  - Adjacent evolutionary and automated strategy discovery records in the repository (`factorengine-program-level-knowledge-infused-factor-mining-2026-09-05.md`, `alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05.md`, `madevolve-evolutionary-alpha-forecasting-passive-limit-order-bitcoin-2026-09-03.md`, `llm-verifier-guided-strategy-genome-evolution-evoquant-2026-09-04.md`) examine MCTS tree-search over formulaic grammars, genetic programming for passive limit orders, or multi-agent verification.
  - LVPG is mechanically and mathematically distinct: it addresses the fundamental credit-assignment failure of greedy, immediate-return evolutionary search by formalizing the "time value of evolution" in a finite-horizon MDP. It assigns path-based policy-gradient credit ($\gamma = 1.0$) across multi-step mutation trees, decoupling search control into separate LoRA actor and bootstrapped critic heads over an offline-calibrated Qwen3-8B foundation model.

## Economic mechanism

### Source-reported

In evolutionary search for trading rules, a newly generated child program may have lower immediate fitness than its parent, yet serve as an essential stepping stone—a "valuable ancestor"—that unlocks high-fitness regions reachable within the remaining search budget. Conventional operator control and evolutionary algorithms evaluate a mutation solely through its immediate offspring fitness ($\gamma = 0$). This myopic credit assignment penalizes structural mutations that temporarily degrade fitness, prematurely abandoning productive lineages.

Analogous to financial option pricing—where total option value decomposes into immediate intrinsic exercise value and extrinsic time value preserved by time to expiry—the utility of an evolutionary mutation decomposes into immediate offspring fitness and the finite-budget continuation value of reachable lineages. As the remaining search budget $h = H - t$ shrinks, this time value decays. An exploratory mutation early in an eight-step lineage can be refined and repaired, whereas the identical mutation near budget exhaustion expires before its downstream yield can materialize.

### Research interpretation

The alpha discovery mechanism operates through **temporal credit assignment and budget-aware search pacing**:
1. **Regime / Context Filter:** The search controller observes execution metrics, program AST context, budget remaining ($h$), stagnation counters, and recent progress.
2. **Primary Search Signal:** An actor network modulates mutation radius across three discrete behaviorally calibrated displacement tiers: `Refine` (narrow adjustments), `Interpolate` (moderate recombinations), and `Explore` (structural innovations).
3. **Lineage Valuation:** A critic network bootstrapped from multi-step mutation trees estimates the expected future path yield ($Q^\pi(s, z)$), providing non-myopic guidance that values exploratory stepping stones.
4. **Execution Policy Output:** The resulting evolved programs are expressed in Genetic Programming Trading Language (GPTL), generating typed Boolean entry and exit signals for continuous futures markets.

The core falsifiable thesis is that finite-budget automated alpha discovery is constrained by myopic credit assignment rather than lack of semantic variation: rewarding mutations based on the terminal performance of their descendants ($\gamma = 1.0$) enables search to navigate fitness valleys, reducing unrecoverable regressions and discovering trading policies with superior out-of-sample risk-adjusted returns compared to immediate-return optimization.

## Signal

The strategy operates on two distinct levels: (1) the meta-level search algorithm (LVPG) that discovers trading rules, and (2) the executable trading policies discovered by LVPG.

### Meta-Level Search Protocol (LVPG)

- **Search State Representation:** At step $t$, the state $s_t$ presented to the controller comprises:
  - Natural language specification of current candidate policy $p_t^{\mathrm{NL}}$.
  - GPTL program tree representation.
  - In-sample training window execution metrics $m_t$ (training Sharpe, return, drawdown, win rate, trade count).
  - Search budget state: remaining evaluation steps $h = H - t$ (out of total budget $H = 256$).
  - Stagnation metrics: steps since last path-best improvement ($B_t$).
- **Action Space:** Discrete choice of mutation radius $z_t \in \{\text{Refine}, \text{Interpolate}, \text{Explore}\}$.
  - Calibrated using Offset Direct Preference Optimization (ODPO) on Qwen3-8B to produce distinct median behavioral displacements: 0.095 (`Refine`), 0.194 (`Interpolate`), and 0.326 (`Explore`) executed action-sequence disagreement.
- **Reward Formulation:**
  - Best-so-far step reward: $R_t = \max(0, \widetilde{B}_{t+1} - \widetilde{B}_t)$, where $\widetilde{B}_t$ is the running path-best standardized fitness.
  - Undiscounted return: $\gamma = 1.0$, allowing telescoping path value $G_t = \widetilde{B}_H - \widetilde{B}_t$.
  - Invalidation penalty: $-0.25$ standardized fitness for non-compiling or degenerate programs (<10 trades).
- **Optimization:** PPO with clip ratio $\epsilon = 0.2$, GAE parameter $\lambda = 0.95$, entropy coefficient $0.01$, 8 actor epochs, and 10 critic epochs per round.

### Executed Trading Policy Specification (GPTL Output)

The end-deliverable produced by LVPG is a typed rule-based trading program executed on hourly continuous futures bars:
- **Formation Timestamp:** Evaluated at the close of each 1-hour futures bar. Traded on the open of the next hourly bar (`research-proposed execution timestamp convention`).
- **Lookback Windows:** Configured by numeric leaf nodes in the GPTL tree (e.g., EMA windows 10–200 hours, RSI lookbacks 14–48 hours, breakout lookbacks 12–72 hours).
- **Long Entry:** Boolean expression evaluates to `True` (e.g., trend confirmation AND price above moving average band).
- **Long Exit:** Boolean exit expression evaluates to `True` OR fixed stop-loss / holding horizon triggered.
- **Short Entry:** Symmetric or independently evolved Boolean short condition evaluates to `True`.
- **Short Exit:** Symmetric or independently evolved Boolean short exit condition evaluates to `True`.
- **Holding Period:** Multi-hour to multi-day swing holding horizon (minimum 10 trades per training fold required for policy validity).
- **Position Sizing:** Binary fixed unit contract allocation ($\pm 1$ or $0$) per market (`research-proposed fill and sizing model`).

## Required data

- **Instruments:** Continuous hourly futures contracts:
  - S&P 500 E-mini futures (equity index futures).
  - Silver futures (commodity futures).
  - 30-Year US Treasury bond futures (fixed income futures).
- **Data Period:** Historical hourly continuous bars through October 20, 2025:
  - S&P 500 E-mini: 23,915 bars.
  - Silver: 24,020 bars.
  - 30-Year Treasury: 23,947 bars.
- **Timeframe:** 1-hour bar frequency.
- **Fields Required:** OHLCV (Open, High, Low, Close, Volume).
- **Point-in-Time Discipline:**
  - End-anchored rolling-origin folds: 4 months training, 1 month validation, 3-day embargo, 1 month sealed test.
  - Folds are evaluated strictly sequentially with no look-ahead.
  - Champion policy selected once per run on validation data; numeric parameters tuned on validation through at most 64 deterministic backtests without altering program tree logic.
  - Sealed test evaluated exactly once per champion.
- **Missing Data Handling:** Non-trading hours and holiday market closures respected per CME contract specifications; illiquid/untraded bars omitted without forward-fill interpolation.
- **Execution Cost Modeling:** Fixed execution cost deduction per contract round turn applied in the backtesting simulator.

## Execution assumptions

- **Signal-to-Order Timing:** Signal generated at hourly bar close $t$; executed at bar open $t+1$ (`research-proposed`).
- **Order Type:** Market orders assumed filled at the bar open price (`research-proposed`).
- **Fill Model:** Full execution at bar open; no partial fills or market impact modeled in the baseline study.
- **Fees & Commission:** Fixed round-turn commissions incorporated into the backtester (`source-reported`), though explicit dollar/tick fee schedule is not itemized in the paper text (`provenance gap`).
- **Slippage:** Zero execution slippage assumed in baseline simulator (`source-reported limitation`).
- **Leverage & Margin:** Unlevered unit futures position sizing assumed for comparative validation (`research-proposed`).
- **Latency:** 1-hour decision cycle; latency assumed non-binding for swing futures execution.

## Evidence

### Source-reported

All quantitative figures trace directly to Siper, Khalifa, and Togelius (arXiv:2608.13297v1, August 2026, Sections 4–7, Figure 3, Figure 4, Table 2):

1. **Sealed Out-of-Sample Test Champion Performance (Table 2 & Figure 3B):**
   - **Mean Out-of-Sample Sharpe Ratio:**
     - **LVPG (PPO-Path):** **1.321**
     - **PPO-Immediate (Myopic baseline):** **0.862**
     - **Paired Sharpe Gain:** **+0.459** (95% CI: `[0.113, 0.795]`, probability of superiority = `0.633`, Holm-adjusted $p = 0.0188$).
     - Contrast against fixed medium mutation radius: statistically significant ($p < 0.05$).
     - Contrast against uniform mutation selection: statistically significant ($p < 0.05$).
     - Contrast against scheduled mutation decay: statistically significant ($p < 0.05$).
   - **Secondary Financial Endpoints (Descriptive):**
     - **Annualized Return:** **22.8%** (PPO-Path) vs. **15.3%** (PPO-Immediate).
     - **Sortino Ratio:** **2.462** (PPO-Path) vs. **1.623** (PPO-Immediate).
     - **Maximum Drawdown:** **3.87%** (PPO-Path) vs. **4.29%** (PPO-Immediate).
     - **Positive Test Sharpe Frequency:** **86.7%** (PPO-Path) vs. **81.1%** (PPO-Immediate).
   - Paired daily returns evaluated via Ledoit-Wolf studentized circular-block bootstrap (2,000 replicates, automatic block length; Ledoit & Wolf 2008).

2. **Validation Search Performance & Search Efficiency (Section 6, Figure 3A):**
   - **Best-so-far AUC:** PPO-Path increases validation best-so-far AUC by **+0.394** Sharpe units (95% CI: `[0.261, 0.526]`, probability of superiority = `0.822`, Holm-adjusted $p < 0.001$).
   - All five planned validation AUC contrasts remain statistically significant after Holm correction ($p < 0.001$).

3. **Temporary Regressions & Search Dynamics (Section 6):**
   - PPO-Path generates fewer temporary fitness regressions ($F(p_{t+1}) < B_t$): **54.2%** (95% CI: `[53.5%, 54.8%]`) vs. **59.8%** (95% CI: `[58.9%, 60.6%]`).
   - PPO-Path recovers from temporary regressions more frequently: **48.0%** (95% CI: `[46.5%, 49.7%]`) vs. **39.9%** (95% CI: `[38.4%, 41.5%]`).
   - PPO-Path accepts deeper temporary regressions (**0.94** vs. **0.77** Sharpe units) but recovers faster (**1.93** vs. **2.20** steps) and yields greater post-recovery improvement (**+0.535** vs. **+0.251** Sharpe units).

4. **Horizon & Credit Scaling (Section 6, Figure 4):**
   - Moving credit horizon from 1 step to 4 steps raises validation AUC by **+0.399** (95% CI: `[0.146, 0.630]`, adjusted $p = 0.0036$).
   - Moving from 1 step to 8 steps raises validation AUC by **+0.599** (95% CI: `[0.411, 0.795]`, adjusted $p < 0.001$).
   - Moving from 4 steps to 8 steps yields an incremental **+0.200** (95% CI: `[-0.038, 0.451]`, $p = 0.0954$).

5. **Critic Validation & Interventional Value (Section 6):**
   - On 23,040 held-out states excluded from training, critic predictions achieve mean Spearman rank correlation of **0.597** (95% CI: `[0.585, 0.608]`) with realized path returns, explained variance **19.3%**, and MAE **0.509** Sharpe units.
   - After controlling for parent fitness, path best, budget, stagnation, and recent improvement, the critic retains a partial $R^2 = 0.116$ (coefficient $0.361$, 95% CI: `[0.332, 0.388]`).
   - Across 720 held-out interventional states, the controller selects the highest-value action in **51.9%** (95% CI: `[48.2%, 55.8%]`) of states (vs. 33.3% random baseline), with mean regret of **0.157** Sharpe units.

### Independently reproduced

Not independently reproduced. All metrics reflect third-party reported findings from Siper, Khalifa, and Togelius (arXiv:2608.13297v1, August 2026).

### Negative evidence

1. **Omnibus Non-Treasury Inconclusiveness:** While paired contrasts within matched blocks were statistically significant, a conservative omnibus Friedman rank test across the 30 shared blocks yielded $p = 0.265$, indicating that outperformance varies across market regimes and is not uniformly superior on every single asset fold.
2. **Fixed-Cost and Zero-Slippage Idealization:** Backtest evaluation in the primary source assumes fixed execution costs and zero market impact/slippage. In realistic high-turnover trading or during market dislocations, transaction costs could erode the +0.459 Sharpe spread.
3. **Critic Calibration Asymmetry:** The bootstrapped critic tends to overpredict realized returns in the highest predicted quintile; it acts as an informative relative ranker rather than an unbiased point estimator.
4. **Short Out-of-Sample Horizon:** Test folds are 1 month each across 10 folds (10 months aggregate out-of-sample test time per asset). While non-overlapping and strictly embargoed, 10 months does not span multi-year macroeconomic cycles.
5. **No Independent Out-of-Domain Generalization:** The system was evaluated on three liquid futures markets (ES, SI, US); performance on fragmented, 24/7, or illiquid crypto markets is unmeasured.

## Falsification plan

1. **Transaction Cost and Slippage Stress Test:**
   - *Protocol:* Re-evaluate the 90 paired test runs under escalating transaction cost schedules: 0.5, 1.0, 2.0, and 3.0 ticks round-turn slippage plus exchange execution fees.
   - *Failure Rule (`research-defined falsification threshold`):* If the out-of-sample Sharpe advantage of LVPG over PPO-Immediate drops below **0.10** Sharpe units or loses statistical significance ($p \ge 0.05$) under a 1-tick slippage penalty, falsify the claim that LVPG produces economically deployable execution advantage.
2. **True Out-of-Sample Temporal Forward Walk:**
   - *Protocol:* Deploy the frozen LVPG policy discovery engine to generate champion policies on data strictly post-dating October 20, 2025 (e.g., November 2025 through August 2026) across ES, SI, and Treasury futures.
   - *Failure Rule (`research-defined falsification threshold`):* If the forward walk yields mean test Sharpe $< 0.80$ or negative annualized returns across the 3 markets, falsify temporal stability.
3. **Ablation of Critic Head vs. Random Search:**
   - *Protocol:* Replace the bootstrapped LoRA critic with random action selection under identical evaluation budgets ($H = 256$).
   - *Failure Rule (`research-defined falsification threshold`):* If random operator pacing achieves within **0.15** Sharpe units of LVPG validation AUC, reject the hypothesis that value-bootstrapped lineage credit is the causal mechanism driving search efficiency.
4. **Crypto Perpetual Portability Test:**
   - *Protocol:* Apply the LVPG framework to Binance or Bybit BTCUSDT, ETHUSDT, and SOLUSDT 1-hour perpetual futures, incorporating hourly funding rates and taker fees (4 bps).
   - *Failure Rule (`research-defined falsification threshold`):* If net out-of-sample Sharpe is $\le 0.50$ after deducting funding and trading fees, reject direct crypto portability.

## Crypto portability

**unproven**

The primary paper evaluates exclusively US traditional futures (CME S&P 500 E-mini, COMEX Silver, CBOT 30-Year Treasury). Porting to cryptocurrency markets involves substantial structural differences:
- **Session Continuity (24/7 vs. CME Trading Halts):** Continuous futures on CME have weekend closes and maintenance pauses. Crypto perpetual futures operate 24/7/365, which may alter indicator lookbacks, weekend volatility dynamics, and bar boundary alignments.
- **Funding Rate Friction:** Perpetual futures require periodic funding payments (typically every 8 hours). Trading policies discovered by LVPG must explicitly incorporate funding cash flows into the fitness function, otherwise long/short holding periods during high-funding regimes will suffer hidden bleed.
- **Venue Fragmentation & Basis:** Unlike centralized CME clearing, crypto markets feature fragmented liquidity across Binance, OKX, Bybit, and decentralized perpetual protocols (e.g., Hyperliquid), introducing venue-specific basis, liquidation engine behaviors, and divergent slippage dynamics.
- **Taker/Maker Fee Asymmetry:** High-frequency hourly trading rules are highly sensitive to fee tiers (VIP/taker fees of 2–5 bps). LVPG's reward function must be modified to embed fee tiering directly into fitness normalization.

## Limitations

- **Coarse Operator Action Space:** LVPG controls only three discrete mutation radii (`Refine`, `Interpolate`, `Explore`). It does not dynamically adapt semantic instructions or token-level generation.
- **Optimistic Critic Targets:** Critic targets are generated from deterministic depth-5 tree expansions rather than full stochastic policy rollouts, creating systematic upside optimism in critic value estimates.
- **Underspecified Execution Costs in Source:** The primary paper reports that backtests are evaluated net of fixed trading costs, but omits the exact dollar-per-contract commission or tick value used in the backtester (`data gap`).
- **Absence of Live Execution Testing:** All evidence is derived from historical backtesting across rolling folds; no paper, testnet, or live execution evidence is provided.
- **Reliance on Proprietary/Large LLM Infrastructure:** The mutation engine requires hosting an 8-billion parameter language model (Qwen3-8B) with multiple LoRA adapters, requiring substantial GPU compute during the search phase.

## Implementation status

`not-implemented`

This capture represents external published academic research. No implementation exists in our PyBroker or NautilusTrader pipelines. No automated trading system has been authorized or built.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

A record being present in this repository does not indicate strategy adoption, implementation authorization, or permission to trade live or paper capital.

## Related Wiki records

- `[[quant/factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]]` — Program-level factor discovery and LLM code evolution.
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05.md]]` — Grammar-guided MCTS and Tree-LSTM search for symbolic formulaic alpha.
- `[[quant/madevolve-evolutionary-alpha-forecasting-passive-limit-order-bitcoin-2026-09-03.md]]` — Evolutionary alpha discovery for passive limit order placement.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Walk-forward validation with strict embargoing and leakage protection.

## Sources

1. Matthew Siper, Ahmed Khalifa, and Julian Togelius. *"The Time Value of Evolution"*. arXiv preprint `arXiv:2608.13297v1 [cs.LG]`, submitted August 14, 2026.
   - Stable Abstract: [https://arxiv.org/abs/2608.13297](https://arxiv.org/abs/2608.13297)
   - Full Text HTML: [https://arxiv.org/html/2608.13297v1](https://arxiv.org/html/2608.13297v1)
   - Canonical DOI: [10.48550/arXiv.2608.13297](https://doi.org/10.48550/arXiv.2608.13297)
