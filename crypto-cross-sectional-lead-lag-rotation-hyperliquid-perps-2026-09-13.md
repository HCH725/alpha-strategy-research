---
schema: strategy-research-record-v1
title: "Cross-Sectional Lead-Lag Rotation on Hyperliquid Crypto Perpetuals"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetuals
  - lead-lag
  - cross-sectional
  - relative-value
  - hyperliquid
  - levy-area
status: research-only
confidence: medium
source_as_of: 2026-05-01
sources:
  - https://github.com/mateofrqt/Crypto-LeadLag-Strategy
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4599565
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Lead-Lag Rotation on Hyperliquid Crypto Perpetuals

## Provenance

- **Repository:** https://github.com/mateofrqt/Crypto-LeadLag-Strategy
- **Latest commit SHA:** `1cf5fd1` (May 1, 2026, "Update README with research references")
- **Repository created:** February 23, 2026
- **Author:** mateofrqt (quant/systematic trader, crypto perpetuals focus)
- **Academic foundation:** Bennett et al. (2023), "Detecting Lead-Lag Relationships in Stock Returns and Portfolio Strategies," SSRN 4599565, 63 pages, posted November 8, 2023, revised November 28, 2024.

### Deduplication audit

A comprehensive search across all `*.md` records in `alpha-strategy-research` confirmed no existing record matches the combination of: (a) Lévy-area based cross-sectional lead-lag detection, (b) applied to ~220 Hyperliquid perpetuals, (c) daily rebalancing cross-sectional L/S portfolio. The closest existing record is `crypto-cross-asset-seesaw-lead-lag-rotation-2026-08-31.md`, which covers the academic "seesaw effect" (Jia et al. 2023) — a different mechanism (negative cross-predictability between large and small caps on spot exchanges), different source, different universe, and different signal construction. These are independent captures.

## Economic mechanism

### Source-reported

The strategy exploits **cross-sectional lead-lag dynamics** in crypto perpetual futures. In traditional equity markets, large-cap assets tend to lead small-cap assets due to gradual information diffusion (Hou, 2007). Bennett et al. (2023) develop a method using **pairwise Lévy-area and cross-correlation of returns** to rank assets from leaders to followers, then construct portfolios that long or short followers based on leaders' previous returns.

The Crypto-LeadLag-Strategy repo adapts this framework to crypto perpetuals on Hyperliquid. The author states: "The strategies are grounded in academic research on lead-lag dynamics and rough path theory. The primary theoretical foundation is Bennett et al. (2023)." The cross-sectional lead-lag strategy ranks ~220 Hyperliquid perpetuals using a rolling lookback, identifies leader-follower relationships, and takes positions in follower assets weighted by signal strength.

### Research interpretation

The falsifiable alpha hypothesis is **cross-sectional information diffusion in crypto perpetual futures**: some assets (leaders) incorporate information faster than others (followers), creating a predictable return propagation pattern. A daily cross-sectional portfolio that systematically longs followers after positive leader returns and shorts followers after negative leader returns should earn a risk-adjusted premium if the lead-lag relationship is persistent and not fully arbitraged.

The mechanism is distinct from simple momentum or mean reversion:
- It is **cross-sectional** (relative to peers), not time-series
- It uses **Lévy-area based detection** (capturing nonlinear lead-lag, not just linear correlation)
- It operates on **perpetual futures** (with funding rate dynamics), not spot

## Signal

The signal construction is partially disclosed in the README; exact thresholds and parameters are withheld by the author to preserve live trading integrity.

### Disclosed elements

- **Formation timestamp:** Positions are rebalanced daily; the signal is computed at each daily cycle from a rolling lookback window.
- **Lookback:** Rolling lookback windows — no future leakage; parameters calibrated on in-sample, evaluated on untouched out-of-sample windows (walk-forward validation).
- **Universe:** ~220 Hyperliquid perpetuals, filtered on data availability each cycle. 123 distinct assets were traded in the backtest.
- **Entry:** Cross-sectional ranking extracted from the asset return matrix over the rolling lookback. Followers (assets whose returns are predicted by leaders' past returns) are longed or shorted based on leader returns. Position weights are driven by signal strength.
- **Exit:** Daily rebalancing; positions are reconstructed every cycle.
- **Position sizing:** Vol-targeting, rolling signal-reliability score, drawdown circuit breaker, intraday stop-loss.
- **Risk management:** Separate module exposing volatility targeting, rolling signal-reliability scoring, and a drawdown circuit breaker that can flatten all positions.

### Undisclosed elements (research-proposed)

- The exact Lévy-area computation window and cross-correlation lag
- The leader-follower ranking threshold or cutoff
- The precise position-weighting formula
- Signal-reliability score parameters
- Drawdown circuit breaker thresholds

**Signal is underspecified.** An independent researcher cannot fully reconstruct the signal from the disclosed information. The author intentionally withholds these details.

## Required data

- **Instrument:** ~220 Hyperliquid perpetual futures contracts (crypto perpetuals)
- **Venue:** Hyperliquid (decentralized perpetual exchange)
- **Market type:** Perpetual futures (USDC-margined)
- **Timeframe:** Daily bars (1D)
- **Fields:** OHLCV (open, high, low, close, volume) per asset, per day
- **Additional:** Cross-asset return matrix for lead-lag computation; data availability filtering per cycle
- **Point-in-time:** Walk-forward validation with rolling lookback; no future leakage claimed
- **Timestamp:** UTC (Hyperliquid operates 24/7)
- **Missing-data:** Filtered on data availability each cycle; assets with missing data are excluded

## Execution assumptions

- **Signal-to-order timing:** Daily rebalancing; signal computed at cycle close, positions adjusted at next cycle open
- **Order type:** Market/ALO (Adjusted Limit Order) routing via Hyperliquid REST API
- **Fill model:** Not explicitly stated; author mentions fees and spread modelled in backtest
- **Fees:** Exchange taker/maker fees modelled; total fees paid in backtest: $8,448 on $10,000 start capital over 14 months
- **Slippage:** Half-spread modelled; market-impact slippage modelled where relevant
- **Spread:** Modelled in backtest
- **Funding:** Not explicitly stated whether funding rate payments are included in backtest PnL. Since positions are in perpetual futures, funding is a material cost that may or may not be captured.
- **Leverage:** Not explicitly stated
- **Capacity:** 385 trading cycles over 14 months across 123 distinct assets; average ~3 trades per cycle. Capacity claims are not made.
- **Latency:** REST API execution; not HFT

## Evidence

### Source-reported

All figures below are from the repository README (mateofrqt/Crypto-LeadLag-Strategy, commit `1cf5fd1`, May 2026):

**Cross-Sectional Lead-Lag (Daily) — Backtest Feb 2025 → Apr 2026 (14 months, full walk-forward, fees & spread modelled):**

| Metric | Value |
|---|---|
| Total return ($10,000 start) | +172% ($10k → $27k) |
| Sharpe — 1-year window (annualised, daily) | 1.69 |
| Max drawdown | -41% |
| Cycle win rate | 49.6% (191/385 cycles) |
| Profit factor (cycle-level) | 1.26 |
| Total fees paid | $8,448 |
| Distinct assets traded | 123 |
| Trading cycles | 385 |

**Session-Filtered Directional (15m) — Backtest Jan 2026 → Mar 2026 (fees 0.09% round-trip):**

| Metric | Value |
|---|---|
| Trades | 58 |
| Win rate | ~50% |
| Profit factor | 1.89 |
| Total return | +9.40% |
| Sharpe (annualised) | 2.51 |
| Max drawdown | ~-3% |
| Bootstrap p-value (PF under H₀) | 3.49% |

**Pairwise Vol-Spread (1m) — Backtest IS/OOS (fees 0.09% round-trip):**

| Window | Trades | Return | Max DD |
|---|---|---|---|
| In-sample | 24 | +14.54% | -0.81% |
| Out-of-sample | 31 | +6.78% | -1.99% |

The author states the cross-sectional lead-lag strategy is **live-deployed** via Hyperliquid REST API with scheduled execution and market/ALO routing.

### Independently reproduced

Not independently reproduced. All results are self-reported by the repository author.

### Negative evidence

- The session-filtered directional strategy's out-of-sample window (9 trades) returned flat-to-negative, consistent with small sample size.
- Max drawdown of -41% on the daily strategy is substantial, suggesting significant tail risk.
- The repository warning states: "This repository is not actively updated. Source code, notebooks and results files may be several months old."
- The author withholds exact signal construction, making independent replication impossible.

## Falsification plan

1. **Replicate Lévy-area lead-lag detection on Hyperliquid perps:** Reconstruct the leader-follower ranking using pairwise Lévy-area and cross-correlation on the full ~220 Hyperliquid perpetual universe. If the ranking does not produce statistically significant cross-sectional return predictability, the mechanism is falsified.
   - *Data:* Hyperliquid historical OHLCV at daily frequency, Feb 2025 – Apr 2026
   - *Metric:* Cross-sectional Rank IC of follower returns predicted by leader returns
   - *Threshold:* Rank IC > 0.02 (t-stat > 2.0) after accounting for multiple testing
   - *Action:* If Rank IC is indistinguishable from zero, abandon the strategy

2. **Walk-forward out-of-sample test:** Apply the reconstructed signal on a held-out period (e.g., May–Sep 2026) without retuning. If the Sharpe ratio drops below 0.5 or the strategy loses money, the in-sample results are likely overfit.
   - *Threshold:* OOS Sharpe < 0.5
   - *Action:* If OOS Sharpe < 0.5, reject the strategy

3. **Funding rate sensitivity:** Determine whether the backtest includes funding rate payments. If not, recalculate net PnL with actual historical funding rates. Since perpetual futures funding can be 5–30% annualized, this could substantially erode or eliminate the Sharpe.
   - *Threshold:* If including funding reduces Sharpe below 1.0, flag as cost-sensitive
   - *Action:* If funding erases alpha, reject the strategy

4. **Bootstrap significance of profit factor:** The session-filtered strategy reports bootstrap p-value of 3.49% for the profit factor. Verify this with 10,000+ bootstrap resamples on the daily strategy's cycle-level PnL. If the bootstrap p-value exceeds 5%, the result is not statistically significant.
   - *Threshold:* Bootstrap p-value > 0.05
   - *Action:* If not significant, reject the strategy

5. **Drawdown stress test:** The -41% max drawdown on a $10,000 account is severe. Test whether a vol-targeting or position-sizing overlay can reduce max DD below 20% without destroying the Sharpe. If not, the strategy may be untradeable in practice.
   - *Threshold:* Max DD > 30% after vol-targeting
   - *Action:* If max DD remains > 30%, flag as untradeable at retail scale

## Crypto portability

**direct** — the strategy is native to crypto perpetual futures on Hyperliquid.

Crypto-specific considerations:
- **Funding rate dynamics:** Perpetual futures funding payments are a material cost/benefit that may not be captured in the backtest. If the strategy is long followers and short leaders, funding payments depend on the relative funding rates of the positions.
- **Venue fragmentation:** The strategy operates on Hyperliquid only; cross-exchange lead-lag dynamics may differ.
- **24/7 trading:** Daily rebalancing on a 24/7 market means the "daily" bar definition matters (e.g., UTC midnight vs. exchange-specific candle boundaries).
- **Liquidity:** Hyperliquid perps vary widely in liquidity; the 123 assets traded may include illiquid names where slippage is material.
- **Smart contract risk:** Hyperliquid is a decentralized exchange; protocol-level risks (smart contract bugs, oracle failures, liquidation cascades) are not captured in the backtest.

## Limitations

- **Signal underspecification:** The exact signal construction (Lévy-area window, cross-correlation lag, ranking threshold, position-weighting formula) is withheld by the author. Independent replication is impossible without these details.
- **Not independently reproduced:** All results are self-reported.
- **Short backtest period:** 14 months (Feb 2025 – Apr 2026) is a single market regime; the strategy has not been tested across bull, bear, and range-bound markets.
- **Funding rate treatment unclear:** Whether the backtest includes funding rate payments on perpetual futures positions is not explicitly stated. This is a material omission for a perpetual futures strategy.
- **Repository not actively updated:** The author warns the repo may be outdated; source code and results files may not reflect current state.
- **Survivorship bias risk:** The ~220 Hyperliquid perps universe may include survivorship bias if delisted contracts are excluded from historical data.
- **-41% max drawdown:** Substantial drawdown suggests significant tail risk; the strategy may be untradeable at scale without aggressive risk management.
- **Win rate below 50%:** The 49.6% cycle win rate means the strategy relies on larger wins than losses (profit factor 1.26) — a pattern that can be fragile under regime changes.

## Implementation status

No implementation in our research stack. The strategy is described as live-deployed by the repository author on Hyperliquid via REST API, but we have not verified this claim.

## Adoption boundary

This record represents research material only. The strategy's presence in this repository does not constitute evidence of profitability, validated alpha, or authorization for deployment in paper trading, testnet, or live trading systems.

## Related Wiki records

- `crypto-cross-asset-seesaw-lead-lag-rotation-2026-08-31.md` — Academic "seesaw effect" (Jia et al. 2023): negative cross-predictability between large and small-cap crypto on spot exchanges. Different mechanism (negative lead-lag), different source, different universe.
- `crypto-cross-sectional-price-delay-information-diffusion-2026-08-31.md` — Price delay and information diffusion across crypto tokens. Related concept (information propagation) but different signal construction.
- `path-portfolio-optimization-signature-defect-lift-2026-09-02.md` — Path signature decomposition including Lévy-area components for portfolio optimization. Theoretical foundation related to the Lévy-area detection method used here.

## Sources

1. mateofrqt, "Systematic Trading — Research & Live Strategies," GitHub repository https://github.com/mateofrqt/Crypto-LeadLag-Strategy, commit `1cf5fd1` (May 1, 2026).
2. Bennett, M., et al. (2023). "Detecting Lead-Lag Relationships in Stock Returns and Portfolio Strategies." SSRN working paper, SSRN 4599565, 63 pages. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4599565
3. Hou, K. (2007). "Industry Information Diffusion and the Lead-Lag Effect in Stock Returns." *The Review of Financial Studies* 20(4), 1113–1138. DOI: https://doi.org/10.1093/rfs/hhl035
