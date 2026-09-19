---
schema: strategy-research-record-v1
title: "Alpha-Foundry: Strongly-Typed GP + GFlowNet Formulaic Alpha Mining with C++/OpenMP Backtest Kernels for Crypto Perpetuals"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - formulaic-alpha
  - genetic-programming
  - gflownet
  - crypto-perpetuals
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - "https://github.com/Huang-Hg/alpha-foundry (commit 0a87be0034d93adede9b0621ae02b029a96ad309, 2026-09-19)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alpha-Foundry: Strongly-Typed GP + GFlowNet Formulaic Alpha Mining with C++/OpenMP Backtest Kernels for Crypto Perpetuals

## Provenance

- **Repository:** https://github.com/Huang-Hg/alpha-foundry
- **Full commit SHA:** `0a87be0034d93adede9b0621ae02b029a96ad309` (HEAD as of 2026-09-19)
- **License:** MIT
- **Language:** Python + C/C++ (OpenMP) + CUDA (cupy NVRTC)
- **Primary source:** The GitHub repository README and source code. No separate published paper exists for this specific implementation.
- **Related published work referenced in the repo:**
  - AlphaSAGE (arXiv:2509.25055, ICLR 2026): structure-aware GFlowNet alpha mining — the GFlowNet search component is based on this method.
  - FACT (arXiv:2604.26666): compositional kernel-synthesis — the CUDA operator fusion in `backtest/ops_cuda/` adopts this paradigm.
  - NSGA-II (Deb et al., 2002) + DEAP (Fortin et al., 2012): multi-objective strongly-typed GP.
- **Data access:** The repository is a public snapshot; mining requires user-provided parquet panels matching the format read by `evaluation/crypto_adapter.py`. The data-collection pipeline is not included.

## Economic mechanism

### Source-reported

Alpha-Foundry does not define a single trading signal. It is a **formulaic alpha mining framework** that searches for trading signals (formulaic alphas) expressed as typed abstract syntax trees (ASTs) over a context-free grammar (CFG). The framework's economic thesis is that:

1. **Formulaic alpha mining can discover novel, orthogonal factors** from raw market data (OHLCV + derived features) that traditional hand-crafted indicators miss.
2. **Multi-objective search** (net Sharpe + behavioral diversity) combined with **admission gates** (|IC| threshold, orthogonal contribution Δ, OOS holdout) can filter spurious overfitted signals from genuinely predictive ones.
3. **Deterministic sizing fusion** (z-score → AFF causal rolling least-squares → top-K long-short → vol-target scalar leverage) can combine multiple weak alphas into a portfolio with improved risk-adjusted returns.

### Research interpretation

The hypothesis is that formulaic alpha mining — searching a structured DSL space for factor expressions — can discover exploitable signals in crypto perpetual futures markets. The framework proposes a specific pipeline:

- **Search layer:** Two independent search engines (GP with NSGA-II, GFlowNet with AlphaSAGE-style structure-aware sampling) explore the AST space.
- **Evaluation layer:** rank-IC and portfolio backtest returns assess each candidate.
- **Admission gates:** Candidates must pass |IC| minimum, orthogonal contribution Δ, and OOS holdout profitability to enter the alpha pool.
- **Sizing layer:** Deterministic fusion combines pool members into a portfolio.

The economic mechanism of any discovered alpha is unknown until the mining process completes and the resulting AST is interpreted. The framework itself is mechanism-agnostic — it discovers signals but does not prescribe their economic rationale.

## Signal

Alpha-Foundry does not define a fixed signal. It defines a **search space** (typed DSL) and a **pipeline** for discovering signals. The DSL grammar is defined in `evaluation/grammar.py` with:
- **Operands:** Price (open, high, low, close), volume, and derived features — auto-classified from parquet column names.
- **Operators:** Arithmetic, comparison, windowing, normalization, and technical-function primitives constrained by a CFG with α-Sem-k cost budget (max_cost=25, min_cost=3, max_len=5 production count).
- **Output:** A typed AST that compiles to C (or CUDA) for batch evaluation.

The search engines produce candidate ASTs; the admission gates filter them; the sizing layer fuses survivors. The actual signal definition is the discovered AST, which varies per mining run.

**Signal formation:** Per-bar evaluation of the AST against the panel data. The signal becomes tradable at the next bar's open (signal on bar t → entry at open of bar t+1).

**Holding period:** Determined by the portfolio construction: top-K long-short with vol-target scalar leverage, rebalanced per-bar with swap_n=2 (max 2 names swapped per leg per rebalance) and min_hold=4 (minimum 4 bars hold).

**Position sizing:** research-proposed — vol-target scalar leverage with leverage_cap=2.0, top_k=8 per leg.

## Required data

- **Instrument:** USDT-margined perpetual futures on Binance (crypto perpetuals market profile: continuous24x7).
- **Universe:** Top-N most liquid symbols by quote-volume (default top_n=30, dynamic per-bar universe with hold_max_persist=4 bars and qv_window_hours=4).
- **Timeframe:** 5-minute bars (parquet_5m_root = ./data/parquet_5m_univ4h).
- **Fields:** OHLCV + derived features (auto-classified from parquet column names). The data pipeline also supports funding rates, long/short ratios, basis, and open interest for crowding neutralization.
- **Venue:** Binance USDT-M perpetual futures.
- **Point-in-time:** Not specified in the repo; user-provided data must ensure no look-ahead.
- **Missing-data:** Not specified; the framework assumes clean parquet panels.

## Execution assumptions

- **Fee model:** 5 bps per side (taker, VIP0 standard), configured in `fee_rate=0.00050`.
- **Half-spread:** 0.0 (half_spread_rate=0.0, not modeled).
- **Market impact:** sqrt-impact model: Y·σ_5m·√(notional/bar_volume), with Y=0.5.
- **Slippage:** Not explicitly modeled beyond impact.
- **Leverage cap:** 2.0x gross target (Σ|w| capped at 2.0, split evenly between long and short legs).
- **Order book:** Not modeled in the backtest engine.
- **Fill model:** Not specified; assumed perfect fill at bar open.
- **Liquidation:** Included in the backtest engine (trailing stop + liquidation modeling in C++ kernels).
- **Funding:** Included in the backtest engine (funding cost is part of the crypto perpetual cost model).
- **Crowding neutralization:** Optional (enabled by default): candidate signals are orthogonalized against funding/long-short-ratio/basis/OI crowding subspace.
- **Beta neutralization:** Optional (enabled by default): signals are orthogonalized against causal rolling market β.

## Evidence

### Source-reported

The repository does not publish backtest results. The README states: "This repository is a public snapshot: mining requires your own parquet panel matching the format read by `evaluation/crypto_adapter.py` (the data-collection pipeline is not included)."

No specific IC, Sharpe, CAGR, drawdown, or other performance figures are claimed by the repository for the crypto perpetuals configuration.

The underlying methods have published benchmarks:
- **AlphaSAGE** (arXiv:2509.25055, referenced as the GFlowNet baseline): reported IC/ICIR/RankIC/RankICIR metrics on Chinese equity universes (CSI300, CSI500, CSI800, CSI1000) — not on crypto perpetuals.
- **FACT** (arXiv:2604.26666): reported kernel-synthesis benchmarks — not directly applicable to the backtest engine.

### Independently reproduced

Not independently reproduced. No implementation has been integrated into internal quantitative backtesting frameworks (PyBroker/Nautilus).

### Negative evidence

- The admission gates (|IC| ≥ 0.01, orthogonal contribution Δ ≥ 0.02, OOS holdout profitability, R² cap 0.5) are designed to filter overfitted signals, but their effectiveness on crypto perpetuals specifically is untested.
- The GP search includes a `reward=flat` probe that was found to increase collected candidates 87× but degrade validation net Sharpe from +0.363 to −0.187 (documented in config comments). This confirms that unconstrained search produces overfit candidates, and the admission gates are necessary but their thresholds are research-defined.
- The `max_len=5` production count limit is documented as a practical boundary: "5=实测极限勿调大:长树扩容搜索空间 → 多重比较选择偏差" (translation: 5 is the measured limit; do not increase: longer trees expand the search space → multiple comparison selection bias).

## Falsification plan

1. **Published backtest on crypto perpetuals:** Run the full pipeline (gp-baseline or alphasage → pool → materialize) on a user-provided crypto perpetual panel with strict walk-forward evaluation. If no discovered alpha achieves out-of-sample RankIC > 0.01 after admission gates, the framework's crypto mining value is unsupported. (research-defined falsification threshold)
2. **GP vs. GFlowNet comparison:** Compare the GP (NSGA-II) and GFlowNet (AlphaSAGE) search engines on the same crypto panel. If both produce similar pool quality, the GFlowNet component adds marginal value over cheaper GP search. (research-defined falsification threshold)
3. **Admission gate ablation:** Remove each admission gate sequentially (|IC|, Δ, OOS holdout, R² cap) and measure pool overfitting. If removing a gate does not degrade validation Sharpe, that gate is not load-bearing. (research-defined falsification threshold)
4. **Cost sensitivity:** Vary fee_rate from 0 to 20 bps per side and measure pool Sharpe decay. If the pool collapses below Sharpe 0.5 at 10 bps, the discovered alphas are not cost-robust. (research-defined falsification threshold)

## Crypto portability

**direct** — the framework is designed for crypto perpetuals as its primary market. The `continuous24x7` market profile handles 24/7 trading, and the backtest engine models funding and liquidation specific to perpetual futures.

Crypto-specific considerations:
- **Funding:** Modeled in the backtest engine (funding cost is part of the perpetual cost model).
- **Liquidation:** Modeled in the backtest engine (trailing stop + liquidation).
- **24/7 sessions:** Handled by the `continuous24x7` market profile.
- **Venue fragmentation:** The framework targets Binance USDT-M specifically; porting to other venues requires changing the data pipeline.
- **Liquidity:** Dynamic per-bar universe construction (top-N by quote-volume) addresses liquidity filtering.
- **Order book:** Not modeled; the sqrt-impact model is a simplified approximation.

## Limitations

- **No published results:** The repository does not include backtest results for any market. All performance claims would need to be generated by the user with their own data.
- **Data pipeline not included:** The parquet data-collection pipeline is excluded from the public snapshot. Users must construct their own data panels.
- **Order book not modeled:** The backtest engine uses a sqrt-impact model but does not simulate order-book dynamics, partial fills, or queue priority.
- **Admission gate thresholds are research-defined:** The specific thresholds (|IC| ≥ 0.01, Δ ≥ 0.02, OOS holdout, R² cap 0.5) are tuned by the author and may not generalize to all crypto markets or time periods.
- **DSL grammar is fixed:** The search space is constrained by the CFG; novel operator types or data sources require grammar modifications.
- **No walk-forward or regime testing in the framework itself:** The framework provides a single train/test split via holdout_frac; proper walk-forward evaluation is the user's responsibility.
- **Not independently reproduced:** No external validation of the framework's mining pipeline exists.
- **Single author, limited stars (9):** The repository is early-stage with limited community adoption or review.
- **CUDA dependency for GPU path:** The CUDA operator compilation requires cupy and a GPU; the CPU path is available but slower.

## Implementation status

No implementation of Alpha-Foundry's formulaic alpha mining pipeline or C++/OpenMP backtest kernels has been integrated into internal quantitative backtesting frameworks (PyBroker/Nautilus), paper trading, or live execution. This record serves strictly as a normalized research capture of the framework methodology.

## Adoption boundary

This record is research material only. The repository is present in this staging area as a normalized research capture of an open-source formulaic alpha mining framework for crypto perpetuals. Its presence does not mean:

- that any specific alpha has been validated;
- that the framework has been tested on our data;
- that any discovered signal is profitable;
- that the framework is approved for implementation;
- that any mining output is approved for paper trading, testnet, or live execution.

## Related Wiki records

- `[[quant/alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05]]` — Related formulaic alpha discovery using GFlowNets (AlphaG-OPD), which benchmarks against AlphaSAGE (the GFlowNet component used in alpha-foundry).
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — Related formulaic alpha discovery using grammar-guided MCTS Tree-LSTM.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — Related multi-agent factor generation, also benchmarked against formulaic mining approaches.
- `[[quant/alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17]]` — Related generative formulaic alpha mining framework (different system: AlphaForge by Shi et al., arXiv:2406.18394, focused on Chinese equities with dynamic factor timing).

## Sources

1. Huang-Hg. "alpha-foundry: Formulaic Alpha Mining + Backtest Kernels." GitHub repository: https://github.com/Huang-Hg/alpha-foundry, commit `0a87be0034d93adede9b0621ae02b029a96ad309` (2026-09-19). License: MIT.
2. Berkin Chen, Han Ding, Ning Shen, Ting Guo, Jiawei Huang, Lu Liu, and Meng Zhang. "AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration." arXiv preprint `arXiv:2509.25055`, 2025. Published at ICLR 2026. Referenced as the GFlowNet method implemented in alpha-foundry's `search/alphasage/`.
3. FACT (arXiv:2604.26666). Compositional kernel-synthesis paradigm adopted in `backtest/ops_cuda/`.
