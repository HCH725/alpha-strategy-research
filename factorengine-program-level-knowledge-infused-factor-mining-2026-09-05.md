---
schema: strategy-research-record-v1
title: "FactorEngine: Program-Level Knowledge-Infused Alpha Factor Mining via Turing-Complete Code Evolution"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - alpha-discovery
  - llm
  - factor-mining
  - program-synthesis
status: research-only
confidence: medium
source_as_of: 2026-09-05
sources:
  - "https://arxiv.org/abs/2603.16365"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FactorEngine: Program-Level Knowledge-Infused Alpha Factor Mining via Turing-Complete Code Evolution

## Provenance

- **Paper:** FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment
- **arXiv:** 2603.16365v1 (submitted 2026-03-17), v2 (submitted 2026-04-09)
- **Authors:** Qinhong Lin, Ruitao Feng, Yinglun Feng, Zhenxin Huang, Yuken Chen, Zhongliang Yang, Linna Zhou, Binjie Fei, Jiaqi Liu, Yu Li
- **Affiliations:** Not explicitly stated in the paper; Chinese institutional affiliations implied by Chinese A-share focus and CNY-denominated portfolio
- **Primary source URL:** https://arxiv.org/abs/2603.16365
- **PDF:** https://arxiv.org/pdf/2603.16365
- **Public GitHub repo:** Not available at time of capture (data gap)
- **Source as-of date:** 2026-09-05 (arXiv v2 retrieved)

## Economic mechanism

### Source-reported

FactorEngine posits that alpha factor mining is fundamentally a program-synthesis problem: factors should be expressed as Turing-complete executable code (Python programs) rather than constrained symbolic expressions (DSL, formulaic alphas). The authors identify three limitations of existing approaches:

1. **Bounded expressiveness** of symbolic factors constrained by predefined operator spaces
2. **Limited factor diversity and stability** — inability to integrate financial theory from unstructured reports into executable factors
3. **Inefficient evolution pipelines** — speed mismatch between LLM generation and backtest evaluation

The proposed mechanism operates through three separations:
- **Logic separation:** macro-level program logic/idea evolution (LLM-driven) vs. micro-level hyperparameter optimization (Bayesian search)
- **Search strategy separation:** LLM-guided directional search vs. automated Bayesian search
- **Resource separation:** LLM utilization vs. local computation

A **knowledge-infused bootstrapping module** transforms unstructured financial research reports into executable factor programs through a closed-loop multi-agent pipeline (PDF processing → factor extraction → code generation with iterative verification). An **experience knowledge base** supports trajectory-aware refinement, learning from both successes and failures.

### Research interpretation

This is an **alpha factor discovery framework**, not a specific trading signal. The falsifiable hypothesis is that program-level (Turing-complete) factor representations, combined with knowledge-infused initialization from financial reports and experience-driven evolution, produce factors with higher predictive stability and portfolio impact than constrained symbolic approaches or neural-only methods.

The core economic claim is that financial research reports contain structured alpha hypotheses that can be automatically extracted, compiled into executable code, and iteratively refined through backtest feedback — producing a compounding knowledge advantage over purely generative approaches.

This framework belongs to the **meta-alpha** or **alpha-mining-tooling** family, similar to AlphaCFG, AlphaCrafter, AlphaR1, AlphaLogics, and QuantEvolver, but with a materially distinct representation (program-level vs. DSL/formulaic/grammar-constrained) and a knowledge-infused bootstrapping mechanism.

## Signal

FactorEngine does not produce a single fixed signal. It is a **factor discovery engine** that generates an evolving pool of programmatic alpha factors. The signal characteristics of the discovered factors are:

- **Formation timestamp:** Factors operate on daily close OHLCV data (Chinese A-share market); signal generated at close of trading day t
- **Lookback:** Variable per discovered factor; the framework uses a configurable lookback window L (default varies by experiment)
- **Entry:** Top-50 stock ranking by composite predictive signal from discovered factor pool; equal-weight allocation within each tranche
- **Exit:** 5-day rolling holding period; each sub-portfolio liquidated at maturity
- **Re-entry:** Continuous rolling: on each trading day, liquidate the oldest tranche and reinvest in top-50 ranked stocks
- **Parameters:** Factor-specific parameters optimized via Bayesian search; evolution controlled by LLM-guided logic revision
- **Position sizing:** Equal-weight across 5 overlapping sub-portfolios; minimum 1 lot (100 shares); volume limit ≤10% of daily trading volume

The factor expressions are Turing-complete Python programs, enabling complex control flows, conditional logic, iterative computation, and higher-order feature interactions beyond what DSL-constrained systems can express.

## Required data

- **Instrument:** Chinese A-share equities (Shanghai and Shenzhen)
- **Universe:** Full A-share market with liquidity filtering (paper uses top-50 stock selection from a broader universe)
- **Venue:** Chinese A-share market (SSE/SZSE)
- **Market type:** Spot equity (no derivatives)
- **Timeframe:** Daily bars (OHLCV)
- **Fields:** Open, High, Low, Close, Volume; additional derived features from OHLCV via programmatic factor logic
- **Point-in-time:** Standard market data availability; no explicit point-in-time treatment described beyond standard backtesting conventions
- **Timestamp:** Trading day close (CST)
- **Missing-data:** Not explicitly addressed in the paper (data gap)
- **Funding/fee/spread:** Commission 1.5×10⁻⁴ (bilateral), stamp duty 5×10⁻⁴ (sell-side only), slippage 8×10⁻⁴ (proportional); modeled in backtests

## Execution assumptions

- **Signal-to-order timing:** End-of-day signal, next-day execution assumption (standard for daily factors)
- **Order type:** Market order assumed
- **Fill model:** Proportional slippage of 8×10⁻⁴ on all trades
- **Fees:** Bilateral commission 1.5×10⁻⁴ + sell-side stamp duty 5×10⁻⁴
- **Slippage:** 8×10⁻⁴ proportional (explicitly modeled)
- **Impact / capacity:** Volume limit ≤10% of daily trading volume per stock; initial capital CNY 100,000,000
- **Leverage / margin:** Not applicable (long-only equity)
- **Partial fills / failures:** Not explicitly addressed (data gap)
- **Minimum trading unit:** 1 lot = 100 shares (Chinese A-share convention)

## Evidence

### Source-reported

Source reports the following performance metrics for FactorEngine on Chinese A-share backtests (Appendix 0.A, paper Tables):

- **58% improvement in Information Coefficient (IC)** compared to Alpha158 baseline
- **126% increase in excess annual return** compared to Alpha158 baseline
- Higher IC/ICIR and Rank IC/ICIR than baseline methods (GPLearn, Transformer, LSTM, TRA, LightGBM)
- Improved AR/Sharpe over baselines
- Enhanced factor pool diversity compared to state-of-the-art methods
- Knowledge-infused seeds from financial reports provide measurable improvement over randomly initialized seeds

The paper uses a realistic cost model aligned with Chinese A-share market conventions (commission, stamp duty, slippage, lot size, volume limits). Backtests use real-world OHLCV data.

This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

Notable caveats from the paper:
- Results are specific to Chinese A-share market — generalizability to other markets (including crypto) is untested
- The 5-day holding period and top-50 stock selection are parameter choices that may be overfit to the sample
- No out-of-sample or walk-forward validation is explicitly described beyond standard backtesting
- The knowledge-infused bootstrapping depends on the quality and availability of Chinese-language financial research reports

## Falsification plan

1. **Out-of-sample / walk-forward test:** Run FactorEngine on a held-out time period (e.g., 2024-2025) not used in any evolution or hyperparameter tuning; require IC > 0 and Sharpe > 0 after costs
2. **Parameter perturbation:** Vary holding period (3, 5, 10, 20 days), number of top-N stocks (30, 50, 100), and commission/slippage assumptions (±50%); if performance collapses, the original result is fragile
3. **Ablation — knowledge infusion:** Run FactorEngine without the knowledge-infused bootstrapping module (random initialization only); if the IC improvement disappears, the bootstrapping is the primary driver, not the evolution
4. **Ablation — program-level vs. DSL:** Replace program-level factors with DSL-constrained factors (e.g., Alpha158-style expressions); if performance gap narrows, the Turing-complete representation is not essential
5. **Alternative universe:** Apply to a non-Chinese market (e.g., US equities or crypto); if performance degrades substantially, the result is market-specific
6. **Regime decomposition:** Evaluate separately in bull, bear, and sideways regimes; if alpha is concentrated in one regime, the strategy is regime-dependent
7. **Failure threshold:** Reject if IC < 0.02 or Sharpe < 0.5 after realistic costs in the out-of-sample period

## Crypto portability

**unproven**

FactorEngine is designed for and evaluated exclusively on Chinese A-share equities. Crypto portability requires addressing:

- **Market structure:** Chinese A-share T+1 settlement, lot-size constraints, and stamp duty have no direct crypto equivalent
- **Data availability:** Crypto markets have different data streams (funding, open interest, on-chain) not captured by OHLCV-only factors
- **Universe characteristics:** Crypto is a single-asset or small-universe problem; FactorEngine's cross-sectional ranking approach assumes a large equity universe
- **Volatility and non-stationarity:** Crypto markets are far more volatile and regime-dependent than A-shares
- **24/7 session:** No concept of "trading day close" in crypto

The program-level factor representation (Turing-complete Python) is general enough to handle crypto-specific data, but the framework would need substantial adaptation for single-asset or small-universe crypto trading. The knowledge-infused bootstrapping module would need a corpus of crypto-relevant research reports.

## Limitations

- **Chinese A-share only:** No evidence of generalizability to other markets or crypto
- **Daily frequency:** Factors operate on daily bars; no intraday or high-frequency application demonstrated
- **Long-only:** Only long-stock selection is demonstrated; no short-selling, derivatives, or cross-asset application
- **No public code:** No publicly available implementation at time of capture; reproducibility is limited
- **Overfitting risk:** Evolution over 40+ iterations with LLM guidance may overfit to the training period; no explicit out-of-sample or walk-forward validation described
- **Knowledge dependency:** Quality of bootstrapped factors depends on the availability and quality of Chinese-language financial research reports
- **Parameter sensitivity:** Holding period (5 days), top-N selection (50 stocks), and cost assumptions may be sample-specific
- **No regime analysis:** No decomposition of performance across bull/bear/sideways markets
- **Not independently reproduced**

## Implementation status

not-implemented

No implementation in our research stack (PyBroker/Nautilus) has been completed. The paper does not provide a public GitHub repository. The framework requires an LLM API, a backtesting engine, and Bayesian optimization infrastructure.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:

- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

FactorEngine is a **factor discovery framework**, not a specific trading strategy. The factors it discovers would need individual validation before any implementation consideration.

## Related Wiki records

- [[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]] — AlphaCFG: grammar-constrained DSL factor generation via MCTS + Tree-LSTM; material distinction in representation (DSL vs. program-level)
- [[quant/alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03]] — AlphaCrafter: multi-agent cross-sectional equity alpha framework; material distinction in approach (multi-agent workflows vs. bootstrapped knowledge evolution)
- [[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]] — AlphaLogics: market logic-driven multi-agent factor generation; material distinction in knowledge source (market logic vs. financial reports)
- [[quant/alpha-r1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]] — AlphaR1: RL-trained reasoning model for alpha screening; material distinction in mechanism (screening vs. generation)

## Sources

- Lin, Q., Feng, R., Feng, Y., Huang, Z., Chen, Y., Yang, Z., Zhou, L., Fei, B., Liu, J., & Li, Y. (2026). FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment. arXiv:2603.16365v2. https://arxiv.org/abs/2603.16365
