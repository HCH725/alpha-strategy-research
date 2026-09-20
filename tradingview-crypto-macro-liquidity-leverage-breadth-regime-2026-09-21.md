---
schema: strategy-research-record-v1
title: Crypto Macro Liquidity-Leverage-Breadth Regime Filter
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-06-20
sources:
  - https://www.tradingview.com/script/PFbmeGww-Crypto-Macro-Heatmap-invincible3/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Macro Liquidity-Leverage-Breadth Regime Filter

## Provenance

Public TradingView open-source indicator **Crypto: Macro Heatmap [invincible3]**, author/page identity `invincible3`. The page states an initial publication date of June 11 and a June 20 update; the page was reviewed on 2026-09-21 and its latest visible update is 2026-06-20. Stable source: https://www.tradingview.com/script/PFbmeGww-Crypto-Macro-Heatmap-invincible3/ .

The source is a macro-regime dashboard rather than a complete execution strategy. This record therefore preserves a falsifiable regime-filter hypothesis and does not infer a source-specified trading system where none is supplied.

## Economic mechanism

### Source-reported

The author describes a crypto market-regime dashboard that converts multiple data sources into normalized 0-100 scores and summarizes conditions as risk-on, neutral, or risk-off. The dashboard groups information into three sections:

- **Liquidity:** Global M2, total crypto market capitalization, USDT dominance, and BTC volume confirmation.
- **Leverage:** open-interest pressure, a funding-risk proxy, a liquidation-risk proxy, and OI acceleration.
- **Breadth:** TOTAL2, TOTAL3, BTC dominance, ETH dominance, and altcoin participation.

The source says the composite score combines liquidity support, market breadth, and leverage-adjusted risk, and is intended for higher-timeframe regime context rather than direct buy/sell signals. It also reports a confidence score, section changes versus seven days earlier, market-phase detection, and risk-state classification.

### Research interpretation

The falsifiable hypothesis is that **crypto trend/momentum outcomes are conditional on agreement or conflict among liquidity support, breadth participation, and leverage stress**, and that a point-in-time composite regime state can add predictive information beyond price trend and volatility alone.

A coherent mechanism is plausible but unverified: broad liquidity and participation may support persistent risk-taking, while high leverage stress may make otherwise bullish conditions fragile and increase squeeze/reversal risk. Conversely, improving breadth and liquidity while leverage stress falls may represent a healthier continuation regime than price strength alone.

The strongest research question is not whether the source's dashboard score is visually useful, but whether its component families provide incremental out-of-sample information after controlling for BTC trend, realized volatility, and market-cap momentum. Any operational rule below that is not explicitly specified by the source is labeled `research-proposed`.

## Signal

### Source-specified state construction

- Signal formation is based on the source's normalized liquidity, leverage, and breadth components and their composite regime score.
- The source explicitly uses daily external-data requests after its June 20 update.
- It reports section deltas versus seven days earlier.
- It classifies the broader market into risk-on, neutral, or risk-off context and provides market-phase/risk-state outputs.
- The June 20 update warns when less than 180 days of data are available and states that some metrics may then fall back to neutral values.

### Source gaps

The public description does not unambiguously disclose all normalization equations, weights, component thresholds, market-phase boundaries, confidence-score formula, exact funding/liquidation proxy construction, entry/exit rules, holding period, re-entry rules, or position sizing. These are **underspecified** and must not be invented as source rules.

### Research-proposed operationalization

For falsification only, construct point-in-time component families matching the source-described inputs and test them as regime filters rather than direct orders:

1. At each confirmed daily timestamp, compute leakage-safe liquidity, leverage, and breadth features using only data actually available by that timestamp.
2. Normalize each feature with trailing-only distributions; exact windows and weighting schemes are hyperparameters to be declared before each experiment, not attributed to the source.
3. Test individual families first, then an equal-weight family composite, then alternative predeclared weighting schemes.
4. Test whether subsequent BTC/ETH and broad-alt returns, trend persistence, drawdown, and realized volatility differ materially across composite regime quantiles/states.
5. Separately test **regime level** and **7-day regime change** so that a static high score is not conflated with improving conditions.

No source-specified long/short entry, exit, holding, sizing, or execution rule exists in the reviewed description.

## Required data

- Crypto market prices and OHLCV for BTC, ETH, and the intended test universe.
- Global M2 series with original publication/revision timestamps if used.
- Total crypto market-cap series and point-in-time methodology.
- USDT dominance.
- TOTAL2 and TOTAL3 or reconstructable point-in-time equivalents.
- BTC and ETH dominance.
- Altcoin-participation/breadth inputs; exact source definition is underspecified.
- Perpetual open interest and OI changes/acceleration.
- Funding data or a documented funding-risk proxy; exact source proxy is underspecified.
- Liquidation data or a documented liquidation-risk proxy; exact source proxy is underspecified.
- BTC volume.
- UTC timestamps and explicit daily bar boundaries.
- Point-in-time availability metadata for macro and market-cap series, including revisions and missing observations.

The source's TradingView symbols/feed mappings are not fully enumerated in the public description. Reproduction must document the exact provider/symbol lineage rather than silently substituting economically different series.

## Execution assumptions

The source does not specify an executable strategy. It omits signal-to-order timing, market versus limit orders, fill model, fees, spread, slippage, impact/capacity, funding treatment for traded perpetuals, leverage/margin, borrow/shorting, latency, partial fills, and failure handling.

For any downstream experiment, a conservative default is `research-proposed`: form daily regime features only after all required observations for that timestamp are available and permit trading no earlier than the next eligible bar. If the experiment trades perpetuals, include realized funding, fees, spread, and slippage. No same-bar use of data published after the decision timestamp is permitted.

## Evidence

### Source-reported

The source describes the dashboard architecture and intended regime interpretation but does not report a traceable backtest, Sharpe ratio, CAGR, drawdown, hit rate, or other verified performance statistic for a trading rule. No performance claim is therefore imported into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly warns that with less than 180 days of available history some metrics may fall back to neutral values. This creates a material risk that apparent historical states depend on data availability rather than economics.

No independent negative-result study was identified in the reviewed source. Absence is not evidence of no negative result.

## Falsification plan

1. **Baseline:** compare against BTC/ETH price trend, realized volatility, and total-market-cap momentum. Reject the composite as useful alpha context if it does not add stable out-of-sample information beyond these simpler controls.
2. **Ablation:** test price baseline -> + liquidity -> + breadth -> + leverage, then all permutations of the three component families. A complicated composite is not justified if one simple component explains the result.
3. **Level versus change:** separately test composite level and 7-day section/composite change. Require incremental information from the change term before retaining it.
4. **Leverage stress interaction:** test whether high leverage weakens continuation or increases tail risk conditional on otherwise strong liquidity/breadth. Reject this mechanism if interaction signs are unstable across BTC, ETH, and liquid altcoin cohorts.
5. **Point-in-time macro audit:** Global M2 and any revised macro series must use release-time vintages. Repeat without Global M2. If the effect disappears only when leakage-safe vintages are used, reject it.
6. **Market-cap/breadth survivorship audit:** reconstruct TOTAL2/TOTAL3/alt breadth point-in-time where possible. Do not use today's constituent set to manufacture historical breadth.
7. **Proxy audit:** replace funding/liquidation proxies with direct historical funding, OI, and liquidation data where available. Require the claimed leverage-state result to survive materially reasonable proxy choices.
8. **Missing-history test:** explicitly flag observations with less than 180 days of source-equivalent history and exclude/falsify neutral fallback artifacts.
9. **Placebos:** shuffle component labels within volatility regimes and lag macro/breadth inputs by deliberately incorrect offsets. Genuine timing information should beat these placebos.
10. **OOS/regime robustness:** use walk-forward evaluation spanning bull, bear, high-volatility, low-volatility, deleveraging, and broad-alt participation regimes. Predeclare thresholds and do not optimize on the final test window.
11. **Cost test:** if the regime is used to trade or rotate positions, include fees, spread, slippage, funding, and turnover. Reject any implementation whose incremental net performance is not robust to conservative costs.

Failure of the composite to outperform simple controls on leakage-safe out-of-sample tests should result in rejection or reduction to the surviving simpler component, not additional indicator stacking.

## Crypto portability

**direct** for the research hypothesis because the cited source itself is explicitly crypto-specific and uses crypto liquidity, leverage, dominance, market-cap, and breadth inputs.

Portability is not uniform across venues or eras. OI/funding/liquidation coverage differs by exchange; TOTAL2/TOTAL3 and dominance methodology can change; crypto trades 24/7 while Global M2 is lower-frequency macro data; and daily candle boundaries must be standardized. These differences require explicit timestamp and feed lineage controls.

## Limitations

- `underspecified`: complete normalization formulas, weights, thresholds, confidence formula, and some proxy definitions are not exposed in the reviewed public description.
- `not independently reproduced`.
- `data gap`: historical point-in-time Global M2 vintages, crypto market-cap methodology, breadth membership, liquidation feeds, and exchange OI/funding coverage may differ from TradingView's historical series.
- Composite dashboards have substantial multiple-component and overfitting risk.
- Correlated inputs can create apparent confirmation without independent information.
- Macro data frequency and publication lag can create look-ahead bias if naively aligned to daily crypto bars.
- The source is explicitly a regime-context tool, not a source-specified trading strategy.

## Implementation status

Research capture only. No implementation in the research stack, Qlib full backtest, survivor validation, Paper, Testnet, or Live evaluation has been completed for this record.

## Adoption boundary

This artifact is research-only. Its presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard strategy, demonstrated profitability, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted here. GitHub-only operation prevents local/Wiki lookup, and no link is fabricated.

## Sources

- TradingView, **Crypto: Macro Heatmap [invincible3]**, author `invincible3`, public open-source script, initial page date June 11, latest visible update June 20, reviewed 2026-09-21: https://www.tradingview.com/script/PFbmeGww-Crypto-Macro-Heatmap-invincible3/
