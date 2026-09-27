---
schema: strategy-research-record-v1
title: "Crypto Day–Night Session-Partitioned Lagged Reversal/Drift Rules with Model-Search-Adjusted Inference (BTC/ETH, Kraken Hourly)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - ethereum
  - intraday
  - session-structure
  - momentum-reversal
  - model-selection
  - spot
status: research-only
confidence: medium
source_as_of: 2026-09-06
sources:
  - "https://doi.org/10.3390/jrfm19090692 (Zhefan Wu, Eugene Pinsky, 'On the Performance of Lagged Momentum and Reversal Strategies Across Daytime and Overnight Sessions in Bitcoin and Ethereum Cryptocurrencies', Journal of Risk and Financial Management 2026, 19(9), 692, MDPI, published online 2026-09-06, CC BY 4.0)"
  - "https://www.mdpi.com/1911-8074/19/9/692 (full-text article page, read end to end in a browser session 2026-09-27; a plain curl fetch returned MDPI 'Access Denied', so the browser rendering was the read path)"
  - "https://github.com/wzf01195010-png/Crypto-day-night-effects at full commit 5693993e108f2b3668bd21b1dd36ae31f79d8fcd (MIT, HEAD as of 2026-09-27; replication code and paper_outputs CSVs read at that commit)"
  - "https://raw.githubusercontent.com/wzf01195010-png/Crypto-day-night-effects/5693993e108f2b3668bd21b1dd36ae31f79d8fcd/paper_outputs/tables/preferred_vs_buyhold_tests.csv (4,196 bytes, downloaded 2026-09-27; companion files conditional_predictability_tests.csv 2,968 B, cutoff_strategy_best_by_cutoff.csv 2,260 B, etf_2025_metrics.csv 1,711 B, btc_eth_all_metrics.csv 486,841 B all downloaded and read)"
  - "https://api.crossref.org/works/10.3390/jrfm19090692 (metadata check 2026-09-27: type journal-article, publisher MDPI AG, volume 19, issue 9, page 692, published-online 2026-09-06, license CC BY 4.0 for version of record, no relation/update entry)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Day–Night Session-Partitioned Lagged Reversal/Drift Rules with Model-Search-Adjusted Inference (BTC/ETH, Kraken Hourly)

## Provenance

**Primary source.** Zhefan Wu (Department of Mathematical Finance, Questrom School of Business, Boston University) and Eugene Pinsky (Department of Computer Science, Metropolitan College, Boston University), listed as equal contributors, *"On the Performance of Lagged Momentum and Reversal Strategies Across Daytime and Overnight Sessions in Bitcoin and Ethereum Cryptocurrencies"*, *Journal of Risk and Financial Management* (MDPI AG), 2026, **19(9), 692**, DOI `10.3390/jrfm19090692`.

- **Version/date (source-reported on the article page):** Submission 19 August 2026; Revised 3 September 2026; Accepted 4 September 2026; **Published 6 September 2026**. Crossref reports `published-online 2026-09-06`, record created `2026-09-07T12:12:25Z`, `type: journal-article`, `publisher: MDPI AG`, `volume 19 / issue 9 / page 692`, license `https://creativecommons.org/licenses/by/4.0/` for the version of record, and an empty `relation` object (no correction, retraction, or update linked as of 2026-09-27). The landing page shows an **Open Access** badge, Academic Editor **Thanasis Stengos**, and membership in the Special Issue *"Asset Pricing and Cryptocurrencies"*.
- **Publication status:** peer-reviewed journal article (not a preprint). Article views shown on the page at read time: 625.
- **Sample period (source-reported, §3.1):** hourly BTCUSD and ETHUSD from **00:00 UTC 1 January 2016 through 23:00 UTC 31 December 2025** — 3,652 calendar days, **87,672 hourly observations per asset**, validated with no missing hours, duplicate timestamps, timestamp mismatches, or non-positive closes.
- **Universe / venue (source-reported, §3.1):** two spot instruments, BTC/USD and ETH/USD, **Kraken official historical market-data archive only**, hourly closes in UTC; no cross-exchange merge and no interpolation. An exploratory extension uses the US ETFs **IBIT** and **ETHA** over the 2025 evaluation year.
- **Transaction-cost treatment (source-reported, §4.3–§4.4):** the cutoff-and-rule **selection stage is run at zero cost**; proportional costs of **0, 1 and 2 basis points per unit of turnover** are applied afterwards (turnover 1 for cash↔±1, 2 for long↔short). §4.4 states explicitly that the calculation **does not** model bid–ask spread, boundary slippage, market impact, exchange fees, short-borrow cost, perpetual-futures funding, or taxes. §6.3 gives linear-extrapolated one-way break-even costs of **≈2.1 bps (BTC)** and **≈5.6 bps (ETH)**.
- **Replication package (source-reported, Data Availability Statement):** `https://github.com/wzf01195010-png/Crypto-day-night-effects` (accessed 19 August 2026 per the paper). Pinned here at full commit **`5693993e108f2b3668bd21b1dd36ae31f79d8fcd`** (commit date 2026-08-19T17:44:20Z, merge of PR #2; the tree API at that commit returned 23 blobs, `truncated: false`). Read at that commit: `README.md` (4,545 B), `paper_outputs/README.md` (1,513 B), `LICENSE` (MIT, 1,072 B, "Copyright (c) 2026 wzf01195010-png"), `btc_eth_backtest.py`, `cutoff_strategy_analysis.py`, `statistical_tests.py` listing, and the pinned `paper_outputs/tables/*.csv` files (byte sizes matched the tree API exactly).
- **Data-availability limit (source-reported, README):** raw hourly CSVs (`BTCUSD_1h_2016_2025.csv`, `ETHUSD_1h_2016_2025.csv`, `IBIT_1h_2024_07_05_to_2026_07_08.csv`, `ETHA_1h_2024_07_23_to_2026_07_06.csv`) are **not committed**; the README states that raw BTC/ETH data must be re-obtained from Kraken and that "an older Bitstamp or third-party file must not be relabeled as Kraken data". Paper outputs were generated **19 August 2026**; `outputs/` is git-ignored.
- **Read path:** `curl` against `https://www.mdpi.com/1911-8074/19/9/692` returned an MDPI *Access Denied* page (398 bytes), so the full text was read through a browser session on 2026-09-27; Crossref and the GitHub API were used as independent metadata checks.

**Repository-wide source-identity dedup (deterministic, pre-write, 2026-09-27).** `rg --hidden -g '!.git'` over **2,614 files** (including `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv`) for six identity patterns — `jrfm19090692`, `10.3390/jrfm19090692`, `Daytime and Overnight Sessions`, `Crypto-day-night-effects`, `wzf01195010`, `Zhefan Wu`, `Eugene Pinsky` — returned **0 matching files**; `coverage_manifest.csv` (5,808 lines) returned 0 hits for `jrfm19090692` and for the exact title. A Wiki Brain `kb_search` for *"cryptocurrency intraday session momentum reversal time-of-day predictability"* returned **0 pages**.

**Four-axis distinction against the nearest existing records (source identity + mechanism).**

- `crypto-intraday-utc-return-seasonality-tea-time-2026-09-03` — Brauneis/Mestel/Theissen (RQFA 2025) documents descriptive hourly time-of-day patterns across 38 exchanges with **no trading rule**; this record is a searched session-partition *trading rule* with sign-based lagged positions and model-search inference.
- `bitcoin-intraday-time-series-momentum-volume-session-2026-08-31` — Shen/Urquhart/Wang (Financial Review 2022) uses **volume-defined** intraday sessions and time-series momentum; here the partition is a **clock-time 12 h/12 h split searched over 12 UTC boundaries**, and the winning BTC rule is **reversal**, not momentum.
- `crypto-quarter-hour-algorithmic-order-flow-predictability-2026-09-14` and `crypto-quarter-hour-opening-order-imbalance-medium-horizon-2026-08-31` — quarter-hour **order-imbalance** microstructure predictability; different mechanism (order-flow), different horizon (minutes/hours), different signal construction.
- `crypto-weekday-hour-localized-return-anomaly-2026-09-04` — calendar weekday×hour anomaly mapping (descriptive localization), not a paired-session lagged rule.
- `fmz-overnight-range-fib62-lost-momentum-532865-2026-09-20` — FX overnight-range Fibonacci entry (different market type and mechanism).
- `crypto-momentum-opening-price-cycle-trough-peak-arbitrage-2026-09-18` (arXiv 2609.18149) — cycle/opening-price arbitrage framing, not session-lagged conditional reversal.

Mechanism, signal construction, and material data dependency all differ from the above; the source identity (MDPI DOI + pinned MIT repo) is unique in the repository.

## Economic mechanism

### Source-reported

The authors argue that although crypto trades continuously, participation, liquidity and information arrival are not uniform over the 24 h cycle, so a full-day return may superimpose several return processes. Dividing the day into two complementary 12 h sessions and applying simple lagged rules therefore can expose predictability that daily returns hide. The paper is explicit that the contribution is **not** a new momentum/reversal concept but the joint organization of familiar rules with session definitions, return-source tests and model-search adjustment (§1, §2).

Reported structure: **BTC**'s full-sample maximum is *conditional reversal in both sessions* under an **08:00 UTC** daytime start; **ETH** combines an **unconditional positive nighttime drift** with **daytime reversal** under a **05:00 UTC** daytime start (§5.1, §5.4). The authors note the 05:00 and 08:00 boundaries sit near the late-Asia/early-Europe activity transition, but state this interpretation is *"plausible but not causal"* and that volume, liquidity, order-flow and investor-mix mechanisms cannot be separated by the price-only design (§6.3).

### Research interpretation

Hypothesized mechanism (falsifiable terms): **session-local overreaction with an asset-specific overnight drift component.**

- Regime/partition: two complementary 12 h UTC sessions per trading date (daytime start `h` searched over 12 non-redundant hours).
- Primary signal: the **sign of the same-session return observed one session earlier** (Reversal = trade against it, Momentum = trade with it). Daytime position uses the *preceding daytime* return, never the preceding nighttime return (§4.1).
- Secondary component: ETH's nighttime position is an unconditional **Long**, i.e. a positive 12 h drift rather than a conditional response.
- Economic channels consistent with the pattern: short-horizon overreaction to session-local news/flow (reversal), and regional participation/attention drift across the Asia–Europe hand-over (ETH nighttime long). Competing non-alpha explanations the source itself lists: liquidity provision, order-flow imbalance, volatility clustering, changing regional investor mix (§6.3).

Component roles are separable, so an ablation can attribute any edge: (i) partition choice, (ii) sign-conditioned reversal, (iii) unconditional night long, (iv) pure in-sample selection luck. The paper's own SPA test and holdout exercise are evidence that (iv) is a live alternative, not a rhetorical one.

## Signal

All items below are `source-reported` unless marked `research-proposed`.

- **Formation timestamp / tradability.** Session returns are compounded from hourly Kraken **closes** (§3.2). For trading date `t` and daytime start `h`: the nighttime session runs from hour `h+12` on the preceding calendar date to hour `h` on `t`; the daytime session runs from `h` to `h+12` on `t` (§3.3, Figure 1). The current session's position is fixed **before** the session begins, from the previous realization of the **same** session type. Ties/undefined lags (zero lagged return, first session) → **Cash** (§4.1). All times UTC; DST-free by construction.
- **Lookback.** Exactly **one prior realization of the same session** (12 h lag). No averaging window, no warm-up beyond the first session, endpoints assigned by hour labels modulo 24. Only dates containing all 12 hourly observations in **both** sessions are retained → 3,652 complete night–day cycles for every symmetric cutoff (§3.2).
- **Rule set and search.** Five positions per session — Cash (0), Long (+1), Short (−1), Momentum (sign of lagged same-session return), Reversal (opposite sign of that lag) — combined as ordered night/day pairs → **25 strategies per cutoff**, over **12 non-redundant daytime starts** (`h = 00:00 … 11:00` UTC; `h+12` duplicates the same boundaries with swapped labels) → **300 cutoff–strategy combinations per asset** (§4.1–§4.3). Cash/Cash is kept as a normalization check; 24 active strategies enter the main comparison.
- **Selection rule (in-sample).** For each asset, choose `(h, strategy)` jointly by **maximum zero-cost terminal wealth** over the full 2016–2025 sample, initial wealth 100 (§4.3). The paper states the result is an in-sample optimum *"mechanically subject to model-selection bias"*.
- **Selected rules.** **BTC:** Reversal/Reversal with daytime `08:00–20:00` UTC (night `20:00–08:00`). **ETH:** Long/Reversal with daytime `05:00–17:00` UTC (night `17:00–05:00`) (§5.1).
- **Long entry / short entry.** Long = position +1 for the whole session after a positive lagged same-session return (or, for ETH night, unconditionally); Short = position −1 after a negative lagged same-session return (BTC night and day, ETH day). No leverage: admissible positions are `{−1, 0, +1}` (§4.1).
- **Exit / precedence.** There is no separate stop or take-profit: the position is re-evaluated at each session boundary, and the new session's rule (or Cash on an undefined lag) supersedes the previous position. Two sessions per trading date are combined into one daily strategy return (§4.4).
- **Holding period.** 12 h per session, two sessions per day, 3,652 dates / 7,304 sessions; positions may repeat indefinitely while the sign pattern persists.
- **Turnover / costs.** Turnover `= |Δposition|` charged at each change: cash↔±1 = 1, long↔short = 2 (§4.4). Cost scenarios 0 / 1 / 2 bps per unit of turnover, applied **after** selection.
- **Parameters.** Cutoff `h`, rule pair, cost rate, initial wealth 100, √365 annualization, risk-free rate 0 (§4.5). Cutoff and rule are **tuned in-sample**; the cost rates are the authors' chosen sensitivity grid; everything is printed in the source.
- **Underspecified.** Shorting mechanics (spot margin vs futures vs borrow), the exact price used at the boundary within the hourly bar, whether a position change is executed at the boundary close or the next bar, and any re-entry/hysteresis rule — **not stated in source**. `research-proposed` additions used later in this record (e.g. multi-venue replication, rolling re-selection, exposure-matched benchmarks) are labelled as such.

## Required data

- **Instrument / universe:** BTC/USD and ETH/USD spot; two assets only; no market-cap or liquidity screen (the universe is the pair of majors on one venue).
- **Venue / market type:** Kraken spot, hourly bars, official historical market-data archive; **single venue** (the paper flags cross-exchange robustness as future work, §6.3).
- **Timeframe:** 1 h bars, aggregated into two 12 h sessions per UTC date.
- **Fields used:** hourly `close` (strategy and signals); source files contain OHLC + volume but **volume is not used** in any rule. ETF extension additionally uses `open`, `high`, `low`, `volume`, `adj_close` (repo README).
- **Point-in-time / availability:** pure price-lag construction, so no publication lag; all inputs are observable before the session opens. Train/test boundary: full-sample selection vs the 2016–2020 → 2021–2025 chronological holdout (§4.6).
- **Timestamp:** UTC, cross-checked against the Unix timestamp in each file; no DST.
- **Missing data:** the source reports zero missing/duplicate hours after validation (§3.1); no imputation described. Raw files are withheld from the repository, so this claim is **not independently verified** (`data gap`).
- **Funding / fee / spread needs:** not requested by the source's cost model; for any tradable version, funding, spread and borrow would have to be added (`data gap`).

## Execution assumptions

- **Signal-to-order:** position decided before the session starts; **execution assumed at the observed session-boundary price** (§6.3) — the paper notes slippage is "especially relevant" because of this.
- **Order type / fill model:** not stated; a boundary-crossing market order at the closing price of the boundary hour is implied (`underspecified`).
- **Latency / partial fills / failures:** not modelled (`data gap`).
- **Fees / spread / slippage / impact:** only the proportional 0/1/2 bps-per-turnover scenarios; **spread, slippage, impact, exchange fees, borrow, funding and taxes are explicitly excluded by the source (§4.4)** — never read as zero.
- **Capacity:** not modelled. Replication turnover for the selected rules: **BTC 7,485 units of turnover over 3,743 position changes and 7,304 sessions; ETH 7,331 units over 3,668 changes** (`btc_eth_all_metrics.csv`, 0 bps rows) — i.e. roughly one unit of turnover per session (`research interpretation`, our arithmetic on the pinned file).
- **Leverage / margin / shorting:** no leverage (positions in `{−1,0,+1}`); short legs require a margin/derivatives account whose cost and feasibility are not modelled (`underspecified`).
- **Funding:** not applicable to the source's spot design; a perpetual port would need it (`data gap`).
- **Benchmark exposure:** buy-and-hold is continuously long while the rules can be long/short/cash, so the comparison is **not exposure matched** (§6.3, source-reported).

## Evidence

### Source-reported

Every figure below is `source-reported` from Wu & Pinsky (2026), DOI `10.3390/jrfm19090692`, cross-checked against the paper's own pinned replication CSVs at commit `5693993e…`. None has been independently reproduced.

**Terminal wealth (initial 100, Table 8 + `preferred_vs_buyhold_tests.csv`), full sample 2016–2025, 3,652 observations:**

| Asset / rule | 0 bps | 1 bps | 2 bps | Buy-and-hold 0 / 1 / 2 bps | Wealth ratio 0 / 1 / 2 bps |
|---|---|---|---|---|---|
| BTC Reversal/Reversal @08:00 | 95,015.46 | 44,946.13 | 21,258.15 | 20,216.11 / 20,214.09 / 20,212.07 | 4.70 / 2.22 / 1.05 |
| ETH Long/Reversal @05:00 | 18,443,599.11 | 8,859,976.25 | 4,255,550.63 | 319,710.72 / 319,678.75 / 319,646.78 | 57.69 / 27.72 / 13.31 |

Paper §5.2 additionally reports CAGR ≈ **98.5%** vs **70.0%** (BTC, zero cost) and ≈ **236.2%** vs **124.1%** (ETH, zero cost), and explicitly warns the ETH figure is a compounding artefact of 3,652 daily observations that "should not be interpreted as evidence that capital of arbitrary size could be scaled through the same trades".

**Risk at zero cost (paper Table 9 reports MDD, Sharpe and annualized volatility at 0 bps; the HTML rendering exposes those cells only as table images, so the numbers below are read from the pinned replication file `paper_outputs/tables/btc_eth_all_metrics.csv`, rows at the selected cutoffs):**

| Row (cutoff, 0 bps) | Final wealth | Sharpe | Full-period MDD | Avg. annual MDD | Ann. daily vol | Trades / turnover |
|---|---|---|---|---|---|---|
| BTC Reversal/Reversal @08 | 95,015.46 | 1.3529 | −0.7506 | −0.4200 | 0.6746 | 3,743 / 7,485 |
| BTC buy-and-hold (Night Long/Day Long) @08 | 20,216.11 | 1.1270 | −0.8359 | −0.4559 | 0.6719 | 1 / 1 |
| ETH Long/Reversal @05 | 18,443,599.11 | 1.7468 | −0.7302 | −0.4981 | 0.9490 | 3,668 / 7,331 |
| ETH buy-and-hold @05 | 319,710.72 | 1.3192 | −0.9399 | −0.6143 | 0.9531 | 1 / 1 |

Sharpe is computed on daily net returns with **risk-free = 0** and annualized with √365 (§4.5). The paper's §5.3 prose matches this ordering (higher Sharpe, shallower drawdown, roughly unchanged volatility for BTC; lower drawdown and higher Sharpe with slightly lower volatility for ETH).

**Conditional predictability (Table 10; identical values in `conditional_predictability_tests.csv`), stationary block bootstrap, 5,000 replications, expected block length 7 days, Holm-adjusted:**

- BTC night reversal contrast **23.89 bps/session**, 95% CI [8.33, 40.16], raw p = 0.00260, Holm p = 0.00260.
- BTC day reversal contrast **27.71 bps**, CI [11.25, 43.76], raw p = 0.000800, Holm p = 0.00160.
- ETH day reversal contrast **42.79 bps**, CI [21.66, 64.85], raw p = 0.000600, Holm p = 0.000600.
- ETH night unconditional mean **24.15 bps**, CI [12.60, 36.40], raw p = 0.000200, Holm p = 0.000400.
- Subperiods (2016–2020 / 2021–2025): BTC night 20.54 (Holm p = 0.120, **ns**) / 27.27 (0.0132); BTC day 34.27 (0.0208) / 22.72 (0.0304); ETH day 39.98 (0.0204) / 45.68 (0.00320); ETH night 40.93 (0.00120) / **7.37 (Holm p = 0.259, ns)**.

**Preferred rule vs buy-and-hold (Table 11; `preferred_vs_buyhold_tests.csv`), mean daily log-return differential:**

- BTC: **4.24 bps** (0 bps) → 2.19 (1 bps) → **0.14 bps** (2 bps); 95% CIs [−13.85, 23.00], [−15.92, 20.94], [−17.99, 18.92]; raw p = 0.656 / 0.816 / 0.989; **Holm p = 1.0 at every cost**.
- ETH: **11.10 bps** → 9.10 → **7.09 bps**; CIs [−4.80, 26.07], [−6.87, 24.10], [−8.90, 22.13]; raw p = 0.166 / 0.250 / 0.374; **Holm p = 0.498 / 0.500 / 0.500**; every `significance_*` flag in the CSV is `False`.
- Subperiod wealth ratios (Table 11 / CSV): BTC 2016–2020 **0.375 / 0.260 / 0.180**, BTC 2021–2025 **12.64 / 8.64 / 5.90**; ETH 2016–2020 **4.30 / 2.98 / 2.07**, ETH 2021–2025 **13.53 / 9.36 / 6.48**.

**Model-search-adjusted inference (Table 12, §5.4):** Hansen's SPA test over all 300 cutoff–strategy combinations, benchmark = buy-and-hold, performance = daily log-return differential, 5,000 stationary-bootstrap replications, block length 7 days: consistent SPA p-values **0.899–0.996 for BTC** and **0.656–0.771 for ETH** at every cost level → **the null of no superior model is never rejected**.

**Chronological holdout (Table 13, §6.2):** selection on 2016–2020 only, evaluation on 2021–2025. **BTC** selects **Momentum/Long with an 11:00 UTC daytime start** (not the full-sample Reversal/Reversal@08:00); that frozen rule **loses 29.1% before costs** in 2021–2025 and reaches only **23.6% of buy-and-hold wealth**, worse with costs. **ETH** independently re-selects the same **05:00 Long/Reversal** rule and stays above buy-and-hold at 0, 1 and 2 bps.

**Subperiod matrices (Appendix Tables A1–A2, §6.1):** BTC Reversal/Reversal 100 → **2,511** (0 bps) and **1,204** (2 bps) in 2016–2020 vs buy-and-hold **6,691 / 6,689**; 100 → **3,820 / 1,783** in 2021–2025 vs **302**. ETH Long/Reversal 100 → **336,367 / 162,172** in 2016–2020 vs **78,259 / 78,243**; → **5,529 / 2,646** in 2021–2025 vs **409 / 408**.

**Cutoff search surface (§5.1 and `cutoff_strategy_best_by_cutoff.csv`):** BTC best-by-cutoff — `h=5` 61,773 (Night Long/Day Reversal), `h=7` 31,648 (Night Reversal/Day Long), **`h=8` 95,015**, `h=9` 20,226 and `h=10` 20,223 where the **best strategy is buy-and-hold itself** (excess −51.3 and −53.6). ETH best-by-cutoff — `h=3` 557,272, **`h=5` 18,443,599**, `h=6` 6,420,362, `h=7` 828,827, `h=8` 5,287,829, with buy-and-hold the winner at `h=0,1,2,4,9,10,11`.

**Exploratory ETF transfer (§6.4, Tables 14–15, `etf_2025_metrics.csv`, 250 trading days / 500 sessions in 2025):** IBIT with the transferred Reversal/Reversal rule — final wealth **194.53** (0 bps), 184.66 (1 bp), 175.28 (2 bps) vs buy-and-hold **93.62 / 93.61 / 93.60**; Sharpe **1.659 / 1.547 / 1.434** vs **0.053 / 0.053 / 0.052**; MDD −0.235 vs −0.334. ETHA with Long/Reversal — **356.97 / 340.55 / 324.88** vs **88.77 / 88.76 / 88.75**; Sharpe **2.094 / 2.031 / 1.967** vs **0.213 / 0.213 / 0.213**; MDD −0.434 vs −0.606. The paper labels this exercise exploratory (one year, close-price execution, no spread, exchange-defined sessions rather than the UTC cutoffs).

### Independently reproduced

**Not independently reproduced.**

We read the pinned article text and every pinned replication CSV (byte sizes matched the GitHub tree) and cross-checked the paper's prose against those files, but we did **not** re-run `btc_eth_backtest.py`, `statistical_tests.py` or `etf_2025_analysis.py`, because the raw Kraken hourly files required as inputs are deliberately not distributed with the repository (README). No independent data, code execution, or out-of-sample replication was performed by this Scout.

### Negative evidence

1. **Hansen SPA never rejects** at any cost level after searching all 300 cutoff–strategy combinations: p = 0.899–0.996 (BTC) and 0.656–0.771 (ETH) (Table 12, §5.4).
2. **Every paired strategy-vs-buy-and-hold 95% CI contains zero** and no Holm-adjusted p-value is significant at 10% (Table 11 / `preferred_vs_buyhold_tests.csv`, all `significance_*` flags `False`).
3. **BTC fails the chronological holdout:** the 2016–2020 optimum (Momentum/Long @11:00) loses 29.1% pre-cost in 2021–2025 and delivers only 23.6% of buy-and-hold wealth (§6.2, Table 13).
4. **Boundary fragility:** BTC terminal wealth falls from 95,015 at `h=08` to 31,648 at `h=07` and 20,226 at `h=09` — a 3× drop from a one-hour shift; the authors call it "evidence of boundary sensitivity, not a stable economic optimum" (§5.1).
5. **At most cutoffs the winner is passive:** buy-and-hold is the best of the 25 rules at BTC `h=9,10` (and ETH `h=0,1,2,4,9,10,11`), i.e. the search often returns no active rule at all (`cutoff_strategy_best_by_cutoff.csv`).
6. **BTC's gross edge is almost entirely consumed by 2 bps:** wealth ratio falls 4.70 → 2.22 → **1.05**; §6.3 puts the one-way break-even near **2.1 bps**, below typical retail all-in cost once spread and boundary slippage are added.
7. **Subperiod sign instability for BTC:** ratio 0.375 → 0.180 in 2016–2020 (underperforms) versus 12.64 → 5.90 in 2021–2025 (Table 11); §6.1 calls it regime dependence, not proof of superiority.
8. **ETH's nighttime premium decays:** 40.93 bps/session (2016–2020, Holm p = 0.0012) collapses to 7.37 bps and becomes insignificant (2021–2025, Holm p = 0.259) (Table 10).
9. **BTC nighttime reversal is not significant in 2016–2020** (20.54 bps, Holm p = 0.120), so half of the "Reversal/Reversal" mechanism is unsupported in the first five years (Table 10).
10. **Selection was done at zero cost** (§4.3): cutoff and rule were chosen ignoring the very frictions that later erase the result.
11. **Cost model is a bare proportional grid:** spread, boundary slippage, market impact, exchange fees, short-borrow cost, perpetual funding and taxes are all explicitly excluded (§4.4) — they are `data gap`, never zero.
12. **Turnover is high:** BTC preferred rule churns 7,485 turnover units over 7,304 sessions (≈1.02/session; our arithmetic on the pinned CSV), so at 2 bps the additive charge over the sample is ≈149.7% of notional traded (`research interpretation`), consistent with the 95,015 → 21,258 collapse.
13. **Execution is assumed at the observed session-boundary price** with no fill model, latency, partial-fill or queue-priority treatment (§6.3).
14. **Benchmarks are not exposure matched:** the rules hold cash or short positions while buy-and-hold is always long, so terminal-wealth and Sharpe gaps are "comparisons of complete investment paths, not estimates of alpha at equal market exposure" (§6.3, source-reported).
15. **Risk-free rate is set to zero** in all Sharpe ratios (§4.5), and annualization uses √365 on daily returns.
16. **Single venue:** all spot evidence is Kraken hourly data; cross-exchange replication, volatility/autocorrelation controls and heteroskedasticity-robust tests are explicitly deferred to future work (§6.3).
17. **Mechanism is unidentified:** no volume, liquidity or order-flow controls; the cutoffs are "empirical labels rather than institutional opening times", with liquidity provision, order-flow imbalance, volatility clustering and investor-mix changes left as unseparated competitors (§6.3).
18. **Scale illusion:** ETH's 18,443,599 terminal wealth is 3,652 days of compounding from 100 with no liquidity, spread or capacity model; the authors themselves warn against reading it as scalable (§5.2).
19. **The rule family contains ruinous cells:** in the same pinned table, BTC Night Cash/Day Trend ends at 0.21 and ETH Night Trend/Day Trend at ≈0.000099 from 100 — so the search space mixes near-total-loss outcomes with the selected winners, which is exactly the setting in which maximum-wealth selection overstates expected performance (`btc_eth_all_metrics.csv`; `research interpretation`).
20. **Raw input data are withheld**, so the source's own "no missing hours" validation and every headline number cannot be re-derived without re-downloading Kraken data (repo README).
21. **Cross-file baseline inconsistency inside the replication package** (`research interpretation`, our comparison of two pinned files): buy-and-hold terminal wealth for BTC is 20,216.11 in `btc_eth_all_metrics.csv`/`preferred_vs_buyhold_tests.csv` but 20,276.89 in `cutoff_strategy_best_by_cutoff.csv` (+0.30%), and for ETH 319,710.72 vs 318,302.05 (−0.44%); `btc_eth_all_metrics.csv` itself varies the buy-and-hold baseline by cutoff (BTC 20,209.60–20,280.62), so the passive benchmark is not computed identically across scripts.
22. **ETF evidence is one calendar year (2025) with falling benchmarks:** IBIT buy-and-hold returned −6.4% and ETHA −11.2% in that window, so the transferred rules are compared against a declining passive leg; the authors label the exercise exploratory (§6.4).
23. **The authors' own conclusion is narrower than a strategy claim:** "The defensible conclusion is therefore narrower than a claim of a generally profitable nighttime strategy" (§7).
24. **No independent third-party replication identified** in the repository or in the reviewed sources; absence is not evidence that none exists.

## Falsification plan

Thresholds below are `research-defined falsification thresholds`; constructions are `research-proposed`. None is claimed by the source.

- **F1 — Frozen forward replication.** Run BTC Reversal/Reversal@08:00 and ETH Long/Reversal@05:00 unchanged on hourly data from 2026-01-01 onward (no re-selection, ≥ 12 months). **Fail** if either rule's wealth ratio vs its buy-and-hold benchmark is ≤ 1.00 net of 2 bps per unit of turnover, or if the paired mean differential's 95% block-bootstrap CI excludes zero in the *wrong* (negative) direction.
- **F2 — All-in cost ladder.** Re-run at 0 / 1 / 2 / 5 / 10 / 20 bps per turnover unit plus a quoted-spread and taker-fee model. **Fail** if either preferred rule's wealth ratio drops below 1.00 at 5 bps, or if the ETH ratio at 10 bps falls below 1.00.
- **F3 — Turnover and capacity audit.** Recompute one-way turnover per session and compare with 30-day median dollar volume on each venue. **Fail** if required participation exceeds 10% of median hourly dollar volume at a US$10m book (research-defined), or if the printed trade counts (3,743 BTC / 3,668 ETH) cannot be reproduced from the pinned code.
- **F4 — Decisive four-way ablation.** (a) circularly permute the lagged same-session sign 1,000 times; (b) fix the cutoff at 00:00 UTC instead of 08:00/05:00; (c) compare against an **exposure-matched** benchmark (buy-and-hold scaled to the strategy's average gross exposure) and against unconditional Long/Long at the same cutoff; (d) drop the unconditional ETH night-long component. **Fail the mechanism** if the daytime reversal contrast in fresh data is < 10 bps with a 95% CI containing zero, or if rule (c) erases the advantage at any cost level ≤ 2 bps.
- **F5 — Multi-venue replication.** Rebuild the same sessions on Binance, Coinbase and Kraken hourly closes. **Fail** if the sign of the daytime reversal contrast flips in ≥ 2 of the 3 venues or if only Kraken reproduces the ranking.
- **F6 — Cutoff stability.** Re-select `h` on the first half and evaluate on the second; also test `h±1`. **Fail** if the re-selected cutoff differs by more than 2 hours, or if the neighbouring cutoff's wealth ratio vs buy-and-hold is ≤ 1.00 at 0 bps.
- **F7 — Rolling holdout.** Repeat the 2016–2020 → 2021–2025 design with five rolling origins. **Fail** if the ETH rule fails to beat buy-and-hold in ≥ 3 of 5 origins, or if BTC's training-selected rule underperforms in ≥ 3 of 5.
- **F8 — Search-aware permutation null.** Build a null by circularly shifting session returns (preserving marginal volatility), re-run the *full* 300-combo search on each of 1,000 draws. **Fail** if the observed best terminal wealth is not above the 95th percentile of the null best-wealth distribution.
- **F9 — Multiplicity control across the grid.** Apply Benjamini–Hochberg at q < 0.10 to the paired differentials of all 300 cells × 2 assets × 3 cost levels. **Fail** if no cell survives.
- **F10 — Exposure-matched horse race with HAC inference.** Compare each preferred rule against scaled buy-and-hold and against a 50/50 cash–long mix using Newey–West t ≥ 1.96 on the daily log differential. **Fail** if neither comparison clears 1.96.
- **F11 — Regime/subperiod stability.** Compute the daytime reversal contrast per calendar year over ≥ 10 years. **Fail** if the contrast is negative in ≥ 50% of years, or if the ETH night premium stays insignificant in ≥ 3 consecutive recent years.
- **F12 — Reproduction gate.** Re-download Kraken hourly data and re-run the pinned scripts at `5693993e…`. **Fail** if any headline terminal wealth, Sharpe or contrast deviates by more than ±1% from the printed value.
- **F13 — ETF extension out-of-sample.** Extend IBIT/ETHA evaluation to ≥ 3 years including 2026 forward data with spread and fee modelling. **Fail** if the transferred rules' wealth ratio vs buy-and-hold is ≤ 1.00 at 2 bps.

## Crypto portability

**direct.**

The source evidence *is* crypto: BTC/USD and ETH/USD spot on Kraken, hourly UTC bars, 24/7 sessions, √365 annualization, and the mechanism (session-local reversal plus an overnight drift) is defined on the crypto clock rather than ported from equities. The exploratory extension also uses crypto-linked US ETFs.

Within that `direct` setting the following remain `data gap` for any tradable version:

- **Spot vs perpetual:** the rules short BTC/ETH outright; a perp port must add **funding**, mark/index price, leverage, maintenance margin and liquidation handling — none of which the source models.
- **Venue fragmentation:** single-venue Kraken signals and boundary prices; cross-exchange price dispersion and which venue's boundary is canonical are untested (§6.3).
- **Session boundary vs exchange mechanics:** the 05:00/08:00 UTC boundaries are empirical labels; funding settlement windows (commonly 00:00/08:00/16:00 UTC) and exchange maintenance windows may interact with them — unexamined in the source.
- **Liquidity and impact:** majors are liquid, but the ≈1.02 turnover units per session × two legs implies constant two-sided crossing at each boundary; spread and slippage at those instants are unmeasured.
- **Shorting venue:** spot shorting needs margin inventory or a derivatives leg; borrow/availability and its cost are not stated.
- **Timestamp/candle convention:** hourly close aggregation and boundary-close execution are assumed; alternate vendors' candle boundaries could change the sign of a 12 h session return in thin hours.

Crypto portability is not authorization to trade.

## Limitations

- **Not independently reproduced** — headline numbers rest on the authors' own code and outputs; raw data withheld.
- **`underspecified`:** shorting/borrow mechanics, fill price within the boundary bar, order type, latency, partial-fill handling, re-entry rules, ETF hourly data vendor (repo lists filenames only), and any capacity model.
- **`data gap`:** spread, slippage, impact, exchange fees, funding, borrow cost, taxes, and cross-exchange prices — all explicitly excluded by the source rather than measured as zero.
- **`data gap`:** paper Tables 9, 12, 13 and 14/15 cells are exposed in the HTML only as table images, so those figures here come from the article's prose plus the pinned replication CSVs; the cross-checks that could be made (Tables 8, 10, 11 prose vs CSV) matched exactly.
- **Selection bias acknowledged by the source:** cutoff and rule are full-sample maximizers of terminal wealth; SPA and holdout are the source's own partial controls and both undercut the headline (§4.3, §5.4, §6.2).
- **Interpretation risk:** our reading of "session-local overreaction plus overnight drift" is a research interpretation of the source's descriptive results, not a demonstrated causal channel; the source offers no volume/liquidity/order-flow identification.
- **Sample regime concentration:** 2016–2025 includes two full crypto cycles; subperiod rankings flip for BTC, and the ETH night premium decays.
- **No capacity or AUM claim** can be attached to any figure in this record.
- **Publication-status caveat:** peer-reviewed but published within three weeks of submission (received 19 Aug, accepted 4 Sep 2026) in a guest-edited special issue; independent scrutiny is young.

## Implementation status

`implementation_status: not-implemented`.

No part of this record has been implemented in our research stack: no Kraken data pull, no session engine, no backtest, no Qlib validation, no Paper/Testnet/Live run. Nothing in this record implies Research Intake Review, Wiki Brain ingestion, candidate-pool entry, or any frozen survivor.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this artifact in the staging repository means only that normalized, source-traceable research material was captured. It does **not** mean: passed intake review; entered Hermes Wiki Brain or the production candidate pool; completed Qlib full-backtest validation; became a survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. The source's own statistical tests fail to reject "no superiority", and that framing must survive any downstream summary.

## Related Wiki records

Pre-write `kb_search` for *"cryptocurrency intraday session momentum reversal time-of-day predictability"* returned **0 pages**; a broader *"cryptocurrency intraday seasonality"* search returned verified pages, of which the following are materially adjacent and are linked without any claim of shared source identity:

- [[quant/crypto-intraday-utc-return-seasonality-tea-time-2026-09-03]] — descriptive time-of-day seasonality across 38 exchanges, no trading rule.
- [[quant/crypto-quarter-hour-opening-order-imbalance-medium-horizon-2026-08-31]] — quarter-hour boundary order-imbalance predictability (different horizon and signal).
- [[quant/bitcoin-rolling-fpca-hourly-return-direction-2026-09-03]] — hourly directional forecasting with a functional-PCA model rather than sign-lagged session rules.
- [[quant/bitcoin-friday-3pm-est-post-event-drift-2026-09-03]] — a single named calendar boundary event, not a searched session partition.

## Sources

- Wu, Z., and Pinsky, E. (2026). "On the Performance of Lagged Momentum and Reversal Strategies Across Daytime and Overnight Sessions in Bitcoin and Ethereum Cryptocurrencies." *Journal of Risk and Financial Management*, 19(9), 692. https://doi.org/10.3390/jrfm19090692 — published online 2026-09-06, CC BY 4.0 (Crossref-verified 2026-09-27).
- Full-text article page: https://www.mdpi.com/1911-8074/19/9/692 — read end to end in a browser session on 2026-09-27 (Sections 1–7, Appendix A, Figures 1–5 captions, Data Availability and Conflict-of-Interest statements); a direct `curl` fetch was refused with MDPI "Access Denied".
- Crossref metadata: https://api.crossref.org/works/10.3390/jrfm19090692 — checked 2026-09-27 (journal-article, MDPI AG, 19(9) 692, published-online 2026-09-06, CC BY 4.0, no linked updates).
- Replication repository: https://github.com/wzf01195010-png/Crypto-day-night-effects at full commit `5693993e108f2b3668bd21b1dd36ae31f79d8fcd` (MIT) — `README.md`, `paper_outputs/README.md`, `LICENSE`, `btc_eth_backtest.py`, `cutoff_strategy_analysis.py`, `statistical_tests.py`, `etf_2025_analysis.py` listing, and the tree API response read 2026-09-27.
- Pinned replication tables read 2026-09-27 (raw URLs under the commit above): `paper_outputs/tables/preferred_vs_buyhold_tests.csv` (4,196 B), `conditional_predictability_tests.csv` (2,968 B), `cutoff_strategy_best_by_cutoff.csv` (2,260 B), `etf_2025_metrics.csv` (1,711 B), `btc_eth_all_metrics.csv` (486,841 B); byte sizes match the GitHub tree API.
- Kraken official historical market-data archive — named by the article (§3.1) and repo README as the BTC/ETH hourly source; not fetched by this Scout (`data gap`).
