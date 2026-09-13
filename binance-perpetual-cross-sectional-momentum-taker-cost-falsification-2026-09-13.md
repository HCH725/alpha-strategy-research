---
schema: strategy-research-record-v1
title: "Binance USDⓈ-M Perpetual Futures Cross-Sectional Momentum: Multi-Year Survivorship-Free Panel Replication, Retail Taker Fee Wall, and Phase Arbitrariness Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - cross-sectional-momentum
  - replication
  - falsification
  - negative-evidence
  - transaction-costs
  - phase-instability
  - heavy-tails
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "https://github.com/Silent47boryara/searching-for-edge/tree/dd4399a7218ae15e52e7dc342ee89d345ea74d14"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/momentum-evidence-from-binance-replication.md"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step3_full_history_spread/RESULT.md"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step3_full_history_spread/RESULT_net_of_costs.md"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step3_full_history_spread/RESULT_liquidity_exploratory.md"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step4_j2k2_spread/RESULT.md"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step3_full_history_spread/full_history_spread.py"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step3_full_history_spread/net_of_costs.py"
  - "https://github.com/Silent47boryara/searching-for-edge/blob/dd4399a7218ae15e52e7dc342ee89d345ea74d14/02-momentum/replication/step4_j2k2_spread/j2k2_spread.py"
  - "https://doi.org/10.2139/ssrn.7404139"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance USDⓈ-M Perpetual Futures Cross-Sectional Momentum: Multi-Year Survivorship-Free Panel Replication, Retail Taker Fee Wall, and Phase Arbitrariness Falsification

## Provenance

- **Primary Source Codebase & Research Log:** `Silent47boryara/searching-for-edge` (*Independent Research into Systematic Crypto Trading & Market Microstructure*), authored by Oleg Arefev (`Silent47boryara`), founder of `karaptic.com` (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/Silent47boryara/searching-for-edge` at immutable commit SHA `dd4399a7218ae15e52e7dc342ee89d345ea74d14` (commit timestamp: 2026-09-12T12:38:15+03:00) (`source-reported`).
- **Formal Academic Working Paper:** Oleg Arefev (2026), *"Cross-Sectional Momentum in Cryptocurrency: A Net-of-Costs Replication on Tradable Binance Perpetuals (2020-2026)"*, SSRN Working Paper 7404139, DOI: [10.2139/ssrn.7404139](https://doi.org/10.2139/ssrn.7404139), published September 2026 (`source-reported`).
- **Primary Source Research Files Directly Inspected:**
  - `02-momentum/momentum-evidence-from-binance-replication.md`: Core research synthesis documenting literature review, empirical design, gross vs net spreads, tail risks, and falsification verdicts (`source-reported`).
  - `02-momentum/replication/step2_multiyear_klines/download_multiyear_klines.py`: S3 downloader fetching all monthly 1d klines from `data.binance.vision` with resumable manifests (`source-reported`).
  - `02-momentum/replication/step2_multiyear_klines/build_panel.py`: Panel assembly script building open, close, and quote volume matrices across 832 historical perpetual contracts (`source-reported`).
  - `02-momentum/replication/step3_full_history_spread/full_history_spread.py`: Pre-registered headline $J=1 / K=1$ spread calculation script (338 weeks, 10,000 bootstrap resamples, 10,000 sign-flips, 5,000 within-week permutations) (`source-reported`).
  - `02-momentum/replication/step3_full_history_spread/net_of_costs.py`: Net-of-costs calculation applying Binance VIP 0 taker fees, slippage assumptions, and funding rate integration (`source-reported`).
  - `02-momentum/replication/step3_full_history_spread/RESULT.md`: Full-history gross and net results report with forced closure diagnostics (`source-reported`).
  - `02-momentum/replication/step3_full_history_spread/RESULT_net_of_costs.md`: Detailed breakdown of fee wall consumption and funding rate coverage limitations (`source-reported`).
  - `02-momentum/replication/step3_full_history_spread/RESULT_liquidity_exploratory.md`: Post-hoc 5-bucket liquidity exploratory analysis testing turnover concentration (`source-reported`).
  - `02-momentum/replication/step4_j2k2_spread/j2k2_spread.py`: Pre-registered $J=2 / K=2$ non-overlapping fortnightly spread script with dual-phase evaluation (`source-reported`).
  - `02-momentum/replication/step4_j2k2_spread/RESULT.md`: Diagnostic report establishing sign reversal between Phase A and Phase B (`source-reported`).
  - Raw tabular data: `lab_06_summary.csv`, `weekly_spreads.csv`, `weekly_spreads_net.csv`, `j2k2_summary.csv`, `forced_closures.csv`, `basket_membership.csv` (`source-reported`).
- **Primary Literature Anchors Evaluated in Source:**
  - Liu, Tsyvinski, & Wu (2022), *"Common Risk Factors in Cryptocurrency"*, *The Journal of Finance*, 77(6), 1133–1173 (NBER w25882), and Yukun Liu's November 2019 conference slides (`source-reported`).
  - Leigh Drogen, Corey Hoffstein, & Kevin Otte (2023), *"Cross-sectional Momentum in Cryptocurrency Markets"*, Starkiller Capital, SSRN 4322637 (`source-reported`).
  - Grobys, Kolari, Sandretto, Shahzad, & Äijö (2025), *"Cryptocurrency momentum has (not) its moments"*, *Financial Markets and Portfolio Management*, 39, 443–476 (`source-reported`).
  - Dobrynskaya, V. (2021), *"Cryptocurrency Momentum and Reversal"*, HSE University working paper (`source-reported`).
  - Li, J., & Zhu, Y. (2024), *"A LASSO Type Factor Model in Cryptocurrency"*, Central University of Finance and Economics working paper (`source-reported`).
  - Grobys, K., & Sapkota, N. (2019), *"Cryptocurrencies and momentum"*, *Economics Letters*, 180, 6–10 (`source-reported`).
- **Repository Deduplication Audit:** A full audit across `alpha-strategy-research` confirmed zero pre-existing records citing Oleg Arefev, repository `Silent47boryara/searching-for-edge`, or SSRN 7404139. Adjacent records address distinct universes, factors, or methodologies:
  - `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` captures the Drogen, Hoffstein, & Otte (2023) 30-day spot momentum study on Nomics token data rather than perpetual futures.
  - `bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13.md` evaluates 33 Bitget perpetuals using synthetic shuffled-return null distributions on a 12-major liquid panel.
  - `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` evaluates funding carry cross-sections rather than pure price momentum spreads.
  - `crypto-perp-vol-scaled-cross-sectional-momentum-factor-2026-09-12.md` investigates volatility scaling overlays on Top-50 tokens.

## Economic mechanism

### Source-reported

1. **Underreaction and Information Diffusion:** Cross-sectional momentum in financial assets (Jegadeesh & Titman 1993; Liu, Tsyvinski & Wu 2022) posits that market participants underreact to new fundamental, liquidity, or narrative information, generating multi-week price continuation as capital gradually chases past relative winners and dumps past relative losers (`source-reported`).
2. **Limits to Arbitrage and Shorting Costs:** In spot crypto markets, shorting illiquid tokens is structurally constrained by high borrow fees, exchange insolvency risks, or complete absence of borrow inventory. Perpetual futures theoretically resolve this barrier by providing symmetrical short exposure via cash-settled contracts (`source-reported`).
3. **The Microstructure Cost Wall:** While academic studies document statistically significant gross weekly momentum premiums across unconstrained cross-sections (e.g. $+2.5\%$ to $+4.1\%$ per week in Liu et al. 2022 on CoinMarketCap), institutional and retail execution on perpetual contracts requires crossing the bid-ask spread and paying exchange taker fees at weekly rebalances across 50–100 names per leg. These operational frictions mechanically erode the gross spread (`source-reported`).
4. **Heavy Tails and Asymptotic Inference Failure:** Realized returns in crypto momentum portfolios exhibit extreme tail fatness characterized by a power law distribution with tail exponent $\alpha < 3$ (Grobys et al. 2025). This formally implies theoretically undefined/infinite variance, invalidating standard Gaussian inference, conventional $t$-statistics, and Sharpe ratios (`source-reported`).

### Research interpretation

This study provides a rigorous, pre-registered empirical falsification of academic cross-sectional momentum as a standalone executable strategy for retail and quantitative proprietary desks on Binance perpetuals:
- **Taker Fee Erosion (The 70% Haircut):** The gross weekly spread of $+0.573\%$ observed on Binance perpetuals is genuine but economically fragile. Base retail taker fees ($0.05\%$ per side) and conservative slippage ($0.05\%$ per side) consume $0.400$ percentage points per week (69.8% of the gross spread), depressing the net return to $+0.173\%/\text{week}$ ($+0.013\%/\text{week}$ median) and rendering it statistically indistinguishable from pure noise across all three non-parametric significance tests ($p = 0.65$ sign-flip, $p = 0.80$ within-week permutation).
- **Phase Arbitrariness as Proof of Spuriousness:** Extending holding horizons to $J=2 / K=2$ (fortnightly rebalancing) cuts turnover in half ($0.20$ pp/week net costs). However, testing non-overlapping periods reveals fatal phase arbitrariness: starting the fortnightly cycle on even Mondays yields $+0.858\%$ net ($p = 0.29$), while starting on odd Mondays yields $-0.151\%$ net ($p = 0.85$). This $1.009$ pp divergence and sign reversal based solely on arbitrary calendar phase confirms that the observed positive mean is driven by isolated outlier weeks rather than a persistent economic drift.

## Signal

### Signal Construction & Data Calendar

- **Ranking Timestamp:** Sunday 23:59:59 UTC daily close (`source-reported`).
- **Execution Timestamp:** Monday 00:00:00 UTC daily open (`source-reported`).
- **Lookback Windows ($J$):**
  - **Specification 1 ($J=1 / K=1$, Headline):** 7 calendar days trailing prior to ranking date (`source-reported`):
    $$R_{i, t}^{\text{mom}} = \frac{P_{i, \text{Sunday Close}}}{P_{i, \text{Sunday Close}-7\text{d}}} - 1$$
  - **Specification 2 ($J=2 / K=2$, Literature Alternative):** 14 calendar days trailing prior to ranking date (`source-reported`):
    $$R_{i, t}^{\text{mom}} = \frac{P_{i, \text{Sunday Close}}}{P_{i, \text{Sunday Close}-14\text{d}}} - 1$$
- **Liquidity Hurdle:** Trailing 30-day median daily quote turnover $\ge 1,000,000$ USDT, requiring at least 20 valid observations out of 30 days prior to Sunday close (`source-reported`).
- **Eligibility Filter:** Strictly enforces non-null, strictly positive prices at ranking date, momentum lookback start, and Monday entry open (`source-reported`):
  $$\text{Eligible}_i = \text{Valid}(P_{i, \text{rank}}) \land \text{Valid}(P_{i, \text{mom}}) \land \text{Valid}(P_{i, \text{open}}) \land (\text{MedianTurnover}_{i, 30\text{d}} \ge \$1\text{M})$$
- **Portfolio Construction & Basket Sizing:**
  - Baskets are partitioned into quintiles ($N_{\text{quantiles}} = 5$) based on ranked trailing momentum $R_{i, t}^{\text{mom}}$ (`source-reported`).
  - Basket size: $k = \max(1, \lfloor N_{\text{eligible}} / 5 \rfloor)$ (`source-reported`).
  - Long leg: Top quintile ($k$ highest momentum assets), equal-weighted (`source-reported`).
  - Short leg: Bottom quintile ($k$ lowest momentum assets), equal-weighted (`source-reported`).
- **Holding Period & Exit Logic ($K$):**
  - **Specification 1 ($K=1$):** Exit at Monday 00:00:00 UTC open 7 calendar days following entry (`source-reported`).
  - **Specification 2 ($K=2$):** Exit at Monday 00:00:00 UTC open 14 calendar days following entry (`source-reported`). Non-overlapping cycles executed every 2 weeks (`source-reported`).
- **Dual-Phase Calendar for $J=2 / K=2$:**
  - **Phase A (Headline):** Fortnightly cohorts entering on weeks $0, 2, 4, \dots$ (`source-reported`).
  - **Phase B (Diagnostic):** Fortnightly cohorts entering on weeks $1, 3, 5, \dots$ (`source-reported`).
- **Missing Data & Forced Closure Rules:**
  - If Monday entry open is missing, the asset is excluded immediately; no substitution of subsequent bars is permitted (`source-reported`).
  - If Monday exit open is missing (delisting or trading halt), forced closure occurs at the last available close strictly prior to planned exit, recorded as `missing_exit` (`source-reported`).
  - Assets terminating at the end of the sample panel are recorded as `panel_end` (`source-reported`).
  - Zero forward-filling of missing data is strictly enforced across all matrices (`source-reported`).

## Required data

- **Instrument & Asset Class:** Binance USDⓈ-M perpetual futures (`futures/um`) contracts settled in USDT (`source-reported`).
- **Universe Coverage:** All 832 historical USDT-margined perpetual symbols available in the Binance Vision public archive from 2020-01-01 to 2026-07-31 (2,404 days) (`source-reported`).
- **Survivorship-Bias Controls:** Symbols are sourced from S3 prefixes (`futures/um/monthly/klines/`) rather than the live `/fapi/v1/exchangeInfo` endpoint. This captures 31 delisted contracts (including AERGO, AKRO, ANC, ANT, BTCST, BZRX, BTT) that would otherwise be silently lost, preventing survivorship bias in the short basket (`source-reported`).
- **Data Fields Required:**
  - Daily Open price (`open`) (`source-reported`).
  - Daily Close price (`close`) (`source-reported`).
  - Daily Quote Asset Volume (`quote_volume` in USDT) (`source-reported`).
  - 8-Hour Funding Rate payments (`funding_rate`) (`source-reported`).
- **Timezone & Aggregation:** Strictly UTC daily candles (00:00:00 to 23:59:59) (`source-reported`).
- **Integrity Validation:** Panel verified through five distinct audits:
  1. Shape symmetry between open and close matrices ($2,404 \times 832$; 612,421 non-empty cells each) (`source-reported`).
  2. Bitwise parity against raw zip archives (`source-reported`).
  3. Cell-for-cell NaN mask equivalence (`source-reported`).
  4. Forward-fill rejection test: Open-to-previous-close match rate is 42.5% (median difference 0.0079%), proving absence of synthetic forward-fill (`source-reported`).
  5. Zero-volume verification tracing static prices to frozen market sessions rather than ingestion errors (`source-reported`).

## Execution assumptions

- **Execution Mode:** Market taker orders executed at Monday 00:00:00 UTC open for both entry and exit (`source-reported`).
- **Exchange Fee Model:** Binance USDⓈ-M base retail tier (VIP 0, no BNB fee deduction): $0.0500\%$ per trade (`source-reported`).
- **Slippage Model:** Assumed flat $0.0500\%$ ($5$ bps) per trade on entry and exit (`source-reported` as an explicit modeling assumption; labeled `research-proposed` relative to dynamic order-book impact).
- **Total Transaction Cost per Leg:**
  $$\text{Cost}_{\text{leg}} = 2 \times (\text{Fee}_{\text{taker}} + \text{Slippage}) = 2 \times (0.0500\% + 0.0500\%) = 0.2000\% \quad (20\text{ bps})$$
- **Total Portfolio Friction:** $0.4000$ percentage points ($40$ bps) per rebalance across both long and short legs (`source-reported`).
  - For $J=1 / K=1$: $0.4000$ pp per week (`source-reported`).
  - For $J=2 / K=2$: $0.4000$ pp per 14-day cycle ($0.2000$ pp annualized weekly rate) (`source-reported`).
- **Borrow & Shorting Friction:** Symmetrical margin access via perpetual contracts; no cash borrow fee, but short positions are subject to 8-hour funding rate flows (`source-reported`).
- **Capital Capacity:** At the $\$1\text{M}$ median daily volume threshold, a $\$10,000$ individual position represents $1\%$ of daily turnover. For a basket of $\sim 100$ assets per leg, this supports a theoretical desk capacity of approximately $\$1,000,000$ per leg (`source-reported`).

## Evidence

### Source-reported

#### 1. Specification 1: $J=1 / K=1$ (Headline 7-Day / 7-Day, 338 Weeks: Feb 2020 – Jul 2026)

Evaluated across 338 independent weekly cohorts with an average active eligible universe of 175 perpetual contracts (ranging from 10 to 544 assets) (`source-reported`):

| Metric | Long Leg (Top 20%) | Short Leg (Bottom 20%) | Gross Spread (L - S) | Net Spread (After 40 bps Costs) |
| :--- | :--- | :--- | :--- | :--- |
| **Mean Weekly Return** | $+1.055\%$ | $+0.482\%$ | **$+0.573\%$** | **$+0.173\%$** |
| **Median Weekly Return** | $-1.542\%$ | $-1.000\%$ | **$+0.413\%$** | **$+0.013\%$** |
| **Standard Deviation** | — | — | $6.942\text{ pp}$ | $6.942\text{ pp}$ |
| **Positive Weeks Share** | — | — | $52.7\%$ ($178/338$) | **$50.0\%$** ($169/338$) |
| **Bootstrap 95% CI** | — | — | $[-0.147\%, +1.340\%]$ | **$[-0.551\%, +0.941\%]$** |
| **Sign-Flip Test ($p$-value)** | — | — | $p = 0.1344$ | **$p = 0.6526$** |
| **Within-Week Permutation** | — | — | **$p = 0.0352$** | **$p = 0.8040$** |

- **Cost Consumption:** Operational taker friction ($0.400$ pp) consumes **$69.8\%$** of the gross spread (`source-reported`).
- **Statistical Significance:** While within-week permutation is significant gross ($p=0.035$), all three tests fail net of costs. The net median return is $+0.013\%$, and the share of profitable weeks drops to exactly $50.0\%$ (`source-reported`).
- **Funding Rate Impact Limitation:** Binance funding archives cover only $7.7\%$ of positions and **zero weeks** with full basket coverage. On covered positions ($2,323$ asset-weeks), net funding contributed $+0.0721$ pp/week directionally, which is second-order relative to the $0.400$ pp fee barrier (`source-reported`).
- **Outlier Sensitivity (Jackknife):** Dropping the top-5 extreme weeks (spreads up to $+48.1\%$ and $-24.5\%$) reduces gross spread to $+0.250\%$, which turns net return negative ($-0.150\%/\text{week}$) (`source-reported`).

#### 2. Specification 2: $J=2 / K=2$ (Pre-Registered Fortnightly Alternative, 169 Periods)

Evaluated on non-overlapping 14-day holding periods with rebalancing costs of $0.400$ pp per period ($0.200$ pp/week equivalent) (`source-reported`):

| Series | Periods | Mean / Period | Median / Period | Periods $> 0$ | Bootstrap 95% CI | Sign-Flip ($p$) | Permutation ($p$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gross Phase A (Headline)** | 169 | $+1.258\%$ | $+0.471\%$ | $50.3\%$ | $[-0.342\%, +2.926\%]$ | $p = 0.1252$ | N/A |
| **Net Phase A (Headline)** | 169 | **$+0.858\%$** | $+0.071\%$ | $50.3\%$ | $[-0.722\%, +2.501\%]$ | $p = 0.3083$ | $p = 0.2909$ |
| **Gross Phase B (Diagnostic)** | 169 | $+0.249\%$ | $-0.253\%$ | $46.7\%$ | $[-1.327\%, +1.819\%]$ | $p = 0.7602$ | N/A |
| **Net Phase B (Diagnostic)** | 169 | **$-0.151\%$** | $-0.653\%$ | $44.4\%$ | $[-1.720\%, +1.405\%]$ | $p = 0.8536$ | $p = 0.8522$ |

- **Decisive Phase Instability:** Phase A ($+0.858\%$) and Phase B ($-0.151\%$) diverge by **$1.009$ percentage points** and reverse sign based entirely on which Monday the fortnightly cycle initiates (`source-reported`).
- Neither phase passes any of the three significance tests net of costs (`source-reported`).

#### 3. Exploratory Post-Hoc Liquidity Sort (5 Turnover Buckets, 305 Weeks)

Dividing the universe into 5 dynamic turnover quintiles per week (`source-reported`):

| Liquidity Group | Median Turnover | Gross Mean / Week | Gross Median / Week | Weeks $> 0$ | Bootstrap 95% CI | Permutation ($p$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **L1 (Lowest Volume)** | $\$6.1\text{M}$ | $+0.150\%$ | $-0.637\%$ | $45.6\%$ | $[-1.328\%, +1.865\%]$ | $p = 0.8308$ |
| **L2** | $\$11.7\text{M}$ | **$-1.193\%$** | $-0.982\%$ | $41.3\%$ | $[-2.222\%, -0.193\%]$ | **$p = 0.0464$ (Reversal)** |
| **L3** | $\$20.1\text{M}$ | $-0.519\%$ | $-0.227\%$ | $47.9\%$ | $[-1.976\%, +0.832\%]$ | $p = 0.4689$ |
| **L4** | $\$44.7\text{M}$ | $+1.414\%$ | $-0.018\%$ | $49.8\%$ | $[+0.112\%, +2.825\%]$ | $p = 0.0188$ |
| **L5 (Highest Volume)**| $\$181.8\text{M}$| **$+1.638\%$** | $+0.392\%$ | $55.1\%$ | $[+0.404\%, +2.877\%]$ | **$p = 0.0070$** |

- **Non-Monotonicity & Anomaly:** While L5 demonstrates positive gross momentum ($+1.638\%/\text{week}$), the relationship is non-monotonic (L2 exhibits statistically significant reversal at $-1.193\%/\text{week}$), and groups L1 and L4 exhibit negative median returns despite positive means, reflecting skewness rather than uniform drift (`source-reported`).

### Independently reproduced

- Not independently reproduced in this research stack. Primary source codebase and replication outputs verified from immutable GitHub commit `dd4399a7218ae15e52e7dc342ee89d345ea74d14`.

### Negative evidence

1. **Transaction Cost Extinction:** The academic momentum factor fails to survive realistic exchange taker fees ($0.05\%$) and slippage ($0.05\%$), losing 70% of gross return and yielding an insignificant net spread ($p = 0.65$ to $0.80$) (`source-reported`).
2. **Phase Fragility:** Shifting the rebalance day by one week flips the net return from positive ($+0.858\%$) to negative ($-0.151\%$), proving lack of structural stability (`source-reported`).
3. **Infinite Variance / Heavy Tails:** Realized momentum returns conform to power-law tails with $\alpha < 3$ (Grobys et al. 2025), invalidating classical $t$-tests and Sharpe ratio comparisons (`source-reported`).
4. **Historical Practitioner Failure:** Starkiller Capital's out-of-sample live fund implementation lost $-2.35\%$ annualized during 2021–2022 and failed at costs exceeding $125$ bps (Drogen et al. 2023) (`source-reported`).
5. **Literature Non-Replications:** Grobys & Sapkota (2019) find momentum insignificant on 143 coins (2014–2018); Dobrynskaya (2021) finds $J=1/K=1$ insignificant ($t=0.80$) on CoinMarketCap data (`source-reported`).

## Falsification plan

To disconfirm this negative verdict and establish an executable cross-sectional momentum edge on crypto perpetuals, a candidate implementation must pass all four pre-registered criteria:

1. **Net Taker Survival Hurdle:**
   - *Test:* Run full-history walk-forward backtest on Binance or Bybit perpetuals accounting for verified historical taker fees ($0.05\%$) and minimum $5$ bps slippage (`research-proposed`).
   - *Metric:* Annualized net Sharpe ratio $\ge 1.0$ and 95% non-parametric bootstrap lower bound $> 0.0$ bps (`research-defined falsification threshold`).
   - *Failure Action:* Reject candidate if net spread covers zero or costs exceed $50\%$ of gross spread (`research-defined falsification threshold`).
2. **Phase Invariance Test:**
   - *Test:* For any rebalance cadence $K \ge 2$, evaluate all $K$ non-overlapping sub-phases across the entire multi-year panel (`research-proposed`).
   - *Metric:* Sign consistency across all phases, with cross-phase spread difference $< 0.25$ pp (`research-defined falsification threshold`).
   - *Failure Action:* Reject strategy if changing the starting day flips the sign of net return (`research-defined falsification threshold`).
3. **Passive Execution & Adverse Selection Audit:**
   - *Test:* Simulate passive post-only maker execution for rebalancing instead of aggressive market orders (`research-proposed`).
   - *Metric:* Documented fill rate $> 85\%$ within 60 minutes of week open without adverse price movement exceeding the maker rebate ($0.02\%$) (`research-defined falsification threshold`).
   - *Failure Action:* Retain taker cost assumptions if unfillable quote decay exceeds 2 bps (`research-defined falsification threshold`).
4. **Liquidity Monotonicity Holdout Test:**
   - *Test:* Test the post-hoc L5 mega-cap momentum hypothesis on out-of-sample holdout data (August 2026 onwards) (`research-proposed`).
   - *Metric:* Spearman rank correlation between turnover bucket and net spread $> 0.70$, with zero buckets exhibiting statistically significant reversal (`research-defined falsification threshold`).
   - *Failure Action:* Reject turnover-gated momentum if L5 net spread drops below 20 bps/week (`research-defined falsification threshold`).

## Crypto portability

- **Binance USDⓈ-M Perpetuals:** Direct (`source-reported`). The primary source evaluates this exact venue and instrument class across 832 historical symbols.
- **Other Centralized Derivatives (Bybit, OKX, Bitget):** Adapted / unproven (`research-proposed`). Funding mechanisms and fee structures are comparable, but tick sizes, delisting rules, and contract specifications differ.
- **DEX Perpetuals (Hyperliquid, dYdX):** Adapted / unproven (`research-proposed`). Maker rebate structures and gas-less or low-latency L1 environments provide lower fees, but liquidity profiles are concentrated in the top 20 tokens rather than the broad 175-token universe required for quintile spreads.
- **Portability Boundary:** Symmetrical shorting on perpetual futures eliminates physical borrow fees, but replaces them with 8-hour funding rate variance and mandatory rebalance crossing costs. Porting traditional equity momentum without accounting for crypto taker fees is fundamentally invalid.

## Limitations

- **Funding Rate Data Truncation:** Public funding archives covered only $7.7\%$ of positions and zero full-basket weeks, leaving the exact historical net funding contribution unmeasured (`source-reported`).
- **Equal-Weighted vs Value-Weighted Divergence:** The primary source uses equal-weighted baskets, whereas canonical academic literature (Liu et al. 2022) utilizes value-weighted quintiles (`source-reported`).
- **Static Slippage Assumption:** Slippage is modeled as a fixed 5 bps haircut rather than reconstructed from dynamic historical L2 order book depth (`source-reported`).
- **Retail Fee Baseline:** Results reflect VIP 0 taker fees ($0.05\%$). Institutional desks with VIP 9 taker fees ($0.015\%$) or maker fee rebates would experience lower cost drag, though execution risk remains (`source-reported`).

## Implementation status

- `not-implemented`.
- This research record reflects external empirical replication and falsification from `Silent47boryara/searching-for-edge` and SSRN 7404139.
- No strategy code has been implemented in `nautilus-quant-system`, PyBroker, or NautilusTrader.

## Adoption boundary

- `research-only`.
- Strategy adoption is `not-approved`.
- Approval scope is `research-only`.
- Presence of this record serves as negative evidence and an operational cost warning; it does not authorize paper, testnet, or live deployment.

## Related Wiki records

- `[[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]`
- `[[bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13]]`
- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]`
- `[[crypto-perp-vol-scaled-cross-sectional-momentum-factor-2026-09-12]]`

## Sources

- Arefev, Oleg. (2026). *"Cross-Sectional Momentum in Cryptocurrency: A Net-of-Costs Replication on Tradable Binance Perpetuals (2020-2026)"*. SSRN Working Paper 7404139. Stable URL: `https://ssrn.com/abstract=7404139` · DOI: `https://doi.org/10.2139/ssrn.7404139`.
- Arefev, Oleg (`Silent47boryara`). *Searching for Edge: Independent Research into Systematic Crypto Trading & Market Microstructure*. GitHub repository `https://github.com/Silent47boryara/searching-for-edge`, immutable commit `dd4399a7218ae15e52e7dc342ee89d345ea74d14` (September 12, 2026).
  - Path: `02-momentum/momentum-evidence-from-binance-replication.md`
  - Path: `02-momentum/replication/step3_full_history_spread/RESULT.md`
  - Path: `02-momentum/replication/step3_full_history_spread/RESULT_net_of_costs.md`
  - Path: `02-momentum/replication/step3_full_history_spread/RESULT_liquidity_exploratory.md`
  - Path: `02-momentum/replication/step4_j2k2_spread/RESULT.md`
  - Path: `02-momentum/replication/step3_full_history_spread/full_history_spread.py`
  - Path: `02-momentum/replication/step3_full_history_spread/net_of_costs.py`
  - Path: `02-momentum/replication/step4_j2k2_spread/j2k2_spread.py`
- Liu, Yukun, Aleh Tsyvinski, and Xi Wu. (2022). *"Common Risk Factors in Cryptocurrency"*. *The Journal of Finance*, 77(6), 1133–1173. DOI: `https://doi.org/10.1111/jofi.13119`.
- Liu, Yukun. (2019). *"Common Risk Factors in Cryptocurrency"*. Conference Presentation Slides, November 2019.
- Drogen, Leigh, Corey Hoffstein, and Kevin Otte. (2023). *"Cross-sectional Momentum in Cryptocurrency Markets"*. Starkiller Capital, SSRN Working Paper 4322637. DOI: `https://doi.org/10.2139/ssrn.4322637`.
- Grobys, Klaus, James W. Kolari, Niranjan Sapkota, Syed Jawad Hussain Shahzad, and Janne Äijö. (2025). *"Cryptocurrency momentum has (not) its moments"*. *Financial Markets and Portfolio Management*, 39, 443–476. DOI: `https://doi.org/10.1007/s11156-024-01256-4`.
- Dobrynskaya, Victoria. (2021). *"Cryptocurrency Momentum and Reversal"*. National Research University Higher School of Economics (HSE) Working Paper.
- Li, Jiasheng, and Yanfeng Zhu. (2024). *"A LASSO Type Factor Model in Cryptocurrency"*. Central University of Finance and Economics Working Paper (August 2024).
- Grobys, Klaus, and Niranjan Sapkota. (2019). *"Cryptocurrencies and momentum"*. *Economics Letters*, 180, 6–10. DOI: `https://doi.org/10.1016/j.econlet.2019.03.029`.
