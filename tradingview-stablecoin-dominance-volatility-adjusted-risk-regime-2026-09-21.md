---
schema: strategy-research-record-v1
title: Stablecoin-Dominance Volatility-Adjusted Risk-Regime Alpha
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
  - https://www.tradingview.com/script/ONgoWfJX-Stablecoin-Dominance-Oscillator/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stablecoin-Dominance Volatility-Adjusted Risk-Regime Alpha

## Provenance

Public TradingView open-source indicator **Stablecoin Dominance Oscillator**, author/page identity `coffeequantz`, published 2024-11-09. Stable source: https://www.tradingview.com/script/ONgoWfJX-Stablecoin-Dominance-Oscillator/ . Source reviewed as of 2026-09-21.

Repository deduplication was performed against current `main` before capture by canonical TradingView source identity and normalized stablecoin-dominance signal family. No record for this canonical source was found. Existing repository material referencing stablecoin dominance uses materially different constructions or roles; this record specifically tests a normalized stablecoin-share deviation with an explicit short/long volatility-ratio context.

## Economic mechanism

### Source-reported

The source tracks stablecoin market capitalization (USDT + USDC + DAI) relative to total crypto market capitalization. It describes unusually high stablecoin dominance as commonly associated with fear / market bottoms and unusually low stablecoin dominance as commonly associated with strong bull markets / greed. It also includes a short-term versus long-term volatility ratio to contextualize signal reliability and dynamic bands that expand or contract with volatility.

### Research interpretation

The falsifiable hypothesis is that **changes in the share of crypto capital parked in major stablecoins contain incremental information about subsequent crypto risk-asset returns, and that this information is state-dependent on volatility**.

Two competing mechanisms must be tested rather than assumed:

1. **Risk-regime continuation:** rising abnormal stablecoin dominance reflects continuing de-risking and predicts weaker subsequent BTC / broad-crypto returns; falling abnormal dominance reflects capital deployment and predicts stronger subsequent returns.
2. **Extreme-state reversal:** sufficiently extreme positive stablecoin-dominance deviation represents accumulated dry powder / fear and predicts subsequent positive reversal, while extreme negative deviation represents crowded risk-on positioning and predicts weaker subsequent returns.

The volatility-ratio layer is a context variable, not presumed alpha. Its incremental value must survive ablation.

## Signal

Source-reported construction:

- Numerator concept: combined market capitalization of USDT + USDC + DAI.
- Denominator concept: total crypto market capitalization.
- Main signal: normalized deviation of stablecoin dominance from its trend.
- Source reports a **500-period lookback** for baseline calculations.
- Source reports a **15-period Hull Moving Average** for smoothing.
- Dynamic bands adapt to volatility.
- A volatility reference compares short-term with long-term volatility.

The public description does not unambiguously specify all formulas, exact short/long volatility windows, band equations, canonical entry/exit rules, holding period, re-entry logic, position sizing, or executable portfolio mapping. These remain **underspecified**.

`research-proposed` operationalization for falsification only:

- Freeze a decision timeframe before testing; daily is the lowest-complexity first test because market-cap/dominance data are structural rather than execution-level inputs.
- Form signals only after the completed bar and execute no earlier than the next tradable bar.
- Test both the signed normalized dominance deviation and extreme-state crossings separately.
- Evaluate forward BTC and a survivorship-safe broad-crypto basket at predeclared horizons rather than inventing a single source-implied holding period.
- Treat the volatility ratio as a regime interaction and test whether it improves out-of-sample discrimination versus the dominance signal alone.

## Required data

- Point-in-time USDT, USDC and DAI market capitalization / dominance series matching the TradingView source construction where reproducible.
- Point-in-time total crypto market capitalization.
- BTC OHLCV for the simplest tradable response variable.
- A survivorship-safe crypto universe if testing broad-market or cross-sectional portfolio responses.
- Short- and long-horizon realized-volatility inputs required to reconstruct the source volatility reference; exact windows are underspecified by the public description and must not be guessed as source facts.
- Explicit UTC timestamp / candle-boundary convention.
- Historical constituent / methodology changes in TradingView CRYPTOCAP series must be treated as a point-in-time data risk.

## Execution assumptions

The source is an indicator, not a complete trading strategy. It does not specify signal-to-order timing, order type, fill model, fees, spread, slippage, impact, leverage, shorting, funding, partial fills, or failures.

For any later executable test, all such assumptions must be declared independently as `research-proposed`. Perpetual implementation additionally requires funding and mark/index-price handling; spot implementation requires explicit basket construction and rebalance costs.

## Evidence

### Source-reported

The source describes high normalized stablecoin dominance as commonly associated with market bottoms/fear and low values with strong bull markets/greed. It states that a short/long volatility ratio is intended to contextualize signal reliability. These are source interpretations, not independently verified performance results.

No source-reported Sharpe, CAGR, drawdown, win rate, or independently audited backtest result was identified in the reviewed TradingView description, so none is claimed here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-specific independent negative result was identified in the reviewed source. Absence is not evidence of no negative result.

Important ex-ante concerns are denominator contamination (stablecoin share can change because risky-asset market cap moves even when stablecoin supply does not), stablecoin-universe drift, depegs, issuance/redemption mechanics, and potential historical revisions or methodology changes in aggregate market-cap series.

## Falsification plan

1. **Baseline decomposition:** compare raw BTC momentum / broad-market return baselines against (a) raw stablecoin dominance, (b) normalized dominance deviation, (c) smoothed deviation, and (d) deviation + volatility interaction. The complex form must add out-of-sample information.
2. **Numerator-vs-denominator test:** separately test changes in stablecoin market cap and changes in non-stable crypto market cap. If the apparent signal is only a mechanical mirror of contemporaneous crypto-price moves, reject incremental-alpha claims.
3. **Continuation vs reversal:** predeclare forward horizons and test both hypotheses. Do not select the sign after seeing results.
4. **Stablecoin ablation:** USDT-only, USDC-only, DAI-only, and combined basket. A result dominated by one historical stablecoin episode should not be generalized.
5. **Volatility ablation:** dominance-only versus dominance × volatility regime. Reject the volatility layer if it does not improve OOS performance or calibration.
6. **Placebo:** timestamp-shift and randomized-regime labels while preserving serial dependence as far as practical.
7. **Point-in-time audit:** verify that every market-cap/dominance observation and constituent definition was available at the signal timestamp; reject any result dependent on revised or future constituent information.
8. **Regime robustness:** bull, bear, high-volatility, low-volatility, stablecoin-depeg / stress episodes, and major stablecoin composition changes.
9. **Execution robustness:** if mapped to BTC spot/perpetual or a crypto basket, include realistic fees, spread, slippage, funding where applicable, and next-bar execution.
10. **Failure criterion:** reject or materially weaken the hypothesis if normalized dominance does not improve OOS predictive / portfolio performance versus simple price and volatility baselines, if the sign is unstable across major regimes, or if the edge disappears after point-in-time and execution controls.

## Crypto portability

**direct** — the source is crypto-native and explicitly uses stablecoin and total-crypto market capitalization.

Portability from indicator to tradable strategy is still unproven. Crypto-specific risks include 24/7 timestamp boundaries, stablecoin depegs, stablecoin issuance/redemption and composition changes, venue fragmentation, spot/perpetual basis and funding, and survivorship bias in any broad-crypto basket used as the traded response.

## Limitations

- **underspecified:** exact normalization formula details beyond the public description, dynamic-band formula, volatility windows, entry/exit, holding, sizing and execution.
- **not independently reproduced:** no internal or independent replication was performed during this Scout run.
- **data gap:** historical point-in-time CRYPTOCAP methodology / constituent behavior must be verified before backtesting.
- **mechanical-ratio risk:** stablecoin dominance can rise simply because the denominator falls.
- **structural-break risk:** stablecoin market structure changes materially through time; historical BUSD/UST-era and depeg regimes can alter interpretation even though this source uses USDT + USDC + DAI.
- **unproven:** no validated alpha or trading profitability is claimed.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation has occurred.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor / leaderboard strategy, is profitable, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView — **Stablecoin Dominance Oscillator**, `coffeequantz`, published 2024-11-09: https://www.tradingview.com/script/ONgoWfJX-Stablecoin-Dominance-Oscillator/ (reviewed 2026-09-21).
