---
schema: strategy-research-record-v1
title: TradingView Crypto Narrative Relative-Strength Rotation
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-07-13
sources:
  - https://www.tradingview.com/script/mM4KgUWk-Crypto-Narratives-Relative-Strength-V2/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Narrative Relative-Strength Rotation

## Provenance

Public TradingView open-source script `Crypto Narratives: Relative Strength V2` by Doobelaki. The page was published July 7, 2025 and shows an update dated July 13, 2025. Stable source URL: https://www.tradingview.com/script/mM4KgUWk-Crypto-Narratives-Relative-Strength-V2/ . Source reviewed 2026-09-20.

## Economic mechanism

### Source-reported

The source presents a narrative-relative-strength monitor. It groups major crypto assets into thematic narratives including AI, DeFi, Memes, Gaming, Layer 1, AI Agents, Storage/DePIN and RWA, calculates an aggregate RSI from five high-market-cap coins in each narrative, smooths the narrative series with a 14-period SMA, and compares narrative strength with BTC. It also displays rate of change and configurable overbought/oversold reference levels. The author states that constituent lists should be reviewed and updated as market-cap leadership changes.

### Research interpretation

A falsifiable hypothesis is that crypto capital rotates between narratives rather than moving uniformly across all altcoins. Persistent relative-strength leadership by a narrative basket versus BTC may therefore predict short-horizon continuation in that basket; conversely, an extreme narrative-strength reading that subsequently loses leadership may identify exhaustion rather than continuation.

The economically important component is the cross-sectional narrative aggregation, not RSI alone. Aggregation may suppress idiosyncratic token noise and expose common thematic flow. This interpretation is research-proposed; the source does not establish that the displayed rankings produce profitable trades.

## Signal

Source-supported construction:

- Group tokens into named crypto narratives.
- Use five high-market-cap coins per narrative; the author explicitly says these lists require manual updating as leadership changes.
- Compute RSI for constituents and aggregate them into a narrative-level RSI series.
- Plot a 14-period SMA of narrative RSI; the smoothing period is configurable.
- Compare narrative strength with BTC and display narrative rate of change.
- The source describes a daily reset and UTC+10 timing, with the reset hour editable.
- Configurable upper/lower levels provide overbought/oversold context and can trigger alerts.

The source does not specify a canonical portfolio entry, exit, holding period, rebalancing rule, weighting rule beyond the described narrative aggregation, transaction-cost model, or position sizing. Those elements are underspecified.

Research-proposed tests, not source rules:

1. Rank narrative baskets by point-in-time relative-strength change versus BTC and test top-minus-bottom continuation over fixed forward horizons.
2. Separately test whether crossing into an extreme strength region predicts continuation or subsequent reversal.
3. Test whether leadership persistence across consecutive observations is more informative than a one-bar rank.
4. Compare narrative aggregation against simple constituent-level momentum and BTC-relative momentum baselines.

## Required data

- Point-in-time token prices for every constituent used in each narrative.
- BTC benchmark price from a specified venue/feed.
- Explicit narrative membership history.
- Point-in-time market-cap information if the source's top-five-by-market-cap selection is to be reproduced without survivorship bias.
- Timestamp/timezone metadata sufficient to reproduce the stated daily reset convention.
- OHLCV is sufficient for RSI/price-relative-strength construction; no funding, OI, order-book, options or aggressor-side trade data is required by the source.

Missing-data and delisting treatment are not specified by the source.

## Execution assumptions

The source is an indicator rather than a complete executable strategy. Signal-to-order timing, next-bar versus same-bar execution, market/limit order choice, fees, spread, slippage, market impact, funding, borrow/short availability, leverage, partial fills and capacity are not specified.

Any backtest must form ranks only after all constituent bars needed for that timestamp are closed and available. A research implementation should use next-bar execution unless a stricter timestamp audit supports another convention. This is research-proposed.

## Evidence

### Source-reported

The TradingView page describes the indicator construction and intended relative-strength/narrative-monitoring use. No traceable Sharpe, CAGR, drawdown, win rate, t-statistic or other strategy-performance result is reported on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself exposes a major reproducibility risk: the five coins in each narrative must be manually checked and updated. Using today's leaders historically would introduce constituent survivorship and look-ahead bias. The page does not provide a historical membership dataset or a trading-performance study.

## Falsification plan

1. Build point-in-time narrative membership and market-cap snapshots; reject any result that relies on present-day constituents applied backward through history.
2. Compare `constituent momentum -> narrative aggregate -> narrative relative strength versus BTC -> leadership persistence` by ablation.
3. Test equal-weight aggregation against the source-reconstructable aggregation and simple market-cap-weighted baskets where point-in-time market caps exist.
4. Evaluate continuation and reversal as competing hypotheses after extreme readings rather than assuming overbought means reversal.
5. Use rolling/expanding out-of-sample evaluation across bull, bear, high-volatility and low-volatility regimes.
6. Apply realistic spot/perpetual fees, spread, slippage and funding where relevant; require the effect to survive costs and reasonable turnover constraints.
7. Run membership-label and timestamp placebo tests. Randomized narrative assignments should materially weaken any genuine narrative-rotation effect.
8. Test sensitivity to BTC venue/feed, RSI length, smoothing length, reset timezone, constituent count and rebalance frequency.
9. Reject or materially downgrade the hypothesis if narrative aggregation does not improve forward return separation or risk-adjusted performance over simple BTC-relative constituent momentum out of sample.

## Crypto portability

**direct** — the source itself is crypto-specific and explicitly organizes crypto assets into narratives against BTC.

Portability remains venue- and timestamp-sensitive. Crypto trades 24/7, narrative membership changes rapidly, token listings/delistings create survivorship risk, and different venues can produce small benchmark differences. A perpetual implementation would additionally require funding and contract-specific execution treatment not present in the source.

## Limitations

- Not independently reproduced.
- Canonical trading entry/exit/holding/sizing rules are underspecified.
- Historical narrative membership is a data gap.
- Historical point-in-time top-five market-cap selection is a data gap.
- Manual constituent maintenance creates severe survivorship/look-ahead risk if reconstructed naively.
- Narrative labels are partly subjective and may drift over time.
- RSI and SMA parameters can create multiple-testing risk if optimized after observing outcomes.
- The source provides an indicator, not verified alpha evidence.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received approval for implementation, Paper, Testnet or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted here. GitHub-only Scout operation does not inspect or fabricate Wiki links.

## Sources

1. Doobelaki. `Crypto Narratives: Relative Strength V2`. TradingView open-source script. Published 2025-07-07; page shows update 2025-07-13. https://www.tradingview.com/script/mM4KgUWk-Crypto-Narratives-Relative-Strength-V2/ . Reviewed 2026-09-20.
