---
schema: strategy-research-record-v1
title: "Two-Tiered CEX-Dominant Funding Rate Price Discovery and Structural CEX-DEX Arbitrage Boundary"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - microstructure
  - market-structure
  - cross-venue
status: research-only
confidence: medium
source_as_of: 2026-01-20
sources:
  - "https://doi.org/10.3390/math14020346"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Two-Tiered CEX-Dominant Funding Rate Price Discovery and Structural CEX-DEX Arbitrage Boundary

## Provenance

- **Author:** Petar Zhivkov (Institute of Information and Communication Technologies, Bulgarian Academy of Sciences; "Angel Kanchev" University of Ruse; Centre of Excellence in Informatics and ICT, Bulgarian Academy of Sciences)
- **Paper:** "The Two-Tiered Structure of Cryptocurrency Funding Rate Markets"
- **Journal:** Mathematics, Vol. 14, Issue 2, Article 346
- **Published:** 20 January 2026
- **DOI:** https://doi.org/10.3390/math14020346
- **Full text:** https://www.mdpi.com/2227-7390/14/2/346
- **Sample period:** 8–15 November 2025 (8 consecutive days)
- **Universe:** 35.7 million one-minute funding rate observations across 26 cryptocurrency exchanges (11 centralized, 15 decentralized) spanning 749 symbols
- **Primary source checksum:** All figures below are verified from the published MDPI full text (Zhivkov 2026, Mathematics 14(2):346). The paper was submitted 1 December 2025, revised 11 January 2026, accepted 12 January 2026, published 20 January 2026.

## Economic mechanism

### Source-reported

The paper documents a two-tiered market structure in cryptocurrency perpetual futures funding rates. Centralized exchanges (CEX: Binance, OKX, Bybit, KuCoin, MEXC, Gate.io, Bitget, BingX, Phemex, Crypto.com, HTX) dominate funding rate price discovery, while decentralized exchanges (DEX: Hyperliquid, Drift, Paradex, Kuma, Vest, Bluefin, Pacifica, Lighter, Extended, EdgeX, Hibachi, Ethereal, Variational, Aster, WooFi) operate as price takers. The mechanism has three structural pillars:

1. **Liquidity depth:** CEX platforms account for approximately 75–80% of total perpetual futures trading volume across major cryptocurrencies during the sample period. Large traders and institutional arbitrageurs preferentially operate on CEX platforms where they can execute sizable positions without material price impact.
2. **Execution speed:** CEX platforms process transactions via centralized matching engines with microsecond-level latency; DEX platforms require blockchain transaction confirmation (even on fast chains: sub-second to few-second settlement), orders of magnitude slower than CEX.
3. **Cross-platform arbitrage infrastructure:** Sophisticated arbitrageurs monitoring funding rate differentials maintain primary operations on CEX platforms. When CEX funding rates change, arbitrageur execution propagates information from CEX to DEX. The reverse flow is limited because few arbitrageurs monitor DEX-originated information signals.

### Research interpretation

The hypothesized mechanism is **asymmetric information flow in fragmented perpetual futures markets**: CEX venues, by virtue of deeper liquidity, faster execution, and concentrated arbitrageur infrastructure, lead funding rate price discovery. DEX venues respond to CEX innovations rather than independently driving them. The implication for alpha construction is that a directional signal derived from CEX funding rate dynamics may predict subsequent DEX funding rate movements — a lead-lag effect at the venue-tier level. This is structurally analogous to the equity consolidated-tape / SIP lead-lag literature but operating across venue types rather than within a single market.

## Signal

The paper does not propose a single executable trading rule. The core finding is an empirical market-structure observation (CEX leads DEX with zero reverse causality) that could be operationalized as follows:

### Source-reported structure

1. **Measurement:** Compute the bivariate VAR of CEX funding rate (e.g., Binance) and DEX funding rate (e.g., Hyperliquid) for the same underlying symbol.
2. **Granger causality test:** If past CEX funding rates help predict current DEX funding rates beyond DEX's own history (F-test, AIC-selected lag 1–3), the CEX→DEX channel is active.
3. **Directional asymmetry:** Among 14 CEX-DEX exchange pairs tested across the top 10 cryptocurrencies, all 14 significant relationships show CEX→DEX causality; zero show DEX→CEX causality (92 bidirectional tests, 57 significant at p<0.05).

### Research-proposed operationalization (NOT source-reported)

A scout-generated strategy sketch based on the source's structural finding:

1. **Signal formation:** At each funding rate observation timestamp, compute the difference between the leading CEX funding rate (e.g., Binance 8h-equivalent) and the lagging DEX funding rate (e.g., Hyperliquid 8h-equivalent) for a given symbol.
2. **Entry:** When the CEX-DEX spread exceeds a threshold (research-defined, not source-specified), enter a delta-neutral position: long the perpetual on the lower-rate venue and short on the higher-rate venue.
3. **Exit:** Close when the spread reverts (spread < 0 bps) or when a time-based stop is hit.
4. **Position sizing:** Equal-notional on both legs (research-proposed).
5. **Parameters:** All thresholds, holding periods, and sizing rules are research-proposed, not source-specified. The source does not backtest this specific strategy.

## Required data

- **Instrument:** Perpetual futures for cryptocurrency assets traded on both CEX and DEX venues
- **Venue:** Minimum one CEX (e.g., Binance, OKX) and one DEX (e.g., Hyperliquid) for the same underlying
- **Market type:** Perpetual futures (USDT-margined and coin-margined)
- **Timeframe:** One-minute funding rate observations (or the exchange's native funding interval: 1h, 4h, or 8h); normalized to 8-hour equivalents
- **Fields:** Funding rate (bps), funding rate interval (1h/4h/8h), open interest rank (liquidity proxy), timestamp with millisecond precision
- **Point-in-time:** Funding rates are published at fixed intervals; no look-ahead issues for the normalized 8h-equivalent rate at each observation timestamp
- **Missing-data:** Forward-fill for gaps ≤5 min; structural NA for symbols not offered on an exchange; outlier filter at ±5000 bps (0.0001% of observations removed)
- **Funding/fee/spread:** Taker fees 0.01–0.05% across exchanges; slippage conservatively 0.1% (liquid, OI rank <50) to 0.5% (illiquid); DEX gas costs negligible (<$0.01 on Solana/Arbitrum/Optimism)

## Execution assumptions

- **Signal-to-order timing:** At the moment of each funding rate observation (1-min granularity), the CEX rate is observed and the DEX rate is expected to adjust with a lag. Source-reported: the Granger causality analysis uses AIC-selected lags of 1–3 minutes.
- **Fill model:** Source does not specify. The delta-neutral portfolio simulation assumes simultaneous long/short across two venues at the observed funding rate differential.
- **Fees:** Source charges entry/exit taker fees at 0.05% per side (conservative estimate for retail tier) plus slippage. Round-trip costs: $60 for liquid markets, $220 for illiquid markets per $10,000 notional per side.
- **Spread:** Not explicitly modeled as a separate cost component; included in slippage estimates.
- **Slippage:** 0.1% for liquid pairs (OI rank <50), 0.5% for illiquid pairs (OI rank ≥50).
- **Funding:** Accrues continuously based on the instantaneous funding rate differential. 8h rate divided by 480 min for per-minute accrual.
- **Leverage/margin:** Source does not specify leverage. Each leg requires $10,000 notional.
- **Latency:** Source does not model execution latency between venues. Cross-venue latency is a material risk not quantified.
- **Partial fills/failures:** Not modeled. Cross-venue simultaneous execution is assumed feasible.

## Evidence

### Source-reported

All figures below trace to Zhivkov (2026), Mathematics 14(2):346, verified from the published MDPI full text:

**Granger causality / Information flow (Section 4.5, Table 6):**
- Among 14 CEX-DEX exchange pairs tested across top 10 cryptocurrencies: all 14 significant relationships show CEX→DEX causality; zero show DEX→CEX causality.
- BINANCE Granger-causes HYPERLIQUID for 7 of 9 tested symbols, F-statistics ranging from 4.23 to 127.83 (all p<0.05).
- 92 bidirectional tests performed; 57 exhibit statistically significant causality (62%).
- Robustness: directional asymmetry consistent at 1-min, 5-min, and 15-min sampling frequencies (Table 7).

**Market integration (Section 4.6, Table 8):**
- CEX-CEX average correlation: 0.246 (median 0.203), 576 pairs
- DEX-DEX average correlation: 0.153 (median 0.124), 477 pairs
- CEX-DEX average correlation: 0.175 (median 0.131), 1,141 pairs
- CEX integration 61% higher than DEX: (0.246−0.153)/0.153 = 0.608
- Statistical significance: CEX-CEX vs. DEX-DEX (t=5.77, p<0.001); CEX-CEX vs. CEX-DEX (t=5.39, p<0.001)

**Arbitrage opportunities (Section 4.3, Table 3):**
- 665,251 observations (17% of sample) exceed the 20 bps spread threshold (mean 51.6 bps, max 2401 bps)
- 84% of significant spreads involve CEX-DEX pairings (average 52.4 bps, persisting 91% of observation time)
- 16% involve CEX-CEX pairs (47.2 bps, 92% duration)
- Essentially no DEX-DEX opportunities (30.3 bps, 62% duration)

**Delta-neutral portfolio performance (Section 4.7, Table 9):**
- Top 20 arbitrage opportunities simulated with $10,000 per side
- 8 of 20 portfolios generate positive net returns; 12 incur losses
- Average net P&L across all 20: $22
- Best performer (AIA): $1,433 profit over 2 days
- Average Sharpe ratio: −7.40; best (AIA): −2.73
- 95% of portfolios (19/20) exhibit spread reversal patterns; forced exits for 12 of 20

**Spread persistence (Section 4.4, Table 4–5):**
- First-order autocorrelations: 0.966–0.998 across all symbols
- ETH: rapid mean reversion, half-life ~20 min (AR(1) coefficient 0.966, R²=0.93)
- Other symbols: minimal mean reversion (AR(1) >0.96, half-lives exceeding hours or days)
- GARCH(1,1) for BTC, ETH, SOL: near-IGARCH with α+β≈1.0

### Independently reproduced

Not independently reproduced.

### Negative evidence

- 95% of top-20 simulated delta-neutral portfolios exhibited spread reversals where exchanges swapped funding rate positions, forcing exits.
- Only 40% of top opportunities generated positive returns after transaction costs and spread reversals.
- Average Sharpe ratio across all 20 simulated portfolios was −7.40.
- The paper explicitly challenges the "free money" narrative around funding rate arbitrage, finding that visible mispricings reflect equilibrium outcomes consistent with binding frictions (transaction costs and limited duration before reversals) rather than exploitable inefficiencies.
- The 8-day sample window is explicitly acknowledged as insufficient to distinguish true IGARCH from near-integrated processes; the persistence findings should be interpreted cautiously.

## Falsification plan

1. **CEX→DEX lead-lag replication:** Reconstruct the bivariate VAR for Binance-Hyperliquid BTC/ETH/SOL funding rates using point-in-time data. Verify that CEX Granger-causes DEX at 1-min, 5-min, and 15-min frequencies. **research-defined falsification threshold:** If fewer than 8 of 10 major symbols show significant CEX→DEX causality (p<0.05) at the 5-min frequency, the two-tiered structure claim is materially weakened for the current market regime.
2. **Reversal frequency audit:** Extend the sample beyond 8 days to verify that 95% forced-exit rate is stable. **research-defined falsification threshold:** If the forced-exit rate drops below 60% over a 30-day sample, the spread-reversal risk is regime-dependent rather than structural.
3. **DEX evolution check:** Re-run the analysis quarterly. If DEX→CEX causality emerges for any symbol, the two-tiered structure is breaking down — likely as DEX liquidity deepens. **research-defined falsification threshold:** Any statistically significant DEX→CEX Granger causality for 3+ symbols in a quarterly re-test.
4. **Cost sensitivity:** Re-run the delta-neutral portfolio simulation with maker fees (0.02%) instead of taker fees (0.05%). **research-defined falsification threshold:** If fewer than 12 of 20 portfolios are profitable under maker execution, the strategy is not cost-robust.
5. **Spread-duration interaction:** Test whether profitable opportunities cluster in specific spread-duration regions. **research-defined falsification threshold:** If no region of (average spread, duration) space produces positive average net P&L across bootstrap resamples, the edge is not robust.

## Crypto portability

**Direct.** The paper studies cryptocurrency perpetual futures natively across 26 crypto exchanges (11 CEX, 15 DEX). The two-tiered structure finding is specific to the crypto perpetual futures market architecture.

Crypto-specific considerations:
- The 8-hour funding rate settlement schedule creates periodic anchoring events that structure the lead-lag dynamics. Different funding intervals (1h, 4h) may alter the lag structure.
- DEX platforms operate on fast chains (Solana, Arbitrum, Optimism) with sub-second to few-second settlement. If DEX settlement speeds improve materially, the CEX lead may shrink.
- The DEX-to-CEX perpetuals ratio grew from 3.7% to 11.7% during 2025. Continued DEX growth may erode the two-tiered structure over time.
- Cross-venue margin netting is not possible; each leg requires independent capital.
- Venue-specific risks: oracle manipulation, smart contract risk, withdrawal delays, and regulatory fragmentation differ across CEX and DEX platforms.

## Limitations

- **Sample window:** 8 days (8–15 November 2025) is explicitly acknowledged as short. IGARCH findings may reflect sampling structure rather than true unit-root processes. The two-tiered structure may be regime-dependent.
- **Sample period context:** November 2025 falls within a crypto expansion phase. The CEX→DEX causality pattern may weaken during bear markets or periods of DEX liquidity contraction.
- **Instrument coverage:** The paper focuses on perpetual futures funding rates, not spot price discovery. The two-tiered structure may not extend to spot markets.
- **DEX selection:** The 15 DEX platforms include newer/less liquid venues (Kuma, Vest, Hibachi, Ethereal, Variational) alongside major ones (Hyperliquid, Drift). The aggregation across heterogeneous DEX platforms may overstate DEX fragmentation.
- **Transaction cost model:** Conservative but simplified — does not model queue-position dynamics, partial fills, cross-venue withdrawal latency, or gas fee volatility during network congestion.
- **No independent reproduction:** The findings have not been independently reproduced or verified by a second research group.
- **Survivorship/selection:** The 749 symbols include all symbols with ≥2 exchange coverage. No survivorship-bias adjustment is discussed, though the short sample window limits this concern.
- **Publication venue:** Mathematics (MDPI) is an open-access journal; the paper's novelty depends on how the literature evolves, as the authors themselves note.

## Implementation status

Not implemented. No backtest, paper, testnet, or live execution in our research stack.

## Adoption boundary

Research capture only. Presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

The source's own delta-neutral simulations show that most top opportunities are unprofitable under conservative exit protocols after transaction costs.

## Related Wiki records

- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]` — Pindza (2026), CEX-DEX funding-rate carry as a basis trade. Related: both study cross-venue funding dynamics. Distinct: Pindza focuses on the carry trade risk decomposition and portfolio construction; Zhivkov focuses on the two-tiered market structure and information flow directionality (CEX→DEX with zero reverse causality). The two-tiered finding is a structural precondition that informs where carry opportunities arise (at the CEX-DEX boundary).
- `[[hyperliquid-cex-cross-venue-funding-spread-carry-2026-09-03]]` — Cross-venue funding carry between Hyperliquid and CEX. Related: both study CEX-DEX funding differentials. Distinct: that record focuses on the carry trade premium and its risk decomposition; this record documents the structural CEX→DEX information flow that creates the persistent spread.
- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]` — Cross-sectional funding rate carry factor. Distinct: cross-sectional rather than cross-venue.
- `[[crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11]]` — Funding rate mean reversion signal. Distinct: single-venue mean reversion rather than cross-venue information flow.

## Sources

1. Zhivkov, P. (2026). "The Two-Tiered Structure of Cryptocurrency Funding Rate Markets." *Mathematics*, 14(2), 346. DOI: https://doi.org/10.3390/math14020346. Published 20 January 2026. Open access (CC BY 4.0).
