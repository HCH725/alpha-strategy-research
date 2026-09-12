---
schema: strategy-research-record-v1
title: "Funding-Adjusted Cross-Exchange Perpetual Price-Space Arbitrage via OU S-Score and Illiquidity Guards"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - cross-exchange
  - statistical-arbitrage
  - mean-reversion
  - ornstein-uhlenbeck
  - microstructure
status: research-only
confidence: medium
source_as_of: 2026-08-19
sources:
  - "https://github.com/yoho369/crypto-perpetual-arbitrage (commit c123906f09288c9d4686736f92bd9867e4957abd, 2026-08-19)"
  - "https://github.com/yoho369/crypto-perpetual-arbitrage/blob/main/arbitrage%20report.pdf"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Funding-Adjusted Cross-Exchange Perpetual Price-Space Arbitrage via OU S-Score and Illiquidity Guards

## Provenance

- **Repository:** yoho369/crypto-perpetual-arbitrage
- **Repository URL:** https://github.com/yoho369/crypto-perpetual-arbitrage
- **Full commit SHA:** `c123906f09288c9d4686736f92bd9867e4957abd` (main HEAD, 2026-08-19)
- **Authors:** Joe Ho, Edwin Chan
- **Report date:** June 1, 2026
- **Key files:** `src/data_pipeline.py`, `src/statistical_eng.py`, `src/backtest_eng.py`, `arbitrage report.pdf`
- **Data source:** Tardis.dev 1-minute derivative ticker data (funding rates, index prices, mark prices) and Level-1 BBO (Best Bid/Offer) snapshots
- **In-sample period:** March 1, 2025 – December 31, 2025 (10 months)
- **Out-of-sample period:** January 1, 2026 – February 28, 2026 (2 months)
- **Universe:** BTC, AVAX, BERA, KAITO perpetual futures
- **Venues:** Binance Futures, Bybit, OKX, Gate.io, Hyperliquid, KuCoin (BTC excludes KuCoin due to missing data)
- **Pair count:** 15 pairwise combinations per asset (6 choose 2), 10 for BTC (5 venues)

## Economic mechanism

### Source-reported

The authors investigate whether transient cross-exchange pricing dislocations in cryptocurrency perpetual futures represent a tradable arbitrage opportunity when the deterministic funding accrual effect is removed. The core insight is that raw price spreads between exchanges are contaminated by funding-rate mechanics: when the perpetual trades at a premium (positive funding), deterministic selling pressure from basis traders suppresses the price toward spot; when the perpetual trades at a discount (negative funding), deterministic buying pressure lifts it. Stripping this accrual effect reveals the "true" price-space dislocation.

The strategy exploits mean-reverting deviations in these funding-normalized cross-exchange spreads using an Ornstein-Uhlenbeck (OU) process. The OU framework generates standardized s-scores that identify high-conviction entry points, while bid-ask illiquidity guards filter out phantom liquidity events and toxic order flow.

### Research interpretation

The hypothesized mechanism is **structural cross-exchange price dislocation in perpetual futures** caused by fragmented liquidity, venue-specific order flow imbalances, and differential execution latency across exchanges. The funding-normalization step isolates the stochastic component from the deterministic funding drift, and the OU s-score captures deviations from the mean-reverting equilibrium.

The illiquidity guard mechanism is a microstructure insight: when bid-ask spreads widen abnormally (combined spread across both legs exceeds a threshold), it signals toxic order flow, information asymmetry, or phantom order books — conditions where the spread may not mean-revert. Filtering these events is critical for tail-risk protection, especially in lower-liquidity assets.

**Component roles:**
- **Regime:** Funding normalization removes deterministic funding accrual drift
- **Primary signal:** 1440-minute rolling AR(1) → OU s-score at |s| ≥ 4.0σ
- **Confirmation:** Cost-adjusted expected value gate (gross EV minus fees and 24h median liquidity toll > 0)
- **Microstructure filter:** Bid-ask illiquidity guard (combined spread threshold, asset-specific)
- **Exit:** Raw physical spread crossing 24h trailing moving average
- **Risk control:** 300-minute maximum holding period timeout

## Signal

### Formation timestamp
- **Data frequency:** 1-minute BBO and derivative ticker data, right-labeled (data arriving at T is timestamped to T+1 bucket)
- **Signal formation:** Continuous; s-score recalculated at each minute using rolling 1440-minute (24-hour) window
- **Tradable:** Immediately upon formation (next minute bucket), subject to illiquidity guard and EV gate

### Lookback
- **OU parameter estimation:** 1440-minute rolling AR(1) regression (OLS)
- **Reference mean for EV gate:** 24-hour trailing moving average of raw physical mid-spread
- **Illiquidity toll reference:** 24-hour rolling median of combined bid-ask spread

### Entry
- **Long spread signal:** s_{A,B,t} < −4.0σ (Exchange A at anomalous discount vs B → Long A, Short B)
- **Short spread signal:** s_{A,B,t} > +4.0σ (Exchange A at anomalous premium vs B → Short A, Long B)
- **Additional gate:** Net Expected Value = |x_exec,t − μ_raw,24h| − (C_trip + τ_liq) > 0
- **Execution:** Taker-taker (aggressive fill on both legs)
- **Illiquidity guard:** Combined bid-ask spread across both legs must be ≤ asset-specific threshold (5.0, 10.0, or 20.0 bps depending on asset)

### Exit
- **Primary:** Raw physical spread (unnormalized) crosses the 24h trailing moving average
- **Forced evacuation:** Funding epoch boundary approaching (position closed before settlement to avoid deterministic funding penalty)
- **Timeout:** 300 minutes maximum holding period

### Parameters
- All entry thresholds (4.0σ), illiquidity guard thresholds (5.0/10.0/20.0 bps), and timeout (300 min) are **research-proposed** values selected via in-sample Pareto optimization. Not source-derived from theoretical model.

## Required data

- **Instruments:** BTC, AVAX, BERA, KAITO perpetual futures
- **Venues:** Binance Futures, Bybit, OKX, Gate.io, Hyperliquid, KuCoin
- **Market type:** USDT-margined perpetual futures
- **Timeframe:** 1-minute BBO snapshots; 1-minute aggregated derivative ticker data
- **Fields:** Best Bid, Best Ask, funding rate (implied/predicted), index price, mark price, last traded price
- **Point-in-time:** Right-labeled 1-minute bucketing prevents intra-minute lookahead
- **Missing data:** Forward-fill with 3-minute staleness threshold; stale data triggers Critical Force-Close Override
- **Funding data:** Required for normalization (hourly yield derivation from exchange-specific epoch intervals)

## Execution assumptions

- **Order type:** Taker-taker (market orders on both legs)
- **Fill model:** Assumed executed at BBO (Best Bid/Offer) — no Level-2 depth modeling
- **Fees:** Top-tier VIP fee schedules per exchange (see Table 10 in report): Binance VIP 9 (1.70 bps taker), Bybit Pro 5 (3.20 bps taker), OKX VIP 9 (1.75 bps taker), KuCoin VIP 12 (2.50 bps taker), Gate VIP 16 (2.00 bps taker), Hyperliquid Diamond (1.44 bps taker). Maker fees assumed zero.
- **Slippage:** Conservative assumption: slippage modeled only through illiquidity guard, not explicitly in fill price
- **Round-trip cost:** 2 × (taker_A + taker_B) per trade
- **Impact:** Not modeled; illiquidity guard serves as proxy
- **Capital:** Each pair treated as independent execution instance with identical unconstrained capital base
- **Leverage:** 1x nominal (unlevered)
- **Margin:** Cross-exchange margin silos not modeled (each pair independently funded)
- **Capacity:** Not assessed; BBO-level fill assumes minimal lot sizes

## Evidence

### Source-reported

**In-sample (Mar–Dec 2025):**

| Asset | Trades | Win% | Cum PnL (bps) | Active Sharpe | G2P | Max Loss (bps) | MDD (bps) |
|-------|--------|------|---------------|---------------|-----|----------------|-----------|
| BTC (unconstrained, 4.0σ) | 117 | 44.4% | 432.66 | 5.08 | 2.53 | −19.55 | 57.92 |
| AVAX (unconstrained, 4.0σ) | 132 | 68.2% | 6,128.88 | 2.83 | 4.30 | −893.46 | 141.47 |
| BERA (unconstrained, 4.0σ) | 127 | 59.1% | 1,498.57 | 4.73 | 2.20 | −86.31 | 473.77 |
| KAITO (unconstrained, 4.0σ) | 307 | 53.1% | −1,896.78 | −3.32 | 0.64 | −444.61 | 1,896.78 |
| KAITO (guarded 5.0 bps, 4.0σ) | 161 | 62.1% | 166.55 | 2.89 | 1.72 | −60.15 | 201.27 |

With 10.0 bps illiquidity guard (Panel B in report):
- BTC: 117 trades, 44.4%, 415.58 bps, Sharpe 5.06
- AVAX: 118 trades, 66.9%, 1,375.57 bps, Sharpe 3.71 (truncated MDD from −893 to −38.95 bps)
- BERA: 71 trades, 57.8%, 690.56 bps, Sharpe 3.88

OOS (Jan–Feb 2026):

| Asset (Config) | Trades | Win% | Cum PnL (bps) | Active Sharpe | G2P | Max Loss (bps) |
|----------------|--------|------|---------------|---------------|-----|----------------|
| BTC (10 bps guard) | 12 | 58.3% | 18.90 | 7.34 | 2.82 | −5.14 |
| AVAX (20 bps guard) | 5 | 100.0% | 21.00 | 21.66 | N/A | +1.29 |
| BERA (10 bps guard) | 23 | 78.3% | 336.88 | 11.43 | 5.55 | −20.22 |
| KAITO (5 bps guard) | 3 | 33.3% | 36.03 | 7.39 | 4.05 | −7.06 |

All performance figures are source-reported (Table 4, 6, 8 in the report PDF). OOS period is only 2 months, so Sharpe ratios should not be extrapolated. Trade counts are very low (5–23 trades over 60 days).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Capacity constraint:** OOS trade counts are extremely low (5–23 trades over 60 days). The 4.0σ threshold and tight illiquidity guards severely limit signal frequency. Source acknowledges this as a critical limitation.
2. **KAITO unconstrained failure:** Without illiquidity guards, KAITO generates −1,896.78 bps with 1,896.78 bps MDD and G2P of 0.64, demonstrating that naive application to fragmented assets produces catastrophic tail losses.
3. **In-sample to OOS degradation:** BTC in-sample Active Sharpe of 5.06 drops to 7.34 OOS (due to low trade count, this is not directly comparable). Cumulative PnL drops from 432.66 bps (10 months) to 18.90 bps (2 months).
4. **Funding epoch exit problem:** 38–55% of BTC and AVAX trades exit at funding epoch boundaries rather than organic mean reversion (Table 5), suggesting the forced-evacuation mechanism truncates many trades before they can fully revert.
5. **Funding normalization overstatement risk:** The paper notes that normalizing prices does not guarantee the spread will converge — it only removes one source of deterministic drift. Residual venue-specific structural biases (index composition, clamping limits, interest rate differentials) persist in the normalized spread.
6. **None identified in the source as a separate negative-evidence section; the limitations section (Section 8) provides the caveats above.**

## Falsification plan

1. **Replicate with pre-registered OOS:** Extend the out-of-sample period to at least 6 months beyond the original Feb 2026 endpoint. **Research-defined falsification threshold:** Reject core carry hypothesis if BTC basket (institutional anchor pairs) has net APR ≤ 0 over the OOS horizon after realistic taker fees. (Research-proposed)
2. **Shifted-phase placebo test:** Compute s-scores at non-boundary phases (e.g., minute offsets 01/16/31/46 instead of 00/15/30/45) or with randomly shuffled timestamps. If performance is similar, the mean-reversion mechanism is not anchored to the 1440-minute rolling window. (Research-proposed)
3. **Ablation: funding normalization vs raw spread:** Run the naive Z-score on raw (unnormalized) spreads at the same 4.0σ threshold. The source's Table 6 already shows the naive Z-score underperforms significantly on BTC (−440.50 bps vs +432.66 bps), but this should be replicated independently. (Research-proposed)
4. **Ablation: illiquidity guard removal:** Remove the illiquidity guard entirely and measure tail-risk impact. The source shows KAITO performance collapses without guards, confirming the guard is load-bearing. (Research-proposed)
5. **Cross-venue capital constraint test:** Model a unified capital pool across venues with margin constraints. The current unconstrained-pair assumption is unlikely to hold in production. (Research-proposed)
6. **Level-2 depth replication:** Replace BBO fills with volume-weighted average price over top-25 levels to model realistic slippage at institutional scale. (Research-proposed)
7. **Parameter perturbation:** Sweep σ ∈ {2.0, 2.5, 3.0, 3.5, 4.0} × guard ∈ {5.0, 10.0, 20.0} bps and verify that the Pareto-optimal region is stable across sub-periods. (Research-proposed)

## Crypto portability

**direct**

The strategy is natively designed for cryptocurrency perpetual futures across multiple venues. No adaptation from traditional assets is required.

Crypto-specific considerations:
- **Funding rate mechanics:** Core to the strategy; funding normalization is the primary preprocessing step
- **24/7 markets:** Continuous trading supports the 1-minute signal frequency
- **Venue fragmentation:** 6 venues required; missing data on any venue reduces pair count
- **Liquidity asymmetry:** BTC pairs are in a low-volatility regime requiring extreme divergence (~4.8σ) for profitable entry; altcoin pairs (AVAX, BERA, KAITO) offer more frequent signals but higher tail risk
- **Cross-exchange margin silos:** Each venue requires separate capital; margin cannot be netted across exchanges
- **Exchange counterparty risk:** 6 venues with different operational risks (API reliability, withdrawal restrictions, insolvency risk)
- **Funding epoch alignment:** Exchanges use different settlement intervals (8h, 1h); position timing relative to settlement affects realized PnL

## Limitations

- **Backtest-only:** All results are in-sample and out-of-sample backtests; no paper, testnet, or live execution. (not independently reproduced)
- **Capacity unknown:** OOS trade counts (5–23 per asset over 60 days) suggest very low capacity at 1x unlevered. With leverage, capacity may scale, but liquidation cascade risk increases.
- **BBO fill assumption:** Assumes execution at best bid/offer with no slippage modeling. In production, consuming top-of-book depth would incur additional costs proportional to order size and venue liquidity.
- **Unconstrained capital:** Each pair independently funded; no shared capital pool, no Kelly sizing, no cross-pair correlation management.
- **VIP fee assumption:** Uses top-tier institutional fees (VIP 9, VIP 16, Diamond). Retail traders face substantially higher fees that would erode or eliminate the edge.
- **2-month OOS:** Insufficient sample for robust out-of-sample validation. The OOS Sharpe ratios (7–21) are likely overfitting artifacts of the short validation window.
- **Funding epoch exits:** 38–55% of trades are forced out at funding settlement before organic mean reversion, reducing alpha capture. The source acknowledges this and suggests testing a "hold-through" regime.
- **No slippage model:** The illiquidity guard partially addresses this but does not model volume-weighted execution costs.
- **Author-reported results:** All performance figures are from the source; independent replication is pending.

## Implementation status

not-implemented

No implementation in our research stack (PyBroker, Nautilus, Paper, Testnet, or Live) has been completed.

## Adoption boundary

This record is **research material only**. Presence in this repository does not imply:
- profitable strategy
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- `[[quant/cross-exchange-crypto-spatial-arbitrage-2026-08-31]]` — Makarov & Schoar (2020) cross-exchange spot arbitrage driven by fiat friction. Related: both study cross-exchange price dislocations. Distinct: this record focuses on **perpetual futures price-space** after funding normalization, not spot arbitrage via capital controls.
- `[[quant/crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]` — Cross-venue CEX-DEX funding-rate carry. Related: both study cross-exchange perpetual dynamics. Distinct: that record focuses on funding-rate spread carry (directional funding premium), while this record focuses on **price-space spread** mean-reversion after stripping funding accrual.
- `[[quant/cross-venue-funding-carry-patient-rebalance-vs-active-harvesting-2026-09-12]]` — Cross-venue funding rate carry analysis. Related: both study cross-venue perpetuals. Distinct: that record analyzes funding-rate differential harvesting; this record analyzes price-space spread convergence.
- `[[quant/crypto-quarter-hour-opening-order-imbalance-medium-horizon-2026-08-31]]` — Quarter-hour periodic trading effects. Unrelated mechanism but shares the theme of exploiting market microstructure patterns in crypto perpetuals.

## Sources

1. Joe Ho and Edwin Chan. "Arbitraging the Price Space: Funding-Adjusted Cross-Exchange Perpetual Arbitrage." Research report, June 1, 2026. Repository: https://github.com/yoho369/crypto-perpetual-arbitrage (commit `c123906f09288c9d4686736f92bd9867e4957abd`, 2026-08-19).
2. Report PDF: https://github.com/yoho369/crypto-perpetual-arbitrage/blob/main/arbitrage%20report.pdf
3. Marco Avellaneda and John Lee. "Statistical arbitrage in the US equities market." *Quantitative Finance* 10(7):761–782, 2010. (Foundational OU s-score framework referenced by the source.)
