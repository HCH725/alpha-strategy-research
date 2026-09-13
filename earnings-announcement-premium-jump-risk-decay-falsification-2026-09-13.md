---
schema: strategy-research-record-v1
title: "Earnings-Announcement Premium: Scheduled Jump-Risk Compensation Falsification, Post-2020 Decay, and Event-Window Volatility Confounding"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - earnings-announcement-premium
  - event-study
  - jump-risk
  - abnormal-returns
  - falsification
  - equity-cross-section
  - decay
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "JonathanBeck1, 'Decision: Earnings-Announcement Premium (T43)', research/earnings_premium_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_premium_decision.md"
  - "JonathanBeck1, 'Pre-registration: Earnings-Announcement Premium (T43)', research/earnings_premium_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_premium_preregistration.md"
  - "JonathanBeck1, 'T43 — Earnings-Announcement Premium Study Result', research/earnings_premium_report.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_premium_report.md"
  - "JonathanBeck1, 'Python Pure Earnings Premium Core Implementation', src/trader/catalysts/earnings_premium.py (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/src/trader/catalysts/earnings_premium.py"
  - "JonathanBeck1, 'End-to-End Earnings Premium Study Runner', scripts/run_earnings_premium_study.py (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/scripts/run_earnings_premium_study.py"
  - "JonathanBeck1, 'Financial Unit Tests for Earnings Premium Core', tests/financial/test_earnings_premium.py (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/tests/financial/test_earnings_premium.py"
  - "JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 4.6, 4.7, Table 6 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
  - "Beaver, W. H. (1968), 'The Information Content of Annual Earnings Announcements', Journal of Accounting Research, 6, 67–92."
  - "Chari, V. V., Jagannathan, R., & Ofer, A. R. (1988), 'Risk, Return, and the Timing of Corporate Disclosures: An Investigation of the Earnings Announcement Effect', Journal of Financial Economics, 21(2), 177–201."
  - "Frazzini, A., & Lamont, O. A. (2007), 'The Earnings Announcement Premium and Trading by Individual Investors', The Journal of Finance, 62(5), 2385–2419."
  - "Barber, B. M., De George, E. T., Lehavy, R., & Trueman, B. (2013), 'The Earnings Announcement Premium Around the Globe', The Journal of Financial Economics, 108(1), 118–138."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Earnings-Announcement Premium: Scheduled Jump-Risk Compensation Falsification, Post-2020 Decay, and Event-Window Volatility Confounding

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`)
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`)
- **Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`)
- **As-of Date:** 2026-09-13 (empirical execution run: 2026-06-14T13:51:13Z) (`source-reported`)
- **Primary Source File Paths:**
  - `research/earnings_premium_decision.md`: Official audit decision record detailing the `KILL` verdict, empirical metrics, pre-registered gate evaluation, and diagnostic findings (`source-reported`).
  - `research/earnings_premium_preregistration.md`: Pre-registered research protocol defining the hypothesis, fixed 49-ticker universe, BMO/AMC time-of-day convention, market-adjusted abnormal return model, [-1, +1] event-time window, 10 bps round-trip friction, same-stock non-earnings baseline, and kill criteria (`source-reported`).
  - `research/earnings_premium_report.md`: Complete empirical output report logging sample accounting (2,156 events, 2,940 placebo windows), gross vs after-cost abnormal returns, in-sample vs out-of-sample partitions, event-window Sharpe, and top-5 contributor events (`source-reported`).
  - `src/trader/catalysts/earnings_premium.py`: Pure Python core implementing abnormal return calculation, BMO/AMC $t_0$ resolution, event CAR slicing, non-earnings baseline sampling, cohort aggregation, and gate evaluation (`source-reported`).
  - `scripts/run_earnings_premium_study.py`: End-to-end runner script fetching yfinance earnings dates and daily split/dividend-adjusted prices, executing the full pipeline, and logging JSON/text artifacts (`source-reported`).
  - `tests/financial/test_earnings_premium.py`: Suite of 25 network-free unit tests verifying edge cases, abnormal return calculations, and gate logic (`source-reported`).
  - `research/PAPER_DRAFT.md`: Campaign synthesis paper classifying T43 under Campaign Failure Class 7 ("Compensated Risk / Beta-in-Disguise") and Class 8 ("Decay / In-Noise") (§4.6, §4.7, Table 6) (`source-reported`).
- **Primary Source Verification:** Directly inspected and verified source code, statistical equations, runner scripts, unit tests, and empirical report tables from commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. All empirical values, $t$-statistics, correlation figures, sample sizes, and gate verdicts trace directly to these primary files.
- **Repository Deduplication Audit:** A comprehensive grep across all existing records in `alpha-strategy-research` confirmed zero prior records analyzing the earnings announcement equity holding premium (`earnings-announcement premium`). While another single-name equity earnings record exists (`single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13.md` [T23]), that study investigates an options derivatives strategy (short ATM straddles harvesting implied volatility crush vs realized move) and documents an options bid-ask friction and tail jump loss mechanism. In contrast, T43 investigates the equity spot cash holding premium (holding underlying common shares through scheduled earnings dates vs SPY benchmark), evaluates uncompensated equity alpha vs jump risk compensation, and provides independent empirical evidence across 2,156 historical earnings events.

## Economic mechanism

### Source-reported

1. **The Classical Earnings Announcement Premium Hypothesis:**
   In foundational financial economics literature (Beaver 1968; Chari, Jagannathan, and Ofer 1988; Frazzini & Lamont 2007; Barber, De George, Lehavy, and Trueman 2013), stocks exhibit positive abnormal returns during corporate earnings announcement windows. Because corporate earnings release dates are scheduled well in advance, they represent large, discrete, non-diversifiable information arrival events that generate heavy two-sided return variance ("scheduled jump risk").
2. **Behavioral and Risk-Aversion Rationale:**
   The source-reported economic rationale posits that risk-averse or attention-constrained market participants systematically avoid holding concentrated single-stock equity exposure across scheduled earnings announcements to avert catastrophic negative headline shocks. This pre-announcement avoidance selling exerts downward price pressure on the equity immediately prior to the event. Consequently, market makers and arbitrageurs who bear this scheduled jump risk demand an ex-ante positive expected return premium to hold physical inventory across the announcement print.
3. **Decay and Information Efficiency Prior:**
   Academic literature has historically documented that the earnings announcement premium is strongest in neglected, illiquid, or small-cap equities with low analyst coverage, and that the effect has decayed over time as quantitative hedge funds and institutional capital actively chased the anomaly. On highly liquid, heavily scrutinized mega-cap and large-cap US equities, market efficiency implies that the premium should either be entirely arbed away by modern execution algorithms or represent pure compensation for bearing jump variance rather than uncompensated alpha.

### Research interpretation

1. **Compensated Jump-Risk Variance vs True Alpha:**
   The central empirical question is whether the earnings announcement premium represents an exploitable market inefficiency (excess risk-adjusted alpha) or a trivial factor loading on discrete jump variance (a risk premium). If holding through the announcement earns a positive return solely because the investor absorbs high realized volatility, the strategy's Sharpe ratio will be mediocre, and realized abnormal returns across events will correlate strongly with event-window realized volatility:
   $$\text{Corr}(|\text{CAR}_{[-1, +1]}|, \sigma_{\text{event}}) \gg 0$$
   Under this condition, the payoff profile resembles an unhedged short volatility / catastrophe insurance position rather than an informational trading edge (`research-proposed`).
2. **Distinction from Post-Earnings Announcement Drift (PEAD):**
   The earnings announcement premium (T43) is structurally distinct from Post-Earnings Announcement Drift (PEAD, evaluated and killed in T07). PEAD conditions on the sign and magnitude of the unexpected earnings surprise (Standardized Unexpected Earnings, SUE) and holds the stock over subsequent weeks ($[+1, +21]$ trading days) to capture delayed market underreaction. The announcement premium is an ex-ante unconditional strategy that holds the stock strictly *through* the print ($[-1, +1]$ trading days around $t_0$) based entirely on pre-scheduled disclosure dates, requiring zero post-event information (`research-proposed`).

## Signal

### Pre-Registered Signal Specification

The trading signal is an ex-ante, calendar-driven event capture rule executed across corporate earnings announcements:

1. **Announcement Calendar & Event Time Resolution ($t_0$):**
   - Corporate earnings announcement dates are obtained from corporate investor relations disclosures via `yfinance` `Ticker.get_earnings_dates(limit=100)`. Because scheduled release dates are published weeks in advance, the event date is known ex-ante and introduces zero look-ahead bias (`source-reported`).
   - The first trading session that prices the corporate release is designated as event day $t_0$:
     - **Before Market Open (BMO):** If the announcement timestamp hour is strictly before 13:00 US/Eastern (`hour_et < 13`), the market prices the release during that same trading session. Thus, $t_0$ is the trading session occurring on the calendar announcement date (`source-reported`).
     - **After Market Close (AMC):** If the announcement timestamp hour is at or after 13:00 US/Eastern (`hour_et >= 13`), or if the time-of-day timestamp is missing (default heuristic), the release cannot be priced during regular trading hours on the announcement date. Thus, $t_0$ is the first trading session strictly *after* the calendar announcement date (`source-reported`).
2. **Cumulative Abnormal Return Windows (Event-Trading-Day Time):**
   - Returns are calculated as simple percentage returns on split/dividend-adjusted daily closes:
     $$r_{i, t} = \frac{P_{i, t}}{P_{i, t-1}} - 1$$
   - Abnormal returns ($AR$) are market-adjusted against the S&P 500 ETF (SPY) under a fixed $\beta = 1.0$ convention:
     $$AR_{i, t} = r_{i, t} - r_{\text{SPY}, t}$$
     (`source-reported`).
   - **PRIMARY Evaluation Window (`car_m1_p1`):** A 3-trading-day holding period covering event days $\tau \in \{-1, 0, +1\}$ relative to $t_0$:
     $$\text{CAR}_{[-1, +1]} = \sum_{\tau = -1}^{+1} AR_{i, t_0 + \tau}$$
     This window explicitly captures holding the physical equity *through* the scheduled print: entering at the close of $t_0 - 2$ (or opening of $t_0 - 1$) and exiting at the close of $t_0 + 1$ (`source-reported`).
   - **Secondary Window 1 (`car_0_p1`):** A strict post-announcement no-pre-event-leg window covering event days $\tau \in \{0, +1\}$:
     $$\text{CAR}_{[0, +1]} = \sum_{\tau = 0}^{+1} AR_{i, t_0 + \tau}$$
     (`source-reported`).
   - **Secondary Window 2 (`car_0_p0`):** Announcement-day only reaction window:
     $$\text{CAR}_{[0, 0]} = AR_{i, t_0}$$
     (`source-reported`).
3. **Same-Stock Non-Earnings Baseline (Matched Placebo Control):**
   - For each equity in the universe, candidate non-earnings anchor dates $t_{\text{placebo}}$ are identified such that $t_{\text{placebo}}$ does not fall within an exclusion buffer of $\pm 5$ trading days around any historical earnings $t_0$ (`source-reported`).
   - A matched 3-day placebo CAR is computed across the same window offsets:
     $$\text{CAR}_{\text{placebo}} = \sum_{\tau = -1}^{+1} AR_{i, t_{\text{placebo}} + \tau}$$
   - Exactly $N = 60$ random non-earnings windows are sampled per ticker ($N = 2,940$ pooled baseline windows) using a fixed random seed (`SEED = 43`) (`source-reported`).
   - The true announcement premium is defined as the cohort announcement mean minus the same-stock non-earnings baseline mean:
     $$\Delta_{\text{premium}} = \mu(\text{CAR}_{\text{event}}) - \mu(\text{CAR}_{\text{placebo}})$$
     absorbing any persistent single-name drift or beta-mismatch residual (`source-reported`).
4. **Position Sizing and Portfolio Construction:**
   - Equal-weighted allocation across all eligible earnings events occurring on each trading date (`research-proposed`).
   - 100% long cash equity position held through the 3-day event window, with an equal notional short position in SPY to hedge systematic market beta (`research-proposed`).
5. **Data Glitch Filter:**
   - Any event or placebo window containing a single daily abnormal return exceeding $\pm 60\%$ (`MAX_ABS_DAILY_ABN = 0.60`) is flagged as an exchange data glitch and excluded from the sample (`source-reported`).

## Required data

- **Asset Universe:** Fixed ex-ante universe of 49 liquid US mega-cap and large-cap single-name equities (`source-reported`):
  - 10 Mega-caps: `NVDA`, `AAPL`, `MSFT`, `AMZN`, `META`, `GOOGL`, `TSLA`, `AVGO`, `BRK-B`, `JPM`.
  - 39 Large/Mid-caps: `AMD`, `ORCL`, `CRM`, `COST`, `NFLX`, `ADBE`, `INTC`, `QCOM`, `JNJ`, `PFE`, `MRK`, `LLY`, `ABBV`, `UNH`, `HD`, `LOW`, `WMT`, `DIS`, `NKE`, `MCD`, `KO`, `PEP`, `XOM`, `CVX`, `BA`, `V`, `MA`, `BAC`, `WFC`, `GS`, `MS`, `CAT`, `GE`, `HON`, `IBM`, `CSCO`, `TXN`, `T`, `VZ`.
- **Benchmark Instrument:** `SPY` (SPDR S&P 500 ETF Trust) (`source-reported`).
- **Primary Data Fields:**
  - Corporate earnings announcement calendar timestamps with hour-level precision to identify BMO vs AMC scheduling (`source-reported`).
  - Daily split- and dividend-adjusted closing prices (`auto_adjust=True`) for all 49 equities and `SPY` (`source-reported`).
- **Sample Span & Subperiod Partitioning:**
  - Full sample: 2015-01-01 through 2025-12-31 (11 calendar years) (`source-reported`).
  - In-Sample (IS) partition: Event calendar year $\le 2020$ (2015–2020, 6 years) (`source-reported`).
  - Out-of-Sample (OOS) partition: Event calendar year $\ge 2021$ (2021–2025, 5 years) (`source-reported`).
- **Point-in-Time Integrity:**
  - Scheduled earnings announcement dates are announced by corporate issuers weeks in advance of the actual disclosure date and are strictly known prior to event day $t_0 - 1$ (`source-reported`).
  - No post-event variables (such as reported EPS, revenue surprises, guidance revisions, or post-earnings market movements) are utilized in cohort selection or signal formation (`source-reported`).
- **Missing Data Handling:** If an equity lacks sufficient price history to pad the required $[-1, +1]$ window (including an additional buffer of $[-1, +1]$ for multi-window consistency), the event is omitted (`incomplete`). Across the 49 names, 0 events were dropped due to data glitches or incomplete windows (`source-reported`).

## Execution assumptions

- **Execution Venue:** US National Market System (NYSE, NASDAQ) cash equity exchanges (`source-reported`).
- **Order Timing:** 
  - Entry: Market close on event day $t_0 - 2$ (or market open on $t_0 - 1$) (`source-reported` / `research-proposed`).
  - Exit: Market close on event day $t_0 + 1$ (`source-reported` / `research-proposed`).
- **Execution Cost & Friction Model:**
  - Conservative round-trip execution friction for liquid large-cap US equities is modeled as **10 bps per event** (5 bps half-spread and market impact on entry, 5 bps on exit: `ROUND_TRIP_COST = 0.0010`) (`source-reported`).
  - After-cost cumulative abnormal return is computed by deducting 10 bps once per event:
    $$\text{CAR}_{\text{after-cost}} = \text{CAR}_{\text{gross}} - 0.0010$$
    (`source-reported`).
  - For market-hedged implementations holding a short SPY leg, an additional 2 bps round-trip ETF friction and borrowing cost must be accounted for (`research-proposed`).
- **Margin & Leverage:** Fully funded 1x cash equity long, 1x ETF short hedge (`research-proposed`).
- **Borrow Availability:** All 49 tickers are mega/large-cap general collateral equities with borrowing availability exceeding 99% and borrow fees below 30 bps/yr (`research-proposed`).

## Evidence

### Source-reported

All quantitative metrics, statistical test results, and empirical tables below are directly extracted from the primary study report (`research/earnings_premium_report.md`), decision record (`research/earnings_premium_decision.md`), and raw output data (`data/earnings_premium_results.txt`) from commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`.

#### 1. Primary Announcement-Window Performance (`car_m1_p1`: [-1, +1] Event Days)

| Empirical Metric | Source-Reported Value | Pre-Registered Gate Hurdle | Status |
|:-----------------|:---------------------:|:---------------------------|:-------|
| Usable Earnings Events ($N$) | **2,156** | $N \ge 30$ | **PASS** |
| Unique Equities Contributing | 49 / 49 tickers | Full coverage | **PASS** |
| Events Dropped (glitch / incomplete) | 0 (0.0%) | Quality check | **PASS** |
| Gross Mean Abnormal Return ($\mu_{\text{gross}}$) | **+0.344%** (+34.4 bps) | Informational | Positive |
| After-Cost Mean Abnormal Return ($\mu_{\text{net}}$) | **+0.244%** (+24.4 bps) | $\mu_{\text{net}} > 0$ | Positive |
| After-Cost $t$-Statistic | **+1.85** | $|t| \ge 2.00$ | **FAIL** (Insignificant) |
| Median Abnormal Return | **+0.182%** (+18.2 bps) | Informational | Positive |
| Strategy Win Rate | **51.8%** | Informational | Near coin flip |
| Event-Window Sharpe Ratio ($\mu / \sigma$) | **+0.056** | Informational | Negligible |

#### 2. Matched Baseline & Placebo Disconfirmation

| Sample / Control Cohort | Observations ($N$) | Mean Abnormal Return | $t$-Statistic | Gate Hurdle | Status |
|:------------------------|:------------------:|:--------------------:|:-------------:|:------------|:-------|
| Matched Non-Earnings Placebo Baseline | 2,940 | **+0.041%** | **-1.27** | $|t| < 2.00$ | **PASS** (Clean null) |
| True Announcement Premium (Cohort $-$ Baseline) | 2,156 vs 2,940 | **+0.303%** (+30.3 bps) | **+2.17** (Welch $t$) | Premium $> 0$ | **PASS** (Genuine event effect) |

#### 3. Subperiod Temporal Decay Analysis (In-Sample vs Out-of-Sample)

The pre-registered protocol partitioned the 11-year evaluation span into an In-Sample (IS) calibration phase (2015–2020) and an Out-of-Sample (OOS) validation phase (2021–2025):

| Partition Period | Calendar Years | Events ($n$) | After-Cost Mean | $t$-Statistic | Subperiod Status |
|:-----------------|:--------------:|:------------:|:---------------:|:-------------:|:-----------------|
| In-Sample (IS)   | 2015–2020      | 1,176        | **+0.459%** (+45.9 bps) | **+2.76** | Statistically significant |
| Out-of-Sample (OOS) | 2021–2025   | 980          | **-0.014%** (-1.4 bps)  | **-0.07** | **Complete decay to zero (sign flip)** |

- **Pre-registered Gate Evaluation:** **FAIL**. The strategy fails the OOS sign stability requirement. The after-cost premium collapsed from $+0.459\%$ ($t = +2.76$) in 2015–2020 to $-0.014\%$ ($t = -0.07$) in 2021–2025, demonstrating severe temporal decay.

#### 4. Decisive Mechanism Check: Jump-Risk Compensation vs Alpha

- **Pearson Correlation:**
  $$\text{Corr}(|\text{CAR}_{[-1, +1]}|, \sigma_{\text{event\_window}}) = \mathbf{+0.734}$$
- **Mechanism Interpretation:** The empirical correlation between the magnitude of the abnormal return $|CAR|$ and the realized event-window volatility ($\sigma$) is strongly positive ($r = +0.734$). This confirms that the observed return is not an unpriced behavioral anomaly or informational alpha; rather, it is pure compensation for bearing the scheduled jump variance of earnings announcements. When volatility is high, realized dispersion expands symmetrically, and the residual premium vanishes once adjusted for this jump variance.

#### 5. Secondary Non-Gating Evaluation Windows

- **`car_0_p1` (Days [0, +1], Strict Post-Event Leg):**
  - Gross Mean: $+0.254\%$
  - After-Cost Mean: $+0.154\%$
  - $t$-Statistic: $+1.18$ ($n = 2,156$)
- **`car_0_p0` (Day [0, 0], Announcement Day Only):**
  - Gross Mean: $+0.207\%$
  - After-Cost Mean: $+0.107\%$
  - $t$-Statistic: $+0.91$ ($n = 2,156$)

#### 6. Top-5 Contributor Inspection & Outlier Robustness

The top 5 single-day abnormal return contributors across the 2,156 events were:
1. `AMD` (2016-04-22): $+36.5\%$
2. `AVGO` (2024-12-13): $+34.4\%$
3. `ORCL` (2025-09-10): $+29.6\%$
4. `CRM` (2020-08-26): $+29.6\%$
5. `TSLA` (2019-10-24): $+25.9\%$

- **Mean Abnormal Return Excluding Top-5:** **+0.272%** (compared to the full sample gross mean of **+0.344%**).
- **Outlier Assessment:** The too-good tripwire was not triggered (Sharpe = 0.056, win rate = 51.8%). The effect is not an artifact of a few extreme outlier wins; rather, it is broadly distributed across the universe, but economically tiny and heavily decaying.

### Independently reproduced

`Not independently reproduced.` All empirical figures, tables, $t$-statistics, and correlation metrics represent third-party research results reported by Jonathan Beck (`JonathanBeck1/falsification-campaign` at commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`).

### Negative evidence

- **Failure of Statistical Significance After Costs:** Over 2,156 liquid large-cap earnings events, the after-cost abnormal return of $+0.244\%$ generates a $t$-statistic of only $+1.85$, failing to achieve the standard two-tailed significance threshold ($|t| \ge 2.00$, $p \approx 0.064$).
- **Complete Out-of-Sample Alpha Decay:** In the 2021–2025 out-of-sample period (980 events), the after-cost premium fell to $-0.014\%$ ($t = -0.07$), representing complete decay of the anomaly in large-cap equities.
- **Compensated Jump-Risk Variance Overlay:** The $+0.734$ correlation between realized abnormal returns and event-window volatility confirms that what little historical return existed was compensation for bearing discrete earnings jump risk rather than an unhedged arbitrage edge.
- **Low Sharpe Ratio & Mediocre Win Rate:** The event-window Sharpe ratio is $+0.056$ and the win rate is $51.8\%$, reflecting an unfavorable risk-reward trade-off that cannot survive retail or institutional execution hurdles.

## Falsification plan

To falsify the author's negative findings and determine whether an earnings announcement strategy can produce genuine risk-adjusted alpha under modified conditions, the following stress tests are defined:

1. **Neglected Small-Cap / Micro-Cap Universe Expansion Test:**
   - *Data & Universe:* Expand the universe from 49 liquid mega/large-caps to the Russell 2000 universe, filtering for neglected equities with low institutional ownership ($<30\%$) and low analyst coverage ($\le 2$ covering analysts).
   - *Metric:* After-cost cumulative abnormal return over $[-1, +1]$, deducting realistic tiered micro-cap execution costs (30 bps round-trip) and short borrowing fees.
   - *Decision Rule:* If the after-cost CAR fails to achieve an annualized Sharpe $\ge 1.00$ and $t \ge 2.50$ (`research-defined falsification threshold`), the claim that the earnings announcement premium survives in neglected small-caps is definitively falsified.
2. **Implied Volatility Mispricing Conditioning Test:**
   - *Data & Method:* Filter earnings events using pre-event options implied volatility. Specifically, compare pre-announcement 30-day ATM implied volatility ($IV$) against historical realized volatility ($RV$). Condition entry on names where $IV$ is in the bottom quartile of its historical distribution (cheap event volatility).
   - *Metric:* Out-of-sample after-cost abnormal return across IV-conditioned events.
   - *Decision Rule:* If IV conditioning fails to increase the after-cost $t$-statistic above $2.00$ (`research-defined falsification threshold`), the hypothesis that volatility conditioning unlocks exploitable announcement alpha is falsified.
3. **Firm Quality and Momentum Conditioning (Hybrid Screen):**
   - *Data & Method:* Condition long positions on firms exhibiting high earnings quality (Piotroski F-score $\ge 8$) and strong 12-month pre-announcement momentum ($r_{12-1} > \text{median}$).
   - *Metric:* Cross-sectional spread between quality-momentum winners and losers across the $[-1, +1]$ window.
   - *Decision Rule:* If the quality-conditioned announcement spread fails to achieve $t \ge 2.00$ out-of-sample (`research-defined falsification threshold`), the interaction between momentum/quality and announcement jump risk is falsified.
4. **Execution Timing and Intraday Gap Stress Test:**
   - *Data & Method:* Replace daily close-to-close execution with actual tick-level simulation entering at 15:55 ET prior to AMC prints and exiting at 09:35 ET following market open.
   - *Metric:* Net P&L under realistic opening auction spread widening and bid-ask slippage.
   - *Decision Rule:* If opening auction slippage reduces the gross premium by more than $60\%$ (`research-defined falsification threshold`), execution friction is proven to be the binding constraint.
5. **Placebo Shuffled-Date Permutation Test:**
   - *Data & Method:* Conduct 2,000 Monte Carlo permutations randomly shifting scheduled announcement dates by $\pm 10$ to $\pm 30$ trading days for each ticker.
   - *Decision Rule:* If the empirical $t$-statistic ($+1.85$) falls within the 5th–95th percentile band of the shuffled-date distribution (`research-defined falsification threshold`), the observed performance is conclusively proven to be statistical noise.

## Crypto portability

**Portability Classification:** `adapted` / `unproven`

### Conceptual Portability to Cryptocurrency Markets

1. **Absence of Corporate Statutory Earnings:**
   Cryptocurrency protocols, decentralized networks, and digital tokens do not file SEC quarterly Form 10-Q disclosures or hold quarterly executive earnings conference calls. Therefore, the corporate earnings announcement premium does not translate directly to crypto spot or perpetual markets.
2. **Scheduled Protocol and Macro Catalysts as Crypto Analogs:**
   The fundamental mechanism of the earnings premium—bearing discrete, scheduled, non-diversifiable jump risk—has direct analogs in cryptocurrency scheduled events (`research-proposed`):
   - **Hard Forks and Protocol Upgrades:** Major pre-scheduled network hard forks (e.g., Ethereum London/EIP-1559, The Merge, Shanghai/Shapella, Cancun-Dencun) are scheduled weeks in advance and carry binary technological/operational execution risk.
   - **Token Vesting Unlocks:** Scheduled cliff token unlocks (e.g., large venture capital or foundation vesting distributions) published on tokenomist platforms.
   - **Bitcoin Halving Cycles:** Pre-programmed block height halving events occurring approximately every four years.
   - **Macroeconomic Data Prints:** US CPI, PPI, and FOMC rate decisions, which drive high-beta crypto price discovery.

### Frictions and Operational Risks in Crypto Deployment

- **24/7 Continuous Trading Dynamics:** US equities exhibit discrete overnight session gaps between market close (16:00 ET) and market open (09:30 ET), allowing announcements to land in an illiquid auction window. In contrast, cryptocurrency markets trade continuously 24/7/365. Information is absorbed dynamically across real-time order books, altering jump pricing and eliminating discrete gap auctions (`research-proposed`).
- **Perpetual Funding Rate Drag:** Holding a directional crypto perpetual position across a high-volatility scheduled catalyst subjects the trader to extreme funding rate spikes. During bullish catalyst anticipation, perpetual funding rates frequently surge to $>50-100\%$ APR, rapidly consuming any post-event abnormal return (`research-proposed`).
- **Venue Fragmentation and Reference Price Dispersion:** Unlike US equities where consolidated tape (SIP) and NBBO enforce price consistency, crypto liquidity is fragmented across multiple centralized (Binance, Bybit, OKX, Coinbase) and decentralized exchanges. Jump risk is accompanied by wide cross-venue basis dislocations.
- **Liquidation Cascades:** Crypto events frequently trigger cascading long/short liquidations that create sharp non-linear price wicks exceeding $\pm 10-20\%$, triggering stop losses before any price recovery can occur (`research-proposed`).

## Limitations

- **Liquid Mega/Large-Cap Universe Restriction:** The empirical study was executed exclusively on 49 liquid mega-cap and large-cap US equities. The author explicitly notes that this is the exact market segment where market efficiency is highest and where an announcement premium should be most arbed away. The finding does not disprove the existence of an earnings announcement premium in neglected micro-cap equities, but confirms its absence in liquid names.
- **Heuristic BMO/AMC Time-of-Day Inference:** Time-of-day classification was inferred from the hour of the `yfinance` timestamp ($< 13:00$ ET $\to$ BMO; $\ge 13:00$ ET $\to$ AMC; missing $\to$ AMC). While the $[-1, +1]$ event window absorbs minor 1-session shifts, occasional timestamp classification errors may introduce minor timing noise.
- **Simplified Beta-1 Market Adjustment:** Abnormal returns were computed under a fixed market-adjusted convention ($\beta = 1.0$) against SPY rather than estimating full Fama-French multi-factor loadings or rolling CAPM betas. However, differencing against the same-stock non-earnings baseline absorbed residual single-name beta drift.
- **Unconditional Formulation:** The study evaluated an unconditional holding strategy. It did not test conditional alpha variants that filter by implied volatility skew, options open interest concentrations, pre-announcement sentiment, or short interest.

## Implementation status

`not-implemented`

No implementation of this strategy exists in our research stack, `nautilus-quant-system`, PyBroker, or NautilusTrader. The strategy has been empirically evaluated and killed as uninvestable on liquid equities by the primary source due to statistical insignificance ($t = +1.85 < 2.0$), complete out-of-sample decay, and confounding with jump-risk variance.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an empirical research capture documenting the failure of the unconditional earnings announcement premium in modern liquid equity markets. Its presence in this repository does not constitute authorization for strategy implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]]` — Investigates option surface pricing and short straddle performance across single-name earnings events in the same equity lake, documenting Class 2 (friction scale) and Class 7 (compensated jump risk) failures.
- `[[sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]]` — Pre-registered empirical falsification of corporate announcement drift (S&P 500 index additions/deletions) documenting flow decay and name drift confounding.
- `[[buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13]]` — Pre-registered falsification of SEC Form 8-K share repurchase authorization drift, uncovering small-cap illiquidity mirages.
- `[[put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13]]` — Documents options-implied factor falsification and dividend confounding in equity derivatives.
- `[[sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13]]` — Pre-registered falsification of corporate spin-off post-distribution drift.

## Sources

1. Jonathan Beck (`JonathanBeck1`), *\"A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced\"*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: `https://github.com/JonathanBeck1/falsification-campaign`
2. Jonathan Beck, *\"Decision: Earnings-Announcement Premium (T43)\"*, `research/earnings_premium_decision.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_premium_decision.md`
3. Jonathan Beck, *\"Pre-registration: Earnings-Announcement Premium (T43)\"*, `research/earnings_premium_preregistration.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_premium_preregistration.md`
4. Jonathan Beck, *\"T43 — Earnings-Announcement Premium Study Result\"*, `research/earnings_premium_report.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/earnings_premium_report.md`
5. Jonathan Beck, Python Implementation Core: `src/trader/catalysts/earnings_premium.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/src/trader/catalysts/earnings_premium.py`
6. Jonathan Beck, End-to-End Study Runner: `scripts/run_earnings_premium_study.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/scripts/run_earnings_premium_study.py`
7. Jonathan Beck, Financial Unit Test Suite: `tests/financial/test_earnings_premium.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/tests/financial/test_earnings_premium.py`
8. Jonathan Beck, *\"The negative result: an empirical falsification of retail-accessible trading edges\"*, `research/PAPER_DRAFT.md`, Section 4.6, 4.7, Table 6 in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md`
9. Beaver, W. H. (1968). The Information Content of Annual Earnings Announcements. *Journal of Accounting Research*, 6, 67–92.
10. Chari, V. V., Jagannathan, R., & Ofer, A. R. (1988). Risk, Return, and the Timing of Corporate Disclosures: An Investigation of the Earnings Announcement Effect. *Journal of Financial Economics*, 21(2), 177–201.
11. Frazzini, A., & Lamont, O. A. (2007). The Earnings Announcement Premium and Trading by Individual Investors. *The Journal of Finance*, 62(5), 2385–2419.
12. Barber, B. M., De George, E. T., Lehavy, R., & Trueman, B. (2013). The Earnings Announcement Premium Around the Globe. *The Journal of Financial Economics*, 108(1), 118–138.
