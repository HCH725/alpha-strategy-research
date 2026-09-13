---
schema: strategy-research-record-v1
title: "Put-Call Parity Implied Borrow Rate: Short-Constraint Overvaluation Falsification, Dividend Confounding, and General-Collateral Data Wall"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options-microstructure
  - put-call-parity
  - hard-to-borrow
  - short-sale-constraints
  - dividend-confounding
  - equity-cross-section
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "JonathanBeck1, 'A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced', GitHub repository 'JonathanBeck1/falsification-campaign', commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63, accessed 2026-09-13. https://github.com/JonathanBeck1/falsification-campaign"
  - "JonathanBeck1, 'Decision: Put-Call Parity / Implied Borrow (T26)', research/putcall_parity_borrow_decision.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/putcall_parity_borrow_decision.md"
  - "JonathanBeck1, 'Pre-registration: Put-Call Parity / Implied Borrow (T26)', research/putcall_parity_borrow_preregistration.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/putcall_parity_borrow_preregistration.md"
  - "JonathanBeck1, 'T26 — Put-Call Parity / Implied Borrow Study Result', research/putcall_parity_borrow_report.md (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/putcall_parity_borrow_report.md"
  - "JonathanBeck1, 'Diagnostic for T26 — show that the options-implied carry q* IS borrow + dividend', scripts/diag_putcall_dividend.py (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/scripts/diag_putcall_dividend.py"
  - "JonathanBeck1, 'Python Pure Parity Implementation', src/trader/catalysts/putcall_parity_borrow.py (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/src/trader/catalysts/putcall_parity_borrow.py"
  - "JonathanBeck1, 'The negative result: an empirical falsification of retail-accessible trading edges', research/PAPER_DRAFT.md, Section 5, 7.1, 7.2 (commit 79c3a2a21600cd3a0f9e242de5ce15173f512c63). https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Put-Call Parity Implied Borrow Rate: Short-Constraint Overvaluation Falsification, Dividend Confounding, and General-Collateral Data Wall

## Provenance

- **Repository:** `https://github.com/JonathanBeck1/falsification-campaign` (`source-reported`)
- **Author / Research Lab:** Jonathan Beck (`JonathanBeck1`) (`source-reported`)
- **Immutable Commit SHA:** `79c3a2a21600cd3a0f9e242de5ce15173f512c63` (`source-reported`)
- **As-of Date:** 2026-09-13 (empirical execution run: 2026-06-17T16:59:51Z; foundation spot parity re-run completed 2026-06-18) (`source-reported`)
- **Primary Source File Paths:**
  - `research/putcall_parity_borrow_decision.md`: Official audit decision record detailing the `DATA_WALL` verdict, empirical metrics, gate evaluation, and discovery of the dividend confounding mechanism (`source-reported`).
  - `research/putcall_parity_borrow_preregistration.md`: Pre-registered research protocol defining the hypothesis, universe of 24 large-cap equities, European parity inversion math, near-the-money selection, monthly rebalance cadence, 20 bps round-trip friction, 7-point gate, and kill criteria (`source-reported`).
  - `research/putcall_parity_borrow_report.md`: Complete empirical output report logging per-name median implied carry $q^*$, cross-sectional return spreads on 21-day, 5-day, and 63-day horizons, in-sample vs out-of-sample partitions, and shuffled-borrow placebo results (`source-reported`).
  - `scripts/diag_putcall_dividend.py`: Standalone mechanism diagnostic auditing the correlation between trailing dividend yield and options-implied carry ($r = +0.949$), proving $q^* \approx \text{borrow} + \text{dividend\_yield}$ (`source-reported`).
  - `src/trader/catalysts/putcall_parity_borrow.py`: Pure Python core implementing European put-call parity inversion (`implied_carry`), paired ATM contract selection (`parity_pairs`), per-name robust median aggregation (`name_date_borrow`), cross-sectional tercile sorting (`cross_section_spread`), and gate evaluation (`evaluate_gate`) (`source-reported`).
  - `research/PAPER_DRAFT.md`: Campaign synthesis paper classifying T26 under Campaign Failure Class 5 ("Confounded Label") and Data Wall category (§5, §7.1, §7.2) (`source-reported`).
- **Primary Source Verification:** Directly inspected and verified source code, mathematical equations, backtest logs, and report tables from commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`. All empirical values, $t$-statistics, correlation figures, and basis-point carries trace directly to these primary files.
- **Repository Deduplication Audit:** A comprehensive grep across all existing records in `alpha-strategy-research` confirmed zero prior records citing `putcall_parity_borrow`, `put-call parity implied borrow`, or JonathanBeck1 test T26. While other independent studies from `JonathanBeck1/falsification-campaign` were captured earlier (`sec-form-13f-institutional-cloning-staleness-falsification-2026-09-13.md` [T44], `sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13.md` [T42], `sec-form-8-k-buyback-announcement-drift-smallcap-illiquidity-decay-falsification-2026-09-13.md` [T41], `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` [T39], and `single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13.md` [T23]), T26 investigates a completely distinct economic mechanism (options-implied carry inversion, short-sale constraint pricing, and dividend yield confounding), operates on a distinct options-implied signal, and establishes an independent empirical result.

## Economic mechanism

### Source-reported

1. **The Classical Short-Sale Constraint and Overvaluation Hypothesis:**
   In theoretical equity derivatives literature (Ofek, Richardson, and Whitelaw, 2004, *Journal of Finance*; D'Avolio, 2002, *Journal of Financial Economics*), short-sale constraints prevent arbitrageurs from shorting overvalued stocks. When an equity is hard to borrow (characterized by high equity lending fees or limited inventory), short sellers cannot easily short the physical shares to enforce no-arbitrage bounds between the stock and its derivative contracts.
   Consequently, the downward pressure is expressed in the options market: traders buy synthetic short positions (buy put, sell call), driving the options-implied forward price:
   $$F^* = (C - P + K e^{-r\tau}) e^{q^* \tau}$$
   below the theoretical cost-of-carry forward price $S e^{(r-d)\tau}$. Under European put-call parity with a continuous carry rate $q^*$:
   $$C - P = S e^{-q^* \tau} - K e^{-r\tau}$$
   Solving for the options-implied carry rate yields:
   $$q^* = -\frac{1}{\tau} \ln\left( \frac{C - P + K e^{-r\tau}}{S} \right)$$
   In classical theory, for a zero-dividend asset, $q^*$ represents the options-implied hard-to-borrow rate. Stocks with high implied borrow rates are hypothesized to be severely short-constrained and overvalued, predicting subsequent negative abnormal returns.

2. **The Falsification Findings and the General-Collateral Data Wall (JonathanBeck1 T26):**
   JonathanBeck1 tested this hypothesis across 24 liquid US mega-cap/large-cap equities over the period 2022–2026 and discovered two fundamental structural impediments that falsify the tradeability of this signal:
   - **General Collateral (GC) Data Wall:** Liquid large-cap equities are easy to borrow; institutional lending fees are near zero (<0.50%/yr). Across the 24 liquid names, the pooled cross-sectional median $q^*$ is $-1.9$ bps/yr, with a narrow inter-quartile range of only $+69.9$ bps/yr. There is virtually no true hard-to-borrow rate dispersion to sort on.
   - **Confounded Label / Dividend Identification Trap (Class 5 Artifact):** When put-call parity is inverted assuming zero continuous dividend yield ($q=0$), the derived carry parameter $q^*$ mathematically absorbs both the physical lending/borrow fee $b$ and the continuous dividend yield $d$:
     $$q^* \approx b + d$$
     Because $b \approx 0$ on large-cap equities, $q^*$ is overwhelmingly dominated by the underlying stock's dividend yield. Per-name median $q^*$ correlates with trailing 12-month dividend yield at $+0.949$ ($n=24$).
   - **Consequence:** Sorting cross-sectionally on "implied borrow" without exogenous dividend stripping does not rank stocks by short-sale friction; it ranks them by dividend yield. The top tercile contains dividend-paying value stocks (PEP $+109.4$, TXN $+100.0$, CSCO $+87.4$, HON $+84.7$, LIN $+67.6$, QCOM $+51.4$ bps/yr), while the bottom tercile contains non-dividend growth/tech stocks (AMD $-50.0$, ISRG $-48.1$, ADBE $-48.2$, TSLA $-45.0$, NFLX $-38.2$, META $-31.7$ bps/yr). The resulting return spread is statistically indistinguishable from zero ($t = +0.64$) and mirrors a random placebo.

### Research interpretation

This record documents a critical negative result in derivatives-based cross-sectional equity alpha:
- **Identification Failure:** A derivative pricing relation cannot be inverted to extract an unobservable market friction (borrow fee) unless all other cash-flow components (discrete dividends, ex-date jumps) are modeled with precision exceeding the magnitude of the friction itself. On liquid stocks where borrow fees are 0–30 bps/yr, unadjusted dividend yields of 100–350 bps/yr completely swamp the signal, causing a severe "Confounded Label" artifact.
- **Universe Mismatch:** Testing hard-to-borrow anomalies on liquid large-caps is fundamentally flawed. Liquid stocks satisfy the easy-to-borrow condition, rendering any measured parity deviation purely an artifact of dividend timing, mid-quote bid-ask bounce, or American early-exercise premia rather than short-supply pricing.

Component roles in the tested trading structure:
- **Pricing Anchor:** Put-call parity midpoint inversion on contemporaneous option quotes
- **Candidate Alpha Signal:** Cross-sectional rank of per-name median implied carry $q^*$
- **Execution Vehicle:** Monthly cross-sectional equity long-short portfolio (long bottom tercile, short top tercile)
- **Friction Filter:** 20 bps deduction per rebalance (10 bps round-trip per equity leg)

## Signal

### Formation timestamp

- Option quotes and closing stock prices are captured at the official market close $t$ (16:00 ET / 21:00 UTC) (`source-reported`).
- Implied carry $q^*$ is computed using quotes available at close $t$ (`source-reported`).
- Trading execution occurs at the close of date $t$ or market open $t+1$ (`research-proposed`).
- Rebalance occurs monthly on the first trading session of each calendar month (`source-reported`).

### Lookback and filtering

- Option chains are filtered on trade date $t$ (`source-reported`):
  - **Moneyness Window:** $|K / S - 1.0| \le 0.05$ (near-the-money strikes within $\pm 5\%$ of spot) (`source-reported`). Near-the-money options carry real two-sided liquidity; deep out-of-the-money or in-the-money options have near-zero quote values where wide bid-ask spreads dominate $C - P$.
  - **Tenor Band:** $7\text{d} \le \tau \le 120\text{d}$ ($7/365 \le \tau \le 120/365$) (`source-reported`). Options with $<7$ days to expiration suffer extreme pin risk and settlement distortions; options with $>120$ days suffer from stale quotes and illiquidity.
  - **Quote Validity:** Both call and put legs must be simultaneously present with positive bids and asks; option price is mid $=(bid + ask)/2 > 0$ (`source-reported`).
  - **Outlier Threshold:** $|q^*| \le 1.50$ (150% annualized) (`source-reported`). Implied carries exceeding 150% annualized represent data errors or stale quotes and are purged.
  - **Per-Name Aggregation:** A minimum of 2 valid matched pairs is required per (ticker, date). The per-name implied borrow is the **median** $q^*$ across all qualifying pairs on date $t$ (`source-reported`). Using the median prevents a single bad pair from distorting the ticker's signal.

### Entry logic

- On each monthly rebalance date $t$:
  - Calculate per-name median $q^*$ for all qualifying names in the universe (`source-reported`).
  - Rank tickers in ascending order of $q^*$ (`source-reported`).
  - Form terciles:
    - **Long Leg (Low Implied Borrow):** Bottom tercile ($k = \text{round}(N / 3)$ names with lowest $q^*$) (`source-reported`).
    - **Short Leg (High Implied Borrow):** Top tercile ($k = \text{round}(N / 3)$ names with highest $q^*$) (`source-reported`).
  - Equal weighting across constituents within each tercile leg (`source-reported`).

### Exit logic

- Positions are held for a fixed horizon of 21 trading days (`fwd_21d`, approximately 1 calendar month) and rebalanced at the next monthly cycle (`source-reported`).
- Secondary non-gating horizons evaluated: 5 trading days (`fwd_5d`) and 63 trading days (`fwd_63d`) (`source-reported`).
- Stop-loss or take-profit rules: None specified in the primary source; fixed-tenor rebalance (`source-reported`).

### Parameters

- Risk-free interest rate: $r = 4.0\%$ continuously compounded (`source-reported`). Held constant across all names so it represents a common-mode level shift that differences out of cross-sectional rankings.
- Moneyness band: $\pm 5\%$ (`DEFAULT_MONEYNESS_WINDOW = 0.05`) (`source-reported`).
- Min tenor: 7 calendar days (`DEFAULT_MIN_TAU = 7.0 / 365.0`) (`source-reported`).
- Max tenor: 120 calendar days (`DEFAULT_MAX_TAU = 120.0 / 365.0`) (`source-reported`).
- Min matched pairs per ticker: 2 (`min_pairs = 2`) (`source-reported`).
- Outlier cap: $|q^*| \le 1.50$ (`MAX_ABS_CARRY = 1.50`) (`source-reported`).
- Tercile fraction: $1/3$ (`TERCILE = 1.0 / 3.0`) (`source-reported`).
- Primary holding horizon: 21 trading days (`PRIMARY_WINDOW = "fwd_21d"`) (`source-reported`).
- Execution price assumption: Equity closing price (`research-proposed`).
- Fill model: Midpoint fill without market impact (`research-proposed`).

### Position-sizing logic

- Dollar-neutral long-short equity portfolio: 100% gross exposure, 50% long low-borrow tercile, 50% short high-borrow tercile (`source-reported`).
- Constituent weights: Equal-weighted within each leg (`$w_i = 1 / k$`) (`source-reported`).

## Required data

- **Instruments:** 24 large-cap US equities + 2 index ETFs (QQQ, SPY).
  - Constituents: `ADBE`, `AMAT`, `AMD`, `AVGO`, `BKNG`, `COST`, `CSCO`, `GOOG`, `GOOGL`, `HON`, `INTU`, `ISRG`, `LIN`, `LRCX`, `META`, `MU`, `NFLX`, `PEP`, `QCOM`, `REGN`, `TMUS`, `TSLA`, `TXN`, `VRTX`.
  - Excluded during primary collection: `AAPL`, `AMZN`, `NVDA` (lake incomplete at test time).
- **Option Data:** End-of-day (EOD) options NBBO quotes (bid, ask, strike, expiration, right) sourced from owned ThetaData parquet lake (`$TRADER_EOD_LAKE_ROOT`).
- **Stock Price Data:** Daily adjusted closing prices from yfinance (`trader.catalysts.prices.fetch_daily`), with SPY used for market adjustment ($\beta = 1$).
- **Sample Span:** January 1, 2022 to June 13, 2026 (~1,115 trading sessions per ticker; 53 monthly rebalance periods).
- **Point-in-Time Protections:**
  - Option quotes used for date $t$ ranking are observed strictly at the market close of date $t$.
  - Forward returns are measured strictly over $(t, t+21]$ trading days using closing prices strictly *after* date $t$.
  - Spot price $S$ is derived directly from contemporaneous option chain put-call parity midpoints to prevent split-adjustment date mismatches against unadjusted historical strike prices.
  - Universe is fixed ex-ante across all 24 names, precluding post-hoc survivorship contamination.
- **Missing Data Handling:** If a ticker has fewer than 2 valid matched pairs on rebalance date $t$, it is excluded from that date's cross-section. Dates with fewer than 3 qualifying tickers are skipped.

## Execution assumptions

- **Strategy Venue:** US equity cash market (NYSE / NASDAQ).
- **Execution Cost:** Single-name equity round-trip cost is modeled as 10 bps (5 bps to enter, 5 bps to exit). The long-short spread crosses two names (one long, one short), resulting in a mandatory deduction of **20 bps per rebalance** against the gross return spread (`SPREAD_COST = 0.0020`) (`source-reported`).
- **Execution Instrument:** Equities only. The options chain is used exclusively as a diagnostic measuring instrument; no option contracts are traded in the execution strategy (`source-reported`).
- **Shorting / Borrow Availability:** All 24 equity constituents are general collateral mega-caps with borrowing availability assumed at standard broker GC rates (<0.50%/yr) (`source-reported`).
- **Execution Timing:** Next-day market open or same-day market close (`research-proposed`).
- **Market Impact / Capacity:** Assumed negligible for retail/small-institutional size in mega-caps, but unmodeled for large institutional portfolios (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below are directly extracted from the primary test report (`research/putcall_parity_borrow_report.md`), decision record (`research/putcall_parity_borrow_decision.md`), and diagnostic logs (`scripts/diag_putcall_dividend.py`) at commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`.

#### 1. Implied Carry Level and Dispersion (The Data Wall Evidence)

Per-name median options-implied carry $q^*$ (annualized; basis points per year):

| Ticker | Median $q^*$ (bps/yr) | Usable Days | Dividend Status / Trailing Yield |
|:-------|:---------------------:|:-----------:|:---------------------------------|
| PEP    | **+109.4**           | 1,115       | Dividend payer (+305 bps/yr)     |
| TXN    | **+100.0**           | 1,115       | Dividend payer                   |
| CSCO   | **+87.4**            | 1,115       | Dividend payer                   |
| HON    | **+84.7**            | 1,114       | Dividend payer                   |
| LIN    | **+67.6**            | 1,079       | Dividend payer                   |
| QCOM   | **+51.4**            | 1,115       | Dividend payer                   |
| LRCX   | **+31.8**            | 1,079       | Dividend payer                   |
| TMUS   | **+30.7**            | 1,115       | Dividend payer                   |
| AVGO   | **+23.9**            | 1,115       | Dividend payer                   |
| AMAT   | **+20.0**            | 1,115       | Dividend payer                   |
| INTU   | **+13.6**            | 1,115       | Modest dividend payer            |
| COST   | **+8.9**             | 1,115       | Modest dividend payer            |
| GOOG   | **-12.8**            | 1,115       | Recent/minimal dividend          |
| BKNG   | **-19.6**            | 1,115       | Zero / minimal dividend          |
| MU     | **-19.7**            | 1,115       | Minimal dividend                 |
| GOOGL  | **-22.1**            | 1,115       | Recent/minimal dividend          |
| META   | **-31.7**            | 1,025       | Zero / minimal dividend          |
| VRTX   | **-33.2**            | 1,115       | Zero dividend                    |
| REGN   | **-33.4**            | 1,115       | Zero dividend                    |
| NFLX   | **-38.2**            | 1,115       | Zero dividend                    |
| TSLA   | **-45.0**            | 1,115       | Zero dividend                    |
| ISRG   | **-48.1**            | 1,115       | Zero dividend                    |
| ADBE   | **-48.2**            | 1,115       | Zero dividend                    |
| AMD    | **-50.0**            | 1,115       | Zero dividend                    |

- **Cross-name pooled median $q^*$:** **-1.9 bps/yr** (consistent with general collateral borrow $\approx 0$).
- **Cross-name IQR of median $q^*$:** **+69.9 bps/yr** (tiny dispersion, reflecting dividend differences).
- **Per-date top-minus-bottom tercile dispersion:** **+228.8 bps/yr** (satisfies the mechanical $\ge 100$ bps floor, but represents dividend dispersion rather than borrow dispersion).
- **Correlation with Trailing Dividend Yield:** $\mathbf{r = +0.949}$ ($n=24$).
- **Dividend-payer average $q^*$:** **+27.2 bps/yr**.
- **Zero-dividend average $q^*$:** **-43.8 bps/yr**.
- **Dividend-netted borrow ($b = q^* - d$):** Mean $\approx 0$, median $\approx 0$.

#### 2. Cross-Sectional Performance (Primary Window: fwd_21d, Low-Borrow minus High-Borrow)

| Performance Metric | Reported Value | Falsification / Gate Status |
|:-------------------|:--------------:|:----------------------------|
| Number of monthly rebalances ($N$) | 53 | PASS ($\ge 30$) |
| Gross mean return spread | +0.7653% | Informational |
| After-cost mean return spread (net 20 bps) | **+0.5653%** | **FAIL** (statistically indistinguishable from 0) |
| After-cost $t$-statistic | **+0.64** | **FAIL** (Hurdle $|t| \ge 2.0$) |
| Median return spread | **-0.2231%** | Informational (negative median) |
| Win rate (spread > 0) | 47.2% | Informational (< 50%) |
| Annualized spread Sharpe ratio | **+0.119** | Severe underperformance |
| In-Sample mean (2022–2023, $n=24$) | -0.2397% ($t = -0.20$) | Informational |
| Out-of-Sample mean (2024–2026, $n=29$) | +1.2314% ($t = +0.98$) | **FAIL** (Sign flip IS $\to$ OOS; both halves in-noise) |
| Placebo sort (shuffled borrow) mean ($t$) | **-0.7398% ($t = -1.68$)** | Real sort carries no more alpha than noise |

#### 3. Secondary Evaluation Windows (Non-Gating)

- **fwd_5d (5 trading days):** Gross $+0.1528\%$, after-cost **-0.0472%**, $t = -0.11$ ($n=54$).
- **fwd_63d (63 trading days, ~1 quarter):** Gross $+1.8138\%$, after-cost **+1.6138%**, $t = +1.28$ ($n=51$).

#### 4. Top Contributor Inspection

The largest absolute monthly return spreads occurred during macro regime transitions rather than company-specific short squeezes:
- 2026-04-01: spread $+23.78\%$ (low leg $+17.84\%$, high leg $-5.94\%$, dispersion $+151$ bps)
- 2023-01-03: spread $+20.10\%$ (low leg $+17.31\%$, high leg $-2.79\%$, dispersion $+183$ bps)
- 2023-05-01: spread $+13.33\%$ (low leg $+12.36\%$, high leg $-0.97\%$, dispersion $+278$ bps)
- 2024-12-02: spread $-11.84\%$ (low leg $-4.21\%$, high leg $+7.63\%$, dispersion $+259$ bps)
- 2025-10-01: spread $+11.28\%$ (low leg $+10.12\%$, high leg $-1.16\%$, dispersion $+166$ bps)

### Independently reproduced

`Not independently reproduced.` All quantitative metrics, $t$-statistics, and correlation findings represent third-party empirical results reported by Jonathan Beck (`JonathanBeck1/falsification-campaign` at commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`).

### Negative evidence

- **Statistical Insignificance:** Over 53 monthly cycles, the primary after-cost spread generated $t = +0.64$ ($p > 0.50$), failing the pre-registered $|t| \ge 2.0$ significance hurdle.
- **Negative Median and Low Win Rate:** The median spread is $-0.223\%$, and the strategy produced a positive return in only 47.2% of monthly rebalances.
- **Subperiod Instability (Sign Flip):** The strategy exhibited a sign flip between in-sample ($-0.240\%$) and out-of-sample ($+1.231\%$), with both subperiods statistically indistinguishable from zero.
- **Placebo Indistinguishability:** Shuffled-borrow permutations produced a spread with $t = -1.68$, confirming that the observed spread contains no genuine predictive structure beyond random noise.
- **Confounded Label Confirmation:** Diagnostic testing confirmed that options-implied carry $q^*$ is almost perfectly rank-correlated with trailing dividend yield ($r = +0.949$). Sorting on $q^*$ simply isolates a high-dividend vs zero-dividend factor tilt, completely obscuring any potential short-sale constraint signal.

## Falsification plan

To falsify the author's negative findings and determine whether put-call parity deviations can yield tradeable alpha under modified conditions, the following stress tests are defined:

1. **Small-Cap / Hard-to-Borrow Universe Stress Test:**
   - *Data & Universe:* Expand the universe from 24 liquid mega-caps to 500 US small-cap equities with verified high short interest (short interest $>10\%$ of float) and non-zero indicative borrow fees (from FIS Astec or S3 Partners).
   - *Metric:* Monthly cross-sectional return spread on $fwd\_21d$, net of actual physical borrow fees and 30 bps round-trip execution costs.
   - *Decision Rule:* If the after-cost spread fails to achieve an annualized Sharpe $\ge 0.80$ and $t \ge 2.50$ (`research-defined falsification threshold`), the claim that put-call parity deviations predict cross-sectional equity returns is definitively falsified even in the target small-cap domain.

2. **Exact Point-in-Time Dividend Stripping Test:**
   - *Data & Method:* Replace continuous carry $q^*$ with a discrete dividend-adjusted put-call parity model:
     $$C - P = S - \sum_{i} D_i e^{-r \tau_i} - K e^{-r\tau}$$
     using confirmed ex-dividend dates and projected cash dividend payments. Extract the pure residual implied borrow rate $b^*$.
   - *Metric:* Cross-sectional rank correlation between $b^*$ and realized forward returns.
   - *Decision Rule:* If the dividend-stripped borrow rate $b^*$ fails to achieve $t \ge 2.0$ (`research-defined falsification threshold`), the hypothesis that options chains reflect tradeable short-constraint overvaluation is falsified.

3. **American Early-Exercise Boundary Calibration:**
   - *Data & Method:* Replace the European parity inversion with a numerical American option solver (Barone-Adesi-Whaley or binomial tree) to account for early exercise premia on deep ITM puts and dividend-capture calls.
   - *Metric:* Variance reduction in residual carry $q^*$.
   - *Decision Rule:* If American exercise corrections account for $>50\%$ of the residual cross-sectional variance (`research-defined falsification threshold`), remaining parity deviations are proven to be early-exercise pricing artifacts rather than borrow frictions.

4. **Borrow Fee Escalation and Short-Leg Attrition Test:**
   - *Data & Method:* Simulate physical execution of the short leg, incorporating realistic borrow recall rates and fee escalation spikes (e.g., borrow rate increasing from 5% to 50% mid-holding period).
   - *Metric:* Net strategy P&L under borrow recall risk.
   - *Decision Rule:* If a 200 bps increase in borrow costs across the top tercile erases $>80\%$ of gross strategy alpha (`research-defined falsification threshold`), the strategy is deemed untradeable due to implementation friction.

5. **Placebo Permutation Null Test:**
   - *Data & Method:* Conduct 1,000 Monte Carlo permutations shuffling implied borrow ranks across tickers on each rebalance date.
   - *Decision Rule:* If the empirical $t$-statistic ($+0.64$) falls within the 5th to 95th percentile interval of the permutation distribution (`research-defined falsification threshold`), the strategy is conclusively proven to possess zero empirical edge.

## Crypto portability

**Portability Classification:** `adapted` / `unproven`

### Conceptual Portability to Cryptocurrency Markets

1. **Absence of Corporate Dividends:**
   In cryptocurrency derivatives (e.g., Deribit BTC and ETH options), underlying spot assets do not pay cash dividends. This structural feature eliminates the primary "Confounded Label" failure mode observed in equity markets ($q^* \approx \text{borrow} + \text{dividend}$).

2. **Perpetual Funding Rate as Dynamic Borrow Cost:**
   In crypto, perpetual futures funding rates act as a continuous, explicit price of leverage and borrowing. European options traded against perpetual futures or spot index prices reflect this funding carry directly.

3. **Put-Call Parity Formulation in Crypto:**
   Crypto options on Deribit are European-style, eliminating American early-exercise distortions. Put-call parity holds in pure European form:
   $$C - P = F \cdot e^{-r\tau} - K \cdot e^{-r\tau}$$
   where $F$ is the forward price implied by the futures term structure. The implied carry extracted from spot vs option combinations reflects:
   $$q^* = r_{\text{margin}} + \text{funding\_drag} - \text{staking\_yield}$$

### Frictions and Operational Risks in Crypto Deployment

- **Staking Yield as Crypto Dividend:** For proof-of-stake assets (ETH, SOL), native staking yields (3–6% APR) act as an endogenous dividend yield. Inverting put-call parity on spot ETH without accounting for staking yield will recreate the Class 5 dividend confounding artifact.
- **Exchange Fragmentation:** Unlike US equities where consolidated NBBO exists, crypto options liquidity is heavily concentrated on Deribit, while underlying spot and perpetual volumes are fragmented across Binance, OKX, and Bybit. Implied carry estimates vary widely depending on the chosen spot reference index.
- **Quanto and Inverse Margin Mechanics:** Deribit BTC/ETH options are inverse contracts coin-margined in the underlying cryptocurrency, introducing non-linear quanto convexity into put-call parity inversions that must be adjusted via the Björk-Stenberg identity (`research-proposed`).
- **Shorting Frictions:** While perpetual futures allow frictionless shorting, physical spot shorting requires OTC or exchange margin borrowing, where borrow rates are highly volatile and prone to sudden liquidity exhaustion during market stress.

## Limitations

- **General-Collateral Universe Restriction:** The empirical study was executed exclusively on 24 large-cap/mega-cap equities and 2 index ETFs. It documents a conclusive `DATA_WALL` for liquid names, but leaves the hypothesis untested on illiquid micro-caps where the Ofek-Richardson-Whitelaw effect was originally documented.
- **Dividend Confounding:** Inverting put-call parity without exogenous discrete dividend modeling completely contaminates the carry signal ($r = +0.949$ with dividend yield), turning a short-constraint test into a disguised dividend factor sort.
- **American Exercise Approximations:** Equity options traded on US exchanges are American-style. Applying European put-call parity introduces small structural approximation errors due to early exercise optionality on put contracts.
- **Constant Interest Rate Assumption:** The study utilized a flat $r = 4.0\%$ continuously compounded rate across all dates and tenors. While this shifts all names equally in the cross-section, term structure slope variations across the 7d–120d window introduce minor tenor-dependent noise.
- **Limited Sample Horizon:** The empirical test spans 4.5 years (2022–2026, 53 monthly rebalances). While sufficient to demonstrate statistical insignificance ($t = +0.64$), it covers a specific macro monetary tightening regime.

## Implementation status

`not-implemented`

No implementation of this strategy exists in our research stack, `nautilus-quant-system`, PyBroker, or NautilusTrader. The strategy has been empirically falsified as untradeable on liquid equities by the primary source, and serves as an audit benchmark against "Confounded Label" artifacts in options-implied factor research.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an empirical falsification capture documenting why options-implied borrow rate sorting fails to generate alpha on liquid equities. Its presence in this repository does not constitute approval for paper trading, testnet deployment, or live trading. Any future proposal to adapt this mechanism to crypto derivatives requires rigorous pre-registration, discrete staking yield stripping, and independent out-of-sample validation.

## Related Wiki records

- `[[single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]]` — Investigates option surface pricing dynamics around single-name earnings events in the same equity lake, documenting Class 2 (friction scale) and Class 7 (compensated jump risk) failure modes.
- `[[option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]]` — Examines put-call parity deviations (Cremers-Weinbaum measure) in equity options surfaces as an indicator of informed trading and downside skew.
- `[[bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01]]` — Analyzes implied carry wedges extracted via put-call parity from IBIT ETF options compared against CME Bitcoin futures basis.
- `[[sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]]` — Pre-registered empirical falsification of corporate catalyst drift in large-cap equity markets.

## Sources

1. Jonathan Beck (`JonathanBeck1`), *\"A pre-registered falsification campaign across ~50 trading-strategy families — and the negative result it produced\"*, GitHub repository `JonathanBeck1/falsification-campaign`, commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`, accessed 2026-09-13. URL: `https://github.com/JonathanBeck1/falsification-campaign`
2. Jonathan Beck, *\"Decision: Put-Call Parity / Implied Borrow (T26)\"*, `research/putcall_parity_borrow_decision.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/putcall_parity_borrow_decision.md`
3. Jonathan Beck, *\"Pre-registration: Put-Call Parity / Implied Borrow (T26)\"*, `research/putcall_parity_borrow_preregistration.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/putcall_parity_borrow_preregistration.md`
4. Jonathan Beck, *\"T26 — Put-Call Parity / Implied Borrow Study Result\"*, `research/putcall_parity_borrow_report.md` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/putcall_parity_borrow_report.md`
5. Jonathan Beck, *\"Diagnostic for T26 — show that the options-implied carry q* IS borrow + dividend\"*, `scripts/diag_putcall_dividend.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/scripts/diag_putcall_dividend.py`
6. Jonathan Beck, Python Implementation Core: `src/trader/catalysts/putcall_parity_borrow.py` in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/src/trader/catalysts/putcall_parity_borrow.py`
7. Jonathan Beck, *\"The negative result: an empirical falsification of retail-accessible trading edges\"*, `research/PAPER_DRAFT.md`, Section 5, 7.1, 7.2 in `JonathanBeck1/falsification-campaign` (commit `79c3a2a21600cd3a0f9e242de5ce15173f512c63`). URL: `https://github.com/JonathanBeck1/falsification-campaign/blob/79c3a2a21600cd3a0f9e242de5ce15173f512c63/research/PAPER_DRAFT.md`
8. Ofek, E., Richardson, M., & Whitelaw, R. F. (2004). Limited arbitrage and short sales restrictions: Evidence from the options markets. *Journal of Financial Economics*, 74(3), 449–481.
9. D'Avolio, G. (2002). The market for borrowing stock. *Journal of Financial Economics*, 66(2-3), 271–306.
