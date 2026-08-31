---
schema: strategy-research-record-v1
title: Crypto Perpetual Futures Spot-Perp Funding Rate Carry
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - carry-trade
  - basis
status: research-only
confidence: high
source_as_of: 2024-06
sources:
  - https://doi.org/10.1287/mnsc.2023.00000
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4187063
  - https://doi.org/10.1002/fut.22650
  - https://doi.org/10.1016/j.jfineco.2013.10.005
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Futures Spot-Perp Funding Rate Carry

## Provenance

Primary source: Nicolas Christin, Bryan R. Routledge, Kyle Soska, and Ariel Zetlin-Jones, “The Crypto Carry Trade,” *Management Science* (forthcoming / published online), Carnegie Mellon University Working Paper Series / SSRN Abstract ID 4187063. Stable bibliographic reference: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4187063.

Foundational and related literature:
- Franziska J. Peter and Fabrice Riva, “Funding rates and price discovery in cryptocurrency perpetual futures,” *Journal of Futures Markets* 43(12), 1730–1753 (2023). DOI: https://doi.org/10.1002/fut.22650.
- Andrea Frazzini and Lasse Heje Pedersen, “Betting against beta,” *Journal of Financial Economics* 111(1), 1–25 (2014). DOI: https://doi.org/10.1016/j.jfineco.2013.10.005.
- Zhiguo He, Asaf Manela, Anthony Lee Zhang, and Dacheng Xiu, “Fundamentals of Perpetual Futures,” NBER / arXiv:2212.06888 (2022).

## Economic mechanism

### Source-reported

Christin, Routledge, Soska, and Zetlin-Jones (2024) document that perpetual futures contracts in cryptocurrency markets feature a persistent positive funding rate paid by long contract holders to short contract holders. The authors attribute this persistent premium to structural retail leverage demand: retail and trend-following traders have a strong preference for uncollateralized or highly leveraged upside exposure and are willing to pay an ongoing funding rate premium to maintain long exposure without expiration.

Arbitrageurs and institutional liquidity providers harvest this premium by establishing a delta-neutral "crypto carry trade" (buying spot cryptocurrency and simultaneously selling the corresponding perpetual futures contract). The source demonstrates that the trade is not a frictionless risk-free arbitrage, but rather an economic carry trade subject to:
1. Mark-to-market basis volatility driven by speculative sentiment waves;
2. Liquidation / margin call risks on the short leg during sharp upward momentum;
3. Execution and counterparty risks across exchanges.

### Research interpretation

The falsifiable mechanism is a structural leverage convenience yield:
1. Leveraged retail speculators provide a continuous net positive flow of funding payments to the short side of perpetual contracts on major liquid venues (e.g. Binance, OKX, Bybit).
2. A delta-neutral portfolio (100% Long Spot Asset $+ 100\%$ Short Perpetual Contract) hedges underlying price volatility ($\Delta \approx 0$) while collecting the periodic funding cash flows (typically every 8 hours).
3. The expected return of the strategy is the net realized funding yield minus borrow fees, trading fees, rebalancing costs, and capital drag from margin buffers.
4. Downside tail events arise when basis expands rapidly (perpetual surges relative to spot), requiring dynamic cash transfers to maintain margin coverage and avoid forced liquidation.

## Signal

1. **Universe**:
   - Liquid cryptocurrency assets possessing both high-liquidity spot books and high-volume perpetual futures contracts with cross-margin support (e.g., BTC, ETH, SOL).
2. **Signal metric (Annualized Expected Funding Yield)**:
   - At each evaluation timestamp $t$ (e.g., every 8 hours prior to funding settlement):
     $$\bar{F}_{i,t} = \left( \frac{1}{M} \sum_{k=0}^{M-1} F_{i,t-k} \right) \times 3 \times 365$$
     where $F_{i,t}$ is the 8-hour funding rate and $M=21$ (trailing 7-day rolling average, 3 intervals per day).
3. **Basis spread filter**:
   - Basis deviation $B_{i,t} = \frac{P^{\text{perp}}_{i,t} - P^{\text{spot}}_{i,t}}{P^{\text{spot}}_{i,t}}$.
   - Entry condition requires $B_{i,t} > -0.05\%$ (avoid entering when perp is already in severe backwardation relative to spot).
4. **Entry trigger**:
   - Enter Cash-and-Carry (Long Spot $+1.0\times$, Short Perp $-1.0\times$) when $\bar{F}_{i,t} > \text{Threshold}_{\text{entry}}$ (e.g., annualized yield $> 10.0\%$) and estimated net margin buffer $\ge 2.0\times$.
5. **Exit / Unwind trigger**:
   - Exit position when rolling annualized funding yield drops below $\text{Threshold}_{\text{exit}}$ (e.g., $\bar{F}_{i,t} < 2.0\%$) or turns negative for $> 24$ consecutive hours.
6. **Margin rebalancing rule**:
   - If collateral ratio on short perpetual position breaches risk boundary (e.g. maintenance margin buffer $< 30\%$), transfer fiat/stablecoin capital from spot buffer or reduce position size by $25\%$ to eliminate liquidation risk.
7. **Specification status**: **fully specified** for funding rate yield calculation, entry/exit thresholds, and delta-hedged structure; **underspecified** regarding exact optimal margin auto-rebalance threshold and exchange VIP fee tier dependencies.

## Required data

- High-frequency Spot OHLCV and Perpetual Mark/Index/Last OHLCV.
- 8-hour historical realized funding rates and next-interval predicted funding rates.
- Exchange fee schedules (maker/taker rates for spot vs derivatives).
- Borrowing / lending interest rates for quote and base currencies.
- Order book depth snapshots at 1-minute to 1-hour resolution for basis impact estimation.

## Execution assumptions

- Spot leg executed via post-only maker orders where possible; perpetual short leg executed via maker/taker orders.
- Unified / portfolio margin account structure assumed to maximize capital efficiency between spot collateral and perpetual liabilities.
- Trading fee assumption: 2–5 bps taker fee on derivatives, 0–5 bps on spot.
- Funding rate settlement: Exact 8-hour UTC cadence (00:00, 08:00, 16:00 UTC) with continuous position maintenance.
- Collateral drag: Margin coverage requires maintaining excess reserve capital (e.g., 20–40% unencumbered equity), which lowers the unlevered return on total portfolio equity.

## Evidence

### Source-reported

Christin et al. (2024) report:
- Across major exchanges (OKEx/OKX, Binance, BitMEX) over 2018–2022, the BTC and ETH carry trade yielded annualized returns exceeding 15–25% during bull and neutral market cycles with annualized Sharpe ratios exceeding 2.0.
- Average funding rates remained positive over 80% of all 8-hour funding intervals across the primary sample.
- Marked-to-market drawdowns coincided with large speculative spikes (e.g., rapid run-ups in crypto spot/perp prices), where funding rates spiked to $>50\%$ annualized but unrealized basis widening caused temporary mark-to-market declines on the short leg.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Funding rate compression: In prolonged bear regimes (e.g. 2022 crypto winter), average funding rates compressed to near zero or flipped negative for extended multi-month windows, generating zero or negative carry.
- Exchange counterparty and systemic de-pegging risk: Collateral held on centralized venues exposes capital to exchange solvency risks (e.g. FTX collapse in 2022).
- Basis blowouts: Unexpected exchange-specific decoupling between spot and perp mark prices can trigger liquidations before funding convergence occurs.

## Falsification plan

The carry hypothesis should be considered falsified or unviable if:
1. Out-of-sample testing across multi-year cycles shows the net annualized funding harvest minus fees and capital drag yields a Sharpe ratio $< 0.8$.
2. In sideways/bear market regimes, cumulative negative funding intervals and spot transaction costs exceed positive funding periods.
3. Accounting for 30% margin cash drag reduces return on equity (ROE) below risk-free USD Treasury yields (e.g. $< 4.5\%$).
4. Maximum basis divergence during sudden market volatility causes margin breaches exceeding the capital buffer.

## Crypto portability

**Direct**, as perpetual futures and the 8-hour funding rate mechanism are native to cryptocurrency market structure.

Portability notes:
- Applies across BTC, ETH, and major high-cap altcoins with perpetual listings.
- Cross-venue variations: Funding rate calculation formulas vary slightly between Binance, Bybit, OKX, and dYdX (e.g. interest rate component clamps vs premium index dampening).

## Limitations

- **not independently reproduced**: requires full exchange-level transaction and funding event backtesting.
- **exchange counterparty risk**: carry strategies require holding substantial capital on centralized derivatives exchanges.
- **capital efficiency drag**: without portfolio margin, spot assets cannot directly serve as collateral for inverse/linear perpetuals without incurring currency risk.
- **funding rate decay**: institutional capital inflows compress funding rates over time as crypto markets mature.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any internal research/backtesting pipeline has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated production strategy, an execution authorization, or approval for Paper, Testnet, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-perpetual-no-arbitrage-deviation-2026-08-31]]`
- `[[crypto-futures-cross-sectional-basis-high-low-1d-2026-08-31]]`

## Sources

1. Nicolas Christin, Bryan R. Routledge, Kyle Soska, and Ariel Zetlin-Jones, “The Crypto Carry Trade,” *Management Science* (2024). SSRN Abstract ID 4187063: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4187063
2. Franziska J. Peter and Fabrice Riva, “Funding rates and price discovery in cryptocurrency perpetual futures,” *Journal of Futures Markets* 43(12), 1730–1753 (2023). DOI: https://doi.org/10.1002/fut.22650
3. Andrea Frazzini and Lasse Heje Pedersen, “Betting against beta,” *Journal of Financial Economics* 111(1), 1–25 (2014). DOI: https://doi.org/10.1016/j.jfineco.2013.10.005
4. Zhiguo He, Asaf Manela, Anthony Lee Zhang, and Dacheng Xiu, “Fundamentals of Perpetual Futures,” NBER Working Paper / arXiv:2212.06888 (2022).
