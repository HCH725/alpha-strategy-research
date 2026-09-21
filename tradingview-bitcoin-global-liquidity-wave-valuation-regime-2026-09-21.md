---
schema: strategy-research-record-v1
title: Bitcoin Global Liquidity Wave Valuation Regime
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
  - https://www.tradingview.com/script/fQbceY5t-Bitcoin-Liquidity-Wave/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Global Liquidity Wave Valuation Regime

## Provenance

Public TradingView open-source indicator **Bitcoin Liquidity Wave**, author/page identity `PrismCharts`. Stable source: https://www.tradingview.com/script/fQbceY5t-Bitcoin-Liquidity-Wave/ . The page was reviewed on 2026-09-21 and displayed the publication age as three days; an exact calendar publication date was not exposed in the reviewed page text, so no more precise date is asserted.

This source is materially distinct from the repository's existing crypto macro liquidity-leverage-breadth regime record: this record isolates a Bitcoin/global-central-bank-liquidity valuation-and-impulse hypothesis with explicit source-described lags and fitted valuation bands, rather than a multi-family crypto regime dashboard.

## Economic mechanism

### Source-reported

The author values Bitcoin against a global liquidity index built from eleven series. The source describes the index as Federal Reserve total assets minus the U.S. Treasury General Account and overnight reverse repo, plus the balance sheets of the ECB, Bank of Japan, People's Bank of China, and Bank of England, with non-U.S. balance sheets converted to U.S. dollars at spot FX rates.

The source describes three layers:

- **Baseline:** log Bitcoin price modeled from log global liquidity, with liquidity read using a 60-day lead, plus a curved time/adoption term.
- **Wave:** the baseline shifted by a liquidity impulse defined from the smoothed 270-day change in log liquidity, applied with a 90-day lead.
- **Channel:** age-decaying upper/lower envelopes around the wave, with inner levels between the wave and outer levels.

The author states that the first part of the projection uses already-published liquidity data, while later projection values depend on an assumed liquidity growth rate.

### Research interpretation

The falsifiable hypothesis is that **changes in broad central-bank/system liquidity lead medium-horizon Bitcoin valuation pressure**, such that leakage-safe liquidity level and liquidity impulse contain incremental information for subsequent BTC returns or valuation reversion beyond Bitcoin's own trend, realized volatility, and calendar/adoption trend.

A second, separable hypothesis is that distance from a point-in-time liquidity-implied baseline/wave identifies overextension or underextension that subsequently mean-reverts. These are research hypotheses, not source-verified trading rules.

The economic interpretation must distinguish genuine liquidity information from two confounds: USD FX translation of foreign balance sheets and the fitted time/adoption term. If either explains the apparent relationship, the global-liquidity alpha thesis is weakened.

## Signal

### Source-specified construction

- Intended chart: daily Bitcoin; the source states weekly is also supported by converting day lookbacks to bars.
- Global liquidity index: Fed assets minus TGA minus overnight reverse repo, plus ECB, BOJ, PBOC, and BOE balance sheets converted to USD at spot FX.
- Baseline: log-price relation to log liquidity with a 60-day lead and a curved time/adoption term.
- Source states the default liquidity exponent is about 1.5.
- Liquidity impulse: smoothed 270-day change in log liquidity, applied with a 90-day lead.
- Projection: published liquidity is used for the first 60-90 days; beyond that, the source extends liquidity using trailing three-year growth by default or a user-selected fixed rate.
- The source says the fit coefficients were estimated by least squares on daily data from mid-2012 through September 2026, and envelope scaling was chosen against cycle extremes over that period.

### Source gaps

The reviewed public description does not specify a complete long/short entry rule, exit, holding period, re-entry rule, position sizing, transaction-cost model, or a source-validated trading threshold. It also does not expose enough detail in the description alone to reproduce every fitted coefficient and envelope equation without relying on source code redistribution. These items are **underspecified** as trading rules.

### Research-proposed operationalization

For falsification only:

1. Reconstruct the liquidity index point-in-time using publication timestamps and vintage values available at each decision date.
2. Test liquidity level and 270-day liquidity impulse separately before combining them.
3. Estimate any price/liquidity regression only on an expanding or rolling training window ending before the forecast timestamp; never use the source's full-sample fitted defaults as an out-of-sample signal.
4. Test forward BTC returns and drawdown conditional on liquidity impulse quantiles and standardized distance from the training-only liquidity-implied baseline.
5. Treat all quantile cutoffs, regression windows, distance thresholds, holding horizons, and trading mappings as `research-proposed`; any pass/fail cutoff is a `research-defined falsification threshold`.

No source-specified executable strategy is claimed.

## Required data

- BTC daily OHLCV, with a documented spot/index reference and UTC bar boundary.
- Federal Reserve total assets.
- U.S. Treasury General Account.
- Overnight reverse repo.
- ECB balance sheet.
- Bank of Japan balance sheet.
- People's Bank of China balance sheet.
- Bank of England balance sheet.
- Contemporaneous FX rates required to translate foreign balance sheets into USD.
- Original publication/release timestamps, revision/vintage history, missing-value handling, and frequency metadata for every macro series.
- A calendar alignment policy that prevents lower-frequency macro observations from being assigned to crypto bars before they were publicly available.

Exact TradingView symbol/provider mappings are not fully enumerated in the reviewed description and must not be silently substituted with economically different series.

## Execution assumptions

The source is a descriptive/valuation indicator and does not specify orders, fills, fees, spread, slippage, impact/capacity, leverage, funding, borrow, latency, or partial-fill behavior.

Any downstream experiment should form a macro feature only after all constituent observations used in that feature were publicly available. Trading no earlier than the next eligible BTC bar after feature availability is `research-proposed`. If implemented on perpetuals rather than spot/index BTC, funding and venue-specific execution costs must be added rather than attributed to the source.

## Evidence

### Source-reported

The source reports that its default fit coefficients were estimated by least squares on daily Bitcoin data from mid-2012 through September 2026 and that the channel envelope was scaled to cycle extremes over the same period. It explicitly characterizes the model as descriptive and fitted to past data, and warns that the coefficients may not hold in the future.

The source states that liquidity enters the baseline with an exponent of about 1.5 and describes the liquidity impulse as a smoothed 270-day log change. These are source-described model properties, not independently verified performance evidence.

No traceable Sharpe, CAGR, drawdown, hit rate, or out-of-sample trading result is reported in the reviewed description, so none is imported here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself provides material negative evidence: coefficients were chosen after the fact; the model is descriptive; later projections depend on assumed liquidity growth; foreign balance-sheet translation introduces USD-strength exposure; and the fit/envelope use the same historical period they describe.

No independent negative-result study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. **Point-in-time reconstruction:** use release-time macro vintages, not revised values aligned backward. Reject the thesis if the effect disappears under publication-safe timing.
2. **True OOS refit:** do not evaluate the source's 2012-September-2026 full-sample coefficients on that same interval as validation. Use expanding/rolling training windows and untouched forward periods.
3. **Baseline controls:** compare against BTC trend, realized volatility, calendar/time trend, and a simple buy-and-hold/return baseline. Liquidity must add incremental predictive information.
4. **Ablation:** test time/adoption term -> + liquidity level -> + liquidity impulse -> + valuation distance/channel. Retain only components that add stable OOS information.
5. **Lead sensitivity:** test predeclared lead/lag grids around the source-described 60- and 90-day relationships. A narrow optimum that collapses under small timing changes is evidence of overfit.
6. **FX confound:** test local-currency foreign balance sheets, USD-translated versions, and explicit DXY/broad-dollar controls. Reject a global-liquidity interpretation if the result is primarily an FX factor.
7. **Component ablation:** leave out Fed/TGA/RRP and each foreign central-bank component in turn. Require the result not to depend on one idiosyncratic series or one historical episode.
8. **Envelope falsification:** estimate channel parameters only from training data. Reject valuation-band alpha if extreme-touch/reversion behavior is not stable OOS.
9. **Regime robustness:** evaluate tightening/easing, bull/bear, high/low volatility, pre/post-2020, and ETF-era samples without retuning on the test period.
10. **Placebos:** shift macro release timestamps incorrectly, randomize component timing within low-frequency blocks, and compare unrelated macro aggregates. Correctly timed liquidity should outperform these placebos.
11. **Cost test:** for any research-proposed trading mapping, include fees, spread, slippage, turnover, and funding if perpetuals are used.

A failure to beat simple BTC trend/time controls in leakage-safe OOS tests should reject the predictive alpha interpretation rather than motivate more fitted layers.

## Crypto portability

**direct** for BTC because the cited source itself models Bitcoin. Portability to other crypto assets is **unproven** and should not be inferred from BTC results.

Important crypto-specific risks include 24/7 BTC bars versus scheduled macro releases, choice of BTC spot/index/perpetual reference, FX conversion timestamps, macro revisions, and the possibility that a medium-horizon macro relation does not survive venue-level execution costs or funding.

## Limitations

- `not independently reproduced`.
- `underspecified`: no complete source trading rule, execution model, or validated threshold.
- `data gap`: exact TradingView series/provider mappings and all fitted equations/coefficients are not fully enumerated in the reviewed public description.
- Severe in-sample/curve-fit risk because the source states coefficients were fit through September 2026 and channel extremes were scaled on the same historical period.
- Macro release/revision timing creates substantial look-ahead risk if historical revised series are naively aligned to BTC bars.
- USD conversion of foreign central-bank balance sheets embeds FX exposure.
- The time/adoption term can absorb long-run BTC appreciation and may make liquidity appear more explanatory than it is.
- Projection beyond already-published liquidity depends on an assumed growth path and must not be treated as observed information.

## Implementation status

Research capture only. No implementation in the research stack, Qlib full backtest, survivor validation, Paper, Testnet, or Live evaluation has been completed for this record.

## Adoption boundary

This artifact is research-only. Its presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard strategy, demonstrated profitability, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted. This GitHub-only Scout does not access local/Wiki dependencies and does not fabricate links.

## Sources

- TradingView, `PrismCharts`, **Bitcoin Liquidity Wave** (public open-source script page), reviewed 2026-09-21: https://www.tradingview.com/script/fQbceY5t-Bitcoin-Liquidity-Wave/
