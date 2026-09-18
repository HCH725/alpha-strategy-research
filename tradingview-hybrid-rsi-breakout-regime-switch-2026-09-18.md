---
schema: strategy-research-record-v1
title: "TradingView Hybrid RSI Mean-Reversion / EMA200-ADX Breakout Regime Switch"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/aAszLZWi-Hybrid-RSI-Breakout-Dashboard/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Hybrid RSI Mean-Reversion / EMA200-ADX Breakout Regime Switch

## Provenance

- Public TradingView open-source strategy: **Hybrid: RSI + Breakout + Dashboard**.
- Author/page identity: `RugSurvivor`.
- Stable public URL: https://www.tradingview.com/script/aAszLZWi-Hybrid-RSI-Breakout-Dashboard/
- TradingView publication date: 2025-05-11.
- Source reviewed/as-of: 2026-09-18.
- GitHub dedup on current `main` found no record containing canonical TradingView script ID `aAszLZWi`.

## Economic mechanism

### Source-reported

The author describes an adaptive system that changes trading behavior with market regime. In a ranging regime it uses RSI extremes as a mean-reversion rule: buy when RSI is below 30 and sell when RSI is above 70. In a trending regime it instead trades momentum breakouts only in the direction of the 200-EMA bias, with ADX used to confirm trend strength. A trailing stop is used for risk management.

### Research interpretation

The falsifiable hypothesis is that **regime-conditioned model selection can outperform either unconditional mean reversion or unconditional breakout trading**. The economic roles are distinct:

- **Range mode:** RSI extremes proxy short-horizon overextension and potential mean reversion.
- **Trend mode:** EMA200 supplies directional regime bias; ADX attempts to distinguish persistent directional conditions; the breakout trigger seeks continuation rather than reversal.
- **Risk / exit:** trailing stop is risk management, not treated as alpha.

The key research question is therefore not whether RSI, EMA or ADX works individually, but whether the regime switch correctly assigns opposite trading behaviors to different market states without introducing look-ahead or excessive switching noise.

## Signal

### Source-specified logic

- **Ranging regime:** buy when RSI < 30; sell when RSI > 70.
- **Trending regime:** enter momentum breakouts only in the direction of the 200-EMA bias, with ADX confirming trend strength.
- Source describes a trailing stop for exits/risk control.
- Source says the system is optimized for BTC, ETH and SOL on 1-hour through 1-day charts.

### Underspecified items

The public descriptive text reviewed for this record does **not** unambiguously state:

- the exact Boolean rule that classifies a bar as `ranging` versus `trending`;
- ADX lookback and threshold;
- RSI lookback;
- the exact breakout level/lookback and whether breakout is close-based or intrabar;
- exact EMA boundary semantics;
- trailing-stop distance/calculation;
- position sizing;
- signal-to-order timing, re-entry or cooldown behavior.

These details must be resolved from the public Pine source before implementation. No missing parameter is invented here.

## Required data

- Crypto OHLCV for BTC, ETH and/or SOL.
- Source-described chart horizons: 1h through 1D.
- Sufficient history to compute EMA200, RSI, ADX and the source's breakout construction.
- Timestamped bars with point-in-time indicator formation; no future regime labels may be used.
- Venue and market type are not established by the descriptive source material and remain a data/provenance gap.

## Execution assumptions

The source description reviewed here does not establish market versus limit execution, same-bar versus next-bar fills, fees, spread, slippage, impact, latency, partial fills, leverage, margin, funding, or borrow/shorting mechanics. These must be modeled explicitly in any later test.

Trailing-stop mechanics are source-reported as present but their exact distance and update/fill semantics are underspecified in the reviewed descriptive material.

## Evidence

### Source-reported

The TradingView page says the strategy is optimized for BTC, ETH and SOL on 1h–1D charts and was back-tested from 2017 onward. The reviewed description does not provide a source-traceable Sharpe, CAGR, maximum drawdown, profit factor, or other precise performance statistic, so none is promoted here as evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. Mechanistically, regime misclassification, indicator lag, whipsaw near regime boundaries, and data-mined mode/threshold choices are material risks that require testing rather than being assumed away.

## Falsification plan

1. Reconstruct the exact public Pine rules, especially the range/trend classifier, breakout definition, ADX threshold and trailing-stop semantics, without adding unstated logic.
2. Use point-in-time bar formation and chronological train/OOS splits across BTC, ETH and SOL and across multiple market regimes.
3. Compare the hybrid against two controls using the same execution model: unconditional RSI mean reversion and unconditional trend/breakout logic.
4. Ablate EMA200 direction and ADX trend-strength confirmation separately.
5. Measure regime-switch turnover and performance around regime boundaries; reject any implementation that relies on future information to identify regime.
6. Apply realistic fees, spread and slippage; add funding if tested on perpetuals.
7. Treat the hypothesis as weakened or rejected if the hybrid fails to outperform both simpler controls OOS after costs, if the benefit disappears under small threshold perturbations, or if results are concentrated in one asset or historical regime.

## Crypto portability

**direct** as a research hypothesis because the source explicitly targets BTC, ETH and SOL.

Portability across crypto venues and spot/perpetual markets remains unproven. Perpetuals add funding and mark/index mechanics; venue fragmentation affects OHLCV; 24/7 candle boundaries can alter EMA, RSI, ADX and breakout states.

## Limitations

- Not independently reproduced.
- Regime-classification rule is underspecified in the reviewed descriptive text.
- Breakout construction, ADX/RSI parameters and trailing-stop mechanics are underspecified.
- Source optimization creates material overfitting / multiple-testing risk.
- No independently verified performance evidence.
- Execution and venue assumptions are unspecified.

## Implementation status

Not implemented in our research stack. No backtest or runtime code change was performed by this Scout.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved implementation, paper trading, testnet trading or live trading.

## Related Wiki records

No stable related Wiki record is asserted here.

## Sources

- TradingView — RugSurvivor, **Hybrid: RSI + Breakout + Dashboard**: https://www.tradingview.com/script/aAszLZWi-Hybrid-RSI-Breakout-Dashboard/ (public open-source strategy; published 2025-05-11; reviewed 2026-09-18).
