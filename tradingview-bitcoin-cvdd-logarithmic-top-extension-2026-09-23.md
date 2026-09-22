---
schema: strategy-research-record-v1
title: TradingView Bitcoin CVDD Logarithmic Top Extension
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - tradingview
  - on-chain
  - cvdd
  - valuation
status: research-only
confidence: medium
source_as_of: 2025-01-03
sources:
  - https://www.tradingview.com/script/qxytt0NI-CVDD-Coin-Value-Days-Destroyed-for-Bitcoin-BTC-Logue/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bitcoin CVDD Logarithmic Top Extension

## Provenance

Public TradingView open-source indicator **“CVDD - Coin Value Days Destroyed for Bitcoin (BTC) [Logue]”** by `Da_Prof`, published 2024-03-05 and updated 2025-01-03. Stable source URL is preserved above. The reviewed TradingView page describes CVDD as the cumulative USD value of Coin Days Destroyed divided by market age, and adds a time-varying extension intended to identify Bitcoin cycle tops.

Source as-of date: 2025-01-03, the latest update date visible on the reviewed TradingView page.

## Economic mechanism

### Source-reported

The source states that ordinary CVDD is generally used as a Bitcoin bottom model. It extends CVDD upward for top detection because the apparent “strength” of Bitcoin cycle tops has decreased across cycles. The extension is modeled in log space as a linear function of time (`log extension = slope * time + intercept`); price above the extension is treated as overvalued. The source also shifts CVDD upward by a default 120% for its bottom treatment. Slope, intercept, and bottom-shift parameters are user-adjustable.

### Research interpretation

The materially distinct hypothesis is not the already-known CVDD macro-floor thesis. It is that **the valuation premium of cycle tops over CVDD decays systematically through time, so a logarithmically time-decaying CVDD extension contains incremental information about future medium/long-horizon Bitcoin downside beyond raw CVDD multiples and ordinary price trend/volatility controls**.

This is a falsifiable secular-compression hypothesis. It may instead be an ex-post curve fit to a very small number of Bitcoin cycles; that is the principal competing explanation.

## Signal

### Source-supported construction

- Base state variable: Bitcoin CVDD.
- Top boundary: a CVDD extension whose log multiplier is represented as a linear function of time using adjustable slope and intercept.
- Source-reported top condition: Bitcoin price above the CVDD extension indicates overvaluation / a potential cycle top.
- Bottom treatment: CVDD is shifted upward by a default 120%; this record does **not** treat that bottom rule as the primary hypothesis because the repository already contains a dedicated CVDD floor record.
- The reviewed page does not expose, in its descriptive text, fixed slope/intercept values, exact signal formation timestamp, complete exit rule, holding period, re-entry rule, sizing rule, or order timing. These remain `underspecified` and must not be invented.

### Research-proposed operationalization

For falsification only, estimate any slope/intercept strictly inside each training window, freeze them before the next test window, and evaluate the point-in-time distance of price from the resulting CVDD extension. Test both threshold crossing and continuous distance-to-extension formulations. Any horizon, threshold, exit, or sizing used in that experiment is `research-proposed`, not source-reported.

## Required data

- Bitcoin spot/reference price with explicit timestamp and candle boundary.
- Point-in-time CVDD or sufficient UTXO/Coin Days Destroyed history to reconstruct CVDD without future information.
- Bitcoin network age / calendar time required by the CVDD and time-decay constructions.
- Historical data vintages where available to test whether provider revisions alter signals.
- A sufficiently long sample spanning multiple Bitcoin cycles; the effective number of independent macro-cycle observations remains small.

## Execution assumptions

The source does not specify market versus limit orders, same-bar versus next-bar execution, fees, spread, slippage, leverage, margin, sizing, latency, partial fills, or a complete exit lifecycle.

For research testing, execution should therefore be conservative and explicitly `research-proposed`: form the signal only after all required point-in-time inputs are available and execute no earlier than the next eligible bar. Cost assumptions must be reported separately rather than attributed to the source.

## Evidence

### Source-reported

The TradingView author states that ordinary CVDD is normally used for bottoms and that the logarithmic extension is intended to detect tops, motivated by declining top strength across Bitcoin cycles. The page describes price above the extension as overvalued. No independently verified Sharpe, CAGR, drawdown, hit rate, or statistical significance is reported on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The logarithmic time trend is explicitly motivated by past cycles, creating substantial curve-fitting risk.
- Bitcoin has only a small number of completed macro cycles, so slope/intercept estimation has very low effective sample size.
- A deterministic calendar-time decay can confuse genuine structural valuation change with a fitted trend.
- CVDD itself inherits point-in-time on-chain-data, entity-adjustment, and provider-vintage risks.
- The source does not provide a complete trading lifecycle in the reviewed description.

## Falsification plan

1. **Incremental-information test:** compare the log-time CVDD extension against raw `price / CVDD`, log `price / CVDD`, momentum, drawdown, realized volatility, and time-since-halving controls. Reject the extension layer if it adds no leakage-safe out-of-sample information.
2. **Walk-forward estimation:** fit slope/intercept only on information available before each test period. Never fit the secular decay on the full history and then score earlier cycles.
3. **Leave-one-cycle-out stress:** estimate on prior eligible cycles and test the held-out later cycle. Treat failure on held-out cycles as evidence against structural decay.
4. **Parameter-neighborhood test:** perturb slope/intercept around training estimates. If apparent performance depends on a narrow fitted pair, classify the result as unstable.
5. **Calendar-trend placebo:** compare the extension with simpler deterministic controls such as log-time and days-since-halving. The CVDD interaction must outperform those controls to justify its complexity.
6. **Boundary ablation:** test continuous distance-to-extension versus discrete crossing. Reject a threshold-specific claim if nearby thresholds reverse the result.
7. **Data-vintage test:** where historical vintages exist, reproduce signals using only values available at each timestamp; reject results that depend materially on later revisions.
8. **Cost/OOS test:** any research-proposed tradable implementation must survive realistic fees/slippage and a genuinely untouched test period. Failure means no advancement of this hypothesis.

## Crypto portability

`direct` for Bitcoin because the source is explicitly a Bitcoin on-chain valuation model. Portability to non-UTXO or materially different crypto networks is `unproven`; CVDD depends on coin-age destruction semantics and cannot be assumed equivalent across account-based chains.

## Limitations

- `not independently reproduced`
- `underspecified`: exact source slope/intercept values and complete trade lifecycle are not established by the reviewed descriptive text.
- `data gap`: point-in-time revision behavior of any underlying CVDD provider must be verified before backtesting.
- Very small effective macro-cycle sample.
- High risk that the secular log extension is retrospective curve fitting rather than durable alpha.

## Implementation status

No implementation or Qlib full-backtest validation has been completed for this record. This Scout performed research normalization only.

## Adoption boundary

Research material only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

- `[[bitcoin-onchain-cumulative-value-days-destroyed-cvdd-floor-2026-09-01]]` — existing CVDD macro-floor hypothesis; the present record isolates the distinct logarithmic cycle-top extension.
- `[[bitcoin-onchain-market-cap-to-thermocap-ratio-2026-09-01]]` — alternative long-horizon miner/issuance valuation anchor.

## Sources

- TradingView, Da_Prof, “CVDD - Coin Value Days Destroyed for Bitcoin (BTC) [Logue]”, published 2024-03-05, updated 2025-01-03: https://www.tradingview.com/script/qxytt0NI-CVDD-Coin-Value-Days-Destroyed-for-Bitcoin-BTC-Logue/
