---
schema: strategy-research-record-v1
title: Bitcoin Interaction-Weighted Social Sentiment LSMA Exhaustion
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
  - https://www.tradingview.com/script/79s2wd9X/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Interaction-Weighted Social Sentiment LSMA Exhaustion

## Provenance

Public TradingView open-source indicator: **BTC - Sentiment (Posts weighted) LSMA**, published by **Rob_Maths**. Stable source URL: https://www.tradingview.com/script/79s2wd9X/ . Source reviewed as of 2026-09-22.

The source uses TradingView's `LUNARCRUSH:BTC_SENTIMENT` feed. It describes that series as the percentage of positive posts weighted by interactions rather than a raw mention count.

## Economic mechanism

### Source-reported

The author argues that interaction-weighted Bitcoin social sentiment can proxy crowd conviction and that extreme social enthusiasm or apathy may become detached from price/fundamental conditions. The source frames low sentiment as an accumulation/apathy regime and high sentiment as an overheated/distribution regime, with social exhaustion potentially preceding reversals.

The source states that raw social data is noisy and applies a 28-day Least Squares Moving Average (LSMA) to denoise it. It describes the LSMA as a way to track sentiment shifts with less lag than a simple moving average.

### Research interpretation

The falsifiable hypothesis is that **interaction-weighted social sentiment contains incremental information about subsequent BTC returns or reversal probability after controlling for contemporaneous price trend, volatility and volume**. A second, separable hypothesis is that smoothing sentiment with a 28-day LSMA improves signal quality relative to raw sentiment or simpler smoothing.

A plausible behavioral mechanism is crowding/exhaustion: unusually high interaction-weighted optimism may coincide with late-stage demand and asymmetric downside risk, while unusually low optimism may coincide with depleted attention/selling and asymmetric rebound potential. This mechanism is a hypothesis, not an established fact.

Any directional trade rule, holding horizon, threshold optimization, or divergence rule beyond the source description is **research-proposed**.

## Signal

Source-described construction:

- Input: `LUNARCRUSH:BTC_SENTIMENT`, described as a 0-100 percentage of positive posts weighted by interactions.
- Smoothing: 28-day LSMA.
- Display normalization: `SHI = ((Current LSMA - 65) / 25) * 10`.
- Source-described low/apathy zone: sentiment below 72.5%.
- Source-described high/overheated zone: sentiment above 82.5%; the source also describes SHI above 8.5/10 as elevated flush risk.
- Neutral values are treated as a sustainable-growth / non-extreme region.

The source does **not** provide a complete executable strategy lifecycle. Exact entry timing, exit, holding period, re-entry, position sizing, stop logic and shorting rules are **underspecified**.

Research-proposed tests should keep at least three constructions separate rather than selecting the best after inspection:

1. low-extreme sentiment followed by BTC rebound / mean reversion;
2. high-extreme sentiment followed by BTC reversal / underperformance;
3. change or slope in the 28-day LSMA as a crowd-conviction acceleration/deceleration signal.

Signal formation must use only sentiment observations actually available at the decision timestamp. No same-period revised or delayed social observation may be treated as known earlier.

## Required data

- BTC spot or a clearly specified liquid BTC reference price.
- `LUNARCRUSH:BTC_SENTIMENT` or a point-in-time reconstruction of the same interaction-weighted sentiment field.
- Daily timestamps for the source's 28-day LSMA construction, with explicit timezone/candle-boundary handling.
- BTC OHLCV for baseline controls and subsequent-return labels.
- Point-in-time availability timestamps for the sentiment observations, including publication/update latency if applicable.
- Missing-data and feed-history policy.

A historical feed that has been revised, reclassified, backfilled, or whose interaction universe changed over time can create look-ahead or taxonomy drift. Those properties must be established before a valid backtest.

## Execution assumptions

The TradingView source is an indicator, not a fully specified execution strategy. It does not establish:

- same-bar versus next-bar execution;
- market versus limit orders;
- fees, spread or slippage;
- leverage or margin;
- short availability;
- capacity or market impact;
- stop/target logic;
- position sizing;
- a holding period.

For falsification, any conversion from a confirmed daily signal to a position should be **research-proposed** and executed no earlier than the first tradable timestamp after the sentiment observation is known. Costs must be applied to the chosen BTC venue/market type.

## Evidence

### Source-reported

The source states that BTC sentiment historically rarely falls below 60% or remains above 90% for long, and presents low sentiment as social apathy/accumulation context and high sentiment as overheated/distribution context. It does not provide a traceable backtest table, Sharpe ratio, CAGR, drawdown, sample specification, or independently auditable performance series for those claims.

The source specifies the 28-day LSMA and the 65-to-90 scaling range described above. These are source parameters, not independently validated optima.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-backed negative empirical result was identified on the reviewed TradingView page. Absence is not evidence of no negative result.

Material concerns include endogenous sentiment/price feedback, sentiment reacting to returns rather than leading them, changing social-platform composition, bot/manipulation exposure despite interaction weighting, LunarCrush methodology drift, and data availability/revision bias.

## Falsification plan

1. **Lead-lag test:** compare predictive performance for future BTC returns at predeclared horizons against contemporaneous and lagged BTC returns. Reject a lead-lag interpretation if sentiment adds no leakage-safe out-of-sample information beyond price history.
2. **Raw-vs-smoothing ablation:** compare raw sentiment, 28-day LSMA, a simple 28-day SMA, and LSMA slope. Reject the claimed value of LSMA denoising if it does not improve stability or OOS predictive utility relative to simpler constructions.
3. **Threshold ablation:** test the source's 72.5% and 82.5% zones without tuning, then evaluate broad neighboring threshold bands only as robustness checks. Reject threshold-specific alpha if performance depends on a narrow ex-post cutoff.
4. **Direction separation:** test low-sentiment rebound and high-sentiment reversal independently. Do not pool opposite tails into a favorable composite unless both survive independently or a predeclared symmetric rule survives.
5. **Price/volatility controls:** compare against BTC momentum, drawdown, realized volatility and volume baselines. If sentiment loses incremental information after these controls, treat it as a descriptive reaction proxy rather than alpha.
6. **Timestamp placebo:** shift sentiment observations forward/backward and test whether apparent performance improves under impossible timing. Any such pattern is evidence of timestamp leakage or data alignment error.
7. **Feed stability:** test subperiods and, where metadata permit, methodology/platform-composition regimes. Require the effect not to depend on one social-data era.
8. **Costs and turnover:** apply realistic execution costs for the chosen BTC market. Reject any implementable rule whose net OOS advantage disappears under conservative costs.

Failure of incremental leakage-safe OOS information versus simple price-only baselines should terminate the hypothesis rather than motivate additional indicator stacking.

## Crypto portability

**direct** — the source is explicitly Bitcoin-specific and uses a BTC social-sentiment feed.

Portability across BTC venues still requires care because the sentiment input is market-wide while execution prices, liquidity, fees and candle boundaries are venue-specific. Extension to ETH or other assets is unproven and should not inherit the BTC result.

## Limitations

- **Not independently reproduced.**
- Complete trading lifecycle is **underspecified**.
- The LunarCrush feed methodology, historical revision policy, constituent social platforms and point-in-time availability are not established by the reviewed TradingView page.
- Interaction weighting does not prove removal of bots, coordinated promotion or selection bias.
- Social sentiment may be endogenous to recent BTC returns and volatility.
- The source's historical statements about sentiment extremes are not accompanied by an auditable sample or performance table on the reviewed page.
- The 65/90 scaling anchors and 72.5/82.5 zones may be heuristic and require strict OOS falsification rather than optimization.

## Implementation status

Research capture only. No implementation in the research stack has been completed. No Qlib full backtest or independent reproduction was performed during this Scout run.

## Adoption boundary

This record is **research-only / not-implemented / not-approved**. Repository presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

No canonical Wiki record was consulted because this Scout is GitHub-only. Repository-level related concepts include time-series momentum, behavioral crowding, attention/sentiment, and reversal/mean-reversion research; relationship does not imply equivalence or validation.

## Sources

- Rob_Maths, **BTC - Sentiment (Posts weighted) LSMA**, TradingView open-source script, reviewed 2026-09-22: https://www.tradingview.com/script/79s2wd9X/
