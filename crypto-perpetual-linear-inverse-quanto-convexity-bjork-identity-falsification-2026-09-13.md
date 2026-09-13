---
schema: strategy-research-record-v1
title: "Crypto Perpetual Linear-Inverse Quanto Convexity: Björk No-Arbitrage Identity Violation, Funding Rate Clamping, and Subperiod Carry Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - quanto-convexity
  - no-arbitrage-identity
  - change-of-numeraire
  - binance
  - falsification
  - negative-results
  - deflated-sharpe-ratio
status: research-only
confidence: high
source_as_of: 2026-08-26
sources:
  - "Mukola Hotstore (mykola-zadir), 'Quanto Convexity in Crypto Perpetuals — A Björk Identity Test', GitHub repository 'mykola-zadir/bjork-quanto-convexity', commit feac9fd414e427e21cfc7ca761f619ea2718aad2, published 2026-08-26, accessed 2026-09-13. https://github.com/mykola-zadir/bjork-quanto-convexity"
  - "Foundational theory: Tomas Björk, 'Arbitrage Theory in Continuous Time', Oxford University Press, 3rd/4th editions (Chapters 4: Itô's Lemma, 13: Currency and Quanto Derivatives, 26: Change of Numeraire)."
  - "Primary empirical study log: https://github.com/mykola-zadir/bjork-quanto-convexity/blob/feac9fd414e427e21cfc7ca761f619ea2718aad2/results/study_log.md"
  - "Primary statistical output JSON: https://github.com/mykola-zadir/bjork-quanto-convexity/blob/feac9fd414e427e21cfc7ca761f619ea2718aad2/results/quanto_convexity.json"
  - "Strategy signal and P&L derivation engine: https://github.com/mykola-zadir/bjork-quanto-convexity/blob/feac9fd414e427e21cfc7ca761f619ea2718aad2/strategy/quanto_convexity.py"
  - "Exact contract arithmetic test suite: https://github.com/mykola-zadir/bjork-quanto-convexity/blob/feac9fd414e427e21cfc7ca761f619ea2718aad2/tests/test_quanto_convexity.py"
  - "Multi-testing certification engine: https://github.com/mykola-zadir/bjork-quanto-convexity/blob/feac9fd414e427e21cfc7ca761f619ea2718aad2/backtest/certify.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Linear-Inverse Quanto Convexity: Björk No-Arbitrage Identity Violation, Funding Rate Clamping, and Subperiod Carry Falsification

## Provenance

- **Repository:** `https://github.com/mykola-zadir/bjork-quanto-convexity`
- **Author:** Mukola Hotstore (`mykola-zadir`, `7nickyeet7z@gmail.com`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `feac9fd414e427e21cfc7ca761f619ea2718aad2` (`source-reported`).
- **Commit Date:** 2026-08-26T21:27:51Z (`source-reported`).
- **Source As-Of Date:** 2026-08-26 (`source-reported`).
- **Primary Source Files Directly Audited:**
  - `README.md`: Formal problem statement, change-of-numeraire mathematical motivation, headline empirical tables, derivation explanation, subperiod failure diagnosis, and rejection summary.
  - `strategy/quanto_convexity.py`: Signal generation, jitter-proof 8-hour timestamp alignment (`align_funding`), daily spread aggregation (`daily_spread`), rolling realized variance fair-value calculation (`fair_spread_daily`), deviation signal with hysteresis deadbands (`deviation_signal`, `side_from_signal`), and causal 4-leg cost-adjusted pair P&L simulation (`pair_pnl`).
  - `verify_quanto_convexity.py`: Pre-registered empirical execution script orchestrating the two-hypothesis identity test ($H_0^A$ vs $H_0^B$), 10-trial frozen grid backtest, Mertens skew/kurtosis-aware Sharpe confidence intervals, Newey-West HAC tests, ETH twin replication, and out-of-sample subperiod gate.
  - `tests/test_quanto_convexity.py`: Executable test suite verifying test [0] exact contract arithmetic cancellation ($< 10^{-12}$ error), timestamp jitter tolerance, partial-day exclusion, fair spread causal prefix-invariance, and pair P&L hand-calculated paths.
  - `results/study_log.md`: Raw execution output logging the 6,450-print BTC and 6,427-print ETH empirical identity statistics, 10-trial P&L performance metrics, and the formal certification failure breakdown.
  - `results/quanto_convexity.json`: Machine-readable results containing full statistical outputs for all 10 trials and the final `REJECTED` verdict.
  - `backtest/certify.py` & `backtest/statistics.py`: Institutional multi-testing evaluation engine implementing Mertens Sharpe standard errors, Probabilistic Sharpe Ratio (PSR), Deflated Sharpe Ratio (DSR) charged against 232 historical trials, and Combinatorially Symmetric Cross-Validation (CSCV) Probability of Backtest Overfitting (PBO).
  - `prior_trial_sharpes.json`: Committed historical trial ledger containing 222 prior trial Sharpes from the parent research program (`crypto-quant-research`), preventing post-hoc luck filtering.
- **Foundational Theoretical Source:** Tomas Björk, *Arbitrage Theory in Continuous Time*, Oxford University Press (Chapters 4: Itô's Lemma, 13: Currency and Quanto Derivatives, 26: Change of Numeraire) (`source-reported`).
- **Sample Period:** August 1, 2020 to August 24, 2026 (~6.5 years; 2,149 daily bars for BTC, 2,141 daily bars for ETH) (`source-reported`).
- **Venue & Market Type:** Binance Crypto Perpetual Futures (USDT-margined linear contracts `BTCUSDT`/`ETHUSDT` vs Coin-margined inverse contracts `BTCUSD_PERP`/`ETHUSD_PERP`) (`source-reported`).
- **Repository Deduplication Audit:** Comprehensive grep across all existing Markdown records in `alpha-strategy-research` confirms zero prior records citing `mykola-zadir`, `bjork-quanto-convexity`, Mukola Hotstore, or commit `feac9fd414e4`. An adjacent record (`perpetual-inverse-linear-margin-currency-funding-spread-2026-09-01.md`, citing BitMEX Research / Shang Wu 2026) captured a heuristic hypothesis regarding retail collateral demand asymmetry on BitMEX. The current research is fundamentally distinct: it derives the continuous-time no-arbitrage change-of-numeraire identity ($\text{fair spread} = \sigma^2 \Delta t$), proves that the Binance funding rate channel violates this theorem by two orders of magnitude due to contract base-rate clamping, documents the mathematical category error of trading funding flows as price levels, and demonstrates that the residual carry edge collapsed out-of-sample in 2024–2026 (Sharpe +5.09 $\to$ −1.28).

## Economic mechanism

### Source-reported

1. **Theoretical Derivation from Continuous-Time Arbitrage Theory:**
   - On cryptocurrency exchanges such as Binance, two distinct perpetual contracts exist for the same underlying index (e.g. BTC/USD):
     - **Linear perpetuals:** Margined and settled in a fiat-pegged stablecoin (USDT). Equity and payoff are linear in USD terms.
     - **Inverse perpetuals:** Margined and settled in the underlying cryptocurrency itself (e.g. BTC or ETH). Because the contract pays out in the asset whose price it tracks, it is structurally a **quanto derivative** in the terminology of Björk (*Arbitrage Theory in Continuous Time*, Chapters 13 and 26).
   - In the cryptocurrency numeraire, the inverse position's payoff is linear in $1/S$, but in the USD numeraire it is non-linear and convex. Let $S_t$ denote the spot price following a continuous-time diffusion $dS_t = \mu S_t dt + \sigma S_t dW_t$.
   - By Itô's lemma (Björk, Chapter 4), the process for the inverse price $Y_t = 1/S_t$ satisfies:
     $$d\left(\frac{1}{S_t}\right) = -\frac{1}{S_t^2} dS_t + \frac{1}{2} \frac{2}{S_t^3} (dS_t)^2 = -\frac{1}{S_t} (\mu - \sigma^2) dt - \frac{\sigma}{S_t} dW_t$$
   - Under change of numeraire (Girsanov's theorem with the asset itself as payout currency, where the correlation between the underlying asset and payout currency is identically 1.0), continuous-time no-arbitrage pricing requires that the fair funding rate differential between the linear and inverse contracts must equal the variance rate:
     $$\text{fair spread} = f_{\text{linear}} - f_{\text{inverse}} \approx \sigma^2 \Delta t \quad (\text{source-reported})$$
     On an annualized basis, the theoretical fair funding differential is $\sigma^2$ per year (or $\sigma^2 / 365$ per day). For an asset with 60% annualized volatility ($\sigma = 0.60$), the linear contract should pay a funding rate 36% per year higher than the inverse contract to compensate for the convex payout curvature.

2. **The Exact Pair Price-Leg Cancellation:**
   - Consider a dollar-neutral pair consisting of short \$w linear perpetual and long \$w inverse perpetual, both entered at price $S_0$ and evaluated at subsequent price $S_1$ (return $r = (S_1 - S_0)/S_0$):
     - Linear payoff: $\Pi_{\text{lin}} = \frac{w}{S_0} (S_1 - S_0) = w \cdot r$.
     - Inverse payoff in coin: $\Pi_{\text{inv, coin}} = w \left(\frac{1}{S_0} - \frac{1}{S_1}\right) = w \frac{S_1 - S_0}{S_0 S_1}$.
     - When converted to USD at the contemporaneous settlement close $S_1$:
       $$\Pi_{\text{inv, USD @ } S_1} = w \left(\frac{1}{S_0} - \frac{1}{S_1}\right) S_1 = w \frac{S_1 - S_0}{S_0} = w \cdot r \quad (\text{source-reported})$$
     - Therefore, marking both legs at the same closing price cancels the price return $\Pi_{\text{lin}} - \Pi_{\text{inv, USD @ } S_1} = 0$ exactly to machine precision ($< 10^{-12}$).
   - The quadratic convexity term $w \cdot r^2 / (1+r)$ appears *only* if the inverse payout is converted back to USD at the original entry price $S_0$ rather than the mark price $S_1$.
   - Consequently, holding {short linear, long inverse} isolates purely the **funding rate spread minus transaction costs**, providing an exact empirical instrument to test the Björk identity.

3. **Empirical Identity Violation & Structural Root Cause:**
   - Over 6.5 years of 8-hour funding rate prints on Binance (August 2020 to August 2026), the author tested two mutually exclusive hypotheses:
     - $H_0^A$: Mean daily funding spread = 0 (the market prices zero convexity).
     - $H_0^B$: Mean daily funding spread − $\sigma^2/365 = 0$ (the market prices the full Björk quanto adjustment).
   - Findings:
     - For BTC (6,450 prints): Observed spread is only +1.77%/yr (0.485 bp/day) vs theoretical fair spread of +33.0%/yr (9.04 bp/day), revealing an empirical shortfall of **−31.6%/yr** ($p = 8.8 \times 10^{-102}$ under Newey-West HAC).
     - For ETH (6,427 prints): Observed spread is only +3.10%/yr (0.851 bp/day) vs theoretical fair spread of +59.6%/yr (16.32 bp/day), revealing an empirical shortfall of **−57.3%/yr** ($p = 3.0 \times 10^{-73}$ under Newey-West HAC).
   - Both $H_0^A$ and $H_0^B$ are rejected: the market prices the convexity with the correct theoretical sign ($+$), but at roughly **one-twentieth (1/20th) of the required magnitude**.
   - **Structural Root Cause:** The author discovered that this discrepancy is not an executable inefficiency, but a mechanical limitation of exchange contract design. On Binance, both linear and inverse funding rates anchor to the exact same underlying spot index price, and approximately **43% of BTC and 42% of ETH inverse funding prints are clamped at the 1 bp (0.01%) base rate floor**. The funding mechanism is structurally pinned and incapable of expressing a 33% to 60%/yr spread. If the convexity premium is priced anywhere, it must reside in the unrecorded mark-price basis.

4. **Category Error of Flow vs Level & Out-of-Sample Falsification:**
   - In trading trials, attempting to trade the deviation $D_t = \text{spread}_t - \text{fair}_t$ (buying when "cheap" and shorting when "rich") produced catastrophic losses (Sharpe −2.98 to −4.00, drawdowns −9% to −13%) due to a foundational category error: **funding P&L is a continuous flow (accrual), not an asset price level**. An underpriced funding spread cannot be bought in anticipation of a capital gain; the trader merely pays negative carry during the holding period.
   - The surviving theoretical rule (holding the theory-predicted receiving side permanently: short linear + long inverse, with 0 parameters and 0 turnover) delivered full-sample Sharpe of +3.26 (BTC) and +4.22 (ETH), but experienced severe structural decay:
     - 2021–2023 Sharpe: **+5.09**
     - 2024–2026 Sharpe: **−1.28**
   - The strategy was formally **REJECTED** by the pre-registered certification gate due to failing the out-of-sample subperiod test and the Deflated Sharpe Ratio against 232 prior trials.

### Research interpretation

This study provides an exemplary dual contribution to quantitative finance:
1. **First-Principles Falsification of Continuous-Time No-Arbitrage in Crypto:** Academic derivative pricing models (e.g. Björk 2009) assume continuous friction-free rebalancing and unconstrained contract design. In cryptocurrency exchanges, institutional rules (such as symmetrical interest rate clamping, identical premium index formulas, and retail-oriented 8-hour funding intervals) prevent funding rates from fulfilling continuous-time no-arbitrage conditions.
2. **Methodological Rigor Against Post-Hoc Data Mining:** By freezing a cumulative ledger of 222 prior research trials and evaluating the Deflated Sharpe Ratio against 232 total attempts, the author demonstrates how apparent historical "home runs" (Sharpe > 3.2 across 6.5 years) decompose into early-market structural carry that evaporated once institutional arbitrageurs entered the market post-2023.

## Signal

### Source-reported

1. **Timestamp Alignment & Daily Aggregation:**
   - Raw funding rates are published at 8-hour intervals (nominally 00:00, 08:00, 16:00 UTC) (`source-reported`).
   - Timestamps carry millisecond jitter across linear and inverse endpoints; `align_funding` rounds timestamps to the nearest hour before performing an inner join (`source-reported`).
   - Daily spread aggregation:
     $$\text{spread}_t = \sum_{k=1}^3 \left(f_{\text{lin}, t, k} - f_{\text{inv}, t, k}\right) \quad (\text{source-reported})$$
   - Only days with exactly 3 matched prints are admitted; partial days are strictly excluded (`source-reported`).
2. **Theoretical Fair Spread Calculation:**
   $$\sigma_{\text{ann}, t}^2 = 365 \times \text{Var}\left(\Delta \ln S_{\tau}\right)_{\tau=t-30}^{t-1} \quad (\text{source-reported})$$
   $$\text{fair}_t = \frac{\sigma_{\text{ann}, t-1}^2}{365} \quad (\text{source-reported})$$
   Realized variance is calculated over a rolling 30-day window of daily log returns and lagged by 1 day to guarantee strict causality (`source-reported`).
3. **Signal Rules Evaluated:**
   - **`always|theoryside` (Primary Surviving Candidate):**
     $$\text{side}_t = +1.0 \quad \forall t \quad (\text{source-reported})$$
     Side $+1.0$ corresponds to {short \$1 linear perp, long \$1 inverse perp}, continuously collecting $f_{\text{lin}} - f_{\text{inv}}$ (`source-reported`).
   - **`theory|db{0, 1e-4}` (Deviation Rule):**
     $$D_t = \text{EMA}_5(\text{spread}_t) - \text{fair}_t \quad (\text{source-reported})$$
     $$\text{side}_t = \begin{cases} +1.0 & \text{if } D_t > \text{deadband} \\ -1.0 & \text{if } D_t < -\text{deadband} \\ \text{side}_{t-1} & \text{otherwise (hysteresis)} \end{cases} \quad (\text{source-reported})$$
   - **`receive|sm{5, 20}` (Smoothed Momentum Carry):**
     $$\text{side}_t = \text{sign}\left(\text{SMA}_k(\text{spread}_t)\right), \quad k \in \{5, 20\} \quad (\text{source-reported})$$
4. **Execution Timing & Causality:**
   - The side decided at date $t$ earns the funding spread of date $t+1$:
     $$\Pi_{t+1} = \text{side}_t \cdot \text{spread}_{t+1} - \frac{|\text{side}_{t+1} - \text{side}_t|}{2} \times C_{\text{flip}} \quad (\text{source-reported})$$
   - Causality and prefix-invariance are unit-tested in `tests/test_quanto_convexity.py` (`source-reported`).

### Research interpretation

The signal construction is deterministic, closed-form, and completely reproducible. The operational logic requires zero machine learning or heuristic parameters. While `theory|db*` and `receive|sm*` generate substantial turnover churn, `always|theoryside` is an unmanaged static carry position whose alpha decay directly reflects market maturation (`research-proposed`).

## Required data

### Source-reported

- **Instruments:**
  - BTC: Binance Linear Perpetual (`BTCUSDT`) and Binance Coin-Margined Inverse Perpetual (`BTCUSD_PERP`) (`source-reported`).
  - ETH: Binance Linear Perpetual (`ETHUSDT`) and Binance Coin-Margined Inverse Perpetual (`ETHUSD_PERP`) (`source-reported`).
- **Data Vendor & Endpoints:**
  - Linear funding: Binance Futures API (`https://fapi.binance.com/fapi/v1/fundingRate`) (`source-reported`).
  - Inverse funding: Binance Delivery API (`https://dapi.binance.com/dapi/v1/fundingRate`) (`source-reported`).
  - Hourly kline prices: Binance 1-hour OHLCV close prices for realized volatility computation (`source-reported`).
- **Sampling & Timeframes:**
  - 8-hour funding intervals (00:00, 08:00, 16:00 UTC) (`source-reported`).
  - 1-hour and 1-day resampled bars (`source-reported`).
- **Data Cleansing & Missing Prints:**
  - Nanosecond/millisecond network jitter handled via hour-rounding (`source-reported`).
  - Incomplete days (< 3 prints) filtered out to prevent partial-interval return distortion (`source-reported`).
- **Cached Datasets Committed in Repository:**
  - `data/FUNDING_BTCUSDT_20200101_20260630.parquet` (137 KB) (`source-reported`).
  - `data/DFUNDING_BTCUSD_PERP_20200801_20260824.parquet` (127 KB) (`source-reported`).
  - `data/FUNDING_ETHUSDT_20200101_20260630.parquet` (138 KB) (`source-reported`).
  - `data/DFUNDING_ETHUSD_PERP_20200801_20260824.parquet` (128 KB) (`source-reported`).
  - `data/PERP_BTCUSDT_1h_20210101_20260824.parquet` (3.85 MB) (`source-reported`).
  - `data/PERP_ETHUSDT_1h_20210101_20260824.parquet` (3.76 MB) (`source-reported`).

### Research interpretation

All data inputs are publicly accessible without authentication. The inclusion of committed Parquet fixtures enables 100% offline mathematical and statistical verification without live network dependencies (`research-proposed`).

## Execution assumptions

### Source-reported

- **Position Sizing:** Fixed \$1 notional per leg (\$1 short linear, \$1 long inverse) (`source-reported`).
- **Rebalancing / Execution Model:** Daily discrete settlement; positions adjust at 00:00 UTC close (`source-reported`).
- **Transaction Costs:**
  - Taker fee: 7 bps (0.0007) per leg (`source-reported`).
  - Full side reversal cost ($C_{\text{flip}}$): 4 legs $\times$ 7 bps = **28 bps (0.0028)**, accounting for closing two legs and opening two legs (`source-reported`).
  - Partial turnover cost: Pro-rata charge $\frac{|\Delta \text{side}|}{2} \times 0.0028$ (`source-reported`).
- **Margin & Collateral:**
  - Linear perp requires USDT margin; inverse perp requires BTC or ETH coin collateral (`source-reported`).
  - Margin segregation and cross-collateral rebalancing frictions are unmodeled in the backtest (`source-reported`).
- **Mark-Price Basis Volatility:**
  - The model assumes both legs are marked at identical USD prices at the settlement boundary (`source-reported`).
  - High-frequency intra-day basis divergence between the two perpetuals is unmodeled (`source-reported`).

### Research interpretation

The 7 bps per leg fee assumption is realistic for standard retail-to-VIP tier taker execution on Binance perpetuals. However, because inverse contracts require posting native BTC/ETH, an investor holding the pair must either purchase physical coin collateral or utilize Unified Portfolio Margin, introducing collateral liquidation or borrow interest costs that are not reflected in the pure spread series (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures trace directly to committed JSON artifacts (`results/quanto_convexity.json`), logs (`results/study_log.md`), and code execution in `mykola-zadir/bjork-quanto-convexity` (commit `feac9fd414e4`):

#### 1. Identity Test Results (6.5-Year Sample)

| Metric | BTC (`BTCUSDT` vs `BTCUSD_PERP`) | ETH (`ETHUSDT` vs `ETHUSD_PERP`) |
| :--- | :--- | :--- |
| Evaluated 8h prints | 6,450 | 6,427 |
| Inverse prints pinned at 1 bp base rate | 43% | 42% |
| Observed daily spread | 0.485 bp/day (+1.77%/yr) | 0.851 bp/day (+3.10%/yr) |
| Theoretical fair spread ($\sigma^2/365$) | 9.04 bp/day (+33.0%/yr) | 16.32 bp/day (+59.6%/yr) |
| Empirical shortfall | **−31.6%/yr** | **−57.3%/yr** |
| $H_0^A$ ($p$-value, mean spread = 0) | $0.000$ | $0.000$ |
| $H_0^B$ ($p$-value, mean shortfall = 0) | $8.8 \times 10^{-102}$ | $3.0 \times 10^{-73}$ |

#### 2. Trading Performance Across Frozen Rules (Full Sample)

| Trial Key | Ann. Return | Sharpe | 95% Mertens CI | Max Drawdown | Newey-West $p$ | Flips/Yr | Sample Days ($n$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `ETH|always|theoryside` | +3.07% | +4.22 | [+3.46, +4.98] | −1.62% | $6.76 \times 10^{-8}$ | 0.0 | 2,141 |
| `BTC|always|theoryside` | +1.74% | +3.26 | [+2.60, +3.92] | −1.20% | $1.21 \times 10^{-5}$ | 0.0 | 2,149 |
| `ETH|receive|sm20` | −1.52% | −1.08 | [−1.83, −0.34] | −21.22% | 0.954 | 16.79 | 2,141 |
| `BTC|receive|sm20` | −3.01% | −2.21 | [−2.87, −1.56] | −20.77% | 1.000 | 17.58 | 2,149 |
| `BTC|theory|db1e-4` | −1.42% | −2.98 | [−3.60, −2.35] | −9.14% | 1.000 | 0.42 | 2,149 |
| `BTC|theory|db0` | −1.52% | −2.99 | [−3.59, −2.40] | −9.35% | 1.000 | 0.76 | 2,149 |
| `ETH|receive|sm5` | −6.25% | −3.28 | [−3.96, −2.59] | −37.58% | 1.000 | 36.57 | 2,141 |
| `ETH|theory|db0` | −2.15% | −3.80 | [−4.48, −3.13] | −12.62% | 1.000 | 0.43 | 2,141 |
| `ETH|theory|db1e-4` | −2.19% | −4.00 | [−4.59, −3.41] | −12.82% | 1.000 | 0.43 | 2,141 |
| `BTC|receive|sm5` | −8.37% | −4.43 | [−5.04, −3.81] | −39.71% | 1.000 | 40.00 | 2,149 |

#### 3. Certification Battery Verdict for Best Candidate (`BTC|always|theoryside`)

- **Sharpe CI:** PASS (95% CI [+2.60, +3.92] strictly excludes zero) (`source-reported`).
- **PBO (CSCV):** PASS (`source-reported`).
- **Replication (ETH Twin):** PASS (Replicated on ETH with Sharpe +4.22) (`source-reported`).
- **Deflated Sharpe Ratio (DSR):** **FAIL** (Tested against 232 cumulative trials, fails anti-data-mining threshold) (`source-reported`).
- **Out-of-Sample Sub-Period Gate:** **FAIL** (2021–2023 Sharpe was **+5.09**, but 2024–2026 Sharpe collapsed to **−1.28**) (`source-reported`).
- **Final Official Strategy Verdict:** **`REJECTED`** (`source-reported`).

### Independently reproduced

`Not independently reproduced.` All statistical outputs, $p$-values, confidence intervals, and drawdown curves represent primary research executed and reported by Mukola Hotstore in GitHub repository `mykola-zadir/bjork-quanto-convexity` (commit `feac9fd414e4`). No internal backtest in our PyBroker or NautilusTrader infrastructure has been executed.

### Negative evidence

1. **Failure of Continuous-Time No-Arbitrage:** The empirical funding rate spread fails to reflect the continuous-time quanto convexity identity by a factor of 20x. Rather than reflecting a 33% to 60%/yr spread, the observed spread is only 1.77% to 3.10%/yr.
2. **Failure of Convergence Trading Rules:** Trading the deviation between observed funding and theoretical fair value results in severe negative Sharpe ratios (−2.98 to −4.00) because funding rates are flows rather than mean-reverting asset prices.
3. **Severe Post-2023 Alpha Decay:** The unmanaged theory-side carry suffered severe performance collapse, dropping from Sharpe +5.09 in 2021–2023 to −1.28 in 2024–2026 as institutional participants eliminated the structural funding discrepancy.

## Falsification plan

To further test and stress the quanto convexity and funding basis hypotheses across other crypto assets and venues:

1. **Cross-Exchange Falsification:**
   - Test the linear-vs-inverse funding rate identity on OKX, Bybit, and Deribit (`research-proposed`).
   - If other exchanges with different funding calculation mechanics (e.g. Deribit's 1-minute sampling or OKX's premium index formulas) exhibit identical 1/20th shortfalls, it confirms that contract clamping is an industry-wide structural invariant rather than a Binance-specific anomaly (`research-proposed`).
2. **Mark-Price Basis Audit:**
   - Ingest high-frequency (tick or 1-second) order book and mark-price feeds for linear vs inverse contracts (`research-proposed`).
   - Measure whether the missing 31% (BTC) and 57% (ETH) convexity premium is embedded in the average perpetual mark-to-index basis ($P_{\text{mark}} - P_{\text{index}}$) (`research-proposed`).
   - If the mark-price basis differential is zero or uncorrelated with $\sigma^2 \Delta t$, the hypothesis that "convexity lives in the basis" is falsified (`research-defined falsification threshold`).
3. **Altcoin Inverse Perpetual Expansion:**
   - Test the identity on lower-liquidity altcoins listing coin-margined contracts (e.g. SOL, ADA, XRP) (`research-proposed`).
   - If less-arbitraged altcoins display higher funding spreads that align more closely with $\sigma^2 \Delta t$, it would support the hypothesis that market maturation and institutional capital destroyed the BTC/ETH spread (`research-proposed`).
   - Failure cutoff: If altcoins exhibit Sharpe < 0.5 net of higher borrow/hedging costs, reject altcoin applicability (`research-defined falsification threshold`).

## Crypto portability

`direct`

This strategy and empirical test are crypto-native, evaluated directly on Binance cryptocurrency perpetual futures (`BTCUSDT`, `BTCUSD_PERP`, `ETHUSDT`, `ETHUSD_PERP`).

**Crypto-Specific Structural Factors:**
1. **Collateral Numeraire Asymmetry:** Inverse perpetuals require posting native cryptocurrency (BTC/ETH), creating collateral exposure that must be separately hedged or funded unless operating within a cross-collateralized Unified Account.
2. **Funding Settlement Mechanism:** 8-hour discrete funding intervals allow intra-interval price fluctuations that can create temporary liquidation risk on individual legs despite overall portfolio dollar-neutrality.
3. **Exchange Base Rate Clamping:** Institutional exchange rules (such as the 0.01% 8-hour floor on Binance when the premium index is flat) structurally suppress the expression of continuous volatility dynamics.

## Limitations

1. **Unmodeled Mark-Price Basis Volatility:** The research assumes zero price divergence between linear and inverse contracts at daily close boundaries. In live execution, basis fluctuations between the two contracts could create unexpected mark-to-market drawdowns.
2. **Margin Fragmentation & Borrow Costs:** Operating a short linear (USDT) and long inverse (BTC) book requires maintaining separate collateral pools or paying borrowing interest on USD/coin assets in Unified Margin modes.
3. **Post-2023 Structural Decay:** The strategy is officially rejected for live trading due to the complete collapse of the carry spread post-2023 (Sharpe −1.28 in 2024–2026).
4. **Absence of Historical Basis Data:** Because historical tick-level mark-price premium records are not archived publicly by Binance, the hypothesis that the remaining convexity premium resides in the basis remains empirically unproven.

## Implementation status

`not-implemented`

No implementation of this pair carry or quanto convexity test exists in our internal PyBroker or NautilusTrader research environments. The strategy is documented here strictly as a high-fidelity quantitative falsification study and economic mechanism reference.

## Adoption boundary

`research-only` / `not-approved`

This capture is strictly research material. A record being present in this repository does not constitute approval for paper trading, testnet deployment, or live trading. The strategy failed pre-registered certification gates and is classified as `REJECTED` by its primary author.

## Related Wiki records

- `[[quant/perpetual-inverse-linear-margin-currency-funding-spread-2026-09-01]]` (BitMEX Research / Shang Wu heuristic collateral demand asymmetry hypothesis; evaluated here under continuous-time quanto no-arbitrage with exact cancellation and funding clamp falsification)
- `[[quant/cross-venue-perpetual-funding-carry-cost-decay-falsification-2026-09-13]]` (DavidAyusoPita 2026: Cross-venue perpetual funding carry decay and transaction cost hurdles)
- `[[quant/funding-adjusted-cross-exchange-perpetual-price-space-arbitrage-2026-09-12]]` (Ho & Chan 2026: Cross-exchange perpetual funding rate basis)
- `[[quant/rl-market-making-funding-rate-capture-crypto-perpetual-2026-09-12]]` (Dynamic funding rate capture in crypto perpetuals)
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` (Foundational validation principles and out-of-sample partitioning)

## Sources

1. **Primary Research Repository:** Mukola Hotstore (`mykola-zadir`), *"Quanto Convexity in Crypto Perpetuals — A Björk Identity Test"*, GitHub repository `mykola-zadir/bjork-quanto-convexity`, commit `feac9fd414e427e21cfc7ca761f619ea2718aad2`, dated 2026-08-26 21:27:51 UTC. URL: [https://github.com/mykola-zadir/bjork-quanto-convexity](https://github.com/mykola-zadir/bjork-quanto-convexity)
2. **Primary Study Log & Empirical Output:** Mukola Hotstore, `results/study_log.md` and `results/quanto_convexity.json`, commit `feac9fd414e4`.
3. **Primary Algorithmic Code:** Mukola Hotstore, `strategy/quanto_convexity.py`, `verify_quanto_convexity.py`, `backtest/certify.py`, and `tests/test_quanto_convexity.py`, commit `feac9fd414e4`.
4. **Theoretical Reference:** Tomas Björk, *Arbitrage Theory in Continuous Time*, Oxford University Press, 3rd Edition 2009 / 4th Edition 2020. Chapters:
   - Chapter 4: Itô's Lemma (convexity drift adjustment $d(1/S) = -\frac{1}{S}(\mu - \sigma^2)dt - \frac{\sigma}{S}dW$).
   - Chapter 13: Currency and Quanto Derivatives (quanto payout currency and non-linear drift).
   - Chapter 26: Change of Numeraire (Girsanov transformation and martingale measures).
