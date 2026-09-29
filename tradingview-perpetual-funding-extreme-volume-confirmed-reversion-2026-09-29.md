---
schema: strategy-research-record-v1
title: TradingView Perpetual Funding-Extreme Reversion with Volume Confirmation
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://www.tradingview.com/script/u4emyPXd/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Perpetual Funding-Extreme Reversion with Volume Confirmation

## Provenance

Public, traceable TradingView page **Funding Rate Strategy Indicator** by `RolinLong`, published 2025-05-03. Stable source: https://www.tradingview.com/script/u4emyPXd/ . Source reviewed 2026-09-29.

TradingView labels the script protected-source. This record therefore normalizes only rules stated on the public page and does not infer hidden Pine implementation details.

## Economic mechanism

### Source-reported

The author describes perpetual-swap funding as a market-sentiment measure and uses extreme negative funding for long conditions and extreme positive funding for short conditions. A volume-increase filter is intended to confirm participation, and an optional 4-hour session filter controls when signals can trigger.

### Research interpretation

The falsifiable alpha hypothesis is contrarian crowding reversion: unusually negative funding may represent crowded short positioning vulnerable to reversal, while unusually positive funding may represent crowded long positioning vulnerable to reversal. The volume condition is a confirmation component, not independent evidence of alpha. The 4-hour gate and daily signal cap are timing/frequency controls.

This interpretation does not establish that the source thresholds are correctly scaled for any exchange-native funding series. That mapping must be verified before testing.

## Signal

Source-reported public-page rules:

- Funding input can be an external exchange funding series (example: Binance), a manual custom value, or simulated sine-wave test data. Only real point-in-time exchange funding is relevant to the research hypothesis; simulated data is not evidence.
- Long condition: funding rate <= `-2.0`.
- Short condition: funding rate >= `+2.0`.
- Volume confirmation: volume increase of at least 5% versus the prior bar.
- Optional 4-hour session filter: signals only on a new 4-hour bar; source default is enabled.
- Maximum signals per day: 5.
- Long funding exit: funding rises above `-0.5`.
- Short funding exit: funding falls below `+0.5`.
- Source also exposes fixed take-profit 5%, stop-loss 3%, optional trailing stop (default off), trailing distance 2%, weekend permission, and 10%-of-equity sizing. These are risk/execution controls, not treated as predictive alpha.
- The page says funding dynamics are smoothed but does not specify the smoothing transformation in the reviewed public prose: `underspecified`.
- Exact precedence when a funding exit and price-based TP/SL occur together is `underspecified`.
- Exact signal-to-fill timestamp is `underspecified`.

No hidden source-code behavior is inferred.

## Required data

- Instrument: perpetual swaps; BTCUSDT is given as an example.
- Market type: crypto perpetual derivatives.
- Funding: point-in-time exchange-native funding observations with explicit units and settlement timestamps.
- OHLCV: at least close and volume; price fields are also required for the source's TP/SL/trailing controls.
- Timeframe: source optionally gates entries to new 4-hour bars; underlying chart timeframe and funding-to-bar alignment are otherwise `underspecified`.
- Venue: an external real exchange feed such as Binance is described, but a single mandatory venue is not specified.
- Timestamp/timezone and publication-lag convention: `data gap`.
- Funding series scaling must be preserved exactly; do not mix percent, decimal, annualized, per-settlement, premium-index, or simulated units.

## Execution assumptions

Source-reported defaults include 10% equity sizing, 5% take profit, 3% stop loss, trailing stop disabled by default, 2% trailing distance when enabled, up to five signals per day, and weekend trading allowed.

The public page does not specify order type, same-bar versus next-bar fill, bid/ask treatment, spread, slippage, market impact, liquidation model, leverage/margin, partial fills, latency, or exact commission setting. These remain `underspecified`.

Funding cashflows while the position is held must be included in any reproduction; treating funding only as a signal while omitting realized funding P&L would be economically inconsistent. This requirement is `research-proposed`.

## Evidence

### Source-reported

The public page describes the rule set and defaults but provides no source-traceable Sharpe, CAGR, drawdown, win-rate, or other empirical performance statistic used in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself warns that real funding rates may differ from simulated/custom inputs and instructs users to verify commission/slippage settings.

Repository-adjacent research already contains several funding-extreme and funding-reversion hypotheses, so funding contrarianism is not novel by itself. The potentially distinct object here is the source-specific combination of absolute funding extremes, prior-bar volume expansion, optional 4-hour gating, and explicit funding-normalization exits.

No independent evidence was found in this Scout cycle that this exact combination adds predictive value. Absence is not evidence of no negative result.

## Falsification plan

1. First resolve the exact units and smoothing used by the real funding input. If `-2.0/+2.0` cannot be mapped unambiguously to exchange-native point-in-time funding without guessing, stop reproduction and classify the source as operationally underspecified.
2. Reproduce the source rule causally with funding observations available only after their actual publication/settlement timestamp.
3. Ablate the components: funding-only; funding + volume; funding + 4-hour gate; funding + volume + 4-hour gate. The volume/gating additions must demonstrate incremental out-of-sample value rather than merely lower trade count.
4. Compare fixed absolute thresholds with causally estimated rolling funding quantiles. Quantile rules are `research-proposed`, not source-reported.
5. Include realized funding cashflows, fees, spread and slippage; test spot/perpetual basis and liquidation-sensitive regimes separately.
6. Use walk-forward/out-of-sample testing across multiple liquid perpetual contracts and at least two venues if compatible point-in-time funding data are available.
7. Stress threshold neighborhoods rather than validating only the published defaults.
8. **Research-defined falsification threshold:** reject the composite alpha hypothesis if its net out-of-sample risk-adjusted performance is non-positive, or if the volume-confirmed variant does not improve on the funding-only baseline after controlling for trade frequency and costs.

## Crypto portability

`direct` for the broad mechanism because the source explicitly targets crypto perpetual swaps and names BTCUSDT as an example.

Portability across venues is still unproven. Funding definitions, settlement cadence, caps/floors, premium construction, contract specifications, mark/index conventions, fee tiers and liquidation mechanics differ by venue. The source's absolute thresholds must not be transferred across feeds without unit verification.

## Limitations

- Protected source: hidden Pine implementation cannot be audited from the public page.
- Funding smoothing: `underspecified`.
- Funding units/scaling behind the displayed thresholds: materially important and `underspecified`.
- Signal-to-order and fill timing: `underspecified`.
- Full cost, spread, slippage, leverage, margin and liquidation model: `data gap`.
- The volume filter uses a one-bar percentage change rather than a volume-normalized cross-venue measure; robustness is `unproven`.
- Absolute funding thresholds may be feed-specific.
- Not independently reproduced.

## Implementation status

Research capture only. No implementation in the research stack, no Qlib full backtest, and no independent reproduction were performed by this Scout.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`.

Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain link was resolved or fabricated in this GitHub-only run.

## Sources

- TradingView — RolinLong, **Funding Rate Strategy Indicator**, published 2025-05-03, reviewed 2026-09-29: https://www.tradingview.com/script/u4emyPXd/
