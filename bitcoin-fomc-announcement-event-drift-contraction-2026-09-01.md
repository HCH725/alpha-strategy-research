---
schema: strategy-research-record-v1
title: Bitcoin FOMC Announcement Event Drift and Meeting-Day Contraction
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - fomc
  - event-driven
  - monetary-policy
  - calendar-anomaly
  - garch
status: research-only
confidence: medium
source_as_of: 2020-11
sources:
  - https://doi.org/10.1016/j.frl.2019.101386
  - https://doi.org/10.1111/jofi.12196
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin FOMC Announcement Event Drift and Meeting-Day Contraction

## Provenance

- **Primary source:** Sujin Pyo and Jaewook Lee, "Do FOMC and macroeconomic announcements affect Bitcoin prices?", *Finance Research Letters*, Volume 37 (November 2020), Article 101386.
- **DOI:** https://doi.org/10.1016/j.frl.2019.101386
- **Sample period:** July 18, 2010 to January 30, 2019 (3,119 daily observations).
- **Underlying events examined:** Scheduled Federal Open Market Committee (FOMC) interest rate decision announcements, along with macroeconomic releases for the Consumer Price Index (CPI), Producer Price Index (PPI), and Employment rate.
- **Econometric methodology:** GARCH(1,1) framework with event-day dummy variables for mean return shifts and conditional volatility dynamics.
- **Foundational literature:** David O. Lucca and Emanuel Moench, "The Pre-FOMC Announcement Drift", *The Journal of Finance* 70, no. 1 (2015): 329–371. DOI: https://doi.org/10.1111/jofi.12196.

## Economic mechanism

### Source-reported

Pyo and Lee (2020) examine whether Bitcoin prices behave as a secluded, independent speculative asset or respond systematically to scheduled macroeconomic and monetary policy announcements. 

The authors report that:
1. **FOMC Announcement Day Contraction:** On days when the Federal Reserve releases scheduled FOMC policy announcements, Bitcoin prices exhibit a statistically significant negative mean return of approximately -1.00%, compared to an average daily gain of +0.26% on non-announcement days ($p < 0.05$).
2. **Volatility Sensitivity:** Bitcoin conditional volatility increases significantly around FOMC announcement releases.
3. **Macroeconomic News Independence:** Unscheduled or scheduled releases of traditional macroeconomic indicators (CPI, PPI, and Employment rate) do not show statistically significant unconditional effects on Bitcoin daily returns or volatility in this sample, suggesting Bitcoin's primary institutional sensitivity is monetary policy rather than real economy news.

### Research interpretation

The hypothesized mechanism combines **pre-event risk-premium resolution**, **liquidity withdrawal**, and **monetary stance repricing**:
1. **Pre-Announcement Positioning vs. Event De-risking:** Ahead of high-stakes central bank meetings, speculative market participants frequently build anticipatory positions (analogous to the equity pre-FOMC drift observed by Lucca & Moench, 2015). On the announcement day itself, the resolution of policy uncertainty, potential interest rate hike realization, and tightening liquidity conditions trigger systematic profit-taking or de-leveraging in speculative risk assets like Bitcoin.
2. **Monetary Tightening Discount Channel:** As an unbacked digital asset with no cash flows, Bitcoin behaves as an ultra-long-duration speculative asset whose valuation is highly sensitive to the discount rate and real interest rate expectations set by the Federal Reserve.
3. **Event-Calendar Timing Hypothesis:** A systematic event-driven calendar strategy that reduces long beta or enters a tactical short hedge across scheduled FOMC meeting windows can avoid negative event-day return drag and capture mean reversion post-announcement.

## Signal

Normalized source-consistent event calendar rule:

1. **Event Calendar Identification:**
   - Ingest scheduled FOMC meeting announcement dates from the Federal Reserve calendar (8 scheduled two-day meetings per calendar year, typically concluding on Wednesday at 14:00 EST / 18:00 or 19:00 UTC).
2. **Tactical Risk Reduction / Short Signal ($S_t$):**
   - At the daily close of day $T-1$ (the day preceding the scheduled FOMC policy statement release) or at the open of day $T$ (announcement day):
     - **Long-only portfolio overlay:** De-risk by reducing Bitcoin spot/futures exposure to 0% (cash / stablecoin) or applying a delta hedge.
     - **Directional tactical overlay:** Enter short Bitcoin exposure on day $T$.
3. **Exit / Re-entry ($T+1$):**
   - Close tactical short positions or restore normal baseline long exposure at the daily close of day $T$ or open of day $T+1$ (post-announcement resolution).
4. **Specification Status:** **Partially specified**. The calendar dates and daily return differential are explicitly reported in the source text, but exact intraday entry/exit execution timings (e.g. 15 minutes pre-press conference vs. daily close) are underspecified and require intraday tick/bar calibration.

## Required data

- **Asset Price Data:** Bitcoin (BTC/USD or BTC/USDT) daily OHLCV and intraday 1-minute to 1-hour candles.
- **Calendar Data:** Historical and forward-looking Federal Reserve FOMC schedule (official statement release dates and exact press conference timestamps).
- **Macro Announcement Calendars:** Historical release dates for US Bureau of Labor Statistics (BLS) CPI, PPI, and Non-Farm Payrolls / Employment reports for control testing.
- **Data Lineage / Timestamps:** Synchronized UTC timestamp conventions aligned with US Eastern Time (ET) Daylight Saving Time shifts.

## Execution assumptions

- **Execution Cadence:** Event-driven (8 occurrences per year).
- **Order Timing:** Order dispatch at $T-1$ daily close (00:00 UTC) or intraday pre-announcement cutoff (e.g., 12:00 UTC).
- **Order Type:** Limit orders with passive execution buffer or low-slippage market orders on major liquid venues (Binance, Coinbase).
- **Transaction Costs:** Typical CEX maker/taker fee of 2 to 5 bps per leg; short-leg borrowing or funding rate costs over a 24-hour holding window.
- **Capacity:** Substantial for BTC/USD majors; negligible slippage for institutional order sizes given deep spot and perpetual futures liquidity.

## Evidence

### Source-reported

Pyo and Lee (*Finance Research Letters*, 2020) report the following empirical statistics for the July 2010 – January 2019 sample:
- **FOMC Day Mean Return:** Approximately -1.00% on announcement days.
- **Non-FOMC Day Mean Return:** Approximately +0.26% on non-announcement days.
- **Statistical Significance:** The dummy variable coefficient for FOMC announcement days in the GARCH(1,1) mean equation is negative and statistically significant at the 5% level ($p < 0.05$).
- **Macroeconomic Releases:** Coefficients for CPI, PPI, and Employment announcement dummy variables are statistically indistinguishable from zero ($p > 0.10$).

*All figures above are source-reported from Pyo & Lee (2020) and have not been independently reproduced.*

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Regime Shift / Monetary Cycle Dependence:** The source sample (2010–2019) was dominated by post-GFC zero-interest-rate policy (ZIRP) and quantitative easing (QE). During the 2022–2024 aggressive Fed rate-hiking and subsequent pause/pivot cycles, market sensitivity to Fed press conferences and dot-plot surprises increased dramatically, with intraday price action showing sharp two-way whipsaws.
- **Equity Pre-FOMC Drift Decay:** Literature in traditional finance (e.g., Kurov et al., 2021) documents that the equity pre-FOMC announcement drift substantially diminished after 2015 due to enhanced Fed forward guidance and algorithmic anticipation. A similar fading effect may occur in crypto as institutional participation grows.
- **Low Sample Frequency:** With only 8 scheduled FOMC meetings per year (~70 events over a 9-year window), small sample noise and idiosyncratic outlier news events (e.g. unrelated crypto exchange hacks occurring near meeting dates) can distort point estimates.

## Falsification plan

The hypothesis of a systematic, harvestable FOMC announcement day discount in Bitcoin should be rejected or materially revised if:

1. **Modern Sample Replication (2019–2026):** In a post-2019 out-of-sample test covering the 2020–2026 period, the mean return on FOMC announcement days is not statistically lower than non-announcement days ($t > -1.65$).
2. **Surprise Conditioning:** If separating FOMC meetings into hawkish surprises vs. dovish surprises reveals that the negative return is entirely concentrated in rate-hike surprise days, rejecting the unconditional negative announcement day thesis.
3. **Transaction Cost & Whipsaw Test:** If bid-ask spread expansion and intraday volatility spikes during the 14:00–15:30 EST press conference window cause execution slippage exceeding the theoretical return spread.

## Crypto portability

**Direct**, as the primary empirical study was conducted directly on Bitcoin price series.

Portability considerations:
- **Altcoin Beta Amplification:** Altcoins (ETH, SOL, major tokens) generally exhibit higher beta to Bitcoin during macro volatility events; event de-risking may yield even larger variance reduction in altcoin portfolios.
- **Perpetual Futures Funding Dynamics:** In perpetual futures, funding rates often turn negative or compress sharply immediately prior to FOMC announcements as market participants hedge with short perps.

## Limitations

- **Source-reported only:** Results reflect findings from Pyo & Lee (2020); not independently reproduced in our research stack.
- **Low Event Frequency:** 8 events per year creates a small annual sample size.
- **Underspecified Intraday Timing:** Academic source evaluates daily close-to-close returns; optimal entry/exit minute-level execution windows are not specified.
- **Macro Regime Sensitivity:** Results may vary substantially across ZIRP, high-inflation, and easing regimes.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any other live/paper pipeline has been completed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated trading system, an implementation specification, or authorization for Paper, Testnet, or Live trading.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[quant/crypto-intraday-state-dependent-momentum-jump-reversal-2026-09-01]]`
- `[[quant/bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]]`
- `[[quant/crypto-cross-sectional-financial-uncertainty-beta-premium-2026-09-01]]`

## Sources

1. Sujin Pyo and Jaewook Lee, "Do FOMC and macroeconomic announcements affect Bitcoin prices?", *Finance Research Letters*, Volume 37 (2020), Article 101386. DOI: https://doi.org/10.1016/j.frl.2019.101386.
2. David O. Lucca and Emanuel Moench, "The Pre-FOMC Announcement Drift", *The Journal of Finance*, Volume 70, Issue 1 (2015), Pages 329–371. DOI: https://doi.org/10.1111/jofi.12196.
