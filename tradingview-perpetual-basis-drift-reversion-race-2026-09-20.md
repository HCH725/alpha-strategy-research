---
schema: strategy-research-record-v1
title: Perpetual Basis Drift Reversion-vs-Continuation Race
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/nhDTQvJc-Perpetual-Basis-Drift-Map-AGPro-Series/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Perpetual Basis Drift Reversion-vs-Continuation Race

## Provenance

Public TradingView open-source indicator **Perpetual Basis Drift Map [AGPro Series]** by `AGProLabs`. The public page labels the initial publication `May 14` and updates through `Aug 7`; the retrieved page does not unambiguously expose the year beside those labels, so no year is inferred. Stable source: https://www.tradingview.com/script/nhDTQvJc-Perpetual-Basis-Drift-Map-AGPro-Series/ . Reviewed 2026-09-20.

Repository deduplication on current `main` found no artifact for this canonical TradingView source. Existing premium/basis records are conceptual neighbors, but this source adds a materially distinct hypothesis: **stateful basis drift with velocity and persistence, plus an explicit reset-versus-further-widening race** rather than a static premium level or simple premium ROC.

## Economic mechanism

### Source-reported

The source compares an active perpetual/futures price with an automatically selected matching spot reference. It measures basis percentage, drift from a baseline, normalized basis z-score, drift velocity, persistence and trend context. It classifies positive/negative drift, basis expansion, basis compression and reset states. The author explicitly states that basis does not have to mean-revert and that the tool is contextual rather than a prediction engine.

A later source update adds a historical **Reversion Rate**: once an active drift/expansion episode occurs, it is counted as a reset only if basis returns toward neutral before widening to a meaningfully larger extreme. Widening first or expiry without reset counts as not reverted. The source describes each episode as counted once.

### Research interpretation

Hypothesis: **the joint state of basis displacement, drift velocity and persistence contains incremental information about whether a perp/spot dislocation is more likely to continue widening or normalize, beyond basis level alone.** This can reflect temporary leveraged demand/supply, arbitrage-capital response, and persistence of derivatives-led pressure.

The key research target is not “premium always reverses.” It is a competing-risk problem:

1. **Continuation:** displaced basis with same-direction velocity and persistence reaches a larger extreme before neutralization.
2. **Reversion:** displaced basis loses velocity/compresses and returns toward its baseline before widening materially.
3. **No directional-price alpha:** basis-state information may predict spread behavior without predicting the outright crypto return.

## Signal

Source-specified elements:

- Build a matching spot reference from the active chart base currency, selected exchange and quote.
- Compute perpetual/futures-versus-spot basis percentage.
- Evaluate basis drift from a baseline, normalized basis z-score, drift velocity, persistence and trend context.
- Distinguish Positive Drift, Negative Drift, Basis Expansion, Basis Compression and Reset states.
- Confirm state transitions, historical event labels, pulse markers and alerts on completed bar closes in the later source update.
- Historical reversion proof uses a race: reset toward neutral versus widening to a meaningfully larger extreme within a configurable window; each episode is counted once, and widening first or expiry without reset is non-reversion.
- A reference-mismatch guard is used to avoid treating an invalid spot comparison as genuine basis.

The public description names configurable baseline length, normalization lookback, velocity lookback, persistence window, reversion window and widen margin, but does not expose all exact defaults/formulas/thresholds needed to reconstruct the complete internal score and state engine from the reviewed text. Canonical trade entry, exit, holding period, re-entry, sizing, stop and take-profit are not supplied because the source is explicitly not an automated trading strategy. These items are `underspecified`.

`research-proposed` operationalization for falsification only: reconstruct synchronized point-in-time perp-minus-spot basis; estimate displacement, lagged velocity and persistence using leakage-safe rolling windows; define an event at a completed bar; then measure which barrier occurs first—baseline/neutral reset or further same-direction widening. Any exact lookback, normalization, neutral band, widen barrier or horizon not directly recoverable from the source must remain labeled `research-proposed`.

## Required data

- Liquid crypto perpetual/futures and matching spot price series.
- Venue, symbol, quote currency and contract metadata sufficient to verify the spot reference.
- Synchronized timestamps and identical bar boundaries.
- Point-in-time OHLCV for the response instrument.
- Funding, open interest, volume and realized volatility for confound controls where available.
- Missing/stale feed indicators and exchange outage handling.
- Quote-currency consistency (USD/USDT/USDC etc.) and explicit handling of contract/spot mismatches.

## Execution assumptions

The source provides analytical states and alerts, not executable trading rules. Order type, fills, fees, spread, slippage, impact, funding, leverage, margin, latency, partial fills and failures are unspecified.

For research, states must be formed only after the relevant bar is confirmed, consistent with the source's later confirmed-close behavior. Any hypothetical position may execute no earlier than the next executable observation. A convergence implementation must model both spot and derivative legs, funding, borrow/capital usage, venue-specific fees and transfer/hedging constraints rather than assuming frictionless arbitrage.

## Evidence

### Source-reported

The source reports the construction and interpretation of basis states. Its later Reversion Rate layer reports, on-chart, the historical fraction of active drift/expansion episodes that reset before widening farther, with sample count. The reviewed public page does not provide a fixed cross-market reversion statistic, Sharpe, CAGR, drawdown, win rate or other portable performance number, so no numerical performance claim is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly states that positive or negative basis drift does not imply an immediate reversal, basis expansion is context rather than a trade instruction, and normalization does not guarantee price direction. Reference quality, exchange differences, contract type, liquidity, funding conditions and timeframe can alter observed states. The source also added quote/reference guards and corrected expansion classification in later releases, showing that reference integrity and state definition are material failure modes.

## Falsification plan

1. Reconstruct synchronized perp/spot basis point-in-time and reject observations with mismatched quote, stale reference or unavailable counterpart.
2. Treat the outcome as a competing-risk race: neutral/baseline reset versus further same-direction widening before a fixed horizon. Test spread outcome separately from outright asset return.
3. Ablate `basis level -> normalized displacement -> + velocity -> + persistence -> + trend context`. Reject the incremental hypothesis if velocity/persistence do not improve out-of-sample discrimination beyond basis level and ordinary price trend.
4. Compare continuation and reversion models rather than imposing a mean-reversion sign ex ante.
5. Test source-like episode counting against continuous-regression alternatives; ensure overlapping episodes do not inflate sample size.
6. Use leakage-safe rolling baselines and normalization. All state variables must use only data available at the completed signal bar.
7. Control for funding, OI change, realized volatility, volume shocks and contemporaneous returns. Reject a distinct basis-state interpretation if it merely relabels those variables.
8. Run timestamp-shift, spot-reference permutation and quote-mismatch placebos. Genuine basis structure should degrade under deliberately wrong references.
9. Evaluate BTC, ETH and other sufficiently liquid contracts separately; use walk-forward/OOS testing across bull, bear, high-volatility and low-volatility regimes.
10. Stress baseline length, normalization lookback, velocity lookback, persistence window, neutral band, widen margin and event horizon. Reject parameter-fragile results.
11. Apply realistic two-leg costs and funding to convergence implementations and one-leg costs to directional implementations. Reject economic alpha that disappears under plausible costs.

## Crypto portability

`direct`

The source itself targets crypto perpetual/futures versus spot markets, including BTC, ETH and liquid crypto pairs. Portability remains venue- and contract-dependent because funding, 24/7 trading, quote currencies, liquidity fragmentation, contract specifications and reference-symbol quality vary materially.

## Limitations

- `underspecified`: the reviewed public description does not expose every exact formula/default/threshold in the state score and reversion-proof engine.
- `not independently reproduced`.
- The source's on-chart historical reversion rate is not independent evidence of profitability and is market/timeframe dependent.
- Basis normalization can be contaminated by stale or mismatched spot references.
- A basis-spread forecast does not automatically imply outright directional return alpha.
- Research-proposed barriers/horizons can introduce researcher degrees of freedom and require strict OOS validation.

## Implementation status

Research record only. No implementation, backtest, robustness campaign, paper trading, testnet or live validation has been completed in our research stack.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply Research Intake Review passage, production-candidate admission, Qlib validation, profitability, validated alpha, survivor status, implementation approval, paper-trading approval, testnet approval or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-relative conceptual neighbors include existing spot/perpetual premium-level and premium-ROC records. This record is differentiated by its **stateful basis displacement + velocity + persistence construction and explicit reset-versus-further-widening race**.

## Sources

- TradingView — **Perpetual Basis Drift Map [AGPro Series]**, `AGProLabs`, public open-source script, page labels initial publication `May 14` and updates through `Aug 7`; year not inferred from the retrieved page; reviewed 2026-09-20: https://www.tradingview.com/script/nhDTQvJc-Perpetual-Basis-Drift-Map-AGPro-Series/
