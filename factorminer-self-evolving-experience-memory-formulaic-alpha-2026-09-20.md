---
schema: strategy-research-record-v1
title: "FactorMiner: Self-Evolving Agent with Experience Memory for Interpretable High-Frequency Formulaic Alpha Discovery"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - alpha-discovery
  - llm
  - factor-mining
  - formulaic-alpha
  - experience-memory
  - cross-market
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - "Yanlong Wang, Jian Xu, Hongkang Zhang, Shao-Lun Huang, Danny Dongning Sun, Xiao-Ping Zhang, 'FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery', arXiv:2602.14670v2 [q-fin.TR, cs.MA], submitted 16 Feb 2026, revised 19 Aug 2026. Published at KDD 2026. DOI: 10.1145/3770855.3818978. https://arxiv.org/abs/2602.14670"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FactorMiner: Self-Evolving Agent with Experience Memory for Interpretable High-Frequency Formulaic Alpha Discovery

## Provenance

- **Paper:** FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery
- **Published at:** ACM SIGKDD 2026 (32nd International Conference on Knowledge Discovery and Data Mining), Jeju Island, Republic of Korea, August 9–13, 2026
- **Authors:** Yanlong Wang, Jian Xu, Hongkang Zhang, Shao-Lun Huang, Danny Dongning Sun, Xiao-Ping Zhang
- **arXiv:** 2602.14670v2 [q-fin.TR, cs.MA], submitted 16 Feb 2026 (v1), revised 19 Aug 2026 (v2)
- **DOI:** [10.1145/3770855.3818978](https://doi.org/10.1145/3770855.3818978)
- **Stable URL:** https://arxiv.org/abs/2602.14670
- **Full-text HTML:** https://arxiv.org/html/2602.14670v2
- **Full-text PDF:** https://arxiv.org/pdf/2602.14670v2
- **Source as-of date:** 2026-09-20 (full HTML text retrieved and audited)
- **Open factor library:** 110 A-share equity factors with explicit formulaic expressions released as supplementary material

**Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2602.14670`, `FactorMiner`, `Yanlong Wang`, `Shao-Lun Huang`, `Xiao-Ping Zhang`, or `Ralph Loop`. Adjacent factor-mining records in the repository (`factorengine-program-level-knowledge-infused-factor-mining-2026-09-05`, `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03`, `alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05`) examine different architectures: FactorEngine uses Turing-complete code evolution, AlphaCrafter uses multi-agent cross-sectional equity factor generation, and AlphaCFG uses grammar-guided MCTS. FactorMiner is materially distinct in its use of structured experience memory and the Ralph Loop self-evolution paradigm for navigating the "Correlation Red Sea."

## Economic mechanism

### Source-reported

FactorMiner addresses a specific bottleneck in formulaic alpha factor mining: as the factor library grows, the space of new orthogonal factors (those with low mutual correlation to existing members) shrinks rapidly — the authors term this the "Correlation Red Sea." Standard search methods (genetic programming, reinforcement learning) lack mechanisms to retain and reuse structural insights across mining sessions, leading to repetitive trials and redundant discoveries.

The proposed mechanism operates through two synergistic components:

1. **Modular Skill Architecture:** Factor mining is packaged as a standalone, reusable agent skill with 60+ GPU-accelerated financial operators, a multi-stage validation pipeline (IC screening → correlation check → replacement check → batch dedup → full validation), and standardized evaluation protocols. This offloads computation to deterministic code, preventing LLM "hallucinated metrics."

2. **Experience Memory:** A structured knowledge base that accumulates insights from historical mining sessions, containing:
   - **Mining State:** Global library evolution metrics, admission logs, saturation signals
   - **Structural Experience:** Successful patterns (e.g., higher-moment regimes via Skew/Kurt, trend-regression adaptivity) and forbidden directions (e.g., VWAP-deviation variants that correlate with existing factors)
   - **Strategic Insights:** High-level lessons (e.g., non-linear combinations outperform linear, high-order moments unstable at high frequency)

The agent follows the **Ralph Loop paradigm**: Retrieve → Generate → Evaluate → Distill. Memory priors guide exploration, shifting the sampling distribution toward regions with higher expected yield and lower redundancy.

### Research interpretation

The core hypothesis is that **meta-learning over factor mining sessions** — accumulating structural knowledge about what works and what fails — enables more efficient discovery of orthogonal, interpretable alpha factors than memoryless search. The economic channel is:

- **Cross-sectional predictive signal construction:** Formulaic alpha factors generate cross-sectional predictive scores (Spearman rank IC) for intraday returns
- **Library diversity constraint:** New factors must maintain low pairwise correlation (≤ 0.45) with existing library members
- **Memory-guided exploration:** Successful pattern templates and forbidden direction regions reduce redundant search, enabling continued discovery even as the library saturates

The released 110-factor library spans VWAP deviation, momentum, regime switches, price-range interactions, divergence, higher moments, median-based transforms, and amount-efficiency signals — providing interpretable, auditable formulaic alphas.

## Signal

### Formation timestamp
Factors are computed on 10-minute intraday bars. The prediction target is the non-overlapping next-step return ratio at the same 10-minute frequency. Signal formation is at bar close; tradability is at the next bar open (research-proposed exact timing).

### Lookback
Not specified for individual factors in the paper; the operator library supports variable lookback windows. The training period is 2024-Q1 to 2024-Q4; the held-out test period is 2025. The full 110-factor library was also evaluated on 2026-Q1 data.

### Entry
Not applicable — FactorMiner is a factor mining/discovery framework, not a complete trading strategy. The released factors provide cross-sectional predictive scores that can be used for long-short portfolio construction. The paper evaluates factor quality via IC, ICIR, and downstream portfolio diagnostics (equal-weight, IC-weighted, Lasso, and XGBoost selection).

### Exit
Not applicable (factor mining framework).

### Holding period
Not applicable (factor mining framework).

### Parameters
- **IC threshold for admission:** `≥ 0.03` (main experiments); `≥ 0.02` (ablation with relaxed thresholds) — both research-defined
- **Redundancy threshold:** `ρ ≤ 0.45` pairwise correlation for admission — research-defined
- **Operator library:** 60+ financial operators (TsRank, Rsquare, Skew, Kurt, VWAP, EMA, etc.)
- **Top-40 factor selection:** Factors selected once on CSI500 (2024) and frozen for cross-market evaluation

The admission thresholds are described as fixed protocol parameters, not learned or tuned per dataset.

## Required data

- **Universe (A-share):** CSI 300, CSI 500, CSI 1000 index constituents; intraday 10-minute bars; over 25 million data points in aggregate
- **Universe (Crypto):** 64 major assets from Binance; 10-minute bars
- **Training period:** 2024-Q1 to 2024-Q4
- **Test period:** 2025 (held-out); additional 2026-Q1 evaluation
- **Fields:** OHLCV + VWAP (implied by operator library); exact field list per factor varies
- **Prediction target:** Non-overlapping next-step return ratio at 10-minute frequency
- **Point-in-time:** Standard OHLCV data; no explicit look-ahead audit protocol described
- **Timestamp:** Intraday 10-minute bars; timezone not explicitly stated (A-share = CST implied; Crypto = UTC implied)

## Execution assumptions

- **Factor evaluation only:** FactorMiner evaluates factor predictive quality (IC/ICIR) and redundancy, not end-to-end trading performance. Transaction-cost-aware deployment is explicitly left for future work.
- **Commission/slippage:** Not modeled in factor evaluation. The paper states "transaction-cost-aware deployment is left for future work."
- **Fill model:** Not applicable (factor evaluation framework).
- **Portfolio construction:** Evaluated via equal-weight, IC-weighted, Lasso, and XGBoost downstream selection. These are diagnostic evaluations, not live trading specifications.

## Evidence

### Source-reported

All figures below trace directly to Wang et al. (arXiv:2602.14670v2, Tables 1–5, Section 4):

**Factor Library Quality (2025 out-of-sample, Top-40 factors, frozen from CSI500 2024):**

| Dataset | IC (%) | ICIR | Avg ρ |
|---------|--------|------|-------|
| CSI500 | 8.25 | 0.77 | 0.31 |
| CSI1000 | 7.78 | 0.76 | 0.30 |
| CSI300 | 7.46 | 0.38 | 0.31 |
| Crypto | 3.82 | 0.28 | 0.25 |

**Factor Combination (IC-weighted, 2025 out-of-sample):**

| Dataset | EW IC (%) | EW ICIR | ICW IC (%) | ICW ICIR |
|---------|-----------|---------|------------|----------|
| CSI500 | 14.95 | 1.29 | 15.11 | 1.31 |
| Crypto | 9.48 | 0.61 | 9.48 | 0.62 |

**Comparison vs. baselines (CSI500 IC/ICIR):** FactorMiner 8.25/0.77 vs. GPLearn 6.04/0.43 vs. AlphaAgent 5.90/0.46 vs. Alpha101 (Adapted) 5.06/0.43 vs. AlphaForge 4.48/0.38 vs. Random 2.68/0.25.

**vs. end-to-end models (CSI500):** FactorMiner 8.25/0.77 vs. LightGBM 5.53/0.51 vs. Chronos-2 4.52/0.37 vs. PatchTST 2.21/0.19.

**Experience Memory ablation (relaxed thresholds):** Have Memory: 96 high-quality candidates (60.0% yield); No Memory: 32 (20.0% yield). Have Memory rejects 55.2% for redundancy vs. 43.8% without memory.

**Temporal persistence (CSI500 full 110-factor library, 2025-10 to 2026-03):** IC ranges 4.78%–6.83%; XGB composite IC 12.56%–16.16%. Factors remain predictive in 2026-Q1.

**Mining efficiency:** GPU backend achieves 8–59× speedup over Pandas; evaluating 1,000 candidates takes 6 minutes vs. 70 minutes with Pandas.

### Independently reproduced

Not independently reproduced. All figures are third-party results reported by Wang et al. (KDD 2026, arXiv:2602.14670v2). No internal factor mining, IC computation, or portfolio evaluation has been executed.

### Negative evidence

- **Crypto IC lower than A-shares:** FactorMiner achieves 3.82% IC on Crypto vs. 8.25% on CSI500, reflecting crypto's higher cross-sectional synchronicity (SYN = 0.66 vs. -1.19 for CSI500) and lower cross-sectional dispersion (CSD = 2.56‰ vs. 4.69‰). The paper acknowledges that adaptive admission thresholds may be needed for different market types.
- **Learned selection adds limited value for FactorMiner:** XGBoost selection on FactorMiner's library provides marginal or slightly negative gains vs. simple IC-weighted combination, suggesting the library is already well-diversified.
- **Transaction costs not modeled:** The paper explicitly states this is future work. High-frequency (10-minute) factors are likely to be highly sensitive to transaction costs.
- **Single training year:** Factors are trained on 2024 data and evaluated on 2025; temporal persistence is tested on 2026-Q1 but long-run decay is unknown.
- **A-share focus of released library:** The 110 released factors are validated on A-share equities; crypto results use a subset selected on CSI500.
- **Publication bias:** Results reported by the paper's own authors; no independent replication exists.

## Falsification plan

1. **Out-of-sample persistence:** Re-evaluate the released 110-factor library on 2026-Q2+ data as it becomes available. If IC drops below 2% or ICIR below 0.15 on CSI500, the temporal stability hypothesis is weakened. [research-defined threshold]
2. **Transaction-cost sensitivity:** Apply realistic 10-minute bar transaction costs (maker/taker fees, spread, slippage) to the factor signals. If net-of-cost IC-weighted portfolio Sharpe falls below 0.5 on A-shares or below 0.0 on crypto, the practical utility hypothesis is weakened. [research-defined threshold]
3. **Crypto-native factor mining:** Run FactorMiner directly on crypto 10-minute data with crypto-adapted admission thresholds (lower IC threshold per the paper's CSD/SYN analysis). Compare against the current cross-market transfer results. If crypto-native mining does not materially improve IC, the cross-market transfer hypothesis is supported but the crypto-specific mechanism hypothesis is weakened.
4. **Memory ablation on crypto:** Repeat the experience memory ablation specifically on the crypto universe. If memory provides less yield improvement on crypto than on A-shares (where memory triples yield), the meta-learning benefit may be market-structure dependent.
5. **Correlation decay:** Monitor pairwise correlations among the top-40 factors over time. If average ρ exceeds 0.50 within 6 months of the evaluation window, the diversity constraint may be insufficient.

## Crypto portability

**adapted**

FactorMiner demonstrates cross-market transfer by evaluating factors mined on A-share CSI500 data on a crypto universe (64 Binance assets, 10-minute bars). The crypto IC/ICIR (3.82%/0.28) is lower than A-share results but still positive, suggesting some transferability.

Crypto-specific portability risks:
- **Higher cross-sectional synchronicity:** Crypto shows SYN = 0.66 (positive co-movement) vs. A-share SYN = -1.19 (negative co-movement). Cross-sectional factor ranking is less discriminating when assets co-move.
- **24/7 trading:** The 10-minute bar frequency applies, but session structure differs (no market open/close effects).
- **No price limits:** A-share 10% daily limits create artificial mean-reversion dynamics absent in crypto.
- **Venue fragmentation:** Factors mined on Binance data may not transfer to other venues.
- **Transaction costs:** 10-minute bar trading incurs meaningful taker fees and slippage that are not modeled.
- **Funding rates:** Perpetual funding costs are not incorporated into factor evaluation.

The released 110-factor library is A-share validated; crypto deployment would require independent validation.

## Limitations

- **Transaction-cost-blind:** Factor evaluation is purely predictive IC/ICIR; no cost-aware backtest exists. 10-minute bar factors are likely highly sensitive to execution costs. `data gap`
- **Single training year:** 2024 training, 2025 test, 2026-Q1 extended test. Long-run factor decay is unknown. `underspecified`
- **No live or paper trading:** The framework has not been deployed in any live or paper trading context. `not independently reproduced`
- **A-share bias:** The released factor library and primary results are A-share focused. Crypto results use a transferred subset. `data gap` for crypto-native factor mining
- **LLM dependency:** The mining agent uses Gemini 3.0 Flash for factor proposal generation. Different LLMs may produce different mining trajectories. `underspecified`
- **Admission thresholds fixed:** IC ≥ 0.03 and ρ ≤ 0.45 are protocol parameters, not learned. Sensitivity to these thresholds is not fully explored. `research-proposed`
- **No comparison with factor timing:** The paper evaluates static factor quality, not dynamic factor timing or regime-adaptive allocation. `data gap`
- **110 factors may still face decay:** As the authors note, "published anomalies may erode after becoming known and arbitraged" and "intraday microstructure signals can have shorter half-lives." The released library's public availability may itself accelerate decay.

## Implementation status

No implementation in our research stack has been completed. The paper provides the algorithmic framework and released factor formulas, but no backtest engine, portfolio construction pipeline, or trading system has been built.

## Adoption boundary

This record is research-only material. A record being present in this repository does not mean:
- Passed Research Intake Review
- Entered Hermes Wiki Brain or the production candidate pool
- Completed Qlib full-backtest validation
- Became a frozen survivor or leaderboard entry
- Profitable, validated alpha, or approved for implementation
- Approved for paper, testnet, or live trading

The factor formulas are public and interpretable; they may serve as starting points for our own factor library construction and ablation testing.

## Related Wiki records

- `[[quant/factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]]` — FactorEngine uses Turing-complete code evolution for alpha mining; FactorMiner uses symbolic formulaic expressions with experience memory. Different expressiveness paradigm.
- `[[quant/alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03]]` — AlphaCrafter uses multi-agent LLM reasoning for equity factor generation; FactorMiner uses a single self-evolving agent with skill architecture.
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — AlphaCFG uses grammar-guided MCTS with Tree-LSTM for formulaic alpha; FactorMiner uses memory-guided LLM generation with deterministic evaluation.
- `[[quant/adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05]]` — PPO-based dynamic weighting of LLM-generated formulaic alphas; complementary to FactorMiner's factor discovery (downstream factor timing vs. upstream factor mining).

## Sources

1. Yanlong Wang, Jian Xu, Hongkang Zhang, Shao-Lun Huang, Danny Dongning Sun, Xiao-Ping Zhang. "FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery." *Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26)*, August 9–13, 2026, Jeju Island, Republic of Korea. arXiv preprint `arXiv:2602.14670v2 [q-fin.TR, cs.MA]`, revised August 19, 2026.
   - Stable URL: https://arxiv.org/abs/2602.14670
   - HTML: https://arxiv.org/html/2602.14670v2
   - PDF: https://arxiv.org/pdf/2602.14670v2
   - DOI: [10.1145/3770855.3818978](https://doi.org/10.1145/3770855.3818978)
