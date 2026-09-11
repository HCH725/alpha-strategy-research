---
schema: strategy-research-record-v1
title: "Crypto Funding-Rate Cross-Sectional Carry Factor: Net-of-Costs Evidence and Level-Harvest Artifact Decomposition"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - funding-rate
  - carry
  - cross-sectional
  - perpetual-futures
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "Bryan Vine, 'Crypto Carry: The Funding-Rate Cross-Section, Net of Costs and the Liquidation Tail', Alpha Research Paper 2, bryanvine.github.io/alpha-research/paper2.html (2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Funding-Rate Cross-Sectional Carry Factor: Net-of-Costs Evidence and Level-Harvest Artifact Decomposition

## Provenance

- **Source:** Bryan Vine, "Crypto Carry: The Funding-Rate Cross-Section, Net of Costs and the Liquidation Tail", Alpha Research Paper 2.
- **URL:** https://bryanvine.github.io/alpha-research/paper2.html
- **Source as-of date:** 2026 (exact publication date not stated on page; referenced paper in the series is Vine 2026).
- **Author:** Bryan Vine (Alpha Research).
- **No arXiv DOI or peer-review status stated.** This is an independent research blog/publication, not a peer-reviewed journal.

## Economic mechanism

### Source-reported

The paper separates two distinct crypto carry trades that the literature often conflates:

1. **Level harvest (cash-and-carry):** Hold long-spot / short-perp while funding is positive, collecting the funding stream. Source reports this as a "Sharpe artifact" — headline Sharpe of 8.5 is inflated by funding's near-zero volatility, while the honest net return is +5.6%/yr decaying to negative by 2026. The dominant risk (basis blowouts, forced liquidation, stablecoin de-pegs) is not captured by a funding-only model.

2. **Cross-sectional funding-carry factor:** Sort perps by trailing funding; go long low-funding / short high-funding (dollar-neutral). Source reports this as a genuine modest edge surviving out-of-sample net of costs: IS Sharpe 0.71, purged walk-forward OOS Sharpe 0.39.

### Research interpretation

The cross-sectional factor's economic mechanism is **relative-value dispersion combined with crowded-long mean-reversion**: coins where perpetual funding is abnormally high reflect crowded long positioning that tends to mean-revert, while coins with low/negative funding reflect neglected or short-crowded positions. By going dollar-neutral across the funding cross-section, the strategy harvests the funding spread (receives on low-funding shorts, pays on high-funding longs — net positive) while partially benefiting from crowded-long mean-reversion.

The paper explicitly tests whether extreme funding predicts forward returns (H5) and finds it does **not** significantly: rank-IC between trailing funding and forward 7-day return is −0.005 (t = −0.89). The edge is the funding spread itself, not a directional price forecast.

## Signal

- **Formation timestamp:** Trailing 7-day mean funding rate, shifted one day (applied to the next day's funding accrual and price return). No contemporaneous information enters the position.
- **Lookback:** 7-day trailing funding mean (parameterized as part of 36 configurations: lookback × quantile × rebalance).
- **Universe ranking:** Rank all 30 perps by trailing funding.
- **Long entry:** Bottom tercile (lowest funding) perps.
- **Short entry:** Top tercile (highest funding) perps.
- **Position sizing:** Dollar-neutral, gross exposure 1.0.
- **Rebalance:** Weekly (part of configuration grid).
- **Exit / holding:** Weekly rebalance; positions are reset each week.
- **PnL:** Daily price spread (Σ wᵢ rᵢ) plus funding harvested (−Σ wᵢ fᵢ), net of turnover cost.
- **Parameters:** 36 configurations tested (lookback × quantile × rebalance); all 36 positive (0.58–1.5 IS Sharpe range).
- **Underspecified items:** Exact lookback values, quantile definitions, and rebalance cadences within the 36 configurations are not enumerated in the paper (the grid is described but individual configurations are not listed). The paper acknowledges PBO of 0.81 — configurations are statistically indistinguishable.

## Required data

- **Universe:** 30 liquid Binance USD-M perpetual futures.
- **Venue:** Binance USD-M only (single venue).
- **Market type:** Perpetual futures (Binance USD-M).
- **Data fields:**
  - Funding rate events (112,853 observations, 2023-01 to 2026-05, zero gaps).
  - Daily spot prices (proxy for perp price leg; basis noted as small for liquid perps).
  - Funding settlement cadence: 8h for most coins, 4h for TIA (summed to daily grid).
- **Point-in-time:** Backfilled from Binance public data archive. Universe is today's liquid names — imperfect survivorship (delisted/zero-funding coins beyond MATIC not reconstructed).
- **Data hazard:** MATIC→POL rename (~2024-09) caused funding to become pinned to exchange default (constant, zero variance); flagged by degenerate-signal check and masked.

## Execution assumptions

- **Cost model:** 6 bp/side taker + slippage (swept 0–15 bp in sensitivity analysis).
- **Fill model:** Not specified beyond cost assumption.
- **Order type:** Assumed market orders.
- **Latency:** Not specified.
- **Funding mechanism:** Strategy earns/harvests funding as part of PnL (receives on short legs when funding negative, pays on long legs when funding positive).
- **Leverage / margin:** Not specified for the factor strategy; gross exposure stated as 1.0 (dollar-neutral, no explicit leverage).
- **Short selling:** Implicit — the strategy holds short perp positions. Borrow/availability not discussed (perpetual futures do not require borrows).
- **Capacity:** Limited in smaller perps (source notes this as a limitation).

## Evidence

### Source-reported

- **Cross-sectional funding-carry factor:**
  - IS Sharpe: 0.71 (net of 6 bp/side costs).
  - Purged walk-forward OOS Sharpe: 0.39 (clears +0.3 mean-reversion floor).
  - Gross IS Sharpe: 0.90.
  - All 36 configurations positive (0.58–1.5 range).
  - Robust to dropping any single coin (0.54–0.99 range).
  - Deflated Sharpe: 0.63 (best 0.96).
  - PBO: 0.81 — configurations statistically indistinguishable; honest expectation ~0.4 OOS, not the IS-best 1.5.
  - Max drawdown: −35%.
  - Year-by-year Net Sharpe: 2023: −0.57, 2024: 0.45, 2025: 1.17, 2026 (partial ~5 months): 4.26* (*too short to annualize).
  - Survived Oct-2025 cascade (+1.7% over window) due to dollar-neutral structure.

- **Level harvest (cash-and-carry):**
  - Headline Sharpe: 8.5 (artifact of funding's near-zero volatility).
  - Net annualized return: +5.6%/yr full-sample, decaying year-by-year to negative in 2026.
  - Source explicitly states this "no longer beats T-bills" (~5% risk-free rate).

- **Funding as price predictor (H5):**
  - Cross-sectional rank-IC between trailing funding and forward 7-day return: −0.005 (t = −0.89, n = 1,240 days).
  - Correctly signed but **not significant**.

- **Funding level decay (H2):**
  - Cross-sectional median annualized funding: +7.3% (2023) → +13.4% (2024) → +2.8% (2025) → +0.6% (2026).

All figures above are directly reported by Vine (Alpha Research Paper 2, bryanvine.github.io/alpha-research/paper2.html). This has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Level harvest is a Sharpe artifact with decaying net returns; source explicitly debunks it.
- Cross-sectional factor PBO of 0.81 means the specific configuration cannot be selected reliably — honest expectation is ~0.4 OOS Sharpe, not the IS-best 1.5.
- Max drawdown of −35% is substantial and means live sizing must be vol-targeted and small.
- Extreme funding does NOT significantly predict forward returns (H5 rejected).
- Single venue (Binance only); no point-in-time survivorship-free universe.

## Falsification plan

1. **Out-of-sample extension:** Extend the panel beyond May 2026 and verify the 0.39 OOS Sharpe persists or decays further.
2. **Multi-venue replication:** Replicate on Bybit, OKX, Hyperliquid funding data; if the factor is driven by Binance-specific microstructure, cross-venue evidence should weaken.
3. **Point-in-time universe:** Reconstruct a survivorship-free universe including delisted coins; if delisted coins had extreme funding before delisting, survivorship bias could inflate the factor.
4. **Cost sensitivity:** Sweep taker costs from 0–15 bp/side; at what cost level does the 0.39 OOS Sharpe drop below 0?
5. **Liquidation tail model:** Add Coinalyze open-interest/liquidation data to model the forced-liquidation tail that dominates the level trade's real risk; check whether similar tail risk affects the cross-sectional factor.
6. **Vol-targeted overlay:** Test whether a vol-targeted, defined-risk overlay improves the Sharpe-drawdown profile (source recommends this as future work).
7. **Regime decomposition:** Test whether the factor survives in different funding regimes (e.g., post-ETF compression vs. 2024 boom).

## Crypto portability

**Adapted.** The strategy is native to crypto perpetual futures and requires perpetual-specific funding rate data. It cannot be directly ported to spot, traditional futures (which have a fixed cost-of-carry), or options markets. Crypto-specific risks include:

- Funding rate manipulation on thin-venue perps.
- Exchange-specific funding mechanics (settlement cadence, clamp rules, cap/floor).
- Liquidation cascade risk on the short leg during squeezes (partially mitigated by dollar-neutral structure).
- 24/7 funding settlement vs. traditional market hours.

## Limitations

- **Single venue:** Binance USD-M only. Cross-venue generalization unknown.
- **Imperfect survivorship:** Universe is today's liquid names; delisted/zero-funding coins not reconstructed. Survivorship bias could inflate the factor if delisted coins had extreme funding before removal.
- **Spot-as-perp proxy:** Uses spot returns for the perp price leg. Cannot price basis convergence, funding-clamp dynamics, or forced-liquidation tail.
- **Not independently reproduced:** All results are source-reported.
- **PBO 0.81:** Configurations are statistically indistinguishable; the "best" configuration cannot be reliably selected.
- **Capacity:** Limited in smaller perps.
- **Tail risk:** −35% max drawdown; short-leg squeeze risk in crypto.
- **Decay trajectory uncertain:** Funding levels have been compressing post-ETF; if cross-sectional dispersion also compresses, the factor may decay.
- **No peer review:** Independent research blog, not a peer-reviewed publication.

## Implementation status

No implementation in our research stack. Research-only.

## Adoption boundary

This record is research material only. It does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- [[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]] — Prior record on crypto carry trade (Christin et al., SSRN 4187063), which studies the level harvest. This record captures a distinct source (Vine 2026) with a materially different finding: the level harvest is debunked as a Sharpe artifact, while a cross-sectional funding factor is identified as the surviving edge.
- [[crypto-funding-rate-mean-reversion-ema-taker-filter-walk-forward-2026-09-04]] — Related funding-rate mean-reversion work, but different signal construction (EMA + taker filter vs. cross-sectional funding tercile sorting).

## Sources

1. Bryan Vine, "Crypto Carry: The Funding-Rate Cross-Section, Net of Costs and the Liquidation Tail", Alpha Research Paper 2, bryanvine.github.io/alpha-research/paper2.html (2026).
