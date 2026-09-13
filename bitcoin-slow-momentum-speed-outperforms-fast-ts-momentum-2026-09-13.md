---
schema: strategy-research-record-v1
title: "Bitcoin Time-Series Momentum Speed: Slow Signals Outperform Fast in Crypto"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - momentum
  - time-series-momentum
  - momentum-speed
  - lookback-horizon
  - risk-management
  - regime-dependent
status: research-only
confidence: medium
source_as_of: 2026-07-10
sources:
  - "Kang, Yeonchan and Ryu, Doojin, 'Time-series momentum and market timing in Bitcoin', Risk Management, Vol. 28, Article 54 (July 2026). DOI: 10.1057/s41283-026-00234-7. https://link.springer.com/article/10.1057/s41283-026-00234-7"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Time-Series Momentum Speed: Slow Signals Outperform Fast in Crypto

## Provenance

- **Authors:** Yeonchan Kang, Doojin Ryu
- **Publication:** Risk Management, Vol. 28, Article 54, July 2026 (Springer Nature)
- **DOI:** 10.1057/s41283-026-00234-7
- **Data source:** Binance Public Data (https://data.binance.vision)
- **Sample:** Bitcoin (BTC) on Binance
- **Source URL:** https://link.springer.com/article/10.1057/s41283-026-00234-7
- **Support:** National Research Foundation of Korea (NRF), funded by the Korean government (MSIT) RS-2025-00518388

## Economic mechanism

### Source-reported

Bitcoin markets exhibit continuous 24/7 trading, high volatility, and significant short-horizon noise. The authors argue that these characteristics make rapid momentum signal adjustment prone to overreaction. Slower signals, by contrast, hold exposure through profitable disagreement states where fast signals would have already exited. The authors frame signal speed as an endogenous risk-management device rather than merely a return-prediction choice.

### Research interpretation

The hypothesized mechanism is that crypto markets' continuous trading and high noise-to-signal ratio at short horizons create a regime where fast momentum signals overreact to transient noise, triggering whipsaw losses. Slow momentum signals (12-week baseline) filter out this noise and capture more persistent trend components, resulting in better risk-adjusted performance. This is the reverse of the equity-market pattern, where faster signals can sometimes add value through quicker adaptation to regime changes. The mechanism is consistent with Hong & Stein (1999) underreaction/overreaction dynamics adapted to the crypto microstructure.

## Signal

- **Signal type:** Time-series momentum (trend following) on Bitcoin
- **Formation timestamp:** Weekly rebalancing implied by the "week" lookback convention; signal formation at end of each lookback window
- **Lookback:** Varying speed parameter; optimal baseline at 12 weeks. Authors sweep speed along a continuous parameter from fast to slow.
- **Entry:** Long when cumulative return over the lookback window is positive (standard t-series momentum sign signal); short when negative. Research-proposed: standard Moskowitz, Ooi, Pedersen (2012) sign convention assumed from the "time-series momentum" framing; exact entry/exit rules not fully specified in the abstract.
- **Exit:** Research-proposed: signal reversal triggers exit; exact exit timing not specified in the abstract.
- **Holding period:** Determined by rebalancing frequency (weekly implied)
- **Parameters:** Optimal speed at 12-week baseline; dynamic speed adjustment tested but found to add little beyond the simple low-speed rule
- **Position sizing:** Not specified in the abstract (data gap)
- **Markets:** Bitcoin only (single-asset); no cross-sectional component

## Required data

- Instrument: Bitcoin (BTC) perpetual futures or spot on Binance
- Venue: Binance
- Market type: Perpetual futures or spot (Binance Public Data)
- Timeframe: Weekly or sub-weekly (for computing lookback returns over 12-week windows)
- Fields: OHLCV (at minimum close prices for return computation)
- Point-in-time: Standard historical data; no lookahead requirements beyond the lookback window
- Timestamp: UTC (Binance standard)
- Missing-data: Not specified in the abstract (data gap)

## Execution assumptions

- **Signal-to-order timing:** Not specified in the abstract (data gap)
- **Next-bar vs same-bar execution:** Not specified (data gap)
- **Order type:** Not specified (data gap)
- **Fill model:** Not specified (data gap)
- **Fees:** Not specified in the abstract whether transaction costs are included (data gap)
- **Slippage:** Not specified (data gap)
- **Impact/capacity:** Not specified (data gap)
- **Leverage:** Not specified (data gap)
- **Funding:** Not specified (data gap)

## Evidence

### Source-reported

From the abstract: "slow signals, based on a 12-week baseline horizon, outperform intermediate and fast alternatives." The authors state this holds for risk-adjusted performance. They also find that "dynamic speed adjustment adds little beyond a simple low-speed rule" and that "the optimal speed is market-specific." The equity-market pattern is described as reversed in Bitcoin. Specific Sharpe ratios, returns, or drawdowns are not provided in the abstract or publicly available sections (data gap — requires full-text access to the Springer article for quantitative results).

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample test:** Apply the 12-week slow momentum signal to BTC data post-publication (July 2026 forward) and verify whether the risk-adjusted performance advantage persists.
2. **Parameter sensitivity:** Test lookback horizons around 12 weeks (e.g., 8, 10, 14, 16 weeks) to assess whether the result is robust to small perturbations or concentrated at a single parameter value.
3. **Transaction cost stress:** Re-run with realistic maker/taker fees, slippage, and funding costs for BTC perpetuals to determine whether the slow-signal advantage survives execution friction.
4. **Cross-asset test:** Apply the same speed-sweep methodology to ETH and other major altcoins to test whether the 12-week optimal is Bitcoin-specific or generalizable.
5. **Regime breakdown:** Separate bull and bear regimes to test whether the slow-signal advantage is driven by specific market conditions.
6. **Comparison to buy-and-hold:** Benchmark against simple buy-and-hold of BTC to confirm the momentum signal adds value beyond passive exposure.
7. **Ablation:** Test whether the advantage is truly about signal speed or about exposure duration (slow signals may simply hold positions longer, capturing more of the crypto positive drift).

## Crypto portability

direct — the source studies Bitcoin specifically on Binance, so the mechanism is native to crypto markets. The continuous 24/7 trading structure and high short-horizon noise are crypto-specific characteristics that the authors identify as the reason fast signals overreact. The finding is not a port from equities but a crypto-native result.

## Limitations

- **Single asset:** The study focuses on Bitcoin only; generalizability to other cryptocurrencies is untested.
- **Data gap — quantitative results:** The abstract does not report specific Sharpe ratios, returns, drawdowns, or sample periods. Full-text access to the Springer article is required to verify quantitative claims.
- **Data gap — execution assumptions:** Transaction costs, slippage, funding, and leverage assumptions are not specified in the abstract.
- **Data gap — sample period:** The exact sample window is not stated in the abstract (data.binance.vision is the data source, but the specific date range is not provided).
- **Not independently reproduced.**
- **Market-specific:** The authors note that optimal speed is market-specific, so the 12-week finding may not transfer to other crypto assets or to different time periods.
- **Data gap — position sizing:** No information on position sizing, volatility targeting, or risk management is provided in the abstract.

## Implementation status

Not implemented. No implementation in our research stack has been completed.

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]] — related time-series momentum research in crypto
- [[crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]] — AdaptiveTrend framework with dynamic trailing stops and portfolio construction
- [[hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12]] — volatility-targeted tsmom with drawdown calibration

## Sources

1. Kang, Yeonchan and Ryu, Doojin (2026). "Time-series momentum and market timing in Bitcoin." Risk Management, Vol. 28, Article 54. DOI: 10.1057/s41283-026-00234-7. https://link.springer.com/article/10.1057/s41283-026-00234-7
