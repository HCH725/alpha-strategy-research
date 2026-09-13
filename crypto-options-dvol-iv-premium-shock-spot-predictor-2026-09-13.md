---
schema: strategy-research-record-v1
title: "Crypto Options Implied Volatility Shock as Short-Horizon Spot Predictor: DVOL IV-Premium Signal"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - implied-volatility
  - DVOL
  - deribit
  - spot-prediction
  - lead-lag
  - walk-forward
  - regime-dependent
status: research-only
confidence: medium
source_as_of: 2026-06-16
sources:
  - "https://github.com/TanvirCCC/options-implied-crypto-signals/blob/111923468f97767631af6aeb537d2e2905567cb8/README.md"
  - "https://github.com/TanvirCCC/options-implied-crypto-signals/blob/111923468f97767631af6aeb537d2e2905567cb8/src/signals.py"
  - "https://github.com/TanvirCCC/options-implied-crypto-signals/blob/111923468f97767631af6aeb537d2e2905567cb8/src/backtest.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Options Implied Volatility Shock as Short-Horizon Spot Predictor: DVOL IV-Premium Signal

## Provenance

- **Primary Source:** Tanvir Chowdhury, "Options-Implied Crypto Signals," GitHub repository, MIT license, MSc Mathematical Trading and Finance, Bayes Business School.
- **Repository URL:** https://github.com/TanvirCCC/options-implied-crypto-signals
- **Head Commit SHA:** `111923468f97767631af6aeb537d2e2905567cb8`
- **Key Files:** `src/signals.py` (D1–D4 signal definitions), `src/backtest.py` (event-driven backtest with walk-forward), `src/lead_lag.py` (cross-correlation, Granger causality, placebo tests), `src/event_study.py` (CAR analysis), `src/cross_asset.py` (propagation diagnostics).
- **Source As-of Date:** 2026-06-16 (README data coverage: 2022-01 to 2026-06).
- **Publication Status:** Public GitHub repository with MIT license; not peer-reviewed. Code audit surfaced and fixed 4 bugs before final result publication.

## Economic mechanism

### Source-reported

The author hypothesizes that spikes in Deribit's DVOL (implied-volatility index, analogous to CBOE VIX) carry directional information about spot crypto prices in the next 1–24 hours. The rationale is that sudden jumps in implied volatility—particularly unusual gaps between implied and realised volatility—reflect informed traders expressing directional views through options before those views materialize in spot markets. This is consistent with the informed-trading signature: options activity precedes spot moves when informed participants choose the leverage and payoff asymmetry of options over spot.

### Research interpretation

The D3 headline signal (IV-premium z-score shock) is formally a **volatility risk premium (VRP) signal repurposed for directional prediction**: when the IV-premium (DVOL minus realised vol) spikes to z > 2σ, the options market is pricing a much larger move than recent history warrants. The hypothesis is that this excess pricing is not random fear but reflects informed flow with directional conviction.

Falsifiable mechanism: the VRP shock captures informed-options-flow that is net-long (or net-short) in a way that is not fully absorbed by the realised-vol level, creating a short-horizon directional edge. The signal is asymmetric: it fires when the gap between implied and realised vol becomes unusually wide, not merely when vol is high.

Components:
- **Signal:** D3 = IV-premium (DVOL − realised vol) rolling z-score > 2σ (bullish) or < −2σ (bearish)
- **Universe:** ETH (headline), BTC (no effect found)
- **Horizon:** 24-hour holding period
- **Risk filter:** 1.5σ pre-event vol stop-loss

## Signal

### D3 headline signal

- **Formation timestamp:** Hourly. IV-premium = DVOL(t) − realised_vol(t), where realised vol is computed from hourly Binance spot returns (rolling window unspecified in README; code shows rolling(30) on log-returns).
- **Lookback:** 30-bar rolling window for z-score computation (30 hourly observations = 30 hours).
- **Entry trigger (bullish):** z-score of IV-premium > 2.0 (threshold label: research-proposed).
- **Entry trigger (bearish):** z-score of IV-premium < −2.0 (threshold label: research-proposed).
- **Direction:** Long spot when bullish signal fires; short spot when bearish signal fires (direction label: research-proposed, as the README does not specify explicit long/short construction).
- **Entry timing:** T+1 bar after signal fires (next hourly bar).
- **Exit:** Fixed 24-hour holding period (24 hourly bars), or early exit via stop-loss.
- **Stop-loss:** 1.5 × pre-event 60-bar realised vol (threshold label: research-proposed).
- **Cooldown:** 24 bars between consecutive signals (research-proposed).
- **Position sizing:** research-proposed; backtest uses 1% of capital per trade.

### D1, D2, D4 signals (evaluated but not headline)

- **D1:** DVOL log-change z-score > 2σ AND |Δlog DVOL| > 2%. Failed Granger causality.
- **D2:** |Δlog DVOL| ≥ 5% absolute shock. Sparse (~20–25 events/yr). Walk-forward catastrophic.
- **D4:** D1 conditions plus intrabar DVOL range z-score ≥ 1.5σ. Too few events filtered.

### Underspecified items

- The exact realised-vol estimator and lookback window are not stated in the README; code shows rolling(30) on hourly returns.
- The Sharpe annualisation factor is stated as sqrt(8760) (hourly-equity Sharpe × sqrt(8760)). This is appropriate for hourly data.
- Position sizing, long/short construction, and portfolio-level risk management are not specified in the README; the backtest uses 1% fixed sizing.

## Required data

- **Instrument:** ETH spot (primary), BTC spot (secondary, no effect found).
- **Venue:** Deribit (DVOL index), Binance (spot hourly).
- **Market type:** Spot (for signal generation); DVOL is an options-implied index from Deribit options.
- **Timeframe:** Hourly bars.
- **Fields:** DVOL close/high/low (from Deribit), hourly OHLCV spot (from Binance).
- **Data range:** 2022-01 to 2026-06 (4.5+ years).
- **Point-in-time:** DVOL is published continuously by Deribit; spot data from Binance public archive. No look-ahead issues identified in the signal computation.
- **Timestamp:** UTC.
- **Missing-data:** Not explicitly addressed in README.

## Execution assumptions

- **Signal-to-order timing:** T+1 bar (next hourly bar after signal fires). Same-bar execution is not used.
- **Order type:** market order assumed (research-proposed).
- **Fill model:** At mid price minus slippage (research-proposed).
- **Fees:** Commission 0.075% per trade (assumed by backtest; label: research-proposed).
- **Slippage:** 0.025% per trade (assumed by backtest; label: research-proposed).
- **Spread:** Not modeled separately from slippage.
- **Funding:** Not applicable for spot; no perpetual funding included.
- **Leverage:** Not specified; backtest uses 1% fixed sizing.
- **Capacity:** Not stated; 182 OOS trades over ~4 years implies ~45 trades/year, ~1 per week average.

## Evidence

### Source-reported

Source reports the following headline result from walk-forward validation:

| Metric | Value |
|--------|-------|
| Strategy | ETH_D3_24h |
| OOS trades | 182 |
| OOS Sharpe | 3.83 |
| Walk-forward mean | 2.76 |
| Walk-forward range | −7.24 to +14.72 |

Source notes:
- "ETH IV-risk-premium shocks show a promising short-horizon directional edge after correcting timing, signal, and metric issues, but the effect is **regime-dependent** and requires further conditioning before it can be treated as deployable alpha."
- BTC DVOL spikes do not show a directional effect.
- The headline result was flipped from ETH_D2 to ETH_D3 after an audit fixed 4 bugs (off-by-one in backtest, ignored alpha parameter, overstated Sharpe annualisation, identical D4 signals).
- Walk-forward dispersion is large: per-window OOS Sharpes range from −7 to +15 across 13 windows.
- Cross-asset propagation analysis: BTC DVOL → 15 altcoins tested but correlation is raw, not beta-adjusted.

Source-reported Granger causality:
- D1: Failed Granger causality test.
- D3: Not explicitly reported in README for Granger; event study and walk-forward are the primary validation methods.

Source-reported event study:
- CAR (cumulative abnormal returns) analysis conducted (notebook 04); specific numbers not provided in README.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- BTC DVOL shows no directional signal (source-reported).
- Walk-forward window dispersion is extreme (−7 to +15 Sharpe across 13 windows), indicating regime dependence (source-reported).
- D1 signal failed Granger causality (source-reported).
- D2 signal walk-forward was "catastrophic" before correction; corrected result not separately reported.
- 4 bugs found and fixed before final result; the original headline finding was wrong (source-reported, demonstrating research process integrity).
- Cross-asset propagation analysis is incomplete (raw correlations, not beta-adjusted; source-reported as a limitation).

None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample period extension:** Extend the sample beyond June 2026; the current sample ends mid-2026. A genuine signal should persist across regimes.
2. **Regime conditioning:** Identify when D3 works and when it inverts (source-acknowledged next step). Without regime conditioning, the signal is not deployable.
3. **Parameter sensitivity:** Test z-score thresholds other than 2.0 (research-proposed: test z ∈ {1.5, 2.0, 2.5, 3.0}).
4. **Holding period sensitivity:** Test holding periods other than 24h (research-proposed: test H ∈ {6, 12, 24, 48, 72}).
5. **Fee/stress sensitivity:** Current cost assumptions are 0.075% + 0.025% = 0.10% round trip. Test at 2× and 3× costs. The walk-forward range (−7 to +15) suggests high cost sensitivity.
6. **BTC replication:** Confirm BTC shows no signal (source-reported null; should be a control, not just an absence).
7. **Placebo tests:** The source conducts 2 placebo tests (notebook 03); results not detailed in README.
8. **Capacity/liquidity stress:** The signal fires ~45 times/year on ETH; test whether fills are achievable at signal resolution (hourly DVOL → next-hour entry).

## Crypto portability

direct

The signal originates from and is tested on crypto spot markets (ETH, BTC) using Deribit options data. The mechanism—options-implied vol shocks predicting spot moves—is native to crypto markets. The 24/7 trading structure and hourly DVOL resolution are crypto-specific.

Crypto-specific risks:
- **DVOL availability:** Deribit DVOL is the primary input; if Deribit changes its methodology or liquidity shifts to other venues, the signal may degrade.
- **Spot vs. perpetual:** The backtest uses spot; perpetual execution would add funding rate exposure.
- **Liquidity:** ETH hourly spot on Binance is liquid; the 0.10% cost assumption is plausible but may underestimate slippage during vol spikes when the signal fires.
- **Regime dependency:** The signal is explicitly regime-dependent; the walk-forward range (−7 to +15) is large, and the source acknowledges regime conditioning is needed before deployment.

## Limitations

- **Regime-dependent:** Walk-forward window dispersion is extreme (−7 to +15 Sharpe), indicating the signal is not consistently profitable across regimes.
- **Single-asset limitation:** Works on ETH, not BTC; generalizability to other crypto assets is untested.
- **Non-peer-reviewed:** This is an MSc project, not published in an academic journal or top conference.
- **Bug history:** The headline result was flipped after 4 bugs were found and fixed; while this demonstrates research integrity, it also shows the original analysis was materially incorrect.
- **Incomplete cross-asset analysis:** Propagation to altcoins uses raw correlations, not beta-adjusted residuals.
- **Underspecified realised vol:** The exact estimator and lookback window for realised vol are not documented in the README.
- **No transaction-cost sensitivity analysis:** The paper reports cost assumptions but does not provide sensitivity analysis across cost tiers.
- **182 OOS trades:** Sample size is modest; statistical power for regime-subgroup analysis is limited.
- **Source-reported limitation:** "the effect is regime-dependent and requires further conditioning before it can be treated as deployable alpha."

## Implementation status

Not implemented in our research stack. No prototype, backtest, or validation has been conducted by us.

## Adoption boundary

This record is research material only. It does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

The source itself states the signal "requires further conditioning before it can be treated as deployable alpha."

## Related Wiki records

- [[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay]] — VRP harvesting (volatility carry, not directional prediction); same IV-premium concept used differently (sell vol vs. predict direction).
- [[quant/bitcoin-options-implied-volatility-risk-reversal-skew]] — Risk-reversal skew as directional predictor; different mechanism (smile shape vs. level shock).
- [[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]] — Generic VRP z-score heuristic; underspecified, no empirical validation.

## Sources

- Tanvir Chowdhury, "Options-Implied Crypto Signals," GitHub repository, MIT license. https://github.com/TanvirCCC/options-implied-crypto-signals. Commit SHA: `111923468f97767631af6aeb537d2e2905567cb8`. Source as-of: 2026-06-16.
- Deribit DVOL index (https://www.deribit.com) — options-implied volatility index for BTC and ETH.
- Binance public spot archive — hourly OHLCV data for 15 USDT pairs.
- Bailey & Lopez de Prado (2014), "The Deflated Sharpe Ratio," referenced for multiple-testing correction.
- Granger (1969), "Investigating Causal Relations by Econometric Models and Cross-Spectral Methods," referenced for Granger causality methodology.
