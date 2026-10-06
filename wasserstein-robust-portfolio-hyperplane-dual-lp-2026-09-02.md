---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: "Certified High-Dimensional Wasserstein Robust Portfolio Optimization via Supporting-Hyperplane Dual LP"
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2026-08-07
sources:
  - "Hsieh, Chung-Han, and Rong Gan. Certified High-Dimensional Wasserstein Robust Portfolio Optimization. arXiv:2608.07032v1, submitted 2026-08-07. https://arxiv.org/abs/2608.07032"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Certified High-Dimensional Wasserstein Robust Portfolio Optimization via Supporting-Hyperplane Dual LP

## Provenance

- **Family identity:** `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02`.
- **Primary source:** Chung-Han Hsieh and Rong Gan, *Certified High-Dimensional Wasserstein Robust Portfolio Optimization*, arXiv:2608.07032v1. The paper develops a certified finite approximation and LP for Wasserstein distributionally robust expected-utility portfolio optimization; it reports monthly 476-asset experiments and scalability studies up to 1,000 assets.
- **Source-backed intake record:** Local Wiki Brain record `quant/wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md`, with `reviewed_commit: c405adc4795154334d9d50950795b4711f00445d` and `reviewed_blob: 99f244c16fd2e24021077d05de0c29399be88278`. This record preserves the prior source review and research normalization; its operational interpretations are not treated as paper claims here.
- **Historical evidence:** Four survivor baseline records identify this family and carry the same `bundle_sha256` and `bundle_identity_sha256`. The referenced bundle itself was not available for independent inspection in this reconstruction. No local bundle path is reproduced.
- **Mapping limitation:** The survivor runs are single-symbol crypto daily cohorts with `wasserstein_epsilon`, a return lookback, and DCA parameters. The paper's source mechanism is cross-sectional, long-only portfolio allocation with monthly rebalancing. The available baselines do not establish an exact mapping from the paper's portfolio weights, data, or rebalance events to the old single-symbol Qlib runs. Their metrics below are historical Qlib survivor evidence only; they are not source-reported results or current Hummingbot reproductions.

## Economic mechanism

### Source-reported

The method seeks portfolio weights that maximize worst-case expected utility over an order-1 Wasserstein ambiguity ball around an empirical distribution of asset-return vectors, constrained to a compact polyhedral return support. It replaces the semi-infinite support problem from standard duality with a finite approximation: concave utility is upper-majorized by supporting tangent hyperplanes, then the support subproblems are dualized. A uniform utility approximation error bounds both robust-value error and near-optimality gap. For the paper's long-only simplex, box support, and ℓ1 ground metric specialization, the resulting problem is a single finite linear program rather than exponential vertex enumeration.

The ambiguity radius controls conservatism. The paper also characterizes a large-radius regime in which the Wasserstein ball covers all distributions on the support and the optimizer reduces to maximizing worst-case support return.

### Research interpretation

The method is a portfolio-construction optimizer, not a standalone directional entry/exit rule. Its research hypothesis is that ambiguity-aware optimization can reduce sensitivity to empirical-distribution estimation error while remaining tractable at high asset counts. The historical crypto survivor runs cannot establish that hypothesis for the paper's source-defined portfolio process because their source-to-run mapping is undocumented.

## Signal

At each rebalance, form an empirical distribution from the preceding `N` asset-return vectors and choose feasible long-only portfolio weights maximizing worst-case expected utility over an order-1 Wasserstein ball of radius `ε`, using the supporting-hyperplane approximation and dual LP.

The paper's box-specialized LP requires the ℓ1 ground metric and long-only portfolio simplex with box return support. Its general finite hyperplane-dual formulation supports compact polyhedral return supports and polyhedral portfolio constraints. For the paper's logarithmic Kelly example, utility is `U(y) = log(1+y)`. Tangent points / mesh resolution are selected to satisfy the stated uniform approximation tolerance `η`; they are not interchangeable with undocumented survivor-run settings.

The paper's rolling example uses monthly decisions based on prior-period returns, with the selected portfolio held through the next month. The paper does not define a crypto single-pair long/short signal, DCA entry rule, or candle-close trade-event strategy.

## Required data

- A time-aligned cross-sectional matrix of asset returns over the historical estimation window.
- A defined, bounded polyhedral support for returns; the box-specialized result uses lower and upper return bounds.
- Portfolio constraint set and utility function, plus Wasserstein ground norm and radius.
- For the paper's 11-asset benchmark, daily adjusted closing prices for 10 risky equities and the 1-month U.S. Treasury Constant Maturity yield series, which the authors explicitly include as an additional return series in the DRO model.
- For the rolling experiment, daily adjusted closing-price records for a fixed 475-risky-asset universe plus the same 1-month Treasury proxy; the authors explicitly note that selecting complete histories over the full study period is not a point-in-time S&P 500 constituent strategy.
- Each monthly decision is computed from that calendar month's daily returns and applied in the immediately following calendar month. The paper does not specify a 252-day estimation lookback for this rolling experiment. These are multi-asset return vectors, not a BTC/ETH/BNB/SOL single-pair OHLCV signal.

## Execution assumptions

- Source empirical cadence: compute one weight vector from each calendar month's daily returns, then apply it during the immediately following calendar month; the rolling study computes weights from December 2020 through November 2025 for 60 holding periods from January 2021 through December 2025.
- The paper's model assumes long-only fully invested (cash-financed) weights summing to one. It explicitly includes the time-varying 1-month Treasury yield as an additional return series; this is part of the stated model, not a contradiction with the simplex constraint.
- The rolling study uses the fixed complete-data 475-risky-asset universe plus the risk-free proxy; its authors explicitly caution that this is not a point-in-time constituent strategy.
- Transaction costs of 0.1%, 0.2%, and 0.3% are applied ex post to risky-asset turnover and are not included in the optimization objective. The paper does not specify a market-on-close, VWAP, or other exact fill convention; none is inferred here.
- Solver implementation is a linear-programming solver; the paper reports CVXPY implementations solved with MOSEK.
- These are paper-specific portfolio assumptions, not assumptions proven to have governed the historical Qlib survivor runs.

## Evidence

### Source-reported

The paper reports: (1) an 11-asset single-period numerical comparison, including a maximum robust-value gap of `1.38 × 10⁻⁴` against the exact vertex formulation at `η = 10⁻³`; (2) a 476-asset rolling monthly experiment for January 2021–December 2025, with 60 monthly decisions and reported mean solve time of `0.065s` over 300 solves; and (3) synthetic scalability experiments through 1,000 assets with a reported maximum robust-value gap of `2.29 × 10⁻⁴` at `η = 10⁻³`. These are author-reported results, not independently reproduced here. Refer to the paper for full benchmark and cost details.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source reports that large ambiguity radii approach conservative worst-case allocation behavior and that high turnover costs can degrade aggressive small-radius policies. No independent negative-result audit was performed here.

### HISTORICAL QLIB SURVIVOR EVIDENCE — not source results or current Hummingbot reproduction

All four baseline records identify round `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02-r1`, run `...-r1-u1`, research data cutoff `2026-09-11`, `source_verdict: PASS`, and `source_disposition_band: MULTIPLE_SURVIVORS`. Parameters, performance, and robustness figures below are transcribed from those baselines. Baseline `max_dd_pct` values and PnL are retained in the source's reported units without reinterpretation.

Common recorded DCA parameters: `size_multiplier=1.0`, `invalidation_pct=0.1`. These are historical run settings, not paper-defined strategy rules.

| survivor_id | cohort | ε; lookback N | DCA spacing; breakeven TP | params_sha256 suffix | Historical PnL / Sharpe / episodes / max DD % | OOS PnL / Sharpe / episodes / max DD % | Full PnL / Sharpe / episodes / max DD %; annualized return; trades/year | Robustness: 2× fee (PnL, Sharpe, DD%); 2× funding (PnL, Sharpe, DD%); 1-bar delay (PnL, Sharpe, DD%); 2-tick slippage (PnL, Sharpe, DD%) | Stress floor; neighborhood |
|---|---|---:|---:|---|---|---|---|---|---|
| `sv-02dc05d84a8985f1` | ETHUSDT/1d | 0.0001; 252 | 0.02; 0.01 | `74a3eb9941b29c17519a32d96b3e4d56d019571baa85aff48b91d1dac5b01614` | 11,742.1057 / 3.7836 / 78 / 0.2661 | 7,008.4252 / 6.2615 / 50 / 0.4423 | 18,750.5309 / 4.3205 / 128 / 0.3314; 0.1089; 27.2606 | 16,610.0447 / 4.2892 / 0.3566; 18,669.2743 / 4.3112 / 0.3342; 18,744.9121 / 4.2806 / 0.3486; 18,741.0503 / 4.3205 / 0.3315 | 16,610.0447 (`fee_2x`); passed, 6/7 same sign |
| `sv-3e29e2c75e6fc7a0` | SOLUSDT/1d | 0.01; 252 | 0.01; 0.03 | `c2061a1463f19bc1a1c8cb549d38946ad462b5cc71b7ced6251e036334fd901e` | 309,917.5699 / 3.3649 / 424 / 15.0102 | 60,860.2210 / 4.7847 / 49 / 8.7836 | 370,777.7909 / 3.1868 / 473 / 15.0102; 0.7362; 100.7366 | 349,140.8005 / 3.0403 / 16.0811; 369,211.8788 / 3.1760 / 15.1099; 352,194.2766 / 3.0921 / 15.0945; 365,112.2744 / 3.0406 / 15.4890 | 349,140.8005 (`fee_2x`); passed, 5/7 same sign |
| `sv-6ef66ccd3de85744` | BTCUSDT/1d | 1.0; 63 | 0.01; 0.01 | `3c13895185ae048bfb0f0edfbc02c470ee684b0e347075522b111cc5b1cdef54` | 121,101.0862 / 5.2178 / 626 / 9.3103 | 10,876.4685 / 0.9835 / 162 / 32.8829 | 132,032.3739 / 4.1135 / 787 / 9.3103; 0.4318; 167.6103 | 111,115.3290 / 3.5018 / 10.3879; 130,891.9618 / 4.0833 / 9.3444; 130,810.4888 / 4.0750 / 9.3918; 129,967.9189 / 3.9270 / 10.2446 | 111,115.3290 (`fee_2x`); passed, 6/6 same sign |
| `sv-82b86a10d0a7ccf0` | BNBUSDT/1d | 1.0; 252 | 0.01; 0.01 | `01a1403b77c32f7dfced02e2f28da908ff4077d493d518c9bfd0cb8330ef1b44` | 37,250.4011 / 5.2882 / 177 / 0.6916 | 30,413.6727 / 2.4007 / 189 / 31.4904 | 67,664.0739 / 3.2149 / 366 / 14.5661; 0.2856; 77.9484 | 58,855.7898 / 2.8492 / 15.6978; 67,568.1884 / 3.2146 / 14.5526; 66,945.4044 / 3.1871 / 14.7189; 67,622.0367 / 3.2156 / 14.5614 | 58,855.7898 (`fee_2x`); passed, 6/6 same sign |

The four records share `bundle_sha256=sha256:e838c98b694caeb755d0c286ef4cd67d7619589b6c502b154d9f71246c3a0152` and `bundle_identity_sha256=sha256:5f0ac36fe335edbeb9fb81fedaf68cac0bf096047e6dde6d39946000dde51cca`. Individual survivor IDs and parameter hashes above preserve run identity; the shared bundle was not available for verification. No claim is made that survivor or robustness verdicts were independently validated.

## Falsification plan

- Reimplement the paper-defined LP and its uniform approximation certificate from the primary source, then compare against exact small-instance benchmarks and an independent implementation.
- Use point-in-time, survivorship-bias-controlled asset universes and purged walk-forward evaluation; compare with SAA and equal-weight baselines under identical return data, rebalance dates, and transaction-cost accounting.
- Stress support-bound misspecification, ambiguity-radius selection, temporal dependence, turnover, and execution costs. Reject any claimed advantage that disappears out of sample or under realistic costs.
- Separately, do not use the historical crypto survivor metrics as evidence for the paper unless a complete, auditable source-to-run mapping and run artifact become available.

## Crypto portability

Unproven. A crypto portfolio adaptation would require a point-in-time multi-asset return panel, explicit crypto universe and support construction, a defined rebalance cadence, and source-faithful handling of fees and (for derivatives) funding. The single-symbol historical survivor cohorts do not demonstrate a lossless or validated adaptation.

## Limitations

- This is cross-sectional portfolio optimization with shared weights and periodic rebalancing, not a one-pair directional strategy.
- The paper's box-specialized LP depends on its stated long-only, ℓ1-ground-metric, compact box-support conditions; broader settings use the general polyhedral formulation and need not be the same LP specialization.
- Empirical-return estimation and support-bound choices remain consequential; the source's certification bounds approximation error for the stated utility approximation, not all model or data errors.
- Historical Qlib baselines omit the referenced bundle contents here and do not document a verifiable mapping to the source portfolio process.

## Implementation status

`not-implemented` in the current research/runtime stack. Historical survivor labels do not imply a current implementation or reproduction.

## Adoption boundary

Research record only. Not approved for implementation, performance screening, Paper, Testnet, or live trading. `NOT_LOSSLESS` reflects the current Hummingbot contract: the source requires cross-sectional multi-asset weights, shared portfolio state, and monthly rebalance semantics, which cannot be represented as the required single-pair candle-driven strategy without changing its core mechanism.

## Related Wiki records

- `quant/wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02`

## Sources

1. Hsieh, Chung-Han, and Rong Gan. *Certified High-Dimensional Wasserstein Robust Portfolio Optimization*. arXiv:2608.07032v1, submitted 2026-08-07. https://arxiv.org/abs/2608.07032.
2. Historical family baseline records in the validated-survivor-research corpus: `sv-02dc05d84a8985f1`, `sv-3e29e2c75e6fc7a0`, `sv-6ef66ccd3de85744`, and `sv-82b86a10d0a7ccf0`. Each contains the experiment fields and metrics transcribed above; shared bundle identities are recorded under Evidence.
3. Source-reviewed Wiki Brain record and provenance identity listed above; it is an auxiliary source record, not evidence of runtime implementation or independent reproduction.
