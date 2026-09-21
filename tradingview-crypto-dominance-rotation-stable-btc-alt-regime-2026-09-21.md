---
schema: strategy-research-record-v1
title: Crypto Dominance Rotation — Stablecoin, BTC and Altcoin Regime Alpha
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
  - https://www.tradingview.com/script/BxfHcFQK-FlowTrinity-Crypto-Dominance-Rotation-Index/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Dominance Rotation — Stablecoin, BTC and Altcoin Regime Alpha

## Provenance

Public TradingView open-source indicator **FlowTrinity - Crypto Dominance Rotation Index**, author/page identity `sanbangaje`, published 2025-12-09. Stable public URL: https://www.tradingview.com/script/BxfHcFQK-FlowTrinity-Crypto-Dominance-Rotation-Index/ . Source reviewed as of 2026-09-21.

GitHub deduplication was performed against current `main` before capture by canonical TradingView source identity and normalized signal family. No record for this canonical source was found. Existing stablecoin-dominance research in the repository focuses on stablecoin share as a risk-regime variable; this record is materially distinct because its core hypothesis is **relative capital rotation among stablecoins, BTC and the residual altcoin segment**, with a separate total-market expansion/contraction confirmation term.

## Economic mechanism

### Source-reported

The source decomposes crypto market structure into three dominance-flow regimes: BTC dominance, stablecoin dominance and altcoin dominance. It describes high stablecoin dominance as hedging / sidelined capital, rising altcoin dominance as broad speculative expansion, and BTC dominance as a way to distinguish Bitcoin-led from altcoin-led phases. A fourth normalized histogram measures total-market-cap change minus BTC-plus-stablecoin market-cap change, intended to expose altcoin expansion or retreat not visible in dominance alone.

### Research interpretation

The falsifiable hypothesis is that **joint changes in where crypto market capitalization is concentrated contain incremental information about subsequent relative returns among BTC, altcoins and defensive stablecoin positioning**.

This is a rotation hypothesis rather than a claim that any single dominance series predicts absolute returns. The proposed mechanism is that capital first reallocates between defensive stablecoin balances, BTC concentration and broader altcoin participation; persistence or reversal in those relative flows may forecast the next segment leadership regime.

Two competing hypotheses must be tested:

1. **Rotation continuation:** falling stablecoin dominance with rising altcoin dominance and positive residual market-cap expansion predicts continued altcoin relative strength; rising BTC dominance with weak alt participation predicts BTC relative strength.
2. **Rotation exhaustion:** extreme standardized dominance states predict reversal as positioning becomes crowded rather than continuation.

The source's total-minus-BTC-minus-stable histogram is treated as a confirmation component whose incremental value must survive ablation.

## Signal

Source-reported construction:

- Stablecoin dominance component: combined USDT + USDC share of market dominance.
- Altcoin dominance component: total crypto market capitalization minus BTC and stablecoin capitalization, expressed as a relative flow / dominance measure.
- BTC dominance component: normalized BTC dominance.
- Structural confirmation histogram: normalized total-market-cap change minus BTC-plus-stablecoin market-cap change.
- The source states that flow components use SMA plus standard-deviation scaling with **lookback 7 / smoothing 7**.
- Source interpretation includes high/low oscillator states and relative movement among components to identify rotation regimes.

The public description does not provide a complete executable strategy: exact oscillator transformation details, threshold values for actionable extremes, formation timestamp, entry/exit rules, holding period, re-entry, sizing and portfolio weights are **underspecified**.

`research-proposed` operationalization for falsification only:

- Use completed daily bars initially; execute no earlier than the next bar.
- Construct point-in-time standardized changes for stablecoin, BTC and residual-alt shares without using future constituent information.
- Define relative-return targets separately: alt basket minus BTC, BTC minus alt basket, and BTC absolute return. Do not infer one target after observing results.
- Test continuous rotation scores before testing thresholds.
- If thresholds are later tested, select them only inside training windows and freeze them for OOS evaluation.
- Treat the residual-market expansion histogram as optional confirmation and require incremental OOS value.

## Required data

- Point-in-time total crypto market capitalization.
- Point-in-time BTC market capitalization / dominance.
- Point-in-time USDT and USDC market capitalization / dominance matching the source construction where reproducible.
- Point-in-time residual altcoin market capitalization derived consistently from the above.
- BTC OHLCV.
- Survivorship-safe altcoin universe and constituent history for any tradable alt basket.
- UTC timestamp / candle-boundary convention.
- Historical TradingView CRYPTOCAP methodology and availability metadata where required.

The source does not specify an executable exchange or instrument universe because it is a market-structure indicator rather than a trading strategy.

## Execution assumptions

The source does not specify signal-to-order timing, order type, fill model, fees, spread, slippage, impact, funding, leverage, borrow, partial fills or failures.

Any later implementation must declare these independently as `research-proposed`. A BTC-versus-alt relative-value implementation must also define the alt basket point-in-time, rebalance schedule, liquidity screen and turnover. Perpetual implementation requires funding and mark/index-price handling; spot short legs require borrow availability and cost.

## Evidence

### Source-reported

The source describes stablecoin, BTC and altcoin dominance oscillators as tools for identifying risk-on/risk-off and segment-rotation transitions. It states that positive residual total-market expansion indicates altcoin-segment expansion and negative values indicate retreat toward BTC or stablecoins.

No source-reported Sharpe, CAGR, drawdown, win rate or independently audited backtest result was identified in the reviewed TradingView description, so none is claimed here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-specific independent negative result was identified in the reviewed source; absence is not evidence of no negative result.

Ex-ante concerns include mechanical denominator effects in dominance ratios, survivorship and constituent drift in the residual alt segment, stablecoin supply changes unrelated to risk appetite, and the possibility that all components merely re-express contemporaneous BTC/alt returns rather than forecast future returns.

## Falsification plan

1. **Naive baselines:** compare against BTC momentum, alt-minus-BTC momentum, total-market return and raw BTC dominance. The composite must add OOS information.
2. **Component ablation:** stablecoin only; BTC dominance only; alt dominance only; stable + BTC; stable + alt; all three; then add the residual-market histogram. Reject components that add no OOS value.
3. **Continuation versus reversal:** predeclare both signs and forward horizons. Do not select the mechanism after observing results.
4. **Mechanical-ratio control:** regress or condition rotation scores on contemporaneous BTC and alt returns. If predictive power vanishes after controlling for the same price moves that mechanically alter market-cap shares, reject incremental alpha.
5. **Point-in-time universe audit:** construct the alt segment without future survivors or current constituent knowledge. Reject results dependent on hindsight universe selection.
6. **Stablecoin robustness:** test USDT + USDC as sourced, then individual stablecoin components and broader point-in-time stablecoin baskets only as separate research variants.
7. **Parameter robustness:** test a neighborhood around the source-reported 7-period normalization/smoothing settings; a narrow isolated optimum materially weakens the thesis.
8. **Regime robustness:** bull/bear, high/low volatility, BTC-led, alt-led and stablecoin stress/depeg regimes.
9. **Timestamp placebo:** lag/shift the dominance inputs and use serial-dependence-aware placebo tests. Apparent edge that survives only with contemporaneously unavailable values is invalid.
10. **Execution robustness:** apply next-bar execution, realistic basket turnover, fees, spread, slippage, funding/borrow where applicable.
11. **Failure criterion:** reject or materially weaken the hypothesis if the rotation variables do not improve leakage-safe OOS relative-return prediction versus simple momentum/dominance baselines, if the sign is unstable across major regimes, or if the edge disappears under point-in-time constituent and execution controls.

## Crypto portability

**direct** — the source is crypto-native and explicitly models BTC, stablecoin and altcoin market-cap rotation.

Portability from indicator to a tradable portfolio remains unproven. Major risks are 24/7 timestamp boundaries, dominance denominator mechanics, stablecoin depegs and composition shifts, survivorship in the alt segment, venue fragmentation, liquidity concentration, funding for perpetual legs and borrow constraints for spot relative-value trades.

## Limitations

- **underspecified:** exact executable oscillator transformation, thresholds, entry/exit, holding period, re-entry, sizing and portfolio mapping.
- **not independently reproduced:** no internal replication was performed during this Scout run.
- **data gap:** historical point-in-time market-cap methodology and residual-alt constituent behavior require verification before backtesting.
- **mechanical-ratio risk:** dominance changes can be caused by contemporaneous price changes rather than independent capital flows.
- **survivorship risk:** a current altcoin universe cannot be projected backward.
- **unproven:** no validated alpha or profitability is claimed.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet or Live validation has occurred.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor / leaderboard strategy, is profitable, or is approved for implementation, Paper, Testnet or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView — **FlowTrinity - Crypto Dominance Rotation Index**, `sanbangaje`, published 2025-12-09: https://www.tradingview.com/script/BxfHcFQK-FlowTrinity-Crypto-Dominance-Rotation-Index/ (reviewed 2026-09-21).
