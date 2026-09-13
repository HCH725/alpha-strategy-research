---
schema: strategy-research-record-v1
title: "SEC Form 8-K Item 8.01 Share Repurchase Announcements: Empirical Falsification of Post-Announcement Abnormal Returns as Small-Cap Illiquidity Fiction and Modern Large-Cap Drift Decay"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-catalyst
  - corporate-actions
  - share-repurchases
  - buyback-drift
  - event-driven
  - market-friction
  - liquidity-mirage
  - falsification
  - negative-results
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "Primary audit decision record: JonathanBeck1, 'Decision: Buyback-Announcement Drift (T41)', research/buyback_drift_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/buyback_drift_decision.md"
  - "Primary pre-registration: JonathanBeck1, 'Pre-registration — T41 Buyback-Announcement Drift', research/buyback_drift_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/buyback_drift_preregistration.md"
  - "Primary empirical report: JonathanBeck1, 'T41 — Buyback-Announcement-Drift Study Result', research/buyback_drift_report.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/buyback_drift_report.md"
  - "Primary empirical code: JonathanBeck1, 'src/trader/catalysts/buyback_drift.py', 'scripts/run_buyback_drift_study.py', 'scripts/diag_buyback_drift_liquidity.py', and 'tests/financial/test_buyback_drift.py' (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63)"
  - "Primary research synthesis: JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 4.2, 4.7, and 7 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
  - "Historical academic foundation: David L. Ikenberry, Josef Lakonishok, and Theo Vermaelen, 'Market Underreaction to Open Market Share Repurchases', Journal of Financial Economics, Vol. 39, No. 2-3 (1995), pp. 181–208. DOI: 10.1016/0304-405X(95)00826-Z"
  - "Historical academic foundation: Theo Vermaelen, 'Common Stock Repurchases and Market Signalling: An Empirical Study', Journal of Financial Economics, Vol. 9, No. 2 (1981), pp. 139–183. DOI: 10.1016/0304-405X(81)90011-8"
  - "Historical academic foundation: Urs Peyer and Theo Vermaelen, 'The Nature and Persistence of Buyback Anomalies', The Review of Financial Studies, Vol. 22, No. 4 (2009), pp. 1693–1745. DOI: 10.1093/rfs/hhn056"
  - "Anomaly decay literature: R. David McLean and Jeffrey Pontiff, 'Does Academic Research Destroy Stock Return Predictability?', The Journal of Finance, Vol. 71, No. 1 (2016), pp. 5–32. DOI: 10.1111/jofi.12365"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SEC Form 8-K Item 8.01 Share Repurchase Announcements: Empirical Falsification of Post-Announcement Abnormal Returns as Small-Cap Illiquidity Fiction and Modern Large-Cap Drift Decay

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`).
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`).
- **Commit Date:** 2026-09-08T21:47:53Z (`source-reported`).
- **Source As-Of Date:** 2026-09-08 (`source-reported`).
- **Primary Source Documents & Code Directly Audited:**
  - `research/buyback_drift_preregistration.md`: Pre-registered research design establishing the hypothesis, universe definition via SEC EDGAR full-text search, Item 8.01 exclusion criteria, SPY market adjustment benchmark, flat 15 bps round-trip friction model, temporal in-sample/out-of-sample split, matched (ticker, year) placebo control, and kill criteria (`source-reported`).
  - `research/buyback_drift_decision.md`: Official decision record detailing the `KILL` verdict, the initial full-gate pass (+1.08% after flat cost, $t=+3.39$, $N=1,303$), and the subsequent mandatory too-good tripwire liquidity inspection (`source-reported`).
  - `research/buyback_drift_report.md`: Full empirical report documenting sample accounting, event-study window returns, matched non-event placebo metrics ($-0.283\%$, $t=-1.62$), net-of-matched drift ($+1.516\%$, $t=+4.17$), top-5 contributors, and secondary evaluation windows ($[+1, +5]$ and $[+1, +63]$) (`source-reported`).
  - `scripts/diag_buyback_drift_liquidity.py`: Liquidity diagnostic interrogation establishing trailing 20-day dollar volume percentiles ($41.4\% < \$2\text{M/day}$, $63.7\% < \$10\text{M/day}$), liquidity-tiered round-trip execution cost model (10 bps to 300 bps) yielding $-0.97\%$ after cost ($t = -3.04$), and liquid sub-cohort ($\ge \$10\text{M/day}$, $N=208$) showing complete out-of-sample sign flip (IS $+3.29\% \to$ OOS $-0.64\%$) (`source-reported`).
  - `src/trader/catalysts/buyback_drift.py`: Pure Python implementation containing market-adjusted abnormal return calculation (`abnormal_returns`), event window CAR extraction (`compute_event`), filing deduplication (`dedup_filings`), matched-control placebo sampling (`sample_matched_cars`), metric aggregation (`aggregate`), and gate evaluation (`evaluate_gate`) (`source-reported`).
  - `tests/financial/test_buyback_drift.py`: 24 network-free unit tests verifying announce-to-post window math, ex-ante $t_0$ alignment ($t_0 = \text{file}+1$), synthetic drift injection recovery, quarter deduplication, and gate kill logic (`source-reported`).
  - `research/PAPER_DRAFT.md`: Comprehensive empirical synthesis (§4.2, §4.7, §7) classifying the buyback result within the campaign's 50-strategy falsification taxonomy as Class 2 (Friction-Scale Noise / Illiquidity Mirage) and structural decay (`source-reported`).
- **Historical Academic Precedents:**
  - David L. Ikenberry, Josef Lakonishok, and Theo Vermaelen (1995), *"Market Underreaction to Open Market Share Repurchases"*, *Journal of Financial Economics*, documenting an average abnormal return of $+12.1\%$ over a 4-year holding period following open-market share repurchase announcements (`source-reported`).
  - Theo Vermaelen (1981), *"Common Stock Repurchases and Market Signalling: An Empirical Study"*, *Journal of Financial Economics*, establishing the information signaling hypothesis of corporate tender offers and repurchase programs (`source-reported`).
  - Urs Peyer and Theo Vermaelen (2009), *"The Nature and Persistence of Buyback Anomalies"*, *The Review of Financial Studies*, arguing that undervaluation-driven buybacks persist in outperforming the market over 12-to-48-month horizons (`source-reported`).
  - R. David McLean and Jeffrey Pontiff (2016), *"Does Academic Research Destroy Stock Return Predictability?"*, *The Journal of Finance*, showing that academic publication of cross-sectional return anomalies is followed by an average ~58% post-publication decay in portfolio return predictability (`source-reported`).
- **Underlying Sample & Universe:** All distinct US filers appearing in SEC EDGAR full-text search (`efts.sec.gov/LATEST/search-index`) for 6 explicit repurchase-authorization phrases in Form 8-K, carrying Item 8.01 (Other Events), excluding Item 2.02 (Results of Operations and Financial Condition), matched against Yahoo Finance daily adjusted close prices and SPY benchmark (`source-reported`).
- **Sample Span:** 2015-01-01 to 2025-12-31 (`source-reported`).
  - In-Sample (IS): 2015–2019 ($N=451$ complete events) (`source-reported`).
  - Out-of-Sample (OOS): 2020–2025 ($N=852$ complete events) (`source-reported`).
  - Total complete events evaluated: $N=1,303$ (`source-reported`).
  - Matched (ticker, year) non-event placebo windows: $N=4,779$ (`source-reported`).
  - Tradeable liquid sub-cohort ($\text{ADV} \ge \$10\text{M/day}$): $N=208$ (`source-reported`).
- **Repository Deduplication Audit:** A full grep across the entire `alpha-strategy-research` repository confirmed zero prior records examining corporate share repurchase announcements, SEC Form 8-K Item 8.01 buyback drift, or campaign test T41. Existing corporate-action and event records in the repository (`sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05.md`, `news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02.md`, `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md`) investigate insider transactions, NLP rumor resolution, or S&P 500 reconstitution flow, with zero overlap in mechanism, regulatory filing type, or empirical dataset.

## Economic mechanism

### Source-reported

1. **The Classic Buyback Signaling Hypothesis:**
   - When corporate management possesses private information indicating that the firm's equity is fundamentally undervalued by the public market, it initiates an open-market share repurchase program to reallocate excess corporate cash flow and signal undervaluation to market participants (Vermaelen 1981; Ikenberry, Lakonishok, and Vermaelen 1995).
   - Unlike dividend commitments which establish rigid future cash outlay expectations, share repurchase authorizations grant corporate treasuries asymmetric optionality: management can execute purchases gradually over subsequent quarters during price dips, establishing a price-insensitive source of buy-side demand.
   - The behavioral anomaly thesis asserts that because corporate announcements are non-binding and executed over extended horizons, public equity markets systematically underreact to the initial SEC Form 8-K disclosure, resulting in prolonged post-announcement abnormal return drift over subsequent months.

2. **The Falsification Findings (JonathanBeck1 T41):**
   - **The Superficial Gate Pass:** Under the pre-registered flat cost model of $15\text{ bps}$ round-trip, the broad cohort ($N=1,303$ usable events) cleared every initial pre-registered gate criterion:
     - Gross mean CAR over the primary $[+1, +21]$ trading-day window is $+1.233\%$; after flat $15\text{ bps}$ cost, the mean is $+1.083\%$ with a statistically significant $t$-statistic of $+3.39$.
     - Temporal partitioning showed apparent stability: IS (2015–2019, $N=451$) after-cost mean $+1.248\%$ ($t = +2.87$); OOS (2020–2025, $N=852$) after-cost mean $+0.995\%$ ($t = +2.31$).
     - The matched (ticker, year) non-event control averaged $-0.283\%$ ($t = -1.62$), yielding an apparent net abnormal drift of $+1.516\%$ ($t = +4.17$).
   - **The Too-Good Tripwire & Liquidity Interrogation:** Because a clean full-gate pass was anomalous in a 19-for-19 kill campaign, the pre-registered "too-good" tripwire triggered an in-depth liquidity and contributor audit (`diag_buyback_drift_liquidity.py`), which falsified the edge through three independent structural findings:
     1. **Severe Small-Cap and Micro-Cap Concentration:** Examination of trailing 20-day median dollar volume ($\text{ADV}$) at the time of the event revealed that the cohort is overwhelmingly composed of illiquid small and micro-cap names:
        - 25th percentile ADV: $\$0.45\text{M/day}$; median ADV: $\$4.55\text{M/day}$.
        - $41.4\%$ of all events trade less than $\$2\text{M/day}$; $63.7\%$ trade less than $\$10\text{M/day}$ (median share price $\approx \$28$).
     2. **Realistic Tiered Friction Erases Edge and Inverts Sign:** The pre-registered assumption of flat $15\text{ bps}$ friction is completely unrealistic for microcap equities. When conservative, empirical liquidity-tiered round-trip transaction costs are applied ($10\text{ bps}$ for $\text{ADV} \ge \$50\text{M/day}$; $25\text{ bps}$ for $\$10\text{M} \le \text{ADV} < \$50\text{M}$; $60\text{ bps}$ for $\$2\text{M} \le \text{ADV} < \$10\text{M}$; $150\text{ bps}$ for $\$0.5\text{M} \le \text{ADV} < \$2\text{M}$; and $300\text{ bps}$ floor for $\text{ADV} < \$0.5\text{M}$), the after-cost mean CAR collapses to **$-0.97\%$ ($t = -3.04$)**. The apparent positive drift is entirely consumed by the bid-ask spread and market impact required to establish and liquidate positions in illiquid names.
     3. **Liquid Sub-Cohort Shows Zero Edge and Out-of-Sample Sign Flip:** Restricting the sample strictly to liquid names that an institutional quantitative book could execute ($\text{ADV} \ge \$10\text{M/day}$, $N=208$):
        - Gross mean CAR drops to $+0.38\%$ (median $+0.05\%$).
        - After tiered friction ($25\text{ bps}$ or $10\text{ bps}$), after-cost drift is $+0.205\%$ with $t = +0.32$ (statistically indistinguishable from zero).
        - Temporal partitioning within liquid names reveals a stark sign flip: in-sample (2015–2019, $N=54$) showed $+3.29\%$, but out-of-sample (2020–2025, $N=154$) collapsed to **$-0.64\%$**. Whatever historical drift existed in liquid equities has decayed to negative drift in modern markets.
   - **Supporting Contaminants:**
     - *Wrong-Instrument Trust Contamination:* Two top-5 contributors—Grayscale Ethereum Classic Trust (ETCG, $+55.8\%$) and Grayscale Bitcoin Cash Trust (BCHG, $+44.1\%$) filed on 2022-03-07—were closed-end crypto trusts filing trust-unit repurchase authorizations, not operating company equity buybacks. Their abnormal returns reflected macro crypto market volatility, not corporate signaling.
     - *Negative Placebo Distortion:* Matched same-name non-event windows average $-0.283\%$: illiquid small-caps drift downward between corporate events, creating an artificial mathematical inflation when computing "cohort minus matched control."

### Research interpretation

- The JonathanBeck1 T41 study exposes a critical archetype in event-driven quantitative finance: **The Small-Cap Illiquidity Mirage (Class 2 Friction-Scale Noise)**.
- In financial event studies, filtering solely for statistical significance without conditioning on execution feasibility routinely creates false discoveries. Small-cap stocks frequently pop on corporate headlines due to retail attention, illiquidity, and order-book imbalances. However, because these names trade with wide bid-ask spreads, low quoted depth, and high price impact, the round-trip friction required to execute a systematic 21-day holding strategy far exceeds the gross abnormal return.
- Furthermore, in the liquid, tradeable universe ($\text{ADV} \ge \$10\text{M/day}$), modern electronic market microstructure and algorithmic event-trading desks (utilizing automated SEC EDGAR web-scraping and NLP parsing) price 8-K Item 8.01 disclosures into closing prints within milliseconds of publication. The delayed multi-week drift documented by Ikenberry et al. in 1980s data has completely decayed under institutional competition, consistent with McLean & Pontiff (2016).

## Signal

- **Universe Definition:** All US exchange-listed common equities identified via SEC EDGAR full-text search filing Form 8-K with Item 8.01 between 2015-01-01 and 2025-12-31 (`source-reported`).
- **Event Inclusion Filtering:**
  - Form: `8-K` (`source-reported`).
  - Required Item: `8.01` ("Other Events") (`source-reported`).
  - Excluded Item: `2.02` ("Results of Operations and Financial Condition") to eliminate earnings-release contamination (`source-reported`).
  - Search Query Phrases (logical OR):
    1. `"approved a share repurchase"`
    2. `"approved a stock repurchase"`
    3. `"authorized a share repurchase"`
    4. `"authorized a stock repurchase"`
    5. `"new share repurchase program"`
    6. `"new stock repurchase program"` (`source-reported`).
- **Deduplication Rule:** To prevent multi-filing cluster overweighting, at most 1 event is permitted per `(ticker, calendar quarter)`; subsequent filings within the same quarter are dropped (`source-reported`).
- **Signal Formation Timestamp ($t_0$):**
  - Event date $t_{\text{file}}$ is the official SEC EDGAR acceptance date (`source-reported`).
  - To prevent look-ahead bias and accommodate after-hours filings, $t_0$ is defined strictly as the **next trading session** immediately following the filing date:
    $$t_0 = \min \{ t \in \mathcal{T} \mid t > t_{\text{file}} \}$$
    where $\mathcal{T}$ represents the set of valid US market trading days (`source-reported`).
- **Measurement Windows:**
  - **PRIMARY Window:** $CAR_{[+1, +21]}$, measuring cumulative abnormal returns from trading day $t_0+1$ through $t_0+21$ (20 trading days / ~1 calendar month) (`source-reported`).
  - **Secondary Windows:**
    - Short-horizon: $CAR_{[+1, +5]}$ (5 trading days / 1 calendar week) (`source-reported`).
    - Medium-horizon: $CAR_{[+1, +63]}$ (63 trading days / ~1 quarter) (`source-reported`).
- **Benchmark & Market Adjustment:**
  - Beta-1 market-adjusted abnormal return model:
    $$AR_{i,t} = R_{i,t} - R_{\text{SPY},t}$$
    where $R_{i,t}$ is the percentage return of stock $i$ on trading day $t$ using dividend/split-adjusted close prices, and $R_{\text{SPY},t}$ is the corresponding return of SPY (`source-reported`).
  - Cumulative Abnormal Return:
    $$CAR_{i,[s, e]} = \sum_{t=t_0+s}^{t_0+e} AR_{i,t}$$ (`source-reported`).
- **Matched (Ticker, Year) Non-Event Placebo Control:**
  - For each qualifying event $(i, t_0)$, draw up to 5 non-overlapping random non-event windows of identical duration $[+1, +21]$ for the **same ticker** within the **same calendar year**, requiring that no repurchase filing occurred within $\pm 21$ trading days of the placebo anchor (`source-reported`).
- **Execution & Sizing Specifications:**
  - Position entry: Long position initiated at the market close of $t_0$ (or open of $t_0+1$) `[research-proposed]`.
  - Position sizing: Equal-weighted allocation across all active qualifying events `[research-proposed]`.
  - Holding period: Exactly 20 trading sessions, exiting at market close on $t_0+21$ `[research-proposed]`.
  - Tradeable liquidity filter: Trailing 20-day median dollar volume $\text{ADV} \ge \$10\text{M/day}$ (`source-reported` diagnostic filter; `research-proposed` operational rule).

## Required data

- **Regulatory Filing Feed:**
  - Source: SEC EDGAR Electronic Filing and Transfer System (`https://efts.sec.gov/LATEST/search-index`) (`source-reported`).
  - Document types: Form 8-K filings (`source-reported`).
  - Metadata: Issuer CIK, filing date, accepted timestamp, items reported, document text (`source-reported`).
- **Market Price & Volume History:**
  - Asset class: US equities (`source-reported`).
  - Venue: US exchanges (NYSE, NASDAQ, NYSE American) via Yahoo Finance (`yfinance`) (`source-reported`).
  - Frequency: Daily OHLCV data with dividend and stock split adjustments (`source-reported`).
  - Market Benchmark: SPDR S&P 500 ETF Trust (`SPY`) daily adjusted closes (`source-reported`).
- **Microstructure / Liquidity Fields:**
  - Trailing 20-trading-day median dollar trading volume:
    $$\text{ADV}_{\text{USD}, t} = \text{median}_{k=1}^{20} \left( P_{t-k} \times V_{t-k} \right)$$
    computed strictly ex-ante prior to $t_0$ (`source-reported`).
  - Prior-day closing price $P_{t_0-1}$ (`source-reported`).
- **Missing Data & Glitch Protections:**
  - Missing price series: Tickers without yfinance historical records are excluded ($N=95$ tickers in study) (`source-reported`).
  - Incomplete event windows: Events with missing trading bars within $[t_0-20, t_0+63]$ are dropped ($N=11$ dropped) (`source-reported`).
  - Daily price jump filter: Daily price spikes $>10\times$ flagged as unadjusted split/dividend data corruptions (`source-reported`).

## Execution assumptions

- **Signal-to-Order Timing:** Event identified from EDGAR filing at $t_{\text{file}}$; order submitted for execution at $t_0$ close or $t_0+1$ open (`source-reported` timing convention; `research-proposed` order entry).
- **Order Type:** Market-on-Close (MOC) or limit order with immediate auction execution `[research-proposed]`.
- **Friction Models:**
  - *Pre-registered baseline:* Flat $15\text{ bps}$ round-trip cost ($0.15\%$) applied uniformly across all names (`source-reported`).
  - *Empirical Liquidity-Tiered Model (`diag_buyback_drift_liquidity.py`):*
    - Tier 1 ($\text{ADV} \ge \$50\text{M/day}$): $10\text{ bps}$ round-trip ($0.10\%$) (`source-reported`).
    - Tier 2 ($\$10\text{M} \le \text{ADV} < \$50\text{M/day}$): $25\text{ bps}$ round-trip ($0.25\%$) (`source-reported`).
    - Tier 3 ($\$2\text{M} \le \text{ADV} < \$10\text{M/day}$): $60\text{ bps}$ round-trip ($0.60\%$) (`source-reported`).
    - Tier 4 ($\$0.5\text{M} \le \text{ADV} < \$2\text{M/day}$): $150\text{ bps}$ round-trip ($1.50\%$) (`source-reported`).
    - Tier 5 ($\text{ADV} < \$0.5\text{M/day}$): $300\text{ bps}$ round-trip floor ($3.00\%$) (`source-reported`).
- **Capacity Constraints:**
  - For the broad cohort: Capacity is essentially zero due to severe microcap concentration ($41.4\% < \$2\text{M/day}$), where institutional capital deployment would incur severe market impact exceeding several hundred basis points `[research interpretation]`.
  - For the liquid sub-cohort ($\text{ADV} \ge \$10\text{M/day}$): Capacity is theoretically scalable ($>\$50\text{M}$ AUM), but after-cost expected return is zero to negative `[research interpretation]`.
- **Shorting / Borrow Assumptions:** Long-only equity catalyst; borrow costs not applicable (`source-reported`).

## Evidence

### Source-reported

All quantitative values below trace directly to committed decision and report records in `JonathanBeck1/falsification-campaign` (`research/buyback_drift_decision.md`, `research/buyback_drift_report.md`, and `scripts/diag_buyback_drift_liquidity.py`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`):

1. **Broad Cohort Sample Accounting (2015–2025):**
   - Raw SEC EDGAR qualifying accessions (Item 8.01, excl. 2.02): 1,500 (`source-reported`).
   - Deduped `(ticker, quarter)` filings: 1,479 (`source-reported`).
   - Distinct tickers fetched: 837 (95 missing price history) (`source-reported`).
   - Complete usable event windows: $N = 1,303$ (`source-reported`).
   - Events dropped due to incomplete windows: 11 (`source-reported`).
   - Matched `(ticker, year)` non-event placebo windows: $N = 4,779$ (`source-reported`).

2. **Broad Cohort Performance ($CAR_{[+1, +21]}$, Flat $15\text{ bps}$ Cost):**
   - Gross mean CAR: $+1.233\%$ (`source-reported`).
   - After-cost mean CAR (flat $15\text{ bps}$): $+1.083\%$ (`source-reported`).
   - After-cost $t$-statistic: $+3.39$ (`source-reported`).
   - Median CAR: $+0.667\%$ (mean significantly exceeds median, indicating positive tail skew) (`source-reported`).
   - Win rate (% positive CAR): $53.3\%$ (`source-reported`).
   - Cross-event Sharpe ratio ($\text{mean} / \text{std}$): $+0.107$ (`source-reported`).
   - 2x friction stress (flat $30\text{ bps}$): $+0.933\%$ ($t = +2.92$) (`source-reported`).
   - In-Sample (IS, 2015–2019, $N=451$): $+1.248\%$ ($t = +2.87$) (`source-reported`).
   - Out-of-Sample (OOS, 2020–2025, $N=852$): $+0.995\%$ ($t = +2.31$) (`source-reported`).

3. **Matched Non-Event Control (Placebo):**
   - Placebo sample size: $N = 4,779$ windows (`source-reported`).
   - Placebo mean CAR: $-0.283\%$ (`source-reported`).
   - Placebo $t$-statistic: $-1.62$ (`source-reported`).
   - Net of matched control: $+1.516\%$ ($t = +4.17$) (`source-reported`).

4. **Secondary Horizons (Broad Cohort):**
   - $CAR_{[+1, +5]}$: Gross $+1.161\%$, after-cost $+1.011\%$, $t = +5.10$ ($N=1,303$) (`source-reported`).
   - $CAR_{[+1, +63]}$: Gross $+0.727\%$, after-cost $+0.577\%$, $t = +1.04$ ($N=1,303$) (`source-reported`).

5. **Liquidity Distribution of Broad Cohort (Trailing 20d Median ADV):**
   - 10th percentile ADV: $\$0.11\text{M/day}$ (price: $\$6.53$) (`source-reported`).
   - 25th percentile ADV: $\$0.45\text{M/day}$ (price: $\$13.80$) (`source-reported`).
   - 50th percentile (median) ADV: $\$4.55\text{M/day}$ (price: $\$28.09$) (`source-reported`).
   - 75th percentile ADV: $\$26.47\text{M/day}$ (price: $\$57.51$) (`source-reported`).
   - 90th percentile ADV: $\$106.90\text{M/day}$ (price: $\$108.69$) (`source-reported`).
   - Share of cohort with $\text{ADV} < \$2\text{M/day}$: $41.4\%$ (`source-reported`).
   - Share of cohort with $\text{ADV} < \$10\text{M/day}$: $63.7\%$ (`source-reported`).

6. **Empirical Falsification via Realistic Tiered Costs & Liquid Screening:**
   - **Realistic Tiered Friction ($N=1,303$):** Mean after-cost CAR is **$-0.97\%$ ($t = -3.04$)** (`source-reported`).
   - **Tradeable Liquid Sub-Cohort ($\text{ADV} \ge \$10\text{M/day}$, $N=208$):**
     - Gross mean CAR: $+0.38\%$ (median $+0.05\%$) (`source-reported`).
     - After tiered friction ($10$–$25\text{ bps}$): $+0.205\%$ ($t = +0.32$) (`source-reported`).
     - Temporal Partition (Decay & Sign Flip):
       - IS ($< 2020$, $N=54$): $+3.29\%$ (`source-reported`).
       - OOS ($\ge 2020$, $N=154$): **$-0.64\%$** (`source-reported`).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Illiquidity Mirage Falsification:** Under realistic transaction friction calibrated to trailing ADV, the $+1.08\%$ apparent abnormal return inverts to a statistically significant loss of $-0.97\%$ ($t = -3.04$) (`source-reported`).
- **OOS Decay & Sign-Flip in Liquid Names:** In the tradeable institutional universe ($\text{ADV} \ge \$10\text{M/day}$), modern out-of-sample performance (2020–2025) flips negative to $-0.64\%$ ($N=154$), indicating that the historical buyback premium has been fully arbitraged away in liquid equities (`source-reported`).
- **Contaminated Control:** The matched non-event placebo exhibits negative drift ($-0.283\%$), proving that small-cap stocks drift downward between news events; the "net-of-matched" statistic is inflated by the control's downward drift rather than genuine event potency (`source-reported`).
- **Non-Operating Contaminants:** Closed-end crypto trust repurchases (ETCG $+55.8\%$, BCHG $+44.1\%$) contaminated the top positive tail, masquerading as operating corporate buybacks (`source-reported`).

## Falsification plan

- **Falsification Status:** Pre-registered empirical falsification completed by JonathanBeck1 (T41) with verdict `KILL`.
- **Pre-Registered Falsification Criteria (JonathanBeck1 T41 Gate):**
  1. *Sample Size:* $N \ge 30$ usable events (`source-reported`).
  2. *Statistical Significance:* After-cost primary mean CAR $> 0$ and $|t| \ge 2.0$ (`source-reported`).
  3. *Temporal Sign Stability:* IS and OOS after-cost means must maintain the same sign, with both sub-samples $N \ge 10$ (`source-reported`).
  4. *Placebo Control:* Matched non-event placebo $|t| < 2.0$ (`source-reported`).
  5. *Net-of-Matched Excess:* Net of matched control $> 0$ and $|t| \ge 2.0$ (`source-reported`).
  6. *Too-Good Tripwire:* Full-gate pass triggers mandatory inspection of top-5 contributors, size/liquidity distribution, and realistic execution costs (`source-reported`).
- **Operational Falsification Stress Tests for Future Re-evaluation:**
  1. *Liquidity-Tiered Cost Stress Test:* Evaluate after-cost CAR across discrete liquidity quintiles. If after-cost returns in the top two liquidity quintiles ($\text{ADV} \ge \$10\text{M/day}$) fail to achieve $t \ge 2.0$ or invert sign, confirm that the signal is an unharvestable illiquidity artifact `[research-defined falsification threshold]`.
  2. *Temporal Partition Walk-Forward Test:* Split the sample at 2020-01-01. If the liquid sub-cohort generates an OOS mean CAR $\le 0.0\%$, confirm complete anomaly decay and reject execution deployment `[research-defined falsification threshold]`.
  3. *EDGAR Text Classification Ablation:* Exclude generic open-market repurchase authorizations and evaluate only Accelerated Share Repurchase (ASR) agreements or fixed-price tender offers. If ASR programs also exhibit after-cost CAR $< 0.50\%$ in liquid names, falsify the buyback signaling hypothesis across all sub-types `[research-defined falsification threshold]`.
  4. *Execution Lag Sensitivity Test:* Shift trade execution from $t_0$ market-close to $t_0+1$ open or $t_0+1$ close. If delayed execution reduces gross CAR by $>30\text{ bps}$, reject the hypothesis of multi-week information underreaction `[research-defined falsification threshold]`.

## Crypto portability

- **Portability Classification:** `not applicable` (with `adapted/unproven` analogue).
- **Asset-Class Boundary:** Corporate share repurchases are legal actions governed by SEC Rule 10b-18 and Delaware corporate law, executing repurchases of registered common stock using corporate treasury reserves. No direct analogue exists in decentralized spot or perpetual crypto markets.
- **Porting Analogues & Severe Structural Differences:**
  1. *Token Burns & Buyback Mechanisms:* Certain DeFi protocols (e.g., MakerDAO MKR burns, Binance BNB quarterly burns, Raydium buybacks) use protocol revenue to purchase and burn governance tokens. However, these mechanisms differ fundamentally from corporate 8-Ks:
     - On-chain transparency: Smart contract buybacks are visible on-chain in real-time or predictable algorithmic schedules, eliminating filing-delay information asymmetry `[research interpretation]`.
     - Regulatory & Governance Arbitrage: Unlike corporate boards subject to fiduciary duties, token issuers frequently modify or suspend burn programs without disclosure `[research interpretation]`.
     - Front-Running & MEV: Public on-chain DEX buyback transactions are subject to sandwich attacks and generalized front-running by searchers, severely degrading protocol capital efficiency `[research interpretation]`.
  2. *Market Microstructure & 24/7 Sessions:* Crypto markets trade continuously without market-on-close auctions. Disclosures made via Twitter/X, Discord, or governance forums diffuse instantaneously through automated sentiment bots, leaving no multi-day retail drift `[research interpretation]`.

## Limitations

- **Underspecified Intraday Execution:** The study utilizes daily adjusted closing prices ($t_0$ close to $t_0+21$ close). It does not simulate intra-day execution trajectories (TWAP/VWAP) or quoted order-book depths `[underspecified]`.
- **Survivorship Gap in yfinance History:** 95 qualifying corporate filers could not be matched with active historical price data on Yahoo Finance, likely representing delisted, acquired, or bankrupt microcap firms. Because failing microcaps are disproportionately purged, this survivorship bias conservatively favors the reported gross return; true returns in illiquid names are likely even lower `[data gap]`.
- **Unmodeled Buyback Sub-types:** The study evaluates broad open-market repurchase authorizations (Item 8.01) matching 6 specific phrases. It does not isolate Accelerated Share Repurchases (ASRs), modified Dutch auction tender offers, or authorizations scaled by percentage of shares outstanding `[unproven]`.
- **Absence of Long-Horizon Value Conditioning:** The classic literature (Ikenberry et al. 1995; Peyer & Vermaelen 2009) documented maximum abnormal returns over 1-to-4-year holding periods concentrated in high book-to-market (value) stocks. The 21-day and 63-day horizons tested here examine short-to-intermediate announcement momentum, leaving multi-year fundamental undervaluation drift untested `[unproven]`.

## Implementation status

- `not-implemented`.
- No prototype, backtest harness, or strategy class has been implemented in PyBroker, NautilusTrader, or live trading workflows.
- This record captures external empirical falsification research only.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves as a formal negative-evidence capture demonstrating that broad SEC Form 8-K Item 8.01 share repurchase announcement drift is an unharvestable small-cap illiquidity artifact that has decayed to negative expectancy in liquid equities.
- It is strictly prohibited from being promoted to candidate status, implemented in NautilusTrader, or authorized for Paper, Testnet, or Live execution.

## Related Wiki records

- `[[quant/sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05]]`
- `[[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]`
- `[[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]]`
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]`

## Sources

- JonathanBeck1, *A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: `https://github.com/JonathanBeck1/falsification-campaign`
- JonathanBeck1, *Decision: Buyback-Announcement Drift (T41)*, `research/buyback_drift_decision.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/buyback_drift_decision.md`
- JonathanBeck1, *Pre-registration — T41 Buyback-Announcement Drift*, `research/buyback_drift_preregistration.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/buyback_drift_preregistration.md`
- JonathanBeck1, *T41 — Buyback-Announcement-Drift Study Result*, `research/buyback_drift_report.md`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/buyback_drift_report.md`
- JonathanBeck1, *Python Implementation Core and Unit Tests*, `src/trader/catalysts/buyback_drift.py`, `scripts/run_buyback_drift_study.py`, `scripts/diag_buyback_drift_liquidity.py`, and `tests/financial/test_buyback_drift.py`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`.
- JonathanBeck1, *The negative result: an empirical falsification of retail-accessible trading edges*, `research/PAPER_DRAFT.md`, Section 4.2, 4.7, and 7, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md`
- David L. Ikenberry, Josef Lakonishok, and Theo Vermaelen, *Market Underreaction to Open Market Share Repurchases*, Journal of Financial Economics, Vol. 39, No. 2-3 (1995), pp. 181–208. DOI: [10.1016/0304-405X(95)00826-Z](https://doi.org/10.1016/0304-405X(95)00826-Z)
- Theo Vermaelen, *Common Stock Repurchases and Market Signalling: An Empirical Study*, Journal of Financial Economics, Vol. 9, No. 2 (1981), pp. 139–183. DOI: [10.1016/0304-405X(81)90011-8](https://doi.org/10.1016/0304-405X(81)90011-8)
- Urs Peyer and Theo Vermaelen, *The Nature and Persistence of Buyback Anomalies*, The Review of Financial Studies, Vol. 22, No. 4 (2009), pp. 1693–1745. DOI: [10.1093/rfs/hhn056](https://doi.org/10.1093/rfs/hhn056)
- R. David McLean and Jeffrey Pontiff, *Does Academic Research Destroy Stock Return Predictability?*, The Journal of Finance, Vol. 71, No. 1 (2016), pp. 5–32. DOI: [10.1111/jofi.12365](https://doi.org/10.1111/jofi.12365)
