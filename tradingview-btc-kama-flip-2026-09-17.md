---
schema: strategy-research-record-v1
title: "TradingView BTC KAMA Normalized Momentum Flip"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - momentum
  - kama
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/P3fyKd3i-KAMA-Flip-strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC KAMA Normalized Momentum Flip

## Provenance

Public TradingView open-source strategy **KAMA Flip strategy**, published by `SystemsOverFeelings` on 2025-11-29. Stable source URL: https://www.tradingview.com/script/P3fyKd3i-KAMA-Flip-strategy/. Source reviewed 2026-09-17. TradingView script identity: `P3fyKd3i`.

The author states that the strategy was originally built for BTC on the daily chart. The public description is sufficiently explicit to recover the high-level signal, but not the exact normalization formula or every KAMA input; those gaps are preserved below rather than inferred.

GitHub dedup against current `main` found no record for script ID `P3fyKd3i`, the canonical source identity, or a materially equivalent KAMA normalized-zero-line flip signal.

## Economic mechanism
### Source-reported

The author describes KAMA as adaptive to market efficiency: it speeds up when price moves directionally and slows when price is noisy. The strategy converts KAMA-derived momentum into a normalized oscillator around zero and trades when that momentum changes sign. The stated design objective is deliberately simple: enter on a momentum flip and use fixed stop-loss and take-profit exits rather than stacking confirmation indicators.

### Research interpretation

The falsifiable alpha hypothesis is **adaptive trend-transition persistence**: a sign change in normalized KAMA momentum may identify a transition from noisy/non-directional price action into a directional state early enough for subsequent returns to retain the new sign. KAMA's adaptive response is the predictive component; fixed percentage stop and take-profit rules are risk/holding logic rather than independent alpha.

The key empirical question is whether the normalized KAMA sign flip contains incremental forward-return information versus simpler momentum or moving-average-slope baselines after realistic costs.

## Signal

Source-reported logic:

- Indicator: Kaufman's Adaptive Moving Average (KAMA), transformed by the source into a normalized zero-line momentum oscillator.
- Long entry: normalized KAMA momentum flips from below zero to above zero.
- Short entry: normalized KAMA momentum flips from above zero to below zero.
- Direction can be configured as long-only, short-only, or both.
- Exit: 100% of the position closes at either a fixed percentage stop-loss or fixed percentage take-profit; no scaling, partial exit, or trailing exit is described.
- Author-reported BTC daily preference: lookback `40`, stop-loss `6%`, take-profit `3%`, with other settings described as standard/default. These are source-reported preferences, not independently optimized or verified here.
- The source states that KAMA parameters are user-adjustable.

Underspecified in the reviewed public description:

- exact mathematical normalization used to transform KAMA into the zero-line oscillator;
- exact KAMA fast/slow parameters corresponding to the author's `standard` settings;
- whether `lookback 40` is exclusively the normalization lookback or affects another component;
- exact bar-state/order-fill semantics for the zero crossing;
- pyramiding, re-entry behavior, position sizing and leverage.

`research-proposed` causal convention for later testing: calculate the oscillator using completed bars only, detect a confirmed sign change at bar close, and execute no earlier than the next tradable bar unless inspection of the public Pine source establishes different causal semantics. This convention is not source-reported.

## Required data

- Source-targeted instrument: BTC; the author specifically references the BTC daily chart.
- Venue and market type: underspecified; the source does not establish spot versus perpetual/futures.
- Timeframe: daily for the author's stated preferred BTC setup; the source notes that other charts can be tried but does not establish their efficacy.
- Required market fields: timestamped OHLC data sufficient for KAMA and the source's normalization. The reviewed prose does not state that volume, funding, open interest, order book or trade-level data enter the signal.
- Point-in-time requirement: KAMA and normalization inputs must use only observations available at signal formation; no future bars may enter the lookback or normalization range.
- Crypto candle boundary and venue must be fixed before reproduction because 24/7 daily bars can differ across data vendors.

## Execution assumptions

The source defines fixed percentage stop-loss and take-profit exits but does not specify order type, intrabar fill priority when both levels are touched, spread, fees, slippage, market impact, latency, partial fills, leverage/margin, or perpetual funding. Exact entry fill timing after a momentum flip is also underspecified.

For a causal backtest, stop/target collision within the same bar must use a predeclared conservative or higher-resolution fill rule rather than choosing the favorable outcome retrospectively. Perpetual implementations must separately model funding and liquidation mechanics.

## Evidence
### Source-reported

The author states that, for their use on a 1D BTC chart, the strategy works best with a `6%` stop-loss, `3%` take-profit and lookback `40`. This is an author-reported configuration preference from the TradingView page, not independent evidence of profitability. The reviewed description does not provide a traceable Sharpe ratio, CAGR, maximum drawdown, profit factor, sample interval, trade count, or statistically interpretable performance result, so none is asserted here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in this Scout cycle. The source itself provides no regime decomposition or cost sensitivity. The asymmetric source-preferred `6%` stop versus `3%` target requires a sufficiently high realized hit rate to overcome the unfavorable payoff ratio and trading costs; whether the KAMA flip provides that is unproven. Absence of additional negative evidence is not evidence of robustness.

## Falsification plan

1. Recover the exact normalization formula and KAMA defaults from the public Pine source before claiming exact reproduction; otherwise keep those parameters `underspecified` or label replacements `research-proposed`.
2. Reproduce the author's BTC daily configuration without post-hoc optimization, using point-in-time bars and explicit fees/slippage.
3. Compare normalized KAMA sign flips against simple controls: KAMA slope sign, price/KAMA cross, and conventional fixed-lookback return momentum using the same exit and cost model.
4. Run ablations separating the entry signal from the `6%` stop / `3%` target so risk logic is not mistaken for alpha.
5. Require out-of-sample coverage across BTC bull, bear, sideways and volatility regimes and split long/short legs.
6. Stress neighboring lookbacks and KAMA responsiveness parameters only after exact source specification is recovered; a narrow edge that disappears under small perturbations materially weakens the thesis.
7. Reject the hypothesis if the normalized flip does not improve cost-adjusted out-of-sample forward-return discrimination or risk-adjusted results relative to the simpler controls, or if results depend on favorable same-bar stop/target assumptions.

## Crypto portability

`direct` for BTC because the cited source explicitly states the strategy was built for BTC and gives a preferred BTC daily configuration. Extension to ETH, SOL or other crypto assets is `unproven` because the source only says other charts may be tried; it does not provide crypto-wide empirical evidence.

Spot versus perpetual implementation remains material: shorting feasibility, funding, mark/index pricing, leverage and liquidation differ, while 24/7 daily candle boundaries can change KAMA and normalization values.

## Limitations

- Exact KAMA normalization formula is `underspecified` in the reviewed prose.
- Exact default KAMA fast/slow settings are `underspecified`.
- Venue, market type, sizing, leverage and entry fill semantics are `underspecified`.
- Author-preferred `40 / 6% / 3%` settings are source-reported, not independently reproduced.
- No traceable source-reported risk-adjusted performance statistic is asserted.
- Not independently reproduced.
- Presence in this repository does not imply validated alpha or trading approval.

## Implementation status

`not-implemented`.

No backtest, quantitative runtime implementation, paper trading, testnet or live validation was performed in this Scout cycle.

## Adoption boundary

Research material only. This record is not evidence that the strategy is profitable or validated and is not approval for implementation, paper trading, testnet or live trading.

## Related Wiki records

No stable Hermes Wiki Brain record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `SystemsOverFeelings`, **KAMA Flip strategy**: https://www.tradingview.com/script/P3fyKd3i-KAMA-Flip-strategy/ (published 2025-11-29; public open-source strategy; reviewed 2026-09-17).
