---
schema: strategy-research-record-v1
title: "SEC Form 13F Institutional Equity Cloning: Empirical Falsification of Smart-Money Following and the Binding Nature of the 45-Day Disclosure Lag"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-catalyst
  - institutional-flow
  - 13f-cloning
  - smart-money
  - disclosure-lag
  - market-friction
  - anomaly-decay
  - falsification
  - negative-results
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "Primary audit decision record: JonathanBeck1, 'Decision: 13F Institutional Cloning (T45)', research/thirteenf_clone_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/thirteenf_clone_decision.md"
  - "Primary pre-registration: JonathanBeck1, 'Pre-Registration: 13F Institutional Cloning (T45)', research/thirteenf_clone_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/thirteenf_clone_preregistration.md"
  - "Primary empirical report: JonathanBeck1, '13F Institutional Cloning (filing-date) — Event Study Result', research/thirteenf_clone_report.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/thirteenf_clone_report.md"
  - "Primary empirical code: JonathanBeck1, 'src/trader/catalysts/thirteenf_clone.py', 'scripts/run_thirteenf_clone_study.py', and 'tests/financial/test_thirteenf_clone.py' (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63)"
  - "Primary research synthesis: JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 4.1, 4.2, 8.1, 10.3, Table 1, and Table 2 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
  - "Historical academic foundation on managerial best ideas: Randolph B. Cohen, Christopher Polk, and Bernhard Silli, 'Best Ideas', Working Paper, Harvard Business School / London School of Economics (2010), later published in Journal of Financial Economics."
  - "Academic foundation on fund manager evaluation and co-holdings: Randolph B. Cohen, Joshua D. Coval, and Ľuboš Pástor, 'Judging Fund Managers by the Company They Keep', The Journal of Finance, Vol. 60, No. 3 (2005), pp. 1057–1096. DOI: 10.1111/j.1540-6261.2005.00756.x"
  - "Regulatory reporting requirement: US Securities and Exchange Commission, Rule 13f-1 under Section 13(f) of the Securities Exchange Act of 1934 (Form 13F filing requirements for institutional managers exercising investment discretion over $100M+ in Section 13(f) securities within 45 days after calendar quarter-end)."
  - "Anomaly decay literature: R. David McLean and Jeffrey Pontiff, 'Does Academic Research Destroy Stock Return Predictability?', The Journal of Finance, Vol. 71, No. 1 (2016), pp. 5–32. DOI: 10.1111/jofi.12365"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SEC Form 13F Institutional Equity Cloning: Empirical Falsification of Smart-Money Following and the Binding Nature of the 45-Day Disclosure Lag

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`).
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`).
- **Commit Date:** 2026-09-08T21:47:53Z (`source-reported`).
- **Source As-Of Date:** 2026-09-08 (`source-reported`).
- **Primary Source Documents & Code Directly Audited:**
  - `research/thirteenf_clone_preregistration.md`: Pre-registered research protocol detailing the directional hypothesis, SEC EDGAR Form 13F-HR filings across a frozen universe of 12 notable long-biased institutional managers, CUSIP-level holding diffing, ex-ante filing-date trade anchoring ($t_0 = \text{filing\_date}$), SPY market-adjusted cumulative abnormal return (CAR) framework ($\beta = 1$), 10 bps round-trip friction, temporal split (IS: filing year $\le 2020$, OOS: filing year $> 2020$), same-name random-date placebo controls, and falsification kill criteria (`source-reported`).
  - `research/thirteenf_clone_decision.md`: Official audit decision record recording the outright `KILL` verdict, empirical sample accounting ($N = 6,002$ usable events from 8,142 deduped new positions across 398 filings), after-cost 3-month primary window performance ($-0.56\%$, $t = -2.09$, significant wrong sign), comparison against same-name placebo ($+0.33\%$, which out-earned the real signal), severe out-of-sample sign flip (IS $+1.32\%$ vs OOS $-2.54\%$), and mean filing lag quantification ($47.0$ days) (`source-reported`).
  - `research/thirteenf_clone_report.md`: Complete empirical tables across 1-month, 3-month, 6-month, and 12-month event windows under gross, after-cost, placebo, IS early, and OOS late splits, alongside top-5 contributor ablation data (`source-reported`).
  - `src/trader/catalysts/thirteenf_clone.py`: Pure Python analytical module executing holding normalization (`normalize_cusip`), new position identification (`new_positions`), event formation (`build_clone_events`), forward market-adjusted CAR calculation (`compute_event_metrics`), summary aggregation (`aggregate`), and gate evaluation (`evaluate_gate`) (`source-reported`).
  - `scripts/run_thirteenf_clone_study.py`: End-to-end operational pipeline querying SEC EDGAR via `edgartools` (`edgar` 5.35.x) for Form 13F-HR filings, aggregating `infotable` XML data to equity-long CUSIPs, querying Yahoo Finance for daily auto-adjusted price histories, calculating abnormal returns against SPY, generating same-name placebos, and outputting report artifacts (`source-reported`).
  - `tests/financial/test_thirteenf_clone.py`: 22 deterministic, network-free unit tests verifying CUSIP normalization, diff logic against prior filings, option/put exclusion, ex-ante filing-date timestamping, after-cost deduction, and gate criteria (`source-reported`).
  - `research/PAPER_DRAFT.md`: Formal research manuscript (§4.1, §4.2, §8.1, §10.3, Tables 1 & 2) categorizing test T45 as Class 1 (Decayed Effect / In-Noise) within the broader 50-strategy empirical campaign (`source-reported`).
- **Historical Academic & Market Context:**
  - Cohen, Polk & Silli (2010), *"Best Ideas"*, found that active equity managers' highest-conviction positions outperform benchmarks and their own remaining portfolio holdings when evaluated from quarter-end trade dates (`source-reported`).
  - Cohen, Coval & Pástor (2005), *"Judging Fund Managers by the Company They Keep"*, *The Journal of Finance*, documented that performance evaluation improves when weighting manager positions by the consensus of skilled peers (`source-reported`).
  - US SEC Rule 13f-1 under Section 13(f) of the Securities Exchange Act of 1934 requires institutional managers with over $100\text{M}$ in Section 13(f) securities to submit Form 13F quarterly reports within 45 calendar days after the end of each calendar quarter (`source-reported`).
  - Commercial copycat and "guru" tracking strategies (e.g., AlphaClone, GuruFocus, hedge fund replication ETFs) market the thesis that retail investors can systematically profit by piggybacking on billionaire manager disclosures (`source-reported`).
  - McLean & Pontiff (2016), *"Does Academic Research Destroy Stock Return Predictability?"*, *The Journal of Finance*, demonstrated that publication and widespread visibility systematically degrade return predictability through arbitrage capital inflows (`source-reported`).
- **Underlying Sample & Universe:**
  - Manager Universe: A frozen, declared list of 12 well-known long-biased equity 13F filers selected ex-ante for name recognition and extensive historical filing continuity (no post-hoc performance filtering) (`source-reported`):
    1. Berkshire Hathaway / Warren Buffett (CIK `0001067983`)
    2. Pershing Square Capital Management / Bill Ackman (CIK `0001336528`)
    3. Third Point / Daniel Loeb (CIK `0001040273`)
    4. Greenlight Capital / David Einhorn (CIK `0001079114`)
    5. Appaloosa Management / David Tepper (CIK `0001006438`)
    6. Baupost Group / Seth Klarman (CIK `0001061768`)
    7. Icahn Capital / Carl Icahn (CIK `0001412093`)
    8. Lone Pine Capital (CIK `0001167483`)
    9. Scion Asset Management / Michael Burry (CIK `0001603466`)
    10. Pershing Square Holdings (CIK `0001656456`)
    11. Tiger Global Management (CIK `0001135730`)
    12. Viking Global Investors (CIK `0001167557`)
  - Total 13F-HR filings analyzed: $398$ filings spanning filing dates 2015-01-01 to 2024-06-30 (`source-reported`).
  - Raw clone events (NEW positions with reported market value $\ge \$5,000,000$, deduped by ticker and filing date): $8,142$ events across $2,967$ distinct corporate names (`source-reported`).
  - Usable study sample with complete $[0, +252]$ trading day price windows: $N = 6,002$ events (`source-reported`).
  - Exclusions / Dropouts:
    - 2,108 events dropped due to missing historical prices in Yahoo Finance (delisted tickers, bankruptcies, or ticker collisions) (`source-reported`).
    - 32 events dropped due to incomplete forward price history ($< 252$ trading days available) (`source-reported`).
    - Survivorship note: Yahoo Finance purges delisted entities; because failed clone investments disappear from the historical record, this survivor-only sample is tilted upward, biasing the study *in favor* of the cloning hypothesis. An empirical kill under this upward bias is therefore methodologically conservative (`source-reported`).
- **Temporal Sample Span:**
  - Overall study filing dates: 2015-01-01 to 2024-06-30 (allowing a full 1-year forward evaluation window through mid-2025) (`source-reported`).
  - In-Sample (IS, early split): Filing year $\le 2020$ ($N = 3,083$) (`source-reported`).
  - Out-of-Sample (OOS, late split): Filing year $> 2020$ ($N = 2,919$) (`source-reported`).
- **Repository Deduplication Audit:**
  - A full search of the `alpha-strategy-research` repository confirmed zero existing records evaluating SEC Form 13F institutional cloning, institutional portfolio replication, or campaign test T45.
  - Existing regulatory and event falsification records (`buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13.md` [Form 8-K buybacks], `sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13.md` [Form 10-12B corporate spin-offs], `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` [index reconstitution], and `sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05.md` [Form 4 insider purchases]) evaluate distinct regulatory disclosures, economic mechanisms, signal construction, and empirical datasets.

## Economic mechanism

### Source-reported

1. **The Classic "Smart-Money" Copycat Thesis:**
   - Elite institutional hedge fund managers and high-profile value allocators (e.g., Warren Buffett, Seth Klarman, Michael Burry) possess superior fundamental research resources, informational access, and analytical capabilities (`source-reported`).
   - When such managers initiate new, high-conviction equity positions, their trades reflect non-public fundamental insights or structural undervaluation (`source-reported`).
   - Because the broader market is assumed to under-react to complex institutional portfolio disclosures, retail followers hypothesize that copying newly revealed holdings upon public filing will capture post-announcement information drift over intermediate holding periods (1 to 12 months) (`source-reported`).

2. **The Structural Staleness Killer & Falsification Hypothesis:**
   - Under SEC Rule 13f-1, Form 13F is not filed in real-time; managers are granted a 45-day statutory grace period following the close of each calendar quarter (`source-reported`).
   - Consequently, when a public 13F filing lands on EDGAR, the manager has already owned the underlying position for an average of approximately 47 calendar days (and up to 135 days for purchases made early in the quarter) (`source-reported`).
   - By the time a retail follower can observe the filing, any private information, initial accumulation flow, or fundamental catalyst has already been impounded into the market price (`source-reported`).
   - Furthermore, because 13F disclosures are intensely followed by financial media, retail traders, and quantitative copycat algorithms, the publication itself often causes a transient opening pop followed by adverse price drift as short-term liquidity dries up or institutional allocators distribute shares into retail demand (`source-reported`).
   - Prior academic literature (Cohen-Frazzini-Malloy) localized excess returns to the trade date (quarter-end); when anchored to the actual public disclosure date, the tradeable edge is hypothesized to decay into noise or flip negative once transaction friction is subtracted (`source-reported`).

### Research interpretation

- The hypothesized alpha is an informational spillover / delay-exploitation effect. For the signal to be economically viable, the post-filing market drift must exceed the total transaction costs of entering and exiting single-name equities (`research-proposed`).
- A genuine informational edge must demonstrably outperform a randomized control group of identical securities traded across non-event calendar dates (`research-proposed`).
- If the observed performance is driven primarily by broad market exposure, cyclical growth/tech beta, or macro factor tailwinds rather than manager stock-selection skill, the strategy will exhibit severe regime instability and sign reversal across macroeconomic cycles (`research-proposed`).

## Signal

### Source-reported

- **Universe Identification:** All equity holdings disclosed by the 12 pre-declared institutional managers in quarterly SEC Form 13F-HR filings on EDGAR (`source-reported`).
- **Position Aggregation & Filtering:**
  - For each filing, `infotable` XML rows are aggregated by CUSIP, summing the reported market value (`Value`) across sub-managers (`source-reported`).
  - Filter: Long equity positions only; option contracts and put/call rows (`PutCall` populated) are excluded (`source-reported`).
  - De-Minimis Threshold: Positions with a reported market value $< \$5,000,000$ are excluded to remove residual or trivial holdings (`source-reported`).
- **New Position Identification (`new_positions`):**
  - A position is classified as **NEW** if its CUSIP was absent from that manager's immediately preceding quarterly 13F-HR filing (`source-reported`).
  - Position increases in existing holdings are excluded; only fresh initiations are tracked (`source-reported`).
- **Anchor Timestamp ($t_0$):**
  - Anchor is strictly the public **`filing_date`** posted on SEC EDGAR (`source-reported`).
  - The quarter-end reporting period (`report_period`) is explicitly rejected as an anchor to prevent look-ahead bias (`source-reported`).
- **Trade Execution:**
  - Trade entry occurs at the close of day $t_0$ (the first available regular-way closing price on or immediately after `filing_date`) (`source-reported`).
- **Deduplication:**
  - If multiple managers initiate the same ticker in the same quarterly filing window, the signal is deduplicated to exactly one event per `(ticker, filing_date)` to prevent overweighting identical forward return paths (`source-reported`).
- **Holding Horizons & Evaluation Windows (Trading Days, Inclusive):**
  - 1-Month Horizon (`car_0_p21`): Days $[t_0+0, t_0+21]$ (~1 calendar month) (`source-reported`).
  - **PRIMARY Window (`car_0_p63`):** Days $[t_0+0, t_0+63]$ (~3 calendar months, the standard inter-filing quarterly rebalance horizon) (`source-reported`).
  - 6-Month Horizon (`car_0_p126`): Days $[t_0+0, t_0+126]$ (~6 calendar months) (`source-reported`).
  - 12-Month Horizon (`car_0_p252`): Days $[t_0+0, t_0+252]$ (~1 calendar year) (`source-reported`).
- **Abnormal Return Calculation:**
  - Daily abnormal return for security $i$ on day $\tau$:
    $$\text{AR}_{i, \tau} = R_{i, \tau} - R_{\text{SPY}, \tau}$$
    where $R_{i, \tau}$ is the split- and dividend-adjusted daily close-to-close return of the cloned stock and $R_{\text{SPY}, \tau}$ is the total return of the SPY benchmark ($\beta = 1$) (`source-reported`).
  - Cumulative Abnormal Return (CAR) over event window $[0, h]$:
    $$\text{CAR}_i[0, h] = \sum_{\tau = t_0}^{t_0 + h} \text{AR}_{i, \tau}$$
    (`source-reported`).
- **Position Sizing:** Equal-weighted across all qualifying clone events (`source-reported`).

### Research-proposed (Operational Extensions)

- **Order Execution:** Market-on-Close (MOC) order on day $t_0$ if filing occurs prior to 15:30 EST, or Market-on-Open (MOO) on day $t_0+1$ (`research-proposed`).
- **Beta Neutralization:** Dynamic rolling beta hedging against SPY rather than fixed $\beta = 1$, adjusting for manager-specific cyclical/growth tilt (`research-proposed`).
- **Conviction Sizing:** Weighting clone allocations by the disclosed portfolio weight percentage ($\text{Value} / \text{Total Portfolio Value}$) rather than equal weighting (`research-proposed`).

## Required data

- **Regulatory Filing Ingestion:**
  - Form 13F-HR filings pulled via `edgartools` (`edgar` 5.35.x) from SEC EDGAR with `filing_date` between 2015-01-01 and 2024-06-30 (`source-reported`).
  - Fields extracted: CIK, company name, form type, filing date, reporting period end date, CUSIP, ticker, issuer description, option indicator (`PutCall`), and market value (`Value`) (`source-reported`).
  - Requests tagged with compliant descriptive user agent (`TRADER_SEC_USER_AGENT`) (`source-reported`).
- **Historical Market Data:**
  - Primary Instrument: Daily adjusted close prices (`auto_adjust=True`) for all identified clone tickers from Yahoo Finance (`source-reported`).
  - Market Benchmark: Daily adjusted close prices for SPDR S&P 500 ETF Trust (`SPY`) (`source-reported`).
- **Point-in-Time Availability:**
  - EDGAR filings are public the exact second they are posted; anchoring on `filing_date` ensures strict point-in-time adherence with zero foresight leakage (`source-reported`).
- **Missing Data Handling:**
  - Events lacking the complete 252-trading-day forward window ($N = 32$) or lacking unadjusted price histories in Yahoo Finance due to ticker changes or delistings ($N = 2,108$) are tracked and dropped (`source-reported`).

## Execution assumptions

- **Execution Timing:** Position entered on day $t_0$ close (or $t_0+1$ open) and held through $t_0+h$ close (`source-reported`).
- **Baseline Transaction Cost:** Fixed round-trip transaction friction of **10 bps** ($0.0010$, 5 bps entry + 5 bps exit), representing standard institutional and liquid retail equity execution costs (`source-reported`).
- **Friction Deduction:**
  $$\text{CAR}_{i, \text{after-cost}} = \text{CAR}_{i, \text{gross}} - 0.0010$$
  (`source-reported`).
- **Borrow & Shorting:** Long-only equity execution; benchmark SPY hedge assumed fully borrowable at general collateral rates ($\le 25\text{ bps/yr}$) (`research-proposed`).
- **Fill Model:** Full execution at recorded closing prices without modeled market impact or slippage beyond the declared fee allowance (`source-reported`).

## Evidence

### Source-reported

The primary empirical study evaluated $N = 6,002$ qualifying clone events across 12 prominent institutional managers from 2015 to 2024 (`research/thirteenf_clone_decision.md` and `research/thirteenf_clone_report.md`):

1. **Mean Disclosure Lag:**
   - Average lag between quarter-end reporting date and public SEC EDGAR filing date (`filing_date - report_period`): **47.0 calendar days** (`source-reported`).
   - This empirically confirms that by the time a follower can trade, the position information is approximately 1.5 months stale (`source-reported`).

2. **Gross Market-Adjusted CAR Performance (SPY, $\beta = 1$):**
   - **+1-Month Window (`car_0_p21`):** Mean **$-0.24\%$**, median $-0.11\%$, $49\%$ positive, $t = -1.46$ ($N = 6,002$) (`source-reported`).
   - **+3-Month Window (`car_0_p63`, PRIMARY):** Mean **$-0.46\%$**, median $+0.16\%$, $51\%$ positive, $t = -1.72$ ($N = 6,002$) (`source-reported`).
   - **+6-Month Window (`car_0_p126`):** Mean **$-0.76\%$**, median $+0.00\%$, $50\%$ positive, $t = -2.03$ ($N = 6,002$) (`source-reported`).
   - **+12-Month Window (`car_0_p252`):** Mean **$-0.84\%$**, median $+0.05\%$, $50\%$ positive, $t = -1.54$ ($N = 6,002$) (`source-reported`).

3. **After-Cost Performance (10 bps Round-Trip Friction Deducted):**
   - **+1-Month Window (`car_0_p21`):** Mean **$-0.34\%$**, median $-0.21\%$, $49\%$ positive, $t = -2.07$ ($N = 6,002$) (`source-reported`).
   - **+3-Month Window (`car_0_p63`, PRIMARY):** Mean **$-0.56\%$**, median $+0.06\%$, $50\%$ positive, $t = -2.09$ ($N = 6,002$) (`source-reported`).
   - **+6-Month Window (`car_0_p126`):** Mean **$-0.86\%$**, median $-0.10\%$, $50\%$ positive, $t = -2.30$ ($N = 6,002$) (`source-reported`).
   - **+12-Month Window (`car_0_p252`):** Mean **$-0.94\%$**, median $-0.05\%$, $50\%$ positive, $t = -1.72$ ($N = 6,002$) (`source-reported`).
   - **Finding:** Every single after-cost evaluation horizon is strictly negative, with the primary 3-month horizon exhibiting a statistically significant negative mean ($t = -2.09$, significant wrong sign) (`source-reported`).

4. **Matched-Control Placebo Comparison (Same-Name Random Dates, $N = 6,019$):**
   - For each cloned equity name, random non-event trading dates ($\ge 30$ trading days away from any actual 13F filing) were evaluated across identical forward horizons (`source-reported`).
   - +1-Month Placebo: Mean **$+0.04\%$**, median $+0.04\%$, $50\%$ positive, $t = +0.22$ (`source-reported`).
   - **+3-Month Placebo (PRIMARY):** Mean **$+0.33\%$**, median $+0.13\%$, $50\%$ positive, $t = +1.19$ (`source-reported`).
   - +6-Month Placebo: Mean **$+0.68\%$**, median $-0.10\%$, $50\%$ positive, $t = +1.66$ (`source-reported`).
   - +12-Month Placebo: Mean **$+0.25\%$**, median $-0.09\%$, $50\%$ positive, $t = +0.46$ (`source-reported`).
   - **Critical Falsification Result:** The same corporate names bought on random non-event calendar dates achieved $+0.33\%$ after cost, substantially outperforming the real 13F clone signal ($-0.56\%$). Buying on the 13F filing date actively degraded performance relative to unconditional holding (`source-reported`).

5. **Temporal Split & Severe Out-of-Sample Sign Inversion:**
   - **In-Sample (Filing Year $\le 2020$, $N = 3,083$, After-Cost):**
     - +1-Month: Mean $+0.45\%$, $t = +2.11$ (`source-reported`).
     - +3-Month (PRIMARY): Mean **$+1.32\%$**, median $+1.09\%$, $54\%$ positive, $t = +3.97$ (`source-reported`).
     - +6-Month: Mean $+2.34\%$, $t = +4.93$ (`source-reported`).
     - +12-Month: Mean $+4.03\%$, $t = +5.82$ (`source-reported`).
   - **Out-of-Sample (Filing Year $> 2020$, $N = 2,919$, After-Cost):**
     - +1-Month: Mean $-1.17\%$, $t = -4.61$ (`source-reported`).
     - +3-Month (PRIMARY): Mean **$-2.54\%$**, median $-1.23\%$, $47\%$ positive, $t = -6.07$ (`source-reported`).
     - +6-Month: Mean $-4.24\%$, $t = -7.32$ (`source-reported`).
     - +12-Month: Mean $-6.18\%$, $t = -7.42$ (`source-reported`).
   - **Mechanism Diagnosis:** The apparent profitability during 2015–2020 was a regime-dependent artifact resulting from a multi-year secular bull market in mega-cap technology and growth equities heavily favored by these 12 managers. When the macro regime shifted in 2021–2024, the strategy suffered severe, statistically catastrophic losses ($-2.54\%$ at $t = -6.07$), proving complete lack of signal robustness (`source-reported`).

6. **Too-Good Tripwire & Contributor Inspection:**
   - Top-5 individual positive contributors represented $-30\%$ of the summed primary CAR (softening the aggregate loss rather than manufacturing an artificial gain) (`source-reported`):
     - CD (Third Point), filed 2020-11-13: $+183.6\%$ (`source-reported`).
     - CVNA (Tiger Global), filed 2023-05-15: $+166.4\%$ (`source-reported`).
     - NVAX (Tiger Global), filed 2024-02-14: $+162.1\%$ (`source-reported`).
     - CD (Lone Pine), filed 2020-11-16: $+161.1\%$ (`source-reported`).
     - CBI (Berkshire Hathaway), filed 2015-11-16: $+146.8\%$ (`source-reported`).

7. **Official Universal Gate Evaluation:**
   - $N \ge 30$: **PASS** ($N = 6,002$) (`source-reported`).
   - After-Cost Expectancy $>0$ and $|t| \ge 2.0$: **FAIL** (Mean $-0.56\%$, $t = -2.09$, significant wrong sign) (`source-reported`).
   - Superior to Matched Placebo: **FAIL** (Real $-0.56\%$ loses to placebo $+0.33\%$) (`source-reported`).
   - OOS Sign Stability: **FAIL** (IS $+1.32\%$ vs OOS $-2.54\%$, catastrophic inversion) (`source-reported`).
   - **Verdict:** **KILL (Decayed Effect / In-Noise Anomaly with Binding Structural Staleness Identified)** (`source-reported`).

### Independently reproduced

- Not independently reproduced. The empirical figures cited above reflect the primary research repository's code, data, and analytical reports directly audited at commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63` of `JonathanBeck1/falsification-campaign`.

### Negative evidence

- The retail-accessible 13F cloning strategy generates statistically significant negative market-adjusted returns ($-0.56\%$, $t = -2.09$) over the primary 3-month holding horizon (`source-reported`).
- The 47-day statutory reporting lag ensures that public disclosures contain stale information that has already been fully absorbed by informed market participants (`source-reported`).
- A placebo baseline trading the same equities on random dates achieves positive returns ($+0.33\%$), demonstrating that entering on 13F filing dates introduces adverse timing and negative selection (`source-reported`).
- Out-of-sample performance collapses violently post-2020 ($-2.54\%$, $t = -6.07$), indicating that pre-2021 returns were driven by macro growth factor exposure rather than durable manager selection alpha (`source-reported`).

## Falsification plan

To challenge or falsify this negative verdict and demonstrate that an institutional cloning edge exists, a researcher must satisfy the following pre-declared empirical criteria:

1. **Short-Disclosure Filing Sub-Cohort Test:**
   - **Test Design:** Filter for institutional filings submitted within $\le 10$ calendar days of quarter-end (rapid voluntary filers) or large-position Form 13D/13G filings (which carry a 5-to-10 day reporting requirement) (`research-proposed`).
   - **Threshold:** The expedited cohort ($N \ge 50$) must produce an after-cost 3-month CAR $> +2.00\%$ with $t \ge +2.50$ under 20 bps transaction friction (`research-defined falsification threshold`).
   - **Action:** If successful, validates that disclosure timeliness is the specific governing parameter of informational decay (`research-proposed`).

2. **Consensus Overlap & High-Conviction Sizing Test:**
   - **Test Design:** Restrict entries strictly to equities initiated simultaneously by $\ge 3$ independent top managers within the same filing period, where position size represents $>5\%$ of each manager's reported 13F equity portfolio (`research-proposed`).
   - **Threshold:** The consensus high-conviction portfolio must generate an out-of-sample Sharpe ratio $\ge 1.0$ and net CAR $> +3.00\%$ with $|t| \ge 2.50$ across both 2015–2020 and 2021–2026 subperiods (`research-defined falsification threshold`).
   - **Action:** If passed, demonstrates that manager consensus filters out idiosyncratic high-beta noise (`research-proposed`).

3. **Multi-Factor Risk Model Residualization:**
   - **Test Design:** Regress daily cloned returns against the Fama-French 5-factor model plus Momentum and Quality factors (`research-proposed`).
   - **Threshold:** Statistically significant Jensen's alpha ($\alpha > 0$, $t_\alpha \ge +2.0$) surviving after subtracting factor premia and trading costs (`research-defined falsification threshold`).
   - **Action:** If alpha is zero, confirms that 13F cloning is entirely a disguised factor exposure strategy (`research-proposed`).

## Crypto portability

- **Portability Classification:** `not applicable` (direct) / `adapted` / `unproven` (synthetic analogy).
- **Direct Portability Barrier:** SEC Form 13F is a statutory reporting requirement applicable only to registered institutional managers holding US exchange-listed equity securities. No centralized regulatory body enforces equivalent quarterly portfolio reporting across decentralized protocols or offshore cryptocurrency exchanges (`research-proposed`).
- **Synthetic Analogy — On-Chain "Smart-Money" Whale Wallet Tracking:**
  - In digital assets, public blockchain ledgers enable real-time tracking of known institutional funds, market makers, and prominent whale addresses (e.g., via Arkham, Nansen, Dune Analytics, or Etherscan) (`research-proposed`).
  - Unlike 13F equity filings which suffer a 45-day reporting lag, on-chain transactions are broadcast in mempools and confirmed within seconds, eliminating the disclosure staleness friction (`research-proposed`).
- **Empirical Crypto Hazards:**
  - **Adverse Selection & Wash Trading:** Unidentified wallet addresses often engage in self-dealing, spoofing, and wash trading to bait automated copy-trading bots into illiquid decentralized pools (`research-proposed`).
  - **Hedging Disguise:** Spot token purchases by market makers (e.g., Wintermute, Jump) often represent delta hedges against complex OTC option positions or perpetual basis trades, misleading directional copycat followers (`research-proposed`).
  - **MEV Front-Running:** Publicly broadcast whale accumulation orders in decentralized mempools are immediately targeted by generalized front-running and sandwich bots, extracting all marginal execution value (`research-proposed`).
  - Porting 13F-style copycat following into crypto via on-chain wallet tracking remains unproven as a systematic edge and highly susceptible to adverse selection (`research-proposed`).

## Limitations

- **Omission of Short & Derivative Books:** Form 13F mandates disclosure of long US equity holdings only; short positions, foreign equity listings, commodity futures, credit instruments, and OTC derivatives remain entirely invisible, creating an incomplete representation of true hedge fund exposures (`source-reported`).
- **Survivorship Bias in Historical Pricing:** Yahoo Finance purges delisted tickers ($2,108$ events dropped); because distressed or bankrupt holdings are selectively removed, the empirical sample overstates survivor returns, making the negative result conservative (`source-reported`).
- **Coarse Beta Adjustment:** Abnormal returns are computed using a simplified market model ($\beta = 1$ against SPY), omitting explicit size, value, or sector factor loadings; however, given that raw and after-cost returns are outright negative, multi-factor models would further depress residual performance (`source-reported`).
- **Fixed Manager Universe:** The analysis evaluated 12 prominent managers selected ex-ante; while representative of elite active allocators, results may not generalize to specialized algorithmic funds or smaller niche managers (`source-reported`).

## Implementation status

- **Status:** `not-implemented`.
- No trading algorithms, automated scrapers, or execution engines utilizing SEC Form 13F cloning have been constructed or deployed in PyBroker, NautilusTrader, or production execution environments.
- This record serves strictly as an empirical research capture and audit of external peer research; implementation is neither requested nor authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This document records the empirical falsification and post-publication decay of the institutional cloning anomaly. It does not constitute approval for live capital allocation, strategy deployment, or paper trading.

## Related Wiki records

- [[quant/sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05]] — Machine learning analysis of corporate insider disclosures (SEC Form 4) as equity trading signals.
- [[quant/sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13]] — Empirical falsification of corporate spin-off post-distribution drift (SEC Form 10-12B) and forced-selling decay.
- [[quant/buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13]] — Empirical falsification of SEC Form 8-K share repurchase announcements as an illiquidity artifact.
- [[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]] — Empirical falsification of structural institutional flow anomalies around S&P 500 index reconstitution.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] — Empirical falsification of single-name equity options earnings plays under real quoted bid-ask friction.

## Sources

- Jonathan Beck (`JonathanBeck1`), *"A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced"*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: https://github.com/JonathanBeck1/falsification-campaign
- Jonathan Beck, *"Decision: 13F Institutional Cloning (T45)"*, `research/thirteenf_clone_decision.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/thirteenf_clone_decision.md
- Jonathan Beck, *"Pre-Registration: 13F Institutional Cloning (T45)"*, `research/thirteenf_clone_preregistration.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/thirteenf_clone_preregistration.md
- Jonathan Beck, *"13F Institutional Cloning (filing-date) — Event Study Result"*, `research/thirteenf_clone_report.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/thirteenf_clone_report.md
- Jonathan Beck, Python Implementation Files: `src/trader/catalysts/thirteenf_clone.py`, `scripts/run_thirteenf_clone_study.py`, and `tests/financial/test_thirteenf_clone.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`).
- Jonathan Beck, *"The negative result: an empirical falsification of retail-accessible trading edges"*, `research/PAPER_DRAFT.md`, Section 4.1, 4.2, 8.1, 10.3, Tables 1 & 2 in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md
- Randolph B. Cohen, Christopher Polk, and Bernhard Silli, *"Best Ideas"*, Working Paper, Harvard Business School / London School of Economics (2010).
- Randolph B. Cohen, Joshua D. Coval, and Ľuboš Pástor, *"Judging Fund Managers by the Company They Keep"*, *The Journal of Finance*, Vol. 60, No. 3 (2005), pp. 1057–1096. DOI: 10.1111/j.1540-6261.2005.00756.x
- US Securities and Exchange Commission, Rule 13f-1 under Section 13(f) of the Securities Exchange Act of 1934, 17 C.F.R. § 240.13f-1.
- R. David McLean and Jeffrey Pontiff, *"Does Academic Research Destroy Stock Return Predictability?"*, *The Journal of Finance*, Vol. 71, No. 1 (2016), pp. 5–32. DOI: 10.1111/jofi.12365
