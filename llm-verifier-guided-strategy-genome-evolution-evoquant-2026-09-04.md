---
schema: strategy-research-record-v1
title: "EVOQUANT: Verifier-Guided LLM Strategy Optimization via Typed Genome Evolution and Multi-Stage Promotion"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - LLM-agent
  - strategy-optimization
  - verifier-guided
  - program-evolution
  - cross-market
status: research-only
confidence: medium
source_as_of: 2026-07-14
sources:
  - https://arxiv.org/abs/2607.12455v1 (arXiv:2607.12455v1 [cs.AI], submitted 14 Jul 2026)
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EVOQUANT: Verifier-Guided LLM Strategy Optimization via Typed Genome Evolution and Multi-Stage Promotion

## Provenance

**Primary source:** Jie Mao, Changlun Li, Xiang Li, Qiqi Duan, Jinhui Yuan, Xiang Liu, Yuyu Luo, Jing Tang, Xiaowen Chu, Nan Tang. "EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading." *arXiv preprint* `arXiv:2607.12455v1 [cs.AI]`, submitted 14 Jul 2026.

- **Affiliations:** HKUST(GZ); Paradoox AI Research.
- **Corresponding author:** Nan Tang (nantang@hkust-gz.edu.cn).
- **Version:** v1, submitted 14 Jul 2026.
- **Code:** https://anonymous.4open.science/r/EVOQUANT (anonymous repository as of paper submission).
- **Stable arXiv URL:** https://arxiv.org/abs/2607.12455
- **DOI:** 10.48550/arXiv.2607.12455

**What this record captures:** EVOQUANT is a meta-optimization framework — not a single trading signal. It takes an existing user-provided quantitative strategy and iteratively improves it through LLM-driven diagnosis, controlled genome edits, and multi-stage out-of-sample verification. The record captures the framework mechanism and the cross-market empirical evidence (A-share and Bitcoin strategy families).

## Economic mechanism

### Source-reported

The authors frame quantitative strategy optimization as a closed-loop scientific process: diagnose failure modes → generate controlled hypotheses → verify under out-of-sample gates → promote or reject. The core hypothesis is that an LLM agent can identify performance bottlenecks (e.g., sparse entries, delayed exits, excessive drawdown, validation–OOS decay) and propose targeted edits that improve risk-adjusted returns without introducing overfitting, when constrained by a verifier that screens candidates through hard admission rules and robustness penalties.

### Research interpretation

This is a **meta-alpha** mechanism: it does not discover a new market anomaly but rather automates the iterative refinement of existing strategy hypotheses. The hypothesized alpha channel is: (1) LLM-based failure-mode diagnosis can identify regime-specific weaknesses, parameter sensitivities, and signal inefficiencies that human researchers overlook; (2) a typed "strategy genome" representation constrains edits to interpretable, auditable changes; (3) multi-stage OOS verification with adaptive promotion gates prevents overfitting while allowing genuine improvements to survive.

For crypto (Bitcoin) strategies, the framework demonstrates that even simple base strategies (MACD-RSI-Bollinger, ATR trend-breakout, oversold-reversal) can be improved under this protocol, with the OOS test period Sharpe improving across all three families.

**Component roles (for potential ablation):**
- Strategy genome: typed intermediate representation enabling controlled edits
- Diagnosis agent: identifies failure modes from backtest evidence
- Candidate generator: LLM produces targeted edits (repair → bridge → redesign → family migration)
- OOS-aware verifier: hard admission gates (min trades, drawdown cap, drift bound) + soft ranking score
- Adaptive promotion engine: ADOPT / INCUBATE / REJECT decisions
- Memory module: stores successful paradigms and blacklists recurrent failure patterns

## Signal

EVOQUANT does not define a single trading signal. It defines an optimization protocol applied to a user-provided strategy. The Bitcoin strategies evaluated are:

**Strategy 1: MACD-RSI-Bollinger (optimized)**
- Base signals: MACD crossover, RSI thresholds, Bollinger Band breakout/breakdown.
- Optimization: genome edits to parameters and potentially signal structure, selected through the verifier pipeline.
- Exact optimized parameters: not individually specified in the paper (the paper reports aggregate before/after results).

**Strategy 2: ATR Trend-Breakout (optimized)**
- Base: ATR-based trend breakout with trailing stops.
- Optimization: same pipeline as above.

**Strategy 3: Oversold Reversal (optimized)**
- Base: mean-reversion on oversold conditions.
- Optimization: same pipeline.

**Optimization loop (common to all strategies):**
- Formation timestamp: N/A (optimization is offline, not a real-time signal).
- Iterations: 20 per strategy.
- Edit hierarchy: parameter repair → bridge edit → redesign → family migration.
- Promotion gate: hard (min 20 trades, OOS drawdown ≤ threshold, genome drift ≤ bound) + soft (adaptive score combining validation–OOS delta Sharpe, OOS return, stress penalties for fee/slippage perturbation, one-bar delay, parameter jitter).
- Memory: stores diagnosis, search plan, edit summary, candidate evidence, decision, failure reason.
- Underspecified: the paper does not reveal the exact LLM prompts or genome edits for each Bitcoin strategy; only aggregate performance changes are reported.

## Required data

- **Instrument:** Bitcoin (BTC), daily OHLCV.
- **Venue:** Not specified; data sourced from AKShare (Chinese data library).
- **Market type:** Not specified whether spot or perpetual; the paper says "Bitcoin trading strategies" but does not clarify instrument type.
- **Timeframe:** Daily bars.
- **Fields:** OHLCV, plus indicator fields (MACD, RSI, Bollinger Bands, ATR) derived from OHLCV.
- **Sample period:** 2020-01-01 to 2025-12-31 (6 years).
- **Data splits:** Train/validation/test (exact split boundaries not specified for Bitcoin; for A-share, explicit splits are shown).
- **LLM backend:** DeepSeek-R1.
- **Missing data:** Not discussed; AKShare daily data assumed clean.
- **Data availability:** AKShare is publicly accessible; the specific BTC data endpoint is not named.

## Execution assumptions

- **Signal-to-order:** Not specified for Bitcoin strategies (the paper focuses on portfolio-level Sharpe, not execution-level details).
- **Next-bar vs same-bar:** Not specified; likely next-bar given daily frequency.
- **Order type:** Not specified.
- **Fill model:** Not specified.
- **Fees/slippage:** Base assumption: not specified for Bitcoin. Robustness tests use 2× fee/slippage (A-share only; Bitcoin robustness not reported).
- **Transaction cost treatment:** The paper acknowledges "simplified execution assumptions" and notes this as a limitation.
- **Leverage/margin:** Not specified.
- **Capacity:** Not discussed for Bitcoin.

## Evidence

### Source-reported

All results below are from Mao et al. (`arXiv:2607.12455v1`, Table 1, Section 5.2):

**Bitcoin strategy results (test set, before and after optimization):**

| Strategy | Base Sharpe | Optimized Sharpe | Sharpe Δ | Base MDD | Optimized MDD | MDD Δ |
|---|---|---|---|---|---|---|
| MACD-RSI-Bollinger | −1.118 | 0.265 | +1.383 | 18.22% | 8.54% | −9.68 pp |
| ATR Trend-Breakout | −1.536 | −1.050 | +0.486 | 14.06% | 12.01% | −2.05 pp |
| Oversold Reversal | −0.838 | 0.679 | +1.516 | 16.53% | 12.17% | −4.36 pp |

- All three original Bitcoin strategies had negative test Sharpe before optimization.
- Two of three became positive after optimization (MACD-RSI-Bollinger and Oversold Reversal).
- ATR Trend-Breakout improved but remained negative.
- All three reduced maximum drawdown.

**A-share aggregate (Table 1, portfolio-level):**
- Average test Sharpe uplift: +0.829 (from −0.298 to +0.538).
- 115/120 stock-level tasks (95.8%) showed non-degradation.
- Best-performing strategy achieved 199% relative improvement.

**Ablation (Table 2, A-share Volume Breakout, single strategy):**
- Full system Sharpe uplift: +0.982.
- w/o promotion engine: +0.128 (dramatic degradation).
- Parameter only: +0.274.
- Random mutation only: +0.645.

**Robustness (Table 3, A-share only):**
- 2× fee/slippage: mean Sharpe uplift 0.700.
- Alternative split: uplift 0.368.
- Walk-forward 2020–2023: uplift 0.370.
- Walk-forward 2021–latest: uplift 0.545.
- Note: Bitcoin robustness/walk-forward results are **not reported** in the paper.

**Walk-forward for A-share Volume Breakout (Table 3):**
- Walk-forward 2020–2023: Sharpe Δ = +0.038 (very small).
- Walk-forward 2021–latest: Sharpe Δ = +0.373.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- ATR Trend-Breakout remained negative-Sharpe after optimization (Sharpe −1.050), suggesting the framework cannot always rescue a fundamentally weak strategy.
- Walk-forward uplift is substantially smaller than static-split uplift for some strategies (e.g., A-share Volume Breakout: 0.982 static vs 0.038–0.373 walk-forward), consistent with expected OOS decay.
- Bitcoin robustness and walk-forward results are not reported, leaving OOS stability for crypto unverified.
- The paper acknowledges simplified execution assumptions, no liquidity/market-impact modeling, and no survivorship-bias treatment for A-shares.
- The LLM (DeepSeek-R1) comparison is limited by local configuration and budget.

## Falsification plan

1. **Walk-forward on Bitcoin:** Run the full EVOQUANT pipeline on Bitcoin strategies with strict walk-forward evaluation (fixed parameters from training window, evaluated on held-out period). If the Sharpe uplift collapses to near-zero or negative, the framework's crypto value is unsupported.
2. **Robustness on Bitcoin:** Double fees/slippage and re-run; if optimization gains disappear under realistic cost assumptions for crypto perpetuals (funding rates, spread, impact), the effect is cost-insensitive noise.
3. **Baseline comparison:** Compare EVOQUANT-optimized strategies against pure grid-search or Bayesian optimization of the same base strategies' parameters. If simple hyperparameter search achieves similar Sharpe uplift, the LLM diagnosis/generation adds marginal value over cheaper methods.
4. **Parameter sensitivity:** Re-run with different LLM backends (e.g., GPT-4, Claude). If performance is highly model-dependent, the framework is not portable.
5. **Ablation of memory:** Already reported for A-share; extend to Bitcoin. If memory contributes negligibly in crypto (different regime characteristics), the self-improvement claim weakens.
6. **Failure metric:** Walk-forward Sharpe uplift < 0.1 or non-degradation rate < 80% across Bitcoin strategy families → framework not validated for crypto.

## Crypto portability

**Adapted**

The framework was applied to Bitcoin strategies, so crypto portability is partially demonstrated. However:

- The paper does not clarify whether Bitcoin data is spot or perpetual; perpetual-specific dynamics (funding, basis, liquidation) are not addressed.
- Daily bar frequency may miss intraday microstructure effects important for crypto.
- AKShare's BTC data source and quality are not specified.
- Robustness and walk-forward results are only reported for A-shares, not Bitcoin.
- The 2020–2025 sample period for Bitcoin includes major regime shifts (2021 bull, 2022 crash, 2023 recovery, 2024–2025 halving cycle), but regime-specific performance is not broken out.
- No funding-rate, spread, or liquidity-impact treatment for crypto.

## Limitations

- **Execution assumptions simplified:** The paper explicitly acknowledges no liquidity, market-impact, or survivorship-bias treatment.
- **Bitcoin robustness not reported:** Walk-forward and cost-sensitivity tests are only for A-shares.
- **LLM dependency:** Results depend on DeepSeek-R1; portability to other LLMs is untested.
- **Portfolio-level aggregation:** A-share results are equal-weighted portfolios over 30 stocks; Bitcoin results are single-asset. Comparing across asset classes requires caution.
- **Code availability:** Anonymous repository as of submission; reproducibility depends on future public release.
- **Data source specifics:** AKShare BTC endpoint not named; data quality/availability unknown.
- **Trade count constraint:** The framework requires ≥20 trades per year; this may exclude low-frequency strategies.
- **Family migration risk:** The highest-tier edit (strategy family migration) could introduce overfitting to historical regimes if the verifier is insufficiently strict.

## Implementation status

No implementation in our research stack (PyBroker/Nautilus) has been completed. This record captures a meta-optimization framework and its reported empirical results.

## Adoption boundary

This is research material only. The presence of this record does **not** mean:
- The EVOQUANT framework is validated for our crypto universe or execution assumptions.
- The reported Sharpe improvements are reproducible in our backtesting infrastructure.
- The framework is approved for implementation, paper trading, testnet, or live trading.
- LLM-based strategy optimization is endorsed as a production workflow.

## Related Wiki records

- No related Wiki Brain records identified for this specific meta-optimization framework.
- Adjacent concept: `[[quant/alpha-research-contract-2026-08-28]]` (general alpha research contract).
- Adjacent concept: records on LLM-driven alpha discovery (e.g., AlphaCrafter, AEAP/SEADS) address a different problem (alpha factor mining vs. strategy optimization).

## Sources

1. Mao, J., Li, C., Li, X., Duan, Q., Yuan, J., Liu, X., Luo, Y., Tang, J., Chu, X., & Tang, N. (2026). "EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading." *arXiv preprint* `arXiv:2607.12455v1 [cs.AI]`, submitted 14 Jul 2026. https://arxiv.org/abs/2607.12455
   - Table 1 (main A-share and Bitcoin results), Table 2 (ablation), Table 3 (robustness/walk-forward), Section 5.1–5.3, Section 7 (Discussion), Section 8 (Limitations).
