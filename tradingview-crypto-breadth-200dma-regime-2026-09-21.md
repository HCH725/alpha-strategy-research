---
schema: strategy-research-record-v1
title: "Crypto 200DMA Breadth Regime and Participation Persistence"
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/uDzcYHiM-Crypto-Breadth-Above-200DMA/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto 200DMA Breadth Regime and Participation Persistence

## Provenance

- Public TradingView open-source script: `Crypto Breadth % Above 200DMA`.
- Author / page identity: `andrej87kolar`.
- Publication date shown by TradingView: 2026-03-12.
- Stable public URL: https://www.tradingview.com/script/uDzcYHiM-Crypto-Breadth-Above-200DMA/
- Source reviewed as of 2026-09-21.

## Economic mechanism

### Source-reported

The source measures crypto-market breadth as the percentage of ten selected cryptocurrencies trading above their 200-day simple moving average. The listed basket is BTC, ETH, BNB, SOL, XRP, ADA, DOGE, DOT, LINK, and LTC. It describes values above 70% as strong breadth and values below 40% as weak breadth, intended to characterize broad market strength rather than the condition of one coin.

The source does not report a trading backtest, causal mechanism, Sharpe ratio, return statistic, or execution rule.

### Research interpretation

A falsifiable hypothesis is that broad participation contains information beyond BTC's own trend. If many large crypto assets independently remain above slow trend, the market may be in a persistent risk-on regime with broader capital participation; conversely, weak breadth may indicate a fragile or risk-off regime.

A second, competing hypothesis is that very high or very low breadth is merely a contemporaneous description of an already mature move and has no incremental forward-return information after controlling for BTC trend, market return, and realized volatility.

The alpha question is therefore not whether breadth describes the present market, but whether breadth level, breadth change, or breadth/price disagreement predicts subsequent returns or regime persistence out of sample.

## Signal

Source-specified construction:

1. For each of the ten named cryptocurrencies, compute a 200-day SMA.
2. At each observation, classify the asset as above or not above its 200DMA.
3. Breadth = 100 × (number of selected assets above their 200DMA / number of selected assets).
4. The source labels breadth above 70% as strong and below 40% as weak.

Signal formation timing is not explicitly specified beyond the indicator's bar calculation. A leakage-safe implementation should use only fully closed daily bars and make any trade decision no earlier than the next executable timestamp; this is `research-proposed`.

Potential operationalizations for testing, all `research-proposed` rather than source-reported:

- regime persistence: test whether high breadth predicts positive subsequent market/BTC returns relative to a BTC-trend-only baseline;
- deterioration: test whether falling breadth while BTC remains above its own 200DMA predicts weaker subsequent returns;
- recovery: test whether breadth crossing upward from weak toward broad participation precedes improved forward returns;
- extreme-state reversal: separately test whether very high/low breadth predicts reversal rather than continuation.

Entry, exit, holding period, re-entry, sizing, short rules, and portfolio construction are underspecified by the source and must not be inferred as source rules.

## Required data

- Daily point-in-time OHLC close data for BTC, ETH, BNB, SOL, XRP, ADA, DOGE, DOT, LINK, and LTC.
- A fixed timestamp/candle boundary across assets, preferably a single UTC daily close for research comparability (`research-proposed`).
- At least 200 prior daily observations per eligible asset before its SMA becomes available.
- Point-in-time asset availability and listing history are required to avoid silently filling pre-listing periods.
- For a broader or dynamic-universe replication, historical constituent selection must be point-in-time; today's winners must not be retroactively substituted into history.
- Fees, spread, funding, and execution data are required if the breadth state is converted into a tradable portfolio rather than used only as a regime feature.

## Execution assumptions

The source is an indicator and does not specify execution.

For research, any strategy derived from the signal should execute no earlier than the bar after the breadth state is observable (`research-proposed`). Market/limit order choice, fees, spread, slippage, funding, leverage, borrow, capacity, partial fills, and rebalance cadence are all underspecified.

If breadth is used only as a gate on BTC or a liquid crypto basket, the execution model for that underlying strategy must be evaluated separately from the predictive value of breadth.

## Evidence

### Source-reported

The source reports the construction and interpretation thresholds (above 70% strong breadth; below 40% weak breadth) but provides no source-reported profitability, Sharpe, CAGR, drawdown, win rate, or formal predictive test.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No formal negative empirical result is reported by the reviewed source; absence is not evidence of no negative result. The fixed ten-coin basket creates an obvious survivorship and representativeness risk, and the 200DMA makes the signal structurally slow.

## Falsification plan

1. **Incremental-information test.** Compare BTC trend alone (BTC above/below its 200DMA) against BTC trend + breadth level, breadth change, and breadth/price divergence. Reject the breadth hypothesis if it does not improve leakage-safe out-of-sample prediction or net strategy performance after costs.
2. **Threshold ablation.** Test the source's 70%/40% interpretation against continuous breadth and nearby thresholds. Treat performance concentrated only at the exact published cutoffs as fragile.
3. **Constituent ablation.** Perform leave-one-asset-out tests and compare equal-count breadth with liquidity-weighted alternatives. Reject a claimed market-wide mechanism if one or two assets dominate the result.
4. **Survivorship audit.** Repeat with a point-in-time investable universe where feasible. If the fixed current-style basket materially outperforms the point-in-time construction, classify the original result as survivorship-sensitive.
5. **Regime controls.** Control for BTC return/trend, total-market return, realized volatility, and broad risk-on/risk-off states. Reject incremental alpha if breadth is only a repackaging of those variables.
6. **Competing outcomes.** Test continuation and reversal at both high and low breadth rather than choosing direction after observing results.
7. **Horizon robustness.** Pre-specify multiple forward horizons (for example 1, 5, 20, and 60 daily bars) and require directionally coherent out-of-sample behavior rather than a single favorable horizon (`research-proposed`).
8. **Cost test.** If translated into a rotating multi-asset portfolio, include realistic fees, spread, slippage, funding, and turnover. Reject implementation if gross predictability does not survive costs.

## Crypto portability

`direct`

The source is explicitly constructed from cryptocurrency assets. Important portability risks remain: crypto trades 24/7, daily boundaries differ across data providers, venues may have different price histories, constituents have different listing dates, and perpetual execution adds funding and basis effects absent from a spot-close breadth calculation.

## Limitations

- `underspecified`: no source-defined entry, exit, holding period, sizing, or execution model.
- `not independently reproduced`: no internal replication was performed in this Scout cycle.
- `data gap`: the source does not establish point-in-time constituent methodology.
- `unproven`: descriptive breadth is not itself evidence of forward alpha.
- Fixed ten-asset composition can create survivorship, selection, and representativeness bias.
- The 200-day lookback is slow and may lag abrupt crypto regime transitions.
- Cross-asset daily-bar synchronization must be explicit to prevent timestamp mismatch.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation has occurred.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Wiki record is asserted here; GitHub-only Scout operation does not query Hermes Wiki Brain.

## Sources

- andrej87kolar, `Crypto Breadth % Above 200DMA`, TradingView, public open-source script, published 2026-03-12, reviewed 2026-09-21: https://www.tradingview.com/script/uDzcYHiM-Crypto-Breadth-Above-200DMA/
