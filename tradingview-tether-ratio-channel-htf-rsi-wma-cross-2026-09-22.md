---
schema: strategy-research-record-v1
title: TradingView Tether Ratio Channel Higher-Timeframe RSI / WMA Cross
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - https://www.tradingview.com/script/7dlcPeKa-Tether-Ratio-Channel/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Tether Ratio Channel Higher-Timeframe RSI / WMA Cross

## Provenance

- Public TradingView open-source indicator: **Tether Ratio Channel**, by **ColeGarner**.
- Stable source URL: https://www.tradingview.com/script/7dlcPeKa-Tether-Ratio-Channel/
- TradingView publication date shown by the source: 2024-08-23.
- Source reviewed as of 2026-09-22.
- This record normalizes the public description rather than redistributing Pine source code.

## Economic mechanism

### Source-reported

The author describes the underlying quantity as the relationship between BTC market capitalization and stablecoin market capitalization and argues that this liquidity ratio has tended to lead total crypto market capitalization over short-to-medium horizons. The implementation uses a proxy based on USDT, USDC, and DAI relative to BTC market capitalization, then transforms the ratio with a higher-timeframe RSI, channel normalization/smoothing, and a weighted moving average. The author presents low channel values as greater upside potential and high values as greater downside risk.

The source explicitly describes the metric as optimized to place signals near BTC local tops and bottoms. That is a material in-sample overfitting warning, not evidence of out-of-sample alpha.

### Research interpretation

The falsifiable hypothesis is narrower than the source's broad market-timing claim: **a higher-timeframe momentum/reversal transform of stablecoin purchasing power relative to BTC market capitalization may contain incremental information about subsequent BTC or broad-crypto returns beyond the raw stablecoin-supply ratio itself.**

Possible mechanism: persistent changes in stablecoin purchasing power relative to BTC may reflect changing crypto-native liquidity and risk appetite. The RSI/channel transformation could identify unusually stretched liquidity regimes, while the metric/WMA cross could mark a change in that regime. This mechanism is unproven and must be separated from the source's historical optimization.

## Signal

Source-reported normalized logic:

- **Input proxy:** stablecoin market capitalization represented by USDT + USDC + DAI relative to BTC market capitalization. The source's prose describes the metric both as BTC market cap / stablecoin market cap and later as `(USDT + USDC + DAI) / BTC market cap`; this orientation ambiguity must be resolved from a reproducible implementation before testing.
- **Transform:** higher-timeframe RSI of the stablecoin/BTC ratio, bounded inside a Bollinger-band channel, normalized and smoothed.
- **Signal line:** weighted moving average of the transformed metric.
- **Bullish entry indication:** transformed metric crosses bullishly above its WMA. A bullish cross below the source's green horizontal target is described as higher conviction; a bullish cross above it as lower conviction.
- **Exit / bearish indication:** any bearish cross is described as a profit-taking signal.
- **Top-risk indication:** bearish cross above 55 is described as tending to coincide with BTC local tops.
- **Default higher timeframe:** source says signal/background rendering applies when the chart is at or below the metric timeframe and identifies 8H as the default metric timeframe.
- **Holding behavior:** source visualization keeps the bullish background state until the next sell signal.
- Exact RSI length, Bollinger parameters, WMA length, green-target value, normalization formula, and smoothing parameters are not fully specified in the reviewed public prose and are therefore **underspecified** here. Do not infer them.

Research-proposed operationalization, only after exact source reconstruction is possible: evaluate signals at the close of the completed higher-timeframe bar and execute no earlier than the next tradable bar. This is `research-proposed`, not source-reported.

## Required data

- BTC market capitalization, point-in-time.
- USDT, USDC, and DAI market capitalizations, point-in-time.
- BTC spot or a clearly specified broad-crypto return target for evaluation.
- Higher-timeframe bars consistent with the source's default 8H transform.
- Stablecoin constituent histories and ticker/data-vendor methodology through time.
- Publication/availability timestamps sufficient to prevent revised market-cap observations from leaking backward.
- Missing-data and stablecoin depeg handling must be explicit.

## Execution assumptions

The source is an indicator description, not a complete execution specification. It does not establish order type, same-bar versus next-bar fill, fees, spread, slippage, impact, leverage, position sizing, partial fills, or failure handling.

For research, any tradable rule must use causal completed-bar information and realistic next-bar execution with fees/slippage appropriate to the chosen BTC venue. Those assumptions are `research-proposed` and must not be attributed to the source.

## Evidence

### Source-reported

The author qualitatively states that the ratio tends to lead total crypto market capitalization over short-to-medium horizons; bullish crosses are presented as entries, bearish crosses as profit-taking signals, and bearish crosses above 55 as tending to coincide with BTC local tops. The source also explicitly states that the metric was optimized with the intent of placing signals near historical BTC local tops and bottoms.

No traceable Sharpe ratio, CAGR, maximum drawdown, hit rate, transaction-cost study, formal out-of-sample test, or statistical significance result is reported in the reviewed TradingView description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's explicit historical optimization is a major overfitting risk. The reviewed description does not provide independent out-of-sample validation. Stablecoin composition changes materially through time, stablecoin market capitalization can change because of issuance/redemption or depegs, and BTC market capitalization in the denominator/numerator mechanically embeds BTC price itself. The source prose also contains an orientation ambiguity between BTC/stablecoin and stablecoin/BTC expressions.

None of these concerns independently disproves the hypothesis, but each can create apparent historical timing skill without robust incremental alpha.

## Falsification plan

1. **Reconstruction gate:** resolve the exact ratio orientation and all transform parameters from a reproducible public source representation. If this cannot be done without guessing, do not backtest the source rule.
2. **Raw-factor baseline:** compare the transformed channel against the raw BTC/stablecoin ratio and a simple rolling z-score of that ratio. The complex transform must add OOS information.
3. **Ablation:** test raw ratio -> HTF RSI -> channel normalization -> smoothing -> WMA cross sequentially. Reject layers that do not improve leakage-safe OOS performance.
4. **Optimization stress:** vary RSI, channel, smoothing, WMA, threshold, and higher-timeframe parameters around the source values once reconstructed. A narrow optimum centered on the published settings materially weakens the thesis.
5. **Target controls:** compare predictive value for BTC returns and broad-crypto returns separately; do not infer broad-market alpha from BTC-only timing.
6. **Mechanical-price control:** control for BTC momentum, drawdown, realized volatility, and simple price RSI because BTC market cap is mechanically price-linked.
7. **Stablecoin controls:** compare USDT-only, USDT+USDC, USDT+USDC+DAI, and a point-in-time stablecoin basket. Treat depeg regimes separately.
8. **Point-in-time test:** enforce historical constituent availability and data-publication lag; test timestamp-delay placebos to expose revision/look-ahead sensitivity.
9. **Walk-forward OOS:** parameters must be fixed before each evaluation segment. Do not re-optimize using future cycle extrema.
10. **Cost sensitivity:** evaluate next-bar execution under realistic fees, spread, and slippage.
11. **Failure action:** if the transformed/WMA-cross rule does not robustly beat the raw ratio and simple price/liquidity controls OOS, reject the transformation layer rather than adding more filters.

## Crypto portability

**direct** — the source is explicitly constructed from BTC and crypto stablecoin market-cap data.

Portability across venues still requires care because the factor is market-wide while execution is venue-specific. Stablecoin depegs, constituent changes, market-cap vendor revisions, 24/7 candle boundaries, and spot/perpetual execution differences can materially affect results.

## Limitations

- **underspecified:** exact RSI, Bollinger/channel, WMA, smoothing, normalization, and green-target parameters are not fully recoverable from the reviewed prose alone.
- **orientation ambiguity:** the public description uses both BTC/stablecoin and stablecoin/BTC wording.
- **optimization risk:** the author explicitly describes historical optimization toward local tops/bottoms.
- **data gap:** point-in-time revision policy for the TradingView market-cap series is not established here.
- **not independently reproduced.**
- No source-reported transaction-cost or formal OOS evidence was identified.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

This artifact is research-only staging material. It has not passed Research Intake Review, has not entered Hermes Wiki Brain or the production candidate pool, has not completed Qlib validation, is not a frozen survivor or leaderboard entry, and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- `[[quant/bitcoin-stablecoin-supply-ratio-ssr-oscillator-2026-09-01]]` — closely related raw stablecoin purchasing-power ratio; required baseline, not a duplicate because this record tests whether the HTF RSI/channel/WMA transformation adds incremental information.
- `[[quant/crypto-stablecoin-minting-issuance-inflow-momentum-shock-2026-09-01]]` — stablecoin issuance-flow mechanism rather than a market-cap-ratio transform.
- `[[quant/tradingview-stablecoin-dominance-volatility-adjusted-risk-regime-2026-09-21]]` — stablecoin-dominance regime construction rather than the Tether Ratio Channel cross.

## Sources

- ColeGarner, **Tether Ratio Channel**, TradingView, published 2024-08-23, reviewed 2026-09-22: https://www.tradingview.com/script/7dlcPeKa-Tether-Ratio-Channel/
