---
schema: strategy-research-record-v1
title: "AlphaLogics: Market Logic-Driven Multi-Agent System for Scalable and Interpretable Alpha Factor Generation"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - multi-agent
  - factor-mining
  - market-logic
  - cross-sectional-equity
  - lightgbm
  - qlib
status: research-only
confidence: medium
source_as_of: 2026-03-24
sources:
  - "Zhangyuhua Weng, Shengli Zhang, Taotao Wang, Yihan Xia, 'AlphaLogics: A Market Logic-Driven Multi-Agent System for Scalable and Interpretable Alpha Factor Generation', arXiv:2603.20247v1 [q-fin.CP, cs.MA], March 2026. DOI: 10.48550/arXiv.2603.20247. https://arxiv.org/abs/2603.20247"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaLogics: Market Logic-Driven Multi-Agent Factor Generation and Optimization

## Provenance

- **Primary Source:** Zhangyuhua Weng, Shengli Zhang, Taotao Wang, and Yihan Xia, "AlphaLogics: A Market Logic-Driven Multi-Agent System for Scalable and Interpretable Alpha Factor Generation", arXiv preprint `arXiv:2603.20247v1 [q-fin.CP, cs.MA]`, submitted March 2026.
- **Canonical DOI:** [10.48550/arXiv.2603.20247](https://doi.org/10.48550/arXiv.2603.20247).
- **Traceable URLs:**
  - Abstract: [https://arxiv.org/abs/2603.20247](https://arxiv.org/abs/2603.20247)
  - Full Text HTML: [https://arxiv.org/html/2603.20247v1](https://arxiv.org/html/2603.20247v1)
  - PDF: [https://arxiv.org/pdf/2603.20247](https://arxiv.org/pdf/2603.20247)
- **Authors & Affiliation:** Zhangyuhua Weng, Shengli Zhang, Taotao Wang, Yihan Xia; College of Electronic and Information Engineering, Shenzhen University, Shenzhen, China.
- **Pre-Write Deduplication Audit:** A comprehensive repository-wide audit on 2026-09-05 verified zero existing records referencing `2603.20247`, `AlphaLogics`, `Zhangyuhua Weng`, `Shengli Zhang`, `Taotao Wang`, or `Yihan Xia`. Adjacent agentic factor mining records in the repository (`agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04.md`, `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md`, `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03.md`, `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md`) focus on prompt token economies, software test harnesses, reinforcement reasoning with GRPO, or genetic institutional volume correlation. AlphaLogics is structurally distinct in its explicit two-level nested loop that isolates market logic $H = \langle \mathcal{C}, \mathcal{B} \rangle$ as an interpretable, verifiable, and iteratively refined intermediate object compiled into executable domain-specific language (DSL) constraints $\Gamma$.

## Economic mechanism

### Source-reported

The authors argue that quantitative factor investing is historically divided between two extremes:
1. **Manual market logic-driven factor design:** Factors are derived from human economic hypotheses (e.g., Fama-French size/value/profitability, Alpha191 price-volume momentum and reversal). These have clear behavioral or economic rationale and high interpretability, but discovery is slow, handcrafted, and difficult to scale across high-dimensional data.
2. **Automated data-driven and LLM-driven factor mining:** Machine learning and generative AI can generate thousands of candidate factor formulas (e.g., Alpha101 genetic programming, Alpha-GPT, AlphaAgent). However, these systems optimize formula expressions directly without explicit market logic, producing opaque formulas prone to data mining, spurious correlations, and severe out-of-sample decay across market regimes.

AlphaLogics bridges this gap by treating **market logic** itself as an explicit, verifiable, and optimizable intermediate representation. Market logic is formalized as a pair:
$$H = \langle \mathcal{C}, \mathcal{B} \rangle$$
where:
- $\mathcal{C}$ is a conjunction or disjunction of market predicates $c_i = (v, \text{op}, \theta, w)$ over market variables $v$ (e.g., price, volume), comparison operators $\text{op}$, threshold/quantile $\theta$, and lookback window $w$.
- $\mathcal{B} = (y, d, h)$ specifies the target asset return $y$, directional prediction $d \in \{+1, -1\}$ (long vs. short reversal/momentum), and forecasting horizon $h$.

The framework operates via three coordinated stages:
1. **Market Logic Mining:** Reverse-extracts latent economic logic from established public factor libraries (Alpha101, Alpha191, Alpha158, Alpha360) using a three-agent pipeline (`FormulaStructureAgent` $\to$ `FinancialSemanticsMappingAgent` $\to$ `MarketLogicAbstractionAgent`) to build an initial logic library $\mathcal{H}_{\text{init}}$.
2. **Guided Factor Generation (Inner Loop):** Given a market logic $H$, `LogicToFinanceConstraintAgent` compiles $H$ into executable constraints $\Gamma = \text{Compile}(H^{\text{struct}})$. Candidate factors $F$ are generated within $\Gamma$ by `FactorExpressionGeneratorAgent`, evaluated via a backtest engine on training and validation sets ($D_{\text{train}}, D_{\text{val}}$), and refined using structured feedback from `FactorPerformanceFeedbackAgent`.
3. **Market Logic Generation & Optimization (Outer Loop):** When factor performance under a fixed logic saturates (early stopping $T_{\text{early}} = 3$), `MarketLogicRefinementDirectionAgent` synthesizes cross-factor performance and diagnostics to propose logic-level refinements. `MarketLogicGeneratorAgent` produces new or restructured market logic $H^{\text{new}}$, expanding the persistent logic library $\mathcal{H}_{\text{lib}}$.

### Research interpretation

AlphaLogics establishes a hierarchical two-loop search architecture:
- **Inner loop (exploitation & expression tuning):** Searches the discrete space of mathematical expressions within a constrained sub-grammar defined by $\Gamma$. The compilation step $\Gamma = \text{Compile}(H^{\text{struct}})$ constrains allowed variables (e.g., requiring both price and volume), permissible operator families (e.g., `{rank, zscore, ts_delta, ts_corr, ts_mean}`), parameter ranges ($w, \ell \in \mathbb{N}^+$), and expected sign/direction (e.g., enforcing negative IC for reversal logic). This eliminates unproductive exploration of economically nonsensical combinations.
- **Outer loop (exploration & hypothesis evolution):** Searches the continuous semantic space of market hypotheses. By aggregating feedback across multiple factor realizations of the same hypothesis, the outer loop diagnoses structural flaws in the hypothesis itself (e.g., whether a volume-price divergence requires an additional volatility filter or a specific candlestick body ratio) rather than endlessly tweaking arithmetic constants.

The underlying economic premise is that market anomalies reflect persistent behavioral frictions (e.g., retail overreaction to price surges without institutional volume confirmation, or inventory absorption during liquidity dry-ups) that can be parameterized as logical state transitions. Constraining symbolic factor discovery to search only along these behavioral paths prevents overfitting to noise.

## Signal

### Signal Construction & Logic Compilation

- **Market Logic Formalism:** $H = \langle \mathcal{C}, \mathcal{B} \rangle$, where $\mathcal{C} = \bigwedge_i c_i$ or $\bigvee_i c_i$ with $c_i = (v, \text{op}, \theta, w)$ and $\mathcal{B} = (y, d, h)$ [source-reported].
- **Compilation into Executable Constraints $\Gamma$:** Deterministic mapping via `LogicToFinanceConstraintAgent` [source-reported]:
  - **Required variables:** e.g., $\{ \text{price}, \text{volume} \}$
  - **Allowed operator families:** Arithmetic (`+`, `-`, `*`, `/`), Cross-sectional (`rank`, `zscore`, `mean`, `std`, `skew`, `kurt`, `max`, `min`, `median`), Time-series aggregation (`ts_mean`, `ts_sum`, `ts_rank`, `ts_zscore`, `ts_std`, `ts_min`, `ts_max`), Time-series change (`ts_delta`, `ts_pctchange`, `delay`), Time-series relation (`ts_corr`, `ts_cov`), Smoothing/decay (`decaylinear`, `sma`, `wma`, `ema`), Technicals (`rsi`, `macd`, `bb_upper`, `bb_lower`, `bb_middle`) [source-reported, Appendix A.2–A.3].
  - **Parameter bounds:** Lookback window $w \in \mathbb{N}^+$, lag $\ell \in \mathbb{N}^+$ [source-reported].
  - **Directional consistency:** Filter candidates whose validation IC sign contradicts direction $d$ [source-reported].
- **Factor Combination Model:** LightGBM gradient boosting decision tree [source-reported].
  - **Base Factors:** 4 standardized baseline features: (1) intraday return, (2) daily return, (3) 20-day relative volume, (4) normalized daily range [source-reported].
  - **Generated Factors:** Factors generated and selected by AlphaLogics concatenated with base features [source-reported].
  - **Normalization:** Cross-sectional Z-score transformation applied to all features and forward returns per date [source-reported].
  - **Target Variable:** Next-period cross-sectional return $r_{t+1}$ [source-reported].

### Operational Trading Rules

- **Signal Formation Timestamp:** Formed daily at market close using daily OHLCV bars [source-reported].
- **Lookback Windows:** Parameterized per operator within $w \in [1, 252]$ trading days [source-reported / `research-proposed` upper bound].
- **Portfolio Selection (Top-Outside Rule):**
  - Cross-sectional ranking of all universe constituents by LightGBM predicted return score [source-reported].
  - **Long Entry:** Top 50 highest-ranked stocks [source-reported].
  - **Short / Exclude Rule:** Exclude the 5 lowest-ranked stocks [source-reported, top-outside convention].
- **Position Sizing:** Equal-weighted across the selected top 50 long portfolio [`research-proposed` operational baseline; source evaluates top-50 portfolio return in Qlib].
- **Holding Period & Rebalancing:** Daily rebalancing at close (1-day holding horizon $h = 1$) [source-reported].
- **Execution Fill Model:** Next-bar market-on-close or market-on-open fill assumption in Qlib [`research-proposed` standard fill model].
- **Search Budget & Early Stopping:**
  - Inner loop early stopping threshold: $T_{\text{early}} = 3$ consecutive non-improving candidates on validation objective $J(R_{\text{val}})$ [source-reported].
  - Aligned budget: 20 trials with 5 evolution rounds using LLM backend (GPT-3.5-turbo, DeepSeek-V3, Gemini-2.5-Flash evaluated) [source-reported].

## Required data

- **Instruments:** Equities; evaluated on CSI 500 (China A-share) and S&P 500 (U.S.) [source-reported].
- **Data Providers:** Baostock for CSI 500; Yahoo Finance (`yfinance`) for S&P 500 [source-reported].
- **Timeframe:** Daily OHLCV bars [source-reported].
- **Fields:** Open, High, Low, Close, Volume; plus derived intraday return, daily return, 20-day relative volume, and normalized daily range [source-reported].
- **Universe Filter:** Stocks with fewer than 100 historical trading days are excluded [source-reported].
- **Temporal Partitions:**
  - Training Period ($D_{\text{train}}$): 2015-01-01 to 2019-12-31 (5 years) [source-reported].
  - Validation Period ($D_{\text{val}}$): 2020-01-01 to 2020-12-31 (1 year, strictly reserved for early stopping, feedback, and model selection) [source-reported].
  - Out-of-Sample Test Period ($D_{\text{test}}$): 2021-01-01 to 2024-12-31 (4 years, held-out evaluation) [source-reported].
- **Point-in-Time & Leakage Protection:** Strict temporal splitting; LightGBM fitted on $D_{\text{train}} \cup D_{\text{val}}$ only after model/factor selection on $D_{\text{val}}$ is finalized; factor values and cross-sectional Z-scores computed without future look-ahead [source-reported].

## Execution assumptions

- **Transaction Costs (Source-Reported):**
  - **CSI 500:** Buy fee = 0.0005 (5 bps); Sell fee = 0.0015 (15 bps, accounting for Chinese stamp duty) [source-reported].
  - **S&P 500:** Buy fee = 0.0000 (0 bps); Sell fee = 0.0005 (5 bps) [source-reported].
- **Slippage:** 0 bps explicitly modeled in baseline paper backtest; slippage stress testing is [`research-proposed`].
- **Fill Timing:** Daily execution at close; price-taker assumption without market impact [source-reported].
- **Borrow / Shorting:** Long top-50 portfolio with bottom-5 excluded; long-only cash portfolio with equal weights [`research-proposed` interpretation of Qlib top-outside long portfolio].
- **Capacity / Participation Cap:** Not explicitly reported in paper; 1% of ADV participation cap [`research-proposed`].

## Evidence

### Source-reported

All figures below are transcribed directly from Table 1, Table 2, and Table 3 of Weng et al. (arXiv:2603.20247v1), evaluated on held-out out-of-sample test period (2021.01–2024.12) net of stated transaction costs:

**1. Main Benchmark Results on Held-Out Test Period (2021.01–2024.12, Table 1):**

| Model Class | Method | CSI 500 IC | CSI 500 ICIR | CSI 500 AR (%) | CSI 500 IR | CSI 500 MDD (%) | S&P 500 IC | S&P 500 ICIR | S&P 500 AR (%) | S&P 500 IR | S&P 500 MDD (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Deep Time-Series** | LSTM (Graves, 2012) | 0.0162 | 0.1173 | 6.33% | 0.8494 | -10.45% | 0.0032 | 0.0177 | -7.29% | -0.9732 | -21.91% |
| | Transformer (Vaswani et al., 2017) | 0.0150 | 0.1234 | 4.03% | 0.3650 | -22.85% | 0.0014 | 0.0108 | 0.82% | 0.0952 | -17.71% |
| | GRU (Chung et al., 2014) | 0.0115 | 0.0994 | -1.71% | -0.1733 | -22.05% | 0.0050 | 0.0297 | -1.14% | -0.0970 | -32.10% |
| | MLP (Taud & Mas, 2017) | 0.0115 | 0.0975 | 5.42% | 0.4671 | -23.34% | -0.0007 | -0.0056 | -1.09% | -0.1432 | -23.33% |
| **Tree / Boosting** | LightGBM (Ke et al., 2017) | 0.0116 | 0.0972 | 0.88% | 0.0782 | -24.37% | -0.0014 | -0.0131 | -1.23% | -0.1517 | -28.28% |
| | XGBoost (Chen, 2016) | 0.0122 | 0.1066 | 5.37% | 0.4372 | -26.33% | -0.0028 | -0.0056 | -0.65% | -0.0936 | -22.63% |
| **Quant Model** | TRA (Lin et al., 2021) | 0.0199 | 0.1765 | 1.60% | 0.1467 | -26.11% | 0.0030 | 0.0204 | -3.92% | -0.4541 | -34.15% |
| **Direct LLM Gen** | O3-mini (OpenAI, 2025b) | 0.0171 | 0.1673 | 5.22% | 0.5819 | -10.64% | 0.0021 | 0.0242 | 3.31% | 0.2404 | -19.94% |
| | Deepseek-V3.1 (DeepSeek, 2025) | 0.0184 | 0.1758 | 4.93% | 0.4861 | -16.71% | 0.0026 | 0.0246 | 3.73% | 0.2270 | -20.40% |
| **Agentic Mining** | AlphaForge (Shi et al., 2025) | 0.0111 | 0.1345 | 3.15% | 0.3020 | -25.28% | 0.0026 | 0.0326 | 2.13% | 0.3130 | -28.00% |
| | RD-Agent (Li et al., 2025) | 0.0112 | 0.0966 | 1.01% | 0.0930 | -22.27% | 0.0019 | 0.0165 | 1.61% | 0.1873 | -17.73% |
| | AlphaAgent (Tang et al., 2025) | 0.0221 | 0.2092 | 12.46% | 1.2230 | -6.65% | 0.0060 | 0.0515 | 8.57% | 0.9653 | -9.44% |
| **Proposed System** | **AlphaLogics** | **0.0251** | **0.2312** | **16.72%** | **1.5266** | **-5.31%** | **0.0093** | **0.0878** | **13.75%** | **1.2658** | **-9.06%** |

*Note: AR = Annualized Return; IR = Information Ratio (annualized excess return / tracking error); IC = Spearman rank Information Coefficient; ICIR = mean(IC)/std(IC); MDD = Maximum Drawdown. All reported results reflect net performance after transaction costs.*

**2. Reconstruction Consistency of Market Logic Mining (Table 2):**
Rebuilding factor formulas from extracted explanations across 100 evaluation trials with Gemini-2.5-Flash:
- Alpha101: Mathematical Explanation Consistency = 97.5%; Financial Explanation Consistency = 92.7%
- Alpha158: Mathematical Explanation Consistency = 98.1%; Financial Explanation Consistency = 95.5%
- Alpha360: Mathematical Explanation Consistency = 100.0%; Financial Explanation Consistency = 98.8%
- Alpha191: Mathematical Explanation Consistency = 94.9%; Financial Explanation Consistency = 93.8%

**3. Persistence Ablation (Inner Loop Multi-Round Optimization, Table 3):**
Comparing transient market logic (used once) vs. persistent market logic (optimized across 5 rounds):
- Round 1: Transient IC = 0.0182, ICIR = 0.1776; Persistent IC = 0.0199, ICIR = 0.1792
- Round 2: Transient IC = 0.0181, ICIR = 0.1794; Persistent IC = 0.0208, ICIR = 0.1951
- Round 3: Transient IC = 0.0188, ICIR = 0.1767; Persistent IC = 0.0214, ICIR = 0.2033
- Round 4: Transient IC = 0.0169, ICIR = 0.1556; Persistent IC = 0.0222, ICIR = 0.2071
- Round 5: Transient IC = 0.0165, ICIR = 0.1320; Persistent IC = 0.0232, ICIR = 0.2137
*Finding: Transient logic degrades by Round 5 (IC 0.0182 $\to$ 0.0165, ICIR 0.1776 $\to$ 0.1320), whereas persistent logic steadily improves (IC 0.0199 $\to$ 0.0232, ICIR 0.1792 $\to$ 0.2137).*

### Independently reproduced

Not independently reproduced. All figures above are source-reported extractions directly verified against the primary arXiv text and PDF tables.

### Negative evidence

- **Unconstrained LLM Mining Instability:** Direct factor generation using LLMs without market logic constraints (O3-mini, DeepSeek-V3.1) yields modest performance (CSI 500 AR: 4.93%–5.22%, S&P 500 AR: 3.31%–3.73%) and high drawdown (-16.71% to -20.40%), confirming that unconstrained LLM factor generation struggles with noisy financial data.
- **Transient Logic Degradation:** Table 3 demonstrates that generating fresh market logic in each round without accumulating backtest feedback leads to performance degradation by round 4–5 (IC dropping to 0.0165, ICIR dropping to 0.1320), showing that hypothesis generation without iterative refinement decays rapidly.
- **S&P 500 IC Magnitude:** Absolute rank IC on S&P 500 remains below 0.01 (0.0093 for AlphaLogics), reflecting the extreme informational efficiency and factor crowding in U.S. large-cap equities.
- **Omission of Market Impact & Execution Slippage:** The backtests use zero slippage and mid/close fills. In practical execution, daily rebalancing of 50 equities can suffer substantial turnover friction that could erode the 13.75% S&P 500 annual return.

## Falsification plan

To falsify the claim that market logic constraints provide genuine out-of-sample alpha rather than in-sample LLM search overfitting:

1. **Random / Inverted Logic Constraint Test (Ablation Test):** Replace compiled constraints $\Gamma$ with intentionally inverted directional constraints (e.g., enforce positive IC when reversal predicts negative IC) or randomly permuted operator restrictions.
   - *Metric:* Test period IC and IR.
   - *Research-defined falsification threshold:* If factors generated under inverted or random logic achieve test IR within 15% of AlphaLogics, the market logic constraint mechanism is falsified as causal alpha.
2. **Deflated Sharpe Ratio / Multiple Testing Correction:** Account for the cumulative number of LLM-generated factor candidates across the 20 trials and 5 evolution rounds.
   - *Metric:* Deflated Sharpe Ratio (DSR) using Bailey & López de Prado (2014).
   - *Research-defined falsification threshold:* DSR $p$-value $> 0.05$ on $D_{\text{test}}$.
3. **Execution Friction & Turnover Stress Test:** Apply realistic execution frictions:
   - Variable slippage: 2 bps, 5 bps, 10 bps per trade.
   - Half-spread costs: 5 bps.
   - *Research-defined falsification threshold:* If net Annualized Return drops below benchmark return (S&P 500 Buy & Hold) at 5 bps round-trip slippage, the strategy is unviable for institutional production.
4. **Subperiod Regime Breakdown:** Evaluate performance separately during distinct macro regimes:
   - 2021 Quantitative Easing / Momentum regime.
   - 2022 Federal Reserve Rate Hikes / High-volatility crash regime.
   - 2023–2024 Tech-led concentration regime.
   - *Research-defined falsification threshold:* Maximum drawdown exceeding -20% in any individual calendar year or negative Sharpe ratio across any 12-month rolling window.
5. **Action on Failure:** Reject AlphaLogics factor generation for automated production; isolate individual extracted formulas for standard single-factor econometric vetting.

## Crypto portability

**Portability Status:** Adapted / Unproven.

The primary paper evaluates exclusively on traditional equity indices (CSI 500 and S&P 500). Porting AlphaLogics to cryptocurrency markets is a research adaptation and must be considered unproven until empirically validated in crypto environments:

- **Market Microstructure & 24/7 Trading:** Crypto trades continuously without market closes. The daily bar aggregation convention (00:00 UTC cutoff) creates arbitrary boundaries that can distort volume and candlestick body metrics.
- **Perpetual Futures & Funding Rates:** In crypto perpetual futures, holding costs are dominated by 8-hour funding rates. AlphaLogics currently optimizes solely for price return $r_{t+1}$ without incorporating funding rate drag or basis yield.
- **Cross-Sectional Dynamics & Beta Dominance:** Crypto altcoin universes exhibit massive co-movement and beta correlation with BTC and ETH. Cross-sectional ranking models (top 50) in crypto often pick high-beta tokens during bull runs and suffer catastrophic drawdowns during market corrections unless strict market-beta neutralization is applied.
- **Data Quality & Venue Fragmentation:** Baostock and Yahoo Finance provide consolidated exchange prices; crypto prices and volumes are fragmented across Binance, OKX, Bybit, Coinbase, and DEX liquidity pools. Divergence between venues introduces synthetic volume signals that may mislead LLM logic extractors.
- **Adapted Crypto Universe [`research-proposed`]:** Top 50 liquid perpetual contracts on Binance/OKX with 24-hour volume $> \$20\text{M}$, rebalanced daily at 00:00 UTC with funding cost inclusion and a strict beta-neutralization constraint.

## Limitations

- **Source Code Availability Gap:** While the authors describe the multi-agent architecture, prompt schemas (Appendix A.7), and DSL operators in detail, the proprietary agent orchestration code is not provided in an immutable GitHub repository.
- **No Slippage or Market Impact Modeling:** Qlib backtests assume instant fill at closing prices without market impact or execution delay, inflating reported returns.
- **LLM API Cost & Latency:** Generating, compiling, and validating hundreds of factor candidates across multiple LLM agents introduces notable computational latency and token expense.
- **Evaluation Restricted to Equities:** Empirical validation is limited to China and US equities over a single 4-year test window (2021–2024); cross-asset universality (commodities, FX, crypto) remains unproven.
- **Base Feature Confounding:** The LightGBM model trains on 4 base features in addition to generated factors. While ablation studies show generated factors improve metrics, the interaction between base features and generated factors is not fully decoupled.

## Implementation status

`not-implemented`. This record represents an external research capture. No code has been integrated into `nautilus-quant-system`, PyBroker, or NautilusTrader. No trading strategy family has been instantiated, and no paper, testnet, or live trading has been authorized.

## Adoption boundary

- **Status:** `research-only`
- **Implementation Status:** `not-implemented`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This document is a research hypothesis capture and does not constitute approval for live execution, capital allocation, or strategy adoption. Any future adoption must undergo formal isolated validation in PyBroker (Loop B) followed by event-driven historical backtesting in NautilusTrader.

## Related Wiki records

- `[[quant/alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03]]` — Multi-agent cross-sectional equity alpha generation with test harness validation.
- `[[quant/agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04]]` — Adversarial multi-agent prompt economy for alpha factor search.
- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]` — LLM reasoning with GRPO reinforcement learning for alpha factor screening.
- `[[quant/quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05]]` — Evolutionary factor mining with institutional price-volume correlation.
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery.
- `[[quant/cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03]]` — Econometric selection of Alpha191 factors using double-selection LASSO.

## Sources

1. Zhangyuhua Weng, Shengli Zhang, Taotao Wang, and Yihan Xia, *"AlphaLogics: A Market Logic-Driven Multi-Agent System for Scalable and Interpretable Alpha Factor Generation"*, arXiv preprint `arXiv:2603.20247v1 [q-fin.CP, cs.MA]`, submitted March 2026.
   - Abstract: [https://arxiv.org/abs/2603.20247](https://arxiv.org/abs/2603.20247)
   - Full Text HTML: [https://arxiv.org/html/2603.20247v1](https://arxiv.org/html/2603.20247v1)
   - Full Text PDF: [https://arxiv.org/pdf/2603.20247](https://arxiv.org/pdf/2603.20247)
   - Canonical DOI: [10.48550/arXiv.2603.20247](https://doi.org/10.48550/arXiv.2603.20247)
2. Z. Kakushadze, "101 Formulaic Alphas", *Wilmott*, 2016.
3. Guotai Junan Securities, "Alpha 191 Factors", 2025.
4. Microsoft Qlib Team, "Alpha158 and Alpha360 Factor Libraries", *Qlib Platform*, 2025.
5. G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. Liu, "LightGBM: A Highly Efficient Gradient Boosting Decision Tree", *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.
