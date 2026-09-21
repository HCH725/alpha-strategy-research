---
schema: strategy-research-record-v1
title: Stablecoin Liquidity Pulse Flow-Dominance Parking Regime
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
  - https://www.tradingview.com/script/lwAkmKDg-Stablecoin-Liquidity-Pulse-Map-AGPro-Series/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stablecoin Liquidity Pulse Flow-Dominance Parking Regime

## Provenance

Public TradingView open-source script **Stablecoin Liquidity Pulse Map [AGPro Series]**, author/page identity `AGProLabs`. Stable URL: https://www.tradingview.com/script/lwAkmKDg-Stablecoin-Liquidity-Pulse-Map-AGPro-Series/ . Reviewed 2026-09-22. The page shows original publication on May 14 and an update on Aug 7. The source reads USDT and USDC market-cap series, optionally DAI, and compares stablecoin flow with total-crypto market-cap context to classify liquidity states.

GitHub deduplication on current `main` found no record for this canonical TradingView source or its named flow/dominance/parking-state construction. Related repository records cover stablecoin supply ratios, issuance shocks, cross-chain flows and stablecoin dry-powder effects, but this record isolates a materially distinct state hypothesis: separating liquidity expansion from defensive stablecoin parking by jointly conditioning stablecoin flow on stablecoin dominance and market risk appetite.

## Economic mechanism
### Source-reported

The source argues that stablecoin supply growth is context-dependent rather than mechanically bullish. Expanding stablecoin liquidity may represent capital entering or preparing to rotate into risk assets, while rising stablecoin dominance during weakening market behavior may instead represent defensive parking. Contracting stablecoin flow may indicate thinner risk liquidity. The script combines stablecoin flow, velocity, dominance pressure, parking risk, dry-liquidity behavior and price context into named states including Liquidity Expansion, Risk-Off Parking, Dry Liquidity, Rotation Ready and Neutral Pulse.

The author explicitly states that these states are market-context signals, not guaranteed price predictions or standalone trade instructions.

### Research interpretation

The falsifiable hypothesis is that **the interaction between stablecoin supply flow and stablecoin dominance contains more forward information about crypto risk appetite than stablecoin supply growth alone**. Specifically, equal positive stablecoin-flow observations may imply different subsequent return distributions depending on whether stablecoin dominance is falling/stable (potential deployment into crypto risk) or rising (potential defensive parking).

A second, separable hypothesis is that transitions between the source-defined state families contain information about subsequent BTC/ETH returns or volatility: Expansion may precede constructive risk appetite, Risk-Off Parking may precede weaker risk returns, Dry Liquidity may precede reduced depth or adverse volatility, and Rotation Ready may precede recovery. Translating these context states into explicit forward-return tests is **research-proposed**; the source does not define a complete trading system.

## Signal

Source-described components:

- **Stablecoin inputs:** USDT and USDC market capitalization; DAI is optional.
- **Market context:** total crypto market capitalization when available.
- **Stablecoin flow:** measured over a configurable `Liquidity Flow Length`.
- **Slower context:** configurable `Pulse Baseline Length`.
- **State sensitivity:** configurable inflow/outflow thresholds and a dominance-pressure threshold.
- **Liquidity Expansion:** stablecoin flow improves while dominance pressure is not defensive.
- **Risk-Off Parking:** stablecoin dominance pressure rises while market appetite weakens.
- **Dry Liquidity:** stablecoin flow contracts and liquidity conditions may be thinner.
- **Rotation Ready:** stablecoin flow improves while market behavior begins to recover.
- **Neutral Pulse:** no strong state is active.
- Source guidance favors 1D and 1W analysis and warns against extremely noisy intraday use.

The reviewed public description does not expose numerical defaults for all flow lengths, baselines and thresholds in a way relied upon by this record, nor a complete entry/exit/holding/re-entry/position-sizing lifecycle. Those elements are therefore **underspecified** here rather than inferred.

Research-proposed operationalization for falsification:

1. Reconstruct stablecoin aggregate flow and stablecoin dominance using only point-in-time data available at each observation.
2. Pre-register simple state definitions corresponding to Expansion, Parking, Dry and Rotation using source-supported component directions; exact thresholds must be taken from auditable source code or treated as research parameters, not invented as source facts.
3. Measure forward BTC and ETH returns and realized volatility after state formation at daily/weekly horizons.
4. Compare the joint flow-plus-dominance state with stablecoin-flow-only and price-only baselines.
5. No execution occurs before the state is fully observable; any trade mapping remains research-proposed.

## Required data

- Point-in-time USDT and USDC market capitalization; optional DAI only when historically available.
- Point-in-time total crypto market capitalization sufficient to compute dominance pressure consistently.
- BTC and ETH OHLCV for forward-return/volatility evaluation.
- Daily timestamps with explicit UTC boundary policy; weekly aggregation if testing the source-recommended 1W context.
- Stablecoin listing/existence history and missing-data flags. A stablecoin must not be backfilled before its actual existence or data availability.
- Depeg/event flags are desirable for robustness because market-cap changes during depegs can reflect price effects rather than net issuance/redemption.

## Execution assumptions

The source is a context indicator and does not specify executable orders, fill model, fees, spread, slippage, impact, leverage, margin, shorting, latency, partial fills or failures. It explicitly says the states are not standalone buy/sell instructions.

Any eventual strategy test must therefore define execution separately and label it **research-proposed**. Signal formation must use fully observed point-in-time market-cap inputs, and same-bar execution that depends on end-of-bar state information is prohibited.

## Evidence
### Source-reported

The source describes the economic interpretation of the state machine and, in a later release, adds a historical `Signal Hit` proof layer that checks whether risk-on states receive upside follow-through and risk-off states downside follow-through within configurable proof windows. The reviewed page does not provide a traceable numerical hit rate, Sharpe, CAGR, drawdown or other complete performance statistic, so no such figure is recorded here.

The source also explicitly cautions that Liquidity Expansion does not guarantee upside, Risk-Off Parking does not guarantee downside, Dry Liquidity does not guarantee immediate volatility, and Rotation Ready does not guarantee rotation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself notes that stablecoin supply changes can lag market behavior; timeframe choice changes interpretation; exchange stress, depegs and abnormal data conditions can distort readings; and stablecoin liquidity is not automatically bullish or bearish. No independently reproduced negative result was obtained in this Scout run.

## Falsification plan

1. **Point-in-time reconstruction:** verify stablecoin and total-market-cap observations as they were available at each signal timestamp. Reject any implementation that uses revised/backfilled future information.
2. **Core baseline:** compare `BTC/ETH price-only` -> `stablecoin aggregate flow only` -> `stablecoin dominance only` -> `flow + dominance interaction`. The interaction must add stable OOS information beyond the simpler stablecoin-flow signal.
3. **State ablation:** test Expansion, Parking, Dry and Rotation separately. Do not combine opposite states into one favorable composite after observing outcomes.
4. **Issuer ablation:** `USDT only` -> `USDC only` -> `USDT+USDC` -> `+DAI`. If performance depends entirely on one historical issuer episode, weaken the general liquidity thesis.
5. **Price-denominator control:** stablecoin dominance mechanically depends on total crypto market cap. Control for contemporaneous BTC/ETH returns and total-market-cap moves to test whether the state adds information beyond the denominator's price action.
6. **Supply-vs-price decomposition:** where possible distinguish stablecoin token supply changes from market-cap changes caused by depegs or price deviations from $1. Exclude or separately analyze depeg windows.
7. **Lag/lead test:** compare contemporaneous, lagged and forward relationships. If stablecoin flow merely reacts to prior crypto returns, a predictive interpretation is weakened.
8. **Threshold robustness:** test broad neighboring flow/baseline/dominance parameters rather than selecting a single optimum. Exact source defaults, once audited, remain source parameters; any additional grid is research-defined.
9. **Regime robustness:** split bull/bear, high/low volatility, pre/post spot-ETF era, stress/non-stress and major stablecoin composition changes. Require directionally coherent behavior rather than one episode carrying the result.
10. **Timestamp placebo:** shift stablecoin observations by controlled offsets. Comparable or stronger placebo performance weakens the proposed information channel.
11. **Out-of-sample requirement:** freeze definitions before final evaluation. If the joint flow/dominance state does not improve leakage-safe OOS predictive/economic performance over the strongest simple baseline after realistic costs, reject the composite state complexity.

## Crypto portability

direct

The source is explicitly crypto-native and designed around stablecoin and total-crypto market-cap data, with BTC and ETH listed as intended context uses. Portability across crypto assets is nevertheless unproven: small-cap assets can have idiosyncratic liquidity, and stablecoin flow may first affect BTC/ETH or exchange-specific venues rather than all tokens simultaneously.

Crypto-specific risks include 24/7 timestamp boundaries, stablecoin depegs, issuer composition changes, token migrations, chain fragmentation, exchange stress and differences between circulating supply and market-cap data vendors.

## Limitations

- **underspecified:** the reviewed public description does not provide all numerical state thresholds and complete trade lifecycle parameters relied upon for executable reconstruction.
- **not independently reproduced:** no internal backtest or independent state reconstruction was performed.
- **data gap:** point-in-time stablecoin market-cap histories and revision behavior must be verified before testing.
- **mechanical denominator risk:** stablecoin dominance can rise simply because crypto asset prices fall, even without new stablecoin inflow.
- **depeg contamination:** market-cap changes may reflect stablecoin price deviations rather than mint/burn flows.
- **composition drift:** historical stablecoin leaders change; a fixed present-day basket creates survivorship bias.
- The source's later `Signal Hit` layer is not treated as independent evidence because it is generated inside the same indicator and no traceable numerical result is preserved here.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest have been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitability, or received Paper, Testnet or Live approval.

## Related Wiki records

No Hermes Wiki lookup was performed because this Scout is GitHub-only. Related repository families identified during deduplication include stablecoin supply-ratio, issuance-flow, cross-chain stablecoin-flow and dry-powder/liquidity research; these are comparison baselines, not evidence that this hypothesis is valid.

## Sources

- TradingView — `AGProLabs`, **Stablecoin Liquidity Pulse Map [AGPro Series]**: https://www.tradingview.com/script/lwAkmKDg-Stablecoin-Liquidity-Pulse-Map-AGPro-Series/ (public open-source script; reviewed 2026-09-22; page shows publication May 14 and update Aug 7).
