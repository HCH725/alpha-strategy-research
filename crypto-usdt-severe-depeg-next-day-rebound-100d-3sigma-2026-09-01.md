---
schema: strategy-research-record-v1
title: Crypto USDT Severe-Depeg Next-Day Rebound (100-Day Rolling 3-Sigma)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - stablecoin
  - event-driven
  - mean-reversion
  - liquidity-stress
status: research-only
confidence: medium
source_as_of: 2024-11-03
sources:
  - "https://doi.org/10.1111/acfi.70201"
  - "https://onlinelibrary.wiley.com/doi/10.1111/acfi.70201"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The source reports robust next-day rebound effects only for severe negative USDT depegging; at the rolling 1-sigma threshold the lagged rebound is not statistically significant, so the effect is state- and threshold-dependent rather than a generic depeg reversal rule."
---

# Crypto USDT Severe-Depeg Next-Day Rebound (100-Day Rolling 3-Sigma)

## Provenance

Primary source: Sean Foley, Seung Ah Lee, and George Milunovich, *How Tether Depegging Affects Cryptocurrency Returns*, *Accounting & Finance*, volume 66, issue 2, 1101-1129 (2026). First published 2026-03-08. DOI: https://doi.org/10.1111/acfi.70201.

The paper studies Tether (USDT) deviations from the USD peg and daily returns of BTC, ETH, XRP, DOGE, TRX, BNB, ADA, LTC, XMR, and XLM. The reported sample spans November 2017 through early November 2024; regression tables use return observations from 2017-11-11 through 2024-11-02, with the paper's subsample split extending through 2024-11-03.

This record focuses only on the source's **rolling-window severe negative-depeg lag effect**: after a USDT downside depeg exceeding three rolling standard deviations, the following day's cryptocurrency returns are positive across all ten studied assets. This is distinct from same-day contagion and distinct from stablecoin-supply or Stablecoin Supply Ratio signals already present in the pool.

## Economic mechanism

### Source-reported

The paper interprets stablecoin depegging as a liquidity and confidence shock. Because USDT functions as a major settlement, collateral, and funding instrument across crypto markets, severe downside depegging can transmit stress through withdrawals of liquidity, forced deleveraging, and confidence deterioration.

The authors report that cryptocurrency returns fall on the depegging day, with larger negative effects as the downside depeg becomes more severe. They also report that the lagged effect after severe negative depegging turns positive. Under the 100-day rolling-window method with a 3-standard-deviation threshold, the lag coefficient is positive and statistically significant for all ten cryptocurrencies, and the paper states that the rebound magnitude is roughly comparable to the initial decline.

### Research interpretation

The falsifiable alpha hypothesis is an **event-conditioned one-day mean-reversion effect after exceptional USDT stress**. A severe USDT downside depeg may force rapid deleveraging, inventory liquidation, and generalized risk-off selling across major crypto assets. If that first-day move overshoots the persistent information content of the stablecoin shock, a partial rebound may occur during the next 24-hour interval as collateral conditions normalize, arbitrage restores the peg, or panic selling exhausts itself.

This is not a generic "buy every depeg" rule. The source's own rolling 1-sigma specification does **not** show a statistically significant next-day rebound. The hypothesis is specifically tied to **rare, severe downside deviations**.

## Signal

Source-backed research reconstruction:

1. **Reference asset:** USDT/USD or a defensible USD-parity price index for Tether.
2. **Frequency:** daily.
3. **Rolling state estimation:** use the most recent 100 daily observations to estimate the time-varying mean and standard deviation of the USDT log-price series.
4. **Negative depeg event at day `t`:**

   `D_below(t) = 1` when

   `log(P_USDT,t) < mu_100(t) - 3 * sigma_100(t)`.

   The exact inclusion convention for day `t` in the rolling mean/variance must be matched to the paper before claiming exact reproduction; the source states a 100-day rolling-window method but this implementation detail is **underspecified** in this normalized record.
5. **Tradeable hypothesis:** only after the severe downside-depeg condition is observable using data available at the end of day `t`, establish long exposure to eligible major cryptocurrencies for the next daily return interval `t+1`.
6. **Holding period:** one day, then exit unless a new independently observable qualifying event occurs.
7. **Universe:** direct source universe is BTC, ETH, XRP, DOGE, TRX, BNB, ADA, LTC, XMR, and XLM. A modern implementation may test a liquid subset, but changing the universe is an adaptation and must be treated as such.
8. **Weighting:** **underspecified** for a trading portfolio. The source estimates asset-level regressions rather than prescribing an investable equal-weight or value-weight basket.
9. **Long-only vs. paired hedge:** **underspecified**. A simple long basket tests the lagged rebound directly; a beta-hedged or market-neutral construction would test whether there is residual rebound beyond broad crypto market recovery.

**Specification status:** the event definition and one-day lag hypothesis are reconstructable; production portfolio construction, exact signal cutoff, and fill convention remain **underspecified**.

## Required data

- Daily point-in-time USDT/USD price series from a venue or composite index with documented methodology.
- Consistent daily timestamp and timezone boundary for USDT and target cryptocurrencies.
- Daily close-to-close returns for BTC, ETH, XRP, DOGE, TRX, BNB, ADA, LTC, XMR, and XLM for direct source reproduction.
- At least 100 prior USDT daily observations for rolling mean and variance estimation.
- Point-in-time tradability, delisting, and market-status data if extending beyond the source universe.
- For a perpetual implementation: funding, mark/index price, liquidation rules, and contract availability.

USDT itself trades on fragmented venues and quote conventions. A USD-parity series must not be silently substituted with a crypto cross rate that embeds target-asset moves.

## Execution assumptions

The paper is an econometric event study, not an executable trading backtest. It does not specify market/limit order type, fees, spread, slippage, impact, funding, leverage, or portfolio sizing.

For causal timing, same-day returns associated with the depeg are **not** tradeable evidence if the event is identified using that day's closing USDT price. The only directly usable hypothesis in this record is the following-day lag effect after the depeg has been observed.

A valid backtest should therefore:

- compute the event only from information actually available at or after the daily cutoff;
- enter no earlier than the next executable interval;
- model spread and slippage during stressed liquidity conditions rather than using normal-day averages;
- test spot and perpetual implementations separately;
- include perp funding if derivatives are used;
- avoid assuming that a USDT stress event leaves exchange connectivity, withdrawals, or collateral mechanics fully functional.

## Evidence

### Source-reported

The source reports that downside USDT depegging is associated with immediate negative cryptocurrency returns and that the effect generally becomes larger as depeg severity increases.

Under the 100-day rolling-window threshold method at `k = 3`, Table B3 reports same-day coefficients for the ten cryptocurrencies ranging from approximately -1.965% to -3.803%, all statistically significant at conventional levels.

For the **next-day lag effect** after those same 3-sigma downside depegs, Table B3 reports positive coefficients for every studied asset:

- BTC: +2.649% (5% significance);
- ETH: +3.590% (1%);
- XRP: +3.507% (1%);
- DOGE: +3.208% (1%);
- TRX: +2.289% (5%);
- BNB: +3.087% (1%);
- ADA: +3.078% (5%);
- LTC: +3.032% (1%);
- XMR: +2.930% (1%);
- XLM: +4.090% (1%).

The 3-sigma rolling specification identifies 31 downside-depeg observations in the reported regression sample. The paper summarizes the pattern as a decline on the depeg day followed by a rebound the next day, with rebound magnitude roughly comparable to the initial decline.

These are **source-reported regression coefficients**, not a portfolio backtest and not independently verified trading returns.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's 100-day rolling **1-sigma** specification does not show statistically significant positive next-day downside-depeg lag coefficients. This directly limits the hypothesis: mild or ordinary depegs should not be assumed to exhibit the same rebound.

The event count becomes small at the 3-sigma threshold (31 downside events), which raises small-sample and event-clustering concerns. Severe depegs may also coincide with heterogeneous crises whose mechanisms differ materially.

The source regression contains persistent conditional heteroskedasticity, and some return series show residual autocorrelation even with HAC inference. Statistical significance therefore does not establish implementable net alpha.

## Falsification plan

1. Reconstruct the source event indicator using a documented USDT/USD series and the 100-day rolling mean/std method without future information.
2. Replicate the source universe and 2017-2024 sample first, then freeze the rule before evaluating a post-2024 out-of-sample period.
3. Test `k = 1`, `1.5`, `2`, and `3` separately. The thesis requires stronger and more reliable next-day rebound at severe thresholds; if the relation is flat, inverted, or isolated to one historical episode, reject the severity-conditioned interpretation.
4. Compare next-day returns with unconditional matched-day controls, volatility-matched controls, and broad-market beta-adjusted residual returns.
5. Cluster standard errors by event episode or block-bootstrap around depeg episodes to address nearby-event dependence.
6. Model stressed execution costs. If next-day net returns vanish under realistic spread, slippage, funding, and exchange-access assumptions, reject practical alpha even if gross regression coefficients remain positive.
7. Run leave-one-crisis-out tests. If removing any single major depeg episode destroys the result, classify the signal as event-specific rather than robust.
8. Test alternative USDT price sources/composites. If signal identity depends strongly on one venue's print, treat the event definition as data-source fragile.

## Crypto portability

**direct** for major cryptocurrencies because the primary source directly studies crypto assets and Tether depegging.

Portability beyond the ten-source-asset universe is **unproven**. Smaller tokens may experience larger liquidity shocks, delistings, or exchange-specific collateral effects that prevent a clean next-day reversal. Porting to perpetuals is **adapted** because funding, liquidation mechanics, mark/index pricing, and collateral denomination can materially change outcomes during stablecoin stress.

## Limitations

- **Not independently reproduced.**
- **Small-event sample:** the rolling 3-sigma specification contains 31 downside-depeg observations.
- **underspecified:** exact portfolio weighting and long-only versus beta-hedged implementation.
- **underspecified:** exact rolling-window inclusion convention and practical daily signal cutoff.
- **data-source risk:** USDT depeg classification can vary by venue and USD reference.
- **execution stress risk:** severe stablecoin events are precisely when spreads, slippage, withdrawals, and collateral reliability may deteriorate.
- **regime risk:** the sample ends in 2024; post-2024 stablecoin market structure, reserve transparency, exchange composition, and institutional access differ materially.
- **event heterogeneity:** reserve concerns, exchange failures, market-wide deleveraging, banking shocks, and temporary venue dislocations may all produce similar observed peg deviations but different rebound behavior.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, the strategy registry, any data pipeline, Paper, Testnet, or Live workflow has been performed in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain link was verified or written in this Scout cycle.

Repository-level related families include stablecoin-liquidity research, the Bitcoin Stablecoin Supply Ratio record, and stress-conditioned reversal research. Concept-level clustering and promotion belong to the separate Reviewer workflow.

## Sources

1. Sean Foley, Seung Ah Lee, and George Milunovich, *How Tether Depegging Affects Cryptocurrency Returns*, *Accounting & Finance* 66(2), 1101-1129 (2026), first published 2026-03-08. DOI: https://doi.org/10.1111/acfi.70201
2. Wiley full-text article and appendices, including rolling-window methodology, Tables 6-7, and Appendix Table B3: https://onlinelibrary.wiley.com/doi/10.1111/acfi.70201
