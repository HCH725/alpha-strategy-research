---
schema: strategy-research-record-v1
title: TradingView OI-Funding Capitulation Reversal Hypothesis
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
  - https://www.tradingview.com/script/jqCODXOQ-Liquidation-Hunter-OI-Funding/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView OI-Funding Capitulation Reversal Hypothesis

## Provenance

- Public TradingView open-source script: `Liquidation Hunter - OI & Funding`.
- Author/page identity: `Firsty_y`.
- Stable URL: https://www.tradingview.com/script/jqCODXOQ-Liquidation-Hunter-OI-Funding/
- TradingView publication label visible on the reviewed page: `Mar 2`; the retrieved page does not expose a year, so no publication year is inferred.
- Source reviewed as of 2026-09-23.
- Repository deduplication on current `main` found no artifact for this canonical TradingView source or the same normalized price-down + sharp-OI-down capitulation/reversal rule.

## Economic mechanism

### Source-reported

The source describes three OI/price states. Very elevated OI is characterized as an inflated market with liquidation risk; stable price with increasing OI is characterized as a position battle; and falling price together with sharply falling OI is characterized as liquidation in progress. For the last state, the author describes weak hands as having been removed, funding as having cooled, and presents it as a potential buying opportunity.

### Research interpretation

The falsifiable hypothesis is that a simultaneous price decline and unusually large OI contraction can identify forced long-position deleveraging/capitulation, after which short-horizon forward returns may mean-revert. Funding is potentially useful as a crowding/cooldown state variable, but the public page does not expose enough detail to assert its exact formula or threshold.

The important distinction is between **deleveraging after a price decline** and a generic oversold-price signal. If the OI contraction contains no incremental information beyond the contemporaneous price drawdown, the liquidation interpretation does not establish alpha.

## Signal

Source-reported normalized states from the reviewed public page:

- Very elevated/extended OI: liquidation-hunt risk context.
- Stable price + increasing OI: positioning battle / directional uncertainty.
- Falling price + sharply falling OI: liquidation state; the source presents this as a potential buy opportunity and states that funding has cooled.

The public page does not unambiguously expose the OI source/venue, OI normalization, lookback, threshold for `very long` or `falling sharply`, exact funding calculation, funding threshold, price-change threshold, timeframe, entry timestamp, exit, holding period, re-entry, sizing, stop, or take-profit. These fields are `underspecified` and are not invented here.

Research-proposed operationalization for later testing only: define price return and OI change using point-in-time aligned data; identify joint downside-price / negative-OI-change events using predeclared rolling quantiles or z-scores; then measure subsequent returns over multiple fixed horizons. Thresholds and horizons are research-proposed, not source-reported.

## Required data

- Crypto instrument with reliable derivatives open-interest history.
- Point-in-time OHLCV and open interest aligned to the same venue/contract and bar boundary.
- Funding-rate history if testing the source's funding-cooldown interpretation.
- Prefer perpetual-futures data; the source page does not expose a definitive venue contract.
- Timestamp/timezone and missing-data handling must prevent asynchronous OI/price observations from creating false events.

## Execution assumptions

The source page does not specify order type, same-bar versus next-bar execution, fill model, fees, spread, slippage, market impact, leverage, margin, funding treatment, latency, partial fills, or failure handling.

For any later backtest, execution after a completed signal bar and realistic fees/slippage should be treated as research-proposed assumptions. Same-bar favorable fills must not be inferred from the visual indicator.

## Evidence

### Source-reported

The source provides qualitative interpretation of OI/price states and calls falling price with sharply falling OI a liquidation condition and potential buying opportunity. No traceable performance statistic, Sharpe, CAGR, win rate, drawdown, or independent empirical sample is stated on the reviewed public page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified on the reviewed page; absence is not evidence of no negative result. OI decline can reflect voluntary position closure rather than forced liquidation, and falling price plus falling OI can continue during persistent deleveraging rather than reverse immediately.

## Falsification plan

1. Compare the joint price-down + OI-down event against price-drawdown-only and OI-contraction-only baselines.
2. Test whether adding funding state improves OOS forward-return information versus the joint price/OI event alone.
3. Separate mild OI reductions from extreme contractions using research-defined, predeclared rolling thresholds; reject the thesis if results require a narrow optimized threshold.
4. Test multiple liquid crypto perpetuals, venues, volatility regimes, and fixed forward horizons with walk-forward/OOS evaluation.
5. Control for simple momentum/mean-reversion, realized volatility, volume shocks, and broad-market BTC moves.
6. Apply realistic fees, spread, slippage, and funding. If any apparent edge disappears under plausible costs, reject tradability.
7. Require the OI component to provide stable incremental OOS information over price-only capitulation. Failure means discard the OI-liquidation alpha interpretation rather than add filters.

All thresholds, horizons, controls, and acceptance criteria above are research-proposed; any eventual numerical cutoff is a `research-defined falsification threshold`.

## Crypto portability

`direct` as a research hypothesis: the cited source itself is framed around open interest, funding, liquidation, and leveraged-market behavior applicable to crypto derivatives. Portability across venues remains unproven because OI construction, funding conventions, contract specifications, and liquidation mechanics differ by exchange.

## Limitations

- `underspecified`: exact formulas, thresholds, lookbacks, timeframe, venue and lifecycle are not fully exposed by the reviewed public page.
- `data gap`: no verified liquidation-feed data is supplied; OI contraction is a proxy for position reduction, not proof of forced liquidation.
- `not independently reproduced`.
- `unproven`: the source provides no traceable performance evidence on the reviewed page.
- Funding cooldown is source commentary, but its exact operational definition is not exposed and must not be invented.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed for this record.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView — `Liquidation Hunter - OI & Funding`, author `Firsty_y`: https://www.tradingview.com/script/jqCODXOQ-Liquidation-Hunter-OI-Funding/ (reviewed 2026-09-23).
