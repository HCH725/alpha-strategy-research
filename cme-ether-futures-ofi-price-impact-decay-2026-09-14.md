---
schema: strategy-research-record-v1
title: CME Ether Futures OFI Price-Impact Decay Signal
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - order-flow
  - microstructure
  - cme
  - ether
  - futures
  - ofi
  - price-impact
status: research-only
confidence: high
source_as_of: 2026-06-11
sources:
  - "Tony Li, 'Order Flow Imbalance and the Decay of Price Impact in CME Ether Future', SSRN 6772279, posted 18 May 2026, revised 11 Jun 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6772279"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CME Ether Futures OFI Price-Impact Decay Signal

## Provenance

- **Source**: Tony Li, Imperial College London. "Order Flow Imbalance and the Decay of Price Impact in CME Ether Future." SSRN working paper 6772279, posted 18 May 2026, revised 11 Jun 2026.
- **URL**: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6772279
- **Sample period**: February 2021 – April 2026 (full); out-of-sample January 2024 – April 2026.
- **Universe**: CME Ether futures (ETH).
- **Note**: This is a working paper, not peer-reviewed journal publication. Author affiliation stated as Imperial College London.

## Economic mechanism

### Source-reported

Order Flow Imbalance (OFI), defined following Cont, Kukanov, and Stoikov (2014), captures the net pressure of buyer-versus seller-initiated trading. On CME Ether futures, OFI exhibits strong contemporaneous explanatory power for mid-quote changes (β = +0.249, R² = 0.32). The signal's forward impact rises over the first minutes, peaks near +21.6 bp at approximately four hours, and reverses within a day — consistent with temporary price impact that decays as liquidity replenishes and inventory pressures unwind.

### Research interpretation

The hypothesized mechanism is that aggressive order flow creates temporary price pressure through inventory effects and adverse selection. On regulated, institutional-grade CME Ether futures, this pressure exhibits a predictable decay pattern: the signal's predictive content peaks at the 4-hour horizon and reverses within 24 hours. A vol-targeted trading strategy can harvest this predictable decay by entering in the direction of OFI and exiting as the impact dissipates. The 4-hour peak aligns with the typical horizon at which institutional position-taking and hedging activity completes, and the reversal within a day suggests that the price pressure is temporary rather than informational.

## Signal

- **Formation timestamp**: Dollar-volume bars from the raw tick stream; signal computed at bar boundaries from OFI aggregated within each bar.
- **Lookback**: OFI computed from tick-level trade and quote data on CME Ether futures.
- **Entry**: Long when OFI is positive (net buyer-initiated flow); short when OFI is negative. Vol-targeted sizing with a 10-minute clock cap (research-proposed: the 10-minute cap is part of the fitted strategy, not a source-specified invariant).
- **Exit**: Exit on reversal of price impact; exact exit trigger is the combination of 10-minute clock cap and vol-targeting (research-proposed parameterization).
- **Holding period**: Strategy fitted to target approximately 4-hour peak impact horizon; actual holding depends on vol-targeting and clock cap.
- **Parameters**: Seven parameters fitted jointly on the in-sample window, including vol-targeting parameters, clock cap, and entry/exit thresholds. Parameter fitting is research-proposed and subject to overfitting risk.
- **Position sizing**: Vol-targeted; sizing adjusted based on realized volatility.

## Required data

- **Instrument**: CME Ether futures (ETH).
- **Venue**: CME (Chicago Mercantile Exchange).
- **Market type**: Regulated futures.
- **Timeframe**: Tick-level data aggregated into dollar-volume bars.
- **Fields**: Bid/ask quotes, trade data (aggressor side), dollar-volume for bar construction.
- **Point-in-time**: Data sourced from CME tick stream; no look-ahead issues identified in the abstract.
- **Timestamp**: Not specified in abstract; presumably CME exchange timestamps.
- **Missing-data**: Not stated in source.

## Execution assumptions

- **Signal-to-order timing**: Dollar-volume bar boundary; signal available at bar close.
- **Fill model**: Fill prices reconstructed from the tick stream for realistic execution estimates.
- **Fees**: Not explicitly stated in abstract for the CME contract; CME Ether futures have known fee structure.
- **Slippage**: Accounted for via tick-stream-based fill reconstruction; realistic execution Sharpe drops from +5.11 to +3.5–3.8.
- **Capacity**: Under a square-root impact model (Almgren and Chriss, 2000), Sharpe remains above 2.0 up to $10M of deployed capital under the base average-daily-volume assumption.
- **Leverage/margin**: Not specified in abstract.
- **Partial fills / failures**: Not stated in source.

## Evidence

### Source-reported

- **OFI regression**: β = +0.249 (t = 52.8, R² = 0.32) on 25,546 out-of-sample dollar-volume bars (Jan 2024 – Apr 2026), Newey-West HAC standard errors.
- **Forward impact**: Peaks near +21.6 bp at four hours; reverses within a day.
- **Strategy performance (OOS)**: Vol-targeted strategy achieves Sharpe +5.11 at −2.8% maximum drawdown over 4,531 round-trip trades.
- **Realistic execution**: Fill prices reconstructed from tick stream place realistic execution at Sharpe +3.5 to +3.8.
- **Walk-forward**: Rolling walk-forward re-selection reproduces the single-split figure at Sharpe +4.5 to +5.0.
- **Statistical tests**: Hansen (2005) SPA test over 1,920-configuration joint search space gives p < 0.001; Deflated Sharpe Ratio (Bailey and Lopez de Prado, 2014) gives P(SR > 0) = 0.958.
- **Placebo test**: Direction-shuffled placebo (preserving entry times, exit times, and long/short count) returns mean Sharpe −0.37 over 200 seeds.
- **Capacity**: Sharpe remains above 2.0 up to $10M deployed capital under square-root impact model and base ADV assumption.

All figures above are source-reported. The high Sharpe ratios (+5.11 OOS) are notable but should be interpreted cautiously: the sample is a single asset (ETH) on a single venue (CME), and the 1,920-configuration search space, while addressed by deflated Sharpe, still represents substantial multiple testing.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source. The absence of negative evidence in the abstract does not imply the signal is robust across regimes, assets, or time periods. The paper tests only CME Ether futures; no cross-asset replication is reported in the abstract.

## Falsification plan

1. **Cross-asset replication**: Test the same OFI signal construction on CME Bitcoin futures and other regulated crypto perpetual/futures contracts. If the signal does not generalize beyond ETH, the mechanism may be venue- or asset-specific rather than a general microstructure effect.
2. **Regime decomposition**: Split the OOS period (2024–2026) into bull, bear, and sideways regimes. If the signal degrades in specific regimes, the regime dependency should be characterized.
3. **Cost sensitivity**: Stress-test at higher fee tiers, wider spreads, and during low-liquidity periods (e.g., weekends, holidays). The realistic-execution Sharpe (+3.5–3.8) already shows significant cost erosion from the ideal (+5.11).
4. **Capacity stress**: Test whether the $10M capacity claim holds under varying ADV assumptions and market stress periods.
5. **Parameter stability**: Re-fit the 7 parameters on rolling windows and test whether the parameter landscape is stable or exhibits cliff effects.
6. **Walk-forward permanence**: Extend the walk-forward analysis beyond the reported period to test whether the signal persists as CME ETH futures volume and participant composition evolve.

## Crypto portability

**Adapted**

The signal originates on CME-regulated Ether futures, which are a specific venue with institutional participants, regulated margin, and known fee structure. Portability considerations:

- **Spot vs. perpetual**: The OFI mechanism is expected to exist in crypto perpetual futures and potentially spot markets, but the decay profile (4-hour peak, daily reversal) may differ due to different participant mix, leverage dynamics, and funding-rate interactions.
- **Venue fragmentation**: CME is a single, regulated venue with deep institutional liquidity. Crypto perpetual futures trade across multiple offshore venues with different fee structures, liquidity profiles, and participant compositions.
- **Funding rate**: CME futures do not have funding rates; perpetual futures do. The interaction between OFI-driven price pressure and funding-rate mechanics is not addressed.
- **24/7 session**: CME ETH futures have defined trading hours; crypto perpetuals trade 24/7. The 4-hour impact horizon may not translate directly to continuous markets.
- **Liquidity**: CME ETH futures have institutional-grade liquidity; most crypto venues have thinner books and higher adverse selection risk.

## Limitations

- **Single asset, single venue**: The study tests only CME Ether futures. Generalizability to other crypto assets, perpetual futures, or spot markets is unverified.
- **Working paper**: Not peer-reviewed; results should be treated as preliminary.
- **Multiple testing**: 1,920-configuration search space, addressed by deflated Sharpe but still substantial.
- **High Sharpe concern**: OOS Sharpe of +5.11 is unusually high and may reflect sample-specific conditions, the specific OOS window (Jan 2024 – Apr 2024, which includes the ETH ETF approval rally), or model-specific advantages.
- **Abstract-only verification**: Full paper details (transaction cost model, exact parameter fitting procedure, robustness checks beyond the abstract) were not accessible for this review.
- **Capacity assumption**: The $10M capacity claim relies on a square-root impact model and base ADV assumption; real capacity may be lower during stress periods.
- **Signal decay**: The 4-hour peak and daily reversal imply the signal is short-lived; execution latency and fill quality are critical.

## Implementation status

Not implemented. No implementation in our research stack.

## Adoption boundary

This record represents research material only. It does not mean the strategy is profitable, validated, approved for implementation, or suitable for paper/testnet/live trading.

## Related Wiki records

No directly related Wiki Brain records identified that share the same source identity or materially similar mechanism. Related order-flow research records exist in the repo but target different markets, instruments, or mechanisms.

## Sources

1. Tony Li, "Order Flow Imbalance and the Decay of Price Impact in CME Ether Future," SSRN working paper 6772279, posted 18 May 2026, revised 11 Jun 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6772279
