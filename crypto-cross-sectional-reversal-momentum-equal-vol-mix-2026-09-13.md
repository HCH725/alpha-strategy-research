---
schema: strategy-research-record-v1
title: "Crypto Cross-Sectional Reversal + Momentum Equal-Volatility Mixed Portfolio"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - cross-sectional
  - reversal
  - momentum
  - portfolio-construction
  - equal-volatility
  - market-neutral
status: research-only
confidence: medium
source_as_of: 2025-08-28
sources:
  - "ccollins80/crypto-stat-arb, commit d7623cf203afe5d64f3c04a4ff88550798e552ed, https://github.com/ccollins80/crypto-stat-arb (August 2025)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Reversal + Momentum Equal-Volatility Mixed Portfolio

## Provenance

Primary source: GitHub repository `ccollins80/crypto-stat-arb`, commit `d7623cf203afe5d64f3c04a4ff88550798e552ed` (latest as of 2025-08-28). The repository URL is https://github.com/ccollins80/crypto-stat-arb. The source is a public GitHub repository with backtesting framework, signal construction code, and walk-forward validation results.

The repository evaluates cross-sectional **reversal** and **momentum** strategies on 12 liquid cryptocurrency pairs using hourly bars, then combines them into diversified mixed sleeves using equal-volatility (risk parity) weighting. The source claims walk-forward out-of-sample results of Sharpe ~2.5 with significant alpha versus BTC.

Sample period: ~2.6 years of hourly data (~12,960 hourly observations for walk-forward). Universe: 12 liquid crypto pairs (BTC, ETH, and 10 altcoins). Baseline cost assumption: 7 bps per rebalance.

This record is intentionally separate from:
- `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md` (Arefev 2026), which falsifies cross-sectional momentum alone at taker fees on Binance perpetuals.
- `crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01.md`, which tests short-horizon mean reversion with taker-flow.
- `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md` (Vine 2026), which tests PCA-residual and cointegration pairs approaches.

The material distinction is: this source combines reversal (the dominant Sharpe contributor) with momentum (the diversifier) in an equal-volatility mixed portfolio, whereas the above records test either component in isolation or use fundamentally different signal-construction mechanisms.

## Economic mechanism

### Source-reported

Reversal captures short-term mean reversion: assets that underperform over a 2–4 bar lookback tend to bounce, and assets that outperform tend to give back gains. The source attributes this to behavioral overreaction and crowded positioning at short horizons in crypto markets.

Momentum captures medium-to-long-term trend persistence: assets that outperform over 336–500 bar lookbacks tend to continue. The source attributes this to delayed information diffusion and gradual positioning in crypto markets.

Equal-volatility weighting ensures each sleeve contributes equally on a risk-adjusted basis, improving portfolio Sharpe through diversification. The source reports near-zero correlation between the reversal and momentum sleeves (~−0.008), confirming genuine diversification.

### Research interpretation

The proposed alpha mechanism is a two-component cross-sectional strategy:

1. **Reversal component (primary alpha):** Short-term cross-sectional mean reversion. Assets with extreme short-horizon returns revert due to overreaction, liquidity pressure, or short-term crowded positioning. The banding (capping positions at 2.5σ) prevents excessive exposure to outlier moves and improves robustness.

2. **Momentum component (diversification + secondary alpha):** Medium-to-long-term cross-sectional momentum. Assets that have outperformed over weeks continue to outperform due to gradual information incorporation, slow-moving capital flows, or trend-following behavior.

3. **Equal-volatility weighting (portfolio construction):** Risk-parity allocation between the two sleeves ensures the portfolio is not dominated by the higher-Sharpe but higher-turnover reversal sleeve. The near-zero sleeve correlation (~−0.008) means the combined portfolio achieves substantially higher Sharpe than either sleeve alone (2.5 vs. 1.77 for reversal alone).

## Signal

### Reversal signal
- **Formation timestamp:** Hourly. Signal computed at each hourly bar close.
- **Lookback:** k = 4 bars (4 hours). The source tested k ∈ {2, 3, 4, 6, 8, 12}.
- **Entry:** Rank assets by trailing k-bar return. Fade extremes: go long the bottom decile (recent losers) and short the top decile (recent winners). Band positions at 2.5σ to cap exposure.
- **Exit:** Daily rebalance (every 24 bars). Positions reset at each rebalance.
- **Holding period:** 1 day (24 hours) between rebalances.
- **Residualization:** Returns are residualized vs. BTC over a rolling 168-bar (≈1 week) window, removing market-wide beta.
- **Parameters:** k = 4, band = 2.5σ, beta_win = 168, every = 24, vol_win = 24. All parameters are source-reported (grid-searched).

### Momentum signal
- **Formation timestamp:** Hourly.
- **Lookback:** k ≈ 336–500 bars (≈14–21 days). The source tested k ∈ {168, 336, 500, 720}.
- **Entry:** Rank assets by trailing k-bar return. Go long top decile, short bottom decile. Band positions at 2.0σ.
- **Exit:** Rebalance every 336–720 bars (≈14–30 days).
- **Holding period:** 14–30 days between rebalances.
- **Residualization:** Same as reversal (vs. BTC, 168-bar window).
- **Parameters:** k = 500, band = 2.0, every = 336. Source-reported.

### Mixed portfolio construction
- **Equal-volatility weighting:** Each sleeve is weighted inversely proportional to its realized volatility, ensuring equal risk contribution. This is updated periodically (research-proposed frequency: quarterly, not specified by source).
- **Rebalancing:** The source tests expanding-window and rolling-window walk-forward approaches. Both yield similar OOS results (Sharpe ~2.52).

### Signal fully specified?
The signal rules are fully specified for the individual sleeves. The equal-volatility rebalancing frequency is not explicitly stated by the source (underspecified). The banding threshold (2.0σ for momentum, 2.5σ for reversal) and the residualization window (168 bars) are specified.

## Required data

- **Instrument:** 12 liquid cryptocurrency perpetual futures or spot pairs on a major exchange (exact 12 pairs not named in README; likely BTC, ETH, and 10 mid-to-large-cap alts).
- **Venue:** Not specified; likely Binance or similar major CEX (standard crypto data availability).
- **Market type:** Spot or perpetual (the source does not specify; hourly bars are compatible with either).
- **Timeframe:** 1-hour bars.
- **Fields:** OHLCV (close price, volume). The source uses close-to-close returns and volume for normalization.
- **Residualization data:** BTCUSDT hourly close prices for the rolling 168-bar regression window.
- **Point-in-time:** Data must be available at hourly frequency with no look-ahead.
- **Timestamp:** UTC standard (crypto markets operate 24/7).
- **Missing-data:** The source does not discuss missing-data handling (data gap).

## Execution assumptions

- **Signal-to-order timing:** End-of-bar execution (research-proposed). Signal computed at bar close, positions rebalanced at next bar open.
- **Fill model:** Instantaneous fill at close price (research-proposed). No slippage model beyond the 7 bps cost assumption.
- **Fees:** 7 bps per rebalance (baseline). Cost resilience tested at 10 bps and 20 bps.
- **Slippage:** Not explicitly modeled beyond the 7 bps fee assumption (data gap).
- **Market impact:** Not modeled (data gap).
- **Leverage:** Not specified (data gap).
- **Capacity:** Not assessed (data gap). The source acknowledges that smaller altcoins may face practical liquidity constraints.
- **Partial fills / failures:** Not discussed (data gap).

## Evidence

### Source-reported

**Reversal sleeve (net of 7 bps):**
- Net Sharpe ≈ 1.77 (gross ≈ 2.07)
- Annualized return ≈ 36.6%, annualized volatility ≈ 20.7%
- Turnover ≈ 89/year, cost drag ≈ 6.2%
- Multiple nearby configs (Sharpe 1.66–1.73) confirm robustness

**Momentum sleeve (net of 7 bps):**
- Net Sharpe ≈ 1.32 (gross ≈ 1.34)
- Annualized return ≈ 29.1%, annualized volatility ≈ 22.2%
- Turnover ≈ 18/year, cost drag ≈ 1.3%
- Extremely low turnover in slow variants (k=168, every=720): turnover ≈ 3/year

**Mixed portfolio (Equal-Vol, walk-forward OOS):**
- Sharpe ≈ 2.52 (expanding window); 2.52 (rolling window)
- Annualized return ≈ 40.1%, annualized volatility ≈ 15.9%
- Annual alpha vs. BTC ≈ 42%, t-stat > 3.5
- Beta ≈ −0.02 (near-zero)
- R² < 1% (returns largely independent of BTC)

**Cost resilience (Equal-Vol OOS):**
- At 10 bps: Sharpe ≈ 2.4
- At 20 bps: Sharpe ≈ 2.1

**Sleeve correlation:** ≈ −0.008 (near-zero, confirming diversification benefit)

**Robustness (Train-Opt):** Train-optimized mixes delivered OOS Sharpe ≈ 2.0 with similar alpha, confirming robustness across portfolio construction methods.

Source-reported performance figures are from the repository README. The source does not specify whether these are gross or net of funding costs (data gap). The source does not provide detailed drawdown statistics, win rates, or regime-specific breakdowns in the README.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source itself acknowledges: "Sample length: Only ~2.6 years of hourly data — limited regime coverage."
- The source acknowledges: "Cost model: Simplified constant transaction cost assumption; real-world frictions (slippage, fees, market impact) may be larger and exchange-specific."
- The source acknowledges: "Parameter dependence: While robustness checks are strong, performance still depends on grid choices (lookbacks, banding, residualization)."
- The source acknowledges: "Benchmark choice: Residualization is done vs. BTC; alternative benchmarks may shift outcomes."
- The source acknowledges: "Execution feasibility: Turnover estimates assume perfect liquidity; smaller alts may face practical liquidity constraints."
- No negative evidence from the source regarding regime failure, though the 2.6-year sample limits regime coverage.
- Related falsification record: Arefev (2026) shows cross-sectional momentum alone fails at taker fees on Binance perpetuals. This mixed strategy uses momentum only as a diversifier (lower weight in the equal-vol mix) with very low turnover, which may explain why the combined strategy survives costs where pure momentum does not.

## Falsification plan

1. **Out-of-sample walk-forward test:** Extend the sample to 5+ years to cover bull, bear, and sideways regimes. The 2.6-year sample is insufficient for regime robustness. Failure metric: OOS Sharpe < 1.0 over a 2-year rolling window.

2. **Cost sensitivity stress test:** Test at realistic taker fees (10–20 bps per leg) including slippage and market impact. The 7 bps baseline is optimistic for altcoin execution. Failure metric: Equal-Vol Sharpe < 1.5 at 20 bps round-trip.

3. **Universe expansion / contraction:** Test with 20–30+ assets and with only the top 5 by volume. If the strategy is driven by a few illiquid alts, results will not replicate on a different universe. Failure metric: Sharpe degrades by >50% when moving to a different 12-asset universe.

4. **Benchmark sensitivity:** Residualize vs. ETH, vs. equal-weight basket, vs. no residualization. If the strategy is primarily BTC beta with a residualization artifact, results will change materially. Failure metric: Alpha vs. BTC drops below 10% annualized.

5. **Reversal vs. momentum ablation:** Remove one sleeve and test the other alone. If the strategy is entirely driven by reversal (the higher-Sharpe component), the momentum sleeve adds no value and the Equal-Vol construction is unnecessarily complex. Failure metric: Momentum-only Sharpe < 0.5 OOS.

6. **Parameter perturbation:** Test k ∈ {2, 3, 4, 6, 8} for reversal and k ∈ {168, 336, 500, 720} for momentum simultaneously. If the optimal region is a sharp peak rather than a plateau, the strategy is overfit. Failure metric: Median Sharpe across a 3×3 grid around the optimal drops below 1.5.

7. **Equal-volatility rebalancing frequency:** Test monthly vs. quarterly vs. no rebalancing of the sleeve weights. If performance is highly sensitive to this choice, the construction is fragile. Failure metric: Sharpe degrades by >30% when changing rebalancing frequency.

## Crypto portability

**Direct** — the source is natively implemented on crypto perpetual futures / spot pairs.

Crypto-specific considerations:
- **24/7 session structure:** The hourly bar frequency works well with crypto's continuous market. No session-boundary effects.
- **Funding rates:** The source does not model funding costs for perpetual positions. Funding is paid/received every 8 hours on perpetuals and can significantly erode returns for net-short or net-long positions. This is a material data gap.
- **Venue fragmentation:** The source uses a single-venue data assumption. Cross-venue execution would introduce additional latency and slippage.
- **Liquidity:** The source acknowledges that smaller altcoins may face practical liquidity constraints. The 12-asset universe may not be representative.
- **Mark / index price:** Not relevant for spot; relevant for perpetual margining.

## Limitations

- **Sample length:** Only ~2.6 years of hourly data — limited regime coverage (underspecified regime robustness).
- **Universe scope:** 12 assets; results may not generalize to broader or narrower universes.
- **Cost model:** Simplified constant 7 bps assumption; real-world frictions (slippage, market impact, funding) may be materially larger.
- **Funding costs not modeled:** Perpetual funding is a significant cost for directional positions; the source does not account for this (data gap).
- **Parameter dependence:** While robustness checks are strong, performance depends on grid choices.
- **Benchmark choice:** Residualization vs. BTC may not be the optimal benchmark.
- **Execution feasibility:** Turnover estimates assume perfect liquidity.
- **No regime-specific analysis:** The source does not break down performance by bull/bear/sideways regimes.
- **No drawdown / tail-risk statistics:** The source does not report max drawdown, Calmar ratio, or tail-risk metrics in the README.
- **Not independently reproduced.**

## Implementation status

No implementation in our research stack has been completed. This is a research-only capture from an external source.

## Adoption boundary

A record being present in this repository does **not** mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[quant/binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13]]` — falsification of cross-sectional momentum alone at taker fees; this mixed strategy's momentum sleeve may survive because it uses very low turnover and is paired with a diversifying reversal sleeve.
- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` — falsification of PCA-residual mean reversion; different mechanism (pairs-based vs. cross-sectional ranking).
- `[[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]]` — short-horizon mean reversion; different timeframe (15min vs. hourly) and signal construction (taker-flow vs. cross-sectional ranking).
- `[[quant/bitcoin-slow-momentum-speed-outperforms-fast-ts-momentum-2026-09-13]]` — time-series momentum speed; different mechanism (cross-sectional vs. time-series).

## Sources

1. ccollins80, "Crypto Statistical Arbitrage," GitHub repository, commit d7623cf203afe5d64f3c04a4ff88550798e552ed, https://github.com/ccollins80/crypto-stat-arb, accessed 2026-09-13.
2. Arefev (2026), "Binance Perpetual Cross-Sectional Momentum Multi-Year Panel Replication, Taker Fee Wall, and Phase Arbitrariness Falsification," SSRN 7404139, GitHub commit dd4399a7. (Related falsification context.)
