---
schema: strategy-research-record-v1
title: TradingView ATR Exhaustion + Volume Spike Pivot Reversal
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-25
sources:
  - https://www.tradingview.com/script/8ltrS3Yg-ATR-Exhaustion-Volume-Spike-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView ATR Exhaustion + Volume Spike Pivot Reversal

## Provenance

- **Source type:** public TradingView open-source strategy page.
- **Title:** `ATR Exhaustion & Volume Spike Strategy`.
- **Author/page identity:** `MyStrategyHub`.
- **Stable URL:** https://www.tradingview.com/script/8ltrS3Yg-ATR-Exhaustion-Volume-Spike-Strategy/
- **TradingView page date label:** `Apr 7`; the reviewed public page does not expose the year unambiguously in the captured text.
- **Source inspected as of:** 2026-09-25.
- The page is marked **OPEN-SOURCE SCRIPT**. This record normalizes the public description and does not redistribute Pine source code.

## Economic mechanism

### Source-reported

The source describes a reversal strategy that combines three conditions: a historical pivot/reaction level, a price move extended relative to ATR, and a volume spike. Its stated thesis is that an overextended move reaching a prior supply/demand reaction area with unusually high participation may represent exhaustion and reverse.

### Research interpretation

The falsifiable hypothesis is that **conditional on price reaching a prior pivot zone after an unusually large ATR-scaled displacement, a contemporaneous volume surge identifies terminal participation/exhaustion rather than continuation, increasing subsequent reversal probability**.

Component roles:

- **Location/regime:** prior pivot/reaction level.
- **Primary exhaustion condition:** price displacement greater than an ATR-scaled threshold.
- **Participation confirmation:** volume materially above its recent average.
- **Risk logic:** stop near the pivot/local candle extreme and fixed reward-to-risk target; these are not treated as independent alpha signals.

The economic interpretation is plausible but ambiguous: high volume at an extended pivot can also mark informed breakout participation. Continuation versus reversal is therefore a central falsification test rather than an assumed fact.

## Signal

Source-reported logic:

- Detect historical pivot/reaction levels.
- Identify an overextended price move relative to ATR; the public description gives an example threshold of **greater than 2× ATR**.
- Require a volume surge; the public description gives an example of **1.5× average volume**.
- Enter in the reversal direction when the exhaustion condition occurs at a major pivot/supply-demand zone with the volume confirmation.
- The source states that the stop is placed at the recent pivot level or local candle extreme.
- The source states a fixed **1:2 risk-to-reward** framework and **0.5% equity risk per trade**.
- The source says **2H is preferred for stability**, while 5M/15M require tighter ATR tuning.

Underspecified in the reviewed public description:

- exact pivot algorithm and pivot lookback;
- exact ATR period and whether the 2× threshold measures candle range, distance from a reference price, or another displacement;
- exact volume-average lookback;
- exact bullish/bearish reversal trigger and order timing;
- precedence between pivot-level and candle-extreme stop choices;
- re-entry behavior and simultaneous-signal handling.

No missing rule is inferred here. Any future completion of these gaps must be labelled `research-proposed`.

## Required data

- OHLCV bars.
- Derived ATR and rolling average volume.
- Sufficient historical OHLC data to construct pivot/reaction levels causally.
- Source-preferred timeframe: 2H; lower-timeframe 5M/15M variants are mentioned but require retuning.
- Instrument/universe, venue, market type, exchange timezone, and session convention are not specified by the reviewed source.
- Point-in-time requirement: pivots used in a test must be confirmed only when they would have become observable; no future bars may leak into pivot identification.

## Execution assumptions

The source specifies risk sizing of 0.5% of equity per trade, a stop at a recent pivot or local candle extreme, and a 1:2 reward-to-risk target.

The reviewed public description does **not** specify:

- same-bar versus next-bar execution;
- market versus limit orders;
- commission/fees;
- bid-ask spread;
- slippage or market impact;
- latency or partial fills;
- leverage/margin;
- short borrow;
- funding for perpetual futures.

These remain execution-model gaps.

## Evidence

### Source-reported

The source presents the setup as targeting high-probability reversals and recommends 2H for greater stability, but the reviewed public description does not provide a sufficiently documented sample, benchmark, cost model, or traceable performance statistic suitable for treating profitability as evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative result was identified in the reviewed source. Mechanistically, the main contrary hypothesis is important: an ATR-extreme move accompanied by a volume spike at a prior pivot may be a genuine high-participation breakout rather than exhaustion. Absence of a reported negative result is not evidence that this failure mode is absent.

## Falsification plan

Research-proposed tests:

1. **Reversal versus continuation control:** compare forward returns after pivot + ATR-extreme + volume-spike events in the reversal direction and in the direction of the incoming move. Reject the exhaustion interpretation if continuation is equal or stronger after realistic costs.
2. **Component ablation:** test pivot-only, ATR-extreme-only, volume-spike-only, pivot+ATR, pivot+volume, ATR+volume, and the full three-component rule. The full rule should add out-of-sample information beyond simpler variants.
3. **Threshold robustness:** evaluate neighborhoods around the source examples rather than optimizing one point, including ATR multiples around 2× and volume multiples around 1.5×.
4. **Pivot causality audit:** use only pivots confirmed with information available at signal time. Reject any result that depends materially on future-bar pivot confirmation.
5. **Regime split:** test trending, ranging, high-volatility, and low-volatility periods separately; exhaustion should not be accepted if apparent edge is confined to one narrow regime without a defensible explanation.
6. **Execution sensitivity:** evaluate next-bar execution with explicit fees, spread, and slippage. Reject if modest realistic friction removes the effect.
7. **Out-of-sample requirement:** freeze signal construction and thresholds before evaluating a held-out period and additional instruments.

## Crypto portability

**adapted**

The source says the strategy is based on price action, pivots, volatility, and volume, all of which can be constructed for liquid crypto markets, but the reviewed page does not establish crypto-specific empirical evidence.

Crypto adaptation must distinguish spot from perpetual futures and account for 24/7 candle boundaries, venue fragmentation, exchange-specific volume, funding, mark/index prices, liquidation-driven volume spikes, leverage, and materially different weekend liquidity. Aggregate or venue-specific volume choice may materially change the signal.

## Limitations

- Exact pivot construction is underspecified.
- ATR period and exact exhaustion-distance calculation are underspecified.
- Volume-average lookback is underspecified.
- Entry/order timing is underspecified.
- No independently reproduced evidence.
- No source-documented realistic transaction-cost model was identified.
- Volume spikes can plausibly indicate continuation rather than exhaustion.
- The source's 2× ATR and 1.5× volume values should be treated as source examples, not validated optima.
- Crypto portability is unproven.

## Implementation status

Not implemented in the research stack. No Qlib full backtest or independent reproduction was performed in this Scout cycle.

## Adoption boundary

Research-only. Presence in this repository does not mean this record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable or validated alpha, or received approval for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain page was resolved in this GitHub-only cycle; no Wiki link is fabricated.

## Sources

- TradingView — MyStrategyHub, **ATR Exhaustion & Volume Spike Strategy**: https://www.tradingview.com/script/8ltrS3Yg-ATR-Exhaustion-Volume-Spike-Strategy/ (reviewed 2026-09-25).
