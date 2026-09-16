---
schema: strategy-research-record-v1
title: TradingView HVP-Triggered Opening-Range Breakout and Reversal
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/1oZNa7Oq-HV-Spike-Strategy-HVP-OR-Breakout-Reversal-TP-SL-Modes/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView HVP-Triggered Opening-Range Breakout and Reversal

## Provenance

Public TradingView open-source strategy page by `kostastrovas`, published October 26, 2025: `HV Spike Strategy (HVP + OR Breakout + Reversal + TP/SL Modes)`. Stable source URL: https://www.tradingview.com/script/1oZNa7Oq-HV-Spike-Strategy-HVP-OR-Breakout-Reversal-TP-SL-Modes/. Source reviewed as of 2026-09-16.

The source describes an opening-range-breakout concept adapted to 24/7 crypto by using Historical Volatility Percentile (HVP) to decide when a bar should become the reference range instead of relying on a conventional market-session open.

## Economic mechanism

### Source-reported

The author frames the strategy as a volatility-conditioned version of the opening-range breakout / first-candle rule. In continuously traded crypto, an HVP threshold is used to identify a sufficiently high-volatility bar; that bar establishes the range. Subsequent movement outside that range is treated as directional evidence, while a move back into the range can trigger a reversal trade.

### Research interpretation

The falsifiable hypothesis is that an unusually high-volatility bar creates a temporary information/positioning boundary: sufficiently large continuation beyond its range may exhibit short-horizon momentum, while failure back into the range may identify a false breakout with opposite-direction continuation. HVP is therefore a regime/event trigger, the reference bar range is the state variable, and breakout/re-entry determines direction.

The key incremental feature versus ordinary session ORB is the event-time definition of the opening range for a 24/7 market: the range is activated by volatility percentile rather than a fixed exchange-session clock.

## Signal

- **Formation timing:** Monitor HVP and identify the first bar satisfying the configured HVP activation threshold; that bar establishes the reference high/low (`source-reported`). The exact HVP calculation window and percentile implementation are underspecified in the public description.
- **Reference range:** High-to-low range of the HVP-activated first candle (`source-reported`).
- **Long entry:** Enter when price moves 100% above the reference range according to the author's description (`source-reported`). The exact arithmetic interpretation of “100% above” is underspecified and must be resolved from the source implementation before reproduction.
- **Short entry:** Mirror condition when price moves 100% below the reference range (`source-reported`); exact arithmetic interpretation is underspecified.
- **Reversal:** If price reverses back into the reference range after breakout, the strategy takes the opposite trade (`source-reported`). Exact order timing and whether a close or intrabar touch is required are underspecified.
- **Exit:** Selectable stop-loss / take-profit modes using either percentage or ATR (`source-reported`). Exact defaults and update behavior are not fully specified in the reviewed page description.
- **Holding period:** Not explicitly specified; position duration is governed by TP/SL and reversal behavior.
- **Re-entry / reset:** Underspecified, including how a new HVP event replaces an existing reference range.
- **Parameters:** HVP activation threshold is pair/instrument dependent according to the author; TP/SL mode can use percentage or ATR. Exact defaults beyond these descriptions are not asserted here.
- **Rule completeness:** `underspecified` for exact HVP window, threshold defaults, “100%” breakout arithmetic, bar-close versus intrabar triggering, range reset, and precise order semantics.

No missing rule above is upgraded into a source-reported fact. Any future operationalization of those gaps would be research-proposed unless verified against the public source implementation.

## Required data

- Instrument/universe: source presents the concept for currency pairs, indices, and crypto, with explicit discussion of 24/7 crypto.
- Market type: not fixed by the source; crypto spot or derivatives portability is unproven.
- Timeframe: configurable / not uniquely specified in the reviewed description.
- OHLC: required for reference-bar high/low and breakout/re-entry detection.
- Historical returns or equivalent price history: required to compute historical volatility and its percentile rank.
- ATR: required when ATR-based TP/SL mode is selected.
- Volume, funding, open interest, order book and trades/aggressor side: not required by the source-reported core rule.
- Timestamp/timezone: consistent candle boundaries are required; no fixed session timezone is specified for the crypto adaptation.
- Point-in-time constraint: HVP and reference-range state must be formed only from information available at the signal timestamp. The exact source implementation should be inspected before reproduction for intrabar/repainting behavior.

## Execution assumptions

The public description does not fully specify signal-to-order timing, next-bar versus same-bar fills, market versus limit orders, spread, fees, slippage, funding, leverage, margin, latency, partial fills, or capacity. These are material gaps and must not be silently filled.

A future test should distinguish bar-close confirmation from intrabar threshold crossing because that choice can materially alter breakout and reversal behavior. This is `research-proposed`, not source-reported.

## Evidence

### Source-reported

The source explains the trading logic and states that the HVP activation threshold should be selected for each instrument. No independently traceable Sharpe, CAGR, drawdown, win-rate, or other performance statistic is asserted in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. The source itself implies parameter sensitivity by stating that the HVP activation threshold must be selected per instrument, which creates a material overfitting risk if thresholds are optimized on the evaluation sample.

## Falsification plan

1. Reconstruct the exact HVP calculation, activation threshold semantics, breakout arithmetic, reset logic, and reversal trigger from the public source before testing; fail the reconstruction stage if these cannot be made deterministic without invented rules.
2. For crypto, test liquid USDT spot and perpetual markets separately with point-in-time OHLC data and fixed candle boundaries.
3. Compare the HVP-triggered event-time range against controls: unconditional range breakout, fixed-clock pseudo-ORB, and randomized event bars matched on volatility.
4. Run ablations for breakout continuation only, reversal only, and the combined state machine to determine which component contributes any effect.
5. Freeze HVP thresholds out of sample; reject evidence that depends on selecting a different ex-post optimum for each evaluation asset.
6. Test multiple volatility regimes and bull/bear/sideways periods, with fees, spread, slippage and perpetual funding where applicable.
7. Treat the hypothesis as materially weakened if the HVP trigger does not improve net out-of-sample expectancy or risk-adjusted performance versus matched controls, or if any apparent edge disappears under plausible costs or modest threshold perturbations.
8. On failure, retain the result as negative evidence rather than promoting the strategy toward implementation.

## Crypto portability

`direct`

The cited TradingView source explicitly proposes HVP activation as a way to apply the opening-range concept to 24/7 crypto rather than depending on a traditional session open. That makes the mechanism directly crypto-targeted at the research-hypothesis level, not empirically validated alpha.

Crypto-specific risks include venue fragmentation, continuous trading, inconsistent candle boundaries across venues, spot/perpetual basis and funding, liquidation-driven volatility spikes, and different HVP distributions by asset and regime.

## Limitations

- `underspecified`: exact HVP lookback / percentile calculation and activation defaults.
- `underspecified`: exact arithmetic meaning of the described 100% breakout threshold.
- `underspecified`: same-bar versus close-confirmed entry and reversal semantics.
- `underspecified`: reference-range reset and re-arm behavior.
- `not independently reproduced`.
- `unproven`: no claim of crypto profitability or robustness is made here.
- Parameter-selection risk is unusually important because the author explicitly describes HVP activation threshold selection by instrument.

## Implementation status

No implementation in our research stack has been completed. No PyBroker, Nautilus, paper, testnet, or live verification is implied.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain links asserted from this GitHub-only Scout.

## Sources

- TradingView — kostastrovas, `HV Spike Strategy (HVP + OR Breakout + Reversal + TP/SL Modes)`, published 2025-10-26; reviewed 2026-09-16: https://www.tradingview.com/script/1oZNa7Oq-HV-Spike-Strategy-HVP-OR-Breakout-Reversal-TP-SL-Modes/
