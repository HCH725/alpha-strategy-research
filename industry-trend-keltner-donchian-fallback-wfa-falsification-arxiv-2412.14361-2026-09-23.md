---
schema: strategy-research-record-v1
title: Dual-channel Keltner-Donchian industry trend-following — fallback allocations, momentum overlay, and walk-forward alpha decay across 48 US industry portfolios (arXiv 2412.14361 / SSRN 4857230)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-12-20
sources:
  - "https://arxiv.org/abs/2412.14361 — arXiv:2412.14361v2 [q-fin.PM], 'Refining and Robust Backtesting of A Century of Profitable Industry Trends', Alessandro Massaad; Rene Moawad; Oumaima Nijad Fares; Sahaphon Vairungroj (mentored by Prof. Naftali Cohen, Columbia University), submitted 2024-12-18, revised 2024-12-20 (fully read 2026-09-23)"
  - "https://arxiv.org/pdf/2412.14361 — pinned canonical PDF v2, 14 pages, 1,887,922 bytes, SHA-256 f5c5dd6b49c6f585d7fe589ad716ed36339bd4f2d1bd87187c1ffa4e93b6bf5c (fully read 2026-09-23)"
  - "https://doi.org/10.48550/arXiv.2412.14361 — arXiv/DataCite DOI"
  - "https://github.com/alemassaad/ddmif — open-source replication codebase, commit 6ef220aaa4b223658cc10f63522d74524f2f2a7e (2024-12-17), files asset_allocation.py, wfa_driver.py, visuals.py"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4857230 — Carlo Zarattini and Gary Antonacci, 'A Century of Profitable Industry Trends', SSRN 4857230, 2024 (baseline strategy reviewed and audited by primary source)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dual-channel Keltner-Donchian industry trend-following — fallback allocations, momentum overlay, and walk-forward alpha decay across 48 US industry portfolios (arXiv 2412.14361 / SSRN 4857230)

## Provenance

- **Primary source (pinned):** Alessandro Massaad, Rene Moawad, Oumaima Nijad Fares, and Sahaphon Vairungroj (mentored by Prof. Naftali Cohen, Columbia University), *"Refining and Robust Backtesting of A Century of Profitable Industry Trends"*, arXiv:2412.14361v2 `[q-fin.PM]`, submitted **2024-12-18 21:57:08 UTC**, revised **2024-12-20 18:44:20 UTC** (v2 pinned). License: arXiv non-exclusive distribution. DOI: `10.48550/arXiv.2412.14361`.
- **Primary-source checksum (performed 2026-09-23):**
  - Abstract page `https://arxiv.org/abs/2412.14361`: 40,564 bytes, SHA-256 `acc5c65f565051302676816cbb9ac7fc4a37d06c85bec0312f13bcbbc6cd8628`.
  - Canonical PDF `https://arxiv.org/pdf/2412.14361`: 1,887,922 bytes, SHA-256 `f5c5dd6b49c6f585d7fe589ad716ed36339bd4f2d1bd87187c1ffa4e93b6bf5c`, 14 pages (text extracted and read in full 2026-09-23).
- **Public implementation / code path:** GitHub repository `https://github.com/alemassaad/ddmif`, immutable commit SHA `6ef220aaa4b223658cc10f63522d74524f2f2a7e` (committed 2024-12-17 04:00:43 UTC). Verified code files: `asset_allocation.py`, `wfa_driver.py`, `visuals.py`.
- **Audited baseline source:** Carlo Zarattini and Gary Antonacci, *"A Century of Profitable Industry Trends"*, SSRN abstract `4857230`, 2024. All claims regarding the baseline 1926–2024 century-long performance (18.2% annual return, 1.39 Sharpe) originate from Zarattini & Antonacci and are audited by Massaad et al.
- **Repository deduplication audit (performed 2026-09-23):** Whole-repository ripgrep across all tracked `*.md` files and `coverage_manifest.csv` for `2412.14361`, `ddmif`, `alemassaad`, `Naftali Cohen`, `Massaad`, `4857230`, and `A Century of Profitable Industry Trends`: **0 hits**.
- **Related repository records (different sources and mechanisms):**
  - `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` — shares first author Zarattini, but studies intraday SPY ETF momentum via time-varying noise bands and VWAP trailing stops; distinct universe (single intraday equity ETF vs. 48 daily industry portfolios) and distinct mechanism.
  - `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` — shares author Zarattini, but studies crypto top-20 rotational Donchian trend following; distinct asset class and operational universe.
  - `etf-momentum-operational-rules-super-category-diversification-trailing-stop-2026-09-23.md` — mentions Gary Antonacci's *Dual Momentum* in literature review, but examines a 4-ETF rotation framework; distinct source and strategy logic.
  - `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md` — shares author Zarattini, but examines LLM news sentiment overlays on 12-1 cross-sectional equity momentum; distinct mechanism.
- **Wiki Brain deduplication audit (2026-09-23):** Grep across `/Users/hong/.hermes/wiki` for `2412.14361`, `ddmif`, `alemassaad`, `Massaad`, and `4857230` yielded **0 hits**. No matching record exists.

## Economic mechanism

### Source-reported

1. **Baseline thesis (Zarattini & Antonacci 2024, §1):** Industry-level momentum aggregates firm-level news into sector-wide macroeconomic trends, smoothing company-specific idiosyncratic risk while capturing medium-to-long-term capital rotations across the real economy. A long-only dual-channel system (combining Keltner Channels to capture volatility-scaled expansion and Donchian Channels to capture multi-week extreme breakouts) across 48 U.S. industry portfolios from 1926 to 2024 reportedly produced an 18.2% annualized return with a 1.39 Sharpe ratio (compared to the U.S. equity market benchmark of 9.7% return and 0.63 Sharpe ratio).
2. **Practical critique and audit (Massaad et al. 2024, §1, §3.2, §6.1–§6.7):**
   - **Severe cash drag and T-bill dependence (§3.2, §5):** In the original century-long backtest, capital was parked in 1-month Treasury bills 47% of the time (4,276 days between 2000 and 2024), including 50 full days where zero industry positions satisfied entry criteria. In institutional practice, maintaining large unallocated cash reserves creates tracking error and forfeits equity risk premia.
   - **Overfitting across a century-long sample (§1, §6.3):** Calibrating channel parameters globally across 1926–2024 introduces severe retrospective survivorship and lookback optimization bias. The reported Sharpe ratio relies heavily on dodging major historical crashes (1929–1932, 1973–1974, 2000–2002, 2008) via cash allocations rather than consistent alpha generation.
   - **Modern market structural shifts (§6.7):** Post-2000 financial markets exhibit substantially higher cross-sector correlations and heightened algorithmic efficiency. As sector correlations rise, cross-industry diversification breaks down and simple dual-channel breakouts suffer increased whipsaw losses.
   - **Intervention mechanisms tested (§4.1–§4.7):** Massaad et al. evaluate four modifications: (a) alternative cash fallbacks (moving average momentum ratio, risk parity, equal weight, S&P 500 equity deployment) to keep capital 100% invested; (b) a rolling momentum overlay (top 10 industries by rolling return window); (c) in-sample industry exclusion; and (d) rolling Walk-Forward Analysis (WFA) with 5-year training and 1-year out-of-sample testing.

### Research interpretation

- **Falsifiable hypothesis:** *A systematic long-only trend-following strategy across 48 U.S. industry portfolios using dual Keltner-Donchian breakout channels, volatility-targeted position sizing, and trailing exit stops fails to generate statistically significant positive risk-adjusted excess returns over a broad equity benchmark once subjected to rolling out-of-sample walk-forward optimization, full capital deployment (eliminating artificial T-bill market-timing cash drag), and modern (post-2000) market conditions.*
- **Classification of record:** Empirical replication, robustness audit, and falsification of a published century-long momentum anomaly.
- **Component roles in hybrid structure:**
  - *Regime / cash allocation:* Binary switch between active industry trend positions and fallback allocation (1-month T-bills in baseline; MA ratio, risk parity, equal-weight, or S&P 500 in modifications).
  - *Primary breakout signal:* Dual upper band `min(DonchianUp, KeltnerUp)` requiring price to exceed both channels simultaneously.
  - *Secondary cross-sectional filter (modified variant):* Top 10 ranking by rolling return (`MW` ∈ {20, 60, 360} days).
  - *Risk / exit logic:* Ratcheting trailing lower stop `max(TrailingStop_{t-1}, LowerBand_t)` where `LowerBand = max(DonchianDown, KeltnerDown)`.
  - *Position sizing:* Equal risk contribution scaling via inverse rolling volatility `TargetVol / vol_j`, constrained by a 20% single-industry cap and a 200% gross portfolio leverage ceiling.

## Signal

The trading logic is fully specified in Massaad et al. (§3.1, §4.1–§4.7) and open-sourced in `alemassaad/ddmif` (`asset_allocation.py` and `wfa_driver.py`):

- **Signal formation timestamp / tradability:** Formed at daily market close using daily total returns. All signals and weights are explicitly lagged by one day (`.shift(1)`) to ensure point-in-time tradability without look-ahead bias (§2.3).
- **Price series construction:** For each industry $j \in \{1, \dots, 48\}$, a cumulative total return price index is generated:
  $$P_{j,t} = \prod_{\tau=1}^t (1 + R_{j,\tau})$$
- **Lookback windows and parameters (source-reported defaults from `asset_allocation.py`):**
  - `UP_DAY`: lookback window for upward breakout and volatility calculation (default = 20 days; grid searched over {20, 30, 40}).
  - `DOWN_DAY`: lookback window for downward exit channels (default = 40 days; grid searched over {20, 30, 40}).
  - `KELT_MULT`: Keltner channel band multiplier (default = 2.8; grid searched over {2.4, 2.8, 3.2}). Derived from formula $1.4 \times k$ where $k = 2.0$.
  - `ADR_VOL_ADJ`: Average daily range adjustment factor (default = 1.4; grid searched over {1.2, 1.4, 1.6}).
  - `TargetVol`: Annualized/daily volatility target for inverse-volatility sizing (default = 0.015 daily, i.e., ~23.8% annual; grid tested 0.015 and 0.02).
  - `max_not_trade`: Maximum single-industry portfolio weight cap (default = 0.20, i.e., 20%; grid tested 0.20 and 0.25).
  - `max_leverage`: Maximum portfolio gross leverage constraint (fixed at 2.0, i.e., 200%).
- **Dual upper channel (entry boundary):**
  $$\text{UpperBand}_{j,t} = \min\left(\text{DonchianUp}_{j,t}, \text{KeltnerUp}_{j,t}\right)$$
  where:
  $$\text{DonchianUp}_{j,t} = \max\left(P_{j,t}, P_{j,t-1}, \dots, P_{j,t-\text{UP\_DAY}+1}\right)$$
  $$\text{KeltnerUp}_{j,t} = \text{EMA}(P_j, \text{UP\_DAY})_t + \text{KELT\_MULT} \times \frac{1}{\text{UP\_DAY}} \sum_{i=0}^{\text{UP\_DAY}-1} |\Delta P_{j,t-i}|$$
- **Dual lower channel (exit boundary):**
  $$\text{LowerBand}_{j,t} = \max\left(\text{DonchianDown}_{j,t}, \text{KeltnerDown}_{j,t}\right)$$
  where:
  $$\text{DonchianDown}_{j,t} = \min\left(P_{j,t}, P_{j,t-1}, \dots, P_{j,t-\text{DOWN\_DAY}+1}\right)$$
  $$\text{KeltnerDown}_{j,t} = \text{EMA}(P_j, \text{DOWN\_DAY})_t - \text{KELT\_MULT} \times \frac{1}{\text{DOWN\_DAY}} \sum_{i=0}^{\text{DOWN\_DAY}-1} |\Delta P_{j,t-i}|$$
- **Entry condition:**
  - Long signal trigger: $\text{LongSignal}_{j,t} = 1$ if $P_{j,t} \ge \text{UpperBand}_{j,t-1}$ and $\text{UpperBand}_{j,t-1} > \text{LowerBand}_{j,t-1}$.
  - Entry execution: If $\text{Exposure}_{j,t-1} \le 0$ and $\text{LongSignal}_{j,t} == 1$, enter long: $\text{Exposure}_{j,t} = 1$, and initialize trailing stop $\text{TrailingStop}_{j,t} = \text{LowerBand}_{j,t}$.
- **Exit condition and ratcheting trailing stop:**
  - If $\text{Exposure}_{j,t-1} == 1$:
    - Check threshold: $\text{Threshold}_{j,t} = \max\left(\text{TrailingStop}_{j,t-1}, \text{LowerBand}_{j,t}\right)$.
    - Confirm / hold: If $P_{j,t} > \text{Threshold}_{j,t}$, maintain long ($\text{Exposure}_{j,t} = 1$) and ratchet trailing stop upward: $\text{TrailingStop}_{j,t} = \text{Threshold}_{j,t}$.
    - Exit trigger: If $P_{j,t} \le \text{Threshold}_{j,t}$, close long ($\text{Exposure}_{j,t} = 0$, $\text{Weight}_{j,t} = 0$).
- **Position sizing and portfolio leverage:**
  - Raw volatility: $\sigma_{j,t} = \text{rolling\_std}(R_j, \text{UP\_DAY})$.
  - Leverage per asset: $\omega_{j,t} = \frac{\text{TargetVol}}{\sigma_{j,t}}$ for active long positions ($\text{Exposure}_{j,t} == 1$).
  - Allocation across available portfolios: $\omega_{j,t}^{\text{port}} = \frac{\omega_{j,t}}{N_{\text{available},t}}$.
  - Individual asset cap: $\omega_{j,t}^{\text{capped}} = \min(\omega_{j,t}^{\text{port}}, \text{max\_not\_trade})$.
  - Portfolio gross leverage constraint: If $\sum_j \omega_{j,t}^{\text{capped}} > \text{max\_leverage}$, rescale proportionally:
    $$\omega_{j,t}^* = \omega_{j,t}^{\text{capped}} \times \frac{\text{max\_leverage}}{\sum_k \omega_{k,t}^{\text{capped}}}$$
  - Execution lag: Trading returns are computed against shifted weights $\omega_{j,t}^*.shift(1)$.
- **Cash management and fallback allocations (§4.1–§4.5):**
  - *Baseline:* Uninvested cash weight $1 - \sum_j \omega_{j,t}^*.shift(1)$ earns 1-month T-bill daily return.
  - *Method 1 (Moving Average fallback):* On zero-signal days, rank industries by short-to-long return moving average ratio ($\text{MA}_{\text{short}} / \text{MA}_{\text{long}}$, windows 20 to 100 days); second tier falls back to equal weight.
  - *Method 2 (Risk-parity fallback):* On zero-signal days, allocate capital inversely proportional to rolling volatility across all 48 industries.
  - *Method 3 (Equal-weight fallback):* On zero-signal days, allocate capital equally ($1/48$) across all industries.
  - *Method 4 (S&P 500 fallback):* Uninvested capital dynamically allocated to the cap-weighted S&P 500 index (CRSP `dsp500list` / `dsf`).
- **Momentum ranking modification (§4.2):**
  - Add rolling return window $\text{MW} \in \{20, 60, 360\}$ days. Select top 10 industries by average return over $\text{MW}$, and weight active entries by inverse volatility. Reduces zero-signal days from 50 to 2 since 2000.
- **Operational rule classification:** Every rule and parameter above is **source-reported** from the primary paper and its GitHub repository (`alemassaad/ddmif`). Operationalization proposed by Scout: `research-proposed: none`.

## Required data

- **Universe / instruments (source-reported, §2.1):** 48 Industry Portfolios from Kenneth French's Data Library (`48_Industry_Portfolios_daily_CSV.zip`). Daily total returns, value-weighted, constructed from NYSE, AMEX, and NASDAQ stocks. Point-in-time compliance: stocks assigned to industry portfolios at the start of each year $t$ based on 4-digit SIC codes from year $t-1$. Stocks removed on their CRSP delisting date.
- **Factor / risk-free benchmarks (source-reported, §2.1):** Fama-French Research Factors (`F-F_Research_Data_Factors_daily_CSV.zip`), providing daily market return `mkt_ret` and 1-month Treasury bill rate `tbill_ret`.
- **Equity fallback dataset (source-reported, §4.5):** CRSP daily stock file (`dsf`) and historical S&P 500 constituent list (`dsp500list`) to eliminate survivorship bias in S&P 500 allocation.
- **Timeframe:** Daily closing returns.
- **Evaluation periods (source-reported, §2.2):**
  - In-sample (IS): 2000-01-01 to 2015-12-31 (16 years).
  - In-sample Validation (ISV): 2016-01-01 to 2020-12-31 (5 years).
  - Validation (V): 2021-01-01 to 2022-12-31 (2 years).
  - Out-of-sample / live test (`pt1 data`): 2023-01-01 to 2024-12-31 (2 years).
- **Missing-data handling (source-reported, §2.4):** Returns $\le -99\%$ converted to NaN. Missing values in returns backfilled with zero in cumulative product calculations (`fillna(0)`). Missing market/tbill factors excluded before regression.

## Execution assumptions

- **Signal-to-order timing:** Next-day execution. Signals and portfolio weights are shifted by one period (`.shift(1)`), executing at the closing return of day $t$ based on signals generated through day $t-1$.
- **Order type / fill model:** Daily close-to-close returns on synthetic value-weighted industry portfolios. Intraday execution, order types, and latency models are omitted in the source.
- **Fees / commissions:** **OMITTED / ZERO (data gap).** Neither the original Zarattini & Antonacci paper nor the Massaad et al. replication incorporates transaction costs, rebalancing fees, or exchange commissions. This is a material limitation given the daily rebalancing nature of inverse-volatility weights.
- **Spread / slippage:** **OMITTED / ZERO (data gap).** No bid-ask spread or market impact model is applied to industry portfolio reallocations.
- **Borrow / financing:** Long-only portfolio; no borrow fees incurred. Cash balances earn the 1-month T-bill rate when `invest_cash == "YES"`. Margin leverage financing costs beyond the risk-free rate are not modeled.
- **Leverage constraint:** Hard ceiling of 200% gross exposure (`max_leverage = 2.0`), scaled down proportionally if breached. Individual industry weight capped at 20% (`max_not_trade = 0.20`).

## Evidence

### Source-reported

All figures below are `source-reported` from Massaad et al. (arXiv:2412.14361v2) and Zarattini & Antonacci (SSRN 4857230). Not independently reproduced.

1. **Baseline historical performance (Zarattini & Antonacci 2024, cited in §1):**
   - Sample: 1926 to 2024 (98 years across 48 U.S. industries).
   - Reported annualized return: **18.2%** (vs. U.S. equity market benchmark **9.7%**).
   - Reported Sharpe ratio: **1.39** (vs. U.S. equity market benchmark **0.63**).
   - Caveat identified by Massaad et al. (§3.2): 4,276 days (47% of trading days since 2000) spent entirely in cash/T-bills, with 50 days producing zero valid positions.

2. **Method 1: Moving Average Fallback (§5, Table 1):**
   - `UP_DAY = 5, DOWN_DAY = 15`:
     - `ma_window = 20`: IS Alpha **2.05%** (Beta 0.84), ISV Alpha **-3.23%** (Beta 0.89), Worst Day -28.92%, Best Day 41.18%.
     - `ma_window = 100`: IS Alpha **1.57%** (Beta 0.83), ISV Alpha **1.72%** (Beta 0.71), V Alpha **2.73%** (Beta 0.80), OOS (`pt1 data`) Alpha **-6.91%** (Beta 0.87), Worst Day -2.17%, Best Day 2.35%.
   - `UP_DAY = 20, DOWN_DAY = 40`:
     - `ma_window = 20`: IS Alpha **-0.33%** (Beta 0.79), Worst Day -28.92%, Best Day 10.59%.
     - `ma_window = 100`: IS Alpha **2.92%** (Beta 0.76), ISV Alpha **12.35%** (Beta 0.55), V Alpha **4.54%** (Beta 0.76), OOS (`pt1 data`) Alpha **-9.90%** (Beta 0.87), Worst Day -2.46%, Best Day 2.36%.

3. **Method 2: Risk-Parity Fallback (§5, Table 3):**
   - `UP_DAY = 20, DOWN_DAY = 40`: IS Alpha **1.84%** (Beta 0.80), ISV Alpha **2.65%** (Beta 0.84), V Alpha **2.77%** (Beta 0.76), OOS (`pt1 data`) Alpha **-9.90%** (Beta 0.87), Worst Day -2.46%, Best Day 2.36%.
   - `UP_DAY = 5, DOWN_DAY = 15`: IS Alpha **1.34%** (Beta 0.83), ISV Alpha **-5.93%** (Beta 0.89), Worst Day -16.79%, Best Day 7.25%.

4. **Method 3: Equal-Weight Fallback (§5, Table 4):**
   - `UP_DAY = 20, DOWN_DAY = 40`: IS Alpha **1.66%** (Beta 0.80), ISV Alpha **2.36%** (Beta 0.84), V Alpha **3.58%** (Beta 0.76), OOS (`pt1 data`) Alpha **-10.19%** (Beta 0.88), Worst Day -2.79%, Best Day 2.36%.
   - `UP_DAY = 5, DOWN_DAY = 15`: IS Alpha **1.62%** (Beta 0.84), ISV Alpha **-5.85%** (Beta 0.89), Worst Day -16.79%, Best Day 7.25%.

5. **Modified Strategy with Added Momentum Signal (§5, Table 5):**
   - Incorporating rolling momentum window $\text{MW}$ selecting top 10 industries:
     - $\text{MW} = 20\text{ days}$: IS Alpha **2.88%** (Beta 0.80), ISV Alpha **-0.91%** (Beta 0.84), Worst Day -8.13%, Best Day 7.68%.
     - $\text{MW} = 60\text{ days}$: IS Alpha **3.04%** (Beta 0.81), ISV Alpha **0.53%** (Beta 0.87), V Alpha **7.82%** (Beta 0.78), OOS (`pt1 data`) Alpha **-8.19%** (Beta 0.91), Worst Day -2.18%, Best Day 2.57%.
     - $\text{MW} = 360\text{ days}$: IS Alpha **3.70%** (Beta 0.84), ISV Alpha **1.54%** (Beta 0.90), V Alpha **6.00%** (Beta 0.79), OOS (`pt1 data`) Alpha **-6.39%** (Beta 0.93), Worst Day -2.18%, Best Day 2.54%.

6. **Walk-Forward Analysis (WFA) results (§4.7, §6.7, Figure 6):**
   - Rolling 5-year optimization window shifted by 1 year across hyperparameter grid (`UP_DAY` [20, 30, 40], `DOWN_DAY` [20, 30, 40], `ADR_VOL_ADJ` [1.2, 1.4, 1.6], `KELT_MULT` [2.4, 2.8, 3.2], `TargetVol` [0.015, 0.02], `max_not_trade` [0.20, 0.25], `invest_cash` ["NO", "YES"]).
   - Empirical outcome (§6.7, Figure 6): Under dynamic out-of-sample WFA re-optimization, the original Zarattini & Antonacci strategy cumulatively **underperformed** the U.S. market benchmark over the 2000–2024 period.

### Independently reproduced

not independently reproduced

### Negative evidence

**Source-reported negative evidence (Massaad et al. 2024):**

- **Severe out-of-sample alpha collapse:** Across all tested configurations and fallback implementations, the strategy generates large **negative annual alphas** in the out-of-sample test period (`pt1 data`, 2023–2024):
  - MA fallback 100-day: Alpha drops from +2.92% (IS) to **-9.90%** (OOS).
  - Risk-parity fallback: Alpha drops from +1.84% (IS) to **-9.90%** (OOS).
  - Equal-weight fallback: Alpha drops from +1.66% (IS) to **-10.19%** (OOS).
  - Momentum overlay (60-day MW): Alpha drops from +3.04% (IS) to **-8.19%** (OOS).
  - Momentum overlay (360-day MW): Alpha drops from +3.70% (IS) to **-6.39%** (OOS).
- **Benchmark underperformance under Walk-Forward Analysis (§6.7, Figure 6):** When tested without look-ahead bias under realistic rolling walk-forward conditions, the strategy fails to beat buy-and-hold U.S. equities over 2000–2024.
- **Failure of industry exclusion (§6.6, Figures 4–5):** Filtering out historically underperforming sectors based on in-sample composite scores (Sharpe, IRR, hit ratio, max drawdown, alpha) failed to improve out-of-sample performance, leading to notable underperformance as historical losers rotated into market leaders.
- **Failure of alternative cash management (§6.1):** Forcing unallocated capital into equity or risk-parity fallbacks preserved capital deployment but severely degraded downside protection during market stress, eliminating the primary source of the strategy's historical risk-adjusted return.

**Scout-identified negative evidence (labeled `research-defined`):**

- **Zero transaction cost assumption:** The strategy rebalances 48 industry portfolios daily using rolling 14-day/20-day volatilities and frequent channel breakout entries/exits. In actual trading, bid-ask spread crossing, broker commissions, and market impact across 48 sectors would inflict continuous drag, further worsening the negative out-of-sample alphas.
- **Macro regime dependency:** The century-long 18.2% return was heavily driven by deflationary crash periods where cash/T-bills beat equities (e.g. 1929–1933, 1973–1974, 2000–2002, 2008). In modern sustained bull markets driven by high cross-sector correlation, trend breakouts suffer repeated false breaks and whipsaw losses.

## Falsification plan

The failure thresholds and operational tests below are **`research-defined`** (Scout-generated):

1. **Walk-forward out-of-sample alpha test (primary):**
   - *Data & Universe:* Kenneth French 48 Industry Portfolios, updated post-2024 data (2025–2026).
   - *Method:* Run rolling 5-year train / 1-year test walk-forward analysis with the pre-specified hyperparameter grid.
   - *Metric:* Annualized Jensen's alpha $\alpha$ against the Fama-French market return.
   - *Threshold (research-defined):* Cumulative out-of-sample annualized alpha $\alpha \le 0\%$ or Sharpe ratio $\le$ buy-and-hold market Sharpe $\rightarrow$ **hypothesis of persistent industry trend alpha falsified**.
   - *Action:* Conclude the century-long anomaly is unreplicable in modern markets; maintain status as `research-only / rejected for live deployment`.
2. **Transaction cost stress test:**
   - *Data:* 2000–2024 daily returns under baseline parameters (`UP_DAY=20`, `DOWN_DAY=40`, `TargetVol=0.015`).
   - *Method:* Apply round-trip transaction costs of 5 bps, 10 bps, and 20 bps on daily portfolio turnover.
   - *Metric:* Net annualized Sharpe ratio and net CAGR.
   - *Threshold (research-defined):* If net Sharpe ratio drops by $>40\%$ at 5 bps or becomes negative at 10 bps $\rightarrow$ **implementation viability falsified** due to turnover friction.
3. **Tradable ETF proxy audit:**
   - *Data:* Replace theoretical French 48 industry portfolios with liquid U.S. sector ETFs (e.g., SPDR sectors: XLK, XLE, XLF, XLV, XLI, XLY, XLP, XLU, XLB, XLC, XLRE).
   - *Method:* Execute identical dual-channel logic with 1-day execution lag.
   - *Metric:* Tracking error and net Sharpe ratio relative to theoretical industry results.
   - *Threshold (research-defined):* If sector ETF portfolio Sharpe ratio is $<0.50$ over 2010–2024 $\rightarrow$ **tradable proxy hypothesis falsified**.
4. **Shuffled-timing placebo test:**
   - *Method:* Randomly permute industry entry/exit signal dates while preserving each industry's holding period distribution across 1,000 Monte Carlo runs.
   - *Metric:* Percentile of actual strategy Sharpe ratio within the randomized distribution.
   - *Threshold (research-defined):* Actual Sharpe ratio $<95\text{th}$ percentile of the placebo distribution $\rightarrow$ **timing skill falsified** (returns indistinguishable from random equity exposure).

## Crypto portability

**`unproven`** — The primary source evaluates exclusively U.S. equity industry portfolios and Fama-French factors. It contains **zero** cryptocurrency empirical evidence or validation.

If ported to crypto markets in future research, the following structural impediments apply:

- **Lack of standardized industry taxonomy:** Traditional 4-digit SIC codes do not exist in crypto. Sector groupings (e.g. DeFi, Layer 1, AI, Meme, Gaming) are non-standard, rapidly shifting, and plagued by severe token survivorship and delisting bias.
- **Dominant Bitcoin beta and high cross-asset correlation:** During market downturns, crypto cross-asset correlations approach 1.0. The cross-industry dispersion required for sector rotation strategies is frequently compressed, eliminating the diversification benefit observed in equities.
- **Cash fallback mechanics:** In crypto, there is no sovereign risk-free T-bill. "Cash" fallbacks entail either stablecoins (carrying smart contract and depeg counterparty risks) or centralized exchange deposit yields.
- **Turnover and fee friction:** Trading hundreds of altcoins daily across fragmented centralized and decentralized liquidity venues incurs prohibitive bid-ask spreads (often 10–50 bps) and taker fees, which would severely impair an inverse-volatility rebalancing schedule.
- Any crypto adaptation must be treated as a newly formulated, independent hypothesis requiring its own primary data and validation.

## Limitations

- **underspecified:**
  - Zero transaction cost or slippage modeling in both the original paper and the replication audit.
  - Fill model and intraday order mechanics omitted (assumes execution exactly at daily close).
  - Exact turnover series across the 48 industries is not tabulated in the paper.
- **not independently reproduced:** The Scout executed no local backtests or independent data pipelines; all quantitative claims are `source-reported` from Massaad et al. (2024) and Zarattini & Antonacci (2024).
- **data gap:**
  - Post-2024 performance is unrecorded.
  - S&P 500 fallback results are presented graphically (Figures 3–5) without full numerical summary tables.
- **unproven:** Crypto portability is completely unproven; sector rotation logic across crypto assets remains speculative.
- **Severe alpha decay:** Primary empirical conclusion of the source is that the strategy suffers extreme out-of-sample decay ($\alpha \le -6.39\%$ to $-10.19\%$) and underperforms market benchmarks under walk-forward conditions.

## Implementation status

`implementation_status: not-implemented`. No implementation of this strategy has been performed in our research stack. No code has been deployed to Qlib, PyBroker, NautilusTrader, or any paper/live engine. The Scout performed source retrieval, PDF verification, checksumming, and repository deduplication only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

A record being present in this repository does **not** mean:
- Passed Research Intake Review;
- Entered Hermes Wiki Brain;
- Entered the production candidate pool;
- Completed Qlib full backtest validation;
- Validated alpha or profitable trading strategy;
- Approved for paper trading, testnet, or live deployment.

Given the primary source's negative out-of-sample findings ($\alpha < 0$ in out-of-sample testing and walk-forward underperformance), this artifact serves as an empirical falsification benchmark against naive sector-momentum claims.

## Related Wiki records

No related Wiki Brain pages were identified in `/Users/hong/.hermes/wiki` (`2412.14361`, `ddmif`, `Massaad`, and `4857230` yielded 0 hits). No Wiki link is fabricated. Canonical schema contract: `[[quant/strategy-research-record-spec-v1]]`.

Neighbouring repository records (same repository, different sources, distinct mechanisms):
- `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` — Intraday SPY momentum with time-varying noise bands and VWAP trailing stops.
- `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` — Crypto top-20 Donchian trend following.
- `etf-momentum-operational-rules-super-category-diversification-trailing-stop-2026-09-23.md` — Multi-asset ETF momentum rotation rules.
- `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md` — LLM news sentiment tilt over cross-sectional equity momentum.

## Sources

1. Alessandro Massaad, Rene Moawad, Oumaima Nijad Fares, and Sahaphon Vairungroj (mentored by Prof. Naftali Cohen). *"Refining and Robust Backtesting of A Century of Profitable Industry Trends."* Columbia University, Department of Industrial Engineering and Operations Research (IEOR), December 2024; posted as arXiv preprint `arXiv:2412.14361v2 [q-fin.PM]`, submitted 18 December 2024, revised 20 December 2024. Abstract: https://arxiv.org/abs/2412.14361 ; PDF: https://arxiv.org/pdf/2412.14361 (14 pages, SHA-256 `f5c5dd6b49c6f585d7fe589ad716ed36339bd4f2d1bd87187c1ffa4e93b6bf5c`). *(Primary source for empirical audit, Tables 1, 3, 4, 5, and Figures 1–6.)*
2. Alessandro Massaad. Open-source Python implementation: `https://github.com/alemassaad/ddmif`, commit `6ef220aaa4b223658cc10f63522d74524f2f2a7e` (2024-12-17). Files: `asset_allocation.py`, `wfa_driver.py`, `visuals.py`. *(Primary implementation source for exact signal formulas, parameter grids, and default constants.)*
3. Carlo Zarattini and Gary Antonacci. *"A Century of Profitable Industry Trends."* 2024. Available at SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4857230 ; DOI: https://doi.org/10.2139/ssrn.4857230. *(Baseline audited strategy source reporting 18.2% annualized return and 1.39 Sharpe ratio over 1926–2024.)*
4. Kenneth R. French. Data Library: *48 Industry Portfolios - Daily* (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/48_Industry_Portfolios_daily_CSV.zip) and *Fama-French Research Data Factors - Daily* (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip). *(Underlying dataset vendor sources.)*
