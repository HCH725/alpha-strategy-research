---
schema: strategy-research-record-v1
title: "Crypto Perpetual Futures Alpha: Pre-Registered Multi-Regime Falsification, Four-Cell Validation, and Failure Library"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - scout
  - source-backed
  - crypto-perpetual
  - falsification
  - negative-evidence
  - regime-conditioning
  - four-cell-validation
  - stationary-bootstrap
  - leakage-audit
status: research-only
confidence: high
source_as_of: 2026-08-31
sources:
  - "https://github.com/Xty2750/crypto-perp-alpha-research/tree/9fa286b592405675655cfccf9d8b4e783e24b783"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Futures Alpha: Pre-Registered Multi-Regime Falsification, Four-Cell Validation, and Failure Library

## One-line mental model

A pre-registered, two-year empirical study across 12 crypto perpetual futures pairs (12.6 million 1-minute bars) falsifying 25 popular alpha hypotheses across six strategy families, establishing that retail technical signals and microstructure crowding lack post-cost edge, that apparent regime-conditional revivals fail a four-cell `{bull, bear} × {in-sample, out-of-sample}` validation gate, and that backtest credibility requires strict causal truncation tests, bar-by-bar stop monitoring, and stationary block bootstrap confidence intervals.

## Provenance

- **Author:** `Xty2750`
- **Repository URL:** [https://github.com/Xty2750/crypto-perp-alpha-research](https://github.com/Xty2750/crypto-perp-alpha-research)
- **Full Immutable Commit SHA:** `9fa286b592405675655cfccf9d8b4e783e24b783`
- **Canonical Tree URL:** [https://github.com/Xty2750/crypto-perp-alpha-research/tree/9fa286b592405675655cfccf9d8b4e783e24b783](https://github.com/Xty2750/crypto-perp-alpha-research/tree/9fa286b592405675655cfccf9d8b4e783e24b783)
- **Commit Date:** 2026-08-31T22:41:29Z
- **Primary Source Files Examined:**
  - `README.md` (program overview, 2-year data inventory of 12.6M bars, 7-rule pre-registered protocol, and research philosophy) (`source-reported`).
  - `docs/RESEARCH_PROTOCOL.md` (the seven operational enforcement rules: prove alpha before backtesting, honest cost modeling, frozen cut dates, cross-sectional portfolio engine, parameter plateaus, mechanism novelty, trade audit gating, and stationary block bootstrap arbiter) (`source-reported`).
  - `docs/FAILURE_LIBRARY.md` (detailed catalogue of 25 killed strategy candidates across ranking, calendar, funding, leverage, breadth, and volatility families with specific empirical metrics and causes of death) (`source-reported`).
  - `docs/REGIME_CONDITIONING.md` (econometric analysis of in-sample vs. out-of-sample sign flips, macro regime alignment with 200-day moving average, the danger of regime rationalization, and the four-cell `{bull, bear} × {in-sample, out-of-sample}` test specification) (`source-reported`).
  - `docs/BUGS_AND_LESSONS.md` (forensic post-mortem of six fatal backtesting traps: calendar lookahead via D+1 close, calendar index destruction via `dropna()`, rolling NaN boolean misclassification, exit-only stop monitoring, truncated monitoring windows, and empirical quantification of selection bias) (`source-reported`).
  - `tools/four_cell.py` (executable Python module implementing the four-cell regime validation test with underpowered guards and explicit NaN warm-up dropping) (`source-reported`).
  - `tools/leakage_audit.py` (executable point-in-time verification tools: prefix truncation testing for non-causal features, trade-by-trade ledger invariant audit, and timestamp alignment) (`source-reported`).
  - `tools/bootstrap.py` (executable Politis & Romano 1994 stationary block bootstrap confidence interval calculation for clustered trade return series) (`source-reported`).
  - `tools/walkforward.py` (executable walk-forward fold generation with label purging and post-boundary embargo) (`source-reported`).
  - `examples/demo.py` (end-to-end synthetic verification harness with deliberate planted defects) (`source-reported`).
- **Primary Source Verification:** All files above were directly retrieved and inspected at commit `9fa286b592405675655cfccf9d8b4e783e24b783`. Every quantitative metric, sample size, in-sample/out-of-sample split date, fee/slippage assumption, $t$-statistic, Information Coefficient (IC), Sharpe ratio, and failure diagnosis traces directly to the repository text and code.
- **Repository Deduplication Audit:** A comprehensive audit of all existing records in `alpha-strategy-research` confirmed zero matching records for `Xty2750`, `crypto-perp-alpha-research`, or commit `9fa286b592405675655cfccf9d8b4e783e24b783`. Related falsification records in the repository examine distinct domains: `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md` (Joseph Berachah) investigated cross-sectional funding deciles on Binance; `crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md` (rfukuda06) evaluated spot cointegration pair selection snooping; `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` analyzed cumulative volume delta (CVD) divergence. The current research captures an independent, two-year multi-asset empirical program spanning 94 experiments and 25 documented kills, introducing the four-cell regime validation architecture and structural backtest leakage defenses.

## Economic mechanism

### Source-reported

1. **Intraday Leverage and Forced-Flow Dynamics:**
   Cryptocurrency perpetual futures trade 24/7 with high leverage (often 20x to 100x), continuous order matching, and transparent periodic funding settlement. Common quantitative and technical market beliefs assume that intraday forced-flow dynamics—such as liquidation cascades, extreme funding sentiment, open interest crowding, or sudden volatility spikes—create predictable, mean-reverting or momentum-continuation mispricings that can be profitably extracted by algorithmic traders.
2. **Systematic Falsification Across Core Market Mechanisms:**
   Empirical testing across 12.6 million 1-minute bars over 2024–2026 demonstrates that almost all retail technical and structural indicators fail to deliver positive returns after accounting for exchange taker fees and execution slippage:
   - *Funding Rate Contrarianism:* The hypothesis that extreme positive funding rates signal an overbought market ripe for mean-reversion reversal is contradicted by the data. Extreme positive funding reflects aggressive long crowding accompanied by momentum *continuation*; prices continue rising rather than reversing.
   - *Funding Settlement Microstructure:* The hypothesis that positioning pressure around the 8-hour or 1-hour settlement windows creates actionable order-flow drift fails because market-making arbitrageurs efficiently front-run and absorb the predictable rebalancing flow.
   - *Liquidation Cascade Reversal:* Attempting to buy into sharp price drops accompanied by open-interest collapse (liquidation rebound) acts as "catching a falling knife"; post-liquidation price action displays persistent adverse momentum continuation rather than an immediate liquidity bounce.
   - *Aggregate Market Descriptors:* Market-wide metrics (total open interest, aggregate market breadth, dispersion) describe concurrent market states but exhibit zero predictive Information Coefficient (IC) for future asset returns.
   - *Intraday Anchoring & Session Opens:* 24/7 markets lack an official opening bell; synthetic session opens (e.g., 00:00 or 12:00 UTC) fail out-of-sample, with initial 2-hour momentum completely sign-flipping between bull and bear regimes.
   - *Cross-Asset Lead-Lag:* Lead-lag relationships (e.g., Bitcoin price revisions leading altcoin movements over a 1-hour horizon) yield tiny lagged beta coefficients ($\pm 0.03\text{--}0.08$) that are entirely erased by the 14 bps round-trip transaction cost barrier.
3. **The Microstructure Cost Wall:**
   At the 1-minute bar scale, the expected single-bar price move ($1R$) is approximately $0.07\%$, whereas realistic transaction costs (5 bps taker fee + 2 bps slippage per side = 14 bps round-trip) equal $\approx 1.6R$. Minute-level directional trading in liquid crypto perpetuals is arithmetically impossible for retail takers; high-frequency re-evaluation generates excessive turnover that rapidly drains capital.

### Research interpretation

From an empirical and quantitative infrastructure perspective, the primary lesson of this research is that quantitative failure modes in crypto derivatives are rarely random; they are structural:
- **Sign Flips vs. Noise:** When tested across an out-of-sample split that coincides with a macro regime transition (e.g., bull market shifting to bear market), unhedged directional signals reliably flip sign ($+t \to -t$) rather than oscillating around zero. This indicates that the signals are not capturing independent structural alpha, but are merely disguised proxies for broader market beta.
- **The Regime Rationalization Trap:** When an in-sample positive signal fails out-of-sample during a regime shift, researchers are tempted to rescue the signal by conditioning it on a regime indicator (e.g., 200-day moving average). However, if the backtest window contains only one historical bull period and one historical bear period, conditioning on regime reduces the sample to a single observation per regime cell, creating an unfalsifiable narrative fit.

## Signal

The research program evaluated 25 candidate signals across six core strategy families, all of which were formally falsified and killed (`source-reported`):

### 1. Cross-Sectional and Ranking Signals
- **Cross-Sectional Momentum:**
  - *Formation timestamp:* Daily bar close (00:00 UTC) (`source-reported`).
  - *Lookback:* Multi-horizon trailing returns (1-day, 3-day, 5-day, 20-day) across the 12-pair universe (`source-reported`).
  - *Entry:* Long top quantile, short bottom quantile (`source-reported`).
  - *Exit:* Daily rebalance (`source-reported`).
  - *Result:* Rank IC $\approx 0$ ($-0.005$ to $+0.012$); killed due to lack of predictive rank correlation (`source-reported`).
- **Cross-Sectional 1-Day Reversal:**
  - *Lookback:* 24-hour return (`source-reported`).
  - *Entry:* Long yesterday's worst performers, short yesterday's best performers (`source-reported`).
  - *Result:* IC $-0.014$ to $-0.022$ ($t < 1.5$); gross daily return $+0.12\%$ to $+0.16\%$, falling far short of daily round-trip turnover costs (14 bps) (`source-reported`).
- **Cross-Sectional 20-Day Reversal:**
  - *Lookback:* 20-day return (`source-reported`).
  - *Result:* Weak IC that sign-flipped across subperiods; weekly long/short Sharpe $-0.32$ (`source-reported`).
- **Aggregate Open-Interest Ranking:**
  - *Hypothesis:* Relative open interest growth ranks predict future cross-sectional returns (`source-reported`).
  - *Result:* No cross-period stable parameter configuration (`source-reported`).

### 2. Time-of-Day, Calendar, and Seasonality Signals
- **Intraday Anchoring (Synthetic Open):**
  - *Formation timestamp:* 12:00 UTC (`source-reported`).
  - *Lookback:* First 2 hours of the session (12:00–14:00 UTC) (`source-reported`).
  - *Entry:* If first 2 hours return $> 0$, enter Long at 14:00 UTC; if $< 0$, enter Short (`source-reported`).
  - *Exit:* End of session (24:00 UTC) (`source-reported`).
  - *Result:* In-sample $+0.83\%$ ($t=3.2$) $\to$ Out-of-sample $-0.67\%$ ($t=-4.2$); fatal sign flip (`source-reported`).
- **Standalone Intraday Seasonality & Day-of-Week:**
  - *Result:* In-sample patterns fully decayed or sign-flipped out-of-sample (`source-reported`).

### 3. Funding-Rate Signals
- **Funding Sentiment Extremes:**
  - *Lookback:* Trailing 8-hour funding rate relative to rolling historical percentiles (`source-reported`).
  - *Entry:* Contrarian long on deeply negative funding, contrarian short on extreme positive funding (`source-reported`).
  - *Result:* Sign-flipped out-of-sample; extreme positive funding indicates persistent long momentum rather than reversal (`source-reported`).
- **Pure Delta-Exposed Funding Harvesting:**
  - *Result:* Directional price drift dwarfs the funding yield; noise-to-signal ratio fatal (`source-reported`).
- **Funding + OI Dual Confirmation:**
  - *Result:* High collinearity between OI spikes and funding extremes; combining both left only 9 events in 2 years, rendering the rule statistically unviable (`source-reported`).

### 4. Open-Interest and Leverage Signals
- **Liquidation Rebound:**
  - *Trigger:* Sharp price drop accompanied by sudden contraction in open interest (`source-reported`).
  - *Entry:* Long oversold bounce (`source-reported`).
  - *Result:* Falling knife; post-liquidation flow is momentum continuation (`source-reported`).
- **Aggregate Leverage Speed:**
  - *Result:* All three market-wide leverage rate-of-change metrics sign-flipped between in-sample and out-of-sample (`source-reported`).

### 5. Breadth and Dispersion Signals
- **Market Breadth Filter on Short Strategies:**
  - *Trigger:* Fraction of advancing pairs across the 12-pair universe (`source-reported`).
  - *Flawed Implementation:* Evaluated day $D+1$ breadth (computed from $D+1$ close) to filter a trade running open-to-close on day $D+1$. This calendar lookahead produced a false Sharpe of $2.07$ (`source-reported`).
  - *Corrected Implementation:* Moving the filter strictly to day $D$ close caused every threshold from $0.20$ to $0.67$ to turn negative in-sample (`source-reported`).

### 6. Volatility and Lead-Lag Signals
- **Implied Volatility (BTC DVOL) Timing:**
  - *Trigger:* Daily DVOL falling below 15th percentile (`source-reported`).
  - *Holding Period:* 10 days (`source-reported`).
  - *Result:* In-sample $+1.20\%$ over 10 days $\to$ Out-of-sample $-4.10\%$ ($t=-5.4$); fatal sign flip (`source-reported`).
- **Realized Volatility 5-Day Expansion:**
  - *Result:* In-sample $+3.67\%$ ($t=3.0$) $\to$ Out-of-sample $-1.40\%$ ($t=-2.7$) (`source-reported`).
- **1-Hour Volume Spike $\to$ 2-Hour Long:**
  - *Trigger:* Intraday volume exceeding rolling volume threshold (`source-reported`).
  - *Result:* Pooled $t$-statistic of $3.6\text{--}10.0$ was a statistical illusion caused by cross-pair event clustering; the portfolio engine returned Sharpe $-0.76$ (In-sample $+1.77$, Out-of-sample $-2.78$), with half of the individual pairs negative (`source-reported`).
- **BTC $\to$ Altcoin 1-Hour Lead-Lag:**
  - *Result:* Lag-1 beta sign-flipped from negative ($t=-2.0\text{--}-4.7$) in-sample to positive out-of-sample; when partitioned across regimes, all four cells produced negative returns ($t=-5.4$ to $-16.9$) because 14 bps transaction costs consumed the small lagged beta ($\pm 0.03\text{--}0.08$) (`source-reported`).

## Required data

- **Instrument:** 12 USDT-margined perpetual futures contracts: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `XRPUSDT`, `DOGEUSDT`, `ADAUSDT`, `BNBUSDT`, `AVAXUSDT`, `LINKUSDT`, `LTCUSDT`, `APTUSDT`, `ARBUSDT` (`source-reported`).
- **Universe:** Fixed 12-pair liquid crypto perpetual panel (`source-reported`).
- **Venue:** Centralized cryptocurrency derivatives exchanges (Binance / Bybit public historical archives) (`source-reported`).
- **Timeframe:** 1-minute, 5-minute, and 15-minute OHLCV bars (1,051,200 1-minute bars per pair; 12.6 million total bars) (`source-reported`).
- **External Auxiliary Fields:**
  - *Funding Rates:* Actual settlement records (~2,190 settlements per pair at true 8h and 1h timestamps) (`source-reported`).
  - *Open Interest:* Daily open interest snapshots stamped at 16:00 UTC (800 observations per pair) (`source-reported`).
  - *Implied Volatility:* Deribit Bitcoin DVOL daily OHLC (`source-reported`).
- **Data Integrity & Exclusions:**
  - Manifest verification confirmed zero missing timestamps and zero duplicates across the 2-year window (`source-reported`).
  - Unobserved fields: Order book depth, bid/ask spread, trade-level aggressor side, liquidation prints, spot-perp basis, and cross-exchange flows were *not* included and therefore never assumed (`source-reported`).
- **Point-in-Time Hygiene:**
  - All signals must be knowable strictly prior to execution: $\text{signal\_time} < \text{entry\_time}$ (`source-reported`).
  - Moving-average warm-up periods (e.g., 200 days) must explicitly drop NaN values rather than evaluating boolean conditions (`close >= NaN`), which silently misclassifies early data (`source-reported`).
- **Transaction Costs & Spread:**
  - Default baseline: 5 bps taker fee + 2 bps adverse slippage per side (7 bps one-way, 14 bps round-trip) (`source-reported`).
  - Sensitivity baseline: 2 bps maker fee per side (`source-reported`).
  - Stress testing: 10 bps fee + 4 bps slippage per side (28 bps round-trip) (`source-reported`).

## Execution assumptions

- **Order Type & Execution Timing:** Orders are evaluated on closed bars and filled at the open price of the subsequent bar ($t+1$) with adverse slippage applied (`source-reported`).
- **Stop-Loss Monitoring:** Bar-by-bar intrabar inspection (checking high/low of every bar during the entire holding period, including the exit bar). A trade whose low breached its stop price mid-hold must be recorded as stopped out, never as a winning time exit (`source-reported`).
- **Position Sizing:** Equal-weighting across pairs with inverse-volatility normalization, risking a fixed fraction of 1% account equity per trade (`source-reported`).
- **Calendar Alignment:** Non-signal days must remain in the daily return series with zero return; calling `dropna()` on non-signal days destroys the calendar index, deflating elapsed time by $3.6\times$ and falsely inflating annualized Sharpe ratios from 0.87 to 2.18 (`source-reported`).

## Evidence

### Source-reported

All metrics below trace directly to the audited research documentation and code in `Xty2750/crypto-perp-alpha-research` (Commit `9fa286b592405675655cfccf9d8b4e783e24b783`, August 2026), evaluated across 12 USDT perpetual pairs over the 2-year window (August 13, 2024 to August 13, 2026) with a pre-registered frozen out-of-sample boundary at August 13, 2025:

| Candidate Mechanism | In-Sample Metric (IS) | Out-of-Sample Metric (OOS) | Cause of Death / Diagnosis |
|---|---|---|---|
| **Cross-sectional momentum** | Rank IC $\approx 0$ ($-0.005$ to $+0.012$) | Rank IC $\approx 0$ | No predictive cross-sectional ranking power at any horizon |
| **Cross-sectional 1-day reversal** | Daily return $+0.12\%\text{--}+0.16\%$ ($t < 1.5$) | Daily return $< +0.10\%$ | Gross return is below daily turnover cost (14 bps) |
| **Cross-sectional 20-day reversal** | Weak IC | Sign-flipped across subperiods | Weekly long/short portfolio Sharpe $-0.32$ |
| **Intraday 12:00 UTC anchoring** | Return $+0.83\%$ ($t = +3.2$) | Return $-0.67\%$ ($t = -4.2$) | Fatal sign flip; captured macro drift rather than session alpha |
| **Funding sentiment extremes** | Positive return in bull phase | Negative return in bear phase | Sign flip; high funding represents momentum continuation |
| **Breadth short filter (lookahead)** | Sharpe $2.07$ (flawed D+1 close) | Negative across all thresholds | Calendar lookahead bug; day D close produces negative in-sample |
| **Implied volatility DVOL $<15$th %ile** | $+1.20\%$ over 10 days | $-4.10\%$ ($t = -5.4$) | Fatal sign flip |
| **Realized volatility 5d expansion** | $+3.67\%$ ($t = +3.0$) | $-1.40\%$ ($t = -2.7$) | Fatal sign flip |
| **Volatility asymmetry 1d fear** | $+0.41\%$ ($t = +2.4$) | $-0.37\%$ ($t = -2.4$) | Sign flip; combined engine portfolio Sharpe $-0.55$ |
| **1h volume spike $\to$ 2h long** | Pooled $t = 3.6\text{--}10.0$ (Sharpe $+1.77$) | Engine Sharpe $-2.78$ | Pooled $t$-stat illusion from event clustering; portfolio Sharpe $-0.76$ |
| **BTC $\to$ altcoin 1h lead-lag** | Lag-1 beta negative ($t = -2.0\text{--}-4.7$) | Lag-1 beta positive | 14 bps round-trip fees destroy small lagged beta ($\pm 0.03\text{--}0.08$) |
| **Regime-conditioned lead-lag** | Bull IS/OOS negative | Bear IS/OOS negative | All four cells negative ($t = -5.4$ to $-16.9$) net of costs |
| **Asian session ORB breakout** | Win rate $50.2\%$ | Win rate $< 50\%$ | Naked breakout has zero edge; filters fail to improve win rate |
| **Selection bias quantification** | Full-sample IC $+0.190$, Sharpe $2.40$ | In-sample IC $+0.081$, Sharpe $1.11$ | 95% bootstrap CI spans zero when selection is isolated to training data |

### Independently reproduced

`not independently reproduced`. All metrics and empirical findings represent third-party research reported by `Xty2750` at commit `9fa286b592405675655cfccf9d8b4e783e24b783`. No internal backtest execution has been performed in `nautilus-quant-system` or PyBroker.

### Negative evidence

The entirety of this capture is structured around negative empirical evidence and rigorous falsification:
1. **25 Documented Strategy Kills:** Every technical, ranking, funding, calendar, leverage, breadth, and volatility signal tested failed out-of-sample or collapsed under transaction costs (`source-reported`).
2. **Rejection of Regime Resurrections:** When six previously killed candidates were retested under the four-cell regime validation framework (`{bull, bear} × {in-sample, out-of-sample}`), five were definitively rejected because their apparent revival was an artifact of single-stretch macro exposure (`source-reported`).
3. **Statistical Fallacy of Pooled $t$-Statistics:** Cross-sectional pooling across pairs inflates $t$-statistics ($3.6\text{--}10.0$) due to correlated event clustering, while an equal-weighted, volatility-normalized portfolio generates negative performance (Sharpe $-0.76$) (`source-reported`).
4. **Bootstrap CI Spanning Zero:** Multiple candidates exhibiting positive out-of-sample point returns ($+0.203\%$ with $t=1.25$, $+0.596\%$ with $t=1.51$, and $+0.129\%$ with $t=0.86$) failed acceptance because stationary block bootstrap confidence intervals spanned zero (`source-reported`).

## Falsification

To test and disconfirm any surviving or newly proposed crypto perpetual alpha candidate, the four structural test gates defined by this research must be strictly executed:

1. **Stationary Block Bootstrap Confidence Gate:**
   - *Test:* Resample trade return series using the Politis & Romano (1994) stationary bootstrap with geometric block length $\bar{L} = N^{1/3}$ across $B = 10,000$ iterations (`source-reported`).
   - *Decision Rule:* If the 95% percentile confidence interval of per-trade mean return spans zero (i.e., $\text{lower\_bound} \le 0$), the strategy is rejected as statistically indistinguishable from zero alpha (`research-defined falsification threshold`).
2. **Four-Cell Regime Independence Gate:**
   - *Test:* Partition the trade history into four disjoint cells: $\{\text{Bull}, \text{Bear}\} \times \{\text{In-Sample}, \text{Out-of-Sample}\}$, defining Bull as $\text{BTC} \ge \text{MA}_{200}$ and Bear as $\text{BTC} < \text{MA}_{200}$, dropping the 200-day warm-up window (`source-reported`).
   - *Decision Rule:* Every cell with $N \ge 15$ observations must exhibit the same sign ($+t$ or $-t$). If any adequately powered cell sign-flips or if any regime cell has $N < 15$ (`research-proposed`), the strategy is rejected as an unvalidated regime-fitting artifact (`research-defined falsification threshold`).
3. **Point-in-Time Prefix Truncation Gate:**
   - *Test:* Recompute all feature transformation pipelines on chronological prefixes of raw market data at 50%, 70%, and 90% sample checkpoints (`source-reported`).
   - *Decision Rule:* The maximum absolute difference between prefix values and full-sample values must satisfy $\max |\Delta| \le 10^{-10}$. Any non-zero difference indicates future leakage (e.g., centered rolling windows, whole-sample z-scores, forward `bfill`) and automatically invalidates the strategy (`research-defined falsification threshold`).
4. **Intrabar Stop-Loss Integrity Audit:**
   - *Test:* Inspect trade records against 1-minute intrabar high/low series (`source-reported`).
   - *Decision Rule:* Exactly zero trades may exhibit an exit price above the stop price if the intrabar low breached the stop level during the hold. If violations $> 0$, the backtest is rejected as invalid (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `direct`.
- **Primary Market Context:** The research was developed, executed, and validated natively on cryptocurrency perpetual futures contracts across 12 major assets (`BTC`, `ETH`, `SOL`, `XRP`, etc.) using real 24/7 Binance/Bybit historical data, actual 8-hour and 1-hour funding rates, and exchange-specific open interest timestamps.
- **Perpetual Specifics:**
  - *24/7 Trading Continuity:* Confirms that traditional equity calendar anomalies (session open, day-of-week) do not port cleanly into continuous 24/7 crypto markets and regularly sign-flip across market cycles.
  - *Funding & Basis Frictions:* Funding settlements do not generate profitable retail micro-arbitrage opportunities and cannot be reliably harvested without bearing unacceptable directional delta risk.
  - *Fee & Slippage Realism:* Establishes that crypto perpetual alpha research must incorporate at least 14 bps round-trip taker costs (or 28 bps under stress) before claiming tradability.

## Limitations

1. **Order Book Microstructure Unobserved:** The source study is restricted to 1-minute OHLCV, daily open interest, and funding settlements; it does not evaluate Level 2 order book depth, order flow imbalance (OFI), trade aggressor side, or real-time liquidation feed prints.
2. **Retail Taker Cost Barrier:** The finding that intraday technical signals fail applies primarily to taker execution ($7$ bps per side). Market-making or ultra-low-latency latency-advantaged firms trading with VIP-tier negative maker rebates may face different economics.
3. **Survivor Strategy Parameters Omitted:** The repository deliberately withheld the exact numerical parameters and frozen configs of its single surviving event-conditioned structural entry strategy to prevent parameter over-fitting by third parties.
4. **Finite Macro Regimes:** The 2-year sample (2024–2026) covers primarily one large bull cycle and one significant bear correction, limiting the number of macro regime transitions available for multi-year walk-forward validation.

## Implementation status

- **Frontmatter Status:** `implementation_status: not-implemented`.
- **System Boundaries:** This capture represents third-party empirical falsification research and methodology. Zero strategy code has been implemented in `nautilus-quant-system`, PyBroker, or NautilusTrader. No trading family has been created, and no Paper, Testnet, or Live execution is authorized.

## Adoption boundary

- **Frontmatter Status:** `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- **Operational Scope:** This document is an upstream research capture for Hermes Wiki Brain intake. Its presence in this repository does not imply strategy viability, quantitative approval, or permission to deploy capital. Any future adoption must independently pass NautilusTrader event-driven backtesting, fee audit, and formal risk review.

## Related Wiki records

- `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md`: Pre-registered empirical study by Joseph Berachah falsifying cross-sectional funding rate carry strategies due to daily turnover dissipation on Binance perpetuals.
- `crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md`: Falsification study by rfukuda06 documenting data snooping in cointegration pair selection and in-sample parameter overfitting in crypto spot.
- `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`: Microstructure falsification study demonstrating that retail CVD and funding signals lack standalone predictive power.
- `usdt-exchange-net-inflow-buy-side-liquidity-drift-1h-2h-2026-09-03.md`: Analyzed short-horizon exchange liquidity drifts and volume spikes.

## Sources

1. **Primary Repository:** `Xty2750/crypto-perp-alpha-research`
   - Canonical GitHub URL: [https://github.com/Xty2750/crypto-perp-alpha-research](https://github.com/Xty2750/crypto-perp-alpha-research)
   - Full Immutable Commit SHA: `9fa286b592405675655cfccf9d8b4e783e24b783`
   - Canonical Tree URL: [https://github.com/Xty2750/crypto-perp-alpha-research/tree/9fa286b592405675655cfccf9d8b4e783e24b783](https://github.com/Xty2750/crypto-perp-alpha-research/tree/9fa286b592405675655cfccf9d8b4e783e24b783)
   - Commit Date: 2026-08-31T22:41:29Z
   - Key Documents & Scripts Examined:
     - `README.md`
     - `docs/RESEARCH_PROTOCOL.md`
     - `docs/FAILURE_LIBRARY.md`
     - `docs/REGIME_CONDITIONING.md`
     - `docs/BUGS_AND_LESSONS.md`
     - `tools/four_cell.py`
     - `tools/leakage_audit.py`
     - `tools/bootstrap.py`
     - `tools/walkforward.py`
     - `examples/demo.py`
2. **Methodological References Cited in Source:**
   - Politis, D. N., & Romano, J. P. (1994). "The Stationary Bootstrap." *Journal of the American Statistical Association*, 89(428), 1303–1313.
