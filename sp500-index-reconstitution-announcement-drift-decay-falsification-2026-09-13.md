---
schema: strategy-research-record-v1
title: "S&P 500 Index Reconstitution: Empirical Falsification of Announcement-to-Effective Forced-Flow Abnormal Returns Against Momentum Winner Name Drift and Historical Decay"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-index
  - index-reconstitution
  - index-effect
  - event-driven
  - structural-flow
  - falsification
  - negative-results
  - institutional-flow
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "Primary audit decision record: JonathanBeck1, 'Decision: S&P 500 Index Reconstitution / \"Index Effect\" (T39)', research/index_reconstitution_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/index_reconstitution_decision.md"
  - "Primary pre-registration: JonathanBeck1, 'Pre-registration — T39 S&P 500 Index Reconstitution / \"Index Effect\"', research/index_reconstitution_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/index_reconstitution_preregistration.md"
  - "Primary empirical code: JonathanBeck1, 'src/trader/catalysts/index_reconstitution.py', 'scripts/run_index_reconstitution_study.py', and 'tests/financial/test_index_reconstitution.py' (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63)"
  - "Primary research synthesis: JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 5, 7.2, 7.3, 7.5 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
  - "Historical academic foundation: Andrei Shleifer, 'Do Demand Curves for Stocks Slope Down?', The Journal of Finance, Vol. 41, No. 3 (1986), pp. 579–590. DOI: 10.1111/j.1540-6261.1986.tb04518.x"
  - "Historical academic foundation: Messod E. Beneish and Robert E. Whaley, 'An Anatomy of the \"S&P Game\": The Effects of Changing the Rules', The Journal of Finance, Vol. 51, No. 5 (1996), pp. 1909–1930. DOI: 10.1111/j.1540-6261.1996.tb05231.x"
  - "Decay literature: Robin Greenwood and Marco Sammon, 'The Disappearing Index Effect', Harvard Business School Working Paper 23-025 (2023). SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4204278"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# S&P 500 Index Reconstitution: Empirical Falsification of Announcement-to-Effective Forced-Flow Abnormal Returns Against Momentum Winner Name Drift and Historical Decay

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`).
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`).
- **Commit Date:** 2026-09-08T21:47:53Z (`source-reported`).
- **Source As-Of Date:** 2026-09-08 (`source-reported`).
- **Primary Source Documents & Code Directly Audited:**
  - `research/index_reconstitution_preregistration.md`: Pre-registered research design establishing the hypothesis, universe, snapshot-diff event methodology, announcement proxy ($K=5$ trading days), SPY market adjustment, $10\text{ bps}$ friction model, in-sample/out-of-sample split, same-name placebo control, and kill criteria (`source-reported`).
  - `research/index_reconstitution_decision.md`: Official decision record detailing the `KILL` verdict, full after-cost CAR statistics ($N=277$ usable additions, $N=67$ deletions), IS vs. OOS decay, same-name placebo results ($N=1,385$ windows), $K$-band sensitivity ($K=3, 5, 7$), and artifact classification (`source-reported`).
  - `src/trader/catalysts/index_reconstitution.py`: Pure Python core implementing market-adjusted return calculation (`_abnormal_return`), event window CAR extraction (`compute_event_metrics`), same-name random placebo sampling (`placebo_cars`), metric aggregation (`aggregate`), round-trip cost deduction (`after_cost_mean`), temporal partitioning (`split_is_oos`), and multi-condition gate evaluation (`evaluate_gate`) (`source-reported`).
  - `tests/financial/test_index_reconstitution.py`: 17 network-free unit tests verifying announce-to-effective window math, synthetic jump recovery, daily glitch filtering, placebo sampling, and gate failure logic (`source-reported`).
  - `scripts/run_index_reconstitution_study.py`: End-to-end runner orchestrating event extraction from historical component snapshots and pricing via yfinance (`source-reported`).
  - `research/PAPER_DRAFT.md`: Comprehensive 40-family empirical synthesis (§5, §7.2, §7.3, §7.5) classifying the S&P reconstitution result within the double-failure taxonomy: decay/in-noise and Class 5 pooled-baseline/composition contamination (`source-reported`).
- **Historical Academic Precedents:**
  - Andrei Shleifer (1986), *"Do Demand Curves for Stocks Slope Down?"*, *Journal of Finance*, documenting the original +2.8% to +7% post-announcement price jump in S&P 500 additions (`source-reported`).
  - Messod E. Beneish & Robert E. Whaley (1996), *"An Anatomy of the 'S&P Game': The Effects of Changing the Rules"*, *Journal of Finance*, documenting pre-effective institutional front-running following S&P's October 1989 rule change to announce additions prior to effective dates (`source-reported`).
  - Robin Greenwood & Marco Sammon (2023), *"The Disappearing Index Effect"*, Harvard Business School Working Paper 23-025, documenting the modern structural decay of the index addition premium toward zero as passive indexing grew and proprietary arbitrage capital crowded the pre-effective window (`source-reported`).
- **Underlying Sample & Universe:** S&P 500 constituent additions and deletions derived from historical component snapshots in `fja05680/sp500` (*"S&P 500 Historical Components & Changes (Updated).csv"*) cross-referenced against Yahoo Finance (`yfinance`) daily adjusted close prices (`source-reported`).
- **Sample Span:** 2010-01-01 to 2025-12-31 (`source-reported`).
  - In-Sample (IS): 2010–2017 ($N=121$ usable additions) (`source-reported`).
  - Out-of-Sample (OOS): 2018–2025 ($N=156$ usable additions) (`source-reported`).
  - Total usable additions evaluated: $N=277$ (`source-reported`).
  - Deletions: $N=67$ (purged of ~80% due to survivorship bias from corporate acquisitions/delistings, excluded from verdict) (`source-reported`).
- **Repository Deduplication Audit:** A comprehensive grep across the entire `alpha-strategy-research` repository confirmed zero existing records evaluating S&P 500 index additions/deletions, index reconstitution front-running, or the "index effect". Existing repository records covering index or equity strategies (`sp500-avellaneda-lee-residual-reversion-implementability-falsification-2026-09-13.md`, `sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md`, `us-equity-vortex-top2-cross-sectional-trend-phase-robustness-2026-09-13.md`) investigate statistical arbitrage, pairs trading, or technical trend-following, with no overlap with corporate index reconstitution structural flow.

## Economic mechanism

### Source-reported

1. **The Classic Index Effect Thesis:**
   - When S&P Dow Jones Indices announces that a stock will be added to the S&P 500 index, passive index-tracking mutual funds and ETFs (holding trillions of dollars in aggregate AUM benchmarked directly to the index) are structurally mandated to acquire the stock on or before the market close of the effective date to eliminate tracking error.
   - Because this capital allocation is mandatory, non-discretionary, and price-insensitive, the resulting temporary demand shock should drive the added stock's price significantly higher between the public announcement date and the effective inclusion date ($[t_{\text{announce}}, t_{\text{effective}}]$).
   - Conversely, deleted stocks should suffer forced liquidation by index trackers, creating a downward abnormal return drift over the same window.
   - Historically (1980s through late 1990s), this "index effect" generated documented abnormal cumulative returns of $+3\%$ to $+7\%$ on additions (Shleifer 1986; Beneish & Whaley 1996).

2. **The Falsification Findings (JonathanBeck1 T39):**
   - **The Forced-Flow Edge Has Decayed to Statistical Insignificance:** Over the 2010–2025 period ($N=277$ additions), the mean market-adjusted Cumulative Abnormal Return (CAR) over the primary $[-5, 0]$ trading-day window is only $+0.48\%$ gross and $+0.38\%$ after-cost (assuming a liquid large-cap $10\text{ bps}$ round-trip cost).
   - The $t$-statistic is $+1.11$, failing the pre-registered threshold ($|t| \ge 2.0$).
   - The median after-cost CAR is $-0.09\%$ (strictly below zero), with only $49\%$ of additions generating a positive abnormal return.
   - Temporal partitioning reveals zero edge in either era: in-sample (2010–2017) after-cost CAR is $+0.21\%$ ($t = +0.46$, $N=121$); out-of-sample (2018–2025) after-cost CAR is $+0.68\%$ ($t = +1.01$, $N=156$). Neither era achieves statistical significance.
   - **Placebo Control Exposes Composition Contamination (Class 5 Artifact):** To test whether the $+0.48\%$ gross CAR reflects index-fund forced flow versus general stock characteristics, the study samples 5 random non-event 6-trading-day windows for each added stock across its historical price series ($N=1,385$ placebo windows).
   - The placebo control generates a mean abnormal return of $+0.41\%$ with a $t$-statistic of $+2.85$.
   - Because stocks selected for S&P 500 inclusion are almost exclusively high-performing mega-cap momentum winners that recently expanded their market capitalization and earnings, they exhibit an unconditional positive market-adjusted drift in any arbitrary 6-day window.
   - Subtracting the baseline name drift ($+0.41\%$) from the event window CAR ($+0.48\%$) leaves an incremental flow effect of approximately $+0.07\%$—pure statistical noise. The entire apparent "index effect" in modern data is an artifact of stock selection composition, not tradable forced flow.
   - **Deletion Infeasibility & Survivorship Distortion:** S&P 500 deletions ($N=67$) exhibit an abnormal CAR of $+1.42\%$ ($t = +1.26$), the opposite of the predicted negative sign. This is caused by severe survivorship bias: approximately $80\%$ of true historical deletions are corporate acquisition targets or restructuring casualties that delisted upon removal and are completely purged from free databases like Yahoo Finance. Surviving deletions are biased upward.

### Research interpretation

- The empirical results from JonathanBeck1 confirm two major structural conclusions in equity quantitative research:
  1. **Alpha Decay via Institutional Anticipation:** The structural demand elasticity of large-cap equities has expanded dramatically over four decades. As Greenwood & Sammon (2023) demonstrated, multi-manager hedge funds, quantitative market makers, and liquidity providers front-run expected S&P 500 additions months in advance based on committee rule prediction models (e.g., market cap, liquidity, profitability criteria). By the time the official announcement is released, the price impact is fully discounted or reversed. Furthermore, modern index asset managers have adopted algorithmic execution schedules (TWAP/VWAP across pre-effective days) and negotiated crossing blocks rather than market-on-close dumping.
  2. **Class 5 Artifact (Pooled-Baseline / Selection Composition Trap):** Naive event studies frequently commit the error of attributing post-announcement drift to the event itself without evaluating an identically matched placebo on the same underlying names. When the event cohort is systematically composed of momentum winners (as S&P 500 additions must be by definition), the baseline drift of the cohort is positive ($t = 2.85$). An event CAR that fails to exceed the name's non-event baseline drift contains zero incremental information.

## Signal

- **Universe:** US equities added to the S&P 500 index between 2010 and 2025 (`source-reported`).
- **Event Identification:** Snapshot differences from `fja05680/sp500` identifying additions with effective inclusion dates ($t_{\text{effective}}$) (`source-reported`).
- **Announcement Date Proxy:** In the absence of a clean, programmatic free announcement-date time series, the announcement date is defined ex-ante as:
  $$t_{\text{announce}} = t_{\text{effective}} - K \quad \text{trading days}$$
  where $K = 5$ trading days (calibrated ex-ante to the median 6 calendar days / ~5 trading days observed on Wikipedia disclosure subsets) (`source-reported`).
- **Measurement Windows:**
  - Primary forced-flow window: $[-5, 0]$ trading days relative to $t_{\text{effective}}$ (`car_announce_eff`) (`source-reported`).
  - Pre-effective run-up window: $[-5, -1]$ trading days (`car_announce_m1`) (`source-reported`).
  - Post-effective reversal window: $[0, +5]$ trading days (`car_eff_p5`) (`source-reported`).
- **Abnormal Return Calculation:**
  $$\text{AR}_{i,t} = R_{i,t} - R_{\text{SPY},t}$$
  where $R_{i,t}$ is the percentage return of stock $i$ on trading day $t$, and $R_{\text{SPY},t}$ is the percentage return of SPY (beta=1 market adjustment) (`source-reported`).
- **Cumulative Abnormal Return (CAR):**
  $$\text{CAR}_i[t_1, t_2] = \sum_{t=t_1}^{t_2} \text{AR}_{i,t}$$
  evaluated over trading days $[t0 + lo, t0 + hi]$ where $t0$ is the effective date (`source-reported`).
- **Outlier Filtering:** Any event containing a single-day market-adjusted return $|\text{AR}_{i,t}| > 0.75$ ($75\%$) inside the evaluation window is discarded as a split glitch or unadjusted corporate action error (`MAX_ABS_DAILY_AR = 0.75`) (`source-reported`).
- **Trade Execution (Hypothetical Long Addition):**
  - Entry: Buy stock $i$ at the market close on $t_{\text{announce}}$ ($t_{\text{effective}} - 5\text{ trading days}$) (`source-reported`).
  - Exit: Sell stock $i$ at the market close on $t_{\text{effective}}$ ($t=0$) (`source-reported`).
  - Net Return: Gross $\text{CAR}_i[-5, 0] - \text{ROUND\_TRIP\_COST}$, where $\text{ROUND\_TRIP\_COST} = 0.0010$ ($10\text{ bps}$) (`source-reported`).
- **Position Sizing:** Evaluated as unweighted, per-event trade expectancy in the empirical source (`source-reported`). Portfolio capital allocation across concurrent announcements (e.g., equal dollar notional, risk parity, or liquidity-capped sizing) is `research-proposed`.
- **Alternative Execution Timestamps:** Market close execution is `source-reported`; entering on the open of $t_{\text{announce}} + 1$ or utilizing arrival-price VWAP algorithms is `research-proposed`.

## Required data

- **Instrument:** US equities listed on major US exchanges (NYSE, Nasdaq) and SPY ETF (`source-reported`).
- **Universe:** S&P 500 index constituent changes (additions and deletions) from 1996 through 2025 (`source-reported`).
- **Primary Data Source:**
  - Constituent snapshots: `fja05680/sp500` repository (*"S&P 500 Historical Components & Changes (Updated).csv"*) (`source-reported`).
  - Daily price data: Yahoo Finance (`yfinance`) split- and dividend-adjusted daily close prices (`source-reported`).
  - Market benchmark: SPY daily close prices (`source-reported`).
- **Timeframe:** Daily closing prices (`source-reported`).
- **Fields:** `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume` (`source-reported`).
- **Point-in-Time Availability & Causal Ordering:**
  - Constituent additions are announced publicly by S&P Dow Jones Indices after market close several days before inclusion.
  - The proxy announcement date $t_{\text{effective}} - 5$ is ex-ante and strictly precedes the effective date (`source-reported`).
  - The evaluation window $[-5, 0]$ uses only prices realized within the event interval (`source-reported`).
- **Missing Data Handling:**
  - Stocks lacking sufficient historical trade days around the event window ($t_0 - 5$ to $t_0 + 5$) are dropped (`source-reported`).
  - Stocks with daily return magnitudes $> 75\%$ are dropped (`source-reported`).
  - Deletions that delisted and lack pricing records in yfinance are documented as survivorship purges and omitted from the verdict (`source-reported`).

## Execution assumptions

- **Trade Timing:** Enter at close of $t_{\text{effective}} - 5\text{ td}$; exit at close of $t_{\text{effective}}$ ($t_0$) (`source-reported`).
- **Holding Period:** Exactly 5 trading days (~1 calendar week) (`source-reported`).
- **Order Type:** Market-on-Close (MOC) orders (`source-reported`).
- **Fill Assumptions:** Executed at daily adjusted close price (`source-reported`).
- **Transaction Costs & Slippage:** Flat $10\text{ bps}$ ($0.0010$) round trip ($5\text{ bps}$ entry + $5\text{ bps}$ exit), reflecting typical institutional execution friction in liquid large-cap US equities (`source-reported`).
- **Borrow / Shorting:** Not required for long additions; required for short deletions (omitted from live implementation due to survivorship bias) (`source-reported`).
- **Execution Latency:** Zero latency assumed relative to closing print (`source-reported`). Intraday latency or market impact of multi-billion dollar index rebalance auctions is `research-proposed`.

## Evidence

### Source-reported

- **Addition Cohort Empirical Metrics (2010–2025):**
  - Usable addition events: $N = 277$ (`source-reported`).
  - Gross Mean CAR $[-5, 0]$: $+0.48\%$ (`source-reported`).
  - After-Cost Mean CAR ($10\text{ bps}$ cost): $+0.38\%$ (`source-reported`).
  - $t$-statistic: $+1.11$ (statistically insignificant; fails pre-registered $|t| \ge 2.0$ gate) (`source-reported`).
  - Median CAR: $-0.09\%$ (negative) (`source-reported`).
  - Positive events: $49\%$ (`source-reported`).
- **Subperiod Stability & Temporal Decay:**
  - In-Sample (2010–2017): Mean CAR $+0.21\%$, $t = +0.46$, $N = 121$ (`source-reported`).
  - Out-of-Sample (2018–2025): Mean CAR $+0.68\%$, $t = +1.01$, $N = 156$ (`source-reported`).
  - Both subperiods are statistically indistinguishable from zero, demonstrating complete historical decay of the anomaly since 2010 (`source-reported`).
- **Placebo Control Comparison:**
  - Random non-event 6-day windows on the same addition stocks ($N = 1,385$): Mean CAR $+0.41\%$, $t = +2.85$ (`source-reported`).
  - The placebo is statistically significant ($t = 2.85$), proving that S&P additions exhibit a baseline positive drift independent of index inclusion (`source-reported`).
  - Net abnormal return over placebo: $+0.48\% - 0.41\% = +0.07\%$ ($t$-stat approximately zero) (`source-reported`).
- **$K$-Band Lead Sensitivity (Primary $K=5$):**
  - $K = 3$ trading days: After-cost mean $+0.31\%$, $t = +1.26$ (`source-reported`).
  - $K = 7$ trading days: After-cost mean $+0.72\%$, $t = +1.79$ (`source-reported`).
  - Neither alternative window reaches statistical significance ($|t| \ge 2.0$), confirming that the result is robust across window definitions (`source-reported`).
- **Deletions Cohort Metrics:**
  - $N = 67$ usable deletions (`source-reported`).
  - Mean CAR $[-5, 0]$: $+1.42\%$, $t = +1.26$ (`source-reported`).
  - Sign is positive (opposite of the hypothesized negative drift), driven by extreme survivor selection (~80% of true historical deletions delisted upon M&A and are missing from yfinance) (`source-reported`).
- **Pre-Registered Gate Evaluation:**
  - Event Count ($N \ge 30$): **PASS** ($N = 277$) (`source-reported`).
  - After-Cost Signal (Net $> 0$ and $|t| \ge 2.0$): **FAIL** (Net $+0.38\%$, $t = +1.11$) (`source-reported`).
  - OOS Sign Stability (IS and OOS same sign): **PASS** (Both positive, but both null) (`source-reported`).
  - Placebo Null ($|t| < 2.0$): **FAIL** (Placebo $t = +2.85$, absorbing the signal) (`source-reported`).
  - Official Verdict: **KILL** (`source-reported`).

### Independently reproduced

- `not independently reproduced`

### Negative evidence

- The primary source documents a definitive negative result: the S&P 500 announcement-to-effective index effect is economically and statistically dead in modern US equities (2010–2025).
- Greenwood & Sammon (2023) independently document the structural disappearance of the index addition premium over the past two decades.
- Quoted transaction costs, market impact, and name-level drift consume 100% of the gross $+0.48\%$ return.
- Surviving deletions produce wrong-sign returns due to database survivorship bias.

## Falsification plan

- **Falsification Status:** Pre-registered empirical falsification completed by JonathanBeck1 (T39) with verdict `KILL`.
- **Pre-Registered Falsification Criteria (JonathanBeck1 T39 Gate):**
  1. *Statistical Significance Criterion:* After-cost addition CAR over $[-5, 0]$ trading days must clear $|t| \ge 2.0$ with positive net return. **Result: FAILED ($t = +1.11$, Net $+0.38\%$).**
  2. *Placebo Discrimination Criterion:* Same-name random 6-day windows must be null ($|t| < 2.0$), and cohort net of placebo must clear $|t| \ge 2.0$. **Result: FAILED (Placebo $t = +2.85$; net of placebo CAR is only $+0.07\%$).**
  3. *Temporal Robustness Criterion:* In-sample (2010–2017) and out-of-sample (2018–2025) must show positive, statistically significant abnormal returns. **Result: FAILED (IS $t = +0.46$; OOS $t = +1.01$).**
- **Follow-On Research-Proposed Falsification Tests:**
  1. *Official S&P Press-Release Timestamps:* Re-evaluate the strategy using exact, sub-minute announcement timestamps from S&P Dow Jones press releases / Bloomberg INDX rather than the $K=5$ proxy. `research-defined falsification threshold`: If the true announcement-to-effective CAR exceeds the placebo drift by less than $10\text{ bps}$ ($t < 2.0$), the proxy-bias hypothesis is definitively rejected.
  2. *Russell 1000 / 2000 Annual Reconstitution:* Evaluate mechanical index reconstitution flow in the FTSE Russell annual reconstitution (June ranking to June reconstitution). `research-defined falsification threshold`: If post-ranking Russell additions/deletions fail to produce after-cost abnormal returns $> 25\text{ bps}$ ($t < 2.0$), structural index front-running is rejected across all US index benchmarks.
  3. *Small-Cap / Mid-Cap Index Reconstitution (S&P 600 / S&P 400):* Test whether lower-liquidity names exhibit persistent index inclusion effects. `research-defined falsification threshold`: If S&P MidCap 400 additions fail to achieve after-cost abnormal returns $> 50\text{ bps}$ ($t < 2.0$) net of matched momentum controls, market-cap tiering does not rescue the anomaly.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Mechanism Portability Assessment:**
  - Crypto markets feature decentralized index tokens and exchange-traded structured baskets (e.g., CoinDesk DeFi Index, Bitwise 10 Crypto Index Fund, 21Shares baskets, or exchange-curated perpetual baskets).
  - In theory, when a token is added to or deleted from a prominent crypto index, rebalancing flow by institutional index funds could create price pressure.
  - However, in crypto markets, centralized exchange listings (e.g., Binance, Coinbase listing announcements) function as the primary structural flow catalyst rather than index additions.
- **Crypto-Specific Market Structure Impediments:**
  - *Small Passive AUM:* Unlike US equity markets where trillions of dollars are strictly bound to S&P 500 benchmarks, passive crypto index funds represent a tiny fraction of total crypto market capitalization. Forced institutional rebalancing volume is generally negligible relative to daily spot and perpetual turnover.
  - *Front-Running on Transparent Ledgers:* Crypto index reconstitution rules are published algorithmically and on-chain holdings are visible in real time. Arbitrage bots anticipate basket rebalancings continuously, eliminating any announcement-window delay.
  - *Funding & Basis Volatility:* Holding crypto tokens over multi-day rebalance windows exposes capital to violent funding rate fluctuations and directional beta drawdowns that dwarf any minor basis effect.
  - *Listing Effects vs. Index Effects:* Empirical price spikes in crypto tokens upon major exchange listing announcements decay rapidly within hours, presenting severe adverse selection and liquidity slippage.
- Any adaptation of index reconstitution flow trading to crypto assets is entirely `research-proposed` and unproven.

## Limitations

- **Proxy Announcement Date ($K=5$):** The primary empirical audit used an ex-ante proxy of $t_{\text{effective}} - 5\text{ trading days}$ due to the lack of clean, free programmatic announcement timestamps in Wikipedia / yfinance. If the true announcement lead for individual events differed from 5 days, the evaluation window could be slightly mis-centered, causing potential signal attenuation (`source-reported`).
- **Survivorship Deletion Bias:** S&P 500 deletions could not be evaluated symmetrically because approximately $80\%$ of deleted constituents delisted upon acquisition or bankruptcy, creating a severe survivorship artifact in unadjusted historical price lakes (`source-reported`).
- **Single Benchmark Adjustment:** Abnormal returns were computed using a simple $\beta=1$ SPY adjustment; while added stocks skew large-cap, multi-factor risk model adjustments (Fama-French 5-factor + Carhart momentum) were not computed (`source-reported`).
- **Free Data Boundaries:** Full tick-level and order-book auction liquidity around the market close on effective dates was not evaluated (`source-reported`).

## Implementation status

- `not-implemented`: No execution pipeline, data feed, or backtest logic for index reconstitution trading exists in our research stack.
- This research record documents an external empirical falsification of the S&P 500 index effect and does not authorize or construct an automated strategy in PyBroker or NautilusTrader.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Presence in this repository establishes that the strategy has been rigorously audited and cataloged as an empirically falsified anomaly. It is not approved for implementation, paper trading, demo/testnet, or live trading.

## Related Wiki records

- `[[quant/sp500-avellaneda-lee-residual-reversion-implementability-falsification-2026-09-13]]`
- `[[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]]`
- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]`
- `[[quant/sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12]]`

## Sources

- JonathanBeck1, *A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: `https://github.com/JonathanBeck1/falsification-campaign`
- JonathanBeck1, *Decision: S&P 500 Index Reconstitution / "Index Effect" (T39)*, `research/index_reconstitution_decision.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/index_reconstitution_decision.md`
- JonathanBeck1, *Pre-registration — T39 S&P 500 Index Reconstitution / "Index Effect"*, `research/index_reconstitution_preregistration.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/index_reconstitution_preregistration.md`
- JonathanBeck1, *Python Implementation Core and Unit Tests*, `src/trader/catalysts/index_reconstitution.py` and `tests/financial/test_index_reconstitution.py`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`.
- JonathanBeck1, *The negative result: an empirical falsification of retail-accessible trading edges*, `research/PAPER_DRAFT.md`, Section 5, 7.2, 7.3, 7.5, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md`
- Andrei Shleifer, *Do Demand Curves for Stocks Slope Down?*, *The Journal of Finance*, Vol. 41, No. 3 (1986), pp. 579–590. DOI: `10.1111/j.1540-6261.1986.tb04518.x`
- Messod E. Beneish and Robert E. Whaley, *An Anatomy of the "S&P Game": The Effects of Changing the Rules*, *The Journal of Finance*, Vol. 51, No. 5 (1996), pp. 1909–1930. DOI: `10.1111/j.1540-6261.1996.tb05231.x`
- Robin Greenwood and Marco Sammon, *The Disappearing Index Effect*, Harvard Business School Working Paper 23-025 (2023). SSRN: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4204278`
