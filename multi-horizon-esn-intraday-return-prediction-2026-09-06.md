---
schema: strategy-research-record-v1
title: "Multi-Horizon Echo State Network Intraday Return Prediction via Reservoir Computing"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - echo-state-network
  - reservoir-computing
  - intraday
  - high-frequency
  - return-prediction
  - multi-horizon
  - cross-sectional
  - equity
  - machine-learning
status: research-only
confidence: medium
source_as_of: 2026-09-03
sources:
  - "Ballarin, G., Capra, J., & Dellaportas, P. (2025/2026). 'Multi-Horizon Echo State Network Prediction of Intraday Stock Returns.' arXiv:2504.19623v2 [q-fin.CP]. https://arxiv.org/abs/2504.19623"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Horizon Echo State Network Intraday Return Prediction via Reservoir Computing

## Provenance

- **Authors:** Giovanni Ballarin (Universität Sankt Gallen, Mathematics and Statistics Division), Jacopo Capra (UCL, Department of Statistical Science), Petros Dellaportas (UCL, Department of Statistical Science; Athens University of Economics and Business, Department of Statistics)
- **Paper:** Multi-Horizon Echo State Network Prediction of Intraday Stock Returns
- **arXiv:** 2504.19623v2 (v1 submitted 28 April 2025; v2 updated 3 September 2026)
- **URL:** https://arxiv.org/abs/2504.19623
- **Pages:** 50
- **Subjects:** q-fin.CP, q-fin.ST
- **Data source:** AlgoSeek US equity high-frequency data (SIP consolidated feed, all US exchanges + FINRA), 1-minute bars downsampled to 10-minute resolution
- **Sample period:** January 2013 – December 2013 (12 months, ~16,000 intraday observations)
- **Universe:** 1,290 US stocks; portfolio evaluation subset: 388 stocks (volume-filtered for 10-minute tradability)
- **Hyperparameter tuning sample:** Q4 2012 (out-of-sample period before the test year)

## Economic mechanism

### Source-reported

The authors propose that intraday stock returns contain nonlinear predictive information that is not fully captured by linear models or random forests. They construct idiosyncratic z-score signals following Avellaneda & Lee (2010) — measuring each stock's cumulative residual deviation from its Ornstein-Uhlenbeck mean in units of stationary standard deviation — and feed these signals into an Echo State Network (ESN). The ESN nonlinearly combines signals over time via a recurrent state equation with randomly sampled (untrained) parameters, and predicts returns through a linear readout layer trained by ridge-regularized least squares. The authors argue this approach captures nonlinear cross-temporal signal interactions more efficiently than fully trained neural networks or tree-based ensembles.

### Research interpretation

The hypothesized mechanism is that reservoir computing (ESN) provides a computationally efficient nonlinear feature expansion of cross-sectional z-score signals, where the random recurrent state captures higher-order temporal dependencies that linear models miss. The linear readout layer then maps these expanded features to return predictions via regularized regression. The economic claim is that the nonlinear state transformation improves cross-sectional return ranking, which translates to better mean-variance portfolio allocation at intraday horizons.

Signal components:
- **Signal construction:** Avellaneda-Lee idiosyncratic z-scores with PCA factor regression (15 market factors), OU mean-reversion estimation across 6 lookback windows (P ∈ {10, 20, 30, 60, 100, 150} ten-minute intervals)
- **ESN state transformation:** Recurrent state X_t = αX_{t-1} + (1-α)φ(ρA·X_{t-1} + γC·Z_t) with K=100 state dimensions, horizon-specific hyperparameters
- **Readout:** Linear ridge-regularized least squares with cross-validated penalty matrix
- **Regime filter:** None explicit; the rolling-window training implicitly adapts to regime changes

## Signal

### Formation timestamp
- Signals formed every 10 minutes during US market hours (9:30 AM – 3:50 PM EST)
- State decay: missing signals replaced with zeros; state iterates forward but excluded from training
- No overnight positions; book fully exits at 3:50 PM via closing auction

### Lookback
- z-score signals: cumulative residual over lookback windows P ∈ {10, 20, 30, 60, 100, 150} ten-minute intervals
- PCA factor regression: rolling window (details in Appendix B)
- ESN state: implicitly incorporates full signal history via recurrent state equation
- Training window size Mt,h and buffer τh ≥ h per horizon (tuned via cross-validation)

### Entry
- **Long:** Top-ranked stocks by predicted return at each 10-minute rebalance (MV portfolio weights via Σ̂^{-1}·r̂)
- **Short:** Bottom-ranked stocks (unconstrained MV allows negative weights)
- **Order timing:** Signal at t predicts return at t+h; portfolio rebalanced every 10 minutes

### Exit
- Full book exit at 3:50 PM (closing auction price)
- Intra-day: rebalance every 10 minutes based on updated predictions

### Holding period
- Maximum: 10 minutes (10-min horizon) to end-of-day
- Non-overlapping returns used for 10-minute horizon portfolio evaluation
- Rebalance cadence: every 10 minutes

### Parameters (source-reported)
- State dimension K = 100 (all horizons)
- Horizon-specific: α (leak rate), ρ (spectral radius), γ (input scaling), A-sparsity, C-sparsity — see Table 1 in source
- Hyperparameters tuned on Q4 2012 data to minimize cumulative MSFE per horizon

### Position sizing
- Unconstrained mean-variance: w = Σ̂^{-1}·r̂, normalized to sum to 1
- Covariance: Ledoit-Wolf nonlinear shrinkage estimator (daily frequency)
- research-proposed: no turnover constraint, leverage cap, or position limit applied

## Required data

- **Instrument:** US equities (1,290 stocks from AlgoSeek SIP consolidated feed)
- **Venue:** All US exchanges + FINRA (consolidated SIP)
- **Market type:** Equity spot (no derivatives, no shorting costs modeled)
- **Timeframe:** 10-minute bars (downsampled from 1-minute)
- **Fields:** OHLCV (1-minute bars → 10-minute aggregation); PCA factor returns; idiosyncratic residuals
- **Timestamp:** Eastern Standard Time (EST)
- **Point-in-time:** SIP consolidated feed; no look-ahead in signal construction (OU estimation uses only past data)
- **Missing data:** Forward-fill returns; state decay (zeros) for missing signals in ESN; no imputation for ESN state
- **Data vendor:** AlgoSeek (https://www.algoseek.com/)

## Execution assumptions

- **Signal-to-order timing:** Signal at t predicts return at t+h; portfolio rebalanced at each 10-minute timestamp
- **Execution:** Closing auction at 3:50 PM for end-of-day exit; intra-day rebalancing assumed instant
- **Fill model:** Assumed perfect fill at mid/rebalancing price (no slippage modeled beyond transaction costs)
- **Fees:** 1 basis point transaction cost applied to portfolio return calculations (net-of-cost returns reported)
- **Spread:** Not explicitly modeled; assumed subsumed within 1 bps cost
- **Slippage:** Not explicitly modeled beyond the 1 bps transaction cost
- **Impact:** Not modeled; unconstrained MV weights may generate large positions in small-cap names
- **Leverage/margin:** Not modeled; weights normalized to sum to 1 (long-only constraint from normalization, but individual weights can be large)
- **Shorting:** MV weights allow negative values (implicit shorting), but no borrow cost modeled
- **Capacity:** Not assessed; 388-stock subset may not be tradeable at 10-minute frequency in practice
- **Latency:** Not modeled; assumed instantaneous signal-to-order

## Evidence

### Source-reported

- **MSFE reduction:** ESN achieves up to 0.8775% MSFE reduction vs. linear baseline at 10-minute horizon (Table 3). Reduction diminishes at longer horizons: 0.6059% (30 min), 0.3890% (60 min), 0.3023% (2 hours), 0.0148% (eod).
- **R² values (Table 4):** All negative (typical for high-frequency returns), but ESN consistently improves over linear baseline: -0.0675 vs -0.0766 (10 min), -0.1146 vs -0.1213 (30 min), -0.1084 vs -0.1128 (60 min), -0.1621 vs -0.1656 (2 hours), -0.1758 vs -0.1760 (eod).
- **Statistical significance:** Diebold-Mariano tests reject equal predictive ability at 1% level for all horizons except eod (p > 0.01). Model Confidence Set: ESN is the sole member of the best-model set at 5% level for all horizons except eod (where both ESN and RF are included).
- **Random forest comparison:** RF performs worse than linear baseline by approximately the same absolute margin as ESN outperforms it (Table 3: RF MSFE +1.0024% at 10 min vs ESN -0.8775%).
- **Portfolio performance (10-min horizon, Table 6):** Sharpe ratio: ESN 1.529, EW 1.422, RF 0.166, Ridge -1.044, Linear -1.181. Max drawdown: ESN -0.465, EW -0.743, RF -33.057, Ridge -85.350, Linear -22.882.
- **Net-of-cost returns:** With 1 bps transaction cost, the unconstrained EW portfolio outperforms all forecast-based strategies net of costs (Figure D.3). ESN has substantially lower turnover than Linear/Ridge/RF.
- **Runtime (Table 2):** ESN 139 seconds for full year, Linear 56 seconds, Ridge 89 seconds, RF 2,561 seconds. ESN is ~2.5× linear, ~18× faster than RF.
- **Robustness to random draws:** 100 different ESN random seeds tested; MSFE distribution is highly concentrated around median with tight 90% and 50% frequency bands (Figure 4).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- At end-of-day (eod) horizon, ESN improvement is negligible (0.0148% MSFE reduction); MSFE sometimes exceeds linear baseline (Figure 2).
- Unconstrained MV portfolio with forecast-based strategies is net-negative after 1 bps transaction costs (except ESN, which is slightly positive). The EW passive portfolio outperforms all active strategies net of costs. Source notes this "illustrates the important distinction between statistical predictability and the economic implementability of a forecasting signal."
- Sample is only 12 months (2013); no out-of-sample period beyond the training-tuning split.
- Single-year sample may not be representative of different market regimes.

## Falsification plan

1. **Out-of-sample extension:** Test ESN prediction on multiple years (e.g., 2014–2020) with rolling hyperparameter re-tuning to verify MSFE improvement is not specific to 2013. research-defined falsification threshold: MSFE improvement < 0.1% at 10-min horizon across 3+ years → weaken hypothesis.
2. **Transaction cost sensitivity:** Re-evaluate portfolio performance with realistic costs (5–10 bps round-trip including spread and market impact). research-defined falsification threshold: ESN Sharpe < EW Sharpe net of costs → fail to demonstrate economic value beyond passive.
3. **Parameter perturbation:** Vary state dimension K, leak rate α, spectral radius ρ over wide ranges. Source shows robustness to random draws but not to systematic hyperparameter shifts.
4. **Alternative universe:** Apply to non-US equities, different market-cap segments, or different time periods to test generalizability.
5. **Ablation:** Remove individual z-score lookback windows to test which horizons contribute most to ESN performance.
6. **Capacity/liquidity test:** Restrict to most liquid decile only; test whether MSFE improvement survives when thinly traded stocks are excluded.
7. **Competing explanation:** Test whether the improvement is driven by nonlinear signal interaction or simply by the additional model complexity (parameter count). Compare ESN with K=D (reducing to linear model) to isolate nonlinear contribution.

## Crypto portability

**unproven**

The mechanism originates from US equity intraday return prediction. Direct portability to crypto faces several challenges:
- **Market structure:** US equities have a single consolidated feed (SIP); crypto markets are fragmented across venues with different candle boundaries, liquidity profiles, and tick sizes.
- **24/7 sessions:** Crypto trades continuously; the ESN's session-bounded rebalancing (9:30 AM – 3:50 PM) does not transfer directly. The OU mean-reversion signal construction assumes a bounded trading session with overnight gaps.
- **Data availability:** AlgoSeek-quality tick data is not freely available for most crypto pairs. OHLCV at 10-minute resolution is available but idiosyncratic signal construction (PCA + OU residuals) requires足够大的 cross-section.
- **Market microstructure:** Crypto perpetual futures have funding rates, mark/index prices, and leverage dynamics absent in equities. The signal construction would need adaptation.
- **Signal relevance:** The z-score signal measures mean-reversion of idiosyncratic residuals; crypto assets may exhibit different return dynamics (e.g., trending behavior, regime switching).

A crypto adaptation would require: (1) re-engineering the signal for crypto cross-sections with appropriate factor models, (2) adapting the ESN for 24/7 continuous sessions, (3) incorporating funding rates and leverage effects. This is speculative and not demonstrated in the source.

## Limitations

- **Single-year sample (2013):** Only 12 months of out-of-sample testing. The source acknowledges this is "short, but still performance-representative" for high-frequency data. No multi-year validation.
- **US equities only:** No evidence on other asset classes, geographies, or crypto.
- **Unconstrained portfolio:** No turnover, leverage, position, or capacity constraints applied. Net-of-cost performance is inferior to passive EW.
- **Transaction cost model:** Only 1 bps; does not model spread, market impact, or partial fills.
- **No overnight risk:** Book exits fully at 3:50 PM; no assessment of overnight gap risk.
- **Hyperparameter tuning on Q4 2012:** The tuning period is before the test year but is a single quarter; no walk-forward or cross-validation across multiple periods.
- **Missing data handling:** State decay (zero replacement) for missing signals is pragmatic but may introduce bias; no formal analysis of missingness patterns.
- **ESN randomness:** While robust to different random draws (100 seeds tested), the paper does not provide theoretical guarantees for the specific financial application.
- **No comparison with deep learning baselines:** RF is the only ML baseline; no LSTM, GRU, or transformer comparison.
- **Computational reproducibility:** Full pipeline runs in ~2.5 minutes per year, but specific Optuna tuning budgets and convergence criteria not fully specified.

## Implementation status

not-implemented. No implementation in our research stack has been completed. The paper provides sufficient signal construction detail (Avellaneda-Lee z-scores, ESN state equation, ridge regression readout) for reconstruction, but no public code repository is linked.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The source demonstrates statistical predictability improvement in a single-year US equity sample but does not demonstrate net economic value after realistic transaction costs. The unconstrained MV portfolio analysis shows that net-of-cost returns are inferior to passive EW.

## Related Wiki records

No directly related records identified. The reservoir computing / ESN approach is methodologically distinct from existing records in this repository (which primarily cover RL-based, factor-based, and LLM-based strategies).

## Sources

- Ballarin, G., Capra, J., & Dellaportas, P. (2025/2026). Multi-Horizon Echo State Network Prediction of Intraday Stock Returns. arXiv:2504.19623v2 [q-fin.CP]. https://arxiv.org/abs/2504.19623. v1 submitted 28 April 2025; v2 updated 3 September 2026. 50 pages.
