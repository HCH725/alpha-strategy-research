---
schema: strategy-research-record-v1
title: "Simple Dynamic Stock/Bond/Gold Portfolios: Volatility-Controlled and Markowitz-Optimized Allocation"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volatility-targeting
  - markowitz
  - portfolio-construction
  - traditional-assets
status: research-only
confidence: high
source_as_of: 2026-09-06
sources:
  - https://arxiv.org/abs/2609.07946
  - https://github.com/cvxgrp/simple-portfolio-code
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Simple Dynamic Stock/Bond/Gold Portfolios: Volatility-Controlled and Markowitz-Optimized Allocation

## Provenance

- **Primary Source:** Nikhil Devanathan, Alexandros E. Tzikas, Stephen P. Boyd (Stanford University), *"Simple Dynamic Stock/Bond/Gold Portfolios"*, arXiv preprint `arXiv:2609.07946v1 [q-fin.PM]`, submitted September 6, 2026.
- **Abstract:** https://arxiv.org/abs/2609.07946
- **Full text HTML:** https://arxiv.org/html/2609.07946v1
- **Full text PDF:** https://arxiv.org/pdf/2609.07946v1
- **DOI:** 10.48550/arXiv.2609.07946
- **Open-source code:** https://github.com/cvxgrp/simple-portfolio-code
- **Verification Integrity:** This record was generated following direct inspection of the primary paper text, derivation sections, Tables 1–3, Appendix F, and Appendix G. The GitHub repository `cvxgrp/simple-portfolio-code` was verified to exist and contain the described code structure (data, scripts, src, tests directories). No secondary search snippets or AI aggregator summaries were used to formulate strategy mechanics or empirical figures. A pre-write repository audit confirmed zero existing records matching `arXiv:2609.07946` or the Devanathan-Tzikas-Boyd dynamic stock/bond/gold framework.

## Economic mechanism

### Source-reported

The paper compares three families of dynamic portfolios (stocks + bonds + gold + cash) against fixed-weight benchmarks (60/40, 50/30/20). The two key mechanisms are:

1. **Volatility control:** Diluting a fixed-weight portfolio with cash each month so that estimated ex-ante volatility equals a target (7% annualized). This reduces drawdowns and improves Sharpe ratio by de-risking during high-volatility regimes.

2. **Markowitz optimization:** Monthly convex optimization maximizing estimated next-month return net of trading cost, subject to a volatility constraint (σ_tgt = 7%), non-negativity, and a deviation constraint keeping relative risky-asset allocation within L1 distance 1 of the 50/30/20 target. Two return-forecast variants:
   - **Simple Markowitz:** Exponentially weighted moving average of past daily returns (half-life 252 trading days, scaled ×21 to monthly), i.e., a pure momentum signal.
   - **Markowitz (full):** Rolling regression forecast using asset-specific features (trailing returns, volumes, volatilities), macro-financial features (yields, inflation, VIX), and Fama-French factors.

### Research interpretation

The mechanism is not a novel alpha signal but a demonstration that standard quantitative tools — volatility targeting, momentum, and Markowitz optimization — produce meaningful risk-adjusted improvement over passive allocation when applied under realistic constraints (long-only, no leverage, monthly rebalancing, public data, net of conservative trading costs). The alpha source is (a) time-varying risk allocation via volatility control, (b) momentum-based return forecasting, and (c) cost-aware convex optimization. The paper explicitly states: "It is not methodological: the methods we use are all standard and well established."

The underlying hypothesis is that simple momentum signals combined with risk-aware allocation generate excess risk-adjusted returns relative to fixed-weight benchmarks in traditional multi-asset portfolios. The mechanism relies on momentum persistence in broad asset classes and regime-dependent volatility clustering.

## Signal

### Formation timestamp
- Monthly rebalancing on the first trading day of each month.
- Covariance and return estimates use data available up to the rebalance date (causal, no look-ahead).

### Lookback
- **Covariance estimate (Σ_t):** Empirical covariance of daily returns over trailing 111 trading days (~5 months), annualized. (`source-reported`)
- **Simple Markowitz return forecast (α_t):** Exponentially weighted moving average of each asset's daily returns, half-life 252 trading days (~1 year), multiplied by 21 to scale to monthly. (`source-reported`)
- **Full Markowitz return forecast:** Rolling regression linking asset-specific, macro-financial, and Fama-French features to forward returns (details in paper Appendix B). (`source-reported`)

### Entry
- Monthly rebalance to the optimal weight ŵ_t solving:
  - **maximize** α_t^T w + r_t^mrf (1 - 1^T w) - (s/2) ||w - w_t||_1
  - **subject to:** w ≥ 0, 1^T w ≤ 1, ||w - (1^T w) w_tgt||_1 ≤ 1^T w, (w^T Σ_t w)^{1/2} ≤ σ_tgt
  - where w_tgt = (0.5, 0.3, 0.2), σ_tgt = 7%, s = 0.0005 (5 bps). (`source-reported`)

### Exit
- No separate exit logic; positions are rebalanced monthly. The optimization explicitly accounts for the cost of transitioning from current weights w_t to new weights ŵ. (`source-reported`)

### Holding period
- Monthly rebalance cadence; positions held between monthly rebalances. (`source-reported`)

### Parameters
- **Target volatility:** σ_tgt = 7% annualized. (`source-reported`)
- **Bid-ask spread:** s = 0.0005 (5 bps round-trip). (`source-reported`)
- **Target weights (deviation anchor):** w_tgt = (SPY: 50%, AGG: 30%, GLD: 20%). (`source-reported`)
- **Deviation constraint:** L1 distance of relative weights from w_tgt ≤ 1. (`source-reported`)
- **Covariance lookback:** 111 trading days. (`source-reported`)
- **Momentum half-life:** 252 trading days. (`source-reported`)
- All parameters are source-reported; no Scout-chosen parameters.

## Required data

- **Instruments:** SPY (broad U.S. equity ETF), AGG (U.S. investment-grade bond ETF), GLD (gold ETF). (`source-reported`)
- **Venue:** ETFs traded on U.S. exchanges; data from Yahoo Finance. (`source-reported`)
- **Market type:** Spot ETFs (long-only). (`source-reported`)
- **Timeframe:** Daily adjusted close prices for return and covariance estimation; monthly rebalancing. (`source-reported`)
- **Fields:** Daily adjusted close prices (SPY, AGG, GLD); federal funds rate (FRED series DFF); core CPI (FRED series CPILFESL); Fama-French factors. (`source-reported`)
- **Missing-data:** Not stated in source; data assumed complete from Yahoo Finance and FRED.

## Execution assumptions

- **Signal-to-order timing:** Rebalance on the first trading day of each month; orders executed at month start. (`source-reported`)
- **Order type:** Not explicitly specified; implied market orders for monthly rebalancing. (data gap)
- **Fill model:** Not specified; assumed immediate fill at close. (data gap)
- **Fees:** 5 bps round-trip spread charged on each trade; optimization objective includes trading cost. (`source-reported`)
- **Slippage:** Not separately modeled beyond the 5 bps spread. (data gap)
- **Impact / capacity:** Not discussed; paper focuses on individual-investor-scale portfolios. (data gap)
- **Leverage / margin:** None; long-only, no leverage. (`source-reported`)
- **Shorting:** None; long-only. (`source-reported`)
- **Latency:** Not relevant for monthly rebalancing. (data gap)
- **Partial fills / failures:** Not discussed. (data gap)

## Evidence

### Source-reported

All performance metrics below are extracted from Devanathan, Tzikas & Boyd (arXiv:2609.07946v1, Tables 1–3, Appendix G), evaluated over the 20-year period Jan 2006 – Jan 2026, net of 5 bps trading cost:

| Portfolio | Return | Volatility | Sharpe | Max DD | Mean DD | Turnover |
|---|---|---|---|---|---|---|
| Markowitz | 11.6% | 9.0% | 1.08 | 18.1% | 3.0% | 284.4% |
| Simple Markowitz | 10.4% | 9.3% | 0.91 | 15.8% | 3.1% | 278.9% |
| 50/30/20 VC | 7.8% | 7.3% | 0.82 | 15.9% | 2.4% | 79.0% |
| 60/40 VC | 7.1% | 7.4% | 0.71 | 16.9% | 2.6% | 85.0% |
| 50/30/20 | 9.1% | 10.3% | 0.70 | 27.1% | 3.0% | 4.0% |
| 60/40 | 8.1% | 11.3% | 0.56 | 33.7% | 3.8% | 3.4% |

Markowitz sub-period Sharpe ratios (Table 2): 2006–2011: 1.34; 2011–2016: 0.86; 2016–2021: 1.16; 2021–2026: 0.97.

Risk-based allocation comparison (Appendix F): Risk parity, equal risk contribution, minimum variance, and Black–Litterman on the same assets/data achieve Sharpe ratios between 0.60 and 0.85, well below the Markowitz 1.08.

Cost sensitivity (Appendix G): At 10 bps, Markowitz Sharpe = 1.07; at 20 bps, Markowitz Sharpe = 1.03. Rankings unchanged.

Statistical significance: Detailed bootstrap analysis in Appendix C (not fully reproduced here; paper claims significance at conventional levels).

### Independently reproduced

Not independently reproduced. All empirical findings reflect direct extraction from Devanathan, Tzikas & Boyd (arXiv:2609.07946v1, 2026). The open-source code at `cvxgrp/simple-portfolio-code` is available for replication.

### Negative evidence

- The paper acknowledges that across a large set of equity strategies, volatility management does not systematically improve out-of-sample performance (citing Cederburg et al. 2020), though their specific three-asset setting shows improvement.
- The paper notes return-forecasting strategies can exhibit decreasing performance over time as other traders learn the opportunities (citing McLean and Pontiff 2016), but reports no clear sign of this over their 20-year simulation.
- Results are specific to U.S. SPY/AGG/GLD over 2006–2026; different asset universes, periods, or geographies may not replicate.

## Falsification plan

1. **Out-of-sample period extension:** Re-run beyond Jan 2026 using live forward data. Failure: Sharpe ratio drops below 0.70 (the 50/30/20 VC benchmark). `[research-defined falsification threshold]`
2. **Asset universe substitution:** Replace SPY/AGG/GLD with alternative broad-market ETFs or different asset classes (e.g., emerging market equity, TIPS, commodities). Failure: Markowitz Sharpe drops below the volatility-controlled benchmark. `[research-defined falsification threshold]`
3. **Parameter perturbation:** Test σ_tgt ∈ {5%, 10%, 15%}, covariance lookback ∈ {63, 111, 252} days, momentum half-life ∈ {126, 252, 502} days. Failure: Rank reversal of Markowitz vs. 50/30/20 VC at any tested setting. `[research-defined falsification threshold]`
4. **Ablation:** Run optimization without the momentum forecast (α_t = 0) to isolate the contribution of return forecasting vs. pure risk control. Failure: Markowitz Sharpe falls below 0.82 (50/30/20 VC level). `[research-defined falsification threshold]`
5. **Cost stress test:** Increase trading cost to 50 bps round-trip. Failure: Markowitz Sharpe drops below 0.80. `[research-defined falsification threshold]`
6. **Action on failure:** If the momentum forecast contribution is null or the optimization is not robust to parameter changes, retire the Markowitz variant and retain only the volatility-controlled approach.

## Crypto portability

`unproven`

The paper's mechanisms (momentum-based return forecasting + volatility targeting + Markowitz optimization) are general portfolio construction tools that could theoretically be applied to crypto asset portfolios. However:

- The paper evaluates only U.S. equity/bond/gold ETFs; no crypto assets are tested.
- Crypto assets exhibit much higher volatility (50–80% annualized vs. 10–19% for the tested ETFs), which would significantly alter the effective leverage and position sizing under a 7% volatility target.
- The 24/7 trading structure, perpetual funding rates, and venue fragmentation in crypto markets are not addressed.
- The momentum signal (EWMA with 252-day half-life) may behave differently in crypto's faster-regime environment.
- The 5 bps cost assumption is realistic for liquid ETFs but may be optimistic for some crypto pairs; however, major crypto perpetuals can achieve comparable or tighter effective spreads on top venues.

Any crypto adaptation would require re-validation of the momentum signal, covariance estimation horizon, and cost model under crypto-specific market microstructure.

## Limitations

- **Data gap:** Order type, fill model, and slippage beyond the 5 bps spread assumption are not specified.
- **Data gap:** Capacity / AUM limits not discussed; paper targets individual-investor scale.
- **Not independently reproduced:** All results are source-reported from the paper's own backtest.
- **Traditional-asset only:** Results apply to SPY/AGG/GLD; no crypto evidence exists.
- **Single sample path:** 20-year backtest on a single asset universe (U.S. market); different periods or geographies may differ.
- **High turnover:** Markowitz portfolios have ~284% annualized turnover, which may stress tax efficiency and operational costs beyond what the 5 bps spread captures.
- **Parameter sensitivity:** The paper tests some parameter variations but does not exhaustively explore the joint parameter space.
- **Regime dependency:** Performance in the 2006–2026 window may reflect specific macro regimes (low rates, QE, post-COVID recovery) that may not persist.

## Implementation status

`not-implemented`

No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader has been executed. No strategy family has been created, and no backtest campaign has been initiated. The open-source code at `cvxgrp/simple-portfolio-code` provides a fully reproducible reference implementation.

## Adoption boundary

`research-only`

This record captures theoretical and empirical research published in arXiv:2609.07946v1. Its presence in this repository does not constitute:
- proof of profitability;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- Related to the broader volatility-targeting and dynamic portfolio allocation family.
- No directly adjacent Wiki records identified for this specific framework.

## Sources

1. Nikhil Devanathan, Alexandros E. Tzikas, Stephen P. Boyd, *"Simple Dynamic Stock/Bond/Gold Portfolios"*, arXiv preprint `arXiv:2609.07946v1 [q-fin.PM]`, submitted September 6, 2026.
   - Abstract: https://arxiv.org/abs/2609.07946
   - Full text HTML: https://arxiv.org/html/2609.07946v1
   - Full text PDF: https://arxiv.org/pdf/2609.07946v1
   - DOI: 10.48550/arXiv.2609.07946
2. Stanford University Convex Optimization Group (`cvxgrp`), *"simple-portfolio-code: Simple Dynamic Stock/Bond/Gold Portfolios"*, GitHub public repository.
   - Repository URL: https://github.com/cvxgrp/simple-portfolio-code
   - Verified to exist with code structure: data/, scripts/, src/, tests/ directories.
