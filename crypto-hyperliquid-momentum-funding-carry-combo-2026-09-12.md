---
schema: strategy-research-record-v1
title: Hyperliquid Momentum-Funding Carry Combo
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum
  - funding
  - carry
  - perpetual-futures
  - cross-sectional
  - hyperliquid
status: research-only
confidence: medium
source_as_of: 2026-07-05
sources:
  - "Keel Research, 'Momentum + Funding Strategy on Hyperliquid', https://usekeel.io/strategies/momentum-funding-hyperliquid, data as of 2026-07-05"
  - "Keel Research, 'How we backtest every strategy — Methodology', https://usekeel.io/strategies/methodology"
  - "Keel Trade, open-source strategy development platform, https://github.com/keel-trade/keel-trade (MIT license)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hyperliquid Momentum-Funding Carry Combo

## Provenance

- **Primary source:** Keel Research, "Momentum + Funding Strategy on Hyperliquid", published on usekeel.io with real Hyperliquid market data. Data as of 2026-07-05.
- **Strategy URL:** https://usekeel.io/strategies/momentum-funding-hyperliquid
- **Methodology URL:** https://usekeel.io/strategies/methodology
- **Open-source code:** https://github.com/keel-trade/keel-trade (MIT license). The strategy is defined as a composable pipeline; the same compiled artifact runs in backtest and on Hyperliquid live.
- **Backtest window:** 2024-08-15 to 2026-07-05 (approximately 23 months, spanning both strong uptrends and deep drawdowns).
- **Universe:** Top-30 Hyperliquid perpetuals by 24h volume, resolved at each rebalance. The 30 assets at the default snapshot include: ADA, AVAX, BNB, BTC, DOGE, DYDX, ENA, ETH, FARTCOIN, GRAM, HYPE, LINK, LIT, NEAR, ONDO, PAXG, PUMP, SOL, SUI, TAO, TRUMP, UNI, VVV, WLD, XLM, XPL, XRP, ZEC, kBONK, kPEPE.
- **Public-use status:** Strategy definition and backtest results are publicly visible on usekeel.io without login. Code is MIT-licensed on GitHub.
- **Deduplication audit:** Repository-wide search confirms zero matching records for `Keel`, `usekeel`, `momentum_funding_hyperliquid`, `momentum-carry-combo`, or the specific strategy definition. Existing records cover funding carry (`crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31.md`, cross-exchange CEX-DEX carry), cross-sectional funding carry (`crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-09.md`), and standalone momentum strategies, but none combine cross-sectional momentum with funding carry on a single venue in a blended signal.

## Economic mechanism

### Source-reported

The strategy combines two independent cross-sectional signals: (1) **price momentum** (trending coins tend to continue), and (2) **funding rate carry** (crowded long positions with high positive funding are expensive to hold and prone to squeeze; crowded short positions with negative funding pay you to hold). By blending these two signals, the strategy aims to capture trend persistence while avoiding overcrowded positions and collecting funding income from the short side. The source states that "momentum captures trends that tend to persist, while the funding tilt steers the book away from crowded longs that are costly to hold and toward shorts that are paid to hold."

### Research interpretation

This is a **cross-sectional momentum-carry hybrid** applied to crypto perpetuals. The economic thesis rests on two well-documented anomalies:

1. **Cross-sectional momentum in crypto:** Altcoin returns exhibit short-term continuation at the weekly/2-week horizon, as documented in Liu, Tsyvinski & Wu (2022) and other crypto factor studies. Coins that outperform recently tend to continue outperforming over the next 1-4 weeks.

2. **Funding rate carry as a crowding fee:** Perpetual funding rates reflect leveraged positioning imbalance. When longs are crowded, they pay shorts a periodic fee; when shorts are crowded, the reverse. The carry signal extracts income from the funding mechanism while simultaneously avoiding expensive crowded positions.

The **blend** (70% momentum, 30% carry) creates a composite signal where momentum dominates but the funding tilt acts as a risk filter: it underweights high-funding (crowded long) names on the long side and overweight negative-funding (crowded short) names on the short side. This is mechanically similar to a value-tilted momentum strategy in equities, but the "value" dimension is the funding rate rather than a fundamental multiple.

The balanced long/short structure (1x gross) makes the strategy market-neutral in principle — it should not depend on the overall market direction, only on cross-sectional dispersion.

## Signal

### Formation timestamp

Daily, at 00:00 UTC (the `bar_offset` of 12h from the target timeframe of 1d places the signal formation at 12h offset). The strategy uses 15-minute input bars resampled to the daily target timeframe.

### Lookback

- **Momentum component:** 14-day Rate of Change (ROC), cross-sectionally z-scored across the top-30 universe.
- **Funding component:** Realized funding rate over the most recent period (loaded via `FundingDataLoader` with `use_cache=True`), resampled to daily frequency via mean, negated (so high positive funding → large negative carry score → short bias), then cross-sectionally z-scored.

### Long entry

Coins with the highest combined signal score (70% × z-scored momentum + 30% × z-scored negated funding) receive the largest long allocations.

### Short entry

Coins with the lowest combined signal score (negative momentum, high positive funding) receive the largest short allocations.

### Exit / Rebalance

- **Buffered rebalance:** Positions are only adjusted when they drift more than 20% (`buffer_threshold=0.2`, `buffer_mode=relative`) from their target weights. This reduces turnover.
- **Rebalance method:** `to_edge` — positions are trimmed to the buffer boundary rather than fully re-optimized.
- **No explicit stop-loss or take-profit.** Exits occur only through rebalancing.

### Holding period

No fixed holding period. Positions are held until the next rebalance event (when drift exceeds 20%). In practice, most positions are held for extended periods — the asset-hold table shows 12 of 30 assets held for all 675 days (97.97% of the window).

### Position sizing

- `ForecastScaler`: target average absolute forecast of 10.0.
- `ForecastCapper`: forecast capped at 20.0.
- `ForecastWeightNormalizer`: target leverage of 1.0 (1x gross, dollar-neutral long/short).

### Parameters

| Parameter | Value | Source |
|---|---|---|
| Momentum lookback (ROC period) | 14 | Source-reported (default) |
| Momentum weight | 0.7 | Source-reported (default) |
| Carry weight | 0.3 | Source-reported (default) |
| Universe | Top-30 by volume | Source-reported (default) |
| Buffer threshold | 0.2 (20% relative) | Source-reported |
| Target leverage | 1.0 | Source-reported |
| Target timeframe | 1d | Source-reported |
| Bar offset | 12h | Source-reported |
| Input price timeframe | 15min | Source-reported |

The source provides an 18-cell sensitivity grid across momentum lookback (10, 14, 30), momentum weight (0.5, 0.7, 1.0), and universe size (top-20, top-30). The default is not the best-performing cell — it is the most robust setting.

## Required data

- **Instrument:** Top-30 Hyperliquid perpetual futures contracts by 24h volume, dynamically resolved.
- **Venue:** Hyperliquid (decentralized perpetual futures exchange).
- **Market type:** USDC-margined perpetual futures.
- **Timeframe:** Daily signal, 15-minute input bars for price resampling.
- **Fields:**
  - OHLCV (15-minute candles, resampled to daily).
  - Funding rate settlements (periodic, hourly on Hyperliquid; aggregated to daily mean).
- **Point-in-time:** Real Hyperliquid historical data. Universe membership is resolved at each rebalance using the pinned launch universe (top-20 or top-30 at strategy inception, 2024-08-15). This introduces potential survivorship bias for tokens that delisted or lost volume ranking during the window.
- **Timestamp:** UTC.
- **Missing data:** Not explicitly discussed by source. Hyperliquid is a 24/7 exchange with continuous funding settlements.

## Execution assumptions

- **Signal-to-order timing:** Daily signal formation. The `bar_offset=12h` implies the signal is computed using the bar ending 12 hours before the execution time, providing a buffer against staleness.
- **Fill model:** Assumed filled at the resampled daily close price (or equivalent). The source does not specify intrabar execution.
- **Fees:** 4.5 bps per side (maker/taker combined assumption), 9 bps round trip.
- **Slippage:** 4.5 bps per side, 9 bps round trip.
- **Funding:** Included in all reported figures. A long position pays funding when positive; a short position collects funding when positive. The carry component of the signal explicitly accounts for this.
- **Leverage:** 1x gross (dollar-neutral long/short).
- **Rebalance:** Buffered — only trades when position drifts >20% from target. Rebalance method `to_edge` trims to buffer boundary.
- **Partial fills / failures:** Not discussed by source. Hyperliquid is an order-book venue with liquidity constraints on smaller perps.
- **Capacity:** Not discussed by source. The strategy trades top-30 Hyperliquid perps by volume, which have limited depth compared to BTC/ETH on major CEXs. Position sizing at 1x gross across 30 names implies relatively small individual positions.

## Evidence

### Source-reported

All performance figures below are sourced from Keel Research's backtest on real Hyperliquid market data, 2024-08-15 to 2026-07-05, net of fees (4.5 bps/side), slippage (4.5 bps/side), and funding:

| Metric | Default Settings |
|---|---|
| Sharpe Ratio | 1.98 |
| Total Return | +116.6% |
| Maximum Drawdown | −16.3% |
| Number of Trades | 6,453 |
| Annualized Turnover | High (6,401+ trades) |
| Price-only Sharpe | 1.82 |

Monthly returns (default settings):

| Month | Return |
|---|---|
| 2024-08 | 0.0% |
| 2024-09 | +9.5% |
| 2024-10 | −4.0% |
| 2024-11 | +15.2% |
| 2024-12 | +8.7% |
| 2025-01 | −12.4% |
| 2025-02 | +10.5% |
| 2025-03 | −7.3% |
| 2025-04 | +10.7% |
| 2025-05 | −2.0% |
| 2025-06 | −3.5% |
| 2025-07 | +7.8% |
| 2025-08 | +1.4% |
| 2025-09 | +6.5% |
| 2025-10 | +8.7% |
| 2025-11 | +2.0% |
| 2025-12 | +9.8% |
| 2026-01 | +5.0% |
| 2026-02 | +1.4% |
| 2026-03 | +2.8% |
| 2026-04 | +0.6% |
| 2026-05 | +12.7% |
| 2026-06 | +2.2% |
| 2026-07 | −2.2% |

Sensitivity grid highlights (selected):

| Settings | Sharpe | Return | Worst DD | Trades |
|---|---|---|---|---|
| Momentum 14 · Weight 0.7 · top30 (default) | 1.98 | 116.6% | −16.3% | 6,453 |
| Momentum 14 · Weight 0.7 · top20 | 2.07 | 169.7% | −16.9% | 4,237 |
| Momentum 14 · Weight 1.0 · top20 | 2.09 | 190.4% | −17.5% | 3,411 |
| Momentum 14 · Weight 0.5 · top30 | 1.12 | 47.4% | −23.9% | 7,136 |
| Momentum 10 · Weight 0.7 · top30 | 1.82 | 102.4% | −26.7% | 6,849 |
| Momentum 30 · Weight 0.7 · top30 | 0.91 | 38.4% | −17.6% | 5,873 |

The top-20 universe variants generally outperform top-30 on Sharpe and return, suggesting concentration benefits (or survivorship bias in the smaller set). Longer momentum lookbacks (30 days) degrade performance, suggesting the optimal momentum horizon in crypto perps is shorter (10-14 days).

The source notes that the strategy "held up across both bull and bear stretches in the test window rather than depending on the market's overall direction."

### Independently reproduced

Not independently reproduced.

### Negative evidence

Source-reported weaknesses:
- **Sharp momentum reversals:** When yesterday's leaders crash, the book is caught leaning the wrong way. The funding tilt softens these but does not remove them.
- **High turnover:** 6,453 trades over 23 months (~280 trades/month). Fees matter. The drift buffer (20%) is the primary mechanism controlling turnover.
- **Regime sensitivity:** The strategy performs best in "trending markets with wide dispersion between winners and losers, and with active funding." It underperforms in range-bound, low-funding environments.
- **Survivorship bias:** The universe is pinned at launch (top-30 by volume on 2024-08-15). Tokens that lost volume ranking or delisted during the window are still traded if they remain in the pinned set, introducing potential look-ahead bias. The source shows 12 of 30 assets held for 97.97% of the window, suggesting the pinned universe is largely static.
- **Single-venue, short window:** The entire backtest is on Hyperliquid only, covering ~23 months (2024-08-15 to 2026-07-05). This is a single market regime on a single venue.
- **Cross-exchange funding rate differences are not exploited:** The strategy uses only Hyperliquid funding rates. The existing research (Pindza 2026, Zhivkov et al. 2026) documents significant cross-venue funding rate divergence, particularly CEX-DEX gaps. The strategy does not capture this dispersion.

None identified in external reviewed sources beyond the source itself. Absence is not evidence of no negative result.

## Falsification plan

To test the robustness of the momentum-carry combo hypothesis:

1. **Out-of-sample window extension:** Extend the backtest beyond 2026-07-05. The strategy should be re-tested monthly as new data becomes available (the source commits to monthly re-backtest).
2. **Universe survivorship test:** Replace the pinned universe with a dynamically reconstituted universe (e.g., rolling top-30 by volume each month, with delisted tokens removed). This tests whether the performance is driven by the specific 30 tokens chosen at launch or by the signal construction.
3. **Cross-venue portability:** Replicate the strategy on Binance, Bybit, or OKX perpetuals. The momentum and funding mechanisms should transfer if the alpha is genuine; failure to transfer suggests venue-specific effects.
4. **Funding environment sensitivity:** Test performance in low-funding regimes (when most perps trade near flat funding). The carry component should underperform; the question is whether momentum alone is sufficient.
5. **Parameter perturbation:** The 18-cell grid shows sensitivity to lookback and blend weight. The Sharpe ranges from 0.34 to 2.09 across settings — a 6x spread. This suggests the signal is parameter-sensitive, though the source argues the default is the most robust.
6. **Turnover stress test:** At 6,453 trades over 23 months, the strategy pays ~58 bps in fees per trade (9 bps round trip × ~6,453 trades). Re-run with higher fee assumptions (e.g., 15 bps/side for taker) to test fee sensitivity.
7. **Falsification threshold (research-defined):** If the out-of-sample Sharpe drops below 0.5 over any rolling 6-month window, or if maximum drawdown exceeds 30%, the hypothesis that the strategy captures genuine alpha (rather than overfit noise) is materially weakened.

## Crypto portability

**Adapted.** The strategy is designed for and tested exclusively on Hyperliquid perpetual futures. The underlying mechanisms (cross-sectional momentum, funding rate carry) are documented across crypto perpetual markets on multiple venues. However:

- **Venue-specific:** Hyperliquid's fee structure (4.5 bps/side assumed), funding calculation (hourly settlement), and liquidity profile differ from Binance, Bybit, or OKX. Replication requires adjusting fee, slippage, and funding assumptions for each venue.
- **24/7 session:** The daily rebalance with 12h bar offset is compatible with 24/7 crypto markets.
- **Funding asymmetry:** Funding rates on Hyperliquid have historically been higher on average than on Binance (BitMEX Q2 2026 report: ~7.17% annualized premium for BTC). This means the carry component may perform differently on other venues.
- **Liquidity:** Top-30 Hyperliquid perps have lower depth than top-30 Binance perps. Position sizing at 1x gross across 30 names may face slippage challenges on smaller venues.
- **No on-chain / DeFi-specific data dependency.** The strategy uses only price and funding rate data, which are available on any perpetual venue.

## Limitations

- **Short backtest window:** 23 months (2024-08-15 to 2026-07-05) on a single venue. This is insufficient to evaluate regime robustness across bull, bear, and sideways markets.
- **Survivorship bias:** The pinned universe includes tokens that may have been selected with hindsight. Dynamic reconstitution testing is needed.
- **Not independently reproduced.** The backtest is produced by the same platform (Keel) that offers live execution. While the code is open-source and the methodology is transparent, independent replication has not been reported.
- **High turnover:** 6,453 trades over 23 months generates substantial fee drag. The source's cost assumptions (9 bps round trip) are plausible for Hyperliquid but may be optimistic for larger position sizes or during volatility spikes.
- **No cross-venue validation.** The strategy has not been tested on any venue other than Hyperliquid.
- **Single-asset-class.** Crypto perpetual futures only. No comparison to equity momentum-carry hybrids or traditional commodity carry.
- **Data gap:** Position-level PnL attribution (momentum contribution vs. carry contribution) is not provided. It is unclear how much of the Sharpe comes from momentum vs. carry.
- **Regime window overlap:** The backtest period (Aug 2024 – Jul 2026) includes a significant bull run (BTC from ~$60K to ~$120K+). The strategy's performance in a sustained bear market is partially evidenced by the monthly returns (e.g., Jan 2025 −12.4%, Mar 2025 −7.3%) but a full bear-market test is not available.

## Implementation status

Not implemented. No backtest, paper trade, testnet, or live execution has been performed in our research stack. The strategy is source-reported only.

## Adoption boundary

This record is research-only. The presence of this record does not mean:
- The strategy is profitable in live trading.
- The backtest results are validated or independently reproduced.
- The strategy is approved for implementation, paper trading, testnet, or live trading.
- The cost assumptions are appropriate for our execution context.

Any adoption decision must be based on independent out-of-sample testing, cross-venue replication, and explicit comparison to existing strategies in our pipeline.

## Related Wiki records

- `[[quant/crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]` — CEX-DEX funding-rate carry (cross-exchange arbitrage, distinct mechanism from single-venue momentum+carry blend)
- `[[quant/crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-09]]` — Cross-sectional funding carry factor (pure carry, no momentum component)
- `[[quant/crypto-futures-term-structure-roll-yield-carry-2026-08-31]]` — Crypto carry from futures term structure (different instrument universe)

## Sources

1. Keel Research, "Momentum + Funding Strategy on Hyperliquid", https://usekeel.io/strategies/momentum-funding-hyperliquid, data as of 2026-07-05. Backtested on real Hyperliquid perpetual market data, 2024-08-15 to 2026-07-05, net of fees (4.5 bps/side), slippage (4.5 bps/side), and funding.
2. Keel Research, "How we backtest every strategy — Methodology", https://usekeel.io/strategies/methodology. Describes engine, data, cost model, and disclosure policy.
3. Keel Trade, GitHub repository, https://github.com/keel-trade/keel-trade (MIT license). Strategy definition, backtest engine, and live execution code.
