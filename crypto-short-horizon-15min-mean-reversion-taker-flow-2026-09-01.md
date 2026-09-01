---
schema: strategy-research-record-v1
title: "Crypto Short-Horizon 15-Minute Mean Reversion Conditioned on Taker Flow"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - mean-reversion
  - microstructure
  - intraday
  - order-flow
  - liquidity-provision
  - high-frequency
status: research-only
confidence: high
source_as_of: 2026-08-22
sources:
  - "Nadav A. Kitron, Jonathan M. Wengrowicz, 'Short-horizon mean reversion in cryptocurrency markets: a matched cross-market measurement', arXiv:2608.21888v1 [q-fin.TR], August 22 2026. https://arxiv.org/abs/2608.21888"
  - "Replication code: https://github.com/nadav2/short-horizon-reversion"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Short-Horizon 15-Minute Mean Reversion Conditioned on Taker Flow

## Provenance

- Paper: arXiv:2608.21888v1 [q-fin.TR], submitted August 22, 2026.
- Authors: Nadav A. Kitron (independent), Jonathan M. Wengrowicz (independent).
- Subjects: Trading and Market Microstructure (q-fin.TR); Statistical Finance (q-fin.ST).
- Data: 15-minute Binance USDT spot klines, 183 highest-volume pairs, 2025-01-01 to 2026-02-08 (in-sample), with frozen post-sample holdout 2026-02-12 to 2026-08-08.
- Cross-market control: 187 liquid US stocks/ETFs (Alpaca IEX feed), matched protocol.
- Supporting data: Coinbase, OKX, Bybit independent-venue refetches; Dukascopy spot metals/FX; Binance taker-flow, order-book depth, perpetual funding rate series.
- Replication package: https://github.com/nadav2/short-horizon-reversion (pipeline code, frozen symbol lists, SHA-256-hashed result files).
- Source URL: https://arxiv.org/abs/2608.21888

## Economic mechanism

### Source-reported

At 15-minute horizons, directional mean reversion is pervasive in cryptocurrency markets: 90% of 183 Binance pairs carry significant directional reversal (measured by AUC), versus only 2.7% of 187 US stocks/ETFs under the identical strictly out-of-sample walk-forward protocol. The signal is stable across every focal coin-year since 2021.

Key structural findings:
- The signal lives in signs, not magnitudes: lag-one return autocorrelation is near zero on major coins, yet simply betting against the previous 15-minute candle captures most of the effect.
- On the originating tape, the reversal concentrates after moves driven by aggressive taker flow and grows with flow intensity.
- Order-book depth consumed during a move conditions nothing: consistent with compensated liquidity provision (market makers absorbing overreaction) in a book that reforms within the bar.
- US-listed crypto funds (IBIT, FBTC, GBTC, ETHE, etc.) inherit their underlying's reversal signature; stocks merely correlated with crypto inherit nothing. Transmission is present from a fund's first months, through a futures-based NAV, at 2x leverage, and inside the sampling minute.

### Research interpretation

The hypothesized mechanism is **compensated liquidity provision at short horizons in crypto markets**: aggressive taker orders push prices beyond fair value, and passive limit-order providers capture the mean reversion. The authors explicitly note they cannot exclude an informational alternative — the flow conditioning is consistent with liquidity provision but not a clean identification of it.

The cross-market contrast (crypto vs. US equities) is striking and suggests that the efficiency of short-horizon price discovery is structurally different in crypto, likely due to:
- Retail-dominated order flow (less informed, more overreaction);
- Fragmented liquidity across venues;
- 24/7 trading creating continuous price discovery;
- Absence of specialist market makers or designated liquidity providers.

The effect's persistence across 5 years and 183 pairs, surviving permutation nulls and frozen holdouts, makes this one of the more robust microstructure findings in crypto.

## Signal

- **Universe**: Top-K highest-volume Binance USDT spot pairs (183 pairs in the study).
- **Timeframe**: 15-minute candles.
- **Signal construction**: Lag-one return sign reversal. If the previous 15-minute candle closed up (return > 0), go short at the next candle open; if down, go long. The primary measurement model is a constrained distributed-lag logit (3 parameters), but the simple sign-reversal baseline captures most of the effect.
- **Entry**: Market order at open of candle t+1, opposite direction to candle t's sign.
- **Exit**: Close at end of candle t+1 (1-bar holding period) or use ATR-based trailing stop.
- **Conditioning (optional)**: Filter for candles with high taker-buy volume imbalance (aggressive taker flow). The reversal is stronger after high-intensity taker-flow moves.
- **Sizing**: Equal-weight across universe (cross-sectional) or per-trade fixed risk.
- **Parameters**: Signal amplitude A < 0 indicates mean reversion; kernel decay α controls lag weighting. Simple sign-reversion (no fitting) also works.

## Required data

- Instrument: Binance USDT spot pairs (universe of highest-volume).
- Venue: Binance (primary); Coinbase, OKX, Bybit (robustness).
- Market type: Spot.
- Timeframe: 15-minute candles.
- Fields: OHLCV; taker-buy base-volume (for flow conditioning); bid/ask depth within 1-5% of mid (optional, for depth conditioning).
- Funding rate: Not required for spot execution; useful for cross-validation against perpetuals.
- Timestamps: UTC-aligned candle boundaries.

## Execution assumptions

- **Signal-to-order timing**: Next-bar execution (candle close signal → candle open entry). No same-bar execution assumed.
- **Order type**: Market order at candle open.
- **Fill model**: Assume full fill at open price.
- **Fees**: The study finds the gross edge peaks near 1.3 bp per trade. Round-trip costs are approximately 5 bp at maker fees and 10-20 bp at taker fees on major venues. The signal is too small to clear benchmark spot taker costs but may be viable at maker-tier fees or on perpetuals with lower fee structures.
- **Slippage**: Not explicitly modeled; implicit in the 5 bp cost band.
- **Capacity**: The gross edge of 1.3 bp is large enough to detect but too small to capture at benchmark spot costs. This limits the strategy to low-fee environments (maker tiers, institutional fee schedules, or perpetual markets).
- **Leverage**: Not required; spot execution.
- **Latency**: Not explicitly studied; signal operates at 15-minute resolution.

## Evidence

### Source-reported

- 90% of 183 Binance pairs carry significant directional reversal at 15-minute horizons (out-of-sample AUC > 0.5), versus 2.7% of 187 US stocks/ETFs.
- The signal is stable across every focal coin-year since 2021.
- Gross edge peaks near 1.3 bp per trade against 5 bp round-trip cost (maker fees).
- Class-mean AUC gap of +0.031 as designed and +0.011 (95% CI [+0.008, +0.014]) under the most conservative accounting, clear of zero.
- The contrast survives an artifact battery, an exact permutation null, and a frozen six-month forward holdout (2026-02-12 to 2026-08-08).
- Reversal concentrates after moves driven by aggressive taker flow and grows with flow intensity.
- Order-book depth consumed during a move conditions nothing.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The gross edge (1.3 bp) is below the round-trip taker cost on most retail fee schedules (10-20 bp). This means the strategy is not executable at standard retail costs.
- The signal is too small to capture at benchmark spot costs — this is explicitly stated by the authors as consistent with a limits-to-arbitrage account.
- The mechanism (liquidity provision vs. informational) is not identified; the authors state this limitation.
- Survivorship bias: the universe was selected on post-sample volume rankings, though the authors bound this empirically.
- Flat bars (zero return) are labeled "down" by convention, which affects the base rate; the authors carry this as a separate effect size.

## Falsification plan

- **Out-of-sample decay**: The frozen six-month holdout (2026-02-12 to 2026-08-08) already provides one OOS test. Future holdout periods should be checked for decay.
- **Fee sensitivity**: Any backtest must apply realistic round-trip costs. At taker fees (10-20 bp), the strategy should show negative net returns; at maker fees (5 bp), it should be marginal.
- **Venue sensitivity**: Test on Coinbase, OKX, Bybit data to verify the signal is not Binance-specific.
- **Regime conditioning**: Check whether the signal persists through major market stress events (e.g., FTX collapse, SVB contagion) or if it disappears when liquidity provision is overwhelmed.
- **Taker-flow filter ablation**: Compare signal strength with and without taker-flow conditioning to verify the flow component adds predictive power.
- **Capacity test**: Determine the maximum deployable AUM before the edge is consumed by market impact.
- **Failure metric**: If the post-holdout AUC drops below 0.505 (indistinguishable from chance), the hypothesis is materially weakened.

## Crypto portability

direct

This is a crypto-native finding. The signal is measured and validated on Binance spot data across 183 pairs. The authors explicitly study crypto markets and do not port from equities.

Crypto-specific considerations:
- The signal operates on spot markets; perpetual markets may have different dynamics due to funding rate costs and leverage effects.
- 15-minute candle boundaries may not align across venues; the study uses Binance's REST API bar grid which includes empty bars.
- Venue fragmentation: the signal was validated on Binance; cross-venue execution would require venue-specific calibration.
- 24/7 trading means the signal operates continuously without session boundaries.
- Liquidity varies dramatically across the 183-pair universe; the signal is weaker in the most liquid pairs where cross-sectional reversal is weakest.

## Limitations

- Gross edge (1.3 bp) is below retail taker costs; viable only at maker-tier fees or institutional fee schedules.
- Not independently reproduced.
- Mechanism evidence is descriptive, not identified (cannot distinguish liquidity provision from informational account).
- Universe selection is based on post-sample volume rankings; survivorship bias is bounded but not eliminated.
- 15-minute resolution may be too slow for capture in highly liquid pairs where the edge is strongest.
- The constrained logit measurement device is a low-variance instrument, not a model of markets; the simple sign-reversal baseline captures most of the effect.

## Implementation status

Not implemented. No PyBroker, Nautilus, paper, testnet, or live verification.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- The strategy is profitable after costs.
- The alpha has been validated.
- The strategy is approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[quant/contrarian-market-making-fill-probability-order-flow]]
- [[quant/bitcoin-turn-of-15min-candle-seasonality]]
- [[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure]]

## Sources

1. Nadav A. Kitron, Jonathan M. Wengrowicz, "Short-horizon mean reversion in cryptocurrency markets: a matched cross-market measurement", arXiv:2608.21888v1 [q-fin.TR], August 22 2026. https://arxiv.org/abs/2608.21888
2. Replication code and frozen results: https://github.com/nadav2/short-horizon-reversion
