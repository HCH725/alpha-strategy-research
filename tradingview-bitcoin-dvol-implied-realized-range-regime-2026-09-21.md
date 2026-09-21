---
schema: strategy-research-record-v1
title: Bitcoin DVOL Implied-vs-Realized Range Regime
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/QeNuwUuI-DVOL-based-Bitcoin-Volatility/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin DVOL Implied-vs-Realized Range Regime

## Provenance

Public TradingView open-source script **DVOL based Bitcoin Volatility**, author/page identity `splitmyIVandmelt`. Stable source: https://www.tradingview.com/script/QeNuwUuI-DVOL-based-Bitcoin-Volatility/ . The page was reviewed on 2026-09-21 and shows an update dated Apr 26. The source describes Bitcoin expected-range bands derived from Deribit DVOL alongside realized-volatility bands derived from HV7, HV14 and HV30.

Repository deduplication before capture found no record for this canonical TradingView source. Existing repository volatility-risk-premium/options records are related but materially distinct: this record isolates a spot-price range/regime hypothesis built from fixed-period DVOL and realized-volatility anchors rather than an options carry or variance-swap strategy.

## Economic mechanism
### Source-reported

The source describes DVOL as a forward-looking annualized volatility expectation derived from Deribit options pricing and compares it with trailing realized volatility. It states that the resulting implied and realized ranges provide structural reference levels: realized volatility below implied volatility indicates that options are pricing more movement than has recently been delivered, while realized volatility approaching or exceeding implied volatility indicates a higher-energy regime. It also highlights confluence between independently derived volatility bands as potentially meaningful reference zones.

### Research interpretation

The falsifiable hypothesis is that the ratio and geometry of point-in-time implied versus realized volatility contain incremental information about subsequent BTC spot path behavior. A low realized/implied ratio may identify compression in which price remains contained until a volatility transition; a ratio approaching or exceeding parity may identify expansion in which range breaks are more likely to continue. A separable hypothesis is that touches of fixed-period DVOL-derived expected-range boundaries exhibit non-random continuation or reversal behavior conditional on the implied/realized regime.

These directional interpretations are **research-proposed**. The source presents the bands primarily as a volatility map and does not specify a complete trading strategy.

## Signal

Source-described construction:

- **Instrument:** BTCUSD.
- **Implied-volatility input:** Deribit DVOL.
- **Realized-volatility inputs:** HV7, HV14 and HV30.
- **Daily anchor:** 00:00 UTC daily open; daily bands reset each day.
- **Weekly anchor:** Saturday opening price and DVOL reading at the start of the crypto week; weekly bands remain fixed for the seven-day period.
- **Monthly anchor:** first calendar-day open; monthly bands remain fixed for the month.
- **Weekly realized-volatility comparison:** HV14.
- **Monthly realized-volatility comparison:** HV30.
- **Daily realized-volatility comparison:** HV7.
- The source displays an HV14/IV ratio and labels values below 95% as realized volatility running below implied and values at or above 95% as realized volatility catching up to or exceeding implied.
- The source states that the indicator is intended for intraday BTCUSD charts and requires `DERIBIT:DVOL` access.

The source does not provide a complete entry, exit, holding-period, re-entry or position-sizing rule in its public description. Exact band-scaling implementation details are not relied upon here beyond the source-described concept; any reconstruction must be audited against the public script before testing.

Research-proposed operationalizations for falsification, not source rules:

1. Classify each fixed anchor period using only DVOL and realized volatility available at the anchor timestamp.
2. Test boundary-touch events separately for (a) continuation beyond the implied range and (b) reversal toward the anchor.
3. Condition those event studies on the point-in-time realized/implied ratio rather than choosing the winning direction after observing outcomes.
4. Execute no earlier than the first bar after a fully observed event/condition; exact execution timing remains research-proposed.

## Required data

- BTC spot OHLCV with reliable UTC timestamps and intraday bars.
- Deribit DVOL observations with point-in-time timestamps and no backfilled future values.
- Sufficient BTC return history to compute HV7, HV14 and HV30 using only data available at each signal timestamp.
- Calendar boundaries for 00:00 UTC, Saturday weekly anchors and first-of-month anchors.
- For robustness, multiple liquid BTC spot venues or a defensible composite/index to test venue dependence.
- Point-in-time data alignment is mandatory: DVOL and realized-volatility inputs must be those actually observable at the anchor/event timestamp.

## Execution assumptions

The source does not specify executable orders, fill model, fees, spread, slippage, market impact, leverage, margin, latency, partial fills or failure handling. It also does not define a complete trade lifecycle.

Any backtest must therefore treat execution as research-proposed and apply explicit spot/perpetual-specific costs rather than attributing frictionless event-study behavior to a tradable strategy. Same-bar fills using a boundary that was not known at the bar open are prohibited.

## Evidence
### Source-reported

The source describes the bands as useful structural volatility references and states that price respects the ranges imperfectly but sufficiently to be meaningful as reference. It does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate or other complete strategy-performance statistic on the reviewed public page. No quantitative profitability claim is adopted here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independently verified negative result was identified in the reviewed source; absence is not evidence of no negative result. The source itself does not establish that band touches predict direction, nor that an IV/HV regime adds return predictability after controlling for ordinary volatility and momentum.

## Falsification plan

1. **Leakage-safe anchor reconstruction:** freeze daily, weekly and monthly inputs at their stated anchor timestamps. Reject any implementation that allows later-period DVOL/HV values to alter an earlier fixed band.
2. **Baseline controls:** compare against unconditional BTC returns, simple distance-from-open, ATR/range bands, trailing realized volatility alone, and momentum/trend controls. The DVOL layer must add information beyond price-derived volatility.
3. **Ablation:** test `price/ATR baseline -> realized-volatility band -> DVOL implied band -> IV/HV ratio -> multi-horizon confluence`. Remove any layer that does not add stable out-of-sample information.
4. **Competing hypotheses:** pre-specify and test boundary continuation and boundary reversal separately. Do not pool opposite effects or choose direction ex post.
5. **Ratio robustness:** test the source-highlighted 95% region as source-reported context, but also evaluate broad neighboring thresholds without optimizing to a single best cutoff. Any Scout-chosen acceptance cutoff is a **research-defined falsification threshold**.
6. **Anchor robustness:** compare Saturday weekly anchoring with mechanically defined UTC weekly alternatives. If the effect exists only under one arbitrary boundary and is unstable nearby, materially weaken the thesis.
7. **Venue robustness:** repeat spot-path tests across liquid BTC venues/composites to distinguish a market-wide effect from one feed's microstructure.
8. **Regime robustness:** split high/low DVOL, trending/ranging, stress/non-stress and major-event periods. Require sign stability rather than one regime carrying the full result.
9. **Timestamp placebo:** shift DVOL observations or band anchors forward/backward by controlled offsets. Similar or stronger placebo results would weaken a causal/options-information interpretation.
10. **Out-of-sample:** freeze all definitions before the final evaluation window. If DVOL-derived variables do not improve leakage-safe out-of-sample predictive or economic performance over simpler price/HV baselines after costs, reject the added DVOL complexity.

## Crypto portability

direct

The source is explicitly designed for Bitcoin and Deribit DVOL. Portability to other crypto assets is unproven because equivalent liquid options-implied volatility indices may not exist, and BTC-specific option expiry/liquidity structure may not transfer. Crypto-specific risks include 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual price differences and timestamp synchronization between Deribit options data and spot execution data.

## Limitations

- **underspecified:** no complete source-defined trading lifecycle.
- **not independently reproduced:** no internal validation has been performed.
- **data gap:** exact point-in-time DVOL history and publication/availability behavior must be verified before backtesting.
- **unproven:** the source's visual/reference-level interpretation is not evidence of predictive alpha.
- The public description includes dynamic pivot trend channels; they are intentionally excluded from this normalized hypothesis because the distinct testable mechanism here is implied-versus-realized volatility and fixed-period expected ranges. Adding the trend channels without independent contribution evidence would confound the test.
- The source-highlighted 95% HV14/IV reading is descriptive context, not independently validated as an optimal trading threshold.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest have been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitability, or received Paper, Testnet or Live approval.

## Related Wiki records

No stable related Wiki record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — `splitmyIVandmelt`, **DVOL based Bitcoin Volatility**: https://www.tradingview.com/script/QeNuwUuI-DVOL-based-Bitcoin-Volatility/ (public open-source script; reviewed 2026-09-21).
