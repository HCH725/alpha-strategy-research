---
schema: strategy-research-record-v1
title: TradingView Vol-of-Vol Regime as a Conditional Alpha State Variable
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/nbjI1KmY/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Vol-of-Vol Regime as a Conditional Alpha State Variable

## Provenance

- Public TradingView open-source indicator: **Vol-of-Vol Regime** by `outofsamplelab`.
- Stable source URL: https://www.tradingview.com/script/nbjI1KmY/
- Source reviewed as of 2026-09-23.
- The public page displays `Jul 13` but the reviewed page does not unambiguously expose the publication year, so no year is asserted here.
- The source explicitly describes the script as a regime-measurement panel, not a buy/sell system, and states that it is non-repainting on confirmed bars.
- GitHub deduplication on current `main` found no record for this canonical TradingView source and no materially identical vol-of-vol percentile-regime record.

## Economic mechanism

### Source-reported

The source measures whether realized volatility itself is stable or unstable. It first computes a short rolling realized-volatility series, then computes the standard deviation of that volatility over a longer window as vol-of-vol. Both realized volatility and vol-of-vol are ranked into Low / Normal / High / Extreme percentile buckets. The author presents this as a way to identify periods when the volatility regime itself is unstable and explicitly does not claim a buy/sell signal or performance result.

### Research interpretation

**Research-proposed hypothesis:** vol-of-vol may be useful as a conditional state variable rather than standalone directional alpha. When vol-of-vol is unusually high, the distribution of short-horizon returns and the reliability of simple trend-following or mean-reversion signals may differ from low/stable-vol-of-vol regimes because volatility is changing rapidly rather than merely sitting at a high level.

A falsifiable form is: conditioning a pre-specified simple directional signal on lagged vol-of-vol percentile should produce materially different forward-return distributions or signal efficacy after controlling for realized-volatility level itself. If vol-of-vol adds no incremental information beyond realized volatility, the hypothesis fails.

This interpretation is introduced by the Scout and is not a source-reported trading rule.

## Signal

The source itself supplies a **regime variable**, not an executable strategy.

Source-supported construction:

1. Compute short rolling realized volatility from confirmed bars.
2. Compute the standard deviation of that realized-volatility series over a longer window: vol-of-vol.
3. Rank realized volatility and vol-of-vol by percentile.
4. Map percentile ranks into Low / Normal / High / Extreme regime buckets.

The reviewed public description does not expose exact short-window length, long vol-of-vol window, percentile lookback, or bucket cutoffs. These are **underspecified** and must not be invented.

**Research-proposed operationalization for falsification only:** after independently reconstructing the source parameters, use the lagged vol-of-vol regime as a conditioning variable for simple pre-registered baselines such as time-series momentum and short-horizon mean reversion. Evaluate forward returns and baseline-signal performance separately by vol-of-vol bucket. This is not source-reported and is not approved implementation logic.

- Formation timing: confirmed-bar data only according to the source; any test must lag the completed regime calculation before measuring subsequent returns.
- Entry / short entry: not specified by source.
- Exit / holding period: not specified by source.
- Re-entry: not specified by source.
- Position sizing: not specified by source.
- Exact parameters: underspecified in the reviewed public description.

## Required data

- Instrument / universe: source is generic across chart symbols; crypto testing is research-proposed.
- Market type: spot or perpetual may be tested separately; source does not prescribe one.
- OHLC price bars sufficient to reconstruct the source's realized-volatility estimator.
- Confirmed timestamps and consistent candle boundaries.
- Exact source parameter values are a **data gap** until independently reconstructed from the public script.
- For perpetual-futures tests, funding and mark/index conventions are required for realistic net-return evaluation even though they are not inputs to the regime indicator.
- Point-in-time requirement: each regime label must use only information available by the signal-formation timestamp; percentile estimation must not use future observations.

## Execution assumptions

The source provides no trading lifecycle and therefore no execution model.

Any later strategy test must specify signal-to-order lag, next-bar versus same-bar execution, fees, spread, slippage, impact, funding for perpetuals, leverage/margin, and partial-fill assumptions. Same-bar execution based on a completed-bar regime value must not be assumed unless timing makes it feasible.

## Evidence

### Source-reported

The source reports the indicator construction and intended use as a volatility-regime measurement panel. It explicitly states that it does **not** generate buy or sell signals and gives no performance guarantee. No source-reported Sharpe, CAGR, win rate, drawdown, or predictive statistic was identified on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself provides no evidence that vol-of-vol predicts return direction or improves another alpha signal. A high vol-of-vol reading may simply restate information already captured by realized-volatility level, recent large returns, or volatility clustering. Percentile buckets can also be highly sensitive to estimation window, timeframe, and regime history. Absence of a source-reported trading test is a material evidence gap.

## Falsification plan

1. **Reconstruct before testing:** independently recover the exact realized-volatility estimator, short window, vol-of-vol window, percentile lookback, and bucket boundaries from the public script. If reconstruction is ambiguous, do not substitute convenient parameters without labeling them `research-proposed`.
2. **No-look-ahead:** calculate percentiles from trailing observations only and apply the completed regime no earlier than the next executable timestamp.
3. **Incremental-information test:** compare models/conditional sorts using realized volatility alone versus realized volatility + vol-of-vol. Reject the incremental-state thesis if vol-of-vol does not add stable OOS information.
4. **Baseline ablation:** test simple momentum and mean-reversion baselines unconditioned, conditioned only on realized-volatility bucket, and conditioned on both realized volatility and vol-of-vol. The composite conditioning must beat the simpler controls OOS to justify itself.
5. **Direction agnostic:** pre-register both continuation and mean-reversion possibilities. Do not label High/Extreme vol-of-vol bullish or bearish ex ante.
6. **Parameter robustness:** vary estimation windows and percentile boundaries around the reconstructed source settings. Reject a result that exists only at a narrow parameter choice.
7. **Timeframe robustness:** test multiple liquid-crypto bar sizes with strict timestamp alignment; do not pool incompatible candle boundaries.
8. **Market/venue robustness:** replicate across liquid BTC/ETH spot and perpetual venues where point-in-time data quality is adequate.
9. **Regime balance:** report sample counts and event clustering by bucket so a small number of crisis episodes cannot masquerade as a general effect.
10. **Cost sensitivity:** for any executable conditional strategy, include realistic fees, spread, slippage and perpetual funding. Reject tradable-alpha claims that disappear after costs.
11. **Frozen OOS:** choose all construction and conditioning rules before final out-of-sample evaluation. Failure to improve the strongest simple baseline OOS means the conditional-alpha hypothesis is rejected; do not rescue it by stacking additional filters.

## Crypto portability

**direct** for measurement: the source construction is instrument-agnostic and can be calculated directly from crypto OHLC data.

**unproven** for alpha: the source does not demonstrate that vol-of-vol predicts crypto returns or improves a crypto strategy. Crypto-specific risks include 24/7 candle-boundary choices, venue fragmentation, perpetual funding, mark/index versus traded-price differences, and crisis-event concentration.

## Limitations

- `underspecified`: exact source windows, percentile estimation horizon, and regime thresholds are not exposed in the reviewed public description.
- `not independently reproduced`: neither the indicator nor any proposed conditional-alpha test was reproduced in this Scout cycle.
- `data gap`: no source-reported predictive-return or strategy-performance evidence.
- `unproven`: incremental alpha beyond realized-volatility level and simple price signals.
- The proposed directional use is a Scout research hypothesis, not a claim made by the TradingView author.

## Implementation status

No implementation in the research stack has been completed. No backtest was run in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. This record has not passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, become a frozen survivor or leaderboard entry, or received Paper, Testnet, or Live approval. It must not be represented as profitable, validated alpha, or approved trading logic.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — schema reference only; no Wiki access or write was performed in this GitHub-only Scout cycle.
- No additional Wiki relationship was asserted because this Scout is GitHub-only.

## Sources

- TradingView — **Vol-of-Vol Regime**, `outofsamplelab`: https://www.tradingview.com/script/nbjI1KmY/ (reviewed 2026-09-23).
