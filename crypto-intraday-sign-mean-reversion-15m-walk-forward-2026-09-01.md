---
schema: strategy-research-record-v1
title: Crypto Intraday Sign Mean Reversion at 15-Minute Horizon
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - mean-reversion
  - intraday
  - microstructure
status: research-only
confidence: medium
source_as_of: 2026-08-08
sources:
  - https://arxiv.org/abs/2608.21888
  - https://arxiv.org/html/2608.21888v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - Source reports statistically pervasive 15-minute directional reversal, but the gross edge remains below the paper's benchmark spot round-trip cost band.
---

# Crypto Intraday Sign Mean Reversion at 15-Minute Horizon

## Provenance

Primary source: Nadav A. Kitron and Jonathan M. Wengrowicz, *Short-horizon mean reversion in cryptocurrency markets: a matched cross-market measurement*, arXiv:2608.21888v1 [q-fin.TR], submitted 2026-08-22.

Stable source URLs:

- https://arxiv.org/abs/2608.21888
- https://arxiv.org/html/2608.21888v1

Primary crypto sample: 183 high-volume Binance USDT spot pairs, 15-minute candles from 2025-01-01 through 2026-02-11. The authors also report focal multi-year histories back to 2021 and a frozen post-sample holdout from 2026-02-12 through 2026-08-08. Universe selection for the wide crypto cross-section was performed on 2026-06-08 using highest 24-hour quote volume, excluding pegged-base pairs and leveraged tokens; this creates an explicit survivor-universe concern.

Source/data as-of date used for this record: 2026-08-08, the end of the frozen forward holdout reported in v1.

## Economic mechanism

### Source-reported

The paper reports pervasive short-horizon directional mean reversion in cryptocurrency returns. At the 15-minute horizon, the predictive structure is concentrated in return signs rather than return magnitudes. The authors interpret the pattern as consistent with transitory price pressure and compensated liquidity provision: reversal is stronger after prior-bar moves aligned with aggressive taker flow and increases with flow intensity, while measured order-book depth consumption does not condition the effect.

The source explicitly limits this interpretation. Ordinary aggressor flow is endogenous and may itself contain information, so the design cannot identify liquidity provision as the unique causal mechanism.

### Research interpretation

This is a within-instrument, short-horizon reversal hypothesis:

- Primary signal family: time-series sign mean reversion.
- Regime / conditioning: none required for the baseline hypothesis.
- Optional mechanism conditioner: prior-bar move aligned with aggressive taker imbalance may identify stronger reversal states, but source evidence treats this as conditioning rather than causal identification.
- Expected horizon: strongest around 15 minutes and decaying toward no-skill within hours.

The falsifiable economic hypothesis is that a sufficiently large subset of liquid crypto pairs exhibits negative conditional dependence in the sign of consecutive short-horizon returns after controlling for simple artifact channels, and that this dependence survives genuinely forward data. Profitability is a separate question and is not implied by sign predictability.

## Signal

Baseline source-consistent normalized rule:

1. Form 15-minute UTC candles.
2. Compute each candle's intra-bar return as `(close_t - open_t) / open_t`.
3. Map the most recent return history into directional / soft-clipped features. The paper's primary model uses 12 lagged soft-clipped returns, `s_t = tanh(150 * r_t)`, with a constrained decaying-lag logistic model; an unconstrained AR(12) logit and parameter-free sign statistics are used as robustness checks.
4. Forecast the sign of the next 15-minute candle.
5. Mean-reversion direction: when the fitted reversal coupling is negative, forecast against the recent return-sign path rather than with it.
6. The paper's deployable illustration acts only when model confidence clears `|p_t - 0.5| >= tau`, where `tau` is selected from an ex-ante grid rather than tuned on the out-of-sample series.
7. Hold for the next 15-minute bar and then re-evaluate.

A simpler falsification baseline should be tested first: bet against the immediately preceding candle sign. The authors report that this parameter-free behavior captures much of the effect, so a more complex model must prove incremental value rather than receive it by assumption.

Underspecified for production use:

- exact confidence-threshold grid and production threshold;
- order type and precise entry timestamp relative to candle close/open;
- handling of simultaneous signals across many pairs;
- capital allocation / position sizing;
- whether the optional taker-flow conditioning should be used as a trade filter;
- venue-specific implementation outside the research design.

## Required data

Baseline:

- crypto spot instruments;
- Binance USDT pairs for direct source replication;
- 15-minute OHLC candles;
- UTC bucket-start timestamps;
- point-in-time instrument availability and delisting history;
- exact handling of missing and flat bars.

For mechanism / conditioning tests:

- taker-buy base volume or equivalent aggressor-side trade classification;
- total volume sufficient to construct taker imbalance;
- optionally USDT-M perpetual funding history and basis for robustness controls;
- optionally historical order-book depth snapshots for the book-consumption test.

Point-in-time universe construction is required for an independent replication because the source wide-universe selection is survivor-biased by construction.

## Execution assumptions

The source studies predictability first and economic capture second. A production execution rule is not fully specified.

Material assumptions to model independently:

- signal calculated only from information available at or before the completed 15-minute bar;
- next-bar entry rather than same-bar hindsight fill;
- maker versus taker execution;
- bid-ask spread;
- exchange fees and fee tier;
- slippage and queue position;
- market impact / capacity across 183 pairs;
- partial fills and rejected orders;
- latency around bar boundaries;
- shorting / borrow feasibility for spot, or funding / basis effects if ported to perpetuals.

The paper reports a benchmark cheapest spot round-trip cost band around 5 bp and a taker band around 10-20 bp. Its selected gross edge peaks near 1.3 bp per trade, so benchmark source assumptions imply the measured effect is not directly exploitable as a naive spot strategy.

## Evidence

### Source-reported

For the primary 2025-01-01 to 2026-02-11 sample, the source reports:

- crypto mean out-of-sample AUC of 0.531 across 183 Binance USDT spot pairs;
- 98% of crypto pairs above AUC 0.5;
- 90% of crypto pairs significant after the paper's joint FDR procedure;
- mean-reverting fitted coupling in 98% of crypto pairs;
- a crypto-versus-US-stock class-mean AUC gap of +0.031 with 95% bootstrap CI [+0.027, +0.035].

The walk-forward geometry is source-reported as 5,760 training candles followed by 960 test candles, stepping by the non-overlapping test block and concatenating only out-of-sample predictions.

For the frozen forward holdout from 2026-02-12 through 2026-08-08, the source reports:

- crypto mean AUC 0.522;
- 60% of crypto pairs FDR-significant;
- 96% with negative mean-reversion coupling;
- constrained class-mean crypto-versus-stock AUC gap +0.020 with 95% CI [+0.010, +0.028].

The authors also report that a joint artifact-robust version using a one-bar feature/label gap and dropping flat bars reduces the crypto-versus-stock AUC gap to +0.011, with 95% CI [+0.008, +0.014], but does not eliminate it.

For mechanism evidence, the source reports that 12 sign lags achieve pooled OOS AUC 0.529 across four focal coins, 12 taker-imbalance lags achieve 0.521, and adding imbalance to signs leaves AUC at 0.529. This supports treating order flow as a conditioner rather than a replacement for the sign path.

All figures above are source-reported. They have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The most important negative evidence is economic: the source reports that the gross edge per selected trade stays below benchmark spot round-trip costs, peaking near 1.3 bp versus an approximately 5 bp cheapest realistic spot round-trip band, with taker costs higher still. Statistical predictability therefore does not establish executable alpha after costs.

Further negative / cautionary evidence:

- holdout AUC and the fraction of significant crypto pairs decline relative to the primary sample, consistent with erosion even though the effect remains above chance in the reported forward data;
- the wide crypto universe is selected using 2026-06-08 volume and is therefore survivor-biased;
- a one-bar information gap plus removal of flat bars materially reduces the headline class gap;
- taker-flow conditioning is not causal identification because aggressive order flow is endogenous;
- order-book depth-consumption conditioning is approximately null in the source;
- funding, basis, funding-clock, volatility, and session conditioning are reported as flat in the mechanism appendix;
- the authors disclose that they operate an automated cryptocurrency trading system using a variant of the studied model, although they state that no system data are used and that key design choices predate the paper.

## Falsification plan

An independent test should treat this as a high-bar replication because the reported statistical edge is small relative to trading costs.

1. Rebuild a point-in-time, non-survivor-biased Binance universe over a fresh sample after 2026-08-08.
2. Use exact UTC 15-minute bucket boundaries and preserve missing / flat bars without forward filling.
3. Establish parameter-free baselines first:
   - next-bar sign against previous-bar sign;
   - unconditional 50/50 sign forecast;
   - time-of-day matched placebo;
   - randomly shifted 15-minute grid offsets.
4. Reproduce the AR(12) and constrained-logit variants strictly walk-forward with no overlapping test leakage.
5. Apply a one-bar feature/label information gap and flat-bar-robust scoring from the start, not only as a secondary sensitivity test.
6. Repeat on at least one independent venue such as Coinbase, OKX, or Bybit with venue-native candles / trades.
7. Test whether reversal remains concentrated after flow-aligned moves using point-in-time aggressor-flow data, while treating this as conditioning rather than proof of mechanism.
8. Run cost curves across realistic maker and taker fee tiers, spread, slippage, latency, partial fills, and capacity.
9. Require net-of-cost economic value to remain positive under realistic execution assumptions. If the gross edge remains below attainable round-trip cost, classify the hypothesis as statistically real but non-capturable under that execution regime.
10. Monitor decay: materially weaken the thesis if fresh walk-forward AUC converges to 0.5 or the sign-flip effect loses consistency across liquid pairs and independent venues.

## Crypto portability

direct

The source directly studies cryptocurrency markets, primarily Binance USDT spot pairs. Porting the rule to perpetuals is adapted rather than automatically direct because perpetual funding, mark/index construction, basis, liquidation flow, leverage, and fee structure alter both the signal environment and execution economics.

Crypto-specific risks include 24/7 bar-boundary conventions, venue fragmentation, differing aggressor classifications, tick-size changes, delistings, rapidly changing liquidity, and the possibility that a statistically persistent reversal remains too small to monetize after costs.

## Limitations

- Preprint / working-paper evidence; not peer-reviewed as of arXiv v1 dated 2026-08-22.
- Not independently reproduced.
- Survivor-universe bias in the source wide cross-section.
- Production threshold, execution state machine, position sizing, and portfolio construction are underspecified.
- Statistical sign predictability is not equivalent to positive net PnL.
- The source's own benchmark cost analysis is adverse to naive implementation.
- Mechanism attribution to compensated liquidity provision remains unproven.
- Data gap: no independent post-2026-08-08 replication has been performed here.

## Implementation status

Research-only. No implementation has been completed in PyBroker, NautilusTrader, the strategy registry, Paper, Testnet, or Live workflows.

## Adoption boundary

This record is research material only. Presence in the Alpha Strategy Pool does not mean the hypothesis is profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

No implementation task is created by this record.

## Related Wiki records

No stable Hermes Wiki Brain link is added in this Scout cycle.

Related Alpha Strategy Pool material exists for daily cross-sectional reversal and other microstructure signals, but this record is intentionally preserved separately because its identity is a within-instrument 15-minute sign-reversal process with a distinct source, horizon, signal construction, and cost result.

## Sources

1. Kitron, Nadav A., and Jonathan M. Wengrowicz. *Short-horizon mean reversion in cryptocurrency markets: a matched cross-market measurement*. arXiv:2608.21888v1 [q-fin.TR], 22 August 2026. https://arxiv.org/abs/2608.21888
2. Full HTML version of arXiv:2608.21888v1, including protocol, holdout, mechanism, cost, data-construction, and limitation sections. https://arxiv.org/html/2608.21888v1
