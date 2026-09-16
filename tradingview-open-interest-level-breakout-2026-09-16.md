---
schema: strategy-research-record-v1
title: TradingView Open-Interest Level Breakout
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
  - https://www.tradingview.com/script/KYhokebq-Wunder-OI-breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Open-Interest Level Breakout

## Provenance

Public TradingView strategy page: `Wunder OI breakout`, published by WunderTrading and updated 2024-04-12. Stable source URL: https://www.tradingview.com/script/KYhokebq-Wunder-OI-breakout/. Source reviewed as of 2026-09-16. The Pine source is protected; this record uses only the public strategy description and does not reproduce source code.

## Economic mechanism

### Source-reported

The author describes open interest (OI) as the number of active market positions and proposes trading sharp increases / breakouts in OI levels. The strategy constructs OI levels from highs and lows over a configurable period and uses a break of those levels as the entry concept. The period and required percentage change in OI are configurable by pair and timeframe.

### Research interpretation

The falsifiable hypothesis is that an unusually large expansion of derivatives positioning, measured by OI breaking a recent range by a material percentage, contains information about a transition from balanced positioning into a higher-participation regime. This is materially different from a price-only breakout: the predictive variable is derivatives positioning rather than price resistance/support.

Direction mapping is underspecified in the public description. An OI increase alone does not reveal whether newly opened positioning is net directionally bullish or bearish because every derivatives contract has both a long and a short side. Therefore any directional mapping from OI breakout to price direction requires additional research rather than being treated as source-reported fact.

## Signal

Source-reported normalized rule:

- Formation timing: evaluated from OI observations on the chart; exact intrabar versus completed-bar timing is underspecified.
- Lookback: configurable period used to construct recent OI high/low levels; exact default period is not stated in the reviewed public description.
- Trigger: break of the constructed OI level, with a configurable percentage-change condition in OI.
- Long entry: underspecified in the public description.
- Short entry: underspecified in the public description.
- Exit: underspecified in the public description beyond reference to a configurable Stop Loss used by the sizing feature.
- Holding period: underspecified.
- Re-entry/reset behavior: underspecified.
- Position sizing: optional portfolio-risk sizing calculates a dollar entry amount from configured portfolio risk percentage and Stop Loss distance. This is risk management, not the alpha signal.

Research-proposed operationalization for later testing, not source-reported: treat the OI breakout itself first as a regime/event signal and separately test directional conditioning using contemporaneous price return, price breakout direction, or funding/basis state. This avoids assuming that rising OI has a fixed directional meaning.

## Required data

- Crypto derivatives instrument with reliable point-in-time open-interest history.
- Timestamped OI series at the selected research timeframe.
- OHLC data if a later directional price-conditioning variant is tested.
- Exact venue and contract specification must be retained because OI units and aggregation differ across venues/contracts.
- Point-in-time requirement: only OI observations available at the signal timestamp may enter the rolling high/low and percentage-change calculation.
- Missing or revised OI observations must not be silently forward-filled across material data gaps.

## Execution assumptions

The public description does not fully specify signal-to-order timing, order type, fill model, fees, spread, slippage, funding, leverage, margin, latency, partial fills, or failure handling. These are underspecified and must be defined before any formal backtest.

The source describes a portfolio-risk sizing option tied to Stop Loss distance and notes that dollar-volume sizing can make TradingView backtest net-profit/drawdown displays incorrect because TradingView calculates backtest volume in contracts; it recommends contract-volume mode for correct backtest accounting. This is a source-reported implementation/accounting caveat, not independent evidence of profitability.

## Evidence

### Source-reported

The TradingView page describes the OI-level breakout concept and configurable OI period / percentage-change threshold. It does not provide a sufficiently traceable performance sample or quantitative profitability statistic in the reviewed public description, so no performance claim is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative empirical evidence was identified in the reviewed source. Mechanistically, OI expansion is directionally ambiguous without another conditioning variable; this is a research limitation rather than source-reported negative evidence. Absence of cited negative results is not evidence that none exist.

## Falsification plan

Test the hypothesis on point-in-time crypto perpetual/futures OI with venue-specific data and no look-ahead. Compare OI-break events against matched non-break periods and a price-only breakout baseline. Evaluate multiple predeclared OI lookbacks and thresholds without selecting parameters on the full sample.

Ablate directional conditioning: OI-only event, OI + contemporaneous price direction, OI + price breakout, and OI + funding/basis state. Measure forward returns, hit rate, turnover, drawdown and cost-adjusted expectancy across bull, bear, high-volatility and low-volatility regimes and across multiple liquid contracts. Require out-of-sample persistence after fees, spread, slippage and funding.

The thesis is materially weakened if OI-break events show no stable incremental predictive information versus matched controls / price-only baselines, if sign reverses unpredictably across venues or regimes, or if any apparent edge disappears under realistic costs and out-of-sample testing. Failure should result in rejection or reformulation, not parameter expansion until a pass appears.

## Crypto portability

direct

The source is explicitly a crypto-oriented strategy and its core input, derivatives open interest, is native to crypto futures/perpetual markets. Portability still depends on venue-specific OI definitions, contract denomination, aggregation, funding, fragmented liquidity and timestamp/candle boundaries. OI from different exchanges should not be combined without explicit normalization.

## Limitations

- Protected Pine source prevents direct inspection of implementation details.
- Exact OI lookback default and percentage threshold default are underspecified in the reviewed description.
- Directional long/short mapping is underspecified.
- Exit, holding period and re-entry/reset rules are underspecified.
- OI increase does not identify which side is informed or dominant.
- Venue/contract OI definitions can differ materially.
- Not independently reproduced.

## Implementation status

No implementation in the research stack has been completed. No PyBroker, Nautilus, paper, testnet or live verification is implied.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — WunderTrading, `Wunder OI breakout`, updated 2024-04-12, reviewed 2026-09-16: https://www.tradingview.com/script/KYhokebq-Wunder-OI-breakout/
