---
schema: strategy-research-record-v1
title: "AEAP/SEADS — LLM-Agentic Autonomous Factor Discovery with Formulaic Alpha Signals"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - factor-discovery
  - llm-agent
  - us-equity
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "arXiv:2609.00731v1 [cs.AI, q-fin.ST], September 1, 2026. https://arxiv.org/abs/2609.00731"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AEAP/SEADS — LLM-Agentic Autonomous Factor Discovery with Formulaic Alpha Signals

## Provenance

- **Authors:** Yingjian Pan (Stanford University, Advanced Financial Technologies Laboratory & MS&E), Xiaowei Ding (Nanjing University, School of Information Management), Kay Giesecke (Hasso Plattner Institute, AI & Quantitative Finance).
- **Identifier:** arXiv:2609.00731v1 [cs.AI, cs.LG, q-fin.ST]
- **DOI:** 10.48550/arXiv.2609.00731 (pending DataCite registration)
- **Stable URL:** https://arxiv.org/abs/2609.00731
- **Submitted:** September 1, 2026 (v1; draft July 2026). Preprint, under review.
- **Length:** 26 pages, 5 figures, 12 tables.
- **Source type:** Peer-level academic preprint from Stanford/HPI research groups; not a content farm or SEO summary.

## Economic mechanism

### Source-reported

The paper introduces the **Agentic Empirical Asset Pricing (AEAP)** paradigm: LLM-based agents autonomously execute hypothesis generation → formalization into code → execution against data → evaluation without a human performing any of those steps. **SEADS** (Stanford Engine for Agentic Discovery of Signals) is a concrete implementation of this paradigm.

The core economic insight for SEADS-generated factors is that LLM agents can discover formulaic alpha signals by autonomously proposing candidate mechanisms (factor rationales), formalizing them into executable rank-product formulas, and filtering them through a multi-stage statistical gate. The evaluation standard jointly requires three properties: **productivity** (fraction of the stock universe covered by the signal), **performance** (Rank-IC, Fama–MacBeth regression, out-of-sample Sharpe), and **novelty** (low correlation with an existing reference factor panel).

Three example admitted factors illustrate distinct alpha mechanisms:

1. **Stable Liquidity Efficiency Gate:** `rank(bidaskhl_21d) × rank(zero_trades_126d) × rank(dolvol_var_126d / (1 + trail12m_mean))`. Tight spreads and low trading inactivity indicate low trading frictions and faster price discovery, lowering required returns; downweighting names with unstable dollar-volume regimes isolates the structural (not episodic) component.

2. **Distress-Amplified Performance Mispricing:** `rank(mispricing_perf) × rank(o_score)`. Performance-based mispricing is more likely sustained by limits-to-arbitrage and forced trading among financially weak (high O-Score) firms, so the subsequent correction should be stronger when both signals coincide.

3. **Cash Operating Profit × Low Tax Payable Growth:** `rank(cop_bev) × (1-rank(txp_gr1a))`. Cash operating profitability is more informative when low growth in taxes payable reflects a persistent cash-tax advantage rather than a temporary accounting effect. This multiplicative rank-product form constitutes 83.8% of SEADS's admitted factors.

### Research interpretation

The SEADS factors are **hypothesized formulaic alpha signals** with specific economic rationales (liquidity frictions, mispricing under limits-to-arbitrage, cash-quality persistence). The hypothesis is that LLM agents can systematically discover economically meaningful cross-sectional return predictors that survive a rigorous multi-gate statistical filter. The key falsifiable claim is that the discovered factors generalize out-of-sample and are not merely in-sample overfits or redundant with existing factor panels.

The AEAP evaluation methodology itself is a methodological contribution: backtesting the autonomous discovery system (not just its output) under rolling re-execution to distinguish genuine adaptiveness from one-time luck.

## Signal

### Formation timestamp
- End-of-month cross-sectional ranking signals. The paper does not specify an exact signal-formation timestamp beyond monthly rebalancing. Assumed formation at month-end close; tradable at next month's open (research-proposed).
- **Timezone / convention:** US equity market calendar; CRSP/Compustat point-in-time data.

### Lookback
- The three example factors use lookback windows of 21 days (bid-ask high-low), 126 days (zero-trade days, dollar-volume variance), and 12 months (trailing mean). These are specified by the source.
- Warm-up period: 126 days minimum for the longest lookback window.

### Entry
- Cross-sectional rank-product signal: compute rank percentile of each component within the cross-section at each month-end.
- Long/short or long-only: the paper evaluates cross-sectional IC and Fama–MacBeth t-statistics but does not specify explicit long/short portfolio construction rules for the example factors. The AEAP framework evaluates factors as cross-sectional return predictors, not as explicit trading strategies (research-proposed interpretation).
- **Research-proposed operationalization:** A quintile/decile long-short portfolio sorted on the composite rank-product score is a standard cross-sectional test design.

### Exit
- Monthly rebalance. The paper evaluates monthly return horizons. No explicit stop-loss, take-profit, or time-exit rules for the example factors (research-proposed).

### Holding period
- 1 month (monthly return evaluation horizon, as reported in the source).

### Parameters
- The paper's gate values (Table 6, Appendix D): coverage ≥ 0.5, Rank-IC t ≥ max(3.0, Bonferroni-dynamic), out-of-decade regime sign-agreement, novelty < 0.7 (max absolute correlation with reference panel), partial-IC t ≥ 1.0, Fama–MacBeth t ≥ 1.0.
- The three example factor formulas are source-reported. Their component parameters (21d, 126d, 12m lookbacks) are source-specified.

### Position sizing
- Not specified in the source for the example factors. Standard equal-weight cross-sectional allocation assumed for research interpretation.

### Multi-timeframe dependencies
- The signals use multiple lookback windows (21d, 126d, 12m) within a single monthly evaluation frequency.

### Fully specified?
- **Partially specified.** The factor formulas are precisely defined. The portfolio construction rules (long/short, sizing, entry/exit timing) are not specified by the source for the example factors; these are research-proposed.

## Required data

- **Instrument / universe:** US common stocks. Two panels used: (1) US subset of Jensen, Kelly, and Pedersen (2023) global-characteristics panel; (2) CRSP/Compustat panel of primitive features novelty-checked against the 45-characteristic reference panel of Bryzgalova et al. (2025).
- **Venue:** US equity markets (NYSE, NASDAQ, AMEX).
- **Market type:** Equity (spot); not crypto, not derivatives.
- **Timeframe:** Monthly cross-sectional evaluation.
- **Fields:** Bid-ask high-low (21d), zero-trade count (126d), dollar-volume variance (126d), trailing 12-month mean dollar volume, mispricing performance metric, Ohlson O-Score, cash operating profitability / book equity, tax payable growth (1 year). Exact field definitions follow JKP and Bryzgalova panel conventions.
- **Point-in-time:** CRSP/Compustat with standard point-in-time availability lags. The JKP panel is already constructed with point-in-time protections.
- **Missing-data:** Not explicitly discussed in the source for the example factors.
- **Funding/fee/spread:** Not modeled in the source for the example factors.

## Execution assumptions

- **Signal-to-order timing:** Month-end formation, next-month open execution (research-proposed standard assumption).
- **Market / limit order:** Not specified (research-proposed: market order at next open).
- **Fill model:** Not specified. No slippage or spread model applied in the source's factor evaluation.
- **Fees:** Not included in the source's IC/Fama–MacBeth evaluation framework. The gate metrics (Rank-IC, FM t-stat) are pre-cost.
- **Spread / slippage / impact:** Not modeled. The source evaluates factors as return predictors via IC and regression, not as net-of-cost trading strategies.
- **Leverage / margin:** Not specified.
- **Capacity:** The source does not address capacity limits for the example factors. Cross-sectional factor ranks are economically meaningful for large-cap universes but capacity constraints for small-cap names are unquantified.

## Evidence

### Source-reported

- **Evaluation framework:** Six systems (SEADS + five re-implemented baselines) evaluated on two US equity panels. No single metric ranks all systems consistently, motivating multi-axis evaluation.
- **SEADS performance (Table 1):** Mean per-factor OOS Sharpe across admitted factors is 0.25 (Panel A). The three hand-selected examples exhibit higher OOS Sharpe (0.89, 0.52, 0.88) but are explicitly noted as non-representative of average performance.
- **Example factor metrics (Table 12):**
  - Liquidity Efficiency Gate: OOS Sharpe 0.89, OOS ann. ret. 13.1%, max corr with reference panel 0.662, coverage 97.8%, Rank-IC 0.024 (ICIR 1.25), FM t = 2.65.
  - Distress-Amplified Performance Mispricing: OOS Sharpe 0.52, OOS ann. ret. 7.1%, max corr 0.449, coverage 89.3%, Rank-IC 0.031 (ICIR 1.52), FM t = 3.36.
  - Cash Op Profit × Low Tax Payable Growth: OOS Sharpe 0.88, OOS ann. ret. 7.3%, max corr 0.697, coverage 85.0%, Rank-IC 0.016 (ICIR 1.35), FM t = 2.61.
- **Rolling re-execution:** The paper proposes and implements rolling re-execution of the entire discovery loop to assess whether the discovery process is reliable over time, not just lucky once. This is a novel evaluation contribution.
- **Negative findings (§6):** The paper reports limitations including evaluation pitfalls, the difficulty of ranking systems consistently, and the risk of adaptive overfitting in autonomous discovery systems.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper's own negative findings: no single metric consistently ranks discovery systems; the discovery process can get lucky once but may not be reliable over rolling re-execution windows; adaptive overfitting risk is inherent in self-revising hypothesis generators.
- The mean OOS Sharpe of 0.25 across admitted factors suggests that while some factors are strong, the average admitted factor has modest out-of-sample predictive power.
- The three hand-selected examples are explicitly non-representative of average performance.

## Falsification plan

1. **Out-of-sample / walk-forward:** Re-run SEADS (or equivalent AEAP system) on a held-out time period not used in the gate calibration. If mean OOS Rank-IC drops below 0.01 or mean OOS Sharpe drops below 0.1 across admitted factors, the discovery system's generalizability is weakened.
2. **Point-in-time / leakage audit:** Verify that all data used in factor construction (bid-ask, zero-trade count, dollar volume, O-Score, tax payable) was available at formation time with appropriate lags. Any look-ahead contamination would invalidate the IC/FM results.
3. **Parameter perturbation:** Vary the lookback windows (±50% on 21d, 126d, 12m) and re-evaluate. If factor Rank-IC drops below 0.01 or sign flips under ±50% perturbation, the signal is parameter-unstable.
4. **Reference panel expansion:** Re-evaluate novelty against an expanded reference panel (e.g., all 100+ Barra factors). If max correlation with any reference factor exceeds 0.8, the factor may be a repackaging of existing risk premia.
5. **Ablation on LLM vs. random search:** Replace the LLM hypothesis generator with a random formula sampler of similar complexity. If random search achieves comparable OOS performance, the LLM-specific contribution is diminished.
6. **Transaction cost stress:** Apply 5–20 bps per round-trip to the top-decile minus bottom-decile portfolio. If costs consume > 50% of the factor's gross return, the signal is not net-alpha-viable at the monthly frequency.
7. **Subperiod / regime breakdown:** Evaluate factor performance across bull (SPX +15% YoY), bear (SPX –15% YoY), and flat regimes. If the factor only works in one regime, its economic mechanism is not regime-robust.

## Crypto portability

**Unproven.**

The three example factors are formulated on US equity cross-sectional data using equity-specific fields (bid-ask spreads, O-Score, tax payable, book equity). Crypto markets differ fundamentally:

- No book equity, tax payable, or O-Score equivalents for most tokens/protocols.
- Crypto spot markets have different microstructure (24/7, fragmented venues, different order types).
- Cross-sectional factor ranking is feasible on crypto assets (e.g., BTC, ETH, SOL, etc.) but the specific input variables have no direct analogue.
- The AEAP methodology (LLM-driven factor discovery) is platform-agnostic and could potentially be applied to crypto data with appropriate feature engineering. However, no crypto-specific results are reported in this source.

Potential adaptation: The AEAP discovery framework itself could be applied to crypto cross-sectional data with on-chain and market-structure features (funding rates, OI, liquidation data, on-chain metrics) as inputs. This is a research-proposed extension, not source-reported evidence.

## Limitations

- **Illustrative, not representative:** The three example factors are hand-selected to demonstrate specific properties; they do not represent average SEADS performance (mean OOS Sharpe 0.25 vs. example Sharpe 0.52–0.89).
- **US equity only:** All results are on US equities. No evidence of cross-market or cross-asset generalizability.
- **Pre-cost evaluation:** IC and FM metrics are pre-transaction-cost. Net-of-cost performance is unknown.
- **No explicit trading strategy:** The paper evaluates factors as return predictors, not as implementable trading strategies with entry/exit/sizing rules.
- **Preprint, under review:** Not yet peer-reviewed. Claims await external validation.
- **LLM dependency:** Factor discovery depends on LLM capabilities that may change over time and may not be reproducible across model versions.
- **Survivorship / data snooping:** The paper evaluates against known reference panels, which may create implicit in-sample bias in what counts as "novel."
- **Not independently reproduced.**

## Implementation status

No implementation in our research stack (PyBroker/Nautilus) has been completed. The paper's factors are source-reported formulaic signals evaluated via IC and regression, not via portfolio backtest. Implementation would require: (1) constructing the factor inputs from CRSP/Compustat or equivalent data, (2) forming cross-sectional portfolios, and (3) backtesting with realistic costs.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean:
- The AEAP/SEADS factors are profitable
- The factors have been validated as alpha
- The factors are approved for implementation, paper trading, testnet, or live trading
- The AEAP methodology is endorsed as superior to human-led factor research

## Related Wiki records

- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]` — Related LLM-driven alpha research (different mechanism: GRPO reinforcement learning for alpha screening vs. autonomous hypothesis-code-backtest loop).
- `[[quant/cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03]]` — Related cross-sectional equity factor ranking methodology.

## Sources

1. Yingjian Pan, Xiaowei Ding, and Kay Giesecke, "Agentic Empirical Asset Pricing: Methodological Foundations," arXiv preprint `arXiv:2609.00731v1 [cs.AI, cs.LG, q-fin.ST]`, submitted September 1, 2026. DOI: [10.48550/arXiv.2609.00731](https://doi.org/10.48550/arXiv.2609.00731). Full text: https://arxiv.org/pdf/2609.00731v1.
